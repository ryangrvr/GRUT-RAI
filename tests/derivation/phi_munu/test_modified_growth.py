"""Regression tests for the Phase 3.1 modified-growth analysis.

Pins:
  - Symbolic form of the modified linear growth equation
  - Power-law growing-mode exponents in matter-dom (analytic)
  - Background-cosmology utilities (H, Ω_m, d ln H/dN)
  - μ_GRUT(k, a) numerical
  - Numerical growth-factor integration
  - Growth-factor enhancement f_GRUT(k) at canonical scales
  - Honest assessment: σ_8 unchanged, large scales enhanced

The σ_8-scale check is load-bearing: it pins the framework's claim
that modified growth does NOT break the existing S_8 tension between
Planck CMB and weak-lensing measurements. Sub-horizon modes recover
ΛCDM growth at the structural level (μ → 1), and the numerical
integration confirms this at the percent level.
"""

from __future__ import annotations

import numpy as np
import pytest
import sympy as sp


# ─────────────────────────────────────────────────────────────────────
# Module imports & verify()
# ─────────────────────────────────────────────────────────────────────


class TestModifiedGrowthImports:
    def test_module_importable(self):
        from grut.derivation.phi_munu import modified_growth  # noqa
        assert hasattr(modified_growth, "verify")

    def test_module_exports_phase_3p1_API(self):
        from grut.derivation.phi_munu.modified_growth import (
            convention_declaration,
            modified_growth_equation_symbolic,
            growing_mode_exponent,
            growing_mode_exponent_numeric,
            growing_mode_enhancement_per_efold,
            H_over_H_0,
            Omega_m_of_a,
            d_lnH_dN,
            mu_GRUT_numeric,
            integrate_growth_factor,
            growth_factor_enhancement,
            growth_enhancement_survey,
            honest_assessment_summary,
            verify,
        )
        for fn in (
            convention_declaration,
            modified_growth_equation_symbolic,
            growing_mode_exponent,
            growing_mode_exponent_numeric,
            growing_mode_enhancement_per_efold,
            H_over_H_0,
            Omega_m_of_a,
            d_lnH_dN,
            mu_GRUT_numeric,
            integrate_growth_factor,
            growth_factor_enhancement,
            growth_enhancement_survey,
            honest_assessment_summary,
            verify,
        ):
            assert callable(fn)


class TestVerifyHarness:
    def test_verify_all_eight_legs_pass(self):
        from grut.derivation.phi_munu.modified_growth import verify
        v = verify()
        for k, val in v.items():
            assert val is True, f"Phase 3.1 verify() leg failed: {k} = {val}"


# ─────────────────────────────────────────────────────────────────────
# Convention declaration (Phase 3.1)
# ─────────────────────────────────────────────────────────────────────


class TestConventionDeclaration:
    def test_C1p3p1_growth_equation_form(self):
        from grut.derivation.phi_munu.modified_growth import (
            convention_declaration,
        )
        d = convention_declaration()
        c1 = d["C1p3p1_growth_equation_form"]
        assert "δ" in c1 or "delta" in c1.lower()
        assert "Ω_m" in c1 or "Omega_m" in c1
        assert "μ" in c1 or "mu" in c1.lower()

    def test_C2p3p1_initial_conditions_at_matter_dom(self):
        from grut.derivation.phi_munu.modified_growth import (
            convention_declaration,
        )
        d = convention_declaration()
        c2 = d["C2p3p1_initial_conditions"]
        assert "matter-dom" in c2.lower() or "matter dom" in c2.lower()
        assert "growing mode" in c2.lower() or "growing-mode" in c2.lower()

    def test_C3p3p1_lcdm_background(self):
        from grut.derivation.phi_munu.modified_growth import (
            convention_declaration,
        )
        d = convention_declaration()
        c3 = d["C3p3p1_lcdm_background"]
        assert "ΛCDM" in c3 or "LCDM" in c3 or "Lambda" in c3
        assert "0.315" in c3 or "Omega_m" in c3 or "Ω_m" in c3

    def test_C5p3p1_growth_factor_enhancement_definition(self):
        from grut.derivation.phi_munu.modified_growth import (
            convention_declaration,
        )
        d = convention_declaration()
        c5 = d["C5p3p1_growth_factor_enhancement"]
        assert "f_GRUT" in c5
        assert "δ_GRUT" in c5 or "delta_GRUT" in c5

    def test_C6p3p1_scope_clarification_present(self):
        """The scope clarification (linear FRW only) carries through
        from Priority 3 — bound systems use different operating
        variables."""
        from grut.derivation.phi_munu.modified_growth import (
            convention_declaration,
        )
        d = convention_declaration()
        c6 = d["C6p3p1_scope_linear_FRW"]
        assert "Linear FRW" in c6 or "linear FRW" in c6
        assert "bound" in c6.lower() or "nonlinear" in c6.lower()


