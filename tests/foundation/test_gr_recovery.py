"""Tests for grut.foundation.gr_recovery — promotes gr_recovery
from anchored to computed by verifying the four legs of GR recovery
on the susceptibility / refractive-index structure of the responsive
vacuum.
"""

import math

import numpy as np
import pytest

from grut.foundation.closure_protocol import ALPHA_VAC, TAU_0_SEC
from grut.foundation.gr_recovery import (
    alpha_eff_high_frequency_decay,
    bianchi_consistent,
    bianchi_residual_plane_wave,
    chi_magnitude,
    chi_uv_falloff_exponent,
    gr_potential_pure,
    gr_residual,
    newtonian_potential_constitutive,
    verify,
)


class TestHighFrequencyLimit:
    """Constitutive correction vanishes as ωτ_0 → ∞."""

    def test_alpha_eff_vanishes_at_solar_system(self):
        """Saturn-orbit frequency: ωτ_0 ≈ 10⁷, α_eff ≈ 4 × 10⁻¹⁵."""
        omega_saturn = 2 * math.pi / (30 * 365 * 86400)  # 30-yr period
        a = alpha_eff_high_frequency_decay(omega_saturn)
        assert a < 1e-14

    def test_alpha_eff_below_lab_sensitivity(self):
        """At 1 Hz: ωτ_0 ~ 10¹⁵, α_eff ~ 10⁻³¹."""
        a = alpha_eff_high_frequency_decay(1.0)
        assert a < 1e-30

    def test_gr_residual_to_zero_at_high_freq(self):
        assert gr_residual(1e10) < 1e-30

    def test_constitutive_potential_to_GR_at_high_freq(self):
        """Φ_const(ω→∞) → Φ_GR exactly."""
        M = 1.989e30  # solar mass
        r = 1.496e11  # 1 AU
        omega = 1e10  # high frequency
        phi_c = newtonian_potential_constitutive(M, r, omega)
        phi_gr = gr_potential_pure(M, r)
        assert abs(phi_c - phi_gr) / abs(phi_gr) < 1e-15


class TestLowFrequencyLimit:
    """Full DC enhancement at ωτ_0 → 0."""

    def test_alpha_eff_to_alpha_vac_at_DC(self):
        """ωτ_0 → 0: α_eff → α_vac = 1/3."""
        a = alpha_eff_high_frequency_decay(1e-25)
        assert abs(a - ALPHA_VAC) / ALPHA_VAC < 1e-9

    def test_constitutive_potential_4_thirds_at_DC(self):
        """Φ_const(ω→0) → (4/3) × Φ_GR."""
        M = 1.989e30
        r = 1.496e11
        omega = 1e-25  # deep DC
        phi_c = newtonian_potential_constitutive(M, r, omega)
        phi_gr = gr_potential_pure(M, r)
        assert abs(phi_c / phi_gr - 4.0 / 3.0) < 1e-9


class TestBianchiPreservation:
    """∂_μ Φ^μν = 0 ⇔ ∂_μ T^μν = 0 — single-mode constitutive projection."""

    def test_bianchi_residual_zero_grid(self):
        omega_grid = np.array([1e-20, 1e-15, 1e-10, 1e-5, 1.0, 1e5])
        k_grid = np.array([1e-10, 1.0, 1e10])
        assert bianchi_consistent(omega_grid, k_grid)

    def test_bianchi_residual_zero_at_random_modes(self):
        rng = np.random.default_rng(seed=2024)
        for _ in range(20):
            omega = 10 ** rng.uniform(-20, 10)
            k = 10 ** rng.uniform(-15, 15)
            r = bianchi_residual_plane_wave(omega, k)
            assert r < 1e-15


class TestGravitonUV:
    """χ(ω) ~ 1/ω at large ω — UV falloff exponent = -1."""

    def test_chi_falloff_exponent_minus_one(self):
        e = chi_uv_falloff_exponent()
        assert abs(e - (-1.0)) < 0.01

    def test_chi_magnitude_decays_at_high_omega(self):
        a = chi_magnitude(1.0)
        b = chi_magnitude(1e5)
        assert b < a

    def test_chi_magnitude_at_DC_equals_alpha(self):
        """|χ(0)| = α."""
        c = chi_magnitude(0.0)
        assert abs(c - ALPHA_VAC) < 1e-12


class TestVerifyHarness:

    def test_all_pass(self):
        checks = verify()
        failed = [k for k, v in checks.items() if not v]
        assert not failed, f"GR-recovery failures: {failed}"
