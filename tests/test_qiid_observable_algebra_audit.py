"""
Tests for Appendix Q-II.D --- Observable Algebra and Multi-Observable Grammar
=============================================================================
"""

import math
import pytest

from grut.qiid_observable_algebra_audit import (
    TAU_SQ, TAU, GAMMA,
    COMPOSITE_HILBERT_DIM, SINGLE_SYSTEM_DIM,
    N_ELIGIBILITY_INGREDIENTS, N_CANDIDATE_OBSERVABLES,
    N_DISTINCTNESS_LEVELS, N_NONCOMMUTATIVITY_CANDIDATES,
    N_CORRELATOR_LEVELS, N_ALGEBRA_LEVELS,
    N_COMPOSITE_OBS_TESTS, N_BELL_READINESS_LEVELS,
    N_APPENDIX_P_ENTRIES, N_QIID_NONCLAIMS,
    N_ALLOWED_CLAIMS, N_FORBIDDEN_CLAIMS,
    QIID_OBSERVABLE_VERDICT, QIID_NONCOMMUTATIVITY_VERDICT,
    QIID_CORRELATOR_VERDICT, QIID_BELL_READINESS_VERDICT,
    QIID_AUTHORIZATION_VERDICT, QIID_OVERALL_APPENDIX_P_CLASS,
    ALLOWED_OBSERVABLE_VERDICTS, ALLOWED_NONCOMMUTATIVITY_VERDICTS,
    ALLOWED_CORRELATOR_VERDICTS, ALLOWED_BELL_READINESS_VERDICTS,
    ALLOWED_AUTHORIZATION_VERDICTS, ALLOWED_APPENDIX_P_CLASSES,
    QIID_NONCLAIMS,
    run_qiid_observable_algebra_audit, _self_test,
)


@pytest.fixture(scope="module")
def result():
    return run_qiid_observable_algebra_audit()


class TestQIIDConstants:
    def test_gamma_tau(self):
        assert abs(GAMMA * TAU - 1.0) < 1e-15

    def test_n_eligibility(self):
        assert N_ELIGIBILITY_INGREDIENTS == 5

    def test_n_candidates(self):
        assert N_CANDIDATE_OBSERVABLES == 6

    def test_n_nonclaims(self):
        assert N_QIID_NONCLAIMS == 8

    def test_nonclaims_length(self):
        assert len(QIID_NONCLAIMS) == N_QIID_NONCLAIMS

    def test_all_nonclaims_start_not_claiming(self):
        for nc in QIID_NONCLAIMS:
            assert nc.startswith("NOT_claiming_")

    def test_verdict_constants(self):
        assert QIID_OBSERVABLE_VERDICT == "multiple_observable_classes_extension_level_only"
        assert QIID_NONCOMMUTATIVITY_VERDICT == "toy_noncommuting_pair_justified"
        assert QIID_CORRELATOR_VERDICT == "correlator_grammar_extension_level_only"
        assert QIID_BELL_READINESS_VERDICT == "bell_boundary_structurally_advanced"
        assert QIID_AUTHORIZATION_VERDICT == "authorized_to_proceed_to_QIIE"

    def test_frozenset_sizes(self):
        assert len(ALLOWED_OBSERVABLE_VERDICTS) == 4
        assert len(ALLOWED_NONCOMMUTATIVITY_VERDICTS) == 4
        assert len(ALLOWED_CORRELATOR_VERDICTS) == 4
        assert len(ALLOWED_BELL_READINESS_VERDICTS) == 4
        assert len(ALLOWED_AUTHORIZATION_VERDICTS) == 4


