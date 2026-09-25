#!/usr/bin/env python3
"""cp1_coupling: can the minimal-stress coupling be selected without inserting it?

CHARTER: CP1_COUPLING_CHARTER_01.md (pre-registration frozen at commit d78f9a4 BEFORE this
instrument ran; authority: owner ruling recorded in GR1_CP1_OWNER_RULING_01.md). The answer
is not presumed. The retained-sector import is held fixed and NOT attacked. omega^7 is not
reopened or relabeled; exponents are compared as classes/increments inside GR-1's own L-X
instrument convention only.

Declared family: V^{mu nu} = a(p1p2 + p2p1) + g(p1p1 + p2p2) + b eta (p1.p2) + c eta.

Legs: L-F exponent map + non-injectivity | L-H 𝔠_full as a selector | L-C conservation null
space (D = 2, 4) | L-W conservation + IR Weyl (tracelessness) | L-TT transverse-traceless
access class | L-M geometric (metric) coupling as a chartered CANDIDATE, with
material-modulation counterfactuals.

Pure stdlib. Run: python3 calc/cp1_coupling.py
"""
import cmath
import hashlib
import json
import math
import os
import random
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from partition_selection_p1 import jacobi_eig
from p3_nc_lift import herm_eigs
from gr1_gravity import ALPHA, disp, slope, Cfun

FAIL = []
CHECKS = []
HALT = []
SEED = 20260925
CANON = (1.0, 0.0, -1.0, 0.0)
IMPROVE = (-1.0, -1.0, 2.0, 0.0)


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


# ---------------- the family in strain-probe kinematics (GR-1 L-X class) ----------------------
def strain_vertex(coef):
    a, g, b, c = coef
    return lambda q: -2 * a * q * q + 2 * g * q * q - b * (disp(q) ** 2 + q * q) + c


def fmt(v):
    return "(" + ", ".join(f"{x:.3g}" for x in v) + ")"


# ---------------- L-F: exponent map + non-injectivity ------------------------------------------
def leg_F():
    print("\n=== L-F: EXPONENT MAP OVER THE DECLARED FAMILY (GR-1 L-X instrument) ===")
    members = [("canonical minimal stress", CANON, 8.0),
               ("improved xi = 0.2", (0.8, -0.2, -0.6, 0.0), 4.0),
               ("on-locus NON-canonical", (0.0, 1.0, 1.0, 0.0), 8.0),
               ("contact c = 0.01", (1.0, 0.0, -1.0, 0.01), 0.0)]
    out = {}
    for name, coef, pred in members:
        s = slope(strain_vertex(coef))
        out[name] = s
        check(abs(s - pred) < 0.2, f"L-F GATE {name} {fmt(coef)}: slope = {s:.3f} "
                                   f"(predicted {pred:.0f} +- 0.2)")
    gr1 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                       "GR1_GRAVITY_RESULT.json")
    ref = json.load(open(gr1))["LX"]["s_full"]
    d = abs(out["canonical minimal stress"] - ref)
    check(d < 1e-9, f"L-F matched control: canonical slope reproduces GR-1's recorded "
                    f"s_full = {ref:.6f} to {d:.1e} < 1e-9", "ctrl")
    check(True, "L-F consequence (frozen): the on-locus NON-canonical coupling (0,1,1,0) "
                "also lands at 8 -- the +4 is a property of a PLANE of couplings "
                "{c = 0, a - g + b = 0}, not of minimal stress as such. The exponent does "
                "not identify the coupling", "note")
    return out


