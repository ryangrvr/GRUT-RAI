"""Tests for grut/qb5_complex_structure_audit.py — Appendix Q-B.5.

Full deterministic test suite for the GRUT Complex Structure and Kinematic
Upgrade audit. Covers all 9 audit tracks and all 4 hard-gated verdicts.

Structure
---------
  TestQB5Constants                  (16 tests)
  TestTrackAMissingIngredient       (10 tests)
  TestTrackBNativeRoutesIndividual  (15 tests)
  TestTrackBNativeDerivationAudit   ( 8 tests)
  TestTrackCEffectiveRoutesIndividual (15 tests)
  TestTrackCEffectiveInductionAudit  ( 8 tests)
  TestTrackDPostulate               (12 tests)
  TestTrackEKinematicSufficiency    (11 tests)
  TestTrackFGhostConstraint         (12 tests)
  TestTrackGAppendixP               (10 tests)
  TestTrackHReadiness               ( 9 tests)
  TestTrackINonclaims               ( 8 tests)
  TestHardGatedVerdicts             (14 tests)
  TestMasterAudit                   (14 tests)

Target: ~162 tests
"""

import math

import pytest

from grut.qb5_complex_structure_audit import (
    # Constants
    ALLOWED_PRIMARY_J_STATUSES,
    ALLOWED_SUFFICIENCY_VERDICTS,
    ALLOWED_DOUBLED_FIELD_VERDICTS,
    ALLOWED_READINESS_VERDICTS,
    ALLOWED_APPENDIX_P_CLASSES,
    ALLOWED_MISSING_ELEMENT_TYPES,
    ALLOWED_EFFECTIVE_ROUTE_CLASSIFICATIONS,
    N_NATIVE_ROUTES_TESTED,
    N_EFFECTIVE_ROUTES_TESTED,
    N_NATIVE_ROUTES_ACCEPTED,
    N_EFFECTIVE_ROUTES_VIABLE,
    N_CONVERGENT_MOTIVATIONS_FOR_J,
    N_MINIMUM_KINEMATIC_PACKAGE_ITEMS,
    N_QB5_NONCLAIMS,
    QB5_NONCLAIMS,
    TAU_SQ,
    TAU,
    PHI_MINUS_GROWTH_RATE,
    PHI_MINUS_GROWTH_RATE_SIGN,
    PHI_MINUS_CAN_BE_IMAGINARY_PART,
    GHOST_NORM_GROWTH_COEFFICIENT,
    QB5_PRIMARY_J_STATUS,
    QB5_SUFFICIENCY_VERDICT,
    QB5_DOUBLED_FIELD_VERDICT,
    QB5_READINESS_VERDICT,
    QB5_OVERALL_APPENDIX_P_CLASS,
    QB5_MINIMUM_KINEMATIC_PACKAGE,
    # Dataclasses
    QB5MissingIngredientAnalysis,
    QB5NativeRoute,
    QB5NativeDerivationAudit,
    QB5EffectiveRoute,
    QB5EffectiveInductionAudit,
    QB5PostulateAudit,
    QB5KinematicSufficiencyAudit,
    QB5GhostConstraintAudit,
    QB5AppendixPEntry,
    QB5AppendixPClassificationAudit,
    QB5ReadinessAudit,
    QB5NonclaimFirewall,
    QB5ComplexStructureResult,
    # Builder functions
    build_track_a_missing_ingredient,
    build_track_b_native_derivation,
    build_track_c_effective_induction,
    build_track_d_postulate,
    build_track_e_kinematic_sufficiency,
    build_track_f_ghost_constraint,
    build_track_g_appendix_p,
    build_track_h_readiness,
    build_track_i_nonclaims,
    build_native_route_nr1_ctp_doubled_fields,
    build_native_route_nr2_memory_kernel,
    build_native_route_nr3_galley_ctp_action,
    build_native_route_nr4_response_information_geometry,
    build_native_route_nr5_symplectic_phase_like,
    build_effective_route_er1_low_frequency,
    build_effective_route_er2_coarse_grained,
    build_effective_route_er3_doubled_real,
    build_effective_route_er4_environment_induced,
    build_effective_route_er5_linearized_perturbation,
    build_allowed_claims,
    build_forbidden_claims,
    # Master function
    run_qb5_complex_structure_audit,
)


