"""Tests for grut.foundation.qm_recovery — promotion of qm_recovery
from anchored to computed.

Verifies that the constitutive equation in the τ → 0 limit reproduces
the Schrödinger evolution on a concrete example (precessing qubit
with H = (ℏω/2) σ_z, initial state |+⟩).
"""

import numpy as np
import pytest

from grut.foundation.qm_recovery import (
    IDENTITY,
    SIGMA_X, SIGMA_Y, SIGMA_Z,
    analytic_qubit_precession,
    evolve_constitutive_qm,
    expectation_sigma_x,
    schrodinger_z_target,
    verify,
)
from grut.foundation.constants import HBAR


class TestPauliSetup:
    """Pauli matrices satisfy the standard algebra."""

    def test_sigma_x_squared_is_identity(self):
        assert np.allclose(SIGMA_X @ SIGMA_X, IDENTITY)

    def test_sigma_y_squared_is_identity(self):
        assert np.allclose(SIGMA_Y @ SIGMA_Y, IDENTITY)

    def test_sigma_z_squared_is_identity(self):
        assert np.allclose(SIGMA_Z @ SIGMA_Z, IDENTITY)

    def test_anticommutator_x_y_zero(self):
        assert np.allclose(SIGMA_X @ SIGMA_Y + SIGMA_Y @ SIGMA_X,
                            np.zeros((2, 2)))

    def test_commutator_x_y_is_2i_z(self):
        assert np.allclose(
            SIGMA_X @ SIGMA_Y - SIGMA_Y @ SIGMA_X,
            2j * SIGMA_Z,
        )


class TestSchrodingerZTarget:
    """z_target = (I − i dt H/ℏ) ψ — first-order Euler step."""

    def test_zero_dt_returns_psi(self):
        psi = np.array([1.0, 0.0], dtype=complex)
        H = HBAR * SIGMA_Z
        out = schrodinger_z_target(psi, H, dt=0.0)
        assert np.allclose(out, psi)

    def test_first_order_in_dt(self):
        """ψ - z_target = (i dt/ℏ) H ψ scales linearly in dt."""
        psi = np.array([1.0, 1.0], dtype=complex) / np.sqrt(2.0)
        H = HBAR * SIGMA_Z
        d1 = psi - schrodinger_z_target(psi, H, dt=1e-4)
        d2 = psi - schrodinger_z_target(psi, H, dt=2e-4)
        assert np.allclose(d2, 2 * d1, atol=1e-12)


class TestTauZeroLimit:
    """In τ → 0, constitutive evolution becomes the Schrödinger Euler step."""

    def test_one_step_matches_z_target(self):
        psi_0 = np.array([1.0, 0.0], dtype=complex)
        H = 0.5 * HBAR * SIGMA_X
        dt = 1e-3
        traj = evolve_constitutive_qm(psi_0, H, dt, n_steps=1, tau=1e-30)
        expected = schrodinger_z_target(psi_0, H, dt)
        assert np.allclose(traj[1], expected, atol=1e-12)

    def test_multistep_matches_iterated_first_order(self):
        psi_0 = np.array([1.0, 1.0], dtype=complex) / np.sqrt(2.0)
        H = 0.5 * HBAR * 1.0 * SIGMA_Z
        dt = 1e-4
        n = 50
        # Direct iteration of the first-order Schrödinger step
        psi = psi_0.copy()
        for _ in range(n):
            psi = schrodinger_z_target(psi, H, dt)
        constitutive_traj = evolve_constitutive_qm(
            psi_0, H, dt, n_steps=n, tau=1e-30,
        )
        assert np.allclose(constitutive_traj[-1], psi, atol=1e-12)


class TestNormPreservation:
    """⟨ψ|ψ⟩ stays close to 1 under iteration (first-order in dt)."""

    def test_norm_preserved_to_first_order(self):
        omega = 1.0
        period = 2 * np.pi / omega
        dt = period / 1000
        n = 2000
        psi_0 = np.array([1.0, 1.0], dtype=complex) / np.sqrt(2.0)
        H = 0.5 * HBAR * omega * SIGMA_Z
        traj = evolve_constitutive_qm(psi_0, H, dt, n_steps=n, tau=1e-30)
        norms = np.array([
            float(np.real(np.conjugate(p) @ p)) for p in traj
        ])
        # First-order Euler accumulates O(n × dt²) error in norm
        bound = n * dt * dt
        assert np.max(np.abs(norms - 1.0)) < bound * 5


class TestSigmaXPrecession:
    """⟨σ_x(t)⟩ = cos(ωt) for |+⟩ under H = (ℏω/2) σ_z."""

    def test_sigma_x_matches_analytic(self):
        omega = 1.0
        period = 2 * np.pi / omega
        dt_over_period = 1e-3
        dt = period * dt_over_period
        n = int(2 / dt_over_period)
        psi_0 = np.array([1.0, 1.0], dtype=complex) / np.sqrt(2.0)
        H = 0.5 * HBAR * omega * SIGMA_Z
        traj = evolve_constitutive_qm(psi_0, H, dt, n_steps=n, tau=1e-30)
        t = np.arange(n + 1) * dt
        sx_num = expectation_sigma_x(traj)
        sx_ana = np.cos(omega * t)
        # First-order tolerance: max error ~ O(dt × n_periods)
        max_err = np.max(np.abs(sx_num - sx_ana))
        assert max_err < 0.05  # 5% tolerance for first-order Euler

    def test_analytic_qubit_precession_at_t_zero_is_plus(self):
        """At t = 0, |ψ⟩ = |+⟩ = (|0⟩ + |1⟩) / √2."""
        traj = analytic_qubit_precession(omega=1.0, t=np.array([0.0]))
        plus = np.array([1.0, 1.0]) / np.sqrt(2.0)
        assert np.allclose(traj[0], plus)


class TestVerifyHarness:
    """The full verify() reports all three legs passing."""

    def test_verify_all_pass(self):
        checks = verify()
        failed = [k for k, v in checks.items() if not v]
        assert not failed, f"QM-recovery failures: {failed}"

    def test_verify_returns_three_legs(self):
        checks = verify()
        expected = {
            "tau_zero_step_matches_z_target",
            "norm_preserved_to_first_order",
            "sigma_x_matches_analytic",
        }
        assert expected.issubset(checks.keys())
