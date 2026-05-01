"""Regression tests for the Phase 2C explicit FRW construction.

Pins the explicit χ_FRW(k, η) and n_g²(k, η) results, the three
limits (sub-horizon, super-horizon, transition), and the inheritance
of α_vac and τ_0 from upstream framework constants.

This is the cosmology backbone: with these tests in place, n_g²(k, η)
is a definite computable function of comoving wavenumber and cosmic
time, and Priority 3 (n_g(ω) covariance) has its structural ingredient
fixed.

Pattern matches tests/derivation/phi_munu/test_curved_background.py
and test_linearized_ctp_action.py.
"""

from __future__ import annotations

import math
from fractions import Fraction

import sympy as sp


# ─────────────────────────────────────────────────────────────────────
# Module imports & verify()
# ─────────────────────────────────────────────────────────────────────


class TestFRWModuleImports:
    def test_module_importable(self):
        from grut.derivation.phi_munu import frw_explicit  # noqa
        assert hasattr(frw_explicit, "verify")

    def test_package_exports_FRW_API(self):
        from grut.derivation.phi_munu import (
            chi_FRW_WKB,
            chi_FRW_WKB_in_physical_wavenumber,
            n_g_squared_FRW_WKB,
            n_g_squared_FRW_in_physical_wavenumber,
            n_g_squared_numeric,
            sub_horizon_limit,
            super_horizon_limit,
            transition_wavenumber,
            transition_wavenumber_today_inverse_meters,
            transition_wavelength_today_Mpc,
            beyond_wkb_correction_magnitude_today,
            frw_verify,
            frw_convention_declaration,
        )
        for fn in (
            chi_FRW_WKB,
            chi_FRW_WKB_in_physical_wavenumber,
            n_g_squared_FRW_WKB,
            n_g_squared_FRW_in_physical_wavenumber,
            n_g_squared_numeric,
            sub_horizon_limit,
            super_horizon_limit,
            transition_wavenumber,
            transition_wavenumber_today_inverse_meters,
            transition_wavelength_today_Mpc,
            beyond_wkb_correction_magnitude_today,
            frw_verify,
            frw_convention_declaration,
        ):
            assert callable(fn)


class TestFRWVerifyHarness:
    def test_frw_verify_all_eight_legs_pass(self):
        from grut.derivation.phi_munu.frw_explicit import verify
        v = verify()
        for k, val in v.items():
            assert val is True, f"FRW verify() leg failed: {k} = {val}"


# ─────────────────────────────────────────────────────────────────────
# Convention declaration (Phase 2C)
# ─────────────────────────────────────────────────────────────────────


class TestFRWConventionDeclaration:
    def test_C1f_FRW_metric_in_conformal_time(self):
        from grut.derivation.phi_munu.frw_explicit import (
            convention_declaration,
        )
        d = convention_declaration()
        c1f = d["C1f_FRW_metric"]
        assert "a²(η)" in c1f or "a^2" in c1f
        assert "conformal time" in c1f.lower()

    def test_C2f_distinguishes_conformal_from_cosmic_hubble(self):
        from grut.derivation.phi_munu.frw_explicit import (
            convention_declaration,
        )
        d = convention_declaration()
        c2f = d["C2f_conformal_hubble"]
        assert "H_c" in c2f or "conformal" in c2f.lower()
        assert "H_c/a" in c2f or "cosmic-time" in c2f.lower()

    def test_C4f_states_WKB_regime(self):
        from grut.derivation.phi_munu.frw_explicit import (
            convention_declaration,
        )
        d = convention_declaration()
        c4f = d["C4f_WKB_slow_H_regime"]
        assert "<<" in c4f or "≪" in c4f
        # The (Hτ_0)² ≈ 8.7e-6 today is documented
        assert ("8.7" in c4f or "1e-6" in c4f or "10⁻⁶" in c4f
                or "10^-6" in c4f or "1/(108π)" in c4f)

    def test_C5f_transition_at_k_phys_tau_0_equals_one(self):
        from grut.derivation.phi_munu.frw_explicit import (
            convention_declaration,
        )
        d = convention_declaration()
        c5f = d["C5f_physical_wavenumber_and_transition"]
        assert "k_phys" in c5f
        assert "1/τ_0" in c5f or "1/tau_0" in c5f.lower()

    def test_C6f_alpha_vac_inherits(self):
        from grut.derivation.phi_munu.frw_explicit import (
            convention_declaration,
        )
        d = convention_declaration()
        c6f = d["C6f_alpha_vac_inherits"]
        assert "1/3" in c6f
        assert "KS 2011" in c6f or "Komargodski-Schwimmer" in c6f or "conformal-mode" in c6f.lower()

    def test_phase_2C_status_marks_WKB_completeness(self):
        from grut.derivation.phi_munu.frw_explicit import (
            convention_declaration,
        )
        d = convention_declaration()
        s = d["phase_2C_status"]
        assert "EXPLICIT" in s or "WKB" in s
        assert "Phase 2D" in s or "deferred" in s.lower()


