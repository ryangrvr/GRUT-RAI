"""Tests for grut.derived.cosmology.hz_residuals.

Certifies the H(z) observational comparison module:
  - E(z) formula correctness
  - Moresco+2022 CC dataset completeness (32 CC + 1 BAO = 33 points)
  - GRUT zero-parameter prediction vs observed H(z) (primary physics test)
  - Planck ΛCDM reference comparison
  - GRUT vs Planck statistical equivalence on CC data
  - H_inf structural identity: H₀ × √Ω_Λ = H_inf
  - Legacy 10-point dataset preserved

Key physics result locked in:
  GRUT (H₀≈69.0, Ω_m≈0.290, Ω_Λ≈0.710), derived from (H_inf, τ₀) with zero
  free parameters, fits the 32-point Moresco+2022 CC gold sample with
  χ²/N ≈ 0.465 and RMS ≈ 0.68σ — statistically indistinguishable from
  Planck ΛCDM (χ²/N ≈ 0.466) fitted to the same data.
"""

import math
import pytest


# ── E(z) formula ─────────────────────────────────────────────────────────────

class TestEz:
    """Unit tests for the flat-ΛCDM E(z) function."""

    def test_ez_at_z0_equals_one(self):
        """E(0) = √(Ω_m + Ω_Λ) = 1 for flat ΛCDM."""
        from grut.derived.cosmology.hz_residuals import E_z
        assert abs(E_z(0.0, 0.30, 0.70) - 1.0) < 1e-10
        assert abs(E_z(0.0, 0.290, 0.710) - 1.0) < 1e-10
        assert abs(E_z(0.0, 0.3153, 0.6847) - 1.0) < 1e-10

    def test_ez_monotonically_increasing(self):
        """E(z) increases strictly with z for any physical (Ω_m > 0, Ω_Λ ≥ 0)."""
        from grut.derived.cosmology.hz_residuals import E_z
        zs = [0.0, 0.1, 0.5, 1.0, 2.0, 3.0]
        vals = [E_z(z, 0.290, 0.710) for z in zs]
        for i in range(len(vals) - 1):
            assert vals[i] < vals[i + 1], (
                f"E_z not monotone: E({zs[i]}) = {vals[i]:.4f} ≥ E({zs[i+1]}) = {vals[i+1]:.4f}"
            )

    def test_ez_rejects_non_flat(self):
        """ValueError when Ω_m + Ω_Λ deviates from 1 by > 1%."""
        from grut.derived.cosmology.hz_residuals import E_z
        with pytest.raises(ValueError, match="Flat-ΛCDM"):
            E_z(1.0, 0.5, 0.4)   # sum = 0.9, 10% off

    def test_ez_matter_dominated_limit(self):
        """At high-z, E(z) ≈ √Ω_m × (1+z)^(3/2)."""
        from grut.derived.cosmology.hz_residuals import E_z
        z = 10.0
        Omega_m = 0.290
        E = E_z(z, Omega_m, 1.0 - Omega_m)
        E_matter = math.sqrt(Omega_m) * (1.0 + z) ** 1.5
        # Ω_Λ contribution at z=10 is Ω_Λ / (Ω_m × 11³) ≈ 0.5% — small but non-zero
        assert abs(E / E_matter - 1.0) < 0.01  # within 1%


# ── Dataset integrity ─────────────────────────────────────────────────────────

