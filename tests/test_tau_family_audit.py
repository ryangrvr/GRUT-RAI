"""Tests for Appendix F: τ-family unification / covariant scaling audit.

Tests verify that:
  1. All seven τ-family objects are correctly defined
  2. Level-1/Level-2 factorization is correct
  3. Resolution A/B/C verdicts are defensible
  4. Key identity classifications are correct
  5. Translation rule is partially viable (not fully)
  6. No forbidden claims appear
  7. Appendix E classification is unchanged

WHAT THESE TESTS DO NOT VERIFY:
  - Do NOT verify global consistency of GRUT
  - Do NOT verify that τ is unified (it is not)
  - Do NOT verify that Level-1 is covariant (it is not)
  - Do NOT upgrade any prior classification
"""

import math
import pytest

from grut.tau_family_audit import (
    TAU_0_S,
    ALPHA_VAC,
    BETA_Q,
    EPSILON_Q,
    R_EQ_OVER_RS,
    Q_CANONICAL,
    G_SI,
    C_SI,
    M_REF_KG,
    M_SUN_KG,
    _FORBIDDEN_CLASSIFICATIONS,
    build_tau_family_map,
    compute_level_factorization,
    build_resolution_audit,
    build_identity_audit,
    build_translation_rule,
    run_tau_family_audit,
    TauFamilyMap,
    AppendixFResult,
)


# ================================================================
# τ-Family Map Tests
# ================================================================

class TestTauFamilyMap:

    def test_eight_tau_objects_defined(self):
        """The τ-family map must contain exactly 8 objects (7 τ-like + t_dyn)."""
        fam = build_tau_family_map()
        assert len(fam.objects) == 8, (
            f"Expected 8 τ-family objects (7 τ-like + t_dyn), got {len(fam.objects)}"
        )

    def test_tau_0_is_level_0(self):
        """τ₀ must be Level-0 (global anchor)."""
        fam = build_tau_family_map()
        tau_0 = fam.by_symbol("tau_0")
        assert tau_0.level == 0
        assert tau_0.relation_to_tau0 == "identical"
        assert tau_0.sector == "ALL"

    def test_tau_eff_cosmo_is_level_2(self):
        """τ_eff_cosmo must be Level-2 (Lorentzian filter only, no Level-1)."""
        fam = build_tau_family_map()
        obj = fam.by_symbol("tau_eff_cosmo")
        assert obj.level == 2
        assert "H" in obj.formula_str or "Hubble" in obj.physical_meaning.lower()

    def test_tau_eff_collapse_bare_maybe_translatable(self):
        """τ_eff_collapse_bare must be flagged as maybe_translatable (same formula as cosmo)."""
        fam = build_tau_family_map()
        obj = fam.by_symbol("tau_eff_collapse_bare")
        assert obj.status == "maybe_translatable"

    def test_tau_0_local_is_level_1(self):
        """τ₀_local must be Level-1 (local reduction)."""
        fam = build_tau_family_map()
        obj = fam.by_symbol("tau_0_local")
        assert obj.level == 1
        assert "t_dyn" in obj.formula_str

    def test_tau_eff_collapse_tier0_is_both_levels(self):
        """τ_eff_collapse_tier0 must be Level-12 (both Level-1 and Level-2)."""
        fam = build_tau_family_map()
        obj = fam.by_symbol("tau_eff_collapse_tier0")
        assert obj.level == 12

    def test_tau_local_is_symbolically_conflated(self):
        """τ_local must be flagged as symbolically_conflated."""
        fam = build_tau_family_map()
        obj = fam.by_symbol("tau_local")
        assert obj.status == "symbolically_conflated"

    def test_tau_bath_is_symbolically_conflated(self):
        """τ_bath must be flagged as symbolically_conflated."""
        fam = build_tau_family_map()
        obj = fam.by_symbol("tau_bath")
        assert obj.status == "symbolically_conflated"
        assert obj.relation_to_tau0 == "identical"

    def test_t_dyn_is_independent(self):
        """t_dyn must be independent of τ₀."""
        fam = build_tau_family_map()
        obj = fam.by_symbol("t_dyn")
        assert obj.relation_to_tau0 == "independent"

    def test_exactly_two_conflated_objects(self):
        """Exactly 2 objects must be symbolically_conflated."""
        fam = build_tau_family_map()
        conflated = fam.conflated_objects()
        assert len(conflated) == 2, (
            f"Expected 2 conflated objects, got {len(conflated)}: "
            f"{[o.symbol for o in conflated]}"
        )

    def test_tau_local_and_tau_0_local_same_formula(self):
        """τ_local and τ₀_local must have the same formula (just different evaluation point)."""
        fam = build_tau_family_map()
        tau_local = fam.by_symbol("tau_local")
        tau_0_local = fam.by_symbol("tau_0_local")
        # Both should use the same formula: tau_0 * t_dyn / (t_dyn + tau_0)
        assert "t_dyn" in tau_local.formula_str
        assert "t_dyn" in tau_0_local.formula_str
        assert tau_local.level == tau_0_local.level == 1