# ─────────────────────────────────────────────────────────────────────
# Section 1: FRW background
# ─────────────────────────────────────────────────────────────────────


class TestFRWBackgroundMachinery:
    def test_metric_components_have_correct_signs(self):
        from grut.derivation.phi_munu.frw_explicit import (
            conformal_time_FRW_metric, A_OF_ETA,
        )
        m = conformal_time_FRW_metric()
        # g_00 = -a², g_ii = +a² (signature -+++)
        assert sp.simplify(m["g_00"] + A_OF_ETA**2) == 0
        assert sp.simplify(m["g_ii"] - A_OF_ETA**2) == 0

    def test_sqrt_minus_g_is_a_to_the_fourth(self):
        """For FRW conformal-time metric, det(-g) = a^8, so √-g = a⁴."""
        from grut.derivation.phi_munu.frw_explicit import (
            conformal_time_FRW_metric, A_OF_ETA,
        )
        m = conformal_time_FRW_metric()
        assert sp.simplify(m["sqrt_minus_g"] - A_OF_ETA**4) == 0

    def test_inverse_metric_inverts(self):
        from grut.derivation.phi_munu.frw_explicit import (
            conformal_time_FRW_metric,
        )
        m = conformal_time_FRW_metric()
        # g^00 × g_00 = 1
        assert sp.simplify(m["g_inv_00"] * m["g_00"] - 1) == 0
        # g^ii × g_ii = 1
        assert sp.simplify(m["g_inv_ii"] * m["g_ii"] - 1) == 0

    def test_conformal_hubble_is_a_prime_over_a(self):
        from grut.derivation.phi_munu.frw_explicit import (
            conformal_hubble, A_OF_ETA, ETA,
        )
        H_c = conformal_hubble()
        expected = sp.diff(A_OF_ETA, ETA) / A_OF_ETA
        assert sp.simplify(H_c - expected) == 0


# ─────────────────────────────────────────────────────────────────────
# Section 2: □_g on scalar Fourier modes
# ─────────────────────────────────────────────────────────────────────


class TestBoxGOnScalarMode:
    def test_box_g_has_expected_FRW_structure(self):
        """□_g φ_k = -(1/a²)[∂_η² + 2H_c ∂_η + k²] φ_k"""
        from grut.derivation.phi_munu.frw_explicit import (
            box_g_on_scalar_fourier_mode, ETA, A_OF_ETA, K_COMOVING,
        )
        phi_k = sp.Function("phi_k")(ETA)
        result = box_g_on_scalar_fourier_mode(phi_k)
        H_c = sp.diff(A_OF_ETA, ETA) / A_OF_ETA
        expected = -(1 / A_OF_ETA**2) * (
            sp.diff(phi_k, ETA, 2)
            + 2 * H_c * sp.diff(phi_k, ETA)
            + K_COMOVING**2 * phi_k
        )
        assert sp.simplify(result - expected) == 0

    def test_relaxation_operator_form(self):
        """[1 + τ_0² (-□_g)] φ_k = φ_k + (τ_0²/a²) [...] φ_k"""
        from grut.derivation.phi_munu.frw_explicit import (
            relaxation_operator_on_scalar_fourier,
            box_g_on_scalar_fourier_mode,
            ETA,
        )
        from grut.derivation.phi_munu.linearized_ctp_action import TAU_0
        phi_k = sp.Function("phi_k")(ETA)
        result = relaxation_operator_on_scalar_fourier(phi_k)
        expected = phi_k + TAU_0**2 * (-box_g_on_scalar_fourier_mode(phi_k))
        assert sp.simplify(result - expected) == 0


# ─────────────────────────────────────────────────────────────────────
# Section 3: WKB susceptibility (LOAD-BEARING)
# ─────────────────────────────────────────────────────────────────────


