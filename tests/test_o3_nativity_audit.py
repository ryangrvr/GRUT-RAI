"""Tests for grut/o3_nativity_audit.py.

Deterministic test suite covering all five audit tracks (A–E), three blocking
gaps (BG1–BG3), two convergent motivations (CM1–CM2), four nativity criteria
(N1–N4), uniqueness check, parameter mapping, doctrine compatibility, patchwork
assessment, verdicts, top-level Booleans, forbidden inferences, nonclaims,
cross-consistency checks, and master audit idempotency.
"""

from __future__ import annotations

import math

import pytest

from grut.o3_nativity_audit import (
    # Constants
    M_EXT,
    R_EQ,
    TAU_SQ,
    ALPHA_VAC,
    BETA_Q_CANON,
    OMEGA_0_SQ,
    OMEGA_0,
    X_EQ,
    SPATIAL_DIMENSION,
    N_O3_FIELDS,
    N_CANONICAL_FIELDS,
    PI2_REAL_SCALAR,
    PI2_S2,
    COMP_B_COEFF,
    ETA_SQ_FROM_COMP_B,
    ETA_FROM_COMP_B,
    ETA_SQ_FROM_TAU_FORMULA,
    MU_DEFAULT,
    LAMBDA_DEFAULT,
    N_BLOCKING_GAPS,
    N_CONVERGENT_MOTIVATIONS,
    N_NATIVITY_CRITERIA,
    # Verdict sets
    ALLOWED_NATIVITY_VERDICTS,
    ALLOWED_ROUTE_STATUSES,
    ALLOWED_PATCHWORK_CLASSES,
    ALLOWED_GAP_CLOSEABILITY,
    # Builders
    build_track_a,
    build_track_b,
    build_track_c,
    build_track_d,
    build_track_e,
    build_blocking_gaps,
    build_convergent_motivations,
    build_nativity_criteria,
    build_uniqueness_check,
    build_parameter_mapping,
    build_doctrine_compatibility,
    build_patchwork_assessment,
    assign_verdicts,
    run_o3_nativity_audit,
)


# ---------------------------------------------------------------------------
# 1. TestConstants
# ---------------------------------------------------------------------------

class TestConstants:
    """Lock all module-level constants."""

    def test_m_ext(self):
        assert M_EXT == 0.5

    def test_r_eq(self):
        assert abs(R_EQ - 1.0 / 3.0) < 1e-15

    def test_tau_sq(self):
        assert TAU_SQ == 1.5

    def test_alpha_vac(self):
        assert abs(ALPHA_VAC - 1.0 / 3.0) < 1e-15

    def test_beta_q_canon(self):
        assert BETA_Q_CANON == 2.0

    def test_omega_0_sq(self):
        # β_Q * M / R_eq^3 = 2 * 0.5 / (1/3)^3 = 1 / (1/27) = 27
        assert abs(OMEGA_0_SQ - 27.0) < 1e-12

    def test_omega_0(self):
        assert abs(OMEGA_0 - math.sqrt(27.0)) < 1e-12

    def test_x_eq(self):
        # M / R_eq^2 = 0.5 / (1/9) = 4.5
        assert abs(X_EQ - 4.5) < 1e-12

    def test_spatial_dimension(self):
        assert SPATIAL_DIMENSION == 3

    def test_n_o3_fields(self):
        assert N_O3_FIELDS == 3

    def test_n_canonical_fields(self):
        assert N_CANONICAL_FIELDS == 1

    def test_pi2_real_scalar(self):
        assert PI2_REAL_SCALAR == 0

    def test_pi2_s2(self):
        assert PI2_S2 == "Z"

    def test_comp_b_coeff(self):
        expected = 1.0 / (8.0 * math.pi)
        assert abs(COMP_B_COEFF - expected) < 1e-15

    def test_eta_sq_from_comp_b_equals_comp_b_coeff(self):
        assert abs(ETA_SQ_FROM_COMP_B - COMP_B_COEFF) < 1e-15

    def test_eta_from_comp_b(self):
        assert abs(ETA_FROM_COMP_B - math.sqrt(COMP_B_COEFF)) < 1e-12

    def test_eta_sq_from_tau_formula(self):
        expected = TAU_SQ / (12.0 * math.pi)
        assert abs(ETA_SQ_FROM_TAU_FORMULA - expected) < 1e-15

    def test_tau_formula_equals_comp_b_coeff(self):
        """The critical numerical connection: η² = τ²/(12π) = 1/(8π)."""
        assert abs(ETA_SQ_FROM_TAU_FORMULA - COMP_B_COEFF) < 1e-12

    def test_mu_default(self):
        assert MU_DEFAULT == 1.0

    def test_lambda_default(self):
        # λ = μ² / η² = 1.0 / (1/(8π)) = 8π
        expected = 8.0 * math.pi
        assert abs(LAMBDA_DEFAULT - expected) < 1e-10

    def test_lambda_over_mu_sq_equals_one_over_eta_sq(self):
        assert abs(LAMBDA_DEFAULT / (MU_DEFAULT ** 2) - 1.0 / ETA_SQ_FROM_COMP_B) < 1e-10

    def test_n_blocking_gaps(self):
        assert N_BLOCKING_GAPS == 3

    def test_n_convergent_motivations(self):
        assert N_CONVERGENT_MOTIVATIONS == 2

    def test_n_nativity_criteria(self):
        assert N_NATIVITY_CRITERIA == 4

    def test_tau_sq_numerical_value(self):
        """3/2 exactly."""
        assert TAU_SQ == 3.0 / 2.0


# ---------------------------------------------------------------------------
# 2. TestAllowedVerdictSets
# ---------------------------------------------------------------------------

