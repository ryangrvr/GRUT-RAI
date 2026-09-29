#!/usr/bin/env python3
"""l01e_appendix: the exact computational appendix of the D-DET theorem
document (obligation O-4; O-3's instantiation).

Frozen quantity list: L0_1E_THEOREM_01.md Sec. 6, committed at 550a237
BEFORE evaluation (owner ruling 5888965691: theorem document + exact
appendix, not a gated run; nothing unevaluated is presented as
prediction).

Part A: identity verifications -- halt-grade; a failure is a defect in
the theorem document, disclosed, never a finding.
Part B: evaluated quantities -- reported, not gated, not predictions.

Pure stdlib (fractions for the exact parts). No RNG. Single evaluation.
Run: python3 calc/l01e_appendix.py   (writes ../L0_1E_APPENDIX_RESULT.json)
"""

import hashlib
import json
import math
import os
import sys
import time
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c1_seam import build_K
from partition_selection_p1 import jacobi_eig

T0 = time.time()
N = 23
CHECKS, HALT, DEFECTS = [], [], []


def check(ok, msg, kind="ctrl"):
    CHECKS.append({"kind": kind, "pass": bool(ok), "summary": msg})
    print(("PASS " if ok else "FAIL ") + {"ctrl": "IDENTITY", "diag": "MAP"}[kind]
          + ": " + msg)
    if kind == "ctrl" and not ok:
        HALT.append(msg)


# ---- certified textual copy of the L0-1a comparator (A11) --------------
TAUS = [1.0 + 0.5 * i for i in range(79)]


def fit_residuals(ks):
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


def envelope(ks):
    out, run = [0.0] * len(ks), 0.0
    for i in range(len(ks) - 1, -1, -1):
        run = max(run, abs(ks[i]))
        out[i] = run
    return out


# ---------------- exact substrate ---------------------------------------
Mint = [[0] * N for _ in range(N)]
for i in range(N):
    Mint[i][i] = 23
Mint[N - 1][N - 1] = 13
for i in range(N - 1):
    Mint[i][i + 1] = Mint[i + 1][i] = -10
K = [[Fr(Mint[i][j], 10) for j in range(N)] for i in range(N)]
Kf = [[float(K[i][j]) for j in range(N)] for i in range(N)]
Kfull = build_K(24, 0.0)
Kb_seal = [row[1:] for row in Kfull[1:]]

# ---------------- profiles (frozen Sec. 6) -------------------------------
P = {}
P["F"] = [Fr(1)] * N
P["delta1"] = [Fr(1 if i == 0 else 0) for i in range(N)]
for R in (2, 10, 100, 1000):
    P[f"G({R})"] = [1 + Fr(R - 1) * i / 22 for i in range(N)]
P["G(inf)"] = [Fr(i, 22) for i in range(N)]
for R in (10, 1000):
    P[f"GR({R})"] = [1 + Fr(R - 1) * (22 - i) / 22 for i in range(N)]
P["GR(inf)"] = [Fr(22 - i, 22) for i in range(N)]
P["H(1000)"] = [Fr(1000 if i == 11 else 1) for i in range(N)]
P["H(inf)"] = [Fr(1 if i == 11 else 0) for i in range(N)]
for m in range(1, 23):
    P[f"S_{m}"] = [Fr(1 if i < m else 0) for i in range(N)]


# ---------------- exact helpers -----------------------------------------
IDX = {}
for i in range(N):
    for j in range(i, N):
        IDX[(i, j)] = len(IDX)
NU = len(IDX)


def key(a, b):
    return IDX[(a, b)] if a <= b else IDX[(b, a)]


ROWS = []
for i in range(N):
    for j in range(i, N):
        r = {}
        for m in range(N):
            if K[i][m]:
                r[key(m, j)] = r.get(key(m, j), 0) + K[i][m]
            if K[m][j]:
                r[key(i, m)] = r.get(key(i, m), 0) + K[m][j]
        ROWS.append(r)