class TestWKBSusceptibility:
    """χ_FRW^WKB(k_phys) = 1 / [1 + (τ_0 k_phys)²] — the load-bearing
    explicit formula."""

    def test_chi_has_expected_WKB_form(self):
        from grut.derivation.phi_munu.frw_explicit import (
            chi_FRW_WKB_in_physical_wavenumber, K_PHYS,
        )
        from grut.derivation.phi_munu.linearized_ctp_action import TAU_0
        chi = chi_FRW_WKB_in_physical_wavenumber(K_PHYS, TAU_0)
        expected = 1 / (1 + TAU_0**2 * K_PHYS**2)
        assert sp.simplify(chi - expected) == 0

    def test_chi_at_DC_equals_one(self):
        """k_phys → 0 limit: χ → 1."""
        from grut.derivation.phi_munu.frw_explicit import (
            chi_FRW_WKB_in_physical_wavenumber, K_PHYS,
        )
        from grut.derivation.phi_munu.linearized_ctp_action import TAU_0
        chi = chi_FRW_WKB_in_physical_wavenumber(K_PHYS, TAU_0)
        assert sp.simplify(chi.subs(K_PHYS, 0) - 1) == 0

    def test_chi_at_high_k_vanishes(self):
        """k_phys → ∞ limit: χ → 0 (GR recovery)."""
        from grut.derivation.phi_munu.frw_explicit import (
            chi_FRW_WKB_in_physical_wavenumber, K_PHYS,
        )
        from grut.derivation.phi_munu.linearized_ctp_action import TAU_0
        chi = chi_FRW_WKB_in_physical_wavenumber(K_PHYS, TAU_0)
        assert sp.limit(chi, K_PHYS, sp.oo) == 0

    def test_comoving_form_uses_k_over_a(self):
        """χ_FRW^WKB(k, η) = 1/[1 + (τ_0 k/a(η))²] — comoving form."""
        from grut.derivation.phi_munu.frw_explicit import chi_FRW_WKB
        from grut.derivation.phi_munu.linearized_ctp_action import TAU_0
        eta = sp.Symbol("eta", real=True)
        k = sp.Symbol("k", positive=True)
        chi = chi_FRW_WKB(k, eta, TAU_0)
        # The denominator should contain k/a(η)
        denom = sp.fraction(chi)[1]
        assert "a(eta)" in str(denom) or "a(η)" in str(denom)


# ─────────────────────────────────────────────────────────────────────
# Section 4: n_g²(k_phys)
# ─────────────────────────────────────────────────────────────────────


class TestNgSquaredFRW:
    """n_g²(k_phys) = 1 + α / [1 + (τ_0 k_phys)²]"""

    def test_n_g_squared_form(self):
        from grut.derivation.phi_munu.frw_explicit import (
            n_g_squared_FRW_in_physical_wavenumber, K_PHYS,
        )
        from grut.derivation.phi_munu.linearized_ctp_action import (
            TAU_0, ALPHA,
        )
        n_g_sq = n_g_squared_FRW_in_physical_wavenumber(K_PHYS, TAU_0, ALPHA)
        expected = 1 + ALPHA / (1 + TAU_0**2 * K_PHYS**2)
        assert sp.simplify(n_g_sq - expected) == 0

    def test_n_g_squared_at_DC_is_one_plus_alpha(self):
        """n_g²(0) = 1 + α — same as flat-space DC limit."""
        from grut.derivation.phi_munu.frw_explicit import (
            n_g_squared_FRW_in_physical_wavenumber, K_PHYS,
        )
        from grut.derivation.phi_munu.linearized_ctp_action import (
            TAU_0, ALPHA,
        )
        n_g_sq = n_g_squared_FRW_in_physical_wavenumber(K_PHYS, TAU_0, ALPHA)
        assert sp.simplify(n_g_sq.subs(K_PHYS, 0) - (1 + ALPHA)) == 0

    def test_n_g_squared_at_high_k_is_one(self):
        """n_g²(∞) = 1 — GR recovery on small scales."""
        from grut.derivation.phi_munu.frw_explicit import (
            n_g_squared_FRW_in_physical_wavenumber, K_PHYS,
        )
        from grut.derivation.phi_munu.linearized_ctp_action import (
            TAU_0, ALPHA,
        )
        n_g_sq = n_g_squared_FRW_in_physical_wavenumber(K_PHYS, TAU_0, ALPHA)
        assert sp.limit(n_g_sq, K_PHYS, sp.oo) == 1

    def test_n_g_squared_at_DC_with_alpha_one_third_equals_4_over_3(self):
        from grut.derivation.phi_munu.frw_explicit import (
            n_g_squared_FRW_in_physical_wavenumber, K_PHYS,
        )
        from grut.derivation.phi_munu.linearized_ctp_action import TAU_0, ALPHA
        n_g_sq = n_g_squared_FRW_in_physical_wavenumber(K_PHYS, TAU_0, ALPHA)
        n_g_sq_alpha_third = n_g_sq.subs(ALPHA, sp.Rational(1, 3))
        assert sp.simplify(n_g_sq_alpha_third.subs(K_PHYS, 0) - sp.Rational(4, 3)) == 0


