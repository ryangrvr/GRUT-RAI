"""L0-1h (O-2) exact appendix — instrument for L0_1H_THEOREM_01.md §4 (frozen at 165a5f6).

Frozen list:
  A-1  w*(g): rational bracket of width <= 1e-12 by exact sign evaluation of
       p(w) = w^(n-1)(w+a) - g^n.
  A-2  d_acc(g): rational bracket [l, u] of width <= 1e-12. K_s(u) > 0 is shown
       by all exact LDL^T pivots > 0; K_s(l) not > 0 by some pivot <= 0.
       The band [A-1 upper, A-2 lower] is reported (a consistency check of P-2).
  A-3  witness: a float scan over t in {j/8 : 1 <= j <= 1600} (non-gating) picks
       t*. Then an exact certification at t*: L = lower bound on y = e^{P t*} e1,
       U1 = upper bound on y1. SEPARATED iff g*L_n > (u+a)*U1. K(u, g) is then a
       strictly accretive, non-monotone member.
  A-4  no witness: NOT CERTIFIED, with the float estimate of d_mono. It is never
       promoted, and never read as d_mono < d_acc.
  A-5  P-1 cross-check (not a gate): float max_t k(t) at the witness member,
       compared with e^{-(u - w*) t}.

Rigour in A-3: P = gQ + a(I - E11) >= 0. The squaring is e^{Pt} = (e^{P tau})^(2^s)
with tau = t/2^s, and every intermediate entry is nonnegative. The lower matrix
is the Taylor partial sum, with each entry rounded DOWN to 256 significant bits.
The upper matrix adds the tail bound 2*x^(M+1)/(M+1)! (x = ||P||_inf*tau <= 1/2;
entries of P^m are at most ||P||_inf^m), with each entry rounded UP. The
products preserve the order entrywise because every entry is >= 0.

Usage: python3 calc/l01h_appendix.py MEMBER  -> n=23, a=1, the frozen grid
                                                (writes L0_1H_APPENDIX_RESULT.json)
       python3 calc/l01h_appendix.py n a g1,g2,...  -> non-member test (no file)
"""
import sys, json, hashlib, math
from fractions import Fraction as F
import numpy as np
from scipy.linalg import expm

BITS = 256
TOL = F(1, 10**12)


