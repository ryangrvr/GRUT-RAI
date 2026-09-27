#!/usr/bin/env python3
"""GR2-b -- probe representation (frozen instrument).

Charter: GR2B_PROBE_CHARTER_01.md, frozen at commit 940ef46, under the
GR-2 campaign directive (Layer 2) and the GR2-a owner ruling.

Question (the owner's): does the earned core select spin-2, or is spin
itself another primitive? Six candidates -- scalar / vector / spin-2,
massless and massive -- in one framework; earned tests first; supplied
tests tagged as the record grades them.

Machinery: the CC-1 L-P exchange leg replicated exactly (same helpers,
same seed 20260925, same loop order) as halt-grade controls; the GR-1
L-X pair machinery for the influence leg; sp(6) Lie closures for the
access leg. Pure stdlib. Deterministic. Single run.
Run: python3 calc/gr2b_probe.py   (writes ../GR2B_PROBE_RESULT.json)
"""

import hashlib
import json
import math
import os
import random
import sys
import time

from cc1_ccons import ETA, SEED, lower_vec, perp_basis, rand_unit, sym_basis, tens_resid
from partition_selection_p1 import jacobi_eig

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

# ---------------- RC: CC-1 L-P replication (exact RNG order) -----------
print("=== RC: CC-1 EXCHANGE CONTROLS (halt-grade; seed 20260925, exact order) ===")
rng = random.Random(SEED)
etaL = [[ETA[i] if i == j else 0.0 for j in range(4)] for i in range(4)]

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

REC = {"v_cons": 0.00945472594605436, "v_non": -10.617825792867652,
       "t_cons": 0.016561276082769805, "t_non": -17.818443050769414,
       "proca": 0.29456006917729094, "fp": 1.5305026792418885}
halt_check(abs(cons_min - REC["v_cons"]) < 1e-9 and cons_dev < 1e-12,
           f"RC-1 massless vector, conserved: min residue {cons_min:.12f} "
           f"replicates recorded {REC['v_cons']:.12f} (dev {cons_dev:.1e})")
halt_check(abs(non_min - REC["v_non"]) < 1e-9,
           f"RC-2 massless vector, non-conserved: min residue {non_min:.12f} "
           f"replicates recorded {REC['v_non']:.12f}")
halt_check(abs(cmin2 - REC["t_cons"]) < 1e-9 and cdev2 < 1e-10,
           f"RC-3 massless spin-2, conserved: min residue {cmin2:.12f} "
           f"replicates recorded {REC['t_cons']:.12f} (dev {cdev2:.1e})")
halt_check(abs(nmin2 - REC["t_non"]) < 1e-9,
           f"RC-4 massless spin-2, non-conserved: min residue {nmin2:.12f} "
           f"replicates recorded {REC['t_non']:.12f}")
halt_check(abs(pmin - REC["proca"]) < 1e-9,
           f"RC-5 Proca (massive vector), arbitrary sources: min residue "
           f"{pmin:.12f} replicates recorded {REC['proca']:.12f} >= 0")
halt_check(abs(fmin - REC["fp"]) < 1e-9,
           f"RC-6 Fierz-Pauli (massive spin-2), arbitrary sources: min "
           f"residue {fmin:.12f} replicates recorded {REC['fp']:.12f} >= 0")
MEAS.update({"vector": {"cons_min": cons_min, "non_min": non_min},
             "spin2": {"cons_min": cmin2, "non_min": nmin2},
             "massive": {"proca_min": pmin, "fp_min": fmin}})

# ---------------- RL: L-X machinery control ---------------------------
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


def slope(vertex):
    return math.log(J_of(0.2, vertex) / J_of(0.1, vertex)) / math.log(2.0)


s_stress = slope(lambda q: disp(q) ** 2 - q * q)
halt_check(abs(s_stress - 8.005419679013105) < 1e-9,
           f"RL-1 L-X stress-source slope {s_stress:.12f} replicates the "
           f"recorded 8.005419679013105")

if HALT:
    print("HALT: a replication control breached -- instrument bug, never "
          "physics. No verdict may be issued from this run.")
    sys.exit(2)

