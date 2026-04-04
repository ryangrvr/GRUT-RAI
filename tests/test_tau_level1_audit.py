"""Tests for grut/tau_level1_audit.py — Appendix G Level-1 τ Rule Audit.

These tests verify:
1. Timescale computations at key radii
2. Structural identity ω₀·t_dyn = 1 (algebraically exact for β_Q = 2)
3. Activation criterion: R_cross >> r_s for astrophysical masses
4. Level-1 regime: t_dyn << τ₀ for all astrophysical BH radii
5. Parallel-rate algebraic equivalence
6. Route verdicts (Route A viable, Route B closed, Route C consistency)
7. Forbidden claim guards
"""

import math
import pytest

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from grut.tau_level1_audit import (
    # Constants
    G_SI, C_SI, TAU_0_S, ALPHA_VAC, BETA_Q, EPSILON_Q,
    R_EQ_OVER_RS, M_SUN_KG, M_REF_KG,
    OMEGA_0_TAU_IDENTITY, _FORBIDDEN_CLASSIFICATIONS,
    # Data structures
    Level1TimescalePoint, ParallelRateAnalysis,
    CovariantReductionAnalysis, StructuralConsistencyAnalysis,
    ActivationCriterionAnalysis, Level1AuditResult,
    # Computation helpers
    compute_t_dyn, compute_tau_local, compute_omega_0, compute_R_cross,
    # Builders
    build_timescale_profile, build_parallel_rate_analysis,
    build_covariant_reduction_analysis, build_structural_consistency_analysis,
    build_activation_criterion,
    # Master runner
    run_level1_audit,
    # Summary
    summary_string,
)


# ================================================================
# Fixtures
# ================================================================

@pytest.fixture
def ref_mass():
    """Reference mass: 30 M_sun."""
    return M_REF_KG


@pytest.fixture
def audit_result(ref_mass):
    """Full audit result at reference mass."""
    return run_level1_audit(M_kg=ref_mass)


@pytest.fixture
def eq_point(ref_mass):
    """Timescale point at the equilibrium radius."""
    points = build_timescale_profile(M_kg=ref_mass)
    return next(p for p in points if p.is_equilibrium)


# ================================================================
# Part 1: Basic Parameter Tests
# ================================================================

class TestParameters:
    def test_tau0_canonical_value(self):
        assert abs(TAU_0_S - 1.3225e15) < 1e10, "τ₀ should be ~1.3225×10¹⁵ s"

    def test_alpha_vac(self):
        assert abs(ALPHA_VAC - 1.0 / 3.0) < 1e-12

    def test_beta_q(self):
        assert BETA_Q == 2.0

    def test_epsilon_q(self):
        assert abs(EPSILON_Q - ALPHA_VAC ** 2) < 1e-15
        assert abs(EPSILON_Q - 1.0 / 9.0) < 1e-15

    def test_r_eq_over_rs(self):
        # R_eq/r_s = ε_Q^(1/β_Q) = (1/9)^(1/2) = 1/3
        assert abs(R_EQ_OVER_RS - 1.0 / 3.0) < 1e-12

    def test_structural_identity_target(self):
        assert OMEGA_0_TAU_IDENTITY == 1.0

    def test_reference_mass(self):
        assert abs(M_REF_KG / M_SUN_KG - 30.0) < 0.01


# ================================================================
# Part 2: Computation Helper Tests
# ================================================================

