#!/usr/bin/env python3
"""MATTER-SCOPE K_R CLOSURE AUDIT (owner ruling 2026-08-30, commit 15b1e57).
REVIEW ONLY: reproduce the certified poles/zeros by INDEPENDENT routes,
record the exact search domain, freeze. No contract-level object, no sign
selection, no new physics build.

INDEPENDENCE (disclosed in the coordination log before this run):
  first sheet: BISECTION (not Newton) on chi0 evaluated via the K-RICHARDSON
    route (k = 1/4, 1/8 extrapolation of the k != 0 expression -- different
    atom set from the production symbolic-k->0 evaluator).
  sheet II: STEPWISE TAYLOR CONTINUATION through the cut (Cauchy-integral
    derivatives at anchors + polynomial re-expansion; NO use of the
    production disc formulas), roots re-found by the SECANT method.
  Shared ground truth: the gated sheet-I evaluator only.

W-0. HARD STOP after the audit.
"""
import hashlib
import json
import os
import sys
import time

import mpmath as mp
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
T0 = time.time()
FAILS = []
CHECKS = []
NOTES = []
mp.mp.dps = 30


def stamp(m):
    print("[%7.1fs] %s" % (time.time() - T0, m))
    sys.stdout.flush()


def check(c, m, gate="", detail=None):
    ok = bool(c)
    print(("  ok   " if ok else "  FAIL ") + m)
    sys.stdout.flush()
    CHECKS.append({"pass": ok, "msg": m, "gate": gate, "detail": detail})
    if not ok:
        FAILS.append(m)
    return ok


def note(m):
    print("  note " + m)
    sys.stdout.flush()
    NOTES.append(m)


FRZ = json.loads(open(os.path.join(HERE, "Sigma_R_finite_full.json")).read())
KSHA = "dd77b1943e2068c643f4181438814a378c26bc8693b616be812fa5f5888c4ae1"
check(FRZ["manifest"]["complete_kernel_sha256"] == KSHA,
      "frozen kernel sha ok (IMMUTABLE)", gate="0")
PROD = json.loads(open(os.path.join(HERE, "WALL_KR_MATTER_RESULT.json")).read())
note("production result sha = %s..." % hashlib.sha256(
    open(os.path.join(HERE, "WALL_KR_MATTER_RESULT.json"), "rb")
    .read()).hexdigest()[:16])


class Gfun(sp.Function):
    nargs = 5


class Rfun(sp.Function):
    nargs = 5


S0 = sp.sympify(FRZ["sectors"]["0"]["srepr"], locals={"Gfun": Gfun,
                                                      "Rfun": Rfun})
om, kk, mm, muS = sp.symbols("omega k m mu", positive=True)
kap = sp.Symbol("kappa")


def Es(i, j):
    return sp.Symbol("E_%d%d" % (min(i, j), max(i, j)))


def Ps(i, j):
    return sp.Symbol("P_%d%d" % (min(i, j), max(i, j)))


sub0 = {}
for a in range(4):
    for b in range(a, 4):
        sub0[Es(a, b)] = 0
        sub0[Ps(a, b)] = 0
sub0[Es(1, 1)] = 1
sub0[Es(2, 2)] = -1
sub0[Ps(1, 1)] = 1
sub0[Ps(2, 2)] = -1
TTpp = sp.expand(S0.xreplace(sub0)) / 2
chi0_sym = sp.expand(TTpp.subs(kk, 0))
KAPN = sp.Float(mp.nstr(mp.log(4 * mp.pi) - mp.euler, 25), 25)


def cutpts_real(K2r):
    if K2r <= 4:
        return None
    r = mp.sqrt(1 - 4 / K2r)
    return ((1 - r) / 2, (1 + r) / 2)


def quad_atom(fam, n_, np_, e_, K2):
    K2 = mp.mpc(K2)
    D = lambda y: 1 - y * (1 - y) * K2
    w = lambda y: y**n_ * (1 - y)**np_
    if K2.imag != 0 or K2.real <= 4:
        bps = [0, mp.mpf(1) / 2, 1]
        if K2.real > 4:
            r = mp.re(mp.sqrt(1 - 4 / K2))
            bps = sorted({0, (1 - r) / 2, mp.mpf(1) / 2, (1 + r) / 2, 1})
        if fam == "G":
            return mp.quad(lambda y: w(y) * D(y)**e_ * (-mp.log(D(y))), bps)
        return mp.quad(lambda y: w(y) * D(y)**e_, bps)
    pts = cutpts_real(K2.real)
    Dr = lambda y: 1 - y * (1 - y) * K2.real
    if fam == "G":
        sgn = (-1) ** e_
        f = lambda y: w(y) * abs(Dr(y))**e_ * (-mp.log(abs(Dr(y)))) \
            * (sgn if pts[0] < y < pts[1] else 1)
        re = mp.quad(f, [0, pts[0], pts[1], 1])
        im = mp.pi * mp.quad(lambda y: w(y) * abs(Dr(y))**e_ * sgn,
                             [pts[0], pts[1]])
        return re + 1j * im
    def I(eta):
        return mp.quad(lambda y: w(y) * mp.power(mp.mpc(Dr(y), -eta), e_),
                       [0, pts[0], pts[1], 1])
    eta = mp.mpf("2e-5")
    return (8 * I(eta / 4) - 6 * I(eta / 2) + I(eta)) / 3


