"""Tests for grut.derived.cosmology.fsigma8_growth.

Certifies the fσ₈(z) growth-rate comparison:
  - 13-point RSD compilation (z = 0.02–1.40) correctly encoded
  - GRUT modified-gravity prediction computed via ODE (k = 0.05 Mpc⁻¹)
  - Planck ΛCDM reference curve
  - Scale-dependent enhancement: k=0.05 < k=0.01 (large-scale limit)
  - χ²/N < 1 for GRUT (consistent with data)
  - Key statistics locked to computed values

Key physics results locked in:
  GRUT fσ₈ (k=0.05 Mpc⁻¹, 13 RSD points):  χ²/N = 0.763,  RMS = 0.874σ
  Planck ΛCDM                             :  χ²/N = 0.422,  RMS = 0.650σ
  Large-scale limit (k=0.01)              :  χ²/N ≈ 2.10  (disfavoured)
  GRUT lies ~5% above Planck at z ~ 0.4–0.7; all residuals within 1.5σ
"""

import math
import pytest
import numpy as np


# ── Shared fixtures ───────────────────────────────────────────────────────────

@pytest.fixture(scope="module")
def comparison():
    from grut.derived.cosmology.fsigma8_growth import fsigma8_comparison
    return fsigma8_comparison()


@pytest.fixture(scope="module")
def z_test():
    return np.array([0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.4])


# ── Dataset structure ─────────────────────────────────────────────────────────

class TestRSDDataset:
    """Verify the 13-point fσ₈ compilation is structurally correct."""

    def test_n_rsd_points(self):
        from grut.derived.cosmology.fsigma8_growth import N_RSD_POINTS, RSD_DATA
        assert N_RSD_POINTS == 13
        assert len(RSD_DATA) == 13

    def test_sorted_by_z(self):
        from grut.derived.cosmology.fsigma8_growth import RSD_DATA
        zs = [p.z_eff for p in RSD_DATA]
        assert zs == sorted(zs), "RSD_DATA not sorted by z_eff"

    def test_no_duplicate_z(self):
        from grut.derived.cosmology.fsigma8_growth import RSD_DATA
        zs = [p.z_eff for p in RSD_DATA]
        assert len(zs) == len(set(zs)), "Duplicate z_eff values in RSD_DATA"

    def test_z_range(self):
        """Dataset spans z = 0.02 to 1.40."""
        from grut.derived.cosmology.fsigma8_growth import RSD_DATA
        assert RSD_DATA[0].z_eff  == pytest.approx(0.02)
        assert RSD_DATA[-1].z_eff == pytest.approx(1.40)

    def test_all_sigma_positive(self):
        from grut.derived.cosmology.fsigma8_growth import RSD_DATA
        for p in RSD_DATA:
            assert p.sigma > 0.0, f"Non-positive sigma at z={p.z_eff}"

    def test_expected_sources_present(self):
        """Key surveys represented: BOSS DR12, WiggleZ, 6dFGRS, FastSound."""
        from grut.derived.cosmology.fsigma8_growth import RSD_DATA
        refs = {p.reference for p in RSD_DATA}
        assert any("Alam"       in r for r in refs), "BOSS DR12 missing"
        assert any("Blake"      in r for r in refs), "WiggleZ missing"
        assert any("Beutler"    in r for r in refs), "6dFGRS missing"
        assert any("Okumura"    in r for r in refs), "FastSound missing"
        assert any("de la Torre" in r for r in refs), "VIPERS missing"


# ── GRUT fσ₈ predictions ─────────────────────────────────────────────────────

