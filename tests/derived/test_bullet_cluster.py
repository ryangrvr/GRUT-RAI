"""Tests for grut.derived.cluster.bullet_cluster — Track VII's primary
cluster-scale falsifier.

Verifies:
  - Simple v × τ_0 estimate produces the documented 130-200 kpc range
  - Full memory-kernel convolution lies in the observation band
    (within factor 2 of the observed ~150 kpc gas-to-lensing offset)
  - The kernel result is bracketed by the v_final and v_initial simple
    estimates (the convolution averages the velocity history, so it
    must lie between the post-collision and pre-collision values)
  - Kinematic v × t_since reproduces the cluster-cluster separation
    of 720 kpc (this is NOT a GRUT-specific prediction — it tests
    that we computed kinematics correctly)
"""

import pytest

from grut.derived.cluster.bullet_cluster import (
    BULLET_OBS,
    BulletClusterObs,
    bullet_cluster_report,
    gas_trajectory,
    grut_offset_kernel_convolution_kpc,
    grut_offset_kernel_convolution_m,
    grut_offset_simple_kpc,
    grut_offset_simple_m,
    kinematic_cluster_separation_kpc,
    kinematic_cluster_separation_m,
    verify,
)
from grut.foundation.closure_protocol import TAU_0_SEC


class TestKinematicSeparation:
    """v × t_since reproduces the cluster-to-cluster separation —
    independent of GRUT, just kinematics."""

    def test_separation_is_720_kpc(self):
        sep = kinematic_cluster_separation_kpc()
        assert abs(sep - 720.0) / 720.0 < 0.05

    def test_scales_linearly_with_velocity(self):
        a = kinematic_cluster_separation_kpc(v_km_s=1000)
        b = kinematic_cluster_separation_kpc(v_km_s=2000)
        assert abs(b - 2 * a) < 1e-6

    def test_scales_linearly_with_time(self):
        a = kinematic_cluster_separation_kpc(t_since_Myr=50)
        b = kinematic_cluster_separation_kpc(t_since_Myr=100)
        assert abs(b - 2 * a) < 1e-6


class TestSimpleGRUTOffset:
    """v × τ_0 — leading-order GRUT prediction."""

    def test_v_final_around_130_kpc(self):
        """3000 km/s × 41.9 Myr ≈ 130 kpc."""
        offset = grut_offset_simple_kpc(BULLET_OBS.v_final_km_s)
        assert 120 < offset < 140

    def test_v_initial_around_200_kpc(self):
        """4700 km/s × 41.9 Myr ≈ 200 kpc."""
        offset = grut_offset_simple_kpc(BULLET_OBS.v_initial_km_s)
        assert 190 < offset < 210

    def test_zero_velocity_zero_offset(self):
        assert grut_offset_simple_kpc(0.0) == 0.0

    def test_scales_linearly_with_velocity(self):
        a = grut_offset_simple_kpc(1000)
        b = grut_offset_simple_kpc(3000)
        assert abs(b - 3 * a) / a < 1e-12


class TestGasTrajectory:
    """Piecewise-linear deceleration model is well-defined."""

    def test_now_is_origin(self):
        """At t = now (s = 0), gas is at x = 0."""
        x = gas_trajectory(
            t_offset_sec=0.0,
            v_initial_m_s=4700e3,
            v_final_m_s=3000e3,
            t_since_pericenter_sec=150e6 * 3.156e7,
        )
        assert x == 0.0

    def test_negative_offset_returns_zero(self):
        """Future is not represented (one-sided kernel)."""
        x = gas_trajectory(
            t_offset_sec=-1.0,
            v_initial_m_s=4700e3,
            v_final_m_s=3000e3,
            t_since_pericenter_sec=150e6 * 3.156e7,
        )
        assert x == 0.0

    def test_post_collision_uses_v_final(self):
        """For 0 < s < t_since, gas moves at v_final."""
        v_final = 3000e3
        s = 50e6 * 3.156e7  # 50 Myr ago
        x = gas_trajectory(
            t_offset_sec=s,
            v_initial_m_s=4700e3,
            v_final_m_s=v_final,
            t_since_pericenter_sec=150e6 * 3.156e7,
        )
        # Position 50 Myr ago: gas was AHEAD of current spot by v_final × s
        assert abs(x - v_final * s) / (v_final * s) < 1e-6

    def test_pre_collision_uses_v_initial(self):
        """For s ≫ t_since + t_collision, gas moves at v_initial."""
        v_initial = 4700e3
        v_final = 3000e3
        s = 1000e6 * 3.156e7  # 1 Gyr ago — well pre-collision
        x = gas_trajectory(
            t_offset_sec=s,
            v_initial_m_s=v_initial,
            v_final_m_s=v_final,
            t_since_pericenter_sec=150e6 * 3.156e7,
        )
        # Position must grow approximately linearly in s with slope v_initial
        assert x > v_final * s  # faster than v_final → was at higher position


