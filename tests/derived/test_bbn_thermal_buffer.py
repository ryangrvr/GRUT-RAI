"""Tests for the BBN thermal-buffer calculation.

This test suite pins the standard-cosmology calculation testing one
piece of an external research hypothesis. The framework remains
uncommitted to the broader narrative; this calculation tests only
whether BBN binding energy provides a meaningful thermal buffer
against radiation cooling.

Pre-committed expectation (registered in module): outcome (ii) cooling
slowed but not plateaued. Actual result: outcome (iii) negligible.
The result is materially different from the expectation by ~10
orders of magnitude — driven by the η_B suppression.
"""

from __future__ import annotations

import math

import pytest

from grut.derived.cosmology.bbn_thermal_buffer import (
    B_HE4_MEV,
    ETA_B_PLANCK,
    G_STAR_MID_BBN,
    G_STAR_PRE_ANNIHILATION,
    T_BBN_END_MEV,
    T_BBN_START_MEV,
    T_MID_BBN_MEV,
    Y_P_BBN,
    bbn_thermal_buffer_attempt,
    bbn_window_times,
    binding_energy_per_baryon_MeV,
    cosmic_time_radiation_dom_seconds,
    energy_density_ratio,
    hubble_rate_radiation_dom_per_s,
    per_baryon_energy_comparison,
    radiation_energy_density_natural,
    rate_ratio,
)


# ─────────────────────────────────────────────────────────────────────
# Standard cosmology sanity checks
# ─────────────────────────────────────────────────────────────────────


class TestStandardCosmologySanity:
    def test_eta_B_in_planck_range(self):
        """η_B ≈ 6×10⁻¹⁰ from Planck/standard BBN."""
        assert 5e-10 < ETA_B_PLANCK < 7e-10

    def test_helium_binding_energy(self):
        """B(⁴He) ≈ 28.3 MeV (PDG)."""
        assert 28.0 < B_HE4_MEV < 28.4

    def test_helium_mass_fraction_at_BBN_end(self):
        """Y_p ≈ 0.247 (Planck)."""
        assert 0.24 < Y_P_BBN < 0.26

    def test_cosmic_time_at_T1_MeV_about_1_s(self):
        """Standard relation: t ≈ 2.4 / √g_* / (T/MeV)² seconds.
        At T = 1 MeV with g_* = 10.75, t ≈ 0.74 s.
        Hubble's 1948 estimate, refined to within factor 2."""
        t = cosmic_time_radiation_dom_seconds(1.0, G_STAR_PRE_ANNIHILATION)
        assert 0.5 < t < 2.0

    def test_cosmic_time_at_T_BBN_end_about_1000s(self):
        """At T ≈ 30 keV, post-annihilation, t ~ 1000 s."""
        t = cosmic_time_radiation_dom_seconds(T_BBN_END_MEV, 3.36)
        assert 500 < t < 5000

    def test_hubble_rate_at_mid_BBN(self):
        """At T = 0.1 MeV, H ≈ 0.01 s⁻¹ (Hubble time ~100 s)."""
        H = hubble_rate_radiation_dom_per_s(T_MID_BBN_MEV, G_STAR_MID_BBN)
        assert 1e-3 < H < 1e-1

    def test_radiation_energy_density_scales_as_T4(self):
        """ρ_rad ∝ T⁴ in natural units."""
        rho1 = radiation_energy_density_natural(0.1, G_STAR_MID_BBN)
        rho2 = radiation_energy_density_natural(0.05, G_STAR_MID_BBN)
        ratio_predicted = (0.1 / 0.05) ** 4  # = 16
        ratio_actual = rho1 / rho2
        assert abs(ratio_actual - ratio_predicted) / ratio_predicted < 1e-6


# ─────────────────────────────────────────────────────────────────────
# Per-baryon comparison — the cleanest dimensional read
# ─────────────────────────────────────────────────────────────────────