def lyapunov(T):
    A = [[Fr(0)] * NU + [Fr(0)] for _ in range(NU)]
    k = 0
    for i in range(N):
        for j in range(i, N):
            for c, v in ROWS[k].items():
                A[k][c] = Fr(v)
            A[k][NU] = 2 * T[i] if i == j else Fr(0)
            k += 1
    for c in range(NU):
        p = next(r for r in range(c, NU) if A[r][c] != 0)
        A[c], A[p] = A[p], A[c]
        pv = A[c][c]
        rowc = A[c]
        nz = [j for j in range(c, NU + 1) if rowc[j] != 0]
        for r in range(c + 1, NU):
            f = A[r][c]
            if f != 0:
                f = f / pv
                Ar = A[r]
                for j in nz:
                    Ar[j] -= f * rowc[j]
    x = [Fr(0)] * NU
    for c in range(NU - 1, -1, -1):
        s = A[c][NU] - sum(A[c][j] * x[j] for j in range(c + 1, NU) if A[c][j] != 0)
        x[c] = s / A[c][c]
    return [[x[key(i, j)] for j in range(N)] for i in range(N)]


def matmul(A, B):
    return [[sum(A[i][m] * B[m][j] for m in range(N) if A[i][m] != 0)
             for j in range(N)] for i in range(N)]


def matvec(A, v):
    return [sum(A[i][j] * v[j] for j in range(N) if A[i][j] != 0) for i in range(N)]


def exact_rank(A):
    A = [row[:] for row in A]
    rows, cols, rank = len(A), len(A[0]), 0
    for c in range(cols):
        piv = next((r for r in range(rank, rows) if A[r][c] != 0), None)
        if piv is None:
            continue
        A[rank], A[piv] = A[piv], A[rank]
        for r in range(rank + 1, rows):
            if A[r][c] != 0:
                f = A[r][c] / A[rank][c]
                A[r] = [a - f * b for a, b in zip(A[r], A[rank])]
        rank += 1
        if rank == rows:
            break
    return rank


def sylvester(H):
    A = [row[:] for row in H]
    n = len(A)
    for k in range(n):
        p = A[k][k]
        if p <= 0:
            return False
        for r in range(k + 1, n):
            if A[r][k] != 0:
                f = A[r][k] / p
                A[r] = [a - f * b for a, b in zip(A[r], A[k])]
    return True


def inertia(H):
    A = [row[:] for row in H]
    n = len(A)
    pos = neg = 0
    for k in range(n):
        p = A[k][k]
        if p == 0:
            return None
        pos, neg = (pos + 1, neg) if p > 0 else (pos, neg + 1)
        for r in range(k + 1, n):
            if A[r][k] != 0:
                f = A[r][k] / p
                A[r] = [a - f * b for a, b in zip(A[r], A[k])]
    return [pos, neg]


# response moments s_n (K units), n = 0..46
S_MOM = []
v = [Fr(1 if i == 0 else 0) for i in range(N)]
for n in range(47):
    S_MOM.append(v[0])
    v = matvec(K, v)

# ---------------- T-1 closed form and T-2 weights (float) ---------------
LAM = [2.3 - 2 * math.cos((2 * k - 1) * math.pi / 47) for k in range(1, N + 1)]
VEC = []
for k in range(1, N + 1):
    col = [math.sin((2 * k - 1) * (i + 1) * math.pi / 47) for i in range(N)]
    nrm = math.sqrt(sum(c * c for c in col))
    VEC.append([c / nrm for c in col])
U1 = [VEC[k][0] for k in range(N)]


def resolvent_col1(lam):
    """z = (K + lam I)^{-1} e1 by the Thomas algorithm (float)."""
    a = [-1.0] * (N - 1)
    d = [Kf[i][i] + lam for i in range(N)]
    rhs = [1.0] + [0.0] * (N - 1)
    cp, dp = [0.0] * N, [0.0] * N
    cp[0], dp[0] = a[0] / d[0], rhs[0] / d[0]
    for i in range(1, N):
        den = d[i] - a[i - 1] * cp[i - 1]
        cp[i] = a[i] / den if i < N - 1 else 0.0
        dp[i] = (rhs[i] - a[i - 1] * dp[i - 1]) / den
    z = [0.0] * N
    z[N - 1] = dp[N - 1]
    for i in range(N - 2, -1, -1):
        z[i] = dp[i] - cp[i] * z[i + 1]
    return z


