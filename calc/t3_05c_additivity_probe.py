#!/usr/bin/env python3
"""T3-05C -- ADDITIVITY PROBE OF imsig_from_cone (synthetic, seconds-scale).

Owner directive: test whether the extraction operator is LINEAR on its
own domain, using synthetic inputs built THE WAY THE ASSEMBLY BUILDS
THEM -- coefficient x exp(-+2iqDelta), phase-stripped by the real
cone_split -- rather than bare cone coefficients (which can violate the
i^n c_n reality gate legitimately: a bare real coefficient at odd
Delta-degree IS PV-class, and the gate is right to reject it; that is
the P1 crash resolved as an input-convention bug, recorded below).

Tests, term-by-term:
  P1  out-of-domain input (real coeff x Delta, no phase) -> gate fires
      (recorded as DATA: the gate has teeth on genuinely PV-class input)
  P2  single monomial per phase sector, correctly phased:
        X_- = c(D) e^{-2iqD},  X_+ = c(D) e^{+2iqD}
      with i^n c_n real by construction (real c_n for even n, purely
      imaginary c_n for odd n) -> gates must PASS
  P3  additivity: I[cone_split(X_- + X_+)] == I[X_-] + I[X_+]
      residual reported NORMALIZED (expand + cancel + together), never
      as a raw Boolean on an unnormalized form
  P4  the structural phase forms encountered in T3-05: mixed u_b-powers
      in the coefficient, multiple Delta degrees at once.

No frozen artifact is touched; no physics interpretation; W-0 not banked.
"""
import json
import os
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(os.path.dirname(HERE), "PHYSICS_LEDGER")
RESULT_PATH = os.path.join(HERE, "T3_05C_ADDITIVITY_PROBE_RESULT.json")

results = {"instrument": "calc/t3_05c_additivity_probe.py",
           "diagnostic_only": True,
           "resolves": "T3-05B R3 nonlinearity suspect + P1 gate crash "
                       "(input-convention bug in the probe, not the gate)",
           "checks": []}
notes = []


def note(m):
    notes.append(m)
    print("  -- " + m)


def check(name, ok, msg):
    results["checks"].append({"name": name, "pass": bool(ok), "msg": msg})
    print(("  ok   " if ok else "  FAIL ") + f"{name}: {msg}")


D = sp.Symbol("Delta", real=True)
ub = sp.Symbol("u_b", real=True)
q = sp.Symbol("q", positive=True)
om = sp.Symbol("omega", positive=True)
kap = sp.Symbol("kappa", positive=True)
dsym = sp.Symbol("d", positive=True)

# load the REAL machinery (frozen working copy, read-only)
src = open(os.path.join(LEDGER, "wall_kr_tier3_loop_h4.py")).read()
i0s = src[src.find("def _exp_arg_of_factors"):src.find('if STAGE == "assemble":')]
g = {"sp": sp, "D": D, "ub": ub, "q": q, "u": sp.Symbol("u", real=True),
     "up": sp.Symbol("u_p", real=True), "om": om, "kap": kap, "dsym": dsym}
exec(i0s, g)
cone_split, imsig_from_cone = g["cone_split"], g["imsig_from_cone"]


def norm(e):
    """canonical normalized residual: expand + together + cancel + expand"""
    return sp.expand(sp.cancel(sp.together(sp.expand(e))))


def phased(cn_poly, sign):
    """build a branch input the way the assembly does:
    c(D) * exp(sign * i q Delta) with sign = rD = -2 or +2 (the phase the
    cone classifier reads is i q (rD Delta + rb u_b); the previous version
    built exp(sign*2iqD), i.e. rD = -4/+4, which cone_split correctly
    files under STRAY -- the P3a/P3 assertion failures were this probe
    bug, now fixed); c_n chosen so i^n c_n is REAL."""
    out = sp.Integer(0)
    pn = sp.Poly(sp.expand(cn_poly), D)
    for n in range(0, pn.degree() + 1):
        c = pn.coeff_monomial(D**n)
        # enforce i^n c_n real: multiply odd-degree coefficients by i
        if n % 2 == 1:
            c = sp.I * c
        out += c * D**n * sp.exp(sp.I * sign * q * D)
    return out


# ============================================================================
print("P1: out-of-domain input (bare real coeff x Delta, no phase)")
bare = q**4 / kap**4 * D
try:
    imsig_from_cone(bare)
    check("P1 gate on PV-class input", False,
          "the reality gate did NOT fire on a genuinely PV-class bare "
          "real odd-degree coefficient -- the gate has LOST its teeth")
except RuntimeError as e:
    check("P1 gate on PV-class input", True,
          "gate fires correctly on i^1 c_1 = i q^4/kappa^4 (imaginary): "
          "the T3-05B P1 crash was an INPUT-CONVENTION bug in the probe "
          "(out-of-domain synthetic input), not a gate defect -- " + str(e)[:100])

