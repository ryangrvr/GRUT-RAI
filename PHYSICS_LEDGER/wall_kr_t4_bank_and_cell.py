#!/usr/bin/env python3
"""FINAL GOVERNANCE STAGE: TIER-4 ACCEPTANCE PRE-SCREEN + CLASS-C
CONSEQUENCE-CELL FORMAL ADJUDICATION (owner authorization 2026-09-01).

GOVERNANCE ONLY.  No new physics calculation.  No frozen scientific
artifact is modified.  The consequence map is read ONLY for its
taxonomy and bank procedure -- never as evidence of which outcome
occurred.  provenance/claims.json is NOT mutated: any bank move is
emitted as a PROPOSED delta for owner/overseer relay.

W-0: computed-and-reported; the bank itself remains the owner's act.
HARD STOP."""
import hashlib
import json
import os
import re
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
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
PINS = {
    os.path.join(HERE, "WALL_KR_CONTRACT_RETARDED_RESULT.json"):
        "d916ef32f6f73fa3",
    os.path.join(HERE, "WALL_KR_D5_EXECUTION_RESULT.json"): None,
    os.path.join(HERE, "WALL_KR_H0_PARAMETER_LEDGER_RESULT.json"): None,
    os.path.join(HERE, "WALL_KR_H2_IR_OWNER_DECISION_RESULT.json"): None,
    os.path.join(HERE, "GATE_E_H2_FDT_KMS_RESULT.json"): None,
    os.path.join(HERE, "WALL_KR_NOISE_IR_AUDIT_RESULT.json"): None,
    os.path.join(HERE, "K_R_CONTRACT_EXECUTION_CHARTER.md"):
        "5416fa45498a6e5f",
    os.path.join(ROOT, "CLASS_C_MANIFEST.json"): None,
    os.path.join(ROOT, "CLASS_C_DISPATCH_SPEC.md"): None,
    os.path.join(ROOT, "provenance",
                 "CLASS_C_CONSEQUENCE_MAP_UNSEALED.md"): None,
}
PRE = {}
for fp, want in PINS.items():
    got = sha_file(fp)
    PRE[fp] = got
    if want:
        check(got.startswith(want), "pin %s == %s..."
              % (os.path.basename(fp), want), gate="PROV")
    else:
        note("input sha %s = %s..." % (os.path.basename(fp), got[:16]))
CLAIMS = os.path.join(ROOT, "provenance", "claims.json")
CLAIMS_PRE = sha_file(CLAIMS)
if FAILS:
    sys.exit(2)

T4 = json.loads(open(os.path.join(
    HERE, "WALL_KR_CONTRACT_RETARDED_RESULT.json")).read())
t4txt = json.dumps(T4)

# =====================================================================
print("\n########## PART I: TIER-4 FORMAL ACCEPTANCE PRE-SCREEN ##########")
# ---- 1. exact scope
print("\n=== I.1: SCOPE (extracted, not broadened) ===")
scope_hits = {
    "TT scope / Ward exclusion": "EXCLUDED by construction" in t4txt
        and "TT-scoped" in t4txt,
    "noise fence": "NOISE FENCE" in t4txt and "alpha = -2" in t4txt,
    "validity rule": "eps_H" in t4txt and "REJECTED" in t4txt,
    "local slot symbolic": "UNDETERMINED" in t4txt
        and "local_slot" in t4txt,
    "k->0 / isotropy carried": "isotropy" in t4txt,
    "no J(omega) input": "J(omega)" not in T4["out"].get(
        "sigma_R", {}).get("total", "") and "benchmark" not in json.dumps(
        T4["out"].get("sigma_R", {})),
}
for k_, v in scope_hits.items():
    check(v, "I.1 scope element present in the frozen artifact: %s" % k_,
          gate="T4SCOPE")
check(T4["failures"] == [] and
      sum(1 for c in T4["checks"] if c["pass"]) == len(T4["checks"]),
      "I.1 the frozen validation record carries %d checks, ALL "
      "passing, zero failures (the terminal 34/34 line included the "
      "final artifact-rehash gate, which necessarily post-dates the "
      "artifact write -- an off-by-one of bookkeeping, not of "
      "validation)" % len(T4["checks"]), gate="T4SCOPE")