# ================================================================
# TestQB5Constants
# ================================================================


class TestQB5Constants:
    """Tests for module-level vocabulary constants."""

    def test_primary_j_statuses_is_frozenset(self):
        assert isinstance(ALLOWED_PRIMARY_J_STATUSES, frozenset)

    def test_mip_in_primary_j_statuses(self):
        assert "complex_structure_motivated_independent_postulation" in ALLOWED_PRIMARY_J_STATUSES

    def test_natively_derived_in_primary_j_statuses(self):
        assert "complex_structure_natively_derived" in ALLOWED_PRIMARY_J_STATUSES

    def test_sufficiency_verdicts_is_frozenset(self):
        assert isinstance(ALLOWED_SUFFICIENCY_VERDICTS, frozenset)

    def test_j_necessary_not_sufficient_in_verdicts(self):
        assert "J_necessary_but_not_sufficient" in ALLOWED_SUFFICIENCY_VERDICTS

    def test_doubled_field_verdicts_is_frozenset(self):
        assert isinstance(ALLOWED_DOUBLED_FIELD_VERDICTS, frozenset)

    def test_obstructed_in_doubled_field_verdicts(self):
        assert "doubled_field_pair_complexification_obstructed" in ALLOWED_DOUBLED_FIELD_VERDICTS

    def test_readiness_verdicts_is_frozenset(self):
        assert isinstance(ALLOWED_READINESS_VERDICTS, frozenset)

    def test_proceed_if_postulated_in_readiness(self):
        assert "proceed_only_if_J_is_postulated" in ALLOWED_READINESS_VERDICTS

    def test_n_native_routes_equals_five(self):
        assert N_NATIVE_ROUTES_TESTED == 5

    def test_n_effective_routes_equals_five(self):
        assert N_EFFECTIVE_ROUTES_TESTED == 5

    def test_n_native_routes_accepted_zero(self):
        assert N_NATIVE_ROUTES_ACCEPTED == 0

    def test_n_effective_routes_viable_zero(self):
        assert N_EFFECTIVE_ROUTES_VIABLE == 0

    def test_n_convergent_motivations_two(self):
        assert N_CONVERGENT_MOTIVATIONS_FOR_J == 2

    def test_n_minimum_package_items_three(self):
        assert N_MINIMUM_KINEMATIC_PACKAGE_ITEMS == 3

    def test_n_nonclaims_eight(self):
        assert N_QB5_NONCLAIMS == 8

    def test_phi_minus_growth_rate_sign_positive(self):
        assert PHI_MINUS_GROWTH_RATE_SIGN == +1

    def test_phi_minus_cannot_be_imaginary_part(self):
        assert PHI_MINUS_CAN_BE_IMAGINARY_PART is False

    def test_tau_sq_canonical(self):
        assert TAU_SQ == pytest.approx(1.5)

    def test_tau_consistent(self):
        assert TAU == pytest.approx(math.sqrt(TAU_SQ))

    def test_ghost_norm_growth_positive(self):
        assert GHOST_NORM_GROWTH_COEFFICIENT > 0

    def test_minimum_kinematic_package_length(self):
        assert len(QB5_MINIMUM_KINEMATIC_PACKAGE) == 3


# ================================================================
# TestTrackAMissingIngredient
# ================================================================


