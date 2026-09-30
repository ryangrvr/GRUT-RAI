"""S2-1 exact instantiation / verification instrument (charter S2_NOISE_ORIGIN_CHARTER_01.md, frozen
227dd09; derivation S2_NOISE_ORIGIN_DERIVATION_01.md, verified at 32645cc).

Not the source of any theorem. Exact rational/symbolic arithmetic only: no RNG, no SDE simulation,
no floating stochastic trajectories.

E-1  exact Dynkin coefficients c_n = (L^n x1)(a e1) and c_n^phi = (A^n x1)(a e1), n <= 4, on the full
     23-site K_b, instantiated at every (beta, a, profile). Here L = A + D, A = f.grad and
     D = sum_i T_i d_i^2. Delta_n := c_n - c_n^phi (Dynkin normalization: m1(t) = sum c_n t^n/n!).
E-2  symbolic re-derivation of the finite-moment M2 coefficient algebra, and of the xi-independence
     and q - q0 identities used by HT-B.
E-3  structural checks: K_b symmetric positive definite (exact Cholesky), off-diagonal <= 0, f odd.

Usage: python3 calc/s2_noise_origin.py   (writes S2_NOISE_ORIGIN_RESULT.json)
"""
import hashlib
import json
import pathlib
import traceback

import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "S2_NOISE_ORIGIN_RESULT.json"
N = 23
NMAX = 4
R = {"charter_commit": "227dd09", "derivation_commit": "32645cc",
     "charter_sha256": hashlib.sha256((ROOT / "S2_NOISE_ORIGIN_CHARTER_01.md").read_bytes()).hexdigest(),
     "derivation_sha256": hashlib.sha256((ROOT / "S2_NOISE_ORIGIN_DERIVATION_01.md").read_bytes()).hexdigest(),
     "script_sha256": hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
     "checks": {}, "tables": {}, "reported": {}, "defects": []}

X = sp.symbols("x1:%d" % (N + 1))
b, a = sp.symbols("beta a")
Ts = sp.symbols("T1:%d" % (N + 1))
K = sp.zeros(N, N)
for i in range(N):
    K[i, i] = sp.Rational(23, 10) if i < N - 1 else sp.Rational(13, 10)
for i in range(N - 1):
    K[i, i + 1] = K[i + 1, i] = -1
f = [sp.expand(-sum(K[i, j] * X[j] for j in range(N)) - 4 * b * X[i] ** 3) for i in range(N)]

BETAS = [sp.Integer(0), sp.Rational(3, 100), sp.Rational(1, 10), sp.Rational(3, 10), sp.Integer(1),
         sp.Integer(3)]
AS = [sp.Rational(1, 1000), sp.Rational(-1, 1000), sp.Integer(1), sp.Integer(-1), sp.Integer(3),
      sp.Integer(-3)]
PROFILES = {
    "F": [sp.Integer(1)] * N,
    "G(inf)": [sp.Rational(i - 1, 22) for i in range(1, N + 1)],
    "GR(inf)": [sp.Rational(23 - i, 22) for i in range(1, N + 1)],
}


def check(name, ok, detail=None):
    R["checks"][name] = {"ok": bool(ok), "detail": detail}
    print(f"  {'PASS' if ok else 'FAIL'}  {name}")


def Aop(g):
    return sp.expand(sum(f[i - 1] * sp.diff(g, X[i - 1])
                         for i in range(1, N + 1) if X[i - 1] in g.free_symbols))


def Dop(g):
    return sp.expand(sum(Ts[i - 1] * sp.diff(g, X[i - 1], 2)
                         for i in range(1, N + 1) if X[i - 1] in g.free_symbols))


at_a = {X[0]: a, **{X[i]: 0 for i in range(1, N)}}

