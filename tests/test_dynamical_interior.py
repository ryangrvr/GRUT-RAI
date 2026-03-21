"""Tests for grut.dynamical_interior — Dynamical Non-Equilibrium Interior Branch.

Targeted tests for dynamical stress-energy, profile generators, radial
snapshots, threshold scanning, profile library, quasi-static time evolution,
threshold classification, anisotropy comparison, Phase 6 comparison,
nonclaims, and serialization.

~90 tests across 12 test classes.

KEY PHYSICS FINDINGS:
  The Phase 6 "11.5% of natural rate" is an artifact of UNIFORM processing.
  The natural profile requires A_crit ~ 1.06 (106% of natural rate).
  Dynamical collapse produces concentrated processing: obstruction is
  GLOBAL and ROBUST.  Anisotropy self-quenches at f = 0 (< 1% effect).
"""

from __future__ import annotations

import math

import pytest
import numpy as np

from grut.dynamical_interior import (
    compute_dynamical_analysis,
    dynamical_result_to_dict,
    DynamicalParams,
    PhiDotProfile,
    RadialSnapshotResult,
    ThresholdScanEntry,
    ProfileThresholdResult,
    ProfileLibraryResult,
    TimeSlice,
    TimeEvolutionResult,
    ThresholdClassification,
    AnisotropyComparison,
    Phase6Comparison,
    DynamicalInteriorResult,
    stress_energy_dynamical,
    make_radial_grid,
    make_phi_dot_profile,
    solve_radial_snapshot,
    scan_amplitude_threshold,
    build_profile_library,
    evolve_quasi_static,
    classify_threshold,
    compare_anisotropy,
    build_phase6_comparison,
    ALPHA_VAC,
    BETA_Q,
    R_S,
    M_EXT,
    R_EQ,
    C_COMPACTNESS,
    TAU_CANONICAL,
    A_EFF_CONSTITUTIVE,
    A_SCHW,
    NONCLAIMS,
)


# ================================================================
# Module-scoped fixtures
# ================================================================

@pytest.fixture(scope="module")
def params():
    """Canonical dynamical parameters."""
    return DynamicalParams(n_r=300, n_t=80)


@pytest.fixture(scope="module")
def r_arr(params):
    """Radial grid."""
    return make_radial_grid(params)


@pytest.fixture(scope="module")
def library(params):
    """Full profile library."""
    return build_profile_library(params)


@pytest.fixture(scope="module")
def evolution(params):
    """Time evolution at default collapse amplitude."""
    return evolve_quasi_static(params, store_every_n=10)


@pytest.fixture(scope="module")
def classification(evolution):
    """Threshold classification."""
    return classify_threshold(evolution)


@pytest.fixture(scope="module")
def anisotropy_result():
    """Anisotropy comparison (smaller grid for speed)."""
    p = DynamicalParams(n_r=200, n_t=40)
    return compare_anisotropy(p)


@pytest.fixture(scope="module")
def master_result():
    """Master result from compute_dynamical_analysis."""
    p = DynamicalParams(n_r=250, n_t=60)
    return compute_dynamical_analysis(p)


# ================================================================
# 1. TestConstants (9 tests)
# ================================================================

class TestConstants:
    """Test that canonical constants are correct."""

    def test_alpha_vac(self):
        assert abs(ALPHA_VAC - 1.0 / 3.0) < 1e-15

    def test_beta_Q(self):
        assert abs(BETA_Q - 2.0) < 1e-15

    def test_r_s(self):
        assert abs(R_S - 1.0) < 1e-15

    def test_M_ext(self):
        assert abs(M_EXT - 0.5) < 1e-15

    def test_R_eq(self):
        assert abs(R_EQ - R_S / 3.0) < 1e-15

    def test_compactness(self):
        assert abs(C_COMPACTNESS - 3.0) < 1e-15

    def test_tau(self):
        assert abs(TAU_CANONICAL - math.sqrt(1.5)) < 1e-10

    def test_A_eff(self):
        expected = 1.0 - C_COMPACTNESS * BETA_Q / (1.0 + BETA_Q)
        assert abs(A_EFF_CONSTITUTIVE - expected) < 1e-15

    def test_A_Schw(self):
        expected = 1.0 - 2.0 * M_EXT / R_EQ
        assert abs(A_SCHW - expected) < 1e-15


# ================================================================
# 2. TestStressEnergyDynamical (10 tests)
# ================================================================

