"""Tests for grut/beta_q_sensitivity.py — β_Q Sensitivity Analysis.

Covers:
  TestConstants               — BETA_Q_CANON, EPSILON_Q, PSI_PROXY, OMEGA_0
  TestAssumption              — status, derivation chain, coincidence not justified
  TestSensitivityPoints       — R_eq invariant; omega_0 scales as sqrt(beta_q); psi_proxy shifts
  TestBlastRadius             — invariant/sensitive/conditional classification
  TestVerdict                 — computed from Booleans
  TestNonclaims               — no false claims about locked results
  TestMasterAudit             — end-to-end run_beta_q_sensitivity()
  TestCrossConsistency        — R_eq independent; coincidence breaks at beta_q != 2
"""

from __future__ import annotations

import math
import pytest

from grut.beta_q_sensitivity import (
    BETA_Q_CANON,
    ALPHA_VAC,
    EPSILON_Q_CANON,
    R_EQ_OVER_RS,
    TAU_SQ_CANON,
    OMEGA_0_SQ_CANON,
    OMEGA_0_CANON,
    PSI_PROXY_CANON,
    COINCIDENCE_GAP_CANON,
    KAPPA_RATIO_LOCKED,
    T_KILLING_RATIO_LOCKED,
    A_CRIT_LOCKED,
    FIRST_LAW_GAP_LOCKED,
    build_assumption,
    build_sensitivity_sweep,
    build_blast_radius,
    assign_verdict,
    run_beta_q_sensitivity,
    _compute_sensitivity_point,
)


class TestConstants:
    def test_beta_q_canon(self):
        assert abs(BETA_Q_CANON - 2.0) < 1e-10

    def test_alpha_vac(self):
        assert abs(ALPHA_VAC - 1.0 / 3.0) < 1e-10

    def test_epsilon_q_canon(self):
        """ε_Q = α_vac^β_Q = (1/3)^2 = 1/9"""
        expected = ALPHA_VAC ** BETA_Q_CANON
        assert abs(EPSILON_Q_CANON - expected) < 1e-10
        assert abs(EPSILON_Q_CANON - 1.0 / 9.0) < 1e-10

    def test_r_eq_over_rs(self):
        """R_eq/r_s = α_vac = 1/3 (self-consistent)."""
        assert abs(R_EQ_OVER_RS - ALPHA_VAC) < 1e-10

    def test_psi_proxy_canon(self):
        """Ψ_proxy = 1/(1+β_Q) = 1/3 at β_Q = 2."""
        expected = 1.0 / (1.0 + BETA_Q_CANON)
        assert abs(PSI_PROXY_CANON - expected) < 1e-10
        assert abs(PSI_PROXY_CANON - ALPHA_VAC) < 1e-10

    def test_coincidence_gap_canon(self):
        """Gap = α_vac − Ψ_proxy = 0 at β_Q = 2 (exact coincidence)."""
        assert abs(COINCIDENCE_GAP_CANON) < 1e-10

    def test_omega_0_sq_canon(self):
        """ω₀² = β_Q · GM/R_eq³ = 2 × 0.5 / (1/3)³ = 1/(1/27) = 27.0"""
        M = 0.5
        R = R_EQ_OVER_RS * 1.0   # r_s = 1.0
        expected = BETA_Q_CANON * M / (R ** 3)
        assert abs(OMEGA_0_SQ_CANON - expected) < 1e-6
        assert abs(OMEGA_0_SQ_CANON - 27.0) < 1e-6

    def test_kappa_ratio_locked(self):
        assert abs(KAPPA_RATIO_LOCKED - 3.0 / 5.0) < 1e-10

    def test_t_killing_ratio_locked(self):
        assert abs(T_KILLING_RATIO_LOCKED - 3.0 / 5.0) < 1e-10

    def test_a_crit_locked(self):
        expected = math.sqrt(1.0 + 2.0 / (5.0 * math.pi))
        assert abs(A_CRIT_LOCKED - expected) < 1e-10