RES = [resolvent_col1(LAM[k]) for k in range(N)]


def weights(T):
    Tf = [float(t) for t in T]
    return [2 * U1[k] * sum(Tf[j] * VEC[k][j] * RES[k][j] for j in range(N))
            for k in range(N)]


# ======================= PART A (identity verifications) ================
print("=== PART A: identity verifications (halt-grade; failure = document defect) ===")
lam_j, V_j = jacobi_eig([row[:] for row in Kb_seal])
u2 = [V_j[0][k] ** 2 for k in range(N)]
k40 = sum(u2[k] * math.exp(-lam_j[k] * 40.0) for k in range(N))
seal_ok = all(Kb_seal[i][j] == Kf[i][j] for i in range(N) for j in range(N))
check(abs(k40 - 6.8195192260507686e-09) / 6.8195192260507686e-09 < 1e-9 and seal_ok,
      f"A1 sealed replication k(40) rel {abs(k40 - 6.8195192260507686e-09) / 6.8195192260507686e-09:.1e}; "
      f"build_K bath == float(M/10) entrywise: {seal_ok}")
dl = max(abs(a - b) for a, b in zip(sorted(lam_j), sorted(LAM)))
check(dl < 1e-12, f"A2 T-1 closed-form spectrum vs jacobi_eig: max |dlambda| = {dl:.1e}")

EX = {}
t_ly = time.time()
for name, T in P.items():
    Sig = lyapunov(T)
    KS = matmul(K, Sig)
    SK = matmul(Sig, K)
    resid_ok = all(KS[i][j] + SK[i][j] - (2 * T[i] if i == j else 0) == 0
                   for i in range(N) for j in range(N))
    sym_ok = all(Sig[i][j] == Sig[j][i] for i in range(N) for j in range(N))
    y = [Sig[i][0] for i in range(N)]
    mom, w = [], y[:]
    for n in range(48):
        mom.append(w[0])
        w = matvec(K, w)
    H24 = [[mom[i + j] for j in range(24)] for i in range(24)]
    d = exact_rank(H24)
    H0 = [[mom[i + j] for j in range(d)] for i in range(d)]
    H1 = [[mom[i + j + 1] for j in range(d)] for i in range(d)]
    cm = sylvester(H0)
    EX[name] = {"T": T, "Sig": Sig, "y": y, "mom": mom, "d": d, "CM": cm,
                "H1_PD": sylvester(H1) if cm else None,
                "inertia": inertia(H0), "resid_ok": resid_ok, "sym_ok": sym_ok,
                "commute": all(KS[i][j] == SK[i][j] for i in range(N) for j in range(N)),
                "KS": KS, "SK": SK}
print(f"   ({len(P)} exact Lyapunov solves + Hankel tests in {time.time() - t_ly:.1f}s)")

check(all(e["resid_ok"] and e["sym_ok"] for e in EX.values()),
      "A3 exact Lyapunov residual zero and Sigma symmetric at every profile")
a_, b_ = Fr(23, 10), Fr(1)
a4 = True
for e in EX.values():
    T, m = e["T"], e["mom"]
    a4 &= m[1] == T[0]
    a4 &= m[3] == (a_ ** 2 + 2 * b_ ** 2) * T[0] - b_ ** 2 * T[1]
    a4 &= m[5] == ((a_ ** 4 + 8 * a_ ** 2 * b_ ** 2 + 5 * b_ ** 4) * T[0]
                   - (2 * a_ ** 2 * b_ ** 2 + 4 * b_ ** 4) * T[1] + b_ ** 4 * T[2])
check(a4, "A4 T-7 odd-moment hierarchy: m1 = T1, m3 and m5 closed forms, exact at every profile")
F = EX["F"]
ks_I = all(F["KS"][i][j] == (1 if i == j else 0) for i in range(N) for j in range(N))
fdt = all(F["mom"][n] == S_MOM[n - 1] for n in range(1, 48))
check(ks_I and fdt and F["CM"] and F["d"] == 23,
      f"A5 T-4 (O-3 instantiation): K Sigma = I at F ({ks_I}); m_n = s_(n-1), n=1..47 ({fdt}); "
      f"exact CM with d_c = {F['d']}")