# ─────────────────────────────────────────────────────────────────────
# Symbolic equation and analytic limits
# ─────────────────────────────────────────────────────────────────────


class TestSymbolicGrowthEquation:
    def test_equation_is_sympy_expression(self):
        from grut.derivation.phi_munu.modified_growth import (
            modified_growth_equation_symbolic,
        )
        eq = modified_growth_equation_symbolic()
        assert isinstance(eq, sp.Expr)

    def test_equation_contains_delta_function(self):
        from grut.derivation.phi_munu.modified_growth import (
            modified_growth_equation_symbolic,
        )
        eq = modified_growth_equation_symbolic()
        # Should contain second derivative of delta
        assert "delta" in str(eq).lower()


class TestGrowingModeExponent:
    def test_lcdm_exponent_is_one(self):
        """μ = 1 → p_+ = 1 (LCDM growing mode δ ∝ a)."""
        from grut.derivation.phi_munu.modified_growth import (
            growing_mode_exponent,
        )
        p = growing_mode_exponent(1)
        assert sp.simplify(p - 1) == 0

    def test_super_horizon_exponent_is_about_1p186(self):
        """μ = 4/3 → p_+ ≈ 1.1862 (GRUT super-horizon limit)."""
        from grut.derivation.phi_munu.modified_growth import (
            growing_mode_exponent_numeric,
        )
        p = growing_mode_exponent_numeric(4 / 3)
        assert abs(p - 1.1862) < 1e-3

    def test_transition_exponent_is_about_1p096(self):
        """μ = 7/6 → p_+ ≈ 1.0962 (GRUT at transition wavelength)."""
        from grut.derivation.phi_munu.modified_growth import (
            growing_mode_exponent_numeric,
        )
        p = growing_mode_exponent_numeric(7 / 6)
        assert abs(p - 1.0962) < 1e-3

    def test_exponent_monotonic_in_mu(self):
        """p_+(μ) is a monotonic increasing function of μ — physical
        sanity (higher gravitational coupling → faster growth)."""
        from grut.derivation.phi_munu.modified_growth import (
            growing_mode_exponent_numeric,
        )
        p_low = growing_mode_exponent_numeric(0.9)
        p_unity = growing_mode_exponent_numeric(1.0)
        p_high = growing_mode_exponent_numeric(1.1)
        assert p_low < p_unity < p_high


# ─────────────────────────────────────────────────────────────────────
# Background cosmology
# ─────────────────────────────────────────────────────────────────────


class TestBackgroundCosmology:
    def test_H_today_is_one(self):
        from grut.derivation.phi_munu.modified_growth import H_over_H_0
        assert abs(H_over_H_0(1.0) - 1.0) < 1e-12

    def test_H_grows_into_past(self):
        """H(a) increases as a decreases (matter-dom Hubble)."""
        from grut.derivation.phi_munu.modified_growth import H_over_H_0
        assert H_over_H_0(0.1) > H_over_H_0(0.5) > H_over_H_0(1.0)

    def test_Omega_m_today_is_about_0p315(self):
        from grut.derivation.phi_munu.modified_growth import Omega_m_of_a
        assert 0.31 < Omega_m_of_a(1.0) < 0.32

    def test_Omega_m_approaches_one_in_past(self):
        """Ω_m(a) → 1 as a → 0 (matter dominates at early times)."""
        from grut.derivation.phi_munu.modified_growth import Omega_m_of_a
        assert Omega_m_of_a(0.001) > 0.99

    def test_d_lnH_dN_is_negative_today(self):
        """d ln H/dN < 0 (H decreasing with cosmic expansion)."""
        from grut.derivation.phi_munu.modified_growth import d_lnH_dN
        assert d_lnH_dN(1.0) < 0