class TestTrackAMissingIngredient:
    """Track A: Missing-ingredient confirmation check."""

    def setup_method(self):
        self.track_a = build_track_a_missing_ingredient()

    def test_returns_correct_type(self):
        assert isinstance(self.track_a, QB5MissingIngredientAnalysis)

    def test_missing_element_type_is_complex_structure_j(self):
        assert self.track_a.missing_element_type == "complex_structure_J_on_state_space"

    def test_missing_element_type_in_allowed_set(self):
        assert self.track_a.missing_element_type in ALLOWED_MISSING_ELEMENT_TYPES

    def test_not_symplectic_only(self):
        assert self.track_a.is_symplectic_only is False

    def test_not_doubled_real_structure(self):
        assert self.track_a.is_doubled_real_structure is False

    def test_not_full_hilbert_package(self):
        assert self.track_a.is_full_hilbert_package is False

    def test_not_larger_kinematic_bundle(self):
        assert self.track_a.is_larger_kinematic_bundle is False

    def test_minimum_to_unblock_qc_length(self):
        assert len(self.track_a.minimum_to_unblock_qc) == 3

    def test_n_minimum_items_three(self):
        assert self.track_a.n_minimum_items == 3

    def test_missing_element_p_class_mip(self):
        assert self.track_a.missing_element_appendix_p_class == "motivated_independent_postulation"

    def test_gap_severity_is_kinematic(self):
        assert "kinematic" in self.track_a.gap_severity.lower()

    def test_notes_non_empty(self):
        assert len(self.track_a.notes) >= 4


# ================================================================
# TestTrackBNativeRoutesIndividual
# ================================================================


class TestTrackBNativeRoutesIndividual:
    """Track B: Individual native route tests."""

    def setup_method(self):
        self.nr1 = build_native_route_nr1_ctp_doubled_fields()
        self.nr2 = build_native_route_nr2_memory_kernel()
        self.nr3 = build_native_route_nr3_galley_ctp_action()
        self.nr4 = build_native_route_nr4_response_information_geometry()
        self.nr5 = build_native_route_nr5_symplectic_phase_like()

    def test_nr1_id(self):
        assert self.nr1.route_id == "NR1_ctp_doubled_fields"

    def test_nr1_no_exact_derivation(self):
        assert self.nr1.exact_derivation_exists is False

    def test_nr1_appendix_p_class_foi(self):
        assert self.nr1.appendix_p_class == "forbidden_or_inconsistent"

    def test_nr1_rejection_mentions_ghost(self):
        assert "ghost" in self.nr1.rejection_reason.lower() or "norm" in self.nr1.rejection_reason.lower()

    def test_nr2_id(self):
        assert self.nr2.route_id == "NR2_memory_kernel"

    def test_nr2_no_exact_derivation(self):
        assert self.nr2.exact_derivation_exists is False

    def test_nr2_appendix_p_class_cah(self):
        assert self.nr2.appendix_p_class == "compatible_but_ad_hoc"

    def test_nr3_no_exact_derivation(self):
        assert self.nr3.exact_derivation_exists is False

    def test_nr3_appendix_p_class_cah(self):
        assert self.nr3.appendix_p_class == "compatible_but_ad_hoc"

    def test_nr4_no_exact_derivation(self):
        assert self.nr4.exact_derivation_exists is False

    def test_nr5_id(self):
        assert self.nr5.route_id == "NR5_symplectic_phase_like"

    def test_nr5_no_exact_derivation(self):
        assert self.nr5.exact_derivation_exists is False

    def test_nr5_rejection_mentions_discrete(self):
        reason_lower = self.nr5.rejection_reason.lower()
        assert "discrete" in reason_lower or "z2" in reason_lower or "winding" in reason_lower

    def test_all_routes_have_rejection_reason(self):
        for nr in [self.nr1, self.nr2, self.nr3, self.nr4, self.nr5]:
            assert len(nr.rejection_reason) > 10

    def test_all_routes_p_class_in_allowed(self):
        for nr in [self.nr1, self.nr2, self.nr3, self.nr4, self.nr5]:
            assert nr.appendix_p_class in ALLOWED_APPENDIX_P_CLASSES


