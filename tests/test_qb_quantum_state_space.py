"""Tests for grut/qb_quantum_state_space.py — Appendix Q-B.

Full deterministic test suite for the GRUT-Native Quantum State Space audit.
Covers all 7 audit tracks and all 3 hard-gated verdicts.

Structure
---------
  TestQBConstants              (14 tests)
  TestTrackAOntology           ( 9 tests)
  TestTrackBCandidatesSS1SS2   ( 8 tests)
  TestTrackBCandidatesSS3SS4   ( 8 tests)
  TestTrackBCandidatesSS5SS6   ( 8 tests)
  TestTrackBPrimaryFinding     ( 8 tests)
  TestTrackCPureMixed          ( 9 tests)
  TestTrackDCommutation        (12 tests)
  TestTrackEMapping            (11 tests)
  TestTrackFAppendixP          ( 9 tests)
  TestTrackGNonclaims          ( 8 tests)
  TestHardGatedVerdicts        (12 tests)
  TestMasterAudit              (10 tests)

Target: ~126 tests
"""

import math

import pytest

from grut.qb_quantum_state_space import (
    # Constants
    ALLOWED_ONTOLOGY_VERDICTS,
    ALLOWED_STATE_OBJECT_TYPES,
    ALLOWED_CANDIDATE_STATUSES,
    ALLOWED_PURE_MIXED_STATUSES,
    ALLOWED_COMMUTATION_VERDICTS,
    ALLOWED_MAPPING_VERDICTS,
    ALLOWED_PRIMARY_STATE_SPACE_VERDICTS,
    ALLOWED_APPENDIX_P_CLASSES,
    N_STATE_OBJECT_CANDIDATES,
    N_VIABLE_QUANTUM_CANDIDATES,
    N_QB_NONCLAIMS,
    QB_NONCLAIMS,
    GRUT_EOM_TEMPORAL_ORDER,
    CANONICAL_MOMENTUM_FROM_STANDARD_L,
    BATEMAN_DOUBLED_MOMENTUM,
    CTP_PHI_PLUS_FORMULA,
    CTP_PHI_MINUS_FORMULA,
    PHI_MINUS_EOM,
    PHI_MINUS_GROWTH_RATE_SIGN,
    PHI_MINUS_CAN_BE_IMAGINARY_PART,
    FORMAL_RHO_NOTATION,
    PRIOR_HILBERT_SPACE_REQUIRED_FOR_MAPPING,
    TAU_SQ,
    TAU,
    QB_PRIMARY_STATE_SPACE_VERDICT,
    QB_COMMUTATION_VERDICT,
    QB_MAPPING_VERDICT,
    QB_OVERALL_APPENDIX_P_CLASS,
    # Dataclasses
    QBOntologyCheck,
    QBStateCandidate,
    QBStateObjectCheck,
    QBPureMixedCheck,
    QBCommutationCheck,
    QBMappingCheck,
    QBAppendixPClassification,
    QBNonclaimFirewall,
    QBStateSpaceResult,
    # Builder functions
    build_track_a_ontology,
    build_track_b_state_object,
    build_track_c_pure_mixed,
    build_track_d_commutation,
    build_track_e_mapping,
    build_track_f_appendix_p,
    build_track_g_nonclaims,
    build_state_candidate_ss1_pure_ket,
    build_state_candidate_ss2_density_matrix,
    build_state_candidate_ss3_ctp_kernel,
    build_state_candidate_ss4_wigner,
    build_state_candidate_ss5_influence_functional,
    build_state_candidate_ss6_null,
    # Master function
    run_qb_quantum_state_space,
)


# ================================================================
# TestQBConstants
# ================================================================