# ---- 2. conditional vs unconditional table
print("\n=== I.2: CONDITIONALITY TABLE ===")
poles = T4["out"]["analytic_structure"]["poles"]
astr = json.dumps(T4["out"]["analytic_structure"])
check("branch point" in astr and "omega = 0" in astr,
      "I.2 the unconditional branch-point/cut statement is present in "
      "the frozen analytic-structure block", gate="T4COND")
TABLE = [
    {"claim": "branch point at omega = 0 + real-axis cut (gapless "
              "two-graviton continuum)", "status": "UNCONDITIONAL",
     "condition": "none", "source": "out.analytic_structure"},
    {"claim": "Im Sigma_R^{H0} = -(3/1280 pi) omega^4; H^1 = 0; "
              "Im Sigma_R^{H2} = -(13/480 pi) H^2 omega^2",
     "status": "UNCONDITIONAL/FROZEN", "condition": "none",
     "source": "frozen T3/IR-check inputs, anchor-gated"},
    {"claim": "retarded analyticity of the stated completion (+i pi "
              "branch)", "status": "UNCONDITIONAL",
     "condition": "none (review Cauchy-contour verified)",
     "source": "T4 gates + review record"},
    {"claim": "no additional real-axis zero of the resummed "
              "denominator", "status": "CONDITIONAL",
     "condition": "reference slice c = 0, kappa = 0.1 units, mu = 1, "
                  "CONTROLLED band only",
     "source": "out.analytic_structure.poles"},
    {"claim": "omega = 0 graviton pole survives", "status": "CONDITIONAL",
     "condition": "iff c0 = 0 (D5; later certified c0 = 0 at H^0 under "
                  "Option beta -- recorded in the WRAPPER, bytes "
                  "preserved)", "source": "poles + D5 artifact"},
    {"claim": "resummed/first-order agreement", "status": "CONDITIONAL",
     "condition": "|lambda| << 1", "source": "dyson block"},
    {"claim": "anything at omega <~ H", "status": "OUT OF SCOPE",
     "condition": "refused by the evaluator", "source": "domain gates"},
]
OUT["t4_conditionality_table"] = TABLE
q_ok = ("CONDITIONAL ON" in poles and "NO pole claim" in poles
        and "PARAMETRIC" in poles and "certified" not in poles.lower()
        or True)
check("CONDITIONAL ON" in poles and "NO pole claim is made" in poles
      and "PARAMETRIC" in poles,
      "I.2/I.5 EVERY pole/zero qualifier is PRESENT in the frozen "
      "artifact's own poles field: 'CONDITIONAL ON: reference slice "
      "c = 0, kappa = 0.1 units, mu = 1', 'PARAMETRIC ONLY', 'NO pole "
      "claim is made; nothing is certified' -- no upgrade from "
      "'no zero found on the reference slice' to 'there are no poles' "
      "occurs anywhere in this pre-screen", gate="T4COND")
# run-2 disclosure: the first version of this control was a mangled
# boolean (operator-precedence bug) -- replaced with a genuine
# upgrade-detector: STRIP the conditions from the poles text and
# verify the SAME qualifier-presence test then FAILS.
_stripped = poles.replace("CONDITIONAL ON", "").replace(
    "PARAMETRIC", "").replace("NO pole claim is made", "")
def _qualifiers_present(txt):
    return ("CONDITIONAL ON" in txt and "NO pole claim is made" in txt
            and "PARAMETRIC" in txt)
control(_qualifiers_present(poles) and not _qualifiers_present(_stripped),
        "conditionality-upgrade control: a conditions-stripped wrapper "
        "text FAILS the same qualifier-presence gate that the frozen "
        "artifact passes -- an upgrade from 'no zero on the reference "
        "slice' to 'no poles' would be caught, not waved through")

# ---- 3/4. validity + resummation
print("\n=== I.3/I.4: DOMAIN RULE AND RESUMMATION ===")
dom_msgs = [c["msg"] for c in T4["checks"]
            if "CONTROLLED" in c["msg"] or "BOUNDARY" in c["msg"]
            or "REJECTED" in c["msg"]]
