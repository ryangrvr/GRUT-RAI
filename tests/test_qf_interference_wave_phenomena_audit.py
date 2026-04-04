"""
Tests for Appendix Q-F --- Interference and Wave-Phenomena Audit
================================================================

Deterministic test suite for grut/qf_interference_wave_phenomena_audit.py.
All tests are pure assertions on the audit result --- no I/O, no randomness.
"""

import math
import pytest

from grut.qf_interference_wave_phenomena_audit import (
    # Constants
    TAU_SQ, TAU, GAMMA,
    DELTA_PHI_2STATE, R_DEC_2STATE, TAU_DEC_2STATE,
    PHI_MINUS_GROWTH_RATE_SIGN, PHI_MINUS_CAN_BE_IMAGINARY_PART,
    VISIBILITY_AT_TAU_DEC, VISIBILITY_AT_TAU_2STATE,
    TIMESCALE_RATIO_DEC_TO_CONSTITUTIVE, VISIBILITY_HALF_LIFE_2STATE,
    N_INTERFERENCE_INGREDIENTS, N_CANDIDATE_TOY_MODELS,
    N_SLIT_CANDIDATES, N_COMPARATIVE_ENTRIES,
    N_QF_NONCLAIMS, N_APPENDIX_P_ENTRIES,
    N_ALLOWED_CLAIMS, N_FORBIDDEN_CLAIMS,
    # Inherited verdicts
    QE1_INHERITED, QE2_INHERITED, QE3_INHERITED, QE4_INHERITED,
    QE_INHERITED_AUTHORIZATION,
    QD_INHERITED_DECOHERENCE, QD_INHERITED_POINTER,
    QC_INHERITED_LAW_CLASS, QC5_INHERITED_RECOVERY,
    # Q-F verdicts
    QF_PHASE_VERDICT, QF_INTERFERENCE_VERDICT,
    QF_SLIT_INTERPRETATION_VERDICT, QF_CONSTITUTIVE_INTERFERENCE_VERDICT,
    QF_AUTHORIZATION_VERDICT, QF_OVERALL_APPENDIX_P_CLASS,
    # Frozensets
    ALLOWED_PHASE_VERDICTS, ALLOWED_INTERFERENCE_VERDICTS,
    ALLOWED_SLIT_INTERPRETATION_VERDICTS,
    ALLOWED_CONSTITUTIVE_INTERFERENCE_VERDICTS,
    ALLOWED_AUTHORIZATION_VERDICTS, ALLOWED_APPENDIX_P_CLASSES,
    # Nonclaims
    QF_NONCLAIMS,
    # Functions
    run_qf_interference_wave_phenomena_audit,
    validate_qf_result,
    _self_test,
    print_qf_summary,
)


# ---------------------------------------------------------------------------
# Module-scope fixture: run the audit once, reuse across all tests
# ---------------------------------------------------------------------------

@pytest.fixture(scope="module")
def result():
    return run_qf_interference_wave_phenomena_audit()


# ===========================================================================
# TestQFConstants
# ===========================================================================