class TestGRUTFsigma8:
    """Verify GRUT fσ₈ predictions at representative RSD scale k=0.05 Mpc⁻¹."""

    def test_returns_array_same_length(self, z_test):
        from grut.derived.cosmology.fsigma8_growth import grut_fsigma8
        out = grut_fsigma8(z_test)
        assert out.shape == z_test.shape

    def test_all_positive(self, z_test):
        from grut.derived.cosmology.fsigma8_growth import grut_fsigma8
        assert np.all(grut_fsigma8(z_test) > 0)

    def test_z0_value(self):
        """fσ₈^GRUT(z=0) ≈ 0.455 (f(0) × σ₈^GRUT × 1)."""
        from grut.derived.cosmology.fsigma8_growth import grut_fsigma8
        fs8_0 = float(grut_fsigma8(np.array([0.0]))[0])
        assert abs(fs8_0 - 0.455) < 0.01, f"fσ₈^GRUT(0) = {fs8_0:.4f}"

    def test_peaks_at_intermediate_z(self, z_test):
        """fσ₈ peaks at z ~ 0.3–0.5 (matter-Λ transition), then declines."""
        from grut.derived.cosmology.fsigma8_growth import grut_fsigma8
        fs8 = grut_fsigma8(z_test)
        idx_peak = np.argmax(fs8)
        assert 1 <= idx_peak <= 4, f"Peak at unexpected z={z_test[idx_peak]}"

    def test_scalar_input(self):
        from grut.derived.cosmology.fsigma8_growth import grut_fsigma8
        val = grut_fsigma8(np.array([0.5]))
        assert 0.3 < float(val[0]) < 0.7

    def test_z0_38_near_expected(self):
        """fσ₈^GRUT(z=0.38) ≈ 0.494 (locked from ODE computation)."""
        from grut.derived.cosmology.fsigma8_growth import grut_fsigma8
        val = float(grut_fsigma8(np.array([0.38]))[0])
        assert abs(val - 0.494) < 0.005, f"fσ₈^GRUT(0.38) = {val:.4f}"

    def test_z1_40_near_expected(self):
        """fσ₈^GRUT(z=1.40) ≈ 0.389 (locked)."""
        from grut.derived.cosmology.fsigma8_growth import grut_fsigma8
        val = float(grut_fsigma8(np.array([1.40]))[0])
        assert abs(val - 0.389) < 0.005, f"fσ₈^GRUT(1.40) = {val:.4f}"


# ── Planck ΛCDM reference ─────────────────────────────────────────────────────

class TestLCDMFsigma8:
    """Verify Planck ΛCDM fσ₈ reference curve."""

    def test_lcdm_positive(self, z_test):
        from grut.derived.cosmology.fsigma8_growth import lcdm_fsigma8
        assert np.all(lcdm_fsigma8(z_test) > 0)

    def test_z0_value_lcdm(self):
        """fσ₈^Planck(z=0) ≈ 0.433 — f × σ₈ at z=0 for Planck ΛCDM."""
        from grut.derived.cosmology.fsigma8_growth import lcdm_fsigma8
        val = float(lcdm_fsigma8(np.array([0.0]))[0])
        assert abs(val - 0.433) < 0.010, f"fσ₈^Planck(0) = {val:.4f}"

    def test_lcdm_z0_51_near_expected(self):
        """fσ₈^Planck(z=0.51) ≈ 0.474 — midrange BOSS DR12 epoch."""
        from grut.derived.cosmology.fsigma8_growth import lcdm_fsigma8
        val = float(lcdm_fsigma8(np.array([0.51]))[0])
        assert abs(val - 0.474) < 0.010, f"fσ₈^Planck(0.51) = {val:.4f}"


# ── Scale dependence: GRUT > Planck ──────────────────────────────────────────

class TestScaleDependence:
    """GRUT growth enhancement depends on scale; all predictions are consistent."""

    def test_grut_above_planck_at_rsd_scale(self, z_test):
        """At k=0.05 Mpc⁻¹, GRUT fσ₈ > Planck for z > 0 (μ_eff > 1 at GRUT Ωm)."""
        from grut.derived.cosmology.fsigma8_growth import grut_fsigma8, lcdm_fsigma8
        z_pos = z_test[z_test > 0]
        g = grut_fsigma8(z_pos)
        p = lcdm_fsigma8(z_pos)
        assert np.all(g > p), "Expected GRUT > Planck at all z > 0 (k=0.05)"

    def test_large_scale_above_rsd_scale(self, z_test):
        """Large-scale limit (k=0.01) > representative scale (k=0.05) everywhere."""
        from grut.derived.cosmology.fsigma8_growth import grut_fsigma8, grut_fsigma8_large_scale
        z_pos = z_test[z_test > 0]
        ls = grut_fsigma8_large_scale(z_pos)
        rs = grut_fsigma8(z_pos)
        assert np.all(ls > rs), "Large-scale fσ₈ should exceed RSD-scale fσ₈"

    def test_grut_to_planck_ratio_at_z05(self):
        """GRUT/Planck ratio at z=0.5 is 1.03–1.08 (moderate k=0.05 enhancement)."""
        from grut.derived.cosmology.fsigma8_growth import grut_fsigma8, lcdm_fsigma8
        z = np.array([0.5])
        ratio = float(grut_fsigma8(z)[0] / lcdm_fsigma8(z)[0])
        assert 1.03 < ratio < 1.08, f"GRUT/Planck ratio at z=0.5 = {ratio:.4f}"

    def test_large_scale_grut_to_planck_ratio_at_z05(self):
        """Large-scale limit: GRUT/Planck ratio at z=0.5 ~ 1.11–1.15."""
        from grut.derived.cosmology.fsigma8_growth import grut_fsigma8_large_scale, lcdm_fsigma8
        z = np.array([0.5])
        ratio = float(grut_fsigma8_large_scale(z)[0] / lcdm_fsigma8(z)[0])
        assert 1.10 < ratio < 1.16, f"Large-scale ratio at z=0.5 = {ratio:.4f}"