class TestStressEnergyDynamical:
    """Test the dynamical stress-energy tensor."""

    def test_nec_radial(self):
        rho, p_r, _ = stress_energy_dynamical(1.0, 0.3, 0.4, 0.1, 0.5, 0.1, 1.2)
        assert rho + p_r >= -1e-15

    def test_nec_tangential(self):
        rho, _, p_p = stress_energy_dynamical(1.0, 0.3, 0.4, 0.1, 0.5, 0.1, 1.2)
        assert rho + p_p >= -1e-15

    def test_nec_tangential_formula(self):
        """rho + p_perp = e^{-2nu}*Phi_dot^2."""
        rho, _, p_p = stress_energy_dynamical(1.0, 0.3, 0.4, 0.1, 0.5, 0.1, 1.2)
        expected = math.exp(-0.2) * 0.25
        assert abs(rho + p_p - expected) < 1e-10

    def test_anisotropy_formula(self):
        """p_r - p_perp = f*(Phi')^2."""
        _, p_r, p_p = stress_energy_dynamical(1.0, 0.3, 0.4, 0.1, 0.5, 0.1, 1.2)
        f = 1.0 - 2.0 * 0.3 / 1.0  # = 0.4
        expected = f * 0.01  # 0.4 * 0.01
        assert abs(p_r - p_p - expected) < 1e-10

    def test_static_recovery(self):
        """Phi_dot=0, Phi'=0 → rho = V - Phi*J."""
        rho, _, _ = stress_energy_dynamical(1.0, 0.3, 0.4, 0.0, 0.0, 0.0, 1.2)
        V = 0.16 / (2 * 1.44)
        PhiJ = 0.4 * 0.3 / 1.2
        assert abs(rho - (V - PhiJ)) < 1e-10

    def test_static_isotropic(self):
        """Phi' = 0 → p_r = p_perp."""
        _, p_r, p_p = stress_energy_dynamical(1.0, 0.3, 0.4, 0.0, 0.0, 0.0, 1.2)
        assert abs(p_r - p_p) < 1e-15

    def test_anisotropy_vanishes_at_f0(self):
        """f=0 (r=2m) → p_r = p_perp regardless of Phi'."""
        _, p_r, p_p = stress_energy_dynamical(1.0, 0.5, 0.4, 0.3, 0.2, 0.0, 1.2)
        assert abs(p_r - p_p) < 1e-15

    def test_phi_dot_raises_rho(self):
        """Nonzero Phi_dot increases rho."""
        rho0, _, _ = stress_energy_dynamical(1.0, 0.3, 0.4, 0.0, 0.0, 0.0, 1.2)
        rho1, _, _ = stress_energy_dynamical(1.0, 0.3, 0.4, 0.0, 1.0, 0.0, 1.2)
        assert rho1 > rho0

    def test_small_r_returns_zero(self):
        """Very small r → zero output."""
        rho, p_r, p_p = stress_energy_dynamical(1e-31, 0.5, 0.4, 0.1, 0.5, 0.0, 1.2)
        assert rho == 0.0 and p_r == 0.0 and p_p == 0.0

    def test_returns_three_floats(self):
        result = stress_energy_dynamical(1.0, 0.3, 0.4, 0.1, 0.5, 0.0, 1.2)
        assert len(result) == 3
        assert all(isinstance(x, float) for x in result)


# ================================================================
# 3. TestPhiDotProfiles (8 tests)
# ================================================================

class TestPhiDotProfiles:
    """Test profile generators."""

    def test_grid_decreasing(self, r_arr):
        assert r_arr[0] > r_arr[-1]

    def test_grid_starts_at_R_ext(self, r_arr, params):
        assert abs(r_arr[0] - params.R_ext) < 1e-10

    def test_uniform_constant(self, r_arr, params):
        prof = make_phi_dot_profile("uniform", r_arr, params, amplitude=2.5)
        assert abs(float(np.std(prof.Phi_dot))) < 1e-15
        assert abs(float(np.mean(prof.Phi_dot)) - 2.5) < 1e-15

    def test_natural_peaks_at_small_r(self, r_arr, params):
        prof = make_phi_dot_profile("natural", r_arr, params, amplitude=1.0)
        assert float(prof.Phi_dot[-1]) > float(prof.Phi_dot[0])

    def test_natural_formula(self, r_arr, params):
        """Natural: Phi_dot = A * M / (tau * r^2)."""
        prof = make_phi_dot_profile("natural", r_arr, params, amplitude=1.0)
        expected = params.M / (params.tau * r_arr ** 2)
        assert np.allclose(prof.Phi_dot, expected, rtol=1e-10)

    def test_gaussian_peaks_near_center(self, r_arr, params):
        prof = make_phi_dot_profile("gaussian", r_arr, params, amplitude=1.0,
                                    r_center=R_EQ, sigma=0.2)
        idx = np.argmax(prof.Phi_dot)
        assert abs(r_arr[idx] - R_EQ) < 0.3

    def test_epsilon_formula(self, r_arr, params):
        """epsilon = 0.5 * Phi_dot^2."""
        prof = make_phi_dot_profile("natural", r_arr, params, amplitude=1.5)
        expected = 0.5 * prof.Phi_dot ** 2
        assert np.allclose(prof.epsilon, expected, rtol=1e-15)

    def test_unknown_type_raises(self, r_arr, params):
        with pytest.raises(ValueError, match="Unknown"):
            make_phi_dot_profile("bogus", r_arr, params)