class TestTrackAEligibility:
    def test_n_ingredients(self, result):
        assert result.track_a_eligibility.n_ingredients == N_ELIGIBILITY_INGREDIENTS

    def test_n_present(self, result):
        assert result.track_a_eligibility.n_present == 3

    def test_n_extension(self, result):
        assert result.track_a_eligibility.n_extension_level == 2

    def test_n_absent(self, result):
        assert result.track_a_eligibility.n_absent == 0

    def test_oe1_present(self, result):
        oe1 = result.track_a_eligibility.ingredients[0]
        assert oe1.status == "present"

    def test_oe2_extension(self, result):
        oe2 = result.track_a_eligibility.ingredients[1]
        assert oe2.status == "extension_level"


class TestTrackBCandidates:
    def test_n_candidates(self, result):
        assert result.track_b_candidates.n_candidates == N_CANDIDATE_OBSERVABLES

    def test_n_motivated(self, result):
        assert result.track_b_candidates.n_motivated == 2

    def test_n_compatible(self, result):
        assert result.track_b_candidates.n_compatible == 2

    def test_n_underdetermined(self, result):
        assert result.track_b_candidates.n_underdetermined == 1

    def test_obs1_motivated(self, result):
        obs1 = result.track_b_candidates.candidates[0]
        assert obs1.candidate_id == "OBS1"
        assert obs1.motivation_level == "motivated"

    def test_obs2_compatible(self, result):
        obs2 = result.track_b_candidates.candidates[1]
        assert obs2.candidate_id == "OBS2"
        assert obs2.motivation_level == "compatible"

    def test_obs4_underdetermined(self, result):
        obs4 = result.track_b_candidates.candidates[3]
        assert obs4.candidate_id == "OBS4"
        assert obs4.motivation_level == "underdetermined"

    def test_obs5_motivated(self, result):
        obs5 = result.track_b_candidates.candidates[4]
        assert obs5.candidate_id == "OBS5"
        assert obs5.motivation_level == "motivated"

    def test_all_ids_unique(self, result):
        ids = [c.candidate_id for c in result.track_b_candidates.candidates]
        assert len(ids) == len(set(ids))


class TestTrackCDistinctness:
    def test_n_levels(self, result):
        assert result.track_c_distinctness.n_levels == N_DISTINCTNESS_LEVELS

    def test_strongest_is_dl4(self, result):
        assert "DL4" in result.track_c_distinctness.strongest_distinctness

    def test_dl3_empty(self, result):
        dl3 = result.track_c_distinctness.levels[2]
        assert "NONE" in " ".join(dl3.applies_to) or "none" in " ".join(dl3.applies_to).lower()


class TestTrackDNoncommutativity:
    def test_n_candidates(self, result):
        assert result.track_d_noncommutativity.n_candidates == N_NONCOMMUTATIVITY_CANDIDATES

    def test_nc2_justified(self, result):
        nc2 = result.track_d_noncommutativity.candidates[1]
        assert nc2.justified is True
        assert nc2.level == "toy"

    def test_nc3_justified(self, result):
        nc3 = result.track_d_noncommutativity.candidates[2]
        assert nc3.justified is True

    def test_nc1_not_justified(self, result):
        nc1 = result.track_d_noncommutativity.candidates[0]
        assert nc1.justified is False

    def test_chosen_nc2(self, result):
        assert "NC2" in result.track_d_noncommutativity.justified_candidate_id

    def test_commutator_formula(self, result):
        assert "sigma_z" in result.track_d_noncommutativity.commutator_formula
        assert "sigma_x" in result.track_d_noncommutativity.commutator_formula
        assert "sigma_y" in result.track_d_noncommutativity.commutator_formula

    def test_verdict(self, result):
        assert result.track_d_noncommutativity.noncommutativity_verdict == QIID_NONCOMMUTATIVITY_VERDICT


class TestTrackECorrelator:
    def test_n_levels(self, result):
        assert result.track_e_correlator.n_levels == N_CORRELATOR_LEVELS

    def test_cg1_through_cg4_available(self, result):
        for i in range(4):
            assert result.track_e_correlator.levels[i].available is True

    def test_cg5_not_available(self, result):
        cg5 = result.track_e_correlator.levels[4]
        assert cg5.available is False

    def test_highest_is_cg4(self, result):
        assert "CG4" in result.track_e_correlator.highest_available_id

    def test_verdict(self, result):
        assert result.track_e_correlator.correlator_verdict == QIID_CORRELATOR_VERDICT


