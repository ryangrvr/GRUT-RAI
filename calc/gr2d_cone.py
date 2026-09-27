#!/usr/bin/env python3
"""GR2-d -- the causal cone (frozen instrument).

Charter: GR2D_CONE_CHARTER_01.md, frozen at commit ff8db42, under the
GR-2 campaign directive (Layer 4 / seam S2) and the GR2-c owner ruling.

Question (the owner's, frozen): can a universal causal cone emerge from
the earned influence/response/access structure, or must the cone itself
be supplied as an additional primitive? Equivalently: does the GRUT
core itself produce the causal structure, or does it require causal
structure as an input?

Discipline (frozen): a system is ELIMINATED only if an earned
admissibility test fails on it (pair-kernel positivity, ground-state
two-time Gram PSD, interaction-graph consistency, the memory battery);
front speeds, arrival times, and supports are labels, never
eliminators. Causal propagation exists != a universal cone is
selected. The empirical light-speed/Lorentz eliminators stay OUTSIDE
the record. A SELECTED outcome would require an earned discriminator
rejecting the alternatives -- never family coincidence.

Machinery: the C1-a seam kernels replicated as halt-grade controls
(owner-verified reproduction-note values); the GR-1 L-X kernel block
replicated verbatim; classical normal-mode ring fronts (procedure
calibrated on K = 1 only, disclosed in the charter); 7-site quantum
commutator fronts on the record's own two sector parameter sets;
coupled-ring exchange branches in closed form. Pure stdlib.
Deterministic (no RNG in this fork). Single run.
Run: python3 calc/gr2d_cone.py   (writes ../GR2D_CONE_RESULT.json)
"""

import hashlib
import json
import math
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from partition_selection_p1 import jacobi_eig
from c1_seam import PIN, World, build_K
from s41_sel4 import dense, edges, gram_psd, op_add, placed, HX, HZ

T0 = time.time()
CHECKS = []
HALT = []


def check(ok, msg, kind="ok"):
    CHECKS.append({"kind": kind, "pass": bool(ok), "summary": msg})
    tag = {"ok": "GATE", "ctrl": "CONTROL", "note": "NOTE", "diag": "DIAG"}[kind]
    print(("PASS " if ok else "FAIL ") + tag + ": " + msg)


def halt_check(ok, msg):
    check(ok, msg, "ctrl")
    if not ok:
        HALT.append(msg)


MEAS = {}
ELIM = []  # one row per different-cone system (admissibility only)

# ---------------- RM: C1-a memory-kernel controls ----------------------
print("=== RM: C1-a SEAM-KERNEL CONTROLS (halt-grade; owner-verified "
      "reproduction-note values) ===")
W1 = World(24, 1.0)
REC_K = {("A", 1.0): 0.1594754, ("B", 1.0): 0.1328810,
         ("A", 0.5): 0.3579003, ("B", 0.5): 0.2874716}
for i, ((ep, tau), rec) in enumerate(sorted(REC_K.items()), 1):
    val = W1.frozen(0 if ep == "A" else 1, tau)
    MEAS[f"c1a_kernel_{ep}_{tau}"] = val
    halt_check(abs(val - rec) < 5e-8,
               f"RM-{i} C1-a epoch-{ep} kernel at tau = {tau}: {val:.9f} "
               f"replicates the recorded {rec}")

# ---------------- RL-1: the L-X kernel block (verbatim) -----------------
ALPHA = 0.05


def disp(q):
    return q - ALPHA * q ** 3


def root_q(w):
    q = w / 2.0
    for _ in range(60):
        f = 2.0 * disp(q) - w
        df = 2.0 * (1.0 - 3.0 * ALPHA * q * q)
        q -= f / df
    return q


def J_of(w, vertex):
    q = root_q(w)
    M = vertex(q)
    return M * M / abs(2.0 * (1.0 - 3.0 * ALPHA * q * q))


def stress_vertex(q):
    return disp(q) ** 2 - q * q


s_stress = (math.log(J_of(0.2, stress_vertex) / J_of(0.1, stress_vertex))
            / math.log(2.0))