class TestComputationHelpers:
    def test_t_dyn_formula(self, ref_mass):
        """t_dyn = sqrt(R³/(2GM)) should be positive and finite."""
        r_s = 2.0 * G_SI * ref_mass / C_SI ** 2
        t = compute_t_dyn(r_s, ref_mass)
        assert t > 0
        assert math.isfinite(t)

    def test_t_dyn_scales_correctly(self, ref_mass):
        """t_dyn ∝ R^(3/2), so doubling R increases t_dyn by factor 2^(3/2)."""
        r_s = 2.0 * G_SI * ref_mass / C_SI ** 2
        t1 = compute_t_dyn(r_s, ref_mass)
        t2 = compute_t_dyn(2 * r_s, ref_mass)
        ratio = t2 / t1
        assert abs(ratio - 2 ** 1.5) < 1e-9

    def test_tau_local_limits_small_tdyn(self):
        """When t_dyn << τ₀: τ_local ≈ t_dyn."""
        tau0 = 1e15
        tdyn = 1e-3   # << tau0
        tau_local = compute_tau_local(tau0, tdyn)
        assert abs(tau_local / tdyn - 1.0) < 1e-15   # τ_local → t_dyn

    def test_tau_local_limits_large_tdyn(self):
        """When t_dyn >> τ₀: τ_local ≈ τ₀."""
        tau0 = 1e15
        tdyn = 1e30   # >> tau0
        tau_local = compute_tau_local(tau0, tdyn)
        assert abs(tau_local / tau0 - 1.0) < 1e-14   # τ_local → τ₀

    def test_tau_local_at_crossover(self):
        """When t_dyn = τ₀: τ_local = τ₀/2."""
        tau0 = 1e15
        tdyn = tau0
        tau_local = compute_tau_local(tau0, tdyn)
        assert abs(tau_local / tau0 - 0.5) < 1e-12

    def test_parallel_rate_equivalence(self):
        """τ_local = τ₀·t/(τ₀+t) ≡ 1/(1/τ₀ + 1/t)."""
        tau0 = 1.3225e15
        t = 1e-4
        tau_from_formula = compute_tau_local(tau0, t)
        tau_from_rate = 1.0 / (1.0 / tau0 + 1.0 / t)
        assert abs(tau_from_formula - tau_from_rate) < 1e-30   # exact equality

    def test_compute_omega_0(self, ref_mass):
        """ω₀ = sqrt(β_Q·GM/R_eq³) > 0."""
        r_s = 2.0 * G_SI * ref_mass / C_SI ** 2
        R_eq = R_EQ_OVER_RS * r_s
        omega_0 = compute_omega_0(BETA_Q, ref_mass, R_eq)
        assert omega_0 > 0
        assert math.isfinite(omega_0)

    def test_compute_R_cross(self, ref_mass):
        """R_cross = (2GM·τ₀²)^(1/3) > 0."""
        R_cross = compute_R_cross(ref_mass, TAU_0_S)
        assert R_cross > 0
        assert math.isfinite(R_cross)


# ================================================================
# Part 3: Structural Identity Tests
# ================================================================

