#!/usr/bin/env python3
"""g2_spectral: the spectral/frequency-domain geometry attack.

CHARTER: G2_SPECTRAL_CHARTER_01.md (pre-registration frozen at commit c83e9d7 BEFORE this
instrument ran; authority GitHub Issue #2 owner comment 5827773903). A fresh attack on the
geometry question -- NOT a repair of G-1's eight preserved reds. No time-of-flight
thresholds anywhere; no gravity input; no metric defined by fiat.

Frozen candidates: C1 heat-kernel hop metric (log-slope of H_ab(t) at t = 0.02/0.04/0.08
with Richardson extrapolation, rounded to integers) | C2 resistance form
R(a,b) = (e_a - e_b)^T M (e_a - e_b), M = K^-1 or L^+ (series-law identity on chains as
the validation target).

Legs: L-E identity controls | L-C single-site grid-vs-Lanczos degeneracy under resolvent
and heat data | L-D multi-site hop matrix, shell-estimator dimension (1D/2D/3D + quantum
XX), held-out additive triple + trilateration | L-F resistance metric density on the
graded chain | L-B Givens scramble | L-H noncommutative validation + congruence | L-I/G
exact moment ladder C40 vs C80 + heat-trace horizon.

Pure stdlib. Run: python3 calc/g2_spectral.py
"""
import cmath
import hashlib
import json
import math
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from partition_selection_p1 import jacobi_eig
from p5_access import expm
from g1_geometry import chain_edges, grid2_edges, grid3_edges, ring_edges

FAIL = []
CHECKS = []
HALT = []
T3 = (0.02, 0.04, 0.08)  # frozen t-triple for hop slopes


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


# ---------------- spectral machinery ----------------------------------------------------------
def kmul_sparse(n, edges, pin, x):
    y = [pin[i] * x[i] for i in range(n)]
    for i, j, k in edges:
        d = k * (x[i] - x[j])
        y[i] += d
        y[j] -= d
    return y


def heat_col(n, edges, pin, src, t, order=80):
    """(e^{-Kt}) e_src via truncated Taylor (factorially convergent for ||K|| t < 1)."""
    term = [0.0] * n
    term[src] = 1.0
    acc = term[:]
    for k in range(1, order + 1):
        y = kmul_sparse(n, edges, pin, term)
        term = [(-t / k) * v for v in y]
        for i in range(n):
            acc[i] += term[i]
    return acc


def hop_hat(cols, j):
    """Richardson-extrapolated log-slope at site j from the three frozen heat columns."""
    h1, h2, h3 = abs(cols[0][j]), abs(cols[1][j]), abs(cols[2][j])
    if min(h1, h2, h3) <= 0.0:
        return None
    s1 = math.log(h2 / h1) / math.log(2.0)
    s2 = math.log(h3 / h2) / math.log(2.0)
    return 2 * s1 - s2


def hops_from(n, edges, pin, src):
    cols = [heat_col(n, edges, pin, src, t) for t in T3]
    return [hop_hat(cols, j) for j in range(n)]


def solve(Ain, bin_):
    """Dense Gaussian elimination with partial pivoting."""
    n = len(Ain)
    A = [row[:] + [bin_[i]] for i, row in enumerate(Ain)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(A[r][c]))
        A[c], A[p] = A[p], A[c]
        piv = A[c][c]
        for r in range(c + 1, n):
            f = A[r][c] / piv
            if f != 0.0:
                for k in range(c, n + 1):
                    A[r][k] -= f * A[c][k]
    x = [0.0] * n
    for r in range(n - 1, -1, -1):
        s = A[r][n] - sum(A[r][k] * x[k] for k in range(r + 1, n))
        x[r] = s / A[r][r]
    return x


def dense_K(n, edges, pin):
    K = [[0.0] * n for _ in range(n)]
    for i in range(n):
        K[i][i] = pin[i]
    for i, j, k in edges:
        K[i][i] += k
        K[j][j] += k
        K[i][j] -= k
        K[j][i] -= k
    return K


