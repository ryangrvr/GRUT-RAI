#!/usr/bin/env python3
"""l01d_cycle_affinity: the first floor instrument (D-HERM-a, obligation O-1).

Charter: L0_1D_CHARTER_01.md, FROZEN at commit 3a8ae1b after an
analytic-only pre-freeze review (L0_1D_PREFREEZE_REVIEW_01.md; nothing
previewed, nothing quarantined). Authority: registry rulings R-1..R-4
(R-3 at declared linear-class scope) under the adopted floor
termination condition. The owner's four prohibitions bind.

The frozen question: when the generator stops being self-adjoint, is it
asymmetry itself, or cycle affinity (broken detailed balance), that
bears on the tested response properties?

Instrument E (exact, static): integer matrices M = 10K built from
integers (never from floats); moments s_n = e1^T M^n e1; the atom count
d = rank of the 24x24 moment Hankel; exact CM test H0 (size d) > 0 by
Sylvester pivots; mechanism map (recurrence polynomial of degree d,
squarefreeness, Sturm real-root count, H0 inertia).

Instrument B (time-domain): RK4 of xdot = -K x from e1, L0-1c's
integer-count schedule verbatim; P_memory by the R-1 envelope
comparator.

Float K construction: the sealed base (build_K bath block, plus the
closing spring by float addition) is checked entry by entry against
float(M/10) (RC-9); every member's float K is float(M/10), because
float arithmetic such as -1 + 0.9 does not produce -0.1.

Pure stdlib. Deterministic (no RNG). Single run.
Run: python3 calc/l01d_cycle_affinity.py   (writes ../L0_1D_RESULT.json)
"""

import hashlib
import json
import math
import os
import sys
import time
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c1_seam import build_K
from partition_selection_p1 import jacobi_eig

T0 = time.time()
CHECKS = []
HALT = []
DEFECTS = []
N = 23


def check(ok, msg, kind="ok"):
    CHECKS.append({"kind": kind, "pass": bool(ok), "summary": msg})
    tag = {"ok": "GATE", "ctrl": "CONTROL", "note": "NOTE", "diag": "DIAG"}[kind]
    print(("PASS " if ok else "FAIL ") + tag + ": " + msg)


def halt_check(ok, msg):
    check(ok, msg, "ctrl")
    if not ok:
        HALT.append(msg)


# ---- the certified textual copy of the L0-1a comparator (RC-7) ---------
TAUS = [1.0 + 0.5 * i for i in range(79)]   # 1.0 .. 40.0 step 0.5


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


def envelope(ks):
    """R-1: E(tau_i) = max_{j >= i} |k(tau_j)| over the recorded grid."""
    out = [0.0] * len(ks)
    run = 0.0
    for i in range(len(ks) - 1, -1, -1):
        run = max(run, abs(ks[i]))
        out[i] = run
    return out


EARLY = [0.05 * j for j in range(1, 20)]
K40_SEAL = 6.8195192260507686e-09
R_EXP_SEAL = 1.9809889100368165
R_ALG_SEAL = 4.7907669413552245

# ---------------- exact integer construction (M = 10K) ------------------
G = {"0": Fraction(0), "0.1": Fraction(1, 10), "0.3": Fraction(3, 10),
     "0.6": Fraction(3, 5), "0.9": Fraction(9, 10)}


def M_tree_base():
    M = [[0] * N for _ in range(N)]
    for i in range(N):
        M[i][i] = 23
    M[N - 1][N - 1] = 13
    for i in range(N - 1):
        M[i][i + 1] = M[i + 1][i] = -10
    return M


def M_ring_base():
    M = M_tree_base()
    M[0][0] += 10
    M[N - 1][N - 1] += 10
    M[0][N - 1] = M[N - 1][0] = -10
    return M


def ring_edges():
    return [(i, i + 1) for i in range(N - 1)] + [(N - 1, 0)]


def deform(M, edges, pattern, gamma):
    """K_{p,q} = -(1 - g a), K_{q,p} = -(1 + g a): transport p -> q at
    rate 1 + g a. In M = 10K units, integers exactly."""
    M = [row[:] for row in M]
    for (p, q), a in zip(edges, pattern):
        t = gamma * 10 * a
        assert t.denominator == 1
        t = int(t)
        M[p][q] = -10 + t
        M[q][p] = -10 - t
    return M


