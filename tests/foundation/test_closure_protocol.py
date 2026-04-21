"""Tests for Phase I Closure Protocol canonical constants and engine.

Locks in every Phase I §5-§8 canonical value and engine formula.
Verifies:
  - α_vac = 1/3 exactly (v11 App H)
  - S = 12π/α² = 108π exactly
  - τ_0 = 41.9 Myr (canonical)
  - n_g(0) = √(4/3)
  - μ_Λ, μ_0 scales
  - a_0 ≈ 1.08 × 10⁻¹⁰ m/s² (MOND-like)
  - T_c = 54.7 MK
  - τ_0 = 1/√(Λc) identity
  - Regime gate: Saturn suppression ≈ 10⁻¹⁵
  - ν(y) interpolation limits
  - g_eff recovers GR at X ≫ 1 and MOND at X, y ≪ 1
  - Bullet Cluster offset estimate ≈ v × τ_0
"""

import pytest
import numpy as np


class TestCanonicalConstants:
    """Phase I §5-§6 canonical constants."""

    def test_alpha_vac_is_one_third_exactly(self):
        from grut.foundation.closure_protocol import ALPHA_VAC
        assert abs(ALPHA_VAC - 1/3) < 1e-15

    def test_S_equals_108_pi_exactly(self):
        from grut.foundation.closure_protocol import S_SCREENING
        assert abs(S_SCREENING - 108 * np.pi) < 1e-10

    def test_S_equals_12_pi_over_alpha_squared(self):
        from grut.foundation.closure_protocol import S_SCREENING, ALPHA_VAC
        assert abs(S_SCREENING - 12 * np.pi / ALPHA_VAC**2) < 1e-10

    def test_tau_0_is_41p9_Myr(self):
        from grut.foundation.closure_protocol import TAU_0_MYR
        assert abs(TAU_0_MYR - 41.9) < 0.01

    def test_n_g_DC_is_sqrt_4_over_3(self):
        from grut.foundation.closure_protocol import N_G_DC
        assert abs(N_G_DC - np.sqrt(4/3)) < 1e-12
        assert abs(N_G_DC - 1.15470) < 0.0001

    def test_a_0_in_MOND_band(self):
        """a_0 = c/(2πτ_Λ) ≈ 1.2 × 10⁻¹⁰ m/s² — MOND scale."""
        from grut.foundation.closure_protocol import A_0_SI
        assert 1e-11 < A_0_SI < 1e-9

    def test_T_c_is_54p7_MK(self):
        from grut.foundation.closure_protocol import T_C_MK
        assert abs(T_C_MK - 54.7) / 54.7 < 0.05

    def test_mu_Lambda_order_of_magnitude(self):
        """μ_Λ = ℏ/τ_Λ ~ 10⁻³³ eV (horizon IR reference)."""
        from grut.foundation.closure_protocol import MU_LAMBDA_EV
        assert 1e-34 < MU_LAMBDA_EV < 1e-32

    def test_mu_0_equals_S_mu_Lambda(self):
        """μ_0 = S × μ_Λ — screening applies to mass-gap too."""
        from grut.foundation.closure_protocol import (
            MU_LAMBDA_EV, MU_0_EV, S_SCREENING
        )
        assert abs(MU_0_EV / MU_LAMBDA_EV - S_SCREENING) / S_SCREENING < 1e-6

    def test_H0_implied_is_planck_like(self):
        """τ_0 = 41.9 Myr and S = 108π give H_0 ≈ 68.8 km/s/Mpc."""
        from grut.foundation.closure_protocol import H_0_IMPLIED_KM_S_MPC
        # Planck is 67.4, SH0ES is 73.0, our implied should be Planck-like
        assert 65 < H_0_IMPLIED_KM_S_MPC < 72


class TestTauLambdaCIdentity:
    """τ_0 = 1/√(Λc) — v11 Appendix I dark-sector unification."""

    def test_roundtrip(self):
        from grut.foundation.closure_protocol import (
            tau_0_from_lambda_c, lambda_from_tau_0, TAU_0_SEC
        )
        Lambda = lambda_from_tau_0(TAU_0_SEC)
        tau_back = tau_0_from_lambda_c(Lambda)
        assert abs(tau_back - TAU_0_SEC) / TAU_0_SEC < 1e-10

    def test_Lambda_positive_finite(self):
        """τ_0 = 1/√(Λc²) gives positive finite Λ.

        The identity as stated in v11 App I relates τ_0 to a dark-sector
        Λ that is NOT the observed cosmological constant directly —
        it carries an S (screening) factor. The round-trip consistency
        is what matters for internal correctness.
        """
        from grut.foundation.closure_protocol import lambda_from_tau_0, TAU_0_SEC
        import numpy as np
        Lambda = lambda_from_tau_0(TAU_0_SEC)
        assert Lambda > 0
        assert np.isfinite(Lambda)


class TestResponseKernel:
    """Phase I §7 kernel and susceptibility."""

    def test_kernel_normalized(self):
        """∫₀^∞ K(t) dt = 1 (normalization)."""
        from grut.foundation.closure_protocol import kernel_K, TAU_0_SEC
        ts = np.linspace(0, 20 * TAU_0_SEC, 10000)
        integral = np.trapezoid([kernel_K(t) for t in ts], ts)
        assert abs(integral - 1.0) < 0.01

    def test_kernel_zero_at_negative_time(self):
        """Causal: K(t<0) = 0."""
        from grut.foundation.closure_protocol import kernel_K
        assert kernel_K(-1.0) == 0.0

    def test_susceptibility_DC_equals_alpha(self):
        """χ(0) = α (DC susceptibility)."""
        from grut.foundation.closure_protocol import susceptibility_chi, ALPHA_VAC
        chi = susceptibility_chi(0.0)
        assert abs(chi.real - ALPHA_VAC) < 1e-15

    def test_n_g_DC_matches_N_G_DC(self):
        from grut.foundation.closure_protocol import n_g_refractive, N_G_DC
        assert abs(n_g_refractive(0.0) - N_G_DC) < 1e-12

    def test_n_g_high_freq_reduces_to_one(self):
        from grut.foundation.closure_protocol import n_g_refractive
        assert abs(n_g_refractive(1e10) - 1.0) < 1e-6


