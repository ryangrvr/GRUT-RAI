#!/usr/bin/env python3
"""eq1_equivalence: can geometric-only coupling be selected from earned structure?

CHARTER: EQ1_EQUIVALENCE_CHARTER_01.md (pre-registration frozen at commit 708a31b BEFORE this
instrument ran; authority GitHub Issue #2 owner comment 5834587876). The equivalence
principle is not inserted: the proper-distance direction G is one of five basis couplings,
and the operational weak-equivalence statement (Sel-4) is a CANDIDATE selector, tested.
Scope 1+1 only; the D = 4 strain/TT split and operator-ordering ambiguity stay open; the
retained sector (both dispersions) is given and not attacked; omega^7/class-4 fenced.

Family (mu, kappa, lambda, sigma, xi) over directions M, K, G, S, X; on-shell pair vertex
V = -1/2[(mu + kappa) D + lambda Q D' + sigma Q^2] - 2 xi D.

Legs: L-X exponent counterattack | L-H 𝔠_full as selector | L-G2 what G-2-recoverable
geometry sees | L-C earned constraints (IR conservation + 2D Weyl) | L-I Sel-4 candidate
(constant-probe intrinsic invisibility) | L-A declared-access underdetermination.

Pure stdlib. Run: python3 calc/eq1_equivalence.py
"""
import hashlib
import json
import math
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from partition_selection_p1 import jacobi_eig
from p3_nc_lift import herm_eigs
from gr1_gravity import ALPHA, slope, root_q, Cfun
from cp1_coupling import D_cont, D_latt, dD, latt_slope

FAIL = []
CHECKS = []
HALT = []
NAMES = ["M", "K", "G", "S", "X"]
GEO = (0.5, 0.5, -1.0, 0.0, 0.0)
S_DIR = (0.0, 0.0, 0.0, 1.0, 0.0)
SPECIES = {
    "A": {"D": D_cont, "slope": slope, "tuned": -2.0 * ALPHA, "qhi": 2.5,
          "label": "continuum alpha = 0.05"},
    "B": {"D": D_latt, "slope": latt_slope, "tuned": -1.0 / 12.0, "qhi": 3.1,
          "label": "lattice 4 sin^2(q/2)"},
}


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


def fmt(v):
    return "(" + ", ".join(f"{x:.3g}" for x in v) + ")"


def vertex(coef, Dfun):
    mu, ka, la, si, xi = coef

    def V(q):
        Q = q * q
        D = Dfun(Q).real
        return -0.5 * ((mu + ka) * D + la * Q * dD(Dfun, Q) + si * Q * Q) - 2.0 * xi * D

    return V


# ---------------- linear-algebra helpers --------------------------------------------------------
def null_space(rows, n):
    G = [[sum(r[i] * r[j] for r in rows) for j in range(n)] for i in range(n)]
    lam, V = jacobi_eig(G)
    mx = max(abs(x) for x in lam)
    null = [[V[i][k] for i in range(n)] for k in range(n) if abs(lam[k]) < 1e-10 * mx]
    worst = max((abs(sum(r[i] * v[i] for i in range(n))) for v in null for r in rows),
                default=0.0)
    return null, worst


def residual(v, null):
    n = len(v)
    nv = math.sqrt(sum(x * x for x in v))
    u = [x / nv for x in v]
    proj = [0.0] * n
    for b in null:
        c = sum(u[i] * b[i] for i in range(n))
        proj = [proj[i] + c * b[i] for i in range(n)]
    return math.sqrt(sum((u[i] - proj[i]) ** 2 for i in range(n)))


def vertex_rank(null, Dfun, qs=(0.05, 0.1, 0.2, 0.4)):
    cols = [[vertex(v, Dfun)(q) for q in qs] for v in null]
    k = len(cols)
    if k == 0:
        return 0, None
    G = [[sum(a * b for a, b in zip(cols[i], cols[j])) for j in range(k)] for i in range(k)]
    lam, _ = jacobi_eig(G)
    mx = max(abs(x) for x in lam)
    rank = sum(1 for x in lam if abs(x) > 1e-10 * mx) if mx > 0 else 0
    best = max(null, key=lambda v: sum(vertex(v, Dfun)(q) ** 2 for q in qs))
    return rank, best


