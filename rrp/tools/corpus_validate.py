#!/usr/bin/env python3
"""RRP corpus validator — schema and vocabulary enforcement, never adjudication.

Contract: rrp/CAPABILITY_CONTRACT_01.md (instance 1). Validates FORM and emits COUNTS.
It cannot establish the truth of any entry; a wrong-but-well-formed entry passes.
Schema: CORPUS_SCHEMA v0.
"""
import json
import re
import sys
import glob
import os

SCHEMA_VERSION = "CORPUS_SCHEMA v0"

FIELDS = [
    "phenomena", "formalism", "primitives", "derived_objects", "empirical_inputs",
    "constants", "symmetries", "limits", "known_connections", "known_disconnects",
    "open_problems", "observables", "alternative_formulations", "domain_of_validity",
]
TOP_REQUIRED = ["domain", "grade", "schema", "date", "notes"] + FIELDS
PROVENANCE = {"OBSERVED", "COMMUNITY-DERIVED", "PROGRAM-RESULT", "ABSENCE"}
VERIFICATION = {"VERIFIED", "TO-VERIFY"}
ENTRY_REQUIRED = ["claim", "provenance", "verification", "source"]
# Corpus records what IS, never what is REQUIRED (Stage 4's job). WARN-level screen.
REQUIREMENT_LANGUAGE = re.compile(
    r"\b(must be satisfied|is required by any|any successful theory must|forces any theory)\b",
    re.IGNORECASE)
EDGE_CLASSES = {"IDENTITY", "MATHEMATICAL_ANALOGY", "STRUCTURAL_ISOMORPHISM",
                "LIMIT_RELATION", "EFFECTIVE_CORRESPONDENCE", "EMPIRICAL_CORRELATION",
                "VOCABULARY_ONLY", "UNRESOLVED"}


def validate_file(path):
    errors, warns = [], []
    counts = {p: 0 for p in PROVENANCE}
    vcounts = {v: 0 for v in VERIFICATION}
    try:
        rec = json.load(open(path))
    except Exception as e:  # noqa: BLE001 - report any parse failure uniformly
        return [f"JSON parse failure: {e}"], [], counts, vcounts
    for f in TOP_REQUIRED:
        if f not in rec:
            errors.append(f"missing top-level field: {f}")
    if rec.get("schema") != SCHEMA_VERSION:
        errors.append(f"schema version mismatch: {rec.get('schema')!r} != {SCHEMA_VERSION!r}")
    for f in FIELDS:
        for i, e in enumerate(rec.get(f, []) or []):
            tag = f"{f}[{i}]"
            if not isinstance(e, dict):
                errors.append(f"{tag}: entry is not an object")
                continue
            for k in ENTRY_REQUIRED:
                if k not in e:
                    errors.append(f"{tag}: missing key {k}")
            p, v = e.get("provenance"), e.get("verification")
            if p not in PROVENANCE:
                errors.append(f"{tag}: illegal provenance {p!r}")
            else:
                counts[p] += 1
            if v not in VERIFICATION:
                errors.append(f"{tag}: illegal verification {v!r}")
            else:
                vcounts[v] += 1
            if REQUIREMENT_LANGUAGE.search(str(e.get("claim", ""))):
                warns.append(f"{tag}: requirement-language in corpus claim (Stage-4 material?)")
            ec = e.get("edge_class")
            if ec is not None and ec not in EDGE_CLASSES:
                errors.append(f"{tag}: illegal edge_class {ec!r}")
    return errors, warns, counts, vcounts


def main(paths):
    fail = False
    for path in paths:
        errors, warns, counts, vcounts = validate_file(path)
        status = "PASS" if not errors else "FAIL"
        fail = fail or bool(errors)
        print(f"{status} {os.path.basename(path)}  "
              f"entries={sum(counts.values())} "
              f"[OBSERVED={counts['OBSERVED']} COMM={counts['COMMUNITY-DERIVED']} "
              f"PROG={counts['PROGRAM-RESULT']} ABS={counts['ABSENCE']}] "
              f"VERIFIED={vcounts['VERIFIED']} TO-VERIFY={vcounts['TO-VERIFY']}")
        for e in errors:
            print(f"  ERROR {e}")
        for w in warns:
            print(f"  WARN  {w}")
    print("NOTE: validates form and counts only — it cannot establish the truth of any entry.")
    return 1 if fail else 0


if __name__ == "__main__":
    args = sys.argv[1:] or sorted(glob.glob(os.path.join(os.path.dirname(__file__),
                                                         "..", "corpus", "domains", "*.json")))
    sys.exit(main(args))
