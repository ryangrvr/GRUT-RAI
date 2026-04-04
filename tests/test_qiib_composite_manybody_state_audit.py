"""
Tests for Appendix Q-II.B --- Composite and Many-Body State Structure Audit
===========================================================================
"""

import math
import pytest

from grut.qiib_composite_manybody_state_audit import (
    TAU_SQ, TAU, GAMMA,
    COMPOSITE_HILBERT_DIM, SINGLE_SYSTEM_DIM, N_SUBSYSTEMS_BENCHMARK,
    N_ELIGIBILITY_INGREDIENTS, N_SUBSYSTEM_CANDIDATES,
    N_COMPOSITION_CANDIDATES, N_REDUCED_STATE_CANDIDATES,
    N_MANY_BODY_LEVELS, N_DECOHERENCE_CHECKS,
    N_BENCHMARK_CANDIDATES, N_APPENDIX_P_ENTRIES,
    N_QIIB_NONCLAIMS, N_ALLOWED_CLAIMS, N_FORBIDDEN_CLAIMS,
    QII0_INHERITED, QIIA_INHERITED, QF_INHERITED_CLOSURE,
    QIIB_SUBSYSTEM_VERDICT, QIIB_COMPOSITION_VERDICT,
    QIIB_REDUCED_STATE_VERDICT, QIIB_MANY_BODY_VERDICT,
    QIIB_AUTHORIZATION_VERDICT, QIIB_OVERALL_APPENDIX_P_CLASS,
    ALLOWED_SUBSYSTEM_VERDICTS, ALLOWED_COMPOSITION_VERDICTS,
    ALLOWED_REDUCED_STATE_VERDICTS, ALLOWED_MANY_BODY_VERDICTS,
    ALLOWED_AUTHORIZATION_VERDICTS, ALLOWED_APPENDIX_P_CLASSES,
    QIIB_NONCLAIMS,
    run_qiib_composite_manybody_state_audit, _self_test,
)


@pytest.fixture(scope="module")
def result():
    return run_qiib_composite_manybody_state_audit()


# ===========================================================================
# TestQIIBConstants
# ===========================================================================

class TestQIIBConstants:
    def test_tau_sq(self):
        assert TAU_SQ == 1.5

    def test_gamma_tau(self):
        assert abs(GAMMA * TAU - 1.0) < 1e-15

    def test_composite_dim(self):
        assert COMPOSITE_HILBERT_DIM == 4

    def test_single_dim(self):
        assert SINGLE_SYSTEM_DIM == 2

    def test_dim_product(self):
        assert COMPOSITE_HILBERT_DIM == SINGLE_SYSTEM_DIM ** N_SUBSYSTEMS_BENCHMARK

    def test_n_subsystems(self):
        assert N_SUBSYSTEMS_BENCHMARK == 2

    def test_n_eligibility(self):
        assert N_ELIGIBILITY_INGREDIENTS == 5

    def test_n_subsystem_candidates(self):
        assert N_SUBSYSTEM_CANDIDATES == 5

    def test_n_composition_candidates(self):
        assert N_COMPOSITION_CANDIDATES == 5

    def test_n_reduced_state_candidates(self):
        assert N_REDUCED_STATE_CANDIDATES == 4

    def test_n_many_body_levels(self):
        assert N_MANY_BODY_LEVELS == 4

    def test_n_decoherence_checks(self):
        assert N_DECOHERENCE_CHECKS == 4

    def test_n_benchmark_candidates(self):
        assert N_BENCHMARK_CANDIDATES == 4

    def test_n_appendix_p_entries(self):
        assert N_APPENDIX_P_ENTRIES == 7

    def test_n_nonclaims(self):
        assert N_QIIB_NONCLAIMS == 8

    def test_nonclaims_length(self):
        assert len(QIIB_NONCLAIMS) == N_QIIB_NONCLAIMS

    def test_all_nonclaims_start_with_not_claiming(self):
        for nc in QIIB_NONCLAIMS:
            assert nc.startswith("NOT_claiming_")

    def test_subsystem_verdict_constant(self):
        assert QIIB_SUBSYSTEM_VERDICT == "subsystem_identity_extension_level_only"

    def test_composition_verdict_constant(self):
        assert QIIB_COMPOSITION_VERDICT == "composition_rule_extension_level_only"

    def test_reduced_state_verdict_constant(self):
        assert QIIB_REDUCED_STATE_VERDICT == "reduced_state_map_extension_level_only"

    def test_many_body_verdict_constant(self):
        assert QIIB_MANY_BODY_VERDICT == "two_subsystem_grammar_demonstrated"

    def test_authorization_verdict_constant(self):
        assert QIIB_AUTHORIZATION_VERDICT == "authorized_to_proceed_to_QIIC"

    def test_overall_class(self):
        assert QIIB_OVERALL_APPENDIX_P_CLASS == "motivated_but_unbuilt"

    def test_frozenset_sizes(self):
        assert len(ALLOWED_SUBSYSTEM_VERDICTS) == 4
        assert len(ALLOWED_COMPOSITION_VERDICTS) == 4
        assert len(ALLOWED_REDUCED_STATE_VERDICTS) == 4
        assert len(ALLOWED_MANY_BODY_VERDICTS) == 4
        assert len(ALLOWED_AUTHORIZATION_VERDICTS) == 4
        assert len(ALLOWED_APPENDIX_P_CLASSES) == 8

    def test_inherited_verdicts(self):
        assert "gap_inventory_complete" in QII0_INHERITED
        assert "authorized_and_staged" in QIIA_INHERITED
        assert "close_first_wave" in QF_INHERITED_CLOSURE


