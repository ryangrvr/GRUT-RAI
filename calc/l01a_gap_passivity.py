#!/usr/bin/env python3
"""l01a_gap_passivity: the first instrument of the Level-0 necessity sweep.

Charter: L0_1A_CHARTER_01.md, frozen at commit bb77df9, under
GRUT_PROGRAM_REOPEN_02.md (the successor program; the owner's four
prohibitions bind: no retroactive success conditions, no battery change
after results, no instrument-failure-as-necessity, no
interesting-as-derived).

Two deletions, two properties, never conflated:
    gap deletion      -> P_memory      (D-GAP members only)
    passivity deletion -> P_positivity (D-PASS members only)

Hypotheses under attack (not protection):
    H-GAP:  removing the spectral gap destroys finite-memory-grade decay.
    H-PASS: removing passivity destroys the positivity structure.

Pure stdlib. Deterministic (no RNG). Single run.
Run: python3 calc/l01a_gap_passivity.py   (writes ../L0_1A_RESULT.json)
"""

import hashlib
import json
import math
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c1_seam import World, build_K
from partition_selection_p1 import jacobi_eig

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
TAUS = [1.0 + 0.5 * i for i in range(79)]   # 1.0 .. 40.0 step 0.5


def build_Kp(N, pin, spring23=1.0):
    """The C1-a stiffness, parametric: springs 1.0 (the chain spring
    (2,3) overridable for D-PASS), pins `pin` -- build_K's structure
    exactly, with eps-modulation replaced by the two dials."""
    K = [[0.0] * N for _ in range(N)]
    for i in range(N):
        K[i][i] = pin
    for i in range(N - 1):
        w = spring23 if i == 2 else 1.0
        K[i][i + 1] -= w
        K[i + 1][i] -= w
        K[i][i] += w
        K[i + 1][i + 1] += w
    return K


def bath_kernel(N, pin, spring23=1.0):
    """(lambda_min, k(tau) on the grid, k(0)) for the bath block."""
    K = build_Kp(N, pin, spring23)
    bath = [row[1:] for row in K[1:]]
    lam, V = jacobi_eig(bath)
    u2 = [V[0][k] ** 2 for k in range(N - 1)]
    k0 = sum(u2)
    ks = [sum(u2[k] * math.exp(-lam[k] * t) for k in range(N - 1))
          for t in TAUS]
    return min(lam), ks, k0


def fit_residuals(ks):
    """Frozen comparator: max abs residual of least-squares linear fits
    of ln k vs tau (exponential model) and ln k vs ln tau (algebraic)."""
    y = [math.log(k) for k in ks]

    def rmax(xs):
        n = len(xs)
        sx, sy = sum(xs), sum(y)
        sxx = sum(x * x for x in xs)
        sxy = sum(x * yy for x, yy in zip(xs, y))
        b = (n * sxy - sx * sy) / (n * sxx - sx * sx)
        a = (sy - b * sx) / n
        return max(abs(yy - (a + b * x)) for x, yy in zip(xs, y)), b

    r_exp, rate = rmax(TAUS)
    r_alg, slope = rmax([math.log(t) for t in TAUS])
    grade = "EXPONENTIAL-GRADE" if r_exp < r_alg else "ALGEBRAIC-GRADE"
    return r_exp, r_alg, grade, rate, slope


# ---------------- RC: controls (halt-grade) -----------------------------
print("=== RC: CONTROLS ===")
W1 = World(24, 1.0)
REC_K = [("A", 1.0, 0.1594754), ("B", 1.0, 0.1328810),
         ("A", 0.5, 0.3579003), ("B", 0.5, 0.2874716)]
rep_ok = all(abs(W1.frozen(0 if ep == "A" else 1, tau) - rec) < 5e-8
             for ep, tau, rec in REC_K)
K_mine = build_Kp(24, 0.3)
K_seal = build_K(24, 0.0)
builder_dev = max(abs(K_mine[i][j] - K_seal[i][j])
                  for i in range(24) for j in range(24))
halt_check(rep_ok and builder_dev < 1e-15,
           f"RC-1 the sealed C1-a kernels replicate (all four |Delta| < "
           f"5e-8) and the parametric builder at pin = 0.3 equals "
           f"build_K(24, 0) entrywise (max dev {builder_dev:.1e})")

# ---------------- D-GAP -------------------------------------------------
print("\n=== D-GAP: gap deletion -> P_memory (this leg adjudicates "
      "P_memory ONLY) ===")