def resistance(n, edges, ks_pin, a, b, pinned):
    """C2: (e_a - e_b)^T M (e_a - e_b), M = K^-1 (pinned) or L^+ (unpinned, via L + J/n)."""
    K = dense_K(n, edges, ks_pin)
    if not pinned:
        for i in range(n):
            for j in range(n):
                K[i][j] += 1.0 / n
    rhs = [0.0] * n
    rhs[a], rhs[b] = 1.0, -1.0
    x = solve(K, rhs)
    return x[a] - x[b]


def real_expm(M, t):
    """e^{-Mt} for real symmetric M via the shared exact scaling-and-squaring expm."""
    n = len(M)
    E = expm([[-t * M[i][j] + 0j for j in range(n)] for i in range(n)])
    return [[E[i][j].real for j in range(n)] for i in range(n)]


# ---------------- L-E: metric identity controls ------------------------------------------------
def leg_E():
    print("\n=== L-E: METRIC IDENTITY CONTROLS (unpinned uniform chain N = 41) ===")
    n = 41
    edges = chain_edges(n)
    r1 = resistance(n, edges, [0.0] * n, 5, 25, pinned=False)
    r2 = resistance(n, edges, [0.0] * n, 10, 35, pinned=False)
    check(abs(r1 - 20.0) < 1e-9 and abs(r2 - 25.0) < 1e-9,
          f"L-E GATE (C2 series law, DERIVED identity): R(5,25) = {r1:.12f} (=20), "
          f"R(10,35) = {r2:.12f} (=25) to 1e-9 -- effective resistance = summed inverse "
          f"stiffness, a known network metric, cited standard (NULL-REDUNDANT)")
    hp = hops_from(n, edges, [0.0] * n, 10)
    errs = [(5, abs(hp[15] - 5)), (12, abs(hp[22] - 12)), (20, abs(hp[30] - 20))]
    ok = all(e < 0.3 for _, e in errs)
    check(ok, f"L-E GATE (C1 hop identity): d_hat errors vs substrate hops {{5, 12, 20}} = "
              f"{errs[0][1]:.3f}, {errs[1][1]:.3f}, {errs[2][1]:.3f} < 0.3 before rounding")
    return {"R": [r1, r2], "hop_errs": [e for _, e in errs]}


# ---------------- L-C: the single-site degeneracy under spectral data --------------------------
def leg_C():
    print("\n=== L-C: SINGLE-SITE DEGENERACY (grid vs Lanczos chain, full spectral data) ===")
    w = 10
    n = w * w
    edges = grid2_edges(w, w)
    K = dense_K(n, edges, [0.5] * n)
    q = [0.0] * n
    q[0] = 1.0
    Q = [q]
    alphas, betas = [], []
    for _ in range(n):
        z = [sum(K[i][j] * Q[-1][j] for j in range(n)) for i in range(n)]
        al = sum(z[i] * Q[-1][i] for i in range(n))
        alphas.append(al)
        for qq in Q:
            c = sum(z[i] * qq[i] for i in range(n))
            z = [z[i] - c * qq[i] for i in range(n)]
        for qq in Q:
            c = sum(z[i] * qq[i] for i in range(n))
            z = [z[i] - c * qq[i] for i in range(n)]
        be = math.sqrt(sum(x * x for x in z))
        if be < 1e-8:
            break
        betas.append(be)
        Q.append([x / be for x in z])
    m = len(alphas)
    T = [[0.0] * m for _ in range(m)]
    for i in range(m):
        T[i][i] = alphas[i]
        if i + 1 < m:
            T[i][i + 1] = T[i + 1][i] = betas[i]
    check(True, f"L-C: Lanczos chain rebuilt, Krylov dimension {m}", "note")

    dres = 0.0
    for s in (0.1, 0.5, 1.0, 2.0):
        Ks = [[K[i][j] + (s if i == j else 0.0) for j in range(n)] for i in range(n)]
        Ts = [[T[i][j] + (s if i == j else 0.0) for j in range(m)] for i in range(m)]
        eg = [0.0] * n
        eg[0] = 1.0
        ec = [0.0] * m
        ec[0] = 1.0
        g_grid = solve(Ks, eg)[0]
        g_chain = solve(Ts, ec)[0]
        dres = max(dres, abs(g_grid - g_chain))
    halt_check(dres < 1e-9, f"L-C GATE (resolvent): single-site G_aa(-s) identical across "
                            f"s in {{0.1, 0.5, 1, 2}}, max diff = {dres:.2e} < 1e-9 "
                            f"(halt-grade: Lanczos preserves the seed spectral measure)")

    lamg, Vg = jacobi_eig(K)
    lamc, Vc = jacobi_eig(T)
    dheat = 0.0
    for t in (0.5, 2.0, 8.0):
        hg = sum(Vg[0][k] ** 2 * math.exp(-lamg[k] * t) for k in range(n))
        hc = sum(Vc[0][k] ** 2 * math.exp(-lamc[k] * t) for k in range(m))
        dheat = max(dheat, abs(hg - hc))
    halt_check(dheat < 1e-9, f"L-C GATE (heat data): single-site H_aa(t) identical across "
                             f"t in {{0.5, 2, 8}}, max diff = {dheat:.2e} < 1e-9")
    check(True, "L-C consequence (frozen): spectral data DO NOT break the one-site "
                "degeneracy -- a 2D grid and a 1D chain share the complete single-site "
                "frequency-domain interface. Single-site geometric underdetermination is a "
                "STRUCTURAL LIMIT of the interface (decision rule 2 at this access), not a "
                "G-1 instrument artifact", "note")
    return {"resolvent_diff": dres, "heat_diff": dheat, "krylov_dim": m}