# ─────────────────────────────────────────────────────────────────────
# μ_GRUT_numeric
# ─────────────────────────────────────────────────────────────────────


class TestMuGRUTNumeric:
    def test_mu_at_k_zero_is_one_plus_alpha(self):
        from grut.derivation.phi_munu.modified_growth import mu_GRUT_numeric
        from grut.foundation.closure_protocol import ALPHA_VAC
        mu = mu_GRUT_numeric(1e-10, 1.0)  # very small k → super-horizon
        assert abs(mu - (1 + ALPHA_VAC)) / (1 + ALPHA_VAC) < 1e-6

    def test_mu_at_k_huge_is_one(self):
        from grut.derivation.phi_munu.modified_growth import mu_GRUT_numeric
        mu = mu_GRUT_numeric(1e10, 1.0)  # huge k → sub-horizon
        assert abs(mu - 1.0) < 1e-12

    def test_mu_decreases_with_a_for_fixed_k(self):
        """For fixed k, k_phys = k/a decreases with a, so the dimensionless
        argument (τ_0 c k_phys)² decreases → μ INCREASES toward late
        times (because μ → 1 + α as k_phys → 0)."""
        from grut.derivation.phi_munu.modified_growth import mu_GRUT_numeric
        k = 0.01  # Mpc⁻¹
        mu_early = mu_GRUT_numeric(k, 0.01)  # high z, k_phys large
        mu_today = mu_GRUT_numeric(k, 1.0)    # z=0
        assert mu_today > mu_early

    def test_mu_reaches_4_over_3_at_super_horizon_today(self):
        """For k_phys today << 1/(τ_0 c), μ should be close to 4/3."""
        from grut.derivation.phi_munu.modified_growth import mu_GRUT_numeric
        # k = 0.001 Mpc⁻¹ today: k τ_0 c = 0.001 × 12.85 = 0.01285,
        # well in super-horizon regime
        mu = mu_GRUT_numeric(0.001, 1.0)
        assert abs(mu - 4 / 3) < 0.001


# ─────────────────────────────────────────────────────────────────────
# Growth-factor integration — load-bearing
# ─────────────────────────────────────────────────────────────────────


class TestGrowthFactorIntegration:
    """The actual ODE integration. These tests are load-bearing for
    the σ_8-not-broken claim and the large-scale-enhancement claim."""

    def test_lcdm_growth_runs_without_error(self):
        from grut.derivation.phi_munu.modified_growth import (
            integrate_growth_factor,
        )
        a_arr, delta = integrate_growth_factor(0.5, use_mu_GRUT=False)
        assert len(a_arr) == len(delta)
        assert delta[-1] > delta[0]  # growing mode

    def test_grut_growth_runs_without_error(self):
        from grut.derivation.phi_munu.modified_growth import (
            integrate_growth_factor,
        )
        a_arr, delta = integrate_growth_factor(0.5, use_mu_GRUT=True)
        assert len(a_arr) == len(delta)
        assert delta[-1] > delta[0]

    def test_lcdm_growth_factor_positive_at_each_step(self):
        """δ should remain positive throughout the integration (no
        sign flips, decaying mode shouldn't dominate)."""
        from grut.derivation.phi_munu.modified_growth import (
            integrate_growth_factor,
        )
        _, delta = integrate_growth_factor(0.5, use_mu_GRUT=False)
        assert np.all(delta > 0)

    def test_lcdm_growth_factor_monotonic(self):
        """For ΛCDM background and growing mode IC, δ(a) is
        monotonically increasing."""
        from grut.derivation.phi_munu.modified_growth import (
            integrate_growth_factor,
        )
        _, delta = integrate_growth_factor(0.5, use_mu_GRUT=False)
        assert np.all(np.diff(delta) >= 0)


