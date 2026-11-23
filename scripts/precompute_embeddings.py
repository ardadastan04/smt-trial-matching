"""Embed variable texts (v2 version B) for the variables of chosen patients. Names, types, meanings only.

Calls go through llm.LLMClient.embed (cost log in runs/<run_id>/cost.jsonl, disk cache, MAX_RUN_USD).
Per CLAUDE.md: develop on <= 5 patients; more needs --confirmed (Arda's OK).

  uv run python scripts/precompute_embeddings.py --split dev --limit 5
  uv run python scripts/precompute_embeddings.py --split dev --limit 0 --confirmed
"""

from __future__ import annotations

import argparse
import json
import sys

from smt_trial_matching.answerability import load_split
from smt_trial_matching.llm_answerability import items_for
from smt_trial_matching.llm_embeddings import DIMS, item_text, precompute, store_path

MAX_UNCONFIRMED_PATIENTS = 5


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--split", choices=["dev", "test", "all"], default="dev")
    ap.add_argument("--limit", type=int, default=MAX_UNCONFIRMED_PATIENTS, help="0 = all")
    ap.add_argument("--confirmed", action="store_true")
    ap.add_argument("--dims", type=int, default=DIMS)
    ap.add_argument("--run-id", default="llm_answerability")
    ap.add_argument("--show", type=int, default=0, help="print the first N texts and stop (no calls)")
    a = ap.parse_args()

    qids = sorted(load_split("dev") + load_split("test")) if a.split == "all" else sorted(load_split(a.split))
    if a.limit:
        qids = qids[:a.limit]
    items = items_for(qids)
    if a.show:
        print("\n".join(item_text(it) for it in items[:a.show]))
        return 0
    if len(qids) > MAX_UNCONFIRMED_PATIENTS and not a.confirmed:
        print(f"{len(qids)} patients > {MAX_UNCONFIRMED_PATIENTS}: rerun with --confirmed after Arda's OK",
              file=sys.stderr)
        return 2

    from smt_trial_matching.llm import LLMClient, embed_model

    client = LLMClient(a.run_id)
    model = embed_model()
    path = store_path(model, a.dims)
    print(f"model {model}; store {path}; {len(qids)} patients, {len(items)} variables")
    print(json.dumps(precompute(items, client, model, path, a.dims), indent=1))
    print(client.summary())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