class TestQBConstants:
    """Tests for module-level constants and vocabulary sets."""

    def test_allowed_ontology_verdicts_is_frozenset(self):
        assert isinstance(ALLOWED_ONTOLOGY_VERDICTS, frozenset)

    def test_open_at_effective_level_in_ontology_verdicts(self):
        assert "open_at_effective_level" in ALLOWED_ONTOLOGY_VERDICTS

    def test_closed_in_ontology_verdicts(self):
        assert "closed" in ALLOWED_ONTOLOGY_VERDICTS

    def test_allowed_state_object_types_is_frozenset(self):
        assert isinstance(ALLOWED_STATE_OBJECT_TYPES, frozenset)

    def test_no_native_quantum_state_in_state_types(self):
        assert "no_native_quantum_state" in ALLOWED_STATE_OBJECT_TYPES

    def test_n_state_object_candidates_equals_six(self):
        assert N_STATE_OBJECT_CANDIDATES == 6

    def test_n_viable_quantum_candidates_equals_zero(self):
        assert N_VIABLE_QUANTUM_CANDIDATES == 0

    def test_n_qb_nonclaims_equals_seven(self):
        assert N_QB_NONCLAIMS == 7

    def test_qb_nonclaims_list_length(self):
        assert len(QB_NONCLAIMS) == 7

    def test_grut_eom_temporal_order_equals_one(self):
        assert GRUT_EOM_TEMPORAL_ORDER == 1

    def test_phi_minus_growth_rate_sign_positive(self):
        assert PHI_MINUS_GROWTH_RATE_SIGN == +1

    def test_phi_minus_cannot_be_imaginary_part(self):
        assert PHI_MINUS_CAN_BE_IMAGINARY_PART is False

    def test_tau_sq_canonical_value(self):
        assert TAU_SQ == pytest.approx(1.5)

    def test_tau_consistency(self):
        assert TAU == pytest.approx(math.sqrt(TAU_SQ))

    def test_prior_hilbert_space_required(self):
        assert PRIOR_HILBERT_SPACE_REQUIRED_FOR_MAPPING is True

    def test_allowed_primary_verdicts_is_frozenset(self):
        assert isinstance(ALLOWED_PRIMARY_STATE_SPACE_VERDICTS, frozenset)

    def test_density_matrix_verdict_in_primary_set(self):
        assert "density_matrix_or_functional_state_required" in ALLOWED_PRIMARY_STATE_SPACE_VERDICTS

    def test_allowed_commutation_verdicts_is_frozenset(self):
        assert isinstance(ALLOWED_COMMUTATION_VERDICTS, frozenset)

    def test_quantization_blocked_in_commutation_set(self):
        assert "quantization_route_currently_blocked" in ALLOWED_COMMUTATION_VERDICTS

    def test_allowed_mapping_verdicts_is_frozenset(self):
        assert isinstance(ALLOWED_MAPPING_VERDICTS, frozenset)

    def test_compatible_only_in_mapping_set(self):
        assert "compatible_only" in ALLOWED_MAPPING_VERDICTS


# ================================================================
# TestTrackAOntology
# ================================================================


class TestTrackAOntology:
    """Track A: Closed vs open microphysical ontology."""

    def setup_method(self):
        self.track_a = build_track_a_ontology()

    def test_returns_qb_ontology_check(self):
        assert isinstance(self.track_a, QBOntologyCheck)

    def test_is_deterministic_at_native_level(self):
        assert self.track_a.is_deterministic_at_native_level is True

    def test_bath_not_in_native_ode(self):
        assert self.track_a.bath_coupling_in_native_ode is False

    def test_galley_regime_is_open(self):
        assert self.track_a.galley_regime_is_open is True

    def test_ontology_verdict_open_at_effective_level(self):
        assert self.track_a.ontology_verdict == "open_at_effective_level"

    def test_ontology_verdict_in_allowed_set(self):
        assert self.track_a.ontology_verdict in ALLOWED_ONTOLOGY_VERDICTS

    def test_native_dynamics_type_is_ode(self):
        assert "ode" in self.track_a.native_dynamics_type.lower()

    def test_canonical_equation_mentions_tau(self):
        assert "tau" in self.track_a.canonical_equation.lower()

    def test_notes_non_empty(self):
        assert len(self.track_a.notes) >= 3


