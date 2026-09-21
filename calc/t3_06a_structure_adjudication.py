#!/usr/bin/env python3
"""T3-06A -- STRUCTURE ADJUDICATION OF THE u_b DEPENDENCE (pre-keystone).

Chain position (owner directive): ... -> assembled H^4 contribution ->
[THIS: what the three computed orders jointly say about the u_b
structure] -> Sigma -> G_R^TT if warranted.

INPUT RECORD (quoted; no new loop computation):
  A0: Im Sigma_R^{H0} = -(3/1280 pi) omega^4
      (WALL_KR_CONTRACT_RETARDED_VERDICT.md line 36; independent-route +
       numeric-quadrature convicted, WALL_KR_TIER3_FLAT_RESULT.json)
  A1: Im Sigma_R^{H2} = -(13/480 pi) H^2 omega^2, u_b-FREE
      (same verdict line; the frozen instrument gates every H^1/H^2 cone
       coefficient u_b-free -- WALL_KR_TIER3_LOOP_RESULT.json)
  A2: Im Sigma_R^{H4} = (-18 w^4 u_b^4 + 220 w^2 u_b^2 - 127) H^4
      /(1280 pi)  [d = 3]
      (T3_05_H4_SECTOR_RESULT.json; provenance closed T3-05G; partition
       closed T3-05K2; completeness at Im(omega>0) closed T3-05L)
  Domain: the record's own validity boundary eps_H = (104/9) H^2/omega^2
      (WALL_KR_CONTRACT_RETARDED_VERDICT.md line 56) -- everything below
      lives in the omega >> H expansion domain.

QUESTION (narrow): in dimensionless variables x = H u_b, y = H/omega,
the record is Im Sigma = (omega^4/1280 pi) P(x, y) with
    P = -3 - (104/3) y^2 - 18 x^4 + 220 x^2 y^2 - 127 y^4 + O(H^6).
Which DRESSED-STATIONARY model classes -- the flat stationary law
carried through an amplitude dressing and/or a frequency redshift that
depend on the Wigner time only through x -- are consistent with P?

  C1 FACTORIZED AMPLITUDE:  Im Sigma = F(x) (omega^4/1280 pi) S(y)
  C2 FREQUENCY REDSHIFT:    Im Sigma = (w~^4/1280 pi) T(H/w~),
                            w~ = omega g(x)
  C3 COMBINED:              Im Sigma = F(x) (w~^4/1280 pi) T(H/w~)

with F, g analytic (F(0) = g(0) = 1) and S, T arbitrary through the
matched order.  Each class is expanded EXACTLY to total order 4 in
(x, y) and matched against every monomial coefficient of P, including
the zero ones (no x^2, no odd powers).  A class is REFUTED only by an
inconsistent linear/polynomial system; a class that admits a fit has
its parameters recorded VERBATIM -- admission is an existence statement
at O(H^4), NOT a derivation, and the decisive over-constraint test at
H^6 is named, not computed.

Predeclared outcome classes (exactly one):
  ALL_DRESSING_CLASSES_REFUTED
      -> no amplitude/redshift dressing of the stationary flat law
         reproduces the computed orders: the u_b dependence is
         GENUINELY NONSTATIONARY at O(H^4) evidence level.
  DRESSED_STATIONARY_ADMITTED
      -> the widest class (C3) fits all computed data; parameters
         recorded; H^6 named as the decisive over-constraint.
  MIXED
      -> some classes refuted, some admit; per-class record decides
         what survives.
  INDETERMINATE
      -> a solve fails to terminate/classify; partial record filed.

Scope fences: pure coefficient arithmetic on the quoted record; no new
loop integral; no keystone resummation; no observable claim; no R'; no
H^6 computation; frozen artifacts read-only; W-0: computed-and-reported,
NOT banked.  An admitted fit is NOT evidence the dressing is physical --
it is an unfalsified-at-this-order statement, priced accordingly.
"""
import json
import os
import time

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
RESULT_PATH = os.path.join(HERE, "T3_06A_STRUCTURE_ADJUDICATION_RESULT.json")
T0 = time.time()
results = {"instrument": "calc/t3_06a_structure_adjudication.py",
           "question": ("which dressed-stationary model classes are "
                        "consistent with the computed H^0/H^2/H^4 "
                        "record of Im Sigma_R(omega > 0)?"),
           "checks": [], "notes": [],
           "w0": "computed-and-reported, NOT banked"}


def check(name, ok, msg):
    results["checks"].append({"name": name, "pass": bool(ok), "msg": msg})
    print(("  ok   " if ok else "  FAIL ") + f"{name}: {msg}", flush=True)


def note(m):
    results["notes"].append(m)
    print("  -- " + m, flush=True)


om, ub, H = sp.symbols("omega u_b H", positive=True, real=True)
x, y = sp.symbols("x y", real=True)   # x = H u_b, y = H/omega
eps = sp.Symbol("epsilon", positive=True)

