"""Tests for Appendix R-C --- Stabilization and Bound Structure."""
import pytest
from grut.rc_stabilization_bound_structure_audit import (
    N_STABILITY_CRITERIA, N_NATIVE_CANDIDATES, N_TOPOLOGICAL_CHECKS,
    N_DISSIPATION_TESTS, N_BENCHMARK_CANDIDATES, N_ENERGY_CHECKS,
    N_QUANTUM_CHECKS, N_READINESS_DOMAINS, N_PROBABILITY_TESTS,
    N_APPENDIX_P_ENTRIES, N_RC_NONCLAIMS, N_ALLOWED_CLAIMS, N_FORBIDDEN_CLAIMS,
    RC_NATIVE_STABILITY_VERDICT, RC_DISSIPATION_VERDICT,
    RC_TOPOLOGICAL_VERDICT, RC_BOUND_STRUCTURE_VERDICT,
    RC_AUTHORIZATION_VERDICT, RC_OVERALL_APPENDIX_P_CLASS,
    ALLOWED_NATIVE_STABILITY_VERDICTS, ALLOWED_DISSIPATION_VERDICTS,
    ALLOWED_TOPOLOGICAL_VERDICTS, ALLOWED_BOUND_STRUCTURE_VERDICTS,
    ALLOWED_AUTHORIZATION_VERDICTS, ALLOWED_APPENDIX_P_CLASSES,
    ALLOWED_READINESS_LEVELS, RC_NONCLAIMS,
    run_rc_stabilization_bound_structure_audit, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_rc_stabilization_bound_structure_audit()

class TestRCConstants:
    def test_counts(self):
        assert N_STABILITY_CRITERIA == 6
        assert N_NATIVE_CANDIDATES == 6
        assert N_RC_NONCLAIMS == 8
    def test_nonclaims(self):
        assert len(RC_NONCLAIMS) == N_RC_NONCLAIMS
        for nc in RC_NONCLAIMS:
            assert nc.startswith("NOT_claiming_")
    def test_verdicts(self):
        assert RC_NATIVE_STABILITY_VERDICT == "no_native_stabilizer_found"
        assert RC_DISSIPATION_VERDICT == "dissipation_supports_metastability_only"
        assert RC_TOPOLOGICAL_VERDICT == "topological_route_motivated_but_unbuilt"
        assert RC_BOUND_STRUCTURE_VERDICT == "bosonic_bound_structure_not_yet_established"
        assert RC_AUTHORIZATION_VERDICT == "authorized_to_proceed_to_RD"
    def test_overall_bsr(self):
        assert RC_OVERALL_APPENDIX_P_CLASS == "bounded_structural_result"

class TestTrackACriteria:
    def test_n_criteria(self, result):
        assert result.track_a_criteria.n_criteria == N_STABILITY_CRITERIA
    def test_derrick_not_satisfied(self, result):
        sc1 = result.track_a_criteria.criteria[0]
        assert sc1.satisfied == "not_satisfied"
    def test_restoring_not_satisfied(self, result):
        sc5 = result.track_a_criteria.criteria[4]
        assert sc5.satisfied == "not_satisfied"

class TestTrackBNative:
    def test_n_candidates(self, result):
        assert result.track_b_native.n_candidates == N_NATIVE_CANDIDATES
    def test_zero_provides(self, result):
        assert result.track_b_native.n_provides == 0
    def test_verdict(self, result):
        assert result.track_b_native.native_stability_verdict == RC_NATIVE_STABILITY_VERDICT
    def test_ns1_no_stability(self, result):
        assert result.track_b_native.candidates[0].provides_stability is False

class TestTrackCTopological:
    def test_n_checks(self, result):
        assert result.track_c_topological.n_checks == N_TOPOLOGICAL_CHECKS
    def test_skyrme_mbu(self, result):
        ts3 = result.track_c_topological.checks[2]
        assert ts3.status == "motivated_but_unbuilt"
    def test_verdict(self, result):
        assert result.track_c_topological.topological_verdict == RC_TOPOLOGICAL_VERDICT

class TestTrackDDissipation:
    def test_n_tests(self, result):
        assert result.track_d_dissipation.n_tests == N_DISSIPATION_TESTS
    def test_metastability(self, result):
        assert result.track_d_dissipation.metastability_supported is True
    def test_verdict(self, result):
        assert result.track_d_dissipation.dissipation_verdict == RC_DISSIPATION_VERDICT

class TestTrackEBenchmark:
    def test_n_candidates(self, result):
        assert result.track_e_benchmark.n_candidates == N_BENCHMARK_CANDIDATES
    def test_n_viable(self, result):
        assert result.track_e_benchmark.n_viable == 3
    def test_chosen_sb1(self, result):
        assert "SB1" in result.track_e_benchmark.chosen_id

class TestTrackFEnergy:
    def test_n_checks(self, result):
        assert result.track_f_energy.n_checks == N_ENERGY_CHECKS
    def test_n_available(self, result):
        assert result.track_f_energy.n_available == 3

class TestTrackGQuantum:
    def test_zero_stability(self, result):
        assert result.track_g_quantum.n_adds_stability == 0

class TestTrackHReadiness:
    def test_n_entries(self, result):
        assert result.track_h_readiness.n_entries == N_READINESS_DOMAINS
    def test_native_blocked(self, result):
        ns = [e for e in result.track_h_readiness.entries if "native" in e.domain]
        assert ns[0].readiness_level == "blocked"
    def test_all_valid_levels(self, result):
        for e in result.track_h_readiness.entries:
            assert e.readiness_level in ALLOWED_READINESS_LEVELS

class TestTrackIProbability:
    def test_independent(self, result):
        assert result.track_i_probability.stabilization_independent_of_probability is True

class TestTrackJAppendixP:
    def test_n_entries(self, result):
        assert result.track_j_appendix_p.n_entries == N_APPENDIX_P_ENTRIES
    def test_no_native_canon(self, result):
        assert result.track_j_appendix_p.no_native_canon is True

class TestTrackKAuthorization:
    def test_authorized(self, result):
        assert result.track_k_authorization.rd_authorized is True
    def test_verdict(self, result):
        assert result.track_k_authorization.authorization_verdict == RC_AUTHORIZATION_VERDICT

class TestTrackLNonclaims:
    def test_count(self, result):
        assert result.track_l_nonclaims.n_nonclaims == N_RC_NONCLAIMS
    def test_registered(self, result):
        assert result.track_l_nonclaims.all_registered is True

class TestHardGatedVerdicts:
    def test_all_exact(self, result):
        assert result.native_stability_verdict == RC_NATIVE_STABILITY_VERDICT
        assert result.dissipation_verdict == RC_DISSIPATION_VERDICT
        assert result.topological_stability_verdict == RC_TOPOLOGICAL_VERDICT
        assert result.bound_structure_verdict == RC_BOUND_STRUCTURE_VERDICT
        assert result.authorization_verdict == RC_AUTHORIZATION_VERDICT
    def test_all_in_allowed(self, result):
        assert result.native_stability_verdict in ALLOWED_NATIVE_STABILITY_VERDICTS
        assert result.dissipation_verdict in ALLOWED_DISSIPATION_VERDICTS
        assert result.topological_stability_verdict in ALLOWED_TOPOLOGICAL_VERDICTS
        assert result.bound_structure_verdict in ALLOWED_BOUND_STRUCTURE_VERDICTS
        assert result.authorization_verdict in ALLOWED_AUTHORIZATION_VERDICTS
    def test_all_distinct(self, result):
        v = {result.native_stability_verdict, result.dissipation_verdict,
             result.topological_stability_verdict, result.bound_structure_verdict,
             result.authorization_verdict}
        assert len(v) == 5

class TestMasterAudit:
    def test_valid(self, result):
        assert result.valid is True
    def test_claims(self, result):
        assert len(result.allowed_claims) == N_ALLOWED_CLAIMS
        assert len(result.forbidden_claims) == N_FORBIDDEN_CLAIMS
    def test_diagnostics(self, result):
        assert result.diagnostics["n_native_provides_stability"] == 0
        assert result.diagnostics["quantum_adds_stability"] == 0
        assert result.diagnostics["metastability_supported"] is True
    def test_idempotency(self):
        r1 = run_rc_stabilization_bound_structure_audit()
        r2 = run_rc_stabilization_bound_structure_audit()
        assert r1.bound_structure_verdict == r2.bound_structure_verdict
    def test_self_test(self):
        assert _self_test() is True
