# File: calc/t3_05d_additivity_bisect.py
#!/usr/bin/env python3
"""T3-05D -- NON-ADDITIVITY BISECTION (seconds-scale, synthetic).

SCOPE (narrow, per directive): T3-05C established that the implemented
imsig_from_cone transformation is NON-ADDITIVE on correctly-phased,
phase-stripped combined cone coefficients, while isolated branch
extractions are stable and sign-symmetric.  This instrument localizes the
MINIMAL input class that triggers the non-additivity.

Design (declared before reading any number):
  * synthetic monomial cone coefficients c_n with EXACTLY the phase
    convention that P2 established as gate-passing (i^n c_n real);
  * pairwise residuals  delta_ij = I(c_i + c_j) - I(c_i) - I(c_j);
  * three-way residual delta_024;
  * u_b-free control (c_n with u_b factors removed) -- if additivity
    fails there too, the effect is fundamental to the extraction
    machinery, not tied to the frame sector;
  * ordering control I(c_i + c_j) vs I(c_j + c_i).

NOT done here: any modification of imsig_from_cone, any real-data
assembly, H^6, R', W-0.  Pure operator characterization on small inputs.
"""
import json
import os
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
RESULT_PATH = os.path.join(HERE, "T3_05D_BISECT_RESULT.json")

results = {"instrument": "calc/t3_05d_additivity_bisect.py",
           "conditional_scope": ("imsig_from_cone characterized AS "
                                 "IMPLEMENTED; no physical interpretation"),
           "checks": []}
notes = []


def note(m):
    notes.append(m)
    print("  -- " + m)


def check(name, ok, msg):
    results["checks"].append({"name": name, "pass": bool(ok), "msg": msg})
    print(("  ok   " if ok else "  FAIL ") + f"{name}: {msg}")


H = sp.Symbol("H", real=True)
ub = sp.Symbol("u_b", real=True)
D = sp.Symbol("Delta", real=True)
q = sp.Symbol("q", positive=True)
om = sp.Symbol("omega", positive=True)
kap = sp.Symbol("kappa", positive=True)
dsym = sp.Symbol("d", positive=True)

# ---------------------------------------------------------------- load
ic = json.load(open(os.path.join(HERE, "..", "PHYSICS_LEDGER",
                                 ".tier3_h4_integrand_cache.json")))
src = open(os.path.join(HERE, "..", "PHYSICS_LEDGER",
                        "wall_kr_tier3_loop_h4.py")).read()
i0s = src[src.find("def _exp_arg_of_factors"):src.find('if STAGE == "assemble":')]
g = {"sp": sp, "D": D, "ub": ub, "q": q, "u": sp.Symbol("u", real=True),
     "up": sp.Symbol("u_p", real=True), "om": om, "kap": kap, "dsym": dsym}
exec(i0s, g)
cone_split, imsig_from_cone = g["cone_split"], g["imsig_from_cone"]


def phased_monomial(n, sign, oub=False):
    """Delta^n monomial in the T3-05C phased convention:
    c_n D^n exp(i sign q Delta) with i^n c_n REAL (gate-passing, as P2
    established).  NOTE on signs: the classifier reads the phase as
    i q (rD Delta + rb u_b) with rD = -2 or +2; exp(sign*2*i*q*Delta)
    would be rD = -4/+4 -> STRAY (the T3-05C probe bug).  Build with
    exp(sign*i*q*Delta), sign in (-2, +2).  If oub, multiply by u_b^2."""
    base = om**(4 - n) / kap**n
    c = sp.I**n * base          # i^n c_n real
    if oub:
        c = c * ub**2
    return c * D**n * sp.exp(sp.I * sign * q * D)


def I_of(expr, sign=-2):
    """Extraction through the ACCEPTED route (per T3-05C): cone_split
    strips the phase, imsig_from_cone eats the phase-stripped coefficient.
    A bare phase-bearing expression is out of domain (P1 crash)."""
    slot = "m" if sign < 0 else "p"
    other = "p" if sign < 0 else "m"
    c = cone_split(sp.expand(expr))
    assert c["stray"] == {} and not c[other], "unexpected cone content"
    return imsig_from_cone(sp.cancel(sp.together(c[slot])))


def resid(*coeffs, sign=-2):
    """delta = I(sum c) - sum I(c) within one phase sector, normalized."""
    tot = I_of(sum(coeffs, sp.Integer(0)), sign)
    parts = [I_of(c, sign) for c in coeffs]
    return sp.expand(sp.cancel(sp.together(tot - sum(parts, sp.Integer(0)))))


# --------------------------------------------------------------- B1
print("B1: pairwise bisection (u_b-free monomials first)")
cns = {n: phased_monomial(n, -2) for n in (0, 2, 4)}
pair = {}
for a, b in [(0, 2), (0, 4), (2, 4)]:
    r = resid(cns[a], cns[b])
    pair[f"{a}{b}"] = str(r)
    note(f"delta_{a}{b} (u_b-free) = {str(r)[:120]} -> "
         f"{'NONZERO' if r != 0 else 'zero'}")
results["pairs_ub_free"] = pair

# --------------------------------------------------------------- B2
print("B2: three-way residual (u_b-free)")
r024 = resid(cns[0], cns[2], cns[4])
note(f"delta_024 (u_b-free) = {str(r024)[:120]}")
results["triple_ub_free"] = str(r024)

# --------------------------------------------------------------- B3
print("B3: u_b^2-carrying monomials")
cns_ub = {n: phased_monomial(n, -2, oub=True) for n in (0, 2, 4)}
pair_ub = {}
for a, b in [(0, 2), (0, 4), (2, 4)]:
    r = resid(cns_ub[a], cns_ub[b])
    pair_ub[f"{a}{b}"] = str(r)
    note(f"delta_{a}{b} (u_b^2) = {str(r)[:120]} -> "
         f"{'NONZERO' if r != 0 else 'zero'}")
results["pairs_ub2"] = pair_ub

# --------------------------------------------------------------- B4
print("B4: ordering control")
r01 = resid(cns[0], cns[2])
r10 = resid(cns[2], cns[0])
check("B4a ordering-independent", sp.simplify(r01 - r10) == 0,
      "delta_02(0,2) - delta_02(2,0) = %s" % sp.simplify(r01 - r10))

# --------------------------------------------------------------- B5
print("B5: minimal trigger search -- is the failure present with a PAIR?")
any_pair = any(sp.sympify(v) != 0 for v in list(pair.values()) + list(pair_ub.values()))
results["minimal_trigger"] = {
    "pair_level": any_pair,
    "triple_level": r024 != 0,
}
if any_pair:
    nz = [k for k, v in {**pair, **pair_ub}.items() if sp.sympify(v) != 0]
    note(f"non-additivity fires at PAIR level, first at: {nz[0]}")
else:
    note("all pairs additive; non-additivity is COLLECTIVE (needs >=3 terms)")

# ---------------------------------------------------------- record
results["notes"] = notes
results["w0"] = "computed-and-reported, NOT banked"
results["scope"] = ("synthetic bisection ONLY; imsig_from_cone untouched; "
                    "no real-data assembly; no H^6; R' untouched")
with open(RESULT_PATH, "w") as f:
    json.dump(results, f, indent=2)

print(f"\nT3-05D: {len(results['checks']) - len([c for c in results['checks'] if not c['pass']])}/{len(results['checks'])} checks pass")
print(f"result written: {RESULT_PATH}")