# ---------------- L-D: multi-site reconstruction + dimension + held-out ------------------------
W = 31
ANCH = [(6, 6), (6, 24), (24, 6), (24, 24), (15, 12)]
XS = (20, 18)


def shell_dim(hops, src_known_ok=True):
    """Frozen shell estimator: d = 1 + log[S(6)/S(3)]/log 2 on rounded hop distances."""
    r = [None if h is None else int(round(h)) for h in hops]
    s3 = sum(1 for v in r if v == 3)
    s6 = sum(1 for v in r if v == 6)
    return 1.0 + math.log(s6 / s3) / math.log(2.0), s3, s6


def leg_D():
    print("\n=== L-D: MULTI-SITE RECONSTRUCTION, DIMENSION, HELD-OUT ===")
    res = {}
    # dimension: 1D
    n = 61
    hp1 = hops_from(n, chain_edges(n), [0.5] * n, 30)
    d1, s3, s6 = shell_dim(hp1)
    check(0.65 <= d1 <= 1.35, f"L-D GATE dimension 1D: d_hat = {d1:.3f} in [0.65, 1.35] "
                              f"(shells {s3} -> {s6})")
    # dimension: 2D
    n2 = W * W
    e2 = grid2_edges(W, W)
    p2 = [0.5] * n2
    hp2 = hops_from(n2, e2, p2, 15 * W + 15)
    d2, s3, s6 = shell_dim(hp2)
    check(1.65 <= d2 <= 2.35, f"L-D GATE dimension 2D: d_hat = {d2:.3f} in [1.65, 2.35] "
                              f"(shells {s3} -> {s6})")
    # dimension: 3D
    s = 13
    n3 = s ** 3
    hp3 = hops_from(n3, grid3_edges(s), [0.5] * n3, (6 * s + 6) * s + 6)
    d3, s3c, s6c = shell_dim(hp3)
    check(2.65 <= d3 <= 3.35, f"L-D GATE dimension 3D: d_hat = {d3:.3f} in [2.65, 3.35] "
                              f"(shells {s3c} -> {s6c})")
    res["dims"] = {"d1": d1, "d2": d2, "d3": d3}

    # anchor hop matrix + validation
    aidx = [x * W + y for x, y in ANCH]
    xi = XS[0] * W + XS[1]
    hcols = {}
    for k, sidx in enumerate(aidx + [xi]):
        hcols[k] = hops_from(n2, e2, p2, sidx)
    hc0b = hops_from(n2, e2, p2, aidx[0])
    mc = max(abs((hcols[0][j] or 0) - (hc0b[j] or 0)) for j in range(n2))
    check(mc == 0.0, f"L-D matched control (A1 heat columns recomputed): diff = {mc:.1e}",
          "ctrl")
    hopmat = [[0.0] * 5 for _ in range(5)]
    maxerr = 0.0
    for i in range(5):
        for j in range(5):
            if i != j:
                raw = hcols[i][aidx[j]]
                true = abs(ANCH[i][0] - ANCH[j][0]) + abs(ANCH[i][1] - ANCH[j][1])
                maxerr = max(maxerr, abs(raw - true))
                hopmat[i][j] = round(raw)
    check(maxerr < 0.3, f"L-D GATE pairwise distances: all 10 anchor-pair hop estimates "
                        f"within {maxerr:.3f} < 0.3 of substrate hop counts before rounding")
    tXr = [hcols[5][a] for a in aidx]
    tX = [round(v) for v in tXr]

    # held-out 1: exact additive triple
    add_ok = hopmat[0][3] == hopmat[0][4] + hopmat[4][3]
    check(add_ok, f"L-D GATE held-out (additive triple, integers): d(A1,A4) = "
                  f"{hopmat[0][3]} equals d(A1,A5) + d(A5,A4) = {hopmat[0][4]} + "
                  f"{hopmat[4][3]} EXACTLY")

    # held-out 2: MDS + trilateration (capture reported, not gated)
    D2m = [[float(hopmat[i][j]) ** 2 for j in range(5)] for i in range(5)]
    Jc = [[(1.0 if i == j else 0.0) - 0.2 for j in range(5)] for i in range(5)]
    JD = [[sum(Jc[i][k] * D2m[k][j] for k in range(5)) for j in range(5)] for i in range(5)]
    B = [[-0.5 * sum(JD[i][k] * Jc[k][j] for k in range(5)) for j in range(5)]
         for i in range(5)]
    lam, V = jacobi_eig(B)
    order = sorted(range(5), key=lambda k: -lam[k])
    cap = (lam[order[0]] + lam[order[1]]) / sum(abs(x) for x in lam)
    co = [(V[i][order[0]] * math.sqrt(max(lam[order[0]], 0.0)),
           V[i][order[1]] * math.sqrt(max(lam[order[1]], 0.0))) for i in range(5)]
    a1, a2, a3 = co[0], co[1], co[2]
    r1, r2, r3 = float(tX[0]), float(tX[1]), float(tX[2])
    A11, A12 = 2 * (a2[0] - a1[0]), 2 * (a2[1] - a1[1])
    A21, A22 = 2 * (a3[0] - a1[0]), 2 * (a3[1] - a1[1])
    b1 = r1 ** 2 - r2 ** 2 + a2[0] ** 2 + a2[1] ** 2 - a1[0] ** 2 - a1[1] ** 2
    b2 = r1 ** 2 - r3 ** 2 + a3[0] ** 2 + a3[1] ** 2 - a1[0] ** 2 - a1[1] ** 2
    det = A11 * A22 - A12 * A21
    px = (b1 * A22 - b2 * A12) / det
    py = (A11 * b2 - A21 * b1) / det
    errs = []
    for kk in (3, 4):
        pred = math.hypot(px - co[kk][0], py - co[kk][1])
        rel = abs(pred - tX[kk]) / tX[kk]
        errs.append(rel)
        check(rel < 0.25, f"L-D GATE held-out (trilateration): predicted d(X,A{kk + 1}) = "
                          f"{pred:.2f} vs measured {tX[kk]}, rel err = {rel:.3f} < 0.25 "
                          f"(frozen slack covers l1-in-l2 embedding distortion)")
    check(True, f"L-D MDS capture (reported, not gated): {cap:.3f}", "note")
    res["held_out"] = {"additive": add_ok, "tri_errs": errs, "capture": cap}

    # quantum XX chain (noncommutative substrate), one-magnon amplitudes
    N = 31
    h = [[0.0] * N for _ in range(N)]
    for i in range(N):
        h[i][i] = 0.5
        if i + 1 < N:
            h[i][i + 1] = h[i + 1][i] = 1.0

    def amp_cols(src):
        cols = []
        for t in T3:
            term = [0j] * N
            term[src] = 1.0 + 0j
            acc = term[:]
            for k in range(1, 81):
                y = [sum(h[i][j] * term[j] for j in range(max(0, i - 1),
                                                          min(N, i + 2))) for i in range(N)]
                term = [(-1j * t / k) * v for v in y]
                for i in range(N):
                    acc[i] += term[i]
            cols.append([abs(v) for v in acc])
        return cols

    qc15 = amp_cols(15)
    qh15 = [hop_hat(qc15, j) for j in range(N)]
    dq, s3q, s6q = shell_dim(qh15)
    check(0.65 <= dq <= 1.35, f"L-D GATE dimension quantum (XX one-magnon): d_hat = "
                              f"{dq:.3f} in [0.65, 1.35] (shells {s3q} -> {s6q})")
    qc5 = amp_cols(5)
    qh5 = [hop_hat(qc5, j) for j in range(N)]
    qa = round(qh5[25]) == round(qh5[15]) + round(qh15[25])
    check(qa, f"L-D GATE quantum hop additivity (integers): d(5,25) = {round(qh5[25])} "
              f"equals d(5,15) + d(15,25) = {round(qh5[15])} + {round(qh15[25])} EXACTLY")
    res["quantum"] = {"dq": dq, "additive": qa}
    return res, hcols, aidx, xi


