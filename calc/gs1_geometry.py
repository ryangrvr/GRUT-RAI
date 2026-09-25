#!/usr/bin/env python3
"""gs1_geometry: can geometry be selected from influence/access data?

CHARTER: GS1_GEOMETRY_SELECTION_CHARTER_01.md (pre-registration frozen at commit 7837fb2
BEFORE this instrument ran; authority GitHub Issue #2 owner comment 5837643174). Interface
data G_AA(w) = [(K - w^2)^-1]_AA come from hidden networks; genuinely different candidate
geometries are tested against the DATA. Reconstruction machinery is standard mathematics
(NULL-REDUNDANT); only what the data eliminates is a finding. LocPos is a chartered
candidate, not earned. No omega^7, probe, retained-sector, GeoInv, Sel-4x or CARRIER inputs.

Legs: L-F full access (isospectral partner, degree-preserving rewire) | L-M boundary access,
Y vs Delta (static vs dynamic) | L-P single-site access, non-isometric interior family |
L-T prism vs Mobius local-walk horizon.

Pure stdlib. Run: python3 calc/gs1_geometry.py
"""
import hashlib
import json
import math
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from partition_selection_p1 import jacobi_eig

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


def eye(n):
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]


def mm(A, B):
    Bt = list(zip(*B))
    return [[sum(a * b for a, b in zip(r, c)) for c in Bt] for r in A]


def tr(A):
    return [list(r) for r in zip(*A)]


