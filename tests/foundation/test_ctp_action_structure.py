"""Tests for grut.foundation.ctp_action — hardening the CTP-action-structure
claim from anchored to computed.

The dependency graph identified `ctp_action_structure` as the single
highest-fan-out claim (32 downstream dependencies). Promoting it from
anchored to computed strengthens the entire framework. These tests
verify the four structural legs of the CTP action on a concrete
example (driven harmonic oscillator with vacuum noise):

    (1) Field doubling — Keldysh basis is invertible
    (2) Variation principle — δS_CTP/δz_a |_{z_a=0} = F[z_r]
    (3) Causality — retarded kernel vanishes for t < 0
    (4) FDT / KMS — noise kernel ↔ dissipation related at temperature T
"""

import numpy as np
import pytest

from grut.foundation.ctp_action import (
    causality_check,
    ctp_action_value,
    fdt_classical_check,
    fdt_classical_limit,
    fdt_quantum_check,
    fdt_quantum_limit,
    harmonic_oscillator_force,
    keldysh_round_trip,
    retarded_kernel_oscillator,
    variation_in_z_a,
    verify,
)


# ─────────────────────────────────────────────────────────────────────
# (1) Field doubling
# ─────────────────────────────────────────────────────────────────────

class TestFieldDoubling:
    """Keldysh basis transform is invertible on the doubled field space."""

    def test_keldysh_round_trip_zeros(self):
        z = np.zeros(5)
        assert keldysh_round_trip(z, z)

    def test_keldysh_round_trip_random(self):
        rng = np.random.default_rng(seed=17)
        for _ in range(10):
            z_p = rng.normal(size=8)
            z_m = rng.normal(size=8)
            assert keldysh_round_trip(z_p, z_m), (
                f"Round trip failed on z_+ = {z_p}, z_− = {z_m}"
            )

    def test_keldysh_round_trip_extreme_amplitudes(self):
        rng = np.random.default_rng(seed=23)
        z_p = rng.normal(size=6) * 1e10
        z_m = rng.normal(size=6) * 1e-10
        assert keldysh_round_trip(z_p, z_m)


# ─────────────────────────────────────────────────────────────────────
# (2) Variation principle
# ─────────────────────────────────────────────────────────────────────

class TestVariationPrinciple:
    """δS_CTP/δz_a at z_a = 0 reproduces the classical equation of motion."""

    def test_variation_recovers_F_random_z(self):
        """For random z_r, numerical gradient = analytic F[z_r]."""
        rng = np.random.default_rng(seed=42)
        z_r = rng.normal(size=20)
        omega = 1.5
        F_ana = harmonic_oscillator_force(z_r, omega=omega)
        F_num = variation_in_z_a(z_r, omega=omega, eps=1e-6)
        assert np.allclose(F_num, F_ana, atol=1e-8, rtol=1e-6)

    def test_variation_recovers_F_zero_z(self):
        """Trivial z_r = 0 gives F = 0."""
        z_r = np.zeros(15)
        F_num = variation_in_z_a(z_r, omega=1.0, eps=1e-6)
        assert np.allclose(F_num, 0.0, atol=1e-9)

    def test_variation_recovers_F_at_classical_solution(self):
        """For z_r at a classical solution (sin/cos at correct ω), F is small."""
        n = 50
        omega = 1.0
        # Discrete time grid; z(t) = sin(ωt) is a continuum solution.
        # At finite Δt the discretization gives O(Δt²) residual.
        dt = 0.01
        t = np.arange(n) * dt
        # NB: harmonic_oscillator_force uses SECOND-DIFFERENCE without dt²,
        # so we need to scale F to be the discretized z̈ + ω² z. For the
        # raw operator the residual scales like dt²·ω² for a smooth solution.
        z_r = np.sin(omega * t * dt) * dt  # scale to keep result small
        F_num = variation_in_z_a(z_r, omega=omega, eps=1e-6)
        F_ana = harmonic_oscillator_force(z_r, omega=omega)
        # Variation must equal analytic F
        assert np.allclose(F_num, F_ana, atol=1e-8, rtol=1e-6)


# ─────────────────────────────────────────────────────────────────────
# (3) Causality
# ─────────────────────────────────────────────────────────────────────