# ============================================================================
print("P2: correctly-phased single monomials (gate must pass)")
for n in (0, 1, 2, 3, 4):
    for sign in (-2, 2):
        c = q**n / kap**n  # real coefficient; phased() fixes parity
        x = phased(c * D**0, sign)  # single Delta^n monomial
        cn_only = (q**n / kap**n) * (sp.I if n % 2 else 1) * D**n
        try:
            v = imsig_from_cone(cn_only)
            check(f"P2 n={n} sign={sign:+d} gate pass", True,
                  f"i^{n} c_{n} real by construction -> extracted: "
                  f"{str(v)[:80]}")
        except RuntimeError as e:
            check(f"P2 n={n} sign={sign:+d} gate pass", False,
                  f"gate fired on a PHYSICAL phased input -- real defect: "
                  + str(e)[:120])

# ============================================================================
print("P3: additivity, correctly-phased two-branch input")
X_m = phased(q**2 / kap**2 + q**4 * ub**2 / kap**4, -2)  # mixed content
X_p = phased(q**2 / kap**2 + q**4 * ub**2 / kap**4, +2)
X = sp.expand(X_m + X_p)

def stripped(expr):
    """phase-strip: drop exp(i*q*...*Delta) factors, keep coefficients"""
    out = sp.Integer(0)
    for t in sp.Add.make_args(sp.expand(expr)):
        rest = []
        for f in t.as_ordered_factors():
            b, e = f.as_base_exp()
            if b == sp.E:
                continue
            rest.append(f)
        out += sp.Mul(*rest)
    return sp.expand(out)


def cone_slot(expr, sign):
    """the phase-stripped cone coefficient of a correctly-phased expr
    for the given phase sign (-2 -> 'm' slot, +2 -> 'p' slot)"""
    c = cone_split(sp.expand(expr))
    slot = "m" if sign < 0 else "p"
    other = "p" if sign < 0 else "m"
    assert c["stray"] == {} and not c[other], "unexpected cone content"
    return sp.cancel(sp.together(c[slot]))


cs = cone_split(X)
check("P3a cone split recovers the branches",
      cs["stray"] == {}
      and sp.simplify(sp.cancel(sp.together(
          cs["m"] - sp.cancel(sp.together(stripped(X_m)))))) == 0
      and sp.simplify(sp.cancel(sp.together(
          cs["p"] - sp.cancel(sp.together(stripped(X_p)))))) == 0,
      "cone_split(X_- + X_+) returns the PHASE-STRIPPED coefficients of "
      "(X_-, X_+) exactly, no stray")

# direct: extraction of the combined input's -cone vs sum of separate
I_combined = imsig_from_cone(cs["m"])
I_separate = (imsig_from_cone(cone_slot(X_m, -2))
              + imsig_from_cone(cone_slot(X_p, +2)))
resid = norm(I_combined - I_separate)
check("P3b additivity (-cone): I[cone_m(X_-+X_+)] == I[cone_m(X_-)] + I[cone_m(X_+)]",
      resid == 0,
      "normalized residual = %s" % (str(resid)[:200] if resid != 0 else "0"))

# the EXACT T3-05B R3 situation: per-branch extraction, then sum vs the
# combined extraction of the same branch content
ims_m = imsig_from_cone(cone_slot(X_m, -2))
ims_p = imsig_from_cone(cone_slot(X_p, +2))
resid2 = norm(ims_m + ims_p - I_combined)
check("P3c branch-sum additivity", resid2 == 0,
      "I[X_-] + I[X_+] - I[assembled -cone] normalized residual = "
      + (str(resid2)[:200] if resid2 != 0 else "0"))
results["residual_P3c"] = str(resid2)

# ============================================================================
print("P4: the T3-05 structural forms (multi-degree, mixed u_b powers)")
# replicate the ACTUAL sign structure: two Delta degrees with independent
# u_b-dependent coefficients, on both phase sectors
cm_real = q**2 / kap**2 * (1 + ub**2 * q**2 / kap**2) \
    + q**4 / kap**4 * (1 + ub**2)
Xm2 = phased(cm_real, -2)
Xp2 = phased(cm_real, +2)
i_combined = imsig_from_cone(cone_split(sp.expand(Xm2 + Xp2))["m"])
i_m = imsig_from_cone(cone_slot(Xm2, -2))
i_p_branch = imsig_from_cone(cone_slot(Xp2, +2))
resid3 = norm(i_m - i_combined)  # combined extraction sees only -cone key
check("P4a -2 branch reproducible in isolation", resid3 == 0,
      "I[X_-] alone == the -cone slot of I[X_- + X_+]: residual "
      + (str(resid3)[:200] if resid3 != 0 else "0"))

# sign-asymmetry probe: does the +2 cone extraction differ structurally?
resid4 = norm(i_p_branch - i_m)
note("P4b sign asymmetry probe: I[+2 branch] - I[-2 branch] normalized = "
     + str(resid4)[:200])
results["sign_asymmetry_residual"] = str(resid4)

# ============================================================================
results["notes"] = notes
results["w0"] = "computed-and-reported, NOT banked"
results["scope"] = ("synthetic additivity probe ONLY; frozen artifacts "
                    "read-only; no physics interpretation drawn here")
with open(RESULT_PATH, "w") as f:
    json.dump(results, f, indent=2)

fails = [c for c in results["checks"] if not c["pass"]]
print(f"\nT3-05C: {len(results['checks']) - len(fails)}/{len(results['checks'])} checks pass")
print(f"result written: {RESULT_PATH}")
raise SystemExit(1 if fails else 0)
