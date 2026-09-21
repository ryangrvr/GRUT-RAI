# File: calc/t3_05e_trace_c0c2.py
#!/usr/bin/env python3
"""T3-05E -- FIRST-DIVERGENCE TRACE of imsig_from_cone on {c0, c2}.

Scope (narrow, per directive): instrument, do NOT modify, imsig_from_cone.
Replicate its internal stages EXACTLY (source lines 562-587 of
wall_kr_tier3_loop_h4.py) on three inputs: c0, c2, c0+c2, and compare the
combined route against the sum of the separate routes at EVERY stage.
Report the FIRST stage where they differ, with the exact operation.

Stage map (mirrors the source verbatim):
  S1  cancel(together(x)).as_numer_denom()          -> (num, den)
  S2  den carries Delta? (gate)                     -> raise if so
  S3  Poly(num, Delta); degree                      -> range gate
  S4  per n: c_n = cancel(coeff / den)
  S5  per n: reality gate  simplify(im(expand_complex(I^n c_n)))
  S6  per n: contribution (-pi)(-1)^n I^(n+1) diff(MEAS*c_n, q, n)|q=om/2 / 2^(n+1)
  S7  tot (pre-as_real_imag)
  S8  expand(tot).as_real_imag()
  S9  simplify(im_)

Also run the UNGATED arithmetic analogue: the same S1-S6 with the reality
gate neutralized (record-only), to see whether the gate is where the two
routes first see different objects.
"""
import json
import os
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(os.path.dirname(HERE), "PHYSICS_LEDGER")
RESULT_PATH = os.path.join(HERE, "T3_05E_TRACE_RESULT.json")

