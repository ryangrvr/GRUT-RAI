"""Tests for the primordial-amplitude derivation attempt.

Pins the specific honest-negative result: the OU-process variance and
the inflationary-formula substitution both fail by 10+ orders of
magnitude. A dimensional candidate (α/S³) is within factor 4 of
observed A_s, but is flagged as a clue, not promoted to derivation.

These tests pin the result of the attempt — they verify that the
honest-negative numbers are reproducible and that the disciplined
verdict logic distinguishes derivation-tier matches from dimensional
coincidences.
"""

from __future__ import annotations

import math

import pytest

from grut.derived.cosmology.primordial_amplitude import (
    A_S_PLANCK_2018,
    H_INF_HZ,
    H_TAU_FROM_NS,
    M_PLANCK_REDUCED,
    T_PEAK_KELVIN,
    T_CMB_K,
    kms_noise_amplitude,
    ou_variance_h_dimensional,
    path_a_ou_variance,
    path_b_inflationary_formula,
    path_c_dimensional_ratios,
    primordial_amplitude_attempt,
)


# ─────────────────────────────────────────────────────────────────────
# Reference observables and framework constants
# ─────────────────────────────────────────────────────────────────────


class TestReferenceConstants:
    def test_A_s_observed_is_planck_2018(self):
        assert A_S_PLANCK_2018 == 2.1e-9

    def test_T_CMB_today(self):
        assert abs(T_CMB_K - 2.7255) < 1e-3

    def test_T_peak_matches_framework(self):
        # T_peak = ℏ/(τ₀ k_B). With τ₀ = 41.9 Myr, T_peak ≈ 5.78e-27 K —
        # the τ₀-dual temperature ("boiling point of gravity"), extremely
        # cold, well below CMB. This is NOT the 54.7 MK thermal-transition
        # T_c (the τ_micro-dual); the two differ by ~34 orders of magnitude.
        # Single source of truth: tau_hierarchy_decision.T_PEAK_NOISE_KERNEL_K.
        assert 1e-30 < T_PEAK_KELVIN < 1e-23

    def test_H_inf_terminal_velocity_in_correct_range(self):
        # H_inf = (2-R)/(S × τ₀) ≈ 1.88e-18 Hz
        assert 1e-19 < H_INF_HZ < 1e-17


# ─────────────────────────────────────────────────────────────────────
# Path A — OU-process variance
# ─────────────────────────────────────────────────────────────────────


class TestPathAOUVariance:
    def test_runs_without_error(self):
        result = path_a_ou_variance()
        assert "at_T_c" in result
        assert "at_T_CMB" in result

    def test_at_T_CMB_is_far_below_A_s(self):
        """The OU-process variance with Planck rescaling at T = T_CMB
        is roughly 10⁻¹⁹ — about 10¹⁰ smaller than A_s = 2.1×10⁻⁹.
        This pins the honest-negative result."""
        result = path_a_ou_variance()
        v = result["at_T_CMB"]["dimensionless_planck_normed"]
        assert 1e-21 < v < 1e-17, (
            f"OU variance at T_CMB landed at {v:.3e}, outside expected "
            f"range — recompute and verify"
        )
        # Must NOT match A_s within a decade
        ratio = v / A_S_PLANCK_2018
        assert ratio < 0.1 or ratio > 10.0

    def test_at_T_c_is_far_below_A_s(self):
        """At T_c (extremely cold framework temperature), the variance
        is even smaller (the noise spectrum is dominated by zero-point
        fluctuations)."""
        result = path_a_ou_variance()
        v = result["at_T_c"]["dimensionless_planck_normed"]
        assert v < 1e-30, (
            f"OU variance at T_c landed at {v:.3e} — expected « 10⁻⁹"
        )

    def test_kms_noise_amplitude_classical_limit(self):
        """At low ω with high T (k_BT ≫ ℏω): N → 4 k_B T / τ.
        Pin this for a known case."""
        from grut.foundation.constants import K_B
        tau = 1e-15  # 1 fs — very fast
        T = 300.0  # K
        omega = 1e3  # very low compared to k_BT/ℏ
        N = kms_noise_amplitude(omega, tau, T)
        N_classical = 4 * K_B * T / tau
        assert abs(N - N_classical) / N_classical < 1e-3


# ─────────────────────────────────────────────────────────────────────
# Path B — Inflationary-formula substitution
# ─────────────────────────────────────────────────────────────────────