# ---------------------------------------------------- the record -> P
A0 = -sp.Rational(3, 1280) / sp.pi * om**4
A1 = -sp.Rational(13, 480) / sp.pi * om**2          # x H^2
A2 = (-18 * om**4 * ub**4 + 220 * om**2 * ub**2 - 127) / (1280 * sp.pi)
IM = A0 + A1 * H**2 + A2 * H**4
P_target = (-3 - sp.Rational(104, 3) * y**2
            - 18 * x**4 + 220 * x**2 * y**2 - 127 * y**4)
recon = (om**4 / (1280 * sp.pi)) * P_target.subs(
    {x: H * ub, y: H / om})
check("R0 dimensionless assembly exact",
      sp.simplify(sp.expand(IM - recon)) == 0,
      "A0 + A1 H^2 + A2 H^4 == (omega^4/1280 pi) P(x, y) with "
      "P = -3 - (104/3) y^2 - 18 x^4 + 220 x^2 y^2 - 127 y^4 -- "
      "and (13/480)/(3/1280) = 104/9 reproduces the record's own "
      "validity coefficient eps_H (WALL_KR_CONTRACT_RETARDED_VERDICT "
      "line 56, ROOT1_KERNEL_ORIGIN line 67)")

# grade by total order: x -> eps*x, y -> eps*y; keep through eps^4
def grade4(expr):
    e = sp.expand(expr.subs({x: eps * x, y: eps * y}))
    e = sp.series(e, eps, 0, 5).removeO()
    return sp.expand(e.subs(eps, 1))


TARGET = sp.expand(P_target)
MONOMIALS = [(a, b) for a in range(0, 5) for b in range(0, 5) if a + b <= 4]


def match_system(model_expr, params):
    """Coefficient-match model against TARGET on every monomial of total
    order <= 4 (zero coefficients included). Returns (solutions, eqs)."""
    diff = sp.expand(grade4(model_expr) - TARGET)
    eqs = []
    for a, b in MONOMIALS:
        c = diff.coeff(x, a).coeff(y, b)
        if c != 0 or True:
            eqs.append(sp.Eq(sp.nsimplify(c), 0))
    sols = sp.solve(eqs, params, dict=True)
    return sols, eqs


# ------------------------------------------------- C1: factorized
print("\n== C1: factorized amplitude F(x) * S(y) ==")
f1, f2, f3, f4 = sp.symbols("f1 f2 f3 f4", real=True)
s0, s1, s2, s3, s4 = sp.symbols("s0 s1 s2 s3 s4", real=True)
F = 1 + f1 * x + f2 * x**2 + f3 * x**3 + f4 * x**4
S = s0 + s1 * y + s2 * y**2 + s3 * y**3 + s4 * y**4
sols1, _ = match_system(F * S, [f1, f2, f3, f4, s0, s1, s2, s3, s4])
c1_refuted = (sols1 == [])
check("C1 factorized class adjudicated", True,
      "REFUTED (no solution)" if c1_refuted
      else f"ADMITS FIT: {sols1[:2]}")
if c1_refuted:
    # minimal certificate, verified: s0 = -3 (order 0); x^2: f2 s0 = 0
    # => f2 = 0; x^2 y^2: f2 s2 = 220 => 0 = 220, contradiction.
    cert = [sp.Eq(s0, -3), sp.Eq(f2 * s0, 0),
            sp.Eq(f2 * (-sp.Rational(104, 3)), 220)]
    csol = sp.solve([cert[0], cert[1]], [s0, f2], dict=True)
    cert_ok = (len(csol) == 1 and csol[0][s0] == -3
               and csol[0][f2] == 0
               and cert[2].lhs.subs(csol[0]) != cert[2].rhs)
    check("C1 refutation certificate verified", cert_ok,
          "s0 = -3 (flat), x^2 coefficient f2*s0 = 0 forces f2 = 0 "
          "(the u_b-free H^2 sector), then x^2 y^2 = f2*s2 = 0 != 220: "
          "the mixed term is unreachable by ANY factorized dressing")
results["C1"] = {"class": "F(x) * S(y)",
                 "verdict": "REFUTED" if c1_refuted else "ADMITS_FIT",
                 "solutions": [str(s) for s in sols1[:4]]}

# ------------------------------------------------- C2: pure redshift
print("\n== C2: frequency redshift (w~/w)^4 T(H/w~), w~ = w g(x) ==")
g1, g2, g3, g4 = sp.symbols("g1 g2 g3 g4", real=True)
t0, t1, t2, t3, t4 = sp.symbols("t0 t1 t2 t3 t4", real=True)
gx = 1 + g1 * x + g2 * x**2 + g3 * x**3 + g4 * x**4
z = y / gx                                    # H/w~ = y/g(x)
T = t0 + t1 * z + t2 * z**2 + t3 * z**3 + t4 * z**4
model2 = gx**4 * T                            # (w~^4/w^4) T(H/w~)
sols2, _ = match_system(model2, [g1, g2, g3, g4, t0, t1, t2, t3, t4])
c2_refuted = (sols2 == [])
check("C2 redshift class adjudicated", True,
      "REFUTED (no solution)" if c2_refuted
      else f"ADMITS FIT: {sols2[:2]}")