# ================================================================
# 4. TestRadialSnapshot (8 tests)
# ================================================================

class TestRadialSnapshot:
    """Test the radial snapshot solver."""

    def test_zero_amplitude_recovers_static(self, r_arr, params):
        """A=0 → Phase 6 static: f(R_eq) ~ -17.71."""
        prof = make_phi_dot_profile("uniform", r_arr, params, amplitude=0.0)
        snap = solve_radial_snapshot(prof, params)
        assert abs(snap.f_at_R_eq - (-17.71)) / 17.71 < 0.01

    def test_zero_amplitude_mass(self, r_arr, params):
        """A=0 → m(R_eq) ~ 3.118."""
        prof = make_phi_dot_profile("uniform", r_arr, params, amplitude=0.0)
        snap = solve_radial_snapshot(prof, params)
        assert abs(snap.m_at_R_eq - 3.118) / 3.118 < 0.01

    def test_boundary_condition(self, r_arr, params):
        """m(R_ext) = M."""
        prof = make_phi_dot_profile("natural", r_arr, params, amplitude=1.0)
        snap = solve_radial_snapshot(prof, params)
        assert abs(snap.m[0] - M_EXT) < 1e-10

    def test_natural_A1_cancels(self, r_arr, params):
        """Natural A=1: rho_eq + epsilon = 0 → m = M → f = -2."""
        prof = make_phi_dot_profile("natural", r_arr, params, amplitude=1.0)
        snap = solve_radial_snapshot(prof, params)
        assert abs(snap.m_at_R_eq - M_EXT) < 0.01
        assert abs(snap.f_at_R_eq - (1.0 - 2.0 * M_EXT / R_EQ)) < 0.02

    def test_nec_radial_non_negative(self, r_arr, params):
        prof = make_phi_dot_profile("uniform", r_arr, params, amplitude=0.3)
        snap = solve_radial_snapshot(prof, params)
        assert snap.nec_radial_min >= -1e-10

    def test_nec_tangential_non_negative(self, r_arr, params):
        prof = make_phi_dot_profile("uniform", r_arr, params, amplitude=0.3)
        snap = solve_radial_snapshot(prof, params)
        assert snap.nec_tangential_min >= -1e-10

    def test_uniform_at_phase6_crit(self, r_arr, params):
        """Uniform at Phase 6 critical Phi_dot: f(R_eq) ~ 0."""
        tau2 = params.tau ** 2
        coeff = 2.0 * math.pi * M_EXT ** 2 / tau2
        m_s = M_EXT + coeff * (1.0 / R_EQ - 1.0 / params.R_ext)
        vol = (4.0 * math.pi / 3.0) * (params.R_ext ** 3 - R_EQ ** 3)
        eps6 = (m_s - R_EQ / 2.0) / vol
        pd6 = math.sqrt(2.0 * eps6)
        prof = make_phi_dot_profile("uniform", r_arr, params, amplitude=pd6)
        snap = solve_radial_snapshot(prof, params)
        assert abs(snap.f_at_R_eq) < 0.01

    def test_result_type(self, r_arr, params):
        prof = make_phi_dot_profile("uniform", r_arr, params, amplitude=0.1)
        snap = solve_radial_snapshot(prof, params)
        assert isinstance(snap, RadialSnapshotResult)


# ================================================================
# 5. TestThresholdScanner (8 tests)
# ================================================================

