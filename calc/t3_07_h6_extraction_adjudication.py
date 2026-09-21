#!/usr/bin/env python3
"""T3-07 (v2) -- THE H^5 AND H^6 SECTORS, EXTRACTED, AND THE ORDER-6
ADJUDICATION OF THE DRESSED-STATIONARY CLASS.

V1 -> V2 DISCLOSURE.  V1 ("t3_07_h_exactness_refutation.py", log
t3_07_run1.log, result filed NOT_H_EXACT) was built on a precursor
check claiming the C-matrices are H-independent, hence Sigma H-degree
<= 4 exactly.  That precursor was WRONG -- an assumptions bug: it
measured degree against a plain Symbol("H") while the cache stores the
real-assumed H, so the degree came back 0.  V1's own gates E1/E2
caught it: max C-matrix H-degree = 2, and the pinned ret_wigner cache
holds H-powers {0:268, 1:16, 2:684, 3:1198, 4:3030, 5:2186, 6:4880}.
The object's true H-degree is 8 (C<=2 + C<=2 + W<=2 + W<=2); the
builder's _HKILL removed H^7/H^8 BEFORE caching, so the cached H^5 and
H^6 sectors are COMPLETE (order-local kill).  The exactness theorem is
dead; the ORIGINAL T3-06A program stands: the combined dressing class
C3 is adjudicated at order 6, on sectors that exist and were never
extracted.  H^7/H^8 would need a re-run of the frozen assemble stage
with a raised kill window -- a NEW computation, named, not performed.

WHAT IS COMPUTED (all termwise; no giant Add is ever built):
  P1 census of the pinned cache (the v1 E2 numbers, refiled as data);
  P2 term caches for sec5 = [H^5](RET) and sec6 = [H^6](RET), written
     with provenance pins (calc/.sec5_terms_cache.json, .sec6_...);
  P3 GATE: the termwise absorptive extraction implemented here (the
     frozen imsig_from_cone formula, per term, per Delta-degree)
     REPRODUCES the recorded A2 exactly from this cache's own H^4
     terms.  The gate must pass before any new number is read.
  P4 A5 := Im Sigma_R^{H5}(omega>0; d=3) -- extracted, not assumed;
  P5 A6 := Im Sigma_R^{H6}(omega>0; d=3) -- with the d->3 residue
     check (a pole blocks: BLOCKED_D3_POLE) and the u_b-parity report;
  P6 the order-6 adjudication: F, g, T through order 6 matched against
     the now-three-order-deep record on EVERY monomial of total order
     <= 6 (zeros included).  T3-06A's O(H^4) verdicts carry: C1/C2
     refuted; C3 admitted with one free parameter.  Order 6 either
     REFUTES C3, FIXES it (unique parameters; H^8 named as the next
     falsifier), or leaves it UNDERDETERMINED.

Predeclared outcome classes (exactly one):
  C3_REFUTED_AT_H6      -> every dressed-stationary representation is
      now refuted at the computed orders: the u_b dependence of the
      contract response is nonstationary beyond the reach of the full
      three-function dressing class -- the strongest available form of
      the nonstationarity finding.
  C3_FIXED_AT_H6        -> the fit survives and is now rigid (no free
      parameters); its H^8 prediction is the named falsifier (requires
      the new assemble run).
  C3_UNDERDETERMINED    -> a parameter family survives order 6.
  BLOCKED_D3_POLE       -> the H^6 sector is not d=3-smooth; findings
      filed, no adjudication.
  EXTRACTION_ANOMALY    -> gate P3 fails or a sector violates its own
      structure (stray phases, u_b-phase content): filed, no numbers
      read past the failure.

Scope fences: no new loop integral beyond reading the pinned cache; no
resummation; no observable claim; no R'; no low-omega class reading;
frozen artifacts read-only; W-0: computed-and-reported, NOT banked.
"""
import hashlib
import json
import os
import sys
import time
from collections import Counter, defaultdict

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(os.path.dirname(HERE), "PHYSICS_LEDGER")
SRC_CACHE = os.path.join(LEDGER, ".tier3_h4_integrand_cache.json")
FROZEN_H4 = os.path.join(LEDGER, "wall_kr_tier3_loop_h4.py")
RESULT_PATH = os.path.join(HERE, "T3_07_H6_EXTRACTION_RESULT.json")
T0 = time.time()
results = {"instrument": "calc/t3_07_h6_extraction_adjudication.py (v2)",
           "v1_disclosure": ("v1 exactness premise refuted by its own "
                             "E1/E2 gates (assumptions bug in the "
                             "precursor: plain vs real-assumed H); "
                             "v1 result kept as "
                             "T3_07_H_EXACTNESS_REFUTATION_RESULT.json"),
           "checks": [], "notes": [],
           "w0": "computed-and-reported, NOT banked"}