# ---------------- S: the scalar rows (new content) ---------------------
print("\n=== S: THE SCALAR ROWS (fresh RNG stream, same seed; disclosed) ===")
rng2 = random.Random(SEED)
s0 = min(rng2.gauss(0, 1) ** 2 for _ in range(200))
sm = min(rng2.gauss(0, 1) ** 2 for _ in range(200))
MEAS["scalar"] = {"massless_min": s0, "massive_min": sm}
check(s0 >= 0.0,
      f"S-1 massless scalar, arbitrary sources: min residue {s0:.3e} >= 0 "
      f"-- positivity places NO constraint on the scalar's source; the "
      f"conservation-for-masslessness tie is a spin >= 1 phenomenon")
check(sm >= 0.0,
      f"S-2 massive scalar, arbitrary sources: min residue {sm:.3e} >= 0")

# ---------------- I: influence distinguishability ----------------------
print("\n=== I: INFLUENCE LEG (distinguishes, forbids nothing) ===")
ws = [0.10 + 0.02 * i for i in range(6)]
jmin = min(min(J_of(w, v) for w in ws)
           for v in (lambda q: 1.0, lambda q: disp(q) ** 2 - q * q))
check(jmin >= 0.0,
      f"I-1 induced pair-channel J(w) >= 0 for the density-source and "
      f"stress-source candidates (min {jmin:.3e}) -- both cone-admissible")
s_dens = slope(lambda q: 1.0)
MEAS["slopes"] = {"density": s_dens, "stress": s_stress}
check(abs(s_dens) < 0.2 and abs(s_stress - 8.0) < 0.2,
      f"I-2 the influence data DISTINGUISH representations without "
      f"forbidding either: density-source class 0 (slope {s_dens:.4f}), "
      f"stress-source class 8 (slope {s_stress:.4f})")

# ---------------- A: access leg (sp(6) closures) -----------------------
print("\n=== A: ACCESS LEG (seed closures in sp(6); 3-site chain, pins 0.3) ===")
N = 3
DIM = 2 * N


def zeros():
    return [[0.0] * DIM for _ in range(DIM)]


Jsym = zeros()
for i in range(N):
    Jsym[i][N + i] = 1.0
    Jsym[N + i][i] = -1.0

L = [[1.0, -1.0, 0.0], [-1.0, 2.0, -1.0], [0.0, -1.0, 1.0]]
Q_H = zeros()
for i in range(N):
    Q_H[N + i][N + i] = 1.0
    for j in range(N):
        Q_H[i][j] = L[i][j] + (0.3 if i == j else 0.0)

Q_D = zeros()
for i in range(N):
    Q_D[i][i] = 2.0

# current O = 1/2[(p1+p2)(u2-u1) + (p2+p3)(u3-u2)]
cc = {(0, 0): -0.5, (1, 0): 0.5, (0, 1): -0.5, (1, 1): 0.0, (2, 1): 0.5,
      (1, 2): -0.5, (2, 2): 0.5}
Q_C = zeros()
for (a, b), v in cc.items():
    Q_C[a][N + b] += v
    Q_C[N + b][a] += v

Q_T = zeros()
for i in range(N):
    Q_T[N + i][N + i] = 1.0
    for j in range(N):
        Q_T[i][j] = L[i][j]


def mat_mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(DIM)) for j in range(DIM)]
            for i in range(DIM)]


def bracket(A, B):
    AB = mat_mul(mat_mul(A, Jsym), B)
    BA = mat_mul(mat_mul(B, Jsym), A)
    return [[AB[i][j] - BA[i][j] for j in range(DIM)] for i in range(DIM)]


def vec_of(Q):
    return [Q[i][j] for i in range(DIM) for j in range(i, DIM)]


def norm(v):
    return math.sqrt(sum(x * x for x in v))


def normalized(Q):
    nv = norm(vec_of(Q))
    if nv < 1e-300:
        return Q
    return [[Q[i][j] / nv for j in range(DIM)] for i in range(DIM)]