# ================================================================
# TestTrackBCandidatesSS1SS2
# ================================================================


class TestTrackBCandidatesSS1SS2:
    """Track B candidates SS1 (pure ket) and SS2 (density matrix)."""

    def setup_method(self):
        self.ss1 = build_state_candidate_ss1_pure_ket()
        self.ss2 = build_state_candidate_ss2_density_matrix()

    def test_ss1_candidate_id(self):
        assert self.ss1.candidate_id == "SS1_pure_ket"

    def test_ss1_type_is_pure_ket(self):
        assert self.ss1.candidate_type == "pure_ket"

    def test_ss1_is_not_quantum_state_space(self):
        assert self.ss1.is_quantum_state_space is False

    def test_ss1_appendix_p_class(self):
        assert self.ss1.appendix_p_class == "compatible_but_ad_hoc"

    def test_ss1_not_present_in_grut(self):
        assert self.ss1.present_in_grut is False

    def test_ss1_has_disqualifying_reason(self):
        assert self.ss1.disqualifying_reason is not None
        assert len(self.ss1.disqualifying_reason) > 0

    def test_ss2_candidate_id(self):
        assert self.ss2.candidate_id == "SS2_density_matrix"

    def test_ss2_type_is_density_matrix(self):
        assert self.ss2.candidate_type == "density_matrix"

    def test_ss2_is_not_quantum_state_space(self):
        assert self.ss2.is_quantum_state_space is False

    def test_ss2_appendix_p_class(self):
        assert self.ss2.appendix_p_class == "compatible_but_ad_hoc"

    def test_ss2_not_present_in_grut(self):
        assert self.ss2.present_in_grut is False

    def test_ss2_status_absent(self):
        assert self.ss2.candidate_status == "absent"


# ================================================================
# TestTrackBCandidatesSS3SS4
# ================================================================


class TestTrackBCandidatesSS3SS4:
    """Track B candidates SS3 (CTP kernel) and SS4 (Wigner)."""

    def setup_method(self):
        self.ss3 = build_state_candidate_ss3_ctp_kernel()
        self.ss4 = build_state_candidate_ss4_wigner()

    def test_ss3_candidate_id(self):
        assert self.ss3.candidate_id == "SS3_ctp_kernel_rho"

    def test_ss3_type_is_ctp_kernel(self):
        assert self.ss3.candidate_type == "ctp_kernel_rho"

    def test_ss3_present_in_grut(self):
        assert self.ss3.present_in_grut is True

    def test_ss3_is_not_quantum_state_space(self):
        assert self.ss3.is_quantum_state_space is False

    def test_ss3_status_formally_compatible(self):
        assert self.ss3.candidate_status == "formally_compatible"

    def test_ss3_appendix_p_class(self):
        assert self.ss3.appendix_p_class == "compatible_but_ad_hoc"

    def test_ss3_disqualification_mentions_ghost(self):
        assert self.ss3.disqualifying_reason is not None
        reason_lower = self.ss3.disqualifying_reason.lower()
        assert "ghost" in reason_lower or "growth" in reason_lower or "ffm6" in reason_lower

    def test_ss4_candidate_id(self):
        assert self.ss4.candidate_id == "SS4_wigner_phase_space"

    def test_ss4_type_is_wigner(self):
        assert self.ss4.candidate_type == "wigner_phase_space"

    def test_ss4_not_present_in_grut(self):
        assert self.ss4.present_in_grut is False

    def test_ss4_is_not_quantum_state_space(self):
        assert self.ss4.is_quantum_state_space is False

    def test_ss4_disqualification_mentions_momentum(self):
        assert self.ss4.disqualifying_reason is not None
        reason_lower = self.ss4.disqualifying_reason.lower()
        assert "momentum" in reason_lower or "pi" in reason_lower or "phase" in reason_lower


# ================================================================
# TestTrackBCandidatesSS5SS6
# ================================================================


