"""Tests for constitutive_growth.py — D=1.0 diagnosis and Poisson closure.

These tests pin the key numbers and structural properties:
  1. The decoupled constitutive equation gives D ≈ 1 (not 2626)
  2. The Poisson closure gives D_ΛCDM ≈ 2626 at the σ_8 scale
  3. Dark energy suppresses D from ~3333 (pure matter-dom) to ~2626
  4. The quasi-static limit is valid (τ₀ H₀ ≪ 1)
  5. Super-horizon modes show significant GRUT enhancement
  6. The open gap (Poisson closure from S_CTP) is correctly flagged
"""

import pytest
import numpy as np

from grut.derivation.phi_munu.constitutive_growth import (
    quasi_static_validity,
    decoupled_constitutive_growth,
    poisson_closure_demonstration,
    growth_survey_with_closure,
    open_derivation_gap,
    constitutive_growth_verdict,
    TAU_0_H0,
)


# ─────────────────────────────────────────────────────────────────────
# Class 1 — Quasi-static validity
# ─────────────────────────────────────────────────────────────────────

class TestQuasiStaticValidity:
    """τ₀ H(a) ≪ 1 is the key check — conformal-mode relaxes fast."""

    def test_tau0_H0_small(self):
        """τ₀ H₀ ≈ 0.003 ≪ 1 — quasi-static valid today."""
        assert TAU_0_H0 < 0.05, f"τ₀ H₀ = {TAU_0_H0:.4f} should be < 0.05"

    def test_quasi_static_today_valid(self):
        qs = quasi_static_validity()
        assert qs["today_a1"]["quasi_static_ok"] is True

    def test_quasi_static_de_entry_valid(self):
        qs = quasi_static_validity()
        assert qs["de_entry_a0p5"]["quasi_static_ok"] is True

    def test_quasi_static_equality_marginal(self):
        """At matter-rad equality τ₀ H ≈ 5 — NOT strictly quasi-static."""
        qs = quasi_static_validity()
        tau_H_eq = qs["equality_a3e4"]["tau_0_H"]
        # Should be greater than 1 (quasi-static breaks at equality)
        assert tau_H_eq > 1.0, (
            f"τ₀ H at equality = {tau_H_eq:.2f} should be > 1.0 "
            "(quasi-static is approximate at early times)"
        )


# ─────────────────────────────────────────────────────────────────────
# Class 2 — D = 1.0 failure (decoupled constitutive equation)
# ─────────────────────────────────────────────────────────────────────

class TestDecoupledGrowthFailure:
    """The decoupled eq (no matter sourcing) gives D ≈ initial value."""

    def setup_method(self):
        self.result = decoupled_constitutive_growth()

    def test_decoupled_D_is_small_compared_to_LCDM(self):
        """D_decoupled << D_LCDM — no growth in the decoupled system."""
        ratio = self.result["ratio_decoupled_LCDM"]
        assert ratio < 0.01, (
            f"Decoupled/LCDM ratio = {ratio:.5f}; "
            "should be << 1 (near zero growth)"
        )

    def test_decoupled_D_close_to_initial(self):
        """D_decoupled ≈ initial value (barely grew from δ₀ = 1)."""
        D_dec = self.result["D_decoupled_today"]
        # Initial δ₀ = 1; the decoupled solution grows slightly (not zero exactly)
        # because there's still some late-time growth from friction alone.
        # The dominant mode grows as a^0 (constant) but with IC δ' = 1
        # there's a brief transient. By z=0, D should be < 5 (tiny vs 2626).
        assert D_dec < 10, (
            f"D_decoupled = {D_dec:.2f}; should be < 10 (tiny vs D_LCDM ≈ 2626)"
        )

    def test_LCDM_reference_is_large(self):
        """ΛCDM reference D_LCDM ≈ 2626 — shows the required growth."""
        D_lcdm = self.result["D_LCDM_today"]
        # Allow 30% either side of 2626 for numerical/cosmology variation
        assert 1800 < D_lcdm < 3400, (
            f"D_LCDM = {D_lcdm:.0f}; expected ≈ 2626 (range 1800–3400)"
        )

    def test_decoupled_delta_array_shape(self):
        """delta_decoupled has the right shape."""
        arr = self.result["delta_decoupled"]
        assert len(arr) == 1001  # n_steps + 1

    def test_a_array_runs_to_1(self):
        """a_array ends at a = 1 (today)."""
        a = self.result["a_array"]
        assert abs(a[-1] - 1.0) < 1e-10

    def test_diagnosis_string_mentions_D_equals_1(self):
        """Diagnosis string mentions the failure."""
        diag = self.result["diagnosis"]
        assert "D = 1.0 failure" in diag or "decoupled" in diag.lower()


