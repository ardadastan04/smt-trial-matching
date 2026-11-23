"""Dev evaluation of LLM answerability (v2 version A) against the name model. No LLM calls.

Reads the precomputed store and compares, on every dev answer-key entry whose variable is in the store:
- AUC of P(answered) (answered vs unknown): LLM (zero-shot, so every dev patient is held out) vs the
  name model cross-fitted by patient (each dev patient scored by the model that did not see them);
- AUC of P(true) on answered Bool entries; mean predicted vs observed rates (calibration at a glance).
Writes the same numbers to runs/llm_answerability/dev_eval.json.

  uv run python scripts/eval_llm_answerability.py [--store PATH]

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
    y = np.array([e.value is not None for e, *_ in rows])
    out = {"covered": len(rows), "answered_rate": float(y.mean()),
           "llm_mean_p_answered": float(np.mean([r[1] for r in rows])),
           "auc_p_answered": {"llm": float(roc_auc_score(y, [r[1] for r in rows])),
                              "name_crossfit": float(roc_auc_score(y, [r[3] for r in rows]))}}
    b = [r for r in rows if isinstance(r[0].value, bool) and r[2] is not None]
    if b and len({r[0].value for r in b}) == 2:
        yt = [r[0].value for r in b]
        out["true_rate"] = float(np.mean(yt))
        out["auc_p_true"] = {"llm": float(roc_auc_score(yt, [r[2] for r in b])),
                             "name_crossfit": float(roc_auc_score(yt, [r[4] for r in b]))}
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--store", default=None)
    ap.add_argument("--key", default="gpt5_oracle")
    a = ap.parse_args()
    path = a.store or str(store_path(default_model_id()))
    res = evaluate(load_store(__import__("pathlib").Path(path)), a.key)
    print(json.dumps(res, indent=1))
    STORE_DIR.mkdir(parents=True, exist_ok=True)
    (STORE_DIR / "dev_eval.json").write_text(json.dumps({"store": path, **res}, indent=1))


if __name__ == "__main__":
    main()
