"""Tests for the Genesis noise-kernel spectral analysis.

Pins the Stage 2 forward derivation: the framework's KMS noise kernel
applied to the linearized OU process around z = 0 produces a
Lorentzian × linear spectrum, NOT a thermal/Planck/Bose-Einstein
spectrum. Multiple "characteristic temperatures" can be extracted but
none match CMB.

These tests pin the load-bearing outputs:
  - spectrum form at T = 0
  - spectral peak at ω = 1/τ_0 → T = 5.78×10⁻²⁷ K
  - cross-verification against existing fdt_noise infrastructure
  - shape is NOT Planck/Bose-Einstein
"""

from __future__ import annotations

import math

import pytest

from grut.derived.cosmology.genesis_noise_kernel import (
    OMEGA_PLANCK_HZ,
    T_CMB_K,
    T_PLANCK_K,
    genesis_noise_kernel_attempt,
    kms_noise_spectrum,
    planck_spectral_shape,
    shape_difference_from_planck,
    spectral_density_h,
    spectral_peak_omega_T0,
    temperature_from_spectral_peak,
    temperature_from_uv_cutoff,
    variance_h_integrated_T0,
)
from grut.foundation.constants import HBAR, K_B
from grut.foundation.closure_protocol import TAU_0_SEC


# ─────────────────────────────────────────────────────────────────────
# Cross-verification with existing infrastructure
# ─────────────────────────────────────────────────────────────────────


class TestCrossVerificationWithExistingFDT:
    """The new kms_noise_spectrum must reproduce existing
    fdt_noise (grut/foundation/noise_kernel.py) exactly. This is
    the framework-internal sanity check."""

    def test_classical_limit_matches_fdt(self):
        from grut.foundation.noise_kernel import fdt_noise
        omega, T = 1.0, 100.0
        assert (
            abs(kms_noise_spectrum(omega, T) - fdt_noise(omega, TAU_0_SEC, T))
            < 1e-50
        )

    def test_quantum_limit_matches_fdt(self):
        from grut.foundation.noise_kernel import fdt_noise
        omega, T = 1e15, 0.0
        assert (
            abs(kms_noise_spectrum(omega, T) - fdt_noise(omega, TAU_0_SEC, T))
            < 1e-40
        )

    def test_intermediate_regime_matches_fdt(self):
        from grut.foundation.noise_kernel import fdt_noise
        omega, T = 1.0/TAU_0_SEC, 1e-26
        assert (
            abs(kms_noise_spectrum(omega, T) - fdt_noise(omega, TAU_0_SEC, T))
            < 1e-70
        )


# ─────────────────────────────────────────────────────────────────────
# Spectrum form at T = 0
# ─────────────────────────────────────────────────────────────────────


class TestSpectrumFormT0:
    def test_T_zero_gives_linear_in_omega(self):
        """At T = 0, N(ω) → 2ℏω/τ_0, linear in ω."""
        omega = 1.0
        N = kms_noise_spectrum(omega, T_kelvin=0.0)
        expected = 2 * HBAR * omega / TAU_0_SEC
        assert abs(N - expected) / expected < 1e-12

    def test_S_h_lorentzian_modulation(self):
        """S_h(ω, T=0) = (2ℏω/τ_0) / (1 + (ωτ_0)²) — Lorentzian
        modulation of the linear noise spectrum."""
        omega = 1.0 / TAU_0_SEC  # at peak
        S = spectral_density_h(omega, T_kelvin=0.0)
        # At peak, S = (2ℏω/τ_0) / 2 = ℏω/τ_0
        expected = HBAR * omega / TAU_0_SEC
        assert abs(S - expected) / expected < 1e-10


# ─────────────────────────────────────────────────────────────────────
# Spectral peak — the load-bearing characteristic frequency
# ─────────────────────────────────────────────────────────────────────