PATH = [(i, i + 1) for i in range(N - 1)]
BAL = [1] * 11 + [-1] * 11 + [0]
MEMBERS = {}
MEMBERS["T(0)"] = ("zero-affinity", M_tree_base(), "0")
MEMBERS["T(0.9)"] = ("zero-affinity",
                     deform(M_tree_base(), PATH, [1] * 22, G["0.9"]), "0.9")
for g in ("0", "0.1", "0.3", "0.6", "0.9"):
    MEMBERS[f"C({g})"] = ("zero-affinity" if g == "0" else "adjudicating",
                          deform(M_ring_base(), ring_edges(), [1] * 23, G[g]),
                          g)
for g in ("0.3", "0.9"):
    MEMBERS[f"B({g})"] = ("zero-affinity",
                          deform(M_ring_base(), ring_edges(), BAL, G[g]), g)


def affinity(name):
    g = float(G[MEMBERS[name][2]])
    if name.startswith("C("):
        return 23 * math.log((1 + g) / (1 - g)) if g > 0 else 0.0
    return 0.0


def to_float(M):
    return [[float(Fraction(m, 10)) for m in row] for row in M]


# ---------------- float linear algebra helpers --------------------------
def sym_part(K):
    return [[0.5 * (K[i][j] + K[j][i]) for j in range(N)] for i in range(N)]


def eig_kernel(S, taus):
    lam, V = jacobi_eig([row[:] for row in S])
    u2 = [V[0][k] ** 2 for k in range(len(lam))]
    return [sum(u2[k] * math.exp(-lam[k] * t) for k in range(len(lam)))
            for t in taus], sum(u2)


def rk4_linear(K, n1, h1, n2, h2, rec1, rec2):
    rows = [[(j, -K[i][j]) for j in range(N) if K[i][j] != 0.0]
            for i in range(N)]

    def f(x):
        return [sum(c * x[j] for j, c in r) for r in rows]

    x = [0.0] * N
    x[0] = 1.0
    early, gated = [], []
    for s in range(1, n1 + 1):
        k1 = f(x)
        k2 = f([a + 0.5 * h1 * b for a, b in zip(x, k1)])
        k3 = f([a + 0.5 * h1 * b for a, b in zip(x, k2)])
        k4 = f([a + h1 * b for a, b in zip(x, k3)])
        x = [a + h1 / 6.0 * (p + 2 * q + 2 * r + w)
             for a, p, q, r, w in zip(x, k1, k2, k3, k4)]
        if s % rec1 == 0 and s < n1:
            early.append(x[0])
    gated.append(x[0])
    for s in range(1, n2 + 1):
        k1 = f(x)
        k2 = f([a + 0.5 * h2 * b for a, b in zip(x, k1)])
        k3 = f([a + 0.5 * h2 * b for a, b in zip(x, k2)])
        k4 = f([a + h2 * b for a, b in zip(x, k3)])
        x = [a + h2 / 6.0 * (p + 2 * q + 2 * r + w)
             for a, p, q, r, w in zip(x, k1, k2, k3, k4)]
        if s % rec2 == 0:
            gated.append(x[0])
    return early, gated


# ---------------- exact arithmetic helpers ------------------------------
def moments(M, nmax):
    v = [0] * N
    v[0] = 1
    s = [1]
    for _ in range(nmax):
        v = [sum(M[i][j] * v[j] for j in range(N) if M[i][j]) for i in range(N)]
        s.append(v[0])
    return s


def krylov_rank(M):
    vs = []
    v = [0] * N
    v[0] = 1
    for _ in range(N + 1):
        vs.append(v[:])
        v = [sum(M[i][j] * v[j] for j in range(N) if M[i][j]) for i in range(N)]
    return exact_rank([[Fraction(vs[c][r]) for c in range(len(vs))]
                       for r in range(N)])


