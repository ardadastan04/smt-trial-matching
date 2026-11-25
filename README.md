# Conversational clinical-trial matching with SMT state (CS224V)

Our CS224V project, built on the trial-matching package the CA shared. The CA's README follows unchanged below
the setup section. See `CLAUDE.md` for project rules.

## Results so far (dev split)

**Dev only:** 28 patients, 188 patient–trial pairs. Budget 30 questions, no early stopping, seed 0, solver and
answer-key simulator. Only policy-v1 has been run on test (see "Results: policy-v1" below). The v2 variants are not
frozen. Main answer key: `gpt5_oracle`.

| Policy | k=5 | k=10 | k=20 | k=30 | Accuracy AUC | Answerability AUC | Useful & answered | Not useful | Questions / patient |
|---|---|---|---|---|---|---|---|---|---|
| no_questions | 0.532† | 0.532† | 0.532† | 0.532† | 0.532† | – | – | – | 0 |
| greedy_smt (CA baseline) | 0.564 | 0.564† | 0.612† | 0.691† | 0.599† | – | 46.0% | 0.0% | 28.0 |
| **policy-v1** (`answerable_informative`, name model) | **0.622** | **0.670** | **0.745** | **0.793** | **0.700** | **0.748** | **51.1%** | **3.4%** | 26.4 |
| v2-A: Gemini zero-shot P(answered) (`answerable_informative_llm`) | 0.617 | 0.681 | 0.729 | 0.777 | 0.694 | 0.717 | 50.2% | 7.7% | 26.5 |
| v2-B: Gemini embeddings + v1's word features (`answerable_informative_emb`) | 0.628 | 0.670 | 0.718 | 0.787 | 0.687 | 0.766† | 53.4% | 3.8% | 26.4 |
| *Ablations (dev) of policy-v1:* | | | | | | | | | |
| v1 without answerability (P(answered) = 1; `..._no_answerability`) | 0.628 | 0.670 | 0.723 | 0.793 | 0.695 | – | 41.3% | 2.0% | 27.4 |
| v1 without value weighting (answerability only; `..._no_value`) | 0.612 | 0.633 | 0.665† | 0.718† | 0.649† | 0.748 | 59.3% | 8.2% | 26.1 |
| *Answerability oracle (reads the key; a reference)* | *0.665†* | *0.739†* | *0.862†* | *0.910†* | *0.783†* | *1.000* | *93.8%* | *6.2%* | *20.2* |
| *Full answer key (no budget; ceiling)* | | | | 0.957 | | | | | |

- Accuracy is pair-level, with undetermined counted as eligible. Accuracy AUC is the mean accuracy over k = 0..30.
  Answerability AUC is the held-out AUC of P(answered): answered vs unknown, each dev patient scored by a model that
  did not see them.
- **†** = significantly different from policy-v1 (paired bootstrap over patients, 95% CI excludes 0). Accuracy uses
  2,000 resamples; answerability AUC uses the same patient bootstrap. Everything unmarked is within noise of v1.