class TestTrackFAlgebra:
    def test_n_levels(self, result):
        assert result.track_f_algebra.n_levels == N_ALGEBRA_LEVELS

    def test_al1_through_al4_achieved(self, result):
        for i in range(4):
            assert result.track_f_algebra.levels[i].achieved is True

    def test_al5_not_achieved(self, result):
        assert result.track_f_algebra.levels[4].achieved is False

    def test_highest_is_al4(self, result):
        assert "AL4" in result.track_f_algebra.highest_achieved_id


class TestTrackGCompositeObs:
    def test_n_tests(self, result):
        assert result.track_g_composite_obs.n_tests == N_COMPOSITE_OBS_TESTS

    def test_all_available(self, result):
        assert result.track_g_composite_obs.n_available == N_COMPOSITE_OBS_TESTS

    def test_co1_product(self, result):
        assert result.track_g_composite_obs.tests[0].available is True


class TestTrackHBellReadiness:
    def test_n_levels(self, result):
        assert result.track_h_bell_readiness.n_levels == N_BELL_READINESS_LEVELS

    def test_br1_achieved(self, result):
        assert result.track_h_bell_readiness.levels[0].achieved is True

    def test_br2_achieved(self, result):
        assert result.track_h_bell_readiness.levels[1].achieved is True

    def test_br3_not_achieved(self, result):
        assert result.track_h_bell_readiness.levels[2].achieved is False

    def test_br4_not_achieved(self, result):
        assert result.track_h_bell_readiness.levels[3].achieved is False

    def test_remaining_gap_born(self, result):
        assert "born" in result.track_h_bell_readiness.remaining_gap.lower()

    def test_verdict(self, result):
        assert result.track_h_bell_readiness.bell_readiness_verdict == QIID_BELL_READINESS_VERDICT


class TestTrackIAppendixP:
    def test_n_entries(self, result):
        assert result.track_i_appendix_p.n_entries == N_APPENDIX_P_ENTRIES

    def test_no_native_canon(self, result):
        assert result.track_i_appendix_p.no_native_canon is True

    def test_overall_class(self, result):
        assert result.track_i_appendix_p.overall_class == QIID_OVERALL_APPENDIX_P_CLASS

    def test_all_classes_valid(self, result):
        for e in result.track_i_appendix_p.entries:
            assert e.appendix_p_class in ALLOWED_APPENDIX_P_CLASSES

    def test_at_least_one_bsr(self, result):
        n = sum(1 for e in result.track_i_appendix_p.entries
                if e.appendix_p_class == "bounded_structural_result")
        assert n >= 1


class TestTrackJAuthorization:
    def test_authorized(self, result):
        assert result.track_j_authorization.qiie_authorized is True

    def test_verdict(self, result):
        assert result.track_j_authorization.authorization_verdict == QIID_AUTHORIZATION_VERDICT

    def test_basis_length(self, result):
        assert len(result.track_j_authorization.authorization_basis) >= 3

    def test_constraints_length(self, result):
        assert len(result.track_j_authorization.qiie_constraints) >= 3


class TestTrackKNonclaims:
    def test_count(self, result):
        assert result.track_k_nonclaims.n_nonclaims == N_QIID_NONCLAIMS

    def test_registered(self, result):
        assert result.track_k_nonclaims.all_registered is True

    def test_all_start_not_claiming(self, result):
        for nc in result.track_k_nonclaims.nonclaims:
            assert nc.startswith("NOT_claiming_")

    def test_mentions_bell(self, result):
        text = " ".join(result.track_k_nonclaims.nonclaims).lower()
        assert "bell" in text

    def test_mentions_native_canon(self, result):
        text = " ".join(result.track_k_nonclaims.nonclaims).lower()
        assert "native_canon" in text or "native canon" in text