# ─────────────────────────────────────────────────────────────────────
# Class 3 — Poisson closure gives D ≈ 2626
# ─────────────────────────────────────────────────────────────────────

class TestPoissonClosure:
    """Once Poisson closure is added, D_ΛCDM ≈ 2626."""

    def setup_method(self):
        self.result = poisson_closure_demonstration(k_per_Mpc=0.5)

    def test_D_LCDM_approximately_2626(self):
        """D_ΛCDM ≈ 2626 at σ_8 scale."""
        D = self.result["D_LCDM"]
        assert 2400 < D < 2900, f"D_LCDM = {D:.0f}; expected ≈ 2626"

    def test_D_GRUT_near_D_LCDM_at_sigma8(self):
        """At σ_8 scale, GRUT ≈ ΛCDM (deep sub-horizon)."""
        f = self.result["f_GRUT"]
        assert abs(f - 1.0) < 0.002, (
            f"f_GRUT = {f:.6f} at σ_8; should be < 0.2% from 1"
        )

    def test_pure_matter_dom_D_is_3333(self):
        """Pure matter-dom D = 1/a_init ≈ 3333."""
        pmd = self.result["pure_matter_dom_D"]
        assert 3200 < pmd < 3500, f"Pure-MD D = {pmd:.0f}; expected ≈ 3333"

    def test_lambda_suppression_positive(self):
        """Dark energy suppresses D below pure-matter-dom value."""
        supp = self.result["lambda_suppression_pct"]
        assert supp > 10, (
            f"Λ suppression = {supp:.1f}%; should be > 10% (Ω_Λ = 0.685)"
        )

    def test_lambda_suppression_not_too_large(self):
        """Dark energy suppression is ≤ 30%."""
        supp = self.result["lambda_suppression_pct"]
        assert supp < 35, f"Λ suppression = {supp:.1f}%; should be ≤ 30%"

    def test_decoupled_normalized_is_tiny(self):
        """D_decoupled / D_LCDM ≈ 1/2626 ≈ 3.8×10⁻⁴."""
        ratio = self.result["D_decoupled_normalized"]
        assert ratio < 0.01, (
            f"D_decoupled/D_LCDM = {ratio:.5f}; should be << 1"
        )

    def test_verdict_string_mentions_2626(self):
        v = self.result["closure_verdict"]
        assert "2626" in v or "D_LCDM" in v


# ─────────────────────────────────────────────────────────────────────
# Class 4 — Scale-dependent growth survey
# ─────────────────────────────────────────────────────────────────────