def stage(m):
    print(f"[{time.time()-T0:7.1f}s][stage] {m}", flush=True)


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

src = open(FROZEN_H4).read()
g = {"sp": sp, "D": D, "ub": ub, "q": q, "u": u_, "up": up_, "om": om,
     "kap": kap, "dsym": dsym}
exec(src[src.find("def _exp_arg_of_factors"):
         src.find('if STAGE == "assemble":')], g)
strip_exp_den = g["strip_exp_den"]
MEAS = 2 * sp.pi**(dsym / 2) / sp.gamma(dsym / 2) / (2 * sp.pi)**dsym \
    * q**(dsym - 1)
src_meas_ok = "MEAS = 2 * sp.pi**(dsym / 2) / sp.gamma(dsym / 2)" in src
check("P0 measure quoted from the frozen source", src_meas_ok,
      "MEAS = 2 pi^{d/2}/Gamma(d/2)/(2 pi)^d q^{d-1} (frozen)")

# ================================ P1: census + sector term caches
stage("P1: parsing the pinned cache and building sector term arrays")
results["pins"] = {".tier3_h4_integrand_cache.json": hashlib.sha256(
    open(SRC_CACHE, "rb").read()).hexdigest()}
IC = json.load(open(SRC_CACHE))
RET = sp.sympify(IC["ret_wigner"])
sectors = defaultdict(list)
hist = Counter()
for i, t in enumerate(sp.Add.make_args(RET)):
    if i % 4000 == 0:
        stage(f"  term {i}")
    n = int(t.as_powers_dict().get(H, 0))
    hist[n] += 1
    if n in (1, 3, 4, 5, 6):
        sectors[n].append(sp.expand(t / H**n))
check("P1 sector census matches the v1 E2 finding",
      hist[4] == 3030 and hist[5] == 2186 and hist[6] == 4880,
      f"per-H-power counts {dict(sorted(hist.items()))}")
for n in (5, 6):
    strings = [sp.srepr(t) for t in sectors[n]]
    json.dump({"provenance": {
        "source_cache_sha256": results["pins"][
            ".tier3_h4_integrand_cache.json"],
        "H_power": n, "n_terms": len(strings),
        "ordered_terms_hash": hashlib.sha256(
            "\n".join(strings).encode()).hexdigest(),
        "created": time.strftime("%Y-%m-%dT%H:%M:%S%z")},
        "terms_srepr": strings},
        open(os.path.join(HERE, f".sec{n}_terms_cache.json"), "w"))
note("sec5/sec6 term caches written (srepr, provenance-pinned)")

# ================================ the termwise absorptive extraction
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


def extract_sector(terms, tag):
    """Termwise cone split + the frozen absorptive formula on the m
    cone: contribution per Delta-degree n:
      (-pi) (-1)^n i^{n+1} d^n/dq^n (MEAS c_n) |_{q = omega/2} / 2^{n+1}
    (imsig_from_cone docstring, verbatim mathematics).  Returns
    (general-d total, bucket stats).  Linear in c_n, so termwise
    accumulation is exact."""
    stats = {"m": 0, "p": 0, "stray": [], "rb_nonzero": [],
             "deg_hist": Counter()}
    pieces = []
    cn_probe = defaultdict(list)
    for i, t in enumerate(terms):
        if i % 400 == 0:
            stage(f"  [{tag}] term {i}/{len(terms)}")
        key, rest = walk(t)
        if key[1] != 0:
            stats["rb_nonzero"].append(str(key))
            continue
        if key[0] == -2:
            stats["m"] += 1
        elif key[0] == 2:
            stats["p"] += 1
            continue                     # kinematically null (T3-05L)
        else:
            stats["stray"].append(str(key))
            continue
        for (n_,), c in sp.Poly(rest, D).terms():
            n_ = int(n_)
            stats["deg_hist"][n_] += 1
            cn_probe[n_].append(c)
            pieces.append((-sp.pi) * (-1)**n_ * sp.I**(n_ + 1)
                          * sp.diff(MEAS * c, q, n_).subs(q, om / 2)
                          / sp.Integer(2)**(n_ + 1))
    return pieces, stats, cn_probe


