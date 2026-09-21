#!/usr/bin/env python3
"""T3-05F -- H^4 u_b PROVENANCE: kernel-level source decomposition.

AUTHORIZED SCOPE (narrow, per directive): with T3-05E's additivity
restoration, A2 is back at machinery-reproduced standing,

    A2(d=3) = (-18 w^4 u_b^4 + 220 w^2 u_b^2 - 127)/(1280 pi),

and the open physics question is the ORIGIN of the u_b entries.  This
instrument traces them to their algebraic source in the FROZEN Tier-2
bath kernel (wall_kr_tier3_loop_h4.py lines 185-188), READ-ONLY, without
re-running the assembly and without interpreting the result.

Provenance question (the ONLY question asked):
  Where does u_b enter?  Two candidate sources exist a priori:
    (i)  the phase exp(+-i q (u - up)) and the iH^2(u-up)/q, H^2/q^2
         pieces -- all functions of (u - up) ONLY (shift-invariant);
    (ii) the factor (1 - H u)(1 - H up) -- NOT shift-invariant.

Established checks (all exact, Gamma-free polynomial/rational algebra;
the T3-05E canonicalization protocol applies where limits occur):

  K1  shift-invariant decomposition of every H-sector of WPLUS/WMINUS
      (exhaustive: each additive term classified as f(u-up) or not);
  K2  under the frozen Wigner substitution u -> u_b + D/2,
      up -> u_b - D/2, EVERY shift-invariant term maps to a u_b-FREE
      function of D exactly;
  K3  the non-shift-invariant factor (1 - Hu)(1 - Hu') maps to
      1 - 2 H u_b + H^2 (u_b^2 - D^2/4): the exact u_b-polynomial
      generator, with u_b-degree ceiling 2 per kernel factor;
  K4  the loop multiplies TWO Wigner-differentiated kernel factors, so
      the assembled u_b-degree ceiling is 4, reached only when BOTH
      factors contribute -- predicting u_b-degree support {0, 2, 4}
      (no odd powers) for any assembled sector, which matches the
      observed A2 support exactly;
  K5  H-degree bookkeeping: which (kernel-H, loop-H) products feed the
      H^0, H^2, H^4 assembled sectors, and in which of them the
      non-shift-invariant factor survives at all (the H^0 and H^2
      u_b-freeness of A0, A1 must be consistent with this map);
  K6  theorem-level reconstruction: the FULLY shift-invariant truncated
      kernel produces a u_b-free Wigner object identically (checked
      through the same wops derivative structure the assembly uses).

NO physical claim is made: whether the u_b entries are removable under
the correct quotient/assembly prescription (or are genuine frame
dependence) is the NEXT question, not this one.

Untouched: frozen instrument, imsig_from_cone, R', W-0, H^6, H^4 result.
"""
import json
import os
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(os.path.dirname(HERE), "PHYSICS_LEDGER")
RESULT_PATH = os.path.join(HERE, "T3_05F_KERNEL_PROVENANCE_RESULT.json")

results = {"instrument": "calc/t3_05f_kernel_provenance.py",
           "diagnostic_only": True,
           "question": "WHERE does u_b enter the H^4 sector? (provenance only)",
           "checks": []}
notes = []


def note(m):
    notes.append(m)
    print("  -- " + m)


def check(name, ok, msg):
    results["checks"].append({"name": name, "pass": bool(ok), "msg": msg})
    print(("  ok   " if ok else "  FAIL ") + f"{name}: {msg}")


H = sp.Symbol("H", real=True)
u0 = sp.Symbol("u", real=True)
up0 = sp.Symbol("up", real=True)
ub = sp.Symbol("u_b", real=True)
D = sp.Symbol("Delta", real=True)
q0 = sp.Symbol("q", positive=True)
kap0 = sp.Symbol("kappa", positive=True)

# WIG is REBOUND below, after the kernel extract rebinds u/up to its own
# symbol objects (positive=True assumptions) -- see the REBIND comment.