# ================================================================
# Level Factorization Tests
# ================================================================

class TestLevelFactorization:

    def test_tau_0_local_much_less_than_tau_0(self):
        """For astrophysical masses, τ₀_local ≪ τ₀."""
        lr = compute_level_factorization()
        assert lr.tau_0_local < TAU_0_S * 1e-10, (
            f"tau_0_local = {lr.tau_0_local:.2e} should be much less than tau_0 = {TAU_0_S:.2e}"
        )

    def test_tau_local_approximately_equals_t_dyn(self):
        """τ_local ≈ t_dyn for astrophysical masses (within 0.1%)."""
        lr = compute_level_factorization()
        assert lr.level1_equals_t_dyn, (
            f"tau_0_local = {lr.tau_0_local:.2e} should ≈ t_dyn = {lr.t_dyn_s:.2e}"
        )

    def test_cosmo_static_limit_is_tau_0(self):
        """τ_eff_cosmo at H=0 must equal τ₀."""
        lr = compute_level_factorization()
        assert abs(lr.tau_eff_cosmo_at_H_zero - TAU_0_S) < 1e-6 * TAU_0_S

    def test_interior_static_limit_is_tau_local(self):
        """τ at V=0 in interior must equal τ₀_local (Level-1 only)."""
        lr = compute_level_factorization()
        assert abs(lr.tau_local_at_V_zero - lr.tau_0_local) < 1e-15

    def test_ratio_cosmo_to_interior_is_large(self):
        """Ratio τ_cosmo/τ_interior at static equilibrium must be ~10^19–20."""
        lr = compute_level_factorization()
        assert lr.ratio_cosmo_to_interior > 1e18, (
            f"ratio = {lr.ratio_cosmo_to_interior:.2e} should be > 10^18"
        )
        assert lr.ratio_cosmo_to_interior < 1e22

    def test_structural_identity_holds_for_tau_local(self):
        """ω₀·τ_local ≈ 1 (Level-1 identity)."""
        lr = compute_level_factorization()
        assert lr.structural_identity_holds, (
            f"omega_0 * tau_local = {lr.omega_0_tau_local:.4f}, should be ≈ 1"
        )

    def test_structural_identity_false_for_tau_0(self):
        """ω₀·τ₀ ≫ 1 (structural identity does NOT apply at τ₀)."""
        lr = compute_level_factorization()
        assert lr.structural_identity_false_at_tau0, (
            f"omega_0 * tau_0 = {lr.structural_identity_tau0:.2e} should be >> 1"
        )

    def test_q2_resonance_is_false(self):
        """Q2 resonance ω₀ = Ω = 1/τ₀ must be numerically false."""
        lr = compute_level_factorization()
        assert lr.resonance_false, (
            f"omega_0 / Omega = {lr.resonance_ratio_omega0_to_Omega:.2e}, "
            f"resonance (ratio ≈ 1) should be FALSE"
        )

    def test_interior_cutoff_much_larger_than_q2_cutoff(self):
        """The interior Lorentzian cutoff 1/τ_local must be >> 1/τ₀ (Q2 cutoff)."""
        lr = compute_level_factorization()
        assert lr.ratio_interior_to_q2_cutoff > 1e18, (
            f"ratio (1/tau_local) / (1/tau_0) = {lr.ratio_interior_to_q2_cutoff:.2e} "
            f"should be > 10^18 (interior and Q2 cutoffs are in different regimes)"
        )

    def test_level2_factorization_holds_cosmo(self):
        """Level-2 factorization must hold in the cosmological sector."""
        lr = compute_level_factorization()
        assert lr.level2_factorization_holds_cosmo

    def test_level2_factorization_holds_collapse(self):
        """Level-2 factorization must hold in the collapse sector."""
        lr = compute_level_factorization()
        assert lr.level2_factorization_holds_collapse

    def test_omega_0_tau_0_equals_ratio(self):
        """ω₀·τ₀ should equal the cosmo/interior ratio (same factor)."""
        lr = compute_level_factorization()
        expected_ratio = lr.structural_identity_tau0  # = omega_0 * tau_0
        actual_ratio = lr.ratio_cosmo_to_interior
        # ratio ≈ tau_0 / tau_local ≈ tau_0 / t_dyn ≈ omega_0 * tau_0
        assert abs(math.log10(actual_ratio) - math.log10(expected_ratio)) < 0.1, (
            f"ratio_cosmo_to_interior = {actual_ratio:.2e}, "
            f"omega_0 * tau_0 = {expected_ratio:.2e}. "
            f"Should agree on log scale."
        )


