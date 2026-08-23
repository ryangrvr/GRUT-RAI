#!/usr/bin/env python3
"""class_c_dependency_closure: can Class-C code acquire a physical parameter
WITHOUT passing through the manifest gate?

Owner brief 2026-08-21: the manifest contract is only airtight if ALL physical
inputs must pass through require(). This scanner polices the CLASS-C EXECUTABLE
SURFACE (currently calc/class_c_solver.py; glob calc/class_c*.py) for the
known bypass channels:

    ENV_BYPASS          os.environ / getenv reads
    SEED_BYPASS         random seed setting
    CONFIG_FILE_READ    open()/read of any non-manifest file
    HISTORICAL_IMPORT   import of class-A/historical calculation modules
    MODULE_CONSTANT     module-level numeric assignment to a physics-named name
    DEFAULT_ARG_NUMERIC numeric default argument on a physics-named parameter
    FORBIDDEN_TOKEN     tau_0 / s=3 / single-pole / J~omega^3 / 41.9 (reuse of
                        the Phase-0 contamination set)
    POLE_INJECTION      variables/flags asserting a favourable pole outcome

MUTATION SELFTEST (runs first, in-memory -- nothing is written to the tree):
six known-bad source strings are fed to the detector; every one MUST be caught,
and a known-clean source MUST pass. If any mutant survives, exit 1.

Exit 0 = surface closed (no bypass found, mutants all caught); 1 = open.
Pure stdlib. Run: python3 provenance/class_c_dependency_closure.py
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SURFACE_GLOB = "calc/class_c*.py"

PHYS_NAME = r"\w*(k_min|kmax|kmin|tau|epoch|regulator|omega_c|cutoff|window)\w*"

# (name, pattern, flags) -- MODULE_CONSTANT/DEFAULT_ARG_NUMERIC are
# case-insensitive because physics-named constants arrive as K_MIN, Tau0, ...
RULES = [
    ("ENV_BYPASS", r"os\.environ|getenv\s*\(", 0),
    ("SEED_BYPASS", r"\bseed\s*\(|random\.seed", 0),
    ("CONFIG_FILE_READ", r"\bopen\s*\(", 0),
    ("HISTORICAL_IMPORT",
     r"import\s+(worldline_reduction|tt_worldline_spectrum|finite_T_pole_structure)"
     r"|from\s+(worldline_reduction|tt_worldline_spectrum|finite_T_pole_structure)\s+import",
     0),
    ("MODULE_CONSTANT",
     r"^[A-Z_]*(" + PHYS_NAME + r")\w*\s*=\s*[-+]?[0-9]",
     re.MULTILINE | re.IGNORECASE),
    ("DEFAULT_ARG_NUMERIC",
     r"def\s+\w+\s*\([^)]*" + PHYS_NAME + r"\w*\s*=\s*[-+]?[0-9\.]",
     re.IGNORECASE),
    ("FORBIDDEN_TOKEN",
     r"\btau_?0\b|\b41\.9\b|\bs\s*=\s*3\b|single[- ]pole|omega\s*\^\s*3|\bw\s*\*\*\s*3\b",
     re.IGNORECASE),
    ("POLE_INJECTION", r"(?i)\b(pole_found|has_pole|pole_detected|favourable|favorable)\b", 0),
]

# ------------------------------------------------------------- mutants (bad)
MUTANTS = {
    "ENV_BYPASS": "import os\nK = os.environ.get('K_MIN', 0.25)\n",
    "SEED_BYPASS": "import random\nrandom.seed(1234)\n",
    "CONFIG_FILE_READ": "cfg = open('hidden_calibration.json')\n",
    "HISTORICAL_IMPORT": "import worldline_reduction as wr\nJ = wr.J\n",
    "MODULE_CONSTANT": "K_MIN = 0.25\ntau_eff = K_MIN * 3\n",
    "DEFAULT_ARG_NUMERIC": "def kernel(omega, k_min=0.25):\n    return omega\n",
    "FORBIDDEN_TOKEN": "J = w ** 3  # the registered super-Ohmic bath, s = 3\n",
    "POLE_INJECTION": "pole_found = True  # favourable outcome confirmed\n",
}
CLEAN_SOURCE = (
    "import math\n"
    "from class_c_manifest_gate import load, require, ClassCUndeclared\n"
    "def amplitude(manifest):\n"
    "    gauge = require(manifest, 'gauge')\n"
    "    return gauge\n"
)


def scan_source(src):
    """Return list of rule names triggered by one source string."""
    found = []
    for name, pat, flags in RULES:
        if re.search(pat, src, flags | re.MULTILINE):
            found.append(name)
    return found


def main():
    print("=" * 78)
    print("class_c_dependency_closure -- bypass-channel scan + mutation selftest")
    print("=" * 78)
    ok = True

    # ---- 1. mutation selftest: every known-bad mutant must be CAUGHT -------
    print("\nMUTATION SELFTEST (in memory; nothing written to the tree)")
    caught_all = True
    for name, bad_src in MUTANTS.items():
        hits = scan_source(bad_src)
        caught = len(hits) > 0
        print(f"  {'CAUGHT' if caught else 'SURVIVED'}: mutant {name} -> {hits}")
        caught_all &= caught
    clean_hits = scan_source(CLEAN_SOURCE)
    clean_ok = len(clean_hits) == 0
    print(f"  {'PASS' if clean_ok else 'FALSE POSITIVE'}: clean source -> {clean_hits}")
    check_mut = caught_all and clean_ok

    # ---- 2. live surface scan ----------------------------------------------
    print("\nLIVE SURFACE SCAN")
    files = sorted(glob.glob(os.path.join(ROOT, SURFACE_GLOB)))
    if not files:
        print(f"  FAIL: no files matched {SURFACE_GLOB} -- the execution surface")
        print("  is empty; the closure audit has nothing to police.")
        ok = False
    for path in files:
        rel = os.path.relpath(path, ROOT)
        src = open(path, encoding="utf-8").read()
        hits = scan_source(src)
        print(f"  {'CLEAN' if not hits else 'OPEN':7s} {rel}"
              + ("" if not hits else " -> " + ", ".join(hits)))
        if hits:
            ok = False

    verdict = (ok and check_mut)
    print("\n" + "=" * 78)
    if verdict:
        print("DEPENDENCY CLOSURE: CLOSED.")
        print("Every physical parameter on the Class-C executable surface must")
        print("arrive through manifest require(); no bypass channel is present;")
        print("all eight bypass mutants are caught by the detector; the clean")
        print("source passes. Phase 2-4 enforcement demonstrated against the")
        print("executable surface, not just the documentation.")
    else:
        print("DEPENDENCY CLOSURE: OPEN -- see FAIL lines above.")
    print("(This audit polices the surface; it does NOT certify physics results.)")
    if not verdict:
        print("SELFTEST: FAIL")
        return 1
    print("SELFTEST GREEN.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