class TestQFConstants:
    """Tests for module-level constants."""

    def test_tau_sq_value(self):
        assert TAU_SQ == 1.5

    def test_tau_value(self):
        assert abs(TAU - math.sqrt(1.5)) < 1e-15

    def test_gamma_value(self):
        assert abs(GAMMA - 1.0 / TAU) < 1e-15

    def test_gamma_tau_product(self):
        assert abs(GAMMA * TAU - 1.0) < 1e-15

    def test_delta_phi_2state(self):
        assert DELTA_PHI_2STATE == 2.0

    def test_r_dec_2state(self):
        assert abs(R_DEC_2STATE - 2.0 / TAU) < 1e-15

    def test_tau_dec_2state(self):
        assert abs(TAU_DEC_2STATE - TAU / 2.0) < 1e-15

    def test_phi_minus_growth_sign(self):
        assert PHI_MINUS_GROWTH_RATE_SIGN == +1

    def test_phi_minus_not_imaginary(self):
        assert PHI_MINUS_CAN_BE_IMAGINARY_PART is False

    def test_visibility_at_tau_dec(self):
        assert abs(VISIBILITY_AT_TAU_DEC - math.exp(-1.0)) < 1e-15

    def test_visibility_at_tau_2state(self):
        assert abs(VISIBILITY_AT_TAU_2STATE - math.exp(-2.0)) < 1e-15

    def test_timescale_ratio(self):
        assert TIMESCALE_RATIO_DEC_TO_CONSTITUTIVE == 0.5

    def test_visibility_half_life(self):
        assert abs(VISIBILITY_HALF_LIFE_2STATE - TAU_DEC_2STATE * math.log(2.0)) < 1e-15

    def test_n_interference_ingredients(self):
        assert N_INTERFERENCE_INGREDIENTS == 5

    def test_n_candidate_toy_models(self):
        assert N_CANDIDATE_TOY_MODELS == 4

    def test_n_slit_candidates(self):
        assert N_SLIT_CANDIDATES == 4

    def test_n_comparative_entries(self):
        assert N_COMPARATIVE_ENTRIES == 4

    def test_n_nonclaims(self):
        assert N_QF_NONCLAIMS == 8

    def test_n_appendix_p_entries(self):
        assert N_APPENDIX_P_ENTRIES == 6

    def test_n_allowed_claims(self):
        assert N_ALLOWED_CLAIMS == 7

    def test_n_forbidden_claims(self):
        assert N_FORBIDDEN_CLAIMS == 7

    def test_qe1_inherited(self):
        assert QE1_INHERITED == "qe1_demonstrates_relaxation_and_decoherence"

    def test_qe2_inherited(self):
        assert QE2_INHERITED == "qe2_demonstrates_pointer_record_structure"

    def test_qe3_inherited(self):
        assert QE3_INHERITED == "qe3_uncertainty_like_structure_underdetermined"

    def test_qe4_inherited(self):
        assert QE4_INHERITED == "qe4_constitutive_observable_classicality_demonstrated"

    def test_qe_authorization_inherited(self):
        assert QE_INHERITED_AUTHORIZATION == "authorized_to_proceed_to_QF"

    def test_qd_decoherence_inherited(self):
        assert QD_INHERITED_DECOHERENCE == "effective_regime_decoherence_demonstrated"

    def test_qd_pointer_inherited(self):
        assert QD_INHERITED_POINTER == "pointer_basis_class_selected"

    def test_qc_law_inherited(self):
        assert QC_INHERITED_LAW_CLASS == "lindbladian_like_law_preferred"

    def test_qc5_recovery_inherited(self):
        assert QC5_INHERITED_RECOVERY == "effective_regime_constitutive_recovery_demonstrated"

    def test_phase_verdict_constant(self):
        assert QF_PHASE_VERDICT == "relative_phase_structure_demonstrated_in_toy_form"

    def test_interference_verdict_constant(self):
        assert QF_INTERFERENCE_VERDICT == "transient_interference_before_decoherence_demonstrated"

    def test_slit_verdict_constant(self):
        assert QF_SLIT_INTERPRETATION_VERDICT == "abstract_two_path_interpretation_justified"

    def test_constitutive_verdict_constant(self):
        assert QF_CONSTITUTIVE_INTERFERENCE_VERDICT == (
            "interference_requires_complementary_observable_sector"
        )

    def test_authorization_verdict_constant(self):
        assert QF_AUTHORIZATION_VERDICT == "authorized_to_close_first_wave_quantum_program"

    def test_overall_appendix_p_class(self):
        assert QF_OVERALL_APPENDIX_P_CLASS == "motivated_but_unbuilt"

    # Frozenset sizes
    def test_allowed_phase_verdicts_size(self):
        assert len(ALLOWED_PHASE_VERDICTS) == 4

    def test_allowed_interference_verdicts_size(self):
        assert len(ALLOWED_INTERFERENCE_VERDICTS) == 4

    def test_allowed_slit_verdicts_size(self):
        assert len(ALLOWED_SLIT_INTERPRETATION_VERDICTS) == 4

    def test_allowed_constitutive_verdicts_size(self):
        assert len(ALLOWED_CONSTITUTIVE_INTERFERENCE_VERDICTS) == 4

    def test_allowed_authorization_verdicts_size(self):
        assert len(ALLOWED_AUTHORIZATION_VERDICTS) == 4

    def test_allowed_appendix_p_classes_size(self):
        assert len(ALLOWED_APPENDIX_P_CLASSES) == 8

    # Nonclaims list
    def test_nonclaims_list_length(self):
        assert len(QF_NONCLAIMS) == N_QF_NONCLAIMS

    def test_all_nonclaims_start_with_not_claiming(self):
        for nc in QF_NONCLAIMS:
            assert nc.startswith("NOT_claiming_"), f"Nonclaim does not start with NOT_claiming_: {nc[:40]}"


# ===========================================================================
# TestTrackAEligibility
# ===========================================================================

class TestTrackAEligibility:
    """Tests for Track A --- interference eligibility audit."""

    def test_n_ingredients(self, result):
        assert result.track_a_eligibility.n_ingredients == 5

    def test_n_present(self, result):
        assert result.track_a_eligibility.n_present == 2

    def test_n_conditionally_present(self, result):
        assert result.track_a_eligibility.n_conditionally_present == 3

    def test_n_absent(self, result):
        assert result.track_a_eligibility.n_absent == 0

    def test_n_extension_level(self, result):
        assert result.track_a_eligibility.n_extension_level == 0

    def test_eligibility_verdict(self, result):
        assert result.track_a_eligibility.eligibility_verdict == "eligible_for_toy_interference"

    def test_ingredients_count(self, result):
        assert len(result.track_a_eligibility.ingredients) == 5

    def test_ing1_complex_structure_j(self, result):
        ing = result.track_a_eligibility.ingredients[0]
        assert ing.ingredient_id == "ING1"
        assert ing.status == "conditionally_present"
        assert "Q-B.5" in ing.source

    def test_ing2_two_components(self, result):
        ing = result.track_a_eligibility.ingredients[1]
        assert ing.ingredient_id == "ING2"
        assert ing.status == "present"
        assert "Q-E" in ing.source

    def test_ing3_relative_phase(self, result):
        ing = result.track_a_eligibility.ingredients[2]
        assert ing.ingredient_id == "ING3"
        assert ing.status == "conditionally_present"

    def test_ing4_cross_term_observable(self, result):
        ing = result.track_a_eligibility.ingredients[3]
        assert ing.ingredient_id == "ING4"
        assert ing.status == "conditionally_present"

    def test_ing5_coherence_lifetime(self, result):
        ing = result.track_a_eligibility.ingredients[4]
        assert ing.ingredient_id == "ING5"
        assert ing.status == "present"

    def test_all_ingredient_ids_unique(self, result):
        ids = [ing.ingredient_id for ing in result.track_a_eligibility.ingredients]
        assert len(ids) == len(set(ids))

    def test_no_absent_ingredients(self, result):
        for ing in result.track_a_eligibility.ingredients:
            assert ing.status != "absent"

    def test_present_plus_conditional_equals_total(self, result):
        ta = result.track_a_eligibility
        assert ta.n_present + ta.n_conditionally_present + ta.n_absent + ta.n_extension_level == ta.n_ingredients

    def test_notes_length(self, result):
        assert len(result.track_a_eligibility.notes) >= 3

    def test_all_ingredients_have_source(self, result):
        for ing in result.track_a_eligibility.ingredients:
            assert len(ing.source) > 0

    def test_all_ingredients_have_notes(self, result):
        for ing in result.track_a_eligibility.ingredients:
            assert len(ing.notes) >= 2


# ===========================================================================
# TestTrackBRelativePhase
# ===========================================================================