# ================================================================
# TestTrackBNativeDerivationAudit
# ================================================================


class TestTrackBNativeDerivationAudit:
    """Track B: Aggregated native derivation audit."""

    def setup_method(self):
        self.track_b = build_track_b_native_derivation()

    def test_returns_correct_type(self):
        assert isinstance(self.track_b, QB5NativeDerivationAudit)

    def test_n_routes_tested_five(self):
        assert self.track_b.n_routes_tested == 5

    def test_n_routes_accepted_zero(self):
        assert self.track_b.n_routes_accepted == 0

    def test_native_derivation_not_possible(self):
        assert self.track_b.native_derivation_possible is False

    def test_routes_list_length_five(self):
        assert len(self.track_b.routes) == 5

    def test_all_routes_no_exact_derivation(self):
        for r in self.track_b.routes:
            assert r.exact_derivation_exists is False

    def test_rejection_summary_non_empty(self):
        assert len(self.track_b.rejection_summary) > 50

    def test_notes_non_empty(self):
        assert len(self.track_b.notes) >= 4


# ================================================================
# TestTrackCEffectiveRoutesIndividual
# ================================================================


class TestTrackCEffectiveRoutesIndividual:
    """Track C: Individual effective-induction route tests."""

    def setup_method(self):
        self.er1 = build_effective_route_er1_low_frequency()
        self.er2 = build_effective_route_er2_coarse_grained()
        self.er3 = build_effective_route_er3_doubled_real()
        self.er4 = build_effective_route_er4_environment_induced()
        self.er5 = build_effective_route_er5_linearized_perturbation()

    def test_er1_not_viable(self):
        assert self.er1.effective_j_viable is False

    def test_er1_blocked(self):
        assert self.er1.classification == "blocked"

    def test_er2_not_viable(self):
        assert self.er2.effective_j_viable is False

    def test_er2_blocked_mentions_circular(self):
        reason_lower = self.er2.rejection_reason.lower()
        assert "circular" in reason_lower or "quantum" in reason_lower

    def test_er3_not_viable(self):
        assert self.er3.effective_j_viable is False

    def test_er3_classification_underdetermined(self):
        assert self.er3.classification == "underdetermined_compatibility_only"

    def test_er3_mentions_ghost(self):
        combined = (self.er3.rejection_reason or "") + " ".join(self.er3.notes)
        assert "ghost" in combined.lower() or "grow" in combined.lower()

    def test_er4_not_viable(self):
        assert self.er4.effective_j_viable is False

    def test_er4_blocked(self):
        assert self.er4.classification == "blocked"

    def test_er5_not_viable(self):
        assert self.er5.effective_j_viable is False

    def test_er5_mentions_dispersion(self):
        reason_lower = (self.er5.rejection_reason or "").lower()
        notes_lower = " ".join(self.er5.notes).lower()
        combined = reason_lower + notes_lower
        assert "imaginary" in combined or "damp" in combined or "omega" in combined

    def test_all_classifications_in_allowed_set(self):
        for er in [self.er1, self.er2, self.er3, self.er4, self.er5]:
            assert er.classification in ALLOWED_EFFECTIVE_ROUTE_CLASSIFICATIONS

    def test_all_have_rejection_reason(self):
        for er in [self.er1, self.er2, self.er3, self.er4, self.er5]:
            assert er.rejection_reason is not None
            assert len(er.rejection_reason) > 10

    def test_er3_is_closest_route(self):
        # ER3 is the least-bad (underdetermined vs blocked)
        assert self.er3.classification == "underdetermined_compatibility_only"


# ================================================================
# TestTrackCEffectiveInductionAudit
# ================================================================