class TestTrackBCandidatesSS5SS6:
    """Track B candidates SS5 (influence functional) and SS6 (null)."""

    def setup_method(self):
        self.ss5 = build_state_candidate_ss5_influence_functional()
        self.ss6 = build_state_candidate_ss6_null()

    def test_ss5_candidate_id(self):
        assert self.ss5.candidate_id == "SS5_influence_functional"

    def test_ss5_type_is_influence_functional(self):
        assert self.ss5.candidate_type == "influence_functional"

    def test_ss5_present_in_grut(self):
        assert self.ss5.present_in_grut is True

    def test_ss5_is_not_quantum_state_space(self):
        assert self.ss5.is_quantum_state_space is False

    def test_ss5_status_present_not_quantum(self):
        assert self.ss5.candidate_status == "present_not_quantum"

    def test_ss5_appendix_p_class_effective_reduction(self):
        assert self.ss5.appendix_p_class == "effective_reduction"

    def test_ss6_candidate_id(self):
        assert self.ss6.candidate_id == "SS6_no_native_quantum_state"

    def test_ss6_type_is_null(self):
        assert self.ss6.candidate_type == "no_native_quantum_state"

    def test_ss6_is_not_quantum_state_space(self):
        assert self.ss6.is_quantum_state_space is False

    def test_ss6_status_null_result(self):
        assert self.ss6.candidate_status == "null_result"

    def test_ss6_appendix_p_class_bsr(self):
        assert self.ss6.appendix_p_class == "bounded_structural_result"

    def test_ss6_no_disqualifying_reason(self):
        assert self.ss6.disqualifying_reason is None


# ================================================================
# TestTrackBPrimaryFinding
# ================================================================


class TestTrackBPrimaryFinding:
    """Track B: Primary finding tests (aggregated state object result)."""

    def setup_method(self):
        self.track_b = build_track_b_state_object()

    def test_returns_qb_state_object_check(self):
        assert isinstance(self.track_b, QBStateObjectCheck)

    def test_n_candidates_equals_six(self):
        assert self.track_b.n_candidates == 6

    def test_n_viable_quantum_equals_zero(self):
        assert self.track_b.n_viable_quantum == 0

    def test_candidates_list_length(self):
        assert len(self.track_b.candidates) == 6

    def test_primary_candidate_type_null(self):
        assert self.track_b.primary_candidate_type == "no_native_quantum_state"

    def test_primary_appendix_p_class_bsr(self):
        assert self.track_b.primary_appendix_p_class == "bounded_structural_result"

    def test_missing_ingredient_mentions_complex_structure(self):
        mi = self.track_b.missing_ingredient.lower()
        assert "complex" in mi or "j" in mi or "structure" in mi

    def test_missing_ingredient_class_mip(self):
        assert self.track_b.missing_ingredient_appendix_p_class == "motivated_independent_postulation"

    def test_all_candidates_not_quantum(self):
        for c in self.track_b.candidates:
            assert c.is_quantum_state_space is False

    def test_candidate_types_all_in_allowed_set(self):
        for c in self.track_b.candidates:
            assert c.candidate_type in ALLOWED_STATE_OBJECT_TYPES

    def test_candidate_statuses_all_in_allowed_set(self):
        for c in self.track_b.candidates:
            assert c.candidate_status in ALLOWED_CANDIDATE_STATUSES

    def test_candidate_appendix_p_classes_all_valid(self):
        for c in self.track_b.candidates:
            assert c.appendix_p_class in ALLOWED_APPENDIX_P_CLASSES


# ================================================================
# TestTrackCPureMixed
# ================================================================


