#!/usr/bin/env python3
"""class_c_solver: the ONLY sanctioned entry point for Class-C execution.

PHASE 1/2 artefact (owner brief 2026-08-21). This solver exists primarily to be
REFUSED: every physics-enabling manifest section is currently UNDECIDED-DISPATCH,
so run() must fail closed. It gives the dependency-closure audit a real
execution surface to police, and it prevents any other entry point from
becoming a de-facto solver.

CONTRACT (hard):
  * EVERY clock/gauge/regulator/approximation/boundary parameter is obtained
    through provenance.class_c_manifest_gate.require() -- never from module
    constants, environment variables, config files, or default arguments.
  * If require() raises ClassCUndeclared, this solver exits with code 2
    (REFUSED) and computes nothing.
  * There is deliberately NO fallback, NO default, NO target timescale, and
    NO imported class-A result anywhere in this file.

Exit codes: 0 impossible while undecided; 2 = REFUSED (expected);
3 = internal contract violation (bug -- investigate, do not route around).

Run: python3 calc/class_c_solver.py [--selftest]
"""
import os
import sys

sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "provenance"))

from class_c_manifest_gate import load, require, ClassCUndeclared  # noqa: E402

REQUIRED_FOR_EXECUTION = [
    "gauge",
    "clock",
    "boundary_conditions",
    "renormalization",
    "approximation_order",
]


def main(argv):
    selftest = "--selftest" in argv
    print("=" * 78)
    print("class_c_solver -- fail-closed Class-C execution entry point")
    print("=" * 78)

    manifest = load()
    missing = []
    for section in REQUIRED_FOR_EXECUTION:
        try:
            val = require(manifest, section)
            print(f"  declared: {section} = {str(val)[:70]}")
        except ClassCUndeclared as exc:
            missing.append(section)
            print(f"  REFUSED : {str(exc)[:100]}")

    # regulators: the list exists but must be NON-EMPTY with declared purpose
    regs = require(manifest, "regulators")
    if not regs:
        missing.append("regulators(non-empty)")
        print("  REFUSED : regulators list is empty; any regulator must be "
              "declared in the manifest BEFORE use")

    if missing:
        print("\nCLASS-C SOLVER REFUSED: {} undeclared prerequisite(s): {}".format(
            len(missing), ", ".join(missing)))
        print("No computation performed. Owner dispatch decisions are required")
        print("in CLASS_C_MANIFEST.json before this solver can execute.")
        if selftest:
            print("\nSELFTEST GREEN (refusal behaviour correct while undecided).")
            return 0
        return 2

    # UNREACHABLE while the manifest holds UNDECIDED-DISPATCH sentinels.
    print("EXECUTING -- this branch is unreachable until the owner populates")
    print("the manifest; its appearance without that is a contract breach.")
    if selftest:
        print("\nSELFTEST: FAIL (executed despite undecided prerequisites)")
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
