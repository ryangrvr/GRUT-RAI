#!/usr/bin/env python3
"""rs1_retained: is the gapless phonon sector selected, or merely chosen?

CHARTER: RS1_RETAINED_SECTOR_CHARTER_01.md (pre-registration frozen at commit 1f18205 BEFORE
this instrument ran; authority GitHub Issue #2 owner comment 5837437988). Success bar: a
selector must ELIMINATE a genuinely different gapless candidate using earned structure. The
geometry selector is conditional on the declared bridging premise CARRIER. omega^7 is never
consulted.

Candidates (ring N = 256, K = 4 sin^2(k/2)): P phonon | F free fermions at half filling |
M ferromagnetic magnon | B flexural chain | G gapped control.

Legs: L-GEO earned additive-metric recovery | L-LOR supplied probe: IR boost-compatible
symmetric stress | L-ST does gauge structure force or permit full-stress coupling | FS-1
matched control.

Pure stdlib. Run: python3 calc/rs1_retained.py
"""
import hashlib
import json
import math
import os
import random
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cp1_coupling import random_pairs, cons_rows, null_space
import fs1_free as F

FAIL = []
CHECKS = []
HALT = []
N = 256
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


def Kf(k):
    return 4.0 * math.sin(k / 2) ** 2


QS = [2 * math.pi * m / N for m in range(1, N)]


def lindhard():
    ks = [2 * math.pi * (j + 0.5) / N for j in range(N)]
    eps = [-2 * math.cos(k) for k in ks]
    occ = [1.0 if e < 0 else 0.0 for e in eps]
    chi = []
    for m in range(1, N):
        s = 0.0
        for j in range(N):
            jj = (j + m) % N
            if occ[j] != occ[jj]:
                s += (occ[j] - occ[jj]) / (eps[jj] - eps[j])
        chi.append(s / N)
    return chi


def resist(chis, d):
    return (2.0 / N) * sum(c * (1 - math.cos(q * d)) for c, q in zip(chis, QS))


# ---------------- L-GEO -----------------------------------------------------------------------------
def leg_GEO():
    print("\n=== L-GEO: EARNED GEOMETRY -- which candidates carry the additive (G-2 resistance) "
          "metric under local access? (conditional on CARRIER) ===")
    chiL = lindhard()
    kern = {"P": [1 / Kf(q) for q in QS], "M": [1 / Kf(q) for q in QS],
            "B": [1 / Kf(q) ** 2 for q in QS], "G": [1 / (Kf(q) + 0.25) for q in QS],
            "F": chiL}
    dev = max(abs(resist(kern["P"], d) - d * (N - d) / N) for d in (1, 8, 16, 100))
    halt_check(dev < 1e-9, f"L-GEO control: phonon kernel reproduces the exact ring identity "
                           f"R(0,d) = d(N-d)/N to {dev:.1e} (halt-grade)")
    dos = chiL[0]
    halt_check(abs(dos / (1 / (2 * math.pi)) - 1) < 0.02,
               f"L-GEO control: Lindhard q -> 0 limit {dos:.5f} equals the Fermi-level DOS "
               f"1/(2 pi) = {1 / (2 * math.pi):.5f} within 2% (halt-grade)")
    A = {lab: resist(c, 16) / resist(c, 8) for lab, c in kern.items()}
    check(1.8 <= A["P"] <= 2.2, f"L-GEO GATE P phonon: additivity A = R(0,16)/R(0,8) = "
                                f"{A['P']:.4f} in [1.8, 2.2] -- carries the additive metric")
    check(1.8 <= A["M"] <= 2.2, f"L-GEO GATE M magnon: A = {A['M']:.4f} in [1.8, 2.2] -- "
                                f"carries it (Goldstone, 1/q^2 static)")
    check(A["B"] > 4, f"L-GEO GATE B flexural: A = {A['B']:.4f} > 4 -- cubic growth, NOT "
                      f"additive: ELIMINATED")
    # ---- POST-HOC DIAGNOSTIC (labeled; a measurement, not a gate edit) ----------------------
    exact = lambda d: (d * d * (N - d) ** 2)
    rB_form = (exact(16) / exact(8))
    NN = 512
    QS2 = [2 * math.pi * m / NN for m in range(1, NN)]
    rB512 = (2.0 / NN) * sum((1 - math.cos(q * 8)) / Kf(q) ** 2 for q in QS2)
    rB256 = resist(kern["B"], 8)
    check(True, f"L-GEO POST-HOC DIAGNOSTIC (labeled): B's A = {A['B']:.4f} matches the ring "
                f"form d^2 (N-d)^2 ratio {rB_form:.4f} -- the 1/q^4 kernel gives R ~ N d^2 "
                f"(QUADRATIC, system-size dependent), not the cubic growth I predicted; "
                f"R(0,8) grows {rB512 / rB256:.3f}x from N = 256 to 512 (not a local "
                f"metric). The frozen '> 4' gate stays RED; B is still outside the additivity "
                f"window [1.8, 2.2], which is what the frozen adjudication uses", "note")
    check(A["G"] < 1.3, f"L-GEO GATE G gapped control: A = {A['G']:.4f} < 1.3 -- screened: "
                        f"ELIMINATED")
    check(A["F"] < 1.3, f"L-GEO GATE F free fermions (local density): A = {A['F']:.4f} < 1.3 "
                        f"-- compressible, saturating: ELIMINATED under local access")
    phase = [c / Kf(q) for c, q in zip(chiL, QS)]
    Aph = resist(phase, 16) / resist(phase, 8)
    check(1.8 <= Aph <= 2.2, f"L-GEO GATE F via its NON-LOCAL bosonized phase field: A = "
                             f"{Aph:.4f} in [1.8, 2.2] -- the elimination is ACCESS-RELATIVE")
    check(True, "L-GEO consequence (frozen): given CARRIER, earned geometry eliminates two "
                "genuinely different gapless candidates (F under local access, B) and the "
                "gapped control; survivors {P, M}. The owner's success bar is met -- "
                "conditionally on CARRIER", "note")
    return {"A": A, "A_F_phase": Aph, "ring_identity_dev": dev, "fermi_dos": dos}