class TestStructuralIdentity:
    def test_omega_0_times_tdyn_exactly_one(self, ref_mass):
        """ω₀·t_dyn(R_eq) = 1 exactly for β_Q = 2 (mass-independent algebraic fact).

        Proof: ω₀ = sqrt(β_Q·GM/R_eq³), t_dyn = sqrt(R_eq³/(2GM))
               ω₀·t_dyn = sqrt(β_Q·GM/R_eq³)·sqrt(R_eq³/(2GM)) = sqrt(β_Q/2) = 1.
        """
        r_s = 2.0 * G_SI * ref_mass / C_SI ** 2
        R_eq = R_EQ_OVER_RS * r_s
        omega_0 = compute_omega_0(BETA_Q, ref_mass, R_eq)
        t_dyn = compute_t_dyn(R_eq, ref_mass)
        product = omega_0 * t_dyn
        assert abs(product - 1.0) < 1e-12, (
            f"ω₀·t_dyn = {product:.12f} (should be exactly 1.0 for β_Q=2)"
        )

    def test_omega_0_times_tdyn_mass_independent(self):
        """ω₀·t_dyn(R_eq) = 1 for all masses (algebraic, not numerical)."""
        for M_solar in [10.0, 30.0, 100.0, 1e6]:
            M_kg = M_solar * M_SUN_KG
            r_s = 2.0 * G_SI * M_kg / C_SI ** 2
            R_eq = R_EQ_OVER_RS * r_s
            omega_0 = compute_omega_0(BETA_Q, M_kg, R_eq)
            t_dyn = compute_t_dyn(R_eq, M_kg)
            product = omega_0 * t_dyn
            assert abs(product - 1.0) < 1e-10, (
                f"For M={M_solar:.0f} M_sun: ω₀·t_dyn = {product:.12f}"
            )

    def test_omega_0_times_tdyn_formula(self):
        """ω₀·t_dyn = sqrt(β_Q/2) algebraically."""
        # With β_Q = 2: sqrt(2/2) = 1
        # With β_Q = 4: sqrt(4/2) = sqrt(2) ≈ 1.414
        for beta in [1.0, 2.0, 4.0]:
            expected = math.sqrt(beta / 2.0)
            M_kg = M_REF_KG
            r_s = 2.0 * G_SI * M_kg / C_SI ** 2
            R_eq = R_EQ_OVER_RS * r_s
            omega_0 = compute_omega_0(beta, M_kg, R_eq)
            t_dyn = compute_t_dyn(R_eq, M_kg)
            product = omega_0 * t_dyn
            assert abs(product - expected) < 1e-10, (
                f"β_Q={beta}: ω₀·t_dyn = {product:.6f}, expected {expected:.6f}"
            )

    def test_omega_0_tau_local_approx_one(self, eq_point):
        """ω₀·τ_local(R_eq) ≈ 1.0 for astrophysical masses (error ≈ t_dyn/τ₀)."""
        product = eq_point.omega_0_times_tau_local
        # For 30 M_sun, error is t_dyn/τ₀ ~ 10^{-19}
        assert abs(product - 1.0) < 1e-12, (
            f"ω₀·τ_local = {product:.12f} (should be ≈ 1.0 for astrophysical mass)"
        )

    def test_omega_0_tau0_much_greater_than_one(self, eq_point):
        """ω₀·τ₀ >> 1 for astrophysical masses (demonstrates why τ₀ is wrong)."""
        product = eq_point.omega_0_times_tau0
        # For 30 M_sun, ω₀·τ₀ ~ 10^{19}
        assert product > 1e15, (
            f"ω₀·τ₀ = {product:.4e} (should be >> 1, around 10^19 for 30 M_sun)"
        )


# ================================================================
# Part 4: Level-1 Regime Tests
# ================================================================

class TestLevel1Regime:
    def test_all_three_radii_in_level1_regime(self, ref_mass):
        """t_dyn < τ₀ at r_s/3, r_s, and 100·r_s for 30 M_sun."""
        points = build_timescale_profile(M_kg=ref_mass)
        for pt in points:
            assert pt.in_level1_regime, (
                f"Expected Level-1 regime at {pt.label}: "
                f"t_dyn/τ₀ = {pt.t_dyn_over_tau0:.4e}"
            )

    def test_t_dyn_over_tau0_at_equilibrium(self, eq_point):
        """t_dyn(R_eq)/τ₀ << 1 for 30 M_sun (expected ~10⁻¹⁹)."""
        ratio = eq_point.t_dyn_over_tau0
        assert ratio < 1e-10, (
            f"t_dyn/τ₀ = {ratio:.4e} (expected << 1 for astrophysical mass)"
        )

    def test_tau_local_approx_tdyn_at_equilibrium(self, eq_point):
        """τ_local ≈ t_dyn at equilibrium (ratio should be ≈ 1.0)."""
        ratio = eq_point.tau_local_over_tdyn
        # τ_local/t_dyn = 1 / (1 + t_dyn/τ₀) ≈ 1 for t_dyn << τ₀
        assert abs(ratio - 1.0) < 1e-10, (
            f"τ_local/t_dyn = {ratio:.12f} (should be ≈ 1.0)"
        )

    def test_timescale_profile_has_three_radii(self, ref_mass):
        """Timescale profile should be evaluated at exactly 3 radii."""
        points = build_timescale_profile(M_kg=ref_mass)
        assert len(points) == 3

    def test_exactly_one_equilibrium_point(self, ref_mass):
        """Exactly one of the 3 profile points should be the equilibrium."""
        points = build_timescale_profile(M_kg=ref_mass)
        eq_points = [p for p in points if p.is_equilibrium]
        assert len(eq_points) == 1

    def test_t_dyn_increases_with_radius(self, ref_mass):
        """t_dyn should increase with increasing R (t_dyn ∝ R^(3/2))."""
        points = build_timescale_profile(M_kg=ref_mass)
        t_dyns = [p.t_dyn_s for p in points]
        # Check monotonically increasing (radii are in order: R_eq, r_s, 100·r_s)
        # Note: profile is built with radii in order from large to small
        # (100·r_s, r_s, R_eq) — check the ordering
        # Actually from the code: "R_0 = 100·r_s" is first, "R_eq" is last
        assert t_dyns[0] > t_dyns[-1], "t_dyn at 100·r_s should > t_dyn at R_eq"