# ===========================================================================
# TestTrackAEligibility
# ===========================================================================

class TestTrackAEligibility:
    def test_n_ingredients(self, result):
        assert result.track_a_eligibility.n_ingredients == N_ELIGIBILITY_INGREDIENTS

    def test_ingredients_count(self, result):
        assert len(result.track_a_eligibility.ingredients) == N_ELIGIBILITY_INGREDIENTS

    def test_all_extension_level(self, result):
        assert result.track_a_eligibility.n_extension_level == N_ELIGIBILITY_INGREDIENTS

    def test_n_present_zero(self, result):
        assert result.track_a_eligibility.n_present == 0

    def test_n_absent_zero(self, result):
        assert result.track_a_eligibility.n_absent == 0

    def test_eligibility_verdict(self, result):
        assert result.track_a_eligibility.eligibility_verdict == "eligible_at_extension_level"

    def test_all_ids_unique(self, result):
        ids = [i.ingredient_id for i in result.track_a_eligibility.ingredients]
        assert len(ids) == len(set(ids))

    def test_ce1_subsystem_labels(self, result):
        ce1 = result.track_a_eligibility.ingredients[0]
        assert ce1.ingredient_id == "CE1"
        assert ce1.status == "extension_level"

    def test_ce3_composition_rule(self, result):
        ce3 = result.track_a_eligibility.ingredients[2]
        assert ce3.ingredient_id == "CE3"
        assert "tensor" in ce3.description.lower() or "composition" in ce3.description.lower()


# ===========================================================================
# TestTrackBSubsystem
# ===========================================================================