# ─────────────────────────────────────────────────────────────────────
# Section 5: Limits and transition
# ─────────────────────────────────────────────────────────────────────


class TestSubHorizonLimit:
    def test_chi_high_k_is_exactly_zero(self):
        from grut.derivation.phi_munu.frw_explicit import sub_horizon_limit
        s = sub_horizon_limit()
        assert s["chi_FRW_high_k_limit"] == 0

    def test_n_g_squared_high_k_is_exactly_one(self):
        from grut.derivation.phi_munu.frw_explicit import sub_horizon_limit
        s = sub_horizon_limit()
        assert s["n_g_squared_high_k"] == 1

    def test_interpretation_mentions_GR_recovery(self):
        from grut.derivation.phi_munu.frw_explicit import sub_horizon_limit
        s = sub_horizon_limit()
        interp = s["interpretation"]
        assert "GR" in interp or "recovery" in interp.lower()
        assert "small scales" in interp.lower() or "shorter" in interp.lower()


class TestSuperHorizonLimit:
    def test_chi_low_k_is_exactly_one(self):
        from grut.derivation.phi_munu.frw_explicit import super_horizon_limit
        s = super_horizon_limit()
        assert s["chi_FRW_low_k_limit"] == 1

    def test_n_g_squared_low_k_is_one_plus_alpha(self):
        from grut.derivation.phi_munu.frw_explicit import super_horizon_limit
        from grut.derivation.phi_munu.linearized_ctp_action import ALPHA
        s = super_horizon_limit()
        assert sp.simplify(s["n_g_squared_low_k"] - (1 + ALPHA)) == 0

    def test_low_k_with_alpha_one_third_equals_4_over_3(self):
        from grut.derivation.phi_munu.frw_explicit import super_horizon_limit
        from grut.derivation.phi_munu.linearized_ctp_action import ALPHA
        s = super_horizon_limit()
        n_g_sq_at_alpha_third = s["n_g_squared_low_k"].subs(
            ALPHA, sp.Rational(1, 3)
        )
        assert sp.simplify(n_g_sq_at_alpha_third - sp.Rational(4, 3)) == 0


class TestTransitionWavenumber:
    def test_transition_k_phys_is_one_over_tau_0(self):
        from grut.derivation.phi_munu.frw_explicit import transition_wavenumber
        from grut.derivation.phi_munu.linearized_ctp_action import TAU_0
        t = transition_wavenumber()
        assert sp.simplify(t["transition_k_phys"] - 1 / TAU_0) == 0

    def test_chi_at_transition_is_one_half(self):
        from grut.derivation.phi_munu.frw_explicit import transition_wavenumber
        t = transition_wavenumber()
        assert sp.simplify(t["chi_at_transition"]) == sp.Rational(1, 2)

    def test_n_g_squared_at_transition_is_one_plus_alpha_over_two(self):
        from grut.derivation.phi_munu.frw_explicit import transition_wavenumber
        from grut.derivation.phi_munu.linearized_ctp_action import ALPHA
        t = transition_wavenumber()
        expected = 1 + ALPHA / 2
        assert sp.simplify(t["n_g_squared_at_transition"] - expected) == 0

    def test_n_g_squared_at_transition_with_alpha_third_is_seven_sixths(self):
        from grut.derivation.phi_munu.frw_explicit import transition_wavenumber
        from grut.derivation.phi_munu.linearized_ctp_action import ALPHA
        t = transition_wavenumber()
        n_g_sq = t["n_g_squared_at_transition"].subs(ALPHA, sp.Rational(1, 3))
        assert sp.simplify(n_g_sq - sp.Rational(7, 6)) == 0

    def test_comoving_transition_form_includes_a_of_eta(self):
        """Comoving k_*(η) = a(η)/τ_0 — sweeps with cosmic expansion."""
        from grut.derivation.phi_munu.frw_explicit import (
            transition_wavenumber, A_OF_ETA,
        )
        t = transition_wavenumber()
        assert t["transition_comoving_k_form"].has(A_OF_ETA)