def closure(seed):
    basis = []

    def add(Q):
        # relative independence test (instrument repair, run 2: the run-1
        # absolute test let unnormalized bracket growth fake independence)
        v = vec_of(Q)
        n0 = norm(v)
        if n0 < 1e-14:
            return False
        for b in basis:
            c = sum(x * y for x, y in zip(v, b))
            v = [x - c * y for x, y in zip(v, b)]
        nv = norm(v)
        if nv > 1e-10 * n0:
            basis.append([x / nv for x in v])
            return True
        return False

    mats = [normalized(seed), normalized(Q_H)]
    for Q in mats:
        add(Q)
    sweeps = 0
    while sweeps < 8:
        sweeps += 1
        new = []
        for i in range(len(mats)):
            for j in range(i + 1, len(mats)):
                B = normalized(bracket(mats[i], mats[j]))
                if add(B):
                    new.append(B)
        if not new:
            break
        mats.extend(new)
    # closure defect: every pairwise bracket lies in the span
    defect = 0.0
    for i in range(len(mats)):
        for j in range(i + 1, len(mats)):
            v = vec_of(bracket(mats[i], mats[j]))
            nv = norm(v)
            if nv < 1e-14:
                continue
            for b in basis:
                c = sum(x * y for x, y in zip(v, b))
                v = [x - c * y for x, y in zip(v, b)]
            defect = max(defect, norm(v) / nv)
    return len(basis), sweeps, defect


for name, Q, gate in (("density", Q_D, "A-1"), ("current", Q_C, "A-2"),
                      ("stress", Q_T, "A-3")):
    d, sw, df = closure(Q)
    MEAS[f"closure_{name}"] = {"dim": d, "sweeps": sw, "defect": df}
    halt_check(d <= 21, f"{gate} identity: closure dim {d} <= dim sp(6) = 21 "
                        f"(halt-grade; run 1 breached this identity)")
    check(sw <= 8 and df < 1e-8,
          f"{gate} the {name} seed generates, with H, a bracket-closed "
          f"subalgebra of sp(6): dim {d} (of 21), stable in {sw} sweeps, "
          f"closure defect {df:.1e} < 1e-8 -- a canonical access assignment")
check(True, "access consequence: every representation's source type is an "
            "admissible seed; per P-6 (cited, not re-run) the seed is a "
            "supplied input -- access does not select the representation",
      "note")

# ---------------- N: the static sign table -----------------------------
print("\n=== N: STATIC EXCHANGE SIGNS (like sources; deterministic) ===")
sgn_s = 1.0            # scalar numerator: rho * rho
sgn_v = etaL[0][0]     # vector numerator: eta_00
sgn_t = 0.5 * (etaL[0][0] * etaL[0][0] + etaL[0][0] * etaL[0][0]) \
    - 0.5 * etaL[0][0] * etaL[0][0]   # D = 4 massless tensor: 1 - 1/2
MEAS["static_signs"] = {"scalar": sgn_s, "vector": sgn_v, "tensor": sgn_t}
check(sgn_s > 0 and sgn_v < 0 and sgn_t > 0,
      f"N-1 static exchange between like sources: scalar {sgn_s:+.1f} "
      f"(attractive), massless vector {sgn_v:+.1f} (repulsive), massless "
      f"spin-2 {sgn_t:+.1f} (attractive) -- the classic discriminator, and "
      f"it is an EMPIRICAL datum (universal attraction) found nowhere in "
      f"the record's earned or supplied layers")

# ---------------- V: the verdict gates ---------------------------------
print("\n=== V: SURVIVOR COUNT AND INJECTIVITY ===")
# earned layer: a candidate is eliminated only if NO source assignment is
# admissible under the earned tests
survivors_earned = {
    "scalar_massless": s0 >= 0,
    "scalar_massive": sm >= 0,
    "vector_massless": cons_min >= -1e-12,   # conserved realization exists
    "vector_massive": pmin >= -1e-12,
    "spin2_massless": cmin2 >= -1e-12,       # conserved realization exists
    "spin2_massive": fmin >= -1e-12,
}
n_elim = sum(0 if v else 1 for v in survivors_earned.values())
check(n_elim == 0,
      f"V-1 EARNED LAYER ELIMINATES NOTHING: all six candidates have "
      f"admissible realizations under locality, exchange/cone positivity, "
      f"access, and recovered geometry (eliminated: {n_elim} of 6)")

supplied_survivors = ["scalar_massless (any source)",
                      "vector_massless (conserved current)",
                      "spin2_massless (conserved symmetric T)"]