# ---------------- L-H: 𝔠_full as a selector ----------------------------------------------------
def leg_H():
    print("\n=== L-H: THE ADMISSIBLE HIERARCHY AS A SELECTOR (expected NULL) ===")
    verts = [("canonical", strain_vertex(CANON)),
             ("improved xi = 0.2", strain_vertex((0.8, -0.2, -0.6, 0.0))),
             ("contact c = 0.01", strain_vertex((1.0, 0.0, -1.0, 0.01))),
             ("mass-only material modulation", lambda q: -0.5 * disp(q) ** 2)]
    n = 30
    lo, hi = 0.05, 1.0
    dw = (hi - lo) / (n - 1)
    oms = [lo + dw * i for i in range(n)]
    res = {}
    from gr1_gravity import root_q
    for name, V in verts:
        g2 = []
        for w in oms:
            q = root_q(w)
            g2.append(V(q) ** 2 / abs(2.0 * (1.0 - 3.0 * ALPHA * q * q)) * dw)
        C0 = sum(g2)
        ts = (0.0, 4.0, 11.0)
        M = [[Cfun(oms, g2, ts[i] - ts[j]) for j in range(3)] for i in range(3)]
        mn = min(herm_eigs(M)) / C0
        res[name] = mn
        check(mn >= -1e-12, f"L-H GATE {name}: two-time Gram PSD, min eig / C0 = "
                            f"{mn:.2e} >= -1e-12")
    check(True, "L-H consequence (frozen): every coupling in the family -- minimal, "
                "improved, contact, material -- is 𝔠_full-admissible. The admissible "
                "hierarchy constrains realizability, not the coupling form: NULL as a "
                "selector", "note")
    return res


# ---------------- tensor machinery for L-C / L-W / L-TT ---------------------------------------
def eta(D):
    return [-1.0] + [1.0] * (D - 1)


def dot(p, r, D):
    e = eta(D)
    return sum(e[m] * p[m] * r[m] for m in range(D))


def basis_tensors(p1, p2, D):
    e = eta(D)
    s = dot(p1, p2, D)
    Ta = [[p1[m] * p2[n] + p2[m] * p1[n] for n in range(D)] for m in range(D)]
    Tg = [[p1[m] * p1[n] + p2[m] * p2[n] for n in range(D)] for m in range(D)]
    Tb = [[(e[m] if m == n else 0.0) * s for n in range(D)] for m in range(D)]
    Tc = [[(e[m] if m == n else 0.0) for n in range(D)] for m in range(D)]
    return [Ta, Tg, Tb, Tc]


def random_pairs(D, n, rng):
    out = []
    for _ in range(n):
        ps = []
        for _ in range(2):
            E = rng.uniform(0.2, 2.0)
            if D == 2:
                sgn = 1.0 if rng.random() < 0.5 else -1.0
                ps.append([E, E * sgn])
            else:
                v = [rng.gauss(0, 1) for _ in range(D - 1)]
                nv = math.sqrt(sum(x * x for x in v))
                ps.append([E] + [E * x / nv for x in v])
        out.append(tuple(ps))
    return out


def cons_rows(pairs, D):
    e = eta(D)
    rows = []
    for p1, p2 in pairs:
        k = [p1[m] + p2[m] for m in range(D)]
        Ts = basis_tensors(p1, p2, D)
        for nu in range(D):
            rows.append([sum(e[m] * k[m] * T[m][nu] for m in range(D)) for T in Ts])
    return rows


def trace_rows(pairs, D):
    e = eta(D)
    rows = []
    for p1, p2 in pairs:
        Ts = basis_tensors(p1, p2, D)
        rows.append([sum(e[m] * T[m][m] for m in range(D)) for T in Ts])
    return rows


def null_space(rows):
    G = [[sum(r[i] * r[j] for r in rows) for j in range(4)] for i in range(4)]
    lam, V = jacobi_eig(G)
    mx = max(abs(x) for x in lam)
    null = [[V[i][k] for i in range(4)] for k in range(4) if abs(lam[k]) < 1e-10 * mx]
    worst = max((abs(sum(r[i] * v[i] for i in range(4))) for v in null for r in rows),
                default=0.0)
    return null, worst


