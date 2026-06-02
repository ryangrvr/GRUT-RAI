"""Tests for grut.derived.cmb.boltzmann_consistency.

Covers three levels:
  1. Case A structural properties — all 6 conditions must hold
  2. Modified P(k) — non-negative enhancement everywhere, scale-dependent
  3. σ₈ and ISW — quantitative bounds consistent with observations
  4. Module constants — transition scale and k_* pinned
"""

import math

import numpy as np
import pytest

from grut.derived.cmb.boltzmann_consistency import (
    K_CANONICAL,
    K_STAR_PER_MPC,
    LAMBDA_STAR_MPC,
    TAU_0_C_MPC,
    boltzmann_consistency_summary,
    case_a_structural_properties,
    isw_enhancement_estimate,
    power_spectrum_at_canonical_scales,
    power_spectrum_ratio,
    sigma8_modification,
)


# ─────────────────────────────────────────────────────────────────────
# Constants
# ─────────────────────────────────────────────────────────────────────

class TestModuleConstants:
    """Transition scale constants are correctly derived from τ₀."""

    def test_tau_0_c_mpc_is_about_12p85(self):
        """τ₀ × c ≈ 12.85 Mpc — gravitational relaxation length scale."""
        assert abs(TAU_0_C_MPC - 12.85) < 0.5

    def test_k_star_is_reciprocal_of_tau_0_c(self):
        """k_* = 1 / (τ₀ c) by definition."""
        assert abs(K_STAR_PER_MPC - 1.0 / TAU_0_C_MPC) < 1e-10

    def test_lambda_star_is_2pi_tau_0_c(self):
        """λ_* = 2π τ₀ c by definition."""
        assert abs(LAMBDA_STAR_MPC - 2.0 * math.pi * TAU_0_C_MPC) < 1e-10

    def test_lambda_star_approx_80p7_mpc(self):
        """Transition wavelength λ_* ≈ 80.7 Mpc — bookkeeping pinned at 5%."""
        assert abs(LAMBDA_STAR_MPC - 80.7) / 80.7 < 0.05

    def test_k_star_approx_0p0778_per_mpc(self):
        """Transition wavenumber k_* ≈ 0.0778 Mpc⁻¹ — pinned at 5%."""
        assert abs(K_STAR_PER_MPC - 0.0778) / 0.0778 < 0.05

    def test_k_star_is_cosmological_ir_scale(self):
        """k_* must be well below any UV threshold (k_* < 1 Mpc⁻¹)."""
        assert K_STAR_PER_MPC < 1.0

    def test_k_canonical_covers_expected_range(self):
        """Canonical grid spans from CMB horizon to σ₈ scale."""
        k_min = min(K_CANONICAL)
        k_max = max(K_CANONICAL)
        assert k_min < 1e-3       # sub-milliMpc⁻¹ horizon scale
        assert k_max >= 0.5       # σ₈ scale


# ─────────────────────────────────────────────────────────────────────
# Case A structural properties
# ─────────────────────────────────────────────────────────────────────

class TestCaseAStructuralProperties:
    """All 6 structural conditions for Case A must hold."""

    @pytest.fixture(scope="class")
    def props(self):
        return case_a_structural_properties()

    def test_returns_six_conditions(self, props):
        expected_keys = {
            "single_equation_entry",
            "no_gravitational_slip",
            "no_higher_derivatives",
            "ir_only",
            "lorentzian_retarded",
            "bianchi_preserved",
        }
        assert set(props.keys()) == expected_keys

    def test_single_equation_entry(self, props):
        """μ(k,a) modifies only the Poisson equation — no other Boltzmann entry."""
        assert props["single_equation_entry"] is True

    def test_no_gravitational_slip(self, props):
        """γ = Φ/Ψ = 1 — GRUT predicts zero gravitational slip."""
        assert props["no_gravitational_slip"] is True

    def test_no_higher_derivatives(self, props):
        """Lorentzian μ(k,a) is smooth and finite — no ∂_k operators generated."""
        assert props["no_higher_derivatives"] is True

    def test_ir_only(self, props):
        """Modification is IR (λ_* = 80.7 Mpc ≫ any UV threshold)."""
        assert props["ir_only"] is True

    def test_lorentzian_retarded(self, props):
        """μ-1 is the FT of a retarded (causal) exponential kernel."""
        assert props["lorentzian_retarded"] is True

    def test_bianchi_preserved(self, props):
        """∇^μ T_μν = 0 maintained — Bianchi identity holds in matter sector."""
        assert props["bianchi_preserved"] is True

    def test_all_conditions_hold(self, props):
        """Combined: Case A holds — no operator completion required."""
        failed = [k for k, v in props.items() if not v]
        assert not failed, f"Case A conditions failed: {failed}"


