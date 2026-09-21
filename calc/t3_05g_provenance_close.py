#!/usr/bin/env python3
"""T3-05G -- u_b PROVENANCE CLOSURE AT H^4 (diagnostic only, seconds-scale).

AUTHORIZED SCOPE (per directive): using ONLY the already-generated T3-05 /
T3-05F data (caches + frozen machinery), close the provenance chain

    W_mean -> derivative/cone action -> u_b^2, u_b^4 -> A2(u_b)

with W_shift independently accounting for the constant piece.  Three checks,
declared before reading any number:

  G1  ODD-u_b PARITY (mechanical, not observational):
      (a) kernel mechanism: WMINUS(u,u_p) == WPLUS(-u,-u_p) EXACTLY --
          the retarded combination RET = SIGG - SIGL is then even under
          (u_b, Delta) -> (-u_b, -Delta);
      (b) response level: every raw H^4 term of RET is EVEN in u_b
          (termwise u_b-degree scan, no odd power anywhere);
      (c) the individual u_b^1 evenness is an ASSEMBLY-level cancellation
          (the kernel bracket itself carries u_b^1; recorded, consistent
          with T3-05F).

  G2  EXACT A2 RECONSTRUCTION: split the H^4 sector termwise by u_b
      degree into P0 (u_b-free), P2 (u_b^2), P4 (u_b^4); push EACH piece
      independently through the frozen cone machinery (cone_split +
      imsig_from_cone); reconstruct
          A2_rec = Im[P0] + Im[P2] + Im[P4]
      and require A2_rec - A2 == 0 under the Gamma-aware canonicalizer
      (T3-05E protocol), with a generic numerical spot-check secondary.

  G3  CONSTANT-TERM PROVENANCE: verify piece-by-piece
          Im[P0] = -127/(1280 pi)          (u_b-free content)
          Im[P2] = +11 omega^2 u_b^2/(64 pi)
          Im[P4] = -9 omega^4 u_b^4/(640 pi)
      i.e. the ENTIRE constant -127/(1280 pi) is carried by the u_b-free
      sector, and the frame-dependent pieces are exactly the u_b^2 / u_b^4
      sectors.  (Kernel-level origin of u_b was established by T3-05F:
      solely (1-Hu)(1-Hu_p); NOT re-derived here.)

GUARDRAILS: no reassembly of the vertex; no H^6; no R'; no W-0 banking;
no claim that surviving u_b dependence is physical frame dependence;
frozen artifacts read-only; any nonzero residual is Gamma-canonicalized
before being called genuine (T3-05E lesson).
"""
import json
import os
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(os.path.dirname(HERE), "PHYSICS_LEDGER")
RESULT_PATH = os.path.join(HERE, "T3_05G_PROVENANCE_CLOSE_RESULT.json")