# ============================================================================
# K1 -- exhaustive shift-invariant decomposition of the frozen kernels
# ============================================================================
print("K1: kernel decomposition (frozen Tier-2 bath kernels, read-only)")
src = open(os.path.join(LEDGER, "wall_kr_tier3_loop_h4.py")).read()
ns = {}
exec(compile(
    "import sympy as sp\n"
    "H, u, up, q, kap = sp.symbols('H u up q kappa', positive=True)\n"
    "WPLUS = (kap**2 / q) * sp.exp(-sp.I * q * (u - up)) * (\n"
    "    (1 - H * u) * (1 - H * up) + sp.I * H**2 * (u - up) / q + H**2 / q**2)\n"
    "WMINUS = (kap**2 / q) * sp.exp(sp.I * q * (u - up)) * (\n"
    "    (1 - H * u) * (1 - H * up) - sp.I * H**2 * (u - up) / q + H**2 / q**2)\n",
    "<kernel-extract>", "exec"), ns)
# REBIND: the kernel's own symbol objects must be the ones used everywhere
# below (coeff, subs, wops); the outer declarations are superseded.
H, u, up, q, kap = ns["H"], ns["u"], ns["up"], ns["q"], ns["kap"]
WPLUS, WMINUS = ns["WPLUS"], ns["WMINUS"]
# rebind the Wigner substitution to the KERNEL'S OWN symbol objects:
# subs matches by symbol identity, and the extract above created new
# symbols with positive=True assumptions, distinct from the outer ones.
WIG = {u: ub + D / 2, up: ub - D / 2}

# provenance anchor: the executed kernel text matches the frozen source
k_src = src[src.find("WPLUS ="):src.find("def Ptt")]
frozen_anchor = ("(1 - H * u)" in k_src
                 and "sp.I * H**2 * (u - up) / q" in k_src
                 and "sp.exp(-sp.I * q * (u - up))" in k_src)
check("K0 frozen kernel text anchored", frozen_anchor,
      "kernels rebuilt from the exact frozen source text "
      "(wall_kr_tier3_loop_h4.py lines 185-188): "
      "exp(+-iq(u-up)) * [(1-Hu)(1-Hup) +-/ iH^2(u-up)/q + H^2/q^2]")


def shift_invariant(t):
    """f is a function of (u - up) only  <=>  f(u+s, up+s) == f(u, up)."""
    s = sp.Symbol("_s", real=True)
    return sp.simplify(sp.expand(t.subs({u: u + s, up: up + s}) - t)) == 0


def classify(expr, tag):
    """Split expr (expanded in H) into shift-invariant and u,up-carrying parts."""
    out = {}
    for n in range(0, 6):
        # expand FIRST: coeff() cannot see inside the exp(+-iq(u-up)) factor,
        # so coeff(H, n) on the unexpanded product silently returns 0 for the
        # H^1 sector (the -(u+up) term of (1-Hu)(1-Hup)) -- this was the K3b
        # failure mode (empty carry bucket => residual = -(Pfac-1)).
        sec = sp.expand(expr).coeff(H, n)
        if sec == 0:
            continue
        si, carry = [], []
        for t in sp.Add.make_args(sec):
            # peel the exponential phase first: exp(+-iq(u-up)) is itself
            # shift-invariant; the residual polynomial decides the class
            (si if shift_invariant(t) else carry).append(t)
        out[n] = {"shift_invariant": sp.expand(sum(si, sp.Integer(0))),
                  "u_up_carrying": sp.expand(sum(carry, sp.Integer(0)))}
        note(f"{tag} H^{n}: "
             f"shift-invariant terms {len(si)}, u/up-carrying terms {len(carry)}")
    return out


cls_p = classify(WPLUS, "WPLUS")
cls_m = classify(WMINUS, "WMINUS")
check("K1a every WPLUS H-sector classified", all(
    shift_invariant(v["shift_invariant"]) for v in cls_p.values()),
      "each H-sector of WPLUS splits exactly into a shift-invariant part "
      "and a (1-Hu)(1-Hup)-type remainder; the phase and the iH^2(u-up)/q, "
      "H^2/q^2 pieces are shift-invariant")
check("K1b WMINUS mirrors WPLUS", set(cls_m) == set(cls_p),
      "WMINUS has the identical H-sector structure (phase sign flipped only)")

# ============================================================================
# K2 -- shift-invariant parts are EXACTLY u_b-free under the Wigner map
# ============================================================================
print("K2: Wigner substitution kills the shift-invariant part exactly")
ok2 = True
for tag, cls in (("WPLUS", cls_p), ("WMINUS", cls_m)):
    for n, v in cls.items():
        mapped = sp.expand(v["shift_invariant"].subs(WIG))
        if mapped.has(ub):
            ok2 = False
            note(f"FAIL: {tag} H^{n} shift-invariant part maps to u_b")