class TestSpectralPeak:
    def test_peak_at_inverse_tau(self):
        """Spectral peak at ω = 1/τ_0."""
        omega_peak = spectral_peak_omega_T0()
        expected = 1.0 / TAU_0_SEC
        assert abs(omega_peak - expected) / expected < 1e-12

    def test_T_at_peak_is_about_5_8e_minus_27(self):
        """T_peak = ℏ/(τ_0 k_B) ≈ 5.78×10⁻²⁷ K."""
        T_peak = temperature_from_spectral_peak()
        expected = HBAR / (TAU_0_SEC * K_B)
        assert abs(T_peak - expected) / expected < 1e-12
        # Pin the order of magnitude
        assert 5e-27 < T_peak < 7e-27

    def test_T_peak_below_CMB_by_27_orders(self):
        """The spectral-peak temperature is 27 orders of magnitude
        below CMB. This is the load-bearing finding: framework's
        noise kernel at T = 0 has natural temperature scale
        astronomically below observed CMB."""
        T_peak = temperature_from_spectral_peak()
        log_diff = math.log10(T_CMB_K) - math.log10(T_peak)
        assert 26 < log_diff < 28


# ─────────────────────────────────────────────────────────────────────
# UV cutoff — Planck-scale temperature
# ─────────────────────────────────────────────────────────────────────


class TestUVCutoff:
    def test_planck_cutoff_gives_planck_T(self):
        """ℏω_Planck/k_B ≈ T_Planck ≈ 1.4×10³² K."""
        T_uv = temperature_from_uv_cutoff(OMEGA_PLANCK_HZ)
        # T_PLANCK_K computed from constants
        assert abs(T_uv - T_PLANCK_K) / T_PLANCK_K < 1e-3
        assert 1e32 < T_uv < 2e32


# ─────────────────────────────────────────────────────────────────────
# UV-divergent variance
# ─────────────────────────────────────────────────────────────────────


class TestVarianceLogDivergent:
    def test_variance_grows_with_cutoff(self):
        """The variance integral is logarithmically UV-divergent.
        Different UV cutoffs give different variances."""
        var_natural = variance_h_integrated_T0(omega_uv_hz=10.0/TAU_0_SEC)
        var_planck = variance_h_integrated_T0(omega_uv_hz=OMEGA_PLANCK_HZ)
        assert var_planck > var_natural
        assert var_planck / var_natural > 50  # log-divergent → large ratio


# ─────────────────────────────────────────────────────────────────────
# Shape is NOT Planck/Bose-Einstein
# ─────────────────────────────────────────────────────────────────────


class TestSpectrumNotPlanck:
    def test_framework_S_h_has_T0_form_documented(self):
        result = shape_difference_from_planck()
        assert "Lorentzian" in result["framework_S_h_T0_form"]
        assert "Bose-Einstein" in result["planck_form_any_T"]

    def test_structural_implication_documented(self):
        result = shape_difference_from_planck()
        impl = result["structural_implication"]
        assert "NOT" in impl  # explicit non-thermal claim
        assert "thermal" in impl.lower()


# ─────────────────────────────────────────────────────────────────────
# Master verdict
# ─────────────────────────────────────────────────────────────────────


class TestMasterVerdict:
    def test_runs_without_error(self):
        result = genesis_noise_kernel_attempt()
        assert "spectral_peak" in result
        assert "characteristic_temperatures" in result
        assert "verdict" in result

    def test_verdict_states_structurally_wrong(self):
        """The verdict must explicitly state Genesis Claim 1's
        thermal-spectrum framing is structurally wrong."""
        result = genesis_noise_kernel_attempt()
        verdict = result["verdict"]
        assert "WRONG" in verdict.upper() or "NOT" in verdict

    def test_verdict_mentions_audit_connection(self):
        """The verdict must connect to the #15 T_c provenance audit."""
        result = genesis_noise_kernel_attempt()
        verdict = result["verdict"]
        assert "#15" in verdict or "audit" in verdict.lower()

    def test_verdict_does_not_resolve_audit(self):
        """The verdict must explicitly state genesis investigation
        does NOT resolve the audit."""
        result = genesis_noise_kernel_attempt()
        verdict = result["verdict"]
        assert "does NOT resolve" in verdict or "not resolve" in verdict.lower()

    def test_scope_notice_disclaims_CMB_match(self):
        """Scope notice must explicitly state this does NOT claim
        the framework produces CMB temperature."""
        result = genesis_noise_kernel_attempt()
        scope = result["scope_notice"]
        assert "CMB" in scope
        assert "NOT claim" in scope or "Does NOT" in scope
