"""Live conversation engine behind the demo UI (solver only, no LLM).

A ``DemoSession`` holds one patient and up to two ``Agent``s (ours and the greedy baseline). Each agent
owns its own ``TrialState`` objects and runs exactly the loop of ``smtstate.runner.run_patient``:
the policy picks ``(nct, var)``, the answer is written into that trial's answers, Z3 recomputes the
statuses. The UI drives it in two calls per turn so it can show the question before the answer:

  ask()           -> the chosen question, the ranked candidates behind the choice
  answer(value)   -> what Z3 concluded: per-side status changes, the assertions involved, new verdicts

``value`` is ``SIM`` (look it up in the answer key, the CA's simulator) or the user's own answer.
``tests/test_demo_engine.py`` checks that a simulated episode asks the same questions as run_patient.
"""

from __future__ import annotations

import json
import random
import re
import sys
from dataclasses import dataclass, field
from functools import cache
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
for p in (str(ROOT), str(ROOT / "src")):
    if p not in sys.path:
        sys.path.insert(0, p)

from baselines.policies import greedy_smt
from demo.phrasing import question_text, unit_of
from smt_trial_matching import metrics as M
from smt_trial_matching.policies import (
    AnswerableInformative,
    _answer_value,
    _greedy_score,
    _undetermined,
    candidate_questions,
    score_question,
)
from smt_trial_matching.replay import meanings, patient_note, trial
from smtstate.sim import AnswerKeySimulator
from smtstate.state import TrialState, _top_level

SIM = "__sim__"
KEY = "gpt5_oracle"
BUDGET = 30
TOP_K = 6

AGENTS = {
    "ours": "Answerable-informative (ours)",
    "greedy": "Greedy SMT (baseline)",
}

SIDE_TEXT = {
    "violated": "B ∧ A ∧ C is UNSAT: some criterion now fails",
    "satisfied": "B ∧ A ∧ ¬C is UNSAT: every way of filling the unknowns meets the criteria",
    "open": "both checks SAT: still depends on facts we don't know",
}


@cache
def _sim() -> AnswerKeySimulator:
    return AnswerKeySimulator(KEY)


@cache
def _gold() -> dict[tuple[str, str], bool]:
    return M.load_gold()


@cache
def _pairs() -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    for p in map(json.loads, (ROOT / "data" / "pairs.jsonl").open()):
        out.setdefault(p["qid"], []).append(p["nct"])
    return out


def dev_patients() -> list[dict]:
    """Dev-split patients only (the demo never shows test patients)."""
    dev = M.load_split("dev")
    out = []
    for q in dev:
        note = patient_note(q)
        first = note.split(". ")[0][:140]
        out.append({"qid": q, "n_trials": len(_pairs()[q]), "summary": first})
    return out


def _fmt(v: Any) -> str:
    if v is None:
        return "unknown"
    if isinstance(v, bool):
        return "yes" if v else "no"
    return f"{v:g}" if isinstance(v, float) else str(v)


def parse_answer(raw: Any, vtype: str) -> bool | float | None:
    """The user's answer from the UI: 'yes' / 'no' / 'unknown' or a number (as text or number)."""
    if raw is None or (isinstance(raw, str) and raw.strip().lower() in ("", "unknown", "not sure", "?")):
        return None
    if vtype == "Bool":
        if isinstance(raw, bool):
            return raw
        s = str(raw).strip().lower()
        if s in ("yes", "y", "true"):
            return True
        if s in ("no", "n", "false"):
            return False
        raise ValueError(f"expected yes / no / unknown, got {raw!r}")
    try:
        return float(raw)
    except (TypeError, ValueError) as e:
        raise ValueError(f"expected a number or unknown, got {raw!r}") from e


def _assertions(text: str, var: str, limit: int = 3) -> list[str]:
    """Top-level asserts of an SMT-LIB program that mention ``var`` (whitespace collapsed)."""
    pat = re.compile(rf"(?<![\w|]){re.escape(var)}(?![\w|])")
    out = []
    for e in _top_level(text):
        if e.lstrip("( ").startswith("assert") and pat.search(e):
            out.append(re.sub(r"\s+", " ", e))
    out.sort(key=lambda e: "AUXILIARY" in e)  # real criteria before definitional links
    return out[:limit]