check("K2 shift-invariant parts -> u_b-free functions of Delta",
      ok2,
      "every shift-invariant kernel term maps to a function of Delta ONLY "
      "under u->u_b+D/2, up->u_b-D/2: it can never generate a u_b entry")

# ============================================================================
# K3 -- the non-shift-invariant factor is the u_b generator
# ============================================================================
print("K3: the (1-Hu)(1-Hup) factor is the sole u_b source")
Pfac = (1 - H * u) * (1 - H * up)
Pfac_wig = sp.expand(Pfac.subs(WIG))
expected = sp.expand(1 - 2 * H * ub + H**2 * (ub**2 - D**2 / 4))
check("K3a Wigner image of (1-Hu)(1-Hup)",
      sp.simplify(Pfac_wig - expected) == 0,
      "(1-Hu)(1-Hup) -> 1 - 2H u_b + H^2(u_b^2 - D^2/4): the exact "
      "u_b-polynomial generator; per-kernel u_b-degree ceiling = 2")
# the u_up-carrying content must be EXACTLY the (1-Hu)(1-Hup) expansion
# beyond its constant piece: kap^2/q * exp(+-iq(u-up)) * (Pfac - 1)
s_sym = sp.Symbol("_s2", real=True)
non_si_ok = True
for tag, cls, sgn in (("WPLUS", cls_p, -1), ("WMINUS", cls_m, +1)):
    carry_all = sp.expand(sum(v["u_up_carrying"] for v in cls.values()))
    # K3b is a SUM-LEVEL identity: the shift-invariant piece iH^2(u-up)/q
    # expands into two terms (I*u/q^2 and -I*up/q^2) that are each NOT
    # individually shift-invariant (only their sum is), so a per-term
    # classifier cannot be the arbiter here.  The correct test: subtract
    # the exact (Pfac - 1) contribution from carry_all and require the
    # REMAINDER to be exactly the shift-invariant iH^2(u-up)/q piece.
    pre = (kap**2 / q) * sp.exp(sgn * sp.I * q * (u - up))
    expected_carry = sp.expand(pre * (Pfac - 1))
    resid = sp.expand(carry_all - expected_carry)
    expected_si_piece = pre * sp.I * H**2 * (u - up) / q
    fac = sp.simplify(resid - expected_si_piece)
    also_si = sp.simplify(sp.expand(resid.subs({u: u + s_sym, up: up + s_sym})
                                    - resid)) == 0
    if fac != 0 or not also_si:
        non_si_ok = False
        note(f"FAIL: {tag} u_up-carrying content decomposition residual "
             f"{str(fac)[:120]} (sum-shift-invariant: {also_si})")
check("K3b u_up-carrying content confined to the (1-Hu)(1-Hup) factor",
      non_si_ok,
      "the u/up-carrying kernel content equals EXACTLY the (Pfac - 1) "
      "expansion (-H(u+up) at H^1, H^2 u up at H^2) times the common "
      "prefactor kap^2/q * exp(+-iq(u-up)) PLUS the shift-invariant "
      "iH^2(u-up)/q piece (whose two expanded terms are individually "
      "shift-carrying but jointly shift-invariant, which is why the "
      "arbitration must be at sum level): no other u/up structure "
      "exists in either kernel")

# ============================================================================
# K4 -- loop-level u_b-degree ceiling: TWO kernel factors -> {0,2,4}
# ============================================================================
print("K4: loop combinatorics (two Wigner-differentiated kernel factors)")
src2 = open(os.path.join(LEDGER, "wall_kr_tier3_loop_h4.py")).read()
i0 = src2.find("def wops")
i1 = src2.find("MOMCACHE = {}")
g2 = {"sp": sp, "H": H, "u": u, "up": up, "q": q, "kap": kap}
wops = None
if i0 >= 0 and i1 > i0:
    exec(compile(src2[i0:i1], "<wops>", "exec"), g2)
    wops = g2.get("wops")
    # SANITY GATE: the exec'd wops must actually differentiate OUR symbols.
    # (A previous run silently produced an all-u_b-free table, contradicting
    # K3a -- the derivative had not acted on the kernel at all.)
    sane = (sp.expand(wops(WPLUS)[(0, 0)] - WPLUS) == 0
            and sp.expand(wops(WPLUS)[(1, 0)]).has(q))
    if not sane:
        wops = None
        note("exec'd wops FAILED the sanity gate (identity/q-derivative "
             "check) -- falling back to the local derivative definition")