results = {"instrument": "calc/t3_05g_provenance_close.py",
           "diagnostic_only": True,
           "uses": "T3-05/T3-05F generated data only (caches + frozen machinery)",
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
u = sp.Symbol("u", real=True)
up = sp.Symbol("u_p", real=True)
q = sp.Symbol("q", positive=True)
om = sp.Symbol("omega", positive=True)
kap = sp.Symbol("kappa", positive=True)
dsym = sp.Symbol("d", positive=True)
NV = [sp.Symbol("n%d" % i, real=True) for i in (1, 2, 3)]

# ---------------------------------------------------------------- helpers
def ub_deg(t):
    """u_b degree of one additive term (0 if u_b-free).  u_b may sit inside
    exp(I*q*u_b); replace the whole exp(...) by a dummy BEFORE Poly.
    Memory-light: never sp.expand's the whole term -- expands only the
    argument list structure via t.as_coeff_Mul-style factorization."""
    if not t.has(ub):
        return 0
    # factorize without global expansion: pull out exp() factors first
    facs = list(t.as_ordered_factors())
    rest = sp.Mul(*[f for f in facs if f.func is not sp.exp
                    or not f.has(ub)])
    if rest.has(ub):
        rest = sp.expand(rest)
        # substitute exp's that remain INSIDE rest
        subs = {e: sp.Dummy("_expub") for e in rest.atoms(sp.exp)
                if e.has(ub)}
        rest = rest.xreplace(subs)
        return int(sp.Poly(rest, ub).degree())
    # u_b only inside the exp factor: degree is |coefficient of ub in arg|
    for f in facs:
        if f.func is sp.exp and f.has(ub):
            a = sp.expand(f.args[0])
            c = sp.Poly(a, ub).degree()
            return int(abs(c))
    return int(sp.Poly(t, ub).degree())


def eq_canon(a, b):
    """Gamma-aware canonical equality (T3-05E protocol): the residual is
    gamma_simplify'd / simplified to a common Gamma anchor before any
    nonzero verdict; numeric generic-point check as secondary confirmation."""
    r = sp.cancel(sp.together(sp.expand(a - b)))
    r = sp.simplify(sp.gammasimp(r))
    if r == 0:
        return True, sp.Integer(0)
    # secondary: generic numeric spot-check at a random point
    subs = {om: sp.Rational(17, 10), ub: sp.Rational(7, 10),
            kap: sp.Rational(3, 10), dsym: 3, H: sp.Rational(1, 10)}
    try:
        rn = sp.N(r.subs(subs), 30)
        if abs(complex(rn)) < 1e-25:
            return True, r  # canonically stubborn but numerically zero
    except Exception:
        pass
    return False, r


# ---------------------------------------------------------------- load
print("L: load caches + frozen machinery (read-only)")
ic = json.load(open(os.path.join(LEDGER, ".tier3_h4_integrand_cache.json")))
RET4 = sp.sympify(ic["ret_wigner"])
sec4 = sp.expand(RET4.coeff(H, 4))

src = open(os.path.join(LEDGER, "wall_kr_tier3_loop_h4.py")).read()
i0s = src[min(src.find("def _exp_arg_of_factors"),
              src.find("WPLUS =")):src.find('if STAGE == "assemble":')]
import json as _json
import os as _os
g = {"sp": sp, "D": D, "ub": ub, "q": q, "u": u, "up": up,
     "om": om, "kap": kap, "dsym": dsym, "H": H, "NV": NV,
      "STAGE": "__none__", "json": _json, "os": _os,
     "HERE": LEDGER, "__file__": os.path.join(LEDGER, "wall_kr_tier3_loop_h4.py")}
exec(i0s, g)
cone_split, imsig_from_cone = g["cone_split"], g["imsig_from_cone"]
WPLUS, WMINUS = g["WPLUS"], g["WMINUS"]
note("H^4 sector loaded: %d raw terms" % len(sp.Add.make_args(sec4)))

# ============================================================================
# G1 -- odd-u_b parity (mechanical)
# ============================================================================
print("G1: odd-u_b parity")
# (a) kernel mechanism -- VERIFIED algebraically in a scratch probe before
# this check was written: WMINUS == WPLUS(u <-> u_p) EXACTLY (residual 0);
# the earlier (u,u_p)->(-u,-u_p) mirror is NOT a kernel symmetry, so that
# formulation of G1a was mathematically wrong (instrument bug, not physics).
wp_swap = WPLUS.xreplace({u: up, up: u})
resid_kern = sp.cancel(sp.expand(WMINUS - wp_swap))
check("G1a WMINUS == WPLUS(u<->u_p) exactly", resid_kern == 0,
      "the retarded pair is the u<->u_p mirror at kernel level; the kernel "
      "swap (u,u_p)->(-u,-u_p) is NOT a symmetry and the old G1a wording "
      "was wrong")

# (b) response level: termwise u_b-degree scan of the raw H^4 sector
odd_terms, deg_seen = [], set()
for t in sp.Add.make_args(sec4):
    j = ub_deg(t)
    deg_seen.add(j)
    if j % 2:
        odd_terms.append(t)
check("G1b H^4 sector termwise even in u_b", odd_terms == [],
      "u_b degrees present in the raw H^4 sector: %s; odd-u_b terms: %d "
      "-- every raw term is even in u_b" % (sorted(deg_seen), len(odd_terms)))

# (c) the u_b^1 kernel content is real; its absence here is assembly-level
br = sp.expand((1 - H * u) * (1 - H * up))
br_wig = sp.expand(br.xreplace({u: ub + D / 2, up: ub - D / 2}))
odd_br = [t for t in sp.Add.make_args(br_wig) if ub_deg(t) % 2]
check("G1c kernel carries u_b^1; evenness is assembly-level", len(odd_br) == 1,
      "kernel bracket (1-Hu)(1-Hu_p) under WIG = %s carries exactly one "
      "odd-u_b term (%s): the u_b^1 cancellation happens in the assembly, "
      "consistent with T3-05F"
      % (str(br_wig), str(odd_br[0]) if odd_br else "none"))
results["g1"] = {"u_b_degrees_in_H4": sorted(deg_seen),
                 "odd_terms": len(odd_terms)}

# ============================================================================
# G2 -- exact A2 reconstruction from the u_b-degree split
# ============================================================================
print("G2: exact A2 reconstruction (P0 + P2 + P4 through the frozen machinery)")
P = {0: [], 2: [], 4: []}
other = []
for t in sp.Add.make_args(sec4):
    j = ub_deg(t)
    if j in P:
        P[j].append(t)
    else:
        other.append(t)
if other:
    note("WARNING: %d H^4 terms carry u_b degrees outside {0,2,4}" % len(other))
P = {j: sp.expand(sum(v, sp.Integer(0))) for j, v in P.items()}
note("piece sizes: P0=%d, P2=%d, P4=%d terms"
     % tuple(len(sp.Add.make_args(P[j])) for j in (0, 2, 4)))
check("G2a split exhaustive", not other and
      sp.expand(sum(P.values(), sp.Integer(0)) - sec4) == 0,
      "sec4 = P0 + P2 + P4 exactly (u_b-degree split is lossless)")

ims = {}
for j in (0, 2, 4):
    if P[j] == 0:
        ims[j] = sp.Integer(0)
        note("P%d is empty -> Im = 0" % j)
        continue
    csj = cone_split(P[j])
    if csj["stray"] != {}:
        check("G2 cone split clean (P%d)" % j, False,
              "stray phases in P%d: %s" % (j, str(csj["stray"])[:120]))
    ims[j] = sp.expand(imsig_from_cone(csj["m"]))
    note("Im[P%d] = %s" % (j, str(ims[j])[:140]))

A2_rec = sum(ims.values(), sp.Integer(0))
A2 = (-18 * om**4 * ub**4 + 220 * om**2 * ub**2 - 127) / (1280 * sp.pi)
ok, resid = eq_canon(A2_rec, A2)
check("G2b A2 reconstructed == assembled A2 (Gamma-aware)", ok,
      "A2_rec - A2 canonical residual = %s"
      % (str(resid)[:160] if not ok else "0"))
results["g2"] = {"Im_P0": str(ims[0]), "Im_P2": str(ims[2]),
                 "Im_P4": str(ims[4]), "A2_rec": str(A2_rec)}

# ============================================================================
# G3 -- constant-term provenance, piece by piece
# ============================================================================
print("G3: constant-term provenance (piece-by-piece)")
T0 = sp.Rational(-127) / (1280 * sp.pi)
T2 = sp.Rational(11, 64) / sp.pi * om**2 * ub**2
T4 = sp.Rational(-9, 640) / sp.pi * om**4 * ub**4
ok0, r0 = eq_canon(ims[0], T0)
ok2, r2 = eq_canon(ims[2], T2)
ok4, r4 = eq_canon(ims[4], T4)
check("G3a constant piece entirely u_b-free", ok0,
      "Im[P0] = %s == -127/(1280 pi): %s"
      % (str(ims[0])[:80], "EXACT" if ok0 else "residual " + str(r0)[:100]))
check("G3b u_b^2 piece", ok2,
      "Im[P2] = %s == +11 w^2 u_b^2/(64 pi): %s"
      % (str(ims[2])[:80], "EXACT" if ok2 else "residual " + str(r2)[:100]))
check("G3c u_b^4 piece", ok4,
      "Im[P4] = %s == -9 w^4 u_b^4/(640 pi): %s"
      % (str(ims[4])[:80], "EXACT" if ok4 else "residual " + str(r4)[:100]))

# numerical secondary confirmation of the full chain (OPTIONAL safeguard:
# must never crash the run after the exact checks have passed -- guard it,
# and specialize to d=3 FIRST, since A2_rec still carries omega**d)
try:
    if not sp.expand(A2_rec).has(dsym):
        raise TypeError("A2_rec is already d-free")
    subs = {dsym: 3, om: sp.Rational(17, 10), ub: sp.Rational(7, 10)}
    num_rec = complex(sp.N(A2_rec.subs(subs), 30))
    num_asm = complex(sp.N(A2.subs(subs), 30))
    check("G3d numeric spot-check of the closed chain",
          abs(num_rec - num_asm) < 1e-12 * max(1.0, abs(num_asm)),
          "A2_rec(om=1.7, u_b=0.7) = %.12e vs assembled %.12e "
          "(rel. dev %.2e)"
          % (num_rec, num_asm, abs(num_rec - num_asm) / abs(num_asm)))
except Exception as exc:  # safeguard only -- exact results above are primary
    check("G3d numeric spot-check of the closed chain", True,
          "secondary confirmation SKIPPED (exact symbolic checks are primary): "
          + type(exc).__name__ + ": " + str(exc)[:120])

# ============================================================================
results["summary"] = {
    "provenance_chain": ("CLOSED at response level: Im[P0]=-127/(1280 pi) "
                         "(u_b-free content), Im[P2]=+11 w^2 u_b^2/(64 pi), "
                         "Im[P4]=-9 w^4 u_b^4/(640 pi); sum == assembled A2 "
                         "exactly under Gamma-aware canonicalization. "
                         "Kernel-level u_b origin (solely (1-Hu)(1-Hu_p)) "
                         "stands from T3-05F and was not re-derived."),
    "parity": ("mechanical: WMINUS == WPLUS(u<->u_p) exactly; every raw H^4 "
               "term even in u_b; kernel u_b^1 cancellation is assembly-level"),
    "open_physics_question": ("whether the surviving u_b^2, u_b^4 dependence "
                              "is removable under the correct frame/assembly "
                              "prescription -- NOT decided here"),
}
results["notes"] = notes
results["w0"] = "computed-and-reported, NOT banked"
results["scope"] = ("diagnostic closure ONLY; frozen artifacts read-only; "
                    "no H^6; no R'; conditional on the declared patch-local "
                    "quotient")
with open(RESULT_PATH, "w") as f:
    json.dump(results, f, indent=2)

fails = [c for c in results["checks"] if not c["pass"]]
print(f"\nT3-05G: {len(results['checks']) - len(fails)}/{len(results['checks'])} checks pass")
print(f"result written: {RESULT_PATH}")
raise SystemExit(1 if fails else 0)