class TestTrackCEffectiveInductionAudit:
    """Track C: Aggregated effective-induction audit."""

    def setup_method(self):
        self.track_c = build_track_c_effective_induction()

    def test_returns_correct_type(self):
        assert isinstance(self.track_c, QB5EffectiveInductionAudit)

    def test_n_routes_tested_five(self):
        assert self.track_c.n_routes_tested == 5

    def test_n_routes_viable_zero(self):
        assert self.track_c.n_routes_viable == 0

    def test_effective_induction_not_possible(self):
        assert self.track_c.effective_induction_possible is False

    def test_closest_route_er3(self):
        assert self.track_c.closest_route == "ER3_doubled_real_effective_complex"

    def test_closest_route_classification_underdetermined(self):
        assert self.track_c.closest_route_classification == "underdetermined_compatibility_only"

    def test_routes_list_length_five(self):
        assert len(self.track_c.routes) == 5

    def test_all_routes_not_viable(self):
        for r in self.track_c.routes:
            assert r.effective_j_viable is False


# ================================================================
# TestTrackDPostulate
# ================================================================


class TestTrackDPostulate:
    """Track D: Independent-postulate qualification audit."""

    def setup_method(self):
        self.track_d = build_track_d_postulate()

    def test_returns_correct_type(self):
        assert isinstance(self.track_d, QB5PostulateAudit)

    def test_j_does_not_require_new_dof(self):
        assert self.track_d.j_requires_new_dof is False

    def test_j_requires_new_kinematic_structure(self):
        assert self.track_d.j_requires_new_kinematic_structure is True

    def test_gap_class_kinematic(self):
        assert "kinematic" in self.track_d.gap_class.lower()

    def test_n_convergent_motivations_two(self):
        assert self.track_d.n_convergent_motivations == 2

    def test_convergent_motivations_list_length_two(self):
        assert len(self.track_d.convergent_motivations) == 2

    def test_motivations_mention_ctp(self):
        combined = " ".join(self.track_d.convergent_motivations).lower()
        assert "ctp" in combined or "open" in combined or "schwinger" in combined

    def test_motivations_mention_o3_topology(self):
        combined = " ".join(self.track_d.convergent_motivations).lower()
        assert "o3" in combined or "topolog" in combined or "winding" in combined

    def test_at_least_one_parameter_constrained(self):
        assert self.track_d.at_least_one_parameter_constrained is True

    def test_constrained_parameter_tau_sq(self):
        assert "tau" in self.track_d.constrained_parameter.lower()

    def test_mip_qualifies(self):
        assert self.track_d.mip_qualifies is True

    def test_postulate_class_mip(self):
        assert self.track_d.postulate_appendix_p_class == "motivated_independent_postulation"

    def test_minimal_postulate_mentions_j_sq(self):
        postulate_lower = self.track_d.minimal_postulate_form.lower()
        assert "j" in postulate_lower and ("sq" in postulate_lower or "squared" in postulate_lower or "²" in postulate_lower or "2" in postulate_lower)

    def test_postulate_conditions_non_empty(self):
        assert len(self.track_d.postulate_conditions) >= 3


# ================================================================
# TestTrackEKinematicSufficiency
# ================================================================


class TestTrackEKinematicSufficiency:
    """Track E: Kinematic sufficiency audit."""

    def setup_method(self):
        self.track_e = build_track_e_kinematic_sufficiency()

    def test_returns_correct_type(self):
        assert isinstance(self.track_e, QB5KinematicSufficiencyAudit)

    def test_j_alone_not_sufficient(self):
        assert self.track_e.j_alone_sufficient is False

    def test_j_is_necessary(self):
        assert self.track_e.j_necessary is True

    def test_j_enables_complex_superposition(self):
        assert self.track_e.j_enables_complex_superposition is True

    def test_j_does_not_enable_inner_product(self):
        assert self.track_e.j_enables_inner_product is False

    def test_j_does_not_enable_normalization(self):
        assert self.track_e.j_enables_normalization is False

    def test_j_does_not_enable_dynamics_generator(self):
        assert self.track_e.j_enables_dynamics_generator is False

    def test_j_does_not_enable_state_space_topology(self):
        assert self.track_e.j_enables_state_space_topology is False

    def test_minimum_package_length_three(self):
        assert len(self.track_e.minimum_sufficient_package) == 3

    def test_n_minimum_package_items_three(self):
        assert self.track_e.n_minimum_package_items == 3

    def test_sufficiency_verdict_j_necessary_not_sufficient(self):
        assert self.track_e.sufficiency_verdict == "J_necessary_but_not_sufficient"

    def test_inner_product_classification_mip(self):
        assert self.track_e.inner_product_classification == "motivated_independent_postulation"


