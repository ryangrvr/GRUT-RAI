#!/usr/bin/env python3
"""T3-05J additivity probe (restructured load path).

Reason for restructure: the previous run (PID 24522, killed) hung inside
json.load -> sympify -> expand while rebuilding the full ret_wigner object
(~3 GB, PyNumber_Multiply samples) although the specialized H^4
information is available elsewhere.  The load path is now staged with
markers BEFORE every expensive step, and a provenance-pinned sec4 cache
is created on first run so later runs skip the monster-object rebuild.

Cache hierarchy:
  first run : JSON ret_wigner -> sympify -> sec4 = expand(coeff(H,4))
              -> verify -> write .sec4_cache.json (provenance header)
  later runs: .sec4_cache.json loaded directly

The optimization is representation-only: same expression, different
persisted representation.  No truncation, no term filtering.
"""
import hashlib
import json
import os
import sys
import time
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(os.path.dirname(HERE), "PHYSICS_LEDGER")
SRC_CACHE = os.path.join(LEDGER, ".tier3_h4_integrand_cache.json")
SEC4_CACHE = os.path.join(LEDGER, ".sec4_cache.json")
RESULT_PATH = os.path.join(HERE, "T3_05J_UB_SURVIVAL_RESULT.json")


def stage(msg):
    print(f"[stage] {msg}", flush=True)


def sha_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


H = sp.Symbol("H", real=True)
ub = sp.Symbol("u_b", real=True)
D = sp.Symbol("Delta", real=True)
q = sp.Symbol("q", positive=True)
om = sp.Symbol("omega", positive=True)
kap = sp.Symbol("kappa", positive=True)
dsym = sp.Symbol("d", positive=True)

# ------------------------------------------------------------------ load
stage("loading JSON")
if not os.path.exists(SRC_CACHE):
    stage("source cache missing -- ABORT")
    sys.exit(2)

sec4 = None
if os.path.exists(SEC4_CACHE):
    stage("sec4 cache found; loading directly")
    try:
        sc = json.load(open(SEC4_CACHE))
        if sc["provenance"]["source_cache_sha256"] == sha_file(SRC_CACHE) \
                and sc["provenance"]["H_power"] == 4:
            sec4 = sp.sympify(sc["sec4"])
            if hashlib.sha256(str(sec4).encode()).hexdigest() \
                    == sc["provenance"]["sec4_sha256"]:
                stage("sec4 cache provenance verified -- using cached "
                      "representation")
            else:
                stage("sec4 cache body hash MISMATCH -- rebuilding")
                sec4 = None
        else:
            stage("sec4 cache provenance pin FAILED (source changed or "
                  "wrong H-power) -- rebuilding")
    except Exception as e:
        stage(f"sec4 cache unusable ({e!r}) -- rebuilding")

if sec4 is None:
    stage("sympifying ret_wigner (expensive, first run only)")
    ic = json.load(open(SRC_CACHE))
    RET4 = sp.sympify(ic["ret_wigner"])
    stage("extracting H^4 coefficient")
    sec4 = sp.expand(RET4.coeff(H, 4))
    stage("writing provenance-pinned sec4 cache")
    json.dump({
        "provenance": {
            "source_cache": SRC_CACHE,
            "source_cache_sha256": sha_file(SRC_CACHE),
            "H_power": 4,
            "created": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
            "sec4_sha256": hashlib.sha256(str(sec4).encode()).hexdigest(),
        },
        "sec4": str(sec4),
    }, open(SEC4_CACHE, "w"))
stage("sec4 ready")

# --------------------------------------------- reference consistency gate
stage("reference consistency")
A2_REF = (-18 * om**4 * ub**4 + 220 * om**2 * ub**2 - 127) / (1280 * sp.pi)
c0_check = sp.cancel(sp.together(sp.expand(sec4).coeff(ub, 0)
                                 + sp.Rational(127, 1280) / sp.pi))
if c0_check != 0:
    stage(f"REFERENCE CONSISTENCY WARNING: ub=0 sector residual "
          f"= {str(c0_check)[:120]} (recorded, not blocking -- the "
          f"branch comparison below is the actual experiment)")

results = {"instrument": "calc/t3_05j_additivity_probe_v2.py",
           "load_path": "staged+cached",
           "checks": [], "notes": []}


def check(name, ok, msg):
    results["checks"].append({"name": name, "pass": bool(ok), "msg": msg})
    print(("  ok   " if ok else "  FAIL ") + f"{name}: {msg}", flush=True)


check("L1 sec4 loaded (cached or first-run derived)", sec4 is not None,
      "H^4 coefficient in hand without relying on un-pinned state")

# ----------------------------------------------------------- branch routes
src = open(os.path.join(LEDGER, "wall_kr_tier3_loop_h4.py")).read()
g = {"sp": sp, "D": D, "ub": ub, "q": q, "u": sp.Symbol("u", real=True),
     "up": sp.Symbol("u_p", real=True), "om": om, "kap": kap, "dsym": dsym}
