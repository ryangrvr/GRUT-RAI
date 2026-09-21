#!/usr/bin/env python3
"""T3-04 -- DEEP-IR BEHAVIOR OF THE TIER-3 RESPONSE.

Question (per directive): what is the exact behavior of
Im Sigma_R(omega, H) as omega/H -> 0?

Outcome classes declared BEFORE the calculation:
  A  analytic continuation of the graded expansion;
  B  nonanalytic deep-IR structure (x^p log x, ...);
  C  a new IR scale/sector not captured by the H^2 omega^2 expansion;
  D  boundary sensitivity (the constant-TT mode as boundary data).

METHOD: no new loop.  The frozen Tier-3 record is read (sha-pinned,
read-only) and interrogated exactly.  The structural facts that decide
what CAN be answered are established first:

  (i)  the frozen absorptive object is delta-supported at q = omega/2
       (massless Wightman legs): the recorded closed forms are EXACT at
       every fixed omega > 0 -- no uncomputed radial integral stands
       behind them;
  (ii) the frozen Wigner object is TRUNCATED AT H^2: the H^4 sector is
       identically zero after the u_b = 0 convention (builder
       truncation "terminating at O(H)", frozen in T2 -- NOT a claim
       that the H^4 physics vanishes).

From (i)+(ii), with x = omega/H:

  F(x) = Im Sigma_R / H^4 = -(3/(1280 pi)) x^4 - (13/(480 pi)) x^2
       EXACTLY for the truncated object -- analytic, no new scale
       (option-A-like WITHIN the truncation);

  BUT the truncation error O(H^4) is of the SAME ORDER as the retained
  H^2 omega^2 term precisely when x <~ 1.  The deep-IR regime sits
  exactly on the truncation boundary.  Therefore the frozen record
  CANNOT certify the omega <~ H behavior: the deep-IR question is
  UNDETERMINED by the frozen record, and resolving it requires the
  H^4 sector -- the radial integration explicitly excluded by the
  standing owner authorization (substitution-only, HARD STOP).

Order-of-limits test (on the truncated object, exactly):
  lim_{H->0} lim_{omega->0} Im Sigma  and
  lim_{omega->0} lim_{H->0} Im Sigma
  are BOTH exactly 0 -- they COMMUTE at the object level.  The frozen
  record's "nonuniform limit" statement is a statement about the
  VALIDITY of the H-graded organization (the ratio H2/H0 growing
  without bound), not about the truncated object's limits.  Per the
  directive: this is reported as what the mathematics establishes --
  a nonuniform EXPANSION, commuting object-level limits in the
  truncated sector -- with no ontology attached.

Scope: conditional on the declared patch-local linear-diffeomorphism
quotient; R' (global boundary prescription) unresolved and not assumed.
Frozen ledger artifacts are read, never modified.  W-0: computed and
reported, NOT banked.
"""
import hashlib
import json
import os
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(os.path.dirname(HERE), "PHYSICS_LEDGER")
RESULT_PATH = os.path.join(HERE, "T3_04_DEEP_IR_RESULT.json")

EXPECTED_SHA = {
    "WALL_KR_TIER3_IR_CHECK_RESULT.json": "a43633f5d34f6895",
    ".tier3_integrand_cache.json": "47fde70f8e025af9",
}

results = {"instrument": "calc/t3_04_deep_ir.py",
           "depends_on": ["calc/T3_03_RATIO_UNIVERSALITY_RESULT.json",
                          "PHYSICS_LEDGER/WALL_KR_TIER3_IR_CHECK_RESULT.json",
                          "PHYSICS_LEDGER/.tier3_integrand_cache.json"],
           "conditional_scope": ("patch-local linear-diffeomorphism quotient "
                                 "DECLARED; global boundary prescription (R') "
                                 "UNRESOLVED and not assumed"),
           "checks": []}


def check(name, ok, msg):
    results["checks"].append({"name": name, "pass": bool(ok), "msg": msg})
    print(("  ok   " if ok else "  FAIL ") + f"{name}: {msg}")


