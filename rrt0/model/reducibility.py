"""RRT-0 reducibility decomposition.

For the registered model class
    finite closed system + linear unitary evolution
    + externally specified linear intervention + fixed operational readout

the intervention response satisfies EXACTLY:

    delta_rho(t)   = E[rho0(t)] - rho0(t)
    Delta_rho_raw  = U^tau delta_rho(t) U^{-tau}

Routes:
    A: propagate delta_rho directly (linear route).
    B: propagate rho0 and rho_E independently, subtract (independent subtraction).
    C: Heisenberg-picture observable response Tr[delta_rho U^{-tau} B U^tau].

No verdict is hard-coded; verdicts are derived from the declared tolerance.
"""

from __future__ import annotations

import numpy as np

EPS = 1e-15
# Declared tolerances (recorded in INPUT_LEDGER; not tuned post hoc):
RESIDUAL_TOLERANCE_REDUCIBLE = 1e-10
RESIDUAL_TOLERANCE_UNRESOLVED = 1e-6


def evolve_delta(delta0: np.ndarray, U: np.ndarray, tau: int) -> np.ndarray:
    """Route A: propagate the injected difference directly."""
    Ut = np.linalg.matrix_power(U, tau)
    return Ut @ delta0 @ Ut.conj().T


def route_a_delta(rho0, sigma, lam, U, tau):
    delta0 = lam * (sigma - rho0)
    return evolve_delta(delta0, U, tau)


def route_b_delta(rho0, sigma, lam, U, tau):
    """Route B: propagate both states independently, then subtract.

    Shares only the matrix_power call with Route A by mathematical necessity;
    the state propagation and subtraction are performed independently.
    """
    Ut = np.linalg.matrix_power(U, tau)
    rho_p = (1.0 - lam) * rho0 + lam * sigma
    return Ut @ rho_p @ Ut.conj().T - Ut @ rho0 @ Ut.conj().T


def route_c_observable_response(delta0, U, tau, B):
    """Route C: Heisenberg-picture response Delta<B> for observable B."""
    Utm = np.linalg.matrix_power(U, tau)
    Ut_min = Utm.conj().T
    return np.trace(delta0 @ (Ut_min @ B @ Utm))


def residual_ratio(delta_raw: np.ndarray, delta_supplied: np.ndarray, tiny: float = EPS):
    residual = np.linalg.norm(delta_raw - delta_supplied, ord="fro")
    total = np.linalg.norm(delta_raw, ord="fro")
    return residual / (total + tiny), residual, total


def explained_fraction(delta_a, delta_b, tiny: float = EPS):
    ratio, residual, total = residual_ratio(delta_a, delta_b, tiny)
    return 1.0 - ratio, ratio, residual, total


def route_agreement(delta_a, delta_b, delta_c_observable=None):
    """Max absolute / relative discrepancy between routes."""
    d_ab = np.linalg.norm(delta_a - delta_b, ord="fro")
    scale = np.linalg.norm(delta_a, ord="fro") + EPS
    out = {
        "abs_discrepancy_AB": float(d_ab),
        "rel_discrepancy_AB": float(d_ab / scale),
    }
    if delta_c_observable is not None:
        out["observable_response_route_c"] = float(np.real(delta_c_observable))
    return out


def verdict_from_residual(ratio: float) -> str:
    """Verdict derived ONLY from the predeclared tolerance ladder."""
    if ratio <= RESIDUAL_TOLERANCE_REDUCIBLE:
        return "FULLY_REDUCIBLE_IN_LINEAR_UNITARY_MODEL_CLASS"
    elif ratio <= RESIDUAL_TOLERANCE_UNRESOLVED:
        return "NUMERICALLY_UNRESOLVED"
    return "RESIDUAL_REQUIRES_AUDIT"
