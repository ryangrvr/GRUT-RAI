#!/usr/bin/env python3
"""T3-05L (v2) -- THE p / (+2) BUCKET THROUGH THE ABSORPTIVE EXTRACTION.

Chain position (owner directive): K2 namespace reconciliation ->
  ** p-bucket through the absorptive extraction **  -> assembled H^4
contribution -> Sigma -> G_R^TT if warranted.  T3-05K2 established the
partitions are IDENTICAL (m <-> (-2,0), p <-> (+2,0), 1515/1515, no
stray); this instrument decides the p-branch's fate in the assembled
Im Sigma_R(omega > 0).

WHY THE FROZEN FUNCTION IS NOT CALLED ON THE p BUCKET VERBATIM.  The
frozen derivation (wall_kr_tier3_loop_h4.py, imsig_from_cone docstring)
extracts "Im Sigma_R(omega > 0) from the omega = +2q cone content of the
retarded combination RET = sum_n c_n(q) Delta^n e^{-2iq Delta} + (+2q
mirror)":
    int_0^inf Delta^n e^{i omega Delta - eta Delta} e^{-2iq Delta} dDelta
        = n!/(eta - i(omega-2q))^{n+1},
Sokhotski delta class supported at q = omega/2 (where it substitutes).
The p branch carries e^{+2iq Delta}: its inner integral is
n!/(eta - i(omega+2q))^{n+1}, delta class delta^(n)(omega+2q), supported
at q = -omega/2.  Calling the m-formula on p-coefficients would evaluate
them at the wrong support point and return a number belonging to no
derivation.  This instrument DERIVES the p-branch absorptive
contribution from the same inner integral and adjudicates.

V1 -> V2 DISCLOSURE (premise refuted by the data; predeclared outcomes
revised BEFORE this filed run; the v1 log is preserved as
calc/t3_05l_run1.log).  V1 predeclared a "conjugate mirror" premise:
p-bucket == conj(m-bucket), from naive anti-hermiticity of Sigma_> -
Sigma_<.  The v1 diagnostic REFUTED it: per-degree ratios
conj(c_n^m)/c_n^p are not +-1 and not constant (e.g. n=0: -0.559 vs
-40.9 at one exact rational point), while BOTH buckets separately
satisfy the i^n c_n-real pattern (n even -> real, n odd -> pure
imaginary).  The mechanism was then located in the frozen source and is
machine-verified below (M1-M3): WMINUS == conj(WPLUS) EXACTLY, but the
assembly's derivative-vertex operators nu^a -> (-i d/du)^a are NOT
conjugation-covariant at odd order (conj((-i d/du) W+) != (-i d/du) W-;
even orders covariant).  The two cones therefore carry INDEPENDENT
coefficient content by construction -- a property of this object's
convention, with the physical reality of Im Sigma_R enforced by the
frozen extraction's own i^n c_n-real gate (which the H^0 sector passed
under conviction by an independent route + numeric quadrature,
WALL_KR_TIER3_FLAT_RESULT.json).  The mirror statement is therefore
REMOVED from the outcome classes; independence is documented instead.

WHAT IS COMPUTED (termwise on the pinned 3030-term array; the giant Add
is never rebuilt):
  L1 provenance: term cache verified against the pinned shas;
  L2 both buckets rebuilt termwise; Delta-degree inventory;
  M1-M3 mechanism: conj(WPLUS) == WMINUS exact; odd-order breaking
     residual nonzero; even-order covariance -- from the frozen W forms;
  L3 reality pattern: i^n c_n real for BOTH buckets at exact rational
     points (the frozen PV-leak gate's precondition), and the non-mirror
     ratios recorded;
  L4 inner integrals: both cone formulas verified for every degree
     present (symbolic on the convergent branch; exact-rational numeric
     backstop);
  L5 SUPPORT: per degree, the p-branch delta class delta^(n)(omega+2q)
     integrated over the measure domain q in (0, inf) with omega > 0 is
     IDENTICALLY ZERO (support q = -omega/2 outside the domain) --
     machine-verified per degree; m-side contrast fires at q = omega/2.

Predeclared outcome classes (exactly one):
  P_BRANCH_KINEMATICALLY_NULL_INDEPENDENT_CONTENT
      -> p contributes ZERO to Im Sigma_R(omega > 0) at H^4 by empty
         delta support (kinematic, termwise, NOT a cancellation), AND
         its coefficients are independent of the m bucket (mechanism
         M1-M3).  Consequences recorded: A2 from the m cone is the
         COMPLETE Im Sigma_R^{H4}(omega > 0); the p cone carries the
         omega < 0 delta support and independent PV/dispersive content
         that any future Re Sigma_R / G_R^TT assembly MUST include
         explicitly (it is NOT reconstructible from the m cone by
         conjugation); T3-05J's "+2 bucket absent from the assembled
         result" is EXPECTED BEHAVIOR of the derivation, not a defect.
  P_BRANCH_CANCELS
      -> support nonempty but the domain integral vanishes by
         cancellation among terms (mechanism recorded).
  P_BRANCH_SURVIVES
      -> nonzero absorptive contribution at omega > 0: the assembled A2
         is INCOMPLETE; defect recorded.
  P_BRANCH_UNINTERPRETABLE
      -> phase content outside the +-2 cone form or a gate failure the
         existing assembly cannot classify.

Scope fences: diagnostic + derivation ONLY at the declared contract
scope; no physics conclusion about u_b beyond the completeness statement;
no R'; no H^6; no keystone resummation; frozen artifacts read-only;
T3-05K and K2 records untouched; W-0: computed-and-reported, NOT banked.
"""
import hashlib
import json
import os
import random
import sys
import time
from collections import defaultdict

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(os.path.dirname(HERE), "PHYSICS_LEDGER")
SRC_CACHE = os.path.join(LEDGER, ".tier3_h4_integrand_cache.json")
SEC4_CACHE = os.path.join(LEDGER, ".sec4_cache.json")
TERM_CACHE = os.path.join(LEDGER, ".sec4_terms_cache.json")
FROZEN_H4 = os.path.join(LEDGER, "wall_kr_tier3_loop_h4.py")
RESULT_PATH = os.path.join(HERE, "T3_05L_P_BRANCH_ABSORPTIVE_RESULT.json")
T0 = time.time()


