# policy-v1 dev tuning grid (Nov 22, 2026)

**What this is for:** the last tuning step before freezing `answerable_informative` as policy-v1. A 3 × 3 × 3 grid
over three knobs was run on the **dev split only** (28 patients, 188 pairs; dev patients use the cross-fitted
answerability models), solver only, no LLM calls. Test was not touched.

**Knobs** (`AnswerableConfig` in `src/smt_trial_matching/policies.py`; every other weight at its default):

| Knob | Meaning | Values tried (default in bold) |
|---|---|---|
| `alpha` | score = P(answered) ** alpha × value | 0.5, **1**, 2 |
| `answerability_c` | inverse regularisation of the two answerability logistic regressions | 0.1, **0.3**, 1.0 |
| `w_numeric` | flat score of numbers with no value distribution (everything but age) | 0.1, **0.3**, 0.5 |

**Selection rule (fixed before running, agreed with Arda):**
1. Highest dev accuracy AUC over k = 0..30 on the `gpt5_oracle` key.
2. Keep the current default unless the winner's paired-bootstrap 95% CI (2,000 patient resamples, seed 0) for the
   AUC difference against the default excludes zero.
3. Check on the `gpt5mini` key for robustness only (not used to select).

**Decision: keep the default (alpha 1, C 0.3, w_numeric 0.3).** The best setting on `gpt5_oracle`
(alpha 0.5, C 1.0, w_numeric 0.1) is +0.011 AUC, CI [−0.010, +0.035], which includes zero. `gpt5mini` agrees: no
setting differs significantly from the default. Consistent but non-significant patterns: C = 1.0 is about +1 point on
both keys, alpha = 2 is about −1 point (k=30 drops by 3–4 points), and w_numeric has no effect. Arda chose to keep the
default on Nov 22.

Reproduce (about 45 minutes, both keys): see the command in `scripts/tune_v1_grid.py`. The AUC and CI columns below
were computed with `scripts/grid_auc.py <key>` from the run's episode logs (`runs/tune_v1_dev/<key>/*.jsonl`, not committed).

## gpt5_oracle (selection key)

| Setting (alpha, C, w_numeric) | Dev AUC k=0..30 | Acc k=10 | Acc k=30 | AUC − default [95% CI] |
|---|---|---|---|---|
| 0.5, 1, 0.1 | 0.711 | 0.681 | 0.824 | +0.011 [-0.010,+0.035] |
| 0.5, 1, 0.3 | 0.710 | 0.681 | 0.824 | +0.011 [-0.012,+0.035] |
| 1, 1, 0.1 | 0.708 | 0.681 | 0.814 | +0.009 [-0.004,+0.028] |
| 1, 1, 0.3 | 0.707 | 0.681 | 0.814 | +0.008 [-0.004,+0.027] |
| 0.5, 1, 0.5 | 0.706 | 0.686 | 0.809 | +0.007 [-0.020,+0.034] |
| 1, 1, 0.5 | 0.703 | 0.670 | 0.824 | +0.004 [-0.008,+0.021] |
| 1, 0.3, 0.1 | 0.700 | 0.670 | 0.798 | +0.001 [+0.000,+0.002] |
| **1, 0.3, 0.3 (default)** | 0.699 | 0.670 | 0.793 | +0.000 [+0.000,+0.000] |
| 1, 0.3, 0.5 | 0.698 | 0.670 | 0.798 | -0.001 [-0.004,+0.001] |
| 0.5, 0.3, 0.1 | 0.696 | 0.660 | 0.809 | -0.003 [-0.025,+0.013] |
| 0.5, 0.3, 0.3 | 0.695 | 0.660 | 0.803 | -0.004 [-0.026,+0.013] |
| 0.5, 0.3, 0.5 | 0.694 | 0.665 | 0.803 | -0.005 [-0.031,+0.013] |
| 2, 1, 0.5 | 0.691 | 0.660 | 0.777 | -0.008 [-0.027,+0.009] |
| 2, 1, 0.1 | 0.691 | 0.670 | 0.766 | -0.008 [-0.027,+0.009] |
| 2, 1, 0.3 | 0.689 | 0.670 | 0.761 | -0.010 [-0.028,+0.007] |
| 2, 0.3, 0.1 | 0.689 | 0.660 | 0.761 | -0.010 [-0.026,+0.003] |
| 2, 0.3, 0.3 | 0.688 | 0.660 | 0.761 | -0.011 [-0.026,+0.002] |
| 0.5, 0.1, 0.1 | 0.688 | 0.660 | 0.787 | -0.011 [-0.038,+0.011] |
| 0.5, 0.1, 0.3 | 0.688 | 0.660 | 0.787 | -0.011 [-0.039,+0.010] |
| 2, 0.1, 0.3 | 0.687 | 0.654 | 0.766 | -0.012 [-0.028,+0.000] |
| 2, 0.1, 0.1 | 0.687 | 0.654 | 0.771 | -0.012 [-0.028,+0.000] |
| 1, 0.1, 0.1 | 0.687 | 0.670 | 0.787 | -0.012 [-0.028,+0.000] |
| 1, 0.1, 0.3 | 0.687 | 0.670 | 0.787 | -0.012 [-0.029,+0.000] |
| 2, 0.3, 0.5 | 0.687 | 0.660 | 0.761 | -0.012 [-0.028,+0.001] |
| 2, 0.1, 0.5 | 0.687 | 0.654 | 0.766 | -0.013 [-0.028,-0.000] |
| 1, 0.1, 0.5 | 0.686 | 0.670 | 0.782 | -0.013 [-0.030,-0.001] |
| 0.5, 0.1, 0.5 | 0.685 | 0.665 | 0.782 | -0.014 [-0.044,+0.009] |
| greedy_smt | 0.600 | 0.564 | 0.691 | -0.099 [-0.177,-0.032] |

