"""Version B of the LLM answerability variant (v2, Nov 23): Gemini embeddings as features for v1's model.

policy-v1's answerability model (``answerability.py``) is two logistic regressions over word pieces of a
variable's name. Here each variable's text (name, type and the CA's plain-language meaning, the same
text version A shows the LLM) is embedded once with a Gemini embedding model, and the embedding is a
feature of the same two regressions, either alone (``mode="emb"``) or next to v1's word features
(``mode="name_emb"``).

Same training data and protocol as v1: dev answer-key labels only, 5 folds by patient, so each dev
patient is scored by a model that never saw that patient. No patient note is ever embedded or read.

Flow:
1. ``scripts/precompute_embeddings.py`` embeds the unique (name, type, meaning) items of chosen
   patients through ``llm.LLMClient.embed`` (cost log, disk cache, budget guard) and writes a store
   ``runs/llm_answerability/emb__<model>__d<dims>.npz`` (gitignored).
2. ``EmbAnswerabilityModel`` fits on dev labels with the stored vectors; ``emb_model_for`` picks the
   fold model exactly as ``answerability.model_for`` does. A variable missing from the store gets a
   zero vector (counted in ``missing``): with ``name_emb`` it then rests on its word features.
"""

from __future__ import annotations

import os
from collections.abc import Iterable
from functools import cache
from pathlib import Path

import numpy as np
from scipy import sparse
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression

from smt_trial_matching.answerability import (
    C_DEFAULT,
    SEED,
    AnswerabilityModel,
    Example,
    _patient_trials,
    _value_distributions,
    dev_fold,
    features,
    load_examples,
    load_split,
)
from smt_trial_matching.llm_answerability import STORE_DIR, Item

DIMS = 768
MODES = ("emb", "name_emb")
#: (C, scale) per mode, chosen on dev by held-out P(answered) AUC on the gpt5_oracle key
#: (scripts/grid_emb_auc.py, Nov 23). v1's name model: C 0.3, AUC 0.748.
CHOSEN = {"name_emb": (0.1, 3.0),  # AUC 0.767
          "emb": (1.0, 1.0)}  # AUC 0.753


def item_text(it: Item) -> str:
    """The text embedded for one variable: readable name, type and meaning (never patient data)."""
    stem, _, qual = it.name.partition("@@")
    name = stem.replace("_", " ")
    if qual:
        name += " (" + qual.replace("@@", "; ").replace("_", " ") + ")"
    kind = "yes/no" if it.vtype == "Bool" else f"number ({it.vtype})"
    meaning = f" | meaning: {it.meaning}" if it.meaning else ""
    return f"{name} | type: {kind}{meaning}"


# ----------------------------------------------------------------------------- store


def store_path(model: str, dims: int = DIMS, store_dir: Path = STORE_DIR) -> Path:
    return store_dir / f"emb__{model.replace('/', '_')}__d{dims}.npz"


def save_store(path: Path, keys: list[tuple[str, str]], vecs: np.ndarray) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(path, names=np.array([k[0] for k in keys]),
                        vtypes=np.array([k[1] for k in keys]), vecs=vecs.astype(np.float32))


def load_store(path: Path) -> dict[tuple[str, str], np.ndarray]:
    """(name, vtype) -> L2-normalised vector."""
    if not path.exists():
        return {}
    z = np.load(path)
    vecs = z["vecs"] / np.maximum(np.linalg.norm(z["vecs"], axis=1, keepdims=True), 1e-12)
    return {(str(n), str(t)): v for n, t, v in zip(z["names"], z["vtypes"], vecs, strict=True)}


def precompute(items: list[Item], client, model: str, path: Path, dims: int = DIMS,
               tag: str = "embeddings") -> dict:
    """Embed every item not yet in the store; rewrite the store. Returns counts."""
    have = load_store(path)
    todo = [it for it in items if (it.name, it.vtype) not in have]
    if todo:
        vecs = client.embed([item_text(it) for it in todo], model=model, dimensions=dims, tag=tag)
        merged = dict(have)
        merged.update({(it.name, it.vtype): np.asarray(v, dtype=np.float32)
                       for it, v in zip(todo, vecs, strict=True)})
        keys = sorted(merged)
        save_store(path, keys, np.stack([merged[k] for k in keys]))
    return {"items": len(items), "already_stored": len(items) - len(todo), "embedded": len(todo)}


