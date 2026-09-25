#!/usr/bin/env python3
"""p6_seed_selection: is the access seed dynamically selectable?

CHARTER: P6_SEED_SELECTION_CHARTER_01.md (pre-registration frozen at commit 179c108 BEFORE
this instrument ran; authority GitHub Issue #2 owner comment 5827344342). Candidate selector
under attack: minimality/dynamical closure. Binding: "minimal given a chosen interface" is
not "uniquely selected by the dynamics"; entropy/complexity/least-action/simplicity are
prohibited as selectors here; no proof-of-QM; hbar located-not-generated.

Legs: L-S positive control (reducible dynamics selects its blocks -- and only that) | L-A
interface-relativity of minimality | L-B/E causal+conservation pair, seeds sz1 vs sz3 on a
chain, closure equality vs coupled-physics difference | L-C symmetry-degenerate orbit +
broken companion | L-D1 order-relative predictive sufficiency (P-4 order-6 pair consumed at
seed level) | L-D2 explicit path dependence (backward elimination, two orders) | L-F
representation control (entangling refactorization; closure covariance).

Pure stdlib. Run: python3 calc/p6_seed_selection.py
"""
import hashlib
import json
import math
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from p3_nc_lift import cmul, cdag
from p5_access import (pauli, madd, mdiff, expm, mvec, vdot, hs_flat,
                       coherence, cdiff, NT)
from p4_hierarchy import yB_3spin, moments, corr2, coherence_delta

FAIL = []
CHECKS = []
HALT = []


def check(ok, msg, kind="ok"):
    tag = {"ok": "ok  ", "ctrl": "ctrl", "note": "note"}[kind]
    print(f"  {tag if ok or kind == 'note' else 'FAIL'}   {msg}")
    CHECKS.append({"ok": bool(ok), "kind": kind, "msg": msg})
    if not ok and kind != "note":
        FAIL.append(msg)


def halt_check(ok, msg):
    check(ok, msg, "ctrl")
    if not ok:
        HALT.append(msg)


# ---------------- span machinery --------------------------------------------------------------
def gs_add(basis, vec, tol=1e-8):
    """Gram-Schmidt add of a flattened vector; returns True if it grew the span."""
    v = list(vec)
    for b in basis:
        c = sum(x.conjugate() * y for x, y in zip(b, v))
        v = [y - c * x for x, y in zip(b, v)]
    nrm = math.sqrt(sum(abs(x) ** 2 for x in v))
    if nrm > tol:
        basis.append([x / nrm for x in v])
        return True
    return False


def residual(basis, vec):
    """Norm of the component of vec outside span(basis), for a normalized vec."""
    v = list(vec)
    for b in basis:
        c = sum(x.conjugate() * y for x, y in zip(b, v))
        v = [y - c * x for x, y in zip(b, v)]
    return math.sqrt(sum(abs(x) ** 2 for x in v))


def normed(M):
    v = hs_flat(M)
    n = math.sqrt(sum(abs(x) ** 2 for x in v))
    return [x / n for x in v]


def try_add(basis, M):
    """Normalize M (HS) before GS so the 1e-8 tolerance is RELATIVE; zero-guard.
    (Defect fix, disclosed: the first run fed raw product matrices, whose norms grow
    exponentially across sweeps, to an absolute tolerance -- spuriously inflating spans
    to dim 96 in a 64-dim space, a numerical impossibility that proved the bug.)"""
    v = hs_flat(M)
    n = math.sqrt(sum(abs(x) ** 2 for x in v))
    if n < 1e-12:
        return False
    return gs_add(basis, [x / n for x in v])


def span_gap(bA, bB):
    """Two-sided subspace distance: max residual of either basis against the other span."""
    g = 0.0
    for v in bA:
        g = max(g, residual(bB, v))
    for v in bB:
        g = max(g, residual(bA, v))
    return g


def comm(H, X):
    return [[sum(H[i][k] * X[k][j] - X[i][k] * H[k][j] for k in range(len(H)))
             for j in range(len(H))] for i in range(len(H))]


