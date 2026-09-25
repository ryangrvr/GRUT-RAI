#!/usr/bin/env python3
"""ca1_carrier: can 'the gravitational bath is the geometry carrier' be derived?

CHARTER: CA1_CARRIER_CHARTER_01.md (pre-registration frozen at commit e67b1d5 BEFORE this
instrument ran; authority GitHub Issue #2 owner comment 5837554943). No omega^7 and no supplied
Lorentz layer anywhere. The working hypothesis -- recovered geometry is a property of the
substrate operator K, carried by any sector built on it -- is attacked, not assumed.

Candidates on one ring substrate K = 4 sin^2(k/2): P phonon | M Schrodinger boson (z = 2) |
T rescaled twin phonon | D classical relaxational field | F free fermions (non-carrier contrast).

Legs: L-MC many carriers? (resistance profile + per-sector hop recovery) | L-SEL earned
selectors: (i) P-2 cone vs the classical carrier, (ii) non-carrier bath F, (iii) access.

Pure stdlib. Run: python3 calc/ca1_carrier.py
"""
import cmath
import hashlib
import json
import math
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rs1_retained import lindhard, resist, QS, N as NR

FAIL = []
CHECKS = []
HALT = []
N64 = 64
T3 = (0.02, 0.04, 0.08)


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


def powers(op, mmax=20):
    v = [0.0] * N64
    v[0] = 1.0
    out = [v[:]]
    for _ in range(mmax):
        v = op(v)
        out.append(v[:])
    return out


def Kop(v):
    return [2 * v[i] - v[(i + 1) % N64] - v[(i - 1) % N64] for i in range(N64)]


def hop_op(v):
    return [-(v[(i + 1) % N64] + v[(i - 1) % N64]) for i in range(N64)]


PK = powers(Kop)
PH = powers(hop_op)


def resp(kind, d, t):
    if kind in ("P", "T"):
        a = 1.0 if kind == "P" else 0.7 / 2.3
        return sum((-1) ** m * t ** (2 * m + 1) * a ** m * PK[m][d] / math.factorial(2 * m + 1)
                   for m in range(0, 10))
    if kind == "M":
        return abs(sum((-1j * t) ** m * PK[m][d] / math.factorial(m) for m in range(21)))
    if kind == "D":
        return sum((-t) ** m * PK[m][d] / math.factorial(m) for m in range(21))
    if kind == "F":
        return abs(sum((-1j * t) ** m * PH[m][d] / math.factorial(m) for m in range(21)))


def slope(kind, d):
    v = [abs(resp(kind, d, t)) for t in T3]
    s1 = math.log(v[1] / v[0]) / math.log(2)
    s2 = math.log(v[2] / v[1]) / math.log(2)
    return 2 * s1 - s2


def hop_recovery(kind):
    s = {d: slope(kind, d) for d in (1, 2, 3, 4)}
    return {d: 1 + (s[d] - s[1]) / (s[2] - s[1]) for d in (3, 4)}


# ---------------- L-MC ------------------------------------------------------------------------------
def leg_MC():
    print("\n=== L-MC: HOW MANY SECTORS CARRY THE SAME RECOVERED GEOMETRY? ===")
    kern = {"P": [1 / Kf(q) for q in QS], "M": [1 / Kf(q) for q in QS],
            "T": [1 / (0.7 * Kf(q)) for q in QS], "D": [1 / Kf(q) for q in QS]}
    dev = max(abs(resist(kern["P"], d) - d * (NR - d) / NR) for d in (1, 8, 32))
    halt_check(dev < 1e-9, f"L-MC control: phonon kernel reproduces R(0,d) = d(N-d)/N to "
                           f"{dev:.1e} (halt-grade)")
    prof = {lab: [resist(c, d) / resist(c, 1) for d in range(1, 33)] for lab, c in kern.items()}
    pdev = max(abs(a - b) for lab in ("M", "T", "D") for a, b in zip(prof[lab], prof["P"]))
    check(pdev < 1e-12, f"L-MC GATE (a): normalized resistance profile R(0,d)/R(0,1), "
                        f"d = 1..32, identical for P, M, T, D to {pdev:.1e} < 1e-12")
    hops = {}
    for lab in ("P", "M", "T", "D"):
        hops[lab] = hop_recovery(lab)
        ok = all(abs(hops[lab][d] - d) < 0.3 for d in (3, 4))
        check(ok, f"L-MC GATE (b) {lab}: hop distances recovered from its OWN short-time "
                  f"response: d_hat(3) = {hops[lab][3]:.3f}, d_hat(4) = {hops[lab][4]:.3f} "
                  f"(each within 0.3)")
    check(True, "L-MC consequence (frozen): genuinely different sectors -- z = 1 and z = 2, "
                "quantum and classical, rescaled -- carry IDENTICAL recovered geometric data. "
                "The recovered geometry is a property of the substrate operator K; 'the "
                "carrier' is not unique", "note")
    return {"ring_dev": dev, "profile_dev": pdev, "hops": hops}


