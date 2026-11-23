"""LLM answerability (v2 version A): prompt, parsing, store and policy wiring, all offline."""

import json
from dataclasses import dataclass

import pytest

from smt_trial_matching import answerability as A
from smt_trial_matching import llm_answerability as L
from smt_trial_matching.policies import AnswerableConfig, AnswerableInformative

DEMO = "trec-202139"  # dev patient, 5 trials (the newborn demo)


@dataclass
class _Reply:
    text: str


class FakeClient:
    """Stands in for llm.LLMClient: answers every fact with fixed probabilities, counts calls."""

    def __init__(self, drop_last: bool = False) -> None:
        self.calls = 0
        self.prompts: list[str] = []
        self.drop_last = drop_last

    def complete(self, messages, **kw):
        self.calls += 1
        user = messages[-1]["content"]
        self.prompts.append(user)
        n = user.split("Facts:\n", 1)[1].count("\n") + 1
        rows = [{"id": i, "p_answered": 0.9, "p_true": 0.1} for i in range(1, n + 1)]
        if self.drop_last and n > 1:
            rows = rows[:-1]
        return _Reply("```json\n" + json.dumps(rows) + "\n```")


def test_parse_response_tolerates_fences_ids_and_garbage():
    text = 'Sure:\n```json\n[{"id": 2, "p_answered": 1.3, "p_true": null}, {"id": 1, "p_answered": "0.4", "p_true": 0.5}]\n```'
    assert L.parse_response(text, 3) == [(0.4, 0.5), (L.P_MAX, None), (None, None)]
    assert L.parse_response("no json here", 2) == [(None, None), (None, None)]


def test_prompt_has_names_and_meanings_but_no_patient_text():
    items = L.items_for([DEMO])
    msgs = L.build_prompt(items[:5])
    body = msgs[-1]["content"]
    assert all(it.name in body for it in items[:5])
    with open(L.DATA / "patients.jsonl") as fh:
        note = next(json.loads(x)["text"] for x in fh if f'"{DEMO}"' in x)
    assert note[:60] not in body and "jaundice that started a day ago" not in body


def test_items_are_unique_per_name_and_type():
    items = L.items_for([DEMO])
    assert len({(i.name, i.vtype) for i in items}) == len(items) > 0


def test_precompute_asks_each_variable_once_and_retries_dropped(tmp_path):
    items = L.items_for([DEMO])[:45]
    path = tmp_path / "store.jsonl"
    fake = FakeClient(drop_last=True)
    counts = L.precompute(items, fake, "fake-model", path, batch_size=20)
    assert counts["stored"] == 45 and counts["failed"] == 0
    assert fake.calls == 3 + 3  # 3 batches, then 1 dropped item retried per batch
    again = FakeClient()
    assert L.precompute(items, again, "fake-model", path)["asked"] == 0 and again.calls == 0


def test_model_reads_store_and_falls_back(tmp_path):
    items = L.items_for([DEMO])
    path = tmp_path / "store.jsonl"
    L.precompute(items[:10], FakeClient(), "fake-model", path)
    fb = A.fit_default()
    m = L.LLMAnswerabilityModel(L.load_store(path), fb)
    bool_item = next(i for i in items[:10] if i.vtype == "Bool")
    assert m.predict(bool_item.name, "Bool") == (0.9, 0.1)
    missing = items[-1]
    assert m.predict(missing.name, missing.vtype) == fb.predict(missing.name, missing.vtype)
    assert m.fallbacks == 1
    with pytest.raises(KeyError):
        L.LLMAnswerabilityModel(L.load_store(path), fb, strict=True).predict(missing.name, missing.vtype)
    assert m.value_distribution("patient_age_value_recorded_now_in_years") == \
        fb.value_distribution("patient_age_value_recorded_now_in_years")


def test_policy_v1_default_unchanged_and_llm_switch_runs(tmp_path, monkeypatch):
    assert AnswerableConfig().answerability == "name"
    path = tmp_path / "store.jsonl"
    L.precompute(L.items_for([DEMO]), FakeClient(), "fake-model", path)
    monkeypatch.setenv("LLM_ANSWERABILITY_STORE", str(path))
    from smt_trial_matching.answerability import _patient_trials
    from smtstate.state import TrialState

    trials = next(sorted(t) for t, q in _patient_trials().items() if q == DEMO)
    states = {n: TrialState(n, {}) for n in trials}
    q = AnswerableInformative(AnswerableConfig(answerability="llm"))(states, set(), None)
    assert q is not None and q[0] in trials


def test_missing_store_fails_clearly(tmp_path):
    with pytest.raises(FileNotFoundError, match="precompute_llm_answerability"):
        L.llm_model_for(["NCT01622699"], store=str(tmp_path / "nope.jsonl"))


def test_estimate_counts_batches():
    items = L.items_for([DEMO])
    est = L.estimate(items, batch_size=20)
    assert est["calls"] == -(-len(items) // 20) and est["usd"] > 0


def test_dev_eval_reports_both_aucs(tmp_path):
    import importlib.util

    spec = importlib.util.spec_from_file_location("ev", L.ROOT / "scripts" / "eval_llm_answerability.py")
    ev = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ev)
    path = tmp_path / "store.jsonl"
    L.precompute(L.items_for(A.load_split("dev")[:3]), FakeClient(), "fake-model", path)
    res = ev.evaluate(L.load_store(path))
    assert res["covered"] > 0 and set(res["auc_p_answered"]) == {"llm", "name_crossfit", "llm_minus_name_ci95"}
    assert res["auc_p_answered"]["llm"] == 0.5  # constant fake predictions carry no signal


def test_boot_auc_diff_is_paired_by_patient():
    import importlib.util

    spec = importlib.util.spec_from_file_location("ev", L.ROOT / "scripts" / "eval_llm_answerability.py")
    ev = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ev)
    qids = ["a", "a", "b", "b", "c", "c"]
    y = [1, 0, 1, 0, 1, 0]
    perfect, noise = [0.9, 0.1, 0.8, 0.2, 0.7, 0.3], [0.5] * 6
    point, lo, hi = ev.boot_auc_diff(qids, y, perfect, noise, n=200)
    assert point == 0.5 and lo == hi == 0.5  # every resample keeps whole patients, so the gap is fixed
    assert ev.boot_auc_diff(qids, y, perfect, perfect, n=50) == [0.0, 0.0, 0.0]
