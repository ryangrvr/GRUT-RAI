#!/usr/bin/env python3
"""GR2-d2 -- quantum cone separation (frozen instrument).

Charter: GR2D2_QCONE_CHARTER_01.md, frozen at commit 75f2069, under the
GR2-d owner ruling: a NARROW re-charter of GR2-d gate Q-2 only. The
classical, exchange, relabeling, and memory legs are adjudicated and
not reopened; GR2-d's V-2/V-3 failures stand under every outcome here.

Question (the owner's, frozen): can an earned GRUT constraint
distinguish genuinely different quantum propagation cones?

The owner's three pre-run gates, implemented in order: (1) parameter
separation established from the exact transverse-field dispersion
BEFORE any front measurement; (2) the estimator calibrated on two
non-target sectors (disclosed pre-freeze) and anchored to the GR2-d
recorded sector-A table; (3) the separation thresholds frozen in the
charter before the targets were ever measured. Hard rule (the
owner's): if the separation gates fail, the failure is recorded --
no parameter re-selection.

Machinery: the GR2-d quantum-front estimator replicated verbatim
(X-probe path). Pure stdlib. Deterministic (no RNG). Single run.
Run: python3 calc/gr2d2_qcone.py   (writes ../GR2D2_QCONE_RESULT.json)
"""

import hashlib
import json
import math
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from partition_selection_p1 import jacobi_eig
from s41_sel4 import dense, edges, gram_psd, op_add, placed, HX, HZ

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

# ---------------- P-1: parameter separation (before any front leg) ------
print("=== P-1: PARAMETER SEPARATION (exact dispersion, computed before "
      "the front legs) ===")
TARGET_C = (1.0, 0.9045, 0.0)
TARGET_D = (0.5, 0.9, 0.0)


def v_analytic(J, h):
    # exact transverse-field group velocity, maximized on a k-grid:
    # eps(k) = 2 sqrt(J^2 + h^2 - 2 J h cos k); v = d eps / d k
    best = 0.0
    for i in range(1, 5000):
        k = math.pi * i / 5000.0
        root = math.sqrt(J * J + h * h - 2.0 * J * h * math.cos(k))
        best = max(best, 2.0 * J * h * math.sin(k) / root)
    return best


vC = v_analytic(TARGET_C[0], TARGET_C[1])
vD = v_analytic(TARGET_D[0], TARGET_D[1])
MEAS["analytic_velocities"] = {"C": vC, "D": vD, "ratio": vC / vD}
halt_check(abs(vC - 1.8090) < 1e-3 and abs(vD - 1.0000) < 1e-3
           and vC / vD >= 1.5,
           f"P-1 the targets are analytically separated BEFORE "
           f"measurement: v_C = {vC:.6f} (2 min(J,h) = 1.8090), v_D = "
           f"{vD:.6f} (1.0000), ratio {vC / vD:.4f} >= 1.5; D is not a "
           f"rescale of C (J/h = 1.105 vs 0.556)")

# ---------------- the GR2-d front estimator (verbatim, X path) ----------
LQ = 7
DQ = 2 ** LQ


def open_chain(J, hx, hz):
    H = {}
    for i in range(LQ - 1):
        H = op_add(H, {placed(LQ, [(i, 3), (i + 1, 3)]): 1.0}, J)
    for i in range(LQ):
        H = op_add(H, {placed(LQ, [(i, 1)]): 1.0}, hx)
        if hz:
            H = op_add(H, {placed(LQ, [(i, 3)]): 1.0}, hz)
    return H


def real(M):
    return [[x.real for x in r] for r in M]


def front_quantum(J, hx, hz, tmax):
    Hop = open_chain(J, hx, hz)
    Hr = real(dense(Hop, LQ))
    lam, V = jacobi_eig(Hr)
    Xd = [[sum(V[i][m] * V[i ^ 1][n] for i in range(DQ)) for n in range(DQ)]
          for m in range(DQ)]

    def apply_evolved(c, t):
        u = [complex(math.cos(-lam[m] * t), math.sin(-lam[m] * t)) * c[m]
             for m in range(DQ)]
        y = [sum(Xd[m][n] * u[n] for n in range(DQ)) for m in range(DQ)]
        z = [complex(math.cos(lam[m] * t), math.sin(lam[m] * t)) * y[m]
             for m in range(DQ)]
        return [sum(V[i][m] * z[m] for m in range(DQ)) for i in range(DQ)]

    tq = [0.05 * i for i in range(int(round(tmax / 0.05)) + 1)]
    rows = {r: [] for r in range(1, 6)}
    unit_dev = 0.0
    for t in tq:
        p = apply_evolved([V[0][m] for m in range(DQ)], t)
        if abs(t - 2.0) < 1e-12:
            unit_dev = abs(math.sqrt(sum(abs(x) ** 2 for x in p)) - 1.0)
        for r in range(1, 6):
            a = apply_evolved([V[1 << r][m] for m in range(DQ)], t)
            F = math.sqrt(sum(abs(a[i] - p[i ^ (1 << r)]) ** 2
                              for i in range(DQ)))
            rows[r].append(F)
    tstar = {}
    for r in range(1, 6):
        h = rows[r]
        thr = 0.1 * max(h)
        tstar[r] = next(tq[i] for i, x in enumerate(h) if x > thr)
    f0max = max(rows[r][0] for r in range(1, 6))
    return Hop, Hr, tstar, f0max, unit_dev


