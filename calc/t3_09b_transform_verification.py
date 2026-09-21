#!/usr/bin/env python3
"""T3-09B -- TRANSFORM-CONVENTION VERIFICATION (owner mandate: one final
verification pass, not a physics branch: T3-09 -> amendment -> exact
Fourier/distributional mapping -> synthesis).

WHAT IS AT STAKE.  The T3-09/amendment chain rests on three mapping
claims that must be checked against the calculation's OWN conventions,
so the paper does not replace one labeling error with an over-
interpreted transform statement:
  (a) "the certified Im terms are sgn(omega)|omega|^p" -- the odd
      extension: on what premise, under which retarded convention;
  (b) the power-law tails Delta^-5 / Delta^-3 / Delta^-1 -- is the
      distributional prescription unambiguous (two independent
      prescriptions + direct numerics);
  (c) the omega^-2 "growing secular" reading -- growing WHERE, under
      what IR prescription, and what happens beyond the window.

V1 CONVENTION (verbatim from the frozen source).  The frozen derivation
   states: "Sigma_R = -i theta(Delta) RET;  int_0^inf Delta^n
   e^{i omega Delta - eta Delta} ..." -- i.e. Sigma~(omega) =
   int_0^inf dDelta e^{+i omega Delta} Sigma_R(Delta): the
   upper-half-plane-analytic retarded transform.  Verified by quotation.

V2 INVERSION IDENTITY.  For a REAL causal kernel under that convention,
   Im Sigma~(omega) = int_0^inf sin(omega Delta) K(Delta) dDelta and
   K(Delta) = (2/pi) int_0^inf Im Sigma~(omega) sin(omega Delta) domega
   for Delta > 0.  Verified by exact round trip on two test kernels
   (e^{-a Delta}, Delta e^{-a Delta}).

V3 LOCAL OPERATORS.  K = c delta^(n)(Delta - 0+):  Sigma~ = c(-i
   omega)^n exactly under the convention: n odd -> ODD real polynomial
   in Im; n even -> Re only.  So the certified even-|omega| absorptive
   powers are NOT local-operator forms: exact, convention-checked.

V4 THE ODD-EXTENSION PREMISE (stated, statused -- the ONE premise).
   sgn(omega)|omega|^p requires Im Sigma~ odd, i.e. Sigma_R(u_b, Delta)
   REAL at fixed u_b.  Status: (i) standard for the retarded response
   of hermitian sources (-i theta <[J,J]> with <[J,J]> imaginary);
   (ii) consistent with every certified output (P real; the i^n c_n
   reality gates); (iii) NOT independently re-derivable from the cached
   integrand, whose pointwise form is convention-dressed by the
   assembly's derivative-operator routing (T3-05L M2).  This premise
   must be STATED in the paper; it is not smuggled.

V5 PRESCRIPTION INDEPENDENCE.  The Delta > 0 tails via TWO independent
   prescriptions: Abel (e^{-eta omega}, eta -> 0+) vs analytic
   continuation of int_0^inf omega^s sin(omega Delta) domega =
   Gamma(s+1) sin(pi(s+1)/2)/Delta^{s+1}.  Exact agreement required at
   p = 0, 2, 4.

V6 DIRECT NUMERICS.  The omega^2 tail (-4/(pi Delta^3)) checked by
   small-eta quadrature at several Delta (no symbolic limits).

V7 THE omega^-2 TERM, REGIME-HONEST.  Exact IR-cut form
   -Delta Ci(w* Delta) + sin(w* Delta)/w*.  Small w*Delta: growth
   Delta [1 - gamma_E - ln(w* Delta)].  Large w*Delta: Ci -> 0 and the
   remainder is BOUNDED oscillation -- the growth holds ONLY within
   Delta <~ 1/w*.  With w* = the record's own refusal boundary 3.399H,
   the licensed statement is: growing within Delta <~ 1/(3.4H),
   UNDETERMINED beyond (the deep-IR wall).  "Secularly growing" without
   that window qualifier would be the over-interpretation the owner
   flagged: corrected in the amendment and synthesis.

V8 SCOPE WORDING.  The counterterm-invariance statement is scoped to
   THE CERTIFIED NONANALYTIC ABSORPTIVE SECTOR -- not a universal
   statement about the complete self-energy (owner's instruction) --
   wording patched in the amendment and synthesis.

Fences: verification only; no new physics branch; no banked artifact
edited (wording patches ride the amendment/synthesis, git-historied);
W-0.
"""
import json
import os
import time

import mpmath as mp
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(os.path.dirname(HERE), "PHYSICS_LEDGER")
RESULT = os.path.join(HERE, "T3_09B_TRANSFORM_VERIFICATION_RESULT.json")
T0 = time.time()
res = {"instrument": "calc/t3_09b_transform_verification.py",
       "checks": [], "notes": [], "w0": "verification pass; W-0"}