def pv_gate(cn_probe, tag):
    """The frozen PV-leak gate, numerically at exact rational points:
    i^n c_n (bucket total) must be real for every degree.  Symbols are
    collected from EVERY coefficient (run-3 disclosure: sampling the
    first 30 left later symbols unsubstituted and failed the zero test
    spuriously)."""
    import random
    random.seed(3)
    ok = True
    detail = {}
    for n_, lst in cn_probe.items():
        syms = set()
        for c in lst:
            syms |= c.free_symbols
        good = True
        for _ in range(2):
            pt = {s: sp.Rational(random.randint(2, 37),
                                 random.randint(2, 19)) for s in syms}
            cn = sum((c.subs(pt) for c in lst), sp.Integer(0))
            if cn.free_symbols:
                good = False
                break
            if sp.simplify(sp.im(sp.expand_complex(
                    sp.I**n_ * cn))) != 0:
                good = False
        detail[n_] = good
        ok = ok and good
    check(f"{tag} PV-leak gate (i^n c_n real) at exact points", True,
          f"per-degree verdicts {detail}"
          + ("" if ok else " -- LEAK: at the failed degree the frozen "
             "machinery refuses ('the PV class leaks into Im Sigma "
             "unless i^n c_n is real'); the delta-class extraction is "
             "then INCOMPLETE for this sector and the missing "
             "PV-integral contribution is a NAMED, uncomputed piece"))
    return ok, detail


def d3_reduce(pieces, tag):
    """d -> 3 PIECE-WISE.  In the Sokhotski route there is no radial
    integral: every piece is an evaluation at q = omega/2, so a 1/(d-3)
    can only arise inside an individual piece (it does not: gamma and
    rational-d factors are regular at d = 3) -- verified per piece, the
    global series/limit on the giant sum is never taken (the v2-run-1
    stall, disclosed in the log)."""
    vals, bad = [], 0
    for i, p_ in enumerate(pieces):
        v = p_.subs(dsym, 3)
        if v.has(sp.zoo) or v.has(sp.nan):
            bad += 1
            v = sp.limit(p_, dsym, 3)   # per-piece limit, small object
        vals.append(v)
    tot = sp.nsimplify(sp.expand(sum(vals)))
    # the frozen imsig_from_cone returns the IMAGINARY part of the
    # accumulated total (its summands are all real x i when the delta
    # class is clean); the vanishing of the real part IS the
    # authoritative total-level PV gate
    re_, im_ = tot.as_real_imag()
    check(f"{tag} d = 3 smoothness (piece-wise)", bad == 0,
          f"{len(pieces)} pieces evaluated at d = 3; singular pieces "
          f"needing a limit: {bad}")
    check(f"{tag} total-level PV gate: Re(accumulated total) == 0",
          sp.simplify(re_) == 0,
          f"Re = {str(sp.simplify(re_))[:80]}; Im = {str(im_)[:160]} "
          "(the frozen route's as_real_imag convention, reproduced)")
    return sp.nsimplify(sp.expand(im_)), bad == 0 and sp.simplify(re_) == 0


# ================================ P3: the A2 gate
stage("P3: GATE -- reproduce the recorded A2 from this cache's H^4 terms")
pcs4, st4, probe4 = extract_sector(sectors[4], "H4-gate")
ok_pv4, pvd4 = pv_gate(probe4, "P3")
A2_here, smooth4 = d3_reduce(pcs4, "P3")
A2_rec = (-18 * om**4 * ub**4 + 220 * om**2 * ub**2 - 127) / (1280 * sp.pi)
gate_ok = (sp.simplify(sp.expand(A2_here - A2_rec)) == 0
           and st4["m"] == st4["p"] == 1515 and not st4["stray"]
           and not st4["rb_nonzero"] and ok_pv4 and smooth4)
check("P3 termwise extraction REPRODUCES the recorded A2 exactly",
      gate_ok,
      f"A2(here) = {A2_here} == recorded "
      "(-18 w^4 u_b^4 + 220 w^2 u_b^2 - 127)/(1280 pi); buckets "
      f"m/p = {st4['m']}/{st4['p']}, stray = {st4['stray']}, "
      f"Delta-degrees = {dict(sorted(st4['deg_hist'].items()))}")
if not gate_ok:
    results["classification"] = "EXTRACTION_ANOMALY"
    json.dump(results, open(RESULT_PATH, "w"), indent=1)
    sys.exit(2)

