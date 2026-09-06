"""Regression: the covariant mirror M (complex conjugation, RRT0_MIRROR_CONTROL.md)
leaves the registered discovery statistic exactly invariant. Frozen semantics
untouched: this test only READS canonical model functions."""
import numpy as np
from rrt0.model.core import BASIS, SIGMAS, LAM, TAU_OP, gue_hamiltonian, step_unitary, e_alpha
from rrt0.model.reducibility import evolve_delta

def _rows(rho0, U, basis, sigmas, lam, tau):
    nb = len(basis)
    X = np.zeros((nb, nb))
    for a in range(nb):
        d0 = e_alpha(rho0, sigmas[a], lam) - rho0
        dt = evolve_delta(d0, U, tau)
        for b in range(nb):
            X[a, b] = abs(float(np.real(np.trace(dt @ basis[b]))))
    return X

def test_mirror_invariance_exact():
    rng = np.random.default_rng(1)
    H = gue_hamiltonian(rng)
    U = step_unitary(H)
    v = (rng.standard_normal(4) + 1j * rng.standard_normal(4)) / np.sqrt(2)
    v /= np.linalg.norm(v)
    rho0 = np.outer(v, v.conj())
    X = _rows(rho0, U, BASIS, SIGMAS, LAM, TAU_OP)
    Xm = _rows(np.conj(rho0), np.conj(U), [np.conj(B) for B in BASIS],
               [np.conj(S) for S in SIGMAS], LAM, TAU_OP)
    assert np.max(np.abs(X - Xm)) == 0.0  # exact: IEEE conj is exact, statistic conj-invariant

def test_mirror_reverses_orientation_representation():
    # U* = exp(+i dt H*): the mirror genuinely reverses the propagator's orientation
    rng = np.random.default_rng(1)
    H = gue_hamiltonian(rng)
    U = step_unitary(H)
    assert not np.allclose(np.conj(U), U)          # a real change of representation...
    assert np.allclose(np.conj(U) @ np.conj(U).conj().T, np.eye(4))  # ...still unitary