nonuni = [n for n in EX if n != "F"]
check(all(not EX[n]["commute"] for n in nonuni),
      "A6 T-11 K Sigma != Sigma K exactly at every nonuniform profile")
check(all(all(v > 0 for v in e["y"]) for e in EX.values()),
      "A7 T-5 y > 0 entrywise, exact, at every profile")
check(not EX["G(inf)"]["CM"] and not EX["H(inf)"]["CM"] and not EX["G(1000)"]["CM"]
      and EX["F"]["CM"] and EX["delta1"]["CM"],
      "A8 T-8/T-9: G(inf), H(inf), G(1000) fail exact CM; F and delta1 pass")
WF = {n: weights(e["T"]) for n, e in EX.items()}
k1 = LAM.index(min(LAM))
check(all(WF[n][k1] > 0 for n in WF), "A9 T-9 Perron: float w_1 > 0 at every profile")

# A10 cone consistency along each ray (halt on monotonicity; float disagreement -> defect)
RAYS = {"ramp": ["F", "G(2)", "G(10)", "G(100)", "G(1000)", "G(inf)"],
        "reversed": ["F", "GR(10)", "GR(1000)", "GR(inf)"],
        "hotspot": ["F", "H(1000)", "H(inf)"]}
SHAPE = {"ramp": "G(inf)", "reversed": "GR(inf)", "hotspot": "H(inf)"}
RVAL = {"F": 1, "G(2)": 2, "G(10)": 10, "G(100)": 100, "G(1000)": 1000,
        "GR(10)": 10, "GR(1000)": 1000, "H(1000)": 1000}
wU = WF["F"]
RSTAR = {}
mono_ok = True
for ray, members in RAYS.items():
    st = [EX[n]["CM"] for n in members]
    seen_false = False
    for s in st:
        if not s:
            seen_false = True
        elif seen_false:
            mono_ok = False
    if EX[SHAPE[ray]]["CM"] and not all(st):
        mono_ok = False
    wS = WF[SHAPE[ray]]
    neg = [wU[k] / abs(wS[k]) for k in range(N) if wS[k] < 0]
    RSTAR[ray] = 1 + min(neg) if neg else float("inf")
    for n in members[:-1]:
        pred = RVAL[n] <= RSTAR[ray]
        if pred != EX[n]["CM"]:
            DEFECTS.append(f"float R* ({RSTAR[ray]:.6g}) disagrees with exact status at {n}; exact prevails")
check(mono_ok, "A10 T-6 cone consistency: exact CM statuses monotone along every ray; "
               "a passing limit shape implies every member passes")

E_anchor = envelope([sum(u2[k] * math.exp(-lam_j[k] * t) for k in range(N)) for t in TAUS])
k_anchor = [sum(u2[k] * math.exp(-lam_j[k] * t) for k in range(N)) for t in TAUS]
re_c, ra_c, gr_c, _, _ = fit_residuals(E_anchor)
check(E_anchor == k_anchor and abs(re_c - 1.9809889100368165) < 1e-12
      and abs(ra_c - 4.7907669413552245) < 1e-12 and gr_c == "EXPONENTIAL-GRADE",
      f"A11 comparator certification: R_exp |D| {abs(re_c - 1.9809889100368165):.1e}, "
      f"R_alg |D| {abs(ra_c - 4.7907669413552245):.1e}, {gr_c}")