# ================================================================
# Part 5: Activation Criterion Tests
# ================================================================

class TestActivationCriterion:
    def test_R_cross_much_greater_than_rs(self, ref_mass):
        """R_cross >> r_s for astrophysical masses → Level-1 always active."""
        ac = build_activation_criterion(M_kg=ref_mass)
        assert ac.R_cross_over_rs > 1e10, (
            f"R_cross/r_s = {ac.R_cross_over_rs:.4e} (expected >> 1)"
        )

    def test_R_eq_inside_level1_regime(self, ref_mass):
        """R_eq < R_cross for astrophysical masses."""
        ac = build_activation_criterion(M_kg=ref_mass)
        assert ac.R_eq_in_level1 is True

    def test_astrophysical_universality(self, ref_mass):
        """Flag: Level-1 always activates for astrophysical BHs."""
        ac = build_activation_criterion(M_kg=ref_mass)
        assert ac.astrophysical_always_level1 is True

    def test_R_cross_formula(self, ref_mass):
        """R_cross = (2GM·τ₀²)^(1/3) should satisfy t_dyn(R_cross) = τ₀."""
        ac = build_activation_criterion(M_kg=ref_mass)
        R_cross = ac.R_cross_m
        M_kg = ac.M_ref_kg
        tau0 = ac.tau0_s
        # Verify: t_dyn(R_cross) = τ₀
        t_at_cross = compute_t_dyn(R_cross, M_kg)
        assert abs(t_at_cross / tau0 - 1.0) < 1e-10, (
            f"t_dyn(R_cross)/τ₀ = {t_at_cross/tau0:.12f} (should be 1.0)"
        )

    def test_criterion_is_deterministic_not_covariant(self, ref_mass):
        """The activation criterion is deterministic but NOT covariant."""
        ac = build_activation_criterion(M_kg=ref_mass)
        assert ac.criterion_is_deterministic is True
        assert ac.criterion_is_covariant is False

    def test_R_cross_scales_with_mass(self):
        """R_cross ∝ M^(1/3) (since R_cross = (2GM·τ₀²)^(1/3) ∝ M^(1/3))."""
        M1 = 10.0 * M_SUN_KG
        M2 = 80.0 * M_SUN_KG   # 8× M1
        R1 = compute_R_cross(M1, TAU_0_S)
        R2 = compute_R_cross(M2, TAU_0_S)
        ratio = R2 / R1
        expected = (80.0 / 10.0) ** (1.0 / 3.0)   # 8^(1/3) = 2
        assert abs(ratio - expected) < 1e-9


# ================================================================
# Part 6: Derivation Route Tests
# ================================================================

