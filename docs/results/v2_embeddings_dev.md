# v2 version B: Gemini embeddings in v1's answerability model, dev results (2026-11-23)

**Dev only. v2 is not frozen and the test split was not touched.** policy-v1 stays frozen at `ede13d9`.
Version A results: `docs/results/v2_llm_answerability_dev.md`.

## What was built and run

- Each variable's text (readable name, type and the CA's plain-language meaning, the same text version A
  shows the LLM) is embedded once with `gemini-embedding-001` at 768 dimensions. Patient notes are never
  embedded or read. All 4,264 dev variables were embedded in 44 requests for $0.029, through the new
  `LLMClient.embed` in `llm.py` (disk cache, cost log, budget guard). The whole `llm_answerability` run, A and
  B together, has spent $0.29.
- The embedding (unit norm, times a scale) is a feature of v1's two logistic regressions (answered vs unknown,
  true vs false). It is used either next to v1's word features (`name_emb`, policy `answerable_informative_emb`)
  or alone (`emb`, policy `answerable_informative_emb_only`). Same dev labels (gpt5_oracle key) and the same
  5 folds by patient as v1, so each dev patient is scored by a model that never saw that patient.
- Settings were chosen on dev by held-out P(answered) AUC on the gpt5_oracle key, as v1's C was
  (`scripts/grid_emb_auc.py`, 5 values of C x 1-3 scales): `name_emb` C 0.1, scale 3; `emb` C 1.0.
- Policy: the frozen v1 scoring with only the answerability model swapped. Budget 30, no early stopping,
  seed 0, both answer keys, 95% CIs from a paired bootstrap over the 28 dev patients (2,000 resamples).

## 1. Answerability prediction (held-out AUC)

Same 5,024 / 5,123 dev entries as version A's table. Δ = minus v1's name model, paired patient-bootstrap 95% CI.

| key | v1 name | A: Gemini zero-shot | B: emb + words | Δ B − v1 | B: emb only | Δ |
|---|---|---|---|---|---|---|
| P(answered), gpt5_oracle | 0.748 | 0.717 | **0.766** | +0.018 [+0.007, +0.032] | 0.753 | +0.005 [-0.014, +0.026] |
| P(answered), gpt5mini | 0.755 | 0.694 | **0.775** | +0.021 [+0.013, +0.029] | 0.775 | +0.021 [+0.008, +0.035] |
| P(true), gpt5_oracle | 0.682 | 0.712 | 0.691 | +0.009 [-0.005, +0.028] | 0.664 | -0.018 [-0.048, +0.015] |
| P(true), gpt5mini | 0.675 | 0.690 | 0.684 | +0.009 [-0.006, +0.028] | 0.649 | -0.026 [-0.057, +0.012] |

Version B is the first answerability model that is **significantly better than v1's** at predicting which
questions get answered, on both keys. The gain is small: about +0.02 AUC, against a 0.910 vs 0.793 accuracy gap
between the answerability oracle and v1. (The gpt5_oracle row is where its settings were chosen, so that row is
slightly optimistic. The gpt5mini row was not used to choose anything.)

## 2. Dev accuracy vs question budget

### Key gpt5_oracle (primary)

| policy | k=5 | k=10 | k=20 | k=30 | AUC (k=0..30) | questions / patient | CA not-useful share |
|---|---|---|---|---|---|---|---|
| greedy_smt | 0.564 | 0.564 | 0.612 | 0.691 | 0.599 | 28.0 | 0.000 |
| v1 (name model) | 0.622 | 0.670 | 0.745 | **0.793** | **0.700** | 26.4 | 0.034 |
| A (Gemini zero-shot) | 0.617 | 0.681 | 0.729 | 0.777 | 0.694 | 26.5 | 0.077 |
| B (emb + words) | 0.628 | 0.670 | 0.718 | 0.787 | 0.687 | 26.4 | 0.038 |
| B (emb only) | 0.622 | 0.660 | 0.718 | 0.771 | 0.681 | 26.1 | 0.033 |
| answerability oracle | 0.665 | 0.739 | 0.862 | 0.910 | 0.783 | 20.2 | 0.062 |

### Key gpt5mini (robustness)