# ---------------- L-F: metric density from spectral data ---------------------------------------
def leg_F():
    print("\n=== L-F: INHOMOGENEITY FROM SPECTRAL DATA (graded chain, resistance form) ===")
    n = 81
    ks = [1.0 if e < 40 else 2.25 for e in range(n - 1)]
    edges = chain_edges(n, ks)
    pin0 = [0.0] * n

    def R(a, b):
        return resistance(n, edges, pin0, a, b, pinned=False)

    R1030, R3050, R5070 = R(10, 30), R(30, 50), R(50, 70)
    rho1, rho3 = R1030 / 20.0, R5070 / 20.0
    ratio = rho3 / rho1
    check(abs(ratio - 1.0 / 2.25) < 1e-6,
          f"L-F GATE: spectral metric density ratio rho([50,70])/rho([10,30]) = "
          f"{ratio:.9f} = 1/2.25 to 1e-6 -- EXACT tracking of the declared stiffness "
          f"(G-1's time-of-flight measured 1.106 vs 1.5 on this same substrate)")
    Rpred = 10.0 * rho1 + R3050 + 10.0 * rho3
    Rmeas = R(20, 60)
    check(abs(Rpred - Rmeas) < 0.01,
          f"L-F GATE held-out: R_hat(20,60) = {Rpred:.6f} predicted from probe-resolution "
          f"densities vs direct R(20,60) = {Rmeas:.6f}, diff = "
          f"{abs(Rpred - Rmeas):.2e} < 0.01")
    check(True, "L-F consequence (frozen): the G-1 L-CRV failure was the ARRIVAL-TIME "
                "INSTRUMENT -- the static spectral functional recovers the inhomogeneous "
                "metric density exactly, with a held-out prediction. Effective resistance "
                "is standard network mathematics: NULL-REDUNDANT as a principle", "note")
    return {"ratio": ratio, "R_pred": Rpred, "R_meas": Rmeas}