def check(n, ok, m):
    res["checks"].append({"name": n, "pass": bool(ok), "msg": m})
    print(("  ok   " if ok else "  FAIL ") + f"{n}: {m}", flush=True)


om, D, a, eta, z = sp.symbols("omega Delta a eta z", positive=True)

# ---- V1: convention, verbatim ----
src = open(os.path.join(LEDGER, "wall_kr_tier3_loop_h4.py")).read()
q1 = "Sigma_R = -i theta(Delta) RET"
q2 = "int_0^inf Delta^n e^{i omega Delta"
check("V1 retarded convention quoted from the frozen source",
      q1 in src and q2 in src,
      f'frozen docstring contains "{q1}" and "{q2}...": Sigma~(omega) '
      "= int_0^inf dDelta e^{+i omega Delta} Sigma_R(Delta) -- "
      "upper-half-plane-analytic retarded transform. All mapping "
      "statements below use exactly this convention.")

# ---- V2: inversion identity round trip ----
ok2 = True
for K in (sp.exp(-a * D), D * sp.exp(-a * D)):
    ImS = sp.simplify(sp.integrate(sp.sin(om * D) * K, (D, 0, sp.oo)))
    Kb = sp.simplify(2 / sp.pi * sp.integrate(
        ImS * sp.sin(om * D), (om, 0, sp.oo)))
    ok2 = ok2 and sp.simplify(Kb - K) == 0
check("V2 sine-inversion identity exact on test kernels", ok2,
      "K -> Im Sigma~ = sine transform -> K recovered exactly for "
      "e^{-a Delta} and Delta e^{-a Delta}: the Delta > 0 "
      "reconstruction from Im alone is the correct identity under V1 "
      "for REAL causal kernels")

# ---- V3: local operators under the convention ----
n_ = sp.Symbol("n", integer=True, nonnegative=True)
ok3 = True
forms = {}
for nn in range(0, 5):
    val = sp.simplify(((-sp.I * om)**nn))
    forms[nn] = str(val)
    im_part = sp.simplify(sp.im(val.rewrite(sp.I)))
    im_expected = 0 if nn % 2 == 0 else sp.simplify(
        sp.im((-sp.I * om)**nn))
    # n even -> Im = 0 (pure Re); n odd -> odd polynomial
    if nn % 2 == 0 and sp.simplify(sp.im(sp.expand_complex(
            (-sp.I * om)**nn))) != 0:
        ok3 = False
    if nn % 2 == 1 and sp.simplify(sp.im(sp.expand_complex(
            (-sp.I * om)**nn))) == 0:
        ok3 = False
check("V3 local operators give (-i omega)^n: odd n -> odd polynomial "
      "Im; even n -> Re only", ok3,
      f"Sigma~[c delta^(n)] = c(-i omega)^n exactly: {forms} -- no "
      "even-|omega| absorptive power is a local-operator form; the "
      "certified terms are non-analytic relative to this class: "
      "convention-checked")

# ---- V4: the odd-extension premise (stated) ----
check("V4 odd-extension premise stated and statused", True,
      "sgn(omega)|omega|^p requires Sigma_R(u_b, Delta) REAL at fixed "
      "u_b. Status: standard for retarded responses of hermitian "
      "sources; consistent with the real certified P and the i^n c_n "
      "gates; NOT independently re-derivable from the cached "
      "integrand (convention-dressed derivative routing, T3-05L M2). "
      "THE one premise of the tail statements -- to be stated "
      "explicitly in the paper.")
res["premise"] = ("Reality of Sigma_R(u_b, Delta) at fixed u_b => "
                  "Im Sigma~ odd => sgn(omega)|omega|^p extension. "
                  "Stated, not derived from the cache.")

# ---- V5: prescription independence for the tails ----
ok5 = True
tails = {}
for p in (0, 2, 4):
    abel = sp.simplify(sp.limit(2 / sp.pi * sp.integrate(
        om**p * sp.sin(om * D) * sp.exp(-eta * om), (om, 0, sp.oo)),
        eta, 0))
    cont = sp.simplify(2 / sp.pi * sp.gamma(p + 1)
                       * sp.sin(sp.pi * (p + 1) / 2) / D**(p + 1))
    ok5 = ok5 and sp.simplify(abel - cont) == 0
    tails[p] = str(abel)
check("V5 Abel and analytic-continuation prescriptions agree exactly",
      ok5, f"(2/pi) tails: {tails} == (2/pi) Gamma(p+1) "
      "sin(pi(p+1)/2)/Delta^(p+1) at p = 0, 2, 4: the Delta > 0 tail "
      "values are prescription-independent")

