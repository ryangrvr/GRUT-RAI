#!/usr/bin/env python3
"""l01b_locality: the second instrument of the Level-0 necessity sweep
(D-LOC).

Charter: L0_1B_CHARTER_01.md, frozen at commit 55dafe6, under
L0_1A_OWNER_RULING_01.md (D-LOC authorized; Outcomes A and B named in
advance) and GRUT_PROGRAM_REOPEN_02.md (the owner's four prohibitions
bind).

The frozen question (the owner's):
    Is locality actually necessary for the response itself, or only
    for geometry?

The deletion touches locality ONLY: every member keeps the pin (0.3)
and positive couplings, so gap and passivity -- both necessity-certified
in L0-1a -- are held fixed by construction. An M-gate breach at a
nonlocal member is therefore identity-impossible and is treated as HALT
(instrument bug, never physics); Outcome A is decidable only by a
future pin-free fork (out of scope, per charter Sec. 5).

Members (norm Sigma_{i<j} w_ij = 23 held): anchor (nearest-neighbor,
w = 1.0) -- alpha in {4, 3, 2, 1.5, 1, 0.5} -- deleted alpha = 0 (the
uniform complete graph). Geometry battery (pre-committed, charter
Sec. 2): resistance metric on L(w), Q = max R / min R, line-ordering
test; SURVIVES iff Q >= 12 and monotone; FAILS iff Q < 2.

Pure stdlib. Deterministic (no RNG). Single run.
Run: python3 calc/l01b_locality.py   (writes ../L0_1B_RESULT.json)
"""

import hashlib
import json
import math
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c1_seam import build_K
from partition_selection_p1 import jacobi_eig

T0 = time.time()
CHECKS = []
HALT = []
N = 24
PIN = 0.3
NORM = 23.0                       # the anchor's total spring weight
TAUS = [1.0 + 0.5 * i for i in range(79)]   # 1.0 .. 40.0 step 0.5 (L0-1a)
K40_L01A = 6.8195192260507686e-09  # the L0-1a artifact's recorded anchor


def check(ok, msg, kind="ok"):
    CHECKS.append({"kind": kind, "pass": bool(ok), "summary": msg})
    tag = {"ok": "GATE", "ctrl": "CONTROL", "note": "NOTE", "diag": "DIAG"}[kind]
    print(("PASS " if ok else "FAIL ") + tag + ": " + msg)


def halt_check(ok, msg):
    check(ok, msg, "ctrl")
    if not ok:
        HALT.append(msg)


# ---------------- member construction (frozen; charter Sec. 1) ----------
def weights(alpha):
    """w_ij = c_alpha * |i-j|^{-alpha}, c_alpha fixed by
    Sigma_{i<j} w_ij = 23. alpha = None is the anchor (nearest-neighbor,
    w = 1.0: 23 springs, norm held identically). alpha = 0 is the
    deleted member (uniform complete graph, w = 23/276 = 1/12)."""
    w = [[0.0] * N for _ in range(N)]
    if alpha is None:
        for i in range(N - 1):
            w[i][i + 1] = w[i + 1][i] = 1.0
        return w
    raw = sum((j - i) ** (-alpha) for i in range(N) for j in range(i + 1, N))
    c = NORM / raw
    for i in range(N):
        for j in range(i + 1, N):
            w[i][j] = w[j][i] = c * (j - i) ** (-alpha)
    return w


def laplacian(w):
    L = [[-w[i][j] for j in range(N)] for i in range(N)]
    for i in range(N):
        L[i][i] = sum(w[i][j] for j in range(N))
    return L


def stiffness(w):
    L = laplacian(w)
    return [[L[i][j] + (PIN if i == j else 0.0) for j in range(N)]
            for i in range(N)]


# ---------------- the L0-1a kernel machinery, unchanged -----------------
def bath_kernel(K):
    """(lambda_min, k(tau) on the grid, k(0)) for the (1:, 1:) block."""
    bath = [row[1:] for row in K[1:]]
    lam, V = jacobi_eig(bath)
    n = len(lam)
    u2 = [V[0][k] ** 2 for k in range(n)]
    k0 = sum(u2)
    ks = [sum(u2[k] * math.exp(-lam[k] * t) for k in range(n)) for t in TAUS]
    return min(lam), ks, k0