def rdown(x):
    if x <= 0:
        assert x == 0
        return F(0)
    n, d = x.numerator, x.denominator
    sh = BITS - (n.bit_length() - d.bit_length())
    if sh >= 0:
        return F((n << sh) // d, 1 << sh)
    return F((n // (d << -sh)) << -sh, 1)


def rup(x):
    if x <= 0:
        assert x == 0
        return F(0)
    n, d = x.numerator, x.denominator
    sh = BITS - (n.bit_length() - d.bit_length())
    if sh >= 0:
        return F(-((-(n << sh)) // d), 1 << sh)
    return F((-((-n) // (d << -sh))) << -sh, 1)


def p_val(w, n, a, g):
    return w ** (n - 1) * (w + a) - g ** n


def bracket_wstar(n, a, g):
    # unique positive root; p(0) = -g^n < 0 and p(g) = g^(n-1)*a > 0
    lo, hi = F(0), g
    assert p_val(lo, n, a, g) < 0 < p_val(hi, n, a, g)
    while hi - lo > TOL:
        m = (lo + hi) / 2
        if p_val(m, n, a, g) < 0:
            lo = m
        else:
            hi = m
    return lo, hi


def Ks(d, n, a, g):
    M = [[F(0)] * n for _ in range(n)]
    for i in range(n):
        M[i][i] = d
    M[0][0] += a
    h = g / 2
    for i in range(n):
        j = (i + 1) % n
        M[i][j] -= h
        M[j][i] -= h
    return M


def is_pd(M):
    """Exact LDL^T; True iff every pivot > 0."""
    n = len(M)
    A = [row[:] for row in M]
    for k in range(n):
        if A[k][k] <= 0:
            return False
        for i in range(k + 1, n):
            if A[i][k] != 0:
                f = A[i][k] / A[k][k]
                for j in range(k, n):
                    if A[k][j] != 0:
                        A[i][j] -= f * A[k][j]
    return True


def bracket_dacc(n, a, g, wlo):
    lo, hi = wlo, g + a  # K_s(w*) is not > 0 (P-2), and shifting down keeps that; Gershgorin: d > g gives PD
    assert not is_pd(Ks(lo, n, a, g)) and is_pd(Ks(hi, n, a, g))
    while hi - lo > TOL:
        m = (lo + hi) / 2
        m = F(math.floor(m * 2 ** 60), 2 ** 60) if m.denominator > 2 ** 60 else m
        if is_pd(Ks(m, n, a, g)):
            hi = m
        else:
            lo = m
    return lo, hi


def P_float(n, a, g):
    Q = np.zeros((n, n))
    for i in range(n - 1):
        Q[i + 1, i] = 1
    Q[0, n - 1] = 1
    E = np.zeros((n, n)); E[0, 0] = 1
    return g * Q + a * (np.eye(n) - E)


def scan(n, a, g, wstar_f):
    P = P_float(n, a, g)
    Ps = P - (wstar_f + a) * np.eye(n)  # shift keeps the ratio and prevents overflow
    best, bj = -1.0, None
    for j in range(1, 1601):
        y = expm(Ps * (j / 8))[:, 0]
        r = g * y[-1] / y[0]
        if r > best:
            best, bj = r, j
    return best, bj


def matmul(A, B, rnd):
    n = len(A)
    C = [[F(0)] * n for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        for k in range(n):
            if Ai[k] == 0:
                continue
            aik = Ai[k]
            Bk = B[k]
            Ci = C[i]
            for j in range(n):
                if Bk[j] != 0:
                    Ci[j] += aik * Bk[j]
    return [[rnd(x) for x in row] for row in C]


def exp_bounds(n, a, g, t):
    """Entrywise lower/upper bounds on the first column of e^{Pt}."""
    norm = g + a  # ||P||_inf
    s = 0
    while norm * t / 2 ** s > F(1, 2):
        s += 1
    tau = t / 2 ** s
    P = [[F(0)] * n for _ in range(n)]
    for i in range(n - 1):
        P[i + 1][i] = g
    P[0][n - 1] = g
    for i in range(1, n):
        P[i][i] = a
    Pt = [[x * tau for x in row] for row in P]
    Mterms = 80
    S = [[F(int(i == j)) for j in range(n)] for i in range(n)]
    T = [row[:] for row in S]
    for m in range(1, Mterms + 1):
        T = matmul(T, Pt, lambda x: x)
        T = [[x / m for x in row] for row in T]
        S = [[S[i][j] + T[i][j] for j in range(n)] for i in range(n)]
        T = [[rup(x) for x in row] for row in T]  # control size; T only feeds the (upper-safe) sum
    # S may contain rounded-up terms, so rebuild a strict lower bound from exact terms instead
    L = [[F(int(i == j)) for j in range(n)] for i in range(n)]
    Tl = [row[:] for row in L]
    for m in range(1, Mterms + 1):
        Tl = matmul(Tl, Pt, rdown)
        Tl = [[rdown(x / m) for x in row] for row in Tl]
        L = [[rdown(L[i][j] + Tl[i][j]) for j in range(n)] for i in range(n)]
    x = norm * tau
    tail = 2 * x ** (Mterms + 1) / math.factorial(Mterms + 1)
    U = [[rup(S[i][j] + tail) for j in range(n)] for i in range(n)]
    for _ in range(s):
        L = matmul(L, L, rdown)
        U = matmul(U, U, rup)
    return [L[i][0] for i in range(n)], [U[i][0] for i in range(n)], s


def one_g(n, a, g):
    wlo, whi = bracket_wstar(n, a, g)
    dl, du = bracket_dacc(n, a, g, wlo)
    wf = float((wlo + whi) / 2)
    best, bj = scan(n, a, g, wf)
    dmono_est = best - a
    rec = {
        "g": str(g),
        "A1_wstar": [str(wlo), str(whi)], "A1_wstar_float": wf,
        "A2_dacc": [str(dl), str(du)], "A2_dacc_float": float(du),
        "A2_band_nonempty": whi < dl,
        "A2_band_float": [float(whi), float(dl)],
        "scan_t_star": f"{bj}/8", "scan_dmono_est_float": dmono_est,
    }
    t = F(bj, 8)
    Lv, Uv, s = exp_bounds(n, a, g, t)
    lhs = g * Lv[-1]
    rhs = (du + a) * Uv[0]
    cert = lhs > rhs
    rec["A3_squarings"] = s
    if cert:
        rec["A3_status"] = "SEPARATED"
        rec["A3_witness_member"] = {"d": str(du), "g": str(g), "t": str(t)}
        rec["A3_certified_margin_ratio"] = float(lhs / rhs)
        # A-5 (non-gating): P-1 cross-check at the witness member
        n_ = n
        Q = np.zeros((n_, n_))
        for i in range(n_ - 1):
            Q[i + 1, i] = 1
        Q[0, n_ - 1] = 1
        E = np.zeros((n_, n_)); E[0, 0] = 1
        K = float(du) * np.eye(n_) + a * E - float(g) * Q
        worst = -1e300; kmax = 0.0
        for j in range(1, 1601):
            tt = j / 8
            k = expm(-K * tt)[0, 0]
            kmax = max(kmax, k)
            worst = max(worst, k - math.exp(-(float(du) - wf) * tt))
        rec["A5_max_k_float"] = kmax
        rec["A5_max_k_minus_P1_bound_float"] = worst
    else:
        rec["A3_status"] = "NOT CERTIFIED"
        rec["A4_float_note"] = ("d_mono_est vs d_acc (float, never promoted): "
                                f"{dmono_est:.6g} vs {float(du):.6g}")
    return rec


def main():
    if sys.argv[1] == "MEMBER":
        n, a = 23, F(1)
        grid = [F(1, 20), F(1, 10), F(1, 4), F(1, 2), F(1), F(2), F(4), F(10)]
    else:
        n, a = int(sys.argv[1]), F(sys.argv[2])
        assert not (n == 23 and a == 1), "member family: use MEMBER"
        grid = [F(x) for x in sys.argv[3].split(",")]
    out = {"instrument": "calc/l01h_appendix.py", "frozen_at": "165a5f6",
           "n": n, "a": str(a), "results": []}
    for g in grid:
        r = one_g(n, a, g)
        print(json.dumps(r), flush=True)
        out["results"].append(r)
    if sys.argv[1] == "MEMBER":
        blob = json.dumps(out, indent=1, sort_keys=True)
        open("L0_1H_APPENDIX_RESULT.json", "w").write(blob)
        print("sha256", hashlib.sha256(blob.encode()).hexdigest())


if __name__ == "__main__":
    main()