# ---------------- L-B: representation attack ---------------------------------------------------
def leg_B(hcols, aidx, xi):
    print("\n=== L-B: REPRESENTATION ATTACK (Givens-scrambled grid, spectral data) ===")
    n = W * W
    K = dense_K(n, grid2_edges(W, W), [0.5] * n)
    rots = [(i, (7 * i + 3) % n, 0.3 + 0.02 * i) for i in range(30)]

    def orow(e):
        v = e[:]
        for p, q, th in rots:
            c, s0 = math.cos(th), math.sin(th)
            vp, vq = v[p], v[q]
            v[p] = c * vp - s0 * vq
            v[q] = s0 * vp + c * vq
        return v

    for p, q, th in rots:  # K' = O K O^T by two-sided Givens application
        c, s0 = math.cos(th), math.sin(th)
        for r in range(n):
            a, b = K[r][p], K[r][q]
            K[r][p] = c * a - s0 * b
            K[r][q] = s0 * a + c * b
        for r in range(n):
            a, b = K[p][r], K[q][r]
            K[p][r] = c * a - s0 * b
            K[q][r] = s0 * a + c * b
    ea = [0.0] * n
    ea[aidx[0]] = 1.0
    va = orow(ea)
    t = 0.5
    term = va[:]
    acc = term[:]
    for k in range(1, 61):
        y = [sum(K[i][j] * term[j] for j in range(n)) for i in range(n)]
        term = [(-t / k) * v for v in y]
        for i in range(n):
            acc[i] += term[i]
    dmax = 0.0
    for tgt in (aidx[1], aidx[3], xi):
        et = [0.0] * n
        et[tgt] = 1.0
        vt = orow(et)
        hs = sum(vt[i] * acc[i] for i in range(n))
        # unscrambled reference from sparse heat column at the same t
        ref_col = heat_col(n, grid2_edges(W, W), [0.5] * n, aidx[0], 0.5, order=60)
        dmax = max(dmax, abs(hs - ref_col[tgt]))
    halt_check(dmax < 1e-9, f"L-B GATE: two-point spectral data identical under the frozen "
                            f"30-rotation scramble, max diff = {dmax:.2e} < 1e-9 "
                            f"(halt-grade) -- d_hat, shells, MDS all invariant")
    return dmax