# ================================================================
# Resolution A/B/C Tests
# ================================================================

class TestResolutionAudit:

    def test_resolution_a_rejected(self):
        """Resolution A (true unification) must be rejected."""
        lr = compute_level_factorization()
        ra = build_resolution_audit(lr)
        assert ra.resolution_a_verdict == "reject", (
            f"Expected 'reject' for Resolution A, got '{ra.resolution_a_verdict}'"
        )

    def test_resolution_b_possible_but_unproven(self):
        """Resolution B (disciplined family) must be possible_but_unproven."""
        lr = compute_level_factorization()
        ra = build_resolution_audit(lr)
        assert ra.resolution_b_verdict == "possible_but_unproven", (
            f"Expected 'possible_but_unproven' for Resolution B, got '{ra.resolution_b_verdict}'"
        )

    def test_resolution_b_has_meta_rule(self):
        """Resolution B must provide the explicit meta-rule."""
        lr = compute_level_factorization()
        ra = build_resolution_audit(lr)
        assert len(ra.resolution_b_meta_rule) > 50, (
            "Resolution B meta-rule must be non-trivial (>50 chars)"
        )

    def test_resolution_c_is_weak(self):
        """Resolution C (structural split) must be weak."""
        lr = compute_level_factorization()
        ra = build_resolution_audit(lr)
        assert ra.resolution_c_verdict == "weak", (
            f"Expected 'weak' for Resolution C, got '{ra.resolution_c_verdict}'"
        )

    def test_strongest_resolution_is_b(self):
        """Resolution B must be the strongest viable resolution."""
        lr = compute_level_factorization()
        ra = build_resolution_audit(lr)
        assert ra.strongest_resolution == "B"


# ================================================================
# Identity Audit Tests
# ================================================================

class TestIdentityAudit:

    def test_tau_equals_tau0_at_equilibrium_cross_sector_is_false(self):
        """τ = τ₀ at equilibrium must be classified as false as cross-sector identity."""
        lr = compute_level_factorization()
        ia = build_identity_audit(lr)
        assert "false" in ia.tau_equals_tau0_at_equilibrium_cross_sector.lower()

    def test_tau_local_approximately_t_dyn(self):
        """τ_local ≈ t_dyn must hold (within 0.1%)."""
        lr = compute_level_factorization()
        ia = build_identity_audit(lr)
        assert ia.tau_local_approx_t_dyn
        assert ia.tau_local_approx_t_dyn_error < 0.001

    def test_structural_identity_uses_tau_local(self):
        """Structural identity ω₀·τ=1 must be associated with tau_local, not τ₀."""
        lr = compute_level_factorization()
        ia = build_identity_audit(lr)
        assert "tau_local" in ia.structural_identity_tau_object.lower()

    def test_structural_identity_cross_sector_is_misleading(self):
        """ω₀·τ=1 must be classified as symbolically misleading across sectors."""
        lr = compute_level_factorization()
        ia = build_identity_audit(lr)
        assert "misleading" in ia.structural_identity_cross_sector.lower() or \
               "false" in ia.structural_identity_cross_sector.lower()

    def test_q2_resonance_does_not_hold(self):
        """Q2 resonance ω₀ = Ω must NOT hold."""
        lr = compute_level_factorization()
        ia = build_identity_audit(lr)
        assert not ia.q2_resonance_holds

    def test_q2_resonance_classified_as_false(self):
        """Q2 resonance must be classified as false as cross-sector identity."""
        lr = compute_level_factorization()
        ia = build_identity_audit(lr)
        assert "false" in ia.q2_resonance_classification.lower()

    def test_collapse_cosmo_translation_valid(self):
        """τ_eff_collapse_bare = τ_eff_cosmo with ω-substitution must be valid."""
        lr = compute_level_factorization()
        ia = build_identity_audit(lr)
        assert ia.collapse_cosmo_translation_valid

    def test_cosmo_formula_valid_in_sector(self):
        """τ_eff_cosmo formula must be valid within the cosmological sector."""
        lr = compute_level_factorization()
        ia = build_identity_audit(lr)
        assert ia.cosmo_formula_valid_in_sector