class TestAllowedVerdictSets:
    """Lock the closed verdict / vocabulary sets."""

    def test_nativity_verdicts_size(self):
        assert len(ALLOWED_NATIVITY_VERDICTS) == 4

    def test_primary_verdict_in_set(self):
        assert "o3_auxiliary_but_minimally_motivated" in ALLOWED_NATIVITY_VERDICTS

    def test_secondary_verdict_in_set(self):
        assert "o3_requires_independent_field_postulation" in ALLOWED_NATIVITY_VERDICTS

    def test_no_derivation_in_set(self):
        assert "no_native_o3_derivation_found" in ALLOWED_NATIVITY_VERDICTS

    def test_conditionally_derivable_in_set(self):
        assert "o3_conditionally_derivable_from_collective_modes" in ALLOWED_NATIVITY_VERDICTS

    def test_patchwork_classes_size(self):
        assert len(ALLOWED_PATCHWORK_CLASSES) == 4

    def test_motivated_independent_postulation_in_patchwork(self):
        assert "motivated_independent_postulation" in ALLOWED_PATCHWORK_CLASSES

    def test_derives_from_canonical_in_patchwork(self):
        assert "derives_from_canonical_scalar" in ALLOWED_PATCHWORK_CLASSES

    def test_arbitrary_extension_in_patchwork(self):
        assert "arbitrary_auxiliary_extension" in ALLOWED_PATCHWORK_CLASSES

    def test_incompatible_in_patchwork(self):
        assert "incompatible_with_canonical_architecture" in ALLOWED_PATCHWORK_CLASSES

    def test_route_statuses_includes_not_derivable(self):
        assert "not_derivable" in ALLOWED_ROUTE_STATUSES

    def test_route_statuses_includes_unique_minimal(self):
        assert "unique_minimal" in ALLOWED_ROUTE_STATUSES

    def test_route_statuses_includes_conditionally_partial(self):
        assert "conditionally_partial" in ALLOWED_ROUTE_STATUSES

    def test_route_statuses_includes_phenomenological(self):
        assert "phenomenological_motivation" in ALLOWED_ROUTE_STATUSES

    def test_gap_closeability_includes_not_closeable(self):
        assert "not_closeable_by_derivation" in ALLOWED_GAP_CLOSEABILITY

    def test_gap_closeability_includes_partially_closeable(self):
        assert "partially_closeable" in ALLOWED_GAP_CLOSEABILITY

    def test_gap_closeability_includes_closeable_under_conditions(self):
        assert "closeable_under_conditions" in ALLOWED_GAP_CLOSEABILITY

    def test_gap_closeability_includes_already_closed(self):
        assert "already_closed" in ALLOWED_GAP_CLOSEABILITY

    def test_all_sets_are_frozensets(self):
        for s in (ALLOWED_NATIVITY_VERDICTS, ALLOWED_ROUTE_STATUSES,
                  ALLOWED_PATCHWORK_CLASSES, ALLOWED_GAP_CLOSEABILITY):
            assert isinstance(s, frozenset)


# ---------------------------------------------------------------------------
# 3. TestTrackA
# ---------------------------------------------------------------------------

class TestTrackA:
    """Track A: canonical scalar → O(3) triplet."""

    def setup_method(self):
        self.track = build_track_a()

    def test_track_id(self):
        assert self.track.track_id == "A"

    def test_name(self):
        assert self.track.name == "canonical_scalar_promotion"

    def test_status(self):
        assert self.track.status == "not_derivable"

    def test_status_in_allowed(self):
        assert self.track.status in ALLOWED_ROUTE_STATUSES

    def test_contributes_to_nativity_false(self):
        assert self.track.contributes_to_nativity is False

    def test_blocking_gap_ref(self):
        assert self.track.blocking_gap_ref == "BG1"

    def test_motivation_ref_none(self):
        assert self.track.motivation_ref is None

    def test_notes_nonempty(self):
        assert len(self.track.notes) > 0

    def test_finding_mentions_discrete_change(self):
        assert "discrete" in self.track.finding.lower() or "discrete" in " ".join(self.track.notes).lower()

    def test_question_nonempty(self):
        assert len(self.track.question) > 0


# ---------------------------------------------------------------------------
# 4. TestTrackB
# ---------------------------------------------------------------------------

class TestTrackB:
    """Track B: target-space geometry ℝ → S²."""

    def setup_method(self):
        self.track = build_track_b()

    def test_track_id(self):
        assert self.track.track_id == "B"

    def test_name(self):
        assert self.track.name == "target_space_geometry"

    def test_status(self):
        assert self.track.status == "not_derivable"

    def test_status_in_allowed(self):
        assert self.track.status in ALLOWED_ROUTE_STATUSES

    def test_contributes_to_nativity_false(self):
        assert self.track.contributes_to_nativity is False

    def test_blocking_gap_ref(self):
        assert self.track.blocking_gap_ref == "BG2"

    def test_motivation_ref_none(self):
        assert self.track.motivation_ref is None

    def test_notes_mention_mexican_hat(self):
        all_text = self.track.finding + " ".join(self.track.notes)
        assert "mexican hat" in all_text.lower() or "mexican_hat" in all_text.lower()

    def test_notes_nonempty(self):
        assert len(self.track.notes) > 0


# ---------------------------------------------------------------------------
# 5. TestTrackC
# ---------------------------------------------------------------------------