# ─────────────────────────────────────────────────────────────────────
# Modified power spectrum — array interface
# ─────────────────────────────────────────────────────────────────────

class TestPowerSpectrumRatio:
    """P_GRUT/P_ΛCDM ≥ 1 everywhere; enhancement is scale-dependent."""

    @pytest.fixture(scope="class")
    def k_arr(self):
        return np.array(list(K_CANONICAL))

    @pytest.fixture(scope="class")
    def ratio(self, k_arr):
        return power_spectrum_ratio(k_arr)

    def test_returns_array_of_correct_length(self, k_arr, ratio):
        assert len(ratio) == len(k_arr)

    def test_all_ratios_are_finite(self, ratio):
        assert np.all(np.isfinite(ratio))

    def test_all_ratios_at_least_one(self, ratio):
        """GRUT only enhances power — never suppresses it."""
        assert np.all(ratio >= 1.0), (
            f"Power suppression found at some scales: {ratio[ratio < 1.0]}"
        )

    def test_ir_enhancement_larger_than_uv(self, k_arr, ratio):
        """Super-horizon modes have larger enhancement than σ₈ scale."""
        idx_ir = np.argmin(k_arr)           # smallest k → largest scale
        idx_uv = np.argmax(k_arr)           # largest k → σ₈ scale
        assert ratio[idx_ir] > ratio[idx_uv]

    def test_sigma8_scale_nearly_unity(self, k_arr, ratio):
        """At k=0.5 Mpc⁻¹ (σ₈ scale) the ratio is < 1.002 — sub-percent."""
        idx = np.where(np.isclose(k_arr, 0.5))[0]
        if len(idx):
            assert ratio[idx[0]] < 1.002

    def test_cmb_horizon_has_large_enhancement(self, k_arr, ratio):
        """At k=4.5×10⁻⁴ (CMB horizon) enhancement is > 5× (f² > 5)."""
        idx = np.where(np.isclose(k_arr, 4.5e-4))[0]
        if len(idx):
            assert ratio[idx[0]] > 5.0   # f_GRUT ≈ 2.35 → f² ≈ 5.5


# ─────────────────────────────────────────────────────────────────────
# Canonical-scale survey
# ─────────────────────────────────────────────────────────────────────

class TestPowerSpectrumAtCanonicalScales:
    """Survey at 11 canonical k values — structure and ordering."""

    @pytest.fixture(scope="class")
    def survey(self):
        return power_spectrum_at_canonical_scales()

    def test_covers_all_canonical_k(self, survey):
        for k in K_CANONICAL:
            assert k in survey, f"Missing k={k} from canonical survey"

    def test_each_entry_has_required_keys(self, survey):
        required = {
            "k_Mpc", "label", "f_GRUT", "P_ratio",
            "P_ratio_percent", "mu_today", "k_phys_tau0c", "regime",
        }
        for k, entry in survey.items():
            missing = required - set(entry.keys())
            assert not missing, f"k={k} missing keys: {missing}"

    def test_f_grut_always_positive(self, survey):
        for k, entry in survey.items():
            assert entry["f_GRUT"] > 0, f"f_GRUT non-positive at k={k}"

    def test_p_ratio_consistent_with_f_grut(self, survey):
        """P_ratio = f_GRUT² within floating-point tolerance."""
        for k, entry in survey.items():
            expected = entry["f_GRUT"] ** 2
            assert abs(entry["P_ratio"] - expected) < 1e-10

    def test_regime_labels_are_valid(self, survey):
        valid = {"super-horizon", "transition", "sub-horizon"}
        for k, entry in survey.items():
            assert entry["regime"] in valid, (
                f"Unknown regime '{entry['regime']}' at k={k}"
            )

    def test_bao_scale_enhancement_is_measurable(self, survey):
        """At k=0.04 Mpc⁻¹ (BAO scale) enhancement should be ~5–15%."""
        entry = survey.get(4.0e-2)
        if entry is not None:
            pct = entry["P_ratio_percent"]
            assert 1.0 < pct < 30.0, f"BAO enhancement out of range: {pct:.2f}%"

    def test_transition_scale_in_transition_regime(self, survey):
        """k_* = 0.078 Mpc⁻¹ should be labelled 'transition' or close."""
        entry = survey.get(7.8e-2)
        if entry is not None:
            assert entry["regime"] in ("transition", "sub-horizon")

    def test_k_phys_tau0c_is_positive(self, survey):
        for k, entry in survey.items():
            assert entry["k_phys_tau0c"] > 0


