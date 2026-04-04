"""
Tests for Appendix Q-II.F --- Probability, Determination, and Outcome Extensions
=================================================================================
"""

import pytest

from grut.qiif_probability_determination_outcome_audit import (
    TAU, GAMMA,
    N_ELIGIBILITY_INGREDIENTS, N_WEIGHT_CANDIDATES,
    N_DETERMINATION_LEVELS, N_OUTCOME_CANDIDATES,
    N_DECOHERENCE_BOUNDARY_TESTS, N_COMPOSITE_TESTS,
    N_MANYMODE_TESTS, N_EXTENSION_CANDIDATES,
    N_APPENDIX_P_ENTRIES, N_QIIF_NONCLAIMS,
    N_ALLOWED_CLAIMS, N_FORBIDDEN_CLAIMS,
    QIIF_PROBABILITY_VERDICT, QIIF_DETERMINATION_VERDICT,
    QIIF_OUTCOME_VERDICT, QIIF_EXTENSION_ROUTE_VERDICT,
    QIIF_AUTHORIZATION_VERDICT, QIIF_OVERALL_APPENDIX_P_CLASS,
    ALLOWED_PROBABILITY_VERDICTS, ALLOWED_DETERMINATION_VERDICTS,
    ALLOWED_OUTCOME_VERDICTS, ALLOWED_EXTENSION_ROUTE_VERDICTS,
    ALLOWED_AUTHORIZATION_VERDICTS, ALLOWED_APPENDIX_P_CLASSES,
    QIIF_NONCLAIMS,
    run_qiif_probability_determination_outcome_audit, _self_test,
)


@pytest.fixture(scope="module")
def result():
    return run_qiif_probability_determination_outcome_audit()


class TestQIIFConstants:
    def test_gamma_tau(self):
        assert abs(GAMMA * TAU - 1.0) < 1e-15

    def test_counts(self):
        assert N_ELIGIBILITY_INGREDIENTS == 5
        assert N_WEIGHT_CANDIDATES == 6
        assert N_DETERMINATION_LEVELS == 5
        assert N_OUTCOME_CANDIDATES == 6
        assert N_QIIF_NONCLAIMS == 8

    def test_nonclaims(self):
        assert len(QIIF_NONCLAIMS) == N_QIIF_NONCLAIMS
        for nc in QIIF_NONCLAIMS:
            assert nc.startswith("NOT_claiming_")

    def test_verdicts(self):
        assert QIIF_PROBABILITY_VERDICT == "diagnostic_weights_available_but_not_probabilities"
        assert QIIF_DETERMINATION_VERDICT == "decoherence_and_diagonal_dominance_only"
        assert QIIF_OUTCOME_VERDICT == "born_rule_and_outcome_selection_not_derived"
        assert QIIF_EXTENSION_ROUTE_VERDICT == "minimum_probability_extension_identified"
        assert QIIF_AUTHORIZATION_VERDICT == "authorized_to_proceed_to_QIIG"

    def test_overall_class(self):
        assert QIIF_OVERALL_APPENDIX_P_CLASS == "bounded_structural_result"

    def test_frozensets(self):
        for fs in [ALLOWED_PROBABILITY_VERDICTS, ALLOWED_DETERMINATION_VERDICTS,
                   ALLOWED_OUTCOME_VERDICTS, ALLOWED_EXTENSION_ROUTE_VERDICTS,
                   ALLOWED_AUTHORIZATION_VERDICTS]:
            assert len(fs) == 4


class TestTrackAEligibility:
    def test_n_ingredients(self, result):
        assert result.track_a_eligibility.n_ingredients == N_ELIGIBILITY_INGREDIENTS

    def test_n_present(self, result):
        assert result.track_a_eligibility.n_present == 2

    def test_n_absent(self, result):
        assert result.track_a_eligibility.n_absent == 2

    def test_n_extension(self, result):
        assert result.track_a_eligibility.n_extension_level == 1

    def test_pe1_present(self, result):
        assert result.track_a_eligibility.ingredients[0].status == "present"

    def test_pe3_absent(self, result):
        assert result.track_a_eligibility.ingredients[2].status == "absent"


class TestTrackBWeightVsProb:
    def test_n_candidates(self, result):
        assert result.track_b_weight_vs_prob.n_candidates == N_WEIGHT_CANDIDATES

    def test_n_diagnostic(self, result):
        assert result.track_b_weight_vs_prob.n_diagnostic == 4

    def test_n_effective(self, result):
        assert result.track_b_weight_vs_prob.n_effective_candidate == 1

    def test_wp1_diagnostic(self, result):
        wp1 = result.track_b_weight_vs_prob.candidates[0]
        assert wp1.status == "diagnostic_only"
        assert wp1.sum_to_one is True
        assert wp1.probability_without_born is False

    def test_wp4_effective(self, result):
        wp4 = result.track_b_weight_vs_prob.candidates[3]
        assert wp4.status == "effective_candidate"
        assert wp4.probability_without_born is False

    def test_verdict(self, result):
        assert result.track_b_weight_vs_prob.probability_verdict == QIIF_PROBABILITY_VERDICT