class TestTrackC:
    """Track C: internal symmetry origin."""

    def setup_method(self):
        self.track = build_track_c()

    def test_track_id(self):
        assert self.track.track_id == "C"

    def test_name(self):
        assert self.track.name == "internal_symmetry_origin"

    def test_status(self):
        assert self.track.status == "conditionally_partial"

    def test_status_in_allowed(self):
        assert self.track.status in ALLOWED_ROUTE_STATUSES

    def test_contributes_to_nativity_false(self):
        # partial != nativity established
        assert self.track.contributes_to_nativity is False

    def test_blocking_gap_ref(self):
        assert self.track.blocking_gap_ref == "BG3"

    def test_motivation_ref_none(self):
        assert self.track.motivation_ref is None

    def test_finding_mentions_hedgehog(self):
        assert "hedgehog" in self.track.finding.lower()

    def test_finding_mentions_spatial_so3(self):
        all_text = self.track.finding + " ".join(self.track.notes)
        assert "so(3)" in all_text.lower() or "so3" in all_text.lower() or "SO(3)" in all_text


# ---------------------------------------------------------------------------
# 6. TestTrackD
# ---------------------------------------------------------------------------

class TestTrackD:
    """Track D: parameter mapping."""

    def setup_method(self):
        self.track = build_track_d()

    def test_track_id(self):
        assert self.track.track_id == "D"

    def test_name(self):
        assert self.track.name == "parameter_mapping"

    def test_status(self):
        assert self.track.status == "phenomenological_motivation"

    def test_status_in_allowed(self):
        assert self.track.status in ALLOWED_ROUTE_STATUSES

    def test_contributes_to_nativity_false(self):
        assert self.track.contributes_to_nativity is False

    def test_blocking_gap_ref_none(self):
        assert self.track.blocking_gap_ref is None

    def test_motivation_ref_cm2(self):
        assert self.track.motivation_ref == "CM2"

    def test_notes_mention_tau(self):
        all_text = self.track.finding + " ".join(self.track.notes)
        assert "tau" in all_text.lower() or "τ" in all_text

    def test_notes_mention_comp_b(self):
        all_text = " ".join(self.track.notes)
        assert "comp_b" in all_text.lower() or "component b" in all_text.lower()


# ---------------------------------------------------------------------------
# 7. TestTrackE
# ---------------------------------------------------------------------------

class TestTrackE:
    """Track E: uniqueness of O(3) as minimal extension."""

    def setup_method(self):
        self.track = build_track_e()

    def test_track_id(self):
        assert self.track.track_id == "E"

    def test_name(self):
        assert self.track.name == "uniqueness_of_o3"

    def test_status(self):
        assert self.track.status == "unique_minimal"

    def test_status_in_allowed(self):
        assert self.track.status in ALLOWED_ROUTE_STATUSES

    def test_contributes_to_nativity_false(self):
        # uniqueness ≠ derivation from canonical architecture
        assert self.track.contributes_to_nativity is False

    def test_blocking_gap_ref_none(self):
        assert self.track.blocking_gap_ref is None

    def test_motivation_ref_cm1(self):
        assert self.track.motivation_ref == "CM1"

    def test_finding_mentions_pi2(self):
        all_text = self.track.finding + " ".join(self.track.notes)
        assert "π₂" in all_text or "pi_2" in all_text.lower() or "pi2" in all_text.lower()

    def test_finding_mentions_cp1_equivalent(self):
        all_text = self.track.finding + " ".join(self.track.notes)
        assert "cp(1)" in all_text.lower() or "cp1" in all_text.lower()


# ---------------------------------------------------------------------------
# 8. TestBlockingGaps
# ---------------------------------------------------------------------------

class TestBlockingGaps:
    """BG1, BG2, BG3 — blocking gaps."""

    def setup_method(self):
        self.gaps = build_blocking_gaps()
        self.bg1 = self.gaps[0]
        self.bg2 = self.gaps[1]
        self.bg3 = self.gaps[2]

    def test_count(self):
        assert len(self.gaps) == 3

    # BG1
    def test_bg1_id(self):
        assert self.bg1.gap_id == "BG1"

    def test_bg1_name(self):
        assert self.bg1.name == "discrete_dof_change"

    def test_bg1_closeability(self):
        assert self.bg1.closeability == "not_closeable_by_derivation"

    def test_bg1_in_allowed_closeability(self):
        assert self.bg1.closeability in ALLOWED_GAP_CLOSEABILITY

    def test_bg1_is_mathematical_impossibility(self):
        assert self.bg1.is_mathematical_impossibility is True

    def test_bg1_closes_nativity_question(self):
        # BG1 closes nativity if resolved — but it's irresolvable, so this is False
        assert self.bg1.closes_nativity_question is False

    def test_bg1_notes_nonempty(self):
        assert len(self.bg1.notes) > 0

    # BG2
    def test_bg2_id(self):
        assert self.bg2.gap_id == "BG2"

    def test_bg2_name(self):
        assert self.bg2.name == "target_space_constraint"

    def test_bg2_closeability(self):
        assert self.bg2.closeability == "closeable_under_conditions"

    def test_bg2_in_allowed_closeability(self):
        assert self.bg2.closeability in ALLOWED_GAP_CLOSEABILITY

    def test_bg2_not_mathematical_impossibility(self):
        assert self.bg2.is_mathematical_impossibility is False

    def test_bg2_closes_nativity_question_false(self):
        assert self.bg2.closes_nativity_question is False

    # BG3
    def test_bg3_id(self):
        assert self.bg3.gap_id == "BG3"

    def test_bg3_name(self):
        assert self.bg3.name == "internal_symmetry_origin"

    def test_bg3_closeability(self):
        assert self.bg3.closeability == "partially_closeable"

    def test_bg3_in_allowed_closeability(self):
        assert self.bg3.closeability in ALLOWED_GAP_CLOSEABILITY

    def test_bg3_not_mathematical_impossibility(self):
        assert self.bg3.is_mathematical_impossibility is False

    def test_bg3_closes_nativity_question_false(self):
        assert self.bg3.closes_nativity_question is False

    # Gap ordering: BG1 is most fundamental
    def test_bg1_is_hardest_gap(self):
        """Only BG1 is mathematically irresolvable."""
        impossibilities = [g.is_mathematical_impossibility for g in self.gaps]
        assert impossibilities == [True, False, False]

    # All closeability values in allowed set
    def test_all_closeability_values_in_allowed(self):
        for gap in self.gaps:
            assert gap.closeability in ALLOWED_GAP_CLOSEABILITY


