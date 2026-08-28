#!/usr/bin/env python3
"""F1 LOCALITY-PREDICATE SCOPE CONFLICT -- standalone diagnostic for owner adjudication.

THE CONFLICT.
  FROZEN A3 (checker-amended, 2026-08-25):  local <=> polynomial in (omega^2, k^2),
      coefficients arbitrary finite functions of (m^2, H^2, mu).
  PHASE-12 IMPLEMENTATION:                  local <=> polynomial in (omega, k),
      justified because the corrected action-functional Hessians contain mixed-odd
      structures such as omega*k.
This is a SUBSTANTIVE predicate change, made after seeing the pole output. It is NOT
adjudicated here. This instrument only exhibits the mathematics so the owner can rule.

PROVENANCE, stated plainly: the frozen (omega^2, k^2) form was written by the CHECKER at
the A3 freeze gate. If it is too narrow, that is a checker defect, not a builder liberty.
"""
import sympy as sp
import json, os, sys

FAIL = []
def ck(c, m):
    print(("  ok   " if c else "  FAIL ") + m)
    if not c: FAIL.append(m)
    return c

om, kk, mm, t, z = sp.symbols('omega k m t z', real=True)
print("=== 1. AN EXPLICITLY LOCAL FINITE-DERIVATIVE KERNEL CONTAINING omega*k ===")
# Position space: a finite sum of derivatives of delta is LOCAL by definition (support
# only at coincidence). Take L(x) = A d_t d_z delta(x) + B d_t^2 delta + C delta.
# Fourier with d_t -> -i om, d_z -> -i k  (the machinery's convention):
A_, B_, C_ = sp.symbols('A B C')
K_local_mixed = A_*(-sp.I*om)*(-sp.I*kk) + B_*(-sp.I*om)**2 + C_
K_local_mixed = sp.expand(K_local_mixed)
print(f"   K_local(om,k) = {K_local_mixed}")
print("   position-space preimage: A d_t d_z delta + B d_t^2 delta + C delta")
print("   -> SUPPORT AT COINCIDENCE ONLY, hence LOCAL by the definition of locality.")
ck(sp.expand(K_local_mixed).has(om*kk),
   "1: the kernel genuinely contains a MIXED-ODD om*k term")

print("\n=== 2. EXPLICITLY NONLOCAL STRUCTURES IN THE SAME VARIABLES ===")
NONLOCAL = {"log branch cut": sp.log(om**2 + mm**2),
            "inverse power":  om**4 / kk**2,
            "arctan":         sp.atan(om / mm),
            "mixed log":      om*kk*sp.log(om**2 + kk**2)}
for n_, e_ in NONLOCAL.items():
    print(f"   {n_:16s}: {e_}")

print("\n=== 3./4. CLASSIFICATION UNDER BOTH PREDICATES ===")
def is_poly_in(expr, gens):
    try:
        p = sp.Poly(sp.expand(expr), *gens)
        return all(all(isinstance(e, int) or e.is_Integer for e in mo) for mo in p.monoms())
    except (sp.PolynomialError, sp.GeneratorsNeeded, TypeError):
        return False

def literal_F1(expr):      # frozen: polynomial in (om^2, k^2)
    w2, k2 = sp.symbols('w2 k2', positive=True)
    sub = sp.expand(expr).subs({om**2: w2, kk**2: k2})
    return is_poly_in(sub, (w2, k2)) and not sp.expand(sub).has(om) and not sp.expand(sub).has(kk)

def broadened(expr):       # implemented: polynomial in (om, k)
    return is_poly_in(expr, (om, kk))

rows = []
CASES = [("local, mixed-odd (om*k)", K_local_mixed, True),
         ("local, even only",        sp.expand(B_*om**2 + C_*kk**2), True),
         ("local, odd single (om)",  sp.expand(A_*om), True)]