def default_store() -> Path:
    from smt_trial_matching.llm import embed_model

    return Path(os.getenv("EMB_ANSWERABILITY_STORE") or store_path(embed_model()))


# ------------------------------------------------------------------------------ model


class EmbAnswerabilityModel(AnswerabilityModel):
    """v1's two regressions with embedding features. ``scale`` multiplies the unit-norm embedding,
    which sets how strongly it is regularised relative to the 0/1 word features."""

    def __init__(self, vectors: dict[tuple[str, str], np.ndarray], mode: str = "name_emb",
                 c: float = C_DEFAULT, scale: float = 1.0) -> None:
        if mode not in MODES:
            raise ValueError(f"mode must be one of {MODES}")
        super().__init__(c=c)
        self.vectors, self.mode, self.scale = vectors, mode, scale
        self.dims = len(next(iter(vectors.values()))) if vectors else DIMS
        self.missing = 0
        self._answered = LogisticRegression(C=c, max_iter=5000, random_state=SEED)
        self._true = LogisticRegression(C=c, max_iter=5000, random_state=SEED)

    def _emb(self, keys: list[tuple[str, str]]) -> sparse.csr_matrix:
        rows = []
        for k in keys:
            v = self.vectors.get(k)
            if v is None:
                self.missing += 1
                v = np.zeros(self.dims, dtype=np.float32)
            rows.append(v)
        return sparse.csr_matrix(np.stack(rows) * self.scale)

    def _X(self, keys: list[tuple[str, str]], fit: bool = False) -> sparse.csr_matrix:
        emb = self._emb(keys)
        if self.mode == "emb":
            return emb
        feats = [features(n, t) for n, t in keys]
        words = self._vec.fit_transform(feats) if fit else self._vec.transform(feats)
        return sparse.hstack([words, emb], format="csr")

    def fit(self, examples: list[Example]) -> EmbAnswerabilityModel:
        self._vec = DictVectorizer()
        X = self._X([(e.name, e.vtype) for e in examples], fit=True)
        self._answered.fit(X, np.array([e.value is not None for e in examples]))
        bools = [i for i, e in enumerate(examples) if isinstance(e.value, bool)]
        self._true.fit(X[bools], np.array([examples[i].value for i in bools]))
        self._cache.clear()
        self._values = _value_distributions(examples)
        return self

    def predict(self, name: str, vtype: str) -> tuple[float, float]:
        k = (name, vtype)
        if k not in self._cache:
            x = self._X([k])
            self._cache[k] = (float(self._answered.predict_proba(x)[0, 1]),
                              float(self._true.predict_proba(x)[0, 1]))
        return self._cache[k]


@cache
def _vectors(path: str) -> dict[tuple[str, str], np.ndarray]:
    store = load_store(Path(path))
    if not store:
        raise FileNotFoundError(f"No embedding store at {path}. Run scripts/precompute_embeddings.py "
                                "(needs GEMINI_API_KEY in .env) or set EMB_ANSWERABILITY_STORE.")
    return store


@cache
def _fit(fold: int | None, mode: str, c: float, scale: float, key: str,
         path: str) -> EmbAnswerabilityModel:
    """fold None = fit on all of dev (the model for non-dev patients)."""
    train = [q for q in load_split("dev") if fold is None or dev_fold(q) != fold]
    return EmbAnswerabilityModel(_vectors(path), mode, c, scale).fit(load_examples(train, key))


def fold_model(fold: int | None, mode: str = "name_emb", c: float = C_DEFAULT, scale: float = 1.0,
               key: str = "gpt5_oracle", store: str | None = None) -> EmbAnswerabilityModel:
    return _fit(fold, mode, float(c), float(scale), key, store or str(default_store()))


def emb_model_for(trials: Iterable[str], mode: str = "name_emb", c: float = C_DEFAULT,
                  scale: float = 1.0, key: str = "gpt5_oracle",
                  store: str | None = None) -> EmbAnswerabilityModel:
    """Same fold choice as ``answerability.model_for``: a dev patient gets the model of the other folds."""
    qid = _patient_trials().get(frozenset(trials))
    fold = dev_fold(qid) if qid else None
    return fold_model(fold, mode, c, scale, key, store)
