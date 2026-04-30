"""GRUT — Schrödinger-in-the-Box: Bayesian observer filtering.

The framework's worldview rejects the outside-observer position. The
disciplined inversion of Schrödinger's cat: the OBSERVER is the
boxed system (finite, local, information-limited); the cat continues
evolving outside the observer's information horizon. Observation is
synchronization through contact, not creation through measurement.

This module implements the Bayesian filtering equation governing
how the observer's certainty about the cat's status evolves between
contact events. EPISTEMIC, NOT PHYSICS — the equation captures
information-finite-observer dynamics under the framework's
worldview, but does not produce new physics predictions.

THE FILTERING EQUATION:

    dp/dt = −μp − γp(1−p)

    p(t⁺) = 1  at contact-return events

    where:
      p(t) = observer's probability the cat is alive at time t
      μ = death hazard rate (standard survival decay)
      γ = expected return rate when alive (absence-as-data rate)

The second term −γp(1−p) is the load-bearing piece: if returns are
expected at rate γ when alive, NOT seeing a return is itself
Bayesian evidence the cat may not be alive. Absence becomes data.

Reduces to:
  - Standard exponential survival when γ = 0: dp/dt = −μp
  - Pure absence-Bayesian when μ = 0: dp/dt = −γp(1−p)
  - Constant when μ = γ = 0

DOES NOT:
  - Predict new physics (this is epistemic)
  - Add to the decoherence-plateau falsifier surface (Ch 5)
  - Replace the framework's existing measurement_resolution
    machinery (Ch 11)
  - Resolve any open negative

This module supports the registered claim
`bayesian_observer_filtering` (Ch 11, anchored).
"""

from __future__ import annotations

import math
from dataclasses import dataclass


# ─────────────────────────────────────────────────────────────────────
# The filtering equation
# ─────────────────────────────────────────────────────────────────────


def dp_dt(p: float, mu: float, gamma: float) -> float:
    """RHS of the Bayesian filtering ODE: dp/dt = −μp − γp(1−p).

    Args:
        p: current probability the cat is alive (0 ≤ p ≤ 1)
        mu: death hazard rate (standard survival decay) in 1/time
        gamma: expected return rate when alive (absence-as-data) in 1/time

    Returns: dp/dt at this state.
    """
    return -mu * p - gamma * p * (1.0 - p)


def evolve_p(
    p_initial: float,
    t_array: list[float],
    mu: float,
    gamma: float,
) -> list[float]:
    """Integrate dp/dt = −μp − γp(1−p) over t_array (no contacts).

    Uses analytic solution where possible:
      γ = 0:  p(t) = p_0 exp(−μt)
      μ = 0:  p(t) = p_0/(p_0 + (1−p_0) exp(γt))  [standard logistic decay]

    For general μ, γ uses RK4 numerical integration over the array.
    """
    if not t_array:
        return []
    if not 0.0 <= p_initial <= 1.0:
        raise ValueError(f"p_initial={p_initial} must be in [0, 1]")

    p_values = [p_initial]
    for i in range(1, len(t_array)):
        dt = t_array[i] - t_array[i - 1]
        p = p_values[-1]
        # RK4
        k1 = dp_dt(p, mu, gamma)
        k2 = dp_dt(p + 0.5 * dt * k1, mu, gamma)
        k3 = dp_dt(p + 0.5 * dt * k2, mu, gamma)
        k4 = dp_dt(p + dt * k3, mu, gamma)
        p_new = p + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        p_new = max(0.0, min(1.0, p_new))  # clamp to [0, 1]
        p_values.append(p_new)
    return p_values


def evolve_p_with_contacts(
    p_initial: float,
    t_array: list[float],
    mu: float,
    gamma: float,
    contact_times: list[float],
) -> list[float]:
    """Integrate the filtering equation with contact resets.

    At each t in contact_times, p is reset to 1.0 (cat seen alive).
    Between contacts, p evolves under dp/dt = −μp − γp(1−p).
    """
    if not t_array:
        return []
    p_values = [p_initial]
    contact_set = set(contact_times)
    for i in range(1, len(t_array)):
        t = t_array[i]
        dt = t - t_array[i - 1]
        # Check if this t coincides with a contact (within dt/2)
        contact_here = any(
            abs(t - ct) < 0.5 * dt for ct in contact_times
        )
        if contact_here:
            p_values.append(1.0)
        else:
            p = p_values[-1]
            k1 = dp_dt(p, mu, gamma)
            k2 = dp_dt(p + 0.5 * dt * k1, mu, gamma)
            k3 = dp_dt(p + 0.5 * dt * k2, mu, gamma)
            k4 = dp_dt(p + dt * k3, mu, gamma)
            p_new = p + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
            p_values.append(max(0.0, min(1.0, p_new)))
    return p_values


# ─────────────────────────────────────────────────────────────────────
# Closed-form characteristic times
# ─────────────────────────────────────────────────────────────────────


def half_life_pure_hazard(mu: float) -> float:
    """t_{1/2} when γ = 0: pure exponential decay.

        p(t_{1/2}) = 1/2 = exp(−μ t_{1/2})  →  t_{1/2} = ln(2)/μ
    """
    if mu <= 0:
        return float("inf")
    return math.log(2.0) / mu


