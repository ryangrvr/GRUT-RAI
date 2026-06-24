"""GRUT-RAI v4.1 — the build gate. CI fails (exit 1) on any tier violation.

This is the mechanized Principle 0. If this passes, the registry is honest by
construction: no DERIVED claim lacks a passing check or a novelty tag, none
launders an OPEN/CONJECTURAL input into DERIVED, and nothing is RESOLVED over an
open blocker.

Run:  python -m v4.ci_check    (exit 0 = clean; exit 1 = violations printed)
"""
from __future__ import annotations

import sys

from v4.gate import validate
from v4.registry import REGISTRY


def main() -> int:
    violations = validate(REGISTRY)
    if violations:
        print(f"GATE FAILED — {len(violations)} violation(s):")
        for v in violations:
            print(f"  ✗ {v}")
        return 1
    print(f"GATE PASSED — {len(REGISTRY)} claims, 0 violations.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