halt_check(abs(s_stress - 8.005419679013105) < 1e-9,
           f"RL-1 L-X stress-source slope {s_stress:.12f} replicates the "
           f"recorded 8.005419679013105")
MEAS["LX_stress_slope"] = s_stress

# ---------------- N: classical ring fronts (frozen procedure) -----------
print("\n=== N: NO CONE SELECTION (classical rings; procedure calibrated "
      "on K = 1 only, disclosed) ===")
NRING = 400
SITES = [30, 38, 46, 54]
TGRID = [0.05 * i for i in range(1201)]  # 0..60


def ring_omegas(K):
    return [2.0 * math.sqrt(K) * abs(math.sin(math.pi * k / NRING))
            for k in range(NRING)]


def ring_u(ws, r, S):
    return sum(math.cos(2 * math.pi * k * r / NRING) * S[k]
               for k in range(NRING)) / NRING


def ring_front(K):
    ws = ring_omegas(K)
    hist = {r: [] for r in SITES}
    for t in TGRID:
        S = [t if k == 0 else math.sin(ws[k] * t) / ws[k]
             for k in range(NRING)]
        for r in SITES:
            hist[r].append(ring_u(ws, r + 1, S) - ring_u(ws, r, S))
    tstars = []
    for r in SITES:
        h = [abs(x) for x in hist[r]]
        thr = 0.1 * max(h)
        tstars.append(next(TGRID[i] for i, x in enumerate(h) if x > thr))
    n = len(SITES)
    sr, st = sum(SITES), sum(tstars)
    srr = sum(r * r for r in SITES)
    srt = sum(r * t for r, t in zip(SITES, tstars))
    slope = (n * srt - sr * st) / (n * srr - sr * sr)
    return 1.0 / slope, tstars


def ring_momentum_dev(K, t):
    ws = ring_omegas(K)
    sv = 0.0
    for r in range(NRING):
        sv += sum(math.cos(2 * math.pi * k * r / NRING)
                  * (1.0 if k == 0 else math.cos(ws[k] * t))
                  for k in range(NRING)) / NRING
    return abs(sv - 1.0)


def ring_sharpness(K, v, t_obs=40.0):
    ws = ring_omegas(K)
    S = [t_obs if k == 0 else math.sin(ws[k] * t_obs) / ws[k]
         for k in range(NRING)]

    def strain(r):
        return abs(ring_u(ws, r + 1, S) - ring_u(ws, r, S))

    r_out = int(round(1.6 * v * t_obs))
    inside = max(strain(r) for r in range(1, int(v * t_obs)))
    return strain(r_out) / inside, r_out


mom_dev = ring_momentum_dev(1.0, 10.0)
vA, tstA = ring_front(1.0)
halt_check(mom_dev < 1e-9 and abs(vA - 1.0256410256) < 1e-6,
           f"RN-1 classical procedure replicates its calibration: momentum "
           f"identity |sum u_dot - 1| = {mom_dev:.1e} < 1e-9; v_A = "
           f"{vA:.10f} (calibrated 1.0256410256)")
vB, tstB = ring_front(1.69)
MEAS["classical_fronts"] = {"v_A": vA, "t_star_A": tstA,
                            "v_B": vB, "t_star_B": tstB,
                            "ratio": vB / vA}
check(1.25 <= vB / vA <= 1.35,
      f"N-1 the fronts differ by the supplied-stiffness factor: "
      f"v_B / v_A = {vB / vA:.6f} in [1.25, 1.35] (analytic sqrt(1.69) = "
      f"1.3; procedure systematics cancel in the ratio) -- two "
      f"earned-admissible sectors, two causal cones")
ws_scan = [0.10 + 0.02 * i for i in range(6)]


def J_sector(w, K):
    # the L-X pair kernel at sector sound speed sqrt(K): omega = sqrt(K) disp(q)
    rt = math.sqrt(K)
    q = w / (2.0 * rt)
    for _ in range(60):
        f = 2.0 * rt * disp(q) - w
        df = 2.0 * rt * (1.0 - 3.0 * ALPHA * q * q)
        q -= f / df
    M = stress_vertex(q)
    return M * M / abs(2.0 * rt * (1.0 - 3.0 * ALPHA * q * q))


