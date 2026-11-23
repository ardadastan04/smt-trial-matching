"""Unit tests for the cost, cache and budget logic. No network calls."""

from __future__ import annotations

import json

import pytest

from smt_trial_matching.llm import (
    BudgetExceeded,
    BudgetGuard,
    CostEntry,
    CostLog,
    DiskCache,
    Pricing,
    cache_key,
)

FLASH = Pricing(usd_per_mtok_in=0.30, usd_per_mtok_out=2.50)
PRO = Pricing(
    usd_per_mtok_in=1.25,
    usd_per_mtok_out=10.00,
    usd_per_mtok_in_long=2.50,
    usd_per_mtok_out_long=15.00,
    long_prompt_threshold=200_000,
)


class TestPricing:
    def test_flat_rate(self) -> None:
        # 1M in + 1M out at flash rates.
        assert FLASH.cost_usd(1_000_000, 1_000_000) == pytest.approx(2.80)

    def test_realistic_turn_is_tiny(self) -> None:
        assert FLASH.cost_usd(2_000, 150) == pytest.approx(0.000975)

    def test_zero_tokens(self) -> None:
        assert FLASH.cost_usd(0, 0) == 0.0

    def test_below_threshold_uses_base_tier(self) -> None:
        assert PRO.cost_usd(200_000, 1_000) == pytest.approx(0.25 + 0.01)

    def test_above_threshold_uses_long_tier(self) -> None:
        # Strictly greater than the threshold switches tiers.
        assert PRO.cost_usd(200_001, 1_000) == pytest.approx(
            200_001 * 2.50 / 1e6 + 1_000 * 15.0 / 1e6
        )

    def test_no_tier_configured_never_switches(self) -> None:
        assert FLASH.cost_usd(5_000_000, 0) == pytest.approx(1.50)


class TestCacheKey:
    def test_stable_across_dict_ordering(self) -> None:
        a = cache_key("m", [{"role": "user", "content": "hi"}], {"temperature": 0, "max_tokens": 8})
        b = cache_key("m", [{"content": "hi", "role": "user"}], {"max_tokens": 8, "temperature": 0})
        assert a == b

    @pytest.mark.parametrize(
        "model,messages,params",
        [
            ("other", [{"role": "user", "content": "hi"}], {"temperature": 0}),
            ("m", [{"role": "user", "content": "bye"}], {"temperature": 0}),
            ("m", [{"role": "user", "content": "hi"}], {"temperature": 1}),
        ],
    )
    def test_any_component_changes_the_key(self, model, messages, params) -> None:
        base = cache_key("m", [{"role": "user", "content": "hi"}], {"temperature": 0})
        assert cache_key(model, messages, params) != base


class TestDiskCache:
    def test_roundtrip(self, tmp_path) -> None:
        cache = DiskCache(tmp_path)
        cache.put("abc123", {"text": "hello"})
        assert cache.get("abc123") == {"text": "hello"}

    def test_miss_returns_none(self, tmp_path) -> None:
        assert DiskCache(tmp_path).get("nope") is None

    def test_disabled_never_stores(self, tmp_path) -> None:
        cache = DiskCache(tmp_path, enabled=False)
        cache.put("k", {"text": "v"})
        assert cache.get("k") is None

    def test_corrupt_entry_is_a_miss(self, tmp_path) -> None:
        cache = DiskCache(tmp_path)
        cache.put("k", {"text": "v"})
        cache._path("k").write_text("{not json")
        assert cache.get("k") is None


def _entry(usd: float) -> CostEntry:
    return CostEntry(
        ts=0.0, run_id="t", model="m", tag="x",
        prompt_tokens=1, completion_tokens=1, usd=usd, cached=False, latency_s=0.0,
    )