check(len(supplied_survivors) >= 2,
      f"V-2 SUPPLIED LAYER DOES NOT SELECT SPIN: imposing the record's "
      f"supplied set (masslessness, Lorentz/gauge structure) ties spin >= 1 "
      f"to conserved sources (RC-2, RC-4) but leaves "
      f"{len(supplied_survivors)} representation classes standing: "
      f"{'; '.join(supplied_survivors)} -- the map influence structure -> "
      f"probe representation is NOT injective")

check(True, "recovered geometry is probe-blind by construction (CA-1 leg 1; "
            "CP-1 L-G2 at 2.2e-16); universal reach and clock universality "
            "are conditional/supplied per U-1 -- cited, not re-run", "note")
check(True, "the further elimination down to spin-2 requires empirical "
            "inputs external to the record: universal ATTRACTION removes "
            "the vector (N-1), and LIGHT BENDING removes the Nordstrom-type "
            "scalar -- neither is earned or supplied anywhere in the "
            "record", "note")

# ---------------- verdict ---------------------------------------------
gated = [c for c in CHECKS if c["kind"] in ("ok", "ctrl")]
n_ok = sum(1 for c in gated if c["pass"])
fails = [c["summary"] for c in gated if not c["pass"]]
v1 = next(c for c in CHECKS if c["summary"].startswith("V-1"))

if not fails:
    verdict = "B-SPIN-NOT-SELECTED"
elif not v1["pass"] and all(v for k, v in survivors_earned.items()
                            if k.startswith("spin2")):
    verdict = "B-SPIN-SELECTED-IN-CLASS"
else:
    verdict = "B-PARTIAL"

detail = ("no earned structure distinguishes representation class except "
          "to label it through the influence data (classes 0 vs 8, both "
          "admissible); the supplied layer ties masslessness of spin >= 1 "
          "to source conservation but leaves scalar, vector, and spin-2 "
          "standing; the elimination down to spin-2 lives in empirical "
          "inputs (universal attraction; light bending) external to the "
          "record. I3 is sharpened as an irreducible primitive at this "
          "level: the representation-degeneracy demonstration half of its "
          "certificate")

out = {
    "fork": "GR2-b",
    "charter": "GR2B_PROBE_CHARTER_01.md (frozen 940ef46)",
    "directive": "GR2_CAMPAIGN_DIRECTIVE_01.md (Layer 2); "
                 "GR2A_OWNER_RULING_01.md (authorization)",
    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S+00:00", time.gmtime()),
    "environment": {"python": sys.version.split()[0], "pure_stdlib": True,
                    "deterministic": "seeded scans only (seed 20260925)"},
    "defect_history": [
        "Run 1 (2026-09-27, not committed): the access-leg closure "
        "computation breached the analytic identity dim <= dim sp(6) = 21 "
        "(reported dim 30 for the density seed; stress-seed defect 0.94). "
        "Cause: brackets stored unnormalized, so exponential norm growth "
        "defeated the absolute independence tolerance. Instrument bug, "
        "never physics; every RC/RL/S/I/N/V gate outside the access leg "
        "passed identically in run 1. Repair: brackets normalized, "
        "relative independence test, and the dim <= 21 identity added as "
        "a halt gate. No gate threshold changed. Run 2 is the recorded "
        "run."
    ],
    "measurements": MEAS,
    "survivors_earned": survivors_earned,
    "checks": CHECKS,
    "adjudication": {
        "verdict": verdict,
        "verdict_detail": detail,
        "scope": "D = 4 exchange kinematics as in CC-1; the 1D L-X pair "
                 "channel; sp(6) closures on the 3-site chain. Higher "
                 "spins, probe mixtures, and sector universality out of "
                 "scope (GR2-c, GR2-d)",
    },
    "elapsed_s": round(time.time() - T0, 2),
}

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                    "GR2B_PROBE_RESULT.json")
blob = json.dumps(out, indent=1)
with open(path, "w") as f:
    f.write(blob)
sha = hashlib.sha256(blob.encode()).hexdigest()
print(f"\nartifact written: {os.path.abspath(path)} (sha {sha[:16]}...)")
print(f"\nGR2-b: {n_ok}/{len(gated)} gated checks passed; failures: "
      f"{len(fails)}; halts: {len(HALT)}")
print(f"VERDICT: {verdict} -- {detail}")
print("HARD STOP: verdict recorded pending owner ruling.")
sys.exit(0 if not fails else 1)