PINS = [0.3, 0.1, 0.03, 0.01, 0.003, 0.0]
gap_rows = {}
id_ok = True
for pin in PINS:
    lmin, ks, k0 = bath_kernel(24, pin)
    r_exp, r_alg, grade, rate, slope = fit_residuals(ks)
    gap_rows[pin] = {"lambda_min": lmin, "k40": ks[-1], "k0": k0,
                     "R_exp": r_exp, "R_alg": r_alg, "grade": grade,
                     "fit_rate": -rate, "fit_powerlaw": -slope}
    id_ok = id_ok and abs(k0 - 1.0) < 1e-12 and lmin >= pin - 1e-12
    print(f"   pin={pin:5.3f}: lambda_min={lmin:.6f}  k(40)={ks[-1]:.4e}"
          f"  R_exp={r_exp:.4f}  R_alg={r_alg:.4f}  -> {grade}")
halt_check(id_ok, "RC-2 identities: k(0) = 1 (|Delta| < 1e-12) and "
                  "lambda_min >= pin (halt-grade; an eigensolver bug, "
                  "never physics) for every D-GAP member")
MEAS["D_GAP"] = {str(p): r for p, r in gap_rows.items()}

k40_anchor = gap_rows[0.3]["k40"]
contrast = gap_rows[0.0]["k40"] / k40_anchor
g1 = k40_anchor < 1e-5 and contrast > 100.0
check(g1, f"G-1 THE DELETION CONTRAST: k(40 | pin=0.3) = "
          f"{k40_anchor:.3e} < 1e-5 (analytic bound e^-12 = 6.1e-6) and "
          f"k(40 | pin=0)/k(40 | pin=0.3) = {contrast:.3e} > 100")
g2 = (gap_rows[0.3]["grade"] == "EXPONENTIAL-GRADE"
      and gap_rows[0.0]["grade"] == "ALGEBRAIC-GRADE")
check(g2, f"G-2 GRADE AT THE ENDS (frozen comparator): anchor "
          f"{gap_rows[0.3]['grade']} (R_exp {gap_rows[0.3]['R_exp']:.3f} "
          f"vs R_alg {gap_rows[0.3]['R_alg']:.3f}); deleted "
          f"{gap_rows[0.0]['grade']} (R_alg {gap_rows[0.0]['R_alg']:.3f} "
          f"vs R_exp {gap_rows[0.0]['R_exp']:.3f})")
lam_ns = {}
for N in (24, 48, 96):
    lmin, _, _ = bath_kernel(N, 0.0)
    lam_ns[N] = lmin
r1, r2 = lam_ns[24] / lam_ns[48], lam_ns[48] / lam_ns[96]
MEAS["N_scan_pin0"] = {"lambda_min": {str(n): v for n, v in lam_ns.items()},
                       "ratios": [r1, r2]}
g3 = 3.5 <= r1 <= 4.5 and 3.5 <= r2 <= 4.5
check(g3, f"G-3 THE DELETION IS REAL (large-N): lambda_min(pin=0, N) "
          f"scales 1/N^2 -- ratios {r1:.3f}, {r2:.3f} in [3.5, 4.5]; the "
          f"deleted member's residual gap is a finite-size artifact")
check(True, "G-diag (ungated, the crossover map): the intermediate "
            "members classify "
            + ", ".join(f"pin={p}: {gap_rows[p]['grade']}"
                        for p in (0.1, 0.03, 0.01, 0.003))
            + " -- the property degrades where lambda_min * window ~ 1, "
            "as the design anticipated; reported, adjudicating nothing",
      "diag")

# ---------------- D-PASS ------------------------------------------------
print("\n=== D-PASS: passivity deletion -> P_positivity (this leg "
      "adjudicates P_positivity ONLY; pin = 0.3 held) ===")
pass_rows = {}
for w in (1.0, -0.3, -1.0):
    lmin, ks, k0 = bath_kernel(24, 0.3, spring23=w)
    mono_breach = max(ks[i + 1] - ks[i] for i in range(len(ks) - 1))
    pass_rows[w] = {"lambda_min": lmin, "k40": ks[-1], "k0": k0,
                    "max_monotone_breach": mono_breach}
    print(f"   spring(2,3)={w:+5.2f}: lambda_min={lmin:+.6f}  "
          f"k(40)={ks[-1]:.4e}  max step increase={mono_breach:.2e}")
MEAS["D_PASS"] = {str(w): r for w, r in pass_rows.items()}
p1 = (pass_rows[1.0]["lambda_min"] >= 0.3 - 1e-12
      and pass_rows[1.0]["max_monotone_breach"] <= 1e-12)
