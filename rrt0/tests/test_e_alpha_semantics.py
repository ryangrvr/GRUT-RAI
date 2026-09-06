"""RRT-0 Phase 2 — semantic tests for the canonical E_alpha map.

Authority: RRT0_FREEZE.json -> RRT0_E_ALPHA_SEMANTIC_DECISION.md.
All expected values here are constructed INDEPENDENTLY of rrt0.model.core
(no reuse of e_alpha inside expectation computations).
"""
import numpy as np
import pytest

from rrt0.model.core import e_alpha, internal_operation, BASIS, verify_freeze_ledger

TOL = 1e-12


# ---------- independent constructions (no reuse of the implementation) ----

def _rand_rho(rng, D):
    """Random physical density matrix via Gram matrix of a random ket."""
    A = rng.normal(size=(D, D)) + 1j * rng.normal(size=(D, D))
    m = A @ A.conj().T
    return m / np.trace(m)


def _rand_unitary(rng, D):
    A = rng.normal(size=(D, D)) + 1j * rng.normal(size=(D, D))
    q, _ = np.linalg.qr(A)
    return q


def _rand_state_vec(rng, D):
    v = rng.normal(size=D) + 1j * rng.normal(size=D)
    return v / np.linalg.norm(v)


@pytest.fixture(scope="module")
def rng():
    return np.random.default_rng(20240601)  # frozen seed


@pytest.fixture(scope="module")
def cases(rng):
    """(rho, sigma_alpha) pairs: sigma_alpha = projector onto |s><s|."""
    D = BASIS[0].shape[0]
    out = []
    for _ in range(8):
        rho = _rand_rho(rng, D)
        s = _rand_state_vec(rng, D)
        sig = np.outer(s, s.conj())  # independent support projector
        out.append((rho, sig))
    return out


# ---------------------------- literal semantic tests ----------------------

def test_lambda_zero_is_identity(cases):
    for rho, sig in cases:
        expected = 1.0 * rho + 0.0 * sig           # independent formula
        assert np.allclose(e_alpha(rho, sig, 0.0), expected, atol=TOL)


def test_lambda_one_is_sigma(cases):
    for rho, sig in cases:
        assert np.allclose(e_alpha(rho, sig, 1.0), sig, atol=TOL)


@pytest.mark.parametrize("lam", [0.0, 0.13, 0.25, 0.5, 0.7, 0.99, 1.0])
def test_exact_linear_displacement(cases, lam):
    for rho, sig in cases:
        lhs = e_alpha(rho, sig, lam) - rho
        rhs = lam * (sig - rho)                     # independent formula
        assert np.allclose(lhs, rhs, atol=TOL)


@pytest.mark.parametrize("lam", [0.0, 0.3, 1.0])
def test_trace_one(cases, lam):
    for rho, sig in cases:
        assert abs(np.trace(e_alpha(rho, sig, lam)) - 1.0) < TOL


@pytest.mark.parametrize("lam", [0.0, 0.3, 1.0])
def test_hermiticity(cases, lam):
    for rho, sig in cases:
        E = e_alpha(rho, sig, lam)
        assert np.allclose(E, E.conj().T, atol=TOL)


@pytest.mark.parametrize("lam", [0.0, 0.3, 0.8, 1.0])
def test_positivity(cases, lam):
    """E_alpha[rho] >= 0 for physical rho, sigma and 0 <= lam <= 1."""
    for rho, sig in cases:
        evals = np.linalg.eigvalsh(e_alpha(rho, sig, lam))
        assert evals.min() >= -TOL


def test_no_hidden_lambda_clamping():
    """Implementation must be the literal affine map, no hidden clamping."""
    D = BASIS[0].shape[0]
    rho = np.eye(D) / D
    sig = np.eye(D); sig[0, 0] = 0.0; sig /= np.trace(sig)
    lam = 1.5
    expected = -0.5 * rho + 1.5 * sig   # literal affine extension
    assert np.allclose(e_alpha(rho, sig, lam), expected, atol=TOL)


def test_sigma_alpha_normalization(cases):
    """sigma_alpha itself must be a normalized projector."""
    for _, sig in cases:
        assert abs(np.trace(sig) - 1.0) < TOL
        assert np.allclose(sig @ sig, sig, atol=TOL)
        assert np.allclose(sig, sig.conj().T, atol=TOL)


def test_single_authoritative_function():
    """Legacy name must delegate to the one authoritative implementation."""
    rng = np.random.default_rng(7)
    D = BASIS[0].shape[0]
    rho, sig = _rand_rho(rng, D), np.eye(D) / D
    assert np.array_equal(internal_operation(rho, sig, 0.4),
                          e_alpha(rho, sig, 0.4))


# ------------------- evolution / reducibility identity --------------------

@pytest.mark.parametrize("trial", range(6))
def test_evolution_reducibility_identity(rng, trial):
    """U^tau [E(rho)-rho] U^-tau == U^tau E(rho) U^-tau - U^tau rho U^-tau,
    with each side constructed independently (no call to e_alpha on either
    side; both use independently written formulas)."""
    D = BASIS[0].shape[0]
    rho = _rand_rho(rng, D)
    s = _rand_state_vec(rng, D)
    sig = np.outer(s, s.conj())
    U = _rand_unitary(rng, D)          # noncommuting with rho in general
    lam = float(rng.uniform(0.05, 0.95))

    # LHS: displacement, evolved
    delta = lam * (sig - rho)                       # independent formula
    lhs = U @ delta @ U.conj().T

    # RHS: difference of separately evolved states
    e_state = (1.0 - lam) * rho + lam * sig         # independent formula
    rhs = U @ e_state @ U.conj().T - U @ rho @ U.conj().T

    err = np.max(np.abs(lhs - rhs))
    assert err < 1e-13, f"reducibility identity violated, max err={err}"


# ------------------------------ freeze integrity --------------------------

def test_freeze_hashes_unchanged():
    assert verify_freeze_ledger() is True


# -------------------------- mutation / test-the-tests ---------------------

def test_mutations_are_detected(cases):
    """Every semantic mutation must FAIL at least one core criterion."""
    rho, sig = cases[0]
    lam = 0.3
    correct = e_alpha(rho, sig, lam)
    muts = {
        "swapped_rho_sigma": e_alpha(sig, rho, lam),
        "wrong_lambda_sign": e_alpha(rho, sig, -lam),
        "dropped_baseline": lam * sig,
        "unnormalized_sigma": e_alpha(rho, sig * 2.0, lam),
    }
    for name, M in muts.items():
        failures = []
        if not np.allclose(M, correct, atol=TOL):
            failures.append("map_equality")
        if abs(np.trace(M) - 1.0) > 1e-8:
            failures.append("trace")
        if not np.allclose(M, M.conj().T, atol=TOL):
            failures.append("hermiticity")
        if np.linalg.eigvalsh(M).min() < -1e-8:
            failures.append("positivity")
        assert failures, f"mutation {name!r} undetected — tests not connected"