def fit_residuals(ks):
    """The L0-1a frozen grade comparator (M-diag only, ungated here)."""
    y = [math.log(k) for k in ks]

    def rmax(xs):
        n = len(xs)
        sx, sy = sum(xs), sum(y)
        sxx = sum(x * x for x in xs)
        sxy = sum(x * yy for x, yy in zip(xs, y))
        b = (n * sxy - sx * sy) / (n * sxx - sx * sx)
        a = (sy - b * sx) / n
        return max(abs(yy - (a + b * x)) for x, yy in zip(xs, y))

    r_exp = rmax(TAUS)
    r_alg = rmax([math.log(t) for t in TAUS])
    return "EXPONENTIAL-GRADE" if r_exp < r_alg else "ALGEBRAIC-GRADE"


# ---------------- the geometry battery (frozen; charter Sec. 2) ---------
def resistance(w):
    """R_ij = (e_i - e_j)^T L+ (e_i - e_j) on the coupling Laplacian
    (pins excluded). Returns (R, n_zero_modes, lambda_2) so RC-2's
    connectivity identity reads off the same decomposition."""
    lam, V = jacobi_eig(laplacian(w))
    order = sorted(range(N), key=lambda k: lam[k])
    n_zero = sum(1 for k in range(N) if abs(lam[k]) < 1e-10)
    lam2 = lam[order[1]]
    # L+ = sum_{lambda > tol} (1/lambda) v v^T
    Lp = [[sum(V[i][k] * V[j][k] / lam[k] for k in range(N)
               if abs(lam[k]) >= 1e-10) for j in range(N)]
          for i in range(N)]
    R = [[Lp[i][i] + Lp[j][j] - 2.0 * Lp[i][j] for j in range(N)]
         for i in range(N)]
    return R, n_zero, lam2


def battery(R):
    """(Q, monotone, status) under the pre-committed criterion."""
    offs = [R[i][j] for i in range(N) for j in range(N) if i != j]
    Q = max(offs) / min(offs)
    row = [R[0][j] for j in range(1, N)]
    mono = all(row[k + 1] > row[k] for k in range(len(row) - 1))
    if Q >= 12.0 and mono:
        status = "SURVIVES"
    elif Q < 2.0:
        status = "FAILS"
    else:
        status = "DEGRADED"
    return Q, mono, status


# ---------------- the run ------------------------------------------------
MEMBERS = [("anchor", None), ("alpha=4", 4.0), ("alpha=3", 3.0),
           ("alpha=2", 2.0), ("alpha=1.5", 1.5), ("alpha=1", 1.0),
           ("alpha=0.5", 0.5), ("deleted (alpha=0)", 0.0)]
MEAS = {}

print("=== RC: CONTROLS (halt-grade) ===")
K_anchor = stiffness(weights(None))
K_seal = build_K(N, 0.0)
dev = max(abs(K_anchor[i][j] - K_seal[i][j])
          for i in range(N) for j in range(N))
lmin_a, ks_a, _ = bath_kernel(K_anchor)
rel = abs(ks_a[-1] - K40_L01A) / K40_L01A
halt_check(dev < 1e-15 and rel < 1e-6,
           f"RC-1 the anchor reproduces L0-1a exactly: K(anchor) equals "
           f"build_K(24, 0) entrywise (max dev {dev:.1e} < 1e-15) and "
           f"k(40) = {ks_a[-1]:.6e} matches the recorded "
           f"6.8195e-9 (|rel Delta| = {rel:.1e} < 1e-6)")