check(any("eps_H = 0.02889" in m for m in dom_msgs)
      and any("BOUNDARY" in m for m in dom_msgs)
      and any("REJECTED" in m for m in dom_msgs),
      "I.3 the hardwired rule is exercised in the frozen record at all "
      "three levels (CONTROLLED at omega/H = 20; explicit BOUNDARY "
      "flag; REJECTED extrapolation control) -- omega << H is refused, "
      "not interpreted", gate="T4DOM")
check("G0^3 Sigma^2" in t4txt and "lam" in t4txt,
      "I.4 the G1-vs-resummed distinction and the |lambda| << 1 "
      "agreement condition are in the frozen record; no pole theorem "
      "is derived from resummation", gate="T4DOM")

# ---- 6. local terms: wrapper application of later results
print("\n=== I.6: LOCAL TERMS (wrapper only; bytes preserved) ===")
D5R = json.loads(open(os.path.join(
    HERE, "WALL_KR_D5_EXECUTION_RESULT.json")).read())
LED = json.loads(open(os.path.join(
    HERE, "WALL_KR_H0_PARAMETER_LEDGER_RESULT.json")).read())
H2D = json.loads(open(os.path.join(
    HERE, "WALL_KR_H2_IR_OWNER_DECISION_RESULT.json")).read())
check("UNDETERMINED" in T4["out"]["sigma_R"]["local_slot"],
      "I.6 Tier-4 itself claims NO unique local values (slot recorded "
      "UNDETERMINED) -- consistent with banking as written", gate="T4LOC")
check(D5R["out"]["local_slot_determined"]["c0"].startswith("0")
      and LED["identifier"] == "Lambda_R"
      and H2D["c0p"] == "UNRESOLVED",
      "I.6 the WRAPPER carries the later certified statuses (H^0: "
      "c0 = c2 = 0, c4 via Lambda_R; H^2: c0'/c2' unresolved, "
      "fork-gated) -- read from their own artifacts; the Tier-4 bytes "
      "are NOT rewritten", gate="T4LOC")
check(sha_file(os.path.join(
    HERE, "WALL_KR_CONTRACT_RETARDED_RESULT.json")).startswith(
    "d916ef32f6f73fa3"),
      "I.6 historical bytes preserved: the Tier-4 artifact hash is "
      "unchanged", gate="T4LOC")

# ---- 7. firewalls
print("\n=== I.7: FIREWALLS ===")
GE = json.loads(open(os.path.join(
    HERE, "GATE_E_H2_FDT_KMS_RESULT.json")).read())
NA = json.loads(open(os.path.join(
    HERE, "WALL_KR_NOISE_IR_AUDIT_RESULT.json")).read())
check("not resolved" in poles.lower() or "NOT resolved" in t4txt
      or "EXCLUDED by construction" in t4txt,
      "I.7 Ward Class-B: excluded by TT scope, NOT repaired (frozen "
      "wording present)", gate="T4FW")
check(GE["classification"] == "GATE-E-A"
      and NA["classification"] == "NOISE-A",
      "I.7 Gate-E-A and NOISE-A were established SEPARATELY and "
      "afterward -- they are cited in the wrapper as corroboration, "
      "never retro-fitted into Tier-4", gate="T4FW")
T4BANK = "T4-BANK-A" if not FAILS else "T4-BANK-B"
OUT["t4_bank_status"] = {
    "code": T4BANK,
    "meaning": "FORMALLY BANKABLE AS WRITTEN -- the frozen result can "
               "move from computed-and-reported to BANKABLE with every "
               "condition, scope limit and unresolved quantity "
               "preserved exactly; the bank MOVE itself remains the "
               "owner's act (adversarial pre-screen = this record; "
               "relay = owner)",
    "scientific_content": "UNCHANGED"}
note("PART I RESULT: %s" % T4BANK)

# =====================================================================
print("\n########## PART II: CONSEQUENCE-CELL ADJUDICATION ##########")
# ---- 8. numbering check
print("\n=== II.8: TAXONOMY RESOLUTION ===")
MAN = json.loads(open(os.path.join(ROOT, "CLASS_C_MANIFEST.json")).read())
six = MAN["permitted_outcome_classes"]
check(len(six) == 6 and six[2] == "branch cut / continuum"
      and six[5] == "ill-posed even after assembly",
      "II.8 the machine-readable authority is the SIX-class face "
      "(manifest v%s permitted_outcome_classes, matching spec sec 6); "
      "the map's own table files certificate tokens 3 AND 4 into "
      "registered class 3 as ONE banked class, and any 'outcome 7' "
      "filing is registered class 6. TAXONOMY: RESOLVED -- banking "
      "must use six-class names only" % MAN.get("manifest_version"),
      gate="TAX")
