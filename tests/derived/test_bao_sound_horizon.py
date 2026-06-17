"""Tests for grut.derived.cosmology.bao_sound_horizon.

Certifies the self-consistent BAO comparison:
  - CAMB sound horizon for GRUT and Planck cosmologies
  - r_d values physically reasonable and consistent with literature
  - r_d ratio GRUT/Planck within expected range (~+0.76%)
  - Delubac+2015 D_H/r_d self-consistent residual

Key physics result locked in:
  GRUT r_d = 148.21 Mpc (+0.76% vs Planck 147.09 Mpc), driven entirely by
  GRUT's lower ωm = 0.13819 vs Planck ωm = 0.14237 (same ωb, same TCMB).
  Self-consistent D_H/r_d residual = −1.95σ for Delubac+2015 Ly-α at z=2.34.
  Both Planck-calibrated (+1.75σ) and self-consistent (−1.95σ) point to the
  same physical conclusion: GRUT H(z=2.34) is ~2% too high for Ly-α BAO.
"""

import math
import pytest


# ── Shared fixtures ───────────────────────────────────────────────────────────

@pytest.fixture(scope="module")
def sh_grut():
    from grut.derived.cosmology.bao_sound_horizon import grut_sound_horizon
    return grut_sound_horizon()


@pytest.fixture(scope="module")
def sh_planck():
    from grut.derived.cosmology.bao_sound_horizon import planck_sound_horizon
    return planck_sound_horizon()


@pytest.fixture(scope="module")
def comparison():
    from grut.derived.cosmology.bao_sound_horizon import bao_dh_over_rd_comparison
    return bao_dh_over_rd_comparison()


# ── GRUT sound horizon ────────────────────────────────────────────────────────

class TestGRUTSoundHorizon:
    """Verify CAMB-computed GRUT sound horizon is physically reasonable."""

    def test_rdrag_in_physical_range(self, sh_grut):
        """r_d^GRUT lies in [140, 160] Mpc."""
        rd = sh_grut["rdrag"]
        assert 140.0 < rd < 160.0, f"r_d^GRUT = {rd:.3f} Mpc outside [140, 160]"

    def test_zdrag_in_physical_range(self, sh_grut):
        """Drag epoch z_drag lies between 900 and 1200."""
        zd = sh_grut["zdrag"]
        assert 900 < zd < 1200, f"z_drag^GRUT = {zd:.1f} outside [900, 1200]"

    def test_rdrag_expected_value(self, sh_grut):
        """r_d^GRUT ≈ 148.21 Mpc (locked from CAMB computation)."""
        assert abs(sh_grut["rdrag"] - 148.21) < 0.20, (
            f"r_d^GRUT = {sh_grut['rdrag']:.4f} Mpc, expected ~148.21"
        )

    def test_rstar_less_than_rdrag(self, sh_grut):
        """r_star < r_drag: CMB recombination occurs after drag epoch."""
        assert sh_grut["rstar"] < sh_grut["rdrag"], (
            f"r_star={sh_grut['rstar']:.3f} ≥ r_drag={sh_grut['rdrag']:.3f}"
        )

    def test_zstar_greater_than_zdrag(self, sh_grut):
        """z_star > z_drag: recombination at higher z than drag epoch."""
        assert sh_grut["zstar"] > sh_grut["zdrag"]

    def test_params_stored_correctly(self, sh_grut):
        """H0, ombh2, omch2 are stored in the result."""
        from grut.derived.cosmology.bao_sound_horizon import (
            GRUT_H0, GRUT_OMBH2, GRUT_OMCH2
        )
        assert sh_grut["H0"]    == pytest.approx(GRUT_H0)
        assert sh_grut["ombh2"] == pytest.approx(GRUT_OMBH2)
        assert sh_grut["omch2"] == pytest.approx(GRUT_OMCH2)


# ── Planck sound horizon ──────────────────────────────────────────────────────

class TestPlanckSoundHorizon:
    """Verify CAMB-computed Planck sound horizon matches known values."""

    def test_rdrag_near_planck_2018(self, sh_planck):
        """r_d^Planck ≈ 147.09 Mpc — consistent with Planck 2018 Table 2."""
        rd = sh_planck["rdrag"]
        assert abs(rd - 147.09) < 0.20, (
            f"r_d^Planck = {rd:.4f} Mpc, expected ~147.09"
        )

    def test_zdrag_near_1060(self, sh_planck):
        """Drag epoch z_drag ≈ 1060 for Planck cosmology."""
        zd = sh_planck["zdrag"]
        assert abs(zd - 1060) < 5, f"z_drag^Planck = {zd:.2f}, expected ~1060"

    def test_zstar_near_1090(self, sh_planck):
        """CMB recombination z_star ≈ 1090."""
        zs = sh_planck["zstar"]
        assert abs(zs - 1090) < 5, f"z_star^Planck = {zs:.2f}, expected ~1090"


# ── GRUT vs Planck ratio ──────────────────────────────────────────────────────