# ---------------- L-LOR ------------------------------------------------------------------------------
def leg_LOR():
    print("\n=== L-LOR: SUPPLIED PROBE STRUCTURE -- IR boost-compatible symmetric stress "
          "(v_g v_p constant) ===")
    disp = {"P": lambda k: 2 * math.sin(k / 2), "F": lambda p: 2 * math.sin(p),
            "M": lambda k: Kf(k), "B": lambda k: Kf(k),
            "G": lambda k: math.sqrt(0.25 + Kf(k))}
    k1 = 2 * math.pi * 2 / N
    k2 = 2 * k1
    h = 1e-6
    out = {}
    for lab, w in disp.items():
        def prod(k):
            vg = (w(k + h) - w(k - h)) / (2 * h)
            base = w(0.0) if lab == "G" else 0.0
            vp = w(k) / k if lab != "G" else w(k) / k
            return vg * vp
        r = prod(k2) / prod(k1)
        out[lab] = r
    for lab in ("P", "F", "G"):
        check(abs(out[lab] - 1) < 0.05, f"L-LOR GATE {lab}: IR ratio v_g v_p(2k)/v_g v_p(k) = "
                                        f"{out[lab]:.4f} (|r - 1| < 0.05): boost-compatible")
    for lab in ("M", "B"):
        check(3.5 <= out[lab] <= 4.5, f"L-LOR GATE {lab}: ratio = {out[lab]:.4f} in [3.5, 4.5] "
                                      f"-- v_g v_p ~ k^2: no symmetric stress in the IR, cannot "
                                      f"source the supplied massless probe: ELIMINATED")
    check(True, "L-LOR note: v = c per sector is a units choice; cross-sector light cones are "
                "U-1 territory, not tested here", "note")
    return out