# ---------------- L-X: the exponent counterattack ----------------------------------------------
def leg_X():
    print("\n=== L-X: EXPONENT COUNTERATTACK (does +4 identify geometric coupling?) ===")
    out = {}
    for sp, cfg in SPECIES.items():
        Dfun, sl = cfg["D"], cfg["slope"]
        cases = [("M-only", (1, 0, 0, 0, 0), 4.0, 0.2),
                 ("geometric (1/2,1/2,-1)", GEO, 8.0, 0.2),
                 ("S-only (non-geometric)", S_DIR, 8.0, 0.2),
                 ("tuned geometric + S", (0.5, 0.5, -1.0, cfg["tuned"], 0.0), 12.0, 0.3)]
        if sp == "A":
            cases.append(("X-only", (0, 0, 0, 0, 1), 4.0, 0.2))
        for name, coef, pred, tol in cases:
            s = sl(vertex(coef, Dfun))
            out[f"{sp}:{name}"] = s
            check(abs(s - pred) < tol, f"L-X GATE species {sp} {name} {fmt(coef)}: slope = "
                                       f"{s:.3f} (predicted {pred:.0f} +- {tol})")
    cp1 = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                      "CP1_COUPLING_RESULT.json")))["LM"]["slope_cont"]
    d = abs(out["A:geometric (1/2,1/2,-1)"] - cp1)
    check(d < 1e-9, f"L-X matched control: species-A geometric slope reproduces CP-1's "
                    f"recorded L-M slope {cp1:.6f} to {d:.1e} < 1e-9", "ctrl")
    mk = max(abs(vertex((1, -1, 0, 0, 0), SPECIES[s]["D"])(q))
             for s in SPECIES for q in (0.05, 0.2, 0.6))
    halt_check(mk < 1e-15, f"L-X control: the M - K direction's pair vertex is identically "
                           f"zero, max |V| = {mk:.1e} < 1e-15 (mass and stiffness are "
                           f"pair-vertex-identical on shell)")
    check(True, "L-X consequence (frozen): a NON-geometric dispersion-shape coupling lands "
                "in the same +4 class as geometric coupling on both species, and a "
                "fine-tuned geometric + shape member lands in a +8 class. The exponent "
                "identifies neither geometric coupling nor, strictly, its own class", "note")
    return out


# ---------------- L-H: 𝔠_full as a selector ----------------------------------------------------
def leg_H():
    print("\n=== L-H: THE ADMISSIBLE HIERARCHY AS A SELECTOR (species A; expected NULL) ===")
    n, lo, hi = 30, 0.05, 1.0
    dw = (hi - lo) / (n - 1)
    oms = [lo + dw * i for i in range(n)]
    res = {}
    for name, coef in (("M", (1, 0, 0, 0, 0)), ("geometric", GEO), ("S", S_DIR),
                       ("X", (0, 0, 0, 0, 1)),
                       ("tuned", (0.5, 0.5, -1.0, SPECIES["A"]["tuned"], 0.0))):
        V = vertex(coef, D_cont)
        g2 = []
        for w in oms:
            q = root_q(w)
            g2.append(V(q) ** 2 / abs(2.0 * (1.0 - 3.0 * ALPHA * q * q)) * dw)
        C0 = sum(g2)
        ts = (0.0, 4.0, 11.0)
        M = [[Cfun(oms, g2, ts[i] - ts[j]) for j in range(3)] for i in range(3)]
        mn = min(herm_eigs(M)) / C0
        res[name] = mn
        check(mn >= -1e-12, f"L-H GATE {name}: two-time Gram PSD, min eig / C0 = {mn:.2e}")
    check(True, "L-H consequence (frozen): geometric, material, shape, improvement and "
                "tuned couplings are all 𝔠_full-admissible -- NULL as a selector", "note")
    return res


# ---------------- modulated sector (constant probe) ---------------------------------------------
def modulated(Dfun, coef, h):
    mu, ka, la, si, xi = coef  # xi: constant limit is a total derivative -> no change
    m = 1.0 + mu * h

    def P(Q):
        return (1.0 + ka * h) * Dfun((1.0 + la * h) * Q) + si * h * Q * Q

    return P, m


def dP(P, Q):
    eps = 1e-20
    return P(complex(Q, eps)).imag / eps