class TestTrackBRelativePhase:
    """Tests for Track B --- relative phase evolution audit."""

    def test_phase_source(self, result):
        assert "hamiltonian" in result.track_b_relative_phase.phase_source.lower()

    def test_phase_formula_contains_exp(self, result):
        assert "exp" in result.track_b_relative_phase.phase_formula

    def test_phase_formula_contains_delta_e(self, result):
        assert "Delta_E" in result.track_b_relative_phase.phase_formula

    def test_combined_formula_contains_r_dec(self, result):
        assert "R_dec" in result.track_b_relative_phase.combined_off_diagonal_formula

    def test_combined_formula_contains_delta_e(self, result):
        assert "Delta_E" in result.track_b_relative_phase.combined_off_diagonal_formula

    def test_phase_demonstrated_in_toy(self, result):
        assert result.track_b_relative_phase.phase_demonstrated_in_toy is True

    def test_phase_requires_hamiltonian(self, result):
        assert result.track_b_relative_phase.phase_requires_hamiltonian is True

    def test_hamiltonian_status_mip(self, result):
        assert "MIP" in result.track_b_relative_phase.hamiltonian_status or \
               "postulated" in result.track_b_relative_phase.hamiltonian_status

    def test_phase_independent_of_decoherence(self, result):
        assert result.track_b_relative_phase.phase_independent_of_decoherence is True

    def test_phase_verdict(self, result):
        assert result.track_b_relative_phase.phase_verdict == QF_PHASE_VERDICT

    def test_phase_verdict_in_allowed(self, result):
        assert result.track_b_relative_phase.phase_verdict in ALLOWED_PHASE_VERDICTS

    def test_notes_length(self, result):
        assert len(result.track_b_relative_phase.notes) >= 5

    def test_notes_mention_lindblad(self, result):
        notes_text = " ".join(result.track_b_relative_phase.notes).lower()
        assert "lindblad" in notes_text or "lindbladian" in notes_text

    def test_notes_mention_not_native_canon(self, result):
        notes_text = " ".join(result.track_b_relative_phase.notes).lower()
        assert "not" in notes_text and "native" in notes_text


# ===========================================================================
# TestTrackCToyModel
# ===========================================================================

class TestTrackCToyModel:
    """Tests for Track C --- minimal interference toy model audit."""

    def test_n_candidates(self, result):
        assert result.track_c_toy_model.n_candidates == N_CANDIDATE_TOY_MODELS

    def test_candidates_list_length(self, result):
        assert len(result.track_c_toy_model.candidates) == N_CANDIDATE_TOY_MODELS

    def test_n_viable(self, result):
        assert result.track_c_toy_model.n_viable == 2

    def test_chosen_model_id(self, result):
        assert "TM1" in result.track_c_toy_model.chosen_model_id

    def test_interference_verdict(self, result):
        assert result.track_c_toy_model.interference_verdict == QF_INTERFERENCE_VERDICT

    def test_visibility_formula_contains_exp(self, result):
        assert "exp" in result.track_c_toy_model.visibility_formula

    def test_visibility_at_t0(self, result):
        assert result.track_c_toy_model.visibility_at_t0 == 1.0

    def test_visibility_at_tau_dec(self, result):
        assert abs(result.track_c_toy_model.visibility_at_tau_dec - math.exp(-1.0)) < 1e-12

    def test_cross_term_formula_contains_re(self, result):
        assert "Re" in result.track_c_toy_model.cross_term_formula

    def test_tm1_viable(self, result):
        tm1 = result.track_c_toy_model.candidates[0]
        assert tm1.model_id == "TM1"
        assert tm1.viable is True

    def test_tm1_demonstrates_all(self, result):
        tm1 = result.track_c_toy_model.candidates[0]
        assert tm1.demonstrates_cross_terms is True
        assert tm1.demonstrates_phase_sensitivity is True
        assert tm1.demonstrates_transient_interference is True
        assert tm1.demonstrates_constructive_destructive is True

    def test_tm2_not_viable(self, result):
        tm2 = result.track_c_toy_model.candidates[1]
        assert tm2.model_id == "TM2"
        assert tm2.viable is False

    def test_tm3_viable(self, result):
        tm3 = result.track_c_toy_model.candidates[2]
        assert tm3.model_id == "TM3"
        assert tm3.viable is True

    def test_tm4_not_viable(self, result):
        tm4 = result.track_c_toy_model.candidates[3]
        assert tm4.model_id == "TM4"
        assert tm4.viable is False

    def test_all_model_ids_unique(self, result):
        ids = [c.model_id for c in result.track_c_toy_model.candidates]
        assert len(ids) == len(set(ids))

    def test_n_viable_matches_count(self, result):
        counted = sum(1 for c in result.track_c_toy_model.candidates if c.viable)
        assert counted == result.track_c_toy_model.n_viable

    def test_notes_mention_transient(self, result):
        notes_text = " ".join(result.track_c_toy_model.notes).lower()
        assert "transient" in notes_text

    def test_tm1_low_burden(self, result):
        tm1 = result.track_c_toy_model.candidates[0]
        assert tm1.extension_burden == "low"


# ===========================================================================
# TestTrackDDecoherenceCompetition
# ===========================================================================