results = {"instrument": "calc/t3_05e_trace_c0c2.py",
           "conditional_scope": "trace of the operator AS IMPLEMENTED",
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

src = open(os.path.join(LEDGER, "wall_kr_tier3_loop_h4.py")).read()
i0s = src[src.find("def _exp_arg_of_factors"):src.find('if STAGE == "assemble":')]
g = {"sp": sp, "D": D, "ub": ub, "q": q, "u": sp.Symbol("u", real=True),
     "up": sp.Symbol("u_p", real=True), "om": om, "kap": kap, "dsym": dsym}
exec(i0s, g)
cone_split, imsig_from_cone = g["cone_split"], g["imsig_from_cone"]
MEAS = g["MEAS"]

# --- the same synthetic monomials as T3-05D (phase convention: rD=-2 slot)
def phased_monomial(n, sign=-2):
    base = om**(4 - n) / kap**n
    c = sp.I**n * base
    return c * D**n * sp.exp(sp.I * sign * q * D)

c0 = phased_monomial(0)
c2 = phased_monomial(2)
combo = sp.expand(c0 + c2)


def cone_coeff(expr):
    cs = cone_split(sp.expand(expr))
    assert cs["stray"] == {} and not cs["p"], "unexpected cone content"
    return sp.cancel(sp.together(cs["m"]))


# sanity: the operator itself reproduces the T3-05D non-additivity on these
I0 = imsig_from_cone(cone_coeff(c0))
I2 = imsig_from_cone(cone_coeff(c2))
I01 = imsig_from_cone(cone_coeff(combo))
delta = sp.expand(sp.cancel(sp.together(I01 - I0 - I2)))
check("T0 baseline reproduces non-additivity", delta != 0,
      f"delta_02 = {str(delta)[:140]} (must be nonzero for the trace to be "
      f"on the failing case)")
results["baseline_delta"] = str(delta)


def trace(inp, tag):
    """Replicate imsig_from_cone stage by stage; return dict of stages."""
    st = {}
    # S1
    cn_, cd_ = sp.cancel(sp.together(inp)).as_numer_denom()
    st["S1_num"] = str(cn_)
    st["S1_den"] = str(cd_)
    # S2
    st["S2_den_has_D"] = bool(cd_.has(D))
    # S3
    pn = sp.Poly(sp.expand(cn_), D)
    st["S3_degree"] = int(pn.degree())
    # S4/S5/S6 per n
    per_n = {}
    for n_ in range(0, pn.degree() + 1):
        c_n = sp.cancel(pn.coeff_monomial(D**n_) / cd_)
        if c_n == 0:
            continue
        entry = {"c_n": str(c_n)}
        chkr = sp.simplify(sp.im(sp.expand_complex(sp.I**n_ * c_n)))
        entry["gate_value"] = str(chkr)
        entry["gate_raises"] = bool(chkr != 0)
        if not chkr:
            contrib = (-sp.pi) * (-1)**n_ * sp.I**(n_ + 1) \
                * sp.diff(MEAS * c_n, q, n_).subs(q, om / 2) \
                / sp.Integer(2)**(n_ + 1)
            entry["contribution"] = str(contrib)
        per_n[str(n_)] = entry
    st["S4S6_per_n"] = per_n
    # S7: tot = sum of contributions (gate-passing only), as the source does
    tot = sp.Integer(0)
    for k, e in per_n.items():
        if not e["gate_raises"]:
            tot += sp.sympify(e["contribution"])
    st["S7_tot"] = str(sp.expand(tot))
    # S8
    re_, im_ = sp.expand(tot).as_real_imag()
    st["S8_im"] = str(sp.expand(im_))
    # S9
    st["S9_simplified"] = str(sp.simplify(im_))
    return st


print("tracing c0 ...")
t0 = trace(cone_coeff(c0), "c0")
print("tracing c2 ...")
t2 = trace(cone_coeff(c2), "c2")
print("tracing c0+c2 ...")
tc = trace(cone_coeff(combo), "c0+c2")
results["trace_c0"] = t0
results["trace_c2"] = t2
results["trace_combo"] = tc

# --- stage-by-stage comparison: combined vs sum of parts
print("comparing stage by stage ...")
first_div = None
cmp_report = []

# S1: num/den of combo vs (num0*den2 + num2*den0) over den0*den2
n0, d0 = sp.sympify(t0["S1_num"]), sp.sympify(t0["S1_den"])
n2, d2 = sp.sympify(t2["S1_num"]), sp.sympify(t2["S1_den"])
nc, dc = sp.sympify(tc["S1_num"]), sp.sympify(tc["S1_den"])
sum_num = sp.cancel(sp.expand(n0 * d2 + n2 * d0))
sum_den = sp.cancel(sp.expand(d0 * d2))
same_frac = sp.simplify(sp.cancel(sp.expand(nc * sum_den - sum_num * dc))) == 0
cmp_report.append(("S1 cancel(together)", same_frac,
                   "combo (num,den) equals cross-multiplied sum of parts "
                   "(same rational function)" if same_frac else
                   "DIFFERENT rational function after cancel(together)"))
if not same_frac and first_div is None:
    first_div = "S1"

# S3
same_deg = t0["S3_degree"] == 0 and t2["S3_degree"] == 2 \
    and tc["S3_degree"] == 2
cmp_report.append(("S3 Poly degree", same_deg,
                   f"degrees: c0 -> {t0['S3_degree']}, c2 -> {t2['S3_degree']}, "
                   f"combo -> {tc['S3_degree']}"))
if not same_deg and first_div is None:
    first_div = "S3"

# S4/S5 per-n c_n comparison (combined route vs parts, cross-multiplied)
for n_ in ("0", "2"):
    cc = sp.sympify(tc["S4S6_per_n"].get(n_, {}).get("c_n", "0"))
    a = sp.sympify(t0["S4S6_per_n"].get(n_, {}).get("c_n", "0"))
    b = sp.sympify(t2["S4S6_per_n"].get(n_, {}).get("c_n", "0"))
    same = sp.simplify(sp.cancel(sp.expand(cc - a - b))) == 0
    cmp_report.append((f"S4 c_{n_}", same,
                       f"combined c_{n_} {'==' if same else '!='} "
                       f"c_{n_}^{(c0)} + c_{n_}^{(c2)}"))
    if not same and first_div is None:
        first_div = f"S4 c_{n_}"

# gate values
for n_ in ("0", "2"):
    gc = tc["S4S6_per_n"].get(n_, {}).get("gate_value", "absent")
    g0 = t0["S4S6_per_n"].get(n_, {}).get("gate_value", "absent")
    g2 = t2["S4S6_per_n"].get(n_, {}).get("gate_value", "absent")
    same = sp.simplify(sp.sympify(gc) - sp.sympify(g0) - sp.sympify(g2)) == 0
    cmp_report.append((f"S5 gate c_{n_}", same,
                       f"gate(combo)={gc[:60]} vs gate(c0)+gate(c2)={g0[:30]}+{g2[:30]}"))
    if not same and first_div is None:
        first_div = f"S5 gate c_{n_}"

# S6 contributions
for n_ in ("0", "2"):
    cc = sp.sympify(tc["S4S6_per_n"].get(n_, {}).get("contribution", "0"))
    a = sp.sympify(t0["S4S6_per_n"].get(n_, {}).get("contribution", "0"))
    b = sp.sympify(t2["S4S6_per_n"].get(n_, {}).get("contribution", "0"))
    same = sp.simplify(sp.cancel(sp.expand(cc - a - b))) == 0
    cmp_report.append((f"S6 contribution n={n_}", same,
                       "combined contribution == sum of separate"))
    if not same and first_div is None:
        first_div = f"S6 contribution n={n_}"

# S7
s7same = sp.simplify(sp.cancel(sp.expand(
    sp.sympify(tc["S7_tot"]) - sp.sympify(t0["S7_tot"]) - sp.sympify(t2["S7_tot"])))) == 0
cmp_report.append(("S7 tot (pre imag split)", s7same,
                   "combined tot == sum of parts" if s7same else
                   "DIFFERENT pre-split totals"))
if not s7same and first_div is None:
    first_div = "S7"

# S8
s8same = sp.simplify(sp.cancel(sp.expand(
    sp.sympify(tc["S8_im"]) - sp.sympify(t0["S8_im"]) - sp.sympify(t2["S8_im"])))) == 0
cmp_report.append(("S8 as_real_imag", s8same,
                   "combined imag part == sum of parts" if s8same else
                   "DIFFERENT imag parts BEFORE simplify"))
if not s8same and first_div is None:
    first_div = "S8"

# S9
s9same = sp.simplify(sp.cancel(sp.expand(
    sp.sympify(tc["S9_simplified"]) - sp.sympify(t0["S9_simplified"])
    - sp.sympify(t2["S9_simplified"])))) == 0
cmp_report.append(("S9 simplify", s9same,
                   "combined simplified == sum of simplified" if s9same else
                   "DIFFERENT only AFTER the final global simplify"))
if not s9same and first_div is None:
    first_div = "S9"

results["stage_comparison"] = [
    {"stage": s, "match": bool(m), "msg": msg} for s, m, msg in cmp_report]
for s, m, msg in cmp_report:
    print(f"  {'ok  ' if m else 'DIFF'} {s}: {msg[:150]}")

check("T1 first divergence identified", first_div is not None,
      f"first stage where I(c0+c2) departs from I(c0)+I(c2): "
      f"{first_div if first_div else 'NO divergence found in traced stages'}")
results["first_divergence"] = first_div

# ---------------------------------------------------------------- verdict
if first_div == "S9":
    verdict = ("LOCALIZED: the extraction arithmetic (S1-S8) is exactly "
               "additive; the non-additivity is introduced by the FINAL "
               "global sp.simplify(im_) on the combined input -- a "
               "canonicalization-side effect, not a change in the "
               "extracted coefficient class.")
elif first_div and first_div.startswith("S5"):
    verdict = ("LOCALIZED: the reality-pattern GATE (S5) sees different "
               "objects on the combined route -- gate-dependent selection "
               "is the non-additive element.")
elif first_div == "S1":
    verdict = ("LOCALIZED: cancel(together()) at S1 merges the two inputs "
               "into a shared denominator; the combined rational function "
               "differs from the termwise one BEFORE any physics.")
else:
    verdict = (f"divergence first at {first_div}; see stage_comparison.")

results["verdict"] = verdict
results["notes"] = notes
results["w0"] = "computed-and-reported, NOT banked"
results["scope"] = ("operator trace ONLY; imsig_from_cone untouched; no "
                    "real-data assembly; no H^6; R' untouched")
with open(RESULT_PATH, "w") as f:
    json.dump(results, f, indent=2)

fails = [c for c in results["checks"] if not c["pass"]]
print(f"\nT3-05E: {len(results['checks']) - len(fails)}/{len(results['checks'])} checks pass")
print(f"verdict: {verdict}")
print(f"result written: {RESULT_PATH}")
raise SystemExit(1 if fails else 0)