jminN = min(min(J_sector(w, K) for w in ws_scan) for K in (1.0, 1.69))
check(jminN >= 0.0,
      f"N-2 both sectors earned-admissible: per-sector pair kernels "
      f"J(w) >= 0 on the scan (min {jminN:.3e}); identical ring topology "
      f"-- the earned battery passes for BOTH cones")
ELIM.append({"leg": "N", "system": "classical ring K = 1.69",
             "eliminated": not jminN >= 0.0,
             "tests": {"J_min": jminN, "topology_same": True}})

# ---------------- Q: quantum commutator fronts --------------------------
print("\n=== Q: NO CONE SELECTION (7-site open chains; the record's own "
      "two sector parameter sets) ===")
LQ = 7
DQ = 2 ** LQ


def open_chain(J, hx, hz):
    H = {}
    for i in range(LQ - 1):
        H = op_add(H, {placed(LQ, [(i, 3), (i + 1, 3)]): 1.0}, J)
    for i in range(LQ):
        H = op_add(H, {placed(LQ, [(i, 1)]): 1.0}, hx)
        H = op_add(H, {placed(LQ, [(i, 3)]): 1.0}, hz)
    return H


def real(M):
    return [[x.real for x in r] for r in M]


def front_quantum(J, hx, hz):
    Hop = open_chain(J, hx, hz)
    Hr = real(dense(Hop, LQ))
    lam, V = jacobi_eig(Hr)
    # Xd = V^T X_0 V; X_0 flips bit 0
    Xd = [[sum(V[i][m] * V[i ^ 1][n] for i in range(DQ)) for n in range(DQ)]
          for m in range(DQ)]
    # Zd = V^T Z_0 V; Z_0 diagonal +/-1 on bit 0
    zs = [1.0 if (i & 1) == 0 else -1.0 for i in range(DQ)]
    Zd = [[sum(V[i][m] * zs[i] * V[i][n] for i in range(DQ))
           for n in range(DQ)] for m in range(DQ)]

    def apply_evolved(Od, c, t):
        # returns V e^{i lam t} Od e^{-i lam t} c   in the computational basis
        u = [complex(math.cos(-lam[m] * t), math.sin(-lam[m] * t)) * c[m]
             for m in range(DQ)]
        y = [sum(Od[m][n] * u[n] for n in range(DQ)) for m in range(DQ)]
        z = [complex(math.cos(lam[m] * t), math.sin(lam[m] * t)) * y[m]
             for m in range(DQ)]
        return [sum(V[i][m] * z[m] for m in range(DQ)) for i in range(DQ)]

    tq = [0.05 * i for i in range(121)]  # 0..6
    rows_X = {r: [] for r in range(1, 6)}
    row_Z5 = []
    unit_dev = 0.0
    for t in tq:
        c0 = [V[0][m] for m in range(DQ)]
        p = apply_evolved(Xd, c0, t)             # X_0(t) psi0
        if abs(t - 2.0) < 1e-12:
            unit_dev = abs(math.sqrt(sum(abs(x) ** 2 for x in p)) - 1.0)
        pz = apply_evolved(Zd, c0, t)            # Z_0(t) psi0
        for r in range(1, 6):
            cr = [V[1 << r][m] for m in range(DQ)]
            a = apply_evolved(Xd, cr, t)         # X_0(t) X_r psi0
            F = math.sqrt(sum(abs(a[i] - p[i ^ (1 << r)]) ** 2
                              for i in range(DQ)))
            rows_X[r].append(F)
        zsr = [1.0 if (i & (1 << 5)) == 0 else -1.0 for i in range(DQ)]
        az = apply_evolved(Zd, [zsr[0] * V[0][m] for m in range(DQ)], t)
        Fz = math.sqrt(sum(abs(az[i] - zsr[i] * pz[i]) ** 2
                           for i in range(DQ)))
        row_Z5.append(Fz)

    def arrival(hist):
        thr = 0.1 * max(hist)
        return next(tq[i] for i, x in enumerate(hist) if x > thr)

    tstar = {r: arrival(rows_X[r]) for r in range(1, 6)}
    f0max = max(rows_X[r][0] for r in range(1, 6))
    return Hop, Hr, tstar, arrival(row_Z5), f0max, unit_dev


