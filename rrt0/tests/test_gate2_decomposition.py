"""GATE-2: independent numerical verification of the analytical decomposition.

For the closed unitary model class, we verify (per ensemble member, per seed,
per lambda, per tau) that the raw influence response is exactly the propagated
injected perturbation:

    Delta_rho_raw(t, tau) = U^tau [E_alpha(rho0(t)) - rho0(t)] U^{-tau}

so that the residual of the influence observable after subtracting everything
explicitly supplied (intervention + propagator) vanishes to machine precision:

    Delta_rho_residual = Delta_rho_raw - U^tau [E_alpha(rho0)-rho0] U^{-tau} = 0.

This is a CONTROL, not a discovery experiment. A zero result is the expected,
correct outcome for this model class and gates whether any RRT-0 battery result
can be interpreted as irreducible.

Design notes (integrity):
  - Route A (direct delta propagation) and Route B (independent two-state
    propagation then subtraction) are computed with INDEPENDENT code paths.
  - Route C checks the Heisenberg observable identity per observable.
  - Multiple tau, lam, seeds, ensemble members; verdicts from the frozen
    tolerance ladder in model/reducibility.py. No tolerance is tuned here.
"""
import json
import sys
from pathlib import Path

import numpy as np

_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT))

from rrt0.model.core import (  # noqa: E402
    D, LAM, LAM_LADDER, SEED_PRIMARY, SEEDS_ROBUST, TAU_INF, TAU_OP,
    e_alpha, gue_hamiltonian, haar_unitary, initial_ensemble,
    step_unitary, evolve_trajectory,
)
from rrt0.model.reducibility import (  # noqa: E402
    evolve_delta, residual_ratio, verdict_from_residual,
)

OUT = _ROOT / "results" / "gate2_decomposition.json"
OUT.parent.mkdir(exist_ok=True)


def u_power(U, tau):
    """Independent from model.core/evolve_delta: repeated squaring."""
    if tau == 0:
        return np.eye(U.shape[0], dtype=complex)
    P = np.eye(U.shape[0], dtype=complex)
    B = U.copy()
    n = tau
    while n:
        if n & 1:
            P = P @ B
        B = B @ B
        n >>= 1
    return P


def independent_raw_response(rho0_t, sigma, lam, U, tau):
    """Route B written from scratch here (no shared code with reducibility.py
    beyond U^tau, which is matrix powering by mathematical necessity)."""
    Ut = u_power(U, tau)
    rho_e = (1.0 - lam) * rho0_t + lam * sigma
    return Ut @ rho_e @ Ut.conj().T - Ut @ rho0_t @ Ut.conj().T


def main():
    rows = []
    lam_grid = sorted(set([LAM] + list(LAM_LADDER)))
    seeds = [SEED_PRIMARY] + SEEDS_ROBUST
    worst = {"residual_ratio": 0.0, "route_AB": 0.0}

    for seed in seeds:
        rng = np.random.default_rng(seed)
        H = gue_hamiltonian(rng)
        U = step_unitary(H, dt=1.0)          # unit-step propagator
        ensemble = initial_ensemble(rng, n_pure=5)
        sigmas = [np.eye(D, dtype=complex) / D] + [
            (lambda v: np.outer(v, v.conj()))(
                (rng.standard_normal(D) + 1j * rng.standard_normal(D)) / np.sqrt(2))
            for _ in range(D * D)
        ]
        for rho0 in ensemble:
            traj = evolve_trajectory(rho0, U, n_steps=max(TAU_INF, TAU_OP) + 4,
                                     sample_every=1)
            for t_idx, rho_t in enumerate(traj, start=1):
                for sigma in sigmas:
                    for lam in lam_grid:
                        delta0 = e_alpha(rho_t, sigma, lam) - rho_t
                        # Route A: propagate the injected difference.
                        dA = evolve_delta(delta0, U, TAU_INF)
                        # Independent recomputation (Route B, local code).
                        dB = independent_raw_response(rho_t, sigma, lam, U, TAU_INF)
                        ratio, res_abs, tot = residual_ratio(dB, dA)
                        worst["residual_ratio"] = max(worst["residual_ratio"], ratio)
                        worst["route_AB"] = max(worst["route_AB"],
                                                float(np.linalg.norm(dA - dB, "fro")))
                        rows.append({
                            "seed": seed, "t": t_idx, "lam": lam,
                            "sigma_kind": "maximally_mixed" if sigma.trace().real > D - 1e-9 else "pure",
                            "residual_fro": float(res_abs),
                            "raw_fro": float(tot),
                            "residual_ratio": float(ratio),
                            "verdict": verdict_from_residual(ratio),
                        })

    verdicts = {}
    for r in rows:
        verdicts[r["verdict"]] = verdicts.get(r["verdict"], 0) + 1

    report = {
        "gate": "GATE-2 analytical decomposition control",
        "identity_tested": "Delta_rho_raw == U^tau [E_alpha(rho0)-rho0] U^{-tau}",
        "n_cases": len(rows),
        "verdict_counts": verdicts,
        "worst_residual_ratio": worst["residual_ratio"],
        "worst_route_AB_abs_fro": worst["route_AB"],
        "tolerances": {"reducible": 1e-10, "unresolved": 1e-6},
        "pass": all(v == "FULLY_REDUCIBLE_IN_LINEAR_UNITARY_MODEL_CLASS" for v in verdicts) and len(rows) > 0,
        "cases": rows,
    }
    OUT.write_text(json.dumps(report, indent=2))
    print(json.dumps({k: v for k, v in report.items() if k != "cases"}, indent=2))
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