class TestTrackBSubsystem:
    def test_n_candidates(self, result):
        assert result.track_b_subsystem.n_candidates == N_SUBSYSTEM_CANDIDATES

    def test_candidates_count(self, result):
        assert len(result.track_b_subsystem.candidates) == N_SUBSYSTEM_CANDIDATES

    def test_n_viable(self, result):
        assert result.track_b_subsystem.n_viable == 1

    def test_chosen_ss1(self, result):
        assert "SS1" in result.track_b_subsystem.chosen_candidate_id

    def test_subsystem_verdict(self, result):
        assert result.track_b_subsystem.subsystem_verdict == QIIB_SUBSYSTEM_VERDICT

    def test_ss1_viable(self, result):
        ss1 = result.track_b_subsystem.candidates[0]
        assert ss1.candidate_id == "SS1"
        assert ss1.viable is True
        assert ss1.viability_level == "extension_level"

    def test_ss2_blocked(self, result):
        ss2 = result.track_b_subsystem.candidates[1]
        assert ss2.candidate_id == "SS2"
        assert ss2.viable is False
        assert "spatial" in ss2.obstruction_if_not.lower()

    def test_ss3_blocked(self, result):
        ss3 = result.track_b_subsystem.candidates[2]
        assert ss3.candidate_id == "SS3"
        assert ss3.viable is False

    def test_ss4_circular(self, result):
        ss4 = result.track_b_subsystem.candidates[3]
        assert ss4.viable is False
        assert "circular" in ss4.viability_level.lower()

    def test_ss5_rejected(self, result):
        ss5 = result.track_b_subsystem.candidates[4]
        assert ss5.viable is False

    def test_only_one_viable(self, result):
        viable = [c for c in result.track_b_subsystem.candidates if c.viable]
        assert len(viable) == 1
        assert viable[0].candidate_id == "SS1"


# ===========================================================================
# TestTrackCComposition
# ===========================================================================

class TestTrackCComposition:
    def test_n_candidates(self, result):
        assert result.track_c_composition.n_candidates == N_COMPOSITION_CANDIDATES

    def test_chosen_cr1(self, result):
        assert "CR1" in result.track_c_composition.chosen_candidate_id

    def test_composition_verdict(self, result):
        assert result.track_c_composition.composition_verdict == QIIB_COMPOSITION_VERDICT

    def test_cr1_coherent(self, result):
        cr1 = result.track_c_composition.candidates[0]
        assert cr1.candidate_id == "CR1"
        assert cr1.coherent is True
        assert cr1.appendix_p_class == "motivated_independent_postulation"

    def test_cr2_coherent_but_limiting(self, result):
        cr2 = result.track_c_composition.candidates[1]
        assert cr2.coherent is True
        assert cr2.appendix_p_class == "compatible_but_ad_hoc"

    def test_cr3_not_coherent(self, result):
        cr3 = result.track_c_composition.candidates[2]
        assert cr3.coherent is False

    def test_cr5_rejected(self, result):
        cr5 = result.track_c_composition.candidates[4]
        assert cr5.status == "rejected"

    def test_tensor_product_is_mip(self, result):
        cr1 = result.track_c_composition.candidates[0]
        assert cr1.appendix_p_class == "motivated_independent_postulation"


# ===========================================================================
# TestTrackDReducedState
# ===========================================================================

class TestTrackDReducedState:
    def test_n_candidates(self, result):
        assert result.track_d_reduced_state.n_candidates == N_REDUCED_STATE_CANDIDATES

    def test_chosen_rs1(self, result):
        assert "RS1" in result.track_d_reduced_state.chosen_candidate_id

    def test_reduced_state_verdict(self, result):
        assert result.track_d_reduced_state.reduced_state_verdict == QIIB_REDUCED_STATE_VERDICT

    def test_rs1_extension_level(self, result):
        rs1 = result.track_d_reduced_state.candidates[0]
        assert rs1.status == "extension_level"
        assert "partial" in rs1.candidate_name.lower() or "trace" in rs1.candidate_name.lower()

    def test_rs4_rejected(self, result):
        rs4 = result.track_d_reduced_state.candidates[3]
        assert rs4.status == "rejected"


# ===========================================================================
# TestTrackEManyBody
# ===========================================================================

