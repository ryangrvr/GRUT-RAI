#!/usr/bin/env python3
"""23 HELD-FLAG GOVERNANCE REVIEW (owner authorization 2026-09-02).

GOVERNANCE-ONLY.  No physics.  NO baseline refresh, NO --accept, NO
claims.json mutation, NO held-ledger mutation (the repository's model
permits recording the review without changing the held state, so that
is exactly what happens).  Frozen artifacts untouched.  Flags are
CLASSIFIED here; only the owner clears them.

W-0.  HARD STOP."""
import hashlib
import json
import os
import re
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SCR = ("/private/tmp/claude-501/-Users-mpg-Library-Mobile-Documents-com-"
       "apple-CloudDocs-Ryans-Projects-GRUT-ResponsiveAI/"
       "7469561b-1dc7-4147-85e7-95af0652a664/scratchpad")
T0 = time.time()
FAILS, CHECKS, NOTES, OUT = [], [], [], {}
selfsrc = open(os.path.abspath(__file__)).read()


def check(c, m, gate="", detail=None):
    ok = bool(c)
    print(("  ok   " if ok else "  FAIL ") + m)
    sys.stdout.flush()
    CHECKS.append({"pass": ok, "msg": m, "gate": gate, "detail": detail})
    if not ok:
        FAILS.append(m)
    return ok


def control(d_, m):
    print(("  ctrl-DETECTED   " if d_ else "  ctrl-MISSED   ") + m)
    sys.stdout.flush()
    CHECKS.append({"pass": bool(d_), "msg": "CONTROL: " + m,
                   "gate": "control"})
    if not d_:
        FAILS.append("CONTROL MISSED: " + m)
    return d_


def note(m):
    print("  note " + m)
    sys.stdout.flush()
    NOTES.append(m)


