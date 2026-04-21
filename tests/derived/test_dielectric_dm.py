"""Tests for Track VII REFRAMED — dielectric interpretation of Ω_dm.

Locks in:
  - α = 1/3 exactly (Genesis Codex v11.1 App H: α = 1/d, d = 3)
  - n_g(DC) = √(4/3) ≈ 1.15470
  - n_g(ω → ∞) → 1 (GR recovered at high frequency)
  - Solar system: enhancement ~ 0 (no deviation from GR at precision scales)
  - CMB acoustic peak: ωτ < 0.1 so enhancement is ~ α (peaks survive)
  - Galaxy rotation: ωτ ~ 1 so enhancement is partial (~0.19)
  - Bullet Cluster: first-cut offset within an order of magnitude of observed
  - Summary reports three calculations and status label REFRAMED
"""

import pytest
import numpy as np


class TestRefractiveIndex:
    """n_g(ω) and enhancement basic behavior."""

    def test_alpha_equals_one_third_exactly(self):
        from grut.derived.cosmology.dielectric_dm import ALPHA_VACUUM
        assert abs(ALPHA_VACUUM - 1/3) < 1e-15

    def test_n_g_DC_is_sqrt_4_over_3(self):
        from grut.derived.cosmology.dielectric_dm import n_g_refractive
        ng = n_g_refractive(omega_Hz=0.0)
        expected = np.sqrt(4/3)
        assert abs(ng - expected) < 1e-12
        # Matches the three-routes paper value
        assert abs(ng - 1.1547) < 0.0001

    def test_n_g_high_frequency_reduces_to_GR(self):
        from grut.derived.cosmology.dielectric_dm import n_g_refractive
        # At very high ω, enhancement vanishes, n_g → 1 (standard GR)
        ng = n_g_refractive(omega_Hz=1e10)
        assert abs(ng - 1.0) < 1e-6

    def test_enhancement_at_DC_equals_alpha(self):
        from grut.derived.cosmology.dielectric_dm import enhancement, ALPHA_VACUUM
        assert abs(enhancement(0.0) - ALPHA_VACUUM) < 1e-15

    def test_enhancement_monotonically_decreases_with_frequency(self):
        from grut.derived.cosmology.dielectric_dm import enhancement
        freqs = np.logspace(-20, -10, 100)
        vals = [enhancement(f) for f in freqs]
        assert all(vals[i] >= vals[i+1] for i in range(len(vals)-1))


class TestScalesScan:
    """Enhancement at canonical cosmological scales."""

    def test_solar_system_has_essentially_zero_enhancement(self):
        """GR must be recovered at precision-test scales."""
        from grut.derived.cosmology.dielectric_dm import enhancement_at_common_scales
        result = enhancement_at_common_scales()
        assert result["solar_system"]["n_g_squared_minus_1"] < 1e-10

    def test_cosmic_expansion_gives_full_alpha(self):
        """At DC, enhancement = α = 1/3."""
        from grut.derived.cosmology.dielectric_dm import enhancement_at_common_scales
        result = enhancement_at_common_scales()
        assert abs(result["cosmic_expansion"]["n_g_squared_minus_1"] - 1/3) < 0.01

    def test_cmb_acoustic_peak_has_full_enhancement(self):
        """CRITICAL: the modes that set CMB peaks must feel the enhancement.

        Sound-horizon modes have ωτ ≈ 0.05 ≪ 1, so enhancement ≈ α.
        Without this, the CMB kill-condition would trigger.
        """
        from grut.derived.cosmology.dielectric_dm import enhancement_at_common_scales
        result = enhancement_at_common_scales()
        e_acoustic = result["CMB_acoustic_peak"]["n_g_squared_minus_1"]
        # Within 5% of α
        assert abs(e_acoustic - 1/3) / (1/3) < 0.05

    def test_galaxy_rotation_is_intermediate_regime(self):
        """Galaxy rotation (200 km/s @ 10 kpc) has ωτ ~ 1, partial enhancement."""
        from grut.derived.cosmology.dielectric_dm import enhancement_at_common_scales
        result = enhancement_at_common_scales()
        e_gal = result["galaxy_rotation"]["n_g_squared_minus_1"]
        # Should be between 0.1 and 0.3
        assert 0.1 < e_gal < 0.3

    def test_dwarf_galaxy_more_suppressed_than_cluster(self):
        """Smaller/slower systems → higher ωτ → more suppressed enhancement."""
        from grut.derived.cosmology.dielectric_dm import enhancement_at_common_scales
        result = enhancement_at_common_scales()
        e_dwarf = result["dwarf_galaxy"]["n_g_squared_minus_1"]
        e_cluster = result["galaxy_cluster"]["n_g_squared_minus_1"]
        assert e_dwarf < e_cluster

    def test_cmb_recombination_dynamical_is_high_freq(self):
        """ω = 1/t_rec is HIGH-freq regime (not the scale that sets peaks)."""
        from grut.derived.cosmology.dielectric_dm import enhancement_at_common_scales
        result = enhancement_at_common_scales()
        # 1/t_rec dynamical frequency is in high-ω regime
        assert result["CMB_recombination_dyn"]["omega_tau"] > 10


