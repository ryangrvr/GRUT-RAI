"""Tests for the cosmic X = H × τ_0 crossover prediction.

Pins the Stage 2 forward derivation: applying the framework's existing
regime classification X = max(ω, Λ_grav) × τ_0 with ω = H to cosmic
history gives X_cosmic = 1 crossing at z ≈ 71 (Planck cosmology).

These tests pin the load-bearing outputs: crossing redshift under both
H_0 choices, X values at canonical epochs, the redshift-independent
H/Λ_grav structural fact for test particles, and the qualitative
shape (deep fluid today, deep crystal at recombination).
"""

from __future__ import annotations

import math

import pytest

from grut.derived.cosmology.cosmic_x_crossover import (
    H_0_FRAMEWORK_KM_S_MPC,
    H_0_PLANCK_KM_S_MPC,
    M_AMU_KG,
    M_GALAXY_KG,
    M_SUN_KG,
    OMEGA_M,
    OMEGA_R,
    cosmic_x_crossover_attempt,
    evaluate_epochs,
    find_x_crossing_redshift,
    H_over_lambda_grav,
    hubble_z,
    lambda_grav_at_cosmic_separation,
    verify_h_dominates_lambda_grav,
    x_cosmic_z,
)
from grut.foundation.closure_protocol import TAU_0_SEC


# ─────────────────────────────────────────────────────────────────────
# Sanity checks — Friedmann + cosmology baselines
# ─────────────────────────────────────────────────────────────────────


class TestFriedmannBaselines:
    def test_omega_m_planck(self):
        """Ω_m ≈ 0.31 (Planck 2018)."""
        assert 0.30 < OMEGA_M < 0.32

    def test_h_z0_equals_h_0(self):
        """At z = 0, H(0) = H_0."""
        H_at_0 = hubble_z(0.0, H_0_PLANCK_KM_S_MPC)
        H_0_per_s = H_0_PLANCK_KM_S_MPC * 1e3 / 3.0857e22
        assert abs(H_at_0 - H_0_per_s) / H_0_per_s < 1e-6

    def test_x_today_about_3e_minus_3(self):
        """X_cosmic today ≈ 0.003 (deep fluid)."""
        X_today = x_cosmic_z(0.0, H_0_PLANCK_KM_S_MPC)
        assert 2e-3 < X_today < 4e-3

    def test_x_at_recombination_is_deep_crystal(self):
        """At z = 1100, X_cosmic ≈ 67-68 (deep crystal regime)."""
        X_rec = x_cosmic_z(1100.0, H_0_PLANCK_KM_S_MPC)
        assert 60 < X_rec < 75

    def test_x_at_matter_radiation_equality(self):
        """At z = 3400, X_cosmic ≈ 450 (very deep crystal)."""
        X_eq = x_cosmic_z(3400.0, H_0_PLANCK_KM_S_MPC)
        assert 400 < X_eq < 600


# ─────────────────────────────────────────────────────────────────────
# X = 1 crossing — load-bearing output
# ─────────────────────────────────────────────────────────────────────


class TestXCrossingRedshift:
    def test_crossing_at_z_about_71_planck(self):
        """Under Planck cosmology (H_0 = 67.4), X = 1 at z ≈ 71.26."""
        z = find_x_crossing_redshift(H_0_km_s_Mpc=H_0_PLANCK_KM_S_MPC)
        assert 70.0 < z < 72.5

    def test_crossing_at_z_about_70_framework(self):
        """Under framework cosmic-baseline H_0 (≈ 68.8), X = 1 at z ≈ 70.30."""
        z = find_x_crossing_redshift(H_0_km_s_Mpc=H_0_FRAMEWORK_KM_S_MPC)
        assert 69.5 < z < 71.5

    def test_h0_sensitivity_under_2_percent(self):
        """The H_0 choice (Planck 67.4 vs framework 68.8) changes the
        crossing redshift by < 2%. The crossing is robust."""
        z_planck = find_x_crossing_redshift(H_0_km_s_Mpc=H_0_PLANCK_KM_S_MPC)
        z_framework = find_x_crossing_redshift(H_0_km_s_Mpc=H_0_FRAMEWORK_KM_S_MPC)
        rel_diff = abs(z_planck - z_framework) / z_planck
        assert rel_diff < 0.02

    def test_x_at_z_70_is_near_1(self):
        """X_cosmic(z=70) ≈ 0.97 — close to but not exactly 1."""
        X = x_cosmic_z(70.0, H_0_PLANCK_KM_S_MPC)
        assert 0.9 < X < 1.05