# ---------------- L-G2: what the G-2-recoverable geometry sees ---------------------------------
def leg_G2():
    print("\n=== L-G2: WHAT G-2-RECOVERABLE GEOMETRY SEES OF EACH COUPLING (h = 1e-3) ===")
    h = 1e-3
    out = {}
    for sp, cfg in SPECIES.items():
        Dfun = cfg["D"]
        vals = {}
        for i, nm in enumerate(["0"] + NAMES):
            coef = [0.0] * 5
            if nm != "0":
                coef[NAMES.index(nm)] = 1.0
            P, m = modulated(Dfun, coef, h)
            k_ir = dP(P, 1e-12)
            vals[nm] = {"rho": 1.0 / k_ir, "v2": k_ir / m}
        rel = lambda a, b: abs(a / b - 1.0)
        dKG = rel(vals["K"]["rho"], vals["G"]["rho"])
        dSr, dSv = rel(vals["S"]["rho"], vals["0"]["rho"]), rel(vals["S"]["v2"], vals["0"]["v2"])
        dMr, dMv = rel(vals["M"]["rho"], vals["0"]["rho"]), rel(vals["M"]["v2"], vals["0"]["v2"])
        check(dKG < 1e-9, f"L-G2 GATE species {sp}: resistance density under G equals that "
                          f"under K, rel diff {dKG:.1e} < 1e-9 (both shift rho by "
                          f"{rel(vals['G']['rho'], vals['0']['rho']):.2e})")
        check(dSr < 1e-9 and dSv < 1e-9, f"L-G2 GATE species {sp}: shape modulation S "
                                         f"invisible to resistance density ({dSr:.1e}) and "
                                         f"IR speed ({dSv:.1e})")
        check(dMr < 1e-9 and dMv > 1e-4, f"L-G2 GATE species {sp}: mass leaves resistance "
                                         f"density unchanged ({dMr:.1e}) but shifts IR speed "
                                         f"({dMv:.2e} > 1e-4)")
        out[sp] = {"K_vs_G": dKG, "S_rho": dSr, "S_v2": dSv, "M_rho": dMr, "M_v2": dMv}
    check(True, "L-G2 consequence (frozen): in every G-2-recoverable IR geometric datum the "
                "proper-distance direction is indistinguishable from stiffness and the shape "
                "direction is invisible. Recovered geometry cannot select geometric "
                "coupling: NULL as selector. G-2 geometry is not the coupling ansatz", "note")
    return out


# ---------------- earned rows (L-C) and the Sel-4 row (L-I) -----------------------------------
def earned_rows(Dfun):
    Q = 1e-12
    cK = Dfun(Q).real / Q
    cG = dD(Dfun, Q)
    cS = Q
    return [[1.0, cK, cG, cS, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0]]


def Pi(Dfun, coef, h, qhi):
    P, m = modulated(Dfun, coef, h)
    vir = math.sqrt(dP(P, 1e-12) / m)

    def om(q):
        return math.sqrt(P(q * q).real / m)

    def vg(q):
        return q * dP(P, q * q) / (m * om(q))

    lo, hi = 1e-3, qhi
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if vg(mid) > 0.5 * vir:
            lo = mid
        else:
            hi = mid
        if hi - lo < 1e-15 * hi:
            break
    qs = 0.5 * (lo + hi)
    return om(qs) / (vir * qs)


def dPi(Dfun, coef, qhi, h=1e-4):
    if all(c == 0 for c in coef[:4]):
        return 0.0  # X: constant limit is a total derivative (labeled by-construction)
    return (Pi(Dfun, coef, h, qhi) - Pi(Dfun, coef, -h, qhi)) / (2 * h)


def leg_C():
    print("\n=== L-C: ALL EARNED CONSTRAINTS (IR conservation + IR Weyl in D = 2) ===")
    out = {}
    for sp, cfg in SPECIES.items():
        rows = earned_rows(cfg["D"])
        null, worst = null_space(rows, 5)
        rg, rs = residual(GEO, null), residual(S_DIR, null)
        rank, best = vertex_rank(null, cfg["D"])
        check(len(null) == 3, f"L-C GATE species {sp}: earned null space nullity "
                              f"{len(null)} (predicted 3); survivors satisfy every row to "
                              f"{worst:.1e}")
        check(rg < 1e-8 and rs < 1e-8, f"L-C GATE species {sp}: geometric residual "
                                       f"{rg:.1e} and S residual {rs:.1e} (both < 1e-8) -- "
                                       f"both pass every earned constraint")
        check(rank == 2, f"L-C GATE species {sp}: survivors' vertex image has rank {rank} "
                         f"(predicted 2: geometric and non-geometric shape side by side)")
        out[sp] = {"nullity": len(null), "res_geo": rg, "res_S": rs, "vertex_rank": rank}
    check(True, "L-C consequence (frozen): earned structure leaves the geometric and the "
                "non-geometric shape coupling side by side -- CONSTRAINED-NONUNIQUE", "note")
    return out