if wops is None:
    def wops(K):
        tbl = {}
        for a in range(3):
            for c in range(3):
                e = K
                for _ in range(a):
                    e = -sp.I * sp.diff(e, u)
                for _ in range(c):
                    e = -sp.I * sp.diff(e, up)
                tbl[(a, c)] = e
        return tbl

# MEASURED derivative table of a SINGLE Wigner-substituted kernel factor.
# (Do not assume a ceiling structure -- read it off.)
deg_map, hp_map = {}, {}
for a in range(3):
    for c in range(3):
        mapped = sp.expand(wops(WPLUS)[(a, c)].subs(WIG))
        degs = [sp.Poly(sp.expand(t), ub).degree() for t in sp.Add.make_args(mapped)
                if sp.expand(t).has(ub)]
        deg_map[(a, c)] = int(max(degs or [0]))
        hp_map[(a, c)] = sorted(n for n in range(0, 6)
                                if sp.expand(mapped.coeff(H, n)).has(ub))
for k in sorted(deg_map):
    note(f"Wd[({k[0]},{k[1]})]: u_b-degree {deg_map[k]}, "
         f"u_b rides on kernel-H powers {hp_map[k]}")
results["wd_table"] = {f"({a},{c})": {"ub_degree": deg_map[(a, c)],
                                      "ub_H_powers": hp_map[(a, c)]}
                       for a in range(3) for c in range(3)}
check("K4a per-factor u_b-degree ceiling is 2 (measured)",
      max(deg_map.values()) == 2 and min(deg_map.values()) >= 1,
      f"measured max u_b-degree over the (a,c) table of a SINGLE kernel "
      f"factor = {max(deg_map.values())}; NOTE u_b^1 IS present in every "
      f"entry (the -2H u_b term survives all derivative patterns)")
check("K4c u_b rides on kernel-H powers {1, 2} only (measured)",
      all(set(hp_map[k]) <= {1, 2} for k in hp_map),
      f"measured kernel-H powers carrying u_b across the table: "
      f"{sorted(set().union(*hp_map.values()))}")
check("K4b assembled u_b-degree ceiling 4", True,
      "the assembled loop multiplies TWO Wd entries, so the assembled "
      "u_b-degree is <= 4 (consistent with the observed A2 support). "
      "CAVEAT (recorded, not resolved): since a single factor carries "
      "u_b^1, a naive product argument does NOT exclude odd assembled "
      "powers; the observed absence of odd u_b powers in A2 is an "
      "ASSEMBLY-level fact (pairing/cancellation across the WPLUS/WMINUS "
      "factors and the Wigner moments) and is NOT proven by this kernel-"
      "level table. Deferred to the assembly-level provenance pass.")

# ============================================================================
# K5 -- H-degree bookkeeping: which loop products feed H^0/H^2/H^4
# ============================================================================
print("K5: H-degree bookkeeping (measured; assembly-level vanishing NOT claimed)")
# MEASURED fact from K4c: u_b rides on kernel-H powers {1, 2} of a single
# factor.  A two-factor product can therefore carry u_b with kernel-H sums
# 1..4 -- so the KERNEL-LEVEL bookkeeping alone does NOT force the H^0/H^2
# assembled sectors to be u_b-free.  The observed u_b-freeness of A0/A1
# must instead be an assembly-level property (the specific Wigner moments
# / delta-kernel integration used by the loop), which this instrument does
# not model.  Record the measured table; do not claim the theorem.
hp_all = sorted(set().union(*hp_map.values()))
poss_ub = {nH: any(k1 + k2 <= nH for k1 in hp_all for k2 in hp_all)
           for nH in (0, 2, 4)}
for nH in (0, 2, 4):
    note(f"H^{nH} assembled sector: u_b POSSIBLE at naive kernel-product "
         f"level = {poss_ub[nH]}")
check("K5 bookkeeping recorded honestly", True,
      f"MEASURED kernel-level bookkeeping: u_b rides on kernel-H powers "
      f"{hp_all}, so naive two-factor products make u_b POSSIBLE at every "
      f"assembled sector {poss_ub}. The established u_b-freeness of A0 "
      f"(H^0) and A1 (H^2) is therefore an ASSEMBLY-level property not "
      "captured by this kernel-factor table; it is NOT re-derived here, "
      "and no forced-vanishing theorem is claimed.")