# ======================= PART B (evaluated; not gated) ===================
print("\n=== PART B: evaluated quantities (reported, not gated, not predictions) ===")
B = {}
for name, e in EX.items():
    T, m = e["T"], e["mom"]
    w = WF[name]
    tot = sum(w)
    c = [sum(w[k] * math.exp(-LAM[k] * t) for k in range(N)) / tot for t in TAUS]
    E = envelope(c)
    r_e, r_a, gr, _, _ = fit_residuals(E) if min(c) > 0 else (None, None, "UNDEFINED", 0, 0)
    G = [[c[2 + i + j] for j in range(39)] for i in range(39)]
    gmin = min(jacobi_eig(G)[0])
    mono = max(c[i + 1] - c[i] for i in range(78))
    ratios = ({n: float(m[n] / (T[0] * S_MOM[n - 1])) for n in range(2, 6)}
              if T[0] > 0 else None)
    KS, SK = e["KS"], e["SK"]
    num = math.sqrt(sum(float(KS[i][j] - SK[i][j]) ** 2 for i in range(N) for j in range(N)))
    den = math.sqrt(sum(float(KS[i][j]) ** 2 for i in range(N) for j in range(N)))
    B[name] = {"exact_CM": e["CM"], "d_c": e["d"], "H0_inertia": e["inertia"],
               "m3_sign": (m[3] > 0) - (m[3] < 0), "m5_sign": (m[5] > 0) - (m[5] < 0),
               "float_negative_weight_modes": [k + 1 for k in range(N) if w[k] < 0],
               "memory_grade": gr, "R_exp": r_e, "R_alg": r_a, "E40": E[-1],
               "monotone_max_step": mono, "gram_min_eig": gmin,
               "fdt_ratios_n2_5": ratios, "commutator_ratio": num / den}
    print(f"   {name:8s}: CM={str(e['CM']):5s} d_c={e['d']:2d} inertia={e['inertia']}  "
          f"m3{'+' if m[3] > 0 else '-'} m5{'+' if m[5] > 0 else '-'}  "
          f"mem={gr[:3]}  (b)max_step={mono:+.1e}  gram={gmin:+.1e}")
# B2 ramp-line lower exit
wS = WF["G(inf)"]
posk = [1 - wU[k] / wS[k] for k in range(N) if wS[k] > 0]
Rminus = max(posk) if posk else float("-inf")
B2 = {"R_star": RSTAR, "ramp_lower_exit_R_minus": Rminus,
      "consistency_Rminus_le_0_iff_GRinf_CM": (Rminus <= 0) == EX["GR(inf)"]["CM"]}
if not B2["consistency_Rminus_le_0_iff_GRinf_CM"]:
    DEFECTS.append("float R_minus disagrees with exact GR(inf) status; exact prevails")
print(f"\n   B2 thresholds (float): R* = {RSTAR}; ramp lower exit R- = {Rminus:.6g}; "
      f"consistent with exact GR(inf): {B2['consistency_Rminus_le_0_iff_GRinf_CM']}")
steps = {f"S_{m}": EX[f"S_{m}"]["CM"] for m in range(1, 23)}
print(f"   B1 step profiles S_m exact CM: {[m for m in range(1, 23) if steps[f'S_{m}']]} pass; "
      f"{[m for m in range(1, 23) if not steps[f'S_{m}']]} fail")

out = {
    "document": "L0_1E_THEOREM_01.md Sec. 6 (frozen 550a237)",
    "authority": "owner ruling 5888965691 (theorem document + exact appendix)",
    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S+00:00", time.gmtime()),
    "environment": {"python": sys.version.split()[0], "pure_stdlib": True,
                    "deterministic": "no RNG"},
    "defect_history": DEFECTS,
    "part_A": CHECKS,
    "part_B": B,
    "B2": B2,
    "step_profiles_CM": steps,
    "elapsed_s": round(time.time() - T0, 2),
}
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                    "L0_1E_APPENDIX_RESULT.json")
blob = json.dumps(out, indent=1, default=str)
with open(path, "w") as fh:
    fh.write(blob)
sha = hashlib.sha256(blob.encode()).hexdigest()
nA = sum(1 for c in CHECKS if c["kind"] == "ctrl")
print(f"\nartifact written: {os.path.abspath(path)} (sha {sha[:16]}...)")
print(f"Part A: {nA - len(HALT)}/{nA} identity verifications passed; defects: {len(DEFECTS)}")
if HALT:
    print("HALT (document defect): " + "; ".join(HALT))
    sys.exit(2)
print("HARD STOP: appendix recorded pending owner assignment of O-4's terminal label.")
