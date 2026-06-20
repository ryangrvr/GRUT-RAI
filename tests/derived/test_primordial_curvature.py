"""Tests for the Stage-2 forward derivation: primordial curvature ζ
from linearized constitutive equation around z = 0.

Pins the rescaling-conditional result: Lens B/F's forward derivation
produces a definite dimensional variance, but the dimensionless P_ζ
depends on the rescaling choice. Three rescalings tested:
  (A) Planck:           (1/π)(t_Pl/τ_0)³ ≈ 10⁻¹⁷⁶  — no α-S, fails
  (B) Cosmic-baseline:  1/(πS³) ≈ 8.15×10⁻⁹      — S³ family, factor 4 from A_s
  (C) H_inf:            ((2-R)/S)³/π ≈ 4.92×10⁻⁹  — S³ family, factor 2.3 from A_s

The α/S³ family is recovered under (B) and (C), NOT under (A). The
framework does not natively pin the rescaling — this is the
n_g(ω) covariance open negative.

These tests pin:
1. Crossover scale k_* = 1/(cτ_0) and resulting wavelength ~80 Mpc
2. KMS thermal factor at the crossover for various T
3. Dimensional variance value at T=0 and T=T_c
4. The three rescaling outcomes' values and α-S structures
5. The conditional verdict (NOT a clean honest negative)
6. Structural link to n_g(ω) covariance open negative
"""

from __future__ import annotations

import math

import pytest

from grut.derived.cosmology.primordial_curvature import (
    A_S_PLANCK_2018,
    ALPHA_OVER_S_CUBED,
    comparison_to_dimensional_candidates,
    crossover_scale_k_star,
    dimensionless_power_spectrum_at_crossover,
    kms_thermal_factor_at_crossover,
    lens_B_F_forward_derivation,
    mode_variance_at_crossover,
    primordial_curvature_lens_BF_attempt,
    rescaling_sensitivity_analysis,
)
from grut.foundation.constants import C as C_LIGHT, T_PLANCK
from grut.foundation.closure_protocol import (
    ALPHA_VAC,
    S_SCREENING,
    TAU_0_SEC,
)


# ─────────────────────────────────────────────────────────────────────
# Crossover scale
# ─────────────────────────────────────────────────────────────────────


class TestCrossoverScale:
    def test_k_star_equals_inverse_c_tau(self):
        """k_* = 1/(c τ₀)."""
        k_star = crossover_scale_k_star()
        expected = 1.0 / (C_LIGHT * TAU_0_SEC)
        assert abs(k_star - expected) / expected < 1e-12

    def test_crossover_wavelength_is_galaxy_cluster_scale(self):
        """λ_* = 2π/k_* ≈ 81 Mpc — galaxy-cluster / BAO scale.

        This is itself diagnostic: GRUT's natural memory-bandwidth
        scale corresponds to large-scale-structure dynamics, NOT
        the CMB pivot scale (where A_s is observed). Modes at the
        CMB pivot (k ≈ 0.05/Mpc, λ ≈ 125 Mpc) are slightly
        shorter-wavelength than the crossover but in the same
        regime."""
        k_star = crossover_scale_k_star()
        wavelength_m = 2 * math.pi / k_star
        wavelength_Mpc = wavelength_m / 3.0857e22
        # Should be tens of Mpc — pin a reasonable range
        assert 50 < wavelength_Mpc < 200


# ─────────────────────────────────────────────────────────────────────
# KMS thermal factor
# ─────────────────────────────────────────────────────────────────────


