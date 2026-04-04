"""Tests for Appendix R-B --- Bosonic Objecthood and Localization."""
import pytest
from grut.rb_bosonic_objecthood_localization_audit import (
    N_OBJECTHOOD_CRITERIA, N_LOCALIZATION_CANDIDATES, N_PERSISTENCE_CANDIDATES,
    N_MNO_ITEMS, N_QUANTUM_CONTRIBUTIONS, N_BENCHMARK_CANDIDATES,
    N_READINESS_DOMAINS, N_PROBABILITY_TESTS, N_APPENDIX_P_ENTRIES,
    N_RB_NONCLAIMS, N_ALLOWED_CLAIMS, N_FORBIDDEN_CLAIMS,
    RB_LOCALIZATION_VERDICT, RB_PERSISTENCE_VERDICT,
    RB_OBJECTHOOD_VERDICT, RB_TOPOLOGICAL_ROUTE_VERDICT,
    RB_AUTHORIZATION_VERDICT, RB_OVERALL_APPENDIX_P_CLASS,
    ALLOWED_LOCALIZATION_VERDICTS, ALLOWED_PERSISTENCE_VERDICTS,
    ALLOWED_OBJECTHOOD_VERDICTS, ALLOWED_TOPOLOGICAL_VERDICTS,
    ALLOWED_AUTHORIZATION_VERDICTS, ALLOWED_APPENDIX_P_CLASSES,
    ALLOWED_READINESS_LEVELS, RB_NONCLAIMS,
    run_rb_bosonic_objecthood_localization_audit, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_rb_bosonic_objecthood_localization_audit()

class TestRBConstants:
    def test_counts(self):
        assert N_OBJECTHOOD_CRITERIA == 6
        assert N_LOCALIZATION_CANDIDATES == 6
        assert N_PERSISTENCE_CANDIDATES == 6
        assert N_MNO_ITEMS == 5
        assert N_RB_NONCLAIMS == 8
    def test_nonclaims(self):
        assert len(RB_NONCLAIMS) == N_RB_NONCLAIMS
        for nc in RB_NONCLAIMS:
            assert nc.startswith("NOT_claiming_")
    def test_verdicts(self):
        assert RB_LOCALIZATION_VERDICT == "shell_and_excitation_localization_only"
        assert RB_PERSISTENCE_VERDICT == "persistence_criteria_partially_satisfied"
        assert RB_OBJECTHOOD_VERDICT == "bosonic_objecthood_structurally_plausible_but_unbuilt"
        assert RB_TOPOLOGICAL_ROUTE_VERDICT == "topological_object_route_motivated_but_unbuilt"
        assert RB_AUTHORIZATION_VERDICT == "authorized_to_proceed_to_RC"
    def test_frozensets(self):
        for fs in [ALLOWED_LOCALIZATION_VERDICTS, ALLOWED_PERSISTENCE_VERDICTS,
                   ALLOWED_OBJECTHOOD_VERDICTS, ALLOWED_TOPOLOGICAL_VERDICTS,
                   ALLOWED_AUTHORIZATION_VERDICTS]:
            assert len(fs) == 4

class TestTrackAObjecthood:
    def test_n_criteria(self, result):
        assert result.track_a_objecthood.n_criteria == N_OBJECTHOOD_CRITERIA
    def test_stability_not_satisfied(self, result):
        oc5 = result.track_a_objecthood.criteria[4]
        assert oc5.currently_satisfied == "not_satisfied"
    def test_localization_partial(self, result):
        oc1 = result.track_a_objecthood.criteria[0]
        assert oc1.currently_satisfied == "partially"

class TestTrackBLocalization:
    def test_n_candidates(self, result):
        assert result.track_b_localization.n_candidates == N_LOCALIZATION_CANDIDATES
    def test_n_available(self, result):
        assert result.track_b_localization.n_available == 4
    def test_verdict(self, result):
        assert result.track_b_localization.localization_verdict == RB_LOCALIZATION_VERDICT
    def test_lc1_profile(self, result):
        assert result.track_b_localization.candidates[0].localization_type == "profile_only"
    def test_lc3_topological(self, result):
        assert result.track_b_localization.candidates[2].localization_type == "topological"

class TestTrackCPersistence:
    def test_n_candidates(self, result):
        assert result.track_c_persistence.n_candidates == N_PERSISTENCE_CANDIDATES
    def test_n_satisfied(self, result):
        assert result.track_c_persistence.n_satisfied == 3
    def test_excitation_transient(self, result):
        ps3 = result.track_c_persistence.candidates[2]
        assert ps3.satisfied is False
        assert ps3.level == "transient"
    def test_verdict(self, result):
        assert result.track_c_persistence.persistence_verdict == RB_PERSISTENCE_VERDICT

class TestTrackDMNO:
    def test_n_items(self, result):
        assert result.track_d_mno.n_items == N_MNO_ITEMS
    def test_none_changed(self, result):
        assert result.track_d_mno.any_changed is False
    def test_all_unchanged(self, result):
        for item in result.track_d_mno.items:
            assert item.changed_by_q is False

class TestTrackEQuantum:
    def test_n_contributions(self, result):
        assert result.track_e_quantum.n_contributions == N_QUANTUM_CONTRIBUTIONS
    def test_zero_objecthood(self, result):
        assert result.track_e_quantum.n_adds_objecthood == 0

class TestTrackFBenchmark:
    def test_n_candidates(self, result):
        assert result.track_f_benchmark.n_candidates == N_BENCHMARK_CANDIDATES
    def test_n_viable(self, result):
        assert result.track_f_benchmark.n_viable == 3
    def test_chosen_ob1(self, result):
        assert "OB1" in result.track_f_benchmark.chosen_id
    def test_ob1_no_particle(self, result):
        ob1 = result.track_f_benchmark.candidates[0]
        not_d = " ".join(ob1.does_not_demonstrate).lower()
        assert "particle" in not_d or "stability" in not_d

class TestTrackGReadiness:
    def test_n_entries(self, result):
        assert result.track_g_readiness.n_entries == N_READINESS_DOMAINS
    def test_all_valid_levels(self, result):
        for e in result.track_g_readiness.entries:
            assert e.readiness_level in ALLOWED_READINESS_LEVELS
    def test_particle_precondition(self, result):
        p = [e for e in result.track_g_readiness.entries if "particle" in e.domain]
        assert len(p) == 1
        assert p[0].readiness_level == "precondition_only"

class TestTrackHProbability:
    def test_independent(self, result):
        assert result.track_h_probability.objecthood_independent_of_probability is True

class TestTrackIAppendixP:
    def test_n_entries(self, result):
        assert result.track_i_appendix_p.n_entries == N_APPENDIX_P_ENTRIES
    def test_no_native_canon(self, result):
        assert result.track_i_appendix_p.no_native_canon is True
    def test_all_valid(self, result):
        for e in result.track_i_appendix_p.entries:
            assert e.appendix_p_class in ALLOWED_APPENDIX_P_CLASSES

class TestTrackJAuthorization:
    def test_authorized(self, result):
        assert result.track_j_authorization.rc_authorized is True
    def test_verdict(self, result):
        assert result.track_j_authorization.authorization_verdict == RB_AUTHORIZATION_VERDICT
    def test_constraints_mention_stability(self, result):
        text = " ".join(result.track_j_authorization.rc_constraints).lower()
        assert "stability" in text or "skyrme" in text

class TestTrackKNonclaims:
    def test_count(self, result):
        assert result.track_k_nonclaims.n_nonclaims == N_RB_NONCLAIMS
    def test_registered(self, result):
        assert result.track_k_nonclaims.all_registered is True
    def test_mentions_particle(self, result):
        text = " ".join(result.track_k_nonclaims.nonclaims).lower()
        assert "particle" in text
    def test_mentions_fermionic(self, result):
        text = " ".join(result.track_k_nonclaims.nonclaims).lower()
        assert "fermionic" in text

class TestHardGatedVerdicts:
    def test_all_exact(self, result):
        assert result.localization_verdict == RB_LOCALIZATION_VERDICT
        assert result.persistence_verdict == RB_PERSISTENCE_VERDICT
        assert result.objecthood_verdict == RB_OBJECTHOOD_VERDICT
        assert result.topological_route_verdict == RB_TOPOLOGICAL_ROUTE_VERDICT
        assert result.authorization_verdict == RB_AUTHORIZATION_VERDICT
    def test_all_in_allowed(self, result):
        assert result.localization_verdict in ALLOWED_LOCALIZATION_VERDICTS
        assert result.persistence_verdict in ALLOWED_PERSISTENCE_VERDICTS
        assert result.objecthood_verdict in ALLOWED_OBJECTHOOD_VERDICTS
        assert result.topological_route_verdict in ALLOWED_TOPOLOGICAL_VERDICTS
        assert result.authorization_verdict in ALLOWED_AUTHORIZATION_VERDICTS
    def test_all_distinct(self, result):
        v = {result.localization_verdict, result.persistence_verdict,
             result.objecthood_verdict, result.topological_route_verdict,
             result.authorization_verdict}
        assert len(v) == 5

class TestMasterAudit:
    def test_valid(self, result):
        assert result.valid is True
    def test_claims(self, result):
        assert len(result.allowed_claims) == N_ALLOWED_CLAIMS
        assert len(result.forbidden_claims) == N_FORBIDDEN_CLAIMS
    def test_nonclaims(self, result):
        assert len(result.exact_nonclaims) == N_RB_NONCLAIMS
    def test_diagnostics(self, result):
        assert result.diagnostics["mno_any_changed"] is False
        assert result.diagnostics["quantum_adds_objecthood"] == 0
    def test_idempotency(self):
        r1 = run_rb_bosonic_objecthood_localization_audit()
        r2 = run_rb_bosonic_objecthood_localization_audit()
        assert r1.objecthood_verdict == r2.objecthood_verdict
    def test_self_test(self):
        assert _self_test() is True

class TestDoctrinalBoundaries:
    def test_no_particle_claim(self, result):
        for c in result.forbidden_claims:
            if "particle" in c.lower():
                break
        else:
            pytest.fail("No forbidden claim about particles")
    def test_no_native_canon(self, result):
        for c in result.forbidden_claims:
            if "native canon" in c.lower() or "native_canon" in c.lower():
                break
        else:
            pytest.fail("No forbidden claim about native canon")