# ─────────────────────────────────────────────────────────────────────
# σ₈ modification
# ─────────────────────────────────────────────────────────────────────

class TestSigma8Modification:
    """σ₈ is nearly unchanged — GRUT does not worsen the S₈ tension."""

    @pytest.fixture(scope="class")
    def s8(self):
        return sigma8_modification()

    def test_returns_required_keys(self, s8):
        required = {"sigma8_LCDM", "sigma8_GRUT", "f_GRUT_sigma8",
                    "change_percent", "verdict"}
        assert required.issubset(set(s8.keys()))

    def test_sigma8_grut_larger_than_lcdm(self, s8):
        """GRUT increases σ₈ (never decreases it) — growth only enhances."""
        assert s8["sigma8_GRUT"] >= s8["sigma8_LCDM"]

    def test_sigma8_change_less_than_half_percent(self, s8):
        """Change is < 0.5% — consistent with S₈ observational constraint."""
        assert abs(s8["change_percent"]) < 0.5, (
            f"σ₈ change {s8['change_percent']:.4f}% exceeds 0.5% threshold"
        )

    def test_sigma8_grut_is_physically_reasonable(self, s8):
        """σ₈_GRUT must be within plausible observational range (0.7–1.0)."""
        assert 0.7 < s8["sigma8_GRUT"] < 1.0

    def test_f_grut_sigma8_is_close_to_one(self, s8):
        """Growth enhancement at σ₈ scale is < 0.5% above unity."""
        assert 1.0 <= s8["f_GRUT_sigma8"] < 1.005

    def test_verdict_mentions_s8_tension(self, s8):
        """Verdict must address S₈ tension explicitly."""
        assert "S₈" in s8["verdict"] or "s8" in s8["verdict"].lower()

    def test_default_sigma8_lcdm_is_planck_value(self, s8):
        """Default σ₈_ΛCDM is Planck 2018 best-fit 0.811."""
        assert abs(s8["sigma8_LCDM"] - 0.811) < 1e-6


# ─────────────────────────────────────────────────────────────────────
# ISW enhancement estimate
# ─────────────────────────────────────────────────────────────────────

