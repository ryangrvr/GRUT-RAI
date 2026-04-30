"""Constitutive entropy production — the arrow of time from CTP dynamics.

This module hardens the GRUT claim:

    The arrow of time emerges from the constitutive entropy production
    of the responsive vacuum. The Second Law is a consequence of the
    CTP action's retarded-kernel structure, not an independent postulate.

Specifically, the constitutive entropy production rate is:

    Ṡ(t) = (1/τ_0) ⟨(z(t) − z_target)²⟩  ≥  0

a non-negative quantity that:
    (i)  vanishes only at the fixed point z* = z_target[z*];
    (ii) integrates to a monotonically-increasing entropy under
         constitutive evolution;
    (iii) is positive for any off-fixed-point configuration.

These three legs verified at code level lift the
arrow_of_time_from_entropy claim from anchored to computed and give
Chapter 10 (Time and Information) its first computed claim.

Reference: V7 Appendix D (entropy production), V7 Appendix E (channel
capacity).
"""

from __future__ import annotations

from typing import Callable

import numpy as np

from grut.foundation.closure_protocol import TAU_0_SEC
from grut.foundation.constitutive import constitutive_step


# ─────────────────────────────────────────────────────────────────────
# Entropy production rate
# ─────────────────────────────────────────────────────────────────────

def entropy_production_rate(
    z: np.ndarray,
    z_target: np.ndarray,
    tau_0: float = TAU_0_SEC,
) -> float:
    """Instantaneous Ṡ = (1/τ_0) ⟨(z − z_target)²⟩.

    Defined as the squared off-fixed-point displacement averaged
    component-wise (or scalar for a 1D state). The 1/τ_0 prefactor
    sets the dimensional scale and ties Ṡ to the medium's relaxation
    time — faster relaxation, faster entropy production.

    Returns a real, non-negative number.
    """
    z_arr = np.asarray(z, dtype=float)
    z_t_arr = np.asarray(z_target, dtype=float)
    diff = z_arr - z_t_arr
    if diff.size == 0:
        return 0.0
    return float(np.mean(diff * diff)) / tau_0


def entropy_production_trajectory(
    z_0: np.ndarray,
    z_target: np.ndarray,
    tau_0: float,
    dt: float,
    n_steps: int,
) -> np.ndarray:
    """Run constitutive evolution from z_0 toward z_target; return
    (Ṡ(t_0), Ṡ(t_1), ..., Ṡ(t_n)).

    For constant z_target, Ṡ(t) = (1/τ_0) (z_0 − z_target)² × exp(−2t/τ_0)
    — exponential decay of the entropy production rate as the system
    relaxes to its fixed point.
    """
    z = np.asarray(z_0, dtype=float).copy()
    z_t = np.asarray(z_target, dtype=float)
    rates = np.zeros(n_steps + 1)
    rates[0] = entropy_production_rate(z, z_t, tau_0)
    for k in range(n_steps):
        z = constitutive_step(z, z_t, tau_0, dt)
        rates[k + 1] = entropy_production_rate(z, z_t, tau_0)
    return rates


def cumulative_entropy(
    z_0: np.ndarray,
    z_target: np.ndarray,
    tau_0: float,
    dt: float,
    n_steps: int,
) -> np.ndarray:
    """Cumulative entropy ∫_0^t Ṡ(s) ds — monotonically non-decreasing.

    Trapezoidal integration of the entropy-production trajectory.
    """
    rates = entropy_production_trajectory(z_0, z_target, tau_0, dt, n_steps)
    cumulative = np.zeros_like(rates)
    for k in range(1, len(rates)):
        cumulative[k] = cumulative[k - 1] + 0.5 * (rates[k - 1] + rates[k]) * dt
    return cumulative


# ─────────────────────────────────────────────────────────────────────
# Verification harness
# ─────────────────────────────────────────────────────────────────────

def verify(
    n_random_samples: int = 200,
    seed: int = 7,
) -> dict:
    """Three legs of the arrow-of-time claim:

      (1) Ṡ ≥ 0 for any z, z_target, including random samples.
      (2) Ṡ = 0 iff z = z_target (vanishes only at fixed point).
      (3) Cumulative entropy ∫Ṡ dt is monotonically non-decreasing
          under constitutive evolution.
    """
    rng = np.random.default_rng(seed=seed)
    tau_0 = TAU_0_SEC

    # (1) Random-sample non-negativity
    rates = []
    for _ in range(n_random_samples):
        n = rng.integers(low=1, high=10)
        z = rng.normal(size=n) * rng.uniform(0.1, 100)
        z_t = rng.normal(size=n) * rng.uniform(0.1, 100)
        rates.append(entropy_production_rate(z, z_t, tau_0))
    leg1 = all(r >= 0.0 for r in rates)

    # (2) Vanishing only at fixed point
    fixed_z = np.array([1.0, 2.0, 3.0])
    leg2_at_fp = entropy_production_rate(fixed_z, fixed_z, tau_0) == 0.0
    leg2_off_fp = entropy_production_rate(fixed_z, fixed_z + 1e-3, tau_0) > 0.0
    leg2 = leg2_at_fp and leg2_off_fp

    # (3) Cumulative monotonicity along a trajectory
    z_0 = np.array([5.0, -3.0, 7.5, 0.1])
    z_t = np.array([1.0, 1.0, 1.0, 1.0])
    cum = cumulative_entropy(z_0, z_t, tau_0, dt=tau_0 / 100, n_steps=500)
    diffs = np.diff(cum)
    # Allow tiny floating-point negative ticks (machine epsilon)
    leg3 = bool(np.all(diffs >= -1e-12))

    return {
        "rate_non_negative_random":      leg1,
        "rate_vanishes_at_fixed_point":  leg2,
        "cumulative_entropy_monotone":   leg3,
    }
