"""policy-v1 dev tuning grid (Nov 22): 3 x 3 x 3 = 27 settings of answerable_informative.

Knobs (all other AnswerableConfig weights at their defaults):
  alpha            exponent on P(answered) in the score:   0.5, 1 (current), 2
  answerability_c  inverse regularisation of the model:    0.1, 0.3 (current), 1.0
  w_numeric        flat score of numbers without a value distribution (all but age): 0.1, 0.3 (current), 0.5

Selection rule, fixed before running (agreed with Arda Nov 22):
  1. Highest dev accuracy AUC over k = 0..30 on the gpt5_oracle key (dev patients use cross-fitted models).
  2. Keep the current default (a1_c0_3_n0_3) unless the winner's paired-bootstrap 95% CI for the AUC difference
     against the default excludes zero.
  3. Check the winner on the gpt5mini key (robustness only, not used to select).
Solver only, no LLM calls, dev only. Results: docs/tuning/v1_dev_grid.md.

  uv run python -m smt_trial_matching.experiment --split dev --budget 30 --run-id tune_v1_dev --workers 8 \\
    --keys gpt5_oracle,gpt5mini --reference scripts/tune_v1_grid.py:a1_c0_3_n0_3 --policies "$(uv run python \\
    scripts/tune_v1_grid.py)"
"""

from itertools import product

from smt_trial_matching.policies import AnswerableConfig, AnswerableInformative

ALPHAS = (0.5, 1.0, 2.0)
CS = (0.1, 0.3, 1.0)
W_NUMERIC = (0.1, 0.3, 0.5)


def _tag(x: float) -> str:
    return f"{x:g}".replace(".", "_")


NAMES: list[str] = []
for _a, _c, _n in product(ALPHAS, CS, W_NUMERIC):
    _name = f"a{_tag(_a)}_c{_tag(_c)}_n{_tag(_n)}"
    globals()[_name] = AnswerableInformative(AnswerableConfig(alpha=_a, answerability_c=_c, w_numeric=_n))
    NAMES.append(_name)

if __name__ == "__main__":
    print(",".join(f"scripts/tune_v1_grid.py:{n}" for n in NAMES))
