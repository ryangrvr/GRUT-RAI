"""Tests for grut.foundation.measurement_resolution — promotes
measurement_resolution from anchored to computed.

Setup: apparatus (1 g, 1 mm) coupled to a quantum object (atom-scale).
The faster-Λ_grav system pulls the slower one across the crystalline
boundary. This is the measurement-problem dissolution at the level
of rate dynamics.
"""

import pytest

from grut.foundation.closure_protocol import TAU_0_SEC, lambda_grav_dp
from grut.foundation.measurement_resolution import (
    acceleration_factor,
    apparatus_dominated_fraction,
    coupled_quantum_relaxation_time,
    free_quantum_relaxation_time,
    joint_crystallinity,
    joint_lambda_grav,
    lambda_grav_apparatus,
    lambda_grav_quantum_object,
    scaling_separation_ratio,
    verify,
)


class TestScalingSeparation:
    """Apparatus and quantum object differ by many orders of magnitude."""

    def test_apparatus_lambda_at_10_to_20(self):
        """1 g, 1 mm apparatus: Λ_grav ~ 10²⁰ Hz."""
        a = lambda_grav_apparatus()
        assert 1e18 < a < 1e22

    def test_quantum_object_lambda_below_apparatus(self):
        b = lambda_grav_quantum_object()
        a = lambda_grav_apparatus()
        assert b < a

    def test_separation_at_least_10_orders(self):
        assert scaling_separation_ratio() > 1e10


class TestJointDominance:
    """Joint Λ_eff is apparatus-dominated."""

    def test_apparatus_carries_almost_all(self):
        a = lambda_grav_apparatus()
        b = lambda_grav_quantum_object()
        assert apparatus_dominated_fraction(a, b) > 0.99

    def test_joint_in_deep_crystal(self):
        a = lambda_grav_apparatus()
        b = lambda_grav_quantum_object()
        assert joint_crystallinity(a, b) > 1e30

    def test_joint_lambda_grav_additive(self):
        assert joint_lambda_grav(3.0, 4.0) == 7.0


class TestAccelerationFactor:
    """Coupling accelerates the quantum object's decoherence."""

    def test_factor_orders_of_magnitude(self):
        a = lambda_grav_apparatus()
        b = lambda_grav_quantum_object()
        assert acceleration_factor(a, b) > 1e10

    def test_factor_equals_1_plus_lambda_a_over_b(self):
        a = 100.0
        b = 1.0
        # acceleration = (1/b) / (1/(a+b)) = (a+b)/b = 101.0
        assert abs(acceleration_factor(a, b) - 101.0) < 1e-12

    def test_relaxation_times_inverse(self):
        b = 1.5
        assert abs(free_quantum_relaxation_time(b) - 1.0 / b) < 1e-12

    def test_coupled_relaxation_dominated_by_apparatus(self):
        a = 1e20
        b = 1e-10
        coupled = coupled_quantum_relaxation_time(a, b)
        # Should be ~ 1/a, not 1/b
        assert coupled < 1e-15


class TestVerifyHarness:

    def test_all_pass(self):
        checks = verify()
        failed = [k for k, v in checks.items() if not v]
        assert not failed, f"Measurement-resolution failures: {failed}"


class TestMeasurementProblemFraming:
    """Sanity: the canonical Stern-Gerlach example reproduces the
    'apparatus drags atom across the boundary' picture."""

    def test_atom_alone_is_quantum(self):
        """Atom standalone: Λ_grav × τ_0 ≪ 1 (quantum regime)."""
        lam_atom = lambda_grav_dp(m_kg=1e-26, l_m=1e-10, R_m=1e-10)
        assert lam_atom * TAU_0_SEC < 1.0

    def test_atom_with_apparatus_is_classical(self):
        """Atom coupled to a 1g/1mm apparatus: joint X ≫ 1."""
        a = lambda_grav_apparatus()
        lam_atom = lambda_grav_dp(m_kg=1e-26, l_m=1e-10, R_m=1e-10)
        joint_X = joint_crystallinity(a, lam_atom)
        assert joint_X > 1e30