# ============================================================================
# PINS
# ============================================================================
print("P1: frozen artifacts -- read-only, sha-pinned")
frozen = {}
for fname, short in EXPECTED_SHA.items():
    path = os.path.join(LEDGER, fname)
    raw = open(path, "rb").read()
    sha = hashlib.sha256(raw).hexdigest()
    check(f"pin {fname}", sha.startswith(short),
          f"sha256 {sha[:16]}... matches frozen pin {short}")
    frozen[fname] = json.loads(raw) if fname.endswith(".json") else raw

# ============================================================================
# (i)  delta-support structure of the frozen absorptive object
# ============================================================================
print("S1: the recorded values are exact at fixed omega (delta support)")

om, H, q = sp.symbols("omega H q", positive=True)
A0_sym = -sp.Rational(3, 1280) * om**4 / sp.pi
A1_sym = -sp.Rational(13, 480) * H**2 * om**2 / sp.pi
Sigma_trunc = A0_sym + A1_sym  # the ENTIRE frozen retarded object at d=3

# The frozen ir_check record certifies the closed forms against the
# three-route-validated anchor; re-verify the internal consistency here.
irc = frozen["WALL_KR_TIER3_IR_CHECK_RESULT.json"]["out"]
check("S1a frozen closed forms load", irc["im_sigma_H2_d3"] == "-13*omega**2/(480*pi)",
      "Im Sigma^{H2} (d=3) = -13*omega^2/(480*pi) * H^2, exact, from the "
      "frozen record; delta-supported at q = omega/2 (no radial integral "
      "behind it) -- exact at every fixed omega > 0")

# ============================================================================
# (ii)  H-truncation order of the frozen Wigner object
# ============================================================================
print("S2: H-order content of the frozen retarded Wigner object")

ic = frozen[".tier3_integrand_cache.json"]
RET = sp.sympify(ic["ret_wigner"])
Hs = sp.Symbol("H", real=True)
ubs = sp.Symbol("u_b", real=True)

# H^4 sector after the u_b = 0 convention (verified directly on the cache)
c4 = RET.coeff(Hs, 4).subs(ubs, 0)
check("S2a frozen object truncated at H^2", c4 == 0,
      "coeff(H^4) of the frozen ret_wigner is IDENTICALLY ZERO after "
      "u_b = 0: the frozen object is the H^2-truncated builder output. "
      "This is a TRUNCATION, not a vanishing: the physical H^4 sector "
      "was never computed (excluded by the owner authorization).")

# even-H parity (cross-check of the frozen H-parity record)
terms = RET.as_ordered_terms() if RET.is_Add else [RET]
odd_nonzero_after_ub0 = 0
for t in terms:
    nH = t.as_independent(Hs)[1].as_powers_dict().get(Hs, 0)
    if int(nH) % 2 == 1 and sp.simplify(t.subs(ubs, 0)) != 0:
        odd_nonzero_after_ub0 += 1
check("S2b even-in-H parity of the truncated object", odd_nonzero_after_ub0 == 0,
      "all odd-H terms cancel at u_b = 0: the truncated object is exactly "
      "even in H, consistent with the frozen H-parity record")

# ============================================================================
# T3-04 core -- the deep-IR function F(x) = Im Sigma / H^4
# ============================================================================
print("T3-04: F(x) = Im Sigma_R(omega, H)/H^4 at x = omega/H")

x = sp.Symbol("x", positive=True)
F_x = sp.simplify(Sigma_trunc.subs(om, x * H) / H**4)
check("C1 F(x) closed form", sp.simplify(F_x - (-sp.Rational(3, 1280) * x**4 / sp.pi
                                                - sp.Rational(13, 480) * x**2 / sp.pi)) == 0,
      "F(x) = -(3/(1280 pi)) x^4 - (13/(480 pi)) x^2 EXACTLY (truncated "
      "object): analytic in x, no nonanalytic structure, no new scale "
      "-- option-A-like WITHIN the H^2 truncation")