class TestBandwidthIntegral:
    """First-cut Ω_dm estimate from bandwidth integral."""

    def test_alpha_is_27_percent_above_observed(self):
        """DC limit α = 0.333 exceeds observed Ω_dm = 0.263 by ~27%."""
        from grut.derived.cosmology.dielectric_dm import omega_dm_bandwidth_estimate
        result = omega_dm_bandwidth_estimate()
        ratio = result["DC_upper_bound_vs_observed"]
        assert abs(ratio - 1.27) < 0.01

    def test_returns_expected_keys(self):
        from grut.derived.cosmology.dielectric_dm import omega_dm_bandwidth_estimate
        result = omega_dm_bandwidth_estimate()
        for k in ["alpha_d_equals_3", "enhancement_DC_cosmic",
                  "observed_Omega_dm", "DC_upper_bound_vs_observed",
                  "interpretation", "status"]:
            assert k in result

    def test_status_flags_first_cut(self):
        from grut.derived.cosmology.dielectric_dm import omega_dm_bandwidth_estimate
        result = omega_dm_bandwidth_estimate()
        assert "FIRST-CUT" in result["status"]


class TestBulletCluster:
    """Memory-kernel retardation offset vs observed 720 kpc."""

    def test_matter_motion_offset_within_order_of_magnitude(self):
        """v × τ₀ gives ~130 kpc — within factor ~6 of observed 720 kpc."""
        from grut.derived.cosmology.dielectric_dm import bullet_cluster_retardation
        result = bullet_cluster_retardation()
        # Observed is 720 kpc, naive is 128 kpc. Factor 5.6 off.
        # Require the naive value to be between 10 and 1000 kpc.
        assert 10 < result["offset_matter_motion_kpc"] < 1000

    def test_causal_offset_is_upper_bound(self):
        """c × τ₀ = 12.8 Mpc is an upper bound on retardation offset."""
        from grut.derived.cosmology.dielectric_dm import bullet_cluster_retardation
        result = bullet_cluster_retardation()
        assert result["offset_causal_upper_bound_kpc"] > result["offset_observed_kpc"]
        assert result["offset_causal_upper_bound_kpc"] > 10000  # > 10 Mpc

    def test_matter_motion_less_than_observed(self):
        """v × τ₀ < observed — suggests retardation geometry amplifies offset."""
        from grut.derived.cosmology.dielectric_dm import bullet_cluster_retardation
        result = bullet_cluster_retardation()
        assert result["offset_matter_motion_kpc"] < result["offset_observed_kpc"]


class TestCMBKillCondition:
    """The acoustic-peak modes must feel enhancement for the interpretation to survive."""

    def test_acoustic_peak_has_substantial_enhancement(self):
        """Sound-horizon modes at recombination: ωτ << 1 → enhancement ~ α."""
        from grut.derived.cosmology.dielectric_dm import cmb_acoustic_enhancement
        result = cmb_acoustic_enhancement()
        assert result["acoustic_peak_enhancement_survives"]

    def test_recombination_Hubble_is_high_frequency(self):
        """Background Hubble rate at z=1090 is high-ω (~10-100 × τ₀⁻¹)."""
        from grut.derived.cosmology.dielectric_dm import cmb_acoustic_enhancement
        result = cmb_acoustic_enhancement()
        omega_tau_H_rec = result["omega_tau_dimensionless"]["H_recombination"]
        assert omega_tau_H_rec > 10

    def test_verdict_includes_boltzmann_note(self):
        """Full test requires Boltzmann code with n_g(ω) — flagged honestly."""
        from grut.derived.cosmology.dielectric_dm import cmb_acoustic_enhancement
        result = cmb_acoustic_enhancement()
        assert "Boltzmann" in result["verdict"]


class TestDielectricSummary:
    """Integrated Track VII reframing summary."""

    def test_reports_zero_free_knobs(self):
        from grut.derived.cosmology.dielectric_dm import track_vii_dielectric_summary
        result = track_vii_dielectric_summary()
        assert result["fixed_inputs"]["free_knobs"] == "NONE"

    def test_status_label_says_REFRAMED(self):
        from grut.derived.cosmology.dielectric_dm import track_vii_dielectric_summary
        result = track_vii_dielectric_summary()
        assert "REFRAMED" in result["status_label"]

    def test_all_three_calculations_present(self):
        from grut.derived.cosmology.dielectric_dm import track_vii_dielectric_summary
        result = track_vii_dielectric_summary()
        assert "calc_1_bandwidth_integral" in result
        assert "calc_2_bullet_cluster" in result
        assert "calc_3_cmb_acoustic" in result

    def test_physical_picture_mentions_boundary_condition(self):
        """R = 1.15428 should be called a fixed boundary condition, not dynamical."""
        from grut.derived.cosmology.dielectric_dm import track_vii_dielectric_summary
        result = track_vii_dielectric_summary()
        assert "boundary condition" in result["physical_picture"]

    def test_research_priority_order_is_three_items(self):
        from grut.derived.cosmology.dielectric_dm import track_vii_dielectric_summary
        result = track_vii_dielectric_summary()
        assert len(result["research_priority_order"]) == 3