CASES += [(f"NONLOCAL: {n_}", e_, False) for n_, e_ in NONLOCAL.items()]
print(f"   {'structure':28s} {'truly local?':13s} {'literal F1':11s} {'broadened':10s}")
for nm, ex, truly in CASES:
    lf, bf = literal_F1(ex), broadened(ex)
    rows.append(dict(structure=nm, truly_local=truly, literal_F1=bool(lf), broadened=bool(bf)))
    print(f"   {nm:28s} {str(truly):13s} {str(lf):11s} {str(bf):10s}")

print("\n=== 5. DOES EITHER RULE COINCIDE WITH MATHEMATICAL LOCALITY? ===")
print("   DEFINITION USED: a momentum-space kernel is LOCAL iff its position-space")
print("   preimage is a FINITE SUM OF DERIVATIVES OF delta (support at coincidence).")
print("   Fourier fact: that class is EXACTLY the polynomials in the momentum")
print("   components -- each monomial om^a k^b is the transform of")
print("   (i d_t)^a (i d_z)^b delta. No parity restriction appears anywhere.")
lit_fn = [r for r in rows if r['truly_local'] and not r['literal_F1']]
lit_fp = [r for r in rows if not r['truly_local'] and r['literal_F1']]
br_fn  = [r for r in rows if r['truly_local'] and not r['broadened']]
br_fp  = [r for r in rows if not r['truly_local'] and r['broadened']]
ck(len(lit_fn) > 0,
   f"5a: the LITERAL predicate has FALSE NEGATIVES -- it calls {len(lit_fn)} genuinely "
   f"LOCAL kernel(s) nonlocal: {[r['structure'] for r in lit_fn]}")
ck(len(br_fn) == 0 and len(br_fp) == 0,
   "5b: the BROADENED predicate has neither false negatives nor false positives on this "
   "census -- it coincides with mathematical locality")
ck(len(lit_fp) == 0,
   "5c: the literal predicate admits NO nonlocal structure (it errs only by being too "
   "narrow, never too permissive)")
print("\n   CONSEQUENCE (stated, NOT adjudicated): the broadened rule does not WEAKEN the")
print("   nonlocal side -- every nonlocal structure fails BOTH predicates. The literal")
print("   rule's defect is one-sided: it would misclassify a genuinely local mixed-odd")
print("   kernel as nonlocal, i.e. it would FORBID subtracting a real counterterm.")
print("   WHY THE NARROW FORM WAS WRITTEN: on a parity-even, Lorentz-invariant flat")
print("   background only even powers arise, so (om^2, k^2) is sufficient THERE. A")
print("   background with a preferred time direction and a reference slice admits")
print("   d_t d_z structures, so the restriction is not general.")
print("\n   THE RISK THE OWNER MUST WEIGH: broadening a locality criterion AFTER seeing")
print("   the pole output is exactly the move preregistration exists to prevent. The")
print("   mathematics above is independent of the Phase-12 output, but the TIMING is not.")

json.dump({"instrument": "f1_locality_predicate_diagnostic.py",
           "status": "FOR OWNER ADJUDICATION -- no amendment made",
           "frozen_F1": "polynomial in (omega^2, k^2)",
           "implemented": "polynomial in (omega, k)",
           "census": rows,
           "literal_false_negatives": [r['structure'] for r in lit_fn],
           "literal_false_positives": [r['structure'] for r in lit_fp],
           "broadened_false_negatives": [r['structure'] for r in br_fn],
           "broadened_false_positives": [r['structure'] for r in br_fp],
           "provenance": "the frozen (omega^2,k^2) form was written by the CHECKER at the "
                         "A3 freeze gate; if too narrow that is a checker defect",
           "fail_count": len(FAIL)},
          open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "F1_LOCALITY_DIAGNOSTIC_RESULT.json"), "w"), indent=2)
print(f"\n[FAIL count = {len(FAIL)}]")
sys.exit(0 if not FAIL else 1)
