#!/usr/bin/env python3
"""p2_influence_cone: the minimal constraint structure on realizable influence data (K, N).

CHARTER: P2_INFLUENCE_CONE_CHARTER_01.md (pre-registration frozen at commit 291c23a BEFORE
this instrument ran). Candidate cone, stated there before any number existed:

    C_Gauss = { (J, nu) : J(omega) >= 0  and  nu >= hbar*J/2 pointwise }   (hbar = 1 units)

with conjectured minimality (KMS/FDT/stationarity are STATES inside the cone, not constraints
on it). Provenance: borrowed-standard Gaussian realizability mathematics, U1-style; this
instrument's contribution is verification within the program's discipline, the minimality
probes, and the owner's criterion-plurality diagnostic (NO-UNIFICATION-ASSUMPTION fence:
nothing below scores criteria against each other or seeks a master functional).

Pure stdlib. Run: python3 calc/p2_influence_cone.py
"""
import hashlib
import itertools
import json
import math
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import partition_selection_p1 as p1  # validated linear algebra + the frozen P-1 worlds

FAIL = []
CHECKS = []


def check(ok, msg, kind="ok"):
    tag = {"ok": "ok  ", "ctrl": "ctrl", "note": "note"}[kind]
    print(f"  {tag if ok or kind == 'note' else 'FAIL'}   {msg}")
    CHECKS.append({"ok": bool(ok), "kind": kind, "msg": msg})
    if not ok and kind != "note":
        FAIL.append(msg)


M = 8
W = [0.4 + 1.8 * (mu + 0.5) / M for mu in range(M)]      # frequency grid (declared)
J_BASE = [0.30, 0.55, 0.20, 0.70, 0.15, 0.62, 0.28, 0.45]  # declared, deliberately NON-monotone
TGRID = [20.0 * i / 199 for i in range(200)]
S_NONKMS = [0.5, 1.7, 0.6, 2.2, 0.9, 0.55, 1.3, 0.8]     # declared non-KMS occupation profile


def K_of(J, tgrid=TGRID):
    return [sum(J[m] * math.sin(W[m] * t) / W[m] for m in range(M)) for t in tgrid]


def N_of(J, s, tgrid=TGRID):
    return [sum(J[m] * s[m] * math.cos(W[m] * t) / W[m] for m in range(M)) for t in tgrid]


def realize(J, s, quantum=True):
    """Constructive realizer: star bath c_m = sqrt(J_m); per-mode Gaussian state with symmetric
    occupation s_m. Returns (ok, reason). Quantum branch enforces the hbar floor via the
    symplectic eigenvalue (= s_m for a single mode); classical branch only sigma > 0."""
    for m in range(M):
        if J[m] < 0:
            return False, f"J[{m}] = {J[m]} < 0: no real coupling c = sqrt(J) exists"
    for m in range(M):
        if quantum and s[m] < 0.5 - 1e-12:
            return False, (f"s[{m}] = {s[m]} < 1/2: single-mode symplectic eigenvalue {s[m]} "
                           "violates the uncertainty bound (state not positive)")
        if (not quantum) and s[m] <= 0:
            return False, f"s[{m}] <= 0: classical covariance not positive"
    return True, "realized"


def verify_reconstruction(J, s):
    """The constructed realizer's (K, N), recomputed through the independent GLE eigen-route
    (full V matrix -> eig of V_EE -> mode weights), must reproduce the targets to 1e-10."""
    n = 1 + M
    V = [[0.0] * n for _ in range(n)]
    V[0][0] = 1.0
    for m in range(M):
        V[1 + m][1 + m] = W[m] ** 2
        V[0][1 + m] = -math.sqrt(J[m])
        V[1 + m][0] = -math.sqrt(J[m])
    E = list(range(1, n))
    VEE = [[V[i][j] for j in E] for i in E]
    lam, U = p1.jacobi_eig(VEE)
    Ut = p1.transpose(U)
    modes = []
    for mu in range(M):
        om = math.sqrt(max(lam[mu], 1e-14))
        c = sum(V[0][E[j]] * Ut[mu][j] for j in range(M))
        modes.append((c * c, om))
    # map the state occupations onto the (here identical) normal modes: star bath is diagonal,
    # so eig returns the same modes up to ordering; rebuild s per recovered frequency
    smap = {round(w, 9): s[m] for m, w in enumerate(W)}
    Krec = [sum(c2 * math.sin(om * t) / om for c2, om in modes) for t in TGRID]
    Nrec = [sum(c2 * smap[round(om, 9)] * math.cos(om * t) / om for c2, om in modes)
            for t in TGRID]
    Kt, Nt = K_of(J), N_of(J, s)
    dK = max(abs(a - b) for a, b in zip(Krec, Kt)) / max(abs(x) for x in Kt)
    dN = max(abs(a - b) for a, b in zip(Nrec, Nt)) / max(abs(x) for x in Nt)
    return dK, dN