class TestKMSThermalFactor:
    def test_at_T_c_gives_coth_one_half(self):
        """At the real T_c = ℏ/(τ_micro·k_B) = 54.7 MK (post-Correction
        #22), the argument ℏ/(2k_BT_c·τ_micro) = 1/2, so coth(1/2) ≈ 2.16.

        This is the convention reconciliation: the KMS occupation is set
        by the microscopic bath frequency 1/τ_micro, matching
        thermal_transition's f(T) = tanh(T_c/2T) = 1/coth."""
        from grut.foundation.closure_protocol import T_C_KELVIN
        factor = kms_thermal_factor_at_crossover(T_C_KELVIN)
        expected = math.cosh(0.5) / math.sinh(0.5)
        assert abs(factor - expected) < 1e-6
        # Reciprocity with thermal_transition's activation fraction
        assert abs(1.0 / factor - math.tanh(0.5)) < 1e-9

    def test_uses_tau_micro_not_tau_0(self):
        """Guard against regression to the stale τ₀-based convention:
        the stale T_c = ℏ/(τ₀·k_B) must NOT give coth(1/2)."""
        from grut.foundation.constants import HBAR, K_B
        stale_T_c = HBAR / (TAU_0_SEC * K_B)
        factor = kms_thermal_factor_at_crossover(stale_T_c)
        # At the stale T_c the τ_micro argument is astronomically large
        # → quantum limit coth → 1, NOT coth(1/2) ≈ 2.16.
        assert abs(factor - 1.0) < 1e-6

    def test_quantum_limit(self):
        """T → 0: coth(∞) → 1."""
        factor = kms_thermal_factor_at_crossover(0.0)
        assert abs(factor - 1.0) < 1e-6

    def test_classical_limit(self):
        """T ≫ T_c: coth(x) → 1/x = 2k_BT·τ_micro/ℏ."""
        from grut.foundation.constants import HBAR, K_B
        from grut.foundation.closure_protocol import TAU_MICRO_SEC
        T_high = 1e30  # extremely classical
        factor = kms_thermal_factor_at_crossover(T_high)
        expected = 2 * K_B * T_high * TAU_MICRO_SEC / HBAR
        assert abs(factor - expected) / expected < 1e-3


# ─────────────────────────────────────────────────────────────────────
# Dimensional variance
# ─────────────────────────────────────────────────────────────────────


class TestModeVariance:
    def test_variance_at_TC_is_finite(self):
        """⟨|δz_k*(1/τ₀)|²⟩ should be finite at T = T_c = 54.7 MK."""
        from grut.foundation.closure_protocol import T_C_KELVIN
        v = mode_variance_at_crossover(T_C_KELVIN)
        assert 0 < v < math.inf

    def test_variance_scales_with_2pi_G_c2(self):
        """The variance is 2π G c² × coth(1/2) at T_c = 54.7 MK, with the
        KMS occupation set by τ_micro (post-Correction #22)."""
        from grut.foundation.constants import G
        from grut.foundation.closure_protocol import T_C_KELVIN
        v = mode_variance_at_crossover(T_C_KELVIN)
        coth_at_TC = math.cosh(0.5) / math.sinh(0.5)
        expected = 2 * math.pi * G * C_LIGHT**2 * coth_at_TC
        assert abs(v - expected) / expected < 1e-6

    def test_variance_at_zero_T_uses_quantum_limit(self):
        """At T = 0, coth → 1, so variance = 2π G c²."""
        from grut.foundation.constants import G
        v = mode_variance_at_crossover(0.0)
        expected = 2 * math.pi * G * C_LIGHT**2
        assert abs(v - expected) / expected < 1e-6


# ─────────────────────────────────────────────────────────────────────
# Three rescaling outcomes — the core Stage-2 finding
# ─────────────────────────────────────────────────────────────────────