- Useful & answered / not useful: shares of all questions asked. Useful = the answer could change the trial's
  status (the CA's rule). Not useful = could not change it (these still rule out a cohort of a multi-cohort trial).
- **gpt5mini key (robustness),** k=30 / accuracy AUC: no_questions 0.532† / 0.532†, greedy 0.612† / 0.580,
  v1 0.734 / 0.651, v2-A 0.723 / 0.673, v2-B 0.729 / 0.652, oracle 0.771 / 0.684. Answerability AUC: v1 0.755,
  v2-A 0.694† (worse), v2-B 0.775† (better).
- **Ablations** (`configs/ablations_dev.yaml`, `docs/results/ablations_dev.md`): removing answerability changes
  nothing (AUC −0.005, p = .78); removing value weighting costs about 5 points (AUC −0.051, p = .027). On `gpt5mini`
  neither ablation differs from v1 (both −0.01 AUC, n.s.). Dev only; not run on test.
- An embeddings-only variant of v2-B (`answerable_informative_emb_only`) is slightly worse than v1 (accuracy AUC
  0.681, −0.020, p = .049).

**Takeaway:** v1 beats greedy by about 0.10 accuracy AUC. Neither LLM variant beats v1 on accuracy. v2-B predicts
answerability significantly better (+0.02 AUC) but that does not move accuracy. v2-A asks twice as many useless
questions. The oracle shows better answerability is still worth up to +0.12 at k=30. Details:
`docs/results/v2_llm_answerability_dev.md`, `docs/results/v2_embeddings_dev.md`, `docs/tuning/v1_dev_grid.md`.

## Run the demo

The demo is a local web page that runs the real agent live, next to the greedy SMT baseline. It uses the solver
and the answer-key simulator only, so it needs **no API key and no `.env`**, and it costs nothing to run.

**1. Install the prerequisites (once).** You need git and [uv](https://docs.astral.sh/uv/). uv installs
Python 3.11+ for you.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh     # macOS / Linux; or: brew install uv
```

**2. Get the code and install the dependencies (once).**

```bash
git clone https://github.com/ardadastan04/smt-trial-matching.git
cd smt-trial-matching
uv sync
```

**3. Start the server.**

```bash
uv run python demo/server.py                       # default patient trec-202139, port 8000
uv run python demo/server.py --qid trec-202161 --port 8010   # another dev patient / port
```

**4. Open http://localhost:8000** in a browser. Stop the server with `Ctrl+C`.

**What you can do on the page:**
- **Simulated patient:** pick a dev patient. Ours (answerable-informative) and greedy SMT ask questions side by
  side and the answer key answers. Press **Step**, or **Autoplay** with the speed slider.
- **You are the patient:** our agent asks you. Answer Yes, No, Not sure or a number. The "note says: …" hint shows
  the answer key's value so you can stay consistent with the patient note.
- Panels show the conversation, each trial's Z3 status (inclusion / exclusion per cohort, verdict, gold label),
  **why this question** was chosen (P(answered) × value for ours), and the **solver trace** for each answer.
- **How it works** opens a 5-step tour. Keys: `Space` step, `a` autoplay, `r` reset, `h` tour, `c` captions.

Only **dev patients** are available (the server refuses test patients), and the server listens on 127.0.0.1 only,
because the page shows TREC patient notes. `demo/README.md` has panel details and a 1-minute video script.

**Troubleshooting**
- `Address already in use`: another program uses port 8000. Add `--port 8010` and open http://localhost:8010.
- `No module named 'smt_trial_matching'` on macOS: see the note under Setup below.

**Terminal version (no browser).** `scripts/demo_conversation.py` prints one patient's conversation turn by turn:

```bash
uv run python scripts/demo_conversation.py --qid trec-202139 \
  --policy smt_trial_matching.policies:answerable_informative --budget 10
uv run python scripts/demo_conversation.py --qid trec-202139 --policy greedy_smt --budget 10
```

## Setup

```bash
uv sync                                   # installs z3-solver and the LLM client deps
uv run pytest                             # includes a turn-by-turn check against the CA's greedy_smt log
uv run python baselines/run_baselines.py greedy_smt --budget 30 --out logs/greedy_smt.jsonl
uv run python eval/evaluate.py logs/greedy_smt.jsonl --split dev
```

If `uv run` fails with `No module named 'smt_trial_matching'` on macOS, the repo is under iCloud-synced
`~/Documents` and macOS has hidden the venv's `.pth` file; run with `PYTHONPATH=src:. uv run --no-sync ...`
(or `chflags nohidden .venv/lib/python3.*/site-packages/*.pth`).

The CA's reference episode logs live in `logs/reference/` (the README below says `logs/`). For LLM work, copy
`.env.example` to `.env` and fill in the key; every call goes through `src/smt_trial_matching/llm.py`.

### Experiment harness (`src/smt_trial_matching/experiment.py`)

One command runs any set of policies on a split with the CA's runner and answer-key simulator (solver only, no
API cost) and reports accuracy at every budget k = 0..30 with patient-bootstrap CIs, plus paired tests against a
reference policy:

```bash
uv run python -m smt_trial_matching.experiment \
  --policies no_questions,random_stop,greedy_smt --reference greedy_smt \
  --split dev --budget 30 --run-id harness_demo_dev
uv run python -m smt_trial_matching.experiment --config configs/main_dev.yaml      # same, from a config file
```

- **Configs** (`configs/*.yaml`): policies, reference, split, budget, keys, run_id; command-line flags override
  the file. `main_dev` / `ablations_dev` are the dev runs; `main_test` / `ablations_test` are the same on test
  and still need `--confirmed` on the command line (only after the project lead's OK).
- **Policies:** CA names from `baselines/policies.py`, or `module.path:function`, or `path/to/file.py:function`
  (e.g. `src/smt_trial_matching/policies.py:answerable_informative`), all with the signature `(states, asked, rng)`.
  New policies go in our own code; `baselines/` stays untouched.
- **Answer keys:** `--keys gpt5_oracle,gpt5mini` runs every policy against both simulators (default
  `gpt5_oracle`). `gpt5mini` is a noisier reading of the same notes. Tests compare within a key.
- **Output** in `runs/<run_id>/` (not committed): `config.json`; per key `<key>/<policy>.jsonl` (CA log format,
  plus each turn's policy score; reused on rerun unless `--force`), `<key>/replays/<policy>/<qid>.json` (one
  patient's conversation turn by turn, see below), `<key>/accuracy_vs_budget.png`, `<key>/answered_vs_budget.png`; and
  `curves.csv` (per key, policy and k: accuracy, F1, informative rate, answered rate, set F1, questions and
  answered questions per patient, waste shares, each with a CI; plus `accuracy_auc`), `tests.csv`,
  `questions.csv` (every question with the variable's meaning, the answer and its label),
  `waste_breakdown.png`, `summary.md`.
- **Waste breakdown:** each question is `useful_answered` (could change a trial's status and got an answer),
  `useful_unanswered` (could, but the answer was unknown) or `not_useful` (could not change any status). An
  unknown answer never changes a status, so only the first kind can move a verdict. Two usefulness rules are
  reported side by side: the CA's (`informative()`: the *trial's* status could change) and ours, a superset
  (`replay.cohort_useful`: the status of any *open cohort* of an undetermined trial could change), which also
  counts questions that rule out one cohort of a multi-cohort trial, as `answerable_informative` asks on purpose.
  `questions.csv` has both (`label`, `label_cohort`); plots `waste_breakdown.png` and `waste_breakdown_cohort.png`.
- **AUC:** area under accuracy vs k over k = 0..budget divided by the budget, i.e. average accuracy across
  budgets (0–1). One number per policy, with a CI and a paired test.
- **Tests vs the reference** at k = 5, 10, 20, 30, final and on the AUC: paired bootstrap over patients on the
  accuracy (and set-F1) difference (primary, since pairs within a patient are not independent) and exact McNemar
  on pairs (secondary).
- **Oracle references** (read the answer key; references, not methods, and not ceilings):
  - `oracle_answerable_greedy`, the *answerable-greedy oracle*: `greedy_smt` restricted to questions the key can
    answer. It keeps greedy's scoring, so it does not bound other policies: `answerable_informative` (no key)
    already beats it on dev AUC (0.700 vs 0.686).
  - `answerable_informative_oracle`: `answerable_informative` with P(answered) replaced by the key's truth (1 or
    0); P(true) and the age distribution still come from the model. Shows how much better answerability
    prediction could make our policy.

  Ordinary policies never receive the key; a policy only gets it by declaring a `for_patient(qid, sim)` hook
  (see `src/smt_trial_matching/policies.py`), which marks it as an oracle.
- Accuracy at k = 0, 5, 10, 20, 30 matches `eval/evaluate.py` exactly (`tests/test_experiment.py`).
- `--split test` is refused without `--confirmed`. Other flags: `--key`, `--budget`, `--limit N`, `--workers`.

### Answerable-informative policy (`smt_trial_matching.policies:answerable_informative`)

Each turn, scores every unanswered variable of every open cohort of every undetermined trial as
P(answered) × expected value of the answer (1 if it would make the trial ineligible, 1.0 × share of open
cohorts it would rule out, 0.2 if it would make the trial certainly eligible; weights in `AnswerableConfig`).
A number with values from at least 5 training patients (only age today) is scored the same way, averaged over
those observed values, so an 18–65 range is worth only the share of patients outside it. Other numbers get a
flat 0.3. P(answered) and P(true) come from `answerability.py`, a logistic regression on
variable-name features fit on the dev answer key only. Dev patients get a model fit on the other 4 of 5
patient folds, so dev numbers are not in-sample. Uses the full budget; stops only when no question has value.

```bash
uv run python -m smt_trial_matching.answerability     # held-out vs in-sample AUC on dev
uv run python -m smt_trial_matching.experiment --policies no_questions,greedy_smt,\
smt_trial_matching.policies:answerable_informative,smt_trial_matching.policies:oracle_answerable_greedy \
  --reference greedy_smt --split dev --run-id answerable_dev
```

**Ablations** (`AnswerableConfig` switches; defaults reproduce the policy exactly, `tests/test_ablations.py`):

| policy | switch | what is left |
|---|---|---|
| `answerable_informative_no_answerability` | `use_answerability=False` | P(answered) = 1: informativeness × value only |
| `answerable_informative_no_value` | `use_value=False` | value = 1 if some answer could decide something, else 0: answerability only |

Tie-breaks use the same P(answered) as the score, so the first ablation cannot get answerability back through
ties. Run both with `--config configs/ablations_dev.yaml` (reference: `answerable_informative`).

### Results: policy-v1 (frozen Nov 22 at `ede13d9`)

`answerable_informative` was tuned on dev only (`docs/tuning/v1_dev_grid.md`: a 27-setting grid found nothing better
than the defaults beyond noise), frozen, then run **once** on test (`docs/results/policy_v1_test.md`, which has the
full harness summary). Budget 30 questions per patient, `gpt5_oracle` key, solver only. Test patients use the
answerability model fit on all of dev; dev patients use the cross-fitted fold models.

| Policy | Dev k=10 | Dev k=30 | Dev AUC | **Test k=10** | **Test k=30** | **Test AUC** |
|---|---|---|---|---|---|---|
| no_questions | 0.532 | 0.532 | 0.532 | 0.514 | 0.514 | 0.514 |
| random_stop | – | – | – | 0.554 | 0.646 | 0.580 |
| greedy_smt (CA baseline) | 0.564 | 0.691 | 0.600 | 0.594 | 0.646 | 0.599 |
| **answerable_informative (policy-v1)** | **0.670** | **0.793** | **0.699** | **0.640** | **0.760** | **0.663** |
| oracle_answerable_greedy (reads the key) | 0.649 | 0.803 | 0.686 | 0.669 | 0.749 | 0.672 |
| answerable_informative_oracle (reads the key) | – | – | – | 0.737 | 0.857 | 0.756 |
| ask_all (full information, no budget) | – | 0.96 | – | – | 0.96 | – |

Test, policy-v1 minus greedy_smt (paired bootstrap over patients, 95% CI):
- k=30: **+0.114 [+0.01, +0.22], p = .034** (McNemar 23 vs 3 pairs, p < .001). Significant.
- k=10: +0.046 [−0.03, +0.13]; AUC: +0.064 [−0.01, +0.14], p = .091. Positive, not significant.
- `gpt5mini` key: k=30 +0.103 [+0.02, +0.17], p = .023; AUC +0.045, not significant.
- Useful and answered questions: 51% (ours) vs 43% (greedy), at 21.6 vs 20.8 questions per patient.

The dev AUC gap (+0.10) shrank on test (+0.06). The answerability oracle (+0.16 AUC over greedy on test) shows that
better P(answered) prediction is the largest remaining lever (v2). The oracles read the answer key, so they are
references, not methods or ceilings.

### LLM answerability, v2 version A (`src/smt_trial_matching/llm_answerability.py`)

Zero-shot Gemini estimates of P(answered) and P(true) per variable, from the variable's name, type and meaning only
(never a patient note), as an alternative to the name model. The LLM is called once per unique variable by a
precompute script (through `llm.py`: cost log, disk cache, `MAX_RUN_USD`); policy runs only read the resulting store
(`runs/llm_answerability/<model>__a1.jsonl`) and make no calls. Numbers keep the name model's age distribution;
variables missing from the store fall back to the name model. Policy: `answerable_informative_llm`
(`AnswerableConfig(answerability="llm")`); policy-v1 is unchanged.

```bash
uv run python scripts/precompute_llm_answerability.py --estimate               # calls / tokens / USD, no key
uv run python scripts/precompute_llm_answerability.py --split dev --limit 5    # first 5 dev patients
uv run python scripts/precompute_llm_answerability.py --split dev --confirmed  # all dev (~214 calls, ~$0.25)
uv run python scripts/eval_llm_answerability.py                                # AUC vs cross-fitted name model
uv run python -m smt_trial_matching.experiment --config configs/llm_answerability_dev.yaml
```

### LLM answerability, v2 version B (`src/smt_trial_matching/llm_embeddings.py`)

Each variable's name, type and meaning is embedded once with `gemini-embedding-001` (768 dimensions, through
`LLMClient.embed`), and the embedding is a feature of the name model's two logistic regressions, next to its word
features. Same dev labels and 5 patient folds; C and scale chosen on dev by held-out AUC. Policy:
`answerable_informative_emb`.

```bash
uv run python scripts/precompute_embeddings.py --split dev --limit 0 --confirmed   # all dev, ~$0.03
uv run python scripts/grid_emb_auc.py                                              # settings, no calls
uv run python -m smt_trial_matching.experiment --config configs/llm_answerability_b_dev.yaml
```

### Answerability diagnostics (`src/smt_trial_matching/diagnostics.py`)

Why the no-answerability ablation costs so little. Along `answerable_informative`'s conversations (and along
each variant's own), every turn's candidates are scored three ways: predicted P(answered), P = 1, and the key's
truth. Reports AUC and calibration of P(answered) on all key variables, on the candidates the policy weighs, on
the questions it asks and within a turn; how often each weighting's choice is answered and its realized value;
and answer rates by question type. Dev only.

```bash
uv run python -m smt_trial_matching.diagnostics --run-id answerability_diag_dev   # ~5 min, both keys
```

Dev results (28 patients, key `gpt5_oracle`; `gpt5mini` in brackets):

- **Calibration is good, ranking is moderate.** On the questions the policy actually asks, mean predicted
  P(answered) is 0.58 vs 52% observed (ECE 0.10; on all weighed candidates 0.044). AUC 0.68 on asked questions,
  0.71 within a single turn's candidates. With `gpt5mini` the model (fit on `gpt5_oracle`) under-predicts:
  0.42 vs 62% on all key variables, AUC 0.71.
- **How often each weighting's choice gets answered**, on the same state along the policy's conversations:
  predicted P(answered) 52% [70%], P = 1 26% [40%], true answerability 98% [98%]. Predicted P changes the choice
  on 91% of turns.
- **Why the no-answerability ablation still keeps up:** driving its own conversation it gets 11.6 answers per
  patient vs 13.9 for the policy (4.0 vs 6.2 in turns 1–10, then 3.3 vs 2.9 in turns 21–30), and realized value
  6.35 vs 6.82 (−7%). True answerability gets 20.2 answers and 9.16 value: the headroom is ranking, which a
  name-only model lacks.

### Replays, demo and failure sample

```bash
# one patient's conversation, live or from a harness replay
uv run python scripts/demo_conversation.py --qid trec-202112 --policy smt_trial_matching.policies:answerable_informative
uv run python scripts/demo_conversation.py --replay runs/main_dev/gpt5_oracle/replays/answerable_informative/trec-202112.json
# failure-analysis sample (seed 0) -> runs/main_dev/failure_sample.md
uv run python scripts/failure_sample.py main_dev
```

A replay (`src/smt_trial_matching/replay.py`) holds the patient note, each trial's title and gold label, and per
turn the question (variable and meaning), the policy's score, the answer, the waste label, and every trial's
status and verdict after the turn. `failure_sample.md` lists 15 random useful-but-unanswered questions each for
`greedy_smt` and `answerable_informative`, and every pair where exactly one of the two is right at k = 30, with the
trial's criteria line that mentions the variable (keyword match) and a blank `Category:` line per item.

### Demo UI (`demo/`)

See [Run the demo](#run-the-demo) at the top of this file.

---

A self-contained student project. An agent talks with a patient and asks questions, keeping everything it learns as
**solver state over each trial's formal eligibility program**. The goal is to decide which of the patient's candidate
trials they are eligible for, accurately and with few questions.

The data are 363 patient–trial pairs from the TREC 2021 Clinical Trials track (57 patients, 263 trials). The package
includes trial criteria, compiled SMT-LIB programs, variable dictionaries, gold labels, answer keys, a state library, a
patient simulator, baselines, and an evaluator. Python ≥ 3.9 and `pip install z3-solver` are the only requirements.

## 1. The task

Each patient (a TREC topic) has 1–23 candidate trials (6.4 on average); 190 pairs are eligible and 173 ineligible.

The conversation works like this:
- At each turn the agent either asks about one patient fact or stops.
- The patient answers true, false, a number, or **unknown** ("I don't know"; the fact is not in their record).
- When the agent stops, it gives a verdict (eligible or ineligible) for every candidate trial.

Two settings:
- **Single-trial:** one patient and one trial (call the runner with a single NCT id).
- **Multi-trial ("find the right trials"):** one conversation per patient covers all of their candidate trials. This
  is the main setting.

## 2. What is in the package

| Path | Contents |
|---|---|
| `data/pairs.jsonl` | 363 pairs: `pair`, `qid` (patient), `nct` (trial), `gold` (eligible / ineligible), `trec_qrel` (2 / 1) |
| `data/patients.jsonl` | 57 patient notes (`qid`, `text`). The simulator's source of truth; do not show the note to your agent |
| `data/trials/<NCT>.json` | Title, conditions, phase, summary, inclusion and exclusion criteria text, cohort ids |
| `data/programs/<NCT><cohort>_<side>_program.smt2` | 695 SMT-LIB programs, one per trial × cohort × side (inclusion / exclusion) |
| `data/variables/<NCT>.json` | **Variable dictionary** per trial (see below) |
| `data/answer_keys/gpt5_oracle.jsonl` | Per pair, the value of every variable as read from the full note by GPT-5 (unknown = null) |
| `data/answer_keys/gpt5mini.jsonl` | The same, read by GPT-5-mini |
| `data/splits.json` | Patient split: `dev` (28 patients, 188 pairs) and `test` (29 patients, 175 pairs) |
| `smtstate/` | State library (`state.py`), simulator (`sim.py`), conversation runner (`runner.py`) |
| `baselines/` | Baseline policies and the script that runs them |
| `eval/evaluate.py` | Metrics |
| `logs/` | Episode logs of every baseline, for reference |
| `docs/` | Prompts for a natural-language patient simulator and for the LLM-only baseline |

### Variable dictionary

Each entry in `data/variables/<NCT>.json` has:
- `name` and `type` (`Bool`, `Real`, `Int`);
- `side` (inclusion / exclusion);
- `meaning`;
- `when_true`, `when_false`, `when_unknown` (or `when_value` for numbers);
- `polarity`, e.g. "criterion met when true".

Variable names follow a canonical scheme, such as `patient_has_diagnosis_of_<concept>_<timeframe>` with timeframes
`now`, `inthehistory`, `inthepastNmonths` and so on. Qualifiers are attached as `<stem>@@<qualifier>`. Names are
**trial-specific**: two trials may use the same name, and a variable is always answered within the trial that declares it.

### Labels

- **Gold labels** are the official TREC 2021 qrels: 2 → eligible, 1 → ineligible.
- **Why these 363 pairs:** they are the pairs of the TREC 2021 test split on which the compiled programs can reach the
  gold label. Fully informed by the GPT-5 answer key, the programs reproduce the gold label on 348 of 363 pairs
  (0.959). So **0.959 is the ceiling** for any agent that relies on the programs and this answer key. Errors below
  it come from the conversation, not from the programs.

## 3. SMT state (`smtstate/state.py`)

- **Programs:** a program is **satisfiable exactly when the patient is eligible**. Exclusion criteria are written as
  negations inside the exclusion program.
- **State:** the state is a partial assignment of patient variables (the answers so far). Unknowns are left free.
- **Three-valued status per program side:**
  - `violated`: the answers already falsify a criterion (UNSAT);
  - `satisfied`: every way of filling the unknowns satisfies all criteria;
  - `open`: otherwise.

  Definitional links named `AUXILIARY`, such as `qualifier ⇒ stem`, are background constraints, not criteria.
- **Cohort status:** ELIGIBLE if both sides are satisfied, INELIGIBLE if either is violated, otherwise OPEN.
- **Trial status:** ELIGIBLE if any cohort is eligible, INELIGIBLE if all are, otherwise UNDETERMINED.
- `TrialState.informative()` lists the unanswered variables whose answer could change the trial's status, with the
  status each answer would give. These are the questions worth asking.
- `TrialState.verdict()` is the final decision when the agent stops: UNDETERMINED counts as **eligible**, since
  unknown facts do not disqualify. This matches the VERDICT paper's rule.

```python
from smtstate import TrialState
s = TrialState('NCT04772456')            # empty state
s.status()                                # 'undetermined'
s.informative()[:3]                       # [(var, {True: status, False: status}), ...]
s.answers['patient_is_pregnant_now'] = False
s.verdict()
```

## 4. Patient simulators

- **Answer-key simulator (default; deterministic; no API):** `smtstate/sim.py`. A question about a variable returns
  that variable's value from `data/answer_keys/gpt5_oracle.jsonl`, or `None` ("unknown"). About two thirds of the
  values in a typical program are unknown, because notes do not mention them.
- **Natural-language simulator (extension):** an LLM role-plays the patient from the note and answers free-text
  questions. Your agent must then map each answer onto variables. See `docs/nl_simulator_prompt.md`. Keep the
  simulator model fixed across the systems you compare.

## 5. Evaluation

Run your policy with `smtstate/runner.py` (or log your own episodes in the same format), then:

```bash
python eval/evaluate.py logs/<run>.jsonl --split dev    # develop on dev
python eval/evaluate.py logs/<run>.jsonl --split test   # report test once, at the end
```

Metrics:
- **Pair-level verdict quality:** accuracy, and precision / recall / F1 with *eligible* as the positive class.
- **Cost:** questions per patient (mean and median) and per pair.
- **Accuracy at budget k** (k = 0, 5, 10, 20, 30): the verdicts the agent would give after k questions. Report this
  curve. It is the main way to compare policies with different stopping behavior.
- **Informative-question rate:** the share of questions that could change some trial's status when asked.
- **Patient-level eligible-set metrics:** precision, recall, F1 of the predicted set of eligible trials per patient,
  and exact match. This is the "find the right trials" view.

**Episode log format** (one JSON object per patient):
```json
{"qid": "...", "trials": ["NCT..."], "initial_verdicts": {"NCT...": "eligible"},
 "turns": [{"nct": "NCT...", "var": "...", "answer": true, "informative": true, "verdicts": {"NCT...": "eligible"}}],
 "final_verdicts": {"NCT...": "eligible"}, "final_status": {"NCT...": "undetermined"}}
```
`verdicts` in each turn are the verdicts after that turn. For free-text agents, `var` can be the question text;
`informative` is then optional.

**Good practice:**
- Choose methods on `dev` and report `test` once.
- Report questions and accuracy together; neither is meaningful alone.
- State which simulator and answer key you used.
- For LLM-based agents, report model, prompt and cost.

## 6. Baselines (`baselines/`)

```bash
python baselines/run_baselines.py greedy_smt --budget 30      # writes logs/greedy_smt_gpt5_oracle.jsonl
python baselines/run_baselines.py read_note --key gpt5mini    # no conversation: every value at once
```

| Baseline | What it does |
|---|---|
| `no_questions` | Stop immediately; every trial is eligible by the default rule |
| `random_stop` | Random unanswered variable of an undetermined trial; stop when all trials are determined |
| `greedy_smt` | Ask an **informative** variable, preferring answers that would decide a trial; stop when none is left |
| `ask_all` | Ask every variable of every trial (cost upper bound) |
| `read_note` | No conversation: use a whole answer key at once (`gpt5_oracle` = ceiling; `gpt5mini` = the paper's reader) |
| LLM-only conversation | An LLM asks free-text questions and decides from the criteria text, without SMT state. Prompt in `docs/llm_only_baseline_prompt.md` (needs an API) |

Reference results (answer-key simulator `gpt5_oracle`; question budget 30 per patient):

| Baseline | Split | Accuracy | F1 | Questions / patient | Accuracy @10 | Set exact match |
|---|---|---|---|---|---|---|
| no_questions | dev / test | 0.53 / 0.51 | 0.69 / 0.68 | 0 | 0.53 / 0.51 | 0.14 / 0.28 |
| random_stop | dev / test | 0.61 / 0.65 | 0.72 / 0.74 | 29.1 / 25.5 | 0.56 / 0.55 | 0.29 / 0.45 |
| greedy_smt | dev / test | 0.69 / 0.65 | 0.77 / 0.74 | 28.0 / 20.8 | 0.56 / 0.59 | 0.36 / 0.52 |
| ask_all (no budget) | dev / test | 0.96 / 0.96 | 0.96 / 0.96 | 210 / 197 | 0.59 / 0.55 | 0.71 / 0.76 |
| read_note, gpt5mini | dev / test | 0.82 / 0.85 | 0.82 / 0.84 | 0 | – | 0.36 / 0.48 |
| read_note, oracle (ceiling) | dev / test | 0.96 / 0.96 | 0.96 / 0.96 | 0 | – | 0.71 / 0.76 |

What the numbers say:
- **The headroom is large.** The best cheap policy reaches about 0.67 with 20–30 questions per patient; full
  information gives 0.96.
- **"Informative" isn't enough.** `greedy_smt` asks only informative questions, yet many answers are unknown,
  because the patient cannot answer most fine-grained criteria. Predicting which questions are *answerable* (and
  likely to decide a trial) is the main opportunity.

## 7. Suggested project directions

1. **Better question selection:** expected information gain or value of information over trial statuses, using a
   model of how likely each answer is (true / false / unknown) for this patient so far.
2. **Sharing across trials:** pick questions that settle many of the patient's trials at once (shared concepts,
   SNOMED-like hierarchy, similar variable names).
3. **Stopping and ranking:** decide when to stop and present a ranked list of likely-eligible trials with confidence;
   evaluate set F1 and accuracy at budget.
4. **Natural-language conversations:** generate patient-friendly questions, map free-text answers to variables, and
   measure the mapping error separately.
5. **SMT state versus LLM-only:** compare against the LLM-only conversation baseline at equal question budgets; also
   report what the SMT state adds in explanations (which criterion decided each verdict).
6. **Robustness:** noisy or contradictory answers, patients who answer "unknown" more often, and the `gpt5mini` key
   as a noisier simulator.

## 8. Notes and caveats

- These 363 pairs are those where the programs can reach the gold label, so they measure the *conversation and
  reading* layer, not program quality. Do not compare absolute numbers with end-to-end matching results on the full
  TREC 2021 test split.
- Gold labels come from TREC assessors and contain some noise.
- The answer key is a model's reading of the note, not a human annotation.
- **Sources:** patient topics and qrels are from the TREC 2021 Clinical Trials track (NIST); trial criteria are from
  ClinicalTrials.gov. Programs were compiled from the criteria by the SatIR trial compiler. Follow the TREC terms when
  sharing the data.