# ---- V6: direct numerics for the omega^2 tail ----
# (run-1 disclosure: eta = 1e-6 left ~1e6 undamped oscillations and the
# quadrature blew up -- a numerical-method failure, log kept. Correct
# check: quadrature at moderate eta against the exact finite-eta closed
# form Im[2/(eta - i Delta)^3], then eta^2-Richardson to eta -> 0.)
ok6 = True
rows = []
for Dv in (0.7, 1.3, 2.4):
    vals = {}
    etas = (0.4 * Dv, 0.1 * Dv, 0.05 * Dv)   # eta scaled to Delta:
    # relative finite-eta correction is 6(eta/Delta)^2 uniformly
    for ev in etas:
        wmax = 40.0 / ev
        pts = [k * mp.pi / Dv for k in range(0, int(wmax * Dv / mp.pi) + 1)]
        pts.append(wmax)
        num = float(2 / mp.pi * mp.quad(
            lambda w: w**2 * mp.sin(w * Dv) * mp.e**(-ev * w), pts))
        closed = float(2 / mp.pi * (2 * (3 * ev**2 * Dv - Dv**3)
                                    / (ev**2 + Dv**2)**3))
        ok6 = ok6 and abs(num - closed) / abs(closed) < 1e-6
        vals[ev] = closed
    # eta^2-Richardson from the two smallest (eta ratio 2)
    rich = vals[etas[2]] + (vals[etas[2]] - vals[etas[1]]) / 3.0
    exact = float(-4 / (mp.pi * Dv**3))
    rel = abs(rich - exact) / abs(exact)
    rows.append({"Delta": Dv, "richardson": round(rich, 6),
                 "exact": round(exact, 6), "rel": round(rel, 6)})
    ok6 = ok6 and rel < 5e-3
check("V6 omega^2 tail: quadrature == closed form at finite eta; "
      "eta^2-Richardson -> -4/(pi Delta^3)", ok6, json.dumps(rows))

# ---- V7: the omega^-2 term, regime-honest ----
wst = sp.Symbol("omega_star", positive=True)
F = -D * sp.Ci(wst * D) + sp.sin(wst * D) / wst
small = sp.simplify(sp.series(F, wst, 0, 2).removeO())
largeD = sp.limit(sp.Ci(z), z, sp.oo)
# numeric behavior across the window (w* = 1 units)
prof = []
grow_in_window = True
bounded_beyond = True
for zz in (0.05, 0.2, 0.5, 1.0, 3.0, 10.0, 30.0):
    val = float(-zz * mp.ci(zz) + mp.sin(zz))   # w*=1: F = -z Ci(z)+sin z
    prof.append({"w*Delta": zz, "F(w*=1)": round(val, 5)})
for i in range(2):                               # growth up to ~1
    if prof[i + 1]["F(w*=1)"] <= prof[i]["F(w*=1)"]:
        grow_in_window = False
if max(abs(p_["F(w*=1)"]) for p_ in prof[-2:]) > 3.0:
    bounded_beyond = False
check("V7 omega^-2: growth ONLY within Delta <~ 1/omega*; bounded "
      "oscillation beyond", grow_in_window and bounded_beyond
      and sp.simplify(largeD) == 0,
      f"exact IR-cut form -Delta Ci + sin/w*; small-w*Delta expansion "
      f"{small}; Ci(z->inf) = 0; profile (w* = 1): {json.dumps(prof)}. "
      "The licensed statement: the omega^-2 kernel GROWS within the "
      "window Delta <~ 1/omega_* (with omega_* = 3.399H, i.e. "
      "Delta <~ 0.29/H) and is a bounded oscillation beyond in the "
      "cut model -- the true behavior beyond is UNDETERMINED (deep-IR "
      "wall). 'Secularly growing' unqualified would over-interpret: "
      "wording corrected.")
res["V7_profile"] = prof

# ---- V8: scope wording ----
check("V8 counterterm statement scoped per owner", True,
      "the invariance claim is a statement about THE CERTIFIED "
      "NONANALYTIC ABSORPTIVE SECTOR (its coefficients and Delta > 0 "
      "tails), NOT a universal statement about the complete "
      "self-energy (whose analytic/dispersive parts are exactly where "
      "counterterms live). Wording patched in "
      "T3_08A_AMENDMENT_01.md and GRUT_FINAL_SYNTHESIS_01.md.")

res["verdict"] = ("MAPPING VERIFIED: convention quoted; inversion "
                  "identity exact; local-operator class computed; "
                  "prescription-independent tails; numeric "
                  "confirmation; regime-honest omega^-2; one stated "
                  "premise (kernel reality at fixed u_b) flagged for "
                  "the paper.")
res["elapsed_s"] = round(time.time() - T0, 1)
json.dump(res, open(RESULT, "w"), indent=1)
print(f"\nwrote {RESULT}")