def leg_I():
    print("\n=== L-I: Sel-4, THE CANDIDATE WEAK-EQUIVALENCE SELECTOR (constant-probe "
          "intrinsic invisibility) ===")
    out = {}
    for sp, cfg in SPECIES.items():
        Dfun, qhi = cfg["D"], cfg["qhi"]
        row = []
        for i, nm in enumerate(NAMES):
            coef = [0.0] * 5
            coef[i] = 1.0
            row.append(dPi(Dfun, coef, qhi))
        pi0 = Pi(Dfun, [0.0] * 5, 0.0, qhi)
        units_ok = max(abs(row[0]), abs(row[1]), abs(row[2]), abs(row[4])) < 1e-6
        check(units_ok and abs(row[3]) > 1e-3,
              f"L-I GATE species {sp} (Pi_0 = {pi0:.6f}): dPi/dh = M {row[0]:.1e}, "
              f"K {row[1]:.1e}, G {row[2]:.1e}, X {row[4]:.1e} (all < 1e-6: unit changes) "
              f"vs S {row[3]:.3e} (> 1e-3: changes the intrinsic shape)")
        rows = earned_rows(Dfun) + [row]
        null, worst = null_space(rows, 5)
        rank, best = vertex_rank(null, Dfun)
        s = cfg["slope"](vertex(best, Dfun)) if best else float("nan")
        check(len(null) == 2 and rank == 1 and abs(s - 8.0) < 0.2,
              f"L-I GATE species {sp}: earned + Sel-4 -> nullity {len(null)} (predicted 2), "
              f"vertex-image rank {rank} (predicted 1), survivor {fmt(best)} slope {s:.3f} "
              f"(predicted 8 +- 0.2); rows satisfied to {worst:.1e}")
        out[sp] = {"dPi": row, "Pi0": pi0, "nullity": len(null), "rank": rank, "slope": s,
                   "survivor": best}
    check(True, "L-I consequence (frozen): the geometric vertex is selected uniquely (up to "
                "amplitude and the pair-null M - K direction) ONLY once Sel-4 is added. "
                "Sel-4 is not earned: it is the operational weak-equivalence statement", "note")
    return out