def residual(v, null):
    nv = math.sqrt(sum(x * x for x in v))
    u = [x / nv for x in v]
    proj = [0.0] * 4
    for n in null:
        c = sum(u[i] * n[i] for i in range(4))
        proj = [proj[i] + c * n[i] for i in range(4)]
    return math.sqrt(sum((u[i] - proj[i]) ** 2 for i in range(4)))


# ---------------- L-C: conservation ------------------------------------------------------------
def leg_C(rng):
    print("\n=== L-C: CONSERVATION (k_mu V^{mu nu} = 0 on-shell) ===")
    res = {}
    for D in (2, 4):
        pairs = random_pairs(D, 16, rng)
        null, worst = null_space(cons_rows(pairs, D))
        rc, ri = residual(CANON, null), residual(IMPROVE, null)
        check(len(null) == 2, f"L-C GATE D = {D}: conservation null space has nullity "
                              f"{len(null)} (predicted 2); null vectors satisfy every "
                              f"row to {worst:.1e}")
        check(rc < 1e-10 and ri < 1e-10, f"L-C GATE D = {D}: canonical residual {rc:.1e}, "
                                          f"improvement residual {ri:.1e} (both < 1e-10) "
                                          f"-- both are conserved")
        res[D] = {"nullity": len(null), "res_canon": rc, "res_improve": ri}
    check(True, "L-C consequence (frozen): conservation (locality + symmetry) cuts the "
                "family to a 2-dim space = canonical + xi * improvement, and xi spans on- "
                "and off-locus members (L-F: xi = 0.2 -> base). CONSTRAINED-NONUNIQUE", "note")
    return res


# ---------------- L-W: conservation + IR Weyl --------------------------------------------------
def leg_W(rng):
    print("\n=== L-W: CONSERVATION + IR WEYL (tracelessness of the gapless sector) ===")
    res = {}
    for D, pred_dir, pred_slope in ((2, CANON, 8.0), (4, (2.0, -1.0, -1.0, 0.0), 4.0)):
        pairs = random_pairs(D, 16, rng)
        null, worst = null_space(cons_rows(pairs, D) + trace_rows(pairs, D))
        check(len(null) == 1, f"L-W GATE D = {D}: nullity {len(null)} (predicted 1); "
                              f"null vector satisfies every row to {worst:.1e}")
        v = null[0] if null else [0.0] * 4
        rd = residual(pred_dir, [v]) if null else 1.0
        check(rd < 1e-10, f"L-W GATE D = {D}: selected direction {fmt(v)} matches the "
                          f"predicted {fmt(pred_dir)}, residual {rd:.1e} < 1e-10")
        s = slope(strain_vertex(tuple(v)))
        check(abs(s - pred_slope) < 0.2,
              f"L-W GATE D = {D}: strain-probe slope of the Weyl-selected coupling = "
              f"{s:.3f} (predicted {pred_slope:.0f} +- 0.2: "
              f"{'ON' if pred_slope == 8.0 else 'OFF'} the +4 locus)")
        res[D] = {"nullity": len(null), "direction": v, "slope": s, "dir_residual": rd}
    check(True, "L-W consequence (frozen): IR Weyl symmetry of the retained gapless sector "
                "selects a UNIQUE conserved coupling in each D -- in D = 2 it is the "
                "canonical minimal stress (on-locus, +4); in D = 4 it is the improved, "
                "conformally-coupled tensor, which in strain-probe kinematics sits OFF the "
                "locus (base class). The same principle selects different couplings by "
                "dimension", "note")
    return res