class TestGrowthSurvey:
    """Growth factor at all scales: sub-horizon → D_ΛCDM; super-horizon enhanced."""

    def setup_method(self):
        self.survey = growth_survey_with_closure()

    def test_all_scales_present(self):
        expected = {"galaxy_k1", "sigma8_k0p5", "quasi_k0p1",
                    "BAO_k0p04", "sloan_k0p01", "CMB_low_k0p001",
                    "CMB_horiz_k4e4"}
        assert set(self.survey.keys()) == expected

    def test_sub_horizon_LCDM_unchanged(self):
        """σ_8 scale: D_GRUT ≈ D_ΛCDM (< 0.2% difference)."""
        s = self.survey["sigma8_k0p5"]
        assert abs(s["f_GRUT"] - 1.0) < 0.002

    def test_BAO_scale_modest_enhancement(self):
        """BAO scale: 5–15% enhancement."""
        s = self.survey["BAO_k0p04"]
        assert 1.05 < s["f_GRUT"] < 1.15, (
            f"f_GRUT at BAO = {s['f_GRUT']:.4f}; expected 1.05–1.15"
        )

    def test_CMB_horizon_large_enhancement(self):
        """CMB horizon scale: > 50% enhancement (deeply super-horizon)."""
        s = self.survey["CMB_horiz_k4e4"]
        assert s["f_GRUT"] > 1.5, (
            f"f_GRUT at CMB horizon = {s['f_GRUT']:.4f}; expected > 1.5"
        )

    def test_enhancement_monotone_in_scale(self):
        """Enhancement increases from sub-horizon to super-horizon."""
        f_sigma8 = self.survey["sigma8_k0p5"]["f_GRUT"]
        f_BAO = self.survey["BAO_k0p04"]["f_GRUT"]
        f_CMB = self.survey["CMB_horiz_k4e4"]["f_GRUT"]
        assert f_sigma8 < f_BAO < f_CMB, (
            f"Enhancement should grow: σ_8={f_sigma8:.4f} < "
            f"BAO={f_BAO:.4f} < CMB={f_CMB:.4f}"
        )

    def test_all_D_LCDM_approximately_same(self):
        """D_ΛCDM ≈ 2626 at all scales (same background, same IC)."""
        for name, s in self.survey.items():
            assert 2400 < s["D_LCDM"] < 2900, (
                f"{name}: D_LCDM = {s['D_LCDM']:.0f}; expected ≈ 2626"
            )


# ─────────────────────────────────────────────────────────────────────
# Class 5 — Open derivation gap
# ─────────────────────────────────────────────────────────────────────

class TestOpenDerivationGap:
    """The Poisson closure is borrowed, not yet derived from S_CTP."""

    def setup_method(self):
        self.gap = open_derivation_gap()

    def test_gap_name_correct(self):
        assert self.gap["gap_name"] == "constitutive_growth_poisson_closure_gap"

    def test_camb_not_blocked(self):
        assert "NOT blocked" in self.gap["blocking"]

    def test_closure_condition_mentions_mu_grut(self):
        cc = self.gap["closure_condition"]
        assert "μ_GRUT" in cc or "mu_GRUT" in cc.lower() or "Poisson" in cc


# ─────────────────────────────────────────────────────────────────────
# Class 6 — Top-level verdict
# ─────────────────────────────────────────────────────────────────────

class TestConstitutiveGrowthVerdict:
    """Top-level verdict pins all status flags and key numbers."""

    def setup_method(self):
        self.v = constitutive_growth_verdict()

    def test_failure_diagnosed(self):
        assert self.v["status"]["d_1p0_failure_diagnosed"] is True

    def test_poisson_closure_demonstrated(self):
        assert self.v["status"]["poisson_closure_demonstrated"] is True

    def test_D_lcdm_2626_verified(self):
        assert self.v["status"]["d_lcdm_2626_verified"] is True

    def test_poisson_closure_from_sctp_still_open(self):
        assert self.v["status"]["poisson_closure_from_sctp"] is False

    def test_camb_not_blocked(self):
        assert self.v["status"]["camb_class_run_blocked_by_this"] is False

    def test_failure_mode_D_is_small(self):
        D_fail = self.v["failure_mode"]["D_constitutive_without_closure"]
        assert D_fail < 10

    def test_resolution_D_LCDM_correct(self):
        D = self.v["resolution"]["D_LCDM_sigma8"]
        assert 2400 < D < 2900

    def test_verdict_string_present(self):
        v = self.v["verdict"]
        assert len(v) > 100
        assert "Poisson" in v
        assert "D=1.0" in v or "D = 1" in v or "closure" in v.lower()
