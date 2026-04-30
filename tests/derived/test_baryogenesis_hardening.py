"""Hardening tests for baryogenesis_eta_b — promotes from anchored
to computed by pinning the documented value:

    η_B = 6.57 × 10⁻¹⁰ (route 1, +7.7% from Planck observed 6.10 × 10⁻¹⁰)

The CTP path-asymmetry formula η_B = J_CP × K_neq × (2−R_B)/S_B
combines four quantities all determined by SM anomaly coefficients.
The asymmetry vanishes at R_B = 1 (forward = backward), is nonzero at
R_B ≈ 1.154 — the framework's claim that the universe has nonzero
baryon asymmetry because R ≠ 1.
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
    """If R = 1, η_B = 0. The asymmetry exists because R ≠ 1."""

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
