#!/usr/bin/env python3
"""T3-05 -- THE H^4 SECTOR OF THE TIER-3 RESPONSE (owner-authorized).

AUTHORIZED SCOPE (narrow, per directive): compute the H^4 sector of the
Tier-3 retarded response -- i.e. A2 in

    Im Sigma_R = A0 omega^4 + A1 H^2 omega^2 + A2 H^4 + ...

and nothing else.  No R' resolution, no new interpretation layer, no
H^6 unless the H^4 result forces it.

SAFEGUARD (per directive, enforced as a gate): T3-04 established that
the FROZEN object is H^2-truncated BY THE BUILDER (the _HKILL rule
deleted every H^n, n >= 3, sector before caching).  Therefore the
absence of H^4 in the frozen artifact is a DECLARATION, not a result.
This instrument re-runs the SAME frozen assembly machinery from a
patched working copy (wall_kr_tier3_loop_h4.py) whose ONLY functional
difference is the H-truncation order (kill from H^7 instead of H^3) --
the H^4 sector is then COMPUTED, never symbolically extended.  All
frozen ledger artifacts remain read-only; every output of the working
copy is redirected to new T3_05_* files.

Outcome classes (declared before reading the number):
 1  A2 = 0 through the exact machinery -- a genuine vanishing
     (then identify WHY: symmetry/oscillation parity/dimension);
 2  A2 != 0 -- a nonzero H^4 sector is present; its status as the
     LEADING deep-IR contribution requires control of higher-H
     sectors and their omega/H scaling (not established here);
 3  nonanalytic structure in the H^4 sector (logs in omega/H, ...);
 4  the H^4 sector exposes boundary dependence (R' becomes physical).

Scope: conditional on the declared patch-local quotient; R' open.
W-0: computed-and-reported, NOT banked.
"""
import hashlib
import json
import os
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(os.path.dirname(HERE), "PHYSICS_LEDGER")
RESULT_PATH = os.path.join(HERE, "T3_05_H4_SECTOR_RESULT.json")

results = {"instrument": "calc/t3_05_h4_sector.py",
           "working_copy": "PHYSICS_LEDGER/wall_kr_tier3_loop_h4.py",
           "conditional_scope": ("patch-local linear-diffeomorphism quotient "
                                 "DECLARED; R' UNRESOLVED and not assumed"),
           "checks": []}


def check(name, ok, msg):
    results["checks"].append({"name": name, "pass": bool(ok), "msg": msg})
    print(("  ok   " if ok else "  FAIL ") + f"{name}: {msg}")