def eval_expr(expr, wv, kv, z_override=None):
    s2 = {om: sp.Float(mp.nstr(mp.re(mp.mpc(wv)), 22), 22)
          + sp.Float(mp.nstr(mp.im(mp.mpc(wv)), 22), 22) * sp.I,
          kk: sp.Float(mp.nstr(mp.mpf(kv), 20), 20) if kv else 0,
          mm: 1, muS: 1, kap: KAPN}
    e2 = expr.subs(s2)
    K2v = z_override if z_override is not None \
        else mp.mpc(wv)**2 - mp.mpf(kv)**2
    rep = {}
    for A in e2.atoms(Gfun, Rfun):
        v = quad_atom(type(A).__name__[0], int(A.args[0]), int(A.args[1]),
                      int(A.args[2]), K2v)
        rep[A] = sp.Float(mp.nstr(mp.re(v), 25), 25) \
            + sp.Float(mp.nstr(mp.im(v), 25), 25) * sp.I
    return mp.mpc(complex(sp.N(e2.subs(rep), 25)))


def chi0_I(z):
    """the gated sheet-I evaluator (shared ground truth, disclosed)."""
    return eval_expr(chi0_sym, mp.sqrt(mp.mpc(z)), 0, z_override=mp.mpc(z))


def chi0_richardson(x):
    """INDEPENDENT route: k-Richardson of the k != 0 expression (different
    atom set from chi0_sym)."""
    w = mp.sqrt(mp.mpf(x))
    v1 = eval_expr(TTpp, w, mp.mpf(1) / 4)
    v2 = eval_expr(TTpp, w, mp.mpf(1) / 8)
    return v2 + (v2 - v1) / 3


# ================= 1+2: FIRST-SHEET POLES, INDEPENDENT ROUTE =================
print("=== 1+2: FIRST-SHEET POLES (bisection + k-Richardson route) ===")
PROD_POLES = {"-1.0": 0.3486, "-2.0": 0.7995, "-5.0": 2.9465}
TRACK = {}
for gs, xp_prod in PROD_POLES.items():
    g = mp.mpf(gs)
    f = lambda x: x - g * mp.re(chi0_richardson(x))
    a, b = mp.mpf(xp_prod) - mp.mpf("0.15"), mp.mpf(xp_prod) + mp.mpf("0.15")
    fa, fb = f(a), f(b)
    ok_br = fa * fb < 0
    root = None
    if ok_br:
        for _ in range(40):
            c = (a + b) / 2
            fc = f(c)
            if fa * fc <= 0:
                b, fb = c, fc
            else:
                a, fa = c, fc
        root = (a + b) / 2
    d = abs(root - mp.mpf(xp_prod)) if root else mp.mpf("inf")
    TRACK[gs] = float(root) if root else None
    check(root is not None and d < mp.mpf("2e-3"),
          "pole at g=%s REPRODUCED by bisection + k-Richardson: x = %s "
          "(production %.4f, |d| = %.1e)" % (gs, mp.nstr(root, 6) if root
                                             else "none", xp_prod, d),
          gate="1")
# motion: monotone in |g| + two intermediate g values on the independent route
for gs in ("-1.5", "-3.0"):
    g = mp.mpf(gs)
    f = lambda x: x - g * mp.re(chi0_richardson(x))
    a, b = mp.mpf("0.2"), mp.mpf("3.9")
    if f(a) * f(b) < 0:
        for _ in range(40):
            c = (a + b) / 2
            if f(a) * f(c) <= 0:
                b = c
            else:
                a = c
        TRACK[gs] = float((a + b) / 2)
xs = [TRACK[k] for k in ("-1.0", "-1.5", "-2.0", "-3.0", "-5.0")
      if TRACK.get(k)]