def lsq_slope(tstar):
    rs = list(range(1, 6))
    tv = [tstar[r] for r in rs]
    n = len(rs)
    sr, st = sum(rs), sum(tv)
    srr = sum(r * r for r in rs)
    srt = sum(r * t for r, t in zip(rs, tv))
    return (n * srt - sr * st) / (n * srr - sr * sr)


# ---------------- RQ: procedure controls (halt-grade) -------------------
print("\n=== RQ: PROCEDURE CONTROLS (the GR2-d anchor and the two "
      "non-target calibration sectors) ===")
_, _, tsA, f0A, udA = front_quantum(1.0, HX, HZ, 6.0)
REC_A = {1: 0.05, 2: 0.45, 3: 0.90, 4: 1.40, 5: 1.90}
halt_check(all(abs(tsA[r] - REC_A[r]) < 1e-9 for r in range(1, 6)),
           f"RQ-1 the GR2-d recorded sector-A table replicates exactly on "
           f"its original [0, 6] window: t* = "
           f"{[round(tsA[r], 2) for r in range(1, 6)]} (recorded 0.05, "
           f"0.45, 0.90, 1.40, 1.90) -- the estimator is anchored to the "
           f"accepted GR2-d run")
_, _, tsE2, f0E2, udE2 = front_quantum(0.7, 0.6, 0.0, 8.0)
REC_E2 = {1: 0.10, 2: 0.65, 3: 1.30, 4: 2.00, 5: 2.70}
halt_check(all(abs(tsE2[r] - REC_E2[r]) < 1e-9 for r in range(1, 6)),
           f"RQ-2 calibration sector E2 = (0.7, 0.6, 0) replicates its "
           f"disclosed table: t* = "
           f"{[round(tsE2[r], 2) for r in range(1, 6)]} (calibrated 0.10, "
           f"0.65, 1.30, 2.00, 2.70; analytic v 1.2, systematic x1.2723)")
_, _, tsE3, f0E3, udE3 = front_quantum(0.8, 0.75, 0.0, 8.0)
REC_E3 = {1: 0.10, 2: 0.55, 3: 1.10, 4: 1.70, 5: 2.25}
halt_check(all(abs(tsE3[r] - REC_E3[r]) < 1e-9 for r in range(1, 6)),
           f"RQ-3 calibration sector E3 = (0.8, 0.75, 0) replicates its "
           f"disclosed table: t* = "
           f"{[round(tsE3[r], 2) for r in range(1, 6)]} (calibrated 0.10, "
           f"0.55, 1.10, 1.70, 2.25; analytic v 1.5, systematic x1.2232)")
MEAS["controls"] = {"A": tsA, "E2": tsE2, "E3": tsE3}

# ---------------- the targets (measured only here) -----------------------
print("\n=== S: THE TARGETS (first and only measurement; thresholds "
      "frozen in the charter before this run) ===")
HC, HrC, tsC, f0C, udC = front_quantum(*TARGET_C, 8.0)
HD, HrD, tsD, f0D, udD = front_quantum(*TARGET_D, 8.0)
MEAS["targets"] = {"C": tsC, "D": tsD}
halt_check(max(f0A, f0E2, f0E3, f0C, f0D) < 1e-10,
           f"QI-1 identity: F(r, 0) < 1e-10 for every sector and r (max "
           f"{max(f0A, f0E2, f0E3, f0C, f0D):.1e})")
halt_check(max(udA, udE2, udE3, udC, udD) < 1e-8,
           f"QI-2 unitarity at t = 2: max deviation "
           f"{max(udA, udE2, udE3, udC, udD):.1e} < 1e-8, every sector")

slC, slD = lsq_slope(tsC), lsq_slope(tsD)
ratio = slD / slC
MEAS["separation"] = {"slope_C": slC, "slope_D": slD,
                      "slope_ratio": ratio,
                      "v_est_C": 1.0 / slC, "v_est_D": 1.0 / slD,
                      "gap_r5": abs(tsC[5] - tsD[5]),
                      "gap_rel": abs(tsC[5] - tsD[5])
                      / max(tsC[5], tsD[5])}
check(1.5 <= ratio <= 2.1,
      f"S-1 THE CONES SEPARATE: fitted-slope ratio slope_D / slope_C = "
      f"{ratio:.4f} in [1.5, 2.1] (analytic ratio 1.809; measured v_est "
      f"C {1.0 / slC:.4f}, D {1.0 / slD:.4f}) -- frozen blind, before "
      f"this measurement")