# ---------------- L-ST ------------------------------------------------------------------------------
def leg_ST():
    print("\n=== L-ST: DOES THE GAUGE STRUCTURE FORCE FULL-STRESS COUPLING, OR MERELY PERMIT "
          "IT? ===")
    rng = random.Random(SEED)
    null, worst = null_space(cons_rows(random_pairs(2, 16, rng), 2))
    check(len(null) == 2, f"L-ST GATE: D = 2 conservation null space of the declared bilinear "
                          f"family has nullity {len(null)} (predicted 2: canonical + "
                          f"xi-improvement) -- full-stress coupling PERMITTED, not FORCED")
    check(True, "L-ST carried (not re-tested): IR Weyl fixes xi = 0 in D = 2 (CP-1); TT probes "
                "see a rank-1, vacuous form (CP-1)", "note")
    bas = F.basis(2)
    tower = F.null_space_cols([F.flat(F.cons_map(B)) for _, _, B in bas])
    check(len(tower) == 4, f"Matched control: FS-1 phonon conserved tower at R = 2 has dim "
                           f"{len(tower)} (recorded 4) -- FS-1 preserved", "ctrl")
    return {"nullity": len(null), "fs1_tower_R2": len(tower)}


def adjudicate(rG, rL, rS):
    A = rG["A"]
    gapless = ["P", "F", "M", "B"]
    geo_surv = [x for x in gapless if 1.8 <= A[x] <= 2.2]
    geo_elim_gapless = [x for x in gapless if x not in geo_surv]
    lor_pass = [x for x in rL if abs(rL[x] - 1) < 0.05]
    both = [x for x in geo_surv if x in lor_pass]
    earned = ("DERIVED" if geo_surv == ["P"] else
              "CONSTRAINED-NONUNIQUE" if len(geo_surv) > 1 else "FAILS")
    with_sup = ("SELECTED-IN-CLASS" if both == ["P"] else
                "CONSTRAINED-NONUNIQUE" if len(both) > 1 else "FAILS")
    return {"bar_met": len(geo_elim_gapless) >= 1, "eliminated_by_earned": geo_elim_gapless,
            "earned_survivors": geo_surv, "earned_verdict": earned,
            "supplied_pass": lor_pass, "earned_plus_supplied_survivors": both,
            "earned_plus_supplied_verdict": with_sup,
            "stress_coupling": "PERMITTED, not forced" if rS["nullity"] == 2 else "?",
            "overall": "CLASS-SPLIT across layers",
            "conditions": ["CARRIER (declared bridging premise)",
                           "supplied Lorentz/gauge probe structure (for the second layer)",
                           "relative to the tested candidate set"]}


def main():
    t0 = time.time()
    print("RS-1: IS THE GAPLESS PHONON SECTOR SELECTED, OR MERELY CHOSEN? (charter frozen at "
          "1f18205)")
    rG = leg_GEO()
    rL = leg_LOR()
    rS = leg_ST()
    adj = adjudicate(rG, rL, rS)
    print("\n=== ADJUDICATION (frozen outcome rule, computed from the measurements) ===")
    for k in ("bar_met", "eliminated_by_earned", "earned_survivors", "earned_verdict",
              "earned_plus_supplied_survivors", "earned_plus_supplied_verdict",
              "stress_coupling", "overall", "conditions"):
        check(True, f"{k}: {adj[k]}", "note")
    out = {"instrument": "rs1_retained", "charter_commit": "1f18205", "date": "2026-09-25",
           "LGEO": rG, "LLOR": rL, "LST": rS, "adjudication": adj, "halts": HALT,
           "checks": CHECKS, "failures": FAIL, "elapsed_s": round(time.time() - t0, 2),
           "hard_stop": "verdict recorded"}
    path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                         "RS1_RETAINED_RESULT.json"))
    with open(path, "wb") as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True, default=float).encode())
    sha = hashlib.sha256(open(path, "rb").read()).hexdigest()
    print(f"\nartifact written: {path} (sha {sha[:16]}...)")
    n_ok = sum(1 for c in CHECKS if c["ok"])
    print(f"\nRS-1 RETAINED-SECTOR ATTACK: {n_ok}/{len(CHECKS)} checks passed; failures: "
          f"{len(FAIL)}; halts: {len(HALT)}")
    if HALT:
        print("HALT: an analytic identity breached -- instrument bug, never physics. "
              "No verdict may be issued from this run.")
    else:
        print("HARD STOP: verdict recorded pending owner ruling.")
    sys.exit(0 if not FAIL else 1)


if __name__ == "__main__":
    main()