# ---------------- L-SEL -----------------------------------------------------------------------------
def leg_SEL():
    print("\n=== L-SEL: DOES EARNED STRUCTURE PICK ONE CARRIER, OR FORBID A NON-CARRIER BATH? ===")
    Ks = [Kf(q) for q in QS]

    def J(w):
        return sum(w / (k * k + w * w) for k in Ks) / NR

    def nu(w, T):
        return 0.0 if T == 0 else 2 * T * J(w) / w

    j1 = J(1.0)
    halt_check(nu(1.0, 0) == 0.0 and j1 > 0, f"L-SEL control: classical carrier at T = 0 has "
                                             f"noise exactly 0 with response J(1) = {j1:.4f} "
                                             f"> 0 (halt-grade)")
    m0 = nu(1.0, 0) - j1 / 2
    ok05 = nu(1.0, 0.5) - J(1.0) / 2
    bad05 = nu(3.0, 0.5) - J(3.0) / 2
    check(m0 < -1e-3, f"L-SEL GATE (i) T = 0: nu - J/2 = {m0:.4f} < -1e-3 at omega = 1 -- the "
                      f"classical carrier VIOLATES the P-2 floor")
    check(ok05 > 0 and bad05 < -1e-3,
          f"L-SEL GATE (i) T = 0.5: admissible at omega = 1 ({ok05:.4f}) but violates at "
          f"omega = 3 ({bad05:.4f}) -- excluded at every T once omega > 4T")
    check(True, "L-SEL (i) consequence (frozen): 𝔠_full ELIMINATES the classical relaxational "
                "carrier -- an earned elimination of a genuinely different carrier. Quantum "
                "carriers P, M, T sit on the floor in vacuum (P-2, GR-1 L-H; noted by "
                "construction, not re-gated)", "note")
    hF = hop_recovery("F")
    okF = all(abs(hF[d] - d) < 0.3 for d in (3, 4))
    chiL = lindhard()
    AF = resist(chiL, 16) / resist(chiL, 8)
    check(okF, f"L-SEL GATE (ii) non-carrier bath F: its own hop recovery d_hat(3) = "
               f"{hF[3]:.3f}, d_hat(4) = {hF[4]:.3f} -- shares the graph and passes locality/"
               f"hop geometry")
    check(AF < 1.3, f"L-SEL GATE (ii) F's local additive metric FAILS: A = {AF:.4f} < 1.3 -- "
                    f"it does not carry the recovered additive geometry")
    check(True, "L-SEL (ii) note: F's fermionic vacuum sits on the P-2 floor (by construction) "
                "-- 𝔠_full-admissible", "note")
    check(True, "L-SEL (ii) consequence (frozen): a gravitational bath that does NOT carry the "
                "recovered additive geometry passes influence positivity, locality and "
                "hop-geometry recovery. Earned structure does NOT force the bath to be the "
                "geometry carrier", "note")
    check(True, "L-SEL (iii) consequence (frozen): among the surviving carriers {P, M, T} -- "
                "admissible, geometrically identical -- which one the gravitational probe "
                "couples to is an ACCESS declaration (P-6: the seed is irreducible). CARRIER "
                "reduces to: the gravitational probe's access seed coincides with the "
                "geometry-recovery access seed. Supplied", "note")
    return {"J1": j1, "T0_margin": m0, "T05_w1": ok05, "T05_w3": bad05, "F_hops": hF,
            "F_additivity": AF}


def adjudicate(rM, rS):
    carriers = [x for x in ("P", "M", "T", "D")
                if rM["profile_dev"] < 1e-12 and all(abs(rM["hops"][x][d] - d) < 0.3
                                                     for d in (3, 4))]
    cut = ["D"] if (rS["T0_margin"] < -1e-3 and rS["T05_w3"] < -1e-3) else []
    surv = [x for x in carriers if x not in cut]
    carrier_set = ("CONSTRAINED-NONUNIQUE" if len(surv) > 1 else
                   "UNIQUE" if len(surv) == 1 else "FAILS")
    F_survives = rS["F_additivity"] < 1.3 and all(abs(rS["F_hops"][d] - d) < 0.3
                                                  for d in (3, 4))
    ident = "DERIVED" if (len(surv) == 1 and not F_survives) else \
        "IRREDUCIBLE INPUT (reduced to access-seed coincidence, P-6)"
    return {"carriers": carriers, "cut_by_earned": cut, "surviving_carriers": surv,
            "carrier_set": carrier_set, "bar_met_for_carrier_set": len(cut) >= 1,
            "noncarrier_bath_survives": F_survives, "CARRIER_identification": ident}


def main():
    t0 = time.time()
    print("CA-1: CAN 'THE GRAVITATIONAL BATH IS THE GEOMETRY CARRIER' BE DERIVED? (charter "
          "frozen at e67b1d5)")
    rM = leg_MC()
    rS = leg_SEL()
    adj = adjudicate(rM, rS)
    print("\n=== ADJUDICATION (frozen outcome rule, computed from the measurements) ===")
    for k, v in adj.items():
        check(True, f"{k}: {v}", "note")
    out = {"instrument": "ca1_carrier", "charter_commit": "e67b1d5", "date": "2026-09-25",
           "LMC": rM, "LSEL": rS, "adjudication": adj, "halts": HALT, "checks": CHECKS,
           "failures": FAIL, "elapsed_s": round(time.time() - t0, 2),
           "hard_stop": "verdict recorded"}
    path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                         "CA1_CARRIER_RESULT.json"))
    with open(path, "wb") as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True, default=str).encode())
    sha = hashlib.sha256(open(path, "rb").read()).hexdigest()
    print(f"\nartifact written: {path} (sha {sha[:16]}...)")
    n_ok = sum(1 for c in CHECKS if c["ok"])
    print(f"\nCA-1 CARRIER ATTACK: {n_ok}/{len(CHECKS)} checks passed; failures: {len(FAIL)}; "
          f"halts: {len(HALT)}")
    if HALT:
        print("HALT: an analytic identity breached -- instrument bug, never physics. "
              "No verdict may be issued from this run.")
    else:
        print("HARD STOP: verdict recorded pending owner ruling.")
    sys.exit(0 if not FAIL else 1)


if __name__ == "__main__":
    main()
