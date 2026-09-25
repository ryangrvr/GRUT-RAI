#!/usr/bin/env python3
"""tt1_channel: the physical D = 4 TT channel and xi.

CHARTER: TT1_TT_XI_CHARTER_01.md (pre-registration frozen at commit b4a2f33 BEFORE this
instrument ran; owner ruling on SX-1, in-session). Sel-4x is inherited as classified
(IRREDUCIBLE, reduced to the co-stretch declaration), not re-decided. Fences: no absolute
exponent is computed or compared to 7; omega^7 is occupancy evidence only; CARRIER, GeoInv,
the supplied probe and a preselected coupling are not used as selectors.

Kinematics: on-shell graviton k = p1 + p2 (spatial), Omega = w(a) + w(b) = |k| (c = 1); the
opening angle solves cos(theta) = [(w(a) + w(b))^2 - a^2 - b^2] / (2ab); TT projector about
k-hat: Lambda(X) = P X P - 1/2 P tr(P X), P = 1 - k-hat k-hat.

Legs: L-xi (Q1: is xi / the improvement tower visible in TT?) | L-F (Q2: is the coupling form
forced once higher derivatives are allowed?) | L-K (Q3: when does the TT pair channel exist?).

Pure stdlib. Run: python3 calc/tt1_channel.py
"""
import hashlib
import json
import math
import os
import random
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from partition_selection_p1 import jacobi_eig

FAIL = []
CHECKS = []
HALT = []
SEED = 20260925
NPTS = 200


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


# ---------- 3-vector / 3x3 tensor helpers ----------
def dot(u, v):
    return sum(x * y for x, y in zip(u, v))


def norm(u):
    return math.sqrt(dot(u, u))


def outer(u, v):
    return [[u[i] * v[j] for j in range(3)] for i in range(3)]


def add(*Ts):
    return [[sum(T[i][j] for T in Ts) for j in range(3)] for i in range(3)]


def scale(s, T):
    return [[s * T[i][j] for j in range(3)] for i in range(3)]


def mm3(A, B):
    return [[sum(A[i][m] * B[m][j] for m in range(3)) for j in range(3)] for i in range(3)]


def fro(T):
    return math.sqrt(sum(x * x for r in T for x in r))


def flat(T):
    return [x for r in T for x in r]


EYE = [[1.0 if i == j else 0.0 for j in range(3)] for i in range(3)]


def tt(X, k):
    kh = [x / norm(k) for x in k]
    P = [[EYE[i][j] - kh[i] * kh[j] for j in range(3)] for i in range(3)]
    PX = mm3(P, X)
    PXP = mm3(PX, P)
    trPX = sum(PX[i][i] for i in range(3))
    return add(PXP, scale(-0.5 * trPX, P))