results["C2"] = {"class": "g(x)^4 T(y/g(x))",
                 "verdict": "REFUTED" if c2_refuted else "ADMITS_FIT",
                 "solutions": [str(s) for s in sols2[:4]]}

# ------------------------------------------------- C3: combined
print("\n== C3: combined F(x) * g(x)^4 T(H/w~) ==")
model3 = F * gx**4 * T
sols3, _ = match_system(
    model3, [f1, f2, f3, f4, g1, g2, g3, g4, t0, t1, t2, t3, t4])
c3_refuted = (sols3 == [])
if not c3_refuted:
    # verify a representative solution by exact re-expansion
    rep = sols3[0]
    ver = sp.expand(grade4(model3.subs(rep)) - TARGET) == 0
    check("C3 combined class adjudicated + fit re-verified", ver,
          f"ADMITS FIT (existence at O(H^4), NOT a derivation): "
          f"representative solution {rep}")
else:
    check("C3 combined class adjudicated", True, "REFUTED (no solution)")
results["C3"] = {"class": "F(x) * g(x)^4 T(y/g(x))",
                 "verdict": "REFUTED" if c3_refuted else "ADMITS_FIT",
                 "solutions": [str(s) for s in sols3[:6]],
                 "n_solutions": len(sols3),
                 "parameter_counting_caveat": (
                     "at O(H^4) the even sector has 7 free parameters "
                     "(t0,t2,t4,f2,f4,g2,g4) against 6 monomial "
                     "equations: admission is GUARANTEED by counting "
                     "for generic data and carries no evidential "
                     "weight at this order.  The content is (i) the "
                     "REFUTATION of the narrower C1/C2 classes and "
                     "(ii) the fitted structure -- T(y) equals the "
                     "u_b-free sector exactly (t0,t2,t4 = -3, -104/3, "
                     "-127), the amplitude satisfies F g^4 = 1 + "
                     "O(x^4) (f2 = -4 g2), and g2 = 165/52 -- which "
                     "becomes falsifiable at H^6 (fixes the remaining "
                     "freedom) and overconstrained at H^8.")}

# ------------------------------------------------- classification
if c1_refuted and c2_refuted and c3_refuted:
    classification = "ALL_DRESSING_CLASSES_REFUTED"
elif not c3_refuted:
    classification = ("DRESSED_STATIONARY_ADMITTED" if (c1_refuted or
                      c2_refuted) else "DRESSED_STATIONARY_ADMITTED")
    if c1_refuted or c2_refuted:
        classification = "MIXED" if (c1_refuted != c2_refuted or True) \
            else classification
    # naming rule: C3 admitting while narrower classes are refuted is
    # the MIXED outcome; pure admission everywhere would be
    # DRESSED_STATIONARY_ADMITTED
    if c1_refuted or c2_refuted:
        classification = "MIXED"
    else:
        classification = "DRESSED_STATIONARY_ADMITTED"
else:
    classification = "MIXED"
results["classification"] = classification
results["interpretation"] = {
    "REFUTED_classes": [k for k, v in
                        [("C1", c1_refuted), ("C2", c2_refuted),
                         ("C3", c3_refuted)] if v],
    "meaning": ("A refuted class means: no dressing of that shape "
                "applied to the stationary flat law reproduces the "
                "computed H^0/H^2/H^4 coefficients -- order-H^4 "
                "evidence, not a theorem beyond the matched order.  An "
                "admitted class is an existence statement whose "
                "decisive over-constraint test is the H^6 sector "
                "(named, not computed).  Either way the u_b terms are "
                "properties of the complete Im Sigma_R(omega>0) "
                "(T3-05L) inside the record's own validity domain "
                "omega >> H (eps_H = (104/9) H^2/omega^2)."),
    "keystone_bearing": ("The keystone (Sigma -> G_R^TT) inherits this "
                         "adjudication: if MIXED/ADMITTED, the fitted "
                         "F, g, T define a candidate stationary frame "
                         "for the resummation whose H^6 test is the "
                         "falsifier; if ALL REFUTED, no stationary "
                         "frame exists in the dressing sense and the "
                         "two-time structure must be carried "
                         "explicitly."),
}
results["fences"] = ("pure coefficient arithmetic on the quoted record; "
                     "no new loop integral; no keystone; no observable "
                     "claim; no R'; no H^6 computation; W-0")
results["elapsed_s"] = round(time.time() - T0, 1)
json.dump(results, open(RESULT_PATH, "w"), indent=1)
print(f"\nCLASSIFICATION: {classification}")
print(f"wrote {RESULT_PATH}")