class TestTrackDDecoherenceCompetition:
    """Tests for Track D --- decoherence-vs-interference competition."""

    def test_visibility_decay_law(self, result):
        assert "exp" in result.track_d_decoherence_competition.visibility_decay_law

    def test_visibility_decay_rate(self, result):
        assert "gamma" in result.track_d_decoherence_competition.visibility_decay_rate

    def test_decoherence_timescale_formula(self, result):
        assert "tau" in result.track_d_decoherence_competition.decoherence_timescale

    def test_interference_timescale_equals_decoherence(self, result):
        assert "tau_dec" in result.track_d_decoherence_competition.interference_timescale

    def test_timescale_ratio_is_one(self, result):
        assert result.track_d_decoherence_competition.timescale_ratio == 1.0

    def test_interference_survives_short_time(self, result):
        assert "<<" in result.track_d_decoherence_competition.interference_survives_regime or \
               "short" in result.track_d_decoherence_competition.interference_survives_regime.lower()

    def test_interference_suppressed_long_time(self, result):
        assert ">>" in result.track_d_decoherence_competition.interference_suppressed_regime or \
               "long" in result.track_d_decoherence_competition.interference_suppressed_regime.lower()

    def test_tau_controls_visibility(self, result):
        assert result.track_d_decoherence_competition.tau_controls_visibility is True

    def test_eigenvalue_separation_controls_visibility(self, result):
        assert result.track_d_decoherence_competition.eigenvalue_separation_controls_visibility is True

    def test_weak_damping_condition(self, result):
        assert "delta_phi" in result.track_d_decoherence_competition.weak_damping_condition

    def test_competition_verdict(self, result):
        assert "decoherence_wins" in result.track_d_decoherence_competition.competition_verdict

    def test_visibility_half_life_2state(self, result):
        assert abs(result.track_d_decoherence_competition.visibility_half_life_2state
                   - VISIBILITY_HALF_LIFE_2STATE) < 1e-12

    def test_visibility_at_tau_2state(self, result):
        assert abs(result.track_d_decoherence_competition.visibility_at_tau_2state
                   - math.exp(-2.0)) < 1e-12

    def test_notes_length(self, result):
        assert len(result.track_d_decoherence_competition.notes) >= 8

    def test_notes_mention_constitutive_timescale(self, result):
        notes_text = " ".join(result.track_d_decoherence_competition.notes).lower()
        assert "constitutive" in notes_text

    def test_notes_mention_short_time(self, result):
        notes_text = " ".join(result.track_d_decoherence_competition.notes).lower()
        assert "short" in notes_text

    def test_visibility_at_tau_less_than_half(self, result):
        # At t = tau, V = exp(-2) ~ 0.135 < 0.5
        assert result.track_d_decoherence_competition.visibility_at_tau_2state < 0.5

    def test_visibility_at_tau_dec_greater_than_quarter(self, result):
        # V(tau_dec) = exp(-1) ~ 0.368 > 0.25
        assert VISIBILITY_AT_TAU_DEC > 0.25

    def test_half_life_less_than_tau_dec(self, result):
        # Half-life = tau_dec * ln(2) < tau_dec
        assert result.track_d_decoherence_competition.visibility_half_life_2state < TAU_DEC_2STATE


# ===========================================================================
# TestTrackESlitInterpretation
# ===========================================================================

class TestTrackESlitInterpretation:
    """Tests for Track E --- slit-style interpretation audit."""

    def test_n_candidates(self, result):
        assert result.track_e_slit_interpretation.n_candidates == N_SLIT_CANDIDATES

    def test_candidates_list_length(self, result):
        assert len(result.track_e_slit_interpretation.candidates) == N_SLIT_CANDIDATES

    def test_justified_candidate_id(self, result):
        assert "SL2" in result.track_e_slit_interpretation.justified_candidate_id

    def test_slit_verdict(self, result):
        assert result.track_e_slit_interpretation.slit_interpretation_verdict == \
               QF_SLIT_INTERPRETATION_VERDICT

    def test_sl1_not_justified(self, result):
        sl1 = result.track_e_slit_interpretation.candidates[0]
        assert sl1.candidate_id == "SL1"
        assert sl1.justified is False

    def test_sl2_justified(self, result):
        sl2 = result.track_e_slit_interpretation.candidates[1]
        assert sl2.candidate_id == "SL2"
        assert sl2.justified is True

    def test_sl3_not_justified(self, result):
        sl3 = result.track_e_slit_interpretation.candidates[2]
        assert sl3.candidate_id == "SL3"
        assert sl3.justified is False

    def test_sl4_not_justified(self, result):
        sl4 = result.track_e_slit_interpretation.candidates[3]
        assert sl4.candidate_id == "SL4"
        assert sl4.justified is False

    def test_exactly_one_justified(self, result):
        n_justified = sum(1 for c in result.track_e_slit_interpretation.candidates if c.justified)
        assert n_justified == 1

    def test_boundary_notes_length(self, result):
        assert len(result.track_e_slit_interpretation.boundary_notes) >= 3

    def test_boundary_notes_mention_spatial(self, result):
        bn_text = " ".join(result.track_e_slit_interpretation.boundary_notes).lower()
        assert "spatial" in bn_text or "position" in bn_text

    def test_sl3_obstruction_mentions_spatial(self, result):
        sl3 = result.track_e_slit_interpretation.candidates[2]
        assert "spatial" in sl3.obstruction_if_not.lower()

    def test_all_candidate_ids_unique(self, result):
        ids = [c.candidate_id for c in result.track_e_slit_interpretation.candidates]
        assert len(ids) == len(set(ids))

    def test_notes_length(self, result):
        assert len(result.track_e_slit_interpretation.notes) >= 4

    def test_sl2_obstruction_empty(self, result):
        sl2 = result.track_e_slit_interpretation.candidates[1]
        assert sl2.obstruction_if_not == ""


# ===========================================================================
# TestTrackFConstitutiveInterference
# ===========================================================================

