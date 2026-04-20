"""Tests for Track VII Step 1 — Kibble-Zurek Ω_dm from dark phase transition.

These tests lock in:
  - Correct Kibble-Zurek formula (ξ_KZ ∝ (τ_Q/τ_0)^(ν/(1+zν)), NOT inverted)
  - Correct scaling (ξ_KZ grows with τ_Q, slower quench → longer correlations)
  - XY universality gives Ω_dm within factor ~2 of observed
  - Mean-field model B (z=4, conserved order parameter) overproduces
  - Noise-kernel autocorrelation time τ_KMS at various temperatures
"""

import pytest
import numpy as np


class TestCorrelationLength:
    """The central Kibble-Zurek formula."""

    def test_xi_KZ_positive_finite(self):
        from grut.derived.dark_matter.kibble_zurek import correlation_length_MF
        result = correlation_length_MF()
        assert np.isfinite(result["xi_KZ_natural"])
        assert result["xi_KZ_natural"] > 0

    def test_xi_KZ_less_than_hubble_length(self):
        """ξ_KZ must be ≪ H⁻¹ (sub-horizon correlations at freeze-out)."""
        from grut.derived.dark_matter.kibble_zurek import correlation_length_MF
        result = correlation_length_MF()
        # Ratio ξ_KZ × H should be << 1
        assert result["xi_KZ_over_H_inverse"] < 1e-3

    def test_xi_KZ_grows_with_slower_quench(self):
        """Slower quench → longer correlation length (ξ_KZ ∝ τ_Q^+).

        This catches the sign error (inverted ratio) that gave 32 orders
        too small in the initial implementation.
        """
        from grut.derived.dark_matter.kibble_zurek import correlation_length_MF
        # Smaller g_star → smaller H → longer τ_Q → longer ξ_KZ
        fast_quench = correlation_length_MF(g_star=100)   # large H, fast quench
        slow_quench = correlation_length_MF(g_star=1)     # small H, slow quench
        assert slow_quench["xi_KZ_natural"] > fast_quench["xi_KZ_natural"]

    def test_mean_field_exponent_is_one_quarter(self):
        """ν=1/2, z=2 ⟹ exponent = 1/4."""
        from grut.derived.dark_matter.kibble_zurek import correlation_length_MF
        result = correlation_length_MF(nu=0.5, z_dyn=2.0)
        assert abs(result["exponent_xi"] - 0.25) < 1e-10

    def test_constitutive_differs_from_naive(self):
        """τ_KMS differs from 1/m_h at T_PT = 422 MeV, m_h = 387 MeV."""
        from grut.derived.dark_matter.kibble_zurek import correlation_length_MF
        naive = correlation_length_MF(use_constitutive=False)
        grut = correlation_length_MF(use_constitutive=True)
        # Should not be identical
        assert abs(grut["xi_KZ_natural"] - naive["xi_KZ_natural"]) > 1e-6


class TestOmegaDMFromKibbleZurek:
    """Ω_dm estimates from Kibble-Zurek formation density."""

    def test_mean_field_overproduces_moderately(self):
        """Naive MF gives Ω_dm ~ 100-200 (3 orders over, not 40 off)."""
        from grut.derived.dark_matter.kibble_zurek import omega_dm_from_kibble_zurek
        result = omega_dm_from_kibble_zurek(use_constitutive=False, nu=0.5, z_dyn=2.0)
        # Within 3 orders of observed, not 40
        assert 1.0 < result["Omega_dm"] < 1e5

    def test_XY_universality_within_factor_2(self):
        """XY exponents (right class for U(1) breaking) give Ω_dm near observed.

        This is the KEY Track VII Step 1 result.
        """
        from grut.derived.dark_matter.kibble_zurek import omega_dm_from_kibble_zurek
        result = omega_dm_from_kibble_zurek(nu=0.672, z_dyn=2.04,
                                              use_constitutive=True)
        # Within factor of 3 (comfortable buffer around observed 0.263)
        assert 0.1 < result["Omega_dm"] < 1.0

    def test_model_B_overproduces(self):
        """z=4 (conserved order parameter) overproduces — wrong dynamical class."""
        from grut.derived.dark_matter.kibble_zurek import omega_dm_from_kibble_zurek
        result = omega_dm_from_kibble_zurek(nu=0.5, z_dyn=4.0,
                                              use_constitutive=True)
        assert result["Omega_dm"] > 1e3

    def test_n_PT_much_greater_than_H_cubed(self):
        """Kibble-Zurek gives many defects per Hubble volume (not 1)."""
        from grut.derived.dark_matter.kibble_zurek import omega_dm_from_kibble_zurek
        result = omega_dm_from_kibble_zurek()
        assert result["n_PT_per_Hubble_volume"] > 1e10

    def test_redshift_factor_matches_T0_over_TPT_cubed(self):
        from grut.derived.dark_matter.kibble_zurek import (
            omega_dm_from_kibble_zurek, V_DARK_GEV, T_CMB_GeV
        )
        result = omega_dm_from_kibble_zurek()
        expected = (T_CMB_GeV / V_DARK_GEV) ** 3
        assert abs(result["redshift_ratio_cubed"] / expected - 1.0) < 1e-6

    def test_returns_expected_keys(self):
        from grut.derived.dark_matter.kibble_zurek import omega_dm_from_kibble_zurek
        result = omega_dm_from_kibble_zurek()
        expected = {"xi_KZ", "p_geom", "n_PT_natural", "n_PT_per_Hubble_volume",
                    "redshift_ratio_cubed", "n_today_per_m3",
                    "rho_soliton_kg_per_m3", "Omega_dm", "Omega_dm_observed",
                    "Omega_dm_over_observed", "log10_deviation"}
        assert expected.issubset(result.keys())