# ─────────────────────────────────────────────────────────────────────
# Section 6: Beyond-WKB correction
# ─────────────────────────────────────────────────────────────────────


class TestBeyondWKBCorrection:
    def test_H0_tau_0_equals_one_over_S_screening(self):
        """H_0 × τ_0 = 1/S = 1/(108π) ≈ 2.95e-3 (cosmic-baseline relation)."""
        from grut.derivation.phi_munu.frw_explicit import (
            beyond_wkb_correction_magnitude_today,
        )
        from grut.foundation.closure_protocol import S_SCREENING
        b = beyond_wkb_correction_magnitude_today()
        expected_H_tau = 1.0 / S_SCREENING
        assert abs(b["H_0_times_tau_0"] - expected_H_tau) < 1e-10

    def test_correction_is_squared_quantity(self):
        from grut.derivation.phi_munu.frw_explicit import (
            beyond_wkb_correction_magnitude_today,
        )
        b = beyond_wkb_correction_magnitude_today()
        assert b["(H_0_tau_0)_squared"] == b["H_0_times_tau_0"] ** 2

    def test_correction_is_under_ten_to_the_negative_four(self):
        """The (H_0 τ_0)² ≈ 8.7e-6 correction is well under 10⁻⁴ —
        WKB is excellent for late-universe cosmology."""
        from grut.derivation.phi_munu.frw_explicit import (
            beyond_wkb_correction_magnitude_today,
        )
        b = beyond_wkb_correction_magnitude_today()
        assert b["(H_0_tau_0)_squared"] < 1e-4

    def test_subleading_flag_is_True(self):
        from grut.derivation.phi_munu.frw_explicit import (
            beyond_wkb_correction_magnitude_today,
        )
        b = beyond_wkb_correction_magnitude_today()
        assert b["is_subleading_in_late_universe"] is True


# ─────────────────────────────────────────────────────────────────────
# Numerical evaluation
# ─────────────────────────────────────────────────────────────────────


class TestNumericalEvaluation:
    def test_n_g_squared_numeric_at_DC_is_4_over_3(self):
        """At very low k_phys, n_g² = 1 + 1/3 = 4/3."""
        from grut.derivation.phi_munu.frw_explicit import n_g_squared_numeric
        # k_phys very small → super-horizon → n_g² → 4/3
        result = n_g_squared_numeric(1e-30)
        assert abs(result - 4 / 3) < 1e-6

    def test_n_g_squared_numeric_at_high_k_is_one(self):
        """Sub-horizon: n_g² → 1."""
        from grut.derivation.phi_munu.frw_explicit import n_g_squared_numeric
        # k_phys very large → sub-horizon → n_g² → 1
        result = n_g_squared_numeric(1e30)
        assert abs(result - 1.0) < 1e-12

    def test_n_g_squared_at_galactic_scale_is_close_to_one(self):
        """10-kpc scale is deep sub-horizon (much shorter than τ_0 c)."""
        from grut.derivation.phi_munu.frw_explicit import n_g_squared_numeric
        Mpc = 3.0857e22
        k = 2 * math.pi / (10e-3 * Mpc)
        result = n_g_squared_numeric(k)
        assert abs(result - 1.0) < 1e-8

    def test_n_g_squared_at_CMB_horizon_scale_is_close_to_4_over_3(self):
        """14-Gpc scale is super-horizon — full constitutive."""
        from grut.derivation.phi_munu.frw_explicit import n_g_squared_numeric
        Mpc = 3.0857e22
        k = 2 * math.pi / (14e3 * Mpc)
        result = n_g_squared_numeric(k)
        # Should be close to 4/3
        assert abs(result - 4 / 3) < 0.01

    def test_transition_wavelength_today_is_around_80_Mpc(self):
        """λ_*^today = 2π τ_0 c ≈ 80.7 Mpc."""
        from grut.derivation.phi_munu.frw_explicit import (
            transition_wavelength_today_Mpc,
        )
        result = transition_wavelength_today_Mpc()
        assert 70 < result < 90, f"Expected ~80 Mpc, got {result}"

    def test_transition_wavenumber_today_inverse_of_tau_c(self):
        """k_*^phys = 1/(τ_0 c)."""
        from grut.derivation.phi_munu.frw_explicit import (
            transition_wavenumber_today_inverse_meters,
        )
        from grut.foundation.closure_protocol import TAU_0_SEC
        c = 299792458.0
        result = transition_wavenumber_today_inverse_meters()
        expected = 1.0 / (TAU_0_SEC * c)
        assert abs(result - expected) / expected < 1e-12