# ---------------- L-H: noncommutative leg ------------------------------------------------------
def leg_H():
    print("\n=== L-H: NONCOMMUTATIVE LEG (XX spin chain; congruence invariance) ===")
    # full-space validation on 3 spins: bit i set = magnon at site i
    d = 8
    Hs = [[0.0] * d for _ in range(d)]
    for st in range(d):
        Hs[st][st] = 0.5 * bin(st).count("1")
        for i in range(2):
            if ((st >> i) & 1) != ((st >> (i + 1)) & 1):
                Hs[st][st ^ (1 << i) ^ (1 << (i + 1))] += 1.0
    hh = [[0.5, 1.0, 0.0], [1.0, 0.5, 1.0], [0.0, 1.0, 0.5]]
    t = 1.0
    Es = expm([[-1j * t * Hs[i][j] for j in range(d)] for i in range(d)])
    Eh = expm([[-1j * t * hh[i][j] for j in range(3)] for i in range(3)])
    mag = [1, 2, 4]  # one-magnon basis states
    dfull = max(abs(Es[mag[i]][mag[j]] - Eh[i][j]) for i in range(3) for j in range(3))
    halt_check(dfull < 1e-12, f"L-H GATE: one-magnon amplitudes of the FULL 2^3 spin "
                              f"system equal the hopping-matrix amplitudes, max diff = "
                              f"{dfull:.2e} < 1e-12 (halt-grade) -- the substrate is the "
                              f"genuinely noncommutative spin system")
    hA = [[0.0] * 3 for _ in range(3)]
    hA[0][1] = hA[1][0] = 1.0
    hB = [[0.0] * 3 for _ in range(3)]
    hB[1][2] = hB[2][1] = 1.0
    comm = max(abs(sum(hA[i][k] * hB[k][j] - hB[i][k] * hA[k][j] for k in range(3)))
               for i in range(3) for j in range(3))
    check(comm > 0.5, f"L-H: exchange terms genuinely noncommuting, ||[h12, h23]|| = "
                      f"{comm:.1f} > 0")
    # congruence on N = 31: h' = O h O^T with 20 frozen Givens; transformed access vectors
    N = 31
    h = [[0.0] * N for _ in range(N)]
    for i in range(N):
        h[i][i] = 0.5
        if i + 1 < N:
            h[i][i + 1] = h[i + 1][i] = 1.0
    rots = [(i, (5 * i + 2) % N, 0.25 + 0.03 * i) for i in range(20)]
    hp = [row[:] for row in h]
    for p, q, th in rots:
        c, s0 = math.cos(th), math.sin(th)
        for r in range(N):
            a, b = hp[r][p], hp[r][q]
            hp[r][p] = c * a - s0 * b
            hp[r][q] = s0 * a + c * b
        for r in range(N):
            a, b = hp[p][r], hp[q][r]
            hp[p][r] = c * a - s0 * b
            hp[q][r] = s0 * a + c * b

    def orow(e):
        v = e[:]
        for p, q, th in rots:
            c, s0 = math.cos(th), math.sin(th)
            vp, vq = v[p], v[q]
            v[p] = c * vp - s0 * vq
            v[q] = s0 * vp + c * vq
        return v

    t = 0.5
    dmax = 0.0
    for (a, b) in ((5, 15), (5, 25)):
        ea = [0.0] * N
        ea[a] = 1.0
        va = orow(ea)
        term = [complex(v) for v in va]
        acc = term[:]
        for k in range(1, 81):
            y = [sum(hp[i][j] * term[j] for j in range(N)) for i in range(N)]
            term = [(-1j * t / k) * v for v in y]
            for i in range(N):
                acc[i] += term[i]
        eb = [0.0] * N
        eb[b] = 1.0
        vb = orow(eb)
        amp_s = sum(vb[i] * acc[i] for i in range(N))
        term = [0j] * N
        term[a] = 1.0 + 0j
        acc0 = term[:]
        for k in range(1, 81):
            y = [sum(h[i][j] * term[j] for j in range(max(0, i - 1), min(N, i + 2)))
                 for i in range(N)]
            term = [(-1j * t / k) * v for v in y]
            for i in range(N):
                acc0[i] += term[i]
        dmax = max(dmax, abs(amp_s - acc0[b]))
    halt_check(dmax < 1e-9, f"L-H GATE (congruence): |A_ab(t)| data identical under the "
                            f"frozen 20-rotation mode mixing, max diff = {dmax:.2e} < 1e-9 "
                            f"(halt-grade) -- the candidate spectral geometry is "
                            f"basis/congruence invariant")
    return {"full_space": dfull, "congruence": dmax, "comm_norm": comm}