# ---------------- L-A: declared-access underdetermination ---------------------------------------
def leg_A():
    print("\n=== L-A: DECLARED-ACCESS UNDERDETERMINATION (material mimics of geometric "
          "coupling) ===")
    VA = vertex(GEO, D_cont)
    q0, q1 = 0.1, 0.2
    Q0, Q1 = q0 * q0, q1 * q1
    a11, a12, a21, a22 = -0.5 * Q0 ** 2, -0.5 * Q0 ** 3, -0.5 * Q1 ** 2, -0.5 * Q1 ** 3
    b1, b2 = VA(q0), VA(q1)
    det = a11 * a22 - a12 * a21
    sg, sg2 = (b1 * a22 - b2 * a12) / det, (a11 * b2 - a21 * b1) / det
    mimic = lambda q: -0.5 * (sg * q ** 4 + sg2 * q ** 6)
    rA = max(abs(VA(q) - mimic(q)) / abs(VA(q)) for q in (0.05, 0.3, 0.6))
    halt_check(rA < 1e-9, f"L-A GATE species A: material shape mimic (sigma = {sg:.6f}, "
                          f"sigma2 = {sg2:.3e}) reproduces the geometric vertex EXACTLY, max "
                          f"rel residual {rA:.1e} < 1e-9 at q in {{0.05, 0.3, 0.6}} "
                          f"(polynomial identity; halt-grade)")

    def Pmimic(h):
        P = lambda Q: D_cont(Q) + h * (sg * Q * Q + sg2 * Q ** 3)
        return P

    def Pi_custom(h):
        P = Pmimic(h)
        vir = math.sqrt(dP(P, 1e-12))
        om = lambda q: math.sqrt(P(q * q).real)
        vg = lambda q: q * dP(P, q * q) / om(q)
        lo, hi = 1e-3, 2.5
        for _ in range(300):
            mid = 0.5 * (lo + hi)
            if vg(mid) > 0.5 * vir:
                lo = mid
            else:
                hi = mid
            if hi - lo < 1e-15 * hi:
                break
        qs = 0.5 * (lo + hi)
        return om(qs) / (vir * qs)

    dmim = (Pi_custom(1e-4) - Pi_custom(-1e-4)) / 2e-4
    check(abs(dmim) > 1e-3, f"L-A GATE static discriminator: the species-A mimic's constant "
                            f"limit changes the intrinsic shape, dPi/dh = {dmim:.3e} "
                            f"(|.| > 1e-3), while the geometric coupling's does not (L-I) -- "
                            f"static access separates what pair access cannot")

    # ---- POST-HOC DIAGNOSTIC (labeled; a measurement, not a gate edit) ----------------------
    idm = max(abs((sg * q ** 4 + sg2 * q ** 6)
                  - (D_cont(q * q).real - q * q * dD(D_cont, q * q)))
              / abs(D_cont(q * q).real - q * q * dD(D_cont, q * q))
              for q in (0.05, 0.3, 0.6))
    check(True, f"L-A POST-HOC DIAGNOSTIC (labeled): the species-A 'material mimic' shape "
                f"modulation sigma Q^2 + sigma2 Q^3 equals D - QD' to {idm:.1e} -- i.e. it "
                f"acts on the dispersion EXACTLY as stiffness minus proper-distance, "
                f"(mu, kappa, lambda) = (0, 1, -1). That differs from the geometric "
                f"coupling (1/2, 1/2, -1) only by the M - K direction, which is pair-null "
                f"and Sel-4-invisible (a time rescaling). The 'mimic' is the geometric "
                f"coupling in material clothing, so its constant limit is a unit change and "
                f"the frozen static-discriminator gate could not fire. The gate stays RED "
                f"as found; its premise (that the mimic is non-geometric) was wrong", "note")

    VB = vertex(GEO, D_latt)

    def ladder(fit_qs):
        if len(fit_qs) == 1:
            qa = fit_qs[0]
            c = VB(qa) / (-0.5 * qa ** 4)
            fit = lambda q: -0.5 * c * q ** 4
        else:
            qa, qb = fit_qs
            A11, A12, A21, A22 = -0.5 * qa ** 4, -0.5 * qa ** 6, -0.5 * qb ** 4, -0.5 * qb ** 6
            d = A11 * A22 - A12 * A21
            c1 = (VB(qa) * A22 - VB(qb) * A12) / d
            c2 = (A11 * VB(qb) - A21 * VB(qa)) / d
            fit = lambda q: -0.5 * (c1 * q ** 4 + c2 * q ** 6)
        r = lambda q: abs(VB(q) - fit(q)) / abs(VB(q))
        return r(0.2) / r(0.1), r(0.1), r(0.2)

    l1, r1a, r1b = ladder([0.01])
    l2, r2a, r2b = ladder([0.01, 0.02])
    check(3.5 <= l1 <= 4.5, f"L-A GATE species B, 1-term shape fit: residual ratio "
                            f"r(0.2)/r(0.1) = {l1:.3f} in [3.5, 4.5] (r = {r1a:.2e} -> "
                            f"{r1b:.2e})")
    check(13.0 <= l2 <= 19.0, f"L-A GATE species B, 2-term shape fit: residual ratio = "
                              f"{l2:.3f} in [13, 19] (r = {r2a:.2e} -> {r2b:.2e}) -- the "
                              f"separation enters at the first unmatched order (ladder)")
    ratio = (VA(0.01) / 0.01 ** 4) / (VB(0.01) / 0.01 ** 4)
    check(True, f"L-A reported only: geometric vertex species ratio c_A/c_B = {ratio:.5f} "
                f"(dispersion-fixed, = alpha/(1/24) = 1.2). This would be the universality "
                f"discriminator; universality is not earned (S-1 PC-D: amplitudes "
                f"sector-supplied)", "note")
    return {"A_exact_residual": rA, "A_sigma": [sg, sg2], "A_mimic_dPi": dmim,
            "B_ladder_1term": l1, "B_ladder_2term": l2, "universality_ratio": ratio}


