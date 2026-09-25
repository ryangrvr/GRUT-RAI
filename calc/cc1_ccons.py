#!/usr/bin/env python3
"""cc1_ccons: can C_cons be derived from earned structure?

CHARTER: CC1_CCONS_CHARTER_01.md (pre-registration frozen at commit 86a839f BEFORE this
instrument ran; authority GitHub Issue #2 owner comment 5835662238). The selector battery
never mentions [O, H]: 𝔠_full, G-2 hop + resistance geometry, intrinsic spectral shape,
static-limit regularity, positivity of probe-mediated exchange. Stationarity-under-driving is
tested as a separate claim; where conservation follows only from supplied field content, the
dependency is reported. GeoInv is recorded, never used.

Legs: L-A counterexample battery (phonon mass modulation, IR-singular pinning, MFIM sum-X) |
L-S stationarity vs fundamentality (+ GR-1 channel conflict) | L-P positivity route
(massless vs massive vector and spin-2 exchange residues, D = 4).

Pure stdlib. Run: python3 calc/cc1_ccons.py
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
import fs1_free as F
from s41_sel4 import (chain_H, ring_sum, comm, dense, spectrum, shape, gram_psd, edges,
                      op_add, mat_comm_norm, HX, HZ)
from cp1_coupling import D_latt, V_metric

FAIL = []
CHECKS = []
HALT = []
HP = 0.05
SEED = 20260925


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


# ---------------- L-A: the counterexample battery ----------------------------------------------
def mode_omegas(N):
    return [2 * abs(math.sin(math.pi * j / N)) for j in range(1, N)]


def chi(N, kind, h=1e-4):
    om = mode_omegas(N)
    if kind == "mass":
        E = lambda hh: 0.5 * sum(math.sqrt(1 + hh) * w for w in om)
    else:
        E = lambda hh: 0.5 * sum(math.sqrt(w * w + hh) for w in om)
    return -(E(h) - 2 * E(0.0) + E(-h)) / (h * h)


def leg_A():
    print("\n=== L-A: COUNTEREXAMPLE BATTERY (non-conserved couplings vs every earned "
          "constant-level selector) ===")
    out = {}
    OM = F.blocks(pp=F.sym_shift(0))
    nc = max(abs(x) for x in F.flat(F.cons_map(OM)))
    check(nc > 0, f"L-A1 GATE phonon mass modulation O_M = 1/2 sum p^2: NON-conserved, "
                  f"max|AJM_H - M_HJA| = {nc:.3f} > 0")
    Mp = F.madd(F.MH, OM, HP)
    lam, _ = jacobi_eig(Mp)
    check(min(lam) >= -1e-10, f"L-A1 GATE 𝔠_full: H + hO_M PSD, min eigenvalue "
                              f"{min(lam):.2e}")
    hops = [F.hop_hat(Mp, 0, d) for d in (1, 2, 3, 4)]
    check(all(abs(hops[d - 1] - d) < 0.3 for d in (1, 2, 3, 4)),
          f"L-A1 GATE G-2 hop geometry unchanged: d_hat = "
          f"{', '.join(f'{x:.3f}' for x in hops)} (GeoInv also satisfied -- recorded only)")
    uu = lambda M: [[M[i][j] for j in range(F.N)] for i in range(F.N)]
    rr = F.resistance(uu(Mp), 0, 8) / F.resistance(uu(F.MH), 0, 8)
    check(abs(rr - 1) < 1e-12, f"L-A1 GATE G-2 static resistance R(0,8) ratio = {rr:.15f} "
                               f"(unchanged)")
    A = [[Mp[F.N + i][F.N + j] for j in range(F.N)] for i in range(F.N)]
    B = uu(Mp)
    S = [[(A[i][i] ** 0.5) * B[i][j] * (A[j][j] ** 0.5) for j in range(F.N)]
         for i in range(F.N)]
    w1 = sorted(math.sqrt(max(x, 0.0)) for x in jacobi_eig(S)[0])[1:]
    w0 = sorted(math.sqrt(max(x, 0.0)) for x in jacobi_eig(B)[0])[1:]
    sh = lambda w: [(x - w[0]) / (w[-1] - w[0]) for x in w]
    dsh = max(abs(a - b) for a, b in zip(sh(w1), sh(w0)))
    halt_check(dsh < 1e-12, f"L-A1 GATE spectrally a unit change: normalized mode-frequency "
                            f"shape unchanged to {dsh:.1e} < 1e-12 (omega' = sqrt(1+h) "
                            f"omega; halt-grade)")
    rM = chi(40, "mass") / chi(20, "mass")
    check(1.8 <= rM <= 2.2, f"L-A1 GATE static-limit regular: chi(N=40)/chi(N=20) = {rM:.4f} "
                            f"in [1.8, 2.2] (extensive)")
    rP = chi(40, "pin") / chi(20, "pin")
    check(rP > 4, f"L-A1' GATE pinning O_pin = 1/2 sum u^2 (non-conserved): chi ratio = "
                  f"{rP:.3f} > 4 -- IR-singular, excluded by static-limit regularity")
    out["A1"] = {"noncons": nc, "psd_min": min(lam), "hops": hops, "res_ratio": rr,
                 "shape": dsh, "chi_ratio_mass": rM, "chi_ratio_pin": rP}

    N = 6
    H = chain_H(N, 1.0, HX, HZ)
    O = ring_sum(N, (1,))
    cn = math.sqrt(sum(abs(c) ** 2 for c in comm(O, H).values()))
    Hm, Om = dense(H, N), dense(O, N)
    Hr = [[x.real for x in r] for r in Hm]
    Or = [[x.real for x in r] for r in Om]
    gmin = gram_psd(Hr, Or)
    same = edges(op_add(H, O, HP)) == edges(H)
    lamH, V = jacobi_eig(Hr)
    g = min(range(len(lamH)), key=lambda k: lamH[k])
    d = len(lamH)
    row = [sum(V[i][g] * Or[i][j] * V[j][m] for i in range(d) for j in range(d)
               if Or[i][j] != 0.0) for m in range(d)]
    chi2 = 2 * sum(row[m] ** 2 / (lamH[m] - lamH[g]) for m in range(d)
                   if m != g and lamH[m] - lamH[g] > 1e-9)
    dsh2 = max(abs(a - b) for a, b in zip(
        shape(spectrum([[Hm[i][j] + HP * Om[i][j] for j in range(d)] for i in range(d)])),
        shape(spectrum(Hm))))
    check(cn > 0 and gmin >= -1e-12 and same and math.isfinite(chi2) and chi2 > 0,
          f"L-A2 GATE MFIM O_X = sum X_i: non-conserved ({cn:.3f}), 𝔠_full Gram PSD "
          f"({gmin:.2e}), interaction graph unchanged ({same}), static chi finite "
          f"({chi2:.3f})")
    check(dsh2 > 1e-4, f"L-A2 GATE: O_X changes the normalized spectral shape by {dsh2:.3e} "
                       f"> 1e-4 -- only the unearned Sel-4 objects")
    out["A2"] = {"noncons": cn, "gram_min": gmin, "graph_same": same, "chi": chi2,
                 "shape": dsh2}
    check(True, "L-A consequence (frozen): the phonon mass modulation is non-conserved yet "
                "passes EVERY earned constant-level selector -- 𝔠_full, G-2 hop and "
                "resistance geometry, static regularity -- and is even spectrally a unit "
                "change satisfying GeoInv. C_cons is NOT selected at the constant level. "
                "Static regularity does cut IR-singular couplings (pinning): "
                "CONSTRAINED-NONUNIQUE", "note")
    return out


# ---------------- L-S: stationarity vs fundamentality --------------------------------------------
def leg_S():
    print("\n=== L-S: THE OWNER'S SEPARATION -- STATIONARITY UNDER DRIVING vs FUNDAMENTAL "
          "CONSERVATION ===")
    N = 6
    H = chain_H(N, 1.0, HX, HZ)
    Hm = dense(H, N)
    Hr = [[x.real for x in r] for r in Hm]
    d = len(Hr)
    lam, V = jacobi_eig(Hr)
    H2 = [[sum(Hr[i][k] * Hr[k][j] for k in range(d)) for j in range(d)] for i in range(d)]
    ops = {"H": Hr, "sum X": [[x.real for x in r] for r in dense(ring_sum(N, (1,)), N)],
           "sum Z": [[x.real for x in r] for r in dense(ring_sum(N, (3,)), N)], "H^2": H2}
    res = {}
    agree = True
    for name, O in ops.items():
        VO = [[sum(V[k][m] * O[k][j] for k in range(d)) for j in range(d)] for m in range(d)]
        Oe = [[sum(VO[m][j] * V[j][n] for j in range(d)) for n in range(d)] for m in range(d)]
        nO = sum(x * x for r in O for x in r)
        Dw = sum(Oe[m][n] ** 2 for m in range(d) for n in range(d)
                 if abs(lam[m] - lam[n]) > 1e-9) / nO
        cn = mat_comm_norm([[complex(x) for x in r] for r in O], Hm) / math.sqrt(nO)
        zero_D, zero_c = Dw < 1e-18, cn < 1e-10
        agree = agree and (zero_D == zero_c)
        res[name] = {"D_rel": Dw, "comm_rel": cn}
        check(True, f"L-S(i) {name}: driven (nonzero-frequency) weight D/||O||^2 = {Dw:.2e}, "
                    f"||[O,H]||/||O|| = {cn:.2e}", "note")
    halt_check(agree, "L-S(i) GATE: D(O) = 0 <=> [O, H] = 0 for all four operators "
                      "(halt-grade identity) -- 'stationary under driving' IS C_cons, "
                      "restated; it adds no independent ground")
    O = dense(ring_sum(N, (1,)), N)
    Hp = [[Hr[i][j] + HP * O[i][j].real for j in range(d)] for i in range(d)]
    lp, Vp = jacobi_eig(Hp)
    g = min(range(d), key=lambda k: lp[k])
    Z = [(1 if (b & 1) == 0 else -1) for b in range(d)]
    zrow = [sum(Vp[b][g] * Z[b] * Vp[b][m] for b in range(d)) for m in range(d)]

    def C2(t1, t2):
        return sum(zrow[m] ** 2 * cmath.exp(1j * lp[g] * t1) * cmath.exp(-1j * lp[m] * t1)
                   * cmath.exp(1j * lp[m] * t2) * cmath.exp(-1j * lp[g] * t2)
                   for m in range(d))

    c = [C2(1.0, 0.5), C2(3.0, 2.5), C2(7.0, 6.5)]
    dst = max(abs(c[0] - c[1]), abs(c[0] - c[2]))
    check(dst < 1e-12, f"L-S(ii) GATE: under the CONSTANT non-conserved probe H + h sum X, "
                       f"two-time correlators depend only on the time difference "
                       f"(max spread {dst:.1e}) -- a constant probe needs no conservation "
                       f"to be stationary")
    ks = [2 * math.pi * j / F.N for j in range(1, F.N)]
    om = mode_omegas(F.N)
    pairH = max(abs(0.5 * (-(w / 2) + (w * w) / (2 * w))) for w in om)
    Wm = sum(V_metric(D_latt, abs(((k + math.pi) % (2 * math.pi)) - math.pi)) ** 2
             for k in ks)
    check(pairH < 1e-15 and Wm > 1e-6,
          f"L-S(iii) GATE: phonon H pair amplitude max {pairH:.1e} (conserved: none), but "
          f"the geometric T_xx vertex (CP-1) has dynamic weight sum V^2 = {Wm:.4e} > 1e-6 "
          f"-- a BLANKET C_cons would delete GR-1's own channel; C_cons can at most be "
          f"component-specific")
    res["constant_stationary_spread"] = dst
    res["pair_H"] = pairH
    res["W_metric"] = Wm
    res["equivalence"] = agree
    return res


# ---------------- L-P: the positivity route --------------------------------------------------------
ETA = [-1.0, 1.0, 1.0, 1.0]


def lower_vec(v):
    return [ETA[i] * v[i] for i in range(4)]


def rand_unit(rng):
    v = [rng.gauss(0, 1) for _ in range(3)]
    n = math.sqrt(sum(x * x for x in v))
    return [x / n for x in v]


def perp_basis(n):
    a = [1.0, 0.0, 0.0] if abs(n[0]) < 0.9 else [0.0, 1.0, 0.0]
    e1 = [a[i] - sum(a[j] * n[j] for j in range(3)) * n[i] for i in range(3)]
    s = math.sqrt(sum(x * x for x in e1))
    e1 = [x / s for x in e1]
    e2 = [n[1] * e1[2] - n[2] * e1[1], n[2] * e1[0] - n[0] * e1[2], n[0] * e1[1] - n[1] * e1[0]]
    return e1, e2


def tens_resid(Plow, T, coef):
    M = [[sum(Plow[m][a] * T[a][b] for a in range(4)) for b in range(4)] for m in range(4)]
    MM = sum(M[i][j] * M[j][i] for i in range(4) for j in range(4))
    tr = sum(M[i][i] for i in range(4))
    return MM - coef * tr * tr


def sym_basis():
    out = []
    for a in range(4):
        for b in range(a, 4):
            T = [[0.0] * 4 for _ in range(4)]
            T[a][b] = T[b][a] = 1.0
            out.append(T)
    return out


def leg_P():
    print("\n=== L-P: THE POSITIVITY ROUTE -- does 𝔠_full force conservation, and at what "
          "price? (D = 4 exchange residues) ===")
    rng = random.Random(SEED)
    etaL = [[ETA[i] if i == j else 0.0 for j in range(4)] for i in range(4)]
    out = {}
    cons_min, cons_dev, non_min = float("inf"), 0.0, float("inf")
    for _ in range(200):
        n = rand_unit(rng)
        Js = [rng.gauss(0, 1) for _ in range(3)]
        Jc = [sum(n[i] * Js[i] for i in range(3))] + Js
        R = sum(ETA[i] * Jc[i] ** 2 for i in range(4))
        perp = [Js[i] - Jc[0] * n[i] for i in range(3)]
        cons_min = min(cons_min, R)
        cons_dev = max(cons_dev, abs(R - sum(x * x for x in perp)))
        Jn = [rng.gauss(0, 1)] + [rng.gauss(0, 1) for _ in range(3)]
        non_min = min(non_min, sum(ETA[i] * Jn[i] ** 2 for i in range(4)))
    halt_check(cons_min >= -1e-12 and cons_dev < 1e-12,
               f"L-P GATE massless vector, conserved sources: min residue {cons_min:.3e} "
               f">= 0 and equal to the physical transverse sum to {cons_dev:.1e} (halt-grade)")
    check(non_min < -1e-3, f"L-P GATE massless vector, NON-conserved sources: min residue "
                           f"{non_min:.3f} < -1e-3 -- negative-norm exchange, a 𝔠_full "
                           f"violation")
    out["vector"] = {"cons_min": cons_min, "cons_dev": cons_dev, "non_min": non_min}

    SB = sym_basis()
    cmin2, cdev2, nmin2 = float("inf"), 0.0, float("inf")
    for _ in range(200):
        n = rand_unit(rng)
        k = [1.0] + n
        kl = lower_vec(k)
        rows = []
        for nu in range(4):
            rows.append([sum(kl[m] * T[m][nu] for m in range(4)) for T in SB])
        G = [[sum(r[i] * r[j] for r in rows) for j in range(10)] for i in range(10)]
        lam, V = jacobi_eig(G)
        mx = max(abs(x) for x in lam)
        null = [[V[i][c] for i in range(10)] for c in range(10) if abs(lam[c]) < 1e-10 * mx]
        coef = [rng.gauss(0, 1) for _ in null]
        vec = [sum(coef[a] * null[a][i] for a in range(len(null))) for i in range(10)]
        T = [[sum(vec[i] * SB[i][a][b] for i in range(10)) for b in range(4)]
             for a in range(4)]
        R = tens_resid(etaL, T, 0.5)
        e1, e2 = perp_basis(n)
        ep = [[(e1[i] * e1[j] - e2[i] * e2[j]) / math.sqrt(2) for j in range(3)]
              for i in range(3)]
        ex = [[(e1[i] * e2[j] + e2[i] * e1[j]) / math.sqrt(2) for j in range(3)]
              for i in range(3)]
        phys = sum(sum(ep[i][j] * T[i + 1][j + 1] for i in range(3) for j in range(3)) ** 2
                   for _ in (0,)) + \
            sum(ex[i][j] * T[i + 1][j + 1] for i in range(3) for j in range(3)) ** 2
        cmin2 = min(cmin2, R)
        cdev2 = max(cdev2, abs(R - phys))
        Tn = [[0.0] * 4 for _ in range(4)]
        for a in range(4):
            for b in range(a, 4):
                Tn[a][b] = Tn[b][a] = rng.gauss(0, 1)
        nmin2 = min(nmin2, tens_resid(etaL, Tn, 0.5))
    halt_check(cmin2 >= -1e-12 and cdev2 < 1e-10,
               f"L-P GATE massless spin-2, conserved T: min residue {cmin2:.3e} >= 0 and "
               f"equal to the physical helicity-2 sum to {cdev2:.1e} (halt-grade)")
    check(nmin2 < -1e-3, f"L-P GATE massless spin-2, NON-conserved T: min residue "
                         f"{nmin2:.3f} < -1e-3 -- ghost exchange, a 𝔠_full violation")
    out["spin2"] = {"cons_min": cmin2, "cons_dev": cdev2, "non_min": nmin2}

    pmin, fmin = float("inf"), float("inf")
    for _ in range(200):
        ks = [rng.gauss(0, 1) for _ in range(3)]
        E = math.sqrt(1.0 + sum(x * x for x in ks))
        kl = lower_vec([E] + ks)
        P = [[(ETA[i] if i == j else 0.0) + kl[i] * kl[j] for j in range(4)] for i in range(4)]
        J = [rng.gauss(0, 1) for _ in range(4)]
        pmin = min(pmin, sum(J[i] * P[i][j] * J[j] for i in range(4) for j in range(4)))
        Tn = [[0.0] * 4 for _ in range(4)]
        for a in range(4):
            for b in range(a, 4):
                Tn[a][b] = Tn[b][a] = rng.gauss(0, 1)
        fmin = min(fmin, tens_resid(P, Tn, 1.0 / 3.0))
    check(pmin >= -1e-12 and fmin >= -1e-12,
          f"L-P GATE massive probes (Proca, Fierz-Pauli; m = 1, on shell): min residue for "
          f"NON-conserved sources {pmin:.3e} (vector), {fmin:.3e} (spin-2), both >= 0 -- "
          f"positivity does NOT force conservation")
    out["massive"] = {"proca_min": pmin, "fp_min": fmin}
    check(True, "L-P consequence (frozen): 𝔠_full positivity forces source conservation IF "
                "AND ONLY IF the probe is a massless gauge field (covariant, redundant "
                "polarizations). That field content is SUPPLIED -- C_cons reduces to it; it "
                "is not derived. The conservation obtained is CURRENT conservation: its "
                "zero-momentum time component is S4-1's clock C_cons, while T_xx stays a "
                "non-conserved flux, consistent with L-S(iii)", "note")
    return out


def adjudicate(rA, rS, rP):
    a1 = rA["A1"]
    passes = (a1["noncons"] > 0 and a1["psd_min"] >= -1e-10
              and all(abs(a1["hops"][d - 1] - d) < 0.3 for d in (1, 2, 3, 4))
              and abs(a1["res_ratio"] - 1) < 1e-12 and 1.8 <= a1["chi_ratio_mass"] <= 2.2)
    cuts = a1["chi_ratio_pin"] > 4
    restated = rS["equivalence"]
    blanket_conflict = rS["pair_H"] < 1e-15 and rS["W_metric"] > 1e-6
    split = (rP["vector"]["non_min"] < -1e-3 and rP["spin2"]["non_min"] < -1e-3
             and rP["massive"]["proca_min"] >= -1e-12 and rP["massive"]["fp_min"] >= -1e-12)
    derived = not passes
    comps = []
    if not derived:
        comps.append("NOT SELECTED at the constant level (non-conserved survivor)")
    if cuts:
        comps.append("CONSTRAINED-NONUNIQUE (static regularity cuts IR-singular couplings)")
    if restated:
        comps.append("stationarity-under-driving == C_cons (restatement)")
    if blanket_conflict:
        comps.append("blanket C_cons contradicts GR-1's channel (component-specific at most)")
    if split:
        comps.append("CLASS-SPLIT by probe field content (massless gauge forces; massive not)")
    overall = "DERIVED/SELECTED" if derived else \
        ("IRREDUCIBLE INPUT, reduced to supplied massless-gauge probe content" if split
         else "IRREDUCIBLE INPUT")
    return {"components": comps, "overall": overall}


def main():
    t0 = time.time()
    print("CC-1: CAN C_cons BE DERIVED FROM EARNED STRUCTURE? (charter frozen at 86a839f)")
    rA = leg_A()
    rS = leg_S()
    rP = leg_P()
    adj = adjudicate(rA, rS, rP)
    print("\n=== ADJUDICATION (frozen outcome rule, computed from the measurements) ===")
    for c in adj["components"]:
        check(True, c, "note")
    check(True, f"OVERALL: {adj['overall']}. GeoInv untouched and unearned; retained sector, "
                f"omega^7, GR-1 3D red, hbar, D = 4 TT/xi, ordering, geometry selection "
                f"fenced. Class-4 OPEN", "note")
    out = {"instrument": "cc1_ccons", "charter_commit": "86a839f", "date": "2026-09-25",
           "seed": SEED, "LA": rA, "LS": rS, "LP": rP, "adjudication": adj, "halts": HALT,
           "checks": CHECKS, "failures": FAIL, "elapsed_s": round(time.time() - t0, 2),
           "hard_stop": "verdict recorded; owner rules"}
    path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                         "CC1_CCONS_RESULT.json"))
    with open(path, "wb") as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True, default=float).encode())
    sha = hashlib.sha256(open(path, "rb").read()).hexdigest()
    print(f"\nartifact written: {path} (sha {sha[:16]}...)")
    n_ok = sum(1 for c in CHECKS if c["ok"])
    print(f"\nCC-1 C_cons ATTACK: {n_ok}/{len(CHECKS)} checks passed; failures: {len(FAIL)}; "
          f"halts: {len(HALT)}")
    if HALT:
        print("HALT: an analytic identity breached -- instrument bug, never physics. "
              "No verdict may be issued from this run.")
    else:
        print("HARD STOP: verdict recorded pending owner ruling.")
    sys.exit(0 if not FAIL else 1)


if __name__ == "__main__":
    main()