class TestTrackFConstitutiveInterference:
    """Tests for Track F --- constitutive-observable compatibility."""

    def test_constitutive_observable(self, result):
        assert "Phi_hat" in result.track_f_constitutive_interference.constitutive_observable

    def test_pointer_observable(self, result):
        assert "Phi_hat" in result.track_f_constitutive_interference.pointer_observable

    def test_pointer_selected(self, result):
        assert result.track_f_constitutive_interference.pointer_selected is True

    def test_interference_requires_superposition_of_phi(self, result):
        assert "Phi_hat" in result.track_f_constitutive_interference.interference_requires_superposition_of

    def test_decoherence_suppresses(self, result):
        assert result.track_f_constitutive_interference.decoherence_suppresses_that_superposition is True

    def test_tension_described(self, result):
        assert "tension" in result.track_f_constitutive_interference.same_observable_tension.lower()

    def test_complementary_sector_needed(self, result):
        assert result.track_f_constitutive_interference.complementary_sector_needed is True

    def test_complementary_sector_example(self, result):
        assert "sigma_x" in result.track_f_constitutive_interference.complementary_sector_example.lower() or \
               "not diagonal" in result.track_f_constitutive_interference.complementary_sector_example.lower()

    def test_constitutive_interference_verdict(self, result):
        assert result.track_f_constitutive_interference.constitutive_interference_verdict == \
               QF_CONSTITUTIVE_INTERFERENCE_VERDICT

    def test_verdict_in_allowed(self, result):
        assert result.track_f_constitutive_interference.constitutive_interference_verdict in \
               ALLOWED_CONSTITUTIVE_INTERFERENCE_VERDICTS

    def test_notes_length(self, result):
        assert len(result.track_f_constitutive_interference.notes) >= 6

    def test_notes_mention_transient(self, result):
        notes_text = " ".join(result.track_f_constitutive_interference.notes).lower()
        assert "transient" in notes_text

    def test_notes_mention_complementary(self, result):
        notes_text = " ".join(result.track_f_constitutive_interference.notes).lower()
        assert "complementary" in notes_text

    def test_notes_mention_pointer(self, result):
        notes_text = " ".join(result.track_f_constitutive_interference.notes).lower()
        assert "pointer" in notes_text

    def test_notes_mention_decoherence(self, result):
        notes_text = " ".join(result.track_f_constitutive_interference.notes).lower()
        assert "decoherence" in notes_text

    def test_notes_mention_jump_operator(self, result):
        notes_text = " ".join(result.track_f_constitutive_interference.notes).lower()
        assert "jump" in notes_text or "l =" in notes_text


# ===========================================================================
# TestTrackGComparative
# ===========================================================================

class TestTrackGComparative:
    """Tests for Track G --- comparative model audit."""

    def test_entries_count(self, result):
        assert len(result.track_g_comparative.entries) == N_COMPARATIVE_ENTRIES

    def test_strongest_model(self, result):
        assert result.track_g_comparative.strongest_model_id == "TM1"

    def test_weakest_model(self, result):
        assert result.track_g_comparative.weakest_model_id == "TM4"

    def test_tm1_rank_1(self, result):
        for e in result.track_g_comparative.entries:
            if e.model_id == "TM1":
                assert e.strength_ranking == 1

    def test_tm4_rank_4(self, result):
        for e in result.track_g_comparative.entries:
            if e.model_id == "TM4":
                assert e.strength_ranking == 4

    def test_all_rankings_unique(self, result):
        rankings = [e.strength_ranking for e in result.track_g_comparative.entries]
        assert len(rankings) == len(set(rankings))

    def test_rankings_are_1_to_4(self, result):
        rankings = sorted([e.strength_ranking for e in result.track_g_comparative.entries])
        assert rankings == [1, 2, 3, 4]

    def test_tm1_low_burden(self, result):
        for e in result.track_g_comparative.entries:
            if e.model_id == "TM1":
                assert e.extension_burden == "low"

    def test_tm1_high_fidelity(self, result):
        for e in result.track_g_comparative.entries:
            if e.model_id == "TM1":
                assert e.fidelity_to_qb_through_qe == "high"

    def test_tm1_explicit_interference(self, result):
        for e in result.track_g_comparative.entries:
            if e.model_id == "TM1":
                assert e.explicitness_of_interference == "explicit"

    def test_tm1_transient_robustness(self, result):
        for e in result.track_g_comparative.entries:
            if e.model_id == "TM1":
                assert e.robustness_against_decoherence == "transient"

    def test_tm2_high_burden(self, result):
        for e in result.track_g_comparative.entries:
            if e.model_id == "TM2":
                assert e.extension_burden == "high"

    def test_all_model_ids_present(self, result):
        ids = {e.model_id for e in result.track_g_comparative.entries}
        assert ids == {"TM1", "TM2", "TM3", "TM4"}

    def test_notes_length(self, result):
        assert len(result.track_g_comparative.notes) >= 3

    def test_notes_mention_transient(self, result):
        notes_text = " ".join(result.track_g_comparative.notes).lower()
        assert "transient" in notes_text

    def test_no_robust_interference(self, result):
        for e in result.track_g_comparative.entries:
            assert e.robustness_against_decoherence != "robust"


# ===========================================================================
# TestTrackHAppendixP
# ===========================================================================

class TestTrackHAppendixP:
    """Tests for Track H --- Appendix P classification audit."""

    def test_n_entries(self, result):
        assert result.track_h_appendix_p.n_entries == N_APPENDIX_P_ENTRIES

    def test_entries_list_length(self, result):
        assert len(result.track_h_appendix_p.entries) == N_APPENDIX_P_ENTRIES

    def test_overall_class(self, result):
        assert result.track_h_appendix_p.overall_class == QF_OVERALL_APPENDIX_P_CLASS

    def test_no_native_canon(self, result):
        assert result.track_h_appendix_p.no_native_canon is True

    def test_all_classes_valid(self, result):
        for entry in result.track_h_appendix_p.entries:
            assert entry.appendix_p_class in ALLOWED_APPENDIX_P_CLASSES, \
                f"{entry.item_id}: {entry.appendix_p_class}"

    def test_no_entry_is_native_canon(self, result):
        for entry in result.track_h_appendix_p.entries:
            assert entry.appendix_p_class != "native_canon"

    def test_at_least_two_mbu(self, result):
        n_mbu = sum(1 for e in result.track_h_appendix_p.entries
                    if e.appendix_p_class == "motivated_but_unbuilt")
        assert n_mbu >= 2

    def test_at_least_one_bsr(self, result):
        n_bsr = sum(1 for e in result.track_h_appendix_p.entries
                    if e.appendix_p_class == "bounded_structural_result")
        assert n_bsr >= 1

    def test_all_entries_have_allowed_claim(self, result):
        for entry in result.track_h_appendix_p.entries:
            assert len(entry.allowed_claim) > 10

    def test_all_entries_have_forbidden_claim(self, result):
        for entry in result.track_h_appendix_p.entries:
            assert len(entry.forbidden_claim) > 10

    def test_all_entries_have_dependency(self, result):
        for entry in result.track_h_appendix_p.entries:
            assert len(entry.dependency) > 5

    def test_notes_length(self, result):
        assert len(result.track_h_appendix_p.notes) >= 3


