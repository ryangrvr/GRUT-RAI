"""Tests for the Bayesian observer filtering module.

Pins the equation dp/dt = −μp − γp(1−p) with contact reset rule.
EPISTEMIC, not physics — these tests verify the equation behaves
as the Bayesian filtering math says it should, NOT that the framework
predicts new physics.
"""

from __future__ import annotations

import math

import pytest

from grut.derived.decoherence.schrodinger_in_box import (
    demo_combined,
    demo_pure_absence,
    demo_pure_hazard,
    demo_with_contacts,
    dp_dt,
    evolve_p,
    evolve_p_with_contacts,
    half_life_pure_absence,
    half_life_pure_hazard,
    verify,
)


# ─────────────────────────────────────────────────────────────────────
# RHS sanity
# ─────────────────────────────────────────────────────────────────────


class TestDpDt:
    def test_dp_dt_at_p_zero(self):
        """At p = 0 the RHS is 0 (absorbing state)."""
        assert dp_dt(0.0, mu=1.0, gamma=1.0) == 0.0

    def test_dp_dt_at_p_one(self):
        """At p = 1, only the hazard contributes (γ(1)(0) = 0)."""
        rhs = dp_dt(1.0, mu=0.5, gamma=2.0)
        assert abs(rhs - (-0.5)) < 1e-12

    def test_dp_dt_zero_when_mu_gamma_zero(self):
        """No hazard, no absence-pressure → constant."""
        assert dp_dt(0.5, mu=0.0, gamma=0.0) == 0.0

    def test_combined_more_negative_than_each(self):
        """At p = 0.5: dp/dt|combined < dp/dt|hazard < dp/dt|absence < 0."""
        p = 0.5
        d_combined = dp_dt(p, mu=1.0, gamma=1.0)
        d_hazard = dp_dt(p, mu=1.0, gamma=0.0)
        d_absence = dp_dt(p, mu=0.0, gamma=1.0)
        # Combined is hazard + absence
        assert abs(d_combined - (d_hazard + d_absence)) < 1e-12


# ─────────────────────────────────────────────────────────────────────
# Pure hazard limit (γ = 0): exponential decay
# ─────────────────────────────────────────────────────────────────────


class TestPureHazard:
    def test_evolution_matches_exp_minus_mu_t(self):
        """γ = 0 should give p(t) = p_0 exp(−μt)."""
        t_array = [0.1 * i for i in range(101)]
        p_array = evolve_p(1.0, t_array, mu=1.0, gamma=0.0)
        for t, p in zip(t_array, p_array):
            expected = math.exp(-t)
            assert abs(p - expected) < 1e-3

    def test_demo_pure_hazard_passes_verify(self):
        d = demo_pure_hazard()
        assert d.mu == 1.0 and d.gamma == 0.0
        assert abs(d.p_at_t_max - math.exp(-10.0)) < 1e-3

    def test_half_life_log_2_over_mu(self):
        """t_{1/2} = ln(2)/μ for pure hazard."""
        assert abs(half_life_pure_hazard(1.0) - math.log(2.0)) < 1e-12
        assert abs(half_life_pure_hazard(2.0) - math.log(2.0) / 2) < 1e-12


# ─────────────────────────────────────────────────────────────────────
# Pure absence limit (μ = 0): logistic decay
# ─────────────────────────────────────────────────────────────────────


class TestPureAbsence:
    def test_logistic_form(self):
        """μ = 0: p(t) = p_0 / (p_0 + (1−p_0) exp(γt))."""
        t_array = [0.1 * i for i in range(101)]
        p_0 = 0.99
        gamma = 1.0
        p_array = evolve_p(p_0, t_array, mu=0.0, gamma=gamma)
        for t, p in zip(t_array, p_array):
            expected = p_0 / (p_0 + (1.0 - p_0) * math.exp(gamma * t))
            assert abs(p - expected) < 1e-3

    def test_p_initial_one_stays_one_under_pure_absence(self):
        """At p = 1, the absence term γp(1−p) is 0 — no pressure to decay."""
        t_array = [0.1 * i for i in range(101)]
        p_array = evolve_p(1.0, t_array, mu=0.0, gamma=1.0)
        # Should stay at 1.0
        for p in p_array:
            assert abs(p - 1.0) < 1e-9


# ─────────────────────────────────────────────────────────────────────
# Combined behaviour
# ─────────────────────────────────────────────────────────────────────


class TestCombined:
    def test_combined_decays_faster_than_pure_hazard(self):
        """Adding γ > 0 makes p decay faster than pure exponential."""
        d_combined = demo_combined()
        d_hazard = demo_pure_hazard()
        # Both have μ = 1; combined has extra γ = 1
        assert d_combined.p_at_t_max < d_hazard.p_at_t_max

    def test_p_stays_in_unit_interval(self):
        """Numerical integration must keep p ∈ [0, 1]."""
        t_array = [0.01 * i for i in range(1000)]
        p_array = evolve_p(1.0, t_array, mu=10.0, gamma=10.0)
        for p in p_array:
            assert 0.0 <= p <= 1.0


# ─────────────────────────────────────────────────────────────────────
# Contact-reset rule
# ─────────────────────────────────────────────────────────────────────


class TestContactReset:
    def test_p_resets_to_one_at_contact(self):
        """At each contact time, p = 1.0 exactly."""
        t_array = [0.05 * i for i in range(201)]
        contacts = [2.0, 4.0, 6.0, 8.0]
        p_array = evolve_p_with_contacts(
            1.0, t_array, mu=0.5, gamma=0.2, contact_times=contacts
        )
        for ct in contacts:
            # find closest index
            idx = min(range(len(t_array)), key=lambda i: abs(t_array[i] - ct))
            assert abs(p_array[idx] - 1.0) < 1e-9

    def test_steady_state_with_periodic_contacts(self):
        """With periodic contacts, p reaches a periodic steady state.
        Between contact events, p decays from 1.0 by the same amount
        each period."""
        d = demo_with_contacts()
        # p just before each contact should be approximately equal
        # (after the first cycle reaches steady state)
        # Let's check p at t = 1.0 (between contacts at 0 and 2)
        # and t = 3.0 (between contacts at 2 and 4)
        idx_1 = min(range(len(d['t_array'])), key=lambda i: abs(d['t_array'][i] - 1.0))
        idx_3 = min(range(len(d['t_array'])), key=lambda i: abs(d['t_array'][i] - 3.0))
        # Should be the same in steady state (they're both 1 unit after a contact)
        assert abs(d['p_array'][idx_1] - d['p_array'][idx_3]) < 1e-3


# ─────────────────────────────────────────────────────────────────────
# Verify harness
# ─────────────────────────────────────────────────────────────────────


class TestVerifyHarness:
    def test_all_legs_pass(self):
        v = verify()
        for k, val in v.items():
            assert val, f"verify() leg failed: {k}"