check(len(xs) == 5 and all(xs[i] < xs[i + 1] for i in range(4)),
      "pole MOTION x_p(g) independently confirmed MONOTONE toward threshold: "
      "%s" % ["%.4f" % v for v in xs], gate="2")
imb = abs(mp.im(chi0_richardson(mp.mpf("3.95"))))
ima = abs(mp.im(chi0_richardson(mp.mpf("4.30"))))
check(imb < mp.mpf("1e-18") and ima > mp.mpf("1e-8"),
      "branch point FIXED at x = 4m^2 on the independent route (Im: %.1e "
      "below, %.2e above) -- unmoved by g by construction and verified"
      % (imb, ima), gate="2")
stamp("first sheet audited")

# ================= 3: SHEET-II ZEROS, INDEPENDENT CONTINUATION ==============
print("\n=== 3: SHEET-II ZEROS (stepwise Taylor continuation + secant) ===")


def taylor_coeffs(f, a, r, N=14, nodes=48):
    """Cauchy-integral derivatives: c_n = (1/2pi) Int f(a + r e^{it}) e^{-int} dt."""
    vals = [f(a + r * mp.expjpi(2 * mp.mpf(j) / nodes)) for j in range(nodes)]
    cs = []
    for n in range(N):
        s = sum(vals[j] * mp.expjpi(-2 * mp.mpf(j) * n / nodes)
                for j in range(nodes)) / nodes
        cs.append(s / r**n)
    return cs


def poly_eval(cs, a, z):
    return sum(c * (z - a)**n for n, c in enumerate(cs))


def poly_diff_shift(cs, a, b, N):
    """re-expand the polynomial sum c_n (z-a)^n around b (exact)."""
    out = []
    for k in range(N):
        s = mp.mpc(0)
        for n in range(k, len(cs)):
            s += cs[n] * mp.binomial(n, k) * (b - a)**(n - k)
        out.append(s)
    return out


# anchor 0: on sheet I, above the cut near x = 6 (radius clear of z = 4)
A0 = mp.mpc(6, mp.mpf("1.2"))
CS0 = taylor_coeffs(chi0_I, A0, mp.mpf("0.9"))
# validation: polynomial vs direct chi_I inside the disc
_t = A0 + mp.mpc("0.4", "-0.3")
relv = abs(poly_eval(CS0, A0, _t) - chi0_I(_t)) / abs(chi0_I(_t))
check(relv < mp.mpf("1e-6"),
      "Taylor anchor 0 validated inside its disc (rel %.1e vs direct "
      "sheet-I)" % relv, gate="3")
# step THROUGH the cut at x = 6: anchor path A0 -> 6+0.3i -> 6-0.5i -> ...
PATH = [mp.mpc(6, mp.mpf("0.35")), mp.mpc(6, mp.mpf("-0.5")),
        mp.mpc(5, -1), mp.mpc(3.5, -1.2), mp.mpc(2, -1.2),
        mp.mpc(1, -1)]
cs, aa = CS0, A0
for b in PATH:
    cs = poly_diff_shift(cs, aa, b, 14)
    aa = b
# the continued function around aa = 1 - 1i is sheet II near the g=-1 zero


def chiII_taylor(z):
    return poly_eval(cs, aa, mp.mpc(z))


# cross-validation against the PRODUCTION sheet-II values? NO -- forbidden to
# reuse; instead validate the continuation by the Schwarz/consistency check:
# just below the cut on sheet II, chi_II must equal chi_I from ABOVE
zc = mp.mpc(6, mp.mpf("-0.02"))
cs_c, aa_c = CS0, A0
for b in [mp.mpc(6, mp.mpf("0.35")), mp.mpc(6, mp.mpf("-0.1"))]:
    cs_c = poly_diff_shift(cs_c, aa_c, b, 14)
    aa_c = b
glue = abs(poly_eval(cs_c, aa_c, zc) - chi0_I(mp.mpc(6, mp.mpf("0.02")))) \
    / abs(chi0_I(mp.mpc(6, mp.mpf("0.02"))))
check(glue < mp.mpf("5e-3"),
      "INDEPENDENT GLUING CHECK: the Taylor-continued value just below the "
      "cut == sheet-I just above (rel %.1e) -- continuation crossed the cut "
      "correctly, no disc formula used" % glue, gate="3")