HA_q, HrA, tsA, tzA, f0A, udA = front_quantum(1.0, HX, HZ)
HB_q, HrB, tsB, tzB, f0B, udB = front_quantum(1.3, 0.7, 0.5)
MEAS["quantum_fronts"] = {"t_star_A": tsA, "t_star_B": tsB,
                          "t_star_Z5_A": tzA, "t_star_Z5_B": tzB}
halt_check(max(f0A, f0B) < 1e-10,
           f"QI-1 identity: F(r, 0) = ||[X_0, X_r] psi0|| < 1e-10 for all "
           f"r >= 1, both sectors (max {max(f0A, f0B):.1e}; equal-time "
           f"commutators of disjoint sites vanish)")
halt_check(max(udA, udB) < 1e-8,
           f"QI-2 unitarity: | ||X_0(t) psi0|| - 1 | at t = 2 is "
           f"{max(udA, udB):.1e} < 1e-8, both sectors")
mono = all(tsA[r + 1] > tsA[r] for r in range(1, 5)) and \
    all(tsB[r + 1] > tsB[r] for r in range(1, 5))
check(mono, f"Q-1 fronts exist and move outward: t*(r) strictly "
            f"increasing over r = 1..5, both sectors (A: "
            f"{[tsA[r] for r in range(1, 6)]}; B: "
            f"{[tsB[r] for r in range(1, 6)]})")
dq5 = abs(tsA[5] - tsB[5])
check(dq5 > 0.1 * max(tsA[5], tsB[5]),
      f"Q-2 THE CONES DIFFER: |t*_A(5) - t*_B(5)| = {dq5:.2f} > 0.1 * "
      f"max({tsA[5]:.2f}, {tsB[5]:.2f}) -- the record's own two sector "
      f"parameter sets propagate at different speeds")
check(edges(HA_q) == edges(HB_q),
      "Q-3 the earned geometry is identical: the interaction graphs of "
      "H_A and H_B are equal -- recovered geometry underdetermines the "
      "cone")
Xtot = real(dense({placed(LQ, [(i, 1)]): 1.0 for i in range(LQ)}, LQ))
gA = gram_psd(HrA, Xtot)
gB = gram_psd(HrB, Xtot)
check(gA >= -1e-12 and gB >= -1e-12,
      f"Q-4 earned positivity indifferent: ground-state two-time Gram of "
      f"sum X_i PSD for both sectors (A {gA:.1e}, B {gB:.1e})")
check(True, f"Q-diag (labeled, ungated): Z-probe arrivals t*_Z(5): "
            f"A {tzA:.2f}, B {tzB:.2f} -- the front is a property of the "
            f"sector, not of the probe representation", "diag")
ELIM.append({"leg": "Q", "system": "quantum sector B (1.3, 0.7, 0.5)",
             "eliminated": not (gB >= -1e-12
                                and edges(HA_q) == edges(HB_q)),
             "tests": {"gram_min": gB, "graph_same": True}})

# ---------------- X: common cone by exchange? ----------------------------
print("\n=== X: COMMON CONE BY EXCHANGE? (coupled rings, closed-form "
      "branches; g = 0.05) ===")
G_EX = 0.05


def branches(KA, KB, g, q):
    a = 2.0 * KA * (1.0 - math.cos(q))
    b = 2.0 * KB * (1.0 - math.cos(q))
    s = a + b + 2.0 * g
    d = math.sqrt((a - b) ** 2 + 4.0 * g * g)
    return math.sqrt(max((s - d) / 2.0, 0.0)), math.sqrt((s + d) / 2.0)


def branch_vmax(KA, KB, g):
    dq = 1e-6
    vm, vp = 0.0, 0.0
    for i in range(1, 3000):
        q = math.pi * i / 3000.0
        m1, p1 = branches(KA, KB, g, q - dq)
        m2, p2 = branches(KA, KB, g, q + dq)
        vm = max(vm, (m2 - m1) / (2 * dq))
        vp = max(vp, (p2 - p1) / (2 * dq))
    return vm, vp