# ─────────────────────────────────────────────────────────────────────
# Stage 3 — Λ_grav vs H verification
# ─────────────────────────────────────────────────────────────────────


class TestLambdaGravVerification:
    def test_redshift_independence_of_H_over_Lambda(self):
        """H/Λ_grav at cosmic separation l = c/H reduces to ℏc/(Gm²),
        which is redshift-independent. Test by computing at two H values
        for the same mass and verifying the ratio is the same."""
        ratio1 = H_over_lambda_grav(M_AMU_KG, H_per_s=1.0)
        ratio2 = H_over_lambda_grav(M_AMU_KG, H_per_s=1e10)
        # H_per_s shouldn't appear in the result
        assert abs(ratio1 - ratio2) / ratio1 < 1e-12

    def test_h_dominates_for_atomic_test_particle(self):
        """For atomic test mass, H/Λ_grav ≈ 10³⁸ — H dominates."""
        ratio = H_over_lambda_grav(M_AMU_KG, H_per_s=1.0)
        assert 1e37 < ratio < 1e39

    def test_lambda_dominates_for_solar_mass(self):
        """For stellar mass, Λ_grav >> H by 76+ orders of magnitude."""
        ratio = H_over_lambda_grav(M_SUN_KG, H_per_s=1.0)
        assert ratio < 1e-70

    def test_lambda_dominates_for_galactic_mass(self):
        """For galactic mass, Λ_grav >> H by ~98 orders of magnitude."""
        ratio = H_over_lambda_grav(M_GALAXY_KG, H_per_s=1.0)
        assert ratio < 1e-90

    def test_verification_returns_structured_result(self):
        result = verify_h_dominates_lambda_grav()
        assert "structural_fact" in result
        assert "per_mass_class" in result
        assert "mass_class_dependence_finding" in result
        assert "open_question_unaddressed" in result
        assert len(result["per_mass_class"]) == 4


# ─────────────────────────────────────────────────────────────────────
# Master attempt — full Stage 2+3 report
# ─────────────────────────────────────────────────────────────────────


class TestMasterAttempt:
    def test_returns_structured_result(self):
        result = cosmic_x_crossover_attempt()
        assert "scope_notice" in result
        assert "tau_0_sec" in result
        assert "H_0_choices" in result
        assert "epoch_evaluation_planck" in result
        assert "qualitative_shape" in result
        assert "stage_3_lambda_grav_verification" in result

    def test_scope_notice_disclaims_T_c_and_ch_13(self):
        """Scope notice must explicitly state this does NOT address
        T_c provenance and does NOT propose Ch 13 revisions."""
        result = cosmic_x_crossover_attempt()
        scope = result["scope_notice"]
        assert "T_c" in scope
        assert "Ch 13" in scope or "Chapter 13" in scope or "ch 13" in scope.lower()

    def test_both_H_0_choices_present(self):
        result = cosmic_x_crossover_attempt()
        choices = result["H_0_choices"]
        assert "planck_2018" in choices
        assert "framework_cosmic_baseline" in choices
        for name, data in choices.items():
            assert "X_at_z_0" in data
            assert "z_at_X_1" in data
            assert "T_at_X_1_K" in data

    def test_temperature_at_crossing_is_about_200K(self):
        """T_CMB at X = 1 is around 195-200 K (post-recombination,
        structure-formation epoch, NOT a thermal phase boundary —
        just the CMB temperature at the crossing redshift)."""
        result = cosmic_x_crossover_attempt()
        T_planck = result["H_0_choices"]["planck_2018"]["T_at_X_1_K"]
        T_framework = result["H_0_choices"]["framework_cosmic_baseline"]["T_at_X_1_K"]
        assert 180 < T_planck < 220
        assert 180 < T_framework < 220