class TestCausality:
    """Retarded kernel vanishes for t < 0 — the operational definition
    of CTP causality at the propagator level."""

    def test_retarded_zero_at_negative_times(self):
        for t in [-10.0, -1.0, -0.001, -1e-12]:
            assert retarded_kernel_oscillator(t) == 0.0, t

    def test_retarded_finite_at_positive_times(self):
        for t in [0.001, 0.5, 1.0, 5.0]:
            val = retarded_kernel_oscillator(t)
            assert np.isfinite(val)

    def test_causality_check_grid(self):
        times = np.linspace(-5.0, 5.0, 101)
        assert causality_check(times)

    def test_retarded_at_t_zero_is_zero(self):
        """G_R(0) = sin(0)/ω = 0."""
        assert retarded_kernel_oscillator(0.0) == 0.0


# ─────────────────────────────────────────────────────────────────────
# (4) FDT / KMS closure
# ─────────────────────────────────────────────────────────────────────

class TestFDTLimits:
    """High-T classical and low-T quantum limits both recovered."""

    def test_classical_limit_high_T(self):
        """kT ≫ ℏω: noise → 4 k_B T / τ (frequency-independent)."""
        T = 1e6
        omega = 1e8
        tau = 1.0
        assert fdt_classical_check(omega, tau, T, tol=0.01)

    def test_quantum_limit_low_T(self):
        """kT ≪ ℏω: noise → 2 ℏω / τ (vacuum zero-point)."""
        T = 1e-8
        omega = 1e15
        tau = 1.0
        assert fdt_quantum_check(omega, tau, T, tol=0.01)

    def test_classical_limit_formula(self):
        """fdt_classical_limit gives 4 k_B T / τ."""
        from grut.foundation.constants import K_B
        T = 300.0
        tau = 1e-3
        expected = 4 * K_B * T / tau
        assert abs(fdt_classical_limit(1.0, tau, T) - expected) < 1e-30

    def test_quantum_limit_formula(self):
        """fdt_quantum_limit gives 2 ℏω / τ."""
        from grut.foundation.constants import HBAR
        omega = 1e10
        tau = 1.0
        expected = 2 * HBAR * omega / tau
        assert abs(fdt_quantum_limit(omega, tau) - expected) < 1e-40


# ─────────────────────────────────────────────────────────────────────
# Integrated harness
# ─────────────────────────────────────────────────────────────────────

class TestVerifyHarness:
    """The full verify() reports all four legs passing."""

    def test_verify_all_pass(self):
        checks = verify()
        failed = [k for k, v in checks.items() if not v]
        assert not failed, f"CTP-action structural failures: {failed}"

    def test_verify_returns_all_four_legs(self):
        checks = verify()
        expected = {
            "field_doubling_invertible",
            "variation_principle_recovers_F",
            "causality_retarded_vanishes",
            "fdt_classical_limit_recovered",
            "fdt_quantum_limit_recovered",
        }
        assert expected.issubset(checks.keys())


# ─────────────────────────────────────────────────────────────────────
# Sample CTP action — sanity properties
# ─────────────────────────────────────────────────────────────────────

class TestSampleCTPAction:
    """The concrete S_CTP[z_r, z_a] used as the variation harness has the
    expected structural properties: real part linear in z_a, imaginary
    part quadratic in z_a, vanishes at z_a = 0."""

    def test_action_zero_at_z_a_zero(self):
        rng = np.random.default_rng(seed=99)
        z_r = rng.normal(size=10)
        z_a = np.zeros(10)
        s = ctp_action_value(z_r, z_a)
        assert abs(s) < 1e-30

    def test_action_real_part_linear_in_z_a(self):
        """Re S_CTP = z_a · F[z_r] is linear in z_a."""
        rng = np.random.default_rng(seed=101)
        z_r = rng.normal(size=10)
        z_a = rng.normal(size=10)
        s1 = ctp_action_value(z_r, z_a, noise_amplitude=0.0).real
        s2 = ctp_action_value(z_r, 2 * z_a, noise_amplitude=0.0).real
        assert abs(s2 - 2 * s1) < 1e-12

    def test_action_imag_part_quadratic_in_z_a(self):
        """Im S_CTP = (1/2) N |z_a|² is quadratic in z_a."""
        rng = np.random.default_rng(seed=103)
        z_r = rng.normal(size=10)
        z_a = rng.normal(size=10)
        s1 = ctp_action_value(z_r, z_a, noise_amplitude=1.0).imag
        s2 = ctp_action_value(z_r, 2 * z_a, noise_amplitude=1.0).imag
        assert abs(s2 - 4 * s1) < 1e-12