class TestDataset:
    """Verify HZ_DATA completeness and internal consistency."""

    def test_dataset_has_33_points(self):
        """Full Moresco+2022 compilation: 32 CC + 1 BAO = 33 total."""
        from grut.derived.cosmology.hz_residuals import HZ_DATA
        assert len(HZ_DATA) == 33

    def test_dataset_has_32_cc_and_1_bao(self):
        """32 calibration-independent CC points; 1 BAO (Ly-α BOSS)."""
        from grut.derived.cosmology.hz_residuals import HZ_DATA
        cc_pts  = [p for p in HZ_DATA if p.tracer == "CC"]
        bao_pts = [p for p in HZ_DATA if p.tracer == "BAO"]
        assert len(cc_pts)  == 32, f"Expected 32 CC points, got {len(cc_pts)}"
        assert len(bao_pts) == 1,  f"Expected 1 BAO point, got {len(bao_pts)}"

    def test_all_sigmas_positive(self):
        from grut.derived.cosmology.hz_residuals import HZ_DATA
        for pt in HZ_DATA:
            assert pt.sigma_H > 0, f"Non-positive sigma at z={pt.z}"

    def test_redshifts_monotone_increasing(self):
        from grut.derived.cosmology.hz_residuals import HZ_DATA
        zs = [pt.z for pt in HZ_DATA]
        assert zs == sorted(zs), f"HZ_DATA not sorted by redshift: {zs}"

    def test_dataset_spans_expected_z_range(self):
        from grut.derived.cosmology.hz_residuals import HZ_DATA
        assert HZ_DATA[0].z == pytest.approx(0.07)
        assert HZ_DATA[-1].z == pytest.approx(2.34)

    def test_bao_is_delubac_only(self):
        """Single BAO point is Delubac+2015 Ly-α at z=2.34."""
        from grut.derived.cosmology.hz_residuals import HZ_DATA
        bao = [p for p in HZ_DATA if p.tracer == "BAO"]
        assert len(bao) == 1
        assert bao[0].z == pytest.approx(2.34)
        assert "Delubac" in bao[0].reference

    def test_sources_include_moresco22_compilation(self):
        """All 9 source families from Moresco+2022 review are represented."""
        from grut.derived.cosmology.hz_residuals import HZ_DATA
        refs = {p.reference for p in HZ_DATA if p.tracer == "CC"}
        expected = {
            "Jimenez+2003", "Simon+2005", "Stern+2010",
            "Moresco+2012", "Zhang+2014", "Moresco+2015",
            "Moresco+2016", "Ratsimbazafy+2017", "Borghi+2022",
        }
        assert expected.issubset(refs), f"Missing sources: {expected - refs}"

    def test_no_duplicate_redshifts(self):
        """No two data points share the same redshift."""
        from grut.derived.cosmology.hz_residuals import HZ_DATA
        zs = [pt.z for pt in HZ_DATA]
        assert len(zs) == len(set(zs)), "Duplicate z values in HZ_DATA"


# ── Legacy dataset ────────────────────────────────────────────────────────────

class TestLegacyDataset:
    """Verify backward-compatible legacy 10-point dataset is preserved."""

    def test_legacy_exists(self):
        from grut.derived.cosmology.hz_residuals import HZ_DATA_LEGACY
        assert HZ_DATA_LEGACY is not None

    def test_legacy_has_10_points(self):
        from grut.derived.cosmology.hz_residuals import HZ_DATA_LEGACY
        assert len(HZ_DATA_LEGACY) == 10

    def test_legacy_sorted(self):
        from grut.derived.cosmology.hz_residuals import HZ_DATA_LEGACY
        zs = [p.z for p in HZ_DATA_LEGACY]
        assert zs == sorted(zs)

    def test_legacy_spans_same_z_range(self):
        from grut.derived.cosmology.hz_residuals import HZ_DATA_LEGACY
        assert HZ_DATA_LEGACY[0].z  == pytest.approx(0.07)
        assert HZ_DATA_LEGACY[-1].z == pytest.approx(2.34)


# ── GRUT prediction vs observations ──────────────────────────────────────────