# ---------------------------------------------------------------------------
# 9. TestConvergentMotivations
# ---------------------------------------------------------------------------

class TestConvergentMotivations:
    """CM1 (topological), CM2 (Component B)."""

    def setup_method(self):
        self.motivations = build_convergent_motivations()
        self.cm1 = self.motivations[0]
        self.cm2 = self.motivations[1]

    def test_count(self):
        assert len(self.motivations) == 2

    # CM1
    def test_cm1_id(self):
        assert self.cm1.motivation_id == "CM1"

    def test_cm1_name(self):
        assert self.cm1.name == "topological_gap_fill"

    def test_cm1_is_topological(self):
        assert self.cm1.is_topological is True

    def test_cm1_not_phenomenological(self):
        assert self.cm1.is_phenomenological is False

    def test_cm1_motivates_uniquely(self):
        assert self.cm1.motivates_o3_uniquely is True

    def test_cm1_not_parameter_constrained(self):
        assert self.cm1.parameter_constrained is False

    def test_cm1_parameter_constraint_none(self):
        assert self.cm1.parameter_constraint is None

    def test_cm1_notes_nonempty(self):
        assert len(self.cm1.notes) > 0

    # CM2
    def test_cm2_id(self):
        assert self.cm2.motivation_id == "CM2"

    def test_cm2_name(self):
        assert self.cm2.name == "component_b_tail_matching"

    def test_cm2_not_topological(self):
        assert self.cm2.is_topological is False

    def test_cm2_is_phenomenological(self):
        assert self.cm2.is_phenomenological is True

    def test_cm2_does_not_motivate_uniquely(self):
        # Component B tail alone does not uniquely select O(3)
        assert self.cm2.motivates_o3_uniquely is False

    def test_cm2_parameter_constrained(self):
        assert self.cm2.parameter_constrained is True

    def test_cm2_parameter_constraint_nonempty(self):
        assert self.cm2.parameter_constraint is not None
        assert "eta" in self.cm2.parameter_constraint.lower()

    def test_cm2_constraint_contains_1_over_8pi(self):
        assert "8" in self.cm2.parameter_constraint and "pi" in self.cm2.parameter_constraint.lower()


# ---------------------------------------------------------------------------
# 10. TestNativityCriteria
# ---------------------------------------------------------------------------

class TestNativityCriteria:
    """N1–N4 nativity criteria."""

    def setup_method(self):
        tracks = [build_track_a(), build_track_b(), build_track_c(),
                  build_track_d(), build_track_e()]
        blocking_gaps = build_blocking_gaps()
        self.criteria = build_nativity_criteria(tracks, blocking_gaps)
        self.n1 = self.criteria[0]
        self.n2 = self.criteria[1]
        self.n3 = self.criteria[2]
        self.n4 = self.criteria[3]

    def test_count(self):
        assert len(self.criteria) == 4

    # N1
    def test_n1_id(self):
        assert self.n1.criterion_id == 1

    def test_n1_name(self):
        assert "field_content" in self.n1.name.lower()

    def test_n1_passes_false(self):
        assert self.n1.passes is False

    def test_n1_pass_level_hard_fail(self):
        assert self.n1.pass_level == "hard_fail"

    def test_n1_blocking_gap_bg1(self):
        assert self.n1.blocking_gap_ref == "BG1"

    def test_n1_no_conditional_path(self):
        assert self.n1.conditional_path is None

    # N2
    def test_n2_id(self):
        assert self.n2.criterion_id == 2

    def test_n2_name(self):
        assert "target_space" in self.n2.name.lower()

    def test_n2_passes_false(self):
        assert self.n2.passes is False

    def test_n2_pass_level_soft_fail(self):
        assert self.n2.pass_level == "soft_fail"

    def test_n2_blocking_gap_bg2(self):
        assert self.n2.blocking_gap_ref == "BG2"

    def test_n2_has_conditional_path(self):
        assert self.n2.conditional_path is not None
        assert len(self.n2.conditional_path) > 0

    # N3
    def test_n3_id(self):
        assert self.n3.criterion_id == 3

    def test_n3_name(self):
        assert "internal_symmetry" in self.n3.name.lower() or "symmetry" in self.n3.name.lower()

    def test_n3_passes_false(self):
        assert self.n3.passes is False

    def test_n3_pass_level_partial(self):
        assert self.n3.pass_level == "partial"

    def test_n3_blocking_gap_bg3(self):
        assert self.n3.blocking_gap_ref == "BG3"

    def test_n3_has_conditional_path(self):
        assert self.n3.conditional_path is not None

    # N4
    def test_n4_id(self):
        assert self.n4.criterion_id == 4

    def test_n4_name(self):
        assert "parameter" in self.n4.name.lower()

    def test_n4_passes_false(self):
        assert self.n4.passes is False

    def test_n4_pass_level_partial(self):
        assert self.n4.pass_level == "partial"

    def test_n4_no_blocking_gap(self):
        assert self.n4.blocking_gap_ref is None

    def test_n4_has_conditional_path(self):
        assert self.n4.conditional_path is not None

    # Summary across all criteria
    def test_none_pass(self):
        assert all(not c.passes for c in self.criteria)

    def test_all_pass_false(self):
        assert not any(c.passes for c in self.criteria)

    def test_pass_levels(self):
        expected = ["hard_fail", "soft_fail", "partial", "partial"]
        actual = [c.pass_level for c in self.criteria]
        assert actual == expected

    def test_n1_hardest_fail(self):
        """N1 is a hard_fail; N2 is a soft_fail (weaker)."""
        assert self.n1.pass_level == "hard_fail"
        assert self.n2.pass_level == "soft_fail"