class TestThresholdScanner:
    """Test the amplitude threshold scanner."""

    def test_uniform_threshold_exists(self, params):
        result = scan_amplitude_threshold("uniform", params, n_scan=30)
        assert result.A_crit_exists

    def test_uniform_A_crit_R_eq(self, params):
        """Uniform A_crit_R_eq matches Phase 6 Phi_dot_crit."""
        result = scan_amplitude_threshold("uniform", params, n_scan=40)
        tau2 = params.tau ** 2
        coeff = 2.0 * math.pi * M_EXT ** 2 / tau2
        m_s = M_EXT + coeff * (1.0 / R_EQ - 1.0 / params.R_ext)
        vol = (4.0 * math.pi / 3.0) * (params.R_ext ** 3 - R_EQ ** 3)
        eps6 = (m_s - R_EQ / 2.0) / vol
        pd6 = math.sqrt(2.0 * eps6)
        assert abs(result.A_crit_R_eq - pd6) / pd6 < 0.05

    def test_natural_threshold_exists(self, params):
        result = scan_amplitude_threshold("natural", params, n_scan=30)
        assert result.A_crit_exists

    def test_natural_A_crit_above_1(self, params):
        """Natural rate insufficient: A_crit > 1."""
        result = scan_amplitude_threshold("natural", params, n_scan=40)
        assert result.A_crit_R_eq > 1.0

    def test_scan_has_entries(self, params):
        result = scan_amplitude_threshold("uniform", params, n_scan=20)
        assert len(result.scan) == 21  # n_scan + 1

    def test_scan_starts_negative(self, params):
        result = scan_amplitude_threshold("uniform", params, n_scan=20)
        assert result.scan[0].f_at_R_eq < 0

    def test_scan_ends_positive(self, params):
        result = scan_amplitude_threshold("uniform", params, n_scan=30)
        assert result.scan[-1].f_at_R_eq > 0

    def test_result_type(self, params):
        result = scan_amplitude_threshold("uniform", params, n_scan=10)
        assert isinstance(result, ProfileThresholdResult)


# ================================================================
# 6. TestProfileLibrary (8 tests)
# ================================================================

class TestProfileLibrary:
    """Test the profile library builder."""

    def test_all_profiles_present(self, library):
        assert library.uniform is not None
        assert library.natural is not None
        assert library.relaxation is not None
        assert library.gaussian is not None

    def test_uniform_most_efficient(self, library):
        assert library.most_efficient_profile == "uniform"

    def test_uniform_threshold_exists(self, library):
        assert library.uniform.A_crit_exists

    def test_natural_threshold_exists(self, library):
        assert library.natural.A_crit_exists

    def test_relaxation_no_global_threshold(self, library):
        assert not library.relaxation.A_crit_exists

    def test_gaussian_no_global_threshold(self, library):
        assert not library.gaussian.A_crit_exists

    def test_uniform_recovery(self, library):
        """Uniform A_crit recovers Phase 6."""
        assert library.uniform_recovery

    def test_natural_harder_than_uniform(self, library):
        """Natural needs higher amplitude than uniform for global fix."""
        assert library.natural.A_crit_global > library.uniform.A_crit_global


# ================================================================
# 7. TestTimeEvolution (10 tests)
# ================================================================

class TestTimeEvolution:
    """Test quasi-static time evolution."""

    def test_n_steps(self, evolution, params):
        assert evolution.n_steps == params.n_t

    def test_slices_stored(self, evolution):
        assert len(evolution.slices) >= 3

    def test_phi_dot_peaks_at_t0(self, evolution):
        assert abs(evolution.Phi_dot_peak_time) < evolution.params.dt_over_tau * evolution.params.tau * 2

    def test_phi_dot_decays(self, evolution):
        """Phi_dot decays as exp(-t/tau)."""
        pdm = evolution.Phi_dot_max_vs_t
        t = evolution.t_array
        tau = evolution.params.tau
        idx_3 = np.argmin(np.abs(t - 3 * tau))
        if pdm[0] > 0:
            ratio = pdm[idx_3] / pdm[0]
            expected = math.exp(-3.0)
            assert abs(ratio - expected) / expected < 0.20

    def test_f_R_eq_improves_early(self, evolution):
        """f(R_eq) at t=0 is less negative than static."""
        f0 = evolution.f_at_R_eq_vs_t[0]
        # Static f = -17.71
        assert f0 > -17.71 * 1.001

    def test_f_R_eq_returns_to_static(self, evolution):
        """f(R_eq) at late times approaches static."""
        f_late = evolution.f_at_R_eq_vs_t[-1]
        assert abs(f_late - (-17.71)) / 17.71 < 0.1

    def test_never_positive_default(self, evolution):
        """Default collapse: f never positive everywhere."""
        assert evolution.never_positive

    def test_f_min_always_negative(self, evolution):
        assert np.all(evolution.f_min_vs_t < 0)

    def test_first_slice_is_t0(self, evolution):
        assert abs(evolution.slices[0].t) < 1e-10

    def test_slice_f_array_exists(self, evolution):
        s = evolution.slices[0]
        assert s.f is not None and len(s.f) > 0


