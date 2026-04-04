"""Tests for Appendix R-F --- Statistics, Probability, and Matter Interpretation."""
import pytest
from grut.rf_statistics_probability_matter_audit import (
    N_ELIGIBILITY_ITEMS, N_BOSONIC_TESTS, N_FERMIONIC_CHECKS,
    N_EXCHANGE_CANDIDATES, N_MEMORY_TESTS, N_PROBABILITY_TESTS,
    N_BENCHMARK_CANDIDATES, N_INTERPRETATION_LEVELS,
    N_APPENDIX_P_ENTRIES, N_RF_NONCLAIMS, N_ALLOWED_CLAIMS, N_FORBIDDEN_CLAIMS,
    RF_BOSONIC_STATS_VERDICT, RF_FERMIONIC_STATS_VERDICT,
    RF_INDISTINGUISHABILITY_VERDICT, RF_MATTER_INTERPRETATION_VERDICT,
    RF_AUTHORIZATION_VERDICT, RF_OVERALL_APPENDIX_P_CLASS,
    ALLOWED_BOSONIC_STATS_VERDICTS, ALLOWED_FERMIONIC_STATS_VERDICTS,
    ALLOWED_INDISTINGUISHABILITY_VERDICTS, ALLOWED_MATTER_INTERPRETATION_VERDICTS,
    ALLOWED_AUTHORIZATION_VERDICTS, RF_NONCLAIMS,
    run_rf_statistics_probability_matter_audit, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_rf_statistics_probability_matter_audit()

class TestRFConstants:
    def test_counts(self):
        assert N_RF_NONCLAIMS == 8
        assert N_BOSONIC_TESTS == 4
        assert N_MEMORY_TESTS == 5
    def test_nonclaims(self):
        assert len(RF_NONCLAIMS) == N_RF_NONCLAIMS
        for nc in RF_NONCLAIMS:
            assert nc.startswith("NOT_claiming_")
    def test_verdicts(self):
        assert RF_BOSONIC_STATS_VERDICT == "bosonic_exchange_structure_demonstrated"
        assert RF_FERMIONIC_STATS_VERDICT == "fermionic_statistics_obstruction_unchanged"
        assert RF_INDISTINGUISHABILITY_VERDICT == "exchange_symmetry_with_open_system_caveats"
        assert "probability_postulate" in RF_MATTER_INTERPRETATION_VERDICT
        assert RF_AUTHORIZATION_VERDICT == "authorized_to_proceed_to_RG"

class TestTrackBBosonic:
    def test_n_tests(self, result):
        assert result.track_b_bosonic.n_tests == N_BOSONIC_TESTS
    def test_bs1_demonstrated(self, result):
        assert result.track_b_bosonic.tests[0].result == "demonstrated"
    def test_verdict(self, result):
        assert result.track_b_bosonic.bosonic_statistics_verdict == RF_BOSONIC_STATS_VERDICT

class TestTrackCFermionic:
    def test_unchanged(self, result):
        assert result.track_c_fermionic.obstruction_unchanged is True
    def test_verdict(self, result):
        assert result.track_c_fermionic.fermionic_statistics_verdict == RF_FERMIONIC_STATS_VERDICT

class TestTrackDExchange:
    def test_n_available(self, result):
        assert result.track_d_exchange.n_available == 3

class TestTrackEMemory:
    def test_tau_memory(self, result):
        assert result.track_e_memory.tau_creates_transient_memory is True
    def test_verdict(self, result):
        assert result.track_e_memory.indistinguishability_verdict == RF_INDISTINGUISHABILITY_VERDICT
    def test_ml5_not_fundamental(self, result):
        ml5 = result.track_e_memory.tests[4]
        assert ml5.result == "confirmed"

class TestTrackFProbability:
    def test_born_required(self, result):
        assert result.track_f_probability.born_rule_required_for_interpretation is True

class TestTrackGBenchmark:
    def test_n_viable(self, result):
        assert result.track_g_benchmark.n_viable == 2
    def test_chosen_sb2(self, result):
        assert "SB2" in result.track_g_benchmark.chosen_id

class TestTrackHInterpretation:
    def test_n_levels(self, result):
        assert result.track_h_interpretation.n_levels == N_INTERPRETATION_LEVELS
    def test_all_achieved(self, result):
        for l in result.track_h_interpretation.levels:
            assert l.achieved is True
    def test_verdict(self, result):
        assert result.track_h_interpretation.matter_interpretation_verdict == \
               RF_MATTER_INTERPRETATION_VERDICT

class TestHardGatedVerdicts:
    def test_all_exact(self, result):
        assert result.bosonic_statistics_verdict == RF_BOSONIC_STATS_VERDICT
        assert result.fermionic_statistics_verdict == RF_FERMIONIC_STATS_VERDICT
        assert result.indistinguishability_verdict == RF_INDISTINGUISHABILITY_VERDICT
        assert result.matter_interpretation_verdict == RF_MATTER_INTERPRETATION_VERDICT
        assert result.authorization_verdict == RF_AUTHORIZATION_VERDICT
    def test_all_in_allowed(self, result):
        assert result.bosonic_statistics_verdict in ALLOWED_BOSONIC_STATS_VERDICTS
        assert result.fermionic_statistics_verdict in ALLOWED_FERMIONIC_STATS_VERDICTS
        assert result.indistinguishability_verdict in ALLOWED_INDISTINGUISHABILITY_VERDICTS
        assert result.matter_interpretation_verdict in ALLOWED_MATTER_INTERPRETATION_VERDICTS
        assert result.authorization_verdict in ALLOWED_AUTHORIZATION_VERDICTS
    def test_all_distinct(self, result):
        v = {result.bosonic_statistics_verdict, result.fermionic_statistics_verdict,
             result.indistinguishability_verdict, result.matter_interpretation_verdict,
             result.authorization_verdict}
        assert len(v) == 5

class TestMasterAudit:
    def test_valid(self, result):
        assert result.valid is True
    def test_claims(self, result):
        assert len(result.allowed_claims) == N_ALLOWED_CLAIMS
        assert len(result.forbidden_claims) == N_FORBIDDEN_CLAIMS
    def test_diagnostics(self, result):
        assert result.diagnostics["fermionic_obstruction_unchanged"] is True
        assert result.diagnostics["tau_creates_memory"] is True
        assert result.diagnostics["born_required"] is True
    def test_idempotency(self):
        r1 = run_rf_statistics_probability_matter_audit()
        r2 = run_rf_statistics_probability_matter_audit()
        assert r1.bosonic_statistics_verdict == r2.bosonic_statistics_verdict
    def test_self_test(self):
        assert _self_test() is True