def closure(seeds, H, adh=True, max_sweeps=12):
    """Dynamical closure: unital product-closed span of seeds, ad_H-closed when adh.
    Returns (basis, mats, dim, stable). Stability = one extra sweep does not grow it."""
    d = len(H)
    I = [[(1.0 + 0j) if i == j else 0j for j in range(d)] for i in range(d)]
    basis, mats = [], []

    def add(M):
        if try_add(basis, M):
            v = hs_flat(M)
            n = math.sqrt(sum(abs(x) ** 2 for x in v))
            mats.append([[M[i][j] / n for j in range(d)] for i in range(d)])
            return True
        return False

    add(I)
    for S in seeds:
        add(S)

    def sweep():
        grew = False
        cur = list(mats)
        if adh:
            for X in cur:
                if add(comm(H, X)):
                    grew = True
        cur = list(mats)
        for A in cur:
            for B in cur:
                if add(cmul(A, B)):
                    grew = True
        return grew

    for _ in range(max_sweeps):
        if not sweep():
            break
    dim = len(basis)
    stable = not sweep()
    return basis, mats, dim, stable


def conj(V, M):
    return cmul(V, cmul(M, cdag(V)))


# ---------------- L-S: positive control -- where the selector DOES work -----------------------
def leg_S():
    print("\n=== L-S: POSITIVE CONTROL (reducible dynamics selects its blocks) ===")
    H = madd((0.5, pauli(3, 0, "z")),
             (0.8, cmul(pauli(3, 1, "x"), pauli(3, 2, "x"))), (0.3, pauli(3, 1, "z")))
    basis, _, dim, st = closure([pauli(3, 0, "x")], H)
    check(dim == 4 and st, f"L-S GATE: cl({{I, sx1}}; H_S) dim = {dim} (expected 4: exactly "
                           f"the decoupled site-1 algebra), stable = {st}")
    rz2 = residual(basis, normed(pauli(3, 1, "z")))
    rxx = residual(basis, normed(cmul(pauli(3, 1, "x"), pauli(3, 2, "x"))))
    check(min(rz2, rxx) > 1 - 1e-9,
          f"L-S GATE: zero overlap with the hidden sector -- residuals of sz2, sx2sx3 "
          f"against the closure: {rz2:.6f}, {rxx:.6f} (both = 1 to 1e-9)")
    check(True, "L-S reading (frozen): dynamics DOES select access exactly up to its own "
                "dynamically closed (block/central) decomposition -- SELECTED-IN-CLASS for "
                "reducible dynamics; central decomposition is standard structure, so "
                "NULL-REDUNDANT as a new principle", "note")
    return dim


# ---------------- L-A: minimality is interface-relative ---------------------------------------
H_A = None  # set in leg_A, reused by L-D2


def leg_A():
    print("\n=== L-A: MINIMALITY ATTACK (interface-relativity) ===")
    global H_A
    H_A = madd((0.9, pauli(2, 0, "z")), (1.1, pauli(2, 1, "z")),
               (0.7, cmul(pauli(2, 0, "x"), pauli(2, 1, "x"))))
    bZ, _, dZ, sZ = closure([pauli(2, 0, "z")], H_A)
    bX, _, dX, sX = closure([pauli(2, 0, "x")], H_A)
    check(dZ == 8 and sZ, f"L-A GATE: cl({{I, sz1}}; H_A) dim = {dZ} (expected 8: the parity "
                          f"commutant), stable = {sZ}")
    check(dX == 16 and sX, f"L-A GATE: cl({{I, sx1}}; H_A) dim = {dX} (expected 16: full), "
                           f"stable = {sX}")
    check(dZ != dX, f"L-A GATE: the two minimal algebras DIFFER ({dZ} vs {dX}) -- same "
                    f"dynamics, different declared interfaces, different 'minimal' access")
    check(True, "L-A consequence (frozen): minimality is INTERFACE-RELATIVE -- 'the smallest "
                "dynamically closed algebra preserving the interface' changes with the "
                "interface; no unique dynamics-selected seed", "note")
    return dZ, dX


