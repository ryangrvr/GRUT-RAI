"""Tests for the Koide circulant unification (frontier #1 partial result).

Locks in: K_N(A) = (1+A²/2)/N; K=2/3 ⟺ A=√2 (Z₃ alone does NOT fix K);
A²=N−1 ⟹ (K,θ) = ((N+1)/2N, (N+1)/2N²) = (2/3, 2/9) at N=3.
"""

from fractions import Fraction

import numpy as np
import pytest

from grut.derived.flavor.koide_circulant_unification import (
    K_circulant_symbolic, K_closed_form, K_from_unification,
    theta_from_unification, amplitude_for_koide, observed_amplitude,
    fixed_point_amplitude_nogo, verify,
)


def test_verify_all_legs():
    assert all(verify().values())


@pytest.mark.parametrize("N", [3, 4, 5])
def test_circulant_closed_form(N):
    import sympy as sp
    A = sp.Symbol("A", real=True)
    assert sp.simplify(K_circulant_symbolic(N) - K_closed_form(A, N)) == 0


def test_Z3_alone_does_not_force_two_thirds():
    # K depends on amplitude; Z₃ symmetry (theta-independence) is not enough.
    assert not np.isclose(float(K_closed_form(1.0, 3)), 2 / 3)
    assert np.isclose(float(K_closed_form(np.sqrt(2), 3)), 2 / 3)


def test_koide_requires_amplitude_sqrt2():
    assert np.isclose(amplitude_for_koide(Fraction(2, 3), 3), np.sqrt(2))


def test_unification_gives_K_and_theta_at_N3():
    assert K_from_unification(3) == Fraction(2, 3)
    assert theta_from_unification(3) == Fraction(2, 9)


@pytest.mark.parametrize("N", [3, 4, 5])
def test_unification_consistency(N):
    # A²=N−1 numeric K matches (N+1)/(2N); θ = K/N exactly.
    assert np.isclose(float(K_closed_form(np.sqrt(N - 1), N)),
                      float(K_from_unification(N)))
    assert theta_from_unification(N) == K_from_unification(N) * Fraction(1, N)


def test_measured_leptons_sit_at_sqrt2():
    obs = observed_amplitude()
    assert abs(obs["A_obs_minus_sqrt2"]) < 1e-3
    assert np.isclose(obs["K_obs"], 2 / 3, atol=1e-4)


def test_fixed_point_nogo():
    # GRUT impedance balance gives 4/9 (not 2/3); equipartition gives 2/3;
    # Koide amplitude is ~4x the impedance (too large to be a GRUT-impedance effect).
    ng = fixed_point_amplitude_nogo()
    assert np.isclose(ng["K_impedance_balance"], 4 / 9)
    assert not np.isclose(ng["K_impedance_balance"], 2 / 3)
    assert np.isclose(ng["K_equipartition"], 2 / 3)
    assert ng["A_over_alpha"] > 4.0
    assert np.isclose(ng["K_eq_half_n_g_sq"], 2 / 3)  # K = n_g²/2 coincidence
