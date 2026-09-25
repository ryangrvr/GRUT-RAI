#!/usr/bin/env python3
"""u1_universality: can clock universality for genuinely non-interacting sectors be derived?

CHARTER: U1_UNIVERSALITY_CHARTER_01.md (pre-registration frozen at commit f31ab7d BEFORE this
instrument ran; authority GitHub Issue #2 owner comment 5835886532). C_cons is an irreducible
input reduced to the supplied massless gauge/Lorentz-redundancy structure (clock component);
GeoInv is not used. The only units-fixing step is ONE common time rescaling, optimized out --
no per-sector rescaling (that would be the universality assumption).

Legs: L-C decoupled counterexample battery (g = 0) | L-G supplied gauge structure: soft-emission
gauge variation, decoupled vs exchanging processes | L-D does a dynamical probe create an
exchange channel (clock-only vs non-conserved components) | L-g finite small-coupling sequence
vs the exact decoupled endpoint.

Pure stdlib. Run: python3 calc/u1_universality.py
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
from s41_sel4 import (ladder_H, dense, evo_setup, discriminator, gram_psd, edges, op_add,
                      spectrum, shape, mat_comm_norm, placed, HX, HZ)

FAIL = []
CHECKS = []
HALT = []
HP = 0.05
EPS_B = 0.6
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


def real(M):
    return [[x.real for x in r] for r in M]


def lin(A, B, a=1.0, b=1.0):
    return [[a * A[i][j] + b * B[i][j] for j in range(len(A))] for i in range(len(A))]


def expect_series(Hr, psi_vec, O):
    lam, V = jacobi_eig(Hr)
    d = len(lam)
    c = [sum(V[k][m] * psi_vec[k] for k in range(d)) for m in range(d)]
    VO = [[sum(V[k][m] * O[k][j] for k in range(d)) for j in range(d)] for m in range(d)]
    Oe = [[sum(VO[m][j] * V[j][n] for j in range(d)) for n in range(d)] for m in range(d)]
    terms = [(c[m] * c[n] * Oe[m][n], lam[m] - lam[n]) for m in range(d) for n in range(d)
             if abs(c[m] * c[n] * Oe[m][n]) > 1e-18]
    return lambda t: sum(w * math.cos(f * t) for w, f in terms)


# ---------------- L-C: the decoupled counterexample battery -------------------------------------
def leg_C():
    print("\n=== L-C: GENUINELY DECOUPLED SECTORS (g = 0) -- non-universal clock coupling "
          "O = H_A + 0.6 H_B ===")
    L, N = 3, 6
    HA, HB, V = ladder_H(L, 0.0)
    H = op_add(HA, HB)
    O = op_add(HA, HB, EPS_B)
    Hm, Om = dense(H, N), dense(O, N)
    Hr, Or = real(Hm), real(Om)
    cn = mat_comm_norm(Om, Hm)
    halt_check(cn < 1e-12, f"L-C GATE C_cons-compatible: ||[O, H]|| = {cn:.1e} < 1e-12 "
                           f"(halt-grade)")
    gmin = gram_psd(Hr, Or)
    check(gmin >= -1e-12, f"L-C GATE 𝔠_full: ground-state two-time Gram of O PSD, min eig / "
                          f"scale = {gmin:.2e}")
    same = edges(op_add(H, O, HP)) == edges(H)
    check(same, "L-C GATE G-2: interaction graph of H + hO equals that of H (hop geometry "
                "blind)")
    HAm, HBm = dense(HA, N), dense(HB, N)
    dA = max(abs(a - b) for a, b in zip(shape(spectrum([[x * (1 + HP) for x in r] for r in HAm])),
                                        shape(spectrum(HAm))))
    dB = max(abs(a - b) for a, b in zip(
        shape(spectrum([[x * (1 + EPS_B * HP) for x in r] for r in HBm])),
        shape(spectrum(HBm))))
    check(dA < 1e-12 and dB < 1e-12, f"L-C GATE each sector internally a pure unit change: "
                                     f"normalized spectrum shape change A {dA:.1e}, "
                                     f"B {dB:.1e} (both < 1e-12)")
    psi = (1 << 3) | (1 << 4) | (1 << 5)
    obs = [(1 if (b & 1) == 0 else -1) * (1 if ((b >> 3) & 1) == 0 else -1)
           for b in range(2 ** N)]
    ts = [10.0 * i / 40 for i in range(41)]
    base = evo_setup(Hr, psi, obs)
    uni = evo_setup([[x * (1 + HP) for x in r] for r in Hr], psi, obs)
    non = evo_setup(lin(Hr, Or, 1.0, HP), psi, obs)
    du, cu = discriminator(base, uni, ts)
    dn, cn2 = discriminator(base, non, ts)
    halt_check(du < 1e-10, f"L-C GATE universal probe: joint Delta = {du:.1e} < 1e-10 at best "
                           f"common rescale c = {cu:.6f} (halt-grade)")
    check(dn > 1e-3, f"L-C GATE non-universal probe: joint Delta = {dn:.3e} > 1e-3 even at "
                     f"the best common rescale c = {cn2:.6f} -- observable by joint access")
    check(True, "L-C note (P-6 carried): the two sectors are different, so no earned symmetry "
                "relates them; for identical sectors, swap covariance of the probe would force "
                "equality only if supplied", "note")
    check(True, "L-C consequence (frozen): a non-universal clock coupling passes every earned "
                "selector PLUS C_cons -- 𝔠_full, G-2 geometry, per-sector unit change -- yet "
                "is observable by joint access", "note")
    return {"comm": cn, "gram_min": gmin, "graph_same": same, "shapeA": dA, "shapeB": dB,
            "Delta_universal": du, "Delta_nonuniversal": dn}


# ---------------- L-G: the supplied gauge structure ---------------------------------------------
def leg_G():
    print("\n=== L-G: THE SUPPLIED GAUGE STRUCTURE -- soft-emission gauge variation "
          "q_mu M^{mu nu} = sum_n kappa_s(n) eta_n p_n (D = 4) ===")
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
    check(vI < 1e-12, f"L-G GATE class I (genuinely decoupled, momentum conserved separately): "
                      f"max gauge variation {vI:.1e} < 1e-12 with kappa_A != kappa_B -- NOT "
                      f"forced")
    check(vIIne > 1e-3 and vIIeq < 1e-12,
          f"L-G GATE class II (sectors exchange momentum): min variation {vIIne:.3f} > 1e-3 "
          f"for kappa_A != kappa_B; max {vIIeq:.1e} < 1e-12 for kappa_A = kappa_B -- FORCED")
    check(True, "L-G consequence (frozen): the supplied massless gauge structure forces "
                "universality EXACTLY when the sectors exchange energy-momentum, and not for "
                "genuinely decoupled sectors. (The algebra is the Weinberg soft-emission "
                "argument: standard, NULL-REDUNDANT as a principle)", "note")
    return {"classI_max": vI, "classII_min_neq": vIIne, "classII_max_eq": vIIeq}


# ---------------- L-D: does a dynamical probe create an exchange channel? ------------------------
def kron(A, B):
    n, m = len(A), len(B)
    return [[A[i // m][j // m] * B[i % m][j % m] for j in range(n * m)] for i in range(n * m)]


def eye(n):
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]


def leg_D():
    print("\n=== L-D: DOES A DYNAMICAL PROBE CREATE AN EXCHANGE CHANNEL? (two 2-site sectors + "
          "probe oscillator, 80-dim) ===")
    Ns = 4

    def sector(sites, J, hx, hz):
        op = {placed(Ns, [(sites[0], 3), (sites[1], 3)]): J}
        for s in sites:
            op = op_add(op, {placed(Ns, [(s, 1)]): hx})
            op = op_add(op, {placed(Ns, [(s, 3)]): hz})
        return op

    HA = sector((0, 1), 1.0, HX, HZ)
    HB = sector((2, 3), 1.3, 0.7, 0.5)
    XA = op_add({placed(Ns, [(0, 1)]): 1.0}, {placed(Ns, [(1, 1)]): 1.0})
    XB = op_add({placed(Ns, [(2, 1)]): 1.0}, {placed(Ns, [(3, 1)]): 1.0})
    HAm, HBm = real(dense(HA, Ns)), real(dense(HB, Ns))
    XAm, XBm = real(dense(XA, Ns)), real(dense(XB, Ns))
    nb = 5
    b = [[0.0] * nb for _ in range(nb)]
    for n in range(1, nb):
        b[n - 1][n] = math.sqrt(n)
    bpb = [[b[i][j] + b[j][i] for j in range(nb)] for i in range(nb)]
    nnum = [[float(i) if i == j else 0.0 for j in range(nb)] for i in range(nb)]
    I16, I5 = eye(16), eye(nb)
    Hsec = kron(lin(HAm, HBm), I5)
    Hprobe = kron(I16, nnum)
    HA_full = kron(HAm, I5)
    HB_full = kron(HBm, I5)
    psi = [0.0] * (16 * nb)
    psi[0] = 1.0
    ts = [10.0 * i / 40 for i in range(41)]
    out = {}
    for tag, OA, OB in (("clock-only", HAm, HBm), ("non-conserved (T_xx-type)", XAm, XBm)):
        coup = kron(lin(OA, OB, 0.3, 0.18), bpb)
        Hf = lin(lin(Hsec, Hprobe), coup)
        d = len(Hf)
        AB = [[sum(HA_full[i][k] * Hf[k][j] for k in range(d)) for j in range(d)]
              for i in range(d)]
        BA = [[sum(Hf[i][k] * HA_full[k][j] for k in range(d)) for j in range(d)]
              for i in range(d)]
        cn = max(abs(AB[i][j] - BA[i][j]) for i in range(d) for j in range(d))
        f = expect_series(Hf, psi, HB_full)
        vals = [f(t) for t in ts]
        var = max(vals) - min(vals)
        out[tag] = {"comm_HA": cn, "HB_variation": var}
        if tag == "clock-only":
            halt_check(cn < 1e-12, f"L-D GATE (i) clock-only probe: ||[H_A, H_full]|| = "
                                   f"{cn:.1e} < 1e-12 (halt-grade)")
            check(var < 1e-10, f"L-D GATE (i) clock-only probe: <H_B>(t) varies by {var:.1e} "
                               f"< 1e-10 on [0, 10] -- the probe mediates NO energy exchange: "
                               f"L-G class I, equality not forced")
        else:
            check(cn > 1e-3 and var > 1e-4,
                  f"L-D GATE (ii) probe with non-conserved components: ||[H_A, H_full]|| = "
                  f"{cn:.3f} > 1e-3 and <H_B>(t) varies by {var:.3e} > 1e-4 -- the probe IS "
                  f"an exchange channel: L-G class II, equality forced (given the supplied "
                  f"gauge structure)")
    check(True, "L-D consequence (frozen): a dynamical probe coupled only through clocks leaves "
                "the sectors genuinely decoupled; a dynamical probe carrying non-conserved "
                "(T_xx-type) components -- the kind GR-1's channel uses -- makes every sector "
                "it touches exchange energy-momentum with the others", "note")
    return out


# ---------------- L-g: approach to the decoupled endpoint ----------------------------------------
def leg_g():
    print("\n=== L-g: THE APPROACH TO THE DECOUPLED ENDPOINT (finite small-g sequence vs g = 0) "
          "===")
    L, N = 3, 6
    gs = [0.01, 0.003, 0.001, 0.0]
    psi_i = (1 << 3) | (1 << 4) | (1 << 5)
    psi = [0.0] * (2 ** N)
    psi[psi_i] = 1.0
    ts = [10.0 * i / 40 for i in range(41)]
    comm_rel, drift = {}, {}
    for g in gs:
        HA, HB, V = ladder_H(L, g)
        H = op_add(op_add(HA, HB), V) if g else op_add(HA, HB)
        Hm = dense(H, N)
        Om = dense(op_add(HA, HB, EPS_B), N)
        nO = max(abs(x) for r in Om for x in r)
        comm_rel[g] = mat_comm_norm(Om, Hm) / nO
        f = expect_series(real(Hm), psi, real(Om))
        v0 = f(0.0)
        drift[g] = max(abs(f(t) - v0) for t in ts)
    lin_dev = max(abs((comm_rel[a] / comm_rel[b]) / (a / b) - 1)
                  for a, b in ((0.01, 0.003), (0.003, 0.001)))
    check(lin_dev < 1e-8 and comm_rel[0.0] < 1e-14,
          f"L-g GATE (i): ||[O,H]||/||O|| = {comm_rel[0.01]:.3e}, {comm_rel[0.003]:.3e}, "
          f"{comm_rel[0.001]:.3e}, {comm_rel[0.0]:.1e} -- exactly linear in g (deviation "
          f"{lin_dev:.1e}), zero at the endpoint")
    s1 = math.log(drift[0.01] / drift[0.003]) / math.log(0.01 / 0.003)
    s2 = math.log(drift[0.003] / drift[0.001]) / math.log(3.0)
    check(0.8 <= s1 <= 1.2 and 0.8 <= s2 <= 1.2 and drift[0.0] < 1e-12,
          f"L-g GATE (ii): observable non-conservation max|<O>(t) - <O>(0)| = "
          f"{drift[0.01]:.3e}, {drift[0.003]:.3e}, {drift[0.001]:.3e}, {drift[0.0]:.1e}; "
          f"log-slopes {s1:.3f}, {s2:.3f} in [0.8, 1.2]; zero at g = 0")
    check(True, "L-g consequence (frozen): C_cons forces universality exactly for any g != 0, "
                "but the violation it forbids is proportional to g -- visible only on "
                "timescales ~1/g -- and vanishes continuously at the endpoint. The g -> 0 "
                "'singularity' belongs to treating C_cons as an exact constraint, not to the "
                "physics", "note")
    return {"comm_rel": {str(k): v for k, v in comm_rel.items()},
            "drift": {str(k): v for k, v in drift.items()}, "slopes": [s1, s2],
            "lin_dev": lin_dev}


def adjudicate(rC, rG, rD, rg):
    survivor = (rC["comm"] < 1e-12 and rC["gram_min"] >= -1e-12 and rC["graph_same"]
                and rC["shapeA"] < 1e-12 and rC["shapeB"] < 1e-12
                and rC["Delta_nonuniversal"] > 1e-3)
    gauge_decoupled_forces = rG["classI_max"] >= 1e-12
    decoupled = "DERIVED" if (not survivor or gauge_decoupled_forces) else "IRREDUCIBLE INPUT"
    exchange = (rG["classII_min_neq"] > 1e-3 and rG["classII_max_eq"] < 1e-12
                and rD["non-conserved (T_xx-type)"]["HB_variation"] > 1e-4)
    clock_quiet = rD["clock-only"]["HB_variation"] < 1e-10
    overall = "CLASS-SPLIT" if (decoupled == "IRREDUCIBLE INPUT" and exchange) else decoupled
    return {"genuinely_decoupled": decoupled,
            "exchanging": "DERIVED-IN-CLASS (conditional on supplied gauge structure)"
            if exchange else "not forced",
            "clock_only_probe_decouples": clock_quiet, "overall": overall,
            "residual": "whether every sector couples to a dynamical probe through "
                        "exchange-carrying (non-conserved) components -- supplied"}


def main():
    t0 = time.time()
    print("U-1: CAN CLOCK UNIVERSALITY FOR NON-INTERACTING SECTORS BE DERIVED? (charter frozen "
          "at f31ab7d)")
    rC = leg_C()
    rG = leg_G()
    rD = leg_D()
    rg = leg_g()
    adj = adjudicate(rC, rG, rD, rg)
    print("\n=== ADJUDICATION (frozen outcome rule, computed from the measurements) ===")
    for k in ("genuinely_decoupled", "exchanging", "clock_only_probe_decouples", "overall",
              "residual"):
        check(True, f"{k}: {adj[k]}", "note")
    out = {"instrument": "u1_universality", "charter_commit": "f31ab7d", "date": "2026-09-25",
           "seed": SEED, "LC": rC, "LG": rG, "LD": rD, "Lg": rg, "adjudication": adj,
           "halts": HALT, "checks": CHECKS, "failures": FAIL,
           "elapsed_s": round(time.time() - t0, 2), "hard_stop": "verdict recorded"}
    path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                         "U1_UNIVERSALITY_RESULT.json"))
    with open(path, "wb") as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True, default=float).encode())
    sha = hashlib.sha256(open(path, "rb").read()).hexdigest()
    print(f"\nartifact written: {path} (sha {sha[:16]}...)")
    n_ok = sum(1 for c in CHECKS if c["ok"])
    print(f"\nU-1 UNIVERSALITY ATTACK: {n_ok}/{len(CHECKS)} checks passed; failures: "
          f"{len(FAIL)}; halts: {len(HALT)}")
    if HALT:
        print("HALT: an analytic identity breached -- instrument bug, never physics. "
              "No verdict may be issued from this run.")
    else:
        print("HARD STOP: verdict recorded pending owner ruling.")
    sys.exit(0 if not FAIL else 1)


if __name__ == "__main__":
    main()
