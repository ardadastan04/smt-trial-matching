"""Dev evaluation of LLM answerability (v2 version A) against the name model. No LLM calls.

Reads the precomputed store and compares, on every dev answer-key entry whose variable is in the store:
- AUC of P(answered) (answered vs unknown): LLM (zero-shot, so every dev patient is held out) vs the
  name model cross-fitted by patient (each dev patient scored by the model that did not see them);
- AUC of P(true) on answered Bool entries; mean predicted vs observed rates (calibration at a glance).
Paired bootstrap CIs (2,000 resamples of dev patients, seed 0) on the AUC differences.
Writes the same numbers to runs/llm_answerability/dev_eval_<key>.json.

  uv run python scripts/eval_llm_answerability.py [--store PATH] [--key gpt5mini]

The dev policy curve is a harness run:
  uv run python -m smt_trial_matching.experiment --config configs/llm_answerability_dev.yaml
"""

from __future__ import annotations

import argparse
import json

import numpy as np
from sklearn.metrics import roc_auc_score

from smt_trial_matching.answerability import _fold_model, dev_fold, load_examples, load_split
from smt_trial_matching.llm_answerability import STORE_DIR, default_model_id, load_store, store_path


def _emb_predictors(key: str) -> dict:
    """Version B fold models at the chosen settings, if the embedding store exists."""
    from smt_trial_matching.llm_embeddings import CHOSEN, default_store, fold_model

    if not default_store().exists():
        return {}
    return {f"emb_{m}": (lambda e, m=m, c=c, s=s: fold_model(dev_fold(e.qid), m, c, s, key)
                         .predict(e.name, e.vtype)) for m, (c, s) in CHOSEN.items()}


def evaluate(store: dict[str, dict], key: str = "gpt5_oracle") -> dict:
    by = {(r["name"], r["vtype"]): r for r in store.values()}
    rows = []
    for e in load_examples(load_split("dev"), key):
        r = by.get((e.name, e.vtype))
        if r is None:
            continue
        name_pa, name_pt = _fold_model(dev_fold(e.qid), key).predict(e.name, e.vtype)
        rows.append((e, r["p_answered"], r["p_true"], name_pa, name_pt))
    if not rows:
        return {"covered": 0}
    emb = {n: [f(e) for e, *_ in rows] for n, f in _emb_predictors(key).items()}
    y = np.array([e.value is not None for e, *_ in rows])
    out = {"covered": len(rows), "answered_rate": float(y.mean()),
           "llm_mean_p_answered": float(np.mean([r[1] for r in rows])),
           "auc_p_answered": {"llm": float(roc_auc_score(y, [r[1] for r in rows])),
                              "name_crossfit": float(roc_auc_score(y, [r[3] for r in rows]))}}
    qids = [e.qid for e, *_ in rows]
    name_pa = [r[3] for r in rows]
    out["auc_p_answered"]["llm_minus_name_ci95"] = boot_auc_diff(qids, y, [r[1] for r in rows], name_pa)
    for n, preds in emb.items():
        pa = [p[0] for p in preds]
        out["auc_p_answered"][n] = float(roc_auc_score(y, pa))
        out["auc_p_answered"][f"{n}_minus_name_ci95"] = boot_auc_diff(qids, y, pa, name_pa)
    bi = [i for i, r in enumerate(rows) if isinstance(r[0].value, bool) and r[2] is not None]
    b = [rows[i] for i in bi]
    if b and len({r[0].value for r in b}) == 2:
        yt = np.array([r[0].value for r in b])
        out["true_rate"] = float(np.mean(yt))
        out["auc_p_true"] = {"llm": float(roc_auc_score(yt, [r[2] for r in b])),
                             "name_crossfit": float(roc_auc_score(yt, [r[4] for r in b])),
                             "llm_minus_name_ci95": boot_auc_diff(
                                 [r[0].qid for r in b], yt, [r[2] for r in b], [r[4] for r in b])}
        for n, preds in emb.items():
            pt = [preds[i][1] for i in bi]
            out["auc_p_true"][n] = float(roc_auc_score(yt, pt))
            out["auc_p_true"][f"{n}_minus_name_ci95"] = boot_auc_diff(
                [r[0].qid for r in b], yt, pt, [r[4] for r in b])
    return out


def boot_auc_diff(qids: list[str], y, a: list[float], b: list[float], n: int = 2000,
                  seed: int = 0) -> list[float]:
    """AUC(a) - AUC(b): point estimate and 95% CI, paired bootstrap resampling patients."""
    y, a, b = np.asarray(y), np.asarray(a), np.asarray(b)
    groups: dict[str, list[int]] = {}
    for i, q in enumerate(qids):
        groups.setdefault(q, []).append(i)
    idx = [np.array(v) for v in groups.values()]
    rng = np.random.default_rng(seed)
    diffs = []
    for _ in range(n):
        sel = np.concatenate([idx[j] for j in rng.integers(0, len(idx), len(idx))])
        if len(set(y[sel].tolist())) == 2:
            diffs.append(roc_auc_score(y[sel], a[sel]) - roc_auc_score(y[sel], b[sel]))
    point = roc_auc_score(y, a) - roc_auc_score(y, b)
    lo, hi = np.percentile(diffs, [2.5, 97.5])
    return [round(float(point), 4), round(float(lo), 4), round(float(hi), 4)]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--store", default=None)
    ap.add_argument("--key", default="gpt5_oracle")
    a = ap.parse_args()
    path = a.store or str(store_path(default_model_id()))
    res = evaluate(load_store(__import__("pathlib").Path(path)), a.key)
    print(json.dumps(res, indent=1))
    STORE_DIR.mkdir(parents=True, exist_ok=True)
    (STORE_DIR / f"dev_eval_{a.key}.json").write_text(json.dumps({"store": path, **res}, indent=1))


if __name__ == "__main__":
    main()