# ---------------------------------------------------------------------------
# 11. TestUniquenessCheck
# ---------------------------------------------------------------------------

class TestUniquenessCheck:
    """O(3) uniqueness as minimal real-scalar π₂ ≠ 0 extension."""

    def setup_method(self):
        self.check = build_uniqueness_check()

    def test_o3_is_minimal_for_pi2_nonzero(self):
        assert self.check.o3_is_minimal_for_pi2_nonzero is True

    def test_no_alternative_with_fewer_real_fields(self):
        assert self.check.alternative_with_fewer_real_fields is False

    def test_cp1_equivalent(self):
        assert self.check.cp1_equivalent is True

    def test_cp1_uses_same_dof_count(self):
        assert self.check.cp1_uses_same_dof_count is True

    def test_uniqueness_verdict_nonempty(self):
        assert len(self.check.uniqueness_verdict) > 0

    def test_uniqueness_verdict_contains_unique(self):
        assert "unique" in self.check.uniqueness_verdict.lower()

    def test_uniqueness_verdict_contains_cp1(self):
        all_text = self.check.uniqueness_verdict + " ".join(self.check.notes)
        assert "cp1" in all_text.lower() or "cp(1)" in all_text.lower()

    def test_notes_cover_1_to_3_scalars(self):
        notes_text = " ".join(self.check.notes)
        assert "1 real scalar" in notes_text or "single real scalar" in notes_text.lower() or "1 real" in notes_text

    def test_notes_cover_s2(self):
        notes_text = " ".join(self.check.notes)
        assert "S²" in notes_text or "s2" in notes_text.lower()


# ---------------------------------------------------------------------------
# 12. TestParameterMapping
# ---------------------------------------------------------------------------

class TestParameterMapping:
    """O(3) parameter connections to canonical GRUT."""

    def setup_method(self):
        self.pm = build_parameter_mapping()

    def test_eta_sq_from_comp_b_value(self):
        expected = 1.0 / (8.0 * math.pi)
        assert abs(self.pm.eta_sq_from_comp_b - expected) < 1e-15

    def test_eta_sq_from_tau_formula_value(self):
        expected = TAU_SQ / (12.0 * math.pi)
        assert abs(self.pm.eta_sq_from_tau_formula - expected) < 1e-15

    def test_both_eta_sq_equal(self):
        assert abs(self.pm.eta_sq_from_comp_b - self.pm.eta_sq_from_tau_formula) < 1e-12

    def test_tau_connection_holds_numerically(self):
        assert self.pm.tau_connection_holds_numerically is True

    def test_tau_connection_mechanism_unknown(self):
        assert self.pm.tau_connection_mechanism_known is False

    def test_mu_not_fixed_by_grut(self):
        assert self.pm.mu_fixed_by_grut is False

    def test_lambda_not_fixed_by_grut(self):
        assert self.pm.lambda_fixed_by_grut is False

    def test_ratio_lambda_over_mu_sq_constrained(self):
        assert self.pm.ratio_lambda_over_mu_sq_constrained is True

    def test_grut_constants_not_used_includes_alpha_vac(self):
        assert "alpha_vac" in self.pm.grut_constants_not_used

    def test_grut_constants_not_used_includes_beta_q(self):
        assert "beta_Q" in self.pm.grut_constants_not_used

    def test_grut_constants_not_used_includes_omega_0(self):
        assert "omega_0" in self.pm.grut_constants_not_used

    def test_grut_constants_not_used_includes_r_eq(self):
        assert "R_eq" in self.pm.grut_constants_not_used

    def test_summary_nonempty(self):
        assert len(self.pm.summary) > 0

    def test_notes_nonempty(self):
        assert len(self.pm.notes) > 0


# ---------------------------------------------------------------------------
# 13. TestDoctrineCompatibility
# ---------------------------------------------------------------------------

class TestDoctrineCompatibility:
    """All prior audit verdicts remain consistent."""

    def setup_method(self):
        self.dc = build_doctrine_compatibility()

    def test_consistent_with_phi_bifurcation(self):
        assert self.dc.consistent_with_phi_bifurcation is True

    def test_consistent_with_tau_eff_domain(self):
        assert self.dc.consistent_with_tau_eff_domain is True

    def test_consistent_with_beta_q_hypothesis(self):
        assert self.dc.consistent_with_beta_q_hypothesis is True

    def test_consistent_with_fermionic_audit(self):
        assert self.dc.consistent_with_fermionic_audit is True

    def test_consistent_with_appendix_m(self):
        assert self.dc.consistent_with_appendix_m is True

    def test_consistent_with_skyrme_audit(self):
        assert self.dc.consistent_with_skyrme_audit is True

    def test_introduces_new_field_content(self):
        assert self.dc.introduces_new_field_content is True

    def test_introduces_new_free_parameters(self):
        assert self.dc.introduces_new_free_parameters is True

    def test_compatible_with_prior_doctrine(self):
        assert self.dc.compatible_with_prior_doctrine is True

    def test_doctrine_impact_nonempty(self):
        assert len(self.dc.doctrine_impact) > 0

    def test_notes_nonempty(self):
        assert len(self.dc.notes) > 0


# ---------------------------------------------------------------------------
# 14. TestPatchworkAssessment
# ---------------------------------------------------------------------------