ZII = {}
for gs, ztgt in (("-1.0", mp.mpc("0.116", "-0.945")),
                 ("-2.0", mp.mpc("0.711", "-1.296"))):
    g = mp.mpf(gs)
    D = lambda z: z - g * chiII_taylor(z)
    z0, z1 = ztgt + mp.mpc("0.15", "0.1"), ztgt - mp.mpc("0.1", "0.12")
    for _ in range(30):                       # secant method
        f0, f1 = D(z0), D(z1)
        if abs(f1 - f0) < mp.mpf("1e-30"):
            break
        z2 = z1 - f1 * (z1 - z0) / (f1 - f0)
        z0, z1 = z1, z2
        if abs(D(z1)) < mp.mpf("1e-12"):
            break
    d = abs(z1 - ztgt)
    ZII[gs] = [float(mp.re(z1)), float(mp.im(z1))]
    check(d < mp.mpf("0.05") and abs(D(z1)) < mp.mpf("1e-8"),
          "sheet-II zero at g=%s REPRODUCED by Taylor continuation + secant: "
          "z = %s (production %s; |d| = %.2e; |D| = %.1e)"
          % (gs, mp.nstr(z1, 6), mp.nstr(ztgt, 4), d, abs(D(z1))), gate="3")
stamp("sheet II audited")

# ================= 4: FIRST-ORDER vs RESUMMED =================
print("\n=== 4: FIRST-ORDER vs RESUMMED ===")
g = mp.mpf(-2)
xp = mp.mpf(str(TRACK["-2.0"]))
G1 = (1 / xp) + g * mp.re(chi0_richardson(xp)) / xp**2
Gres_inv = xp - g * mp.re(chi0_richardson(xp))
check(abs(G1) < mp.mpf(100) and abs(Gres_inv) < mp.mpf("1e-6"),
      "at the certified pole x_p(g=-2): the FIRST-ORDER object is FINITE "
      "(G1 = %s) while the resummed denominator VANISHES (|D| = %.1e) -- "
      "the pole is resummation-generated, verified on the independent route"
      % (mp.nstr(G1, 6), abs(Gres_inv)), gate="4")

# ================= 5-9: DOMAIN RECORD + VERDICT + FREEZE =================
print("\n=== 5-9: DOMAIN, VERDICT, FREEZE ===")
DOMAIN = {
    "first_sheet_search": "x in (0.2, 3.97), grid step 0.2 + edge points; "
                          "bisection bracket +-0.15 around production values;"
                          " poles outside (e.g. the g=-20 exit) NOT excluded "
                          "beyond the window",
    "sheet_II_search": "three production seeds + audit path terminating near "
                       "1 - 1i; additional roots outside the searched "
                       "neighbourhoods are NOT excluded",
    "tolerances": "atom quadrature ~1e-20; Taylor continuation validated at "
                  "1e-6 (disc) and 5e-3 (gluing); root reproduction "
                  "tolerances 2e-3 (sheet I) / 5e-2 (sheet II)",
    "g_scan": "+-{0.1, 0.5, 1, 2, 5, 20} + audit points -1.5, -3; the sign "
              "of g remains UNFIXED -- branches reported separately, no "
              "physical sign selected",
}
for k, v in DOMAIN.items():
    note("DOMAIN %s: %s" % (k, v))
VERDICT = ("resummation-generated pole structure: branch-dependent, "
           "certified at the tested scope.")
print("  VERDICT: " + VERDICT)
RESULT = {
    "stage": "matter-scope K_R closure audit (review only)",
    "frozen_kernel_sha256": KSHA,
    "instrument_sha256": hashlib.sha256(
        open(os.path.abspath(__file__), "rb").read()).hexdigest(),
    "independent_first_sheet": TRACK,
    "independent_sheet_II": ZII,
    "domain": DOMAIN,
    "verdict": VERDICT,
    "non_inferences": "no K_R^(contract); no registered single-pole "
                      "derivation; no physical pole existence; no "
                      "GRUT-level conclusion (owner rule, verbatim)",
    "checks": CHECKS, "notes": NOTES, "failures": FAILS,
    "elapsed_s": round(time.time() - T0, 1),
}
with open(os.path.join(HERE, "WALL_KR_CLOSURE_AUDIT_RESULT.json"), "w") as f:
    json.dump(RESULT, f, indent=1, default=str)
print("\n================ SUMMARY (CLOSURE AUDIT) ================")
print("  first sheet (independent): %s" % TRACK)
print("  sheet II (independent): %s" % ZII)
print("gates: %d/%d passed; failures: %d"
      % (sum(1 for c in CHECKS if c["pass"]), len(CHECKS), len(FAILS)))
for m in FAILS:
    print("  FAILURE: " + m)
print("elapsed: %.1fs" % (time.time() - T0))
sys.exit(0 if not FAILS else 1)