# ================================================================
# Translation Rule Tests
# ================================================================

class TestTranslationRule:

    def test_rule_recovers_all_taus(self):
        """Translation rule must recover all sector τ objects."""
        tr = build_translation_rule()
        assert tr.rule_recovers_all_sector_taus

    def test_rule_resolves_resonance_confusion(self):
        """Translation rule must resolve the Q2 resonance confusion."""
        tr = build_translation_rule()
        assert tr.rule_resolves_resonance_confusion

    def test_rule_scopes_q2_bath(self):
        """Translation rule must correctly scope Q2 bath to Level-0."""
        tr = build_translation_rule()
        assert tr.rule_scopes_q2_bath_correctly

    def test_rule_preserves_prior_appendices(self):
        """Translation rule must preserve all prior appendix results."""
        tr = build_translation_rule()
        assert tr.rule_preserves_prior_appendices

    def test_rule_is_not_covariant(self):
        """Translation rule must NOT be classified as fully covariant."""
        tr = build_translation_rule()
        assert not tr.rule_is_covariant

    def test_level1_is_not_covariant(self):
        """Level-1 application must NOT be covariant (it is a mode switch)."""
        tr = build_translation_rule()
        assert not tr.rule_level1_is_covariant

    def test_level1_is_mode_switch(self):
        """Level-1 application must be documented as a mode switch."""
        tr = build_translation_rule()
        assert tr.level1_application_is_mode_switch

    def test_level2_is_universal(self):
        """Level-2 Lorentzian filter must be documented as universal."""
        tr = build_translation_rule()
        assert tr.rule_level2_is_universal

    def test_classification_is_partially_viable(self):
        """Translation rule classification must be translation_rule_partially_viable."""
        tr = build_translation_rule()
        assert tr.classification == "translation_rule_partially_viable", (
            f"Expected 'translation_rule_partially_viable', got '{tr.classification}'"
        )

    def test_nonclaims_present(self):
        """Translation rule must document at least 4 nonclaims."""
        tr = build_translation_rule()
        assert len(tr.nonclaims) >= 4


# ================================================================
# Full Audit Tests
# ================================================================

class TestFullAudit:

    def test_executive_determination(self):
        """Executive determination must be tau_symbolically_conflated_but_rescuable."""
        result = run_tau_family_audit()
        assert result.executive_determination == "tau_symbolically_conflated_but_rescuable", (
            f"Got: '{result.executive_determination}'"
        )

    def test_appendix_e_unchanged(self):
        """Appendix E classification must remain unchanged."""
        result = run_tau_family_audit()
        assert result.appendix_e_classification_unchanged
        assert result.appendix_e_classification == "locally_consistent_globally_underdetermined"

    def test_no_unsupported_claims(self):
        """No forbidden claims must appear in the result."""
        result = run_tau_family_audit()
        result.assert_no_unsupported_claims()   # Should not raise

    def test_valid_flag(self):
        """Result must be valid."""
        result = run_tau_family_audit()
        assert result.valid

    def test_cross_sector_impacts_documented(self):
        """All four cross-sector impact statements must be non-empty."""
        result = run_tau_family_audit()
        assert len(result.appendix_d_impact) > 20
        assert len(result.q1q4_impact) > 20
        assert len(result.constitutive_impact) > 20
        assert len(result.cosmological_impact) > 10

    def test_cosmological_impact_is_none(self):
        """Cosmological impact must be documented as minimal/none."""
        result = run_tau_family_audit()
        assert "NONE" in result.cosmological_impact or "none" in result.cosmological_impact.lower()

    def test_q1q4_impact_is_reinterpretation(self):
        """Q1-Q4 impact must be documented as reinterpretation, not contradiction."""
        result = run_tau_family_audit()
        assert "REINTERPRETATION" in result.q1q4_impact or \
               "reinterpretation" in result.q1q4_impact.lower()

    def test_serialization(self):
        """Full result must serialize to dict without error."""
        result = run_tau_family_audit()
        d = result.to_dict()
        assert isinstance(d, dict)
        assert "executive_determination" in d
        assert "tau_family_map" in d
        assert "level_factorization" in d
        assert "resolutions" in d
        assert "identities" in d
        assert "translation_rule" in d

    def test_to_dict_classification_correct(self):
        """Serialized classification must match expected value."""
        result = run_tau_family_audit()
        d = result.to_dict()
        assert d["appendix_e_classification"] == "locally_consistent_globally_underdetermined"
        assert d["executive_determination"] == "tau_symbolically_conflated_but_rescuable"


