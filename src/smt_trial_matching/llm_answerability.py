"""Version A of the LLM answerability variant (v2 work, Nov 22): zero-shot Gemini P(answered), P(true).

The name model (``answerability.py``) learns P(answered) from variable-name words; its held-out AUC
is 0.75, and the answerability oracle shows better P(answered) is our largest remaining lever. Here an
LLM is asked, with no training, how likely a short admission-style case note is to settle each
variable, and how likely the answer is "true".

What the LLM sees, per variable: its canonical name, its type (Bool or a number), and the CA's
plain-language meaning from ``data/variables/<NCT>.json`` when one exists. It NEVER sees a patient
note, an answer key, or a gold label, so predictions are the same for every patient and there is
nothing to cross-fit.

Flow:
1. ``scripts/precompute_llm_answerability.py`` collects the unique (name, type, meaning) items for
   chosen patients, asks the LLM in batches through ``llm.LLMClient`` (cost log, disk cache, budget
   guard), and appends one JSON line per variable to a prediction store
   (``runs/llm_answerability/<model>__<PROMPT_VERSION>.jsonl``, gitignored). Each variable is asked
   once; reruns are free.
2. During a policy run, ``LLMAnswerabilityModel`` only reads that store: no network calls, so runs
   are fast, parallel-safe and reproducible. A variable missing from the store falls back to the
   name model (counted in ``.fallbacks``), or raises with ``strict=True``.
3. Numbers keep the name model's empirical value distribution (age): that is data, not a guess, and
   it stays cross-fitted for dev patients.

Select it with ``AnswerableConfig(answerability="llm")`` (policy ``answerable_informative_llm``).
policy-v1 is unchanged (its default is ``"name"``).
"""

from __future__ import annotations

import hashlib
import json
import math
import os
import re
from collections.abc import Iterable
from dataclasses import dataclass
from functools import cache
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
STORE_DIR = ROOT / "runs" / "llm_answerability"

#: Bump when the prompt or parsing changes: it is part of the store name and every item key.
PROMPT_VERSION = "a1"
DEFAULT_BATCH = 20
#: Probabilities are clipped to this range, so no question is treated as impossible or certain.
P_MIN, P_MAX = 0.02, 0.98

SYSTEM = (
    "You estimate what a clinical case note is likely to contain. You never see the note itself. "
    "Answer only with JSON."
)

INSTRUCTIONS = """Context: patients are screened for clinical trials from a short, de-identified
case note written like the start of a hospital admission note (1-2 paragraphs plus a past medical
history list; it states age, sex, the presenting problem, key findings, labs and history). A
coordinator asks about one fact at a time. Each fact below is a variable from a trial's
eligibility rules, with its type and, when available, a plain-language meaning.

For each fact give:
- "p_answered": the probability (0-1) that a typical note of this kind settles the fact, either
  by stating it or by clearly implying its value. Facts a note rarely mentions (allergies,
  genotypes, consent, contraception, exact severity grades, protocol-specific items) are low;
  demographics and the main diagnosis are high.
- "p_true": for a yes/no fact, the probability that the answer is "yes" when the note does settle
  it, for a typical patient screened for a trial that asks about it. For numbers use null.

Return a JSON list with one object per fact, in the same order:
[{"id": 1, "p_answered": 0.0, "p_true": 0.0}, ...]

Facts:
"""


@dataclass(frozen=True)
class Item:
    """One variable to ask about. ``meaning`` may be empty."""

    name: str
    vtype: str
    meaning: str

    @property
    def key(self) -> str:
        raw = json.dumps([PROMPT_VERSION, self.name, self.vtype, self.meaning])
        return hashlib.sha256(raw.encode()).hexdigest()[:20]


# ------------------------------------------------------------------------------- items


@cache
def _variables(nct: str) -> tuple[dict, ...]:
    path = DATA / "variables" / f"{nct}.json"
    return tuple(json.loads(path.read_text())) if path.exists() else ()