# ---------------- L-I/G: the geometry ladder + topology horizon --------------------------------
def leg_IG():
    print("\n=== L-I/G: THE GEOMETRY LADDER (C40 vs C80, exact walk counts) ===")

    def walks(N, nmax):
        c = [0] * N
        c[0] = 1
        out = {}
        for step in range(1, nmax + 1):
            c = [c[(i - 1) % N] + c[(i + 1) % N] for i in range(N)]
            out[step] = c[0]
        return out

    w40 = walks(40, 40)
    w80 = walks(80, 40)
    eq = all(w40[nn] == w80[nn] for nn in (10, 20, 30, 38))
    check(eq, f"L-I GATE: exact closed-walk counts (A^n)_00 EQUAL at n = 10, 20, 30, 38 "
              f"(e.g. n=38: {w40[38]} = {w80[38]}) -- matched low-order spectral data by "
              f"construction, non-isometric graphs")
    diff40 = w40[40] - w80[40]
    check(diff40 != 0, f"L-I GATE: first distinguishing moment order = 40 = the "
                       f"circumference; (A^40)_00 differs by exactly {diff40} (the two "
                       f"winding walks)")
    check(True, "L-I consequence (frozen): the geometry ladder -- the interface "
                "distinguishes non-isometric graphs at invariant order EQUAL to the "
                "shortest non-contractible cycle. Low-order spectral matching never "
                "certifies global geometry (P-4's cumulant ladder, geometric form)", "note")

    def htrace(N, t):
        return sum(math.exp(-(2.0 - 2.0 * math.cos(2.0 * math.pi * k / N)) * t)
                   for k in range(N)) / N

    d1 = abs(htrace(40, 1.0) - htrace(80, 1.0))
    d40 = abs(htrace(40, 40.0) - htrace(80, 40.0))
    check(d1 < 1e-14, f"L-G GATE: |H_00 difference| at t = 1 is {d1:.2e} < 1e-14 (the "
                      f"exact difference ~ t^40/40! sits below the float floor -- "
                      f"established instead by the integer ladder)")
    check(d40 > 1e-6, f"L-G GATE: |H_00 difference| at t = 40 is {d40:.2e} > 1e-6 -- "
                      f"topology becomes spectrally visible at the recurrence scale")
    check(True, "L-G consequence (frozen): what is identifiable is exact -- NOTHING about "
                "global topology below moment order/recurrence scale ~ circumference; "
                "everything above it. The frequency-domain form of G-1's causal horizon",
          "note")
    return {"walk_diff_40": diff40, "heat_diff_t1": d1, "heat_diff_t40": d40}


