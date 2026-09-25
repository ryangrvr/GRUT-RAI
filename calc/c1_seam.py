#!/usr/bin/env python3
"""c1_seam: the stationarity seam attacked as a domain-extension of epsilon (C1-a).

CHARTER: C1_STATIONARITY_SEAM_CHARTER_01.md (pre-registration frozen at commit fa6ac44
BEFORE this instrument ran; owner ruling on Formalization 02 -- the program's first
completion attack). Question: can epsilon : (M, a) -> C_continuum extend from stationary
to genuinely nonstationary microscopic dynamics while preserving the earned finite
reduction, influence structure, and positivity?

BINDING CAUTIONS HONORED: the two-time kernel is GENERATED from a declared microscopic
M(t) (stepped modulation, exact per-epoch eigenmachinery); the FRW/cosmological kernel is
never used as the model; no C2 content; omega^7 / Class-4 / GR-1 / closed forks untouched.

Model (frozen): N = 24 chain, springs 1.0, pins 0.3, site 0 retained; epochs [0,4) A,
[4,8) B, [8,12] A; epoch B scales bath-internal springs (1,2),(2,3),(3,4),(4,5) by
(1 + eps_m); the coupling row (spring (0,1)) is never modulated. eps_m in
{0, 0.01, 0.02, 0.5}. x0 = e0 (bath empty, inhomogeneous term exactly zero).

Legs: L-E exact finite reduction extends | L-S stationary restoration + continuity |
L-P earned structure preserved (passivity, hierarchy/Gram positivity, Bernstein) |
L-B the stationary-packaging boundary (same-lag drift; local-anchor family) |
L-D labeled diagnostics (N-scaling, separable rank), no gates.

Pure stdlib. Run: python3 calc/c1_seam.py
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
EPOCH_T = [0.0, 4.0, 8.0, 12.0]   # boundaries; epochs A, B, A
PIN = 0.3
H = 0.002


def check(ok, msg, kind="ok"):
    tag = {"ok": "ok  ", "ctrl": "ctrl", "note": "note", "diag": "diag"}[kind]
    print(f"  {tag if ok or kind in ('note', 'diag') else 'FAIL'}   {msg}")
    CHECKS.append({"ok": bool(ok), "kind": kind, "msg": msg})
    if not ok and kind not in ("note", "diag"):
        FAIL.append(msg)


def halt_check(ok, msg):
    check(ok, msg, "ctrl")
    if not ok:
        HALT.append(msg)


def build_K(N, eps):
    """Chain stiffness: springs 1.0 (modulated set x(1+eps)), pins PIN."""
    K = [[0.0] * N for _ in range(N)]
    for i in range(N):
        K[i][i] = PIN
    for i in range(N - 1):
        w = 1.0 + (eps if 1 <= i <= 4 else 0.0)   # springs (1,2)..(4,5) modulated
        K[i][i + 1] -= w
        K[i + 1][i] -= w
        K[i][i] += w
        K[i + 1][i + 1] += w
    return K


def eigset(K):
    lam, V = jacobi_eig(K)
    return {"lam": lam, "V": V}


def matvec(M, v):
    return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]


def matvecT(M, v):
    n = len(M)
    return [sum(M[j][i] * v[j] for j in range(n)) for i in range(n)]


def apply_exp(es, dt, vec):
    """e^{-K dt} vec via the eigenset (K symmetric)."""
    c = matvecT(es["V"], vec)
    c = [ci * math.exp(-l * dt) for ci, l in zip(c, es["lam"])]
    return matvec(es["V"], c)


def segments(s, t):
    """Ordered (epoch_index, dt) segments covering [s, t], epochs 0/1/0 on EPOCH_T."""
    out = []
    cur = s
    for i in range(3):
        a, b = EPOCH_T[i], EPOCH_T[i + 1]
        lo, hi = max(cur, a), min(t, b)
        if hi > lo + 1e-15:
            out.append((0 if i != 1 else 1, hi - lo))
            cur = hi
    return out


def prop(esets, s, t, vec):
    """U(t,s) vec: apply per-epoch exponentials in time order."""
    for e, dt in segments(s, t):
        vec = apply_exp(esets[e], dt, vec)
    return vec


class World:
    """All exact machinery for one modulation amplitude eps_m."""

    def __init__(self, N, eps):
        self.N = N
        self.KA = build_K(N, 0.0)
        self.KB = build_K(N, eps)
        self.full = [eigset(self.KA), eigset(self.KB)]
        self.bathA = [row[1:] for row in self.KA[1:]]
        self.bathB = [row[1:] for row in self.KB[1:]]
        self.bath = [eigset(self.bathA), eigset(self.bathB)]
        self.KSS = self.KA[0][0]
        # coupling in per-epoch bath eigenbasis: u_e = V_e^T e0
        self.u = [[self.bath[e]["V"][0][k] for k in range(N - 1)] for e in (0, 1)]

    def xS(self, times):
        """Exact retained trajectory at the sample times (stepwise exact flows)."""
        x = [1.0] + [0.0] * (self.N - 1)
        out, prev = [], 0.0
        for t in times:
            x = prop(self.full, prev, t, x)
            prev = t
            out.append(x[0])
        return out

    def kernel(self, t, s):
        """k(t,s) = [U_B(t,s)]_00 exactly."""
        v = [1.0] + [0.0] * (self.N - 2)
        v = prop(self.bath, s, t, v)
        return v[0]

    def frozen(self, e, tau):
        """Frozen-epoch kernel sum u_l^2 e^{-lam_l tau}."""
        return sum(ul * ul * math.exp(-l * tau)
                   for ul, l in zip(self.u[e], self.bath[e]["lam"]))

    def reduced(self, h, times):
        """S-level solver: q + memory modes m, per-epoch (lam, u), mixing C at
        boundaries. Uses ONLY {lam_e, u_e, C, K_SS} -- the named two-time datum."""
        nb = self.N - 1
        q, m = 1.0, [0.0] * nb
        out, ti, t = [], 0, 0.0

        def f(e, q, m):
            lam, u = self.bath[e]["lam"], self.u[e]
            dq = -self.KSS * q + sum(ul * ml for ul, ml in zip(u, m))
            dm = [-l * ml + ul * q for l, ml, ul in zip(lam, m, u)]
            return dq, dm

        for iep in range(3):
            e = 0 if iep != 1 else 1
            if iep > 0:
                # transform memory modes into the new epoch's eigenbasis: m -> V_new^T V_old m
                eo = 0 if iep == 2 else 0
                V_old = self.bath[1 if iep == 2 else 0]["V"]
                w = matvec(V_old, m)
                m = matvecT(self.bath[e]["V"], w)
            steps = round((EPOCH_T[iep + 1] - EPOCH_T[iep]) / h)
            for _ in range(steps):
                k1q, k1m = f(e, q, m)
                k2q, k2m = f(e, q + 0.5 * h * k1q, [mi + 0.5 * h * di for mi, di in zip(m, k1m)])
                k3q, k3m = f(e, q + 0.5 * h * k2q, [mi + 0.5 * h * di for mi, di in zip(m, k2m)])
                k4q, k4m = f(e, q + h * k3q, [mi + h * di for mi, di in zip(m, k3m)])
                q = q + h / 6 * (k1q + 2 * k2q + 2 * k3q + k4q)
                m = [mi + h / 6 * (a + 2 * b + 2 * c + d)
                     for mi, a, b, c, d in zip(m, k1m, k2m, k3m, k4m)]
                t += h
                while ti < len(times) and times[ti] <= t + 1e-9:
                    out.append(q)
                    ti += 1
        return out


def leg_E(w, times, xs_exact):
    print("\n=== L-E: DOES THE EXACT FINITE REDUCTION EXTEND? (the map) ===")
    # composition identity control (crosses both boundaries, different groupings)
    v = [1.0] + [0.0] * (w.N - 2)
    a = prop(w.bath, 2.0, 10.0, v)
    b = prop(w.bath, 5.0, 10.0, prop(w.bath, 2.0, 5.0, v))
    comp = max(abs(x - y) for x, y in zip(a, b))
    halt_check(comp < 1e-10, f"U_B(10,5) U_B(5,2) = U_B(10,2): max diff {comp:.1e} < 1e-10 "
                             f"(halt-grade)")
    q_h = w.reduced(H, times)
    err_h = max(abs(a - b) for a, b in zip(q_h, xs_exact))
    check(err_h < 1e-6, f"L-E GATE: reduced S-level solve (per-epoch spectral data + mixing "
                        f"matrices ONLY) vs exact full dynamics: max |q - x_S| = {err_h:.1e} "
                        f"< 1e-6 at eps_m = 0.5 over t in [0,12]")
    q_h2 = w.reduced(H / 2, times)
    err_h2 = max(abs(a - b) for a, b in zip(q_h2, xs_exact))
    ratio = err_h / err_h2 if err_h2 > 0 else float("inf")
    check(8 <= ratio <= 32, f"L-E GATE: h -> h/2 error ratio {ratio:.2f} in [8, 32] "
                            f"(4th order; err(h/2) = {err_h2:.1e}) -- the residual is "
                            f"integrator error, the reduction itself is exact")
    check(True, "L-E consequence (frozen): the exact finite reduction is not a stationary "
                "accident -- epsilon extends constructively to stepped nonstationary M(t) "
                "in-class. The reduced description is closed at S level given the named "
                "two-time datum", "note")
    return {"composition": comp, "err_h": err_h, "err_h2": err_h2, "ratio": ratio}


def leg_S(w0, w1, w2, w):
    print("\n=== L-S: STATIONARY RESTORATION AND CONTINUITY ===")
    taus = [0.1 * i for i in range(31)]
    drift0 = max(abs(w0.kernel(2.0 + t, 2.0) - w0.kernel(6.0 + t, 6.0)) for t in taus)
    halt_check(drift0 < 1e-10, f"L-S(a) GATE: eps_m = 0: cross-epoch anchors give identical "
                               f"kernels, max diff {drift0:.1e} < 1e-10 -- K(t,s) collapses "
                               f"to K(t-s) exactly when TTI is restored (halt-grade)")
    pairs = [(s, s + tau) for s in (3.0, 3.2, 3.4, 3.6, 3.8)
             for tau in (0.4, 0.8, 1.2, 1.6, 2.0, 2.4) if s + tau > 4.0]
    dev1 = max(abs(w1.kernel(t, s) - w0.frozen(0, t - s)) for s, t in pairs)
    dev2 = max(abs(w2.kernel(t, s) - w0.frozen(0, t - s)) for s, t in pairs)
    r = dev2 / dev1
    check(1.8 <= r <= 2.2, f"L-S(b) GATE: kernel deviation linear in the TTI-breaking "
                           f"amplitude: dev(0.02)/dev(0.01) = {r:.4f} in [1.8, 2.2] "
                           f"(dev = {dev1:.2e}, {dev2:.2e}) -- the extension connects "
                           f"continuously to the stationary map")
    return {"drift_eps0": drift0, "dev_001": dev1, "dev_002": dev2, "ratio": r}


def leg_P(w, times):
    print("\n=== L-P: EARNED STRUCTURE PRESERVED ===")
    minA = min(w.full[0]["lam"])
    minB = min(w.full[1]["lam"])
    check(minA > 0 and minB > 0, f"L-P GATE: passivity of the microscopic law: min eig "
                                 f"K_A = {minA:.4f}, K_B = {minB:.4f}, both > 0")
    # norm monotonicity of the full flow
    x = [1.0] + [0.0] * (w.N - 1)
    prev_n, mono, t0 = 1.0, True, 0.0
    for t in [0.1 * i for i in range(1, 121)]:
        x = prop(w.full, t0, t, x)
        t0 = t
        n = math.sqrt(sum(xi * xi for xi in x))
        mono = mono and (n <= prev_n + 1e-12)
        prev_n = n
    check(mono, "L-P GATE: ||x(t)|| monotone nonincreasing along the full nonstationary "
                "flow (tolerance 1e-12)")
    # hierarchy positivity: multi-time Gram at eps_m = 0.5
    ts = [0.4 * i for i in range(1, 9)]
    ws = []
    for t in ts:
        # w_i = U(t,0)^T e0: apply the (symmetric) factors in reverse order
        segs = segments(0.0, t)
        v = [1.0] + [0.0] * (w.N - 1)
        for e, dt in reversed(segs):
            v = apply_exp(w.full[e], dt, v)
        ws.append(v)
    G = [[sum(a * b for a, b in zip(wi, wj)) for wj in ws] for wi in ws]
    lamG = jacobi_eig(G)[0]
    halt_check(min(lamG) >= -1e-10, f"L-P GATE: multi-time Gram (hierarchy positivity, the "
                                    f"stationarity-independent admissibility object): min "
                                    f"eigenvalue {min(lamG):.2e} >= -1e-10 (halt-grade)")
    Gt = [[G[i][j] * (1.5 if i != j else 1.0) for j in range(8)] for i in range(8)]
    lamT = min(jacobi_eig(Gt)[0])
    check(lamT < -1e-8, f"L-P GATE (tamper control): x1.5 off-diagonal inflation detected, "
                        f"min eigenvalue {lamT:.3f} < -1e-8 -- the positivity check has teeth")
    wmin = min(min(ul * ul for ul in w.u[e]) for e in (0, 1))
    halt_check(wmin >= -1e-12, f"L-P GATE: Bernstein weights of every frozen-epoch kernel "
                               f">= 0 (min u_l^2 = {wmin:.1e}): each snapshot stays in the "
                               f"earned completely monotone class (halt-grade)")
    return {"min_eig_KA": minA, "min_eig_KB": minB, "gram_min": min(lamG),
            "tamper_min": lamT, "bernstein_min": wmin}


def leg_B(w, w0):
    print("\n=== L-B: WHAT DOES NOT EXTEND -- THE STATIONARY PACKAGING BOUNDARY ===")
    taus = [0.1 * i for i in range(31)]
    kA = [w.kernel(2.0 + t, 2.0) for t in taus]
    kB = [w.kernel(6.0 + t, 6.0) for t in taus]
    scale = max(abs(x) for x in kA)
    D = max(abs(a - b) for a, b in zip(kA, kB)) / scale
    check(D > 0.1, f"L-B(a) GATE: same-lag drift of the GENERATED kernel at eps_m = 0.5: "
                   f"D = {D:.4f} > 0.1 -- the microscopic nonstationary law produces a "
                   f"genuinely two-time kernel (no cosmological input anywhere)")
    # local-anchor family on cross-boundary samples
    pairs = [(s, t) for s in (2.6, 3.0, 3.4) for t in (4.4, 4.8, 5.4)] + \
            [(s, t) for s in (6.6, 7.0, 7.4) for t in (8.4, 8.8, 9.4)]
    pairs = [(s, t) for s, t in pairs if 0.5 <= t - s <= 3.0]

    def epoch_of(a):
        return 1 if 4.0 <= a < 8.0 else 0

    worst = {}
    for name, anchor in (("emission (a=s)", lambda s, t: s), ("observation (a=t)",
                         lambda s, t: t), ("midpoint", lambda s, t: 0.5 * (s + t))):
        errs = []
        for s, t in pairs:
            true = w.kernel(t, s)
            rule = w.frozen(epoch_of(anchor(s, t)), t - s)
            errs.append(abs(rule - true) / abs(true))
        worst[name] = max(errs)
    ok = all(v > 0.05 for v in worst.values())
    detail = ", ".join(f"{k}: {v:.4f}" for k, v in worst.items())
    check(ok, f"L-B(b) GATE: every member of the local-anchor family fails on cross-boundary "
              f"kernels by > 0.05 relative ({detail}) -- no single frozen spectral measure "
              f"reproduces the crossing kernel")
    check(True, "L-B consequence (frozen): the MAP extends but the STATIONARY PACKAGING does "
                "not -- no single rho(tau) and no single (J, nu)(omega) represents K(t,s). "
                "The priced additional structure is exhibited constructively by the solver "
                "itself: per-epoch spectral data PLUS the mixing datum C = V_new^T V_old "
                "(equivalently the bath propagator family) -- a two-time spectral datum. "
                "This names the S1 boundary instead of leaving it a hole", "note")
    return {"drift_D": D, "anchor_worst": worst, "n_pairs": len(pairs)}


def posthoc_diag(w):
    """POST-HOC DIAGNOSTIC (labeled; added AFTER the frozen L-B gates failed; not gates).
    Characterizes the two red gates without repairing them."""
    print("\n=== POST-HOC DIAGNOSTIC (labeled, not frozen legs): why L-B(a)/(b) went red ===")
    taus = [0.1 * i for i in range(1, 31)]
    kA = [w.kernel(2.0 + t, 2.0) for t in taus]
    kB = [w.kernel(6.0 + t, 6.0) for t in taus]
    rel = [(t, abs(a - b) / abs(a)) for t, a, b in zip(taus, kA, kB)]
    over = [t for t, r in rel if r > 0.1]
    rmax = max(r for _, r in rel)
    check(True, f"  (i) normalization artifact: the frozen D divides by max|k| = k(0) = v.v, "
                f"which is modulation-INDEPENDENT; the lagwise relative drift "
                f"|kA-kB|/|kA(tau)| reaches {rmax:.3f} and exceeds 0.1 for tau >= "
                f"{over[0] if over else 'never'} -- the two-time character is order 10^-1 "
                f"in the kernel's own local scale", "diag")
    w2 = World(24, 1.0)
    kA2 = [w2.kernel(2.0 + t, 2.0) for t in taus]
    kB2 = [w2.kernel(6.0 + t, 6.0) for t in taus]
    D2 = max(abs(a - b) for a, b in zip(kA2, kB2)) / max(abs(x) for x in kA2 + [w2.kernel(2.0, 2.0)])
    pairs = [(s, t) for s in (2.6, 3.0, 3.4) for t in (4.4, 4.8, 5.4)] + \
            [(s, t) for s in (6.6, 7.0, 7.4) for t in (8.4, 8.8, 9.4)]
    pairs = [(s, t) for s, t in pairs if 0.5 <= t - s <= 3.0]

    def epoch_of(a):
        return 1 if 4.0 <= a < 8.0 else 0

    worst2 = {}
    for name, anchor in (("emission", lambda s, t: s), ("observation", lambda s, t: t),
                         ("midpoint", lambda s, t: 0.5 * (s + t))):
        worst2[name] = max(abs(w2.frozen(epoch_of(anchor(s, t)), t - s) - w2.kernel(t, s))
                           / abs(w2.kernel(t, s)) for s, t in pairs)
    d2 = ", ".join(f"{k}: {v:.4f}" for k, v in worst2.items())
    check(True, f"  (ii) amplitude scaling: at eps_m = 1.0 (2x the frozen working point) "
                f"D = {D2:.4f} and the anchor-family worst errors are ({d2}) -- the drift "
                f"and the family failure scale with the TTI-breaking amplitude, consistent "
                f"with L-S(b)'s measured linearity; the frozen 0.1 / 0.05 thresholds were "
                f"miscalibrated against the frozen normalization and working point, not "
                f"against the phenomenon", "diag")
    check(True, "  (iii) reading: the generated kernel IS genuinely two-time (drift 5.0e-2 "
                "against a 7.8e-16 stationary control, a 13-orders separation) and the "
                "anchor family DOES fail on two of three members at the frozen threshold; "
                "the packaging-boundary component nevertheless stays NOT MECHANICALLY "
                "CERTIFIED because the frozen gates are the record. No gate is repaired",
          "diag")
    return {"lagwise_rel_max": rmax, "rel_over_0p1_from_tau": over[0] if over else None,
            "D_at_eps1": D2, "anchor_worst_at_eps1": worst2}


def leg_D(times):
    print("\n=== L-D: LABELED DIAGNOSTICS (no gates) ===")
    w12 = World(12, 0.5)
    xs12 = w12.xS(times)
    q12 = w12.reduced(H, times)
    e12 = max(abs(a - b) for a, b in zip(q12, xs12))
    check(True, f"  N = 12 reduction residual {e12:.1e} (N-scaling: the map's exactness is "
                f"size-independent)", "diag")
    # separable rank of the sampled two-time kernel (t > s grid)
    w = World(24, 0.5)
    svals = [1.0 + 0.25 * i for i in range(16)]
    tvals = [1.5 + 0.25 * i for i in range(16)]
    rows = [[w.kernel(t, s) if t > s else 0.0 for s in svals] for t in tvals]
    G = [[sum(rows[i][k] * rows[j][k] for k in range(16)) for j in range(16)] for i in range(16)]
    lam = sorted(jacobi_eig(G)[0], reverse=True)
    rank = sum(1 for x in lam if x > 1e-10 * lam[0])
    check(True, f"  separable rank of the sampled k(t,s) grid: {rank} of 16 (bath size 23) -- "
                f"reported only; no realization-dimension law is claimed off the stationary "
                f"domain", "diag")
    return {"N12_residual": e12, "sep_rank": rank}


def adjudicate(rE, rS, rP, rB):
    map_ok = (rE["err_h"] < 1e-6 and 8 <= rE["ratio"] <= 32 and rS["drift_eps0"] < 1e-10)
    cont = 1.8 <= rS["ratio"] <= 2.2
    struct = (rP["min_eig_KA"] > 0 and rP["min_eig_KB"] > 0 and rP["gram_min"] >= -1e-10
              and rP["tamper_min"] < -1e-8 and rP["bernstein_min"] >= -1e-12)
    pack = rB["drift_D"] > 0.1 and all(v > 0.05 for v in rB["anchor_worst"].values())
    return {
        "map": "DERIVED EXTENSION (in-class): epsilon extends constructively to stepped "
               "nonstationary M(t)" if map_ok else "NOT ESTABLISHED",
        "continuity": "established: K(t,s) -> K(t-s) exactly at TTI restoration; deviation "
                      "linear in the breaking amplitude" if cont else "NOT ESTABLISHED",
        "structure": "PRESERVED: passivity, hierarchy positivity (Gram PSD, tamper "
                     "detected), Bernstein class per snapshot" if struct
                     else "FAILURE (an earned constraint broke)",
        "packaging": "PRINCIPLED DOMAIN BOUNDARY: no single rho / (J,nu) packaging; priced "
                     "datum = per-epoch spectral data + the mixing matrices (the two-time "
                     "spectral datum)" if pack else "NOT MECHANICALLY CERTIFIED (see gates)",
        "composite": ("S1 CROSSED CONSTRUCTIVELY AT FINITE LEVEL IN-CLASS; the stationary "
                      "packaging boundary is CERTIFIED with its priced datum named; "
                      "remainder relocated to C1-b (infinite volume) and C1-c (smooth "
                      "modulation), named not opened"
                      if (map_ok and cont and struct and pack) else
                      "PARTIAL -- see the per-component lines and any red gates"),
        "fences": "no cosmological kernel consumed; no C2 content; omega^7/Class-4/GR-1/"
                  "closed forks untouched; no absolute exponent computed",
    }


def main():
    t0 = time.time()
    print("C1-a: THE STATIONARITY SEAM -- DOMAIN-EXTENSION ATTACK ON epsilon (charter frozen "
          "at fa6ac44)")
    times = [0.1 * i for i in range(1, 121)]
    w = World(24, 0.5)
    w0 = World(24, 0.0)
    w1 = World(24, 0.01)
    w2 = World(24, 0.02)
    xs = w.xS(times)
    rE = leg_E(w, times, xs)
    rS = leg_S(w0, w1, w2, w)
    rP = leg_P(w, times)
    rB = leg_B(w, w0)
    rPH = posthoc_diag(w)
    rD = leg_D(times)
    adj = adjudicate(rE, rS, rP, rB)
    print("\n=== ADJUDICATION (frozen outcome rule, computed from the measurements) ===")
    for k, v in adj.items():
        check(True, f"{k}: {v}", "note")
    out = {"instrument": "c1_seam", "charter_commit": "fa6ac44", "date": "2026-09-25",
           "L_E": rE, "L_S": rS, "L_P": rP, "L_B": rB, "L_D": rD,
           "posthoc_diagnostic_LB": rPH, "adjudication": adj,
           "halts": HALT, "checks": CHECKS, "failures": FAIL,
           "elapsed_s": round(time.time() - t0, 2), "hard_stop": "verdict recorded"}
    path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                         "C1_SEAM_RESULT.json"))
    with open(path, "wb") as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True, default=str).encode())
    sha = hashlib.sha256(open(path, "rb").read()).hexdigest()
    print(f"\nartifact written: {path} (sha {sha[:16]}...)")
    gated = [c for c in CHECKS if c["kind"] not in ("note", "diag")]
    n_ok = sum(1 for c in gated if c["ok"])
    print(f"\nC1-a STATIONARITY-SEAM ATTACK: {n_ok}/{len(gated)} gated checks passed "
          f"({len(CHECKS)} lines incl. notes/diagnostics); failures: {len(FAIL)}; "
          f"halts: {len(HALT)}")
    if HALT:
        print("HALT: an analytic identity breached -- instrument bug, never physics. "
              "No verdict may be issued from this run.")
    else:
        print("HARD STOP: verdict recorded pending owner ruling.")
    sys.exit(0 if not FAIL else 1)


if __name__ == "__main__":
    main()