class TestRescalingOutcomes:
    """Pin each of the three rescaling outcomes' values and α-S
    structures. These are the central Stage-2 numerical findings."""

    def test_planck_rescaling_no_alpha_S_structure(self):
        """(A) Planck rescaling: (1/π)(t_Pl/τ_0)³ — no α or S."""
        result = lens_B_F_forward_derivation()
        opt = result["rescaling_outcomes"]["A_planck_rescaling"]
        assert "NONE" in opt["alpha_S_structure"]
        assert "(t_Pl/τ_0)" in opt["formula"]

    def test_planck_rescaling_value_far_below_A_s(self):
        """(A) Planck: ~10⁻¹⁷⁶, fails by ~167 orders of magnitude."""
        result = lens_B_F_forward_derivation()
        opt = result["rescaling_outcomes"]["A_planck_rescaling"]
        assert 1e-180 < opt["value"] < 1e-170
        assert 150 < opt["log10_below_A_s"] < 200

    def test_cosmic_baseline_rescaling_in_alpha_S_cubed_family(self):
        """(B) Cosmic-baseline rescaling: 1/(πS³) ≈ 8.15×10⁻⁹ — IN
        the α/S³ family. Differs from α/S³ by α·π = π/3 ≈ 1.047
        (ratio ≈ 0.955 since 1/(πS³) is slightly smaller)."""
        result = lens_B_F_forward_derivation()
        opt = result["rescaling_outcomes"]["B_cosmic_baseline_rescaling"]
        # Pin the value (within a small fractional tolerance)
        expected = 1.0 / (math.pi * S_SCREENING**3)
        assert abs(opt["value"] - expected) / expected < 1e-6
        # Pin S³ structure
        assert "S³" in opt["alpha_S_structure"] or "S^3" in opt["alpha_S_structure"]
        # Pin "in α/S³ family"
        assert "family" in opt["alpha_S_structure"].lower()

    def test_cosmic_baseline_rescaling_factor_from_A_s(self):
        """(B) Cosmic-baseline: factor ~3.88 from A_s."""
        result = lens_B_F_forward_derivation()
        opt = result["rescaling_outcomes"]["B_cosmic_baseline_rescaling"]
        assert 3.0 < opt["vs_A_s"] < 5.0

    def test_cosmic_baseline_rescaling_close_to_alpha_over_S_cubed(self):
        """(B) value / (α/S³) = 3/π ≈ 0.955 (5% apart, same family)."""
        result = lens_B_F_forward_derivation()
        opt = result["rescaling_outcomes"]["B_cosmic_baseline_rescaling"]
        ratio = opt["vs_alpha_over_S_cubed"]
        # Should be exactly 3/π ≈ 0.9549
        expected_ratio = 3.0 / math.pi
        assert abs(ratio - expected_ratio) < 1e-6

    def test_H_inf_rescaling_in_alpha_S_cubed_family(self):
        """(C) H_inf rescaling: (H_inf τ_0)³/π ≈ 4.92×10⁻⁹.
        S³ structure with (2-R)³ prefactor."""
        result = lens_B_F_forward_derivation()
        opt = result["rescaling_outcomes"]["C_H_inf_rescaling"]
        # Pin the value
        H_INF_HZ = 1.884021899694621e-18
        H_inf_tau_0 = H_INF_HZ * TAU_0_SEC
        expected = H_inf_tau_0**3 / math.pi
        assert abs(opt["value"] - expected) / expected < 1e-6
        # Pin S³ family
        assert "S³" in opt["alpha_S_structure"] or "S^3" in opt["alpha_S_structure"]

    def test_H_inf_rescaling_factor_from_A_s(self):
        """(C) H_inf: factor ~2.34 from A_s — actually CLOSER to A_s
        than (B)."""
        result = lens_B_F_forward_derivation()
        opt = result["rescaling_outcomes"]["C_H_inf_rescaling"]
        assert 2.0 < opt["vs_A_s"] < 3.0


# ─────────────────────────────────────────────────────────────────────
# Verdict
# ─────────────────────────────────────────────────────────────────────


class TestVerdict:
    def test_verdict_is_rescaling_conditional(self):
        """The verdict is RESCALING-CONDITIONAL, not a clean honest
        negative. The α/S³ family IS recovered under cosmic-baseline
        and H_inf rescalings."""
        result = lens_B_F_forward_derivation()
        assert "RESCALING-CONDITIONAL" in result["verdict"]

    def test_verdict_acknowledges_alpha_S_recovered_under_B_C(self):
        """The verdict must explicitly state that α/S³ IS recovered
        under (B) and (C). This is the load-bearing finding."""
        result = lens_B_F_forward_derivation()
        verdict = result["verdict"]
        assert "RECOVERED" in verdict.upper()
        assert "(B)" in verdict
        assert "(C)" in verdict

    def test_verdict_links_to_open_negative_9(self):
        """The verdict must connect to the n_g(ω) covariance gap."""
        result = lens_B_F_forward_derivation()
        verdict = result["verdict"]
        assert "covariance" in verdict.lower() or "n_g" in verdict.lower()

    def test_structural_link_field_present(self):
        """The result must include the explicit structural link to
        the covariance open negative."""
        result = lens_B_F_forward_derivation()
        assert "structural_link_to_open_negative_9" in result
        link = result["structural_link_to_open_negative_9"]
        assert "n_g_omega_cosmological_covariance" in link
        assert "covariance" in link.lower()