class TestSoundHorizonRatio:
    """GRUT r_d is slightly larger than Planck's due to lower ωm."""

    def test_grut_rdrag_larger_than_planck(self, sh_grut, sh_planck):
        """r_d^GRUT > r_d^Planck: lower ωm → slower early expansion → larger r_d."""
        assert sh_grut["rdrag"] > sh_planck["rdrag"], (
            f"Expected r_d^GRUT > r_d^Planck, got "
            f"{sh_grut['rdrag']:.3f} vs {sh_planck['rdrag']:.3f}"
        )

    def test_rd_ratio_near_expected(self, sh_grut, sh_planck):
        """r_d ratio GRUT/Planck ≈ 1.0076 (+0.76%)."""
        ratio = sh_grut["rdrag"] / sh_planck["rdrag"]
        assert abs(ratio - 1.0076) < 0.005, (
            f"r_d ratio = {ratio:.5f}, expected ~1.0076"
        )

    def test_rd_ratio_within_2pct(self, sh_grut, sh_planck):
        """r_d ratio is within 2% of unity — a small correction."""
        ratio = sh_grut["rdrag"] / sh_planck["rdrag"]
        assert abs(ratio - 1.0) < 0.02, (
            f"r_d ratio = {ratio:.4f} deviates by > 2% from 1.0"
        )

    def test_same_ombh2_same_recombination_epoch(self, sh_grut, sh_planck):
        """Same ωb → z_star agrees to within 1% between GRUT and Planck."""
        diff_pct = abs(sh_grut["zstar"] / sh_planck["zstar"] - 1.0) * 100
        assert diff_pct < 1.0, (
            f"z_star differs by {diff_pct:.2f}% despite same ωb"
        )


# ── Self-consistent BAO comparison ───────────────────────────────────────────

class TestBaoDhOverRd:
    """Self-consistent D_H(z=2.34)/r_d comparison — Delubac+2015 Ly-α."""

    def test_result_has_required_keys(self, comparison):
        required = {
            "z", "H_grut_km_s_Mpc", "DH_grut_Mpc", "rd_grut_Mpc",
            "rd_planck_Mpc", "rd_ratio_grut_over_planck",
            "DH_over_rd_grut", "DH_over_rd_observed", "sigma",
            "residual_sigma", "reference", "note",
        }
        assert required.issubset(comparison.keys())

    def test_z_is_delubac(self, comparison):
        from grut.derived.cosmology.bao_sound_horizon import DELUBAC_Z
        assert comparison["z"] == pytest.approx(DELUBAC_Z)

    def test_grut_h_at_z234_near_234(self, comparison):
        """H_GRUT(z=2.34) ≈ 234.2 km/s/Mpc."""
        H = comparison["H_grut_km_s_Mpc"]
        assert abs(H - 234.2) < 1.0, f"H_GRUT(z=2.34) = {H:.3f}"

    def test_dh_over_rd_grut_matches_expected(self, comparison):
        """GRUT D_H/r_d ≈ 8.635 (locked from CAMB computation)."""
        dh_rd = comparison["DH_over_rd_grut"]
        assert abs(dh_rd - 8.635) < 0.05, (
            f"D_H/r_d^GRUT = {dh_rd:.4f}, expected ~8.635"
        )

    def test_observed_dh_over_rd_matches_delubac(self, comparison):
        """Stored observation matches Delubac+2015: 9.18 ± 0.28."""
        from grut.derived.cosmology.bao_sound_horizon import (
            DELUBAC_DH_OVER_RD, DELUBAC_SIGMA
        )
        assert comparison["DH_over_rd_observed"] == pytest.approx(DELUBAC_DH_OVER_RD)
        assert comparison["sigma"]               == pytest.approx(DELUBAC_SIGMA)

    def test_residual_is_negative(self, comparison):
        """GRUT underpredicts D_H/r_d (overpredicts H), giving negative residual."""
        assert comparison["residual_sigma"] < 0, (
            "Expected negative residual: GRUT H too high → D_H/r_d too low"
        )

    def test_residual_near_expected(self, comparison):
        """Residual ≈ −1.95σ (locked from CAMB computation)."""
        r = comparison["residual_sigma"]
        assert abs(r - (-1.945)) < 0.10, (
            f"Residual = {r:.3f}σ, expected ~−1.95σ"
        )

    def test_residual_within_2point5_sigma(self, comparison):
        """Self-consistent residual within ±2.5σ — mild tension, not ruled out."""
        r = comparison["residual_sigma"]
        assert abs(r) < 2.5, (
            f"BAO residual = {r:.3f}σ exceeds 2.5σ — Ly-α tension too large"
        )

    def test_note_is_string(self, comparison):
        assert isinstance(comparison["note"], str) and len(comparison["note"]) > 20

    def test_caching_returns_same_object(self, comparison):
        """grut_sound_horizon() returns the same cached dict on second call."""
        from grut.derived.cosmology.bao_sound_horizon import grut_sound_horizon
        sh1 = grut_sound_horizon()
        sh2 = grut_sound_horizon()
        assert sh1 is sh2, "Cache not working: different objects returned"