def exact_rank(A):
    A = [row[:] for row in A]
    rows, cols = len(A), len(A[0])
    rank = 0
    for c in range(cols):
        piv = None
        for r in range(rank, rows):
            if A[r][c] != 0:
                piv = r
                break
        if piv is None:
            continue
        A[rank], A[piv] = A[piv], A[rank]
        for r in range(rank + 1, rows):
            if A[r][c] != 0:
                fct = A[r][c] / A[rank][c]
                A[r] = [a - fct * b for a, b in zip(A[r], A[rank])]
        rank += 1
        if rank == rows:
            break
    return rank


def sylvester_pd(H):
    """Exact elimination without pivoting; stop at first pivot <= 0.
    Returns (is_pd, pivot_signs_or_None, index_of_first_nonpositive)."""
    A = [[Fraction(x) for x in row] for row in H]
    n = len(A)
    signs = []
    for k in range(n):
        p = A[k][k]
        if p <= 0:
            return False, None, k
        signs.append(1)
        for r in range(k + 1, n):
            if A[r][k] != 0:
                fct = A[r][k] / p
                A[r] = [a - fct * b for a, b in zip(A[r], A[k])]
    return True, signs, None


def inertia(H):
    """Pivot signs without pivoting (map only); None if a zero pivot."""
    A = [[Fraction(x) for x in row] for row in H]
    n = len(A)
    pos = neg = 0
    for k in range(n):
        p = A[k][k]
        if p == 0:
            return None
        if p > 0:
            pos += 1
        else:
            neg += 1
        for r in range(k + 1, n):
            if A[r][k] != 0:
                fct = A[r][k] / p
                A[r] = [a - fct * b for a, b in zip(A[r], A[k])]
    return pos, neg


def solve_exact(A, b):
    n = len(A)
    Mx = [[Fraction(x) for x in row] + [Fraction(bb)] for row, bb in zip(A, b)]
    for c in range(n):
        piv = next(r for r in range(c, n) if Mx[r][c] != 0)
        Mx[c], Mx[piv] = Mx[piv], Mx[c]
        for r in range(n):
            if r != c and Mx[r][c] != 0:
                fct = Mx[r][c] / Mx[c][c]
                Mx[r] = [a - fct * bb for a, bb in zip(Mx[r], Mx[c])]
    return [Mx[i][n] / Mx[i][i] for i in range(n)]


def poly_trim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def poly_rem(a, b):
    a = a[:]
    while len(a) >= len(b) and any(a):
        if a[-1] == 0:
            a.pop()
            continue
        fct = a[-1] / b[-1]
        shift = len(a) - len(b)
        for i in range(len(b)):
            a[shift + i] -= fct * b[i]
        a.pop()
    return poly_trim(a) if a else [Fraction(0)]


def poly_deriv(p):
    return [p[i] * i for i in range(1, len(p))] or [Fraction(0)]


def poly_gcd_deg(a, b):
    while any(b):
        a, b = b, poly_rem(a, b)
        b = poly_trim(b)
        if len(b) == 1 and b[0] == 0:
            break
    return len(poly_trim(a[:])) - 1


def sturm_real_roots(p):
    """Distinct real roots via Sturm sequence; signs at +-inf from
    leading coefficients (valid even when p is not squarefree)."""
    seq = [p, poly_deriv(p)]
    while True:
        r = poly_rem(seq[-2], seq[-1])
        if len(r) == 1 and r[0] == 0:
            break
        r = [-c for c in r]
        lc = abs(r[-1])
        r = [c / lc for c in r]
        seq.append(r)

    def changes(signs):
        s = [x for x in signs if x != 0]
        return sum(1 for a, b in zip(s, s[1:]) if a != b)

    plus = [1 if q[-1] > 0 else -1 for q in seq]
    minus = [(1 if q[-1] > 0 else -1) * (1 if (len(q) - 1) % 2 == 0 else -1)
             for q in seq]
    return changes(minus) - changes(plus)


# ======================= RUN ============================================
print("=== CONSTRUCTION & RC-9 (exact vs float link to sealed machinery) ===")
Kfull = build_K(24, 0.0)
Kb_seal = [row[1:] for row in Kfull[1:]]
Mb = M_tree_base()
Ms = M_ring_base()
base_ok = all(Kb_seal[i][j] == float(Fraction(Mb[i][j], 10))
              for i in range(N) for j in range(N))