def stage(msg):
    print(f"[{time.time()-T0:7.1f}s][stage] {msg}", flush=True)


def sha_file(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


results = {"instrument": "calc/t3_05l_p_branch_absorptive.py (v2)",
           "question": ("does the p / (+2,0) bucket of the H^4 sector "
                        "contribute to the assembled Im Sigma_R(omega>0), "
                        "and what is its information content?"),
           "v1_disclosure": ("v1's conjugate-mirror premise REFUTED by "
                             "its own diagnostic (log: t3_05l_run1.log); "
                             "outcome classes revised before this filed "
                             "run; mechanism M1-M3 below"),
           "checks": [], "notes": [],
           "w0": "computed-and-reported, NOT banked"}


def check(name, ok, msg):
    results["checks"].append({"name": name, "pass": bool(ok), "msg": msg})
    print(("  ok   " if ok else "  FAIL ") + f"{name}: {msg}", flush=True)


def note(m):
    results["notes"].append(m)
    print("  -- " + m, flush=True)


# ------------------------------------------------------------ symbols
H = sp.Symbol("H", real=True)
ub = sp.Symbol("u_b", real=True)
D = sp.Symbol("Delta", real=True)
q = sp.Symbol("q", positive=True)
om = sp.Symbol("omega", positive=True)
kap = sp.Symbol("kappa", positive=True)
dsym = sp.Symbol("d", positive=True)
u_ = sp.Symbol("u", real=True)
up_ = sp.Symbol("u_p", real=True)
eta = sp.Symbol("eta", positive=True)

# ===================================================== L1: provenance
stage("L1: term-array cache provenance")
results["pins"] = {"wall_kr_tier3_loop_h4.py": sha_file(FROZEN_H4)}
sc_prov = json.load(open(SEC4_CACHE))["provenance"]
tc = json.load(open(TERM_CACHE))
prov = tc["provenance"]
prov_ok = (prov["source_cache_sha256"] == sha_file(SRC_CACHE)
           and prov["sec4_sha256"] == sc_prov["sec4_sha256"]
           and hashlib.sha256("\n".join(tc["terms"]).encode()).hexdigest()
           == prov["ordered_terms_hash"])
check("L1 term-array cache provenance verified", prov_ok,
      f"{len(tc['terms'])} terms; source_cache_sha256/sec4_sha256/"
      "ordered_terms_hash all match")
if not prov_ok:
    json.dump(results, open(RESULT_PATH, "w"), indent=1)
    sys.exit(1)
_locals = {"q": q, "Delta": D, "u_b": ub, "omega": om, "kappa": kap,
           "d": dsym, "u": u_, "u_p": up_, "H": H}
terms = [sp.sympify(s, locals=_locals) for s in tc["terms"]]
N = len(terms)

src = open(FROZEN_H4).read()
g = {"sp": sp, "D": D, "ub": ub, "q": q, "u": u_, "up": up_, "om": om,
     "kap": kap, "dsym": dsym}
exec(src[src.find("def _exp_arg_of_factors"):
         src.find('if STAGE == "assemble":')], g)
strip_exp_den = g["strip_exp_den"]
doc = " ".join(g["imsig_from_cone"].__doc__.split())
check("L1 frozen derivation quotation on record",
      "omega = +2q cone content" in doc and "(+2q mirror)" in doc,
      "imsig_from_cone docstring (verbatim head): " + doc[:200])

# =============================== L2: rebuild both buckets, termwise
stage("L2: termwise classification into the two cone buckets")


def walk(t):
    t = strip_exp_den(t)
    arg = sp.Integer(0)
    rest = []
    for f in t.as_ordered_factors():
        b, e = f.as_base_exp()
        if b == sp.E:
            arg += e
        else:
            rest.append(f)
    arg = sp.expand(arg)
    rD = sp.cancel(arg.coeff(D, 1) / (sp.I * q))
    rb = sp.cancel(arg.coeff(ub, 1) / (sp.I * q))
    if sp.cancel(sp.expand(arg - sp.I * q * (rD * D + rb * ub))) != 0:
        raise RuntimeError("unrecognized phase: %s" % str(arg))
    return (rD, rb), sp.Mul(*rest)


KM, KP = (sp.Integer(-2), sp.Integer(0)), (sp.Integer(2), sp.Integer(0))
m_by_deg, p_by_deg = defaultdict(list), defaultdict(list)
n_m = n_p = n_other = 0
for i, t in enumerate(terms):
    if i % 500 == 0:
        stage(f"  term {i}/{N}")
    k, r = walk(t)
    if k == KM:
        n_m += 1
        tgt = m_by_deg
    elif k == KP:
        n_p += 1
        tgt = p_by_deg
    else:
        n_other += 1
        continue
    for (e_,), c in sp.Poly(r, D).terms():
        tgt[int(e_)].append(c)
check("L2 every pinned term lands in the two cone buckets",
      n_other == 0 and n_m == n_p == N // 2,
      f"m: {n_m}, p: {n_p}, other: {n_other} (matches K2: 1515/1515, "
      "no stray)")
if n_other:
    results["classification"] = "P_BRANCH_UNINTERPRETABLE"
    json.dump(results, open(RESULT_PATH, "w"), indent=1)
    sys.exit(2)
degrees = sorted(set(m_by_deg) | set(p_by_deg))
check("L2 Delta-degree inventory identical between buckets",
      sorted(m_by_deg) == sorted(p_by_deg),
      f"degrees present: {degrees}; per-degree monomial counts "
      f"m={ {n: len(v) for n, v in sorted(m_by_deg.items())} } "
      f"p={ {n: len(v) for n, v in sorted(p_by_deg.items())} }")
results["delta_degrees"] = {
    "present": degrees,
    "m_counts": {n: len(v) for n, v in sorted(m_by_deg.items())},
    "p_counts": {n: len(v) for n, v in sorted(p_by_deg.items())}}

# ================== M1-M3: the non-mirror mechanism, from the source
stage("M: conjugation structure of the frozen W kernels")
WPLUS = (kap**2 / q) * sp.exp(-sp.I * q * (u_ - up_)) * (
    (1 - H * u_) * (1 - H * up_) + sp.I * H**2 * (u_ - up_) / q
    + H**2 / q**2)
WMINUS = (kap**2 / q) * sp.exp(sp.I * q * (u_ - up_)) * (
    (1 - H * u_) * (1 - H * up_) - sp.I * H**2 * (u_ - up_) / q
    + H**2 / q**2)
src_has = ("WPLUS = (kap**2 / q) * sp.exp(-sp.I * q * (u - up))" in src
           and "WMINUS = (kap**2 / q) * sp.exp(sp.I * q * (u - up))" in src)
check("M1 WMINUS == conj(WPLUS) EXACTLY (frozen Tier-2 forms)",
      src_has and sp.simplify(sp.conjugate(WPLUS) - WMINUS) == 0,
      "the W forms are quoted from the frozen source and the conjugation "
      "identity is exact")
d1res = sp.simplify(sp.conjugate((-sp.I) * sp.diff(WPLUS, u_))
                    - (-sp.I) * sp.diff(WMINUS, u_))
check("M2 odd derivative order BREAKS conjugation covariance",
      d1res != 0,
      "conj((-i d/du) WPLUS) - (-i d/du) WMINUS != 0: residual/WMINUS = "
      + str(sp.simplify(d1res / WMINUS))[:120]
      + " -- the assembly's nu^a -> (-i d/du)^a operators (frozen "
      "dependency graph) are not conjugation-covariant at odd order")
check("M3 even derivative order IS conjugation-covariant",
      sp.simplify(sp.conjugate((-sp.I)**2 * sp.diff(WPLUS, u_, 2))
                  - (-sp.I)**2 * sp.diff(WMINUS, u_, 2)) == 0,
      "a = 2 exact -- the breaking is strictly odd-order, which is why "
      "the two cones carry independent coefficient content while each "
      "separately satisfies the i^n c_n reality pattern")

# ======================= L3: reality pattern + independence, numeric
stage("L3: i^n c_n reality pattern (both buckets) + non-mirror ratios")
random.seed(20260920)
allsyms = set()
for lst in list(m_by_deg.values()) + list(p_by_deg.values()):
    for c in lst[:40]:
        allsyms |= c.free_symbols
allsyms = sorted(allsyms, key=str)
results["coefficient_symbols"] = [str(s) for s in allsyms]
pts = [{s: sp.Rational(random.randint(2, 41), random.randint(2, 23))
        for s in allsyms} for _ in range(4)]
real_ok = True
ratio_rec = {}
for n in degrees:
    rec = []
    for j, pt in enumerate(pts):
        cm = sp.expand_complex(sum((c.subs(pt) for c in m_by_deg[n]),
                                   sp.Integer(0)))
        cp = sp.expand_complex(sum((c.subs(pt) for c in p_by_deg[n]),
                                   sp.Integer(0)))
        rm = sp.simplify(sp.im(sp.I**n * cm)) == 0
        rp = sp.simplify(sp.im(sp.I**n * cp)) == 0
        real_ok = real_ok and rm and rp
        if j < 2 and cp != 0:
            rec.append(str(sp.nsimplify(sp.simplify(
                sp.conjugate(cm) / cp)))[:60])
    ratio_rec[n] = rec
check("L3 i^n c_n real for BOTH buckets at every exact rational point",
      real_ok,
      "the frozen PV-leak gate's precondition holds on the p bucket "
      "too: its own absorptive/PV split is clean")
note("non-mirror ratios conj(c_n^m)/c_n^p (2 points per degree, "
     "recorded to document coefficient independence): "
     + json.dumps(ratio_rec))
results["nonmirror_ratios"] = ratio_rec

# ============================== L4: inner time integral, both cones
stage("L4: exact inner time integral for every degree present")
maxn = max(degrees)
inner_ok = True
inner_rec = {}
npts = [{eta: sp.Rational(1, 7), om: sp.Rational(3, 2),
         q: sp.Rational(5, 3)},
        {eta: sp.Rational(2, 9), om: sp.Rational(7, 4),
         q: sp.Rational(1, 6)},
        {eta: sp.Rational(1, 3), om: sp.Rational(11, 5),
         q: sp.Rational(8, 3)}]
for n in range(0, maxn + 1):
    rec = {}
    for tag, sgn in (("m", -1), ("p", +1)):
        I_ = sp.integrate(D**n * sp.exp(sp.I * om * D - eta * D)
                          * sp.exp(sgn * 2 * sp.I * q * D), (D, 0, sp.oo))
        f_ = sp.factorial(n) / (eta - sp.I * (om - sgn * (-2) * q
                                              * (-1)))**(n + 1)
        f_ = sp.factorial(n) / (eta - sp.I * (om + sgn * 2 * q))**(n + 1)
        if isinstance(I_, sp.Piecewise):
            br = I_.args[0][0]
        else:
            br = I_
        sym_ok = sp.simplify(sp.cancel(sp.together(br - f_))) == 0
        num_ok = all(sp.expand_complex(sp.nsimplify(
            br.subs(p_) - f_.subs(p_))) == 0 for p_ in npts)
        rec[tag] = {"symbolic": bool(sym_ok), "numeric_3pts": bool(num_ok)}
        inner_ok = inner_ok and (sym_ok or num_ok)
    inner_rec[n] = rec
check("L4 inner integrals verified (both cones, n = 0..%d)" % maxn,
      inner_ok,
      "int_0^inf Delta^n e^{i omega Delta - eta Delta} e^{s 2iq Delta} "
      "dDelta == n!/(eta - i(omega + s 2q))^{n+1}, s = -+1 -- convergent "
      "Piecewise branch checked symbolically with an exact-rational "
      "3-point backstop; the s = -1 form is the frozen docstring's "
      "recorded integral")
results["inner_integrals"] = inner_rec

# ============================== L5: p-branch delta support is EMPTY
stage("L5: p-branch Sokhotski delta support over the measure domain")
phi = sum(sp.Symbol("a%d" % k, real=True) * q**k for k in range(0, 4))
qf = sp.Symbol("q_f", real=True)
support_ok = True
supp_rec = {}
for n in range(0, maxn + 1):
    val = sp.integrate(phi * sp.DiracDelta(om + 2 * q, n), (q, 0, sp.oo))
    ok = sp.simplify(val) == 0
    root = sp.solve(om + 2 * qf, qf)
    ok_root = (len(root) == 1 and sp.simplify(root[0] + om / 2) == 0
               and bool(sp.simplify(root[0]).is_negative))
    support_ok = support_ok and ok and ok_root
    supp_rec[n] = {"integral_zero": bool(ok),
                   "support_point": str(root[0]),
                   "outside_domain": bool(ok_root)}
check("L5 p-branch absorptive support EMPTY on q in (0, inf), all n",
      support_ok,
      "delta^(n)(omega + 2q) support q = -omega/2 < 0 for omega > 0; the "
      "integral over the measure domain vanishes identically for every "
      "degree present -- the exclusion is KINEMATIC and termwise, not a "
      "cancellation")
results["p_support"] = supp_rec
val_m = sp.integrate(phi * sp.DiracDelta(om - 2 * q), (q, 0, sp.oo))
check("L5b m-branch support fires inside the domain (contrast)",
      sp.simplify(val_m - phi.subs(q, om / 2) / 2) == 0,
      "int_0^inf phi(q) delta(omega - 2q) dq == phi(omega/2)/2 -- the "
      "frozen extraction's support point; the cone asymmetry at "
      "omega > 0 is kinematic, exactly as the docstring records")

# ================================================== classification
stage("classification")
if support_ok and inner_ok and real_ok:
    classification = "P_BRANCH_KINEMATICALLY_NULL_INDEPENDENT_CONTENT"
elif not support_ok:
    classification = "P_BRANCH_SURVIVES"
else:
    classification = "P_BRANCH_UNINTERPRETABLE"
results["classification"] = classification
results["consequences"] = {
    "assembled_H4_Im": ("Im Sigma_R^{H4}(omega > 0) = A2 = "
                        "(-18*omega**4*u_b**4 + 220*omega**2*u_b**2 - "
                        "127)/(1280*pi) [d = 3] is COMPLETE from the m "
                        "cone alone: the p cone's delta support lies at "
                        "q = -omega/2, outside the measure domain, for "
                        "every Delta-degree present."),
    "p_information_content": ("NOT redundant: the p-cone coefficients "
                              "are INDEPENDENT of the m cone (mechanism "
                              "M1-M3, odd-derivative vertices).  The p "
                              "cone carries (i) the omega < 0 delta "
                              "support and (ii) its own principal-value "
                              "(dispersive) content.  Any future "
                              "Re Sigma_R / full G_R^TT assembly must "
                              "include the p cone EXPLICITLY -- it "
                              "cannot be reconstructed from the m cone "
                              "by conjugation."),
    "t3_05j_reading": ("T3-05J's 'the +2 bucket's coefficients are "
                       "absent from the assembled result' is EXPECTED "
                       "BEHAVIOR of the recorded derivation, not a "
                       "defect: the assembled object is Im(omega > 0), "
                       "which the m cone exhausts kinematically."),
    "u_b_status": ("unchanged: the u_b^2/u_b^4 dependence is a property "
                   "of the complete Im Sigma_R^{H4}(omega > 0); its "
                   "frame/assembly fate remains the keystone question "
                   "(T3-05I/J)."),
}
results["fences"] = ("no R'; no H^6; no keystone resummation; no u_b "
                     "interpretation beyond completeness; frozen "
                     "artifacts read-only; T3-05K/K2 untouched; W-0")
results["elapsed_s"] = round(time.time() - T0, 1)
json.dump(results, open(RESULT_PATH, "w"), indent=1)
print(f"\nCLASSIFICATION: {classification}")
print(f"wrote {RESULT_PATH}")
sys.exit(0 if all(c["pass"] for c in results["checks"]) else 2)
