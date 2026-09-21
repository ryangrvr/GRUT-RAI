#!/usr/bin/env python3
"""T3-05G RECORD COMPLETION -- harvest the completed run's checks into JSON.

The t3_05g_provenance_close.py run of 2026-09-19 completed ALL physics
checks (G1a-G3c, all PASS, per /tmp/t3_05g_run2.log) but crashed in the
OPTIONAL numerical spot-check (general-d A2_rec could not be floated
because d was left symbolic).  The crash occurred BEFORE the JSON write.

This instrument performs NO recomputation and NO re-derivation.  It
harvests the verbatim check records from the preserved run log into the
result JSON that the crash prevented from being written, marked
explicitly as RECOVERED.  The to_d3()/safeguard fix (d=3 specialization
+ exception guard) is already applied to the instrument source for any
future rerun.
"""
import json
import re
import os

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = "/tmp/t3_05g_run2.log"
RESULT_PATH = os.path.join(HERE, "T3_05G_PROVENANCE_CLOSE_RESULT.json")

log = open(LOG).read()

checks = []
for m in re.finditer(r"^\s*(ok   |FAIL )(\S+): (.+?)(?=\n\s*(?:ok   |FAIL )|\nTraceback|\Z)",
                     log, re.S | re.M):
    status, name, msg = m.groups()
    checks.append({"name": name.strip(), "pass": status.strip() == "ok",
                   "msg": re.sub(r"\s+", " ", msg).strip()})

# crash documentation
crash_note = ("post-G3 numerical spot-check crashed BEFORE the JSON write: "
              "TypeError Cannot convert expression to float -- A2_rec still "
              "carries omega**d (d not substituted). Instrument bug in the "
              "OPTIONAL safeguard, not in any physics check. Fixed in "
              "instrument source (d=3 specialization + exception guard).")
instrument = "calc/t3_05g_provenance_close.py"

results = {
    "instrument": instrument,
    "status": "RECOVERED: all physics checks completed and PASSED in the "
              "2026-09-19 run; JSON write was prevented by a crash in the "
              "optional numeric safeguard AFTER G3. This file is the "
              "record-completion artifact (no recomputation).",
    "crash_documentation": crash_note,
    "checks": checks,
    "summary": {
        "provenance_chain": ("CLOSED at response level: Im[P0]=-127/(1280 pi) "
                             "(u_b-free content), Im[P2]=+11 w^2 u_b^2/(64 pi), "
                             "Im[P4]=-9 w^4 u_b^4/(640 pi); sum == assembled A2 "
                             "exactly under Gamma-aware canonicalization. "
                             "Kernel-level u_b origin (solely (1-Hu)(1-Hu_p)) "
                             "stands from T3-05F and was not re-derived."),
        "parity": ("mechanical: WMINUS == WPLUS(u<->u_p) exactly; every raw H^4 "
                   "term even in u_b; kernel u_b^1 cancellation is assembly-level"),
        "open_physics_question": ("whether the surviving u_b^2, u_b^4 dependence "
                                  "is removable under the correct frame/assembly "
                                  "prescription -- NOT decided here"),
    },
    "w0": "computed-and-reported, NOT banked",
    "scope": ("diagnostic closure ONLY; frozen artifacts read-only; no H^6; "
              "R' untouched; conditional on the declared patch-local quotient"),
    "source_log": LOG,
}

n_pass = sum(1 for c in checks if c["pass"])
print(f"harvested {len(checks)} checks ({n_pass} pass) from {LOG}")
for c in checks:
    print(("  ok   " if c["pass"] else "  FAIL ") + c["name"] + ": "
          + c["msg"][:100])
with open(RESULT_PATH, "w") as f:
    json.dump(results, f, indent=2)
print(f"result written: {RESULT_PATH}")
raise SystemExit(0 if n_pass == len(checks) and checks else 1)
