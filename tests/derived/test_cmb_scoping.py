"""Tests for grut.derived.cmb.scoping — quantitative answers to the
four CMB Boltzmann scoping questions.

The framework's CMB prediction at recombination is parts-in-10⁵
(below Planck's 3 × 10⁻⁴ precision, near CMB-S4's 5 × 10⁻⁵ target).
These tests pin the scoping numbers so they don't drift as the
framework evolves.
"""

import math

import pytest

from grut.derived.cmb.scoping import (
    CLASS_CAMB_EFFORT_ESTIMATE,
    CLASS_ENTRY_POINTS,
    CMB_S4_TARGET_PRECISION,
    CAMB_ENTRY_POINTS,
    H_0_KM_S_MPC,
    H_0_Hz,
    H_at_redshift,
    OMEGA_M,
    OMEGA_L,
    PLANCK_THETA_PRECISION,
    Z_RECOMBINATION,
    alpha_eff,
    cmb_scoping_report,
    delta_n_g_over_n_g,
    n_g_at_omega,
    omega_acoustic_first_peak,
    omega_tau_0,
    sound_horizon_shift_estimate,
    verify,
)
from grut.foundation.closure_protocol import ALPHA_VAC, TAU_0_SEC


class TestCosmologicalBaseline:
    """Planck 2018 cosmological inputs are correct."""

    def test_h0_value(self):
        assert abs(H_0_KM_S_MPC - 67.66) < 0.01

    def test_omega_m_plus_omega_l_near_1(self):
        """Flat universe — Ω_m + Ω_Λ ≈ 1 (radiation negligible today)."""
        assert abs(OMEGA_M + OMEGA_L - 1.0) < 0.001

    def test_z_recombination_is_1100(self):
        assert Z_RECOMBINATION == 1100.0

    def test_h0_in_Hz_is_correct(self):
        """H_0 in Hz = (h × 100 km/s/Mpc) / Mpc-in-km."""
        from grut.derived.cmb.scoping import H_0_Hz
        h0 = H_0_Hz()
        # 67.66 km/s/Mpc ≈ 2.19 × 10⁻¹⁸ Hz
        assert abs(h0 - 2.19e-18) / 2.19e-18 < 0.01


class TestQ1OmegaTauAtRecombination:
    """ωτ_0 at recombination is in the deep-crystal regime."""

    def test_h_rec_is_around_5e_minus_14_Hz(self):
        H_rec = H_at_redshift(1100)
        assert 4e-14 < H_rec < 6e-14

    def test_h_rec_over_h0_around_2e4(self):
        H_rec = H_at_redshift(1100)
        assert 1e4 < H_rec / H_0_Hz() < 5e4

    def test_expansion_omega_tau_around_68(self):
        """H_rec × τ_0 ≈ 68 (deep crystal, but not infinite)."""
        H_rec = H_at_redshift(1100)
        ot = omega_tau_0(H_rec)
        assert 60 < ot < 80

    def test_acoustic_omega_tau_around_140(self):
        """ω_acoustic × τ_0 ≈ 140 at the first peak."""
        omega_ac = omega_acoustic_first_peak()
        ot = omega_tau_0(omega_ac)
        assert 100 < ot < 200

    def test_both_in_crystal_regime(self):
        """Both relevant frequencies have ωτ_0 > 1 — vacuum is crystallized."""
        H_rec = H_at_redshift(1100)
        omega_ac = omega_acoustic_first_peak()
        assert omega_tau_0(H_rec) > 1
        assert omega_tau_0(omega_ac) > 1


class TestQ2SoundHorizonShift:
    """The n_g(ω) shift at recombination is parts-in-10⁵."""

    def test_alpha_eff_at_recombination_is_small(self):
        """At ωτ_0 ≈ 68, α_eff ≈ α / 4625 ≈ 7 × 10⁻⁵."""
        H_rec = H_at_redshift(1100)
        ot = omega_tau_0(H_rec)
        a = alpha_eff(ot)
        assert 1e-5 < a < 1e-4

    def test_n_g_shift_at_h_rec(self):
        """Δn_g/n_g at H_rec ≈ 3.6 × 10⁻⁵."""
        H_rec = H_at_redshift(1100)
        d = delta_n_g_over_n_g(H_rec)
        assert 1e-5 < d < 1e-4
        assert abs(d - 3.6e-5) / 3.6e-5 < 0.10

    def test_sound_horizon_shift_estimate(self):
        """Δr_s/r_s leading-order = α / [2(ωτ_0)²] ≈ 3.6 × 10⁻⁵."""
        H_rec = H_at_redshift(1100)
        ot = omega_tau_0(H_rec)
        s = sound_horizon_shift_estimate(ot)
        assert abs(s - 3.6e-5) / 3.6e-5 < 0.10

    def test_n_g_at_h_rec_close_to_one(self):
        """n_g(H_rec) ≈ 1.0000356 — vacuum essentially GR-like at recombination."""
        H_rec = H_at_redshift(1100)
        n = n_g_at_omega(H_rec)
        assert 1.0 < n < 1.001


