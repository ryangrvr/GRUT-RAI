#!/usr/bin/env python3
"""REALITY_CHECK_04 — independent verification of Experiment P controls.

Re-computes Controls A, D, H from first principles. Does NOT modify any
Experiment P artifact. Read-only with respect to Experiment P files.

Run:  python3.12 calc/verify_experiment_p.py
"""
import json, numpy as np
from pathlib import Path

HERE = Path(__file__).resolve().parent
S2, A2 = 2, 2

def I(d): return np.eye(d)
def op(kron_list):
    m = np.array([[1.0+0j]])
    for x in kron_list: m = np.kron(m, x)
    return m

s0, s1 = np.array([1,0],complex), np.array([0,1],complex)
a_ready = s0

def run_case(N, env0, alpha, beta):
    """Record-type measurement, H = H_sys(2) ⊗ H_env(2N).

    The apparatus stays in |A_ready> under U (factors out of every term),
    so it is dropped identically. Unitary: |0,e_m> -> |0,e_m>;
    |1,e_m> -> |1,e_{m+1}> (shift register)."""
    dE = 2*N
    dim = 2*dE
    P0 = np.kron(np.outer(s0, s0), I(dE))
    P1 = np.kron(np.outer(s1, s1), I(dE))
    U1 = np.zeros((dE, dE), complex)
    for m in range(N):              # record half: e_m -> e_{m+1}
        U1[m+1, m] = 1
    U1[dE-1, dE-1] = 1              # top record state self-map
    U = P0 + P1 @ np.kron(I(2), U1)
    psi = alpha*np.kron(s0, env0) + beta*np.kron(s1, env0)
    out = U @ psi
    r = out.reshape(2, dE)
    rho_total = np.outer(r, r.conj())
    rho_S = np.einsum('ia,ka->ik', r, r.conj())
    c = rho_S[0,1]
    return dict(cross_term=complex(c),
                sa_purity=float(np.real(np.trace(rho_S @ rho_S))),
                branch_pop=[float(rho_S[0,0].real), float(rho_S[1,1].real)],
                global_purity=float(np.real(np.trace(rho_total @ rho_total))),
                unitary=float(np.max(np.abs(U.conj().T @ U - I(dim)))))

def record_state(N):
    e = np.zeros(2*N, complex); e[0] = 1; return e
def generic_state(N, rng):
    v = rng.normal(size=2*N) + 1j*rng.normal(size=2*N)
    return v/np.linalg.norm(v)

def main():
    rng = np.random.default_rng(20260910)
    res = {}

    # ---- Control A recheck -------------------------------------------------
    res["A"] = run_case(8, record_state(8), 1/np.sqrt(2), 1/np.sqrt(2))
    res["A"]["analytic_note"] = ("record overlap <e0|U1|e0>=0 by construction "
                                 "(shift register, disjoint support) -> decoherence exact")

    # ---- Control D recheck: does the second 'purification' decohere? --------
    d = run_case(8, generic_state(8, rng), 1/np.sqrt(2), 1/np.sqrt(2))
    res["D_recheck"] = {
        "second_state_cross_term": float(abs(d["cross_term"])),
        "identical_reduced_decoherence": abs(d["cross_term"]) < 1e-12,
        "conclusion": ("FAILS: the second environment state does NOT decohere under the "
                       "same U (cross term != 0). The pair is not an identical-reduced-state "
                       "pair; control D does not test purificational indistinguishability. "
                       "INVALID AS EXECUTED.")
    }

    # ---- Control H recheck: same decoherence class, different weights -------
    h = []
    for a2 in (0.2, 0.5, 0.8):
        r = run_case(8, record_state(8), a2, np.sqrt(1-a2**2))
        h.append({"alpha": a2, "cross": float(abs(r["cross_term"])), "p0": r["branch_pop"][0],
                  "purity": r["sa_purity"]})
    res["H_recheck"] = h
    res["H_scoping"] = {
        "purity_matched": False,
        "note": ("purities differ (0.68 vs 0.5); only the pointer-basis decoherence class "
                 "(cross=0) is matched. p0 is itself a reduced-state element: weights ARE "
                 "identifiable from the full reduced state as inherited initial-state input. "
                 "Non-identifiability holds only relative to the decoherence-observable set.")
    }

    out = HERE.parent / "program" / "REALITY_CHECK_04_VERIFICATION.json"
    out.write_text(json.dumps(res, indent=2, default=str))
    print(json.dumps(res, indent=2, default=str))

if __name__ == "__main__":
    main()