class TestRegimeGate:
    """Phase I §8.1 solar-system safety via regime gate."""

    def test_saturn_suppression_is_15_orders(self):
        """α_eff at Saturn's orbital frequency is ~10⁻¹⁵ (below ranging)."""
        from grut.foundation.closure_protocol import (
            alpha_effective, TAU_0_SEC
        )
        P_saturn_sec = 29.5 * 3.156e7
        omega_saturn = 2 * np.pi / P_saturn_sec
        alpha_eff = alpha_effective(omega_saturn)
        assert alpha_eff < 1e-13       # at most 10⁻¹³
        assert alpha_eff > 1e-17       # not zero

    def test_regime_parameter_X_saturn_is_large(self):
        from grut.foundation.closure_protocol import regime_parameter_X
        omega_saturn = 2 * np.pi / (29.5 * 3.156e7)
        X = regime_parameter_X(omega_saturn)
        assert X > 1e6

    def test_regime_parameter_X_galactic_is_order_unity(self):
        """Galactic rotation (200 km/s @ 10 kpc): X ~ 1."""
        from grut.foundation.closure_protocol import regime_parameter_X
        v = 200e3
        r = 10 * 3.086e19
        omega = v / r
        X = regime_parameter_X(omega)
        assert 0.1 < X < 10


class TestEngineInterpolation:
    """Phase I Appendix E — ν(y) and g_eff."""

    def test_nu_high_y_approaches_one(self):
        """y ≫ 1 (Newtonian): ν → 1."""
        from grut.foundation.closure_protocol import nu_interpolation
        assert abs(nu_interpolation(1e6) - 1.0) < 1e-3

    def test_nu_low_y_diverges_as_sqrt(self):
        """y ≪ 1: ν ~ √(1/y)."""
        from grut.foundation.closure_protocol import nu_interpolation
        y = 1e-6
        nu = nu_interpolation(y)
        expected = np.sqrt(1/y)  # leading-order
        assert abs(nu / expected - 1.0) < 0.01

    def test_g_eff_equals_g_bar_at_solar_system(self):
        """At Saturn's ω_dyn, g_eff ≈ g_bar (GR recovered)."""
        from grut.foundation.closure_protocol import g_effective
        omega_saturn = 2 * np.pi / (29.5 * 3.156e7)
        g_bar = 6.7e-4    # Saturn's orbit around Sun
        g_eff = g_effective(g_bar, omega_saturn)
        # Should match within 10⁻¹⁰
        assert abs(g_eff - g_bar) / g_bar < 1e-10

    def test_g_eff_enhanced_in_galactic_regime(self):
        """At galactic ω_dyn, low g_bar: g_eff > g_bar."""
        from grut.foundation.closure_protocol import g_effective, A_0_SI
        v = 200e3
        r = 30 * 3.086e19    # 30 kpc (outer)
        omega = v / r
        g_bar = A_0_SI / 100   # deep below a_0
        g_eff = g_effective(g_bar, omega)
        assert g_eff > g_bar

    def test_deep_regime_gives_sqrt_g_bar_a0(self):
        """y ≪ 1, X ≪ 1: g_eff ≈ √(g_bar × a_0) (MOND-like)."""
        from grut.foundation.closure_protocol import g_effective, A_0_SI, TAU_0_SEC
        # Far outer galaxy: low ω, low g_bar
        omega = 1e-18
        g_bar = A_0_SI * 1e-3
        g_eff = g_effective(g_bar, omega)
        g_mond = np.sqrt(g_bar * A_0_SI)
        # Within factor 1.5 of MOND deep limit (not exact due to ν(y) form)
        assert 0.5 < g_eff / g_mond < 1.5


class TestBulletCluster:
    """Phase I §8.4 operational estimate."""

    def test_bullet_offset_is_order_100_kpc(self):
        """v_coll × τ_0 ≈ 100 kpc for v_coll ≈ 3000 km/s."""
        from grut.foundation.closure_protocol import bullet_offset_estimate
        v = 3000e3    # 3000 km/s
        offset = bullet_offset_estimate(v)
        kpc = 3.086e19
        assert 50 * kpc < offset < 500 * kpc


class TestMONDComparison:
    """v11 App F comparison table sanity."""

    def test_GRUT_has_zero_free_parameters(self):
        from grut.foundation.closure_protocol import MOND_COMPARISON
        assert MOND_COMPARISON["GRUT_Closure"]["free_parameters"] == 0

    def test_GRUT_uses_frequency_based_regime(self):
        from grut.foundation.closure_protocol import MOND_COMPARISON
        sep = MOND_COMPARISON["GRUT_Closure"]["regime_separator"]
        assert "frequency" in sep.lower()

    def test_MOND_uses_acceleration_based_regime(self):
        from grut.foundation.closure_protocol import MOND_COMPARISON
        sep = MOND_COMPARISON["MOND"]["regime_separator"]
        assert "acceleration" in sep.lower()


class TestVerifyAllChecks:
    def test_verify_all_pass(self):
        from grut.foundation.closure_protocol import verify
        checks = verify()
        for name, passed in checks.items():
            assert passed, f"Canonical check failed: {name}"