class TestQ3EntryPointsDocumented:
    """CLASS / CAMB modification entry points are named and described."""

    def test_class_has_three_entry_points(self):
        assert len(CLASS_ENTRY_POINTS) == 3

    def test_class_includes_perturb_einstein(self):
        """Most consequential entry point is perturb_einstein."""
        keys = " ".join(CLASS_ENTRY_POINTS.keys())
        assert "einstein" in keys.lower() or "perturb" in keys.lower()

    def test_class_includes_background(self):
        keys = " ".join(CLASS_ENTRY_POINTS.keys())
        assert "background" in keys.lower()

    def test_camb_entry_points_documented(self):
        assert len(CAMB_ENTRY_POINTS) >= 1
        names = " ".join(CAMB_ENTRY_POINTS.keys())
        assert "equations" in names.lower() or "f90" in names.lower()

    def test_effort_estimate_is_specific(self):
        """Effort estimate names a specific timeframe."""
        assert "week" in CLASS_CAMB_EFFORT_ESTIMATE.lower()


class TestQ4Detectability:
    """Predicted shift vs Planck and CMB-S4 precision."""

    def test_below_planck_precision(self):
        """Δθ_*/θ_* (~3.6e-5) below Planck's 3e-4 precision by factor 10."""
        rep = cmb_scoping_report()
        assert rep.theta_star_shift_relative < PLANCK_THETA_PRECISION
        ratio = PLANCK_THETA_PRECISION / rep.theta_star_shift_relative
        assert 5 < ratio < 30

    def test_below_cmb_s4_precision(self):
        """Δθ_*/θ_* (~3.6e-5) below CMB-S4's 5e-5 target — at threshold."""
        rep = cmb_scoping_report()
        assert rep.theta_star_shift_relative < CMB_S4_TARGET_PRECISION

    def test_within_factor_2_of_cmb_s4_threshold(self):
        """The prediction sits within factor 2 of CMB-S4's target —
        i.e. detectable (or excluded) by the next-generation experiment."""
        rep = cmb_scoping_report()
        ratio = CMB_S4_TARGET_PRECISION / rep.theta_star_shift_relative
        assert ratio < 2

    def test_planck_does_not_detect(self):
        rep = cmb_scoping_report()
        assert rep.detectability_now is False


class TestVerifyHarness:

    def test_all_pass(self):
        checks = verify()
        failed = [k for k, v in checks.items() if not v]
        assert not failed, f"CMB scoping verify failures: {failed}"


class TestScopingReportStructure:

    def test_report_fields_populated(self):
        rep = cmb_scoping_report()
        assert rep.H_rec_Hz > 0
        assert rep.omega_tau_0_expansion > 1
        assert rep.omega_tau_0_acoustic > 1
        assert rep.delta_n_g_over_n_g_at_H_rec > 0
        assert rep.theta_star_shift_relative > 0


class TestScopingDocumentExists:
    """The scoping document referenced from the registry must exist."""

    def test_doc_present(self):
        from pathlib import Path
        repo = Path(__file__).resolve().parents[2]
        doc = repo / "theory" / "CMB_BOLTZMANN_SCOPING.md"
        assert doc.is_file(), f"scoping doc missing: {doc}"

    def test_doc_addresses_all_four_questions(self):
        from pathlib import Path
        repo = Path(__file__).resolve().parents[2]
        doc = repo / "theory" / "CMB_BOLTZMANN_SCOPING.md"
        text = doc.read_text(encoding="utf-8")
        # The four scoping questions must each have a section
        assert "Q1." in text
        assert "Q2." in text
        assert "Q3." in text
        assert "Q4." in text
