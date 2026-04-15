"""Tests for the GRUT foundation — axioms, constitutive equation, noise kernel, anomaly."""

import numpy as np


class TestConstants:
    def test_planck_mass(self):
        from grut.foundation.constants import verify
        assert verify()["M_PLANCK"]

    def test_alpha_em(self):
        from grut.foundation.constants import verify
        assert verify()["ALPHA_EM"]


class TestAxioms:
    def test_keldysh_invertible(self):
        from grut.foundation.axioms import verify
        assert verify()["A0_invertible"]

    def test_tau_I(self):
        from grut.foundation.axioms import verify
        assert verify()["N0_tau_I"]

    def test_tau_I_value(self):
        from grut.foundation.axioms import TAU_I
        from grut.foundation.constants import HBAR
        assert TAU_I == HBAR / 2


class TestConstitutive:
    def test_large_tau_preserves(self):
        from grut.foundation.constitutive import verify
        assert verify()["large_tau_holds"]

    def test_small_tau_tracks(self):
        from grut.foundation.constitutive import verify
        assert verify()["small_tau_tracks"]

    def test_fixed_point_zero(self):
        from grut.foundation.constitutive import verify
        assert verify()["fixed_point_zero"]

    def test_stability_check(self):
        from grut.foundation.constitutive import jacobian_eigenvalues, is_stable
        # Stable: z_target = 0.5 z → eigenvalue = 0.5 < 1
        evs = jacobian_eigenvalues(lambda z: 0.5 * z, 0.0)
        assert is_stable(evs)

    def test_unstable_check(self):
        from grut.foundation.constitutive import jacobian_eigenvalues, is_stable
        # Unstable: z_target = 2 z → eigenvalue = 2 > 1
        evs = jacobian_eigenvalues(lambda z: 2.0 * z, 0.0)
        assert not is_stable(evs)

    def test_newton_target(self):
        from grut.foundation.constitutive import newton_target
        # F(z) = z - 1, dF/dz = 1 → z_target = z - F/dF = z - (z-1) = 1
        z_tgt = newton_target(lambda z: z - 1, lambda z: 1.0, 5.0)
        assert abs(z_tgt - 1.0) < 1e-10


class TestNoiseKernel:
    def test_gold_benchmark(self):
        from grut.foundation.noise_kernel import verify
        assert verify()["gold_benchmark_689Hz"]

    def test_suppression_factor(self):
        from grut.foundation.noise_kernel import verify
        assert verify()["suppression_at_l_eq_R"]

    def test_fdt_classical(self):
        from grut.foundation.noise_kernel import verify
        assert verify()["fdt_classical_limit"]

    def test_lambda_grav_scaling(self):
        from grut.foundation.noise_kernel import lambda_grav
        # Mass-squared scaling: double m → 4x rate
        L1 = lambda_grav(1e-15, 1e-6)
        L2 = lambda_grav(2e-15, 1e-6)
        assert abs(L2 / L1 - 4.0) < 0.01

    def test_lambda_grav_separation(self):
        from grut.foundation.noise_kernel import lambda_grav
        # Far-field l^-1 scaling: double l → half rate
        L1 = lambda_grav(1e-15, 1e-6)
        L2 = lambda_grav(1e-15, 2e-6)
        assert abs(L1 / L2 - 2.0) < 0.01

    def test_kms_tau(self):
        from grut.foundation.noise_kernel import tau_kms
        # At 300 K: tau ~ 4e-14 s
        tau = tau_kms(300.0)
        assert 1e-15 < tau < 1e-12


class TestAnomaly:
    def test_c_final(self):
        from grut.foundation.anomaly import verify
        assert verify()["C_FINAL"]

    def test_r_anomaly(self):
        from grut.foundation.anomaly import verify
        assert verify()["R_ANOMALY"]

    def test_s_ctp(self):
        from grut.foundation.anomaly import verify
        assert verify()["S_CTP"]

    def test_c_final_positive(self):
        from grut.foundation.anomaly import C_FINAL
        assert C_FINAL > 0

    def test_r_between_1_and_2(self):
        from grut.foundation.anomaly import R_ANOMALY
        assert 1 < R_ANOMALY < 2