def rotation(rng):
    q = [rng.gauss(0, 1) for _ in range(4)]
    n = norm(q)
    w, x, y, z = (c / n for c in q)
    return [[1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
            [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
            [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)]]


def apply(R, v):
    return [dot(R[i], v) for i in range(3)]


def cos_theta(disp, a, b):
    W = disp(a) + disp(b)
    return (W * W - a * a - b * b) / (2 * a * b)


def pair(disp, a, b, R):
    """On-shell pair (p1, p2) with |p1| = a, |p2| = b, rotated by R; None if no solution."""
    c = cos_theta(disp, a, b)
    if c > 1.0 + 1e-13 or c < -1.0 - 1e-13:
        return None, c
    c = max(-1.0, min(1.0, c))
    s = math.sqrt(max(0.0, 1.0 - c * c))
    p1 = apply(R, [a, 0.0, 0.0])
    p2 = apply(R, [b * c, b * s, 0.0])
    return (p1, p2), c


def onshell_residual(disp, p1, p2):
    k = [x + y for x, y in zip(p1, p2)]
    return abs(norm(k) - (disp(norm(p1)) + disp(norm(p2))))


def v08(p):
    return 0.8 * p


def sample(rng, disp, n):
    pts = []
    while len(pts) < n:
        a, b = rng.uniform(0.2, 1.0), rng.uniform(0.2, 1.0)
        pr, _ = pair(disp, a, b, rotation(rng))
        if pr is not None:
            pts.append(pr)
    return pts


def T_family(p1, p2, disp):
    a2, b2 = dot(p1, p1), dot(p2, p2)
    T1 = add(outer(p1, p2), outer(p2, p1))
    T2 = add(outer(p1, p1), outer(p2, p2))
    T3 = add(scale(a2, outer(p1, p1)), scale(b2, outer(p2, p2)))
    T4 = scale(dot(p1, p2), T1)
    T5 = scale(disp(math.sqrt(a2)) * disp(math.sqrt(b2)), T1)
    return [T1, T2, T3, T4, T5]


# ---------- legs ----------
def leg_xi(pts):
    print("\n=== L-xi (Q1): IS xi / THE IMPROVEMENT TOWER VISIBLE IN THE PHYSICAL TT CHANNEL? ===")
    worst = 0.0
    worst_onshell = 0.0
    fnames = ["1", "p1.p2", "|p1|^2+|p2|^2"]
    per_f = {f: 0.0 for f in fnames}
    for p1, p2 in pts:
        worst_onshell = max(worst_onshell, onshell_residual(v08, p1, p2))
        k = [x + y for x, y in zip(p1, p2)]
        Om = v08(norm(p1)) + v08(norm(p2))
        k4sq = Om * Om - dot(k, k)
        canon = fro(tt(add(outer(p1, p2), outer(p2, p1)), k))
        base = add(scale(-k4sq, EYE), scale(-1.0, outer(k, k)))
        for f, fv in zip(fnames, [1.0, dot(p1, p2), dot(p1, p1) + dot(p2, p2)]):
            r = fro(tt(scale(fv, base), k)) / canon
            per_f[f] = max(per_f[f], r)
            worst = max(worst, r)
    halt_check(worst_onshell < 1e-12, f"on-shell condition re-verified on all {len(pts)} pairs: "
                                      f"max ||k| - Omega| = {worst_onshell:.1e} < 1e-12")
    halt_check(worst < 1e-12, f"L-xi GATE: max |Lambda(improvement)| / |Lambda(canonical)| = "
                              f"{worst:.1e} < 1e-12 over {len(pts)} on-shell pairs and "
                              f"f in {{1, p1.p2, |p1|^2+|p2|^2}} (halt-grade identity)")
    for f in fnames:
        check(True, f"  f = {f}: max ratio {per_f[f]:.1e}", "note")
    # sensitivity note (not a frozen leg): the same structure is visible off the TT channel
    p1, p2 = pts[0]
    k = [x + y for x, y in zip(p1, p2)]
    strain_trace = abs(sum(add(scale(-(0.0 - dot(k, k)), EYE),
                               scale(-1.0, outer(k, k)))[i][i] for i in range(3)))
    check(True, f"  sensitivity note (not a frozen gate): at static strain kinematics (Omega = 0, "
                f"k^2 = -|k|^2) the trace of the improvement structure is {strain_trace:.4f} != 0 "
                f"-- xi is visible off-shell/trace, as CP-1 found; retained, not contradicted",
          "note")
    check(True, "L-xi consequence (frozen): xi and the whole improvement tower are invisible in "
                "the physical TT channel (Lambda(k k) = 0 and Lambda(1) = 0 identically). The "
                "D = 4 xi ambiguity dissolves there; it survives only for off-shell/trace "
                "(strain) probes", "note")
    return {"max_ratio": worst, "per_f": per_f, "onshell_max": worst_onshell,
            "strain_trace_sensitivity": strain_trace}


def ff_rank(pts, disp):
    """Per-point TT rank (Gram eigenvalues) and across-point form-factor rank."""
    worst_rel2 = 0.0
    rows = []
    for p1, p2 in pts:
        k = [x + y for x, y in zip(p1, p2)]
        imgs = [flat(tt(T, k)) for T in T_family(p1, p2, disp)]
        Gm = [[dot(u, v) for v in imgs] for u in imgs]
        ev = sorted(jacobi_eig(Gm)[0], reverse=True)
        worst_rel2 = max(worst_rel2, ev[1] / ev[0])
        E = imgs[0]
        EE = dot(E, E)
        rows.append([dot(u, E) / EE for u in imgs])
    cols = list(zip(*rows))
    ncols = [[x / norm(c) for x in c] for c in cols]
    Gc = [[dot(u, v) for v in ncols] for u in ncols]
    evc = sorted(jacobi_eig(Gc)[0], reverse=True)
    rank = sum(1 for e in evc if e / evc[0] > 1e-10)
    t2t1 = max(abs(r[1] / r[0] - rows[0][1] / rows[0][0]) for r in rows)
    return worst_rel2, rows, evc, rank, t2t1


def leg_F(pts):
    print("\n=== L-F (Q2): IS THE COUPLING FORM FORCED ONCE HIGHER DERIVATIVES ARE ALLOWED? ===")
    worst_rel2, rows, evc, rank, t2t1 = ff_rank(pts, v08)
    halt_check(worst_rel2 < 1e-10, f"L-F(a) GATE: per-point TT images of T1..T5 have rank 1 on "
                                   f"all {len(pts)} points: max lambda_2/lambda_1 of the Gram "
                                   f"matrix = {worst_rel2:.1e} < 1e-10 -- the TT TENSOR "
                                   f"structure is forced")
    check(True, f"  T2 proportional to T1 in TT: form-factor ratio constant to {t2t1:.1e} "
                f"(value {rows[0][1] / rows[0][0]:+.4f})", "note")
    check(True, f"  form-factor Gram eigenvalues (normalized columns): "
                f"{', '.join(f'{e:.2e}' for e in evc)}", "note")
    check(rank == 4, f"L-F(b) GATE: form-factor rank across {len(pts)} points = {rank} "
                     f"(frozen prediction 4)")
    # (c) IR suppression at symmetric kinematics a = b = p
    ratios = {}
    R0 = [[1.0 if i == j else 0.0 for j in range(3)] for i in range(3)]
    for p in (0.2, 0.4):
        (p1, p2), _ = pair(v08, p, p, R0)
        k = [x + y for x, y in zip(p1, p2)]
        T = T_family(p1, p2, v08)
        ratios[p] = fro(tt(T[2], k)) / fro(tt(T[0], k))
    grow = ratios[0.4] / ratios[0.2]
    check(3.5 <= grow <= 4.5, f"L-F(c) GATE: |Lambda(T3)|/|Lambda(T1)| at a = b = p: "
                              f"{ratios[0.2]:.4f} (p = 0.2) -> {ratios[0.4]:.4f} (p = 0.4), growth "
                              f"x{grow:.4f} in [3.5, 4.5] -- the higher-derivative form factor "
                              f"is IR-suppressed")
    check(True, "L-F consequence (frozen): in TT the leading IR coupling is forced (rank-1 "
                "tensor, constant form factor); beyond leading order the form factor is "
                "CONSTRAINED-NONUNIQUE and inherits the supplied geometric-coupling/Sel-4x "
                "choice", "note")
    return {"per_point_max_l2_over_l1": worst_rel2, "ff_gram_eigs": evc, "ff_rank": rank,
            "T2_over_T1": rows[0][1] / rows[0][0], "T2_over_T1_spread": t2t1,
            "ir_ratio": {str(k): v for k, v in ratios.items()}, "ir_growth": grow}


def diag_F(pts, rng):
    """LABELED POST-HOC DIAGNOSTIC (not frozen): why the L-F(b) rank is what it is."""
    print("\n=== POST-HOC DIAGNOSTIC (labeled, not a frozen leg): the on-shell identity behind "
          "the L-F(b) rank ===")
    # on shell, 2 p1.p2 = (w1 + w2)^2 - a^2 - b^2 ; for w = v|p| this is
    # p1.p2 = (v^2 - 1)/2 (a^2 + b^2) + w1 w2, a linear relation between the T4, T3, T5 scalars
    res = 0.0
    for p1, p2 in pts:
        a, b = norm(p1), norm(p2)
        res = max(res, abs(dot(p1, p2) - (0.5 * (0.64 - 1.0) * (a * a + b * b)
                                          + v08(a) * v08(b))))
    check(True, f"  linear sector v = 0.8: on-shell identity p1.p2 = (v^2-1)/2 (a^2+b^2) + w1 w2 "
                f"holds to {res:.1e} -- the T4 form factor is a combination of T3 and T5 there, "
                f"so the rank drops from 4 to 3", "diag")

    def curved(p):
        return 0.8 * p - 0.1 * p ** 3

    cpts = sample(rng, curved, NPTS)
    wr, _, evc, rank_c, _ = ff_rank(cpts, curved)
    check(True, f"  curved sector w = 0.8|p| - 0.1|p|^3: per-point TT rank 1 "
                f"(max lambda_2/lambda_1 = {wr:.1e}); form-factor rank = {rank_c} "
                f"(Gram eigenvalues {', '.join(f'{e:.1e}' for e in evc)}) -- dispersion "
                f"curvature breaks the identity", "diag")
    check(True, "  diagnostic reading: the form-factor rank is > 1 in both classes (the frozen "
                "CONSTRAINED-NONUNIQUE outcome is unaffected); the specific count 4 was an "
                "overcount for a linear sector, where the on-shell condition itself ties p1.p2 to "
                "(a^2+b^2) and w1 w2", "diag")
    return {"linear_identity_residual": res, "curved_rank": rank_c, "curved_gram_eigs": evc,
            "curved_per_point_l2_over_l1": wr}


def vertex(disp, a, b):
    R0 = [[1.0 if i == j else 0.0 for j in range(3)] for i in range(3)]
    pr, c = pair(disp, a, b, R0)
    if pr is None:
        return None, c, None
    p1, p2 = pr
    k = [x + y for x, y in zip(p1, p2)]
    return fro(tt(add(outer(p1, p2), outer(p2, p1)), k)), c, onshell_residual(disp, p1, p2)


def leg_K(rng):
    print("\n=== L-K (Q3): WHEN DOES THE TT PAIR CHANNEL EXIST? ===")
    grid = [0.2 + 0.1 * i for i in range(9)]
    # (a) exactly linear, v = c
    worst_a, worst_on, worst_c = 0.0, 0.0, 0.0
    for a in grid:
        for b in grid:
            V, c, on = vertex(lambda p: p, a, b)
            worst_a = max(worst_a, V)
            worst_on = max(worst_on, on)
            worst_c = max(worst_c, abs(c - 1.0))
    halt_check(worst_a < 1e-12, f"L-K(a) GATE: w = |p| (v = c): |cos theta - 1| <= "
                                f"{worst_c:.1e}, collinear locus; max TT vertex {worst_a:.1e} "
                                f"< 1e-12 over {len(grid) ** 2} (a, b) -- aligned death "
                                f"(halt-grade)")
    # (b) subluminal linear v = 0.8, the random on-shell locus
    minb = float("inf")
    for p1, p2 in sample(rng, v08, NPTS):
        k = [x + y for x, y in zip(p1, p2)]
        minb = min(minb, fro(tt(add(outer(p1, p2), outer(p2, p1)), k)))
    check(minb > 1e-3, f"L-K(b) GATE: v = 0.8: min TT vertex over {NPTS} random on-shell pairs "
                       f"= {minb:.4f} > 1e-3 -- channel open, non-collinear locus")
    # (c) v = c in the IR with subluminal curvature
    Vc = {}
    for al in (0.01, 0.02):
        V, c, on = vertex(lambda p, al=al: p - al * p ** 3, 0.5, 0.5)
        Vc[al] = V
        worst_on = max(worst_on, on)
    rc = Vc[0.02] / Vc[0.01]
    check(Vc[0.01] > 0 and 1.8 <= rc <= 2.2,
          f"L-K(c) GATE: w = |p| - alpha|p|^3 at a = b = 0.5: vertex {Vc[0.01]:.3e} (alpha = "
          f"0.01), {Vc[0.02]:.3e} (alpha = 0.02); ratio {rc:.4f} in [1.8, 2.2] -- the channel "
          f"is open in proportion to subluminal curvature")
    # (d) superluminal curvature
    minc = float("inf")
    closed = True
    for a in grid:
        for b in grid:
            c = cos_theta(lambda p: p + 0.01 * p ** 3, a, b)
            minc = min(minc, c)
            closed = closed and c > 1.0
    check(closed, f"L-K(d) GATE: w = |p| + 0.01|p|^3: cos theta > 1 for all {len(grid) ** 2} "
                  f"(a, b) (min cos theta = 1 + {minc - 1.0:.2e}) -- no on-shell solution, the "
                  f"channel is closed")
    halt_check(worst_on < 1e-12, f"on-shell re-verified on the L-K(a)/(c) loci: max residual "
                                 f"{worst_on:.1e} < 1e-12")
    check(True, "L-K consequence (frozen): the TT channel's existence is CLASS-SPLIT by the "
                "retained sector's light cone relative to the probe's -- dead for an exactly "
                "Lorentz-matched linear sector, open in proportion to subluminality, closed for "
                "superluminal dispersion. With RS-1's per-sector v = c units choice the channel "
                "lives only on dispersion curvature (microscopic retained-sector content); the "
                "cross-sector light-cone relation is U-1 territory (supplied)", "note")
    return {"a_max_vertex": worst_a, "a_max_cos_dev": worst_c, "b_min_vertex": minb,
            "c_vertex": {str(k): v for k, v in Vc.items()}, "c_ratio": rc,
            "d_closed": closed, "d_min_cos_minus_1": minc - 1.0, "onshell_max": worst_on}


def adjudicate(rx, rf, rk):
    q1 = ("DERIVED-IN-CLASS: xi irrelevant in the physical TT channel" if rx["max_ratio"] < 1e-12
          else "not derived")
    q2 = {"tensor": "FORCED (rank 1 per point)" if rf["per_point_max_l2_over_l1"] < 1e-10
          else "not forced",
          "form_factor": ("CONSTRAINED-NONUNIQUE" if rf["ff_rank"] > 1 else "forced")
          + f" (rank {rf['ff_rank']}; frozen prediction 4)",
          "ir": "IR-forced (higher-derivative form factor suppressed)"
          if 3.5 <= rf["ir_growth"] <= 4.5 else "no IR suppression shown"}
    kall = (rk["a_max_vertex"] < 1e-12 and rk["b_min_vertex"] > 1e-3
            and 1.8 <= rk["c_ratio"] <= 2.2 and rk["d_closed"])
    q3 = ("CLASS-SPLIT: dead (v = c exactly) / open proportional to subluminality / closed "
          "(superluminal)" if kall else "not established")
    return {"Q1": q1, "Q2": q2, "Q3": q3,
            "fence": "no absolute exponent computed; no omega^7 comparison"}


def main():
    t0 = time.time()
    print("TT-1: THE PHYSICAL D = 4 TT CHANNEL AND xi (charter frozen at b4a2f33)")
    rng = random.Random(SEED)
    pts = sample(rng, v08, NPTS)
    rx = leg_xi(pts)
    rf = leg_F(pts)
    rk = leg_K(rng)
    rd = diag_F(pts, rng)
    adj = adjudicate(rx, rf, rk)
    print("\n=== ADJUDICATION (frozen outcome rule, computed from the measurements) ===")
    for k, v in adj.items():
        check(True, f"{k}: {v}", "note")
    out = {"instrument": "tt1_channel", "charter_commit": "b4a2f33", "date": "2026-09-25",
           "seed": SEED, "L_xi": rx, "L_F": rf, "L_K": rk,
           "posthoc_diagnostic_LF_rank": rd, "adjudication": adj, "halts": HALT,
           "checks": CHECKS, "failures": FAIL, "elapsed_s": round(time.time() - t0, 2),
           "hard_stop": "verdict recorded"}
    path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                         "TT1_CHANNEL_RESULT.json"))
    with open(path, "wb") as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True, default=str).encode())
    sha = hashlib.sha256(open(path, "rb").read()).hexdigest()
    print(f"\nartifact written: {path} (sha {sha[:16]}...)")
    gated = [c for c in CHECKS if c["kind"] not in ("note", "diag")]
    n_ok = sum(1 for c in gated if c["ok"])
    print(f"\nTT-1 CHANNEL ATTACK: {n_ok}/{len(gated)} gated checks passed "
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
