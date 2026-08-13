#!/usr/bin/env python3
"""KMS / fluctuation-dissipation admission gate (rung 2).

The hard gate, as a function, not a slogan: no kernel enters the GRUT foundation
until it satisfies detailed balance. For a bosonic bath the quantum FDT (Kubo 1966;
Callen-Welton 1951) in Keldysh components is

    G_K(omega) = coth(hbar*omega / 2 k_B T) * ( G_R(omega) - G_A(omega) )

with G_A(omega) = conj(G_R(omega)). Equivalently the symmetrized noise spectrum is
    S(omega) = hbar * coth(hbar*omega / 2kT) * Im[chi(omega)].

A candidate (chi=G_R, noise G_K) pair PASSES iff the max relative residual over the
frequency grid is below tolerance. White-noise / temperature-independent kernels FAIL.

Units: hbar = k_B = 1. Pure stdlib.
"""
import cmath
import math


def coth(x):
    if x == 0:
        return math.inf
    ax = abs(x)
    if ax > 20:              # tanh ~ 1, avoid overflow
        return math.copysign(1.0, x)
    if ax < 1e-8:            # coth(x) ~ 1/x + x/3
        return 1.0 / x
    return 1.0 / math.tanh(x)


def gate(omega_grid, G_R, G_K, T, tol=1e-6):
    """Admit or reject a kernel.

    omega_grid : list of angular frequencies (must avoid omega=0)
    G_R        : list of complex retarded Green functions chi(omega)
    G_K        : list of complex Keldysh (noise) components
    T          : temperature (T>0). T<=0 is rejected: KMS undefined.
    Returns dict {passed, max_residual, reason, worst_omega}.
    """
    if T <= 0:
        return {"passed": False, "max_residual": math.inf,
                "reason": "T<=0: KMS/detailed-balance undefined", "worst_omega": None}
    if not (len(omega_grid) == len(G_R) == len(G_K)):
        raise ValueError("omega_grid, G_R, G_K must be same length")

    max_res = 0.0
    worst = None
    for w, gr, gk in zip(omega_grid, G_R, G_K):
        if w == 0:
            continue
        ga = gr.conjugate()
        predicted = coth(w / (2.0 * T)) * (gr - ga)   # = coth * 2i*Im[chi]
        denom = abs(gk) if abs(gk) > 1e-30 else 1e-30
        res = abs(gk - predicted) / denom
        if res > max_res:
            max_res = res
            worst = w
    passed = max_res <= tol
    reason = ("detailed balance holds within tol"
              if passed else
              f"FDT/KMS residual {max_res:.3e} > tol {tol:.1e} at omega={worst}")
    return {"passed": passed, "max_residual": max_res, "reason": reason, "worst_omega": worst}


def _self_test():
    # super-Ohmic-ish susceptibility chi(omega) with a Lorentzian-style response.
    grid = [10 ** (-3 + 6 * i / 400) for i in range(401)]   # 1e-3 .. 1e3 log grid
    T = 2.0
    chi = []
    for w in grid:
        im = (w ** 3) / (1.0 + (w / 5.0) ** 2) ** 2          # Im[chi], some loss profile
        re = 1.0 / (1.0 + (w / 5.0) ** 2)                    # a storage profile
        chi.append(complex(re, im))
    # (A) the THERMAL kernel built to satisfy FDT -> must PASS
    G_K_thermal = [coth(w / (2 * T)) * (c - c.conjugate()) for w, c in zip(grid, chi)]
    rA = gate(grid, chi, G_K_thermal, T)
    # (B) a WHITE-noise kernel (constant, T-independent) -> must FAIL
    G_K_white = [complex(0.0, 2.0) for _ in grid]
    rB = gate(grid, chi, G_K_white, T)

    print("KMS GATE SELF-TEST (hbar=kB=1, T=%.1f)" % T)
    print("  (A) FDT-consistent thermal kernel : %s  (residual %.2e)  -- expect PASS"
          % ("PASS" if rA["passed"] else "FAIL", rA["max_residual"]))
    print("  (B) white-noise kernel            : %s  (residual %.2e)  -- expect FAIL"
          % ("PASS" if rB["passed"] else "FAIL", rB["max_residual"]))
    ok = rA["passed"] and not rB["passed"]
    print("  gate working as intended:", ok)
    return 0 if ok else 1


if __name__ == "__main__":
    import sys
    sys.exit(_self_test())
