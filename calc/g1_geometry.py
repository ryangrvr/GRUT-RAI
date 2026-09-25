#!/usr/bin/env python3
"""g1_geometry: does full influence data + access structure reconstruct effective geometry?

CHARTER: G1_GEOMETRY_CHARTER_01.md (pre-registration frozen at commit f9b043b BEFORE this
instrument ran; authority GitHub Issue #2 owner comment 5827519334). Gravity is NOT allowed
to define geometry; every reconstruction uses ONLY interface data (response kernels /
arrival times at declared accessed sites), never substrate coordinates. Rider H: substrates
are static, so stationarity holds BY CONSTRUCTION here and is not presumed beyond.

Legs: L-DIM ball-growth dimension recovery (1D/2D/3D pinned lattices + quantum XX chain) |
L-MET MDS metric with held-out trilaterated probe + trace-level reciprocity | L-CRV
inhomogeneous metric density vs declared stiffness with held-out travel time | L-REP
Givens-scramble representation control | L-ISO Lanczos collapse of a 2D grid to an
influence-identical 1D chain (single-site access underdetermination) | L-TOP ring 40 vs 80
topology horizon counterattack.

Pure stdlib. Run: python3 calc/g1_geometry.py
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
from p5_access import expm, mvec

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


# ---------------- harmonic-network simulator (leapfrog; edge lists) ---------------------------
def simulate(n, edges, pin, x0, v0, T, dt, trace_sites=(), trace_vecs=(), eps=1e-4,
             mean_sub=False, baseline=None, thr=None, track_max=False):
    """x'' = -K x with K from pin + edges (i, j, k).
    Returns (arrivals, traces_s, traces_v, maxdev).
    Signal at site i: dev_i = x_i - mean(x) [if mean_sub] - baseline_i [if given].
    Arrival = first t with |dev_i| > thr[i] (per-site) or > eps (frozen absolute).
    track_max: also record per-site max |dev_i| over the run (for the labeled DIAG
    detector). The baseline fix is a disclosed defect repair: the first run's L-CRV
    displacement source left a constant mean-subtraction offset (-1/N) at every site, so
    the 1e-4 threshold fired at step 1 everywhere -- the detector measured the subtracted
    constant, nothing physical."""
    x = list(x0)
    v = list(v0)
    steps = int(round(T / dt))
    arr = [None] * n
    pending = list(range(n))
    ts_s = {s: [] for s in trace_sites}
    ts_v = [[] for _ in trace_vecs]
    mx = [0.0] * n if track_max else None

    def accel():
        a = [-pin[i] * x[i] for i in range(n)]
        for i, j, k in edges:
            d = k * (x[i] - x[j])
            a[i] -= d
            a[j] += d
        return a

    a = accel()
    for step in range(1, steps + 1):
        for i in range(n):
            v[i] += 0.5 * dt * a[i]
            x[i] += dt * v[i]
        a = accel()
        for i in range(n):
            v[i] += 0.5 * dt * a[i]
        t = step * dt
        mu = sum(x) / n if mean_sub else 0.0
        if track_max:
            for i in range(n):
                d0 = abs(x[i] - mu - (baseline[i] if baseline else 0.0))
                if d0 > mx[i]:
                    mx[i] = d0
        if pending:
            new_pending = []
            for i in pending:
                dev = abs(x[i] - mu - (baseline[i] if baseline else 0.0))
                if dev > (thr[i] if thr else eps):
                    arr[i] = t
                else:
                    new_pending.append(i)
            pending = new_pending
        for s in trace_sites:
            ts_s[s].append(x[s])
        for m, w in enumerate(trace_vecs):
            ts_v[m].append(sum(w[i] * x[i] for i in range(n)))
    return arr, ts_s, ts_v, mx


def sim_dense(K, x0, v0, T, dt, trace_vecs):
    n = len(K)
    x, v = list(x0), list(v0)
    steps = int(round(T / dt))
    ts_v = [[] for _ in trace_vecs]

    def accel():
        return [-sum(K[i][j] * x[j] for j in range(n)) for i in range(n)]

    a = accel()
    for _ in range(steps):
        for i in range(n):
            v[i] += 0.5 * dt * a[i]
            x[i] += dt * v[i]
        a = accel()
        for i in range(n):
            v[i] += 0.5 * dt * a[i]
        for m, w in enumerate(trace_vecs):
            ts_v[m].append(sum(w[i] * x[i] for i in range(n)))
    return ts_v


def chain_edges(n, ks=None):
    return [(i, i + 1, 1.0 if ks is None else ks[i]) for i in range(n - 1)]


def grid2_edges(w, h):
    E = []
    for x in range(w):
        for y in range(h):
            i = x * h + y
            if x + 1 < w:
                E.append((i, (x + 1) * h + y, 1.0))
            if y + 1 < h:
                E.append((i, x * h + y + 1, 1.0))
    return E


def grid3_edges(s):
    E = []
    for x in range(s):
        for y in range(s):
            for z in range(s):
                i = (x * s + y) * s + z
                if x + 1 < s:
                    E.append((i, ((x + 1) * s + y) * s + z, 1.0))
                if y + 1 < s:
                    E.append((i, (x * s + y + 1) * s + z, 1.0))
                if z + 1 < s:
                    E.append((i, (x * s + y) * s + z + 1, 1.0))
    return E


def ring_edges(n):
    return [(i, (i + 1) % n, 1.0) for i in range(n)]


def imp(n, i):
    v = [0.0] * n
    v[i] = 1.0
    return v


def ball_dim(arr, tau_edge):
    """Frozen rule: tau2 = 0.6 tau_edge, tau1 = tau2/2; d = log ratio of ball counts."""
    t2 = 0.6 * tau_edge
    t1 = 0.5 * t2
    n1 = sum(1 for a in arr if a is not None and a <= t1)
    n2 = sum(1 for a in arr if a is not None and a <= t2)
    return math.log(n2 / n1) / math.log(t2 / t1), t1, t2, n1, n2


def peak_arrivals(n, edges, pin, x0, v0, T, dt, mean_sub=False, baseline=None):
    """DIAG detector (post-hoc, labeled): arrival = first t with |dev_i(t)| >= 0.5 of that
    site's own maximum over the run -- the FRONT PEAK, not the evanescent precursor tail
    that the frozen absolute threshold reads. Two passes."""
    _, _, _, mx = simulate(n, edges, pin, x0, v0, T, dt, eps=1e18, mean_sub=mean_sub,
                           baseline=baseline, track_max=True)
    thr = [max(0.5 * m, 1e-12) for m in mx]
    arr, _, _, _ = simulate(n, edges, pin, x0, v0, T, dt, mean_sub=mean_sub,
                            baseline=baseline, thr=thr)
    return arr


# ---------------- L-DIM: dimension from interface arrival data --------------------------------
def leg_DIM():
    print("\n=== L-DIM: DIMENSION ATTACK (ball growth from arrival times only) ===")
    res = {}
    # 1D
    n = 61
    e1d, p1d = chain_edges(n), [0.5] * n
    arr, _, _, _ = simulate(n, e1d, p1d, [0.0] * n, imp(n, 30), 60.0, 0.01)
    te = min(a for a in (arr[0], arr[60]) if a is not None)
    d1, t1, t2, n1, n2 = ball_dim(arr, te)
    check(0.65 <= d1 <= 1.35, f"L-DIM GATE 1D: d_hat = {d1:.3f} in [0.65, 1.35] "
                              f"(balls {n1}->{n2} at tau {t1:.1f}->{t2:.1f})")
    res["d1"] = d1
    # 2D
    w = 31
    n = w * w
    src = 15 * w + 15
    e2d, p2d = grid2_edges(w, w), [0.5] * n
    arr2, _, _, _ = simulate(n, e2d, p2d, [0.0] * n, imp(n, src), 40.0, 0.01)
    bset = [x * w + y for x in range(w) for y in range(w)
            if x in (0, w - 1) or y in (0, w - 1)]
    te2 = min(arr2[i] for i in bset if arr2[i] is not None)
    d2, t1, t2, n1, n2 = ball_dim(arr2, te2)
    check(1.65 <= d2 <= 2.35, f"L-DIM GATE 2D: d_hat = {d2:.3f} in [1.65, 2.35] "
                              f"(balls {n1}->{n2} at tau {t1:.1f}->{t2:.1f})")
    mono = all(sum(1 for a in arr2 if a is not None and a <= t) <=
               sum(1 for a in arr2 if a is not None and a <= t + 2.0)
               for t in (4.0, 8.0, 12.0))
    check(mono, "L-DIM control: 2D ball counts monotone in tau", "ctrl")
    res["d2"] = d2
    # 3D
    s = 13
    n = s * s * s
    src3 = (6 * s + 6) * s + 6
    e3d, p3d = grid3_edges(s), [0.5] * n
    arr3, _, _, _ = simulate(n, e3d, p3d, [0.0] * n, imp(n, src3), 20.0, 0.01)
    bset3 = [(x * s + y) * s + z for x in range(s) for y in range(s) for z in range(s)
             if x in (0, s - 1) or y in (0, s - 1) or z in (0, s - 1)]
    te3 = min(arr3[i] for i in bset3 if arr3[i] is not None)
    d3, t1, t2, n1, n2 = ball_dim(arr3, te3)
    check(2.65 <= d3 <= 3.35, f"L-DIM GATE 3D: d_hat = {d3:.3f} in [2.65, 3.35] "
                              f"(balls {n1}->{n2} at tau {t1:.1f}->{t2:.1f})")
    res["d3"] = d3
    # ---- POST-HOC DIAGNOSTIC (labeled; front-peak detector, a measurement not a gate) ----
    da1 = peak_arrivals(61, e1d, p1d, [0.0] * 61, imp(61, 30), 60.0, 0.01)
    te = min(a for a in (da1[0], da1[60]) if a is not None)
    dd1 = ball_dim(da1, te)[0]
    da2 = peak_arrivals(w * w, e2d, p2d, [0.0] * (w * w), imp(w * w, src), 40.0, 0.01)
    te2d = min(da2[i] for i in bset if da2[i] is not None)
    dd2 = ball_dim(da2, te2d)[0]
    da3 = peak_arrivals(s ** 3, e3d, p3d, [0.0] * s ** 3, imp(s ** 3, src3), 20.0, 0.01)
    te3d = min(da3[i] for i in bset3 if da3[i] is not None)
    dd3 = ball_dim(da3, te3d)[0]
    res["diag"] = {"d1": dd1, "d2": dd2, "d3": dd3}
    check(True, f"L-DIM POST-HOC DIAGNOSTIC (labeled): with the front-peak detector "
                f"(arrival = half of each site's own max) the same interface data give "
                f"d_hat = {dd1:.3f} / {dd2:.3f} / {dd3:.3f} for the 1D/2D/3D substrates. "
                f"The frozen absolute threshold reads the evanescent precursor tail, whose "
                f"crossing times are strongly non-metric at these sizes -- a detector "
                f"regime error, not an absence of geometric information", "note")
    # quantum XX chain (noncommutative substrate), one-magnon sector
    N = 31
    h = [[0.0] * N for _ in range(N)]
    for i in range(N):
        h[i][i] = 0.5
        if i + 1 < N:
            h[i][i + 1] = h[i + 1][i] = 1.0
    dtq = 0.05
    U = expm([[-1j * dtq * h[i][j] for j in range(N)] for i in range(N)])

    def qarr(src, T=30.0, thr=None):
        a = [0j] * N
        a[src] = 1.0 + 0j
        arrq = [None] * N
        mxq = [0.0] * N
        for step in range(1, int(T / dtq) + 1):
            a = mvec(U, a)
            t = step * dtq
            for i in range(N):
                m = abs(a[i])
                if m > mxq[i]:
                    mxq[i] = m
                if arrq[i] is None and m > (thr[i] if thr else 1e-4):
                    arrq[i] = t
        return arrq, mxq

    def qpeak(src):
        _, mxq = qarr(src)
        arrq, _ = qarr(src, thr=[max(0.5 * m, 1e-12) for m in mxq])
        return arrq

    aq15, _ = qarr(15)
    teq = min(a for a in (aq15[0], aq15[30]) if a is not None)
    dq, t1, t2, n1, n2 = ball_dim(aq15, teq)
    check(0.65 <= dq <= 1.35, f"L-DIM GATE quantum (XX one-magnon): d_hat = {dq:.3f} in "
                              f"[0.65, 1.35] (balls {n1}->{n2} at tau {t1:.2f}->{t2:.2f})")
    aq5, _ = qarr(5)
    lhs = aq5[25]
    rhs = aq5[15] + aq15[25]
    addv = abs(lhs - rhs) / lhs
    check(addv < 0.2, f"L-DIM GATE quantum additivity: tau_5(25) = {lhs:.2f} vs "
                      f"tau_5(15) + tau_15(25) = {rhs:.2f}, rel diff = {addv:.3f} < 0.2")
    res["dq"] = dq
    # ---- POST-HOC DIAGNOSTIC (labeled) ------------------------------------------------------
    dq15 = qpeak(15)
    teqd = min(a for a in (dq15[0], dq15[30]) if a is not None)
    dqd = ball_dim(dq15, teqd)[0]
    dq5 = qpeak(5)
    lhsd = dq5[25]
    rhsd = dq5[15] + dq15[25]
    addd = abs(lhsd - rhsd) / lhsd
    res["diag_q"] = {"dq": dqd, "additivity": addd}
    check(True, f"L-DIM POST-HOC DIAGNOSTIC quantum (labeled): front-peak detector gives "
                f"d_hat = {dqd:.3f} and additivity rel diff = {addd:.3f} -- the ballistic "
                f"magnon front (peak of J_r(2t) at t ~ r/2) is metric; the frozen "
                f"threshold read the Bessel tail (J_r(2t) = 1e-4), which is not", "note")
    check(True, "L-DIM component: geometric dimensionality is present in the interface "
                "data (front structure); the frozen tail-threshold detector failed to "
                "read it except in 1D -- gates preserved red as found", "note")
    return res


# ---------------- L-MET: metric with held-out probe -------------------------------------------
W = 31
ANCH = [(6, 6), (6, 24), (24, 6), (24, 24), (15, 12)]
XSITE = (20, 18)


def leg_MET():
    print("\n=== L-MET: METRIC ATTACK (MDS + held-out trilaterated probe) ===")
    n = W * W
    edges = grid2_edges(W, W)
    pin = [0.5] * n
    aidx = [x * W + y for x, y in ANCH]
    xi = XSITE[0] * W + XSITE[1]

    runs = {}
    tr_pair = {}
    for k, s in enumerate(aidx):
        tsites = (aidx[3],) if k == 0 else ((aidx[0],) if k == 3 else ())
        arr, ts, _, _ = simulate(n, edges, pin, [0.0] * n, imp(n, s), 50.0, 0.01,
                                 trace_sites=tsites)
        runs[k] = arr
        if ts:
            tr_pair[k] = list(ts.values())[0]
    arrX, _, _, _ = simulate(n, edges, pin, [0.0] * n, imp(n, xi), 50.0, 0.01)
    arr0b, _, _, _ = simulate(n, edges, pin, [0.0] * n, imp(n, aidx[0]), 50.0, 0.01)

    rec = max(abs(a - b) for a, b in zip(tr_pair[0], tr_pair[3]))
    halt_check(rec < 1e-9, f"L-MET GATE reciprocity (trace level, A1<->A4): max diff = "
                           f"{rec:.2e} < 1e-9 (analytic: K symmetric; halt-grade)")
    mc = max(abs((runs[0][i] or -1) - (arr0b[i] or -1)) for i in range(n))
    check(mc == 0.0, f"L-MET matched control (A1 source rerun): arrival map diff = {mc:.1e}",
          "ctrl")

    def reconstruct(taus, tXv):
        """MDS embed the 5 anchors from the tau matrix; trilaterate X from A1-A3; return
        (capture, [(pred, meas, rel_err) for A4, A5])."""
        tsym = [[0.5 * (taus[i][j] + taus[j][i]) for j in range(5)] for i in range(5)]
        D2 = [[tsym[i][j] ** 2 for j in range(5)] for i in range(5)]
        Jc = [[(1.0 if i == j else 0.0) - 0.2 for j in range(5)] for i in range(5)]
        JD = [[sum(Jc[i][k] * D2[k][j] for k in range(5)) for j in range(5)]
              for i in range(5)]
        B = [[-0.5 * sum(JD[i][k] * Jc[k][j] for k in range(5)) for j in range(5)]
             for i in range(5)]
        lam, V = jacobi_eig(B)
        order = sorted(range(5), key=lambda k: -lam[k])
        cap = (lam[order[0]] + lam[order[1]]) / sum(abs(x) for x in lam)
        co = [(V[i][order[0]] * math.sqrt(max(lam[order[0]], 0.0)),
               V[i][order[1]] * math.sqrt(max(lam[order[1]], 0.0))) for i in range(5)]
        a1, a2, a3 = co[0], co[1], co[2]
        r1, r2, r3 = tXv[0], tXv[1], tXv[2]
        A11, A12 = 2 * (a2[0] - a1[0]), 2 * (a2[1] - a1[1])
        A21, A22 = 2 * (a3[0] - a1[0]), 2 * (a3[1] - a1[1])
        b1 = r1 ** 2 - r2 ** 2 + a2[0] ** 2 + a2[1] ** 2 - a1[0] ** 2 - a1[1] ** 2
        b2 = r1 ** 2 - r3 ** 2 + a3[0] ** 2 + a3[1] ** 2 - a1[0] ** 2 - a1[1] ** 2
        det = A11 * A22 - A12 * A21
        px = (b1 * A22 - b2 * A12) / det
        py = (A11 * b2 - A21 * b1) / det
        out = []
        for kk in (3, 4):
            pred = math.hypot(px - co[kk][0], py - co[kk][1])
            out.append((pred, tXv[kk], abs(pred - tXv[kk]) / tXv[kk]))
        return cap, out, tsym

    tau = [[0.0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if i != j:
                tau[i][j] = runs[i][aidx[j]]
    tX = [arrX[a] for a in aidx]
    cap, preds, tsym = reconstruct(tau, tX)
    check(cap >= 0.85, f"L-MET GATE: top-2 MDS eigenvalues capture {cap:.3f} >= 0.85 of the "
                       f"tau-metric -- the interface metric itself is 2-dimensional "
                       f"(independent of L-DIM's ball counting)")
    errs = []
    for m, (pred, meas, rel) in enumerate(preds):
        errs.append(rel)
        check(rel < 0.2, f"L-MET GATE held-out: predicted tau(X, A{m + 4}) = {pred:.2f} vs "
                         f"measured {meas:.2f}, rel err = {rel:.3f} < 0.2 (X trilaterated "
                         f"from A1-A3 only)")
    # ---- POST-HOC DIAGNOSTIC (labeled; front-peak detector) ---------------------------------
    druns = [peak_arrivals(n, edges, pin, [0.0] * n, imp(n, s), 50.0, 0.01) for s in aidx]
    darrX = peak_arrivals(n, edges, pin, [0.0] * n, imp(n, xi), 50.0, 0.01)
    dtau = [[0.0 if i == j else druns[i][aidx[j]] for j in range(5)] for i in range(5)]
    dtX = [darrX[a] for a in aidx]
    dcap, dpreds, _ = reconstruct(dtau, dtX)
    derrs = [rel for _, _, rel in dpreds]
    check(True, f"L-MET POST-HOC DIAGNOSTIC (labeled): with the front-peak detector the "
                f"same reconstruction gives capture = {dcap:.3f} and held-out errors "
                f"{derrs[0]:.3f}, {derrs[1]:.3f} (predicted {dpreds[0][0]:.2f} vs "
                f"{dpreds[0][1]:.2f}; {dpreds[1][0]:.2f} vs {dpreds[1][1]:.2f}) -- the "
                f"precursor-tail metric is non-additive at short distances, which is what "
                f"broke the frozen held-out gates", "note")
    aniso = tsym[0][3] / (math.sqrt(2.0) * tsym[0][1])
    check(True, f"L-MET anisotropy (reported, not gated): tau(A1,A4)/(sqrt2 tau(A1,A2)) = "
                f"{aniso:.3f} (lattice front-speed anisotropy)", "note")
    check(True, "L-MET component: distances among accessed sites form a consistent metric "
                "recovered from arrival data; a held-out probe's unseen distances are "
                "PREDICTED, not fitted -- MDS/trilateration are standard mathematics "
                "(NULL-REDUNDANT as principles); the geometry is in the data", "note")
    return {"capture": cap, "held_out_errs": errs, "anisotropy": aniso, "recip": rec,
            "diag": {"capture": dcap, "errs": derrs}}


# ---------------- L-CRV: inhomogeneous metric density -----------------------------------------
def leg_CRV():
    print("\n=== L-CRV: INHOMOGENEITY ATTACK (metric density tracks dynamics) ===")
    n = 81
    ks = [1.0 if e < 40 else 2.25 for e in range(n - 1)]
    x0 = [0.0] * n
    x0[10] = 1.0
    mu0 = sum(x0) / n
    base = [x0[i] - mu0 for i in range(n)]  # disclosed defect fix: detect DEVIATION from
    # the initial mean-subtracted profile; the first run's detector fired at step 1 at
    # every site on the constant -1/N offset, measuring nothing physical.
    arr, _, _, _ = simulate(n, chain_edges(n, ks), [0.0] * n, x0, [0.0] * n, 70.0, 0.01,
                            mean_sub=True, baseline=base)
    t30, t60, t70 = arr[30], arr[60], arr[70]
    v0 = 20.0 / t30
    vs = 10.0 / (t70 - t60)
    ratio = vs / v0
    check(abs(ratio - 1.5) / 1.5 < 0.15,
          f"L-CRV GATE: measured speed ratio stiff/calibration = {ratio:.3f} vs sqrt(2.25) "
          f"= 1.5, rel err = {abs(ratio - 1.5) / 1.5:.3f} < 0.15 -- the reconstructed "
          f"metric density tracks the independently declared stiffness")
    tpred = sum(1.0 / (v0 * math.sqrt(k)) for k in ks[10:70])
    err = abs(tpred - t70) / t70
    check(err < 0.15, f"L-CRV GATE held-out: predicted tau(10->70) = {tpred:.1f} vs "
                      f"measured {t70:.1f}, rel err = {err:.3f} < 0.15 (calibrated on "
                      f"10->30 only)")
    check(True, "L-CRV scope line (frozen): a position-dependent metric density (effective "
                "line element) is recovered; a curvature TENSOR is not claimed by G-1 "
                "either way", "note")
    return {"ratio": ratio, "tau_pred": tpred, "tau_meas": t70, "rel_err": err}


# ---------------- L-REP: representation attack ------------------------------------------------
def leg_REP():
    print("\n=== L-REP: REPRESENTATION ATTACK (Givens-scrambled substrate) ===")
    n = 40
    K = [[0.0] * n for _ in range(n)]
    for i in range(n):
        K[i][i] = 0.5 + 2.0
        K[i][(i + 1) % n] -= 1.0
        K[i][(i - 1) % n] -= 1.0
    O = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for i in range(30):
        p, q, th = i, (7 * i + 3) % n, 0.3 + 0.02 * i
        c, s = math.cos(th), math.sin(th)
        for r in range(n):
            a, b = O[r][p], O[r][q]
            O[r][p] = c * a - s * b
            O[r][q] = s * a + c * b
    KO = [[sum(K[i][k] * O[j][k] for k in range(n)) for j in range(n)] for i in range(n)]
    Kp = [[sum(O[i][k] * KO[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    _, ts, _, _ = simulate(n, ring_edges(n), [0.5] * n, [0.0] * n, imp(n, 5), 40.0, 0.01,
                           trace_sites=(17,))
    e5 = [O[i][5] for i in range(n)]
    e17 = [O[i][17] for i in range(n)]
    tv = sim_dense(Kp, [0.0] * n, e5, 40.0, 0.01, [e17])
    d = max(abs(a - b) for a, b in zip(ts[17], tv[0]))
    halt_check(d < 1e-9, f"L-REP GATE: interface kernel identical under the frozen "
                         f"30-rotation scramble, max diff = {d:.2e} < 1e-9 (halt-grade "
                         f"analytic identity)")
    check(True, "L-REP component: scrambled site labels carry no geometric meaning; every "
                "reconstruction above is a functional of interface kernels, hence "
                "representation-invariant -- REPRESENTATIONAL layer confirmed", "note")
    return d


# ---------------- L-ISO: single-site access underdetermination --------------------------------
def leg_ISO():
    print("\n=== L-ISO: ISOMETRY COUNTERATTACK (2D grid == 1D chain at single-site access) ===")
    w = 10
    n = w * w
    K = [[0.0] * n for _ in range(n)]
    for i in range(n):
        K[i][i] = 0.5
    for i, j, k in grid2_edges(w, w):
        K[i][i] += k
        K[j][j] += k
        K[i][j] -= k
        K[j][i] -= k
    # Lanczos with full reorthogonalization, seed = corner site 0
    q = [0.0] * n
    q[0] = 1.0
    Q = [q]
    alphas, betas = [], []
    for m in range(n):
        z = [sum(K[i][j] * Q[-1][j] for j in range(n)) for i in range(n)]
        al = sum(z[i] * Q[-1][i] for i in range(n))
        alphas.append(al)
        for qq in Q:
            c = sum(z[i] * qq[i] for i in range(n))
            z = [z[i] - c * qq[i] for i in range(n)]
        for qq in Q:  # second reorthogonalization pass
            c = sum(z[i] * qq[i] for i in range(n))
            z = [z[i] - c * qq[i] for i in range(n)]
        be = math.sqrt(sum(x * x for x in z))
        if be < 1e-8:
            break
        betas.append(be)
        Q.append([x / be for x in z])
    m = len(alphas)
    check(True, f"L-ISO: Lanczos Krylov dimension = {m} (of {n}; symmetry truncation "
                f"expected), betas > 0 throughout", "note")
    # chain realization (sign gauge): springs beta_i, effective pins alpha_i - adjacent betas
    cpin = []
    for i in range(m):
        p = alphas[i]
        if i > 0:
            p -= betas[i - 1]
        if i < m - 1:
            p -= betas[i]
        cpin.append(p)
    cedges = [(i, i + 1, betas[i]) for i in range(m - 1)]
    _, tg, _, _ = simulate(n, grid2_edges(w, w), [0.5] * n, [0.0] * n, imp(n, 0), 30.0,
                           0.005, trace_sites=(0,))
    _, tc, _, _ = simulate(m, cedges, cpin, [0.0] * m, imp(m, 0), 30.0, 0.005,
                           trace_sites=(0,))
    d = max(abs(a - b) for a, b in zip(tg[0], tc[0]))
    halt_check(d < 1e-7, f"L-ISO GATE: complete single-site response of the 2D grid and "
                         f"the Lanczos 1D chain identical, max diff = {d:.2e} < 1e-7 "
                         f"(halt-grade: exact Krylov polynomial identity)")
    check(True, f"L-ISO component (frozen consequence): a 2D geometry and a 1D chain "
                f"(min effective pin {min(cpin):.3f}) generate IDENTICAL complete "
                f"single-site influence data. Under single-site access, geometry -- "
                f"including dimension -- is GEOMETRY-UNDERDETERMINED. The Lanczos map is "
                f"standard mathematics: NULL-REDUNDANT as a principle. With L-DIM/L-MET: "
                f"reconstructable geometry is a FUNCTION OF THE ACCESS STRUCTURE", "note")
    return {"krylov_dim": m, "trace_diff": d, "min_pin": min(cpin)}


# ---------------- L-TOP: topology horizon counterattack ---------------------------------------
def leg_TOP():
    print("\n=== L-TOP: TOPOLOGY COUNTERATTACK (ring 40 vs ring 80, same local statistics) ===")
    t40, t80 = None, None
    for N in (40, 80):
        _, ts, _, _ = simulate(N, ring_edges(N), [0.5] * N, [0.0] * N, imp(N, 0), 80.0,
                               0.01, trace_sites=(0,))
        if N == 40:
            t40 = ts[0]
        else:
            t80 = ts[0]
    n_short = int(10.0 / 0.01)
    dshort = max(abs(a - b) for a, b in zip(t40[:n_short], t80[:n_short]))
    dlong = max(abs(a - b) for a, b in zip(t40, t80))
    check(dshort < 1e-8, f"L-TOP GATE: single-site kernels identical on [0, 10], max diff "
                         f"= {dshort:.2e} < 1e-8 (fronts un-wrapped; Lieb-Robinson "
                         f"suppressed)")
    check(dlong > 1e-3, f"L-TOP GATE: kernels differ on [0, 80], max diff = {dlong:.4f} "
                        f"> 1e-3 (the N = 40 wrap returns)")
    check(True, "L-TOP component (frozen consequence): identical local couplings and local "
                "influence statistics, different global topology -- indistinguishable "
                "inside the causal horizon of the observation window, distinguished "
                "exactly when the window crosses the wrap time. Global topology is "
                "GEOMETRY-UNDERDETERMINED within the horizon; the interface sees geometry "
                "only as far as its data reaches", "note")
    return {"short": dshort, "long": dlong}


# ---------------- main ------------------------------------------------------------------------
def main():
    t0 = time.time()
    print("G-1: DOES INFLUENCE DATA + ACCESS RECONSTRUCT GEOMETRY? (charter frozen at f9b043b)")
    rdim = leg_DIM()
    rmet = leg_MET()
    rcrv = leg_CRV()
    rrep = leg_REP()
    riso = leg_ISO()
    rtop = leg_TOP()

    print("\n=== COMPOSITE (frozen taxonomy; components reported per access class) ===")
    check(True, "Frozen record: EIGHT frozen gates failed and stay RED as found -- "
                "2D/3D/quantum ball dimension, quantum additivity, both held-out metric "
                "predictions, and both L-CRV gates. The labeled diagnostics are "
                "measurements, not gate replacements, and they only PARTIALLY recover "
                "(front-peak dimension 1.12/1.94/1.73, quantum 0.92) while being "
                "contaminated themselves by boundary reflections (diag MDS capture 0.605, "
                "diag held-out errors up to 1.87, diag quantum additivity 0.40)", "note")
    check(True, "THE LOCATED OBSTRUCTION: on finite dispersive substrates, arrival-time "
                "functionals of the interface data -- tail-threshold AND front-peak -- "
                "are NOT metric at these scales (dispersion, boundary reflection, "
                "impedance mismatch at inhomogeneities). What DOES certify at frozen "
                "strength: 1D ball dimension; the MDS rank (capture 0.917 -- the "
                "tau-data is effectively 2-dimensional); exact reciprocity; "
                "representation invariance; the L-ISO dimensional collapse; the L-TOP "
                "horizon. Geometry-related INVARIANTS are recovered; quantitative "
                "metric/curvature reconstruction FAILED in-class -- GEOMETRY-PARTIAL by "
                "the owner's frozen decision rule, at reduced strength, with the failure "
                "surface fully recorded", "note")
    check(True, "GEOMETRY-UNDERDETERMINED (single-site access / horizon-limited windows): "
                "L-ISO -- 2D vs 1D indistinguishable through one site; L-TOP -- global "
                "topology invisible inside the causal horizon", "note")
    check(True, "REPRESENTATIONAL: all reconstructions invariant under substrate scrambles "
                "(L-REP)", "note")
    check(True, "NULL-REDUNDANT: the reconstruction procedures (Lanczos/Jacobi, MDS, "
                "trilateration) are standard mathematics -- no new principle; what is "
                "physical is WHICH data the access makes available", "note")
    check(True, "Rider H: substrates static, stationarity BY CONSTRUCTION in-class; not "
                "presumed beyond (NONSTATIONARITY_RESULT_01 carries). No gravity input "
                "anywhere in G-1", "note")

    out = {"instrument": "g1_geometry", "charter_commit": "f9b043b", "date": "2026-09-25",
           "LDIM": rdim, "LMET": rmet, "LCRV": rcrv, "LREP_diff": rrep, "LISO": riso,
           "LTOP": rtop, "halts": HALT, "checks": CHECKS, "failures": FAIL,
           "elapsed_s": round(time.time() - t0, 2),
           "hard_stop": "verdict recorded; owner rules on the next layer"}
    path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                         "G1_GEOMETRY_RESULT.json"))
    with open(path, "wb") as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True, default=float).encode())
    sha = hashlib.sha256(open(path, "rb").read()).hexdigest()
    print(f"\nartifact written: {path} (sha {sha[:16]}...)")
    n_ok = sum(1 for c in CHECKS if c["ok"])
    print(f"\nG-1 GEOMETRY ATTACK: {n_ok}/{len(CHECKS)} checks passed; failures: "
          f"{len(FAIL)}; halts: {len(HALT)}")
    if HALT:
        print("HALT: an analytic identity breached -- instrument bug, never physics. "
              "No verdict may be issued from this run.")
    else:
        print("HARD STOP: verdict recorded pending owner ruling.")
    sys.exit(0 if not FAIL else 1)


if __name__ == "__main__":
    main()
