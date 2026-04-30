"""Hardening tests for omega_dm_equals_alpha — promotes from anchored
to computed by pinning the bandwidth integral's documented output:

    Ω_dm,eff = α_vac = 1/3 = 0.3333

via the BBKS-weighted bandwidth integral over linear-regime modes.
"""

import math

import pytest

from grut.foundation.closure_protocol import ALPHA_VAC


class TestBandwidthIntegralProducesAlpha:
    """The Track VII bandwidth integral returns Ω_dm = α = 1/3."""

    def test_returns_one_third_to_4dp(self):
        from grut.derived.cosmology.bandwidth_integral import (
            omega_dm_bandwidth_integral,
        )
        r = omega_dm_bandwidth_integral()
        assert "Omega_dm_eff_dk" in r
        # Result rounds to 0.3333 — within 1e-3 of α_vac = 1/3
        assert abs(r["Omega_dm_eff_dk"] - 1.0 / 3.0) < 1e-3

    def test_uses_alpha_vac_one_third(self):
        from grut.derived.cosmology.bandwidth_integral import (
            omega_dm_bandwidth_integral,
        )
        r = omega_dm_bandwidth_integral()
        assert abs(r["alpha"] - ALPHA_VAC) < 1e-15

    def test_returns_omega_dm_observed_in_dict(self):
        from grut.derived.cosmology.bandwidth_integral import (
            omega_dm_bandwidth_integral,
        )
        r = omega_dm_bandwidth_integral()
        # Planck observed value should be exposed for comparison
        assert "Omega_dm_observed" in r
        assert 0.20 < r["Omega_dm_observed"] < 0.30  # ≈ 0.263

    def test_overshoot_27_percent(self):
        """Documented +27% overshoot vs Planck (0.3333 / 0.263 − 1)."""
        from grut.derived.cosmology.bandwidth_integral import (
            omega_dm_bandwidth_integral,
        )
        r = omega_dm_bandwidth_integral()
        ratio = r["Omega_dm_eff_dk"] / r["Omega_dm_observed"]
        assert 1.20 < ratio < 1.35  # ≈ 1.27


class TestBandwidthSensitivity:
    """Sensitivity to c_s and τ_0 — the result is geometric, not kinematic."""

    def test_insensitive_to_c_s_50_to_500(self):
        """Across c_s = 50–500 km/s, Ω_dm,eff stays at α = 1/3."""
        from grut.derived.cosmology.bandwidth_integral import (
            omega_dm_bandwidth_integral,
        )
        for c_s_km in [50, 100, 200, 350, 500]:
            r = omega_dm_bandwidth_integral(c_s_m_per_s=c_s_km * 1000)
            assert abs(r["Omega_dm_eff_dk"] - 1.0 / 3.0) < 1e-3