class TestPatchworkAssessment:
    """O(3) patchwork vs native status."""

    def setup_method(self):
        blocking_gaps = build_blocking_gaps()
        tracks = [build_track_a(), build_track_b(), build_track_c(),
                  build_track_d(), build_track_e()]
        criteria = build_nativity_criteria(tracks, blocking_gaps)
        motivations = build_convergent_motivations()
        uniqueness = build_uniqueness_check()
        self.pw = build_patchwork_assessment(blocking_gaps, criteria, motivations, uniqueness)

    def test_derives_from_canonical_scalar_false(self):
        assert self.pw.derives_from_canonical_scalar is False

    def test_motivated_independent_postulation_true(self):
        assert self.pw.motivated_independent_postulation is True

    def test_arbitrary_auxiliary_extension_false(self):
        assert self.pw.arbitrary_auxiliary_extension is False

    def test_incompatible_with_canonical_architecture_false(self):
        assert self.pw.incompatible_with_canonical_architecture is False

    def test_patchwork_verdict(self):
        assert self.pw.patchwork_verdict == "motivated_independent_postulation"

    def test_patchwork_verdict_in_allowed(self):
        assert self.pw.patchwork_verdict in ALLOWED_PATCHWORK_CLASSES

    def test_comparison_to_skyrme_term_nonempty(self):
        assert len(self.pw.comparison_to_skyrme_term) > 0

    def test_comparison_mentions_skyrme(self):
        assert "skyrme" in self.pw.comparison_to_skyrme_term.lower()

    def test_comparison_mentions_motivated_but_unbuilt(self):
        assert "motivated_but_unbuilt" in self.pw.comparison_to_skyrme_term

    def test_what_best_outcome_looks_like_nonempty(self):
        assert len(self.pw.what_best_outcome_looks_like) > 0

    def test_notes_nonempty(self):
        assert len(self.pw.notes) > 0


# ---------------------------------------------------------------------------
# 15. TestVerdicts
# ---------------------------------------------------------------------------

class TestVerdicts:
    """Verdict assignment from closed label set."""

    def setup_method(self):
        tracks = [build_track_a(), build_track_b(), build_track_c(),
                  build_track_d(), build_track_e()]
        self.blocking_gaps = build_blocking_gaps()
        self.criteria = build_nativity_criteria(tracks, self.blocking_gaps)
        self.uniqueness = build_uniqueness_check()
        self.primary, self.secondary = assign_verdicts(
            self.criteria, self.uniqueness, self.blocking_gaps
        )

    def test_primary_verdict(self):
        assert self.primary == "o3_auxiliary_but_minimally_motivated"

    def test_secondary_verdict(self):
        assert self.secondary == "o3_requires_independent_field_postulation"

    def test_primary_in_allowed(self):
        assert self.primary in ALLOWED_NATIVITY_VERDICTS

    def test_secondary_in_allowed(self):
        assert self.secondary in ALLOWED_NATIVITY_VERDICTS

    def test_primary_and_secondary_different(self):
        assert self.primary != self.secondary

    def test_primary_is_not_no_derivation(self):
        """When uniquely motivated, we get auxiliary_but_minimally_motivated not no_derivation."""
        assert self.primary != "no_native_o3_derivation_found"

    def test_primary_is_not_conditionally_derivable(self):
        """Criteria don't all pass — not conditionally derivable."""
        assert self.primary != "o3_conditionally_derivable_from_collective_modes"


# ---------------------------------------------------------------------------
# 16. TestTopLevelBooleans
# ---------------------------------------------------------------------------

class TestTopLevelBooleans:
    """Master result top-level Boolean summary."""

    def setup_method(self):
        self.result = run_o3_nativity_audit()

    def test_canonical_scalar_implies_o3_false(self):
        assert self.result.canonical_scalar_implies_o3 is False

    def test_target_space_generated_by_grut_false(self):
        assert self.result.target_space_generated_by_grut is False

    def test_internal_symmetry_from_grut_false(self):
        assert self.result.internal_symmetry_from_grut is False

    def test_o3_is_unique_minimal_extension_true(self):
        assert self.result.o3_is_unique_minimal_extension is True

    def test_component_b_motivates_o3_true(self):
        assert self.result.component_b_motivates_o3 is True

    def test_parameter_connection_found_true(self):
        assert self.result.parameter_connection_found is True

    def test_parameter_connection_mechanism_known_false(self):
        assert self.result.parameter_connection_mechanism_known is False

    def test_all_nativity_criteria_pass_false(self):
        assert self.result.all_nativity_criteria_pass is False

    def test_n_canonical_fields(self):
        assert self.result.n_canonical_fields == 1

    def test_n_o3_fields(self):
        assert self.result.n_o3_fields == 3

    def test_field_content_change_is_discrete(self):
        assert self.result.field_content_change_is_discrete is True

    def test_doctrine_compatible_true(self):
        assert self.result.doctrine_compatible is True

    def test_primary_verdict(self):
        assert self.result.primary_verdict == "o3_auxiliary_but_minimally_motivated"

    def test_secondary_verdict(self):
        assert self.result.secondary_verdict == "o3_requires_independent_field_postulation"


# ---------------------------------------------------------------------------
# 17. TestForbiddenInferences
# ---------------------------------------------------------------------------