# ---------------- L-TT: the transverse-traceless access class ----------------------------------
def leg_TT(rng):
    print("\n=== L-TT: TRANSVERSE-TRACELESS PROBE CLASS (D = 4) ===")
    D = 4
    pairs = random_pairs(D, 16, rng)
    cols = [[], [], [], []]
    worst_bc, worst_ga = 0.0, 0.0
    for p1, p2 in pairs:
        ks = [p1[m] + p2[m] for m in range(1, 4)]
        nk = math.sqrt(sum(x * x for x in ks))
        kh = [x / nk for x in ks]
        P = [[(1.0 if i == j else 0.0) - kh[i] * kh[j] for j in range(3)] for i in range(3)]
        Ts = basis_tensors(p1, p2, D)
        tts = []
        for T in Ts:
            X = [[T[i + 1][j + 1] for j in range(3)] for i in range(3)]
            PX = [[sum(P[i][m] * X[m][j] for m in range(3)) for j in range(3)]
                  for i in range(3)]
            PXP = [[sum(PX[i][m] * P[m][j] for m in range(3)) for j in range(3)]
                   for i in range(3)]
            tr = sum(PX[i][i] for i in range(3))
            tts.append([[PXP[i][j] - 0.5 * P[i][j] * tr for j in range(3)]
                        for i in range(3)])
        scale = max(abs(x) for row in tts[0] for x in row)
        worst_bc = max(worst_bc, max(abs(x) for t in (tts[2], tts[3])
                                     for row in t for x in row) / scale)
        worst_ga = max(worst_ga, max(abs(tts[1][i][j] + tts[0][i][j])
                                     for i in range(3) for j in range(3)) / scale)
        for c in range(4):
            cols[c].extend(tts[c][i][j] for i in range(3) for j in range(3))
    halt_check(worst_bc < 1e-12, f"L-TT GATE: TT(b) = TT(c) = 0, max relative "
                                 f"{worst_bc:.1e} < 1e-12 (halt-grade identity)")
    halt_check(worst_ga < 1e-12, f"L-TT GATE: TT(g) = -TT(a), max relative "
                                 f"{worst_ga:.1e} < 1e-12 (halt-grade identity)")
    G = [[sum(x * y for x, y in zip(cols[i], cols[j])) for j in range(4)] for i in range(4)]
    lam, _ = jacobi_eig(G)
    mx = max(abs(x) for x in lam)
    rank = sum(1 for x in lam if abs(x) > 1e-10 * mx)
    check(rank == 1, f"L-TT GATE: TT image of the entire declared family has rank {rank} "
                     f"(predicted 1) over 16 random pairs")
    check(True, "L-TT consequence (frozen): for transverse-traceless probes the coupling "
                "FORM is forced up to amplitude -- kinetic/gradient weighting, contact and "
                "improvement terms are all invisible. The minimal-stress import is VACUOUS "
                "in the TT access class. Whether the TT channel then carries +4 is "
                "kinematic (v3 territory, NOT re-adjudicated here)", "note")
    return {"rank": rank, "bc_zero": worst_bc, "g_plus_a": worst_ga}


# ---------------- L-M: geometric (metric) coupling as a chartered CANDIDATE --------------------
def D_cont(Q):
    r = cmath.sqrt(Q)
    return (r - ALPHA * r ** 3) ** 2


def D_latt(Q):
    return 4.0 * cmath.sin(cmath.sqrt(Q) / 2.0) ** 2


def dD(Dfun, Q):
    eps = 1e-20
    return (Dfun(complex(Q, eps))).imag / eps  # complex-step: exact to machine precision


def V_metric(Dfun, q):
    Q = q * q
    return 0.5 * (Q * dD(Dfun, Q) - Dfun(Q).real)


def V_metric_fd(Dfun, q, h=1e-5):
    Q = q * q

    def P(hh):
        s = math.sqrt(1.0 + hh)
        return 0.5 * s * (-Dfun(Q).real) - 0.5 * s * Dfun(Q / (1.0 + hh)).real

    return (P(h) - P(-h)) / (2.0 * h)


def latt_slope(V):
    def J(w):
        q = 2.0 * math.asin(w / 4.0)
        return V(q) ** 2 / abs(2.0 * math.cos(q / 2.0))

    return math.log(J(0.2) / J(0.1)) / math.log(2.0)