class TestTrackEManyBody:
    def test_n_levels(self, result):
        assert result.track_e_many_body.n_levels == N_MANY_BODY_LEVELS

    def test_mb1_achieved(self, result):
        mb1 = result.track_e_many_body.levels[0]
        assert mb1.level_id == "MB1"
        assert mb1.achieved is True

    def test_mb2_not_achieved(self, result):
        mb2 = result.track_e_many_body.levels[1]
        assert mb2.achieved is False

    def test_mb3_not_achieved(self, result):
        mb3 = result.track_e_many_body.levels[2]
        assert mb3.achieved is False

    def test_mb4_not_achieved(self, result):
        mb4 = result.track_e_many_body.levels[3]
        assert mb4.achieved is False

    def test_highest_achieved_mb1(self, result):
        assert "MB1" in result.track_e_many_body.highest_achieved_id

    def test_many_body_verdict(self, result):
        assert result.track_e_many_body.many_body_verdict == QIIB_MANY_BODY_VERDICT

    def test_only_mb1_achieved(self, result):
        achieved = [l for l in result.track_e_many_body.levels if l.achieved]
        assert len(achieved) == 1
        assert achieved[0].level_id == "MB1"


# ===========================================================================
# TestTrackFDecoherence
# ===========================================================================

class TestTrackFDecoherence:
    def test_n_checks(self, result):
        assert result.track_f_decoherence.n_checks == N_DECOHERENCE_CHECKS

    def test_overall_compatible(self, result):
        assert result.track_f_decoherence.overall_compatible is True

    def test_requires_new_postulates(self, result):
        assert result.track_f_decoherence.requires_new_postulates is True

    def test_dc1_compatible(self, result):
        dc1 = result.track_f_decoherence.checks[0]
        assert dc1.result == "compatible"

    def test_dc2_underdetermined(self, result):
        dc2 = result.track_f_decoherence.checks[1]
        assert dc2.result == "underdetermined"

    def test_dc3_compatible(self, result):
        dc3 = result.track_f_decoherence.checks[2]
        assert dc3.result == "compatible"

    def test_dc4_requires_postulate(self, result):
        dc4 = result.track_f_decoherence.checks[3]
        assert dc4.result == "requires_new_postulate"

    def test_check_ids_unique(self, result):
        ids = [c.check_id for c in result.track_f_decoherence.checks]
        assert len(ids) == len(set(ids))


# ===========================================================================
# TestTrackGBenchmark
# ===========================================================================

class TestTrackGBenchmark:
    def test_n_candidates(self, result):
        assert result.track_g_benchmark.n_candidates == N_BENCHMARK_CANDIDATES

    def test_n_viable(self, result):
        assert result.track_g_benchmark.n_viable == 2

    def test_chosen_cb1(self, result):
        assert "CB1" in result.track_g_benchmark.chosen_benchmark_id

    def test_hilbert_dim(self, result):
        assert result.track_g_benchmark.benchmark_hilbert_dim == COMPOSITE_HILBERT_DIM

    def test_n_subsystems(self, result):
        assert result.track_g_benchmark.benchmark_n_subsystems == N_SUBSYSTEMS_BENCHMARK

    def test_cb1_viable(self, result):
        cb1 = result.track_g_benchmark.candidates[0]
        assert cb1.viable is True
        assert len(cb1.demonstrates) >= 3

    def test_cb1_no_entanglement(self, result):
        cb1 = result.track_g_benchmark.candidates[0]
        not_demo = " ".join(cb1.does_not_demonstrate).lower()
        assert "entanglement" in not_demo

    def test_cb2_not_viable(self, result):
        cb2 = result.track_g_benchmark.candidates[1]
        assert cb2.viable is False

    def test_cb4_not_viable(self, result):
        cb4 = result.track_g_benchmark.candidates[3]
        assert cb4.viable is False


# ===========================================================================
# TestTrackHAppendixP
# ===========================================================================