class TestTrackCPureMixed:
    """Track C: Pure vs mixed state mandate."""

    def setup_method(self):
        self.track_c = build_track_c_pure_mixed()

    def test_returns_qb_pure_mixed_check(self):
        assert isinstance(self.track_c, QBPureMixedCheck)

    def test_classical_state_is_pure(self):
        assert self.track_c.classical_state_is_pure is True

    def test_quantum_pure_state_not_natively_supported(self):
        assert self.track_c.quantum_pure_state_natively_supported is False

    def test_quantum_mixed_state_not_natively_supported(self):
        assert self.track_c.quantum_mixed_state_natively_supported is False

    def test_mixing_mechanism_absent(self):
        assert self.track_c.mixing_mechanism_present is False

    def test_open_system_suggests_mixed(self):
        assert self.track_c.effective_open_system_suggests_mixed is True

    def test_pure_mixed_verdict_not_natively_supported(self):
        assert self.track_c.pure_mixed_verdict == "not_natively_supported"

    def test_pure_mixed_verdict_in_allowed_set(self):
        assert self.track_c.pure_mixed_verdict in ALLOWED_PURE_MIXED_STATUSES

    def test_notes_non_empty(self):
        assert len(self.track_c.notes) >= 3


# ================================================================
# TestTrackDCommutation
# ================================================================


class TestTrackDCommutation:
    """Track D: Canonical momentum / commutation audit."""

    def setup_method(self):
        self.track_d = build_track_d_commutation()

    def test_returns_qb_commutation_check(self):
        assert isinstance(self.track_d, QBCommutationCheck)

    def test_eom_temporal_order_equals_one(self):
        assert self.track_d.grut_eom_temporal_order == 1

    def test_canonical_equation_mentions_tau(self):
        assert "tau" in self.track_d.canonical_equation.lower()

    def test_no_standard_lagrangian_kinetic_term(self):
        assert self.track_d.standard_lagrangian_kinetic_term is False

    def test_canonical_momentum_degenerate(self):
        assert "degenerate" in self.track_d.canonical_momentum_standard.lower()

    def test_bateman_doubled_momentum_cites_phi2(self):
        assert "phi_2" in self.track_d.bateman_doubled_momentum.lower() or \
               "phi2" in self.track_d.bateman_doubled_momentum.lower()

    def test_standard_ccr_not_applicable(self):
        assert self.track_d.standard_ccr_applicable is False

    def test_variational_obstruction_non_empty(self):
        assert len(self.track_d.variational_obstruction_description) > 20

    def test_no_alternative_symplectic_established(self):
        assert self.track_d.alternative_symplectic_established is False

    def test_commutation_verdict_currently_blocked(self):
        assert self.track_d.commutation_verdict == "quantization_route_currently_blocked"

    def test_commutation_verdict_in_allowed_set(self):
        assert self.track_d.commutation_verdict in ALLOWED_COMMUTATION_VERDICTS

    def test_notes_mention_first_order(self):
        notes_str = " ".join(self.track_d.notes).lower()
        assert "first" in notes_str or "order" in notes_str


# ================================================================
# TestTrackEMapping
# ================================================================


class TestTrackEMapping:
    """Track E: Doubled-field to state mapping ⟨Φ₁|ρ|Φ₂⟩."""

    def setup_method(self):
        self.track_e = build_track_e_mapping()

    def test_returns_qb_mapping_check(self):
        assert isinstance(self.track_e, QBMappingCheck)

    def test_ctp_fields_present(self):
        assert self.track_e.ctp_fields_present is True

    def test_phi_plus_formula_correct(self):
        assert self.track_e.phi_plus_formula == CTP_PHI_PLUS_FORMULA

    def test_phi_minus_formula_correct(self):
        assert self.track_e.phi_minus_formula == CTP_PHI_MINUS_FORMULA

    def test_phi_minus_eom_set(self):
        assert len(self.track_e.phi_minus_eom) > 0

    def test_phi_minus_growth_rate_sign_positive(self):
        assert self.track_e.phi_minus_growth_rate_sign == +1

    def test_phi_minus_cannot_be_imaginary_part(self):
        assert self.track_e.phi_minus_can_be_imaginary_part is False

    def test_formal_rho_notation_compatible(self):
        assert self.track_e.formal_rho_notation_compatible is True

    def test_prior_hilbert_space_required(self):
        assert self.track_e.prior_hilbert_space_required is True

    def test_mapping_verdict_compatible_only(self):
        assert self.track_e.mapping_verdict == "compatible_only"

    def test_mapping_verdict_in_allowed_set(self):
        assert self.track_e.mapping_verdict in ALLOWED_MAPPING_VERDICTS

    def test_notes_mention_ghost(self):
        notes_str = " ".join(self.track_e.notes).lower()
        assert "ghost" in notes_str or "grow" in notes_str