class TestAssumption:
    def setup_method(self):
        self.a = build_assumption()

    def test_value(self):
        assert abs(self.a.value - 2.0) < 1e-10

    def test_status_is_working_hypothesis(self):
        assert "working_hypothesis" in self.a.status

    def test_status_not_derived(self):
        assert "not_derived" in self.a.status or "not derived" in self.a.status.lower() or "coincidence" in self.a.status

    def test_derivation_chain_nonempty(self):
        assert len(self.a.derivation_chain) > 50

    def test_derivation_chain_mentions_psi_proxy(self):
        assert "Psi_proxy" in self.a.derivation_chain or "Ψ_proxy" in self.a.derivation_chain or "psi" in self.a.derivation_chain.lower()

    def test_blocking_gap_nonempty(self):
        assert len(self.a.blocking_gap) > 30

    def test_blocking_gap_mentions_unestablished(self):
        low = self.a.blocking_gap.lower()
        assert "unestablished" in low or "not derived" in low or "absent" in low

    def test_psi_proxy_coincidence_value(self):
        assert abs(self.a.psi_proxy_coincidence - ALPHA_VAC) < 1e-10

    def test_coincidence_not_justified(self):
        assert self.a.coincidence_justified is False


class TestSensitivityPoints:
    def setup_method(self):
        self.points = build_sensitivity_sweep([1.0, 1.5, 2.0, 2.5, 3.0, 4.0])

    def test_six_points(self):
        assert len(self.points) == 6

    def test_r_eq_invariant_across_all(self):
        """R_eq/r_s = α_vac for all β_Q (under self-consistent ε_Q encoding)."""
        for p in self.points:
            assert abs(p.r_eq_over_rs - ALPHA_VAC) < 1e-10, (
                f"R_eq/r_s = {p.r_eq_over_rs} != α_vac at β_Q = {p.beta_q}"
            )

    def test_epsilon_q_varies(self):
        """ε_Q = α_vac^β_Q changes with β_Q (not invariant)."""
        eps_values = [p.epsilon_q for p in self.points]
        assert len(set(round(e, 8) for e in eps_values)) > 1

    def test_omega_0_scales_as_sqrt_beta_q(self):
        """ω₀ ∝ √β_Q at fixed R_eq."""
        p1 = next(p for p in self.points if abs(p.beta_q - 1.0) < 1e-6)
        p2 = next(p for p in self.points if abs(p.beta_q - 2.0) < 1e-6)
        p4 = next(p for p in self.points if abs(p.beta_q - 4.0) < 1e-6)
        # omega_0 ∝ sqrt(beta_q): omega_0(4)/omega_0(1) = sqrt(4) = 2
        ratio_4_to_1 = p4.omega_0 / p1.omega_0
        assert abs(ratio_4_to_1 - 2.0) < 1e-6
        # omega_0(2)/omega_0(1) = sqrt(2)
        ratio_2_to_1 = p2.omega_0 / p1.omega_0
        assert abs(ratio_2_to_1 - math.sqrt(2.0)) < 1e-6

    def test_psi_proxy_shifts_with_beta_q(self):
        """Ψ_proxy = 1/(1+β_Q) is not invariant."""
        psi_values = [p.psi_proxy for p in self.points]
        assert len(set(round(v, 6) for v in psi_values)) > 1

    def test_psi_proxy_coincidence_only_at_beta_q_2(self):
        for p in self.points:
            if abs(p.beta_q - 2.0) < 1e-6:
                assert p.coincidence_holds, "Coincidence must hold at β_Q = 2"
            else:
                assert not p.coincidence_holds, (
                    f"Coincidence must break at β_Q = {p.beta_q}"
                )

    def test_tau_eff_inversely_proportional_to_omega_0(self):
        """τ_eff = 1/ω₀ at each β_Q."""
        for p in self.points:
            assert abs(p.tau_eff_canon * p.omega_0 - 1.0) < 1e-10

    def test_kappa_and_a_crit_only_at_canon(self):
        """κ_ratio and A_crit are NaN for β_Q ≠ 2 (τ²(β_Q) unknown)."""
        for p in self.points:
            if abs(p.beta_q - BETA_Q_CANON) < 1e-6:
                assert not math.isnan(p.kappa_ratio)
                assert not math.isnan(p.a_crit)
            else:
                assert math.isnan(p.kappa_ratio), (
                    f"kappa_ratio should be NaN at β_Q = {p.beta_q}"
                )
                assert math.isnan(p.a_crit)

    def test_kappa_ratio_at_canon(self):
        p = next(p for p in self.points if abs(p.beta_q - 2.0) < 1e-6)
        assert abs(p.kappa_ratio - KAPPA_RATIO_LOCKED) < 1e-10

    def test_a_crit_at_canon(self):
        p = next(p for p in self.points if abs(p.beta_q - 2.0) < 1e-6)
        assert abs(p.a_crit - A_CRIT_LOCKED) < 1e-8


