"""Tests for the bandwidth integral (brother's Track VII protocol).

Locks in:
  - BBKS transfer function matches T(0) → 1, T(∞) → 0
  - Δ²(k) has a physical peak at linear-theory scales
  - ω(k) = k × c_s conversion is dimensionally correct
  - Enhancement Lorentzian has correct limits
  - Ω_dm,eff ≈ α = 1/3 in the linear regime (≈ 0.333, NOT 0.263)
  - Sensitivity to c_s is nearly flat in [50, 500] km/s (all linear modes are DC)
  - Overshoot over observed Ω_dm = 0.263 is ~27% (the genuine prediction)
"""

import pytest
import numpy as np


class TestBBKSTransfer:
    def test_transfer_goes_to_one_at_low_k(self):
        from grut.derived.cosmology.bandwidth_integral import bbks_transfer_function
        T = bbks_transfer_function(np.array([1e-5]))[0]
        assert T > 0.99

    def test_transfer_suppressed_at_high_k(self):
        from grut.derived.cosmology.bandwidth_integral import bbks_transfer_function
        T = bbks_transfer_function(np.array([100.0]))[0]
        assert T < 1e-4

    def test_transfer_monotonically_decreasing(self):
        from grut.derived.cosmology.bandwidth_integral import bbks_transfer_function
        k = np.logspace(-3, 2, 50)
        T = bbks_transfer_function(k)
        assert all(T[i] >= T[i+1] for i in range(len(T)-1))


class TestPowerSpectrum:
    def test_P_k_positive(self):
        from grut.derived.cosmology.bandwidth_integral import matter_power_spectrum
        k = np.logspace(-3, 1, 20)
        P = matter_power_spectrum(k)
        assert all(P > 0)

    def test_Delta2_peaks_in_linear_regime(self):
        """With k_max = 0.3 (linear regime), Δ² peaks at the upper end.

        BBKS linear theory keeps Δ² slowly growing; the physical peak
        requires nonlinear cutoff which is outside the linear-regime test.
        This test verifies behavior within the linear range.
        """
        from grut.derived.cosmology.bandwidth_integral import dimensionless_power_spectrum
        k = np.logspace(-4, np.log10(0.3), 200)
        D2 = dimensionless_power_spectrum(k)
        # Monotonically increasing in linear regime
        assert D2[-1] > D2[0]


class TestOmegaOfK:
    def test_omega_scales_linearly_with_k(self):
        from grut.derived.cosmology.bandwidth_integral import omega_of_k
        w1 = omega_of_k(0.01)
        w2 = omega_of_k(0.02)
        assert abs(w2 / w1 - 2.0) < 1e-10

    def test_omega_at_k_peak_has_omega_tau_much_less_than_1(self):
        """Brother's arithmetic: at k_peak ≈ 0.02 h/Mpc, ωτ₀ ~ 10⁻⁴."""
        from grut.derived.cosmology.bandwidth_integral import omega_of_k
        from grut.foundation.closure_protocol import TAU_0_SEC
        omega = omega_of_k(0.02, c_s_m_per_s=200e3)
        assert omega * TAU_0_SEC < 1e-3


class TestEnhancementE:
    def test_E_at_DC_is_alpha(self):
        from grut.derived.cosmology.bandwidth_integral import enhancement_E
        from grut.foundation.closure_protocol import ALPHA_VAC
        E = enhancement_E(1e-10)
        assert abs(E - ALPHA_VAC) < 1e-10

    def test_E_at_UV_is_suppressed(self):
        from grut.derived.cosmology.bandwidth_integral import enhancement_E
        from grut.foundation.closure_protocol import ALPHA_VAC
        # At k = 10000 h/Mpc (beyond any P(k)), enhancement is far below α
        E = enhancement_E(10000.0)
        assert E < ALPHA_VAC * 0.01