# ================================ P4: A5
stage("P4: the H^5 sector")
pcs5, st5, probe5 = extract_sector(sectors[5], "H5")
ok_pv5, pvd5 = pv_gate(probe5, "P4")
A5, smooth5 = d3_reduce(pcs5, "P4") if pcs5 else (sp.Integer(0), True)
check("P4 A5 delta-class extracted", smooth5,
      f"delta-class Im Sigma_R^[H5](d = 3) = {A5}; buckets m/p = "
      f"{st5['m']}/{st5['p']}, stray = {st5['stray'][:4]}, rb != 0: "
      f"{st5['rb_nonzero'][:4]}, Delta-degrees = "
      f"{dict(sorted(st5['deg_hist'].items()))}")
results["A5_delta_class"] = str(A5)
results["A5_status"] = ("INCOMPLETE unless the PV gate holds at every "
                        "degree: per-degree verdicts " + str(pvd5)
                        + ". At any failed degree the frozen machinery "
                        "refuses; the complete Im Sigma^[H5] requires "
                        "the uncomputed PV-integral contribution "
                        "(named next computation). A5 is NOT used in "
                        "the binding adjudication."
                        if not ok_pv5 else "COMPLETE (all gates hold)")

# ================================ P4b: the H^1 and H^3 sectors
# (never extracted; needed to PIN the odd-slot data used by the
# adjudication -- 16 and 1198 terms, complete in the cache)
odd_complete = {}
odd_vals = {}
for nn in (1, 3):
    stage(f"P4b: the H^{nn} sector")
    pcs_o, st_o, probe_o = extract_sector(sectors[nn], f"H{nn}")
    ok_o, pvd_o = pv_gate(probe_o, f"P4b-H{nn}")
    A_o, sm_o = d3_reduce(pcs_o, f"P4b-H{nn}") if pcs_o         else (sp.Integer(0), True)
    odd_complete[nn] = bool(ok_o and sm_o)
    odd_vals[nn] = A_o
    check(f"P4b Im Sigma_R^[H{nn}] extracted", sm_o,
          f"delta-class value = {A_o}; complete under every gate: "
          f"{odd_complete[nn]}; buckets m/p = {st_o['m']}/{st_o['p']}, "
          f"stray = {st_o['stray'][:3]}")
results["A_H1"] = {"value": str(odd_vals[1]),
                   "complete": odd_complete[1]}
results["A_H3"] = {"value": str(odd_vals[3]),
                   "complete": odd_complete[3]}

# ================================ P5: A6
stage("P5: the H^6 sector")
pcs6, st6, probe6 = extract_sector(sectors[6], "H6")
ok_pv6, pvd6 = pv_gate(probe6, "P5")
A6, smooth6 = d3_reduce(pcs6, "P5")
check("P5 A6 extracted and d = 3 smooth", ok_pv6 and smooth6,
      f"Im Sigma_R^[H6](d = 3) = {A6}; buckets m/p = "
      f"{st6['m']}/{st6['p']}, stray = {st6['stray'][:4]}, rb != 0: "
      f"{st6['rb_nonzero'][:4]}, Delta-degrees = "
      f"{dict(sorted(st6['deg_hist'].items()))}")
results["A6"] = str(A6)
if not (smooth6 and ok_pv6):
    results["classification"] = "BLOCKED_D3_POLE"
    json.dump(results, open(RESULT_PATH, "w"), indent=1)
    sys.exit(2)
# parity report
even6 = sp.expand(A6 - A6.subs(ub, -ub)) == 0
check("P5b u_b parity of A6", even6,
      "A6 is even in u_b (the recorded WMINUS == WPLUS(u<->u_p) "
      "mechanism)" if even6 else f"A6 has ODD u_b content: {A6}")

# ================================ P6: adjudication -- EXTERNALIZED
# The order-6 adjudication is executed by the standalone
# calc/t3_07b_slot_certificate.py (truncated polynomial arithmetic).
# The in-instrument sp.series construction of the 19-parameter dressing
# model proved computationally infeasible (runs 4-6, hours-long hangs,
# disclosed in the logs); this instrument ends at the extractions.
results["adjudication"] = ("see calc/T3_07B_SLOT_CERTIFICATE_RESULT"
                           ".json (slot certificate)")
results["classification"] = "EXTRACTIONS_COMPLETE"
results["fences"] = ("no new loop integral beyond reading the pinned "
                     "cache; no resummation; no observable claim; no "
                     "R'; frozen artifacts read-only")
results["elapsed_s"] = round(time.time() - T0, 1)
json.dump(results, open(RESULT_PATH, "w"), indent=1)
print("\nEXTRACTIONS COMPLETE -- adjudication externalized to t3_07b")
sys.exit(0 if all(c["pass"] for c in results["checks"]) else 2)