# ================================================================
# Guard Tests
# ================================================================

class TestGuards:

    def test_forbidden_classification_tau_unified_raises(self):
        """Injecting tau_unified must raise AssertionError."""
        result = run_tau_family_audit()
        original = result.executive_determination
        result.executive_determination = "tau_unified"
        with pytest.raises(AssertionError, match="tau_unified"):
            result.assert_no_unsupported_claims()
        result.executive_determination = original

    def test_forbidden_classification_fully_covariant_raises(self):
        """Injecting tau_fully_covariant must raise AssertionError."""
        result = run_tau_family_audit()
        original = result.executive_determination
        result.executive_determination = "tau_fully_covariant"
        with pytest.raises(AssertionError):
            result.assert_no_unsupported_claims()
        result.executive_determination = original

    def test_forbidden_classification_upgrading_appendix_e_raises(self):
        """Setting classification_unchanged=False must raise AssertionError."""
        result = run_tau_family_audit()
        result.appendix_e_classification_unchanged = False
        with pytest.raises(AssertionError):
            result.assert_no_unsupported_claims()

    def test_forbidden_set_is_complete(self):
        """The forbidden classification set must include at least 5 entries."""
        assert len(_FORBIDDEN_CLASSIFICATIONS) >= 5

    def test_omega_0_does_not_equal_omega_bath(self):
        """ω₀ must NOT equal the Q2 bath cutoff Ω = 1/τ₀."""
        lr = compute_level_factorization()
        # omega_0 ~ 10^4 rad/s, Omega = 1/tau_0 ~ 10^-15 rad/s
        assert abs(lr.omega_0_rad_s - lr.omega_bath_cutoff) > lr.omega_0_rad_s * 0.5, (
            f"omega_0 = {lr.omega_0_rad_s:.2e}, Omega = {lr.omega_bath_cutoff:.2e}. "
            f"These should differ by >> 1."
        )


# ================================================================
# Numerical Verification Tests
# ================================================================

class TestNumericalVerification:

    def test_tau_0_local_formula_at_reference_mass(self):
        """τ₀_local = τ₀·t_dyn/(t_dyn+τ₀) ≈ t_dyn for 30 M_sun."""
        lr = compute_level_factorization(M_REF_KG)
        # tau_0_local should be approximately t_dyn for astrophysical masses
        assert abs(lr.tau_0_local / lr.t_dyn_s - 1.0) < 1e-10, (
            f"tau_0_local/t_dyn = {lr.tau_0_local/lr.t_dyn_s:.10f}, "
            f"should be ≈ 1.0 (since t_dyn << tau_0)"
        )

    def test_structural_identity_value(self):
        """ω₀·τ_local must be within 5% of 1.0."""
        lr = compute_level_factorization()
        assert abs(lr.omega_0_tau_local - 1.0) < 0.05

    def test_resonance_ratio_magnitude(self):
        """Resonance ratio ω₀/Ω must be ~10^19 for 30 M_sun."""
        lr = compute_level_factorization()
        assert lr.resonance_ratio_omega0_to_Omega > 1e18
        assert lr.resonance_ratio_omega0_to_Omega < 1e21

    def test_interior_vs_q2_cutoff_ratio(self):
        """Interior cutoff / Q2 cutoff must be ~10^19 for 30 M_sun."""
        lr = compute_level_factorization()
        # Both ratios should be approximately equal (both ≈ tau_0/t_dyn)
        assert abs(
            math.log10(lr.ratio_interior_to_q2_cutoff) -
            math.log10(lr.resonance_ratio_omega0_to_Omega)
        ) < 0.2, (
            "Interior/Q2 cutoff ratio should equal omega_0/Omega (both ≈ tau_0/t_dyn)"
        )

    def test_level1_reduction_factor_is_tiny(self):
        """Level-1 reduction factor τ₀_local/τ₀ must be negligibly small."""
        lr = compute_level_factorization()
        assert lr.level1_reduction_factor < 1e-10, (
            f"Level-1 reduction factor = {lr.level1_reduction_factor:.2e}, should be < 10^-10"
        )