def items_for(qids: Iterable[str]) -> list[Item]:
    """Unique (name, type, meaning) items over the candidate trials of the given patients.

    Keyed by (name, type): the first non-empty meaning found (trials sorted) is used, so the
    prediction for a name does not depend on which trial asks it, matching ``predict(name, vtype)``.
    """
    keep = set(qids)
    ncts = sorted({p["nct"] for p in map(json.loads, (DATA / "pairs.jsonl").open())
                   if p["qid"] in keep})
    by: dict[tuple[str, str], str] = {}
    for nct in ncts:
        for v in _variables(nct):
            k = (v["name"], v["type"])
            if not by.get(k):
                by[k] = (v.get("meaning") or "").strip()
    return [Item(n, t, m) for (n, t), m in sorted(by.items())]


# ------------------------------------------------------------------------- prompt / parse


def build_prompt(batch: list[Item]) -> list[dict[str, str]]:
    lines = []
    for i, it in enumerate(batch, 1):
        kind = "yes/no" if it.vtype == "Bool" else f"number ({it.vtype})"
        meaning = f" | meaning: {it.meaning}" if it.meaning else ""
        lines.append(f"{i}. {it.name} | type: {kind}{meaning}")
    return [{"role": "system", "content": SYSTEM},
            {"role": "user", "content": INSTRUCTIONS + "\n".join(lines)}]


def _clip(x: Any) -> float | None:
    try:
        v = float(x)
    except (TypeError, ValueError):
        return None
    if math.isnan(v):
        return None
    return min(P_MAX, max(P_MIN, v))


def parse_response(text: str, n: int) -> list[tuple[float | None, float | None]]:
    """(p_answered, p_true) per fact, in order; (None, None) where the reply is missing or bad.

    Tolerates ```json fences and prose around the list; matches by ``id`` when present."""
    m = re.search(r"\[.*\]", text, flags=re.DOTALL)
    if not m:
        return [(None, None)] * n
    try:
        rows = json.loads(m.group(0))
    except json.JSONDecodeError:
        return [(None, None)] * n
    out: list[tuple[float | None, float | None]] = [(None, None)] * n
    for pos, row in enumerate(rows if isinstance(rows, list) else []):
        if not isinstance(row, dict):
            continue
        idx = row.get("id", pos + 1)
        if isinstance(idx, int) and 1 <= idx <= n:
            out[idx - 1] = (_clip(row.get("p_answered")), _clip(row.get("p_true")))
    return out


# ----------------------------------------------------------------------------- store


def store_path(model: str, store_dir: Path = STORE_DIR) -> Path:
    safe = re.sub(r"[^A-Za-z0-9._-]+", "_", model)
    return store_dir / f"{safe}__{PROMPT_VERSION}.jsonl"


def load_store(path: Path) -> dict[str, dict]:
    """key -> row. Later lines win, so a re-asked item replaces an earlier one."""
    out: dict[str, dict] = {}
    if path.exists():
        for line in path.read_text().splitlines():
            if line.strip():
                row = json.loads(line)
                out[row["key"]] = row
    return out


def precompute(items: list[Item], client: Any, model: str, path: Path,
               batch_size: int = DEFAULT_BATCH, run_id_tag: str = "llm_answerability") -> dict:
    """Ask the LLM about every item not yet in the store; append results. Returns counts.

    ``client`` is an ``llm.LLMClient`` (or a test double with the same ``complete``). Items the
    reply leaves out or garbles are retried once in a batch of their own size 1; still-bad items
    are not stored (they fall back to the name model at run time)."""
    have = load_store(path)
    todo = [it for it in items if it.key not in have]
    path.parent.mkdir(parents=True, exist_ok=True)
    stored = failed = 0

    def ask(batch: list[Item]) -> list[Item]:
        nonlocal stored
        reply = client.complete(build_prompt(batch), model=model, tag=run_id_tag,
                                temperature=0.0, max_tokens=60 * len(batch) + 100)
        bad = []
        with path.open("a") as fh:
            for it, (pa, pt) in zip(batch, parse_response(reply.text, len(batch)), strict=True):
                if pa is None or (it.vtype == "Bool" and pt is None):
                    bad.append(it)
                    continue
                fh.write(json.dumps({"key": it.key, "name": it.name, "vtype": it.vtype,
                                     "p_answered": pa, "p_true": pt, "model": model,
                                     "prompt_version": PROMPT_VERSION}) + "\n")
                stored += 1
        return bad

    retry: list[Item] = []
    for i in range(0, len(todo), batch_size):
        retry += ask(todo[i:i + batch_size])
    for it in retry:
        failed += len(ask([it]))
    return {"items": len(items), "already_stored": len(items) - len(todo),
            "asked": len(todo), "stored": stored, "failed": failed}