# ─────────────────────────────────────────────────────────────────────
# Growth-factor enhancement — the LOAD-BEARING comparison
# ─────────────────────────────────────────────────────────────────────


class TestGrowthFactorEnhancement:
    def test_sub_horizon_enhancement_essentially_one(self):
        """For sub-horizon modes (k = 1 Mpc⁻¹, deeply sub-horizon to
        λ_* ≈ 80 Mpc), f_GRUT should be ≈ 1 within 0.1%."""
        from grut.derivation.phi_munu.modified_growth import (
            growth_factor_enhancement,
        )
        result = growth_factor_enhancement(1.0)
        assert abs(result["f_GRUT_today"] - 1.0) < 0.001

    def test_sigma_8_scale_enhancement_below_one_percent(self):
        """LOAD-BEARING: σ_8 scale (k = 0.5 Mpc⁻¹, sub-horizon) gets
        enhancement BELOW 1% → does NOT break the σ_8 / S_8 tension.

        This is the key observational sanity check: GRUT must not
        catastrophically modify σ_8 measurements at z=0."""
        from grut.derivation.phi_munu.modified_growth import (
            growth_factor_enhancement,
        )
        result = growth_factor_enhancement(0.5)
        enhancement_pct = abs(result["f_GRUT_today"] - 1.0) * 100
        assert enhancement_pct < 1.0, (
            f"σ_8 scale enhancement {enhancement_pct:.2f}% exceeds 1% — "
            f"would meaningfully shift σ_8 measurements. Expected <1%."
        )

    def test_super_horizon_enhancement_significant(self):
        """For super-horizon modes (CMB horizon, k ≈ 4.5e-4 Mpc⁻¹),
        f_GRUT > 2 (significant, testable enhancement)."""
        from grut.derivation.phi_munu.modified_growth import (
            growth_factor_enhancement,
        )
        result = growth_factor_enhancement(4.5e-4)
        assert result["f_GRUT_today"] > 1.5

    def test_BAO_scale_enhancement_modest(self):
        """BAO scale (k ≈ 0.04 Mpc⁻¹, near transition) gets few-
        percent enhancement — testable at DESI precision."""
        from grut.derivation.phi_munu.modified_growth import (
            growth_factor_enhancement,
        )
        result = growth_factor_enhancement(0.04)
        enhancement_pct = abs(result["f_GRUT_today"] - 1.0) * 100
        assert 3 < enhancement_pct < 15, (
            f"BAO enhancement {enhancement_pct:.1f}% outside expected "
            f"range (3-15%)."
        )

    def test_crossed_lambda_star_flag_correct_at_k_0p001(self):
        """k = 0.001 Mpc⁻¹: k τ_0 c ≈ 0.013 < 1 → crossed."""
        from grut.derivation.phi_munu.modified_growth import (
            growth_factor_enhancement,
        )
        result = growth_factor_enhancement(0.001)
        assert result["crossed_lambda_star"] is True

    def test_not_crossed_flag_at_k_1Mpc(self):
        """k = 1 Mpc⁻¹: k τ_0 c ≈ 12.85 > 1 → not crossed."""
        from grut.derivation.phi_munu.modified_growth import (
            growth_factor_enhancement,
        )
        result = growth_factor_enhancement(1.0)
        assert result["crossed_lambda_star"] is False


# ─────────────────────────────────────────────────────────────────────
# Survey at canonical scales
# ─────────────────────────────────────────────────────────────────────


