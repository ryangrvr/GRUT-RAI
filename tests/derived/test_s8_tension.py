"""Tests for grut.derived.cosmology.s8_tension.

Certifies the S₈ = σ₈(Ω_m/0.3)^0.5 tension assessment:
  - 4-point WL compilation correctly encoded
  - GRUT S₈ = 0.803 (locked from σ₈=0.817, Ω_m=0.290)
  - Planck S₈ = 0.831 (locked)
  - GRUT tension vs WL (RMS 1.535σ) < Planck tension (RMS 2.741σ) for all 4 surveys
  - Tension reduction factor 1.79× locked

Key physics results locked in:
  GRUT  S₈ = 0.803   χ²/N = 2.356   RMS = 1.535σ  (partial tension resolution)
  Planck S₈ = 0.831   χ²/N = 7.511   RMS = 2.741σ  (~3σ tension with WL)
  GRUT reduces S₈ tension by 1.79× through lower Ω_m = 0.290
  GRUT still above all 4 WL surveys; tension reduced but not eliminated
"""

import math
import pytest


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(scope="module")
def comparison():
    from grut.derived.cosmology.s8_tension import s8_tension_comparison
    return s8_tension_comparison()


# ── S₈ formula ────────────────────────────────────────────────────────────────

class TestS8Formula:
    """Verify the S₈ = σ₈(Ω_m/0.3)^0.5 computation."""

    def test_formula_definition(self):
        from grut.derived.cosmology.s8_tension import compute_s8
        val = compute_s8(0.811, 0.3)
        assert abs(val - 0.811) < 1e-10, "S₈(σ₈, Ω_m=0.3) should equal σ₈"

    def test_grut_s8_locked(self):
        """GRUT S₈ = 0.8033 (locked from σ₈=0.817, Ω_m=0.290)."""
        from grut.derived.cosmology.s8_tension import grut_s8
        val = grut_s8()
        assert abs(val - 0.8033) < 0.0005, f"GRUT S₈ = {val:.5f}, expected ~0.8033"

    def test_planck_s8_lss_locked(self):
        """Planck S₈ (LSS-derived) = 0.8314 (locked)."""
        from grut.derived.cosmology.s8_tension import planck_s8_lss
        val = planck_s8_lss()
        assert abs(val - 0.8314) < 0.0005, f"Planck S₈ = {val:.5f}, expected ~0.8314"

    def test_grut_s8_below_planck(self):
        """GRUT S₈ < Planck S₈: lower Ω_m wins over higher σ₈."""
        from grut.derived.cosmology.s8_tension import grut_s8, planck_s8_lss
        assert grut_s8() < planck_s8_lss()

    def test_grut_s8_formula_consistent(self):
        """compute_s8(GRUT_SIGMA8, GRUT_OMEGA_M) equals grut_s8()."""
        from grut.derived.cosmology.s8_tension import (
            compute_s8, grut_s8, GRUT_SIGMA8, GRUT_OMEGA_M
        )
        assert compute_s8(GRUT_SIGMA8, GRUT_OMEGA_M) == pytest.approx(grut_s8())


# ── WL dataset structure ──────────────────────────────────────────────────────

class TestWLDataset:
    """Verify the 4-point WL compilation is structurally correct."""

    def test_n_wl_points(self):
        from grut.derived.cosmology.s8_tension import N_WL_POINTS, WL_DATA
        assert N_WL_POINTS == 4
        assert len(WL_DATA) == 4

    def test_sorted_ascending(self):
        """Data sorted by S₈ ascending (lowest tension first for display)."""
        from grut.derived.cosmology.s8_tension import WL_DATA
        s8s = [p.s8 for p in WL_DATA]
        assert s8s == sorted(s8s), "WL_DATA not sorted by S₈"

    def test_all_sigma_positive(self):
        from grut.derived.cosmology.s8_tension import WL_DATA
        for p in WL_DATA:
            assert p.sigma > 0.0, f"Non-positive sigma at {p.survey}"

    def test_expected_surveys_present(self):
        from grut.derived.cosmology.s8_tension import WL_DATA
        refs = {p.survey for p in WL_DATA}
        assert any("KiDS" in r for r in refs), "KiDS missing from WL_DATA"
        assert any("DES"  in r for r in refs), "DES missing from WL_DATA"
        assert any("HSC"  in r for r in refs), "HSC missing from WL_DATA"

    def test_s8_values_in_physical_range(self):
        """All WL S₈ values in plausible range [0.70, 0.82]."""
        from grut.derived.cosmology.s8_tension import WL_DATA
        for p in WL_DATA:
            assert 0.70 < p.s8 < 0.82, f"S₈ = {p.s8} out of range at {p.survey}"

    def test_planck_cmb_s8_constant(self):
        """Planck 2018 Table 2 S₈ = 0.832 ± 0.013 stored correctly."""
        from grut.derived.cosmology.s8_tension import PLANCK_S8_CMB, PLANCK_S8_CMB_SIGMA
        assert abs(PLANCK_S8_CMB - 0.832)  < 0.002
        assert abs(PLANCK_S8_CMB_SIGMA - 0.013) < 0.002