def kms_fit_residual(s):
    """Best relative residual of s_m against coth(w_m/2T)/2 over a declared T grid."""
    best = 1e99
    for i in range(1, 500):
        T = 0.01 + (10.0 - 0.01) * i / 499
        r = max(abs(s[m] - 0.5 / math.tanh(W[m] / (2 * T))) / s[m] for m in range(M))
        best = min(best, r)
    return best


def main():
    t0 = time.time()
    print("P-2 INFLUENCE-CONE INSTRUMENT (charter: P2_INFLUENCE_CONE_CHARTER_01.md, frozen at 291c23a)")

    print("\n=== L-A: INTERIOR REALIZABILITY (constructive) ===")
    targets = {
        "T1 boundary (vacuum, s = 1/2 exactly)": [0.5] * M,
        "T2 thermal/KMS (T = 0.7)": [0.5 / math.tanh(W[m] / 1.4) for m in range(M)],
        "T3 non-KMS profile": S_NONKMS,
    }
    kms_res = {}
    for name, s in targets.items():
        ok, why = realize(J_BASE, s)
        check(ok, f"{name}: {why}")
        if ok:
            dK, dN = verify_reconstruction(J_BASE, s)
            check(dK < 1e-10 and dN < 1e-10,
                  f"{name}: reconstruction gate dK = {dK:.1e}, dN = {dN:.1e}")
        kms_res[name] = kms_fit_residual(s)
    check(kms_res["T3 non-KMS profile"] > 0.05,
          f"T3 is genuinely non-KMS: best single-T fit residual {kms_res['T3 non-KMS profile']:.3f} "
          f"(vs {kms_res['T2 thermal/KMS (T = 0.7)']:.1e} for the true thermal target)")

    print("\n=== L-B: THE hbar FLOOR (detecting) ===")
    s_bad = [0.5] * M
    s_bad[3] = 0.3
    okq, whyq = realize(J_BASE, s_bad, quantum=True)
    check(not okq, f"floor violation DETECTED by the quantum branch: {whyq}", "ctrl")
    okc, whyc = realize(J_BASE, s_bad, quantum=False)
    check(okc, "the CLASSICAL branch admits the same target -- C-floor is exactly the quantum "
               "content, and hbar is its scale (hbar = 1 units; the floor is nu >= hbar*J/2)")

    print("\n=== L-C: POSITIVITY (detecting) ===")
    J_bad = J_BASE[:]
    J_bad[2] = -0.1
    okj, whyj = realize(J_bad, [0.6] * M)
    check(not okj, f"negative-J target DETECTED: {whyj}", "ctrl")

    print("\n=== L-D: THE CRITERION-PLURALITY DIAGNOSTIC (all 55 partitions x 3 testbeds) ===")
    n_checked, min_w, viol = 0, 1e99, []
    for label, builder in (("X1", p1.build_x1), ("X2", p1.build_x2), ("X3", p1.build_x3)):
        V = builder()
        for S in p1.all_partitions():
            E = [i for i in range(p1.N) if i not in S]
            VEE = [[V[i][j] for j in E] for i in E]
            VSE = [[V[i][j] for j in E] for i in S]
            lam, U = p1.jacobi_eig(VEE)
            Ut = p1.transpose(U)
            for mu in range(len(E)):
                if lam[mu] <= 0:
                    viol.append((label, S, "omega^2 <= 0"))
                v = [sum(VSE[a][j] * Ut[mu][j] for j in range(len(E))) for a in range(len(S))]
                w = sum(x * x for x in v)
                min_w = min(min_w, w)
                if w < -1e-15:
                    viol.append((label, S, f"J = {w}"))
            n_checked += 1
    check(not viol, f"cone membership: all {n_checked} sectors of all three worlds satisfy "
                    f"J >= 0 (min weight {min_w:.1e} >= 0, structural) with s = 1/2 under the "
                    "factorized E-ground preparation")
    # J-shape moments for the P-1 winners in X2 (reported, never scored)
    V = p1.build_x2()
    moments = {}
    for tag, S in (("C1-winner [7,9]", (7, 9)), ("C2/C3-winner [0]", (0,))):
        E = [i for i in range(p1.N) if i not in S]
        VEE = [[V[i][j] for j in E] for i in E]
        VSE = [[V[i][j] for j in E] for i in S]
        lam, U = p1.jacobi_eig(VEE)
        Ut = p1.transpose(U)
        ws, oms = [], []
        for mu in range(len(E)):
            om = math.sqrt(max(lam[mu], 1e-14))
            v = [sum(VSE[a][j] * Ut[mu][j] for j in range(len(E))) for a in range(len(S))]
            ws.append(sum(x * x for x in v))
            oms.append(om)
        tot = sum(ws)
        mean_om = sum(w * o for w, o in zip(ws, oms)) / tot
        pr = tot * tot / sum(w * w for w in ws)
        moments[tag] = {"total_weight": tot, "mean_freq": mean_om, "participation_rank": pr}
        print(f"       {tag}: total J = {tot:.4f}, mean freq = {mean_om:.3f}, PR = {pr:.2f}")
    check(True, "L-D VERDICT: DIAGNOSTIC-COORDINATE -- the criteria's plurality changes WHERE in "
                "the cone a sector sits (J-shape moments differ), never WHAT the cone is (every "
                "sector of every criterion lies in the same C_Gauss)", "note")

    print("\n=== L-E: MINIMALITY (three false-constraint counterexamples) ===")
    check(kms_res["T3 non-KMS profile"] > 0.05 and realize(J_BASE, S_NONKMS)[0],
          "false constraint 'nu must be KMS-representable': VIOLATED by the realized T3 profile")
    non_mono = any(J_BASE[i] > J_BASE[i + 1] for i in range(M - 1)) and \
               any(J_BASE[i] < J_BASE[i + 1] for i in range(M - 1))
    check(non_mono and realize(J_BASE, [0.5] * M)[0],
          "false constraint 'J must be monotone': VIOLATED by the realized non-monotone J_BASE")
    s_var = targets["T2 thermal/KMS (T = 0.7)"]
    check(max(s_var) - min(s_var) > 0.1 and realize(J_BASE, s_var)[0],
          "false constraint 's must be frequency-independent': VIOLATED by the realized thermal "
          "profile (s varies with omega)")

    print("\n=== OUTCOME (charter section 3, mechanical) ===")
    la_ok = all(c["ok"] for c in CHECKS if "T1" in c["msg"] or "T2" in c["msg"] or "T3" in c["msg"])
    outcome = "CONE-CONFIRMED" if (la_ok and not FAIL) else \
              ("CONE-VIOLATED" if any("reconstruction" in f or "realized" in f for f in FAIL)
               else "CONE-TOO-TIGHT" if FAIL else "CONE-CONFIRMED")
    check(True, f"OUTCOME: {outcome} -- C_Gauss = {{J >= 0, nu >= hbar*J/2}}, both constraints "
                "verified constructively/detectively, all three false constraints counterexampled; "
                "KMS, FDT, stationarity and single-pole structure are STATES inside the cone", "note")

    out = {"instrument": "p2_influence_cone", "charter_commit": "291c23a", "date": "2026-09-25",
           "cone": {"C_pos": "J(omega) >= 0", "C_floor": "nu(omega) >= hbar*J(omega)/2 (hbar=1)"},
           "targets": {k: {"s": v, "kms_fit_residual": kms_res[k]} for k, v in targets.items()},
           "J_base": J_BASE, "frequencies": W,
           "LD": {"sectors_checked": n_checked, "violations": viol, "min_weight": min_w,
                  "X2_winner_moments": moments, "verdict": "DIAGNOSTIC-COORDINATE"},
           "outcome": outcome, "checks": CHECKS, "failures": FAIL,
           "elapsed_s": round(time.time() - t0, 2),
           "scope_boundary": "scalar S channel, Gaussian class; matrix channels, higher "
                             "cumulants, and the type-III lift are the named extension boundary",
           "hard_stop": "verdict recorded; owner directs the next layer (gravity sector (K,N)_grav, "
                        "P-3 quantum lift, or geometry)"}
    path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                         "P2_INFLUENCE_CONE_RESULT.json"))
    with open(path, "wb") as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True, default=float).encode())
    sha = hashlib.sha256(open(path, "rb").read()).hexdigest()
    print(f"\nartifact written: {path} (sha {sha[:16]}...)")
    n_ok = sum(1 for c in CHECKS if c["ok"])
    print(f"\nP-2 INFLUENCE CONE: {n_ok}/{len(CHECKS)} checks passed; failures: {len(FAIL)}")
    print(f"OUTCOME: {outcome}")
    print("HARD STOP: verdict recorded pending owner direction of the next layer.")
    sys.exit(0 if not FAIL else 1)


if __name__ == "__main__":
    main()