Ks_float = [row[:] for row in Kb_seal]
Ks_float[0][0] += 1.0
Ks_float[N - 1][N - 1] += 1.0
Ks_float[0][N - 1] = Ks_float[N - 1][0] = -1.0
ring_ok = all(Ks_float[i][j] == float(Fraction(Ms[i][j], 10))
              for i in range(N) for j in range(N))
KF = {name: to_float(M) for name, (_, M, _) in MEMBERS.items()}
member_ok = all(KF[n][i][j] == float(Fraction(MEMBERS[n][1][i][j], 10))
                for n in KF for i in range(N) for j in range(N))
sym_ok = all(sym_part(KF[n]) == (Kb_seal if n.startswith("T") else Ks_float)
             for n in KF)

print("\n=== INSTRUMENT E: exact moments, ranks, Hankel tests ===")
EX = {}
for name, (role, M, g) in MEMBERS.items():
    s = moments(M, 47)
    r = krylov_rank(M)
    H24 = [[Fraction(s[i + j]) for j in range(24)] for i in range(24)]
    d = exact_rank(H24)
    H0 = [[s[i + j] for j in range(d)] for i in range(d)]
    H1 = [[s[i + j + 1] for j in range(d)] for i in range(d)]
    pd0, _, fail0 = sylvester_pd(H0)
    pd1, _, fail1 = sylvester_pd(H1)
    inert = inertia(H0)
    c = solve_exact(H0, [-s[d + i] for i in range(d)])
    p = [Fraction(x) for x in c] + [Fraction(1)]
    sqfree = poly_gcd_deg(p, poly_deriv(p)) == 0
    nreal = sturm_real_roots(p)
    EX[name] = {"role": role, "r": r, "d": d, "H0_pd": pd0, "H1_pd": pd1,
                "H0_first_nonpositive_pivot": fail0,
                "H0_inertia": list(inert) if inert else None,
                "p_squarefree": sqfree, "distinct_real_roots": nreal,
                "moments_s0_s4_scaled": [s[i] for i in range(5)]}
    print(f"   {name:7s}: r={r:2d} d={d:2d}  H0_PD={pd0!s:5s} H1_PD={pd1!s:5s}"
          f"  inertia={inert}  squarefree={sqfree}  real_roots={nreal}")

rc9 = (base_ok and ring_ok and member_ok
       and EX["C(0)"]["r"] == 12 and EX["C(0)"]["d"] == 12
       and EX["T(0)"]["r"] == 23 and EX["T(0)"]["d"] == 23)
halt_check(rc9, f"RC-9 exact construction: sealed build_K bath == float(M_b/10) "
                f"entrywise ({base_ok}); float ring K_s == float(M_s/10) "
                f"({ring_ok}); every member K == float(M/10) ({member_ok}); "
                f"C(0) r=d={EX['C(0)']['r']}/{EX['C(0)']['d']} (12); "
                f"T(0) r=d={EX['T(0)']['r']}/{EX['T(0)']['d']} (23)")
check(True, f"NOTE (not a frozen gate): float symmetric parts equal K_b / K_s "
            f"exactly at every member: {sym_ok} (the exact integer "
            f"symmetric parts are held by construction)", "note")
zero_aff = [n for n, v in EX.items() if v["role"] == "zero-affinity"]
rc8 = all(EX[n]["d"] == EX[n]["r"] and EX[n]["H0_pd"] for n in zero_aff)
halt_check(rc8, "RC-8 exact CM at every zero-affinity member (d = r and "
                "H0 > 0 exactly): " + ", ".join(
                    f"{n}: d={EX[n]['d']}, H0_PD={EX[n]['H0_pd']}"
                    for n in zero_aff))
rc10 = all(EX[n]["H1_pd"] for n in EX if EX[n]["H0_pd"])
halt_check(rc10, "RC-10 H1 identity: H1 > 0 at every member where H0 > 0")