def estimate(items: list[Item], batch_size: int = DEFAULT_BATCH, usd_in: float = 0.25,
             usd_out: float = 1.50) -> dict:
    """Rough call count, tokens and USD before any call (4 characters per token)."""
    calls, tok_in, tok_out = 0, 0, 0
    for i in range(0, len(items), batch_size):
        batch = items[i:i + batch_size]
        calls += 1
        tok_in += sum(len(m["content"]) for m in build_prompt(batch)) // 4
        tok_out += 25 * len(batch)
    usd = (tok_in * usd_in + tok_out * usd_out) / 1e6
    return {"items": len(items), "calls": calls, "tokens_in": tok_in, "tokens_out": tok_out,
            "usd": round(usd, 4)}


# ------------------------------------------------------------------------------ model


def default_model_id() -> str:
    """LLM_ANSWERABILITY_MODEL if set, else the project's CHEAP_MODEL (CLAUDE.md: cheapest)."""
    from smt_trial_matching.llm import load_env, resolve_model

    load_env()
    return os.getenv("LLM_ANSWERABILITY_MODEL") or resolve_model("cheap")


class LLMAnswerabilityModel:
    """Same interface as ``answerability.AnswerabilityModel``, reading a precomputed store.

    ``fallback`` is the name model for the same patient (used for numbers' value distributions,
    and for any variable missing from the store unless ``strict``)."""

    def __init__(self, store: dict[str, dict], fallback: Any, strict: bool = False) -> None:
        self._by_name = {(r["name"], r["vtype"]): r for r in store.values()}
        self.fallback = fallback
        self.strict = strict
        self.fallbacks = 0

    def predict(self, name: str, vtype: str) -> tuple[float, float]:
        row = self._by_name.get((name, vtype))
        if row is None:
            if self.strict:
                raise KeyError(f"{name} ({vtype}) is not in the LLM answerability store; "
                               "run scripts/precompute_llm_answerability.py for these patients")
            self.fallbacks += 1
            return self.fallback.predict(name, vtype)
        p_true = row["p_true"] if row["p_true"] is not None else self.fallback.p_true(name, vtype)
        return float(row["p_answered"]), float(p_true)

    def p_answered(self, name: str, vtype: str) -> float:
        return self.predict(name, vtype)[0]

    def p_true(self, name: str, vtype: str) -> float:
        return self.predict(name, vtype)[1]

    def value_distribution(self, name: str) -> list[tuple[float, float]] | None:
        return self.fallback.value_distribution(name)


@cache
def _store_for(path: str) -> dict[str, dict]:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(
            f"No LLM answerability store at {p}. Run scripts/precompute_llm_answerability.py "
            "(needs GEMINI_API_KEY in .env) or set LLM_ANSWERABILITY_STORE.")
    return load_store(p)


_MODELS: dict[tuple[str, int], LLMAnswerabilityModel] = {}


def llm_model_for(trials: Iterable[str], key: str = "gpt5_oracle", c: float | None = None,
                  store: str | None = None) -> LLMAnswerabilityModel:
    """The LLM model for one patient: the shared store plus that patient's name model (fallback).

    One object per (store, name model), so ``.fallbacks`` accumulates over a run."""
    from smt_trial_matching.answerability import C_DEFAULT, model_for

    path = store or os.getenv("LLM_ANSWERABILITY_STORE") or str(store_path(default_model_id()))
    fallback = model_for(list(trials), key, C_DEFAULT if c is None else c)
    k = (path, id(fallback))
    if k not in _MODELS:
        _MODELS[k] = LLMAnswerabilityModel(_store_for(path), fallback)
    return _MODELS[k]