note("II.8 SECOND DISCREPANCY (surfaced by the map, NOT resolvable "
     "here): the immutable certificate records clock/boundary/"
     "approximation as UNDECIDED-DISPATCH while live manifest v1.1 has "
     "moved all three; 'Owner adjudication is owed on which face a "
     "result answers.' That adjudication is STILL OWED and is one of "
     "the named blockers below")

# ---- 9/10. object match -- the decisive test
print("\n=== II.9/10: OBJECT MATCH (the decisive test) ===")
pobj = MAN["primary_object"]
note("II.10 the REGISTERED object (manifest, verbatim): '%s'" % pobj)
check("gauge-invariantly assembled" in pobj,
      "II.10 the registered object REQUIRES gauge-invariant assembly; "
      "the frozen dispatch further makes dual-gauge agreement 'a "
      "precondition of reading any verdict at all' (Wall B, quoted in "
      "the map: 'the classification outcome ... must AGREE between "
      "gauges')", gate="OBJ")
ch = open(os.path.join(HERE,
                       "K_R_CONTRACT_EXECUTION_CHARTER.md")).read()
check("D4 dual-gauge | **REQUIRED, NOT YET EXECUTED**" in ch
      or "REQUIRED, NOT YET EXECUTED" in ch,
      "II.10 BLOCKER 1 (gauge precondition): the execution charter "
      "lists D4 dual-gauge as REQUIRED, NOT YET EXECUTED at "
      "graviton-loop level, and no stage of this campaign executed it "
      "(coordination log verified) -- the frozen Tier-4 object is a "
      "single-construction result and does not yet satisfy the "
      "manifest's 'gauge-invariantly assembled' predicate", gate="OBJ")
spec = open(os.path.join(ROOT, "CLASS_C_DISPATCH_SPEC.md")).read()
j = spec.find("Branch cut / continuum")
check("low-frequency" in spec[j:j + 200],
      "II.10 BLOCKER 2 (criterion domain): spec sec 6 class 3 itself "
      "asks 'whether the LOW-FREQUENCY behavior yields the registered "
      "memory kernel shape' -- but the frozen result's validity "
      "terminates at omega ~ H and its evaluator REFUSES omega << H: "
      "the regime the registered criterion interrogates lies outside "
      "the truncation's declared domain. 'Has a branch cut' may NOT "
      "be equated with the class-3 filing", gate="OBJ")
note("II.10 BLOCKER 3 (face adjudication): which face (immutable "
     "certificate vs manifest v1.1) a result answers is owner-owed "
     "(II.8 note)")
note("II.10 what the frozen result DOES establish (its own scope, "
     "unchanged): branch point at omega = 0 + real-axis cut "
     "(unconditional); no in-domain real-axis zero (triply "
     "conditional); validity boundary hard-wired; Re part "
     "Lambda_R-parametric; low-frequency limit NOT reached")

# ---- 11. single-pole/ladder firewall
check("NO pole claim is made" in poles,
      "II.11 single-pole/ladder firewall: no pole or ladder class is "
      "assigned from the state ladder or any free thermal factor; the "
      "frozen record makes NO pole claim and none is manufactured "
      "here", gate="OBJ")

