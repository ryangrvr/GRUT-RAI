#!/usr/bin/env python3
"""TIER 3 RETARDED IR CHECK -- SUBSTITUTION ONLY (owner authorization
2026-09-01: 'Perform ONLY the already-proposed substitution-level
evaluation of the recorded H2 retarded coefficients').

WHAT THIS IS: the delta-supported evaluation of the RECORDED Tier-3
retarded cone coefficients at q = omega/2 -- the machinery the flat
anchor validated against three independent routes. NO radial integration,
NO regulator, NO regeneration of T3, NO noise-sector input, NO J(omega)/
benchmark/matter-K_R content. The frozen T3 artifact and instrument are
read, never written.

CLASSIFICATION RULE (declared BEFORE the numbers):
  RETARDED IR OBSTRUCTION   -- the fixed-omega Im Sigma_R^{H2}(omega)
                               fails to exist (a surviving 1/(d-3) pole
                               at fixed omega, or an undefined
                               substitution);
  RETARDED VALIDITY BOUNDARY -- it exists, is d=3-smooth, and the ratio
                               Im Sigma^{H2}/Im Sigma^{H0} grows without
                               bound as omega -> 0 with a definite power
                               (reported; the expansion is controlled for
                               omega >> H and NOT extrapolated below);
  RETARDED IR-SOFT           -- it exists and the ratio is bounded as
                               omega -> 0;
  UNRESOLVED                 -- anything else.
The noise alpha = -2 result is NOT an input to this verdict.
HARD STOP after the report.
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
OUT = {}
mp.mp.dps = 25


def stamp(m):
    print("[%7.1fs] %s" % (time.time() - T0, m))
    sys.stdout.flush()


def check(c, m, gate=""):
    ok = bool(c)
    print(("  ok   " if ok else "  FAIL ") + m)
    sys.stdout.flush()
    CHECKS.append({"pass": ok, "msg": m, "gate": gate})
    if not ok:
        FAILS.append(m)
    return ok


def note(m):
    print("  note " + m)
    sys.stdout.flush()
    NOTES.append(m)


def sha_file(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


# ---- pins: everything read is the frozen record ----
print("=== PINS (read-only) ===")
check(sha_file(os.path.join(HERE, "WALL_KR_TIER3_LOOP_RESULT.json"))
      .startswith("4c016e93b889bd04"),
      "frozen T3 merged artifact sha 4c016e93... (untouched)", gate="PIN")
note("T3 instrument sha = %s..." % sha_file(
    os.path.join(HERE, "wall_kr_tier3_loop.py"))[:16])
note("integrand cache sha = %s..." % sha_file(
    os.path.join(HERE, ".tier3_integrand_cache.json"))[:16])
note("adjudication commit b4a6943; T3 commit 65ccb1b; owner authorization "
     "= substitution-only, this instrument")

# ---- symbols aligned with the frozen instrument ----
u, up, ub, D = sp.symbols("u u_p u_b Delta", real=True)
H = sp.Symbol("H", real=True)
q = sp.Symbol("q", positive=True)
om = sp.Symbol("omega", positive=True)
kap = sp.Symbol("kappa", positive=True)
dsym = sp.Symbol("d", positive=True)

# ---- import the FROZEN extraction/evaluation machinery by exec of the
# committed instrument's own source (no reimplementation, no drift) ----
src = open(os.path.join(HERE, "wall_kr_tier3_loop.py")).read()
i0 = src.find("def _exp_arg_of_factors")
i1 = src.find("if STAGE == \"assemble\":")
g = {"sp": sp, "D": D, "ub": ub, "q": q, "u": u, "up": up,
     "om": om, "kap": kap, "dsym": dsym}
exec(src[i0:i1], g)
cone_split = g["cone_split"]
imsig_from_cone = g["imsig_from_cone"]
stamp("frozen machinery loaded from the committed instrument")

IC = json.loads(open(os.path.join(
    HERE, ".tier3_integrand_cache.json")).read())
RET = sp.sympify(IC["ret_wigner"])
note("RETARDED cache only is read; the noise entry nk_wigner is NOT "
     "loaded (owner rule: the noise result may not force this verdict)")

# ---- H^0: re-derive from the cache and PIN against the frozen value ----
print("\n=== H^0 (consistency pin against the frozen artifact) ===")
c0 = cone_split(sp.expand(RET.subs(H, 0)))
check(c0["stray"] == {}, "H^0 cone split complete (no strays)", gate="H0")
ims0 = imsig_from_cone(c0["m"])
ims0_d3 = sp.simplify(ims0.subs(dsym, 3))
check(sp.simplify(ims0_d3.subs(kap, 1)
                  + 3 * om**4 / (1280 * sp.pi)) == 0,
      "Im Sigma_R^{H0} == -3 omega^4/(1280 pi) -- matches the frozen, "
      "three-route-validated value EXACTLY (the substitution machinery "
      "is pinned before touching H^2)", gate="H0")

# ---- H^2: the authorized substitution-level evaluation ----
print("\n=== H^2 (substitution-level; u_b = 0 Wigner convention) ===")
t_ = time.time()
R2 = sp.expand(RET.coeff(H, 2))
c2 = cone_split(R2)
stamp("H^2 cone extraction done (%.1fs)" % (time.time() - t_))
check(c2["stray"] == {}, "H^2 cone split complete (no strays)", gate="H2")
cm2 = sp.cancel(sp.together(c2["m"]))
check(not cm2.has(ub), "H^2 cone coefficient is u_b-free (gated)",
      gate="H2")
ims2 = imsig_from_cone(c2["m"])
ims2_gen = sp.simplify(ims2)
OUT["im_sigma_H2_general_d"] = str(ims2_gen)
# existence / d = 3 smoothness (the OBSTRUCTION test)
ims2_d3 = sp.simplify(sp.limit(ims2_gen, dsym, 3))
pole_d3 = sp.simplify(sp.limit(ims2_gen * (dsym - 3), dsym, 3))
obstructed = (pole_d3 != 0) or ims2_d3.has(sp.zoo) or ims2_d3.has(sp.oo)
check(not obstructed,
      "EXISTENCE: Im Sigma_R^{H2}(omega) exists at fixed omega > 0 and "
      "is SMOOTH at d = 3 (no surviving 1/(d-3) pole: residue = %s)"
      % str(pole_d3), gate="H2")
note("Im Sigma_R^{H2}(omega; d=3, u_b=0) = %s" % str(ims2_d3))
OUT["im_sigma_H2_d3"] = str(ims2_d3)

# ---- the ratio and the omega -> 0 classification ----
print("\n=== RATIO AND CLASSIFICATION ===")
ratio = sp.simplify(ims2_d3 / ims0_d3)
OUT["ratio_H2_over_H0_d3"] = str(ratio)
note("Sigma_H2 / Sigma_H0 (absorptive, d = 3) = %s" % str(ratio))
# leading omega -> 0 power of the ratio (exact, on the closed forms)
lead_pow = None
rr = sp.expand(sp.simplify(ratio / H**2))
for p_ in range(-6, 3):
    cc = sp.simplify(sp.limit(rr * om**(-p_), om, 0))
    if cc not in (sp.oo, -sp.oo, sp.zoo) and cc != 0:
        lead_pow = p_
        lead_c = cc
        break
check(lead_pow is not None, "the ratio has a definite leading omega "
      "power (found omega^%s with coefficient %s, per H^2)"
      % (str(lead_pow), str(lead_c) if lead_pow is not None else "-"),
      gate="RATIO")
# numeric spot substitutions (several, as ordered)
fr = sp.lambdify((om, H), ratio.subs(kap, 1), "mpmath")
for wv, Hv in (("1.0", "0.1"), ("0.5", "0.1"), ("0.25", "0.1"),
               ("2.0", "0.3")):
    note("spot: omega=%s, H=%s -> ratio = %s"
         % (wv, Hv, mp.nstr(fr(mp.mpf(wv), mp.mpf(Hv)), 8)))

# ---- verdict (per the declared rule) ----
print("\n=== VERDICT ===")
if obstructed:
    verdict = "RETARDED IR OBSTRUCTION"
elif lead_pow is None:
    verdict = "UNRESOLVED"
elif lead_pow < 0:
    verdict = "RETARDED VALIDITY BOUNDARY"
else:
    verdict = "RETARDED IR-SOFT"
OUT["verdict"] = verdict
if verdict == "RETARDED VALIDITY BOUNDARY":
    note("VERDICT: RETARDED VALIDITY BOUNDARY -- Im Sigma^{H2}/Im "
         "Sigma^{H0} = (exact) %s: the retarded H^2 sector EXISTS at "
         "every fixed omega > 0 with no IR scale, and the graded "
         "expansion is controlled for omega >> H, marginal at omega ~ H, "
         "and NOT VALID for omega << H (no extrapolation performed -- "
         "the strict omega -> 0 limit is nonuniform in H). The noise "
         "alpha = -2 finding remains a SEPARATE SK-state record and was "
         "not consulted." % str(ratio))
else:
    note("VERDICT: %s (see the recorded closed forms)" % verdict)

RESULT = {"instrument": "wall_kr_tier3_ir_check.py",
          "authorization": "owner 2026-09-01: substitution-only retarded "
                           "H^2 IR check; HARD STOP after",
          "out": OUT, "checks": CHECKS, "notes": NOTES,
          "failures": FAILS,
          "elapsed_s": round(time.time() - T0, 1),
          "hard_stop": "no H^2 radial integration performed; no "
                       "regulator; no noise input; no benchmark/J/matter "
                       "content; frozen T3 untouched"}
outp = os.path.join(HERE, "WALL_KR_TIER3_IR_CHECK_RESULT.json")
json.dump(RESULT, open(outp, "w"), indent=1, default=str)
print("\nartifact: %s (sha %s...)" % (outp, sha_file(outp)[:16]))
npass = sum(1 for c in CHECKS if c["pass"])
print("IR CHECK: %d/%d passed; failures: %d" % (npass, len(CHECKS),
                                                len(FAILS)))
for m in FAILS:
    print("  FAILURE: " + m)
print("HARD STOP.")
sys.exit(0 if not FAILS else 1)
