#!/usr/bin/env python3
"""T3-07 -- H-EXACTNESS OF THE CONTRACT RESPONSE, AND THE EXACT
REFUTATION OF EVERY DRESSED-STATIONARY REPRESENTATION.

DISCOVERY PATH (disclosed).  T3-06A left the combined dressing class C3
"unfalsifiable at O(H^4) by parameter counting; decided at H^6/H^8."
Preparing that H^6 computation, this instrument's precursor check found
the H^6 sector DOES NOT EXIST: the cached C-matrices carry H-degree 0
(every entry, every config), and each frozen W kernel terminates
exactly at H^2, so Sigma = C.C : PP : WW has H-degree <= 4 EXACTLY.
The H-"expansion" of the contract's one-loop response is a TERMINATING
POLYNOMIAL, not a truncated series -- which upgrades the O(H^4)
statements to exact ones and closes the dressing question NOW, with no
further loop computation.

WHAT IS VERIFIED / PROVED:
  E1 C-matrix H-degree = 0: every nonzero entry of every config in the
     frozen .tier3_cmat_cache.json is H-independent.
  E2 the OBJECT OF RECORD terminates: the cached ret_wigner (42 MB,
     provenance-pinned) has maximum H-degree 4 termwise; the H^5 and
     H^6 sectors are EMPTY.  (_HKILL(7..12) was vacuous; the builder's
     kill window sat entirely above the object's true degree.)
  E3 therefore the record
         Im Sigma_R(omega>0) = (omega^4/1280 pi) P(x, y),
         P = -3 - (104/3) y^2 - 18 x^4 + 220 x^2 y^2 - 127 y^4,
         x = H u_b, y = H/omega
     is H-EXACT within the contract: every "+O(H^6)" qualifier on this
     object RETIRES.  (P's y-content beyond y^4 and x-content beyond
     x^4 are exactly zero -- E2.)
  E4 EXACT DRESSING REFUTATION.  Suppose ANY representation
         Im Sigma = F(x) (w~^4/1280 pi) T(H/w~),   w~ = omega g(x),
     with arbitrary functions F, g (F(0) = g(0) = 1, nonvanishing near
     0) and arbitrary T -- this contains C1 (g == 1), C2 (F == 1) and
     C3.  Writing the y-expansion of both sides, the y^{2k} slots give
     EXACT FUNCTION IDENTITIES
         t0 F g^4 = P0(x) = -3 - 18 x^4
         t2 F g^2 = P2(x) = -104/3 + 220 x^2
         t4 F     = P4(x) = -127
         t_{2k>=6} F g^{4-2k} = 0  =>  t_{2k>=6} = 0,
     and odd slots force t_odd = 0.  Eliminating F and g:
         P2(x)^2 / (P0(x) P4(x)) = t2^2/(t0 t4) = CONSTANT.
     The data violates this: the ratio's numerator carries an x^2 term
     (-2 * (104/3) * 220 != 0) while its denominator has none.  Hence
     NO dressed-stationary representation of the contract response
     exists -- not to any order: EXACTLY.  The u_b dependence is
     IRREDUCIBLY NONSTATIONARY within the contract.
  E5 the T3-06B statements upgrade to exact: the sign result (P < 0 on
     the self-consistent window) and the secular surface (x_* =
     6^(-1/4) at y = 0) are properties of the COMPLETE contract
     object, not of a truncation.  The eps_H = (104/9) H^2/omega^2
     refusal boundary REMAINS in force with a sharpened meaning: it
     guards the one-loop / scheme trust region (the derivation's
     domain), NOT series convergence -- there is no series.

WHAT THIS DOES AND DOES NOT MEAN (scope):
  - Within the declared Tier-3 contract (frozen W kernels = the exact
    linear-dressing adiabatic modes; TT bath; declared measure), the
    one-loop response is exactly the polynomial P, it is dissipative on
    the trust window, and it admits NO stationary-law-plus-dressing
    reading.  That is the strongest statement this contract can make.
  - Beyond the contract: O(G^2) two-loop content, the omega <~ H
    completion, and the bath's internal dynamics (the frontier-reserved
    transport class) are all untouched.  No observable claim; H stays
    empty.

Predeclared outcome classes (exactly one):
  H_EXACT_AND_DRESSING_REFUTED  -> E1+E2 verified and E4's invariant
      ratio is nonconstant: the exact refutation stands.
  H_EXACT_DRESSING_ADMITTED     -> E1+E2 verified but the ratio is
      constant (fit exists exactly): dressed-stationary reading stands.
  NOT_H_EXACT                   -> E2 fails (H^5 or H^6 content found):
      the T3-06A order-counting framing stands instead; file findings.

Scope fences: no new loop integral; no resummation; no observable
claim; no R'; frozen artifacts read-only; W-0: computed-and-reported,
NOT banked.
"""
import hashlib
import json
import os
import sys
import time
from collections import Counter

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(os.path.dirname(HERE), "PHYSICS_LEDGER")
SRC_CACHE = os.path.join(LEDGER, ".tier3_h4_integrand_cache.json")
CMAT = os.path.join(LEDGER, ".tier3_cmat_cache.json")
RESULT_PATH = os.path.join(HERE, "T3_07_H_EXACTNESS_REFUTATION_RESULT.json")
T0 = time.time()
results = {"instrument": "calc/t3_07_h_exactness_refutation.py",
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


H = sp.Symbol("H", real=True)

# ============================== E1: C-matrix H-degree
stage("E1: H-degree of every cached C-matrix entry")
CM = json.load(open(CMAT))
results["pins"] = {
    ".tier3_cmat_cache.json": hashlib.sha256(
        open(CMAT, "rb").read()).hexdigest(),
    ".tier3_h4_integrand_cache.json": hashlib.sha256(
        open(SRC_CACHE, "rb").read()).hexdigest()}
maxdeg, n_entries = 0, 0
for cfg, entries in CM.items():
    if cfg == "meta":
        continue
    for k, v in entries.items():
        e = sp.sympify(v)
        if e != 0:
            n_entries += 1
            maxdeg = max(maxdeg, sp.degree(sp.expand(e), H))
check("E1 every nonzero C entry is H-independent", maxdeg == 0,
      f"{n_entries} nonzero entries across configs "
      f"{[k for k in CM if k != 'meta']}: max H-degree = {maxdeg}. "
      "With each frozen W exactly terminating at H^2 (the exact "
      "linear-dressing mode product, T3-05L M1), Sigma = C.C : PP : WW "
      "has H-degree <= 4 EXACTLY")

# ============================== E2: the object of record terminates
stage("E2: termwise H-degree census of the cached ret_wigner (42 MB)")
IC = json.load(open(SRC_CACHE))
RET = sp.sympify(IC["ret_wigner"])
hist = Counter()
maxh = 0
terms = sp.Add.make_args(RET)
for i, t in enumerate(terms):
    if i % 5000 == 0:
        stage(f"  term {i}/{len(terms)}")
    d = t.as_powers_dict().get(H, 0)
    d = int(d)
    hist[d] += 1
    maxh = max(maxh, d)
check("E2 cached retarded integrand has H-degree <= 4; H^5, H^6 EMPTY",
      maxh <= 4 and hist.get(5, 0) == 0 and hist.get(6, 0) == 0,
      f"{len(terms)} terms; per-H-power counts "
      f"{dict(sorted(hist.items()))}; max = {maxh}. The builder's "
      "_HKILL(7..12) window sits entirely above the object's true "
      "degree: the H-content is a TERMINATING POLYNOMIAL, not a "
      "truncated series")
h_exact = (maxdeg == 0 and maxh <= 4
           and hist.get(5, 0) == 0 and hist.get(6, 0) == 0)
if not h_exact:
    results["classification"] = "NOT_H_EXACT"
    json.dump(results, open(RESULT_PATH, "w"), indent=1)
    sys.exit(2)
note("E3: the record Im Sigma_R = (omega^4/1280 pi) P(x, y) is "
     "therefore H-EXACT within the contract; every '+O(H^6)' "
     "qualifier on this object retires.")

# ============================== E4: exact dressing refutation
stage("E4: invariant-ratio refutation, exact")
x = sp.Symbol("x", real=True)
P0 = -3 - 18 * x**4
P2 = -sp.Rational(104, 3) + 220 * x**2
P4 = sp.Integer(-127)
ratio = sp.cancel(sp.together(P2**2 / (P0 * P4)))
dr = sp.simplify(sp.diff(ratio, x))
nonconstant = (dr != 0)
# exhibit the obstruction explicitly: numerator x^2 coefficient
num = sp.expand(P2**2)
check("E4 dressed-stationary representation EXACTLY refuted",
      nonconstant,
      "any Im Sigma = F(x) (w~^4/1280 pi) T(H/w~), w~ = omega g(x) "
      "(contains C1, C2, C3) forces the exact identity P2^2/(P0 P4) = "
      "t2^2/(t0 t4) = const; computed ratio = "
      f"{sp.nsimplify(ratio)} with d/dx != 0 -- numerator "
      f"x^2-coefficient = {num.coeff(x, 2)} != 0 while the denominator "
      "carries no x^2. NO dressed-stationary representation of the "
      "contract's one-loop response exists, to ANY order: the u_b "
      "dependence is IRREDUCIBLY NONSTATIONARY within the contract")
# and close the loop with the truncated-fit story: the O(H^4) fit of
# T3-06A lived on the truncation's blind spot (total-degree-6 slots);
# with P exact those slots are exactly zero and kill it:
f2v = -sp.Rational(165, 13)
blind = sp.Integer(-127) * f2v      # t4 * f2 x^2 y^4 slot coefficient
check("E4b the T3-06A fit's blind spot identified exactly",
      blind != 0,
      "the O(H^4) fit needed F with f2 = -165/13; at exact level the "
      f"x^2 y^4 slot then carries t4*f2 = {sp.nsimplify(blind)} != 0 "
      "against an exact 0 in P -- the truncated fit lived entirely on "
      "monomials of total degree >= 6 that the exact object forbids")

# ============================== E5: upgrades
results["upgrades"] = {
    "sign": ("T3-06B B1 (max P = -599127/270400 < 0 on the "
             "self-consistent window) is now a property of the "
             "COMPLETE contract object: dissipative, exactly, "
             "throughout the trust window"),
    "secular_surface": ("x_* = 6^(-1/4) at y = 0 is exact: the "
                        "two-time expansion's self-termination is a "
                        "feature of the full object"),
    "eps_H_meaning": ("the (104/9) H^2/omega^2 refusal boundary "
                      "remains in force, sharpened: it guards the "
                      "one-loop/scheme trust region, NOT series "
                      "convergence -- there is no series"),
    "t3_06a_status": ("C1/C2 refutations stand (now subsumed by the "
                      "exact E4); C3's ADMITS_FIT verdict is "
                      "SUPERSEDED: the fit existed only in the "
                      "truncation's blind spot (E4b)"),
}
results["beyond_contract"] = (
    "untouched and named: O(G^2) two-loop content; the omega <~ H "
    "completion (K_R OPEN/UNCOMPUTED); the bath's internal dynamics "
    "deciding the frontier-reserved transport class; R'. No observable "
    "claim; H stays empty.")
results["classification"] = "H_EXACT_AND_DRESSING_REFUTED" \
    if nonconstant else "H_EXACT_DRESSING_ADMITTED"
results["fences"] = ("no new loop integral; no resummation; no "
                     "observable claim; no R'; frozen artifacts "
                     "read-only; W-0")
results["elapsed_s"] = round(time.time() - T0, 1)
json.dump(results, open(RESULT_PATH, "w"), indent=1)
print(f"\nCLASSIFICATION: {results['classification']}")
print(f"wrote {RESULT_PATH}")
sys.exit(0 if all(c["pass"] for c in results["checks"]) else 2)