# ================================================================
# TestTrackFGhostConstraint
# ================================================================


class TestTrackFGhostConstraint:
    """Track F: Ghost / doubled-field constraint audit."""

    def setup_method(self):
        self.track_f = build_track_f_ghost_constraint()

    def test_returns_correct_type(self):
        assert isinstance(self.track_f, QB5GhostConstraintAudit)

    def test_phi_minus_growth_rate_sign_positive(self):
        assert self.track_f.phi_minus_growth_rate_sign == +1

    def test_phi_minus_growth_rate_positive(self):
        assert self.track_f.phi_minus_growth_rate > 0

    def test_phi_minus_cannot_be_imaginary_part(self):
        assert self.track_f.phi_minus_can_be_imaginary_part is False

    def test_formal_j_satisfies_j_sq(self):
        assert self.track_f.formal_j_satisfies_j_sq is True

    def test_norm_not_conserved(self):
        assert self.track_f.norm_conserved_under_dynamics is False

    def test_norm_growth_rate_sign_positive(self):
        assert self.track_f.norm_growth_rate_sign == +1

    def test_no_repackaging_attempts(self):
        assert self.track_f.n_repackaging_attempts == 0

    def test_repackaging_not_viable(self):
        assert self.track_f.repackaging_viable is False

    def test_repackaging_failure_mentions_phi_minus(self):
        failure_lower = self.track_f.repackaging_failure_reason.lower()
        assert "phi_minus" in failure_lower or "ghost" in failure_lower or "phi" in failure_lower

    def test_doubled_field_verdict_obstructed(self):
        assert self.track_f.doubled_field_verdict == "doubled_field_pair_complexification_obstructed"

    def test_doubled_field_verdict_in_allowed_set(self):
        assert self.track_f.doubled_field_verdict in ALLOWED_DOUBLED_FIELD_VERDICTS

    def test_norm_growth_formula_mentions_phi_minus(self):
        formula_lower = self.track_f.norm_growth_term.lower()
        assert "phi_minus" in formula_lower or "phi" in formula_lower


# ================================================================
# TestTrackGAppendixP
# ================================================================


class TestTrackGAppendixP:
    """Track G: Appendix P classification per route."""

    def setup_method(self):
        self.track_g = build_track_g_appendix_p()

    def test_returns_correct_type(self):
        assert isinstance(self.track_g, QB5AppendixPClassificationAudit)

    def test_n_entries_populated(self):
        assert self.track_g.n_entries >= 4

    def test_entries_list_length_matches(self):
        assert len(self.track_g.entries) == self.track_g.n_entries

    def test_overall_class_mip(self):
        assert self.track_g.overall_j_class == "motivated_independent_postulation"

    def test_mip_entry_present(self):
        classes = [e.appendix_p_class for e in self.track_g.entries]
        assert "motivated_independent_postulation" in classes

    def test_foi_entry_present_for_nr1(self):
        classes = [e.appendix_p_class for e in self.track_g.entries]
        assert "forbidden_or_inconsistent" in classes

    def test_all_entries_have_allowed_claim(self):
        for e in self.track_g.entries:
            assert len(e.allowed_claim) > 10

    def test_all_entries_have_forbidden_claim(self):
        for e in self.track_g.entries:
            assert len(e.forbidden_claim) > 10

    def test_all_p_classes_in_allowed_set(self):
        for e in self.track_g.entries:
            assert e.appendix_p_class in ALLOWED_APPENDIX_P_CLASSES

    def test_notes_non_empty(self):
        assert len(self.track_g.notes) >= 4


