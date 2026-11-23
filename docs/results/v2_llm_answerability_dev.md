# v2 version A: zero-shot Gemini answerability, dev results (2026-11-23)

**Dev only. v2 is not frozen and the test split was not touched.** policy-v1 stays frozen at `ede13d9`.

## What was run

- Answerability source: `gemini-3.1-flash-lite` (the project's CHEAP_MODEL), prompt version `a1`, asked once per
  unique (variable name, type, meaning) over the candidate trials of all 28 dev patients. The LLM sees the
  variable name, its type and the CA's plain-language meaning only. It never sees a patient note, an answer
  key or a label, so the predictions are the same for every patient and there is nothing to cross-fit.
- 4,264 variables, 4,236 stored (28, or 0.7%, came back unparseable twice and fall back to the name model).
  273 calls, **$0.26 total** (5-patient check 64 calls / $0.06, rest of dev $0.20), logged in
  `runs/llm_answerability/cost.jsonl`.
- Policy: `answerable_informative_llm` = the frozen v1 scoring (`P(answered) x value`, alpha 1, C 0.3) with
  only the P(answered) / P(true) source swapped. Numbers keep the name model's value distribution.
- Comparison: v1 (`answerable_informative`, name model cross-fitted by patient on dev), `greedy_smt`, and the
  answerability oracle (reads the key; a reference, not a method). Budget 30, no early stopping, seed 0.
  Both answer keys: `gpt5_oracle` (primary) and `gpt5mini` (robustness). 95% CIs are a paired bootstrap over
  the 28 dev patients (2,000 resamples, seed 0).

5-patient sanity check (before the full run): p_answered spread from 0.02 to 0.98 (median 0.3); the top was age,
sex and "has the disease / is in hospital", the bottom was caregiver facts, CFU counts and six-minute-walk
details. That looked sensible, so the full dev run went ahead.

## 1. Answerability prediction (AUC, all dev answer-key entries the store covers)

LLM minus name model, with paired patient-bootstrap 95% CI.

| key | entries | answered rate | P(answered) AUC: LLM | name (cross-fit) | Δ [95% CI] | P(true) AUC: LLM | name | Δ [95% CI] |
|---|---|---|---|---|---|---|---|---|
| gpt5_oracle | 5,024 | 0.431 | 0.717 | 0.748 | -0.031 [-0.071, +0.007] | 0.712 | 0.682 | +0.030 [-0.068, +0.119] |
| gpt5mini | 5,123 | 0.621 | 0.694 | 0.755 | -0.060 [-0.095, -0.032] | 0.690 | 0.675 | +0.015 [-0.083, +0.087] |

Zero-shot Gemini **does not beat** the name model at predicting whether a fact gets answered. It is slightly
worse on the primary key (not significant) and clearly worse on gpt5mini. It is a bit better at P(true), but
the CI includes zero. It also under-predicts overall: mean p_answered 0.39 against an observed 0.43 (oracle key)
and 0.62 (gpt5mini key).

## 2. Dev accuracy vs question budget

Pair-level accuracy, 188 pairs, [95% CI over patients].

### Key gpt5_oracle (primary)

| policy | k=5 | k=10 | k=20 | k=30 | AUC (k=0..30) | questions / patient | CA not-useful share |
|---|---|---|---|---|---|---|---|
| greedy_smt | 0.564 | 0.564 | 0.612 | 0.691 | 0.599 | 28.0 | 0.000 |
| v1 (name model) | 0.622 | 0.670 | 0.745 | **0.793** | **0.700** | 26.4 | 0.034 |
| v2-A (Gemini) | 0.617 | 0.681 | 0.729 | 0.777 | 0.694 | 26.5 | 0.077 |
| answerability oracle | 0.665 | 0.739 | 0.862 | 0.910 | 0.783 | 20.2 | 0.062 |

v1 and greedy reproduce the frozen numbers (0.793 and 0.691 at k=30).

### Key gpt5mini (robustness)

| policy | k=5 | k=10 | k=20 | k=30 | AUC | questions / patient | CA not-useful share |
|---|---|---|---|---|---|---|---|
| greedy_smt | 0.564 | 0.569 | 0.590 | 0.612 | 0.580 | 27.9 | 0.000 |
| v1 (name model) | 0.601 | 0.617 | 0.686 | 0.734 | 0.651 | 26.1 | 0.034 |
| v2-A (Gemini) | 0.622 | 0.654 | 0.713 | 0.723 | 0.673 | 25.5 | 0.072 |
| answerability oracle | 0.622 | 0.660 | 0.718 | 0.771 | 0.684 | 22.2 | 0.055 |

### Paired differences (accuracy, policy minus reference, [95% CI], p)

| key | comparison | k=5 | k=10 | k=20 | k=30 | AUC |
|---|---|---|---|---|---|---|
| gpt5_oracle | v2-A − v1 | -0.005 [-0.04, +0.02] | +0.011 [-0.03, +0.05] | -0.016 [-0.07, +0.03] | -0.016 [-0.08, +0.05], p .69 | -0.006 [-0.03, +0.02], p .74 |
| gpt5_oracle | v2-A − greedy | +0.053 [-0.01, +0.12] | +0.117 [+0.05, +0.19] | +0.117 [+0.04, +0.20] | +0.085 [+0.01, +0.16], p .037 | +0.095 [+0.04, +0.16], p <.001 |
| gpt5_oracle | v1 − greedy | +0.059 [-0.01, +0.13] | +0.106 [+0.02, +0.20] | +0.133 [+0.04, +0.23] | +0.101 [+0.01, +0.19], p .026 | +0.101 [+0.03, +0.18], p <.001 |
| gpt5mini | v2-A − v1 | +0.021 [-0.02, +0.06] | +0.037 [+0.00, +0.08], p .072 | +0.027 [-0.04, +0.09] | -0.011 [-0.06, +0.04], p .81 | +0.022 [-0.01, +0.06], p .18 |
| gpt5mini | v2-A − greedy | +0.059 [+0.00, +0.12] | +0.085 [+0.01, +0.17] | +0.122 [+0.03, +0.21] | +0.112 [+0.03, +0.20], p .012 | +0.094 [+0.03, +0.17], p .005 |
| gpt5mini | v1 − greedy | +0.037 [-0.03, +0.11] | +0.048 [-0.03, +0.14] | +0.096 [-0.01, +0.21] | +0.122 [+0.02, +0.23], p .023 | +0.072 [-0.00, +0.16], p .068 |

## Reading

- **v2-A is a tie with v1, not an improvement.** On the primary key it is within 0.02 of v1 at every budget and
  AUC, with CIs on both sides of zero. On gpt5mini it is slightly ahead at small budgets (AUC +0.022, not
  significant) and level at k=30.
- Like v1, it beats greedy clearly on both keys (AUC about +0.09, k=30 +0.09 to +0.11).
- **It asks more useless questions.** The share of questions that could not change any trial's status (CA rule)
  roughly doubles, from 3.4% to 7.7% (oracle key) and from 3.4% to 7.2% (gpt5mini). Since you prefer few
  useless questions, that counts against v2-A. Under the cohort rule both are 0%, so these questions do rule
  out cohorts of multi-cohort trials.
- This matches section 1: the LLM's P(answered) ranks facts worse than the name model, so swapping it in cannot
  close much of the gap to the oracle (0.910 at k=30). Better answerability is still the largest lever, but
  zero-shot from names and meanings alone does not deliver it.
- Possible next steps (not done): blend the LLM and name-model probabilities (for example, the LLM as a feature
  in the logistic model, fit on dev with patient cross-fitting), or calibrate the LLM's scale. Either needs a
  dev decision first, and v2 is not frozen.

## Reproduce

```bash
uv run python scripts/precompute_llm_answerability.py --split dev --limit 0 --confirmed   # cached: free on rerun
uv run python scripts/eval_llm_answerability.py --key gpt5_oracle
uv run python scripts/eval_llm_answerability.py --key gpt5mini
uv run python -m smt_trial_matching.experiment --config configs/llm_answerability_dev.yaml
uv run python -m smt_trial_matching.experiment --config configs/llm_answerability_dev.yaml --run-id llm_answerability_dev_vs_greedy --reference greedy_smt
```

The harness runs make no LLM calls. They read the prediction store
`runs/llm_answerability/gemini-3.1-flash-lite__a1.jsonl` (gitignored, like all run output).