@dataclass
class Agent:
    kind: str  # "ours" | "greedy"
    qid: str
    ncts: list[str]
    states: dict[str, TrialState] = field(init=False)
    asked: set = field(default_factory=set)
    turns: list[dict] = field(default_factory=list)
    pending: dict | None = None
    done: bool = False

    def __post_init__(self) -> None:
        self.states = {n: TrialState(n, {}) for n in self.ncts}
        self.rng = random.Random(0)
        self.policy = AnswerableInformative() if self.kind == "ours" else greedy_smt

    # ------------------------------------------------------------ views

    def trial_view(self, nct: str) -> dict:
        s = self.states[nct]
        cohorts = []
        for c, (inc, exc) in s.cohorts.items():
            cohorts.append({"id": c or "main", "inclusion": inc.status(s.answers),
                            "exclusion": exc.status(s.answers)})
        cs = s.cohort_status()
        for row, c in zip(cohorts, s.cohorts):
            row["status"] = cs[c]
        gold = "eligible" if _gold()[(self.qid, nct)] else "ineligible"
        return {"nct": nct, "title": trial(nct).get("title", ""), "status": s.status(),
                "verdict": s.verdict(), "gold": gold, "cohorts": cohorts,
                "n_vars": len(s.variables),
                "n_answered": sum(1 for v in s.answers.values() if v is not None),
                "n_asked": sum(1 for n, _ in self.asked if n == nct)}

    def view(self) -> dict:
        trials = [self.trial_view(n) for n in self.ncts]
        unknown = sum(t["answer"] is None for t in self.turns)
        return {"kind": self.kind, "name": AGENTS[self.kind], "done": self.done,
                "n_turns": len(self.turns), "n_unknown": unknown,
                "n_correct": sum(t["verdict"] == t["gold"] for t in trials),
                "n_decided": sum(t["status"] != "undetermined" for t in trials),
                "trials": trials}

    # ------------------------------------------------------------ ranking (for display)

    def _rank_ours(self) -> list[dict]:
        from smt_trial_matching.answerability import model_for

        pol: AnswerableInformative = self.policy  # type: ignore[assignment]
        model = model_for(self.states, c=pol.cfg.answerability_c)
        rows = []
        for n in _undetermined(self.states):
            s = self.states[n]
            open_c = [c for c, st in s.cohort_status().items() if st == "open"]
            for v in candidate_questions(s):
                if (n, v) in self.asked:
                    continue
                vt = s.types[v]
                p_ans, p_true = model.predict(v, vt)
                score = score_question(s, v, model, pol.cfg, p_ans=p_ans)
                if score <= 0:
                    continue
                row = {"nct": n, "var": v, "type": vt, "p_answered": p_ans, "score": score,
                       "value": score / p_ans if p_ans else 0.0}
                if vt == "Bool":
                    row["p_true"] = p_true
                    row["if_yes"] = s.status({**s.answers, v: True})
                    row["if_no"] = s.status({**s.answers, v: False})
                    row["value_yes"] = _answer_value(s, v, True, open_c, pol.cfg)
                    row["value_no"] = _answer_value(s, v, False, open_c, pol.cfg)
                rows.append(row)
        rows.sort(key=lambda r: (-r["score"], -r["p_answered"], r["nct"], r["var"]))
        return rows

    def _rank_greedy(self) -> list[dict]:
        rows = []
        for n in _undetermined(self.states):
            for v, res in self.states[n].informative():
                if (n, v) in self.asked:
                    continue
                row = {"nct": n, "var": v, "type": self.states[n].types[v],
                       "score": float(_greedy_score(res))}
                if True in res:
                    row["if_yes"], row["if_no"] = res[True], res[False]
                rows.append(row)
        rows.sort(key=lambda r: -r["score"])  # stable: ties keep greedy_smt's order (first wins)
        return rows

    # ------------------------------------------------------------ the two steps of a turn

    def ask(self) -> dict | None:
        """Pick the next question (the real policy), plus the ranked candidates behind it."""
        if self.pending is not None:
            return self.pending
        if self.done or len(self.turns) >= BUDGET:
            self.done = True
            return None
        ranked = self._rank_ours() if self.kind == "ours" else self._rank_greedy()
        q = self.policy(self.states, self.asked, self.rng)
        if q is None:
            self.done = True
            return None
        nct, var = q
        s = self.states[nct]
        vt = s.types[var]
        meaning = meanings(nct).get(var) or ""
        chosen = next((r for r in ranked if (r["nct"], r["var"]) == q), None)
        for r in ranked[:TOP_K]:
            r["text"] = question_text(r["var"], r["type"], meanings(r["nct"]).get(r["var"]) or "")
        self.pending = {
            "turn": len(self.turns) + 1, "nct": nct, "var": var, "type": vt, "meaning": meaning,
            "text": question_text(var, vt, meaning), "unit": unit_of(var) if vt != "Bool" else "",
            "trial_title": trial(nct).get("title", ""),
            "informative": any(v == var for v, _ in s.informative()),
            "candidates": ranked[:TOP_K], "n_candidates": len(ranked), "chosen": chosen,
            # shown only in "you are the patient" mode, as a prompt for whoever plays the patient
            "key_answer": _fmt(_sim().answer(self.qid, nct, var)),
        }
        return self.pending

    def answer(self, raw: Any = SIM) -> dict:
        """Apply the answer to the pending question; report what the solver concluded."""
        q = self.pending
        if q is None:
            raise RuntimeError("no pending question; call ask() first")
        nct, var, vt = q["nct"], q["var"], q["type"]
        value = _sim().answer(self.qid, nct, var) if raw == SIM else parse_answer(raw, vt)
        s = self.states[nct]
        before_trial = self.trial_view(nct)
        before_sides = {c: (inc.status(s.answers), exc.status(s.answers)) for c, (inc, exc) in s.cohorts.items()}
        verdicts_before = {n: st.verdict() for n, st in self.states.items()}

        s.answers[var] = value
        self.asked.add((nct, var))
        self.pending = None

        trace = []
        for c, (inc, exc) in s.cohorts.items():
            for side, prog, old in (("inclusion", inc, before_sides[c][0]), ("exclusion", exc, before_sides[c][1])):
                if var not in prog.types:
                    continue
                new = prog.status(s.answers)
                trace.append({"cohort": c or "main", "side": side, "before": old, "after": new,
                              "changed": old != new, "explain": SIDE_TEXT[new],
                              "assertions": _assertions(prog.text, var)})
        after_trial = self.trial_view(nct)
        turn = {**{k: q[k] for k in ("turn", "nct", "var", "type", "text", "informative")},
                "answer": value, "answer_text": _fmt(value),
                "label": M.label({"informative": q["informative"], "answer": value}),
                "status_before": before_trial["status"], "status_after": after_trial["status"],
                "verdict_changed": verdicts_before[nct] != s.verdict()}
        self.turns.append(turn)
        if len(self.turns) >= BUDGET:
            self.done = True
        return {"turn": turn, "trace": trace, "agent": self.view()}


class DemoSession:
    """One patient, one or two agents. ``mode`` is 'sim' (answer key answers, both agents) or
    'manual' (the user answers; our agent only)."""

    def __init__(self, qid: str, mode: str = "sim") -> None:
        if qid not in M.load_split("dev"):
            raise ValueError(f"{qid} is not a dev patient (the demo only shows dev patients)")
        self.qid, self.mode = qid, mode
        ncts = _pairs()[qid]
        kinds = ["ours", "greedy"] if mode == "sim" else ["ours"]
        self.agents = {k: Agent(k, qid, ncts) for k in kinds}

    def view(self) -> dict:
        return {"qid": self.qid, "mode": self.mode, "note": patient_note(self.qid),
                "agents": {k: a.view() for k, a in self.agents.items()}}