## gpt5mini (robustness check)

| Setting (alpha, C, w_numeric) | Dev AUC k=0..30 | Acc k=10 | Acc k=30 | AUC − default [95% CI] |
|---|---|---|---|---|
| 1, 1, 0.3 | 0.659 | 0.606 | 0.750 | +0.009 [-0.005,+0.029] |
| 1, 1, 0.1 | 0.658 | 0.606 | 0.745 | +0.008 [-0.007,+0.027] |
| 0.5, 1, 0.3 | 0.657 | 0.617 | 0.745 | +0.006 [-0.017,+0.030] |
| 0.5, 1, 0.5 | 0.655 | 0.617 | 0.734 | +0.005 [-0.022,+0.031] |
| 0.5, 1, 0.1 | 0.655 | 0.617 | 0.745 | +0.004 [-0.018,+0.029] |
| 1, 1, 0.5 | 0.655 | 0.606 | 0.739 | +0.004 [-0.009,+0.023] |
| **1, 0.3, 0.3 (default)** | 0.651 | 0.617 | 0.734 | +0.000 [+0.000,+0.000] |
| 0.5, 0.3, 0.3 | 0.651 | 0.617 | 0.739 | +0.000 [-0.023,+0.017] |
| 0.5, 0.3, 0.5 | 0.650 | 0.622 | 0.745 | -0.001 [-0.026,+0.017] |
| 1, 0.3, 0.5 | 0.650 | 0.617 | 0.734 | -0.001 [-0.004,+0.002] |
| 1, 0.3, 0.1 | 0.650 | 0.617 | 0.734 | -0.001 [-0.004,+0.001] |
| 0.5, 0.3, 0.1 | 0.650 | 0.617 | 0.739 | -0.001 [-0.024,+0.017] |
| 2, 0.3, 0.3 | 0.649 | 0.644 | 0.707 | -0.002 [-0.015,+0.013] |
| 2, 0.3, 0.1 | 0.649 | 0.644 | 0.713 | -0.002 [-0.015,+0.012] |
| 2, 0.3, 0.5 | 0.649 | 0.644 | 0.707 | -0.002 [-0.016,+0.013] |
| 0.5, 0.1, 0.3 | 0.646 | 0.606 | 0.723 | -0.005 [-0.034,+0.020] |
| 2, 0.1, 0.3 | 0.646 | 0.628 | 0.702 | -0.005 [-0.023,+0.011] |
| 0.5, 0.1, 0.1 | 0.646 | 0.606 | 0.718 | -0.005 [-0.035,+0.019] |
| 2, 0.1, 0.5 | 0.646 | 0.628 | 0.702 | -0.005 [-0.023,+0.011] |
| 2, 1, 0.5 | 0.646 | 0.628 | 0.707 | -0.005 [-0.021,+0.014] |
| 0.5, 0.1, 0.5 | 0.646 | 0.612 | 0.729 | -0.005 [-0.036,+0.020] |
| 2, 1, 0.1 | 0.645 | 0.633 | 0.713 | -0.006 [-0.021,+0.014] |
| 2, 0.1, 0.1 | 0.645 | 0.628 | 0.691 | -0.006 [-0.024,+0.010] |
| 2, 1, 0.3 | 0.644 | 0.633 | 0.702 | -0.007 [-0.023,+0.013] |
| 1, 0.1, 0.3 | 0.641 | 0.617 | 0.729 | -0.010 [-0.029,+0.007] |
| 1, 0.1, 0.5 | 0.641 | 0.617 | 0.729 | -0.010 [-0.029,+0.006] |
| 1, 0.1, 0.1 | 0.641 | 0.617 | 0.723 | -0.010 [-0.029,+0.006] |
| greedy_smt | 0.579 | 0.569 | 0.612 | -0.072 [-0.155,+0.008] |
