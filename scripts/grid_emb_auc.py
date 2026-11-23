"""Choose version B's settings on dev: held-out answerability AUC over modes x C x embedding scale.

For each setting, every dev patient is scored by the fold model that did not see them (5 folds by
patient, as v1), and AUC is taken over all pooled held-out entries, as for v1's C choice
(``answerability.crossfit_auc``). No LLM calls: reads the embedding store. Writes
runs/llm_answerability/emb_grid.json.

  uv run python scripts/grid_emb_auc.py
"""

from __future__ import annotations

import json

from sklearn.metrics import roc_auc_score

from smt_trial_matching.answerability import _fold_model, dev_fold, load_examples, load_split
from smt_trial_matching.llm_answerability import STORE_DIR
from smt_trial_matching.llm_embeddings import fold_model

CS = (0.03, 0.1, 0.3, 1.0, 3.0)
SCALES = {"emb": (1.0,), "name_emb": (1.0, 3.0, 10.0)}
KEYS = ("gpt5_oracle", "gpt5mini")


def heldout_auc(predict, key: str) -> dict[str, float]:
    ex = load_examples(load_split("dev"), key)
    pa, ya, pt, yt = [], [], [], []
    for e in ex:
        p_ans, p_true = predict(dev_fold(e.qid), e)
        pa.append(p_ans)
        ya.append(e.value is not None)
        if isinstance(e.value, bool):
            pt.append(p_true)
            yt.append(e.value)
    return {"auc_p_answered": round(float(roc_auc_score(ya, pa)), 4),
            "auc_p_true": round(float(roc_auc_score(yt, pt)), 4)}


def main() -> None:
    rows = []
    for key in KEYS:
        rows.append({"key": key, "mode": "name (v1)", "c": 0.3, "scale": None,
                     **heldout_auc(lambda f, e, k=key: _fold_model(f, k).predict(e.name, e.vtype), key)})
        print(rows[-1], flush=True)
        for mode, scales in SCALES.items():
            for c in CS:
                for s in scales:
                    def pred(f, e, k=key, m=mode, c=c, s=s):
                        return fold_model(f, m, c, s, k).predict(e.name, e.vtype)
                    rows.append({"key": key, "mode": mode, "c": c, "scale": s, **heldout_auc(pred, key)})
                    print(rows[-1], flush=True)
    STORE_DIR.mkdir(parents=True, exist_ok=True)
    (STORE_DIR / "emb_grid.json").write_text(json.dumps(rows, indent=1))


if __name__ == "__main__":
    main()