class TestGRUTHzComparison:
    """Primary physics tests: GRUT zero-parameter H(z) vs Moresco+2022 data."""

    @pytest.fixture(scope="class")
    def result(self):
        from grut.derived.cosmology.hz_residuals import grut_hz_comparison
        return grut_hz_comparison()

    def test_result_has_expected_keys(self, result):
        required = {"H0", "omega_m", "omega_lambda", "n_points",
                    "points", "cc", "bao", "all", "note_bao"}
        assert required.issubset(result.keys())

    def test_n_points_is_33(self, result):
        assert result["n_points"] == 33

    def test_grut_h0_near_69(self, result):
        """GRUT first-principles H₀ lies in [68, 71] km/s/Mpc."""
        H0 = result["H0"]
        assert 68.0 <= H0 <= 71.0, f"GRUT H₀ = {H0:.3f} outside [68, 71]"

    def test_grut_cc_rms_below_1sigma(self, result):
        """PRIMARY TEST: 32-point CC RMS < 1σ.

        GRUT's zero-parameter (H₀, Ω_m, Ω_Λ) passes the full 32-point
        Moresco+2022 calibration-independent cosmic chronometer compilation
        within 1σ RMS. Current value: ~0.68σ.
        """
        cc = result["cc"]
        assert cc["rms_sigma"] < 1.0, (
            f"GRUT CC RMS = {cc['rms_sigma']:.3f}σ — exceeds 1σ threshold. "
            f"χ²/N_CC = {cc['chi2_per_n']:.3f}"
        )

    def test_grut_cc_chi2_per_n_below_1(self, result):
        """χ²/N_CC < 1 for the 32-point gold sample."""
        cc = result["cc"]
        assert cc["chi2_per_n"] < 1.0, (
            f"χ²/N_CC = {cc['chi2_per_n']:.3f} — model underfits CC data"
        )

    def test_grut_cc_chi2_per_n_expected_value(self, result):
        """χ²/N_CC ≈ 0.465 (locked from Moresco+2022 computation)."""
        cc = result["cc"]
        assert abs(cc["chi2_per_n"] - 0.465) < 0.05, (
            f"χ²/N_CC = {cc['chi2_per_n']:.4f}, expected ~0.465"
        )

    def test_all_cc_points_within_2sigma(self, result):
        """Every CC point individually lies within ±2σ of the GRUT curve."""
        cc_pts = [p for p in result["points"] if p["tracer"] == "CC"]
        for p in cc_pts:
            resid = p["residual_sigma"]
            assert abs(resid) < 2.0, (
                f"CC point z={p['z']} lies {resid:.2f}σ from GRUT curve "
                f"({p['reference']})"
            )

    def test_bao_stats_are_finite(self, result):
        """BAO χ² and RMS are finite (elevated due to sound-horizon calibration)."""
        bao = result["bao"]
        assert bao["chi2"] is not None and math.isfinite(bao["chi2"])
        assert bao["rms_sigma"] is not None and math.isfinite(bao["rms_sigma"])

    def test_per_point_dicts_have_required_keys(self, result):
        required = {"z", "tracer", "reference", "H_obs", "sigma_H",
                    "H_model", "E_z", "delta_H", "residual_sigma"}
        for pt in result["points"]:
            assert required.issubset(pt.keys()), (
                f"Point z={pt['z']} missing keys: {required - pt.keys()}"
            )

    def test_h_model_equals_ez_times_h0(self, result):
        """H_model = E(z) × H₀ for every point."""
        H0 = result["H0"]
        for pt in result["points"]:
            expected = pt["E_z"] * H0
            assert abs(pt["H_model"] - expected) < 1e-6, (
                f"H_model inconsistent at z={pt['z']}"
            )


# ── Planck ΛCDM reference ─────────────────────────────────────────────────────

class TestLCDMReference:
    """Planck ΛCDM comparison — validates module works for arbitrary parameters."""

    @pytest.fixture(scope="class")
    def lcdm_result(self):
        from grut.derived.cosmology.hz_residuals import lcdm_hz_comparison
        return lcdm_hz_comparison()

    def test_lcdm_h0_is_planck_value(self, lcdm_result):
        from grut.derived.cosmology.hz_residuals import PLANCK_H0
        assert lcdm_result["H0"] == pytest.approx(PLANCK_H0)

    def test_lcdm_cc_rms_also_below_1sigma(self, lcdm_result):
        """Both GRUT and Planck ΛCDM fit the 32 CC points within 1σ RMS."""
        cc = lcdm_result["cc"]
        assert cc["rms_sigma"] < 1.0, (
            f"Planck ΛCDM CC RMS = {cc['rms_sigma']:.3f}σ — sanity check failed"
        )