class TestTrackHAppendixP:
    def test_n_entries(self, result):
        assert result.track_h_appendix_p.n_entries == N_APPENDIX_P_ENTRIES

    def test_no_native_canon(self, result):
        assert result.track_h_appendix_p.no_native_canon is True

    def test_overall_class(self, result):
        assert result.track_h_appendix_p.overall_class == QIIB_OVERALL_APPENDIX_P_CLASS

    def test_all_classes_valid(self, result):
        for e in result.track_h_appendix_p.entries:
            assert e.appendix_p_class in ALLOWED_APPENDIX_P_CLASSES

    def test_no_entry_native_canon(self, result):
        for e in result.track_h_appendix_p.entries:
            assert e.appendix_p_class != "native_canon"

    def test_at_least_one_mip(self, result):
        n_mip = sum(1 for e in result.track_h_appendix_p.entries
                    if e.appendix_p_class == "motivated_independent_postulation")
        assert n_mip >= 1

    def test_at_least_one_bsr(self, result):
        n_bsr = sum(1 for e in result.track_h_appendix_p.entries
                    if e.appendix_p_class == "bounded_structural_result")
        assert n_bsr >= 1

    def test_all_have_allowed_claim(self, result):
        for e in result.track_h_appendix_p.entries:
            assert len(e.allowed_claim) > 10

    def test_all_have_forbidden_claim(self, result):
        for e in result.track_h_appendix_p.entries:
            assert len(e.forbidden_claim) > 10


# ===========================================================================
# TestTrackIAuthorization
# ===========================================================================

class TestTrackIAuthorization:
    def test_qiic_authorized(self, result):
        assert result.track_i_authorization.qiic_authorized is True

    def test_authorization_verdict(self, result):
        assert result.track_i_authorization.authorization_verdict == QIIB_AUTHORIZATION_VERDICT

    def test_authorization_basis_length(self, result):
        assert len(result.track_i_authorization.authorization_basis) >= 3

    def test_qiic_constraints_length(self, result):
        assert len(result.track_i_authorization.qiic_constraints) >= 3

    def test_constraints_mention_tensor_product(self, result):
        text = " ".join(result.track_i_authorization.qiic_constraints).lower()
        assert "tensor" in text

    def test_constraints_mention_nonfactorized(self, result):
        text = " ".join(result.track_i_authorization.qiic_constraints).lower()
        assert "nonfactorized" in text or "product" in text


# ===========================================================================
# TestTrackJNonclaims
# ===========================================================================

class TestTrackJNonclaims:
    def test_n_nonclaims(self, result):
        assert result.track_j_nonclaims.n_nonclaims == N_QIIB_NONCLAIMS

    def test_all_registered(self, result):
        assert result.track_j_nonclaims.all_registered is True

    def test_all_start_with_not_claiming(self, result):
        for nc in result.track_j_nonclaims.nonclaims:
            assert nc.startswith("NOT_claiming_")

    def test_mentions_entanglement(self, result):
        text = " ".join(result.track_j_nonclaims.nonclaims).lower()
        assert "entanglement" in text

    def test_mentions_tensor_product(self, result):
        text = " ".join(result.track_j_nonclaims.nonclaims).lower()
        assert "tensor" in text

    def test_mentions_native_canon(self, result):
        text = " ".join(result.track_j_nonclaims.nonclaims).lower()
        assert "native_canon" in text or "native canon" in text

    def test_mentions_matter_readiness(self, result):
        text = " ".join(result.track_j_nonclaims.nonclaims).lower()
        assert "matter" in text


# ===========================================================================
# TestHardGatedVerdicts
# ===========================================================================

class TestHardGatedVerdicts:
    def test_subsystem_exact(self, result):
        assert result.subsystem_verdict == QIIB_SUBSYSTEM_VERDICT

    def test_composition_exact(self, result):
        assert result.composition_verdict == QIIB_COMPOSITION_VERDICT

    def test_reduced_state_exact(self, result):
        assert result.reduced_state_verdict == QIIB_REDUCED_STATE_VERDICT

    def test_many_body_exact(self, result):
        assert result.many_body_verdict == QIIB_MANY_BODY_VERDICT

    def test_authorization_exact(self, result):
        assert result.authorization_verdict == QIIB_AUTHORIZATION_VERDICT

    def test_subsystem_in_allowed(self, result):
        assert result.subsystem_verdict in ALLOWED_SUBSYSTEM_VERDICTS

    def test_composition_in_allowed(self, result):
        assert result.composition_verdict in ALLOWED_COMPOSITION_VERDICTS

    def test_reduced_state_in_allowed(self, result):
        assert result.reduced_state_verdict in ALLOWED_REDUCED_STATE_VERDICTS

    def test_many_body_in_allowed(self, result):
        assert result.many_body_verdict in ALLOWED_MANY_BODY_VERDICTS

    def test_authorization_in_allowed(self, result):
        assert result.authorization_verdict in ALLOWED_AUTHORIZATION_VERDICTS

    def test_all_five_distinct(self, result):
        verdicts = {
            result.subsystem_verdict,
            result.composition_verdict,
            result.reduced_state_verdict,
            result.many_body_verdict,
            result.authorization_verdict,
        }
        assert len(verdicts) == 5

    def test_appendix_p_class(self, result):
        assert result.qiib_appendix_p_class == QIIB_OVERALL_APPENDIX_P_CLASS

    def test_appendix_p_in_allowed(self, result):
        assert result.qiib_appendix_p_class in ALLOWED_APPENDIX_P_CLASSES