class TestBlastRadius:
    def setup_method(self):
        self.b = build_blast_radius()

    def test_invariant_list_nonempty(self):
        assert len(self.b.invariant) >= 3

    def test_sensitive_value_list_nonempty(self):
        assert len(self.b.sensitive_value) >= 3

    def test_conditional_list_nonempty(self):
        assert len(self.b.conditional) >= 3

    def test_self_healing_in_invariant(self):
        combined = " ".join(self.b.invariant).lower()
        assert "self-healing" in combined or "self_healing" in combined

    def test_omega_tau_identity_in_invariant(self):
        # Text uses Unicode ω₀ and τ_eff; search for 'tau' and '= 1'
        combined = " ".join(self.b.invariant)
        assert ("tau" in combined.lower() or "τ" in combined) and "1" in combined

    def test_r_eq_in_invariant(self):
        combined = " ".join(self.b.invariant).lower()
        assert "r_eq" in combined or "req" in combined or "r_eq/r_s" in combined

    def test_omega_0_in_sensitive(self):
        # Text uses Unicode ω₀; check for either ASCII or Unicode
        combined = " ".join(self.b.sensitive_value)
        assert "omega_0" in combined.lower() or "ω₀" in combined or "omega" in combined.lower()

    def test_psi_proxy_in_sensitive(self):
        # Text uses Unicode ψ_proxy; check for ψ or Psi or proxy
        combined = " ".join(self.b.sensitive_value)
        assert "psi" in combined.lower() or "ψ" in combined or "proxy" in combined.lower()

    def test_kappa_ratio_in_conditional(self):
        combined = " ".join(self.b.conditional)
        assert "kappa" in combined.lower() or "κ" in combined

    def test_a_crit_in_conditional(self):
        combined = " ".join(self.b.conditional).lower()
        assert "a_crit" in combined or "acrit" in combined or "crit" in combined

    def test_tau_sq_dependency_in_conditional(self):
        # Text uses Unicode τ²; check for τ or tau
        combined = " ".join(self.b.conditional)
        assert "tau" in combined.lower() or "τ" in combined


class TestVerdict:
    def setup_method(self):
        self.r = run_beta_q_sensitivity()

    def test_verdict_computed(self):
        assert len(self.r.verdict) > 20

    def test_verdict_not_full_closure(self):
        assert "full_closure" not in self.r.verdict

    def test_verdict_mentions_assumed(self):
        assert "assumed" in self.r.verdict.lower()

    def test_verdict_mentions_psi_proxy(self):
        assert "Psi_proxy" in self.r.verdict or "psi" in self.r.verdict.lower()

    def test_verdict_mentions_r_eq_invariant(self):
        assert "R_eq_invariant" in self.r.verdict or "invariant" in self.r.verdict


class TestNonclaims:
    def setup_method(self):
        self.r = run_beta_q_sensitivity()

    def test_nonclaims_nonempty(self):
        assert len(self.r.nonclaims) >= 4

    def test_not_claiming_beta_q_wrong(self):
        combined = " ".join(self.r.nonclaims).lower()
        assert "not claiming" in combined and "wrong" in combined

    def test_not_claiming_kappa_ratio_incorrect(self):
        combined = " ".join(self.r.nonclaims).lower()
        assert "kappa" in combined or "κ" in combined or "ratio" in combined

    def test_nan_explanation_in_nonclaims(self):
        combined = " ".join(self.r.nonclaims).lower()
        assert "nan" in combined or "missing" in combined or "unknown" in combined


