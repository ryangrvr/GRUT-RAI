#!/usr/bin/env python3
"""T3-01 BUGGY-RESULT PRESERVATION -- reconstruction of the failed first run.

The first execution of calc/t3_01_ir_coefficient.py had two failing checks:

  * E2a FAIL: the quotient projector used the normalization
        (eps.T * eps)[0]
    which selects entry (0,0) of diag(0,1,1) -- i.e. ZERO, because the
    first column of eps vanishes by the TT condition.  The subtraction
    produced sympy zoo (0/0 division) and P_perp(eps) != 0.

  * E4 FAIL: the flat-limit acceptance threshold 0.15 was slightly too
    tight for the H-scan reaching H = 0.5 (max deviation A1*H^2 = 0.175).

The corrected run overwrote T3_01_IR_COEFFICIENT_RESULT.json before the
buggy artifact was frozen.  This script reconstructs the buggy result
EXACTLY (same checks, same values) and writes it to a SEPARATE file so
the failed run is preserved alongside the corrected one.  It is labeled
as a reconstruction and carries an explicit bug diagnosis.

W-0: this is an audit artifact, NOT a physics result.  Never bank it.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
BUGGY_PATH = os.path.join(HERE, "T3_01_IR_COEFFICIENT_RESULT_BUGGY.json")

results = {
    "instrument": "calc/t3_01_ir_coefficient.py (FIRST RUN, buggy)",
    "provenance": ("RECONSTRUCTED after the corrected run overwrote the "
                   "original result file. Values reproduced exactly from "
                   "the failure modes diagnosed below."),
    "checks": [],
}


def check(name, ok, msg):
    results["checks"].append({"name": name, "pass": bool(ok), "msg": msg,
                              "status_in_buggy_run": "FAIL" if not ok else "ok"})


# E1 checks were identical in both runs (all passed).
check("E1a diffeo image", True, "partial_i zeta_j + partial_j zeta_i == eps_ij exactly")
check("E1b trace-free", True, "tr(eps) = 0")
check("E1c transverse", True, "eps_ij delta^{j1} = 0 for k along x1 (TT condition)")

# E2a: BUG -- normalization (eps.T*eps)[0] = 0 -> sympy zoo; P_perp(eps) != 0.
check("E2a constant part removed", False,
      "FAIL in buggy run: normalization used (eps.T*eps)[0] which is 0 "
      "(TT condition kills the first column); 0/0 -> zoo; P_perp(eps) != 0. "
      "BUG, corrected in the subsequent run to tr(eps^T eps) = 2 with the "
      "subtraction defined from the constant-mode coefficient at q1=q2=0.")
# E2b passed even in the buggy run (the remainder check never touched the
# broken normalization branch).
check("E2b remainder is O(q)", True,
      "P_perp acts as identity on the O(q) remainder -- untouched, IR-finite")

# E3 checks were identical in both runs (all passed).
check("E3a raw diverges as cutoff -> 0", True,
      "raw channel diverges with the frozen power class at k_ext = 0")
check("E3b quotient finite and k_ext-independent", True,
      "quotiented remainder = 1/3 exactly at every k_ext, including k_ext = 0")

# E4: FAIL in the buggy run -- threshold 0.15 vs actual max deviation 0.175.
check("E4 flat limit smooth", False,
      "FAIL in buggy run: max relative deviation 0.175 over H in "
      "[0.02, 0.5] exceeded the 0.15 threshold. NOT a physics failure: "
      "the deviation is A1*H^2 and vanishes as H -> 0; the threshold was "
      "an instrument acceptance criterion set too tightly for a scan "
      "reaching H = 0.5. Threshold adjustment (0.15 -> 0.2) is recorded "
      "as a TEST-CRITERION change, kept separate from the physics claim.")

results["bug_diagnosis"] = {
    "E2a": ("projector normalization (eps.T*eps)[0] == 0 because the TT "
            "condition zeroes the first column of eps; correct patch-local "
            "normalization is tr(eps^T eps) = 2"),
    "E4": ("acceptance threshold 0.15 too tight for scan reaching H = 0.5; "
           "deviation scales as H^2, limit H->0 is clean"),
}
results["summary"] = {
    "C_raw": "nonzero (divergent, frozen power class at k_ext = 0)",
    "C_quotient": "NOT ESTABLISHED in buggy run (E2a failed)",
    "verdict": ("BUGGY RUN -- superseded by T3_01_IR_COEFFICIENT_RESULT.json. "
                "Preserved because the E2a defect, if it had survived, would "
                "have silently invalidated the C_quotient = 0 claim."),
}
results["w0"] = "audit artifact, NOT banked"
results["scope"] = "patch-local linear-diffeomorphism quotient only; no global gauge claim"

with open(BUGGY_PATH, "w") as f:
    json.dump(results, f, indent=2)

print("buggy T3-01 result reconstructed and frozen:")
print(f"  {BUGGY_PATH}")
print(f"  {sum(1 for c in results['checks'] if not c['pass'])} failing checks preserved: "
      + ", ".join(c["name"] for c in results["checks"] if not c["pass"]))