# ── Full comparison statistics ────────────────────────────────────────────────

class TestFsigma8Comparison:
    """Verify the full fσ₈ comparison statistics are locked."""

    def test_result_has_required_keys(self, comparison):
        required = {
            "n_points", "z_arr", "obs_fsigma8", "obs_sigma",
            "grut_fsigma8", "lcdm_fsigma8",
            "residuals_grut", "residuals_lcdm",
            "chi2_N_grut", "chi2_N_lcdm",
            "rms_grut", "rms_lcdm",
            "k_rsd_mpc", "grut_sigma8", "planck_sigma8", "note",
        }
        assert required.issubset(comparison.keys())

    def test_n_points(self, comparison):
        from grut.derived.cosmology.fsigma8_growth import N_RSD_POINTS
        assert comparison["n_points"] == N_RSD_POINTS == 13

    def test_grut_chi2_N_below_1(self, comparison):
        """χ²/N < 1 for GRUT: consistent with data at k=0.05 Mpc⁻¹."""
        c = comparison["chi2_N_grut"]
        assert c < 1.0, f"χ²/N^GRUT = {c:.4f} ≥ 1 (unexpected tension)"

    def test_grut_chi2_N_locked(self, comparison):
        """χ²/N^GRUT ≈ 0.763 (locked from ODE computation)."""
        c = comparison["chi2_N_grut"]
        assert abs(c - 0.763) < 0.020, f"χ²/N^GRUT = {c:.4f}, expected ~0.763"

    def test_lcdm_chi2_N_below_1(self, comparison):
        """χ²/N < 1 for Planck ΛCDM reference."""
        c = comparison["chi2_N_lcdm"]
        assert c < 1.0, f"χ²/N^ΛCDM = {c:.4f} ≥ 1"

    def test_lcdm_chi2_N_locked(self, comparison):
        """χ²/N^ΛCDM ≈ 0.422 (locked)."""
        c = comparison["chi2_N_lcdm"]
        assert abs(c - 0.422) < 0.020, f"χ²/N^ΛCDM = {c:.4f}, expected ~0.422"

    def test_rms_grut_reasonable(self, comparison):
        """RMS residual < 1.5σ: no single measurement drives a large pull."""
        rms = comparison["rms_grut"]
        assert rms < 1.5, f"RMS^GRUT = {rms:.4f}σ too large"

    def test_rms_grut_locked(self, comparison):
        """RMS^GRUT ≈ 0.874σ (locked)."""
        rms = comparison["rms_grut"]
        assert abs(rms - 0.874) < 0.020, f"RMS^GRUT = {rms:.4f}σ, expected ~0.874"

    def test_all_grut_residuals_within_2sigma(self, comparison):
        """All 13 GRUT residuals within ±2σ — no outlier driven by a single point."""
        res = comparison["residuals_grut"]
        worst = float(np.max(np.abs(res)))
        assert worst < 2.0, f"Largest GRUT residual = {worst:.3f}σ ≥ 2σ"

    def test_grut_sigma8_matches_scenario_d(self, comparison):
        """σ₈^GRUT = 0.817 (Scenario D from CAMB)."""
        from grut.derived.cosmology.fsigma8_growth import GRUT_SIGMA8
        assert comparison["grut_sigma8"] == pytest.approx(GRUT_SIGMA8)
        assert abs(comparison["grut_sigma8"] - 0.817) < 0.001

    def test_caching_returns_same_object(self, comparison):
        """fsigma8_comparison() returns the same cached dict on second call."""
        from grut.derived.cosmology.fsigma8_growth import fsigma8_comparison
        c1 = fsigma8_comparison()
        c2 = fsigma8_comparison()
        assert c1 is c2, "Cache broken: different objects returned"

    def test_note_is_informative(self, comparison):
        note = comparison["note"]
        assert isinstance(note, str) and len(note) > 50
        assert "χ²/N" in note or "chi2" in note.lower()
