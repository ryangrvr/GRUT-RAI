"""Tests for baryogenesis_eta_b (tier: ANCHORED — Category-B / hosted).

    η_B = J_CP × K_neq × (2−R_B)/S_B ≈ 6.57 × 10⁻¹⁰ (route 1, +7.7% vs Planck 6.10 × 10⁻¹⁰)

These tests pin the documented value and inputs; they do NOT establish a
responsive-vacuum derivation. The decisive-responsiveness test
(theory/GRUT_BARYOGENESIS_RESPONSIVENESS_TEST.md) found this sector HOSTED
(CONTAINER-SEAM): the magnitude is the hosted SM Jarlskog J_CP × an empirical
K_neq, the GRUT factor (2−R_B)/S_B is off the canonical α-spine and cosmetic,
and the +7.7% match was reverse-fit via an S_B re-choice.

CORRECTION: the asymmetry does NOT vanish at R_B = 1. The zero of (2−R_B) is at
R_B = 2; at R_B = 1, η_B = J_CP·K_neq/S_B ≈ 6.7×10⁻¹⁰ (nonzero, +9.7%). The code's
route-1 R_B = 1.018 (not 1.154).
"""

import pytest


class TestEtaBMatchesPrediction:
    """Route 1 produces η_B ≈ 6.6 × 10⁻¹⁰."""

    def test_route_1_in_band(self):
        from grut.derived.baryogenesis.eta import compute_eta_b
        r = compute_eta_b(route=1)
        assert "eta_B" in r
        assert 6.0e-10 < r["eta_B"] < 7.0e-10

    def test_route_1_specific_value(self):
        """6.57 × 10⁻¹⁰ ± 5 × 10⁻¹².

        The framework's documented prediction is 6.56–6.57 × 10⁻¹⁰ from
        the integer-traced anomaly decomposition; we accept any value
        within 1% of this.
        """
        from grut.derived.baryogenesis.eta import compute_eta_b
        r = compute_eta_b(route=1)
        target = 6.56e-10
        assert abs(r["eta_B"] - target) / target < 0.01

    def test_deviation_from_planck_under_10_percent(self):
        """+7.7% from Planck — within the documented 8% band."""
        from grut.derived.baryogenesis.eta import compute_eta_b, ETA_OBS
        r = compute_eta_b(route=1)
        deviation = abs(r["eta_B"] / ETA_OBS - 1.0)
        assert deviation < 0.10  # within 10%

    def test_eta_obs_is_planck_value(self):
        """η_observed from the module matches Planck's 6.1 × 10⁻¹⁰."""
        from grut.derived.baryogenesis.eta import ETA_OBS
        assert abs(ETA_OBS - 6.1e-10) / 6.1e-10 < 0.01


class TestCPViolationFromR:
    """The (2−R_B) factor enters η_B (same factor as in H_inf). NOTE: η_B does
    NOT vanish at R_B=1 — the zero of (2−R_B) is at R_B=2; this only checks η_B>0."""

    def test_r_b_anomaly_imported(self):
        """The R coefficient enters via (2 - R) — the same factor as in H_inf."""
        from grut.derived.baryogenesis.eta import compute_eta_b
        r = compute_eta_b(route=1)
        # The result must be finite and positive
        assert r["eta_B"] > 0


class TestFieldContentScaling:
    """N_WEYL = 45 and the B^2-weighted fermion fraction enter the formula."""

    def test_n_weyl_is_45(self):
        from grut.derived.baryogenesis.eta import N_WEYL
        assert N_WEYL == 45

    def test_jarlskog_invariant_pdg_value(self):
        """J_CP from PDG ≈ 3.18 × 10⁻⁵."""
        from grut.derived.baryogenesis.eta import J_CP
        assert abs(J_CP - 3.18e-5) / 3.18e-5 < 0.01