class TestForbiddenInferences:
    """Explicit forbidden inference labels are present and enforced."""

    def setup_method(self):
        self.result = run_o3_nativity_audit()
        self.fi = self.result.forbidden_inferences

    def test_forbidden_inferences_nonempty(self):
        assert len(self.fi) > 0

    def test_o3_derived_inference_forbidden(self):
        assert "o3_is_derived_from_canonical_grut_scalar" in self.fi

    def test_topological_implies_architectural_forbidden(self):
        assert "topological_uniqueness_implies_architectural_derivation" in self.fi

    def test_component_b_implies_nativity_forbidden(self):
        assert "component_b_matching_implies_o3_nativity" in self.fi

    def test_hedgehog_derives_symmetry_forbidden(self):
        assert "hedgehog_ansatz_derives_internal_o3_symmetry" in self.fi

    def test_eta_tau_implies_full_parameter_derivation_forbidden(self):
        assert "eta_tau_connection_implies_full_parameter_derivation" in self.fi

    def test_motivated_postulate_means_native_forbidden(self):
        assert "motivated_postulate_means_same_as_native_sector" in self.fi

    def test_bg1_closeable_by_gradient_expansion_forbidden(self):
        assert "bg1_is_closeable_by_gradient_expansion_or_ctp" in self.fi

    def test_o3_not_arbitrary_because_motivated_forbidden(self):
        assert "o3_postulation_is_arbitrary_because_not_derived" in self.fi

    def test_no_overlap_with_allowed_nativity_verdicts(self):
        for fi in self.fi:
            assert fi not in ALLOWED_NATIVITY_VERDICTS


# ---------------------------------------------------------------------------
# 18. TestNonclaims
# ---------------------------------------------------------------------------

class TestNonclaims:
    """Six explicit nonclaims are present."""

    def setup_method(self):
        self.result = run_o3_nativity_audit()
        self.nc = self.result.nonclaims

    def test_nonclaims_nonempty(self):
        assert len(self.nc) > 0

    def test_at_least_six_nonclaims(self):
        assert len(self.nc) >= 6

    def test_not_claiming_o3_arbitrary(self):
        text = " ".join(self.nc).lower()
        assert "arbitrary" in text

    def test_not_claiming_deeper_derivation_impossible(self):
        text = " ".join(self.nc).lower()
        assert "deeper" in text or "canonical scalar" in text

    def test_not_claiming_eta_tau_connection_meaningless(self):
        text = " ".join(self.nc)
        assert "τ" in text or "tau" in text.lower() or "12" in text

    def test_not_claiming_doctrine_violated(self):
        text = " ".join(self.nc).lower()
        assert "doctrine" in text or "prior" in text or "violates" in text

    def test_not_claiming_bg3_uncloseable(self):
        text = " ".join(self.nc).lower()
        assert "bg3" in text or "internal symmetry" in text or "hedgehog" in text

    def test_all_nonclaims_are_strings(self):
        for nc in self.nc:
            assert isinstance(nc, str)
            assert len(nc) > 0


# ---------------------------------------------------------------------------
# 19. TestCrossConsistency
# ---------------------------------------------------------------------------

class TestCrossConsistency:
    """Cross-checks between structural components."""

    def setup_method(self):
        self.result = run_o3_nativity_audit()

    def test_track_count(self):
        assert len(self.result.tracks) == 5

    def test_blocking_gap_count(self):
        assert len(self.result.blocking_gaps) == N_BLOCKING_GAPS

    def test_convergent_motivation_count(self):
        assert len(self.result.convergent_motivations) == N_CONVERGENT_MOTIVATIONS

    def test_nativity_criteria_count(self):
        assert len(self.result.nativity_criteria) == N_NATIVITY_CRITERIA

    def test_track_ids_unique(self):
        ids = [t.track_id for t in self.result.tracks]
        assert len(ids) == len(set(ids))

    def test_track_ids_are_abcde(self):
        ids = sorted(t.track_id for t in self.result.tracks)
        assert ids == ["A", "B", "C", "D", "E"]

    def test_blocking_gap_ids_bg1_bg2_bg3(self):
        ids = [g.gap_id for g in self.result.blocking_gaps]
        assert ids == ["BG1", "BG2", "BG3"]

    def test_motivation_ids_cm1_cm2(self):
        ids = [m.motivation_id for m in self.result.convergent_motivations]
        assert ids == ["CM1", "CM2"]

    def test_n1_blocking_gap_matches_bg1(self):
        n1 = self.result.nativity_criteria[0]
        assert n1.blocking_gap_ref == "BG1"
        bg1 = self.result.blocking_gaps[0]
        assert bg1.gap_id == "BG1"
        assert bg1.is_mathematical_impossibility is True

    def test_all_blocking_gaps_closeability_in_allowed(self):
        for gap in self.result.blocking_gaps:
            assert gap.closeability in ALLOWED_GAP_CLOSEABILITY

    def test_all_track_statuses_in_allowed(self):
        for track in self.result.tracks:
            assert track.status in ALLOWED_ROUTE_STATUSES

    def test_patchwork_verdict_matches_top_level(self):
        assert self.result.patchwork.patchwork_verdict == "motivated_independent_postulation"

    def test_primary_verdict_in_diagnostics(self):
        assert self.result.diagnostics["primary_verdict"] == self.result.primary_verdict

    def test_secondary_verdict_in_diagnostics(self):
        assert self.result.diagnostics["secondary_verdict"] == self.result.secondary_verdict

    def test_canonical_fields_in_diagnostics(self):
        assert self.result.diagnostics["N_CANONICAL_FIELDS"] == 1

    def test_o3_fields_in_diagnostics(self):
        assert self.result.diagnostics["N_O3_FIELDS"] == 3

    def test_comp_b_coeff_in_diagnostics(self):
        expected = 1.0 / (8.0 * math.pi)
        assert abs(self.result.diagnostics["COMP_B_COEFF"] - expected) < 1e-15

    def test_eta_tau_connection_in_diagnostics(self):
        assert self.result.diagnostics["eta_tau_connection_holds"] is True
        assert self.result.diagnostics["eta_tau_mechanism_known"] is False

    def test_bg1_irresolvable_in_diagnostics(self):
        assert self.result.diagnostics["bg1_irresolvable_by_derivation"] is True

    def test_bg2_partially_closeable_in_diagnostics(self):
        assert self.result.diagnostics["bg2_partially_closeable"] is True

    def test_bg3_partially_closeable_in_diagnostics(self):
        assert self.result.diagnostics["bg3_partially_closeable"] is True

    def test_patchwork_verdict_in_diagnostics(self):
        assert self.result.diagnostics["patchwork_verdict"] == "motivated_independent_postulation"

    def test_all_nativity_criteria_pass_in_diagnostics(self):
        assert self.result.diagnostics["all_nativity_criteria_pass"] is False

    def test_n_blocking_gaps_in_diagnostics(self):
        assert self.result.diagnostics["n_blocking_gaps"] == 3

    def test_n_convergent_motivations_in_diagnostics(self):
        assert self.result.diagnostics["n_convergent_motivations"] == 2

    def test_parameter_connection_found_in_diagnostics(self):
        assert self.result.diagnostics["parameter_connection_found"] is True

    def test_eta_sq_values_consistent_in_diagnostics(self):
        diag = self.result.diagnostics
        assert abs(diag["ETA_SQ_FROM_COMP_B"] - diag["ETA_SQ_FROM_TAU_FORMULA"]) < 1e-12

    def test_lambda_default_in_diagnostics(self):
        expected = 8.0 * math.pi
        assert abs(self.result.diagnostics["LAMBDA_DEFAULT"] - expected) < 1e-10

    def test_doctrine_compatible_in_diagnostics(self):
        assert self.result.diagnostics["doctrine_compatible"] is True

    def test_o3_unique_minimal_in_diagnostics(self):
        assert self.result.diagnostics["o3_is_unique_minimal_extension"] is True

    def test_canonical_scalar_implies_o3_false_in_diagnostics(self):
        assert self.result.diagnostics["canonical_scalar_implies_o3"] is False