# ---------------- adjudication (mechanical) ----------------------------------------------------
def adjudicate(rH, rG2, rC, rI, rA):
    earned_rank = {sp: rC[sp]["vertex_rank"] for sp in SPECIES}
    derived = all(earned_rank[sp] == 1 for sp in SPECIES)
    nonunique = any(earned_rank[sp] >= 2 and rC[sp]["res_geo"] < 1e-8 for sp in SPECIES)
    sel4 = {sp: rI[sp]["rank"] == 1 and abs(rI[sp]["slope"] - 8.0) < 0.2 for sp in SPECIES}
    counter = (rH["S"] >= -1e-12 and all(rC[sp]["res_S"] < 1e-8 for sp in SPECIES)
               and all(rG2[sp]["S_rho"] < 1e-9 and rG2[sp]["S_v2"] < 1e-9 for sp in SPECIES))
    irreducible = (not derived) and all(sel4.values()) and counter
    under = {"A": rA["A_exact_residual"] < 1e-9, "B": False}
    underdetermined = any(under.values())
    split_fields = {sp: (earned_rank[sp], sel4[sp], under[sp]) for sp in SPECIES}
    class_split = split_fields["A"] != split_fields["B"]
    comps = []
    if derived:
        comps.append("DERIVED/SELECTED")
    if nonunique:
        comps.append("CONSTRAINED-NONUNIQUE")
    if irreducible:
        comps.append("IRREDUCIBLE INPUT (reduced to Sel-4)")
    if underdetermined:
        comps.append("UNDERDETERMINED under pair access")
    if class_split:
        comps.append("CLASS-SPLIT")
    return {"earned_rank": earned_rank, "sel4_selects": sel4, "counterexample_passes": counter,
            "pair_exact": under, "class_split_fields": {k: list(v) for k, v in
                                                          split_fields.items()},
            "components": comps, "import_discharged": derived}


# ---------------- main -------------------------------------------------------------------------
def main():
    t0 = time.time()
    print("EQ-1: CAN GEOMETRIC-ONLY COUPLING BE SELECTED FROM EARNED STRUCTURE? (charter "
          "frozen at 708a31b)")
    rX = leg_X()
    rH = leg_H()
    rG2 = leg_G2()
    rC = leg_C()
    rI = leg_I()
    rA = leg_A()
    adj = adjudicate(rH, rG2, rC, rI, rA)

    print("\n=== ADJUDICATION (frozen outcome rule, computed from the measurements) ===")
    check(True, f"earned vertex-image rank {adj['earned_rank']}; Sel-4 selects "
                f"{adj['sel4_selects']}; non-geometric counterexample passes every earned "
                f"constraint: {adj['counterexample_passes']}; pair-access exact mimic "
                f"{adj['pair_exact']}; per-species fields {adj['class_split_fields']}", "note")
    check(True, f"VERDICT COMPONENTS (mechanical): {' + '.join(adj['components'])}. "
                f"Geometric coupling discharged: {adj['import_discharged']}", "note")
    check(True, "Import consequence (frozen): geometric coupling stays SUPPLIED. Reduced "
                "form: Sel-4 -- a constant probe must act on each retained sector as a pure "
                "change of units (intrinsically invisible) -- which, with earned IR "
                "conservation and 2D Weyl, fixes the geometric vertex. Its test is a STATIC "
                "(constant-probe) measurement of the sector's intrinsic dispersion shape. "
                "Class-4 stays OPEN (retained sector untouched); D = 4 TT/xi and the "
                "ordering ambiguity stay open", "note")

    out = {"instrument": "eq1_equivalence", "charter_commit": "708a31b",
           "date": "2026-09-25", "LX": rX, "LH": rH, "LG2": rG2, "LC": rC, "LI": rI,
           "LA": rA, "adjudication": adj, "halts": HALT, "checks": CHECKS, "failures": FAIL,
           "elapsed_s": round(time.time() - t0, 2),
           "hard_stop": "verdict recorded; owner rules on the next layer"}
    path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                         "EQ1_EQUIVALENCE_RESULT.json"))
    with open(path, "wb") as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True, default=float).encode())
    sha = hashlib.sha256(open(path, "rb").read()).hexdigest()
    print(f"\nartifact written: {path} (sha {sha[:16]}...)")
    n_ok = sum(1 for c in CHECKS if c["ok"])
    print(f"\nEQ-1 EQUIVALENCE ATTACK: {n_ok}/{len(CHECKS)} checks passed; failures: "
          f"{len(FAIL)}; halts: {len(HALT)}")
    if HALT:
        print("HALT: an analytic identity breached -- instrument bug, never physics. "
              "No verdict may be issued from this run.")
    else:
        print("HARD STOP: verdict recorded pending owner ruling.")
    sys.exit(0 if not FAIL else 1)


if __name__ == "__main__":
    main()