# ── GRUT vs Planck statistical equivalence ───────────────────────────────────

class TestGRUTvsLCDM:
    """GRUT and Planck ΛCDM are statistically indistinguishable on CC data.

    This is the key positive result: GRUT with zero free parameters achieves
    the same fit quality as Planck ΛCDM which was MCMC-fitted to CMB data.
    """

    @pytest.fixture(scope="class")
    def both(self):
        from grut.derived.cosmology.hz_residuals import (
            grut_hz_comparison, lcdm_hz_comparison
        )
        return grut_hz_comparison(), lcdm_hz_comparison()

    def test_cc_chi2_per_n_differ_by_less_than_1pct(self, both):
        """GRUT and Planck CC χ²/N agree to within 1%."""
        gr, lc = both
        ratio = gr["cc"]["chi2_per_n"] / lc["cc"]["chi2_per_n"]
        assert abs(ratio - 1.0) < 0.01, (
            f"χ²/N ratio GRUT/Planck = {ratio:.4f}, expected ~1.000"
        )

    def test_cc_rms_sigma_differ_by_less_than_01(self, both):
        """CC RMS σ for GRUT and Planck differ by < 0.01σ."""
        gr, lc = both
        diff = abs(gr["cc"]["rms_sigma"] - lc["cc"]["rms_sigma"])
        assert diff < 0.01, (
            f"RMS difference GRUT-Planck = {diff:.4f}σ — unexpectedly large"
        )

    def test_grut_n_cc_is_32(self, both):
        """32 CC points in the dataset."""
        gr, _ = both
        assert gr["cc"]["n"] == 32

    def test_all_32_cc_points_within_2sigma_grut(self, both):
        """All 32 CC points within 2σ for GRUT zero-parameter curve."""
        gr, _ = both
        worst = max(
            abs(p["residual_sigma"])
            for p in gr["points"] if p["tracer"] == "CC"
        )
        assert worst < 2.0, f"Worst CC residual = {worst:.3f}σ for GRUT"

    def test_all_32_cc_points_within_2sigma_lcdm(self, both):
        """All 32 CC points within 2σ for Planck ΛCDM curve."""
        _, lc = both
        worst = max(
            abs(p["residual_sigma"])
            for p in lc["points"] if p["tracer"] == "CC"
        )
        assert worst < 2.0, f"Worst CC residual = {worst:.3f}σ for Planck"


# ── H_inf structural identity ─────────────────────────────────────────────────

class TestHInfIdentity:
    """Verify the GRUT falsifier: H₀ × √Ω_Λ = H_inf."""

    def test_h_inf_cross_check_consistent(self):
        """H₀√Ω_Λ (from Friedmann solution) matches H_inf (from CTP integral).

        This structural identity H_inf = H₀√Ω_Λ is GRUT's cosmological
        falsifier: any survey measuring both H₀ and Ω_Λ independently can
        test it. Discrepancy must be < 10⁻⁶ — it's an identity, not a fit.
        """
        from grut.derived.cosmology.hz_residuals import h_inf_cross_check
        result = h_inf_cross_check()
        assert result["consistent"], (
            f"H_inf identity broken: H₀√Ω_Λ = {result['H_inf_derived_km_s_Mpc']:.4f} "
            f"≠ H_inf_direct = {result['H_inf_direct_km_s_Mpc']:.4f} "
            f"({result['discrepancy_pct']:.2e}%)"
        )

    def test_h_inf_value_near_58(self):
        """H_inf ≈ 58.16 km/s/Mpc (structural constant from CTP action)."""
        from grut.derived.cosmology.hz_residuals import h_inf_cross_check
        result = h_inf_cross_check()
        H_inf = result["H_inf_direct_km_s_Mpc"]
        assert 57.0 < H_inf < 60.0, (
            f"H_inf = {H_inf:.3f} km/s/Mpc outside expected range [57, 60]"
        )