gap = abs(tsC[5] - tsD[5])
check(gap > 0.25 * max(tsC[5], tsD[5]),
      f"S-2 the GR2-d Q-2 form at STRICTER threshold: |t*_C(5) - "
      f"t*_D(5)| = {gap:.2f} > 0.25 * max({tsC[5]:.2f}, {tsD[5]:.2f}) = "
      f"{0.25 * max(tsC[5], tsD[5]):.3f} (the threshold that failed in "
      f"GR2-d was 0.10)")
monoC = all(tsC[r + 1] > tsC[r] for r in range(1, 5))
monoD = all(tsD[r + 1] > tsD[r] for r in range(1, 5))
gC = gram_psd(HrC, real(dense({placed(LQ, [(i, 1)]): 1.0
                               for i in range(LQ)}, LQ)))
gD = gram_psd(HrD, real(dense({placed(LQ, [(i, 1)]): 1.0
                               for i in range(LQ)}, LQ)))
s3_ok = (monoC and monoD and edges(HC) == edges(HD)
         and gC >= -1e-12 and gD >= -1e-12)
check(s3_ok,
      f"S-3 both targets EARNED-ADMISSIBLE: fronts strictly outward "
      f"(C {[tsC[r] for r in range(1, 6)]}; D "
      f"{[tsD[r] for r in range(1, 6)]}); identical interaction graphs; "
      f"ground-state Gram of sum X_i PSD (C {gC:.1e}, D {gD:.1e}) -- the "
      f"different-cone sector D survives the whole earned battery")
ELIM = [{"leg": "S", "system": "quantum sector D = (0.5, 0.9, 0)",
         "eliminated": not s3_ok,
         "tests": {"gram_min": gD, "graph_same": edges(HC) == edges(HD),
                   "fronts_monotone": monoD}}]

check(True, "consequence discipline (frozen from the ruling): a clean "
            "result establishes in-class quantum cone DISTINCTION only; "
            "the universal cone is NOT thereby derived, and GR2-d's "
            "V-2/V-3 failures stand at recorded strength under every "
            "outcome here", "note")
check(True, "the hard rule (frozen from the ruling): had S-1/S-2 "
            "failed, the failure would be recorded with no parameter "
            "re-selection", "note")

# ---------------- verdict -------------------------------------------------
gated = [c for c in CHECKS if c["kind"] in ("ok", "ctrl")]
n_ok = sum(1 for c in gated if c["pass"])
fails = [c["summary"] for c in gated if not c["pass"]]
s12_ok = 1.5 <= ratio <= 2.1 and gap > 0.25 * max(tsC[5], tsD[5])

if HALT:
    verdict = "HALT"
elif not fails:
    verdict = "D2-QCONE-DISTINCT"
elif not s12_ok and s3_ok:
    verdict = "D2-QCONE-INDISTINCT"
else:
    verdict = "D2-PARTIAL"

detail = ("two earned-admissible quantum sectors of the record's own "
          "chain family, analytically separated before measurement "
          "(exact transverse-field velocities 1.809 vs 1.000), exhibit "
          "measurably distinct causal cones under thresholds frozen "
          "blind -- quantum causal-cone distinction is demonstrable "
          "within the tested class. The irreducibility demonstration "
          "for the cone coordinate is strengthened: locality + "
          "influence + geometry + memory + quantum dynamics do not "
          "imply c_universal. The universal cone is NOT thereby "
          "derived; GR2-d's D-PARTIAL and its V-2/V-3 failures stand "
          "as recorded")

out = {
    "fork": "GR2-d2",
    "charter": "GR2D2_QCONE_CHARTER_01.md (frozen 75f2069)",
    "directive": "GR2D_OWNER_RULING_01.md (narrow authorization: a "
                 "re-charter of GR2-d gate Q-2 only)",
    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S+00:00", time.gmtime()),
    "environment": {"python": sys.version.split()[0], "pure_stdlib": True,
                    "deterministic": "no RNG in this fork"},
    "defect_history": [],
    "measurements": MEAS,
    "elimination_table": ELIM,
    "checks": CHECKS,
    "adjudication": {
        "verdict": verdict,
        "verdict_detail": detail if verdict == "D2-QCONE-DISTINCT" else "",
        "scope": "exactly the GR2-d quantum-leg construction: 7-site "
                 "open chains, D = 1, the X-commutator front estimator. "
                 "The classical, exchange, relabeling, and memory legs "
                 "are adjudicated in GR2-d and untouched here",
    },
    "elapsed_s": round(time.time() - T0, 2),
}

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                    "GR2D2_QCONE_RESULT.json")
blob = json.dumps(out, indent=1)
with open(path, "w") as f:
    f.write(blob)
sha = hashlib.sha256(blob.encode()).hexdigest()
print(f"\nartifact written: {os.path.abspath(path)} (sha {sha[:16]}...)")
print(f"\nGR2-d2: {n_ok}/{len(gated)} gated checks passed; failures: "
      f"{len(fails)}; halts: {len(HALT)}")
if HALT:
    print("HALT: a control or analytic identity breached -- instrument "
          "bug, never physics. No verdict may be issued from this run.")
    sys.exit(2)
print(f"VERDICT: {verdict}")
print("HARD STOP: verdict recorded pending owner ruling.")
sys.exit(0 if not fails else 1)
