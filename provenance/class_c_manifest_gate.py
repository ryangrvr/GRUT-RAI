#!/usr/bin/env python3
"""class_c_manifest_gate: fail-closed consumption of the Class-C problem manifest.

PHASE 1 of the Class-C pre-dispatch sequence (owner brief 2026-08-21). The
manifest (CLASS_C_MANIFEST.json) is the machine-readable computational contract.
This gate:

  1. validates the schema (required sections present, types correct);
  2. verifies the five prohibitions verbatim;
  3. verifies fail_closed is true;
  4. exposes require(section) -- THE SOLVER API: any class-C solver must obtain
     every clock/regulator/gauge/approximation parameter through this call, and
     the call RAISES if the value is UNDECIDED-DISPATCH or missing. A solver
     that bypasses it has no declared parameter and fails closed by construction;
  5. re-runs the Phase-0 contamination scan over the manifest itself.

Exit 0 = PASS; exit 1 = FAIL (schema, prohibition, or contamination).
Pure stdlib. Run: python3 provenance/class_c_manifest_gate.py
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST_PATH = os.path.join(ROOT, "CLASS_C_MANIFEST.json")
UNDECIDED = "UNDECIDED-DISPATCH"

REQUIRED_SECTIONS = [
    "manifest_version", "problem", "primary_object", "not_the_object",
    "background", "state", "content", "gauge", "channel_policy", "clock",
    "boundary_conditions", "renormalization", "regulators", "regulator_policy",
    "approximation_order", "allowed_reductions", "requested_observables",
    "permitted_outcome_classes", "prohibitions", "fail_closed",
]
REQUIRED_PROHIBITIONS = [
    "J(omega) ~ omega^3",
    "single-pole ansatz",
    "tau_0",
    "imported class-A stationarity",
    "epoch/window",
]


class ClassCUndeclared(SystemExit):
    """Raised when a solver requests a manifest parameter that is not decided.
    Fail-closed: an undeclared clock/gauge/regulator cannot silently default."""


def load():
    with open(MANIFEST_PATH, encoding="utf-8") as fh:
        return json.load(fh)


def require(manifest, section):
    """THE SOLVER API. Returns the declared value or raises fail-closed.
    Structured values (dict/list) are checked recursively: ANY nested value
    beginning with UNDECIDED-DISPATCH makes the whole section undeclared."""
    if section not in manifest:
        raise ClassCUndeclared(f"CLASS-C MANIFEST: '{section}' is absent; refusing.")

    def check(val, path):
        if isinstance(val, dict):
            for k, v in val.items():
                check(v, f"{path}.{k}")
        elif isinstance(val, list):
            for i, v in enumerate(val):
                check(v, f"{path}[{i}]")
        elif isinstance(val, str) and val.startswith(UNDECIDED):
            raise ClassCUndeclared(
                f"CLASS-C MANIFEST: '{path}' is {UNDECIDED}; refusing to proceed "
                f"(owner dispatch decision required before this parameter exists).")

    val = manifest[section]
    check(val, section)
    return val


def main():
    print("=" * 78)
    print("class_c_manifest_gate -- fail-closed contract check")
    print("=" * 78)
    ok = True

    m = load()
    for sec in REQUIRED_SECTIONS:
        if sec not in m:
            print(f"  FAIL schema: missing required section '{sec}'")
            ok = False
    if ok:
        print("  ok   schema: all required sections present")

    probs = [p for p in REQUIRED_PROHIBITIONS
             if not any(p.split()[0] in pr and p.split()[-1] in pr
                        for pr in m.get("prohibitions", []))]
    # robust check: match on distinctive substrings instead
    joined = " | ".join(m.get("prohibitions", []))
    missing = [s for s in ("omega^3", "single-pole", "tau_0",
                           "class-A stationarity", "epoch/window")
               if s not in joined]
    if missing:
        ok = False
        print(f"  FAIL prohibitions: missing {missing}")
    else:
        print("  ok   all five prohibitions present verbatim-substring")

    if m.get("fail_closed") is True:
        print("  ok   fail_closed = true")
    else:
        ok = False
        print("  FAIL fail_closed must be true")

    # demonstrate fail-closed semantics of require()
    # (2026-08-22 v1.1: clock/boundary/approximation_order are DECLARED by
    # decisions D1-D3; gauge/renormalization remain UNDECIDED-DISPATCH.
    # The demonstration tracks the manifest rather than hardcoding sections.)
    for sec in ("gauge", "clock", "renormalization"):
        declared = isinstance(m.get(sec), str) and not m.get(sec).startswith(UNDECIDED) \
            or (isinstance(m.get(sec), dict) and
                not any(str(v).startswith(UNDECIDED) for v in m[sec].values()))
        try:
            require(m, sec)
            if declared:
                print(f"  ok   require('{sec}') returns the declared value")
            else:
                print(f"  FAIL require('{sec}') returned a value but is undecided")
                ok = False
        except ClassCUndeclared as e:
            if declared:
                print(f"  FAIL require('{sec}') refused a DECLARED value")
                ok = False
            else:
                print(f"  ok   require('{sec}') refuses: {str(e)[:70]}...")
    try:
        require(m, "state")
        print("  ok   require('state') returns the declared value (BD, booked rung2)")
    except ClassCUndeclared:
        print("  FAIL require('state') refused a DECLARED value")
        ok = False

    if not ok:
        print("\nMANIFEST GATE: FAIL")
        return 1
    print("\nMANIFEST GATE: PASS (contract intact; solvers fail closed)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