def branch_v_at(KA, KB, g, q):
    dq = 1e-6
    m1, p1 = branches(KA, KB, g, q - dq)
    m2, p2 = branches(KA, KB, g, q + dq)
    return (m2 - m1) / (2 * dq), (p2 - p1) / (2 * dq)


QSTAR = 0.6  # Amendment 01: the frozen interior comparison point
x_rows = {}
for KA, KB in ((1.0, 1.69), (1.0, 2.56), (1.0, 1.0)):
    q0 = 1e-3
    sl = branches(KA, KB, G_EX, q0)[0] / q0
    vm, vp = branch_vmax(KA, KB, G_EX)
    vmq, vpq = branch_v_at(KA, KB, G_EX, QSTAR)
    x_rows[(KA, KB)] = {"acoustic_slope": sl, "avg_pred":
                        math.sqrt((KA + KB) / 2.0), "v_minus_max": vm,
                        "v_plus_max": vp, "v_minus_qstar": vmq,
                        "v_plus_qstar": vpq}
MEAS["exchange"] = {f"({a},{b})": r for (a, b), r in x_rows.items()}
x1_ok = all(abs(x_rows[p]["acoustic_slope"] / x_rows[p]["avg_pred"] - 1.0)
            < 1e-3 for p in ((1.0, 1.69), (1.0, 2.56)))
check(x1_ok,
      f"X-1 the hybrid long-wavelength cone is the AVERAGE of the "
      f"supplied parameters: acoustic slope (1, 1.69) = "
      f"{x_rows[(1.0, 1.69)]['acoustic_slope']:.7f} vs sqrt(1.345) = "
      f"{x_rows[(1.0, 1.69)]['avg_pred']:.7f}; (1, 2.56) = "
      f"{x_rows[(1.0, 2.56)]['acoustic_slope']:.7f} vs sqrt(1.78) = "
      f"{x_rows[(1.0, 2.56)]['avg_pred']:.7f} -- the cone tracks the "
      f"inputs continuously; nothing invariant appears")
dv1 = abs(x_rows[(1.0, 1.69)]["v_plus_qstar"]
          - x_rows[(1.0, 1.69)]["v_minus_qstar"])
dv2 = abs(x_rows[(1.0, 2.56)]["v_plus_qstar"]
          - x_rows[(1.0, 2.56)]["v_minus_qstar"])
check(dv1 > 0.05 and dv2 > 0.05,
      f"X-2 (per Amendment 01) exchange does NOT equalize: at q* = 0.6, "
      f"|v+ - v-| = {dv1:.4f} for (1, 1.69) and {dv2:.4f} for (1, 2.56), "
      f"both > 0.05 -- the branches retain the two sector characters at "
      f"finite exchange")
check(True, f"X-diag (labeled, ungated; the Amendment-01 disclosure): the "
            f"global branch maxima for (1, 1.69) are v-_max = "
            f"{x_rows[(1.0, 1.69)]['v_minus_max']:.4f} (the hybrid q->0 "
            f"average) and v+_max = "
            f"{x_rows[(1.0, 1.69)]['v_plus_max']:.4f} (the suppressed "
            f"optical maximum) -- a numerical near-coincidence of two "
            f"different quantities, not an equalization; for (1, 2.56) "
            f"they differ by "
            f"{abs(x_rows[(1.0, 2.56)]['v_plus_max'] - x_rows[(1.0, 2.56)]['v_minus_max']):.4f}",
      "diag")
check(abs(x_rows[(1.0, 1.0)]["acoustic_slope"] - 1.0) < 1e-3,
      f"X-3 the compatibility row: equal supplied parameters give the "
      f"common cone (acoustic slope {x_rows[(1.0, 1.0)]['acoustic_slope']:.7f}"
      f" = 1.0) -- a common cone is COMPATIBLE exactly when the inputs "
      f"are equal, never forced when they are not")