# ================================================================
# TestTrackFAppendixP
# ================================================================


class TestTrackFAppendixP:
    """Track F: Appendix P status per result."""

    def setup_method(self):
        self.track_f = build_track_f_appendix_p()

    def test_returns_qb_appendix_p_classification(self):
        assert isinstance(self.track_f, QBAppendixPClassification)

    def test_track_a_class_native_canon(self):
        assert self.track_f.track_a_class == "native_canon"

    def test_track_b_class_bsr(self):
        assert self.track_f.track_b_class == "bounded_structural_result"

    def test_track_c_class_bsr(self):
        assert self.track_f.track_c_class == "bounded_structural_result"

    def test_track_d_class_bsr(self):
        assert self.track_f.track_d_class == "bounded_structural_result"

    def test_track_e_class_cah(self):
        assert self.track_f.track_e_class == "compatible_but_ad_hoc"

    def test_overall_qb_class_bsr(self):
        assert self.track_f.overall_qb_class == "bounded_structural_result"

    def test_all_classes_in_allowed_set(self):
        for cls in [
            self.track_f.track_a_class,
            self.track_f.track_b_class,
            self.track_f.track_c_class,
            self.track_f.track_d_class,
            self.track_f.track_e_class,
            self.track_f.overall_qb_class,
        ]:
            assert cls in ALLOWED_APPENDIX_P_CLASSES

    def test_notes_non_empty(self):
        assert len(self.track_f.notes) >= 4


# ================================================================
# TestTrackGNonclaims
# ================================================================


class TestTrackGNonclaims:
    """Track G: Nonclaim firewall."""

    def setup_method(self):
        self.track_g = build_track_g_nonclaims()

    def test_returns_qb_nonclaim_firewall(self):
        assert isinstance(self.track_g, QBNonclaimFirewall)

    def test_n_nonclaims_at_least_seven(self):
        assert self.track_g.n_nonclaims >= 7

    def test_nonclaims_list_length_matches(self):
        assert len(self.track_g.nonclaims) == self.track_g.n_nonclaims

    def test_all_registered_true(self):
        assert self.track_g.all_registered is True

    def test_not_claiming_impossibility(self):
        combined = " ".join(self.track_g.nonclaims).lower()
        assert "not_claiming" in combined or "not claiming" in combined

    def test_nonclaim_about_ctp_hilbert_space(self):
        combined = " ".join(self.track_g.nonclaims).lower()
        assert "hilbert" in combined or "ffm6" in combined

    def test_nonclaim_about_complex_structure_j(self):
        combined = " ".join(self.track_g.nonclaims).lower()
        assert "complex" in combined or "structure" in combined

    def test_nonclaim_about_null_verdict(self):
        combined = " ".join(self.track_g.nonclaims).lower()
        assert "null" in combined or "bsr" in combined or "bounded" in combined


# ================================================================
# TestHardGatedVerdicts
# ================================================================