class TestKernelConvolution:
    """Full memory-kernel convolution gives a result in the
    observation band, bracketed by the simple-estimate envelope."""

    def test_convolution_in_band(self):
        """Result lies within factor 2 of observed ~150 kpc."""
        offset = grut_offset_kernel_convolution_kpc()
        assert 75 < offset < 300  # half to double of 150 kpc

    def test_convolution_close_to_v_final_simple(self):
        """For τ_0 ≪ t_since, the kernel sees mostly post-collision
        gas, so the result should be dominated by v_final × τ_0."""
        kernel_offset = grut_offset_kernel_convolution_kpc()
        simple_v_final = grut_offset_simple_kpc(BULLET_OBS.v_final_km_s)
        # Kernel result should be within 10% of v_final × τ_0
        assert abs(kernel_offset - simple_v_final) / simple_v_final < 0.10

    def test_convolution_bracketed(self):
        """v_final × τ_0 ≤ kernel result ≤ v_initial × τ_0."""
        kernel = grut_offset_kernel_convolution_kpc()
        v_final = grut_offset_simple_kpc(BULLET_OBS.v_final_km_s)
        v_initial = grut_offset_simple_kpc(BULLET_OBS.v_initial_km_s)
        assert v_final - 1.0 <= kernel <= v_initial + 1.0

    def test_convolution_increases_with_velocity(self):
        a = grut_offset_kernel_convolution_kpc(v_initial_km_s=2000, v_final_km_s=2000)
        b = grut_offset_kernel_convolution_kpc(v_initial_km_s=4000, v_final_km_s=4000)
        assert b > a


class TestObservationComparison:
    """The framework's prediction matches observation within factor 2."""

    def test_grut_in_observation_band(self):
        rep = bullet_cluster_report()
        assert rep.grut_in_observation_band

    def test_kinematic_matches_observation(self):
        rep = bullet_cluster_report()
        assert rep.kinematic_matches_observation

    def test_match_factor_under_2(self):
        rep = bullet_cluster_report()
        ratio = rep.grut_kernel_convolution_kpc / rep.obs_gas_lensing_kpc
        assert 0.5 < ratio < 2.0

    def test_match_within_factor_1_5(self):
        """Tighter band: GRUT prediction is within 50% of observation."""
        rep = bullet_cluster_report()
        ratio = rep.grut_kernel_convolution_kpc / rep.obs_gas_lensing_kpc
        assert 0.6 < ratio < 1.5  # 130 / 150 ≈ 0.87, well in range


class TestVerifyHarness:

    def test_all_pass(self):
        checks = verify()
        failed = [k for k, v in checks.items() if not v]
        assert not failed, f"Bullet Cluster verify failures: {failed}"


class TestObservationalConstants:
    """Inputs match published Bullet Cluster values."""

    def test_v_initial_in_published_band(self):
        """3000-5000 km/s per Markevitch 2002, Springel & Farrar 2007."""
        assert 3000 <= BULLET_OBS.v_initial_km_s <= 5000

    def test_t_since_in_published_band(self):
        """100-200 Myr per Clowe et al. 2006."""
        assert 100 <= BULLET_OBS.t_since_Myr <= 200

    def test_observed_gas_lensing_offset_in_published_band(self):
        """100-200 kpc per Clowe et al. 2006."""
        assert 100 <= BULLET_OBS.gas_lensing_offset_kpc <= 200


class TestCustomGeometry:
    """The module accepts custom collision parameters — useful for
    sensitivity analysis on cluster-by-cluster basis."""

    def test_custom_obs_via_dataclass(self):
        custom = BulletClusterObs(
            v_initial_km_s=3500,
            v_final_km_s=2500,
            t_since_Myr=120,
            gas_lensing_offset_kpc=140,
            cluster_cluster_separation_kpc=500,
        )
        rep = bullet_cluster_report(obs=custom)
        # 2500 km/s × 41.9 Myr ≈ 107 kpc
        assert 95 < rep.grut_simple_v_final_kpc < 120