# ── Tension comparison ────────────────────────────────────────────────────────

class TestS8TensionComparison:
    """Verify locked tension statistics for GRUT and Planck vs WL surveys."""

    def test_result_has_required_keys(self, comparison):
        required = {
            "grut_s8", "planck_s8_lss", "planck_s8_cmb", "planck_s8_cmb_sigma",
            "n_wl_points", "wl_s8", "wl_sigma",
            "tensions_grut", "tensions_planck",
            "chi2_N_grut", "chi2_N_planck",
            "rms_grut", "rms_planck",
            "tension_reduction", "note",
        }
        assert required.issubset(comparison.keys())

    def test_n_wl_points(self, comparison):
        from grut.derived.cosmology.s8_tension import N_WL_POINTS
        assert comparison["n_wl_points"] == N_WL_POINTS == 4

    def test_grut_chi2_N_locked(self, comparison):
        """χ²/N^GRUT ≈ 2.356 (locked)."""
        c = comparison["chi2_N_grut"]
        assert abs(c - 2.356) < 0.020, f"χ²/N^GRUT = {c:.4f}, expected ~2.356"

    def test_planck_chi2_N_locked(self, comparison):
        """χ²/N^Planck ≈ 7.511 (locked)."""
        c = comparison["chi2_N_planck"]
        assert abs(c - 7.511) < 0.050, f"χ²/N^Planck = {c:.4f}, expected ~7.511"

    def test_grut_chi2_N_below_planck(self, comparison):
        """GRUT is a better fit to WL surveys than Planck."""
        assert comparison["chi2_N_grut"] < comparison["chi2_N_planck"]

    def test_rms_grut_locked(self, comparison):
        """RMS^GRUT ≈ 1.535σ (locked)."""
        rms = comparison["rms_grut"]
        assert abs(rms - 1.535) < 0.015, f"RMS^GRUT = {rms:.4f}σ, expected ~1.535"

    def test_rms_planck_locked(self, comparison):
        """RMS^Planck ≈ 2.741σ (locked)."""
        rms = comparison["rms_planck"]
        assert abs(rms - 2.741) < 0.015, f"RMS^Planck = {rms:.4f}σ, expected ~2.741"

    def test_all_grut_tensions_positive(self, comparison):
        """GRUT S₈ > all WL measurements — overpredicts but by less than Planck."""
        assert all(t > 0 for t in comparison["tensions_grut"]), (
            "Expected GRUT S₈ above all WL surveys"
        )

    def test_grut_tension_below_planck_per_survey(self, comparison):
        """For every WL survey, GRUT tension < Planck tension."""
        for tg, tp in zip(comparison["tensions_grut"], comparison["tensions_planck"]):
            assert tg < tp, f"GRUT tension {tg:.3f}σ ≥ Planck {tp:.3f}σ"

    def test_tension_reduction_locked(self, comparison):
        """Tension reduction factor ≈ 1.79× (locked)."""
        r = comparison["tension_reduction"]
        assert abs(r - 1.786) < 0.020, f"Reduction = {r:.3f}×, expected ~1.786"

    def test_tension_reduction_exceeds_1point5(self, comparison):
        """GRUT reduces S₈ tension by at least 1.5× vs Planck."""
        assert comparison["tension_reduction"] > 1.5

    def test_max_grut_tension_below_2point5sigma(self, comparison):
        """No single WL survey is more than 2.5σ from GRUT."""
        worst = max(abs(t) for t in comparison["tensions_grut"])
        assert worst < 2.5, f"Worst GRUT tension = {worst:.3f}σ ≥ 2.5σ"

    def test_caching_returns_same_object(self, comparison):
        from grut.derived.cosmology.s8_tension import s8_tension_comparison
        c1 = s8_tension_comparison()
        c2 = s8_tension_comparison()
        assert c1 is c2, "Cache broken: different objects returned"

    def test_note_contains_key_numbers(self, comparison):
        note = comparison["note"]
        assert isinstance(note, str) and len(note) > 50
        assert "1.5" in note or "1.53" in note or "RMS" in note