rows = {}
rc2_ok = True
print("\n=== THE DELETION LATTICE (locality only; pin held) ===")
for name, alpha in MEMBERS:
    w = weights(alpha)
    K = stiffness(w)
    lmin, ks, k0 = bath_kernel(K)
    R, n_zero, lam2 = resistance(w)
    Q, mono, status = battery(R)
    breach = max(ks[i + 1] - ks[i] for i in range(len(ks) - 1))
    grade = fit_residuals(ks)
    rows[name] = {"alpha": alpha, "lambda_min_bath": lmin, "k0": k0,
                  "k40": ks[-1], "max_monotone_breach": breach,
                  "grade": grade, "laplacian_zero_modes": n_zero,
                  "laplacian_lambda2": lam2, "Q": Q,
                  "ordering_monotone": mono, "geometry": status,
                  "R_1_24": R[0][N - 1],
                  "R_min_offdiag": min(R[i][j] for i in range(N)
                                       for j in range(N) if i != j)}
    rc2_ok = rc2_ok and (abs(k0 - 1.0) < 1e-12
                         and lmin >= PIN - 1e-12
                         and n_zero == 1 and lam2 > 1e-10)
    print(f"   {name:18s}: lam_min={lmin:.6f}  k(40)={ks[-1]:.4e}  "
          f"Q={Q:9.3f}  mono={str(mono):5s}  -> {status}")
MEAS["members"] = rows

halt_check(rc2_ok,
           "RC-2 per-member identities: k(0) = 1 (|Delta| < 1e-12); "
           "lambda_min(bath) >= 0.3 - 1e-12 (the pin identity -- gap and "
           "passivity held by construction); L(w) has exactly one zero "
           "mode (< 1e-10) with lambda_2 > 1e-10 (connectivity)")

R_anc, _, _ = resistance(weights(None))
dev_anc = max(abs(R_anc[i][j] - abs(i - j))
              for i in range(N) for j in range(N))
R_del, _, _ = resistance(weights(0.0))
dev_del = max(abs(R_del[i][j] - 1.0)
              for i in range(N) for j in range(N) if i != j)
halt_check(dev_anc < 1e-9 and dev_del < 1e-9,
           f"RC-3 the end identities: anchor max|R_ij - |i-j|| = "
           f"{dev_anc:.1e} < 1e-9 (series law); deleted member "
           f"max|R_ij - 1| = {dev_del:.1e} < 1e-9 (complete-graph "
           f"symmetry, R = 2/(N*w) = 1)")

print("\n=== M: P_memory / P_positivity under the deletion "
      "(analytic-backed; a failure here is HALT -- identity-impossible "
      "with the pin held) ===")
m1 = all(r["k40"] < 1e-5 for r in rows.values())
check(m1, f"M-1 finite-memory-grade survival at EVERY member including "
          f"the full deletion: max k(40) = "
          f"{max(r['k40'] for r in rows.values()):.3e} < 1e-5 (the held "
          f"pin guarantees k(40) <= e^-12 = 6.1e-6)")
m2 = all(r["max_monotone_breach"] <= 1e-12 for r in rows.values())
check(m2, f"M-2 the kernel is monotone decreasing at every member: max "
          f"step increase "
          f"{max(r['max_monotone_breach'] for r in rows.values()):.2e} "
          f"<= 1e-12 (positivity survival by construction)")
if not (m1 and m2):
    HALT.append("M-gate breach at a pinned member: identity-impossible; "
                "instrument bug, never physics (charter Sec. 5)")
check(True, "M-diag (ungated): the grade comparator reads "
            + ", ".join(f"{n}: {r['grade']}" for n, r in rows.items())
            + " -- reported, adjudicating nothing", "diag")

print("\n=== G: P_geometry under the deletion ===")
g1 = (rows["anchor"]["geometry"] == "SURVIVES"
      and rows["deleted (alpha=0)"]["geometry"] == "FAILS")
check(g1, f"G-1 (identity-backed) the anchor SURVIVES (Q = "
          f"{rows['anchor']['Q']:.3f} >= 12, ordering monotone) and the "
          f"deleted member FAILS (Q = "
          f"{rows['deleted (alpha=0)']['Q']:.6f} < 2): removing locality "
          f"entirely destroys recoverable line geometry")