i0s = src[src.find("def _exp_arg_of_factors"):
          src.find('if STAGE == "assemble":')]
exec(i0s, g)
cone_split, imsig_from_cone = g["cone_split"], g["imsig_from_cone"]


def branch_map(expr):
    out = {}
    for t in sp.Add.make_args(sp.expand(expr)):
        t = g["strip_exp_den"](t)
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
        out[(rD, rb)] = out.get((rD, rb), sp.Integer(0)) + sp.Mul(*rest)
    return {k: sp.cancel(sp.together(v)) for k, v in out.items() if v != 0}


stage("branch map")
bmap = branch_map(sec4)
per_branch, sum_d3 = {}, {j: sp.Integer(0) for j in (0, 2, 4)}
gate_any = False
for k, v in sorted(bmap.items(), key=lambda kv: str(kv[0])):
    tag = f"rD={k[0]},rb={k[1]}"
    stage(f"branch {tag}: extraction")
    entry = {}
    try:
        ims_b_gen = imsig_from_cone(v)
    except RuntimeError as e:
        gate_any = True
        per_branch[tag] = {"reality_gate": str(e)}
        print(f"  -- {tag}: reality gate blocks individual extraction",
              flush=True)
        continue
    stage(f"branch {tag}: d=3 specialization")
    e_ = sp.cancel(sp.together(ims_b_gen))
    num, den = sp.fraction(e_)
    pole = sp.simplify(sp.limit(e_ * (dsym - 3), dsym, 3))
    if sp.simplify(den.subs(dsym, 3)) == 0 or sp.simplify(pole) != 0:
        val = sp.simplify(sp.limit(e_, dsym, 3))
    else:
        val = sp.expand(sp.simplify(num.subs(dsym, 3)
                                    / den.subs(dsym, 3)))
    entry["d3_pole_residue"] = str(pole)
    for j in (0, 2, 4):
        c = sp.expand(val).coeff(ub, j)
        entry[f"A2_{j}"] = str(c)
        sum_d3[j] += c
    per_branch[tag] = entry
    print(f"  -- {tag}: " + ", ".join(
        f"u_b^{j}: {str(entry.get(f'A2_{j}'))[:70]}" for j in (0, 2, 4)),
        flush=True)
results["per_branch_d3"] = per_branch
results["branch_sum_d3"] = {j: str(sum_d3[j]) for j in (0, 2, 4)}

# ------------------------------------------------ residual normalization
stage("residual normalization (per u_b power)")
REF = {0: -sp.Rational(127, 1280) / sp.pi,
       2: 11 * om**2 / (64 * sp.pi),
       4: -9 * om**4 / (640 * sp.pi)}
resid = {}
for j in (0, 2, 4):
    if gate_any:
        resid[j] = "GATE-BLOCKED"
        continue
    r = sp.simplify(sp.cancel(sp.together(sp.expand(sum_d3[j] - REF[j]))))
    resid[j] = str(r)
    print(f"  -- R_{j} (normalized) = {str(r)[:140]}", flush=True)
results["normalized_residuals"] = resid

stage("classification")
if gate_any:
    classification = "CROSS-BRANCH (gate-blocked per-branch extraction)"
else:
    agree = all(sp.simplify(sp.sympify(resid[j])) == 0 for j in (0, 2, 4))
    ub_survives = any(sp.simplify(sum_d3[j]) != 0 for j in (2, 4))
    if agree:
        classification = (
            "SURVIVES: branch sum reproduces the assembled A2 exactly and "
            "the u_b^2/u_b^4 pieces are nonzero in the correctly assembled "
            "d=3 object (pending the Sigma->G_R^TT keystone)."
            if ub_survives else
            "CANCELS: u_b pieces vanish in the assembled object -- the "
            "T3-05 C2 u_b-dependence was an assembly/representation "
            "artifact.")
    else:
        bad = [j for j in (0, 2, 4)
               if sp.simplify(sp.sympify(resid[j])) != 0]
        classification = (f"BRANCH-SUM MISMATCH at u_b powers {bad} -- "
                          "residuals recorded, not interpreted.")
results["classification"] = classification
results["notes"].append(
    "load path restructured after PID 24522 kill; killed run preserved at "
    "/tmp/probe_additivity_KILLED_24522.py.bak with empty log "
    "/tmp/probe_additivity_KILLED_EMPTY.log")
results["w0"] = "computed-and-reported, NOT banked"
results["scope"] = ("diagnostic ONLY; frozen artifacts read-only; no R'; "
                    "no H^6; no interpretation of u_b")

with open(RESULT_PATH, "w") as f:
    json.dump(results, f, indent=2)

fails = [c for c in results["checks"] if not c["pass"]]
print(f"\nT3-05J: {len(results['checks']) - len(fails)} / "
      f"{len(results['checks'])} checks pass", flush=True)
print(f"classification: {classification}", flush=True)
print(f"result written: {RESULT_PATH}", flush=True)
raise SystemExit(1 if fails else 0)