class TestPathBInflationaryFormula:
    def test_runs_without_error(self):
        result = path_b_inflationary_formula()
        assert "A_s_path_b_eps_HinfTau" in result
        assert "A_s_path_b_eps_ns" in result

    def test_path_b_is_astronomically_too_small(self):
        """GRUT has no inflationary epoch — H_inf is the terminal
        velocity (~10⁻⁵² M_Pl), not the inflationary scale (~10⁻⁵
        M_Pl). The naive inflationary-formula substitution gives
        ~10⁻¹¹⁸, which is correctly far below A_s.

        This is a CLEAN HONEST NEGATIVE: the framework as currently
        formulated cannot produce A_s via the standard inflation
        formula because it lacks an inflationary epoch."""
        result = path_b_inflationary_formula()
        # Both ε conventions should give astronomically tiny values
        assert result["A_s_path_b_eps_HinfTau"] < 1e-110
        assert result["A_s_path_b_eps_ns"] < 1e-110

    def test_epsilon_from_n_s_matches_spectral_running_module(self):
        """The slow-roll-analog ε = (Hτ)² with Hτ derived from
        observed n_s = 0.9649 should match what spectral_running.py
        computes."""
        from grut.derived.cosmology.spectral_running import grut_predictions
        sr = grut_predictions()
        x_match = sr["H_tau"]
        assert abs(x_match - H_TAU_FROM_NS) / H_TAU_FROM_NS < 1e-6


# ─────────────────────────────────────────────────────────────────────
# Path C — Dimensional ratios
# ─────────────────────────────────────────────────────────────────────


class TestPathCDimensionalRatios:
    def test_runs_without_error(self):
        result = path_c_dimensional_ratios()
        assert "candidates" in result
        assert "closest_match" in result

    def test_eleven_candidates_tested(self):
        """The disciplined comparison tests 11 dimensional candidates.
        Adding/removing changes the prior probability of one matching
        by chance, so this is pinned."""
        result = path_c_dimensional_ratios()
        assert len(result["candidates"]) == 11

    def test_alpha_over_S_cubed_is_closest_match(self):
        """α/S³ = (1/3) / (108π)³ ≈ 8.53e-9, factor ~4 from observed
        A_s = 2.1e-9. With 11 candidates and log-uniform distribution
        over many decades, finding one match within a decade is
        plausible coincidence, NOT a derivation."""
        result = path_c_dimensional_ratios()
        closest = result["closest_match"]
        assert closest["name"] == "alpha_over_S_cubed"
        # Pin the value at factor 4 from A_s
        assert 3.0 < closest["vs_A_s"] < 5.0

    def test_alpha_over_S_cubed_value(self):
        """Pin the exact α/S³ value: (1/3) / (108π)³."""
        from grut.foundation.closure_protocol import ALPHA_VAC, S_SCREENING
        expected = ALPHA_VAC / S_SCREENING**3
        result = path_c_dimensional_ratios()
        for c in result["candidates"]:
            if c["name"] == "alpha_over_S_cubed":
                assert abs(c["value"] - expected) / expected < 1e-12
                return
        pytest.fail("alpha_over_S_cubed candidate missing from Path C")

    def test_kT_c_over_E_Pl_is_negligible(self):
        """T_c-based ratios are far too small (10⁻⁵⁰+ for the linear
        ratio). Confirms that thermal-scale arguments don't reach A_s."""
        result = path_c_dimensional_ratios()
        for c in result["candidates"]:
            if c["name"] == "kT_c_over_E_Pl":
                assert c["value"] < 1e-50


# ─────────────────────────────────────────────────────────────────────
# Master verdict
# ─────────────────────────────────────────────────────────────────────


class TestMasterVerdict:
    def test_verdict_is_honest_negative_with_clue(self):
        """The disciplined verdict: derivation-tier paths fail; one
        dimensional candidate lands close. This is a clue, not a
        derivation."""
        result = primordial_amplitude_attempt()
        assert result["verdict"] == "HONEST_NEGATIVE_WITH_DIMENSIONAL_CLUE"

    def test_no_derivation_path_matches(self):
        """Path A (OU-process) and Path B (inflationary substitution)
        both fail to produce A_s within a decade. Pinning this is
        the core honest-negative claim."""
        result = primordial_amplitude_attempt()
        assert not result["derivation_path_matches"]

    def test_dimensional_clue_is_alpha_over_S_cubed(self):
        """The closest dimensional candidate is α/S³."""
        result = primordial_amplitude_attempt()
        clues = result["dimensional_candidates_within_decade"]
        assert len(clues) >= 1
        names = {c["name"] for c in clues}
        assert "alpha_over_S_cubed" in names

    def test_closure_conditions_named(self):
        """The honest negative must come with closure conditions."""
        result = primordial_amplitude_attempt()
        conditions = result["closure_conditions"]
        assert len(conditions) >= 3
        # At least one condition mentions Genesis Hypothesis
        assert any("Genesis" in c for c in conditions)
        # At least one condition mentions inflationary-epoch
        assert any("inflation" in c.lower() for c in conditions)

    def test_no_epsilon_tuning_admonition_present(self):
        """The discipline note must explicitly state no parameter
        tuning was applied."""
        result = primordial_amplitude_attempt()
        note = result["discipline_note"]
        assert "tuning" in note.lower() or "fitting" in note.lower()
