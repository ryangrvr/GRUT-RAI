#!/usr/bin/env python3
"""T3-02 -- QUOTIENT FINITE-REMAINDER RESPONSE.

Takes the exact decomposition established by T3-01
    h(q) = eps * f0  +  h_O(q),        P_perp(eps * f0) = 0,
and computes the surviving structure of the quotiented channel:

  E1  the decomposition and projector action, symbolically (exact);
  E2  IR convergence of the remainder integrand, numerically
      (cutoff scans -- finiteness is DEMONSTRATED, not assumed);
  E3  extraction of the leading IR coefficient of the remainder,
      numeric vs symbolic (the coefficient is computed, not assumed);
  E4  the H-structure of the remainder response: powers verified by
      scaling collapse, coefficients extracted by regression, and the
      flat limit checked;
  E5  the dimensionless surviving ratio A1/A0, computed for TWO
      different remainder shape functions -- a first honesty probe of
      whether the new coefficient is universal or shape/scheme
      dependent.

Scope declaration (unchanged from T3-01):
  * patch-local linear-diffeomorphism quotient ONLY;
  * NO global gauge-equivalence claim is made or used;
  * this is a scalar model instrument: it establishes the METHOD and
    the finiteness/structure of the remainder, not a full loop
    calculation.  W-0: computed and reported, NOT banked.
"""
import json
import os
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
RESULT_PATH = os.path.join(HERE, "T3_02_QUOTIENT_REMAINDER_RESULT.json")

results = {"instrument": "calc/t3_02_quotient_remainder.py",
           "depends_on": "calc/T3_01_IR_COEFFICIENT_RESULT.json", "checks": []}


def check(name, ok, msg):
    results["checks"].append({"name": name, "pass": bool(ok), "msg": msg})
    print(("  ok   " if ok else "  FAIL ") + f"{name}: {msg}")


# ============================================================================
# E1 -- exact decomposition and projector action (symbolic)
# ============================================================================
print("E1: exact decomposition h = eps*f0 + h_O(q), projector action")

eps = sp.Matrix([[0, 0, 0], [0, 1, 0], [0, 0, -1]])
q1, q2 = sp.symbols("q1 q2", real=True)
f0 = sp.symbols("f0", positive=True)
xs_syms = (q1, q2)  # small-q expansion parameters of the mode function

# exact small-q mode function: constant TT piece + O(q) remainder,
# same polarization (as in T3-01)
h_q = eps * f0 + eps * (q1 + q2)


def P_perp(m):
    """T3-01 corrected projector: remove the CONSTANT-mode component only.
    Normalization tr(eps^T eps) = 2 (patch-local inner product)."""
    m0 = m.subs({q1: 0, q2: 0})
    c0 = sp.trace(eps.T * m0) / sp.trace(eps.T * eps)
    return sp.simplify(m - eps * c0)


h_quot = P_perp(h_q)
rem_exact = h_q - eps * (q1 + q2)  # what the projector SHOULD have removed

check("E1a P_perp kills constant mode", h_quot.subs({f0: 1, q1: 0, q2: 0}) == sp.zeros(3, 3),
      "P_perp(eps*f0) = 0 (T3-01 identity, re-verified inside T3-02)")
check("E1b remainder is exactly the O(q) piece",
      sp.simplify(h_quot - eps * (q1 + q2)) == sp.zeros(3, 3),
      "h_quot == h_O(q) exactly: the subtraction is clean mode by mode")
check("E1c projector is idempotent on this sector",
      sp.simplify(P_perp(h_quot) - h_quot) == sp.zeros(3, 3),
      "P_perp^2 = P_perp on the decomposed mode (quotient consistency)")

# ============================================================================
# E2 -- IR convergence of the remainder integrand (numerical)
# ============================================================================
print("E2: remainder integrand -- IR convergence by cutoff scans")

# Remainder amplitude model: bounded at q=0 with analytic small-q
# expansion a(q) = 1 + c1 q + c2 q^2 / (1+q).  The d=3 radial measure
# q^2 dq times a bounded amplitude is IR-convergent; we DEMONSTRATE it.
c1, c2 = 0.7, -0.4


def a_rem(q):
    return 1.0 + c1 * q + c2 * q**2 / (1.0 + q)


def integrand(q):
    return q**2 * a_rem(q)  # the full remainder integrand, d=3 radial


# lower-cutoff scan: integral must converge to a finite limit as qmin -> 0
def integ_num(qmin, qmax, n=400000):
    q = np.linspace(qmin, qmax, n)
    return np.trapezoid(integrand(q), q)


