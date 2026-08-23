#!/usr/bin/env python3
"""class_c_freeze: freeze the Class-C dispatch package and emit the execution
certificate. PHASE 12 (owner adjudication 2026-08-22: Phase 12 FREEZE).

Behaviour:
  * re-runs every gate as a PRECONDITION (contamination audit CLEAN; manifest
    gate PASS; dependency closure CLOSED; solver selftest REFUSES correctly;
    benchmark matrix ALL PASS; register validator PASS). Any nonzero aborts
    the freeze before the certificate is written.
  * hashes every package component (sha256).
  * emits CLASS_C_DISPATCH_FROZEN.md -- ONCE. If the certificate already
    exists, the freeze REFUSES: the frozen contract is immutable; any change
    requires a NEW VERSIONED DISPATCH explaining why the old one failed
    (owner operational rule 2026-08-22).

Exit 0 = frozen; 1 = a gate failed; 2 = already frozen.
Pure stdlib. Run: python3 provenance/class_c_freeze.py
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CERT = os.path.join(ROOT, "CLASS_C_DISPATCH_FROZEN.md")

COMPONENTS = [
    "CLASS_C_MANIFEST.json",
    "CLASS_C_DISPATCH_SPEC.md",
    "provenance/CLASS_C_CONTAMINATION_AUDIT.md",
    "provenance/class_c_contamination_audit.py",
    "provenance/class_c_dependency_closure.py",
    "provenance/class_c_manifest_gate.py",
    "provenance/CLASS_C_BENCHMARK_MATRIX.md",
    "provenance/class_c_benchmark_matrix.py",
    "provenance/SCREEN_RECORD_2026-08-22_classc_infrastructure.md",
    "provenance/CLASS_C_PROVENANCE_LEDGER.md",
    "calc/class_c_solver.py",
]

GATES = [
    ("contamination audit", ["provenance/class_c_contamination_audit.py"]),
    ("manifest gate", ["provenance/class_c_manifest_gate.py"]),
    ("dependency closure", ["provenance/class_c_dependency_closure.py"]),
    ("solver selftest (must REFUSE)", ["calc/class_c_solver.py", "--selftest"]),
    ("benchmark matrix", ["provenance/class_c_benchmark_matrix.py"]),
    ("register validator", ["provenance/validate.py"]),
]




def sha(rel):
    with open(os.path.join(ROOT, rel), "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def main():
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # ---- immutability gate --------------------------------------------------
    if os.path.exists(CERT):
        print("FREEZE REFUSED: CLASS_C_DISPATCH_FROZEN.md already exists.")
        print("The frozen contract is immutable. Any necessary change requires")
        print("a NEW VERSIONED DISPATCH explicitly explaining why the old one failed.")
        return 2

    # ---- precondition gates -------------------------------------------------
    for name, cmd in GATES:
        r = subprocess.run([sys.executable] + cmd, cwd=ROOT,
                           capture_output=True, text=True)
        ok = r.returncode == 0
        print(f"  {'ok  ' if ok else 'FAIL'} {name}")
        if not ok:
            print((r.stdout + r.stderr).strip()[-600:])
            print("\nFREEZE ABORTED: gate failed ->", name)
            return 1

    # ---- hashes -------------------------------------------------------------
    hashes = [(rel, sha(rel)) for rel in COMPONENTS]

    # ---- manifest-declared parameter state ---------------------------------
    m = json.load(open(os.path.join(ROOT, "CLASS_C_MANIFEST.json"), encoding="utf-8"))
    unresolved = []
    for sec in ("gauge", "clock", "boundary_conditions", "renormalization",
                "approximation_order"):
        unresolved.append(f"{sec}: {m.get(sec)}")
    regs = m.get("regulators", [])
    unresolved.append("regulators: " + (str(regs) if regs else "NONE DECLARED"))

    # ---- emit certificate ---------------------------------------------------
    L = [
        "# CLASS-C DISPATCH FROZEN",
        "",
        f"*Frozen {ts} by `provenance/class_c_freeze.py`. This certificate is*"
        "*IMMUTABLE: emitted once, never edited. Any necessary change to the*"
        "*Class-C computational contract is a NEW RESEARCH EVENT requiring a new*"
        "*versioned dispatch that explicitly explains why this one failed.*",
        "",
        "## Package hashes (sha256)",
        "",
    ]
    for rel, h in hashes:
        L.append(f"- `{rel}` — `{h}`")
    L += [
        "",
        "## Executable entry point",
        "",
        "`calc/class_c_solver.py` — fail-closed via the manifest gate's require();",
        "demonstrated at freeze to refuse while any prerequisite is undecided.",
        "",
        "## Declared parameters at freeze time",
        "",
    ]
    for u in unresolved:
        L.append(f"- {u}")
    L += [
        "",
        "## Pre-dispatch requirements",
        "",
        "- Forbidden target leakage: **PASS** (contamination audit CLEAN)",
        "- Independent-route requirement: **PASS** (INDEPENDENT-CODE benchmark cell exact)",
        "- Fail-closed requirement: **PASS** (require() refusal demonstrated on",
        "  gauge/clock/renormalization; solver refuses six prerequisites)",
        "- Dependency closure: **CLOSED** (8 bypass mutants caught; live surface clean)",
        "",
        "## Preserved physics-dependent gates (not applicable yet != forgotten)",
        "",
        "- H->0 limit of assembled G_R^TT: blocked on class C execution",
        "- KMS behaviour of the assembled response: blocked on class C execution",
        "- gauge-equivalent agreement: blocked on gauge decision",
        "- weak-coupling Sigma limit: blocked on class C execution",
        "",
        "## Permitted outcomes (all first-class)",
        "",
        "isolated pole / multiple poles / branch cut / continuum / secular or",
        "nonstationary memory / no long-memory structure / ill-posed even after",
        "assembly. No outcome is preferred; none may be promoted without the",
        "four-lens screen and bank gate.",
        "",
        "## First-result treatment",
        "",
        "The first class-C result is a DISCOVERY RESULT about the assembled",
        "gravitational response. It is not a GRUT result and carries no favour.",
    ]
    with open(CERT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))

    print("\nFROZEN:", os.path.relpath(CERT, ROOT))
    for rel, h in hashes:
        print(f"  {h[:16]}...  {rel}")
    return 0


if __name__ == "__main__":
    sys.exit(main())


