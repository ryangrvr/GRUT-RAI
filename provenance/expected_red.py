#!/usr/bin/env python3
"""expected_red: classification, not suppression -- declared at (test, CASE) granularity.

A suite that is always red teaches its readers that red means nothing, and a fourth failure hides
among three. But quieting a test that caught a real, unadjudicated problem would be adjusting the
instrument -- and adjusting the instrument that found your own error is the worst version of it.
So failures get a THIRD state: declared here, WITH the open adjudication each one waits on.

TWO HOLES IN THE FIRST VERSION, BOTH FOUND 2026-08-18, BOTH STRUCTURAL RATHER THAN LOCAL:

  1. IT DECLARED WHOLE TESTS. Several of these guards are SET-VALUED -- one test over every sealed
     pre-registration, one over every claim in the register. Declaring such a test red silences it
     FOR EVERY FUTURE MEMBER OF THE SET, and declarations here are permanent by design, so the
     blindness would be too. A third file with the very defect a guard was written against would
     have sealed cleanly, because the guard's failure was already on the books.
     FIX: every declaration supplies an ENUMERATOR -- the same function the test asserts on -- and
     the runner diffs the LIVE CASE SET against the declared one. A new member is a NEW RED even
     while the test remains a declared failure. It paid for itself on its first run: three cases
     were masked by fail-fast, and one declared case turned out never to have been detected.

  2. THE ADJUDICATIONS WERE UNCHECKED PROSE. Each declaration asserted "an adjudication is open"
     and nothing verified it. A pass closes, the test keeps failing for an unrelated reason, and
     this runner prints green while citing a ruling that already happened. Staleness cannot catch
     it -- stale fires only when a test starts PASSING.
     FIX: passes have ids in OPEN_PASSES.txt; every CASE cites one; an unknown or CLOSED pass
     fails in its own right. This too paid immediately: the four declarations turned out to span
     four passes distributed differently than they were written -- two declarations sharing one
     adjudication, and one declaration silently spanning two.

Nothing is silenced: every test still runs and still fails. This says only which failures are
known, at which cases, and what would close them.

Run:  python3 expected_red.py   -> exit 0 iff the failing set AND every case set is as declared
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PASSES_FILE = os.path.join(HERE, "OPEN_PASSES.txt")
sys.path.insert(0, HERE)


def _tier_cases():
    from test_resident import tier_contradiction_cases
    return tier_contradiction_cases()


def _annotation_cases():
    from test_resident import clean_annotation_rejection_cases
    return clean_annotation_rejection_cases()


def _pointer_cases():
    from test_prereg_immutable import pointer_leak_cases
    return pointer_leak_cases()


def _numeric_cases():
    from test_prereg_immutable import numeric_leak_cases
    return numeric_leak_cases()


# Every declaration: the enumerator that produces its live case set, and each declared case mapped
# to the OPEN PASS it waits on. The prose for a pass lives in OPEN_PASSES.txt, once, not here.
DECLARED = {
    "test_resident.py::TestResident::test_no_tier_contradiction_in_live_register": {
        "enumerate": _tier_cases,
        "cases": {
            "rung1_inin_action": "P1-RUNG1-TIER",
            "rung2_kms_gate": "P1-RUNG1-TIER",
        },
    },
    "test_resident.py::TestResident::test_clean_annotation_change_passes": {
        "enumerate": _annotation_cases,
        "cases": {
            "rung1_inin_action": "P1-RUNG1-TIER",
            "rung2_kms_gate": "P1-RUNG1-TIER",
        },
    },
    "test_prereg_immutable.py::TestBlindSafe::"
    "test_no_sealed_prereg_points_outward_at_its_own_context": {
        "enumerate": _pointer_cases,
        "cases": {
            "PREREG_DESI_DR3_2026-08-18_v2.txt -> RESULT_DESI_DR3_CONTEXT_2026-08-18.txt "
            ":: an arXiv id": "P3-SEALED-HISTORY-POLICY",
            "PREREG_TERMINATION_V3_2026-08-10.txt -> RESULT_TERMINATION_events.txt "
            ":: an arXiv id": "P2-TERMINATION-EVENTLOG",
            "PREREG_TERMINATION_V4_2026-08-10.txt -> RESULT_TERMINATION_events.txt "
            ":: an arXiv id": "P2-TERMINATION-EVENTLOG",
            "PREREG_TERMINATION_V3_2026-08-10.txt -> RESULT_KAPPA_2026-08-08.txt "
            ":: a sigma value": "P4-TERMINATION-KAPPA-RESULT",
            "PREREG_TERMINATION_V3_2026-08-10.txt -> RESULT_KAPPA_2026-08-08.txt "
            ":: a sigma value stated as a quantity rather than as a bound":
                "P4-TERMINATION-KAPPA-RESULT",
            "PREREG_TERMINATION_V3_2026-08-10.txt -> RESULT_KAPPA_2026-08-08.txt "
            ":: a signed numeric range": "P4-TERMINATION-KAPPA-RESULT",
        },
    },
    "test_prereg_immutable.py::TestBlindSafe::"
    "test_blind_safe_preregs_carry_no_result_adjacent_numerics": {
        "enumerate": _numeric_cases,
        "cases": {
            "PREREG_DESI_DR3_2026-08-18.txt :: an arXiv id": "P3-SEALED-HISTORY-POLICY",
        },
    },
}


def open_passes():
    """{id: STATUS} from OPEN_PASSES.txt. Closing a pass is a human act performed in that file."""
    out, cur = {}, None
    with open(PASSES_FILE) as f:
        for line in f:
            m = re.match(r"^PASS\s+(\S+)\s*$", line)
            if m:
                cur = m.group(1)
                out[cur] = None
                continue
            m = re.match(r"^STATUS:\s*(\S+)\s*$", line)
            if m and cur:
                out[cur] = m.group(1).upper()
                cur = None
    return out


def main():
    problems = []
    passes = open_passes()

    # -- the adjudications each case cites must exist and still be open ------------------------
    for test, d in DECLARED.items():
        for case, pid in d["cases"].items():
            if pid not in passes:
                problems.append(f"UNKNOWN PASS {pid!r} cited by {test}\n"
                                f"      case: {case}\n"
                                f"      No such id in OPEN_PASSES.txt. A declaration must cite a "
                                f"pass that exists.")
            elif passes[pid] != "OPEN":
                problems.append(f"CLOSED PASS {pid!r} ({passes[pid]}) still cited by {test}\n"
                                f"      case: {case}\n"
                                f"      The adjudication has been ruled. Remove this declaration; "
                                f"if the test still fails, that failure is NEW.")

    # -- the failing tests must be exactly the declared tests -----------------------------------
    r = subprocess.run([sys.executable, "-m", "pytest", "-q", HERE],
                       capture_output=True, text=True, cwd=HERE)
    failing = set(re.findall(r"^FAILED (\S+)", r.stdout, re.M))
    declared = set(DECLARED)
    for t in sorted(failing - declared):
        problems.append(f"NEW RED: {t}\n      Not a declared adjudication.")
    for t in sorted(declared - failing):
        problems.append(f"STALE DECLARATION: {t} now PASSES -- remove it from DECLARED.")

    # -- and each declared test's LIVE case set must be exactly its declared case set -----------
    for t in sorted(failing & declared):
        d = DECLARED[t]
        live = set(d["enumerate"]())
        want = set(d["cases"])
        if not live:
            problems.append(f"UNMODELLED FAILURE: {t} fails, but its enumerator finds no case.\n"
                            f"      It is failing for a reason this declaration does not model, "
                            f"which is a NEW RED wearing an old declaration's name.")
            continue
        for c in sorted(live - want):
            problems.append(f"NEW RED (case): {t}\n      {c}\n"
                            f"      The test is a declared failure; THIS CASE IS NOT. A new "
                            f"member of a declared set is new.")
        for c in sorted(want - live):
            problems.append(f"STALE CASE: {t}\n      {c}\n"
                            f"      Declared, but no longer produced. Remove it.")
        by_pass = {}
        for c in sorted(live & want):
            by_pass.setdefault(d["cases"][c], []).append(c)
        print(f"  EXPECTED-RED  {t}")
        for pid, cs in sorted(by_pass.items()):
            print(f"                [{pid}] {len(cs)} case(s)")
            for c in cs:
                print(f"                  - {c}")

    if problems:
        print("\n" + "\n".join(f"  *** {p}" for p in problems))
        print("\nFAIL: the failing set is not the declared set.")
        return 1
    n_cases = sum(len(d["cases"]) for d in DECLARED.values())
    print(f"\nAll {len(failing)} failing tests are declared, at {n_cases} declared cases, "
          f"each citing an OPEN pass. No new red.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