# ===========================================================================
# TestTrackIAuthorization
# ===========================================================================

class TestTrackIAuthorization:
    """Tests for Track I --- quantum-program authorization audit."""

    def test_first_wave_closure_authorized(self, result):
        assert result.track_i_authorization.first_wave_closure_authorized is True

    def test_second_wave_opening_noted(self, result):
        assert result.track_i_authorization.second_wave_opening_noted is True

    def test_further_refinement_not_needed(self, result):
        assert result.track_i_authorization.further_interference_refinement_needed is False

    def test_remaining_gaps_length(self, result):
        assert len(result.track_i_authorization.remaining_gaps) >= 3

    def test_born_rule_gap_present(self, result):
        gaps_text = " ".join(result.track_i_authorization.remaining_gaps).lower()
        assert "born" in gaps_text

    def test_outcome_selection_gap_present(self, result):
        gaps_text = " ".join(result.track_i_authorization.remaining_gaps).lower()
        assert "outcome" in gaps_text

    def test_qe3_gap_present(self, result):
        gaps_text = " ".join(result.track_i_authorization.remaining_gaps).lower()
        assert "qe3" in gaps_text or "uncertainty" in gaps_text

    def test_gaps_documented_as(self, result):
        assert "BSR" in result.track_i_authorization.gaps_documented_as or \
               "MBU" in result.track_i_authorization.gaps_documented_as

    def test_authorization_verdict(self, result):
        assert result.track_i_authorization.authorization_verdict == QF_AUTHORIZATION_VERDICT

    def test_verdict_in_allowed(self, result):
        assert result.track_i_authorization.authorization_verdict in ALLOWED_AUTHORIZATION_VERDICTS

    def test_second_wave_scope_length(self, result):
        assert len(result.track_i_authorization.second_wave_scope) >= 3

    def test_second_wave_mentions_entanglement(self, result):
        scope_text = " ".join(result.track_i_authorization.second_wave_scope).lower()
        assert "entanglement" in scope_text

    def test_second_wave_mentions_field(self, result):
        scope_text = " ".join(result.track_i_authorization.second_wave_scope).lower()
        assert "field" in scope_text

    def test_notes_length(self, result):
        assert len(result.track_i_authorization.notes) >= 5


# ===========================================================================
# TestTrackJNonclaims
# ===========================================================================

class TestTrackJNonclaims:
    """Tests for Track J --- nonclaim firewall."""

    def test_n_nonclaims(self, result):
        assert result.track_j_nonclaims.n_nonclaims == N_QF_NONCLAIMS

    def test_nonclaims_list_length(self, result):
        assert len(result.track_j_nonclaims.nonclaims) == N_QF_NONCLAIMS

    def test_all_registered(self, result):
        assert result.track_j_nonclaims.all_registered is True

    def test_all_start_with_not_claiming(self, result):
        for nc in result.track_j_nonclaims.nonclaims:
            assert nc.startswith("NOT_claiming_"), f"Does not start with NOT_claiming_: {nc[:40]}"

    def test_at_least_one_mentions_double_slit(self, result):
        nc_text = " ".join(result.track_j_nonclaims.nonclaims).lower()
        assert "slit" in nc_text

    def test_at_least_one_mentions_born_rule(self, result):
        nc_text = " ".join(result.track_j_nonclaims.nonclaims).lower()
        assert "born" in nc_text

    def test_at_least_one_mentions_entanglement(self, result):
        nc_text = " ".join(result.track_j_nonclaims.nonclaims).lower()
        assert "entanglement" in nc_text

    def test_at_least_one_mentions_native_canon(self, result):
        nc_text = " ".join(result.track_j_nonclaims.nonclaims).lower()
        assert "native_canon" in nc_text or "native canon" in nc_text

    def test_at_least_one_mentions_experimental(self, result):
        nc_text = " ".join(result.track_j_nonclaims.nonclaims).lower()
        assert "experimental" in nc_text or "phenomenological" in nc_text

    def test_n_nonclaims_matches_list(self, result):
        assert result.track_j_nonclaims.n_nonclaims == len(result.track_j_nonclaims.nonclaims)


# ===========================================================================
# TestHardGatedVerdicts
# ===========================================================================