# ---------------------------------------------------------------------------
# 20. TestMasterAudit
# ---------------------------------------------------------------------------

class TestMasterAudit:
    """Master audit is deterministic and idempotent."""

    def test_runs_without_exception(self):
        result = run_o3_nativity_audit()
        assert result is not None

    def test_idempotent(self):
        r1 = run_o3_nativity_audit()
        r2 = run_o3_nativity_audit()
        assert r1.primary_verdict == r2.primary_verdict
        assert r1.secondary_verdict == r2.secondary_verdict
        assert r1.canonical_scalar_implies_o3 == r2.canonical_scalar_implies_o3
        assert r1.all_nativity_criteria_pass == r2.all_nativity_criteria_pass
        assert r1.patchwork.patchwork_verdict == r2.patchwork.patchwork_verdict

    def test_result_type(self):
        from grut.o3_nativity_audit import O3NativityResult
        result = run_o3_nativity_audit()
        assert isinstance(result, O3NativityResult)

    def test_diagnostics_is_dict(self):
        result = run_o3_nativity_audit()
        assert isinstance(result.diagnostics, dict)

    def test_nonclaims_is_list(self):
        result = run_o3_nativity_audit()
        assert isinstance(result.nonclaims, list)

    def test_forbidden_inferences_is_list(self):
        result = run_o3_nativity_audit()
        assert isinstance(result.forbidden_inferences, list)

    def test_primary_verdict_in_allowed(self):
        result = run_o3_nativity_audit()
        assert result.primary_verdict in ALLOWED_NATIVITY_VERDICTS

    def test_secondary_verdict_in_allowed(self):
        result = run_o3_nativity_audit()
        assert result.secondary_verdict in ALLOWED_NATIVITY_VERDICTS

    def test_patchwork_verdict_in_allowed(self):
        result = run_o3_nativity_audit()
        assert result.patchwork.patchwork_verdict in ALLOWED_PATCHWORK_CLASSES

    def test_eta_sq_tau_identity_holds_in_result(self):
        """Core numerical identity: η² = τ²/(12π) = 1/(8π)."""
        result = run_o3_nativity_audit()
        pm = result.parameter_mapping
        expected = 1.0 / (8.0 * math.pi)
        assert abs(pm.eta_sq_from_comp_b - expected) < 1e-14
        assert abs(pm.eta_sq_from_tau_formula - expected) < 1e-14
        assert abs(pm.eta_sq_from_comp_b - pm.eta_sq_from_tau_formula) < 1e-14

    def test_bg1_irresolvable_propagates_to_n1(self):
        """BG1's mathematical impossibility propagates to N1 hard_fail."""
        result = run_o3_nativity_audit()
        n1 = result.nativity_criteria[0]
        bg1 = result.blocking_gaps[0]
        assert bg1.is_mathematical_impossibility is True
        assert n1.passes is False
        assert n1.pass_level == "hard_fail"

    def test_uniqueness_propagates_to_primary_verdict(self):
        """O(3) uniqueness (not arbitrary) gives auxiliary_but_minimally_motivated."""
        result = run_o3_nativity_audit()
        assert result.uniqueness_check.o3_is_minimal_for_pi2_nonzero is True
        assert result.primary_verdict == "o3_auxiliary_but_minimally_motivated"

    def test_patchwork_not_arbitrary_and_not_derives(self):
        """Both extremes (derives / arbitrary) are False; middle verdict holds."""
        result = run_o3_nativity_audit()
        assert result.patchwork.derives_from_canonical_scalar is False
        assert result.patchwork.arbitrary_auxiliary_extension is False
        assert result.patchwork.motivated_independent_postulation is True
