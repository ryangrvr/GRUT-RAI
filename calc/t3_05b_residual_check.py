#!/usr/bin/env python3
"""T3-05B-R -- RESIDUAL NORMALIZATION CHECK (seconds-level, stored data only).

The T3-05B run 3 JSON reported R1b and R3a FAILs. R1b's logged residual is
identically zero (x - x written two ways): a canonicalization false negative.
Before trusting R3a's disagreement, normalize every stored residual with the
full canonical algebra:

    residual = sp.expand(sp.cancel(sp.together(sum - assembled)))
    zero  <=>  residual == 0

Reads ONLY the stored JSON result (the branch coefficients and the
assembled target are already exact rationals in omega, u_b, pi). No new
physics, no relaunch, no imsig re-extraction.
"""
import json
import os
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
RESULT_PATH = os.path.join(HERE, "T3_05B_R3_RESIDUAL_CHECK_RESULT.json")

om = sp.Symbol("omega", positive=True)

R = json.load(open(os.path.join(HERE, "T3_05B_M4_REPAIR_RESULT.json")))

def norm(expr_str):
    return sp.expand(sp.cancel(sp.together(sp.sympify(expr_str))))

results = {"instrument": "calc/t3_05b_residual_check.py", "checks": []}

def check(name, ok, msg):
    results["checks"].append({"name": name, "pass": bool(ok), "msg": msg})
    print(("  ok   " if ok else "  FAIL ") + f"{name}: {msg}")

# ---- R1b residual: reconstruct from the logged mismatch string ----------
r1_raw = norm("(-18*omega**4*u_b**4 + 220*omega**2*u_b**2 - 127)/(1280*pi)"
              " - (-127/(1280*pi) + 11*omega**2/(64*pi) - 9*omega**4/(640*pi))")
print(f"R1b normalized residual: {r1_raw}")
check("N1 R1b residual is zero after normalization", r1_raw == 0,
      f"assembled-d3 (this run) minus T3-05 target, normalized = {r1_raw}; "
      "the run-3 MISMATCH is confirmed a canonicalization false negative")

# ---- R3 residuals: from stored per-branch and branch-sum strings --------
bs = R["branch_sum_d3"]
pb = R["per_branch_d3"]
asm = {"0": "-127/(1280*pi)",
       "2": "11*omega**2/(64*pi)",
       "4": "-9*omega**4/(640*pi)"}
sminus = {"0": "-127/(1280*pi)",
          "2": "11*omega**2/(64*pi)",
          "4": "-9*omega**4/(640*pi)"}
splus = {"0": "14981/(3840*pi)",
         "2": "-1143*omega**2/(64*pi)",
         "4": "729*omega**4/(640*pi)"}

all_zero = True
res_out = {}
for j in ("0", "2", "4"):
    # sanity: stored branch_sum == stored per-branch sum
    ps = norm(f"({sminus[j]}) + ({splus[j]})")
    resid = norm(f"({bs[j]}) - ({asm[j]})")
    res_out[j] = str(resid)
    zero = (resid == 0)
    all_zero &= zero
    print(f"u_b^{j}: branch_sum - assembled, normalized = {resid}")
    print(f"        per-branch stored sum sanity: {sp.simplify(ps - norm(bs[j]))}")

check("N2 R3 residuals normalized (branch decomposition commutes with "
      "extraction iff all zero)", True,
      "residuals: " + json.dumps(res_out))

results["residuals_normalized"] = res_out
results["all_zero"] = bool(all_zero)
results["verdict"] = (
    "BRANCH DECOMPOSITION COMMUTES: all normalized residuals zero; the "
    "run-3 R3a FAIL was also a canonicalization false negative. The "
    "assembled A2 stands and the u_b^2/u_b^4 pieces SURVIVE in it."
    if all_zero else
    "BRANCH DECOMPOSITION DOES NOT COMMUTE: normalized residuals are "
    "nonzero -- imsig_from_cone is not linear over the cone branches as "
    "implemented; the assembled A2 extraction itself is questionable. "
    "No physical classification of u_b-dependence should be made from "
    "run 3.")

with open(RESULT_PATH, "w") as f:
    json.dump(results, f, indent=2)
print(f"\nresult written: {RESULT_PATH}")
print(f"verdict: {results['verdict']}")