class TestHardGatedVerdicts:
    """Tests for all five hard-gated verdicts on the master result."""

    def test_phase_verdict_exact(self, result):
        assert result.phase_verdict == QF_PHASE_VERDICT

    def test_interference_verdict_exact(self, result):
        assert result.interference_verdict == QF_INTERFERENCE_VERDICT

    def test_slit_verdict_exact(self, result):
        assert result.slit_interpretation_verdict == QF_SLIT_INTERPRETATION_VERDICT

    def test_constitutive_verdict_exact(self, result):
        assert result.constitutive_interference_verdict == QF_CONSTITUTIVE_INTERFERENCE_VERDICT

    def test_authorization_verdict_exact(self, result):
        assert result.authorization_verdict == QF_AUTHORIZATION_VERDICT

    def test_phase_verdict_in_allowed(self, result):
        assert result.phase_verdict in ALLOWED_PHASE_VERDICTS

    def test_interference_verdict_in_allowed(self, result):
        assert result.interference_verdict in ALLOWED_INTERFERENCE_VERDICTS

    def test_slit_verdict_in_allowed(self, result):
        assert result.slit_interpretation_verdict in ALLOWED_SLIT_INTERPRETATION_VERDICTS

    def test_constitutive_verdict_in_allowed(self, result):
        assert result.constitutive_interference_verdict in ALLOWED_CONSTITUTIVE_INTERFERENCE_VERDICTS

    def test_authorization_verdict_in_allowed(self, result):
        assert result.authorization_verdict in ALLOWED_AUTHORIZATION_VERDICTS

    def test_all_five_verdicts_are_distinct(self, result):
        verdicts = {
            result.phase_verdict,
            result.interference_verdict,
            result.slit_interpretation_verdict,
            result.constitutive_interference_verdict,
            result.authorization_verdict,
        }
        assert len(verdicts) == 5

    def test_qf_appendix_p_class(self, result):
        assert result.qf_appendix_p_class == QF_OVERALL_APPENDIX_P_CLASS

    def test_appendix_p_class_in_allowed(self, result):
        assert result.qf_appendix_p_class in ALLOWED_APPENDIX_P_CLASSES

    def test_phase_verdict_matches_track_b(self, result):
        assert result.phase_verdict == result.track_b_relative_phase.phase_verdict

    def test_interference_verdict_matches_track_c(self, result):
        assert result.interference_verdict == result.track_c_toy_model.interference_verdict


# ===========================================================================
# TestMasterAudit
# ===========================================================================

class TestMasterAudit:
    """Tests for the master audit result and its aggregation."""

    def test_valid_true(self, result):
        assert result.valid is True

    def test_track_a_not_none(self, result):
        assert result.track_a_eligibility is not None

    def test_track_b_not_none(self, result):
        assert result.track_b_relative_phase is not None

    def test_track_c_not_none(self, result):
        assert result.track_c_toy_model is not None

    def test_track_d_not_none(self, result):
        assert result.track_d_decoherence_competition is not None

    def test_track_e_not_none(self, result):
        assert result.track_e_slit_interpretation is not None

    def test_track_f_not_none(self, result):
        assert result.track_f_constitutive_interference is not None

    def test_track_g_not_none(self, result):
        assert result.track_g_comparative is not None

    def test_track_h_not_none(self, result):
        assert result.track_h_appendix_p is not None

    def test_track_i_not_none(self, result):
        assert result.track_i_authorization is not None

    def test_track_j_not_none(self, result):
        assert result.track_j_nonclaims is not None

    def test_allowed_claims_length(self, result):
        assert len(result.allowed_claims) == N_ALLOWED_CLAIMS

    def test_forbidden_claims_length(self, result):
        assert len(result.forbidden_claims) == N_FORBIDDEN_CLAIMS

    def test_exact_nonclaims_length(self, result):
        assert len(result.exact_nonclaims) == N_QF_NONCLAIMS

    def test_all_exact_nonclaims_start_with_not_claiming(self, result):
        for nc in result.exact_nonclaims:
            assert nc.startswith("NOT_claiming_")

    def test_diagnostics_tau_sq(self, result):
        assert abs(result.diagnostics["tau_sq"] - TAU_SQ) < 1e-15

    def test_diagnostics_gamma_tau(self, result):
        assert abs(result.diagnostics["gamma_tau"] - 1.0) < 1e-12

    def test_diagnostics_visibility_at_tau_dec(self, result):
        assert abs(result.diagnostics["visibility_at_tau_dec"] - math.exp(-1.0)) < 1e-12

    def test_diagnostics_visibility_at_tau_2state(self, result):
        assert abs(result.diagnostics["visibility_at_tau_2state"] - math.exp(-2.0)) < 1e-12

    def test_diagnostics_timescale_ratio(self, result):
        assert abs(result.diagnostics["timescale_ratio_dec_to_constitutive"] - 0.5) < 1e-12

    def test_diagnostics_n_ingredients(self, result):
        assert result.diagnostics["n_interference_ingredients"] == N_INTERFERENCE_INGREDIENTS

    def test_diagnostics_n_toy_models(self, result):
        assert result.diagnostics["n_candidate_toy_models"] == N_CANDIDATE_TOY_MODELS

    def test_diagnostics_n_viable(self, result):
        assert result.diagnostics["n_viable_toy_models"] == 2

    def test_diagnostics_n_nonclaims(self, result):
        assert result.diagnostics["n_nonclaims"] == N_QF_NONCLAIMS

    def test_diagnostics_half_life(self, result):
        assert abs(result.diagnostics["visibility_half_life_2state"]
                   - VISIBILITY_HALF_LIFE_2STATE) < 1e-12

    # Idempotency tests
    def test_idempotency_valid(self):
        r1 = run_qf_interference_wave_phenomena_audit()
        r2 = run_qf_interference_wave_phenomena_audit()
        assert r1.valid == r2.valid

    def test_idempotency_phase_verdict(self):
        r1 = run_qf_interference_wave_phenomena_audit()
        r2 = run_qf_interference_wave_phenomena_audit()
        assert r1.phase_verdict == r2.phase_verdict

    def test_idempotency_interference_verdict(self):
        r1 = run_qf_interference_wave_phenomena_audit()
        r2 = run_qf_interference_wave_phenomena_audit()
        assert r1.interference_verdict == r2.interference_verdict

    def test_idempotency_authorization_verdict(self):
        r1 = run_qf_interference_wave_phenomena_audit()
        r2 = run_qf_interference_wave_phenomena_audit()
        assert r1.authorization_verdict == r2.authorization_verdict


# ===========================================================================
# TestPhysicsInvariants
# ===========================================================================

