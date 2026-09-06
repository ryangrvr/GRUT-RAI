"""RRT-0 analytic reducibility pre-results gate — run under frozen spec.

ROLE: historical_audit_only — NOT an evidentiary route. The authoritative
pre-results gate is scripts/run_reducibility_gate.py (Routes A/B: matrix_power
and eigh on the Hermitian generator H). The logm(U) route below uses a matrix
logarithm of a unitary, which is branch-prone; it is retained for historical
comparison only and carries no evidentiary status.

Identity tested (closed unitary model, canonical E_alpha):
    Delta_raw       = U^tau E_alpha(rho) U^{-tau} - U^tau rho U^{-tau}
                    = U^tau [E_alpha(rho) - rho] U^{-tau}
    Delta_supplied  = U^tau [E_alpha(rho) - rho] U^{-tau}   (independently constructed)
    Delta_residual  = Delta_raw - Delta_supplied

Numerical test matrix (frozen/test-defined domain):
  seeds:        frozen primary + robustness set
  states:       maximally mixed + Haar-random pure (initial_ensemble)
  alphas:       all D^2-1 support projectors of the Gell-Mann basis (SIGMAS)
  lambda:       frozen lam plus lam_ladder
  tau:          {1, TAU_OP, TAU_INF} (positive integers, within frozen domain)
  readout O:    basis observables (trace/Hermiticity checks on Delta itself)

Route discipline (lesson from the failure analysis recorded in the audit):
  U^tau is built via the HERMITIAN generator H (step_unitary's own route) or
  matrix_power for integer tau. np.linalg.eigh is NEVER applied to U itself
  (non-Hermitian => silent garbage: eigh reads only the lower triangle).

Read-only w.r.t. frozen spec: no ledger/freeze/spec file is modified, no
Phi_raw is altered, no sector-selection firewall, no full battery, nothing
committed.
"""
import numpy as np

from rrt0.model.core import (
    D, DT, LAM, LAM_LADDER, TAU_OP, TAU_INF, SEED_PRIMARY, SEEDS_ROBUST,
    SIGMAS, BASIS, gue_hamiltonian, step_unitary, initial_ensemble, e_alpha,
)

TOL_REPORT = 1e-10        # explicitly reported pass tolerance (Frobenius norm)
TAUS = sorted({1, TAU_OP, TAU_INF})


def u_power(U, H, tau):
    """U^tau by the Hermitian-generator route (exact for integer tau).

    U = V exp(-i w dt) V^dagger with H = V diag(w) V^dagger (Hermitian), so
    U^tau = V exp(-i w tau dt) V^dagger. For integer tau this equals
    matrix_power(U, tau) to machine precision (verified in-test).
    """
    w, v = np.linalg.eigh(H)
    return (v * np.exp(-1j * w * tau * DT)) @ v.conj().T


def delta_raw(rho, sigma, U, tau, lam):
    """Raw response: evolve intervened and unintervened trajectories, differ.
    (Phi_raw is NOT altered here; this is the raw difference of evolutions.)"""
    Ut = np.linalg.matrix_power(U, tau)
    Ut_dag = np.linalg.matrix_power(U.conj().T, tau)
    rho_int = U @ e_alpha(rho, sigma, lam) @ U.conj().T
    for _ in range(tau - 1):
        rho_int = U @ rho_int @ U.conj().T
    rho_base = U @ rho @ U.conj().T
    for _ in range(tau - 1):
        rho_base = U @ rho_base @ U.conj().T
    return rho_int - rho_base


def delta_supplied(rho, sigma, U, tau, lam):
    """INDEPENDENT construction of U^tau [E_alpha(rho) - rho] U^{-tau}.
    Uses the spectral route on the Hermitian generator (different code path
    from delta_raw's iterated/matrix_power route), so agreement is a real
    cross-check, not a copied calculation."""
    Ut = u_power(U, _H_of(U), tau)             # spectral route
    Utm = u_power(U, _H_of(U), -tau)
    return Ut @ (e_alpha(rho, sigma, lam) - rho) @ Utm


def _H_of(U):
    """Recover the Hermitian generator from U via matrix log (audit-only
    helper; the model itself stores H). Uses scipy if available, else the
    principal-branch eigendecomposition of U (angles in (-pi, pi])."""
    import scipy.linalg as sla
    return sla.logm(U) / (-1j * DT)


def run(seed):
    rng = np.random.default_rng(seed)
    H = gue_hamiltonian(rng)
    U = step_unitary(H)
    # route consistency check (spectral vs matrix_power) — recorded, not fixed
    w, v = np.linalg.eigh(H)
    Ut_check = (v * np.exp(-1j * w * TAU_OP * DT)) @ v.conj().T
    route_err = np.linalg.norm(Ut_check - np.linalg.matrix_power(U, TAU_OP))
    rhos = initial_ensemble(rng)
    rows = []
    for lam in [LAM] + LAM_LADDER:
        for tau in TAUS:
            for ai, sigma in enumerate(SIGMAS):
                for si, rho in enumerate(rhos):
                    dr = delta_raw(rho, sigma, U, tau, lam)
                    ds = delta_supplied(rho, sigma, U, tau, lam)
                    res = np.linalg.norm(dr - ds)
                    herm = np.linalg.norm(dr - dr.conj().T)
                    tr = abs(np.trace(dr))
                    rows.append((seed, si, ai, lam, tau, res, herm, tr))
    return rows, route_err


def main():
    all_rows = []
    route_errs = []
    for seed in [SEED_PRIMARY] + SEEDS_ROBUST:
        rows, route_err = run(seed)
        all_rows.extend(rows)
        route_errs.append(route_err)

    residuals = np.array([r[5] for r in all_rows])
    herms = np.array([r[6] for r in all_rows])
    trs = np.array([r[7] for r in all_rows])
    max_res = residuals.max()
    n_tests = len(all_rows)
    passed = max_res < TOL_REPORT and route_errs and max(route_errs) < TOL_REPORT

    print(f"tests            : {n_tests}")
    print(f"max residual     : {max_res:.3e}")
    print(f"median residual  : {np.median(residuals):.3e}")
    print(f"p95 residual     : {np.percentile(residuals, 95):.3e}")
    print(f"max hermiticity  : {herms.max():.3e}")
    print(f"max |trace|      : {trs.max():.3e}")
    print(f"max route err    : {max(route_errs):.3e}")
    print(f"tolerance        : {TOL_REPORT:.1e}")
    print(f"PASS             : {passed}")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