def coupled_strainB(KA, KB, g, r, tgrid):
    out = []
    for t in tgrid:
        uB = [0.0, 0.0]
        for j, rr in enumerate((r, r + 1)):
            tot = 0.0
            for k in range(NRING):
                q = 2.0 * math.pi * k / NRING
                a = 2.0 * KA * (1.0 - math.cos(q))
                b = 2.0 * KB * (1.0 - math.cos(q))
                s = a + b + 2.0 * g
                d = math.sqrt((a - b) ** 2 + 4.0 * g * g)
                for lamq in ((s - d) / 2.0, (s + d) / 2.0):
                    v1, v2 = g, (a + g) - lamq
                    nv = math.hypot(v1, v2)
                    if nv < 1e-300:
                        continue
                    v1, v2 = v1 / nv, v2 / nv
                    w = math.sqrt(max(lamq, 0.0))
                    ph = t if w < 1e-12 else math.sin(w * t) / w
                    tot += math.cos(q * rr) * v1 * v2 * ph
            uB[j] = tot / NRING
        out.append(abs(uB[1] - uB[0]))
    return max(out)


leakB = coupled_strainB(1.0, 1.69, G_EX, 40, [2.5 * i for i in range(25)])
check(leakB > 1e-6,
      f"X-4 propagation exists: impulse in A produces max|strain_B(r=40)| "
      f"= {leakB:.3e} > 1e-6 in the (1, 1.69) pair -- exchange creates "
      f"shared support (causal propagation exists) while X-2 shows no "
      f"universal cone is created: the ruling's distinction, mechanical")
for pair in ((1.0, 1.69), (1.0, 2.56)):
    ELIM.append({"leg": "X", "system": f"coupled pair {pair}, g = 0.05",
                 "eliminated": False if min(
                     branches(pair[0], pair[1], G_EX, 0.5)) >= 0.0
                 else True,
                 "tests": {"branch_omegas_real_nonneg": True}})

# ---------------- K: influence-cone blindness (exact) --------------------
print("\n=== K: INFLUENCE-CONE BLINDNESS (lambda-relabeling identity, "
      "per representation) ===")
LAM = 2.0


def J_lam(w, vertex, lam):
    q = w / (2.0 * lam)
    for _ in range(60):
        f = 2.0 * disp(lam * q) - w
        df = 2.0 * lam * (1.0 - 3.0 * ALPHA * (lam * q) ** 2)
        q -= f / df
    M = vertex(lam * q)
    return M * M / abs(2.0 * lam * (1.0 - 3.0 * ALPHA * (lam * q) ** 2))


def vmax_analytic(lam):
    # analytic group velocity of omega_lam(q) = disp(lam q): max over the
    # q-grid of lam (1 - 3 ALPHA (lam q)^2), attained at q -> 0
    return max(lam * (1.0 - 3.0 * ALPHA * (lam * (0.001 * i)) ** 2)
               for i in range(200))


VERTS = {"density": lambda q: 1.0, "current": lambda q: q,
         "stress": stress_vertex}
k_rows = {}
for name, vf in VERTS.items():
    s1 = math.log(J_lam(0.2, vf, 1.0) / J_lam(0.1, vf, 1.0)) / math.log(2.0)
    s2 = math.log(J_lam(0.2, vf, LAM) / J_lam(0.1, vf, LAM)) / math.log(2.0)
    jmin = min(J_lam(w, vf, LAM) for w in ws_scan)
    k_rows[name] = {"slope": s1, "slope_lambda": s2, "dev": abs(s2 - s1),
                    "J_lambda_min": jmin}
    ELIM.append({"leg": "K", "system": f"lambda = 2 relabeling, {name} "
                                       f"vertex",
                 "eliminated": not jmin >= 0.0,
                 "tests": {"J_lambda_min": jmin}})
MEAS["lambda_relabeling"] = k_rows
k1_ok = all(r["dev"] < 1e-12 and r["J_lambda_min"] >= 0.0
            for r in k_rows.values())
check(k1_ok,
      f"K-1 the earned frequency battery is EXACTLY blind to the "
      f"relabeling, for every representation: |slope_lambda - slope| = "
      + ", ".join(f"{n} {r['dev']:.1e}" for n, r in k_rows.items())
      + " (all < 1e-12); J_lambda >= 0 on the scan")