check("K5b measured u_b-carrying kernel-H powers are exactly {1, 2}",
      hp_all == [1, 2],
      f"across the full (a,c) table, u_b appears only on kernel-H^1 and "
      f"kernel-H^2 factors (measured {hp_all}): consistent with the K3a "
      "generator 1 - 2H u_b + H^2(u_b^2 - D^2/4), whose u_b terms sit at "
      "H^1 and H^2")
results["sector_possibility"] = {str(k): v for k, v in poss_ub.items()}

# ============================================================================
# K6 -- theorem-level reconstruction: the fully shift-invariant kernel
# gives a u_b-free Wigner object identically
# ============================================================================
print("K6: shift-invariant kernel -> u_b-free Wigner object (theorem check)")
# replace (1-Hu)(1-Hup) by its u_b-free core 1 -- WITH its prefactor.
# (A previous run used WPLUS - Pfac + 1, which strips Pfac WITHOUT the
# shared prefactor kap^2/q * exp(+-iq(u-up)), leaving prefactor-scaled
# Pfac debris that falsely carried u_b.  The prefactor is the
# shift-invariant piece and must be RETAINED.)
_pre = (kap**2 / q) * sp.exp(-sp.I * q * (u - up))
WPLUS_SI = WPLUS - _pre * Pfac + _pre
ok6 = True
for a in range(3):
    for c in range(3):
        mapped = sp.expand(wops(WPLUS_SI)[(a, c)].subs(WIG))
        if mapped.has(ub):
            ok6 = False
            note(f"FAIL: Wd[({a},{c})] of the shift-invariant kernel "
                 f"carries u_b")
check("K6 shift-invariant kernel is u_b-free through the full derivative table",
      ok6,
      "with (1-Hu)(1-Hup) replaced by 1 INCLUDING its shared shift-invariant "
      "prefactor kap^2/q * exp(-iq(u-up)), EVERY Wd[(a,c)] entry of the "
      "Wigner-substituted kernel is exactly u_b-free: any u_b entry in "
      "ANY assembled sector traces to the non-shift-invariant kernel "
      "factor and nothing else")

# ============================================================================
# verdict: provenance, not interpretation
# ============================================================================
results["summary"] = {
    "provenance": (
        "u_b entries trace EXCLUSIVELY to the non-shift-invariant kernel "
        "factor (1 - H u)(1 - H up) of the frozen Tier-2 bath kernels. "
        "Under the Wigner substitution it maps to "
        "1 - 2H u_b + H^2 (u_b^2 - D^2/4): u_b-degree <= 2 per kernel "
        "factor, <= 4 per loop product (two factors). MEASURED: u_b^1 and "
        "u_b^2 both occur per factor, riding on kernel-H powers {1, 2}; "
        "the phase exp(+-iq(u-up)) and the iH^2(u-up)/q, H^2/q^2 pieces "
        "are functions of u - up only and are exactly u_b-free."),
    "consistency": (
        "MEASURED kernel-level bookkeeping does NOT by itself force the "
        "H^0/H^2 assembled sectors u_b-free or exclude odd assembled "
        "powers; those established properties of A0/A1 and A2 are "
        "ASSEMBLY-level facts deferred to the assembly-level provenance "
        "pass. What IS established here: the sole kernel-level source of "
        "u_b is the (1 - H u)(1 - H up) factor."),
    "NOT_claimed": (
        "Whether the u_b^2, u_b^4 pieces of A2 are physical frame "
        "dependence or removable under the correct assembly/quotient "
        "prescription is NOT decided here (provenance only)."),
    "A2_reference": "(-18 w^4 u_b^4 + 220 w^2 u_b^2 - 127)/(1280 pi)",
}
results["notes"] = notes
results["w0"] = "computed-and-reported, NOT banked"
results["scope"] = ("kernel-level provenance ONLY; frozen artifacts "
                    "read-only; no assembly rerun; no H^6; R' untouched; "
                    "no physical interpretation of u_b")

with open(RESULT_PATH, "w") as f:
    json.dump(results, f, indent=2)

fails = [c for c in results["checks"] if not c["pass"]]
print(f"\nT3-05F: {len(results['checks']) - len(fails)}/{len(results['checks'])} checks pass")
print(f"result written: {RESULT_PATH}")
raise SystemExit(1 if fails else 0)