class TestTrackCDetermination:
    def test_n_levels(self, result):
        assert result.track_c_determination.n_levels == N_DETERMINATION_LEVELS

    def test_dt1_through_dt3_achieved(self, result):
        for i in range(3):
            assert result.track_c_determination.levels[i].achieved is True

    def test_dt4_not_achieved(self, result):
        assert result.track_c_determination.levels[3].achieved is False

    def test_highest_is_dt3(self, result):
        assert "DT3" in result.track_c_determination.highest_achieved_id

    def test_verdict(self, result):
        assert result.track_c_determination.determination_verdict == QIIF_DETERMINATION_VERDICT


class TestTrackDOutcome:
    def test_n_candidates(self, result):
        assert result.track_d_outcome.n_candidates == N_OUTCOME_CANDIDATES

    def test_born_not_derived(self, result):
        assert result.track_d_outcome.born_rule_derived is False

    def test_outcome_not_derived(self, result):
        assert result.track_d_outcome.outcome_selection_derived is False

    def test_os1_confirmed_absent(self, result):
        os1 = result.track_d_outcome.candidates[0]
        assert os1.status == "confirmed_absent"

    def test_os3_extension_level(self, result):
        os3 = result.track_d_outcome.candidates[2]
        assert os3.status == "extension_level"

    def test_verdict(self, result):
        assert result.track_d_outcome.outcome_verdict == QIIF_OUTCOME_VERDICT


class TestTrackEDecoherenceBoundary:
    def test_n_tests(self, result):
        assert result.track_e_decoherence_boundary.n_tests == N_DECOHERENCE_BOUNDARY_TESTS

    def test_not_sufficient(self, result):
        assert result.track_e_decoherence_boundary.decoherence_sufficient_for_probability is False

    def test_db1_confirmed(self, result):
        assert result.track_e_decoherence_boundary.tests[0].result == "confirmed"

    def test_db4_confirmed(self, result):
        assert result.track_e_decoherence_boundary.tests[3].result == "confirmed"


class TestTrackFComposite:
    def test_n_tests(self, result):
        assert result.track_f_composite.n_tests == N_COMPOSITE_TESTS

    def test_no_adds_content(self, result):
        # Only CP4 "adds content" (confirming no new probability)
        assert result.track_f_composite.n_adds_content == 1

    def test_cp4_confirmed(self, result):
        assert result.track_f_composite.tests[3].adds_probability_content is True


class TestTrackGManyMode:
    def test_n_tests(self, result):
        assert result.track_g_manymode.n_tests == N_MANYMODE_TESTS

    def test_mm4_confirmed(self, result):
        assert result.track_g_manymode.tests[3].adds_probability_content is True

    def test_no_probability_gain(self, result):
        # Only MM4 "adds" (confirming no new probability)
        assert result.track_g_manymode.n_adds_content == 1


class TestTrackHExtension:
    def test_n_candidates(self, result):
        assert result.track_h_extension.n_candidates == N_EXTENSION_CANDIDATES

    def test_n_viable(self, result):
        assert result.track_h_extension.n_viable == 2

    def test_chosen_px1(self, result):
        assert "PX1" in result.track_h_extension.chosen_candidate_id

    def test_px1_viable(self, result):
        px1 = result.track_h_extension.candidates[0]
        assert px1.viable is True
        assert px1.appendix_p_class == "motivated_independent_postulation"

    def test_px3_not_viable(self, result):
        px3 = result.track_h_extension.candidates[2]
        assert px3.viable is False

    def test_verdict(self, result):
        assert result.track_h_extension.extension_route_verdict == QIIF_EXTENSION_ROUTE_VERDICT


class TestTrackIAppendixP:
    def test_n_entries(self, result):
        assert result.track_i_appendix_p.n_entries == N_APPENDIX_P_ENTRIES

    def test_no_native_canon(self, result):
        assert result.track_i_appendix_p.no_native_canon is True

    def test_overall_bsr(self, result):
        assert result.track_i_appendix_p.overall_class == "bounded_structural_result"

    def test_all_valid(self, result):
        for e in result.track_i_appendix_p.entries:
            assert e.appendix_p_class in ALLOWED_APPENDIX_P_CLASSES

    def test_multiple_bsr(self, result):
        n = sum(1 for e in result.track_i_appendix_p.entries
                if e.appendix_p_class == "bounded_structural_result")
        assert n >= 3