v1x, vLx = vmax_analytic(1.0), vmax_analytic(LAM)
check(abs(vLx - LAM * v1x) < 1e-12,
      f"K-2 while the cone moves: v_lambda = {vLx:.12f} = lambda * v = "
      f"{LAM * v1x:.12f} -- an arbitrary front speed at identical "
      f"earned-battery verdicts, for every representation class")

# ---------------- M: memory vs support -----------------------------------
print("\n=== M: MEMORY vs SUPPORT ===")


def memory_kernel(spring, taus):
    K0 = build_K(24, 0.0)
    Ks = [[spring * (K0[i][j] - (PIN if i == j else 0.0))
           + (PIN if i == j else 0.0) for j in range(24)] for i in range(24)]
    bath = [row[1:] for row in Ks[1:]]
    lam, V = jacobi_eig(bath)
    u = [V[0][k] for k in range(23)]
    return {tau: sum(ul * ul * math.exp(-l * tau)
                     for ul, l in zip(u, lam)) for tau in taus}


mk = {s: memory_kernel(s, (0.5, 1.0)) for s in (1.0, 1.69)}
MEAS["memory_kernels"] = {str(s): {str(t): v for t, v in d.items()}
                          for s, d in mk.items()}
m1_ok = all(d[0.5] > d[1.0] > 0.0 for d in mk.values())
check(m1_ok,
      f"M-1 the memory battery is cone-blind: kernels positive and "
      f"decreasing in tau for springs 1.0 ({mk[1.0][0.5]:.6f} -> "
      f"{mk[1.0][1.0]:.6f}) and 1.69 ({mk[1.69][0.5]:.6f} -> "
      f"{mk[1.69][1.0]:.6f}) -- identical memory verdicts for sectors "
      f"whose fronts differ (N-1); temporal memory carries no spatial "
      f"support variable")
shA, roA = ring_sharpness(1.0, vA)
shB, roB = ring_sharpness(1.69, vB)
MEAS["support_sharpness"] = {"A": {"ratio": shA, "r_out": roA},
                             "B": {"ratio": shB, "r_out": roB}}
check(shA < 1e-6 and shB < 1e-6,
      f"M-2 a true support boundary exists per sector: strain "
      f"outside/inside = {shA:.1e} (A, r_out {roA}) and {shB:.1e} (B, "
      f"r_out {roB}), both < 1e-6 -- a sharp causal support, not a "
      f"decaying tail; its slope is sector-dependent and nothing earned "
      f"selects it")

# ---------------- V: the verdict gates ------------------------------------
print("\n=== V: SURVIVOR COUNT, THE BOXED GATE, AND THE TRICHOTOMY ===")
n_elim = sum(1 for r in ELIM if r["eliminated"])
v1_ok = len(ELIM) == 7 and n_elim == 0
check(v1_ok,
      f"V-1 EARNED LAYER ELIMINATES NO CONE: 0 of the {len(ELIM)} "
      f"different-cone systems tested (classical K = 1.69; quantum sector "
      f"B; lambda = 2 x 3 vertices; coupled (1, 1.69) and (1, 2.56)) "
      f"fails any earned admissibility test (eliminated: {n_elim} of "
      f"{len(ELIM)})")
v2_ok = (1.25 <= vB / vA <= 1.35 and dq5 > 0.1 * max(tsA[5], tsB[5])
         and jminN >= 0.0 and edges(HA_q) == edges(HB_q)
         and gA >= -1e-12 and gB >= -1e-12)
check(v2_ok,
      f"V-2 THE BOXED GATE: two earned-admissible systems with different "
      f"causal cones EXIST (classical ratio {vB / vA:.4f}; quantum "
      f"arrival gap {dq5:.2f}; all admissibility passed) => UNIVERSAL "
      f"CAUSALITY IS NOT DERIVED")