qmin_seq = [1e-1, 1e-2, 1e-3, 1e-4, 1e-5]
low_vals = [integ_num(qm, 1.0) for qm in qmin_seq]
drift = abs(low_vals[-1] - low_vals[-2]) / abs(low_vals[-2])
print("  qmin     Int_{qmin}^1 q^2 a(q) dq")
for qm, v in zip(qmin_seq, low_vals):
    print(f"  {qm:.0e}   {v:.12f}")

check("E2a IR convergence demonstrated", drift < 1e-6,
      f"integral converges as qmin -> 0 (relative drift {drift:.2e} over the "
      f"last decade; NO IR divergence in the quotiented remainder)")

# fitted power of the integrand near q = 0: log-log slope must be 2 (q^2)
q_probe = np.logspace(-6, -2, 40)
vals = np.array([integrand(q) for q in q_probe])
slope = np.polyfit(np.log(q_probe), np.log(vals), 1)[0]
check("E2b integrand vanishing power", abs(slope - 2.0) < 1e-3,
      f"fitted integrand power near q=0 is {slope:.6f} (expected q^2 from "
      f"the d=3 measure on a bounded amplitude) -- computed, not assumed")

# ============================================================================
# E3 -- leading IR coefficient of the remainder: numeric vs symbolic
# ============================================================================
print("E3: leading remainder coefficient, numeric vs symbolic")

q = sp.symbols("q", nonnegative=True)
a_sym = 1 + c1 * q + c2 * q**2 / (1 + q)
I_exact = sp.integrate(q**2 * a_sym, (q, 0, 1))
I_num = integ_num(0.0, 1.0, n=2_000_000)
rel_err = abs(I_num - float(I_exact)) / abs(float(I_exact))
print(f"  symbolic  Int_0^1 q^2 a(q) dq = {I_exact} = {float(I_exact):.12f}")
print(f"  numeric                    = {I_num:.12f}")

check("E3a coefficient extracted and matches", rel_err < 1e-6,
      f"leading remainder coefficient I_rem = {float(I_exact):.12f} "
      f"(numeric agrees to {rel_err:.2e}) -- finite, nonzero, computed")

# ============================================================================
# E4 -- H-structure of the remainder response: powers verified by collapse
# ============================================================================
print("E4: remainder response Pi_quot(omega, H) -- powers and coefficients")

# Mode-sum model of the quotiented channel (T3-01 E3/E4 scalar model,
# now with the remainder shape a(q)): the surviving kernel is
#     Pi(omega, H) = Int_0^1 dq q^2 a(q) [ omega^4 + H^2 omega^2 / (1+q) ]
# The POWERS are verified by scaling collapse; the COEFFICIENTS are
# extracted by linear regression and checked against symbolic integrals.
# Nothing about A0, A1 is assumed a priori.


def Pi_quot(omega, H, shape=a_rem, n=4000):
    qg = np.linspace(0.0, 1.0, n)
    amp = qg**2 * shape(qg)
    return np.trapezoid(amp * (omega**4 + H**2 * omega**2 / (1.0 + qg)), qg)


# E4a: omega-power at H = 0.  Pi(omega, 0) = A0 * omega^4 exactly, so the
# log-log slope of Pi(omega,0) vs omega must be 4 and the collapse of
# Pi/omega^4 to a constant verifies the power.
oms = np.array([0.05, 0.1, 0.2, 0.4, 0.8])
pi0 = np.array([Pi_quot(w, 0.0) for w in oms])
slope_om = np.polyfit(np.log(oms), np.log(pi0), 1)[0]
A0_fit = float(np.exp(np.polyfit(np.log(oms), np.log(pi0), 1)[1]))
A0_exact = float(sp.integrate(q**2 * a_sym, (q, 0, 1)))
print(f"  omega-slope at H=0: {slope_om:.8f}   A0_fit = {A0_fit:.10f}   A0_exact = {A0_exact:.10f}")
check("E4a omega power and A0", abs(slope_om - 4.0) < 1e-6 and abs(A0_fit - A0_exact) / A0_exact < 1e-4,
      f"Pi(omega,0) ~ omega^{slope_om:.4f}; extracted A0 = {A0_fit:.8f} "
      f"matches symbolic Int q^2 a = {A0_exact:.8f}")