# ---------------- L-B/E: causal + conservation attack + counterexample ------------------------
def leg_BE():
    print("\n=== L-B/E: CAUSAL ATTACK + COUNTEREXAMPLE (chain ends sz1 vs sz3) ===")
    H = madd((0.9, pauli(3, 0, "z")), (1.1, pauli(3, 1, "z")), (1.3, pauli(3, 2, "z")),
             (0.7, cmul(pauli(3, 0, "x"), pauli(3, 1, "x"))),
             (0.6, cmul(pauli(3, 1, "x"), pauli(3, 2, "x"))))
    P = cmul(pauli(3, 0, "z"), cmul(pauli(3, 1, "z"), pauli(3, 2, "z")))
    halt_check(mdiff(cmul(H, P), cmul(P, H)) < 1e-12,
               "L-B conservation law verified: [H_B, P] = 0 with P = sz1 sz2 sz3 (both seeds "
               "share it; identical causal graph 1-2-3 by construction)")
    bL, _, dL, sL = closure([pauli(3, 0, "z")], H)
    bR, _, dR, sR = closure([pauli(3, 2, "z")], H)
    check(dL <= 32 and dR <= 32 and sL and sR,
          f"L-B GATE (analytic parity bound): both closures inside the 32-dim parity "
          f"commutant -- dims {dL}, {dR}, stable = {sL}/{sR}")
    gap = span_gap(bL, bR)
    equal = gap < 1e-8
    check(True, f"L-B measured branch: closures {'EQUAL' if equal else 'UNEQUAL'} as "
                f"subspaces (two-sided span gap = {gap:.2e}, dims {dL}/{dR})", "note")

    psi0 = [0j] * 8
    psi0[7] = 1.0 + 0j
    BL = madd((0.5, pauli(3, 0, "z")))
    BR = madd((0.5, pauli(3, 2, "z")))
    CL, _ = coherence(H, BL, psi0)
    CR, _ = coherence(H, BR, psi0)
    CL2, _ = coherence(H, BL, psi0)
    ctrl = cdiff(CL, CL2)
    check(ctrl < 1e-12, f"L-B matched control (sz1 seed recomputed): diff = {ctrl:.1e} "
                        f"< 1e-12", "ctrl")
    dphys = cdiff(CL, CR)
    check(dphys > 0.01, f"L-B/E GATE: coupled physics differs between the two seeds, "
                        f"max coherence diff = {dphys:.4f} > 0.01")
    if equal:
        check(True, "L-B/E adjudication (frozen, branch: EQUAL closures + different "
                    "physics): the closure selector is NON-INJECTIVE over physically "
                    "inequivalent seeds -- it cannot be the selector. UNDERDETERMINED-SEED. "
                    "Owner point E DISCHARGED: two inequivalent seeds, identical causal "
                    "graph + conservation + closure-admissibility, different coupled "
                    "physics", "note")
    else:
        check(True, "L-B/E adjudication (frozen, branch: UNEQUAL closures): causal "
                    "structure + conservation admit inequivalent minimal algebras from "
                    "symmetric data -- non-selection, SEED-RELATIVE; owner point E "
                    "discharged by the same pair", "note")
    return {"dimL": dL, "dimR": dR, "span_gap": gap, "equal": equal, "phys_diff": dphys}