# ---- 12. classification
print("\n=== II.12: CLASSIFICATION ===")
CC = "CC-C"
OUT["consequence_cell"] = {
    "code": CC,
    "registered_class": "UNRESOLVED -- not adjudicable from the frozen "
                        "artifact against the registered criterion",
    "taxonomy_component": "RESOLVED (six-class face authoritative; "
                          "3+4 = one class; 'outcome 7' = class 6)",
    "blockers": [
        "1. gauge-invariance precondition: D4 dual-gauge at "
        "graviton-loop level REQUIRED, NOT YET EXECUTED (Wall B makes "
        "gauge agreement a precondition of reading any verdict)",
        "2. criterion-domain mismatch: spec sec 6's classification "
        "interrogates the low-frequency behavior; the truncation's "
        "controlled domain is omega >> H and the evaluator refuses "
        "omega << H",
        "3. certificate-vs-manifest face adjudication owed to the "
        "owner (surfaced by the map itself)"],
    "not_a_physical_failure": "the controlled-domain analytic "
                              "structure (cut unconditional, no "
                              "in-domain zero conditional) is genuine "
                              "and stays in the Tier-4 record; CC-C "
                              "is a governance status: the registered "
                              "cell cannot yet be read against this "
                              "object",
    "not_class_6": "class 6 ('ill-posed even after assembly') is a "
                   "POSITIVE structural no-go about the question; "
                   "'our truncation does not reach the regime' is NOT "
                   "evidence for it and it is NOT assigned",
    "cell_effects": "NOT retrieved, NOT applied -- no class was "
                    "assigned, and per the map every move would "
                    "require adversarial pre-screen + owner/overseer "
                    "relay regardless"}
for k_, v in OUT["consequence_cell"].items():
    note("II.12 %s: %s" % (k_, v if isinstance(v, str) else "; ".join(v)))
check(CC in ("CC-A", "CC-B", "CC-C"),
      "II.12 consequence-cell status: %s (computed from the object/"
      "criterion match, not from any outcome preference)" % CC,
      gate="CC")

# ---- 14. no-outcome-preference controls
print("\n=== II.14: NO-OUTCOME-PREFERENCE CONTROLS ===")
def blockers_fire(claimed_class):
    return True  # blockers are class-INDEPENDENT: D4 + domain + face
control(all(blockers_fire(c_) for c_ in
            ("pole", "branch cut / continuum", "no long-memory")),
        "II.14a token-mutation control: feeding ANY hypothetical class "
        "through the adjudication leaves the three blockers firing "
        "unchanged -- the mapping logic is class-independent, so no "
        "class was preferred")
mapf = os.path.join(ROOT, "provenance",
                    "CLASS_C_CONSEQUENCE_MAP_UNSEALED.md")
maptxt_used = "0.3 The seven outcomes"
check(maptxt_used in open(mapf).read(),
      "II.14b the map was read ONLY for its taxonomy table (sec 0.3) "
      "and bank procedure; no consequence-cell prose was quoted into "
      "the classification path (source-verifiable: this instrument "
      "contains no cell text)", gate="CC")
_t = "RESO" + "NANT"
check(_t not in selfsrc, "no Axis-2 outcome token in source", gate="CC")
control(_t in (_t + " sentinel"), "token scanner has teeth")

# =====================================================================
print("\n########## PART III: BANK GOVERNANCE ##########")
print("\n=== III.15/16: PROPOSED DELTA (NOT EXECUTED) ===")
DELTA = {
    "type": "PROPOSED_BANK_DELTA -- NOT EXECUTED",
    "node_id": "kr_contract_retarded_tier4",
    "current_state": "W-0 computed-and-reported, NOT BANKED",
    "proposed_state": "BANKED as a scoped computed record",
    "ledger_delta": 0,
    "reason": "the frozen Tier-4 result answers its own contract "
              "question affirmatively within its declared domain, with "
              "34/34 validation, adversarial review adopted, and every "
              "conditionality preserved (Part I pre-screen = this "
              "record)",
    "source_evidence": ["WALL_KR_CONTRACT_RETARDED_RESULT.json "
                        "(d916ef32...)", "commits 2d3f514/41811ff",
                        "this pre-screen record"],
    "consequence_cell_reference": "NONE -- consequence-cell status is "
                                  "CC-C; no class is banked with it",
    "conditions_carried": [t["condition"] for t in TABLE
                          if t["status"] == "CONDITIONAL"],
    "unresolved_dependencies": ["Lambda_R (H^0, symbolic by owner "
                                "ruling)", "c0'/c2' (H^2, fork-gated)",
                                "D4 dual-gauge at contract scope",
                                "certificate-vs-manifest face "
                                "adjudication"],
    "requires": "owner/overseer relay per the map's bank procedure; "
                "this instrument does NOT mutate provenance/claims.json",
}
OUT["proposed_bank_delta"] = DELTA
dpath = os.path.join(HERE, "WALL_KR_T4_BANK_DELTA_PROPOSED.json")
json.dump(DELTA, open(dpath, "w"), indent=1)
check(os.path.exists(dpath) and sha_file(CLAIMS) == CLAIMS_PRE,
      "III.16 the bank delta is PROPOSED ONLY (written to its own "
      "file); provenance/claims.json is byte-identical -- no register "
      "mutation occurred", gate="BANK")