class TestTrackJAuthorization:
    def test_authorized(self, result):
        assert result.track_j_authorization.qiig_authorized is True

    def test_verdict(self, result):
        assert result.track_j_authorization.authorization_verdict == QIIF_AUTHORIZATION_VERDICT

    def test_constraints_mention_born(self, result):
        text = " ".join(result.track_j_authorization.qiig_constraints).lower()
        assert "born" in text


class TestTrackKNonclaims:
    def test_count(self, result):
        assert result.track_k_nonclaims.n_nonclaims == N_QIIF_NONCLAIMS

    def test_registered(self, result):
        assert result.track_k_nonclaims.all_registered is True

    def test_mentions_born(self, result):
        text = " ".join(result.track_k_nonclaims.nonclaims).lower()
        assert "born" in text

    def test_mentions_decoherence(self, result):
        text = " ".join(result.track_k_nonclaims.nonclaims).lower()
        assert "decoherence" in text

    def test_mentions_outcome(self, result):
        text = " ".join(result.track_k_nonclaims.nonclaims).lower()
        assert "outcome" in text


class TestHardGatedVerdicts:
    def test_probability_exact(self, result):
        assert result.probability_verdict == QIIF_PROBABILITY_VERDICT

    def test_determination_exact(self, result):
        assert result.determination_verdict == QIIF_DETERMINATION_VERDICT

    def test_outcome_exact(self, result):
        assert result.outcome_verdict == QIIF_OUTCOME_VERDICT

    def test_extension_exact(self, result):
        assert result.extension_route_verdict == QIIF_EXTENSION_ROUTE_VERDICT

    def test_authorization_exact(self, result):
        assert result.authorization_verdict == QIIF_AUTHORIZATION_VERDICT

    def test_all_in_allowed(self, result):
        assert result.probability_verdict in ALLOWED_PROBABILITY_VERDICTS
        assert result.determination_verdict in ALLOWED_DETERMINATION_VERDICTS
        assert result.outcome_verdict in ALLOWED_OUTCOME_VERDICTS
        assert result.extension_route_verdict in ALLOWED_EXTENSION_ROUTE_VERDICTS
        assert result.authorization_verdict in ALLOWED_AUTHORIZATION_VERDICTS

    def test_all_distinct(self, result):
        v = {result.probability_verdict, result.determination_verdict,
             result.outcome_verdict, result.extension_route_verdict,
             result.authorization_verdict}
        assert len(v) == 5


class TestMasterAudit:
    def test_valid(self, result):
        assert result.valid is True

    def test_all_tracks(self, result):
        for attr in ['track_a_eligibility', 'track_b_weight_vs_prob',
                     'track_c_determination', 'track_d_outcome',
                     'track_e_decoherence_boundary', 'track_f_composite',
                     'track_g_manymode', 'track_h_extension',
                     'track_i_appendix_p', 'track_j_authorization',
                     'track_k_nonclaims']:
            assert getattr(result, attr) is not None

    def test_claims(self, result):
        assert len(result.allowed_claims) == N_ALLOWED_CLAIMS
        assert len(result.forbidden_claims) == N_FORBIDDEN_CLAIMS

    def test_nonclaims(self, result):
        assert len(result.exact_nonclaims) == N_QIIF_NONCLAIMS

    def test_diagnostics_born(self, result):
        assert result.diagnostics["born_rule_derived"] is False
        assert result.diagnostics["outcome_selection_derived"] is False
        assert result.diagnostics["decoherence_sufficient_for_probability"] is False

    def test_idempotency(self):
        r1 = run_qiif_probability_determination_outcome_audit()
        r2 = run_qiif_probability_determination_outcome_audit()
        assert r1.probability_verdict == r2.probability_verdict

    def test_self_test(self):
        assert _self_test() is True


class TestDoctrinalBoundaries:
    def test_no_born_claimed(self, result):
        for c in result.forbidden_claims:
            if "born" in c.lower():
                break
        else:
            pytest.fail("No forbidden claim about Born rule")

    def test_no_decoherence_probability(self, result):
        for c in result.forbidden_claims:
            if "decoherence" in c.lower() and "probabilit" in c.lower():
                break
        else:
            pytest.fail("No forbidden claim about decoherence -> probability")

    def test_no_outcome_from_pointer(self, result):
        for c in result.forbidden_claims:
            if "pointer" in c.lower() or "outcome" in c.lower():
                break
        else:
            pytest.fail("No forbidden claim about outcome from pointer")

    def test_diagnostic_in_allowed(self, result):
        text = " ".join(result.allowed_claims).lower()
        assert "diagnostic" in text

    def test_extension_route_in_allowed(self, result):
        text = " ".join(result.allowed_claims).lower()
        assert "extension" in text or "mip" in text