| policy | k=5 | k=10 | k=20 | k=30 | AUC | questions / patient | CA not-useful share |
|---|---|---|---|---|---|---|---|
| greedy_smt | 0.564 | 0.569 | 0.590 | 0.612 | 0.580 | 27.9 | 0.000 |
| v1 (name model) | 0.601 | 0.617 | 0.686 | 0.734 | 0.651 | 26.1 | 0.034 |
| A (Gemini zero-shot) | 0.622 | 0.654 | 0.713 | 0.723 | 0.673 | 25.5 | 0.072 |
| B (emb + words) | 0.612 | 0.628 | 0.681 | 0.729 | 0.652 | 25.9 | 0.039 |
| B (emb only) | 0.622 | 0.644 | 0.654 | 0.713 | 0.643 | 26.2 | 0.038 |
| answerability oracle | 0.622 | 0.660 | 0.718 | 0.771 | 0.684 | 22.2 | 0.055 |

### Paired differences (accuracy, [95% CI], p)

| key | comparison | k=5 | k=10 | k=20 | k=30 | AUC |
|---|---|---|---|---|---|---|
| gpt5_oracle | B (emb + words) − v1 | +0.005 [-0.02, +0.03] | +0.000 [-0.02, +0.02] | -0.027 [-0.06, +0.01] | -0.005 [-0.04, +0.03], p .89 | -0.013 [-0.03, +0.00], p .15 |
| gpt5_oracle | B (emb only) − v1 | +0.000 [-0.03, +0.03] | -0.011 [-0.04, +0.02] | -0.027 [-0.06, +0.00] | -0.021 [-0.08, +0.02], p .49 | -0.020 [-0.04, -0.00], p .049 |
| gpt5_oracle | B (emb + words) − greedy | +0.064 [+0.00, +0.14] | +0.106 [+0.02, +0.20] | +0.106 [+0.03, +0.19] | +0.096 [+0.01, +0.19], p .049 | +0.088 [+0.02, +0.16], p .005 |
| gpt5mini | B (emb + words) − v1 | +0.011 [-0.03, +0.05] | +0.011 [-0.02, +0.04] | -0.005 [-0.05, +0.04] | -0.005 [-0.03, +0.02], p .85 | +0.001 [-0.02, +0.02], p .94 |
| gpt5mini | B (emb only) − v1 | +0.021 [-0.01, +0.06] | +0.027 [-0.01, +0.07] | -0.032 [-0.08, +0.01] | -0.021 [-0.06, +0.02], p .34 | -0.009 [-0.03, +0.02], p .51 |
| gpt5mini | B (emb + words) − greedy | +0.048 [-0.03, +0.13] | +0.059 [-0.03, +0.15] | +0.090 [-0.01, +0.19] | +0.117 [+0.02, +0.22], p .025 | +0.073 [+0.00, +0.15], p .045 |

(Version A vs v1 and greedy: unchanged from the version A doc.)

## Reading

- **Better answerability, same accuracy.** B ranks answerable questions measurably better than v1 (+0.02 AUC,
  CI above zero on both keys), but dev accuracy does not move. With embeddings plus words it is within 0.03 of
  v1 at every budget on both keys (AUC −0.013 on the primary key, +0.001 on gpt5mini; both CIs include zero).
  Embeddings alone are slightly worse than v1 (primary-key AUC −0.020, p .049).
- **Useless questions stay low.** B with words asks no more useless questions than v1 (3.8% vs 3.4%), unlike
  version A (7.7%). It also gets a few more questions answered (CA useful and answered 0.534 vs 0.511 per question
  on the primary key).
- Like v1, B beats greedy clearly (AUC +0.07 to +0.09 on both keys).
- So a +0.02 AUC gain in answerability is too small to show up in accuracy over 28 patients. This matches the
  earlier diagnostics (`diagnostics.py`): the policy's choices change little unless P(answered) gets much
  sharper. The oracle shows a large gap is still there (0.910 at k=30), but neither zero-shot LLM probabilities
  (A) nor embeddings of the variable text (B) close it.
- **No v2 candidate beats v1 on dev.** If one goes forward, B with words is the safer pick: it ties v1 and keeps
  useless questions low. Freeze and test stay on hold until you decide.

## Reproduce

```bash
uv run python scripts/precompute_embeddings.py --split dev --limit 0 --confirmed   # cached: free on rerun
uv run python scripts/grid_emb_auc.py
uv run python scripts/eval_llm_answerability.py --key gpt5_oracle
uv run python scripts/eval_llm_answerability.py --key gpt5mini
uv run python -m smt_trial_matching.experiment --config configs/llm_answerability_b_dev.yaml
uv run python -m smt_trial_matching.experiment --config configs/llm_answerability_b_dev.yaml --run-id llm_answerability_b_dev_vs_greedy --reference greedy_smt
```

Only the first command calls the API. The rest read the embedding store
`runs/llm_answerability/emb__gemini-embedding-001__d768.npz` (gitignored, like all run output).