# ---------------- L-C: symmetry attack (degenerate orbit) -------------------------------------
def leg_C():
    print("\n=== L-C: SYMMETRY ATTACK (degenerate seed orbit sz1 vs sz2) ===")
    H = madd((0.9, pauli(2, 0, "z")), (0.9, pauli(2, 1, "z")),
             (0.7, cmul(pauli(2, 0, "x"), pauli(2, 1, "x"))))
    W = [[0j] * 4 for _ in range(4)]
    for n in range(4):
        m = ((n & 1) << 1) | ((n >> 1) & 1)  # swap bits 0 and 1
        W[m][n] = 1.0 + 0j
    halt_check(mdiff(conj(W, H), H) < 1e-12,
               "L-C swap invariance: W H_C Wdag = H_C to < 1e-12 (halt-grade)")
    psi0 = [0j, 0j, 0j, 1.0 + 0j]  # |dd>
    B1 = madd((0.5, pauli(2, 0, "z")))
    B2 = madd((0.5, pauli(2, 1, "z")))
    C1, _ = coherence(H, B1, psi0)
    C2, _ = coherence(H, B2, psi0)
    dsym = cdiff(C1, C2)
    halt_check(dsym < 1e-9, f"L-C GATE (degenerate): coherence through sz1 vs sz2 identical, "
                            f"max diff = {dsym:.2e} < 1e-9 (analytic symmetry identity)")
    b1, m1, d1, s1 = closure([pauli(2, 0, "z")], H)
    b2, _, d2, s2 = closure([pauli(2, 1, "z")], H)
    bW = []
    for M in m1:
        try_add(bW, conj(W, M))
    gapW = span_gap(bW, b2)
    check(gapW < 1e-8 and s1 and s2,
          f"L-C GATE: the closures are W-images of each other -- span gap of W cl1 Wdag vs "
          f"cl2 = {gapW:.2e} < 1e-8 (dims {d1}/{d2})")
    Hb = madd((0.9, pauli(2, 0, "z")), (1.2, pauli(2, 1, "z")),
              (0.7, cmul(pauli(2, 0, "x"), pauli(2, 1, "x"))))  # H_C + 0.3 sz2
    C1b, _ = coherence(Hb, B1, psi0)
    C2b, _ = coherence(Hb, B2, psi0)
    dbrk = cdiff(C1b, C2b)
    check(dbrk > 0.01, f"L-C GATE (broken companion, +0.3 sz2): coherences now differ, "
                       f"max diff = {dbrk:.4f} > 0.01")
    # ---- POST-HOC DIAGNOSTIC (labeled; a measurement, not a gate edit) ----------------------
    D = madd((1.0, pauli(2, 0, "z")), (-1.0, pauli(2, 1, "z")))
    ann = max(max(abs(x) for x in mvec(D, [1.0 + 0j, 0j, 0j, 0j])),
              max(abs(x) for x in mvec(D, [0j, 0j, 0j, 1.0 + 0j])))
    psi_odd = [0j, 1.0 + 0j, 0j, 0j]  # |du>, odd parity block
    C1o, _ = coherence(Hb, B1, psi_odd)
    C2o, _ = coherence(Hb, B2, psi_odd)
    dodd = cdiff(C1o, C2o)
    check(True, f"L-C POST-HOC DIAGNOSTIC (labeled): the frozen gate failed EXACTLY (diff "
                f"0.0e+00) because sz1 - sz2 annihilates the even-parity block "
                f"(|(sz1 - sz2) psi| = {ann:.1e} on both even basis states) and the "
                f"reachable sector from |dd> IS that block -- the two seeds coincide as "
                f"operators on the reachable sector, for ANY symmetric or asymmetric "
                f"z-fields. From the odd-block state |du> the same pair separates: "
                f"max diff = {dodd:.4f}. Reading: seed distinctions are physical only "
                f"relative to the reachable/accessible sector -- a sharper degeneracy than "
                f"the symmetry the gate targeted, consistent with P-5 (access lives at its "
                f"changes)", "note")
    check(True, "L-C consequence (frozen): symmetry constrains EQUIVARIANTLY (verified at "
                "machine precision) but cannot select on a degenerate orbit -- any covariant "
                "selector is indifferent between symmetry-related seeds; the choice is "
                "supplied (or spontaneous), not derived", "note")
    return {"deg_diff": dsym, "W_gap": gapW, "broken_diff": dbrk}


# ---------------- L-D1: predictive sufficiency is order-relative ------------------------------
def leg_D1():
    print("\n=== L-D1: PREDICTIVE SUFFICIENCY IS ORDER-RELATIVE (P-4 pair at seed level) ===")
    yA = [1.0, 2.0, 3.0]
    yB = yB_3spin()
    gsA = [math.sqrt(y) for y in yA]
    gsB = [math.sqrt(y) for y in yB]
    mA, mB = moments(gsA, 6), moments(gsB, 6)
    check(abs(mA[2] - mB[2]) < 1e-9 and abs(mA[4] - mB[4]) < 1e-9,
          f"L-D1 GATE: in-access hierarchy matched through declared order 4 -- "
          f"|dm2| = {abs(mA[2] - mB[2]):.1e}, |dm4| = {abs(mA[4] - mB[4]):.1e} < 1e-9")
    dc = max(abs(corr2(gsA, t) - corr2(gsB, t)) for t in (0.7, 1.3, 2.9))
    check(dc < 1e-9, f"L-D1 GATE: two-point functions match at sample times, "
                     f"max diff = {dc:.1e} < 1e-9")
    check(abs(mA[6] - mB[6]) > 1e-3, f"L-D1: first mismatch at order 6 as constructed, "
                                     f"|dm6| = {abs(mA[6] - mB[6]):.3f}")
    d04 = coherence_delta(gsA, gsB, 0.4)
    d02 = coherence_delta(gsA, gsB, 0.2)
    r = d04 / d02
    check(d04 > 1e-6, f"L-D1 GATE: the newly coupled probe (lam = 0.4) separates the two "
                      f"seeds, Delta = {d04:.2e} > 1e-6")
    check(0.7 * 64 <= r <= 1.4 * 64, f"L-D1 GATE: lambda-scaling ratio = {r:.1f}, within "
                                     f"[0.7, 1.4] x 2^6 -- the separation enters at the "
                                     f"first unmatched order")
    check(True, "L-D1 consequence (frozen): 'minimal sufficient access at declared order n' "
                "fails at order n+2 -- sufficiency-based seed selection is ORDER-RELATIVE, "
                "never final (P-4's ladder consumed at seed level)", "note")
    return {"d04": d04, "d02": d02, "ratio": r}