# ─────────────────────────────────────────────────────────────────────
# Cross-consistency with linearized and curved-scaffold modules
# ─────────────────────────────────────────────────────────────────────


class TestCrossConsistency:
    def test_alpha_inherits_from_linearized(self):
        from grut.derivation.phi_munu.frw_explicit import (
            n_g_squared_FRW_in_physical_wavenumber, K_PHYS,
        )
        from grut.derivation.phi_munu.linearized_ctp_action import (
            ALPHA, TAU_0,
        )
        n_g_sq = n_g_squared_FRW_in_physical_wavenumber(K_PHYS, TAU_0, ALPHA)
        # The expression must contain ALPHA from linearized module
        assert n_g_sq.has(ALPHA)

    def test_tau_0_inherits_from_linearized(self):
        from grut.derivation.phi_munu.frw_explicit import (
            chi_FRW_WKB_in_physical_wavenumber, K_PHYS,
        )
        from grut.derivation.phi_munu.linearized_ctp_action import TAU_0
        chi = chi_FRW_WKB_in_physical_wavenumber(K_PHYS, TAU_0)
        assert chi.has(TAU_0)

    def test_consistency_with_closure_protocol_TAU_0_SEC(self):
        """Numerical TAU_0_SEC matches the canonical value."""
        from grut.foundation.closure_protocol import TAU_0_SEC
        from grut.derivation.phi_munu.frw_explicit import (
            transition_wavelength_today_Mpc,
        )
        # τ_0 = 41.9 Myr → λ_* = 2π τ_0 c
        c = 299792458.0
        Mpc = 3.0857e22
        expected_lambda_star = 2 * math.pi * TAU_0_SEC * c / Mpc
        actual = transition_wavelength_today_Mpc()
        assert abs(actual - expected_lambda_star) / expected_lambda_star < 1e-6

    def test_alpha_vac_value_one_third_recovers_4_over_3_DC(self):
        from grut.derivation.phi_munu.frw_explicit import (
            n_g_squared_FRW_in_physical_wavenumber, K_PHYS,
        )
        from grut.derivation.phi_munu.linearized_ctp_action import (
            ALPHA, TAU_0, alpha_vac_from_conformal_mode,
        )
        # Assert α_vac structurally is 1/3
        assert alpha_vac_from_conformal_mode() == Fraction(1, 3)
        n_g_sq = n_g_squared_FRW_in_physical_wavenumber(K_PHYS, TAU_0, ALPHA)
        # Substitute α = 1/3 and k = 0:
        n_g_sq_DC = n_g_sq.subs([(ALPHA, sp.Rational(1, 3)), (K_PHYS, 0)])
        assert sp.simplify(n_g_sq_DC - sp.Rational(4, 3)) == 0

    def test_curved_scaffold_FRW_compatibility_marker_consistent(self):
        """The curved scaffold (Phase 2B) marked FRW scalar-mode
        compatibility as the Priority 3 bridge. Phase 2C closes the
        bridge by deriving χ_FRW(k, η) explicitly. The two modules'
        n_g² formulas must be structurally consistent."""
        from grut.derivation.phi_munu.curved_background import (
            frw_scalar_mode_compatibility,
        )
        from grut.derivation.phi_munu.frw_explicit import chi_FRW_WKB
        # The curved scaffold expressed n_g² in operator form (with
        # operator placeholder symbols). The frw_explicit module
        # produces the WKB-leading explicit form. Both have the
        # n_g² = 1 + α χ structure — matched at the FORM level.
        scaffold = frw_scalar_mode_compatibility()
        assert scaffold["is_priority_3_bridge"] is True
        # Phase 2C produces the explicit χ:
        chi = chi_FRW_WKB()
        # χ must reduce to 1 in the k → 0 limit (matches the curved
        # scaffold's super-horizon endpoint)
        from grut.derivation.phi_munu.frw_explicit import K_COMOVING
        chi_at_k_zero = chi.subs(K_COMOVING, 0)
        assert sp.simplify(chi_at_k_zero - 1) == 0