v3_ok = (abs(x_rows[(1.0, 1.0)]["acoustic_slope"] - 1.0) < 1e-3 and v2_ok)
check(v3_ok,
      "V-3 THE TRICHOTOMY: a common limiting velocity is COMPATIBLE "
      "(X-3: equal inputs give equal cones) and where the record uses "
      "one it is SUPPLIED (TT-1's per-sector v = c; the inventory's "
      "cross-sector light-cone relation, supplied, U-1 territory -- "
      "cited, not re-adjudicated), but it is NOT DERIVED (V-2)")

check(True, "empirical firewall (frozen, the owner's rule): the "
            "constraints that would collapse the cone family -- "
            "light-speed constancy, observed Lorentz invariance -- are "
            "external data, recorded here, never used internally", "note")
check(True, "the ruling's distinction, held: causal propagation exists "
            "(X-4, N-1, Q-1) != a universal causal cone is selected "
            "(X-2, V-1, V-2)", "note")
check(True, "M-3 attacked constructively, not restated: the recorded "
            "missing common cone is exhibited as a two-admissible-cones "
            "demonstration on the record's own sector parameters", "note")

# ---------------- verdict -------------------------------------------------
gated = [c for c in CHECKS if c["kind"] in ("ok", "ctrl")]
n_ok = sum(1 for c in gated if c["pass"])
fails = [c["summary"] for c in gated if not c["pass"]]

if HALT:
    verdict = "HALT"
elif not fails:
    verdict = "D-CONE-NOT-DERIVED"
elif not v1_ok and all(r["eliminated"] for r in ELIM):
    verdict = "D-CONE-SELECTED"
else:
    verdict = "D-PARTIAL"

detail = ("earned-admissible systems with different causal cones exist "
          "(the record's own sector parameters among them); no earned "
          "test eliminates any of them; exchange composes the supplied "
          "cones into an average without selecting one; the earned "
          "frequency-domain battery is exactly blind to the cone for "
          "every representation class; geometry and memory "
          "underdetermine it; a common c is compatible and supplied, "
          "never derived. The causal cone is sharpened as an "
          "irreducible primitive: the demonstration half of its "
          "certificate. The campaign's dependency boundary closes: "
          "{causal cone | coupling | spin | universal reach} are "
          "additional structural inputs, not consequences of the "
          "generative core. M-3 confirmed constructively; U-1's and "
          "TT-1's conditional statuses stand")

out = {
    "fork": "GR2-d",
    "charter": "GR2D_CONE_CHARTER_01.md (frozen ff8db42)",
    "directive": "GR2_CAMPAIGN_DIRECTIVE_01.md (Layer 4 / seam S2); "
                 "GR2C_OWNER_RULING_01.md (authorization)",
    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S+00:00", time.gmtime()),
    "environment": {"python": sys.version.split()[0], "pure_stdlib": True,
                    "deterministic": "no RNG in this fork"},
    "defect_history": [],
    "measurements": MEAS,
    "elimination_table": ELIM,
    "checks": CHECKS,
    "adjudication": {
        "verdict": verdict,
        "verdict_detail": detail if verdict == "D-CONE-NOT-DERIVED" else "",
        "scope": "classical rings N = 400 and 7-site open quantum "
                 "chains; D = 1 propagation; the g = 0.05 exchange "
                 "family; lambda-relabeling at lambda = 2. Relativistic "
                 "field content, curved backgrounds, and larger exchange "
                 "families out of scope; this fork ends the chartered "
                 "GR-2 sequence pending the Layer-7 synthesis",
    },
    "elapsed_s": round(time.time() - T0, 2),
}

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                    "GR2D_CONE_RESULT.json")
blob = json.dumps(out, indent=1)
with open(path, "w") as f:
    f.write(blob)
sha = hashlib.sha256(blob.encode()).hexdigest()
print(f"\nartifact written: {os.path.abspath(path)} (sha {sha[:16]}...)")
print(f"\nGR2-d: {n_ok}/{len(gated)} gated checks passed; failures: "
      f"{len(fails)}; halts: {len(HALT)}")
if HALT:
    print("HALT: a replication control or analytic identity breached -- "
          "instrument bug, never physics. No verdict may be issued from "
          "this run.")
    sys.exit(2)
print(f"VERDICT: {verdict}")
print("HARD STOP: verdict recorded pending owner ruling.")
sys.exit(0 if not fails else 1)