class TestMasterAudit:
    def setup_method(self):
        self.r = run_beta_q_sensitivity()

    def test_beta_q_canon(self):
        assert abs(self.r.beta_q_canon - 2.0) < 1e-10

    def test_r_eq_independent_of_beta_q(self):
        assert self.r.r_eq_independent_of_beta_q is True

    def test_omega_0_scales_as_sqrt(self):
        assert self.r.omega_0_scales_as_sqrt_beta_q is True

    def test_psi_proxy_coincidence_breaks(self):
        assert self.r.psi_proxy_coincidence_breaks is True

    def test_coincidence_not_justified(self):
        assert self.r.assumption.coincidence_justified is False

    def test_verdict_nonempty(self):
        assert len(self.r.verdict) > 20

    def test_diagnostics_epsilon_q(self):
        assert abs(self.r.diagnostics["EPSILON_Q_CANON"] - 1.0 / 9.0) < 1e-10

    def test_diagnostics_psi_proxy(self):
        assert abs(self.r.diagnostics["PSI_PROXY_CANON"] - ALPHA_VAC) < 1e-10

    def test_diagnostics_coincidence_gap_zero(self):
        assert abs(self.r.diagnostics["COINCIDENCE_GAP_CANON"]) < 1e-10

    def test_diagnostics_kappa_ratio_locked(self):
        assert abs(self.r.diagnostics["KAPPA_RATIO_LOCKED"] - 3.0 / 5.0) < 1e-10

    def test_diagnostics_r_eq_invariant(self):
        assert self.r.diagnostics["r_eq_invariant_across_sweep"] is True

    def test_diagnostics_coincidence_breaks(self):
        assert self.r.diagnostics["psi_proxy_coincidence_breaks_for_beta_q_ne_2"] is True


class TestCrossConsistency:
    def test_r_eq_invariant_all_test_values(self):
        """R_eq/r_s = α_vac for all β_Q under self-consistent ε_Q encoding."""
        for beta in [0.5, 1.0, 1.5, 2.0, 3.0, 5.0]:
            p = _compute_sensitivity_point(beta)
            assert abs(p.r_eq_over_rs - ALPHA_VAC) < 1e-10, (
                f"R_eq/r_s = {p.r_eq_over_rs} != α_vac at β_Q = {beta}"
            )

    def test_coincidence_exactly_at_beta_q_2(self):
        p = _compute_sensitivity_point(2.0)
        assert abs(p.coincidence_gap) < 1e-10
        assert p.coincidence_holds

    def test_coincidence_breaks_monotonically(self):
        """Gap increases as β_Q moves away from 2."""
        p1 = _compute_sensitivity_point(1.5)
        p2 = _compute_sensitivity_point(2.0)
        p3 = _compute_sensitivity_point(2.5)
        assert abs(p1.coincidence_gap) > abs(p2.coincidence_gap)
        assert abs(p3.coincidence_gap) > abs(p2.coincidence_gap)

    def test_psi_proxy_monotone_in_beta_q(self):
        """Ψ_proxy = 1/(1+β_Q) is strictly decreasing in β_Q."""
        betas = [1.0, 1.5, 2.0, 2.5, 3.0]
        points = [_compute_sensitivity_point(b) for b in betas]
        psis = [p.psi_proxy for p in points]
        for i in range(len(psis) - 1):
            assert psis[i] > psis[i + 1], "Ψ_proxy must decrease with β_Q"

    def test_omega_0_monotone_in_beta_q(self):
        """ω₀ = sqrt(β_Q · GM/R_eq³) is strictly increasing in β_Q (at fixed R_eq)."""
        betas = [1.0, 1.5, 2.0, 2.5, 3.0]
        points = [_compute_sensitivity_point(b) for b in betas]
        omegas = [p.omega_0 for p in points]
        for i in range(len(omegas) - 1):
            assert omegas[i] < omegas[i + 1], "ω₀ must increase with β_Q"

    def test_tau_eff_monotone_decreasing_in_beta_q(self):
        """τ_eff = 1/ω₀ decreases as β_Q increases."""
        betas = [1.0, 2.0, 4.0]
        points = [_compute_sensitivity_point(b) for b in betas]
        taus = [p.tau_eff_canon for p in points]
        for i in range(len(taus) - 1):
            assert taus[i] > taus[i + 1], "τ_eff must decrease with β_Q"

    def test_nan_propagation_for_non_canon_beta_q(self):
        """κ_ratio and A_crit are NaN for all β_Q != 2."""
        import math
        for beta in [1.0, 1.5, 2.5, 3.0]:
            p = _compute_sensitivity_point(beta)
            assert math.isnan(p.kappa_ratio)
            assert math.isnan(p.a_crit)

    def test_epsilon_q_scales_as_power(self):
        """ε_Q = α_vac^β_Q scales correctly."""
        for beta in [1.0, 2.0, 3.0, 4.0]:
            p = _compute_sensitivity_point(beta)
            expected = ALPHA_VAC ** beta
            assert abs(p.epsilon_q - expected) < 1e-12
