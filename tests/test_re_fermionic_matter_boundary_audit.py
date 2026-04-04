"""Tests for Appendix R-E --- Fermionic Matter Boundary and Extension Routes."""
import pytest
from grut.re_fermionic_matter_boundary_audit import (
    N_INHERITANCE_ITEMS, N_REQUIREMENT_ITEMS, N_EXTENSION_ROUTES,
    N_QUANTUM_CHECKS, N_ORGANIZATION_ITEMS, N_BENCHMARK_CANDIDATES,
    N_READINESS_DOMAINS, N_APPENDIX_P_ENTRIES, N_RE_NONCLAIMS,
    N_ALLOWED_CLAIMS, N_FORBIDDEN_CLAIMS,
    RE_OBSTRUCTION_VERDICT, RE_ROUTE_VERDICT, RE_MATTER_ROLE_VERDICT,
    RE_READINESS_VERDICT, RE_AUTHORIZATION_VERDICT, RE_OVERALL_APPENDIX_P_CLASS,
    ALLOWED_OBSTRUCTION_VERDICTS, ALLOWED_ROUTE_VERDICTS,
    ALLOWED_MATTER_ROLE_VERDICTS, ALLOWED_READINESS_VERDICTS,
    ALLOWED_AUTHORIZATION_VERDICTS, ALLOWED_APPENDIX_P_CLASSES,
    ALLOWED_READINESS_LEVELS, RE_NONCLAIMS,
    run_re_fermionic_matter_boundary_audit, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_re_fermionic_matter_boundary_audit()

class TestREConstants:
    def test_counts(self):
        assert N_INHERITANCE_ITEMS == 5
        assert N_REQUIREMENT_ITEMS == 6
        assert N_EXTENSION_ROUTES == 4
        assert N_RE_NONCLAIMS == 8
    def test_nonclaims(self):
        assert len(RE_NONCLAIMS) == N_RE_NONCLAIMS
        for nc in RE_NONCLAIMS:
            assert nc.startswith("NOT_claiming_")
    def test_verdicts(self):
        assert RE_OBSTRUCTION_VERDICT == "fermionic_obstruction_unchanged"
        assert RE_ROUTE_VERDICT == "coherent_extension_routes_identified"
        assert RE_MATTER_ROLE_VERDICT == "fermionic_matter_needed_for_later_matter_organization"
        assert RE_READINESS_VERDICT == "fermionic_precondition_map_complete"
        assert RE_AUTHORIZATION_VERDICT == "authorized_to_proceed_to_RF"

class TestTrackAInheritance:
    def test_n_items(self, result):
        assert result.track_a_inheritance.n_items == N_INHERITANCE_ITEMS
    def test_none_changed(self, result):
        assert result.track_a_inheritance.any_changed is False
    def test_all_unchanged(self, result):
        for i in result.track_a_inheritance.items:
            assert i.changed_by_later_work is False

class TestTrackBRequirements:
    def test_n_items(self, result):
        assert result.track_b_requirements.n_items == N_REQUIREMENT_ITEMS
    def test_mostly_blocked(self, result):
        assert result.track_b_requirements.n_blocked >= 4
    def test_fr1_blocked(self, result):
        assert result.track_b_requirements.items[0].status == "blocked"
    def test_fr2_blocked(self, result):
        assert result.track_b_requirements.items[1].status == "blocked"

class TestTrackCRoutes:
    def test_n_routes(self, result):
        assert result.track_c_routes.n_routes == N_EXTENSION_ROUTES
    def test_n_viable(self, result):
        assert result.track_c_routes.n_viable == 3
    def test_er1_strongest(self, result):
        assert "ER1" in result.track_c_routes.strongest_route_id
    def test_er4_blocked(self, result):
        er4 = result.track_c_routes.routes[3]
        assert "blocked" in er4.viability

class TestTrackDQuantum:
    def test_zero_fermionic(self, result):
        assert result.track_d_quantum.n_adds_fermionic == 0

class TestTrackEOrganization:
    def test_all_need_fermionic(self, result):
        assert result.track_e_organization.n_needs_fermionic == N_ORGANIZATION_ITEMS

class TestTrackFBenchmark:
    def test_n_viable(self, result):
        assert result.track_f_benchmark.n_viable == 3
    def test_chosen_fb1(self, result):
        assert "FB1" in result.track_f_benchmark.chosen_id

class TestTrackGReadiness:
    def test_n_entries(self, result):
        assert result.track_g_readiness.n_entries == N_READINESS_DOMAINS
    def test_mostly_blocked(self, result):
        blocked = sum(1 for e in result.track_g_readiness.entries
                     if e.readiness_level == "blocked")
        assert blocked >= 5
    def test_route_clarity_extension(self, result):
        route = [e for e in result.track_g_readiness.entries
                if "route" in e.domain]
        assert route[0].readiness_level == "extension_ready"

class TestTrackHProbability:
    def test_independent(self, result):
        assert result.track_h_probability.fermionic_route_independent_of_probability is True

class TestTrackIAppendixP:
    def test_no_native_canon(self, result):
        assert result.track_i_appendix_p.no_native_canon is True
    def test_overall_bsr(self, result):
        assert result.track_i_appendix_p.overall_class == "bounded_structural_result"

class TestTrackJAuthorization:
    def test_authorized(self, result):
        assert result.track_j_authorization.rf_authorized is True

class TestHardGatedVerdicts:
    def test_all_exact(self, result):
        assert result.obstruction_verdict == RE_OBSTRUCTION_VERDICT
        assert result.route_verdict == RE_ROUTE_VERDICT
        assert result.matter_role_verdict == RE_MATTER_ROLE_VERDICT
        assert result.readiness_verdict == RE_READINESS_VERDICT
        assert result.authorization_verdict == RE_AUTHORIZATION_VERDICT
    def test_all_in_allowed(self, result):
        assert result.obstruction_verdict in ALLOWED_OBSTRUCTION_VERDICTS
        assert result.route_verdict in ALLOWED_ROUTE_VERDICTS
        assert result.matter_role_verdict in ALLOWED_MATTER_ROLE_VERDICTS
        assert result.readiness_verdict in ALLOWED_READINESS_VERDICTS
        assert result.authorization_verdict in ALLOWED_AUTHORIZATION_VERDICTS
    def test_all_distinct(self, result):
        v = {result.obstruction_verdict, result.route_verdict,
             result.matter_role_verdict, result.readiness_verdict,
             result.authorization_verdict}
        assert len(v) == 5

class TestMasterAudit:
    def test_valid(self, result):
        assert result.valid is True
    def test_claims(self, result):
        assert len(result.allowed_claims) == N_ALLOWED_CLAIMS
        assert len(result.forbidden_claims) == N_FORBIDDEN_CLAIMS
    def test_diagnostics(self, result):
        assert result.diagnostics["any_inheritance_changed"] is False
        assert result.diagnostics["quantum_adds_fermionic"] == 0
        assert result.diagnostics["n_organization_needs_fermionic"] == 4
        assert result.diagnostics["n_viable_routes"] == 3
    def test_idempotency(self):
        r1 = run_re_fermionic_matter_boundary_audit()
        r2 = run_re_fermionic_matter_boundary_audit()
        assert r1.obstruction_verdict == r2.obstruction_verdict
    def test_self_test(self):
        assert _self_test() is True