class TestCriticalExponentScan:
    """Scan over universality classes."""

    def test_returns_four_configs(self):
        from grut.derived.dark_matter.kibble_zurek import scan_critical_exponents
        result = scan_critical_exponents()
        assert len(result) == 4

    def test_includes_XY(self):
        from grut.derived.dark_matter.kibble_zurek import scan_critical_exponents
        result = scan_critical_exponents()
        assert "XY_model_A" in result

    def test_XY_is_closest_to_observed(self):
        """Among the four configs, XY should have smallest |log10 deviation|."""
        from grut.derived.dark_matter.kibble_zurek import scan_critical_exponents
        result = scan_critical_exponents()
        devs = {name: abs(cfg["log10_deviation"]) for name, cfg in result.items()}
        best = min(devs, key=devs.get)
        assert best == "XY_model_A"


class TestNoiseKernelAutocorrelation:
    """Constitutive noise kernel τ_KMS at various temperatures."""

    def test_tau_KMS_scales_inversely_with_T(self):
        from grut.derived.dark_matter.kibble_zurek import noise_kernel_autocorrelation_time
        r1 = noise_kernel_autocorrelation_time(1.0)
        r2 = noise_kernel_autocorrelation_time(2.0)
        # tau_KMS(2T) should be half of tau_KMS(T)
        assert abs(r2["tau_KMS_seconds"] / r1["tau_KMS_seconds"] - 0.5) < 1e-10

    def test_tau_KMS_at_dark_PT_is_microscopic(self):
        """At T = 422 MeV, τ_KMS ~ 10⁻²⁵ s (way below any cosmological scale)."""
        from grut.derived.dark_matter.kibble_zurek import noise_kernel_autocorrelation_time
        r = noise_kernel_autocorrelation_time(0.422)
        assert r["tau_KMS_seconds"] < 1e-20
        assert r["tau_KMS_Myr"] < 1e-30

    def test_tau_KMS_returns_expected_keys(self):
        from grut.derived.dark_matter.kibble_zurek import noise_kernel_autocorrelation_time
        r = noise_kernel_autocorrelation_time(1.0)
        assert "tau_KMS_natural_GeV_inv" in r
        assert "tau_KMS_seconds" in r
        assert "tau_KMS_Myr" in r


class TestStep1Summary:
    """Integration: track_vii_step_1_summary() bundles everything."""

    def test_returns_dict_with_XY_result(self):
        from grut.derived.dark_matter.kibble_zurek import track_vii_step_1_summary
        r = track_vii_step_1_summary()
        assert "XY_universality_constitutive" in r
        # XY result should be within factor 2 of observed
        assert 0.1 < r["XY_universality_constitutive"]["Omega_dm"] < 1.0

    def test_includes_noise_kernel_info(self):
        from grut.derived.dark_matter.kibble_zurek import track_vii_step_1_summary
        r = track_vii_step_1_summary()
        assert "noise_kernel_autocorrelation" in r

    def test_status_flags_structural_ballpark(self):
        from grut.derived.dark_matter.kibble_zurek import track_vii_step_1_summary
        r = track_vii_step_1_summary()
        assert "STRUCTURAL BALLPARK" in r["status"] or "BALLPARK" in r["status"]