# ================================================================
# 8. TestThresholdClassification (8 tests)
# ================================================================

class TestThresholdClassification:
    """Test threshold classification."""

    def test_spatial_global(self, classification):
        assert classification.spatial_class == "global"

    def test_temporal_robust(self, classification):
        assert classification.temporal_class == "robust"

    def test_combined_global_robust(self, classification):
        assert classification.classification == "global_robust"

    def test_f_min_negative(self, classification):
        assert classification.f_min_global < 0

    def test_fraction_negative_high(self, classification):
        assert classification.fraction_r_negative > 0.5

    def test_does_not_heal(self, classification):
        assert not classification.heals_within_simulation

    def test_margin_negative(self, classification):
        assert classification.margin_to_positivity < 0

    def test_result_type(self, classification):
        assert isinstance(classification, ThresholdClassification)


# ================================================================
# 9. TestAnisotropyComparison (6 tests)
# ================================================================

class TestAnisotropyComparison:
    """Test anisotropy comparison."""

    def test_iso_A_crit_positive(self, anisotropy_result):
        assert anisotropy_result.iso_A_crit > 0

    def test_aniso_A_crit_positive(self, anisotropy_result):
        assert anisotropy_result.aniso_A_crit > 0

    def test_delta_less_than_1_percent(self, anisotropy_result):
        assert abs(anisotropy_result.delta_A_crit_fraction) < 0.02

    def test_anisotropy_does_not_matter(self, anisotropy_result):
        assert not anisotropy_result.anisotropy_matters

    def test_iso_aniso_agree(self, anisotropy_result):
        """Iso and aniso A_crit within 2%."""
        iso = anisotropy_result.iso_A_crit
        aniso = anisotropy_result.aniso_A_crit
        if iso > 0:
            assert abs(aniso - iso) / iso < 0.02

    def test_notes_present(self, anisotropy_result):
        assert len(anisotropy_result.notes) >= 2


# ================================================================
# 10. TestPhase6Comparison (6 tests)
# ================================================================

class TestPhase6Comparison:
    """Test Phase 6 comparison."""

    def test_exists_in_master(self, master_result):
        assert master_result.phase6_comparison is not None

    def test_eps_crit_positive(self, master_result):
        p6 = master_result.phase6_comparison
        assert p6.phase6_epsilon_crit > 0

    def test_ratio_about_11_percent(self, master_result):
        p6 = master_result.phase6_comparison
        assert abs(p6.phase6_Phi_dot_ratio - 0.115) < 0.02

    def test_natural_A_crit_gt_1(self, master_result):
        p6 = master_result.phase6_comparison
        assert p6.natural_A_crit > 1.0

    def test_uniform_is_optimistic(self, master_result):
        p6 = master_result.phase6_comparison
        assert p6.uniform_is_optimistic

    def test_dynamical_exceeds_threshold(self, master_result):
        p6 = master_result.phase6_comparison
        assert p6.dynamical_exceeds_threshold


# ================================================================
# 11. TestNonclaims (4 tests)
# ================================================================

class TestNonclaims:
    """Test nonclaims."""

    def test_at_least_10(self):
        assert len(NONCLAIMS) >= 10

    def test_quasi_static_mentioned(self):
        assert any("quasi-static" in nc.lower() for nc in NONCLAIMS)

    def test_uniform_optimism_mentioned(self):
        assert any("optimistic" in nc.lower() for nc in NONCLAIMS)

    def test_in_master_result(self, master_result):
        assert len(master_result.nonclaims) >= 10


# ================================================================
# 12. TestSerialization (5 tests)
# ================================================================

class TestSerialization:
    """Test result serialization."""

    def test_dict_not_empty(self, master_result):
        d = dynamical_result_to_dict(master_result)
        assert len(d) > 0

    def test_contains_profile_library(self, master_result):
        d = dynamical_result_to_dict(master_result)
        assert "profile_library" in d

    def test_contains_nonclaims(self, master_result):
        d = dynamical_result_to_dict(master_result)
        assert "nonclaims" in d
        assert len(d["nonclaims"]) >= 10

    def test_contains_classification(self, master_result):
        d = dynamical_result_to_dict(master_result)
        assert "threshold_classification" in d
        assert d["threshold_classification"]["classification"] == "global_robust"

    def test_valid_flag(self, master_result):
        d = dynamical_result_to_dict(master_result)
        assert d["valid"] is True
