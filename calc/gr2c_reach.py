#!/usr/bin/env python3
"""GR2-c -- universal reach (frozen instrument).

Charter: GR2C_REACH_CHARTER_01.md, frozen at commit c12edfd, under the
GR-2 campaign directive (Layer 3) and the GR2-b owner ruling.

Question (the owner's, frozen): does anything genuinely earned by the
GRUT core force every retained sector to couple universally to the
proposed gravitational response (g1 = g2 = ... = gN)?

Discipline (frozen): an assignment is ELIMINATED only if an earned
admissibility test fails on it (joint-cone PSD, ground-state two-time
Gram PSD, interaction-graph change, normalized-shape change); the joint
discriminator measures distinguishability, which is labeling, never
elimination. Compatible != selected. Empirical eliminators (universal
attraction, light bending, Eotvos-type universality) stay OUTSIDE the
record and are not introduced as domain data.

Machinery: the U-1 universality legs replicated exactly (same helpers,
same seed 20260925, same loop order) as halt-grade controls; the GR-1
L-X stress-source pair kernel as J0. Pure stdlib. Deterministic.
Single run. Run: python3 calc/gr2c_reach.py
(writes ../GR2C_REACH_RESULT.json)
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
from s41_sel4 import (ladder_H, dense, evo_setup, discriminator, gram_psd,
                      edges, op_add, spectrum, shape, placed, HX, HZ)
from u1_universality import EPS_B, HP, SEED, expect_series, eye, kron, lin, real

T0 = time.time()
CHECKS = []
HALT = []


def check(ok, msg, kind="ok"):
    CHECKS.append({"kind": kind, "pass": bool(ok), "summary": msg})
    tag = {"ok": "GATE", "ctrl": "CONTROL", "note": "NOTE"}[kind]
    print(("PASS " if ok else "FAIL ") + tag + ": " + msg)


def halt_check(ok, msg):
    check(ok, msg, "ctrl")
    if not ok:
        HALT.append(msg)


MEAS = {}
ELIM = []  # one row per tested coupling assignment (admissibility only)

# ---------------- RU-1/RU-2: U-1 L-C joint discriminator (exact) --------
print("=== RU: U-1 REPLICATION CONTROLS (halt-grade; deterministic / seed "
      "20260925, exact order) ===")
L, N = 3, 6
HA, HB, V = ladder_H(L, 0.0)
H = op_add(HA, HB)
O = op_add(HA, HB, EPS_B)
Hm, Om = dense(H, N), dense(O, N)
Hr, Or = real(Hm), real(Om)
psi = (1 << 3) | (1 << 4) | (1 << 5)
obs = [(1 if (b & 1) == 0 else -1) * (1 if ((b >> 3) & 1) == 0 else -1)
       for b in range(2 ** N)]
ts = [10.0 * i / 40 for i in range(41)]
base = evo_setup(Hr, psi, obs)
uni = evo_setup([[x * (1 + HP) for x in r] for r in Hr], psi, obs)
non = evo_setup(lin(Hr, Or, 1.0, HP), psi, obs)
du, cu = discriminator(base, uni, ts)
dn, cn2 = discriminator(base, non, ts)
halt_check(abs(du - 1.84297022087776e-14) < 1e-12,
           f"RU-1 L-C universal probe: joint Delta {du:.6e} replicates the "
           f"recorded 1.84297022087776e-14")
halt_check(abs(dn - 0.04947765826773509) < 1e-9,
           f"RU-2 L-C non-universal probe (eps_B = 0.6): joint Delta "
           f"{dn:.12f} replicates the recorded 0.04947765826773509")
MEAS["LC_replication"] = {"Delta_universal": du, "Delta_nonuniversal": dn}

# ---------------- RU-3: U-1 L-G soft-emission gauge variation (exact) ---
rng = random.Random(SEED)
kA, kB = 1.0, EPS_B
vI, vIIne, vIIeq = 0.0, float("inf"), 0.0


def rv():
    return [rng.gauss(0, 1) for _ in range(4)]


for _ in range(100):
    a1, a2 = rv(), rv()
    a3 = [-(x + y) for x, y in zip(a1, a2)]
    b1, b2 = rv(), rv()
    b3 = [-(x + y) for x, y in zip(b1, b2)]
    SA = [a1[i] + a2[i] + a3[i] for i in range(4)]
    SB = [b1[i] + b2[i] + b3[i] for i in range(4)]
    var = [kA * SA[i] + kB * SB[i] for i in range(4)]
    vI = max(vI, max(abs(x) for x in var))
    a3x = rv()
    SA2 = [a1[i] + a2[i] + a3x[i] for i in range(4)]
    b3x = [-SA2[i] - b1[i] - b2[i] for i in range(4)]
    SB2 = [b1[i] + b2[i] + b3x[i] for i in range(4)]
    ne = [kA * SA2[i] + kB * SB2[i] for i in range(4)]
    eq = [kA * SA2[i] + kA * SB2[i] for i in range(4)]
    vIIne = min(vIIne, max(abs(x) for x in ne))
    vIIeq = max(vIIeq, max(abs(x) for x in eq))
halt_check(vI == 0.0 and abs(vIIne - 0.1297458179916556) < 1e-9
           and abs(vIIeq - 8.881784197001252e-16) < 1e-15,
           f"RU-3 L-G gauge variation replicates: classI_max {vI:.1e} "
           f"(recorded 0.0), classII_min_neq {vIIne:.12f} (recorded "
           f"0.1297458179916556), classII_max_eq {vIIeq:.6e} (recorded "
           f"8.881784197001252e-16)")
MEAS["LG_replication"] = {"classI_max": vI, "classII_min_neq": vIIne,
                          "classII_max_eq": vIIeq}

# ---------------- RU-4/RU-5 + E: the U-1 L-D probe system ---------------
Ns = 4


def sector(sites, J, hx, hz):
    op = {placed(Ns, [(sites[0], 3), (sites[1], 3)]): J}
    for s in sites:
        op = op_add(op, {placed(Ns, [(s, 1)]): hx})
        op = op_add(op, {placed(Ns, [(s, 3)]): hz})
    return op


HA2 = sector((0, 1), 1.0, HX, HZ)
HB2 = sector((2, 3), 1.3, 0.7, 0.5)
XA = op_add({placed(Ns, [(0, 1)]): 1.0}, {placed(Ns, [(1, 1)]): 1.0})
XB = op_add({placed(Ns, [(2, 1)]): 1.0}, {placed(Ns, [(3, 1)]): 1.0})
HAm, HBm = real(dense(HA2, Ns)), real(dense(HB2, Ns))
XAm, XBm = real(dense(XA, Ns)), real(dense(XB, Ns))
nb = 5
b = [[0.0] * nb for _ in range(nb)]
for n in range(1, nb):
    b[n - 1][n] = math.sqrt(n)
bpb = [[b[i][j] + b[j][i] for j in range(nb)] for i in range(nb)]
nnum = [[float(i) if i == j else 0.0 for j in range(nb)] for i in range(nb)]
I5 = eye(nb)
Hsec = kron(lin(HAm, HBm), I5)
Hprobe = kron(eye(16), nnum)
HA_full = kron(HAm, I5)
HB_full = kron(HBm, I5)
psi2 = [0.0] * (16 * nb)
psi2[0] = 1.0


def probe_run(OA, OB, gA, gB):
    coup = kron(lin(OA, OB, gA, gB), bpb)
    Hf = lin(lin(Hsec, Hprobe), coup)
    d = len(Hf)
    AB = [[sum(HA_full[i][k] * Hf[k][j] for k in range(d)) for j in range(d)]
          for i in range(d)]
    BA = [[sum(Hf[i][k] * HA_full[k][j] for k in range(d)) for j in range(d)]
          for i in range(d)]
    cn = max(abs(AB[i][j] - BA[i][j]) for i in range(d) for j in range(d))
    f = expect_series(Hf, psi2, HB_full)
    vals = [f(t) for t in ts]
    return coup, Hf, cn, max(vals) - min(vals)


_, _, cn_clk, var_clk = probe_run(HAm, HBm, 0.3, 0.18)
halt_check(abs(cn_clk - 8.881784197001252e-16) < 1e-15
           and abs(var_clk - 7.549516567451064e-15) < 1e-13,
           f"RU-4 L-D clock-only probe replicates: ||[H_A, H_full]|| = "
           f"{cn_clk:.6e} (recorded 8.881784197001252e-16), <H_B> variation "
           f"{var_clk:.6e} (recorded 7.549516567451064e-15)")
MEAS["LD_clock_replication"] = {"comm_HA": cn_clk, "HB_variation": var_clk}

# ---------------- RL-1: the L-X stress-source kernel (J0) --------------
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
           f"recorded 8.005419679013105 -- J0 is this channel's kernel")
MEAS["LX_stress_slope"] = s_stress

# ---------------- E: the exchange-grid leg ------------------------------
print("\n=== E: EXCHANGE GRID (U-1 L-D system, X-type coupling; do EARNED "
      "gates care about g_A = g_B?) ===")
E_PAIRS = [(0.3, 0.18), (0.3, 0.3), (0.3, 0.03), (0.3, 0.6)]
e_rows = {}
for gA, gB in E_PAIRS:
    coup, Hf, cn, var = probe_run(XAm, XBm, gA, gB)
    gmin = gram_psd(Hf, coup)
    e_rows[(gA, gB)] = {"comm_HA": cn, "HB_variation": var, "gram_min": gmin}
    if (gA, gB) != (0.3, 0.3):
        ELIM.append({"leg": "E", "assignment": f"(g_A, g_B) = ({gA}, {gB})",
                     "eliminated": not gmin >= -1e-12,
                     "tests": {"gram_min": gmin}})
MEAS["exchange_grid"] = {f"({gA},{gB})": r for (gA, gB), r in e_rows.items()}
r0 = e_rows[(0.3, 0.18)]
halt_check(abs(r0["comm_HA"] - 2.1708000000000003) < 1e-9
           and abs(r0["HB_variation"] - 0.30270478920041) < 1e-9,
           f"RU-5 L-D non-conserved probe at (0.3, 0.18) replicates: "
           f"||[H_A, H_full]|| = {r0['comm_HA']:.12f} (recorded "
           f"2.1708000000000003), <H_B> variation "
           f"{r0['HB_variation']:.12f} (recorded 0.30270478920041)")
e1_ok = all(r["gram_min"] >= -1e-12 for r in e_rows.values())
check(e1_ok, "E-1 earned positivity for EVERY pair: ground-state two-time "
             "Gram of the coupling operator PSD (min eig / scale >= -1e-12: "
             + ", ".join(f"({gA},{gB}) {r['gram_min']:.1e}"
                         for (gA, gB), r in e_rows.items())
             + ") -- equal and unequal couplings pass identically")
e2_ok = all(r["comm_HA"] > 1e-3 and r["HB_variation"] > 1e-4
            for r in e_rows.values())
check(e2_ok, "E-2 the exchange channel functions for EVERY pair: "
             "||[H_A, H_full]|| > 1e-3 and <H_B> variation > 1e-4 ("
             + ", ".join(f"({gA},{gB}) var {r['HB_variation']:.3e}"
                         for (gA, gB), r in e_rows.items())
             + ") -- unequal couplings sustain exchange; nothing earned "
             "degrades or forbids g_A != g_B")

# ---------------- J: the joint cone leg ---------------------------------
print("\n=== J: JOINT MULTI-SECTOR CONE (N = 3; C_ij(w) = g_i g_j J0(w), "
      "rank-1) ===")
GVECS = [(1.0, 1.0, 1.0), (1.0, 0.6, 0.36), (1.0, 0.1, 10.0),
         (1.0, -0.7, 0.2), (2.0, 0.0, 1.0)]
ws = [0.10 + 0.02 * i for i in range(6)]
j_rows = {}
worst_min, worst_id, worst_zero = 0.0, 0.0, 0.0
for g in GVECS:
    g2 = sum(x * x for x in g)
    row_min, row_id, row_zero = 0.0, 0.0, 0.0
    for w in ws:
        J0 = J_of(w, stress_vertex)
        C = [[g[i] * g[j] * J0 for j in range(3)] for i in range(3)]
        # instrument repair (run 2): jacobi_eig's convergence tolerance is
        # ABSOLUTE (1e-12), and C's entries are of order J0 ~ 1e-13..1e-11,
        # so run 1 fed it a matrix below its own tolerance and got the raw
        # diagonal back -- caught by the J-2 identity halt gate. The
        # decomposition is scale-invariant, so normalize by the max entry
        # and rescale the eigenvalues. No gate threshold changed.
        sc = max(abs(x) for r in C for x in r)
        lam, _ = jacobi_eig([[x / sc for x in r] for r in C])
        lam = [x * sc for x in lam]
        lam_s = sorted(lam, key=abs)
        lmax, lmin = max(lam), min(lam)
        row_min = min(row_min, lmin / lmax)
        row_id = max(row_id, abs(lam_s[2] - g2 * J0) / lmax)
        row_zero = max(row_zero, max(abs(lam_s[0]), abs(lam_s[1])) / lmax)
    j_rows[g] = {"min_eig_rel": row_min, "identity_dev_rel": row_id,
                 "zero_eigs_rel": row_zero}
    worst_min = min(worst_min, row_min)
    worst_id = max(worst_id, row_id)
    worst_zero = max(worst_zero, row_zero)
    if g != (1.0, 1.0, 1.0):
        ELIM.append({"leg": "J", "assignment": f"g = {g}",
                     "eliminated": not row_min >= -1e-12,
                     "tests": {"joint_cone_min_eig_rel": row_min}})
MEAS["joint_cone"] = {str(g): r for g, r in j_rows.items()}
check(worst_min >= -1e-12,
      f"J-1 the joint cone admits EVERY assignment: min eig of C(w) >= "
      f"-1e-12 * lambda_max across the grid and the w-scan (worst "
      f"{worst_min:.1e}) -- sign-non-universal (1, -0.7, 0.2) and "
      f"zero-coupling (2, 0, 1) included")
halt_check(worst_id < 1e-9 and worst_zero < 1e-10,
           f"J-2 identity: spectrum of C(w) is {{|g|^2 J0(w), 0, 0}} -- "
           f"max |lambda_max - |g|^2 J0| / lambda_max = {worst_id:.1e} < "
           f"1e-9; max |zero eigs| / lambda_max = {worst_zero:.1e} < 1e-10 "
           f"(halt-grade; GR2-b discipline)")

# ---------------- G: the geometry-blindness grid -------------------------
print("\n=== G: GEOMETRY BLINDNESS (U-1 ladder; graph and shape vs the "
      "assignment) ===")
G_EPS = (0.3, 0.6, 0.9, 1.5)
g_rows = {}
for eps in G_EPS:
    Oe = op_add(HA, HB, eps)
    same = edges(op_add(H, Oe, HP)) == edges(H)
    gmin = gram_psd(Hr, real(dense(Oe, N)))
    g_rows[eps] = {"graph_same": same, "gram_min": gmin}
    ELIM.append({"leg": "G", "assignment": f"O = H_A + {eps} H_B",
                 "eliminated": not (same and gmin >= -1e-12),
                 "tests": {"graph_same": same, "gram_min": gmin}})
MEAS["geometry_grid"] = {str(e): r for e, r in g_rows.items()}
check(all(r["graph_same"] for r in g_rows.values()),
      "G-1 the interaction graph of H + hO_eps equals that of H for every "
      "eps in {0.3, 0.6, 0.9, 1.5} -- the recovered hop geometry is blind "
      "to the coupling assignment")
dshape = max(abs(a - c) for a, c in zip(
    shape(spectrum([[x * (1 + HP) for x in r] for r in Hm])),
    shape(spectrum(Hm))))
MEAS["shape_rescale_dev"] = dshape
check(dshape < 1e-12,
      f"G-2 normalized spectral shape invariant under overall rescale "
      f"(1 + h): deviation {dshape:.1e} < 1e-12 -- the earned geometry "
      f"cannot register an absolute coupling")

# ---------------- O: the observability grid ------------------------------
print("\n=== O: OBSERVABILITY (joint discriminator; observable, never "
      "forbidden) ===")
d_of = {0.6: dn}
for eps in (0.3, 0.9):
    One = evo_setup(lin(Hr, real(dense(op_add(HA, HB, eps), N)), 1.0, HP),
                    psi, obs)
    d_of[eps], _ = discriminator(base, One, ts)
MEAS["observability"] = {str(e): d_of[e] for e in (0.3, 0.6, 0.9)}
check(d_of[0.3] > 1e-3 and d_of[0.9] > 1e-3,
      f"O-1 every tested non-universal assignment is observable by joint "
      f"access: Delta(0.3) = {d_of[0.3]:.6f}, Delta(0.9) = "
      f"{d_of[0.9]:.6f}, both > 1e-3")
check(d_of[0.3] > d_of[0.6] > d_of[0.9],
      f"O-2 the deviation is graded in |1 - eps| and vanishes at the "
      f"universal point (RU-1's 1.8e-14): Delta(0.3) = {d_of[0.3]:.6f} > "
      f"Delta(0.6) = {d_of[0.6]:.6f} > Delta(0.9) = {d_of[0.9]:.6f} -- "
      f"observable, never forbidden")
for eps in (0.3, 0.6, 0.9):
    ELIM.append({"leg": "O", "assignment": f"O = H_A + {eps} H_B (joint "
                                           f"access row)",
                 "eliminated": not (g_rows[eps]["graph_same"]
                                    and g_rows[eps]["gram_min"] >= -1e-12),
                 "tests": {"admissibility": "the G-leg tests at this eps "
                                            "(the discriminator is "
                                            "labeling, not elimination)"}})

# ---------------- V: the verdict gates -----------------------------------
print("\n=== V: SURVIVOR COUNT AND FORCING LOCATION ===")
n_elim = sum(1 for r in ELIM if r["eliminated"])
check(len(ELIM) == 14 and n_elim == 0,
      f"V-1 EARNED LAYER ELIMINATES NOTHING: 0 of the {len(ELIM)} "
      f"non-universal coupling assignments tested (J-leg 4, E-leg 3, "
      f"G-leg 4, O-leg 3) fails any earned admissibility test "
      f"(eliminated: {n_elim} of {len(ELIM)})")
v1_ok = len(ELIM) == 14 and n_elim == 0
v2_ok = (vI == 0.0 and vIIne > 1e-3 and vIIeq < 1e-12 and e1_ok and e2_ok
         and v1_ok)
check(v2_ok,
      f"V-2 FORCING LOCATED IN THE SUPPLIED LAYER: the only mechanism in "
      f"the record that forces g_A = g_B is the supplied massless gauge "
      f"structure, acting only on exchanging sectors (class I free at "
      f"{vI:.1e} with kappa_A != kappa_B; class II forced: min variation "
      f"{vIIne:.4f} for unequal vs {vIIeq:.1e} for equal), while every "
      f"unequal exchange pair passes every EARNED gate -- and reach into "
      f"the exchange component is itself SUPPLIED (U-1's recorded "
      f"residual, cited)")

check(True, "compatible != selected (frozen, the owner's warning): the "
            "universal rows (1,1,1) and (0.3,0.3) passing every earned "
            "gate demonstrates COMPATIBILITY only; selection would require "
            "an earned test failing at some non-universal assignment, and "
            "none does", "note")
check(True, "empirical firewall (frozen, the owner's rule): the "
            "eliminators of non-universal reach -- universal attraction, "
            "light bending, Eotvos-type universality -- are empirical "
            "inputs found nowhere in the record's earned or supplied "
            "layers, and this fork does NOT introduce them as domain "
            "data", "note")
check(True, "sign note (frozen): the joint cone is PSD even for the "
            "sign-non-universal assignment (1, -0.7, 0.2) -- the earned "
            "cone does not force a common coupling SIGN, let alone a "
            "common magnitude", "note")
check(True, "recorded fact carried (frozen): U-1's own exchange-channel "
            "demonstration used UNEQUAL couplings (0.3, 0.18) and passed "
            "every earned gate -- the record already contains a "
            "functioning non-universal exchange channel; access does not "
            "select the assignment (P-6, GR2-b A-leg -- cited, not "
            "re-run)", "note")

# ---------------- verdict ------------------------------------------------
gated = [c for c in CHECKS if c["kind"] in ("ok", "ctrl")]
n_ok = sum(1 for c in gated if c["pass"])
fails = [c["summary"] for c in gated if not c["pass"]]

if HALT:
    verdict = "HALT"
elif not fails:
    verdict = "C-REACH-NOT-FORCED"
elif not v1_ok:
    verdict = "C-REACH-FORCED-IN-CORE"
else:
    verdict = "C-PARTIAL"

detail = ("nothing earned eliminates any non-universal coupling "
          "assignment: the joint cone is rank-1 PSD for every real "
          "coupling vector (signs included), the exchange machinery "
          "functions identically at unequal couplings, the recovered "
          "geometry is blind to the assignment, and joint access "
          "OBSERVES non-universality without forbidding it. The only "
          "forcing of g_A = g_B in the record is the supplied massless "
          "gauge structure, conditional on the sectors exchanging "
          "energy-momentum -- and that every sector sits in the "
          "exchange-coupled component is itself supplied (U-1's "
          "residual). The reach coordinate is sharpened as an "
          "irreducible primitive at this level: the demonstration half "
          "of its certificate, feeding C4 and Layer 7. U-1's "
          "DERIVED-IN-CLASS status for exchanging sectors STANDS")

out = {
    "fork": "GR2-c",
    "charter": "GR2C_REACH_CHARTER_01.md (frozen c12edfd)",
    "directive": "GR2_CAMPAIGN_DIRECTIVE_01.md (Layer 3); "
                 "GR2B_OWNER_RULING_01.md (authorization)",
    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S+00:00", time.gmtime()),
    "environment": {"python": sys.version.split()[0], "pure_stdlib": True,
                    "deterministic": "seeded scans only (seed 20260925)"},
    "defect_history": [
        "Run 1 (2026-09-27, not committed): the joint-cone leg breached "
        "the J-2 analytic identity (spectrum of the rank-1 C(w) must be "
        "{|g|^2 J0, 0, 0}; measured relative deviation 2.0, exactly the "
        "raw-diagonal signature). Cause: jacobi_eig's convergence "
        "tolerance is absolute (1e-12) while C(w)'s entries are of order "
        "J0 ~ 1e-13..1e-11, so the solver returned the unrotated diagonal "
        "-- and run 1's J-1 pass was therefore vacuous. Instrument bug, "
        "never physics; every control and every gate outside the J leg "
        "passed identically in run 1. Repair: the matrix is normalized by "
        "its largest entry before jacobi_eig and the eigenvalues rescaled "
        "(the decomposition is scale-invariant). No gate threshold "
        "changed. Run 2 is the recorded run."
    ],
    "measurements": MEAS,
    "elimination_table": ELIM,
    "checks": CHECKS,
    "adjudication": {
        "verdict": verdict,
        "verdict_detail": detail if verdict == "C-REACH-NOT-FORCED" else "",
        "scope": "the U-1 ladder (L = 3) and two-sector+probe (80-dim) "
                 "systems; N = 3 in the joint cone leg; the L-X pair "
                 "channel as J0; the D = 4 soft-emission algebra. Larger "
                 "sector counts, probe mixtures, and the causal cone out "
                 "of scope (GR2-d)",
    },
    "elapsed_s": round(time.time() - T0, 2),
}

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                    "GR2C_REACH_RESULT.json")
blob = json.dumps(out, indent=1)
with open(path, "w") as f:
    f.write(blob)
sha = hashlib.sha256(blob.encode()).hexdigest()
print(f"\nartifact written: {os.path.abspath(path)} (sha {sha[:16]}...)")
print(f"\nGR2-c: {n_ok}/{len(gated)} gated checks passed; failures: "
      f"{len(fails)}; halts: {len(HALT)}")
if HALT:
    print("HALT: a replication control or analytic identity breached -- "
          "instrument bug, never physics. No verdict may be issued from "
          "this run.")
    sys.exit(2)
print(f"VERDICT: {verdict}")
print("HARD STOP: verdict recorded pending owner ruling.")
sys.exit(0 if not fails else 1)