try:
    # ---------------- E-3 structural ----------------
    print("=== E-3 structural ===")
    offdiag_ok = all(K[i, j] <= 0 for i in range(N) for j in range(N) if i != j)
    L_ch = K.cholesky(hermitian=False)
    pd_ok = all(L_ch[i, i] > 0 for i in range(N)) and (L_ch * L_ch.T - K) == sp.zeros(N, N)
    gersh = min(K[i, i] - sum(abs(K[i, j]) for j in range(N) if j != i) for i in range(N))
    odd_ok = all(sp.expand(fi.subs({x: -x for x in X}, simultaneous=True) + fi) == 0 for fi in f)
    check("E-3 K_b symmetric", K == K.T)
    check("E-3 off-diagonal <= 0 (cooperative drift)", offdiag_ok)
    check("E-3 K_b positive definite (exact Cholesky)", pd_ok)
    check("E-3 Gershgorin lower bound = 3/10", gersh == sp.Rational(3, 10), str(gersh))
    check("E-3 f odd", odd_ok)

    # ---------------- E-1 symbolic Dynkin coefficients ----------------
    print("=== E-1 symbolic Dynkin coefficients (n <= 4) ===")
    cS = [X[0]]
    cP = [X[0]]
    for n in range(1, NMAX + 1):
        cS.append(sp.expand(Aop(cS[-1]) + Dop(cS[-1])))
        cP.append(Aop(cP[-1]))
    Delta = [sp.expand((cS[n] - cP[n]).subs(at_a)) for n in range(NMAX + 1)]
    R["symbolic_Delta"] = {str(n): str(sp.factor(Delta[n])) for n in range(NMAX + 1)}
    for n in range(NMAX + 1):
        print(f"    Delta_{n} = {sp.factor(Delta[n])}")
    K11 = K[0, 0]
    check("E-1 Delta_0 = Delta_1 = 0 (symbolic)", Delta[0] == 0 and Delta[1] == 0)
    check("E-1 Delta_2 = -24 beta T1 a (symbolic)", sp.expand(Delta[2] + 24 * b * Ts[0] * a) == 0,
          str(Delta[2]))
    check("E-1 Delta_3 = 24 beta T1 a (44 beta a^2 + 5 K11) (symbolic)",
          sp.expand(Delta[3] - 24 * b * Ts[0] * a * (44 * b * a ** 2 + 5 * K11)) == 0, str(Delta[3]))
    check("E-1 Delta_3 free of T2..T23", not (Delta[3].free_symbols & set(Ts[1:])))
    check("I-2 beta = 0 => Delta_n = 0, n <= 4 (all T, a)",
          all(sp.expand(Delta[n].subs(b, 0)) == 0 for n in range(NMAX + 1)))

    # ---------------- instantiation ----------------
    print("=== instantiation at declared members ===")
    tab = {}
    i1 = i3 = i4 = True
    for pname, Tv in PROFILES.items():
        sub_T = {Ts[i]: Tv[i] for i in range(N)}
        for bv in BETAS:
            for av in AS:
                vals = [sp.nsimplify(Delta[n].subs(sub_T).subs({b: bv, a: av})) for n in range(NMAX + 1)]
                key = f"{pname}|beta={bv}|a={av}"
                tab[key] = {f"Delta_{n}": str(vals[n]) for n in range(NMAX + 1)}
                tab[key].update({f"t^{n}_coeff": str(vals[n] / sp.factorial(n)) for n in range(NMAX + 1)})
                T1 = Tv[0]
                if pname == "F":
                    i1 &= (vals[2] == -24 * bv * T1 * av) and \
                        (vals[3] == 24 * bv * T1 * av * (44 * bv * av ** 2 + 5 * K11))
                if pname == "G(inf)":
                    i3 &= (vals[2] == 0)
                if pname == "GR(inf)":
                    i4 &= (vals[2] == -24 * bv * T1 * av)
    R["tables"]["Delta"] = tab
    check("I-1 F: Delta_2 and Delta_3 identities at every (beta, a)", i1)
    check("I-3 G(inf): Delta_2 = 0 at every (beta, a)", i3)
    check("I-4 GR(inf): Delta_2 = -24 beta T1 a (T1 = 1) at every (beta, a)", i4)

    # reported only
    rep = {}
    for bv in BETAS[1:]:
        for av in AS:
            g = tab[f"G(inf)|beta={bv}|a={av}"]
            first = next((n for n in range(NMAX + 1) if g[f"Delta_{n}"] != "0"), None)
            fk, gk = tab[f"F|beta={bv}|a={av}"], tab[f"GR(inf)|beta={bv}|a={av}"]
            rep[f"beta={bv}|a={av}"] = {
                "G(inf)_Delta_3": g["Delta_3"], "G(inf)_Delta_4": g["Delta_4"],
                "G(inf)_first_nonzero_order<=4": first,
                "F_minus_GR(inf)_Delta_3": str(sp.nsimplify(sp.Rational(fk["Delta_3"]) - sp.Rational(gk["Delta_3"]))),
                "F_minus_GR(inf)_Delta_4": str(sp.nsimplify(sp.Rational(fk["Delta_4"]) - sp.Rational(gk["Delta_4"])))}
    R["reported"] = rep

    # ---------------- E-2 symbolic M2 algebra and HT-B identities ----------------
    print("=== E-2 finite-moment M2 algebra and HT-B identities ===")
    xi = sp.symbols("xi1:%d" % (N + 1))
    y = {X[0]: a + xi[0], **{X[i]: xi[i] for i in range(1, N)}}
    d1 = sp.expand(f[0].subs(y, simultaneous=True) - f[0].subs(at_a))
    target1 = sp.expand(-K[0, 0] * xi[0] - K[0, 1] * xi[1] - 4 * b * (3 * a ** 2 * xi[0] + 3 * a * xi[0] ** 2 + xi[0] ** 3))
    check("E-2 O(t) difference polynomial (=> -12 beta a E xi1^2 - 4 beta E xi1^3 - K12 E xi2 when E xi1 = 0)",
          sp.expand(d1 - target1) == 0)
    fg1 = cP[2]
    y0 = {X[0]: a, **{X[i]: xi[i] for i in range(1, N)}}
    d2 = sp.expand(fg1.subs(y0, simultaneous=True) - fg1.subs(at_a))
    rest = sp.expand(d2 - K[0, 1] * (4 * b * xi[1] ** 3 + K[1, 2] * xi[2]))
    ok2 = sp.expand(rest - sp.expand(rest.coeff(xi[1], 1) * xi[1])) == 0 and \
        not (rest.coeff(xi[1], 1).free_symbols & set(xi))
    check("E-2 O(t^2) difference (xi1 = 0) = K12(4 beta xi2^3 + K23 xi3) + (const) * xi2", ok2)
    # HT-B: Taylor coefficients 0,1,2 of the pair difference g1 at (a, -a) are xi-independent (xi1 = 0)
    yp = {X[0]: a, **{X[i]: xi[i] for i in range(1, N)}}
    ym = {X[0]: -a, **{X[i]: xi[i] for i in range(1, N)}}
    indep = True
    for n in range(3):
        gn = sp.expand(cP[n].subs(yp, simultaneous=True) - cP[n].subs(ym, simultaneous=True))
        indep &= not (gn.free_symbols & set(xi))
    check("E-2 HT-B: pair (a,-a) Taylor coefficients of g1 through t^2 are xi-independent", indep)
    p_, dp, dm = sp.symbols("p deltap deltam")
    Xp, Xm, Xp0, Xm0 = p_ + dp, -p_ + dm, p_, -p_
    q = Xp ** 2 + Xp * Xm + Xm ** 2
    q0 = Xp0 ** 2 + Xp0 * Xm0 + Xm0 ** 2
    e_ = dp - dm
    rho = dp ** 2 + dp * dm + dm ** 2
    check("E-2 HT-B: q - q0 = p e + rho (exact)", sp.expand(q - q0 - p_ * e_ - rho) == 0)
    check("E-2 HT-B: q0 = p^2", sp.expand(q0 - p_ ** 2) == 0)
except Exception:
    tb = traceback.format_exc()
    R["defects"].append(tb)
    print(tb)

R["all_checks_pass"] = all(v["ok"] for v in R["checks"].values()) and not R["defects"]
OUT.write_text(json.dumps(R, indent=1, default=str) + "\n")
print(f"\nall checks pass: {R['all_checks_pass']}")
print(f"wrote {OUT.name}; sha256 {hashlib.sha256(OUT.read_bytes()).hexdigest()}")
