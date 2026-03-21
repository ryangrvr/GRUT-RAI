"""Tests for grut.tov_interior — Numerical TOV Interior Metric Integration.

Targeted tests for the modified TOV system, analytical mass solutions,
Phase 4 sign correction, Phase V reappraisal, stress-energy, conservation,
tau parameter scan, and serialization.

~95 tests across 12 test classes.

KEY PHYSICS FINDING:
  The Phase 4 mass "reduction" claim contains a sign error.
  dm/dr < 0 means mass INCREASES inward (decreasing r).
  The scalar field equilibrium WORSENS metric positivity.
"""

from __future__ import annotations

import math

import pytest
import numpy as np

from grut.tov_interior import (
    compute_tov_analysis,
    tov_result_to_dict,
    TOVParams,
    TOVInteriorResult,
    AnalyticalMassResult,
    CriticalProcessingResult,
    stress_energy,
    exterior_boundary_conditions,
    linearized_mass_solution,
    homogeneous_mass_solution,
    critical_processing_analysis,
    scan_tau_analytical,
    build_phase_v_comparison,
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
    """Canonical TOV parameters."""
    return TOVParams()


@pytest.fixture(scope="module")
def linearized(params):
    """Linearized analytical mass solution."""
    return linearized_mass_solution(params)


@pytest.fixture(scope="module")
def homogeneous(params):
    """Homogeneous self-consistent mass solution."""
    return homogeneous_mass_solution(params)


@pytest.fixture(scope="module")
def processing(params):
    """Critical processing analysis result."""
    return critical_processing_analysis(params)


@pytest.fixture(scope="module")
def master_result():
    """Full TOV analysis result (analytical only, skip numerical for speed)."""
    return compute_tov_analysis(
        do_tau_scan=True,
        do_numerical=False,
    )


# ================================================================
# Test 1: Constants
# ================================================================

class TestConstants:
    def test_alpha_vac(self):
        assert math.isclose(ALPHA_VAC, 1.0 / 3.0)

    def test_beta_Q(self):
        assert math.isclose(BETA_Q, 2.0)

    def test_r_s(self):
        assert math.isclose(R_S, 1.0)

    def test_M(self):
        assert math.isclose(M_EXT, 0.5)

    def test_R_eq(self):
        assert math.isclose(R_EQ, 1.0 / 3.0)

    def test_C(self):
        assert math.isclose(C_COMPACTNESS, 3.0)

    def test_tau_canonical(self):
        assert math.isclose(TAU_CANONICAL, math.sqrt(1.5))

    def test_A_eff_constitutive(self):
        assert math.isclose(A_EFF_CONSTITUTIVE, -1.0)

    def test_A_schw(self):
        assert math.isclose(A_SCHW, -2.0)


# ================================================================
# Test 2: Boundary Conditions
# ================================================================

class TestBoundaryConditions:
    def test_m_ext(self, params):
        y0 = exterior_boundary_conditions(params)
        assert math.isclose(y0[0], M_EXT)

    def test_nu_ext(self, params):
        y0 = exterior_boundary_conditions(params)
        f_ext = 1.0 - 2.0 * M_EXT / params.R_ext
        assert math.isclose(y0[1], 0.5 * math.log(f_ext), abs_tol=1e-12)

    def test_Phi_ext(self, params):
        y0 = exterior_boundary_conditions(params)
        assert math.isclose(y0[2], M_EXT / params.R_ext**2)

    def test_Phi_prime_ext(self, params):
        y0 = exterior_boundary_conditions(params)
        assert math.isclose(y0[3], -2.0 * M_EXT / params.R_ext**3)

    def test_f_ext_positive(self, params):
        f_ext = 1.0 - 2.0 * M_EXT / params.R_ext
        assert f_ext > 0

    def test_raises_inside_horizon(self):
        bad_params = TOVParams(R_ext=0.5)  # Inside horizon
        with pytest.raises(ValueError, match="inside the horizon"):
            exterior_boundary_conditions(bad_params)


# ================================================================
# Test 3: Stress-Energy
# ================================================================

class TestStressEnergy:
    def test_rho_negative_at_equilibrium(self):
        r, m = 1.5, 0.5
        X = m / r**2
        rho, _, _ = stress_energy(r, m, X, 0.0, TAU_CANONICAL)
        assert rho < 0

    def test_rho_formula(self):
        r, m = 1.5, 0.5
        X = m / r**2
        tau2 = TAU_CANONICAL**2
        rho, _, _ = stress_energy(r, m, X, 0.0, TAU_CANONICAL)
        expected = X**2 / (2 * tau2) - X**2 / TAU_CANONICAL
        assert math.isclose(rho, expected, abs_tol=1e-12)

    def test_nec_radial_zero_at_equilibrium(self):
        r, m = 1.5, 0.5
        X = m / r**2
        rho, p_r, _ = stress_energy(r, m, X, 0.0, TAU_CANONICAL)
        assert math.isclose(rho + p_r, 0.0, abs_tol=1e-12)

    def test_nec_tangential_zero(self):
        """rho + p_perp = 0 for any Phi' (kinematic identity)."""
        r, m = 1.5, 0.5
        rho, _, p_perp = stress_energy(r, m, 0.2, -0.1, TAU_CANONICAL)
        assert math.isclose(rho + p_perp, 0.0, abs_tol=1e-12)

    def test_nec_radial_with_gradient(self):
        """rho + p_r = (Phi')^2 f for nonzero Phi'."""
        r, m = 1.5, 0.5
        Phi_prime = -0.1
        f = 1.0 - 2.0 * m / r
        rho, p_r, _ = stress_energy(r, m, 0.2, Phi_prime, TAU_CANONICAL)
        assert math.isclose(rho + p_r, Phi_prime**2 * f, abs_tol=1e-12)

    def test_anisotropy(self):
        """p_r - p_perp = (Phi')^2 f."""
        r, m = 1.5, 0.5
        Phi_prime = -0.15
        f = 1.0 - 2.0 * m / r
        _, p_r, p_perp = stress_energy(r, m, 0.2, Phi_prime, TAU_CANONICAL)
        assert math.isclose(p_r - p_perp, Phi_prime**2 * f, abs_tol=1e-12)

    def test_isotropy_at_equilibrium(self):
        r, m = 1.5, 0.5
        X = m / r**2
        _, p_r, p_perp = stress_energy(r, m, X, 0.0, TAU_CANONICAL)
        assert math.isclose(p_r - p_perp, 0.0, abs_tol=1e-12)

    def test_eos_w_minus_one(self):
        """w_r = p_r/rho = -1 at equilibrium."""
        r, m = 1.5, 0.5
        X = m / r**2
        rho, p_r, _ = stress_energy(r, m, X, 0.0, TAU_CANONICAL)
        assert abs(rho) > 1e-20
        assert math.isclose(p_r / rho, -1.0, abs_tol=1e-12)

    def test_eos_universal(self):
        """w = -1 is universal at equilibrium regardless of position."""
        for r, m in [(0.5, 0.3), (1.0, 0.4), (2.0, 0.5), (5.0, 0.5)]:
            X = m / r**2
            rho, p_r, _ = stress_energy(r, m, X, 0.0, TAU_CANONICAL)
            if abs(rho) > 1e-20:
                assert math.isclose(p_r / rho, -1.0, abs_tol=1e-10)


# ================================================================
# Test 4: Linearized Analytical Solution
# ================================================================

class TestLinearized:
    def test_exists(self, linearized):
        assert linearized is not None
        assert linearized.method == "linearized"

    def test_m_at_R_eq_formula(self, linearized, params):
        tau2 = params.tau**2
        coeff = 2.0 * math.pi * M_EXT**2 / tau2
        expected = M_EXT + coeff * (1.0 / R_EQ - 1.0 / params.R_ext)
        assert math.isclose(linearized.m_at_R_eq, expected, abs_tol=1e-10)

    def test_f_at_R_eq_formula(self, linearized):
        expected = 1.0 - 2.0 * linearized.m_at_R_eq / R_EQ
        assert math.isclose(linearized.f_at_R_eq, expected, abs_tol=1e-10)

    def test_mass_accumulates(self, linearized):
        """m(R_eq) > M: mass INCREASES going inward (the sign correction)."""
        assert linearized.m_at_R_eq > M_EXT

    def test_delta_m_positive(self, linearized):
        assert linearized.delta_m > 0

    def test_f_negative(self, linearized):
        assert linearized.f_at_R_eq < 0

    def test_f_worse_than_schwarzschild(self, linearized):
        assert linearized.f_at_R_eq < A_SCHW

    def test_f_worse_than_constitutive(self, linearized):
        assert linearized.f_at_R_eq < A_EFF_CONSTITUTIVE

    def test_dm_dr_negative(self, linearized):
        assert linearized.dm_dr_at_R_eq < 0

    def test_profile_arrays(self, linearized):
        assert linearized.r is not None
        assert linearized.m is not None
        assert len(linearized.r) > 100

    def test_m_exterior_match(self, linearized, params):
        """m(R_ext) = M at the exterior boundary."""
        assert math.isclose(linearized.m[0], M_EXT, abs_tol=1e-10)

    def test_m_monotonically_increases_inward(self, linearized):
        """m increases as r decreases (inward integration)."""
        # r is decreasing; m should be increasing
        dm = np.diff(linearized.m)
        dr = np.diff(linearized.r)
        # Since r decreasing (dr < 0) and m increasing (dm > 0), dm/dr < 0
        assert np.all(dm >= -1e-10)  # m non-decreasing along array


# ================================================================
# Test 5: Homogeneous Self-Consistent Solution
# ================================================================

class TestHomogeneous:
    def test_exists(self, homogeneous):
        assert homogeneous is not None
        assert homogeneous.method == "homogeneous"

    def test_singularity_location(self, homogeneous, params):
        tau2 = params.tau**2
        inv_r_star = 1.0 / params.R_ext + tau2 / (2.0 * math.pi * M_EXT)
        r_star_expected = 1.0 / inv_r_star
        assert math.isclose(
            homogeneous.r_singularity, r_star_expected, abs_tol=1e-10
        )

    def test_singularity_exists(self, homogeneous):
        assert homogeneous.has_singularity

    def test_singularity_in_domain(self, homogeneous):
        """Singularity lies between R_eq and R_ext at canonical params."""
        assert homogeneous.singularity_in_domain

    def test_singularity_near_r_s(self, homogeneous):
        assert abs(homogeneous.r_singularity - R_S) < 0.5

    def test_formal_m_negative_past_singularity(self, homogeneous):
        """Past the singularity, the formal m is negative (not physical)."""
        if math.isfinite(homogeneous.m_at_R_eq):
            assert homogeneous.m_at_R_eq < 0

    def test_formal_f_positive_past_singularity(self, homogeneous):
        """Formal f > 0 past singularity (not physical!)."""
        if math.isfinite(homogeneous.f_at_R_eq):
            assert homogeneous.f_at_R_eq > 0


# ================================================================
# Test 6: Phase 4 Sign Correction
# ================================================================

class TestPhase4SignCorrection:
    def test_dm_dr_negative(self, linearized):
        """dm/dr < 0 at equilibrium (rho < 0)."""
        assert linearized.dm_dr_at_R_eq < 0

    def test_mass_increases_inward(self, linearized):
        """dm/dr < 0 means m INCREASES with decreasing r (the correction)."""
        assert linearized.m_at_R_eq > M_EXT

    def test_f_gets_worse(self, linearized):
        """f(R_eq) < A_Schw: scalar field makes metric MORE negative."""
        assert linearized.f_at_R_eq < A_SCHW

    def test_accumulation_not_reduction(self, linearized):
        """The mass ACCUMULATES (positive delta), not reduces."""
        assert linearized.delta_m > 0
        assert linearized.delta_m_fraction > 0

    def test_metric_positivity_not_achieved(self, linearized):
        assert linearized.f_at_R_eq < 0


# ================================================================
# Test 7: Phase V Comparison
# ================================================================

class TestPhaseVComparison:
    def test_comparison_exists(self, master_result):
        assert master_result.phase_v_comparison is not None

    def test_A_schw(self, master_result):
        pv = master_result.phase_v_comparison
        assert math.isclose(pv.A_schw, -2.0)

    def test_A_eff_constitutive(self, master_result):
        pv = master_result.phase_v_comparison
        assert math.isclose(pv.A_eff_constitutive, -1.0)

    def test_full_einstein_worse_than_constitutive(self, master_result):
        """The full Einstein result is WORSE (more negative) than constitutive."""
        pv = master_result.phase_v_comparison
        assert pv.f_linearized < A_EFF_CONSTITUTIVE

    def test_sign_correction_confirmed(self, master_result):
        pv = master_result.phase_v_comparison
        assert pv.sign_correction_confirmed

    def test_notes_not_empty(self, master_result):
        pv = master_result.phase_v_comparison
        assert len(pv.notes) > 0


# ================================================================
# Test 8: Critical Processing / Phi-dot Threshold
# ================================================================

class TestCriticalProcessing:
    def test_exists(self, processing):
        assert processing is not None
        assert isinstance(processing, CriticalProcessingResult)

    def test_epsilon_crit_positive(self, processing):
        assert processing.epsilon_crit > 0

    def test_epsilon_formula(self, processing, params):
        """epsilon_crit = (m_static - R_eq/2) / vol_integral."""
        vol = (4.0 * math.pi / 3.0) * (params.R_ext**3 - params.R_eq**3)
        expected = (processing.m_static_at_R_eq - params.R_eq / 2.0) / vol
        assert math.isclose(processing.epsilon_crit, expected, abs_tol=1e-10)

    def test_Phi_dot_crit_formula(self, processing):
        """Phi_dot_crit = sqrt(2 * epsilon_crit)."""
        expected = math.sqrt(2.0 * processing.epsilon_crit)
        assert math.isclose(processing.Phi_dot_crit, expected, abs_tol=1e-10)

    def test_Phi_dot_ratio_below_one(self, processing):
        """Only a fraction of the natural processing rate is needed."""
        assert 0 < processing.Phi_dot_ratio < 1.0

    def test_Phi_dot_natural_positive(self, processing):
        assert processing.Phi_dot_natural > 0

    def test_epsilon_small_fraction_at_R_eq(self, processing):
        """epsilon_crit is a tiny fraction of |rho_eq| at R_eq."""
        assert processing.epsilon_over_rho_eq_R_eq < 0.1

    def test_m_static_matches_linearized(self, processing, linearized):
        """Static mass at R_eq should match the linearized solution."""
        assert math.isclose(
            processing.m_static_at_R_eq, linearized.m_at_R_eq, abs_tol=1e-10
        )

    def test_m_target(self, processing, params):
        """Target mass = R_eq / 2 (for f = 0)."""
        assert math.isclose(processing.m_target, params.R_eq / 2.0, abs_tol=1e-12)

    def test_delta_m_to_remove_positive(self, processing):
        """Need to remove positive mass to reach f = 0."""
        assert processing.delta_m_to_remove > 0

    def test_scan_has_entries(self, processing):
        assert len(processing.scan) > 10

    def test_scan_starts_negative(self, processing):
        """f at epsilon=0 is negative (equilibrium regime)."""
        assert processing.scan[0].f_at_R_eq < 0

    def test_scan_ends_positive(self, processing):
        """f at large epsilon is positive (sufficient processing)."""
        assert processing.scan[-1].f_at_R_eq > 0

    def test_scan_crosses_zero(self, processing):
        """Scan transitions from negative to positive f."""
        n_pos = sum(1 for e in processing.scan if e.f_positive)
        assert 0 < n_pos < len(processing.scan)

    def test_notes_not_empty(self, processing):
        assert len(processing.notes) > 0

    def test_barrier_volume_positive(self, processing):
        assert processing.barrier_volume_integral > 0

    def test_in_master_result(self, master_result):
        """Processing analysis should be present in the master result."""
        assert master_result.processing is not None

    def test_serialization_includes_processing(self, master_result):
        d = tov_result_to_dict(master_result)
        assert "critical_processing" in d
        cp = d["critical_processing"]
        assert "epsilon_crit" in cp
        assert "Phi_dot_crit" in cp
        assert "Phi_dot_ratio" in cp


# ================================================================
# Test 9: Tau Scan
# ================================================================

class TestTauScan:
    def test_scan_performed(self, master_result):
        assert len(master_result.tau_scan) > 0

    def test_all_f_negative(self, master_result):
        """f(R_eq) < 0 for all tau values (metric always negative)."""
        for e in master_result.tau_scan:
            assert e.f_at_R_eq < 0

    def test_larger_tau_less_negative(self, master_result):
        """Larger tau gives less negative f (less accumulation)."""
        scan = master_result.tau_scan
        f_vals = [e.f_at_R_eq for e in scan]
        # Tau is increasing; f should be increasing (less negative)
        assert f_vals[-1] > f_vals[0]

    def test_scan_at_canonical_tau(self, master_result, linearized):
        """Canonical tau entry matches the direct linearized result."""
        for e in master_result.tau_scan:
            if math.isclose(e.tau, TAU_CANONICAL, abs_tol=0.01):
                assert math.isclose(e.f_at_R_eq, linearized.f_at_R_eq, abs_tol=0.1)
                break

    def test_scan_varies(self, master_result):
        f_vals = [e.f_at_R_eq for e in master_result.tau_scan]
        assert max(f_vals) - min(f_vals) > 1e-3


# ================================================================
# Test 10: Master Result
# ================================================================

class TestMasterResult:
    def test_valid(self, master_result):
        assert master_result.valid

    def test_linearized_present(self, master_result):
        assert master_result.linearized is not None

    def test_homogeneous_present(self, master_result):
        assert master_result.homogeneous is not None

    def test_phase_v_present(self, master_result):
        assert master_result.phase_v_comparison is not None

    def test_nonclaims_present(self, master_result):
        assert len(master_result.nonclaims) >= 10


# ================================================================
# Test 11: Nonclaims
# ================================================================

class TestNonclaims:
    def test_count(self):
        assert len(NONCLAIMS) >= 10

    def test_sign_correction_mentioned(self):
        assert any("sign" in nc.lower() for nc in NONCLAIMS)

    def test_singularity_mentioned(self):
        assert any("singularity" in nc.lower() for nc in NONCLAIMS)

    def test_static_caveat(self):
        assert any("static" in nc.lower() for nc in NONCLAIMS)

    def test_tau_caveat(self):
        assert any("tau" in nc.lower() for nc in NONCLAIMS)


# ================================================================
# Test 12: Serialization
# ================================================================

class TestSerialization:
    def test_produces_dict(self, master_result):
        d = tov_result_to_dict(master_result)
        assert isinstance(d, dict)

    def test_has_linearized(self, master_result):
        d = tov_result_to_dict(master_result)
        assert "linearized_analytical" in d

    def test_has_homogeneous(self, master_result):
        d = tov_result_to_dict(master_result)
        assert "homogeneous_analytical" in d

    def test_has_phase_v(self, master_result):
        d = tov_result_to_dict(master_result)
        assert "phase_v_comparison" in d

    def test_has_nonclaims(self, master_result):
        d = tov_result_to_dict(master_result)
        assert "nonclaims" in d
        assert len(d["nonclaims"]) >= 10

    def test_has_tau_scan(self, master_result):
        d = tov_result_to_dict(master_result)
        assert "tau_scan" in d
        assert len(d["tau_scan"]) > 0
