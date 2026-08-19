#!/usr/bin/env python3
"""expected_red: classification, not suppression.

A suite that is always red teaches its readers that red means nothing, and a fourth failure hides
among three. But quieting a test that caught a real, unadjudicated problem would be adjusting the
instrument -- and adjusting the instrument that found your own error is the worst version of it.

So failures get a THIRD state. Each expected red is declared here WITH THE OPEN PASS IT WAITS ON,
so the count is auditable and a genuinely new red is visibly new. Nothing is silenced: every test
still runs and still fails; this only says which failures are known and what would close them.

A declaration here is a claim that an adjudication is open. When the pass lands, the entry is
removed -- and if the test still fails after that, it is a NEW RED.

Run:  python3 expected_red.py     -> exit 0 if the failing set is exactly the declared set
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

EXPECTED = {
    "test_resident.py::TestResident::test_no_tier_contradiction_in_live_register":
        "OPEN PASS: rung1's tier adjudication. Booking background_time_translation_flow and "
        "wiring its mandated R5 edges made rung1 (tier shown) rest on an assumed input. TWO "
        "questions reserved: is the edge representation wrong, AND is 'shown' right for a node "
        "standing on five assumed inputs -- the second being the convention that has never been "
        "screened. Closes when the owner rules.",
    "test_resident.py::TestResident::test_clean_annotation_change_passes":
        "OPEN PASS: same adjudication. A trivial edit to rung1 now flags because rung1 carries a "
        "standing tier contradiction; this is a consequence of the above, not a separate defect.",
    "test_prereg_immutable.py::TestBlindSafe::"
    "test_no_sealed_prereg_points_outward_at_its_own_context":
        "TWO CASES, ONE OWNER-ONLY QUESTION. (1) MINE, permanent: "
        "PREREG_DESI_DR3_2026-08-18_v2.txt is sealed and names the file its motive figures moved "
        "to -- the pointer IS the leak, the defect this guard's own docstring records, reproduced "
        "one hop out inside the repair for a v1 violation. v3 carries the same predicate with no "
        "outbound pointer; the seal forbids editing v2, so the record keeps it. (2) PRE-EXISTING, "
        "SURFACED NOT ADJUDICATED: PREREG_TERMINATION_V3_2026-08-10.txt is blind-safe and names "
        "RESULT_TERMINATION_events.txt, which carries arXiv identifiers. Whether that is the same "
        "defect or a false positive is a JUDGEMENT THE BUILDER SHOULD NOT MAKE ALONE -- the "
        "termination condition names its event log BY ARCHITECTURE (R4: quotes decide, entries "
        "land in the log), and calling a pre-existing sealed instrument defective on a test "
        "written hours ago, which already over-fired once, is exactly the over-demotion this "
        "program treats as its own defect class. Owner rules.",
    "test_prereg_immutable.py::TestBlindSafe::"
    "test_blind_safe_preregs_carry_no_result_adjacent_numerics":
        "PERMANENT AND IRREPARABLE BY DESIGN: PREREG_DESI_DR3_2026-08-18.txt (v1) declared "
        "BLIND-SAFE and carried identifiers and figures. The seal forbids editing it, so the "
        "violation is part of the record forever; v3 carries the same predicate cleanly. Whether "
        "the guard should treat a superseded prereg as history is the OWNER's call, not the "
        "builder's -- the builder is the one it caught, and quieting it would be adjusting the "
        "instrument that found the error.",
}


def main():
    r = subprocess.run([sys.executable, "-m", "pytest", "-q", HERE],
                       capture_output=True, text=True, cwd=HERE)
    failing = set(re.findall(r"^FAILED (\S+)", r.stdout, re.M))
    declared = set(EXPECTED)
    new = sorted(failing - declared)
    stale = sorted(declared - failing)
    for t in sorted(failing & declared):
        print(f"  EXPECTED-RED  {t}\n                {EXPECTED[t].split('.')[0]}.")
    for t in stale:
        print(f"  *** STALE DECLARATION: {t} now PASSES -- remove it from EXPECTED.")
    for t in new:
        print(f"  *** NEW RED: {t} -- not a declared adjudication.")
    if new or stale:
        print("\nFAIL: the failing set is not the declared set.")
        return 1
    print(f"\nAll {len(failing)} failures are declared, each pinned to an open pass. No new red.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