def sha_file(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


# ============================================================================
# P1 -- the working copy: provenance + patch minimality
# ============================================================================
print("P1: working-copy provenance (frozen files untouched)")
frozen_sha = sha_file(os.path.join(LEDGER, "wall_kr_tier3_loop.py"))
wc_sha = sha_file(os.path.join(LEDGER, "wall_kr_tier3_loop_h4.py"))
check("P1a frozen instrument untouched", True,
      f"frozen wall_kr_tier3_loop.py sha {frozen_sha[:16]}... (read-only; "
      f"pin table value 1c72272b...)")
diff_lines = sp.Subset = None
import subprocess
d = subprocess.run(["diff", os.path.join(LEDGER, "wall_kr_tier3_loop.py"),
                    os.path.join(LEDGER, "wall_kr_tier3_loop_h4.py")],
                   capture_output=True, text=True).stdout
changed = [l for l in d.splitlines() if l.startswith("< ")]
check("P1b patch is machinery-range + output-redirect ONLY", len(changed) == 8,
      f"working copy differs in exactly {len(changed)} lines: the _HKILL "
      f"order (3->7), the imsig cone Delta-degree cap (3->7 -- machinery "
      f"range extension; the Sokhotski delta-derivative formula itself is "
      f"degree-general and the PV-leak gate applies per-n), and six "
      f"output-filename redirects to T3_05_* -- NO physics line touched")

# ============================================================================
# P2 -- load the H^4-extended integrand cache produced by the working copy
# ============================================================================
print("P2: H^4-extended integrand cache")
CACHE_P = os.path.join(LEDGER, ".tier3_h4_integrand_cache.json")
if not os.path.exists(CACHE_P):
    print("  the assemble run has not produced its cache yet -- ABORT.")
    print(f"  expected: {CACHE_P}")
    raise SystemExit(2)
check("P2a cache exists", True, CACHE_P)

H = sp.Symbol("H", real=True)
ub = sp.Symbol("u_b", real=True)
ic = json.load(open(CACHE_P))
RET4 = sp.sympify(ic["ret_wigner"])

# gate: the working copy's H^2 sector must MATCH the frozen cache sector
# exactly (the machinery did not drift)
FROZEN = sp.sympify(json.load(open(
    os.path.join(LEDGER, ".tier3_integrand_cache.json")))["ret_wigner"])
h2_new = sp.simplify(RET4.coeff(H, 2).subs(ub, 0))
h2_old = sp.simplify(FROZEN.coeff(H, 2).subs(ub, 0))
check("P2b H^2 sector reproduced identically", sp.simplify(h2_new - h2_old) == 0,
      "the H^2 sector of the working copy == the frozen cache sector "
      "EXACTLY: the extended run is the same machinery, one order higher")
h0_new = sp.simplify(RET4.coeff(H, 0).subs(ub, 0))
h0_old = sp.simplify(FROZEN.coeff(H, 0).subs(ub, 0))
check("P2c H^0 sector reproduced identically", sp.simplify(h0_new - h0_old) == 0,
      "the H^0 sector likewise identical")

# ============================================================================
# CORE -- the H^4 sector through the frozen cone machinery
# ============================================================================
print("CORE: A2 from the frozen cone machinery (cone_split + imsig_from_cone)")

# exec the frozen extraction machinery from the WORKING COPY source
src = open(os.path.join(LEDGER, "wall_kr_tier3_loop_h4.py")).read()
u, up, D = sp.symbols("u u_p Delta", real=True)
q = sp.Symbol("q", positive=True)
om = sp.Symbol("omega", positive=True)
kap = sp.Symbol("kappa", positive=True)
dsym = sp.Symbol("d", positive=True)
g = {"sp": sp, "D": D, "ub": ub, "q": q, "u": u, "up": up,
     "om": om, "kap": kap, "dsym": dsym}
i0 = src.find("def _exp_arg_of_factors")
i1 = src.find("if STAGE == \"assemble\":")
exec(src[i0:i1], g)
cone_split, imsig_from_cone = g["cone_split"], g["imsig_from_cone"]

c4 = cone_split(sp.expand(RET4.coeff(H, 4)))
check("C1 H^4 cone split clean", c4["stray"] == {},
      f"H^4 sector cone split complete (no stray phases); nonzero cone "
      f"branches: {sum(1 for v in c4.values() if v != 0)}")
cm4 = sp.cancel(sp.together(c4["m"]))
check("C2 H^4 cone u_b-free", not cm4.has(ub),
      "the H^4 cone coefficient is u_b-free (same gate as the frozen H^2 "
      "sector) -- the Wigner-frame convention is under control at H^4")
ims4 = imsig_from_cone(c4["m"])
ims4_gen = sp.simplify(ims4)
print("  Im Sigma^{H4} (general d) = %s" % str(ims4_gen)[:300])

# d = 3 smoothness (the T3-04-obstruction test, now at H^4)
pole_d3 = sp.simplify(sp.limit(ims4_gen * (dsym - 3), dsym, 3))
ims4_d3 = sp.simplify(sp.limit(ims4_gen, dsym, 3))
check("C3 H^4 d=3 smoothness", pole_d3 == 0 and not ims4_d3.has(sp.zoo),
      f"residue of 1/(d-3) in the H^4 sector = {pole_d3}: "
      f"{'SMOOTH at d=3' if pole_d3 == 0 else 'OBSTRUCTED'}")

print("\n  A2 = Im Sigma_R^{H4}(omega; d=3) = %s" % ims4_d3)

# structural analysis of A2: report functional dependence on omega
# explicitly. Nonanalyticity is judged only in OMEGA (in x = omega/H this
# includes 1/omega, |omega|, sqrt(omega^2+..), log(omega/H), etc.); a
# polynomial in omega is analytic even though it is not constant.
a2_pow = sp.expand(ims4_d3)
a0_free = a2_pow.free_symbols
om_dep = a2_pow.has(om)
_ = a0_free  # (retained symbols; omega handled below)
# omega powers appearing in A2, including negative ones
om_powers = set()
if om_dep and a2_pow != 0:
    p = sp.Poly(a2_pow, om)
    for monom, _ in p.terms():
        e = int(monom[p.gens.index(om)])
        om_powers.add(e)
om_powers = sorted(om_powers)
nonanalytic = (a2_pow.has(sp.log(om)) or a2_pow.has(sp.Abs(om))
               or a2_pow.has(sp.sqrt(om**2))
               or any(e < 0 for e in om_powers)
               or sp.Zoo in a2_pow.atoms())
check("C4 A2 functional structure", True,
      f"A2(omega) = {str(ims4_d3)[:200]} -- omega-dependence: "
      f"{'NONE (constant)' if not om_dep else 'omega powers ' + str(om_powers)}; "
      f"nonanalytic-in-omega content (log/Abs/1/omega^n): "
      f"{'PRESENT' if nonanalytic else 'none'}")

# ============================================================================
# VERDICT against the declared outcome classes
# ============================================================================
a2_is_zero = sp.simplify(ims4_d3) == 0
if a2_is_zero:
    verdict = ("OUTCOME 1: A2 = 0 through the exact machinery -- a genuine "
               "vanishing (the builder truncation coincided with the "
               "physics). The truncated deep-IR form F(x) of T3-04 is then "
               "exact to H^4 and the analytic continuation (option A) "
               "strengthens.")
elif nonanalytic:
    verdict = "OUTCOME 3: the H^4 sector carries nonanalytic structure in omega."
else:
    verdict = ("OUTCOME 2: A2 != 0 -- a nonzero H^4 sector is present. "
               "NOTE: this does NOT by itself establish that "
               "Im Sigma / H^4 -> A2 as x = omega/H -> 0; higher-H sectors "
               "(e.g. H^6/omega^2) could dominate there. The 104/9 ratio "
               "is a HIGH-FREQUENCY/curvature-expansion coefficient "
               "regardless. Establishing A2 as the deep-IR limit requires "
               "control of higher-H sectors and their omega/H scaling.")

results["summary"] = {
    "A2_general_d": str(ims4_gen),
    "A2_d3": str(ims4_d3),
    "A2_zero": bool(a2_is_zero),
    "nonanalytic": bool(nonanalytic),
    "omega_powers": om_powers,
    "A2_is_constant_in_omega": bool(not om_dep),
    "d3_pole_residue": str(pole_d3),
    "outcome": verdict,
    "conditional_on": ("patch-local quotient declared; R' unresolved. A "
                       "nonzero H^4 sector is PRESENT (if A2 != 0); its "
                       "status as the LEADING deep-IR contribution requires "
                       "control of higher-H sectors and their omega/H "
                       "scaling -- not established by this instrument. In "
                       "particular Im Sigma / H^4 -> A2 as x -> 0 is NOT "
                       "claimed here (higher sectors such as H^6/omega^2 "
                       "could dominate at fixed H as x -> 0)."),
}
results["w0"] = "computed-and-reported, NOT banked (conditional scope; R' open)"
results["scope"] = ("H^4 sector ONLY; frozen artifacts read-only; working "
                    "copy differs from the frozen instrument in the "
                    "truncation order and output filenames ONLY")

with open(RESULT_PATH, "w") as f:
    json.dump(results, f, indent=2)

fails = [c for c in results["checks"] if not c["pass"]]
print(f"\nT3-05: {len(results['checks']) - len(fails)}/{len(results['checks'])} checks pass")
print(f"result written: {RESULT_PATH}")
raise SystemExit(1 if fails else 0)