class TestPerBaryonComparison:
    def test_binding_per_baryon_about_1p75_MeV(self):
        """Y_p × B(⁴He) / 4 ≈ 0.247 × 28.3 / 4 ≈ 1.747 MeV per baryon."""
        e = binding_energy_per_baryon_MeV()
        assert 1.7 < e < 1.8

    def test_radiation_per_baryon_at_mid_BBN(self):
        """At T = 0.1 MeV, photon density / baryon density ≈ 1/η_B ≈ 1.6×10⁹.
        Average photon energy ≈ 2.7 T ≈ 0.27 MeV.
        So radiation energy per baryon ≈ 0.27 × 1.6×10⁹ ≈ 4×10⁸ MeV."""
        comp = per_baryon_energy_comparison()
        assert 1e8 < comp["radiation_MeV_per_baryon"] < 1e10

    def test_ratio_about_4e_minus_9(self):
        """The smoking gun: binding energy per baryon is ~4×10⁻⁹ of
        radiation energy per baryon. This is η_B-suppressed."""
        comp = per_baryon_energy_comparison()
        ratio = comp["ratio_bind_over_rad_per_baryon"]
        # Pin within a factor of 2 (loose enough to allow definitional
        # variation in T or η_B)
        assert 1e-9 < ratio < 1e-8


# ─────────────────────────────────────────────────────────────────────
# Density and rate ratios
# ─────────────────────────────────────────────────────────────────────


class TestEnergyDensityRatio:
    def test_ratio_is_negligible(self):
        """E_bind_total / ρ_rad ≪ 1% at mid-BBN."""
        result = energy_density_ratio()
        assert result["ratio_E_bind_over_rho_rad"] < 0.01

    def test_ratio_is_about_1e_minus_9(self):
        """Pin the order of magnitude."""
        result = energy_density_ratio()
        assert 1e-10 < result["ratio_E_bind_over_rho_rad"] < 1e-8

    def test_interpretation_is_negligible(self):
        result = energy_density_ratio()
        assert "Negligible" in result["interpretation"]


class TestRateRatio:
    def test_rate_ratio_is_negligible(self):
        """Injection rate / cooling rate ≪ 1% at any sensible BBN window."""
        for duration in (100.0, 1000.0, 10000.0):
            result = rate_ratio(bbn_duration_s=duration)
            assert result["ratio_injection_over_cooling"] < 0.01

    def test_rate_ratio_is_about_1e_minus_10(self):
        """Pin the order of magnitude at the 1000 s window."""
        result = rate_ratio(bbn_duration_s=1000.0)
        assert 1e-11 < result["ratio_injection_over_cooling"] < 1e-9


# ─────────────────────────────────────────────────────────────────────
# Master verdict
# ─────────────────────────────────────────────────────────────────────


class TestMasterVerdict:
    def test_outcome_is_iii_negligible(self):
        """The framework's calculation gives outcome (iii) — BBN is
        NOT a thermal buffer. This is materially different from the
        pre-committed expectation (ii) — by ~10 orders of magnitude."""
        result = bbn_thermal_buffer_attempt()
        assert result["outcome"] == "iii_negligible"

    def test_verdict_states_quantitatively_wrong(self):
        """The verdict must explicitly state the hypothesis claim is
        quantitatively wrong, not just imprecise."""
        result = bbn_thermal_buffer_attempt()
        verdict = result["verdict"]
        assert "QUANTITATIVELY WRONG" in verdict or "wrong" in verdict.lower()

    def test_implications_acknowledge_pre_commit_failure(self):
        """The pre-committed expectation was outcome (ii). The actual
        result is (iii). The implications field must surface this."""
        result = bbn_thermal_buffer_attempt()
        assert "materially different" in result["implications_for_hypothesis"]

    def test_scope_notice_disclaims_GRUT_specificity(self):
        """The calculation is standard cosmology, not GRUT-specific.
        The framework is uncommitted to the broader hypothesis."""
        result = bbn_thermal_buffer_attempt()
        scope = result["scope_notice"]
        assert "STANDARD COSMOLOGY" in scope
        assert "uncommitted" in scope

    def test_pre_committed_expectation_recorded(self):
        result = bbn_thermal_buffer_attempt()
        assert "Pre-committed" in result["pre_committed_expectation"]
        assert "(ii)" in result["pre_committed_expectation"]


# ─────────────────────────────────────────────────────────────────────
# BBN window definitions
# ─────────────────────────────────────────────────────────────────────


class TestBBNWindow:
    def test_wide_window_starts_around_1_second(self):
        times = bbn_window_times()
        assert 0.5 < times["wide_window"]["t_start_s"] < 2.0

    def test_wide_window_ends_around_1000_seconds(self):
        times = bbn_window_times()
        assert 500 < times["wide_window"]["t_end_s"] < 5000

    def test_window_brackets_BBN_at_known_T(self):
        """T_BBN_START is neutron freeze-out (~0.7 MeV).
        T_BBN_END is ⁴He completion (~30 keV)."""
        assert 0.5 < T_BBN_START_MEV < 1.0
        assert 0.020 < T_BBN_END_MEV < 0.05