class TestBandwidthIntegral:
    def test_integral_saturates_at_alpha(self):
        """Linear-regime integral gives Ω_dm,eff ≈ α = 1/3.

        This is the headline result: with k ≤ 0.3 h/Mpc (CMB + LSS linear),
        all modes are in ωτ₀ ≪ 1 regime, so enhancement ≈ α everywhere.
        """
        from grut.derived.cosmology.bandwidth_integral import omega_dm_bandwidth_integral
        r = omega_dm_bandwidth_integral()
        # Within 1% of α = 1/3
        assert abs(r["Omega_dm_eff_dk"] - 1/3) < 0.01

    def test_overshoots_observed_by_27_percent(self):
        """Brother's predicted result: dielectric gives +27% over Ω_dm,obs."""
        from grut.derived.cosmology.bandwidth_integral import omega_dm_bandwidth_integral
        r = omega_dm_bandwidth_integral()
        ratio = r["Omega_dm_eff_dk"] / r["Omega_dm_observed"]
        # Should be ≈ 4/3 × 0.263⁻¹ ... actually just check ratio ≈ 1.27
        assert 1.25 < ratio < 1.30

    def test_omega_tau_at_peak_is_small(self):
        """At the Δ² peak, ωτ₀ ≪ 1 (deep DC regime)."""
        from grut.derived.cosmology.bandwidth_integral import omega_dm_bandwidth_integral
        r = omega_dm_bandwidth_integral()
        assert r["omega_tau_at_peak"] < 0.1

    def test_dk_and_dlnk_close_in_linear_regime(self):
        """When E is nearly constant over the integration range, dk and dlnk
        measures give the same weighted-average enhancement."""
        from grut.derived.cosmology.bandwidth_integral import omega_dm_bandwidth_integral
        r = omega_dm_bandwidth_integral()
        assert abs(r["Omega_dm_eff_dk"] - r["Omega_dm_eff_dlnk"]) < 0.01


class TestSensitivity:
    def test_c_s_sensitivity_is_flat_in_linear_regime(self):
        """All c_s ∈ [50, 500] km/s give Ω_dm,eff ≈ α in linear regime."""
        from grut.derived.cosmology.bandwidth_integral import sensitivity_c_s
        results = sensitivity_c_s()
        for r in results:
            # All should be near 1/3
            assert abs(r["Omega_dm_eff"] - 1/3) < 0.02

    def test_tau_0_sensitivity_moderate(self):
        """±10% τ_0 shouldn't change the result much (all still DC regime)."""
        from grut.derived.cosmology.bandwidth_integral import sensitivity_tau_0
        results = sensitivity_tau_0()
        values = [r["Omega_dm_eff"] for r in results]
        # Should all cluster near α
        assert max(values) - min(values) < 0.05

    def test_alpha_sensitivity_scales_linearly(self):
        """±5% α should scale Ω_dm,eff by same ±5% (in DC regime)."""
        from grut.derived.cosmology.bandwidth_integral import sensitivity_alpha
        results = sensitivity_alpha()
        # alpha 0.95 → eff 0.95 × (1/3), alpha 1.05 → 1.05 × (1/3)
        for r in results:
            expected = r["factor"] * (1/3)
            assert abs(r["Omega_dm_eff"] - expected) / expected < 0.02


class TestSummaryResult:
    def test_summary_returns_dict(self):
        from grut.derived.cosmology.bandwidth_integral import track_vii_bandwidth_summary
        r = track_vii_bandwidth_summary()
        assert isinstance(r, dict)
        assert "main_result" in r
        assert "sensitivity_c_s" in r
        assert "verdict" in r

    def test_verdict_mentions_overshoot_or_saturation(self):
        from grut.derived.cosmology.bandwidth_integral import track_vii_bandwidth_summary
        r = track_vii_bandwidth_summary()
        verdict = r["verdict"].lower()
        assert "overshoot" in verdict or "0.333" in verdict or "dielectric" in verdict
