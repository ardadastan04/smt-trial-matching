# Demo UI: the agent and what it does behind the scenes

A local web page that runs the real agent live. It uses the same `TrialState` objects, policies and
answer-key simulator as the experiments, so a simulated run asks exactly the questions
`smtstate.runner.run_patient` would (checked by `tests/test_demo_engine.py`). It is solver only: no LLM and no API key.

```bash
uv run python demo/server.py              # open http://localhost:8000
uv run python demo/server.py --qid trec-202161 --port 8010
```

The page shows **dev patients only** (the server refuses test patients). It binds to 127.0.0.1 only, because the
pages show TREC patient notes.

## Modes

- **Simulated patient**: the answer key answers. Ours (answerable-informative) and the greedy SMT baseline run side
  by side on the same patient. Use Step, or Autoplay with the speed slider.
- **You are the patient**: our agent only. Answer with Yes, No, Not sure or a number. "note says: …" shows the
  answer key's value, so whoever plays the patient can stay consistent with the note.

## What each panel shows

| # | Panel | What it shows |
|---|---|---|
| 1 | Conversation | The question (plain English from `demo/phrasing.py`, raw variable underneath), the answer, and a ⚙ line with what Z3 concluded |
| 2 | Candidate trials | Each trial's status, the inclusion and exclusion program state for each cohort (satisfied / violated / open), the verdict and the gold label |
| 3 | Why this question? | Ours: top candidates with P(answered), value and score. Greedy: the trial status each answer would give, and its score |
| 4 | Solver trace | The assignment, each program side before → after, which Z3 check decided it, and the SMT-LIB assertion that mentions the variable |

The caption bar narrates each step. Turn it off with the Captions checkbox. **How it works** is a 5-step tour that
highlights each panel, good for the opening of the video.

Keys: `Space` step · `a` autoplay · `r` reset · `h` tour (←/→ to move, Esc to close) · `c` captions.

## Suggested 1-minute video (trec-202139, the default)

1. 0–15 s: the tour, steps 1–4 (programs, one fact per question, two Z3 checks, P(answered) × value).
2. 15–40 s: Step three times. Ours rules out three ineligible trials with three answered questions, while
   greedy spends its first questions on one trial ("do the parents refuse to cooperate?").
3. 40–55 s: Autoplay at the fastest speed until the end.
4. 55–60 s: the final caption. Ours is 5/5 correct after 19 questions, with every final verdict reached by
   question 3. Greedy is 4/5 after 30 questions, settled at question 29.

Other dev patients with a clear story: `trec-202161` (5 trials; ours 5/5 by question 7, greedy settles at 18)
and `trec-202132` (2 trials; ours stops after 5 questions, greedy after 24).

## Files

- `server.py`: stdlib HTTP server and JSON API (`/api/patients`, `/api/start`, `/api/ask`, `/api/answer`)
- `engine.py`: `DemoSession` / `Agent`, which split a turn into ask() and answer() and add the ranking and solver trace
- `phrasing.py`: variable name → question templates
- `static/`: `index.html`, `style.css`, `app.js` (no build step)