print("\n=== INSTRUMENT B: 9 members x (full + halved) = 18 trajectories ===")
TD = {}
for name in MEMBERS:
    K = KF[name]
    mu = min(jacobi_eig([row[:] for row in sym_part(K)])[0])
    e_f, g_f = rk4_linear(K, 10000, 1e-4, 15600, 2.5e-3, 500, 200)
    e_h, g_h = rk4_linear(K, 20000, 5e-5, 31200, 1.25e-3, 1000, 400)
    TD[name] = {"mu": mu, "early": e_f, "gated": g_f,
                "early_h": e_h, "gated_h": g_h}
    print(f"   {name:7s}: mu={mu:.6f}  k(40)={g_f[-1]:.4e}")

print("\n=== RC: CONTROLS (halt-grade) ===")
k_anchor_eig, k0_anchor = eig_kernel(Kb_seal, TAUS)
mu_T = TD["T(0)"]["mu"]
rel40 = abs(k_anchor_eig[-1] - K40_SEAL) / K40_SEAL
td_vs = max(abs(a - b) * math.exp(mu_T * t)
            for a, b, t in zip(TD["T(0)"]["gated"], k_anchor_eig, TAUS))
halt_check(rel40 < 1e-9 and td_vs < 1e-6,
           f"RC-1 replication: eigen anchor k(40) |rel Delta| = {rel40:.1e} "
           f"< 1e-9; time-domain vs eigen sup |Dk| e^(mu tau) = "
           f"{td_vs:.1e} < 1e-6")
rc2 = {n: max(abs(a - b) * math.exp(TD[n]["mu"] * t)
              for a, b, t in zip(TD[n]["gated"], TD[n]["gated_h"], TAUS))
       for n in TD}
halt_check(max(rc2.values()) < 1e-6,
           f"RC-2 halved-schedule audit, all 18 trajectories: worst "
           f"sup |Dk| e^(mu tau) = {max(rc2.values()):.1e} < 1e-6")
g9 = math.sqrt(1 - 0.81)
ST = [row[:] for row in Kb_seal]
for i in range(N - 1):
    ST[i][i + 1] = ST[i + 1][i] = -g9
k_ST, _ = eig_kernel(ST, TAUS)
rc3a = max(abs(a - b) * math.exp(TD["T(0.9)"]["mu"] * t)
           for a, b, t in zip(TD["T(0.9)"]["gated"], k_ST, TAUS))
k_C0, _ = eig_kernel(KF["C(0)"], TAUS)
rc3b = max(abs(a - b) * math.exp(TD["C(0)"]["mu"] * t)
           for a, b, t in zip(TD["C(0)"]["gated"], k_C0, TAUS))
halt_check(rc3a < 1e-6 and rc3b < 1e-6,
           f"RC-3 reciprocal twins: T(0.9) vs eigen S_T(0.9) {rc3a:.1e}; "
           f"C(0) vs its eigen kernel {rc3b:.1e} (both < 1e-6, "
           f"envelope-normalized)")
all_rec = {n: TD[n]["early"] + TD[n]["gated"] + TD[n]["early_h"] + TD[n]["gated_h"]
           for n in TD}
minpos = min(min(v) for v in all_rec.values())
halt_check(minpos > 0.0,
           f"RC-5 Metzler sign: k > 0 at every recorded point of every "
           f"trajectory (min = {minpos:.3e})")
env_bad = []
for n in TD:
    mu = TD[n]["mu"]
    for vals, taus in ((TD[n]["early"], EARLY), (TD[n]["gated"], TAUS),
                       (TD[n]["early_h"], EARLY), (TD[n]["gated_h"], TAUS)):
        for v, t in zip(vals, taus):
            if abs(v) > math.exp(-mu * t) * (1 + 1e-9):
                env_bad.append((n, t))
halt_check(not env_bad,
           f"RC-6 accretive envelope |k| <= e^(-mu tau)(1+1e-9) at every "
           f"recorded point of every member: {len(env_bad)} breaches")