check(p1, f"P-1 the anchor is passive and completely monotone: "
          f"lambda_min = {pass_rows[1.0]['lambda_min']:.6f} >= 0.3; k "
          f"strictly decreasing on the grid")
p2 = pass_rows[-1.0]["lambda_min"] < 0.0
check(p2, f"P-2 the deep member breaches passivity: lambda_min = "
          f"{pass_rows[-1.0]['lambda_min']:.6f} < 0 (direction "
          f"guaranteed by Cauchy interlacing against the -0.7 principal "
          f"block eigenvalue; the instrument confirms the algebra)")
p3 = pass_rows[-1.0]["k40"] > pass_rows[-1.0]["k0"]
check(p3, f"P-3 the positivity phenomenon breaks with it: "
          f"k(40) = {pass_rows[-1.0]['k40']:.3e} > k(0) = 1 on the deep "
          f"member -- the kernel grows; complete monotonicity is gone")
check(True, f"P-diag (ungated, the boundary map): the marginal member "
            f"spring(2,3) = -0.3 has lambda_min = "
            f"{pass_rows[-0.3]['lambda_min']:+.6f} and max step increase "
            f"{pass_rows[-0.3]['max_monotone_breach']:.2e} -- reported, "
            f"adjudicating nothing", "diag")
check(True, "separation rule honored (frozen): P_memory was adjudicated "
            "only from D-GAP members and P_positivity only from D-PASS "
            "members; no cross-reading occurred", "note")

# ---------------- the two verdict lines (never composed) ----------------
gated = [c for c in CHECKS if c["kind"] in ("ok", "ctrl")]
n_ok = sum(1 for c in gated if c["pass"])
fails = [c["summary"] for c in gated if not c["pass"]]

if HALT:
    v_gap = v_pass = "HALT"
else:
    if g1 and g2 and g3:
        v_gap = "GAP: NECESSITY-CERTIFIED for P_memory"
    elif gap_rows[0.0]["grade"] == "EXPONENTIAL-GRADE" or not g1:
        v_gap = "GAP: NOT-LOAD-BEARING-ON-WINDOW"
    else:
        v_gap = "L01A-GAP-PARTIAL"
    if p1 and p2 and p3:
        v_pass = "PASSIVITY: NECESSITY-CERTIFIED for P_positivity"
    elif p2 and not p3:
        v_pass = "PASSIVITY: NOT-LOAD-BEARING"
    else:
        v_pass = "L01A-PASS-PARTIAL"

out = {
    "fork": "L0-1a (the successor program's first instrument)",
    "charter": "L0_1A_CHARTER_01.md (frozen bb77df9)",
    "authority": "GRUT_PROGRAM_REOPEN_02.md (owner decision, "
                 "post-deposit, 2026-09-28)",
    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S+00:00", time.gmtime()),
    "environment": {"python": sys.version.split()[0], "pure_stdlib": True,
                    "deterministic": "no RNG"},
    "defect_history": [],
    "measurements": MEAS,
    "checks": CHECKS,
    "adjudication": {
        "verdict_gap": v_gap,
        "verdict_passivity": v_pass,
        "composition": "the two lines are NEVER composed into a single "
                       "label (frozen rule)",
        "scope": "within the declared background mathematics (real "
                 "symmetric matrices, exact eigendecomposition) and the "
                 "tested construction class (the C1-a chain family), on "
                 "the declared window tau in [1, 40]. No claim about "
                 "'the axioms of reality'. No v4 channel moves; no red "
                 "gate is touched",
    },
    "elapsed_s": round(time.time() - T0, 2),
}
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                    "L0_1A_RESULT.json")
blob = json.dumps(out, indent=1)
with open(path, "w") as fh:
    fh.write(blob)
sha = hashlib.sha256(blob.encode()).hexdigest()
print(f"\nartifact written: {os.path.abspath(path)} (sha {sha[:16]}...)")
print(f"\nL0-1a: {n_ok}/{len(gated)} gated checks passed; failures: "
      f"{len(fails)}; halts: {len(HALT)}")
if HALT:
    print("HALT: a control breached -- instrument bug, never physics.")
    sys.exit(2)
print(f"VERDICT LINE 1: {v_gap}")
print(f"VERDICT LINE 2: {v_pass}")
print("HARD STOP: verdicts recorded pending owner ruling.")
sys.exit(0 if not fails else 1)