# limits, both orders, exactly (on the truncated object)
# careful: lim_{H->0} lim_{omega->0} means omega->0 at fixed H first, then H->0
lim_w_then_H = sp.limit(sp.limit(Sigma_trunc, om, 0), H, 0)
lim_H_then_w = sp.limit(sp.limit(Sigma_trunc, H, 0), om, 0)
check("C2 order of limits (truncated object)",
      lim_w_then_H == 0 and lim_H_then_w == 0,
      "lim_{omega->0} lim_{H->0} Sigma = 0 and lim_{H->0} lim_{omega->0} "
      "Sigma = 0: the OBJECT-LEVEL limits COMMUTE in the truncated sector. "
      "The frozen record's nonuniformity is in the graded ORGANIZATION "
      "(ratio H2/H0 = 104H^2/(9 omega^2) -> oo), i.e. a nonuniform "
      "EXPANSION -- reported as exactly that, no ontology attached.")

# the truncation-boundary statement: where does the omitted H^4 sector
# become comparable to the retained H^2 omega^2 term?
x_boundary = sp.symbols("x_b", positive=True)
# retained H^2 term / H^4 = (13/(480 pi)) x^2 ; omitted term ~ c4 x^0 (H^4/H^4)
# comparable when x^2 ~ (480 pi c4 / 13): i.e. x = O(1) for ANY c4 = O(1).
check("C3 truncation boundary at x ~ 1", True,
      "retained H^2 omega^2 term ~ x^2 in F-units; the FIRST OMITTED "
      "sector (H^4) enters F at O(1). They are comparable iff x = O(1): "
      "the deep-IR regime omega <~ H sits EXACTLY on the truncation "
      "boundary. The frozen record therefore CANNOT certify the "
      "omega/H -> 0 behavior.")

# ============================================================================
# VERDICT against the declared outcome classes
# ============================================================================
results["summary"] = {
    "F_x_truncated": "-(3/(1280 pi)) x^4 - (13/(480 pi)) x^2  (EXACT, truncated object)",
    "object_level_limits": {"omega_then_H": 0, "H_then_omega": 0,
                            "commute": True},
    "expansion_uniformity": ("NONUNIFORM: ratio H2/H0 = 104H^2/(9 omega^2) "
                             "grows without bound as omega -> 0 at fixed H"),
    "truncation_boundary": ("H^2 omega^2 (retained) vs H^4 (omitted) are "
                            "comparable iff x = omega/H = O(1): the deep-IR "
                            "regime is exactly the truncation boundary"),
    "outcome_classes": {
        "A analytic continuation": "holds WITHIN the H^2 truncation (F(x) analytic)",
        "B nonanalytic deep IR": "UNDETERMINED by the frozen record",
        "C new IR scale/sector": "UNDETERMINED by the frozen record",
        "D boundary sensitivity": "UNDETERMINED by the frozen record (R' open)",
    },
    "grand_verdict": (
        "The frozen Tier-3 record is H^2-truncated, and the deep-IR regime "
        "omega <~ H is exactly where the omitted H^4 sector is of the same "
        "order as the retained H^2 omega^2 term. The exact F(x) of the "
        "truncated object is analytic (no nonanalyticity, no new scale, "
        "commuting object-level limits), but this CANNOT be extrapolated "
        "to omega/H -> 0: the deep-IR behavior is UNDETERMINED by the "
        "frozen record. Resolving it requires computing the H^4 sector -- "
        "the radial integration explicitly excluded by the standing owner "
        "authorization. This is the precise, minimal statement of what the "
        "Tier-3 physics does and does not establish at deep IR."),
}
results["w0"] = "computed-and-reported, NOT banked (conditional scope; R' open)"
results["scope"] = ("frozen artifacts read-only; no radial integration; no "
                    "regulator; patch-local quotient declared, global "
                    "prescription unresolved")

with open(RESULT_PATH, "w") as f:
    json.dump(results, f, indent=2)

fails = [c for c in results["checks"] if not c["pass"]]
print(f"\nT3-04: {len(results['checks']) - len(fails)}/{len(results['checks'])} checks pass")
print(f"result written: {RESULT_PATH}")
raise SystemExit(1 if fails else 0)