class TestHardGatedVerdicts:
    """Three hard-gated verdict tests — constants and result consistency."""

    def test_primary_verdict_constant_set(self):
        assert QB_PRIMARY_STATE_SPACE_VERDICT == "density_matrix_or_functional_state_required"

    def test_primary_verdict_in_allowed_set(self):
        assert QB_PRIMARY_STATE_SPACE_VERDICT in ALLOWED_PRIMARY_STATE_SPACE_VERDICTS

    def test_commutation_verdict_constant_set(self):
        assert QB_COMMUTATION_VERDICT == "quantization_route_currently_blocked"

    def test_commutation_verdict_in_allowed_set(self):
        assert QB_COMMUTATION_VERDICT in ALLOWED_COMMUTATION_VERDICTS

    def test_mapping_verdict_constant_set(self):
        assert QB_MAPPING_VERDICT == "compatible_only"

    def test_mapping_verdict_in_allowed_set(self):
        assert QB_MAPPING_VERDICT in ALLOWED_MAPPING_VERDICTS

    def test_overall_appendix_p_class_bsr(self):
        assert QB_OVERALL_APPENDIX_P_CLASS == "bounded_structural_result"

    def test_overall_class_in_allowed_set(self):
        assert QB_OVERALL_APPENDIX_P_CLASS in ALLOWED_APPENDIX_P_CLASSES

    def test_pure_hilbert_not_primary_verdict(self):
        assert QB_PRIMARY_STATE_SPACE_VERDICT != "pure_state_hilbert_space_natively_supported"

    def test_ctp_viable_not_primary_verdict(self):
        assert QB_PRIMARY_STATE_SPACE_VERDICT != "ctp_doubled_field_state_space_viable"

    def test_mapping_not_exact(self):
        assert QB_MAPPING_VERDICT != "doubled_field_density_matrix_mapping_exact"

    def test_mapping_not_natural_but_unbuilt(self):
        # compatible_only is more conservative than natural_but_unbuilt
        assert QB_MAPPING_VERDICT != "natural_but_unbuilt"


# ================================================================
# TestMasterAudit
# ================================================================


class TestMasterAudit:
    """Tests for run_qb_quantum_state_space() master function."""

    def setup_method(self):
        self.result = run_qb_quantum_state_space()

    def test_returns_qb_state_space_result(self):
        assert isinstance(self.result, QBStateSpaceResult)

    def test_valid_true(self):
        assert self.result.valid is True

    def test_primary_verdict_matches_constant(self):
        assert self.result.primary_state_space_verdict == QB_PRIMARY_STATE_SPACE_VERDICT

    def test_commutation_verdict_matches_constant(self):
        assert self.result.commutation_verdict == QB_COMMUTATION_VERDICT

    def test_mapping_verdict_matches_constant(self):
        assert self.result.mapping_verdict == QB_MAPPING_VERDICT

    def test_qb_appendix_p_class_bsr(self):
        assert self.result.qb_appendix_p_class == "bounded_structural_result"

    def test_track_b_n_candidates_six(self):
        assert self.result.track_b_state_object.n_candidates == 6

    def test_track_b_n_viable_zero(self):
        assert self.result.track_b_state_object.n_viable_quantum == 0

    def test_track_g_all_registered(self):
        assert self.result.track_g_nonclaims.all_registered is True

    def test_diagnostics_populated(self):
        assert isinstance(self.result.diagnostics, dict)
        assert len(self.result.diagnostics) >= 5

    def test_diagnostics_n_viable_quantum(self):
        assert self.result.diagnostics["n_viable_quantum"] == 0

    def test_diagnostics_phi_minus_growth_rate_sign(self):
        assert self.result.diagnostics["phi_minus_growth_rate_sign"] == +1

    def test_diagnostics_standard_ccr_not_applicable(self):
        assert self.result.diagnostics["standard_ccr_applicable"] is False

    def test_diagnostics_tau_sq(self):
        assert self.result.diagnostics["tau_sq"] == pytest.approx(1.5)

    def test_all_three_verdicts_in_allowed_sets(self):
        assert self.result.primary_state_space_verdict in ALLOWED_PRIMARY_STATE_SPACE_VERDICTS
        assert self.result.commutation_verdict in ALLOWED_COMMUTATION_VERDICTS
        assert self.result.mapping_verdict in ALLOWED_MAPPING_VERDICTS