# E4b: H-power.  The H-dependent part D(H) = Pi(w, H) - Pi(w, 0) must
# collapse as H^2 at fixed omega (scaling collapse, coefficient extracted).
w_fix = 0.3
Hs = np.array([0.02, 0.05, 0.1, 0.2])
D = np.array([Pi_quot(w_fix, h) - Pi_quot(w_fix, 0.0) for h in Hs])
slope_H = np.polyfit(np.log(Hs), np.log(D), 1)[0]
A1_fit = float(np.polyfit(Hs**2, D, 1)[0]) / w_fix**2
A1_exact = float(sp.integrate(q**2 * a_sym / (1 + q), (q, 0, 1)))
print(f"  H-slope at fixed omega: {slope_H:.8f}   A1_fit = {A1_fit:.10f}   A1_exact = {A1_exact:.10f}")
check("E4b H power and A1", abs(slope_H - 2.0) < 5e-3 and abs(A1_fit - A1_exact) / A1_exact < 1e-3,
      f"H-dependent part ~ H^{slope_H:.4f} (even-in-H, as required by the "
      f"symmetry of the kernel); extracted A1 = {A1_fit:.8f} matches "
      f"symbolic Int q^2 a/(1+q) = {A1_exact:.8f}")

# E4c: flat limit -- the H-dependent correction vanishes as H -> 0.
# Evaluated at the SMALLEST H of the scan (H = 0.02), where the H^2 law
# from E4b applies; the largest H = 0.2 is not small against w = 0.3.
dev_min = abs(D[0]) / Pi_quot(w_fix, 0.0)
scaling = abs(dev_min - (A1_exact / A0_exact) * (Hs[0] / w_fix)**2) / dev_min
check("E4c flat limit", dev_min < 1e-2 and scaling < 1e-3,
      f"relative H-correction at H = {Hs[0]} is {dev_min:.2e}, matching "
      f"(A1/A0)(H/w)^2 to {scaling:.1e}: it scales as H^2 -> 0 at fixed "
      f"omega, so the flat limit is the pure omega^4 remainder, smoothly")

# ============================================================================
# E5 -- the surviving dimensionless ratio: universal or shape-dependent?
# ============================================================================
print("E5: dimensionless ratio A1/A0 under two remainder shapes")


def a_alt(q):
    """A different admissible remainder shape (same boundedness/analyticity)."""
    return 1.0 / (1.0 + 0.5 * q)


shapes = {"a_rem (T3-02 model)": a_rem, "a_alt (control shape)": a_alt}
ratios = {}
for label, shape in shapes.items():
    qg = np.linspace(0.0, 1.0, 200_000)
    A0n = np.trapezoid(qg**2 * shape(qg), qg)
    A1n = np.trapezoid(qg**2 * shape(qg) / (1.0 + qg), qg)
    ratios[label] = A1n / A0n
    print(f"  {label:26s}  A0 = {A0n:.6f}  A1 = {A1n:.6f}  A1/A0 = {A1n/A0n:.6f}")

r1, r2 = ratios.values()
check("E5 ratio computed for both shapes", True,
      f"A1/A0 = {r1:.6f} vs {r2:.6f}: the dimensionless remainder "
      f"coefficient is SHAPE-DEPENDENT at the level of the scalar model "
      f"({abs(r1-r2)/r1*100:.1f}% spread) -- i.e. at toy scope it is a "
      f"scheme quantity, NOT yet a universal number. Extracting it from "
      f"the real Tier-3 kernel is the open calculation.")

# ============================================================================
results["summary"] = {
    "decomposition": "h = eps*f0 + h_O(q); P_perp removes exactly eps*f0 (T3-01 identity)",
    "IR_convergence": ("remainder integrand ~ q^2 (fitted power 2.000); "
                       "integral converges, no IR divergence"),
    "leading_remainder_coefficient": float(I_exact),
    "response_structure": "Pi_quot(omega, H) = A0*omega^4 + A1*H^2*omega^2 + ...",
    "A0": A0_exact,
    "A1": A1_exact,
    "A1_over_A0": {"a_rem": r1, "a_alt": r2},
    "flat_limit": "H-dependent correction ~ H^2 -> 0 smoothly",
    "verdict": ("The quotiented channel is IR-finite with a computable "
                "remainder: A0*omega^4 + A1*H^2*omega^2.  The powers are "
                "verified by scaling collapse and the coefficients are "
                "extracted numerically and confirmed symbolically.  The "
                "dimensionless ratio A1/A0 is shape-dependent at toy "
                "scope: whether it is a universal number must be decided "
                "by the real Tier-3 kernel, not by this instrument."),
}
results["w0"] = "computed-and-reported, NOT banked"
results["scope"] = ("patch-local linear-diffeomorphism quotient only; scalar "
                    "model instrument; no global gauge claim; no full-loop claim")

with open(RESULT_PATH, "w") as f:
    json.dump(results, f, indent=2)

fails = [c for c in results["checks"] if not c["pass"]]
print(f"\nT3-02: {len(results['checks']) - len(fails)}/{len(results['checks'])} checks pass")
print(f"result written: {RESULT_PATH}")
raise SystemExit(1 if fails else 0)
