"""Precompute zero-shot LLM answerability (v2 version A) for the variables of chosen patients.

Asks the LLM once per unique variable (batched), through llm.LLMClient (cost log in
runs/<run_id>/cost.jsonl, disk cache, MAX_RUN_USD guard), and appends to the prediction store that
answerable_informative_llm reads. The LLM sees variable names, types and meanings only, never notes.

Per CLAUDE.md: develop on <= 5 patients; more needs --confirmed (Arda's OK). Default model is the
project's CHEAP_MODEL (override with --model or LLM_ANSWERABILITY_MODEL).

  uv run python scripts/precompute_llm_answerability.py --estimate              # no key, no calls
  uv run python scripts/precompute_llm_answerability.py --split dev --limit 5   # first 5 dev patients
  uv run python scripts/precompute_llm_answerability.py --split dev --confirmed # all 28 dev patients
"""

from __future__ import annotations

import argparse
import json
import sys

from smt_trial_matching.answerability import load_split
from smt_trial_matching.llm_answerability import (
    DEFAULT_BATCH,
    estimate,
    items_for,
    load_store,
    precompute,
    store_path,
)

MAX_UNCONFIRMED_PATIENTS = 5


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--split", choices=["dev", "test", "all"], default="dev")
    ap.add_argument("--limit", type=int, default=MAX_UNCONFIRMED_PATIENTS,
                    help="first N patients of the split (sorted ids); 0 = all")
    ap.add_argument("--confirmed", action="store_true", help="allow more than 5 patients")
    ap.add_argument("--estimate", action="store_true", help="print calls / tokens / USD and stop")
    ap.add_argument("--model", default=None)
    ap.add_argument("--batch", type=int, default=DEFAULT_BATCH)
    ap.add_argument("--run-id", default="llm_answerability")
    a = ap.parse_args()

    qids = sorted(load_split("dev") + load_split("test")) if a.split == "all" else sorted(load_split(a.split))
    if a.limit:
        qids = qids[:a.limit]
    if len(qids) > MAX_UNCONFIRMED_PATIENTS and not a.confirmed and not a.estimate:
        print(f"{len(qids)} patients > {MAX_UNCONFIRMED_PATIENTS}: rerun with --confirmed after Arda's OK",
              file=sys.stderr)
        return 2
    items = items_for(qids)

    if a.estimate:
        print(json.dumps({"patients": len(qids), **estimate(items, a.batch)}, indent=1))
        print("(USD at CHEAP_MODEL list prices 0.25 / 1.50 per M tokens, about 4 chars per token)")
        return 0

    from smt_trial_matching.llm import BudgetExceeded, ConfigError, LLMClient
    from smt_trial_matching.llm_answerability import default_model_id

    try:
        model = a.model or default_model_id()
        client = LLMClient(a.run_id)
    except ConfigError as exc:
        print(f"config error: {exc}", file=sys.stderr)
        return 2
    path = store_path(model)
    print(f"model {model}; store {path}; {len(qids)} patients, {len(items)} variables; "
          f"{len(load_store(path))} already stored")
    try:
        counts = precompute(items, client, model, path, a.batch)
    except BudgetExceeded as exc:
        print(f"stopped: {exc}", file=sys.stderr)
        return 3
    print(json.dumps(counts, indent=1))
    print(client.summary())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