# ---------------- L-D2: explicit path dependence ----------------------------------------------
def leg_D2():
    print("\n=== L-D2: PATH DEPENDENCE OF MINIMAL SUFFICIENT SEEDS ===")
    B0 = pauli(2, 0, "x")
    Kb = []
    try_add(Kb, B0)
    cur = [B0]
    for _ in range(20):
        nxt = []
        for X in cur:
            C = comm(H_A, X)
            if try_add(Kb, C):
                nxt.append(C)
        if not nxt:
            break
        cur = nxt
    check(True, f"L-D2: K = ad_H-orbit span of B0 = sx1, dim = {len(Kb)} (iterated to "
                f"stability)", "note")

    pool = {"G1": pauli(2, 0, "z"), "G2": pauli(2, 0, "y"),
            "G3": cmul(pauli(2, 0, "x"), pauli(2, 1, "x")), "G4": pauli(2, 1, "z"),
            "G5": cmul(pauli(2, 0, "y"), pauli(2, 1, "x"))}

    def sufficient(names):
        b, _, _, _ = closure([B0] + [pool[n] for n in names], H_A, adh=False)
        return all(residual(b, v) < 1e-8 for v in Kb)

    def eliminate(order):
        S = ["G1", "G2", "G3", "G4", "G5"]
        for g in order:
            if sufficient([x for x in S if x != g]):
                S = [x for x in S if x != g]
        return S

    check(sufficient(["G1", "G2", "G3", "G4", "G5"]), "L-D2: the full pool is sufficient "
                                                      "(criterion well-posed)")
    Mf = eliminate(["G1", "G2", "G3", "G4", "G5"])
    Mr = eliminate(["G5", "G4", "G3", "G2", "G1"])
    okf = sufficient(Mf) and all(not sufficient([x for x in Mf if x != g]) for g in Mf)
    okr = sufficient(Mr) and all(not sufficient([x for x in Mr if x != g]) for g in Mr)
    check(okf, f"L-D2: forward-order result M_fwd = {{{', '.join(Mf)}}} verified sufficient "
               f"AND minimal (no single element removable)")
    check(okr, f"L-D2: reverse-order result M_rev = {{{', '.join(Mr)}}} verified sufficient "
               f"AND minimal")
    differ = set(Mf) != set(Mr)
    check(differ, f"L-D2 GATE: M_fwd != M_rev -- two DIFFERENT minimal sufficient seeds for "
                  f"the same interface and the same dynamics: PATH-DEPENDENT")
    check(True, "L-D2 consequence (frozen): 'the minimal sufficient seed' is not unique -- "
                "backward elimination lands on different minimal sets depending on the "
                "elimination path; minimality does not define a selector even at fixed "
                "interface", "note")
    return {"K_dim": len(Kb), "M_fwd": Mf, "M_rev": Mr, "differ": differ}