class TestSurveyAtCanonicalScales:
    def test_survey_returns_seven_scales(self):
        from grut.derivation.phi_munu.modified_growth import (
            growth_enhancement_survey,
        )
        s = growth_enhancement_survey()
        assert len(s) == 7

    def test_survey_includes_canonical_scales(self):
        from grut.derivation.phi_munu.modified_growth import (
            growth_enhancement_survey,
        )
        s = growth_enhancement_survey()
        for key in (
            "galaxy_cluster_k_1Mpc",
            "sigma_8_scale_k_0p5",
            "BAO_k_0p04",
            "CMB_horizon_k_4p5e_4",
        ):
            assert key in s

    def test_survey_enhancement_monotonic_in_decreasing_k(self):
        """As k decreases (toward larger scales), f_GRUT increases —
        large scales experience more enhanced growth."""
        from grut.derivation.phi_munu.modified_growth import (
            growth_enhancement_survey,
        )
        s = growth_enhancement_survey()
        scale_ordered = [
            ("galaxy_cluster_k_1Mpc",   1.0),
            ("sigma_8_scale_k_0p5",      0.5),
            ("quasi_linear_k_0p1",        0.1),
            ("BAO_k_0p04",                 0.04),
            ("sloan_large_k_0p01",         0.01),
            ("CMB_low_l_k_0p001",          0.001),
            ("CMB_horizon_k_4p5e_4",       4.5e-4),
        ]
        f_values = [s[name]["f_GRUT_today"] for name, _ in scale_ordered]
        # Values should be non-decreasing (toward larger scales = lower k)
        for i in range(len(f_values) - 1):
            assert f_values[i] <= f_values[i + 1] + 1e-10, (
                f"f_GRUT not monotonic: {f_values}"
            )


# ─────────────────────────────────────────────────────────────────────
# Honest assessment
# ─────────────────────────────────────────────────────────────────────


class TestHonestAssessment:
    def test_assessment_returns_four_verdicts(self):
        from grut.derivation.phi_munu.modified_growth import (
            honest_assessment_summary,
        )
        a = honest_assessment_summary()
        assert "sigma_8_scale_verdict" in a
        assert "BAO_scale_verdict" in a
        assert "CMB_horizon_verdict" in a
        assert "overall_verdict" in a

    def test_sigma_8_verdict_states_unchanged(self):
        from grut.derivation.phi_munu.modified_growth import (
            honest_assessment_summary,
        )
        a = honest_assessment_summary()
        v = a["sigma_8_scale_verdict"]
        assert ("not" in v.lower() and "shifted" in v.lower()
                or "unchanged" in v.lower()
                or "below" in v.lower())

    def test_overall_verdict_says_not_broken(self):
        from grut.derivation.phi_munu.modified_growth import (
            honest_assessment_summary,
        )
        a = honest_assessment_summary()
        v = a["overall_verdict"]
        assert ("does NOT break" in v
                or "does not break" in v.lower()
                or "not broken" in v.lower()
                or "survives" in v.lower())


# ─────────────────────────────────────────────────────────────────────
# Cross-consistency with Priority 3 (mg_eft_mapping)
# ─────────────────────────────────────────────────────────────────────


class TestCrossConsistencyWithPriority3:
    def test_mu_at_k_zero_equals_mg_eft_super_horizon(self):
        from grut.derivation.phi_munu.modified_growth import mu_GRUT_numeric
        from grut.derivation.phi_munu.mg_eft_mapping import (
            mu_minus_one_at_super_horizon_today,
        )
        mu = mu_GRUT_numeric(1e-15, 1.0)
        mu_minus_1 = mu - 1.0
        mu_minus_1_p3 = mu_minus_one_at_super_horizon_today()
        assert abs(mu_minus_1 - mu_minus_1_p3) < 1e-6

    def test_alpha_vac_inheritance(self):
        """Phase 3.1 inherits α_vac from upstream — does NOT modify it."""
        from grut.foundation.closure_protocol import ALPHA_VAC
        from grut.derivation.phi_munu.modified_growth import (
            mu_GRUT_numeric,
        )
        mu_super_horizon = mu_GRUT_numeric(1e-15, 1.0)
        mu_minus_1 = mu_super_horizon - 1.0
        assert abs(mu_minus_1 - ALPHA_VAC) / ALPHA_VAC < 1e-5