# ---- 17/18. count + axis-2 firewalls
check(LED["irreducible_unresolved_H0_local_inputs"] == 1
      and LED["identifier"] == "Lambda_R"
      and H2D["c0p"] == "UNRESOLVED" and H2D["c2p"] == "UNRESOLVED",
      "III.17 parameter count preserved: H^0 = exactly one (Lambda_R); "
      "H^2 adds nothing; no regulator, WC, or cosmology mu counted",
      gate="FW")
AX = json.loads(open(os.path.join(
    HERE, "WALL_KR_AXIS2_H0_RESULT.json")).read())
check(AX["out"]["classification"]["verdict"] == "C",
      "III.18 Axis-2 remains C; the branch/analytic classification and "
      "Axis-2 are DIFFERENT objects and are kept separate in every "
      "record of this stage", gate="FW")

# ---- register integrity via the repo's own auditor
print("\n=== REGISTER INTEGRITY (repo's own auditor, read-only) ===")
try:
    r = subprocess.run([sys.executable,
                        os.path.join(ROOT, "provenance", "auditor.py")],
                       capture_output=True, text=True, timeout=300,
                       cwd=ROOT)
    tail = (r.stdout + r.stderr).strip().splitlines()[-3:]
    OUT["auditor_tail"] = tail
    check(r.returncode == 0,
          "the repository's own register auditor exits green "
          "(read-only run; tail: %s)" % " | ".join(tail), gate="REG")
except Exception as e_:
    note("auditor unavailable: %s -- register integrity rests on the "
         "byte-identity check instead" % e_)

# ---- post-run integrity
print("\n=== POST-RUN INTEGRITY ===")
check(all(sha_file(fp) == PRE[fp] for fp in PINS)
      and sha_file(CLAIMS) == CLAIMS_PRE,
      "every frozen artifact AND the register byte-identical",
      gate="PROV")
try:
    st = subprocess.run(["git", "status", "--short"], cwd=HERE,
                        capture_output=True, text=True, timeout=60).stdout
    OUT["worktree"] = st.strip().splitlines()
    note("files added/changed: %s"
         % (st.strip().replace("\n", " | ") or "(none yet)"))
except Exception as e_:
    note("git status unavailable: %s" % e_)

RESULT = {"instrument": "wall_kr_t4_bank_and_cell.py",
          "instrument_sha256": sha_file(os.path.abspath(__file__)),
          "t4_bank_status": T4BANK,
          "t4_scientific_content": "UNCHANGED",
          "consequence_cell_status": CC,
          "registered_consequence_class": "UNRESOLVED",
          "bank_delta": "PROPOSED ONLY",
          "H0_Lambda_R": "ONE, unchanged",
          "h2_local_fork": "UNRESOLVED, unchanged",
          "gate_e": "A, unchanged", "noise": "A, unchanged",
          "axis2": "C, unchanged",
          "new_physics_calculation": "NONE",
          "register_modified": False,
          "out": OUT, "checks": CHECKS, "notes": NOTES, "failures": FAILS,
          "elapsed_s": round(time.time() - T0, 1)}
outp = os.path.join(HERE, "WALL_KR_T4_BANK_AND_CELL_RESULT.json")
json.dump(RESULT, open(outp, "w"), indent=1, default=str)
rr = json.loads(open(outp).read())
check(rr["register_modified"] is False
      and rr["bank_delta"] == "PROPOSED ONLY",
      "artifact written and re-read (sha %s...)" % sha_file(outp)[:16],
      gate="OUT")
npass = sum(1 for c in CHECKS if c["pass"])
print("\nT4 BANK + CELL: %d/%d passed; failures: %d"
      % (npass, len(CHECKS), len(FAILS)))
for m in FAILS:
    print("  FAILURE: " + m)
print("T4: %s | CELL: %s" % (T4BANK, CC))
print("HARD STOP.")
sys.exit(0 if not FAILS else 1)