class TestHardGatedVerdicts:
    def test_observable_exact(self, result):
        assert result.observable_verdict == QIID_OBSERVABLE_VERDICT

    def test_noncommutativity_exact(self, result):
        assert result.noncommutativity_verdict == QIID_NONCOMMUTATIVITY_VERDICT

    def test_correlator_exact(self, result):
        assert result.correlator_verdict == QIID_CORRELATOR_VERDICT

    def test_bell_exact(self, result):
        assert result.bell_readiness_verdict == QIID_BELL_READINESS_VERDICT

    def test_authorization_exact(self, result):
        assert result.authorization_verdict == QIID_AUTHORIZATION_VERDICT

    def test_all_in_allowed(self, result):
        assert result.observable_verdict in ALLOWED_OBSERVABLE_VERDICTS
        assert result.noncommutativity_verdict in ALLOWED_NONCOMMUTATIVITY_VERDICTS
        assert result.correlator_verdict in ALLOWED_CORRELATOR_VERDICTS
        assert result.bell_readiness_verdict in ALLOWED_BELL_READINESS_VERDICTS
        assert result.authorization_verdict in ALLOWED_AUTHORIZATION_VERDICTS

    def test_all_five_distinct(self, result):
        v = {result.observable_verdict, result.noncommutativity_verdict,
             result.correlator_verdict, result.bell_readiness_verdict,
             result.authorization_verdict}
        assert len(v) == 5

    def test_appendix_p(self, result):
        assert result.qiid_appendix_p_class in ALLOWED_APPENDIX_P_CLASSES


class TestMasterAudit:
    def test_valid(self, result):
        assert result.valid is True

    def test_all_tracks(self, result):
        for attr in ['track_a_eligibility', 'track_b_candidates', 'track_c_distinctness',
                     'track_d_noncommutativity', 'track_e_correlator', 'track_f_algebra',
                     'track_g_composite_obs', 'track_h_bell_readiness',
                     'track_i_appendix_p', 'track_j_authorization', 'track_k_nonclaims']:
            assert getattr(result, attr) is not None

    def test_claims(self, result):
        assert len(result.allowed_claims) == N_ALLOWED_CLAIMS
        assert len(result.forbidden_claims) == N_FORBIDDEN_CLAIMS

    def test_nonclaims(self, result):
        assert len(result.exact_nonclaims) == N_QIID_NONCLAIMS

    def test_tsirelson(self, result):
        assert abs(result.diagnostics["tsirelson_value"] - 2 * math.sqrt(2)) < 1e-12

    def test_commutator(self, result):
        assert "sigma" in result.diagnostics["commutator_formula"]

    def test_idempotency(self):
        r1 = run_qiid_observable_algebra_audit()
        r2 = run_qiid_observable_algebra_audit()
        assert r1.valid == r2.valid
        assert r1.observable_verdict == r2.observable_verdict

    def test_self_test(self):
        assert _self_test() is True


class TestDoctrinalBoundaries:
    def test_no_full_algebra_claim(self, result):
        for c in result.forbidden_claims:
            if "full" in c.lower() and "algebra" in c.lower():
                break
        else:
            pytest.fail("No forbidden claim about full algebra")

    def test_no_bell_achieved(self, result):
        for c in result.forbidden_claims:
            if "bell" in c.lower():
                break
        else:
            pytest.fail("No forbidden claim about Bell")

    def test_no_native_canon(self, result):
        for c in result.forbidden_claims:
            if "native canon" in c.lower() or "native_canon" in c.lower():
                break
        else:
            pytest.fail("No forbidden claim about native canon")

    def test_toy_pair_in_allowed(self, result):
        text = " ".join(result.allowed_claims).lower()
        assert "noncommuting" in text or "commutator" in text

    def test_qe3_resolution_in_allowed(self, result):
        text = " ".join(result.allowed_claims).lower()
        assert "qe3" in text