def leg_M():
    print("\n=== L-M: GEOMETRIC (METRIC) COUPLING -- A CHARTERED CANDIDATE ===")
    Vc = lambda q: V_metric(D_cont, q)
    Vl = lambda q: V_metric(D_latt, q)
    fd = max(abs(V_metric(Df, q) - V_metric_fd(Df, q)) / abs(V_metric(Df, q))
             for Df in (D_cont, D_latt) for q in (0.05, 0.1))
    check(fd < 1e-4, f"L-M control: complex-step metric vertex agrees with an independent "
                     f"finite-difference variation of the action, max rel diff {fd:.1e} "
                     f"< 1e-4", "ctrl")
    sc, sl = slope(Vc), latt_slope(Vl)
    check(abs(sc - 8.0) < 0.2, f"L-M GATE continuum dispersion: metric-coupling slope = "
                               f"{sc:.3f} (predicted 8 +- 0.2)")
    check(abs(sl - 8.0) < 0.2, f"L-M GATE lattice dispersion 4 sin^2(q/2): metric-coupling "
                               f"slope = {sl:.3f} (predicted 8 +- 0.2)")
    q0 = 0.05
    cc = Vc(q0) / q0 ** 4
    cl = Vl(q0) / q0 ** 4
    check(abs(cc / -ALPHA - 1.0) < 0.01, f"L-M GATE continuum coefficient V/q^4 = {cc:.6f} "
                                         f"vs -alpha = {-ALPHA} (within 1%)")
    check(abs(cl / (-1.0 / 24.0) - 1.0) < 0.01, f"L-M GATE lattice coefficient V/q^4 = "
                                                 f"{cl:.6f} vs -1/24 = {-1 / 24:.6f} "
                                                 f"(within 1%)")
    ratio = Vc(q0) / strain_vertex(CANON)(q0)
    check(abs(ratio / 0.5 - 1.0) < 0.01, f"L-M GATE V_metric / V_canonical at q = 0.05 = "
                                         f"{ratio:.6f} (predicted 0.5 within 1%) -- metric "
                                         f"coupling IS canonical minimal stress in the IR")
    zmax = 0.0
    for Df, wfun in ((D_cont, disp), (D_latt, lambda q: 2.0 * math.sin(q / 2.0))):
        for q in (0.05, 0.1, 0.2, 0.4):
            mu, kap = 0.7, -0.7
            Vmat = -0.5 * mu * wfun(q) ** 2 - 0.5 * kap * Df(q * q).real
            zmax = max(zmax, abs(Vmat))
    halt_check(zmax < 1e-14, f"L-M GATE impedance locus (mu = -kappa): material vertex "
                             f"vanishes identically, max |V| = {zmax:.1e} < 1e-14 "
                             f"(both dispersions; halt-grade)")
    s_mass = slope(lambda q: -0.5 * disp(q) ** 2)
    s_stiff = slope(lambda q: -0.5 * D_cont(q * q).real)
    check(abs(s_mass - 4.0) < 0.2 and abs(s_stiff - 4.0) < 0.2,
          f"L-M GATE counterfactuals: mass-only slope {s_mass:.3f}, stiffness-only slope "
          f"{s_stiff:.3f} (both predicted base 4 +- 0.2)")
    check(True, "L-M consequence (frozen): within {mass, stiffness, proper-distance} "
                "modulations of the retained sector, the +4 arises ONLY from "
                "proper-distance (metric) coupling -- material modulations give zero or "
                "base. The minimal-stress import REDUCES to the geometric-coupling "
                "(equivalence) principle at xi = 0. That principle is not already in 𝒯: "
                "a reduction, not a discharge", "note")
    return {"slope_cont": sc, "slope_latt": sl, "coef_cont": cc, "coef_latt": cl,
            "ratio_to_canon": ratio, "impedance_zero": zmax, "s_mass": s_mass,
            "s_stiff": s_stiff, "fd_check": fd}


