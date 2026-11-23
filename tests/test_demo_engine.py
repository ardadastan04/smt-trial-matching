"""The demo engine runs the real agents: same questions and verdicts as smtstate.runner."""

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT), str(ROOT / "src")]

from baselines.policies import greedy_smt
from demo.engine import SIM, Agent, DemoSession, _pairs, parse_answer
from demo.phrasing import question_text
from smt_trial_matching.policies import AnswerableInformative
from smtstate.runner import run_patient
from smtstate.sim import AnswerKeySimulator

QID = "trec-202139"


@pytest.mark.parametrize("kind", ["ours", "greedy"])
def test_sim_episode_matches_runner(kind):
    ncts = _pairs()[QID]
    policy = AnswerableInformative() if kind == "ours" else greedy_smt
    ref = run_patient(QID, ncts, policy, AnswerKeySimulator("gpt5_oracle"), budget=30)
    agent = Agent(kind, QID, ncts)
    while (q := agent.ask()) is not None:
        if agent.kind == "ours":  # the ranking shown in the UI picks the same question
            top = q["candidates"][0]
            assert (top["nct"], top["var"]) == (q["nct"], q["var"])
        agent.answer(SIM)
    assert [(t["nct"], t["var"], t["answer"]) for t in agent.turns] == \
        [(t["nct"], t["var"], t["answer"]) for t in ref["turns"]]
    assert {t["nct"]: t["verdict"] for t in agent.view()["trials"]} == ref["final_verdicts"]


def test_manual_answer_changes_state():
    s = DemoSession(QID, mode="manual")
    a = s.agents["ours"]
    q = a.ask()
    out = a.answer("yes" if q["type"] == "Bool" else "40")
    assert out["turn"]["answer"] in (True, 40.0)
    assert out["trace"], "the asked variable appears in some program side"


def test_test_patients_refused():
    import json
    test_qid = json.loads((ROOT / "data" / "splits.json").read_text())["test"][0]
    with pytest.raises(ValueError):
        DemoSession(test_qid)


def test_parse_answer():
    assert parse_answer("Yes", "Bool") is True
    assert parse_answer("no", "Bool") is False
    assert parse_answer("not sure", "Bool") is None
    assert parse_answer("3.5", "Real") == 3.5
    with pytest.raises(ValueError):
        parse_answer("maybe", "Bool")


@pytest.mark.parametrize("name,vtype,expected", [
    ("patient_has_diagnosis_of_asthma_now", "Bool", "Have you been diagnosed with asthma?"),
    ("patient_has_finding_of_dyskinesia_inthehistory", "Bool", "Have you ever had dyskinesia?"),
    ("patient_is_pregnant_now", "Bool", "Are you pregnant?"),
    ("patient_has_allergy_to_allergy_to_ciprofloxacin_now", "Bool", "Are you allergic to ciprofloxacin?"),
    ("patient_age_value_recorded_now_in_years", "Int", "What is your current age (in years)?"),
    ("patient_has_undergone_surgery_inthepast6months", "Bool", "Have you had surgery in the past 6 months?"),
    ("patient_has_finding_of_skin_lesion_now@@extensive@@caused_by_burns", "Bool",
     "Do you currently have skin lesion (extensive, caused by burns)?"),
    ("patient_has_finding_of_jaundice_now@@visible", "Bool", "Do you currently have jaundice (visible)?"),
])
def test_question_text(name, vtype, expected):
    assert question_text(name, vtype) == expected