# ================================================================
# TestTrackHReadiness
# ================================================================


class TestTrackHReadiness:
    """Track H: Quantum program readiness audit."""

    def setup_method(self):
        self.track_h = build_track_h_readiness()

    def test_returns_correct_type(self):
        assert isinstance(self.track_h, QB5ReadinessAudit)

    def test_native_grut_not_sufficient(self):
        assert self.track_h.native_grut_sufficient_for_qc is False

    def test_j_postulation_required(self):
        assert self.track_h.j_postulation_required is True

    def test_inner_product_postulation_required(self):
        assert self.track_h.inner_product_postulation_required is True

    def test_qc_cannot_proceed_natively(self):
        assert self.track_h.qc_can_proceed_natively is False

    def test_qc_can_proceed_with_postulate(self):
        assert self.track_h.qc_can_proceed_with_postulate is True

    def test_readiness_verdict_proceed_if_postulated(self):
        assert self.track_h.readiness_verdict == "proceed_only_if_J_is_postulated"

    def test_readiness_verdict_in_allowed_set(self):
        assert self.track_h.readiness_verdict in ALLOWED_READINESS_VERDICTS

    def test_qc_appendix_p_floor_mip(self):
        assert self.track_h.qc_appendix_p_floor == "motivated_independent_postulation"

    def test_conditions_for_qc_non_empty(self):
        assert len(self.track_h.conditions_for_qc) >= 4


# ================================================================
# TestTrackINonclaims
# ================================================================


class TestTrackINonclaims:
    """Track I: Nonclaim firewall."""

    def setup_method(self):
        self.track_i = build_track_i_nonclaims()

    def test_returns_correct_type(self):
        assert isinstance(self.track_i, QB5NonclaimFirewall)

    def test_n_nonclaims_eight(self):
        assert self.track_i.n_nonclaims == 8

    def test_nonclaims_list_length_eight(self):
        assert len(self.track_i.nonclaims) == 8

    def test_all_registered_true(self):
        assert self.track_i.all_registered is True

    def test_nonclaim_about_doubled_fields(self):
        combined = " ".join(self.track_i.nonclaims).lower()
        assert "doubled" in combined or "ctp" in combined

    def test_nonclaim_about_notation(self):
        combined = " ".join(self.track_i.nonclaims).lower()
        assert "notation" in combined or "symbol" in combined or "i" in combined

    def test_nonclaim_about_open_system(self):
        combined = " ".join(self.track_i.nonclaims).lower()
        assert "open" in combined or "born" in combined or "probability" in combined

    def test_nonclaim_about_postulated_j_not_native_canon(self):
        combined = " ".join(self.track_i.nonclaims).lower()
        assert "native_canon" in combined or "native" in combined


# ================================================================
# TestHardGatedVerdicts
# ================================================================