# ─────────────────────────────────────────────────────────────────────
# Rescaling sensitivity analysis function
# ─────────────────────────────────────────────────────────────────────


class TestRescalingSensitivityAnalysis:
    def test_returns_three_rescaling_options(self):
        result = rescaling_sensitivity_analysis()
        opts = result["rescaling_options"]
        assert "A_planck_rescaling" in opts
        assert "B_cosmic_baseline_rescaling" in opts
        assert "C_H_inf_rescaling" in opts

    def test_each_option_has_alpha_S_family_flag(self):
        result = rescaling_sensitivity_analysis()
        for name, opt in result["rescaling_options"].items():
            assert "in_alpha_over_S_cubed_family" in opt

    def test_planck_NOT_in_family(self):
        result = rescaling_sensitivity_analysis()
        assert (
            result["rescaling_options"]["A_planck_rescaling"]
            ["in_alpha_over_S_cubed_family"] is False
        )

    def test_cosmic_baseline_IN_family(self):
        result = rescaling_sensitivity_analysis()
        assert (
            result["rescaling_options"]["B_cosmic_baseline_rescaling"]
            ["in_alpha_over_S_cubed_family"] is True
        )

    def test_H_inf_IN_family(self):
        result = rescaling_sensitivity_analysis()
        assert (
            result["rescaling_options"]["C_H_inf_rescaling"]
            ["in_alpha_over_S_cubed_family"] is True
        )

    def test_structural_note_links_to_open_negative_9(self):
        result = rescaling_sensitivity_analysis()
        note = result["structural_note"]
        assert "covariance" in note.lower() or "#9" in note


# ─────────────────────────────────────────────────────────────────────
# Top-level reporter
# ─────────────────────────────────────────────────────────────────────


class TestTopLevelReporter:
    def test_runs_without_error(self):
        result = primordial_curvature_lens_BF_attempt()
        assert "honest_conclusion" in result
        assert "structural_finding" in result

    def test_conclusion_states_rescaling_conditional(self):
        """The conclusion must explicitly say the result is
        rescaling-conditional, not a clean negative."""
        result = primordial_curvature_lens_BF_attempt()
        conclusion = result["honest_conclusion"]
        assert "RESCALING-CONDITIONAL" in conclusion or "conditional" in conclusion.lower()

    def test_conclusion_acknowledges_alpha_S_recovered(self):
        """The conclusion must state α/S³ family IS recovered
        under at least one rescaling."""
        result = primordial_curvature_lens_BF_attempt()
        conclusion = result["honest_conclusion"]
        # Either "recovered" or "is in the α/S³ family"
        assert "recovered" in conclusion.lower() or "family" in conclusion.lower()

    def test_structural_finding_names_open_negative_link(self):
        """The structural_finding must explicitly link to
        n_g_omega_cosmological_covariance_open_question."""
        result = primordial_curvature_lens_BF_attempt()
        finding = result["structural_finding"]
        assert "n_g_omega" in finding or "covariance" in finding.lower()


# ─────────────────────────────────────────────────────────────────────
# Comparison to equivalence class
# ─────────────────────────────────────────────────────────────────────


class TestComparisonToEquivalenceClass:
    def test_alpha_over_S_cubed_in_candidates(self):
        result = comparison_to_dimensional_candidates()
        names = [c["name"] for c in result["candidates"]]
        assert any("α/S³" in n for n in names)

    def test_lens_BF_natural_in_candidates(self):
        """The Planck-rescaled (t_Pl/τ_0)³ result is in the
        candidate list as one of the rescaling options."""
        result = comparison_to_dimensional_candidates()
        names = [c["name"] for c in result["candidates"]]
        assert any("(t_Pl/τ₀)³" in n or "(t_Pl/τ_0)³" in n for n in names)