g2 = rows["alpha=4"]["geometry"] == "SURVIVES"
check(g2, f"G-2 H-SR, the attackable non-identity prediction: the "
          f"short-range class survives genuine nonlocality -- at "
          f"alpha = 4 (all pairs coupled) Q = {rows['alpha=4']['Q']:.3f} "
          f">= 12 and the ordering is monotone")
check(True, "G-map (ungated, the crossover map): "
            + "; ".join(f"{n}: Q={r['Q']:.3f}, {r['geometry']}"
                        for n, r in rows.items())
            + " -- the frozen pre-run note expected the boundary near "
            "alpha ~ 2; reported, adjudicating nothing", "diag")

# ---------------- the verdict lines (never composed) --------------------
gated = [c for c in CHECKS if c["kind"] in ("ok", "ctrl")]
n_ok = sum(1 for c in gated if c["pass"])
fails = [c["summary"] for c in gated if not c["pass"]]

if HALT:
    v_mem = v_pos = v_geo = split = "HALT"
else:
    v_mem = ("LOCALITY: NOT-LOAD-BEARING for P_memory" if m1
             else "L01B-PARTIAL (P_memory line)")
    v_pos = ("LOCALITY: NOT-LOAD-BEARING for P_positivity" if m2
             else "L01B-PARTIAL (P_positivity line)")
    if g1:
        v_geo = ("LOCALITY: NECESSITY-CERTIFIED for P_geometry (G-2 "
                 "H-SR: " + ("survived" if g2 else "FAILED") + ")")
    else:
        v_geo = "L01B-PARTIAL (P_geometry line)"
    split = ("CERTIFIED" if (m1 and m2 and g1 and g2)
             else "NOT CERTIFIED (a gate failed; see lines)")

out = {
    "fork": "L0-1b (D-LOC, the Level-0 sweep's second instrument)",
    "charter": "L0_1B_CHARTER_01.md (frozen 55dafe6)",
    "authority": "L0_1A_OWNER_RULING_01.md (D-LOC authorized; Outcomes "
                 "A and B named in advance)",
    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S+00:00", time.gmtime()),
    "environment": {"python": sys.version.split()[0], "pure_stdlib": True,
                    "deterministic": "no RNG"},
    "defect_history": [],
    "measurements": MEAS,
    "checks": CHECKS,
    "adjudication": {
        "verdict_memory": v_mem,
        "verdict_positivity": v_pos,
        "verdict_geometry": v_geo,
        "outcome_B_the_split": split,
        "outcome_A_note": "Outcome A (collapse) is identity-impossible "
                          "with the pin held; it is decidable only by a "
                          "future fork that deletes locality without the "
                          "pin (out of scope here, per charter Sec. 5)",
        "composition": "the per-property lines are NEVER composed into a "
                       "single label (frozen rule)",
        "scope": "within the declared background mathematics (real "
                 "symmetric matrices, exact eigendecomposition), the "
                 "tested weighted-network class w_ij = c_a*|i-j|^-a on "
                 "N = 24 with the coupling norm held at 23, the window "
                 "tau in [1, 40], and the Sec. 2 resistance-metric "
                 "criterion. No claim about 'the axioms of reality'. No "
                 "v4 channel moves; no red gate is touched",
    },
    "elapsed_s": round(time.time() - T0, 2),
}
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                    "L0_1B_RESULT.json")
blob = json.dumps(out, indent=1)
with open(path, "w") as fh:
    fh.write(blob)
sha = hashlib.sha256(blob.encode()).hexdigest()
print(f"\nartifact written: {os.path.abspath(path)} (sha {sha[:16]}...)")
print(f"\nL0-1b: {n_ok}/{len(gated)} gated checks passed; failures: "
      f"{len(fails)}; halts: {len(HALT)}")
if HALT:
    print("HALT: a control or identity breached -- instrument bug, "
          "never physics.")
    sys.exit(2)
print(f"VERDICT LINE 1: {v_mem}")
print(f"VERDICT LINE 2: {v_pos}")
print(f"VERDICT LINE 3: {v_geo}")
print(f"OUTCOME B (the split): {split}")
print("HARD STOP: verdicts recorded pending owner ruling.")
sys.exit(0 if not fails else 1)