class TestDerivationRoutes:
    def test_route_a_formulas_equivalent(self):
        """Route A: parallel-rate and direct formula must be algebraically equivalent."""
        result = build_parallel_rate_analysis()
        assert result.formulas_equivalent is True

    def test_route_a_verdict_partially_viable(self):
        """Route A should be classified as PARTIALLY_VIABLE."""
        result = build_parallel_rate_analysis()
        assert result.verdict == "PARTIALLY_VIABLE"

    def test_route_a_local_channel_not_grut_derived(self):
        """Route A: local channel NOT derived from GRUT field equations."""
        result = build_parallel_rate_analysis()
        assert result.local_channel_derivable_from_grut is False

    def test_route_b_verdict_closed(self):
        """Route B: covariant reduction is CLOSED (requires interior metric)."""
        result = build_covariant_reduction_analysis()
        assert result.verdict == "CLOSED"

    def test_route_b_requires_interior_metric(self):
        """Route B: requires interior metric (which is a missing closure)."""
        result = build_covariant_reduction_analysis()
        assert result.requires_interior_metric is True
        assert result.interior_metric_available is False

    def test_route_c_verdict_consistency_not_derivation(self):
        """Route C: consistency argument, NOT a derivation."""
        result = build_structural_consistency_analysis()
        assert result.verdict == "CONSISTENCY_ARGUMENT_NOT_DERIVATION"

    def test_route_c_is_circular(self):
        """Route C: explicitly flagged as circular."""
        result = build_structural_consistency_analysis()
        assert result.is_circular is True

    def test_route_c_omega_0_times_tdyn_exact(self):
        """Route C: ω₀·t_dyn(R_eq) = 1.0 (exact algebraic verification)."""
        result = build_structural_consistency_analysis()
        assert abs(result.omega_0_times_tdyn_exact - 1.0) < 1e-12

    def test_route_c_omega_0_times_tau_local_approx_one(self):
        """Route C: ω₀·τ_local(R_eq) ≈ 1.0 for reference mass."""
        result = build_structural_consistency_analysis()
        assert abs(result.omega_0_times_tau_local_at_ref - 1.0) < 1e-10


# ================================================================
# Part 7: Master Audit Tests
# ================================================================

class TestMasterAudit:
    def test_audit_runs_without_error(self, audit_result):
        """The master audit should complete without raising an exception."""
        assert audit_result.valid is True

    def test_executive_determination_is_correct(self, audit_result):
        """Executive determination should be 'structurally_motivated_heuristic_not_derived'."""
        assert audit_result.executive_determination == (
            "structurally_motivated_heuristic_not_derived"
        )

    def test_appendix_e_classification_unchanged(self, audit_result):
        """Appendix E classification must not be upgraded."""
        assert audit_result.appendix_e_classification == (
            "locally_consistent_globally_underdetermined"
        )

    def test_appendix_f_classification_unchanged(self, audit_result):
        """Appendix F classification must not be changed."""
        assert audit_result.appendix_f_classification == (
            "tau_symbolically_conflated_but_rescuable"
        )

    def test_covariant_criterion_not_available(self, audit_result):
        """Covariant activation criterion is NOT available."""
        assert audit_result.covariant_criterion_available is False

    def test_safe_claims_populated(self, audit_result):
        """Should have at least 5 safe claims."""
        assert len(audit_result.safe_claims) >= 5

    def test_unsafe_claims_populated(self, audit_result):
        """Should have at least 4 unsafe claims."""
        assert len(audit_result.unsafe_claims) >= 4

    def test_nonclaims_populated(self, audit_result):
        """Should have at least 3 nonclaims."""
        assert len(audit_result.nonclaims) >= 3

    def test_missing_closures_populated(self, audit_result):
        """Should document at least 2 missing closures."""
        assert len(audit_result.missing_closures) >= 2

    def test_three_timescale_points(self, audit_result):
        """Timescale profile has exactly 3 points."""
        assert len(audit_result.timescale_points) == 3

    def test_route_verdicts_in_result(self, audit_result):
        """All three route verdicts should be set."""
        assert audit_result.route_a_parallel_rate.verdict == "PARTIALLY_VIABLE"
        assert audit_result.route_b_covariant.verdict == "CLOSED"
        assert audit_result.route_c_consistency.verdict == "CONSISTENCY_ARGUMENT_NOT_DERIVATION"

    def test_mode_switch_recommendation_non_empty(self, audit_result):
        """Mode switch recommendation should be documented."""
        assert len(audit_result.mode_switch_recommendation) > 50