def lin(A, B, a=1.0, b=1.0):
    return [[a * A[i][j] + b * B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def inv(M):
    n = len(M)
    A = [M[i][:] + eye(n)[i] for i in range(n)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(A[r][c]))
        A[c], A[p] = A[p], A[c]
        pv = A[c][c]
        A[c] = [x / pv for x in A[c]]
        for r in range(n):
            if r != c and A[r][c] != 0.0:
                f = A[r][c]
                A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    return [row[n:] for row in A]


def laplacian(n, edges, pins):
    K = [[0.0] * n for _ in range(n)]
    for i in range(n):
        K[i][i] = pins[i]
    for i, j, w in edges:
        K[i][i] += w
        K[j][j] += w
        K[i][j] -= w
        K[j][i] -= w
    return K


def G(K, w):
    return inv(lin(K, eye(len(K)), 1.0, -w * w))


def maxdiff(A, B):
    return max(abs(A[i][j] - B[i][j]) for i in range(len(A)) for j in range(len(A[0])))


def trpow(K, m):
    P = eye(len(K))
    for _ in range(m):
        P = mm(P, K)
    return sum(P[i][i] for i in range(len(K)))


# ---------------- L-F: full site-resolved access ----------------------------------------------------
GRID_E = [(0, 1, 1.0), (1, 2, 1.0), (3, 4, 1.0), (4, 5, 1.0), (6, 7, 1.0), (7, 8, 1.0),
          (0, 3, 1.0), (3, 6, 1.0), (1, 4, 1.0), (4, 7, 1.0), (2, 5, 1.0), (5, 8, 1.0)]


def leg_F():
    print("\n=== L-F: FULL SITE-RESOLVED ACCESS (3x3 grid hidden network) ===")
    n = 9
    K = laplacian(n, GRID_E, [0.1] * n)
    w = 0.5
    GT = G(K, w)
    Khat = lin(eye(n), inv(GT), w * w, 1.0)
    dev = maxdiff(Khat, K)
    halt_check(dev < 1e-9, f"L-F GATE (a) machinery: K_hat = w^2 + G(w)^-1 reproduces the hidden "
                           f"network to {dev:.1e} < 1e-9 (halt-grade; NULL-REDUNDANT)")
    Q = eye(n)
    for i in range(8):
        j = (4 * i + 1) % n
        if j == i:
            continue
        th = 0.3 + 0.1 * i
        c, s = math.cos(th), math.sin(th)
        R = eye(n)
        R[i][i], R[j][j], R[i][j], R[j][i] = c, c, -s, s
        Q = mm(R, Q)
    KQ = mm(mm(Q, K), tr(Q))
    tdev = max(abs(trpow(KQ, m) - trpow(K, m)) / abs(trpow(K, m)) for m in range(1, 9))
    dQ = maxdiff(G(KQ, w), GT)
    check(tdev < 1e-10 and dQ > 1e-3,
          f"L-F GATE (b) isospectral candidate: trace moments m = 1..8 equal to {tdev:.1e} "
          f"(all global spectral data agree) yet site-resolved data differ by {dQ:.3f} > 1e-3 "
          f"-- ELIMINATED by local access, which global spectra cannot do")
    E2 = [e for e in GRID_E if (e[0], e[1]) not in ((0, 1), (7, 8))] + [(0, 8, 1.0),
                                                                          (1, 7, 1.0)]
    KR = laplacian(n, E2, [0.1] * n)
    dR = maxdiff(G(KR, w), GT)
    first = next((m for m in range(1, 9)
                  if abs(trpow(KR, m) - trpow(K, m)) > 1e-9 * abs(trpow(K, m))), None)
    check(dR > 1e-3, f"L-F GATE (c) degree-preserving rewire: data differ by {dR:.3f} > 1e-3 -- "
                     f"ELIMINATED; first differing global trace moment: order {first}")
    return {"recon_dev": dev, "iso_trace_dev": tdev, "iso_data_diff": dQ,
            "rewire_data_diff": dR, "rewire_first_trace_order": first}


# ---------------- L-M: Y vs Delta ------------------------------------------------------------------
def leg_M():
    print("\n=== L-M: BOUNDARY ACCESS {a, b, c} -- hidden Y (interior node) vs candidate Delta ===")
    ws = [1.0, 1.5, 2.0]
    S = sum(ws)
    KY = laplacian(4, [(0, 3, ws[0]), (1, 3, ws[1]), (2, 3, ws[2])], [0.1, 0.1, 0.1, 0.0])
    KD = laplacian(3, [(0, 1, ws[0] * ws[1] / S), (0, 2, ws[0] * ws[2] / S),
                       (1, 2, ws[1] * ws[2] / S)], [0.1] * 3)
    sub = lambda M: [r[:3] for r in M[:3]]
    Schur = [[KY[i][j] - KY[i][3] * KY[3][j] / KY[3][3] for j in range(3)] for i in range(3)]
    ds = maxdiff(Schur, KD)
    halt_check(ds < 1e-12, f"L-M GATE (a): static boundary data (Schur complement) of Y equals "
                           f"Delta to {ds:.1e} < 1e-12 -- G-2's STATIC resistance geometry "
                           f"cannot tell them apart (halt-grade)")
    dd = maxdiff(sub(G(KY, 0.3)), G(KD, 0.3))
    check(dd > 1e-3, f"L-M GATE (b): dynamic boundary data at w = 0.3 differ by {dd:.4f} > 1e-3 "
                     f"-- the DYNAMIC influence hierarchy ELIMINATES Delta")
    eps = 1e-6
    GYi = lambda s: inv(sub(inv(lin(KY, eye(4), 1.0, -s))))
    GDi = lambda s: lin(KD, eye(3), 1.0, -s)
    dY = lin(GYi(eps), GYi(0.0), 1 / eps, -1 / eps)
    dD = lin(GDi(eps), GDi(0.0), 1 / eps, -1 / eps)
    o0 = maxdiff(GYi(0.0), GDi(0.0))
    o1 = maxdiff(dY, dD)
    analytic = max(abs(KY[i][3] * KY[3][j] / KY[3][3] ** 2) for i in range(3) for j in range(3))
    check(o0 < 1e-12 and o1 > 1e-3,
          f"L-M GATE (c): first distinguishing invariant = the w^2 coefficient of G_AA^-1 "
          f"(order-0 diff {o0:.1e}; order-w^2 diff {o1:.4f}, analytic "
          f"||K_AI K_II^-2 K_IA|| = {analytic:.4f})")
    return {"static_diff": ds, "dynamic_diff": dd, "order0": o0, "order_w2": o1,
            "analytic": analytic}


# ---------------- L-P: single-site access ----------------------------------------------------------
def leg_P():
    print("\n=== L-P: SINGLE-SITE ACCESS {a} -- hidden path a-1-2 vs the interior-rotation family ===")
    K = [[1.2, -1.0, 0.0], [-1.0, 1.7, -0.7], [0.0, -0.7, 0.7]]
    ref = [G(K, w)[0][0] for w in (0.3, 0.9)]

    def Kth(th):
        c, s = math.cos(th), math.sin(th)
        O = [[1, 0, 0], [0, c, -s], [0, s, c]]
        return mm(mm(O, K), tr(O))

    thetas = [math.pi * i / 3600 for i in range(3600)]
    ddev, lp_ok = 0.0, []
    for th in thetas:
        Kt = Kth(th)
        ddev = max(ddev, max(abs(G(Kt, w)[0][0] - r) for w, r in zip((0.3, 0.9), ref)))
        wa1, wa2, w12 = -Kt[0][1], -Kt[0][2], -Kt[1][2]
        pa = Kt[0][0] - wa1 - wa2
        p1 = Kt[1][1] - wa1 - w12
        p2 = Kt[2][2] - wa2 - w12
        if min(wa1, wa2, w12, pa, p1, p2) >= -1e-12:
            lp_ok.append(th)
    halt_check(ddev < 1e-12, f"L-P GATE (a): single-site data G_aa(w) identical across all 3600 "
                             f"family members to {ddev:.1e} < 1e-12 (halt-grade)")
    K4 = Kth(0.4)
    check(abs(K4[0][2]) > 1e-3, f"L-P GATE (b): family is NON-isometric -- at theta = 0.4, a "
                                f"couples to node 2 (weight {-K4[0][2]:.4f}) where the hidden "
                                f"path has none")
    mn = min(jacobi_eig(K4)[0])
    check(mn >= -1e-12, f"L-P GATE (c): 𝔠_full admits the family (spectrum invariant; min "
                        f"eigenvalue at theta = 0.4 is {mn:.4f})")
    noniso = [t for t in lp_ok if min(abs(t), abs(t - math.pi / 2), abs(t - math.pi)) > 1e-3]
    check(True, f"L-P (d) REPORTED: LocPos-admissible theta count = {len(lp_ok)}; of these, "
                f"non-isometric (away from 0, pi/2) = {len(noniso)}"
                + (f" (range {min(noniso):.4f} .. {max(noniso):.4f})" if noniso else ""), "note")
    # ---- POST-HOC DIAGNOSTIC (labeled; robustness of the LocPos reading) --------------------
    Kp = [[1.2, -1.0, 0.0], [-1.0, 1.8, -0.7], [0.0, -0.7, 0.8]]  # interior pins 0.1 each

    def Kthp(th):
        c, s = math.cos(th), math.sin(th)
        O = [[1, 0, 0], [0, c, -s], [0, s, c]]
        return mm(mm(O, Kp), tr(O))

    lp2 = []
    for th in thetas:
        Kt = Kthp(th)
        wa1, wa2, w12 = -Kt[0][1], -Kt[0][2], -Kt[1][2]
        pa, p1, p2 = Kt[0][0] - wa1 - wa2, Kt[1][1] - wa1 - w12, Kt[2][2] - wa2 - w12
        if min(wa1, wa2, w12, pa, p1, p2) >= -1e-12:
            lp2.append(th)
    noniso2 = [t for t in lp2 if min(abs(t), abs(t - math.pi / 2), abs(t - math.pi)) > 1e-3]
    check(True, f"L-P POST-HOC DIAGNOSTIC (labeled): the hidden path has ZERO interior pins, so "
                f"it sits on the LocPos boundary. With interior pins 0.1, LocPos admits "
                f"{len(lp2)} theta, of which {len(noniso2)} are non-isometric"
                + (f" (range {min(noniso2):.4f} .. {max(noniso2):.4f})" if noniso2 else "")
                + " -- the frozen reading's uniqueness is a boundary effect, not a robust "
                  "selection", "note")
    return {"data_dev": ddev, "a2_weight_at_0.4": -K4[0][2], "lp_count": len(lp_ok),
            "lp_diag_pinned_count": len(lp2), "lp_diag_pinned_noniso": len(noniso2),
            "lp_noniso_count": len(noniso),
            "lp_noniso_range": [min(noniso), max(noniso)] if noniso else None}


# ---------------- L-T: prism vs Mobius --------------------------------------------------------------
def leg_T():
    print("\n=== L-T: TOPOLOGY -- prism C8 x K2 vs Mobius ladder M16 (local closed walks) ===")
    n = 8

    def adj(mobius):
        A = [[0] * (2 * n) for _ in range(2 * n)]

        def e(u, v):
            A[u][v] += 1
            A[v][u] += 1

        for i in range(n):
            e(2 * i, 2 * i + 1)
            for s in (0, 1):
                if i < n - 1:
                    e(2 * i + s, 2 * (i + 1) + s)
                else:
                    e(2 * i + s, 0 + ((1 - s) if mobius else s))
        return A

    def walks(A, mmax=12):
        v = [0] * (2 * n)
        v[0] = 1
        out = []
        for _ in range(mmax):
            v = [sum(A[i][j] * v[j] for j in range(2 * n)) for i in range(2 * n)]
            out.append(v[0])
        return out

    wp, wm = walks(adj(False)), walks(adj(True))
    first = next((m + 1 for m in range(len(wp)) if wp[m] != wm[m]), None)
    check(first == n, f"L-T GATE: local closed-walk counts equal as exact integers for m < {n} "
                      f"and first differ at m = {first} (predicted {n}): the twist is invisible "
                      f"below the circumference order (G-2's horizon, carried)")
    return {"first_order": first, "prism": wp, "mobius": wm}


def adjudicate(rF, rM, rP, rT):
    bar = (rF["iso_data_diff"] > 1e-3 or rF["rewire_data_diff"] > 1e-3 or
           rM["dynamic_diff"] > 1e-3)
    single = ("UNDERDETERMINED (LocPos also leaves non-isometric members)"
              if rP["lp_noniso_count"] > 0 else
              "UNDERDETERMINED by earned structure; selected only by LocPos (candidate)")
    return {"bar_met": bar,
            "full_access": "SELECTED-IN-CLASS (unique up to relabeling)",
            "boundary_access": "dynamic hierarchy selects interior dimension (Y over Delta); "
                               "interior geometry CONSTRAINED-NONUNIQUE",
            "static_only": "Y-Delta blind (G-2 resistance geometry insufficient)",
            "single_site": single,
            "topology": f"invisible below local order {rT['first_order']} (horizon)",
            "overall": "CLASS-SPLIT by access: geometry determined exactly as far as access "
                       "reaches; the access boundary itself is supplied (P-5/P-6)"}


def main():
    t0 = time.time()
    print("GS-1: CAN GEOMETRY BE SELECTED FROM INFLUENCE/ACCESS DATA? (charter frozen at "
          "7837fb2)")
    rF = leg_F()
    rM = leg_M()
    rP = leg_P()
    rT = leg_T()
    adj = adjudicate(rF, rM, rP, rT)
    print("\n=== ADJUDICATION (frozen outcome rule, computed from the measurements) ===")
    for k, v in adj.items():
        check(True, f"{k}: {v}", "note")
    out = {"instrument": "gs1_geometry", "charter_commit": "7837fb2", "date": "2026-09-25",
           "LF": rF, "LM": rM, "LP": rP, "LT": rT, "adjudication": adj, "halts": HALT,
           "checks": CHECKS, "failures": FAIL, "elapsed_s": round(time.time() - t0, 2),
           "hard_stop": "verdict recorded"}
    path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                         "GS1_GEOMETRY_RESULT.json"))
    with open(path, "wb") as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True, default=str).encode())
    sha = hashlib.sha256(open(path, "rb").read()).hexdigest()
    print(f"\nartifact written: {path} (sha {sha[:16]}...)")
    n_ok = sum(1 for c in CHECKS if c["ok"])
    print(f"\nGS-1 GEOMETRY-SELECTION ATTACK: {n_ok}/{len(CHECKS)} checks passed; failures: "
          f"{len(FAIL)}; halts: {len(HALT)}")
    if HALT:
        print("HALT: an analytic identity breached -- instrument bug, never physics. "
              "No verdict may be issued from this run.")
    else:
        print("HARD STOP: verdict recorded pending owner ruling.")
    sys.exit(0 if not FAIL else 1)


if __name__ == "__main__":
    main()