# ---------------- adjudication (mechanical, from measured results) -----------------------------
def adjudicate(rW, rTT, rM):
    d2 = rW[2]["nullity"] == 1 and abs(rW[2]["slope"] - 8.0) < 0.2
    d4 = rW[4]["nullity"] == 1 and abs(rW[4]["slope"] - 8.0) < 0.2
    tt_vac = rTT["rank"] == 1
    metric_red = abs(rM["slope_cont"] - 8.0) < 0.2 and abs(rM["slope_latt"] - 8.0) < 0.2
    if d2 and d4:
        verdict = "COUPLING-DERIVED"
    elif d2 or d4:
        verdict = "CLASS-SPLIT"
    else:
        verdict = "IRREDUCIBLE-INPUT"
    return {"D2_strain_selected_on_locus": d2, "D4_strain_selected_on_locus": d4,
            "TT_vacuous": tt_vac, "metric_reduction": metric_red, "verdict": verdict,
            "import_discharged": verdict == "COUPLING-DERIVED"}


# ---------------- main -------------------------------------------------------------------------
def main():
    t0 = time.time()
    print("CP-1: CAN MINIMAL STRESS BE SELECTED WITHOUT INSERTING IT? (charter frozen at "
          "d78f9a4)")
    rng = random.Random(SEED)
    rF = leg_F()
    rH = leg_H()
    rC = leg_C(rng)
    rW = leg_W(rng)
    rTT = leg_TT(rng)
    rM = leg_M()
    adj = adjudicate(rW, rTT, rM)

    print("\n=== ADJUDICATION (frozen outcome rule, computed from the measurements) ===")
    check(True, f"Per class: D = 2 strain -- Weyl+conservation selects on-locus: "
                f"{adj['D2_strain_selected_on_locus']}; D = 4 strain -- selects on-locus: "
                f"{adj['D4_strain_selected_on_locus']}; TT class -- form vacuous: "
                f"{adj['TT_vacuous']}; metric-coupling reduction holds: "
                f"{adj['metric_reduction']}", "note")
    check(True, f"VERDICT (mechanical): {adj['verdict']}; conservation alone: "
                f"CONSTRAINED-NONUNIQUE; 𝔠_full: NULL as selector. Minimal-stress import "
                f"discharged: {adj['import_discharged']}", "note")
    check(True, "Class-4 consequence (frozen): the minimal-stress import stays "
                "LOAD-BEARING, restated in reduced form -- geometric (proper-distance) "
                "coupling of the retained sector at xi = 0, where xi = 0 is selected by IR "
                "Weyl in D = 2 but NOT in D = 4 strain kinematics, and is invisible to TT "
                "probes. The retained-sector import was not attacked. Class-4 stays OPEN",
          "note")

    out = {"instrument": "cp1_coupling", "charter_commit": "d78f9a4", "date": "2026-09-25",
           "seed": SEED, "LF": rF, "LH": rH, "LC": rC, "LW": rW, "LTT": rTT, "LM": rM,
           "adjudication": adj, "halts": HALT, "checks": CHECKS, "failures": FAIL,
           "elapsed_s": round(time.time() - t0, 2),
           "hard_stop": "verdict recorded; owner rules on the next layer"}
    path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                         "CP1_COUPLING_RESULT.json"))
    with open(path, "wb") as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True, default=float).encode())
    sha = hashlib.sha256(open(path, "rb").read()).hexdigest()
    print(f"\nartifact written: {path} (sha {sha[:16]}...)")
    n_ok = sum(1 for c in CHECKS if c["ok"])
    print(f"\nCP-1 COUPLING ATTACK: {n_ok}/{len(CHECKS)} checks passed; failures: "
          f"{len(FAIL)}; halts: {len(HALT)}")
    if HALT:
        print("HALT: an analytic identity breached -- instrument bug, never physics. "
              "No verdict may be issued from this run.")
    else:
        print("HARD STOP: verdict recorded pending owner ruling.")
    sys.exit(0 if not FAIL else 1)


if __name__ == "__main__":
    main()