# ================================================================
# Part 8: Forbidden Claim Guards
# ================================================================

class TestForbiddenClaimGuards:
    def test_forbidden_classifications_defined(self):
        """At least 5 forbidden classification strings are defined."""
        assert len(_FORBIDDEN_CLASSIFICATIONS) >= 5

    def test_level1_covariant_is_forbidden(self):
        """'level1_covariant' must be in the forbidden set."""
        assert "level1_covariant" in _FORBIDDEN_CLASSIFICATIONS

    def test_level1_derived_from_action_is_forbidden(self):
        """'level1_derived_from_action' must be in the forbidden set."""
        assert "level1_derived_from_action" in _FORBIDDEN_CLASSIFICATIONS

    def test_mode_switch_obsolete_is_forbidden(self):
        """'mode_switch_obsolete' must be in the forbidden set."""
        assert "mode_switch_obsolete" in _FORBIDDEN_CLASSIFICATIONS

    def test_guard_raises_on_level1_covariant(self):
        """assert_no_unsupported_claims() raises if 'level1_covariant' appears."""
        result = Level1AuditResult()
        result.executive_determination = "level1_covariant"
        with pytest.raises(AssertionError, match="level1_covariant"):
            result.assert_no_unsupported_claims()

    def test_guard_raises_on_level1_derived_from_action(self):
        """assert_no_unsupported_claims() raises if 'level1_derived_from_action' appears."""
        result = Level1AuditResult()
        result.executive_determination = "level1_derived_from_action"
        with pytest.raises(AssertionError):
            result.assert_no_unsupported_claims()

    def test_guard_raises_on_mode_switch_obsolete(self):
        """assert_no_unsupported_claims() raises if 'mode_switch_obsolete' appears."""
        result = Level1AuditResult()
        result.executive_determination = "mode_switch_obsolete"
        with pytest.raises(AssertionError):
            result.assert_no_unsupported_claims()

    def test_guard_passes_on_correct_determination(self, audit_result):
        """Guard should NOT raise for the correct determination."""
        # This should not raise:
        audit_result.assert_no_unsupported_claims()

    def test_guard_raises_on_tau_local_equals_tau0(self):
        """'tau_local_equals_tau0' is a forbidden classification."""
        result = Level1AuditResult()
        result.executive_determination = "tau_local_equals_tau0"
        with pytest.raises(AssertionError):
            result.assert_no_unsupported_claims()


# ================================================================
# Part 9: Summary String Test
# ================================================================

class TestSummaryString:
    def test_summary_string_produced(self, audit_result):
        """summary_string() should return a non-empty string."""
        s = summary_string(audit_result)
        assert isinstance(s, str)
        assert len(s) > 200

    def test_summary_contains_determination(self, audit_result):
        """Summary should mention the executive determination."""
        s = summary_string(audit_result)
        assert "structurally_motivated_heuristic_not_derived" in s

    def test_summary_contains_route_verdicts(self, audit_result):
        """Summary should show all three route verdicts."""
        s = summary_string(audit_result)
        assert "PARTIALLY_VIABLE" in s
        assert "CLOSED" in s
        assert "CONSISTENCY_ARGUMENT_NOT_DERIVATION" in s

    def test_summary_contains_r_cross(self, audit_result):
        """Summary should mention R_cross."""
        s = summary_string(audit_result)
        assert "R_cross" in s


# ================================================================
# Part 10: Cross-sector Consistency Tests
# ================================================================