class TestHardGatedVerdicts:
    """Four hard-gated verdict tests — constants and correctness."""

    def test_primary_j_status_constant(self):
        assert QB5_PRIMARY_J_STATUS == "complex_structure_motivated_independent_postulation"

    def test_primary_j_status_in_allowed_set(self):
        assert QB5_PRIMARY_J_STATUS in ALLOWED_PRIMARY_J_STATUSES

    def test_primary_j_not_natively_derived(self):
        assert QB5_PRIMARY_J_STATUS != "complex_structure_natively_derived"

    def test_primary_j_not_effectively_induced(self):
        assert QB5_PRIMARY_J_STATUS != "complex_structure_effectively_induced"

    def test_primary_j_not_underdetermined(self):
        assert QB5_PRIMARY_J_STATUS != "complex_structure_still_underdetermined"

    def test_sufficiency_verdict_constant(self):
        assert QB5_SUFFICIENCY_VERDICT == "J_necessary_but_not_sufficient"

    def test_sufficiency_verdict_in_allowed_set(self):
        assert QB5_SUFFICIENCY_VERDICT in ALLOWED_SUFFICIENCY_VERDICTS

    def test_sufficiency_not_alone_sufficient(self):
        assert QB5_SUFFICIENCY_VERDICT != "J_alone_sufficient_for_QC"

    def test_doubled_field_verdict_constant(self):
        assert QB5_DOUBLED_FIELD_VERDICT == "doubled_field_pair_complexification_obstructed"

    def test_doubled_field_verdict_in_allowed_set(self):
        assert QB5_DOUBLED_FIELD_VERDICT in ALLOWED_DOUBLED_FIELD_VERDICTS

    def test_doubled_field_not_valid_complexification(self):
        assert QB5_DOUBLED_FIELD_VERDICT != "doubled_field_pair_supports_valid_complexification"

    def test_readiness_verdict_constant(self):
        assert QB5_READINESS_VERDICT == "proceed_only_if_J_is_postulated"

    def test_readiness_verdict_in_allowed_set(self):
        assert QB5_READINESS_VERDICT in ALLOWED_READINESS_VERDICTS

    def test_readiness_not_ready_unconditionally(self):
        assert QB5_READINESS_VERDICT != "ready_to_proceed_with_QC"

    def test_overall_p_class_mip(self):
        assert QB5_OVERALL_APPENDIX_P_CLASS == "motivated_independent_postulation"


# ================================================================
# TestMasterAudit
# ================================================================


class TestMasterAudit:
    """Tests for run_qb5_complex_structure_audit() master function."""

    def setup_method(self):
        self.result = run_qb5_complex_structure_audit()

    def test_returns_correct_type(self):
        assert isinstance(self.result, QB5ComplexStructureResult)

    def test_valid_true(self):
        assert self.result.valid is True

    def test_primary_j_status_matches_constant(self):
        assert self.result.primary_J_status == QB5_PRIMARY_J_STATUS

    def test_sufficiency_verdict_matches_constant(self):
        assert self.result.sufficiency_verdict == QB5_SUFFICIENCY_VERDICT

    def test_doubled_field_verdict_matches_constant(self):
        assert self.result.doubled_field_verdict == QB5_DOUBLED_FIELD_VERDICT

    def test_readiness_verdict_matches_constant(self):
        assert self.result.readiness_verdict == QB5_READINESS_VERDICT

    def test_qb5_appendix_p_class_mip(self):
        assert self.result.qb5_appendix_p_class == "motivated_independent_postulation"

    def test_allowed_claims_non_empty(self):
        assert len(self.result.allowed_claims) >= 6

    def test_forbidden_claims_non_empty(self):
        assert len(self.result.forbidden_claims) >= 6

    def test_diagnostics_populated(self):
        assert isinstance(self.result.diagnostics, dict)
        assert len(self.result.diagnostics) >= 8

    def test_diagnostics_n_native_accepted_zero(self):
        assert self.result.diagnostics["n_native_routes_accepted"] == 0

    def test_diagnostics_n_effective_viable_zero(self):
        assert self.result.diagnostics["n_effective_routes_viable"] == 0

    def test_diagnostics_mip_qualifies(self):
        assert self.result.diagnostics["mip_qualifies"] is True

    def test_diagnostics_j_alone_not_sufficient(self):
        assert self.result.diagnostics["j_alone_sufficient"] is False

    def test_all_four_verdicts_in_allowed_sets(self):
        assert self.result.primary_J_status in ALLOWED_PRIMARY_J_STATUSES
        assert self.result.sufficiency_verdict in ALLOWED_SUFFICIENCY_VERDICTS
        assert self.result.doubled_field_verdict in ALLOWED_DOUBLED_FIELD_VERDICTS
        assert self.result.readiness_verdict in ALLOWED_READINESS_VERDICTS