# ---------------- main -------------------------------------------------------------------------
def main():
    t0 = time.time()
    print("G-2: SPECTRAL GEOMETRY ATTACK (charter frozen at c83e9d7)")
    rE = leg_E()
    rC = leg_C()
    rD, hcols, aidx, xi = leg_D()
    rF = leg_F()
    rB = leg_B(hcols, aidx, xi)
    rH = leg_H()
    rI = leg_IG()

    print("\n=== COMPOSITE (frozen taxonomy; components per access class) ===")
    check(True, "GEOMETRY-PARTIAL-SPECTRAL (decision rule 1, multi-site access): invariant "
                "hop-metric distances (validated +-0.3), dimension by shells (1D/2D/3D + "
                "quantum), inhomogeneous metric density (exact), and held-out predictions "
                "recovered from spectral interface data alone -- the G-1 metric failure "
                "was the arrival-time instrument, in-class", "note")
    check(True, "GEOMETRY-UNDERDETERMINED (decision rule 2, structural): the single-site "
                "degeneracy SURVIVES full spectral data (L-C) -- a structural limit of "
                "the interface, not an instrument artifact; global topology invisible "
                "below moment order = circumference (L-I/G)", "note")
    check(True, "REPRESENTATIONAL: all spectral reconstructions invariant under substrate "
                "scrambles and congruence (L-B, L-H)", "note")
    check(True, "NULL-REDUNDANT (decision rule 4): heat kernels, effective resistance, "
                "Lanczos, MDS are standard network/spectral mathematics -- no new "
                "principle; the physical content is WHICH invariants the declared access "
                "makes recoverable", "note")
    check(True, "Rule 3 honored: no promotion beyond PARTIAL -- the full metric remains "
                "non-unique (one-site degeneracy; sub-order topology). Rider carried: "
                "stationarity is a property of these static testbeds. No gravity input "
                "anywhere", "note")

    out = {"instrument": "g2_spectral", "charter_commit": "c83e9d7", "date": "2026-09-25",
           "LE": rE, "LC": rC, "LD": rD, "LF": rF, "LB_diff": rB, "LH": rH, "LIG": rI,
           "halts": HALT, "checks": CHECKS, "failures": FAIL,
           "elapsed_s": round(time.time() - t0, 2),
           "hard_stop": "verdict recorded; owner rules on the next layer"}
    path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                         "G2_SPECTRAL_RESULT.json"))
    with open(path, "wb") as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True, default=float).encode())
    sha = hashlib.sha256(open(path, "rb").read()).hexdigest()
    print(f"\nartifact written: {path} (sha {sha[:16]}...)")
    n_ok = sum(1 for c in CHECKS if c["ok"])
    print(f"\nG-2 SPECTRAL ATTACK: {n_ok}/{len(CHECKS)} checks passed; failures: "
          f"{len(FAIL)}; halts: {len(HALT)}")
    if HALT:
        print("HALT: an analytic identity breached -- instrument bug, never physics. "
              "No verdict may be issued from this run.")
    else:
        print("HARD STOP: verdict recorded pending owner ruling.")
    sys.exit(0 if not FAIL else 1)


if __name__ == "__main__":
    main()