class TestPhysicsInvariants:
    """Tests for physics invariants and relationships."""

    def test_gamma_tau_product_is_one(self, result):
        assert abs(GAMMA * TAU - 1.0) < 1e-15

    def test_r_dec_2state_equals_2_over_tau(self):
        assert abs(R_DEC_2STATE - 2.0 / TAU) < 1e-15

    def test_tau_dec_2state_equals_tau_over_2(self):
        assert abs(TAU_DEC_2STATE - TAU / 2.0) < 1e-15

    def test_visibility_at_tau_dec_equals_exp_minus_1(self):
        assert abs(VISIBILITY_AT_TAU_DEC - math.exp(-1.0)) < 1e-15

    def test_visibility_at_tau_2state_equals_exp_minus_2(self):
        assert abs(VISIBILITY_AT_TAU_2STATE - math.exp(-2.0)) < 1e-15

    def test_decoherence_rate_at_delta_phi_sqrt2_equals_gamma(self):
        # R_dec(sqrt(2)) = 0.5 * gamma * 2 = gamma
        delta_phi = math.sqrt(2.0)
        r_dec = 0.5 * GAMMA * delta_phi ** 2
        assert abs(r_dec - GAMMA) < 1e-15

    def test_decoherence_timescale_at_delta_phi_sqrt2_equals_tau(self):
        # tau_dec(sqrt(2)) = 2*tau / 2 = tau
        delta_phi = math.sqrt(2.0)
        tau_dec = 2.0 * TAU / delta_phi ** 2
        assert abs(tau_dec - TAU) < 1e-15

    def test_half_life_less_than_tau_dec(self):
        # ln(2) < 1, so half-life < tau_dec
        assert VISIBILITY_HALF_LIFE_2STATE < TAU_DEC_2STATE

    def test_visibility_at_tau_less_than_visibility_at_tau_dec(self):
        # exp(-2) < exp(-1)
        assert VISIBILITY_AT_TAU_2STATE < VISIBILITY_AT_TAU_DEC

    def test_timescale_ratio_is_half(self):
        assert abs(TAU_DEC_2STATE / TAU - 0.5) < 1e-15

    def test_r_dec_2state_from_formula(self):
        # R_dec = 0.5 * gamma * delta_phi^2 = 0.5 * (1/tau) * 4 = 2/tau
        r = 0.5 * GAMMA * DELTA_PHI_2STATE ** 2
        assert abs(r - R_DEC_2STATE) < 1e-15

    def test_interference_transient_in_pointer_sector(self, result):
        # The constitutive observable IS the pointer observable, and decoherence
        # suppresses superpositions thereof: interference is transient
        assert result.track_f_constitutive_interference.pointer_selected is True
        assert result.track_f_constitutive_interference.decoherence_suppresses_that_superposition is True
        assert result.track_f_constitutive_interference.complementary_sector_needed is True


# ===========================================================================
# TestDoctrinalBoundaries
# ===========================================================================

class TestDoctrinalBoundaries:
    """Tests for doctrinal boundary enforcement."""

    def test_no_born_rule_claim(self, result):
        for claim in result.forbidden_claims:
            if "born" in claim.lower():
                break
        else:
            pytest.fail("No forbidden claim mentions Born rule")

    def test_no_full_slit_claim(self, result):
        for claim in result.forbidden_claims:
            if "slit" in claim.lower() or "wave mechanics" in claim.lower():
                break
        else:
            pytest.fail("No forbidden claim mentions slit/wave mechanics")

    def test_no_entanglement_claim(self, result):
        for claim in result.forbidden_claims:
            if "entanglement" in claim.lower():
                break
        else:
            pytest.fail("No forbidden claim mentions entanglement")

    def test_no_native_canon_claim(self, result):
        for claim in result.forbidden_claims:
            if "native canon" in claim.lower() or "native_canon" in claim.lower():
                break
        else:
            pytest.fail("No forbidden claim mentions native canon")

    def test_mbu_floor_in_allowed(self, result):
        for claim in result.allowed_claims:
            if "MBU" in claim or "motivated_but_unbuilt" in claim:
                break
        else:
            pytest.fail("No allowed claim mentions MBU floor")

    def test_transient_interference_in_allowed(self, result):
        for claim in result.allowed_claims:
            if "transient" in claim.lower():
                break
        else:
            pytest.fail("No allowed claim mentions transient interference")

    def test_abstract_two_path_in_allowed(self, result):
        for claim in result.allowed_claims:
            if "two-path" in claim.lower() or "two_path" in claim.lower():
                break
        else:
            pytest.fail("No allowed claim mentions two-path interpretation")

    def test_complementary_sector_in_allowed(self, result):
        for claim in result.allowed_claims:
            if "complementary" in claim.lower():
                break
        else:
            pytest.fail("No allowed claim mentions complementary sector")

    def test_first_wave_closure_in_allowed(self, result):
        for claim in result.allowed_claims:
            if "first-wave" in claim.lower() or "first wave" in claim.lower():
                break
        else:
            pytest.fail("No allowed claim mentions first-wave closure")

    def test_nonclaim_double_slit(self, result):
        nc_text = " ".join(result.exact_nonclaims).lower()
        assert "double_slit" in nc_text or "double slit" in nc_text

    def test_nonclaim_born_rule(self, result):
        nc_text = " ".join(result.exact_nonclaims).lower()
        assert "born" in nc_text

    def test_nonclaim_wave_ontology(self, result):
        nc_text = " ".join(result.exact_nonclaims).lower()
        assert "wave_ontology" in nc_text or "wave ontology" in nc_text


# ===========================================================================
# TestSelfTest
# ===========================================================================

class TestSelfTest:
    """Test the module-level self-test function."""

    def test_self_test_returns_true(self):
        assert _self_test() is True


# ===========================================================================
# TestPrintSummary
# ===========================================================================

class TestPrintSummary:
    """Test the print summary function."""

    def test_print_summary_runs(self, result, capsys):
        print_qf_summary(result)
        captured = capsys.readouterr()
        assert "Q-F" in captured.out
        assert QF_PHASE_VERDICT in captured.out
        assert QF_AUTHORIZATION_VERDICT in captured.out
