"""
Module 1: SU(3) Lie algebra — Gell-Mann generators and structure constants.

Status: Implemented and validated.
"""

import numpy as np

# ── Gell-Mann matrices ──────────────────────────────────────
LAMBDA = [
    np.array([[0,1,0],[1,0,0],[0,0,0]], dtype=complex),           # lambda_1
    np.array([[0,-1j,0],[1j,0,0],[0,0,0]], dtype=complex),        # lambda_2
    np.array([[1,0,0],[0,-1,0],[0,0,0]], dtype=complex),           # lambda_3
    np.array([[0,0,1],[0,0,0],[1,0,0]], dtype=complex),           # lambda_4
    np.array([[0,0,-1j],[0,0,0],[1j,0,0]], dtype=complex),        # lambda_5
    np.array([[0,0,0],[0,0,1],[0,1,0]], dtype=complex),           # lambda_6
    np.array([[0,0,0],[0,0,-1j],[0,1j,0]], dtype=complex),        # lambda_7
    np.array([[1,0,0],[0,1,0],[0,0,-2]], dtype=complex)/np.sqrt(3),# lambda_8
]

# SU(3) generators: T^a = lambda^a / 2
T_GEN = [lam / 2 for lam in LAMBDA]
I3 = np.eye(3, dtype=complex)
N_C = 3  # number of colors
N_GEN = 8  # number of generators


def structure_constants() -> np.ndarray:
    """Compute f^{abc} from [T^a, T^b] = i f^{abc} T^c.

    Returns (8, 8, 8) array of structure constants.
    """
    f = np.zeros((N_GEN, N_GEN, N_GEN))
    for a in range(N_GEN):
        for b in range(N_GEN):
            comm = T_GEN[a] @ T_GEN[b] - T_GEN[b] @ T_GEN[a]
            for c in range(N_GEN):
                # f^{abc} = Re(-2i Tr([T^a, T^b] T^c))
                f[a, b, c] = float(np.real(-2j * np.trace(comm @ T_GEN[c])))
    return f


def verify_lie_algebra() -> dict:
    """Verify [T^a, T^b] = i f^{abc} T^c for all a, b."""
    f = structure_constants()
    max_err = 0.0

    for a in range(N_GEN):
        for b in range(N_GEN):
            comm = T_GEN[a] @ T_GEN[b] - T_GEN[b] @ T_GEN[a]
            expected = 1j * sum(f[a, b, c] * T_GEN[c] for c in range(N_GEN))
            err = float(np.max(np.abs(comm - expected)))
            max_err = max(max_err, err)

    return {
        "max_error": max_err,
        "status": "PASS" if max_err < 1e-12 else "FAIL",
    }


def verify_trace_normalization() -> dict:
    """Verify Tr(T^a T^b) = delta^{ab} / 2."""
    max_err = 0.0
    for a in range(N_GEN):
        for b in range(N_GEN):
            tr = np.real(np.trace(T_GEN[a] @ T_GEN[b]))
            expected = 0.5 if a == b else 0.0
            err = abs(tr - expected)
            max_err = max(max_err, err)

    return {
        "max_error": max_err,
        "status": "PASS" if max_err < 1e-14 else "FAIL",
    }


def verify_hermiticity() -> dict:
    """Verify all generators are Hermitian."""
    max_err = 0.0
    for a, T in enumerate(T_GEN):
        err = float(np.max(np.abs(T - T.conj().T)))
        max_err = max(max_err, err)

    return {
        "max_error": max_err,
        "status": "PASS" if max_err < 1e-14 else "FAIL",
    }


def verify_tracelessness() -> dict:
    """Verify all generators are traceless."""
    max_err = 0.0
    for T in T_GEN:
        err = abs(np.trace(T))
        max_err = max(max_err, float(err))

    return {
        "max_error": max_err,
        "status": "PASS" if max_err < 1e-14 else "FAIL",
    }


def casimir_fundamental() -> float:
    """Quadratic Casimir in fundamental rep: C_F = (N^2-1)/(2N) = 4/3."""
    C_F = sum(T @ T for T in T_GEN)
    # Should be C_F * I_3
    c_val = float(np.real(C_F[0, 0]))
    return c_val