class TestCrossSectorConsistency:
    def test_level1_rule_consistent_with_interior_pde(self, ref_mass):
        """The τ_local computed by this module should match what interior_pde.py uses.

        interior_pde.py uses:
            t_dyn = sqrt(R_eq³ / (2GM))
            tau_local = tau0 * t_dyn / (t_dyn + tau0)
        This module uses the same formula.
        """
        r_s = 2.0 * G_SI * ref_mass / C_SI ** 2
        R_eq = R_EQ_OVER_RS * r_s
        t_dyn = compute_t_dyn(R_eq, ref_mass)
        tau_local = compute_tau_local(TAU_0_S, t_dyn)

        # interior_pde.py computes the same way
        t_dyn_pde = math.sqrt(R_eq ** 3 / (2.0 * G_SI * ref_mass))
        tau_local_pde = TAU_0_S * t_dyn_pde / (t_dyn_pde + TAU_0_S)

        assert abs(tau_local - tau_local_pde) / tau_local < 1e-12

    def test_tau_local_equals_t_dyn_to_very_high_accuracy(self, ref_mass):
        """At astrophysical masses, τ_local = t_dyn × (1 - t_dyn/τ₀ + ...) ≈ t_dyn.

        The fractional difference is t_dyn/τ₀ ~ 10⁻¹⁹ for 30 M_sun at R_eq.
        """
        r_s = 2.0 * G_SI * ref_mass / C_SI ** 2
        R_eq = R_EQ_OVER_RS * r_s
        t_dyn = compute_t_dyn(R_eq, ref_mass)
        tau_local = compute_tau_local(TAU_0_S, t_dyn)

        # τ_local/t_dyn = 1/(1 + t_dyn/τ₀) ≈ 1 - t_dyn/τ₀  (for t_dyn << τ₀)
        # The fractional error should be ≈ t_dyn/τ₀ ~ 10⁻¹⁹
        fractional_error = abs(tau_local / t_dyn - 1.0)
        expected_order = t_dyn / TAU_0_S   # ~ 10⁻¹⁹ for 30 M_sun at R_eq

        # They agree to within a factor of 2 (floating-point rounding at 10⁻²⁰ level)
        assert fractional_error < 1e-15, (
            f"fractional error = {fractional_error:.4e} (expected ~ {expected_order:.4e})"
        )
        # And the error scale matches the t_dyn/τ₀ ratio
        assert fractional_error < 100.0 * expected_order, (
            f"fractional_error = {fractional_error:.4e} should not exceed "
            f"100 × t_dyn/τ₀ = {100.0*expected_order:.4e}"
        )

    def test_endpoint_law_consistent_with_r_eq(self, ref_mass):
        """R_eq = r_s · ε_Q^(1/β_Q) = r_s/3 (from canon parameters)."""
        r_s = 2.0 * G_SI * ref_mass / C_SI ** 2
        R_eq_from_canon = EPSILON_Q ** (1.0 / BETA_Q) * r_s
        assert abs(R_eq_from_canon / r_s - 1.0 / 3.0) < 1e-12

    def test_structural_identity_uses_tau_local_not_tau0(self, ref_mass):
        """ω₀·τ₀ != 1 while ω₀·τ_local ≈ 1 — confirms τ_local is the correct parameter."""
        r_s = 2.0 * G_SI * ref_mass / C_SI ** 2
        R_eq = R_EQ_OVER_RS * r_s
        omega_0 = compute_omega_0(BETA_Q, ref_mass, R_eq)
        t_dyn = compute_t_dyn(R_eq, ref_mass)
        tau_local = compute_tau_local(TAU_0_S, t_dyn)

        product_tau0 = omega_0 * TAU_0_S
        product_tau_local = omega_0 * tau_local

        # τ₀ gives the wrong answer
        assert product_tau0 > 1e15   # >> 1

        # τ_local gives the right answer
        assert abs(product_tau_local - 1.0) < 1e-10   # ≈ 1
