"""Tests for Appendix R-D --- Composite Matter and Pre-Atomic Structure."""
import pytest
from grut.rd_composite_matter_preatomic_audit import (
    N_ELIGIBILITY_CRITERIA, N_BOSONIC_ROUTE_LEVELS, N_BINDING_CANDIDATES,
    N_PREATOMIC_LEVELS, N_BENCHMARK_CANDIDATES, N_QUANTUM_CONTRIBUTIONS,
    N_FERMIONIC_CHECKS, N_READINESS_DOMAINS, N_APPENDIX_P_ENTRIES,
    N_RD_NONCLAIMS, N_ALLOWED_CLAIMS, N_FORBIDDEN_CLAIMS,
    RD_COMPOSITE_VERDICT, RD_BINDING_VERDICT, RD_PREATOMIC_VERDICT,
    RD_FERMIONIC_BOUNDARY_VERDICT, RD_AUTHORIZATION_VERDICT,
    RD_OVERALL_APPENDIX_P_CLASS,
    ALLOWED_COMPOSITE_VERDICTS, ALLOWED_BINDING_VERDICTS,
    ALLOWED_PREATOMIC_VERDICTS, ALLOWED_FERMIONIC_VERDICTS,
    ALLOWED_AUTHORIZATION_VERDICTS, ALLOWED_APPENDIX_P_CLASSES,
    ALLOWED_READINESS_LEVELS, RD_NONCLAIMS,
    run_rd_composite_matter_preatomic_audit, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_rd_composite_matter_preatomic_audit()

class TestRDConstants:
    def test_counts(self):
        assert N_ELIGIBILITY_CRITERIA == 6
        assert N_BINDING_CANDIDATES == 5
        assert N_RD_NONCLAIMS == 8
    def test_nonclaims(self):
        assert len(RD_NONCLAIMS) == N_RD_NONCLAIMS
        for nc in RD_NONCLAIMS:
            assert nc.startswith("NOT_claiming_")
    def test_verdicts(self):
        assert RD_COMPOSITE_VERDICT == "bosonic_composite_configurations_extension_ready"
        assert RD_BINDING_VERDICT == "no_true_binding_criterion_found"
        assert RD_PREATOMIC_VERDICT == "pre_atomic_grammar_only"
        assert RD_FERMIONIC_BOUNDARY_VERDICT == "fermionic_boundary_unchanged"
        assert RD_AUTHORIZATION_VERDICT == "authorized_to_proceed_to_RE"

class TestTrackAEligibility:
    def test_n_criteria(self, result):
        assert result.track_a_eligibility.n_criteria == N_ELIGIBILITY_CRITERIA
    def test_binding_not_satisfied(self, result):
        ce5 = result.track_a_eligibility.criteria[4]
        assert ce5.status == "not_satisfied"

class TestTrackBBosonicRoute:
    def test_n_levels(self, result):
        assert result.track_b_bosonic_route.n_levels == N_BOSONIC_ROUTE_LEVELS
    def test_br5_not_achieved(self, result):
        assert result.track_b_bosonic_route.levels[4].achieved is False
    def test_br1_through_br4_achieved(self, result):
        for i in range(4):
            assert result.track_b_bosonic_route.levels[i].achieved is True
    def test_verdict(self, result):
        assert result.track_b_bosonic_route.composite_verdict == RD_COMPOSITE_VERDICT

class TestTrackCBinding:
    def test_n_candidates(self, result):
        assert result.track_c_binding.n_candidates == N_BINDING_CANDIDATES
    def test_zero_provides(self, result):
        assert result.track_c_binding.n_provides == 0
    def test_verdict(self, result):
        assert result.track_c_binding.binding_verdict == RD_BINDING_VERDICT

class TestTrackDPreAtomic:
    def test_n_levels(self, result):
        assert result.track_d_preatomic.n_levels == N_PREATOMIC_LEVELS
    def test_pa2_achieved(self, result):
        assert result.track_d_preatomic.levels[1].achieved is True
    def test_pa5_not_achieved(self, result):
        assert result.track_d_preatomic.levels[4].achieved is False
    def test_verdict(self, result):
        assert result.track_d_preatomic.pre_atomic_verdict == RD_PREATOMIC_VERDICT

class TestTrackEBenchmark:
    def test_n_viable(self, result):
        assert result.track_e_benchmark.n_viable == 3
    def test_chosen_cm2(self, result):
        assert "CM2" in result.track_e_benchmark.chosen_id

class TestTrackFQuantum:
    def test_zero_matter(self, result):
        assert result.track_f_quantum.n_adds_matter == 0

class TestTrackGFermionic:
    def test_unchanged(self, result):
        assert result.track_g_fermionic.obstruction_unchanged is True
    def test_verdict(self, result):
        assert result.track_g_fermionic.fermionic_boundary_verdict == RD_FERMIONIC_BOUNDARY_VERDICT

class TestTrackHReadiness:
    def test_n_entries(self, result):
        assert result.track_h_readiness.n_entries == N_READINESS_DOMAINS
    def test_all_valid(self, result):
        for e in result.track_h_readiness.entries:
            assert e.readiness_level in ALLOWED_READINESS_LEVELS
    def test_fermionic_blocked(self, result):
        f = [e for e in result.track_h_readiness.entries if "fermionic" in e.domain]
        assert f[0].readiness_level == "blocked"
    def test_binding_precondition(self, result):
        b = [e for e in result.track_h_readiness.entries if "binding" in e.domain]
        assert b[0].readiness_level == "precondition_only"

class TestTrackIProbability:
    def test_independent(self, result):
        assert result.track_i_probability.composite_independent_of_probability is True

class TestTrackJAppendixP:
    def test_no_native_canon(self, result):
        assert result.track_j_appendix_p.no_native_canon is True

class TestTrackKAuthorization:
    def test_authorized(self, result):
        assert result.track_k_authorization.re_authorized is True
    def test_verdict(self, result):
        assert result.track_k_authorization.authorization_verdict == RD_AUTHORIZATION_VERDICT

class TestHardGatedVerdicts:
    def test_all_exact(self, result):
        assert result.composite_verdict == RD_COMPOSITE_VERDICT
        assert result.binding_verdict == RD_BINDING_VERDICT
        assert result.pre_atomic_verdict == RD_PREATOMIC_VERDICT
        assert result.fermionic_boundary_verdict == RD_FERMIONIC_BOUNDARY_VERDICT
        assert result.authorization_verdict == RD_AUTHORIZATION_VERDICT
    def test_all_in_allowed(self, result):
        assert result.composite_verdict in ALLOWED_COMPOSITE_VERDICTS
        assert result.binding_verdict in ALLOWED_BINDING_VERDICTS
        assert result.pre_atomic_verdict in ALLOWED_PREATOMIC_VERDICTS
        assert result.fermionic_boundary_verdict in ALLOWED_FERMIONIC_VERDICTS
        assert result.authorization_verdict in ALLOWED_AUTHORIZATION_VERDICTS
    def test_all_distinct(self, result):
        v = {result.composite_verdict, result.binding_verdict,
             result.pre_atomic_verdict, result.fermionic_boundary_verdict,
             result.authorization_verdict}
        assert len(v) == 5

class TestMasterAudit:
    def test_valid(self, result):
        assert result.valid is True
    def test_claims(self, result):
        assert len(result.allowed_claims) == N_ALLOWED_CLAIMS
        assert len(result.forbidden_claims) == N_FORBIDDEN_CLAIMS
    def test_diagnostics(self, result):
        assert result.diagnostics["n_binding_provides"] == 0
        assert result.diagnostics["quantum_adds_matter"] == 0
        assert result.diagnostics["fermionic_obstruction_unchanged"] is True
    def test_idempotency(self):
        r1 = run_rd_composite_matter_preatomic_audit()
        r2 = run_rd_composite_matter_preatomic_audit()
        assert r1.composite_verdict == r2.composite_verdict
    def test_self_test(self):
        assert _self_test() is True