E_anchor = envelope(k_anchor_eig)
re_c, ra_c, grade_c, _, _ = fit_residuals(E_anchor)
halt_check(E_anchor == k_anchor_eig and abs(re_c - R_EXP_SEAL) < 1e-12
           and abs(ra_c - R_ALG_SEAL) < 1e-12 and grade_c == "EXPONENTIAL-GRADE",
           f"RC-7 comparator certification on the eigen-form anchor: E == k "
           f"exactly ({E_anchor == k_anchor_eig}); R_exp |D| = "
           f"{abs(re_c - R_EXP_SEAL):.1e}, R_alg |D| = "
           f"{abs(ra_c - R_ALG_SEAL):.1e}; grade {grade_c}")

print("\n=== X: affinity acts in the window (conditions only L-3) ===")
twins = {}
for g in ("0.1", "0.3", "0.6", "0.9"):
    gf = float(G[g])
    S = [row[:] for row in Ks_float]
    c = math.sqrt(1 - gf * gf)
    for p, q in ring_edges():
        S[p][q] = S[q][p] = -c
    twins[g], _ = eig_kernel(S, TAUS)
xdiff = {g: max(abs(a - b) * math.exp(TD[f"C({g})"]["mu"] * t)
                for a, b, t in zip(TD[f"C({g})"]["gated"], twins[g], TAUS))
         for g in twins}
x1 = xdiff["0.9"] > 0.01
check(x1, f"X-1' C(0.9) vs reciprocal twin S(0.9): sup |Dk| e^(mu tau) = "
          f"{xdiff['0.9']:.4e} > 0.01 (not banded)")

print("\n=== H-1 / M-1: the response properties ===")
adj = [n for n in EX if EX[n]["role"] == "adjudicating"]
h1_fail_members = [n for n in adj if EX[n]["H0_pd"]]
h1 = not h1_fail_members
check(h1, "H-1 exact CM breach at every adjudicating member (H0 of size d "
          "not > 0): " + ", ".join(
              f"{n}: d={EX[n]['d']} r={EX[n]['r']} H0_PD={EX[n]['H0_pd']}"
              for n in adj))
MEM = {}
for n in TD:
    E = envelope(TD[n]["gated"])
    r_e, r_a, gr, _, _ = fit_residuals(E)
    MEM[n] = {"R_exp": r_e, "R_alg": r_a, "grade": gr, "E40": E[-1]}
m1_fail = [n for n in MEM if MEM[n]["grade"] != "EXPONENTIAL-GRADE"]
m1 = not m1_fail
check(m1, "M-1 P_memory (R-1 envelope comparator) EXPONENTIAL-GRADE at every "
          "member" + ("" if m1 else f" -- ALGEBRAIC at {m1_fail}"))

# ---------------- maps (ungated) ----------------------------------------
GRAM = {}
for n in TD:
    out = {}
    for tag, key in (("full", "gated"), ("halved", "gated_h")):
        ks = TD[n][key]
        Gm = [[ks[2 + i + j] for j in range(39)] for i in range(39)]
        out[tag] = min(jacobi_eig(Gm)[0])
    GRAM[n] = out
MONO = {n: max(TD[n]["gated"][i + 1] - TD[n]["gated"][i] for i in range(78))
        for n in TD}
check(True, "Maps (ungated): exact mechanism map " + "; ".join(
    f"{n}: d={EX[n]['d']}, real_roots={EX[n]['distinct_real_roots']}, "
    f"sqfree={EX[n]['p_squarefree']}, inertia={EX[n]['H0_inertia']}"
    for n in EX), "diag")
check(True, "Maps (ungated): operational Gram min eig (full/halved) " + "; ".join(
    f"{n}: {GRAM[n]['full']:+.2e}/{GRAM[n]['halved']:+.2e}" for n in GRAM)
      + " | monotone (b) max step " + "; ".join(
    f"{n}: {MONO[n]:+.1e}" for n in MONO), "diag")

# ---------------- outcome rule (frozen Sec. 5) --------------------------
SCOPE = ("within the declared background mathematics (exact rational "
         "arithmetic for Instrument E, the frozen RK4 schedule for "
         "Instrument B, exact symmetric eigendecomposition for the identity "
         "references), the declared members T in {0, 0.9}, C in {0, 0.1, "
         "0.3, 0.6, 0.9}, B in {0.3, 0.9} on the sealed C1 bath and its "
         "one-spring ring closure, with K_s held, and the declared window, "
         "grids, and comparator")