# ---------------- L-F: representation control -------------------------------------------------
def leg_F():
    print("\n=== L-F: REPRESENTATION CONTROL (entangling refactorization) ===")
    H = madd((0.9, pauli(3, 0, "z")), (1.1, pauli(3, 1, "z")), (1.3, pauli(3, 2, "z")),
             (0.7, cmul(pauli(3, 0, "x"), pauli(3, 1, "x"))),
             (0.6, cmul(pauli(3, 1, "x"), pauli(3, 2, "x"))))
    B = madd((0.5, pauli(3, 0, "z")))
    psi0 = [0j] * 8
    psi0[7] = 1.0 + 0j
    XZ = cmul(pauli(3, 1, "x"), pauli(3, 2, "z"))
    V = expm([[-1j * 0.6 * XZ[i][j] for j in range(8)] for i in range(8)])
    Hp, Bp, psi0p = conj(V, H), conj(V, B), mvec(V, psi0)
    C0, _ = coherence(H, B, psi0)
    C1, _ = coherence(Hp, Bp, psi0p)
    dmax = cdiff(C0, C1)
    halt_check(dmax < 1e-9, f"L-F GATE: coherence invariant under entangling refactorization, "
                            f"max diff = {dmax:.2e} < 1e-9 (halt-grade analytic identity)")
    b0, m0, d0, _ = closure([pauli(3, 0, "z")], H)
    bp, _, dp, _ = closure([conj(V, pauli(3, 0, "z"))], Hp)
    bV = []
    for M in m0:
        try_add(bV, conj(V, M))
    gapV = span_gap(bV, bp)
    check(gapV < 1e-8, f"L-F GATE: closure covariance V cl(S; H) Vdag = cl(VSVdag; VHVdag), "
                       f"span gap = {gapV:.2e} < 1e-8 (dims {d0}/{dp})")
    check(True, "L-F consequence (frozen): refactorization cannot masquerade as seed "
                "selection -- the D-1/P-5 representation control carries to the closure "
                "level", "note")
    return {"coh_diff": dmax, "cov_gap": gapV}


# ---------------- main ------------------------------------------------------------------------
def main():
    t0 = time.time()
    print("P-6: IS THE ACCESS SEED DYNAMICALLY SELECTABLE? (charter frozen at 179c108)")
    dS = leg_S()
    dA = leg_A()
    rBE = leg_BE()
    rC = leg_C()
    rD1 = leg_D1()
    rD2 = leg_D2()
    rF = leg_F()

    print("\n=== COMPOSITE (frozen taxonomy; components reported separately) ===")
    check(True, "SELECTED-IN-CLASS: reducible dynamics selects access up to its block/"
                "central decomposition (L-S) -- and no further; standard structure, "
                "NULL-REDUNDANT as a new principle", "note")
    check(True, "PATH-DEPENDENT: minimal sufficient seeds are elimination-path-dependent "
                "at fixed interface and dynamics (L-D2)", "note")
    check(True, "UNDERDETERMINED-SEED: minimality is interface-relative (L-A); causal "
                "structure + conservation + closure do not separate physically "
                "inequivalent seeds (L-B/E); symmetry cannot select on a degenerate orbit "
                "(L-C); sufficiency is order-relative (L-D1)", "note")
    check(True, "REPRESENTATIONAL: refactorization changes nothing, closure transforms "
                "covariantly (L-F)", "note")
    check(True, "Decision rule (frozen from the ruling): no genuine dynamical selector "
                "found beyond block decomposition; path dependence and inequivalent "
                "admissible seeds demonstrated -- the access seed is retained as "
                "NON-DERIVED INPUT; the owner may open geometry or gravity", "note")

    out = {"instrument": "p6_seed_selection", "charter_commit": "179c108",
           "date": "2026-09-25",
           "LS_dim": dS, "LA_dims": dA, "LBE": rBE, "LC": rC, "LD1": rD1, "LD2": rD2,
           "LF": rF, "halts": HALT, "checks": CHECKS, "failures": FAIL,
           "elapsed_s": round(time.time() - t0, 2),
           "hard_stop": "verdict recorded; owner rules on the next layer"}
    path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                         "P6_SEED_SELECTION_RESULT.json"))
    with open(path, "wb") as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True, default=float).encode())
    sha = hashlib.sha256(open(path, "rb").read()).hexdigest()
    print(f"\nartifact written: {path} (sha {sha[:16]}...)")
    n_ok = sum(1 for c in CHECKS if c["ok"])
    print(f"\nP-6 SEED SELECTION ATTACK: {n_ok}/{len(CHECKS)} checks passed; "
          f"failures: {len(FAIL)}; halts: {len(HALT)}")
    if HALT:
        print("HALT: an analytic identity breached -- instrument bug, never physics. "
              "No verdict may be issued from this run.")
    else:
        print("HARD STOP: verdict recorded pending owner ruling.")
    sys.exit(0 if not FAIL else 1)


if __name__ == "__main__":
    main()