class TestCostLog:
    def test_accumulates_and_writes_jsonl(self, tmp_path) -> None:
        log = CostLog("t", runs_dir=tmp_path)
        log.record(_entry(0.01))
        log.record(_entry(0.02))
        assert log.total_usd == pytest.approx(0.03)
        assert log.calls == 2
        lines = log.path.read_text().strip().splitlines()
        assert [json.loads(line)["usd"] for line in lines] == [0.01, 0.02]

    def test_resumes_prior_spend(self, tmp_path) -> None:
        CostLog("t", runs_dir=tmp_path).record(_entry(0.05))
        # A resumed run must not forget what it already spent.
        assert CostLog("t", runs_dir=tmp_path).total_usd == pytest.approx(0.05)

    def test_tolerates_a_torn_line(self, tmp_path) -> None:
        log = CostLog("t", runs_dir=tmp_path)
        log.record(_entry(0.05))
        with log.path.open("a") as fh:
            fh.write("{partial\n")
        assert CostLog("t", runs_dir=tmp_path).total_usd == pytest.approx(0.05)


class TestBudgetGuard:
    def test_passes_under_cap(self, tmp_path) -> None:
        log = CostLog("t", runs_dir=tmp_path)
        log.record(_entry(0.5))
        BudgetGuard(max_run_usd=1.0, cost_log=log).check()  # must not raise

    def test_raises_at_cap(self, tmp_path) -> None:
        log = CostLog("t", runs_dir=tmp_path)
        log.record(_entry(1.0))
        with pytest.raises(BudgetExceeded, match="cap"):
            BudgetGuard(max_run_usd=1.0, cost_log=log).check()

    def test_projection_extrapolates_from_mean(self, tmp_path) -> None:
        log = CostLog("t", runs_dir=tmp_path)
        log.record(_entry(0.10))
        log.record(_entry(0.30))
        # mean 0.20 over 2 calls, plus 10 more units.
        assert BudgetGuard(2.0, log).projected_usd(10) == pytest.approx(0.40 + 2.0)

    def test_projection_is_zero_before_any_call(self, tmp_path) -> None:
        log = CostLog("t", runs_dir=tmp_path)
        assert BudgetGuard(1.0, log).projected_usd(60) == 0.0


class TestEmbed:
    """LLMClient.embed with the network call replaced: batching, cache, cost lines."""

    def _client(self, tmp_path, monkeypatch):
        from types import SimpleNamespace

        from smt_trial_matching import llm

        monkeypatch.setenv("GEMINI_API_KEY", "test-key")
        monkeypatch.setenv("LLM_BACKEND", "gemini_api")
        monkeypatch.setattr(llm, "EMBED_BATCH", 2)
        calls = []

        def fake(self, texts, model_id, params):
            calls.append(list(texts))
            return SimpleNamespace(usage=SimpleNamespace(prompt_tokens=1000 * len(texts)),
                                   data=[SimpleNamespace(embedding=[float(len(t)), 1.0]) for t in texts])

        monkeypatch.setattr(llm.LLMClient, "_create_embeddings", fake)
        client = llm.LLMClient("emb_test", cache=DiskCache(tmp_path / "cache"), runs_dir=tmp_path,
                               max_run_usd=1.0)
        client_throttle = llm.Throttle(0)
        monkeypatch.setattr(llm, "throttle", lambda: client_throttle)
        return client, calls

    def test_batches_in_order_and_prices(self, tmp_path, monkeypatch) -> None:
        client, calls = self._client(tmp_path, monkeypatch)
        out = client.embed(["a", "bb", "ccc"], model="m", tag="t")
        assert [v[0] for v in out] == [1.0, 2.0, 3.0]
        assert calls == [["a", "bb"], ["ccc"]]
        assert client.cost_log.calls == 2
        assert client.cost_log.total_usd == pytest.approx(3000 * 0.15 / 1e6)

    def test_second_call_is_cached(self, tmp_path, monkeypatch) -> None:
        client, calls = self._client(tmp_path, monkeypatch)
        client.embed(["a", "bb"], model="m")
        out = client.embed(["bb", "a", "dddd"], model="m")
        assert [v[0] for v in out] == [2.0, 1.0, 4.0]
        assert calls == [["a", "bb"], ["dddd"]]