gated = [c for c in CHECKS if c["kind"] in ("ok", "ctrl")]
n_ok = sum(1 for c in gated if c["pass"])
fails = [c["summary"] for c in gated if not c["pass"]]
rc3_ok = rc3a < 1e-6 and rc3b < 1e-6

lines = {}
if HALT:
    label = "HALT"
else:
    lines["L-1"] = ("NON-RECIPROCITY WITHOUT CYCLE AFFINITY: REDUCIBLE TO A "
                    "RECIPROCAL TWIN (identity-grade; F-1 and Kolmogorov "
                    "instantiated) -- these kernels change with gamma and stay "
                    "in the reciprocal class" if (rc3_ok and rc8) else
                    "not issued")
    lines["L-2"] = ("CYCLE AFFINITY: BREAKS P_positivity (c), complete "
                    "monotonicity, exactly, at every declared circulating "
                    "member -- (i) necessity of affinity is a theorem; (ii) "
                    "the breach at each declared member is certified by exact "
                    "computation; (iii) (c) adjudicated exactly, (a) held by "
                    "identity, (b) not adjudicated, mapped" if h1 else
                    f"not issued: exactly CM at {h1_fail_members}")
    if m1 and x1:
        lines["L-3"] = ("CYCLE AFFINITY: NOT-LOAD-BEARING for P_memory (R-1 "
                        "envelope reading; accretivity held)")
    elif not m1:
        lines["L-3"] = (f"not issued: COMPARATOR-LIMITATION at {m1_fail} "
                        "(E graded ALGEBRAIC although |k| <= e^(-mu tau) is "
                        "identity-held; instrument finding)")
    else:
        lines["L-3"] = "not issued: X-1' failed (memory line would be vacuous)"
    if h1_fail_members:
        label = "OUTCOME-C"
    elif not (m1 and x1) or fails:
        label = "L01D-PARTIAL"
    else:
        label = "OUTCOME-B"

out = {
    "fork": "L0-1d (D-HERM-a, cycle affinity; floor obligation O-1)",
    "charter": "L0_1D_CHARTER_01.md (FROZEN 3a8ae1b; review record "
               "L0_1D_PREFREEZE_REVIEW_01.md)",
    "authority": "registry rulings R-1..R-4; floor termination condition "
                 "(L0_1_FLOOR_TERMINATION_ADOPTION_01.md)",
    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S+00:00", time.gmtime()),
    "environment": {"python": sys.version.split()[0], "pure_stdlib": True,
                    "deterministic": "no RNG"},
    "defect_history": DEFECTS,
    "measurements": {
        "exact": EX,
        "affinity": {n: affinity(n) for n in MEMBERS},
        "mu": {n: TD[n]["mu"] for n in TD},
        "rc2_worst": rc2,
        "twin_difference_envelope_normalized": xdiff,
        "memory": MEM,
        "gram_min_eig": GRAM,
        "monotone_max_step": MONO,
        "kernels_gated": {n: TD[n]["gated"] for n in TD},
        "kernels_early": {n: TD[n]["early"] for n in TD},
    },
    "checks": CHECKS,
    "adjudication": {"run_label": label, "lines": lines, "scope": SCOPE,
                     "precedence": "HALT > OUTCOME-C > L01D-PARTIAL; "
                                   "OUTCOME-B requires L-1, L-2, L-3"},
    "elapsed_s": round(time.time() - T0, 2),
}
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                    "L0_1D_RESULT.json")
blob = json.dumps(out, indent=1)
with open(path, "w") as fh:
    fh.write(blob)
sha = hashlib.sha256(blob.encode()).hexdigest()
print(f"\nartifact written: {os.path.abspath(path)} (sha {sha[:16]}...)")
print(f"\nL0-1d: {n_ok}/{len(gated)} gated checks passed; failures: "
      f"{len(fails)}; halts: {len(HALT)}")
if HALT:
    print("HALT: " + "; ".join(HALT))
    sys.exit(2)
print(f"RUN LABEL: {label}")
for k_, v_ in lines.items():
    print(f"{k_}: {v_}")
print("HARD STOP: verdicts recorded pending owner ruling.")
sys.exit(0 if not fails else 1)