class TestISWEnhancementEstimate:
    """ISW power is enhanced at low ℓ — quantitative first estimate."""

    @pytest.fixture(scope="class")
    def isw(self):
        return isw_enhancement_estimate()

    def test_returns_required_keys(self, isw):
        required = {
            "k_horizon", "a_de_start",
            "f_GRUT_today", "f_GRUT_at_DE_entry",
            "f_isw_approx", "C_ell_isw_power_enhancement_approx",
            "C_ell_isw_percent_change", "planck_low_l_anomaly",
            "verdict", "note",
        }
        assert required.issubset(set(isw.keys()))

    def test_f_grut_today_is_large_at_horizon(self, isw):
        """At CMB horizon scale, D_GRUT/D_ΛCDM > 2 (factor 2+ enhancement)."""
        assert isw["f_GRUT_today"] > 2.0, (
            f"Growth factor at CMB horizon scale too small: {isw['f_GRUT_today']:.3f}"
        )

    def test_f_grut_at_de_entry_is_positive(self, isw):
        assert isw["f_GRUT_at_DE_entry"] > 0

    def test_f_grut_at_de_entry_is_above_unity(self, isw):
        """Enhancement already present at DE-era entry."""
        assert isw["f_GRUT_at_DE_entry"] > 1.0

    def test_isw_power_enhancement_is_positive(self, isw):
        """More power at low ℓ — enhancement is positive."""
        assert isw["C_ell_isw_power_enhancement_approx"] > 0.0

    def test_isw_percent_change_is_positive(self, isw):
        assert isw["C_ell_isw_percent_change"] > 0.0

    def test_planck_low_l_anomaly_mentioned(self, isw):
        """Verdict must acknowledge the Planck low-ℓ deficit as the tension."""
        assert "deficit" in isw["planck_low_l_anomaly"].lower() or \
               "low" in isw["planck_low_l_anomaly"].lower()

    def test_verdict_identifies_tension(self, isw):
        """Verdict must name ISW and the observational tension."""
        v = isw["verdict"].lower()
        assert "isw" in v or "ℓ" in isw["verdict"]

    def test_note_acknowledges_approximation(self, isw):
        """Note must flag that this is an approximation requiring CAMB/CLASS."""
        n = isw["note"].lower()
        assert "approximat" in n or "camb" in n or "class" in n

    def test_default_k_horizon_is_cmb_scale(self, isw):
        assert abs(isw["k_horizon"] - 4.5e-4) < 1e-10

    def test_default_a_de_start_is_0p5(self, isw):
        assert abs(isw["a_de_start"] - 0.5) < 1e-10


# ─────────────────────────────────────────────────────────────────────
# Top-level summary
# ─────────────────────────────────────────────────────────────────────

class TestBoltzmannConsistencySummary:
    """Top-level summary assembles all sub-results correctly."""

    @pytest.fixture(scope="class")
    def summary(self):
        return boltzmann_consistency_summary()

    def test_returns_required_top_level_keys(self, summary):
        required = {
            "case_a_structural_properties",
            "case_a_holds",
            "power_spectrum_survey",
            "sigma8",
            "isw_estimate",
            "lambda_star_Mpc",
            "k_star_per_Mpc",
            "tau_0_c_Mpc",
            "implementation_gate",
            "verdict",
        }
        assert required.issubset(set(summary.keys()))

    def test_case_a_holds_is_true(self, summary):
        """All structural conditions satisfied → Case A holds."""
        assert summary["case_a_holds"] is True

    def test_case_a_holds_consistent_with_props(self, summary):
        """case_a_holds must equal all(props.values())."""
        props = summary["case_a_structural_properties"]
        expected = all(props.values())
        assert summary["case_a_holds"] == expected

    def test_lambda_star_consistent_with_module_constant(self, summary):
        assert abs(summary["lambda_star_Mpc"] - LAMBDA_STAR_MPC) < 1e-10

    def test_k_star_consistent_with_module_constant(self, summary):
        assert abs(summary["k_star_per_Mpc"] - K_STAR_PER_MPC) < 1e-10

    def test_tau_0_c_consistent_with_module_constant(self, summary):
        assert abs(summary["tau_0_c_Mpc"] - TAU_0_C_MPC) < 1e-10

    def test_implementation_gate_status_is_pending(self, summary):
        gate = summary["implementation_gate"]
        assert gate["status"] == "PENDING"

    def test_implementation_gate_not_blocking(self, summary):
        """The implementation gate should be non-blocking (v3 can proceed)."""
        gate = summary["implementation_gate"]
        assert gate["blocking"] is False

    def test_verdict_mentions_case_a(self, summary):
        assert "Case A" in summary["verdict"]

    def test_verdict_mentions_isw(self, summary):
        assert "ISW" in summary["verdict"]

    def test_power_spectrum_survey_has_all_canonical_k(self, summary):
        ps = summary["power_spectrum_survey"]
        for k in K_CANONICAL:
            assert k in ps

    def test_sigma8_nested_keys(self, summary):
        s8 = summary["sigma8"]
        assert "sigma8_GRUT" in s8
        assert "change_percent" in s8