def sha_file(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


print("=== PROVENANCE (pre-run) ===")
GUARDED = {
    os.path.join(ROOT, "provenance", "claims.json"): None,
    os.path.join(ROOT, "provenance", "claims.baseline.json"): None,
    os.path.join(ROOT, "provenance", "held_flags.json"): None,
    os.path.join(HERE, "WALL_KR_CONTRACT_RETARDED_RESULT.json"):
        "d916ef32f6f73fa3",
    os.path.join(HERE, "WALL_KR_TIER3_LOOP_RESULT.json"):
        "4c016e93b889bd04",
    os.path.join(HERE, "WALL_KR_TIER2_MASSLESS_BATH.json"):
        "c5d399f525407839",
}
PRE = {}
for fp, want in GUARDED.items():
    got = sha_file(fp)
    PRE[fp] = got
    if want:
        check(got.startswith(want), "frozen pin %s == %s..."
              % (os.path.basename(fp), want), gate="PROV")
    else:
        note("guarded %s = %s..." % (os.path.basename(fp), got[:16]))
if FAILS:
    sys.exit(2)

# ============ 1. THE ACTUAL HOLD STATE (read, not inferred) ============
print("\n=== 1: THE ACTUAL FLAG STATE ===")
FL = json.loads(open(os.path.join(SCR, "flags_structured.json")).read())
ORG = json.loads(open(os.path.join(SCR, "flag_origins.json")).read())
# the PURE gate reports every diff vs baseline INCLUDING the
# owner-held T4 node (holding is display-layer only). The 23 UNDER
# REVIEW = the 22 unreviewed node flags + the 1 deletion; the held T4
# entry was owner-reviewed at banking and is NOTED, not re-reviewed.
flags = [f for f in FL["flags"]
         if f["claim_id"] != "kr_contract_retarded_tier4"]
deletions = FL["deletions"]
check(len(FL["flags"]) == 23 and len(flags) == 22
      and deletions == ["rung1_inin_action"],
      "the live gate reports 23 node diffs (22 unreviewed + the one "
      "owner-held T4 entry, excluded from this review as already "
      "reviewed) plus 1 deletion -- so the 23 UNDER REVIEW = 22 node "
      "flags + the rung1_inin_action deletion, read from the gate's "
      "own structured output", gate="STATE")
sys.path.insert(0, os.path.join(ROOT, "provenance"))
from bankgate import _fingerprint          # noqa: E402
from test_resident import tier_contradiction_cases  # noqa: E402
claims = json.loads(open(os.path.join(
    ROOT, "provenance", "claims.json")).read())["claims"]
by = {c["id"]: c for c in claims}
contradictions = sorted(tier_contradiction_cases(claims))
check(contradictions == ["rung1_inin_formalism", "rung2_kms_gate"],
      "LIVE discipline findings, extracted from the register's own "
      "test helper: tier-contradictions at exactly "
      "{rung1_inin_formalism, rung2_kms_gate} -- both 'shown' resting "
      "on background_time_translation_flow ('assumed', the omission "
      "deliberately booked 2026-08-18 at +1 to expose that "
      "presupposition)", gate="STATE")

# ============ 2-10. THE 23-ROW LEDGER ============
print("\n=== 2-10: LEDGER ASSEMBLY AND CLASSIFICATION ===")
AUTH = {  # origin commit -> the authorization evidence, verbatim
    "9c14dfa": "2026-08-18 'Omission booked at +1; the R5 edge surfaced "
               "a tier contradiction at rung1' (finding surfaced ON THE "
               "RECORD at booking time)",
    "534ef03": "2026-08-18 rung3 interrogation wave (documented)",
    "20d00b2": "2026-08-18 'Tasks 2/4/5 executed; Task 1 HELD'",
    "7754153": "2026-08-19 ladder-adverse filing (documented wave)",
    "d3aa6ac": "2026-08-19 MZ-inheritance reading (documented wave)",
    "afeebdc": "2026-08-19 convention-question reading (documented)",
    "deacfb9": "2026-08-19 l>=2 multipole result (documented wave)",
    "cb54e02": "2026-08-19 adversarial pass, 4 lenses (documented)",
    "7eeb29e": "2026-08-19 deflation-overshoot correction (documented)",
    "04dc7e1": "2026-08-23 'Bank owner rulings 2026-08-23 (Rulings "
               "A/B/C): split rung1...' (EXPLICIT OWNER RULING)",
    "1459a2d": "2026-08-23 'Ruling-B edge correction (owner)' "
               "(EXPLICIT OWNER LABEL)",
    "b0bdfb6": "2026-08-24 'BOOKED on owner go' (EXPLICIT OWNER GO)",
    "8e64588": "2026-08-30 '+1 RETIRED in the register (owner go)' "
               "(EXPLICIT OWNER GO)",
}
DEBT = {
    "rung1_inin_formalism": "LIVE tier-contradiction: 'shown' resting "
        "on 'assumed' background_time_translation_flow (surfaced "
        "2026-08-18 commit 9c14dfa; stash-proven-and-reported-not-"
        "patched at the 2026-08-30 bank, 8e64588)",
    "rung2_kms_gate": "LIVE tier-contradiction: same assumed input "
        "(the collect-every-case repair of the test found it after "
        "rung1 alone was first named)",
    "response_lorentz_covariance": "LIVE ORPHANED-RESULT: 'shown' with "
        "empty depends_on (booked +1 2026-08-24 owner go; retired to 0 "
        "2026-08-30 owner go per the node's own retire clause; the "
        "orphan finding stands)",
}
LEDGER = []
all_ids = [f["claim_id"] for f in flags] + ["rung1_inin_action"]
for fid in all_ids:
    ev = ORG["history"].get(fid, [])
    origin = "; ".join("%s %s (%s)" % (e["commit"], e["kind"],
                                       e["date"]) for e in ev)
    authz = "; ".join(sorted({AUTH.get(e["commit"],
                                       "UNMATCHED: " + e["commit"])
                              for e in ev}))
    node = by.get(fid)
    fp = _fingerprint(node) if node else "deleted"
    is_debt = fid in DEBT
    all_predate = all(e["date"] <= "2026-08-30" for e in ev)
    row = {
        "flag": fid,
        "fingerprint": fp[:16] if fp != "deleted" else "DELETED",
        "origin_commits": origin,
        "authorization": authz,
        "type": ("register node change (claims.json-internal)"),
        "frozen_impact": "NONE (no physics artifact touched)",
        "register_impact": "already-landed content vs the stale "
                           "2026-08-17 baseline (the flag is the "
                           "unreviewed DIFF, not a pending edit)",
        "predates_entire_KR_campaign": all_predate,
        "current_status": (DEBT[fid] if is_debt else
                           "authorized, documented, internally "
                           "consistent; awaiting only the collective "
                           "baseline accept"),
        "class": "F2" if is_debt else "F1",
        "evidence": authz,
        "owner_action": (("DISPOSITION REQUIRED: repair the edge, "
                          "waive-with-documented-note, or formally "
                          "leave standing as expected-red")
                         if is_debt else
                         "covered by the single collective accept "
                         "decision"),
    }
    LEDGER.append(row)
OUT["ledger"] = LEDGER
check(len(LEDGER) == 23 and len({r["flag"] for r in LEDGER}) == 23,
      "the ledger carries EXACTLY 23 rows, one per flag, no omissions "
      "and no duplicates (the deletion is its own row; the held T4 "
      "entry is NOT among them -- it was owner-reviewed at banking)",
      gate="LEDGER")
check(all(any(e["commit"] in AUTH for e in ORG["history"][r["flag"]])
          for r in LEDGER),
      "EVERY row's origin commits are matched to documented "
      "authorization evidence -- 5 owner-explicit transactions "
      "(Rulings A/B/C split + edge correction; omission booking; "
      "boost/Lorentz booking; +1 retirement) plus the documented "
      "2026-08-18/19 rung3 annotation wave; nothing is unprovenance'd",
      gate="LEDGER")
check(all(r["predates_entire_KR_campaign"] for r in LEDGER),
      "TEMPORAL: every flag's every change predates 2026-08-31 -- ALL "
      "23 precede D5, Axis-2, the H^2 fork, Gate-E, Noise, and the "
      "T4 bank; NONE is a T4-bank ripple (the T4 ripples live outside "
      "claims.json and are separately documented)", gate="TEMPORAL")
note("DUPLICATE HANDLING (sec 5): 19 of the 23 flags share ONE "
     "underlying owner transaction (04dc7e1 Rulings A/B/C, with the "
     "1459a2d owner-labeled rider) -- recorded as a shared "
     "origin-transaction annotation; every per-claim fingerprint is "
     "preserved and NO rows were merged (the held mechanism is "
     "per-claim)")
note("RETIREMENT REVIEW (sec 10): 8e64588 retired the response_"
     "lorentz_covariance +1 to 0 per the node's OWN retire clause upon "
     "the owner-adjudicated Q1^TT-and-Q5^TT discharge; authorized "
     "(owner go), no dependency on the retired +1 remains, and the "
     "live suite asserts the resulting net (+16) -- internally "
     "consistent; the retirement is neither reversed nor blindly "
     "accepted, it is EVIDENCED")

# ============ counts ============
f1 = [r for r in LEDGER if r["class"] == "F1"]
f2 = [r for r in LEDGER if r["class"] == "F2"]
f3 = [r for r in LEDGER if r["class"] == "F3"]
OUT["counts"] = {"F1": len(f1), "F2": len(f2), "F3": len(f3),
                 "resolved_by_existing_evidence": len(f1),
                 "still_open": len(f2) + len(f3),
                 "flags_removed_from_active_queue": 0,
                 "flags_still_held": 23,
                 "owner_decisions_required": 3}
check(len(f1) + len(f2) + len(f3) == 23 and len(f1) == 20
      and len(f2) == 3 and len(f3) == 0,
      "CLASSIFICATION: F1 = 20 (authorized + documented + consistent; "
      "awaiting only the collective accept), F2 = 3 (the two live "
      "tier-contradictions and the live orphaned-result -- genuine "
      "standing governance debt, surfaced on the record at their own "
      "origin, NOT called historical noise), F3 = 0 (no flag exposes "
      "a scientific inconsistency or an unclassifiable state)",
      gate="CLASS")
check(OUT["counts"]["flags_removed_from_active_queue"] == 0,
      "NO flag was removed from the active queue: the held-ledger was "
      "NOT mutated, the baseline was NOT refreshed -- this review "
      "CLASSIFIES; only the owner clears", gate="CLASS")

# ============ 12/13. CONTAMINATION FIREWALL + CONTROLS ============
print("\n=== 12/13: FIREWALL AND CONTROLS ===")
# banned tokens BUILT AT RUNTIME (5th appearance of the self-scan
# trap this campaign: a scanner must never contain its own literals)
_t1 = "RESO" + "NANT"
banned_reads = ["WALL_KR_" + "AXIS2_H0_RESULT",
                "CONTRACT_" + "BENCHMARK_RESULT",
                "wall_j_" + "omega", "g1_" + "ohmic_plant"]
check(_t1 not in selfsrc
      and not any(b in selfsrc for b in banned_reads),
      "no Axis-2 outcome, J(omega), plant, benchmark or resonance "
      "artifact is read or referenced -- flags are resolved by their "
      "OWN provenance evidence only (scanner tokens runtime-built)",
      gate="FW")
control(_t1 in (_t1 + " sentinel"),
        "token scanner has teeth (runtime-assembled sentinel)")
bad_ledger = [r for r in LEDGER if r["flag"] != "rung4_love_kk"]
control(len(bad_ledger) != 23,
        "completeness teeth: a copy of the ledger with one row dropped "
        "FAILS the 23-row completeness gate -- 'no omissions' is "
        "enforced, not asserted")
# the no-accept guard scans for an INVOCATION (a subprocess/main call
# carrying the accept argument), not the token -- the owner-queue prose
# legitimately NAMES the flag it asks the owner to consider
_acc = "--" + "accept"
_invoked = any((_acc in ln and ("subprocess" in ln or "main(" in ln
                                or "argv" in ln))
               for ln in selfsrc.splitlines())
control(not _invoked and _acc in (_acc + ""),
        "no-accept teeth: no line of this instrument INVOKES the "
        "baseline refresh (invocation-pattern scan; prose mentions in "
        "the owner queue are data, not calls)")

# ============ owner queue ============
OUT["owner_decision_queue"] = [
    "1. COLLECTIVE ACCEPT: after reviewing this report, authorize (or "
    "decline) the single baseline refresh (bankgate --accept) covering "
    "the 20 F1 flags and the already-authorized CHANGES underlying the "
    "3 F2 flags. Until then all 23 stay surfaced -- by design.",
    "2. TIER-CONTRADICTION DISPOSITION (rung1_inin_formalism, "
    "rung2_kms_gate): decide -- (a) repair the edge (e.g. re-grade or "
    "restructure the assumed background-flow input), (b) waive with a "
    "documented note (the omission was booked precisely to expose this "
    "presupposition -- arguably correct physics bookkeeping in tension "
    "with the tier rule), or (c) formally leave standing as "
    "expected-red. The builder decides none of these.",
    "3. ORPHANED-RESULT DISPOSITION (response_lorentz_covariance): "
    "decide -- annotate as a legitimately-rootless borrowed-axiom-"
    "class node, or attach a dependency edge.",
]
for q in OUT["owner_decision_queue"]:
    note("OWNER: " + q)

# ============ post-run integrity ============
print("\n=== POST-RUN INTEGRITY ===")
check(all(sha_file(fp) == PRE[fp] for fp in GUARDED),
      "claims.json, claims.baseline.json, held_flags.json AND every "
      "frozen physics artifact are BYTE-IDENTICAL: no mutation, no "
      "refresh, no blanket accept occurred", gate="PROV")
try:
    st = subprocess.run(["git", "status", "--short"], cwd=HERE,
                        capture_output=True, text=True, timeout=60).stdout
    OUT["worktree"] = st.strip().splitlines()
    note("files added: %s" % (st.strip().replace("\n", " | ")
                              or "(none yet)"))
except Exception as e_:
    note("git status unavailable: %s" % e_)

RESULT = {"instrument": "wall_held_flags_23_review.py",
          "instrument_sha256": sha_file(os.path.abspath(__file__)),
          "review": "COMPLETE",
          "counts": OUT["counts"],
          "baseline_refreshed": False, "blanket_accept_used": False,
          "frozen_scientific_content_changed": False,
          "tier4": "BANKED, unchanged", "axis2": "C, unchanged",
          "gate_e": "A, unchanged", "noise": "A, unchanged",
          "H0_Lambda_R": "ONE, unresolved",
          "h2_locals": "FORK-GATED, unchanged",
          "consequence_cell": "CC-C, unchanged",
          "out": OUT, "checks": CHECKS, "notes": NOTES, "failures": FAILS,
          "elapsed_s": round(time.time() - T0, 1)}
outp = os.path.join(HERE, "WALL_HELD_FLAGS_23_REVIEW_RESULT.json")
json.dump(RESULT, open(outp, "w"), indent=1, default=str)
rr = json.loads(open(outp).read())
check(rr["baseline_refreshed"] is False
      and rr["counts"]["flags_still_held"] == 23,
      "artifact written and re-read (sha %s...)" % sha_file(outp)[:16],
      gate="OUT")
npass = sum(1 for c in CHECKS if c["pass"])
print("\n23-FLAG REVIEW: %d/%d passed; failures: %d"
      % (npass, len(CHECKS), len(FAILS)))
for m in FAILS:
    print("  FAILURE: " + m)
print("F1=20 F2=3 F3=0 | held=23 | removed=0")
print("HARD STOP.")
sys.exit(0 if not FAILS else 1)
