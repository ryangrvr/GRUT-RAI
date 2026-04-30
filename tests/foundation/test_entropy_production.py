"""Tests for grut.foundation.entropy_production — promotion of
arrow_of_time_from_entropy from anchored to computed.

Three legs:
  (1) Ṡ ≥ 0 always (random sampling)
  (2) Ṡ vanishes only at the fixed point z = z_target
  (3) Cumulative entropy is monotonically non-decreasing under
      constitutive evolution.

These give Chapter 10 (Time and Information) its first computed claim.
"""

import numpy as np
import pytest

from grut.foundation.closure_protocol import TAU_0_SEC
from grut.foundation.entropy_production import (
    cumulative_entropy,
    entropy_production_rate,
    entropy_production_trajectory,
    verify,
)


class TestNonNegativity:
    """Ṡ = (1/τ_0)⟨(z − z_target)²⟩ ≥ 0 for any z, z_target."""

    def test_zero_at_equality(self):
        z = np.array([1.0, 2.0, 3.0])
        rate = entropy_production_rate(z, z, TAU_0_SEC)
        assert rate == 0.0

    def test_positive_off_fixed_point(self):
        z = np.array([1.0, 2.0])
        z_t = np.array([1.5, 2.5])
        rate = entropy_production_rate(z, z_t, TAU_0_SEC)
        assert rate > 0.0

    def test_random_samples_non_negative(self):
        rng = np.random.default_rng(seed=1)
        for _ in range(500):
            n = rng.integers(low=1, high=20)
            z = rng.normal(size=n) * rng.uniform(0.01, 1000)
            z_t = rng.normal(size=n) * rng.uniform(0.01, 1000)
            r = entropy_production_rate(z, z_t, TAU_0_SEC)
            assert r >= 0.0

    def test_scales_inversely_with_tau(self):
        """Doubling τ_0 halves Ṡ for fixed displacement."""
        z = np.array([0.0])
        z_t = np.array([1.0])
        r1 = entropy_production_rate(z, z_t, TAU_0_SEC)
        r2 = entropy_production_rate(z, z_t, 2 * TAU_0_SEC)
        assert abs(r2 - r1 / 2) / r1 < 1e-12


class TestFixedPointVanishing:
    """Ṡ = 0 ⟺ z = z_target (component-wise)."""

    def test_exact_zero_at_fixed_point(self):
        for v in [np.array([0.0]), np.array([1.0, 2.0, 3.0]),
                   np.zeros(10), np.ones(5) * np.pi]:
            assert entropy_production_rate(v, v, TAU_0_SEC) == 0.0

    def test_nonzero_off_fixed_point(self):
        z = np.array([1.0, 2.0, 3.0])
        for delta in [1e-10, 1e-5, 1.0, 1e3]:
            z_t = z + delta
            assert entropy_production_rate(z, z_t, TAU_0_SEC) > 0.0


class TestMonotonicCumulativeEntropy:
    """∫_0^t Ṡ(s) ds is monotonically non-decreasing under
    constitutive evolution."""

    def test_cumulative_starts_at_zero(self):
        z_0 = np.array([5.0])
        z_t = np.array([0.0])
        cum = cumulative_entropy(z_0, z_t, TAU_0_SEC,
                                  dt=TAU_0_SEC / 100, n_steps=10)
        assert cum[0] == 0.0

    def test_cumulative_monotone_simple_relaxation(self):
        z_0 = np.array([10.0])
        z_t = np.array([0.0])
        cum = cumulative_entropy(z_0, z_t, TAU_0_SEC,
                                  dt=TAU_0_SEC / 100, n_steps=500)
        diffs = np.diff(cum)
        assert np.all(diffs >= -1e-12)

    def test_cumulative_monotone_random_starts(self):
        rng = np.random.default_rng(seed=11)
        for _ in range(20):
            z_0 = rng.normal(size=4) * 10
            z_t = rng.normal(size=4)
            cum = cumulative_entropy(z_0, z_t, TAU_0_SEC,
                                      dt=TAU_0_SEC / 50, n_steps=200)
            diffs = np.diff(cum)
            assert np.all(diffs >= -1e-12)


class TestEntropyProductionTrajectory:
    """The rate decays exponentially — Ṡ(t) = (1/τ_0) δ_0² exp(−2t/τ_0)
    for constant z_target."""

    def test_rate_trajectory_is_decreasing(self):
        z_0 = np.array([1.0])
        z_t = np.array([0.0])
        rates = entropy_production_trajectory(
            z_0, z_t, TAU_0_SEC, dt=TAU_0_SEC / 100, n_steps=200,
        )
        # Each rate ≤ the previous one
        diffs = np.diff(rates)
        assert np.all(diffs <= 1e-12)

    def test_rate_starts_at_initial_displacement(self):
        z_0 = np.array([3.0])
        z_t = np.array([0.0])
        rates = entropy_production_trajectory(
            z_0, z_t, TAU_0_SEC, dt=TAU_0_SEC / 1000, n_steps=10,
        )
        expected_initial = (3.0 ** 2) / TAU_0_SEC
        assert abs(rates[0] - expected_initial) < 1e-12


class TestVerifyHarness:
    def test_verify_all_pass(self):
        checks = verify()
        failed = [k for k, v in checks.items() if not v]
        assert not failed, f"Entropy production failures: {failed}"

    def test_verify_returns_three_legs(self):
        checks = verify()
        expected = {
            "rate_non_negative_random",
            "rate_vanishes_at_fixed_point",
            "cumulative_entropy_monotone",
        }
        assert expected.issubset(checks.keys())