# ===========================================================================
# TestMasterAudit
# ===========================================================================

class TestMasterAudit:
    def test_valid(self, result):
        assert result.valid is True

    def test_all_tracks_present(self, result):
        assert result.track_a_eligibility is not None
        assert result.track_b_subsystem is not None
        assert result.track_c_composition is not None
        assert result.track_d_reduced_state is not None
        assert result.track_e_many_body is not None
        assert result.track_f_decoherence is not None
        assert result.track_g_benchmark is not None
        assert result.track_h_appendix_p is not None
        assert result.track_i_authorization is not None
        assert result.track_j_nonclaims is not None

    def test_allowed_claims_length(self, result):
        assert len(result.allowed_claims) == N_ALLOWED_CLAIMS

    def test_forbidden_claims_length(self, result):
        assert len(result.forbidden_claims) == N_FORBIDDEN_CLAIMS

    def test_nonclaims_length(self, result):
        assert len(result.exact_nonclaims) == N_QIIB_NONCLAIMS

    def test_diagnostics_composite_dim(self, result):
        assert result.diagnostics["composite_hilbert_dim"] == COMPOSITE_HILBERT_DIM

    def test_diagnostics_subsystem_viable(self, result):
        assert result.diagnostics["n_subsystem_viable"] == 1

    def test_diagnostics_benchmark_viable(self, result):
        assert result.diagnostics["n_benchmark_viable"] == 2

    def test_idempotency(self):
        r1 = run_qiib_composite_manybody_state_audit()
        r2 = run_qiib_composite_manybody_state_audit()
        assert r1.valid == r2.valid
        assert r1.subsystem_verdict == r2.subsystem_verdict
        assert r1.authorization_verdict == r2.authorization_verdict

    def test_self_test(self):
        assert _self_test() is True


# ===========================================================================
# TestDoctrinalBoundaries
# ===========================================================================

class TestDoctrinalBoundaries:
    def test_no_entanglement_claim(self, result):
        for claim in result.forbidden_claims:
            if "entanglement" in claim.lower():
                break
        else:
            pytest.fail("No forbidden claim mentions entanglement")

    def test_no_derived_tensor_product(self, result):
        for claim in result.forbidden_claims:
            if "derived" in claim.lower() and "tensor" in claim.lower():
                break
        else:
            pytest.fail("No forbidden claim about derived tensor product")

    def test_no_native_canon_claim(self, result):
        for claim in result.forbidden_claims:
            if "native canon" in claim.lower() or "native_canon" in claim.lower():
                break
        else:
            pytest.fail("No forbidden claim mentions native canon")

    def test_mip_in_allowed(self, result):
        text = " ".join(result.allowed_claims).lower()
        assert "mip" in text or "postulated" in text or "extension" in text

    def test_product_state_in_allowed(self, result):
        text = " ".join(result.allowed_claims).lower()
        assert "product" in text

    def test_qiic_authorized_in_allowed(self, result):
        text = " ".join(result.allowed_claims).lower()
        assert "q-ii.c" in text or "qiic" in text or "entanglement" in text