def half_life_pure_absence(gamma: float, p_initial: float = 1.0) -> float:
    """t_{1/2} when μ = 0: pure absence-as-data.

    Solving p(t) = p_0 / (p_0 + (1−p_0) exp(γt)) = 1/2 with p_0 = 1
    requires careful limit. For p_0 < 1:
        t_{1/2} = (1/γ) ln(p_0 / (1 − p_0))
    For p_0 = 1: t_{1/2} = ∞ (no absence-pressure with full prior)."""
    if gamma <= 0 or p_initial >= 1.0:
        return float("inf")
    if p_initial <= 0:
        return 0.0
    return math.log(p_initial / (1.0 - p_initial)) / gamma


# ─────────────────────────────────────────────────────────────────────
# Demonstration / verification
# ─────────────────────────────────────────────────────────────────────


@dataclass(frozen=True)
class FilteringDemo:
    name: str
    mu: float
    gamma: float
    p_initial: float
    t_array: tuple[float, ...]
    p_array: tuple[float, ...]
    p_at_t_max: float


def demo_pure_hazard() -> FilteringDemo:
    """γ = 0, μ = 1: pure exponential decay."""
    t_array = [0.1 * i for i in range(101)]
    p_array = evolve_p(1.0, t_array, mu=1.0, gamma=0.0)
    return FilteringDemo(
        name="pure_hazard",
        mu=1.0, gamma=0.0, p_initial=1.0,
        t_array=tuple(t_array), p_array=tuple(p_array),
        p_at_t_max=p_array[-1],
    )


def demo_pure_absence() -> FilteringDemo:
    """μ = 0, γ = 1: pure Bayesian absence-as-data, slight initial doubt."""
    t_array = [0.1 * i for i in range(101)]
    p_array = evolve_p(0.99, t_array, mu=0.0, gamma=1.0)
    return FilteringDemo(
        name="pure_absence",
        mu=0.0, gamma=1.0, p_initial=0.99,
        t_array=tuple(t_array), p_array=tuple(p_array),
        p_at_t_max=p_array[-1],
    )


def demo_combined() -> FilteringDemo:
    """μ = γ = 1: combined hazard + absence."""
    t_array = [0.1 * i for i in range(101)]
    p_array = evolve_p(1.0, t_array, mu=1.0, gamma=1.0)
    return FilteringDemo(
        name="combined",
        mu=1.0, gamma=1.0, p_initial=1.0,
        t_array=tuple(t_array), p_array=tuple(p_array),
        p_at_t_max=p_array[-1],
    )


def demo_with_contacts() -> dict:
    """Periodic contacts every 2 time units, decay rate μ = 0.5, γ = 0.2."""
    t_array = [0.05 * i for i in range(201)]  # 0 to 10 in steps of 0.05
    contact_times = [2.0, 4.0, 6.0, 8.0]
    p_array = evolve_p_with_contacts(
        1.0, t_array, mu=0.5, gamma=0.2, contact_times=contact_times
    )
    return {
        "t_array": tuple(t_array),
        "p_array": tuple(p_array),
        "contact_times": tuple(contact_times),
        "p_at_t_max": p_array[-1],
        "mu": 0.5,
        "gamma": 0.2,
    }


def verify() -> dict:
    """Self-test the filtering equation."""
    pure_hazard = demo_pure_hazard()
    pure_absence = demo_pure_absence()
    combined = demo_combined()

    # Pure hazard at t=10: p = exp(-10) ≈ 4.5e-5
    pure_hazard_correct = abs(pure_hazard.p_at_t_max - math.exp(-10.0)) < 1e-3

    # Pure absence with p_0 = 0.99 at t=10 should be ~ 0.99/(0.99 + 0.01 e^10)
    expected = 0.99 / (0.99 + 0.01 * math.exp(10.0))
    pure_absence_correct = abs(pure_absence.p_at_t_max - expected) < 1e-3

    # Combined decays faster than pure_hazard (more pressure)
    combined_decays_faster = combined.p_at_t_max < pure_hazard.p_at_t_max

    # Half-life formulas
    hl_hazard = half_life_pure_hazard(1.0)
    hl_correct = abs(hl_hazard - math.log(2.0)) < 1e-6

    return {
        "pure_hazard_matches_exp_decay": pure_hazard_correct,
        "pure_absence_matches_logistic": pure_absence_correct,
        "combined_decays_faster_than_hazard_alone": combined_decays_faster,
        "half_life_formula_correct": hl_correct,
    }


if __name__ == "__main__":
    print("Bayesian observer filtering — Schrödinger-in-the-Box")
    print("=" * 60)
    print()
    for k, v in verify().items():
        print(f"  [{('PASS' if v else 'FAIL')}]  {k}")
    print()
    print("Demo with periodic contacts:")
    d = demo_with_contacts()
    print(f"  μ = {d['mu']}, γ = {d['gamma']}, contacts at {d['contact_times']}")
    # Print every 20th sample
    for i in range(0, len(d['t_array']), 20):
        print(f"  t = {d['t_array'][i]:5.2f}  p = {d['p_array'][i]:.4f}")
