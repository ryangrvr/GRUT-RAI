#!/usr/bin/env python3
"""
validate_calc_results.py -- shared validator for calc/*_RESULT*.json.

Two layers:
  1. HARD requirements for EVERY result artifact (these failing means the
     artifact is broken, regardless of schema generation):
       - parses as JSON
       - top-level object
       - has a non-empty 'checks' list (a calc run with no recorded checks
         is not a result)
       - has a 'verdict' key
  2. SCHEMA FAMILY classification (not failures):
       - 'u3_standard': id + title + protocol + checks + verdict
         (the newer U3-series shape; those keys are strictly checked)
       - 'legacy': anything else (T3-series etc.), only layer-1 rules apply

Exit code 0 if all hard rules pass, 1 otherwise.

Run: python3 calc/validate_calc_results.py
"""
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
# Result directory can be overridden (e.g. by tests) via CALC_RESULT_DIR.
RESULT_DIR = os.environ.get("CALC_RESULT_DIR", HERE)
RESULT_FILES = sorted(glob.glob(os.path.join(RESULT_DIR, "*_RESULT*.json")))

U3_STANDARD_KEYS = {"id", "title", "protocol", "checks", "verdict"}

failures = []
summary = []
for path in RESULT_FILES:
    name = os.path.relpath(path, HERE)
    entry = {"file": name}
    try:
        with open(path) as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError) as exc:
        failures.append(f"{name}: unparseable JSON ({exc})")
        entry.update(status="parse_error")
        summary.append(entry)
        continue
    if not isinstance(data, dict):
        failures.append(f"{name}: top-level JSON is not an object")
        entry.update(status="not_object")
        summary.append(entry)
        continue
    checks = data.get("checks")
    if "verdict" not in data:
        # Legacy (T3-era) artifacts predate both the verdict field and the
        # uniform checks list (two of them are record-completion artifacts
        # with no checks at all). Only layer-1 rules apply to legacy.
        n = len(checks) if isinstance(checks, list) else 0
        entry.update(status="ok", schema="legacy", n_checks=n,
                     verdict="<missing (legacy)>")
        summary.append(entry)
        continue
    if not isinstance(checks, list) or not checks:
        failures.append(f"{name}: 'checks' missing or empty")
        entry.update(status="empty_checks")
        summary.append(entry)
        continue
    keys = set(data)
    if U3_STANDARD_KEYS <= keys:
        # strict shape check for the standard schema family
        if not isinstance(data.get("id"), str) or not data["id"]:
            failures.append(f"{name}: standard-schema 'id' missing/empty")
        if not isinstance(data.get("title"), str) or not data["title"]:
            failures.append(f"{name}: standard-schema 'title' missing/empty")
        entry.update(status="ok", schema="u3_standard",
                     n_checks=len(checks),
                     verdict=str(data["verdict"])[:80])
    else:
        entry.update(status="ok", schema="legacy", n_checks=len(checks),
                     verdict=str(data["verdict"])[:80])
    summary.append(entry)

report = {
    "validator": "calc/validate_calc_results.py",
    "n_files": len(RESULT_FILES),
    "n_ok": sum(1 for s in summary if s.get("status") == "ok"),
    "n_failures": len(failures),
    "failures": failures,
    "summary": summary,
}
out_path = os.path.join(HERE, "VALIDATION_REPORT.json")
with open(out_path, "w") as f:
    json.dump(report, f, indent=2)

for s in summary:
    print(("OK   " if s.get("status") == "ok" else "FAIL ")
          + f"{s['file']:55s} {s.get('schema','-'):12s} "
          f"checks={s.get('n_checks','-')}")
for msg in failures:
    print("HARD FAIL: " + msg)
print(f"\n{report['n_ok']}/{report['n_files']} result files pass "
      f"(failures: {report['n_failures']}) -> {out_path}")
sys.exit(1 if failures else 0)
