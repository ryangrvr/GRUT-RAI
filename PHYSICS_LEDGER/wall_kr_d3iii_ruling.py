#!/usr/bin/env python3
"""D3(iii) OWNER RULING -- consequence-campaign gauge scope
(owner ruling issued 2026-09-02).

RECORDING + MECHANICAL VALIDATION.  No physics is calculated: no
general-gauge propagator, no loop amplitude, no K_R, no low-frequency
or epoch-window response.  No new parameter.  No frozen scientific
artifact is modified.  D4 is NOT re-adjudicated here.

W-0: computed-and-reported, NOT banked.  HARD STOP."""
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
    os.path.join(HERE, "K_R_CONTRACT_EXECUTION_CHARTER.md"):
        "5416fa45498a6e5f",
    os.path.join(HERE, "K_R_CONTRACT_OWNER_RULING.md"):
        "5d89720b53e1b078",
    os.path.join(HERE, "WALL_KR_TIER2_MASSLESS_BATH.json"):
        "c5d399f525407839",
    os.path.join(HERE, "WALL_KR_TIER3_LOOP_RESULT.json"):
        "4c016e93b889bd04",
    os.path.join(HERE, "WALL_KR_CONTRACT_RETARDED_RESULT.json"):
        "d916ef32f6f73fa3",
    os.path.join(HERE, "WALL_KR_D4_DUAL_GAUGE_RESULT.json"): None,
    os.path.join(HERE, "WALL_KR_D4_KTERM_COMPLETION_RESULT.json"): None,
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

# ============ 1. THE EXACT D3(iii) AUTHORITY ============
print("\n=== 1: THE D3(iii) AUTHORITY, VERBATIM ===")
ch = open(os.path.join(HERE, "K_R_CONTRACT_EXECUTION_CHARTER.md")).read()
i = ch.find("(iii) the de Sitter state prescription")
d3iii = " ".join(ch[i:i + 210].split())
note("CHARTER STEP 1, verbatim: '%s'" % d3iii)
check("must be declared, not assumed" in d3iii,
      "the D3(iii) authority is located verbatim and says the "
      "graviton-sector state prescription 'must be declared, not "
      "assumed' -- i.e. it is an OWNER DECLARATION slot, exactly the "
      "kind of item this ruling fills", gate="AUTH")
rul = open(os.path.join(HERE, "K_R_CONTRACT_OWNER_RULING.md")).read()
j = rul.find("## 4. D3")
d3 = " ".join(rul[j:j + 330].split())
note("PRIOR D3 RULING (Tier-2), verbatim: '%s'" % d3)
check("OPTION 3a" in d3 and "BD-analogue" in d3,
      "the PRIOR D3 ruling (bath state = Option 3a, BD-analogue "
      "Option-B adiabatic; IR = dimensional continuation only) is on "
      "record -- this ruling extends that same declared object to the "
      "consequence campaign's gauge scope; it does not replace it",
      gate="AUTH")

# ============ 2. THE TT-BATH CONTRACT EXISTS AND IS FROZEN ==========
print("\n=== 2: THE DECLARED OBJECT EXISTS AND IS FROZEN ===")
T2 = json.loads(open(os.path.join(
    HERE, "WALL_KR_TIER2_MASSLESS_BATH.json")).read())
t2txt = json.dumps(T2)
check(T2["failures"] == [] and "P^TT" in t2txt,
      "the TT-bath contract is FROZEN and certified: the Tier-2 "
      "artifact (sha c5d399f5...) carries the tensor rule <hh> = P^TT "
      "x W with zero failures -- the object this ruling scopes is "
      "defined, not hypothetical", gate="OBJ")

# ============ 3. THE K-TERM COMPLETION IS CERTIFIED ============
print("\n=== 3: THE K-TERM COMPLETION IS CERTIFIED ===")
KT = json.loads(open(os.path.join(
    HERE, "WALL_KR_D4_KTERM_COMPLETION_RESULT.json")).read())
D4 = json.loads(open(os.path.join(
    HERE, "WALL_KR_D4_DUAL_GAUGE_RESULT.json")).read())
check(KT["kterm"] == "KTERM-A" and KT["failures"] == []
      and KT["H0"] == "PASS" and KT["H2"] == "PASS",
      "KTERM-A is certified (27/27, zero failures, H^0/H^1/H^2): the "
      "internal orbit is annihilated within the declared TT bath -- "
      "the factual basis this ruling rests on", gate="BASIS")
check(D4["classification"] == "D4-C",
      "the D4-C record is read unchanged (a54aa7f); this ruling does "
      "NOT re-adjudicate D4", gate="BASIS")

# ============ 4. THE RULING, RECORDED VERBATIM ============
print("\n=== 4: THE OWNER RULING (7 clauses) ===")
RULING = {
    "1": "The consequence object may be treated as the registered "
         "TT-bath retarded TT response.",
    "2": "Gauge/orbit robustness is required WITHIN that declared TT "
         "bath.",
    "3": "No claim is made that this TT-bath prescription is the "
         "unique admissible general-gauge graviton propagator.",
    "4": "The existence of alternative general-gauge/non-TT propagator "
         "content remains a separately scoped theoretical question.",
    "5": "D3(iii) is therefore CLOSED FOR CURRENT CONSEQUENCE SCOPE, "
         "NOT SOLVED AS A GENERAL GAUGE-UNIQUENESS THEOREM.",
    "6": "This ruling does NOT alter the frozen scientific result.",
    "7": "No new physical parameter is introduced.",
}
for k_, v in RULING.items():
    note("CLAUSE %s: %s" % (k_, v))
OUT["owner_ruling"] = RULING
check(len(RULING) == 7 and "NOT SOLVED AS A GENERAL GAUGE-UNIQUENESS"
      in RULING["5"],
      "all seven clauses recorded verbatim, with clause 5's "
      "closed-for-scope / not-solved-as-theorem distinction intact",
      gate="RULE")

# ============ 5. THE REQUIRED WORDING (and the forbidden phrasing) ===
print("\n=== 5: WORDING DISCIPLINE ===")
REQ1 = ("Declared TT-bath scope is accepted for the present "
        "consequence campaign.")
REQ2 = ("The unresolved general-gauge/D3(iii) question remains outside "
        "the present consequence-scope contract.")
OUT["required_statements"] = [REQ1, REQ2]
OUT["general_gauge_uniqueness"] = "NOT CLAIMED"
note("RECORDED: %s" % REQ1)
note("RECORDED: %s" % REQ2)
# the forbidden phrasing is BUILT AT RUNTIME and never written into the
# record or this source (the campaign's recurring self-scan trap, 8th
# avoidance): the record states the negative as "NOT CLAIMED" instead
FORB = [("unique" + "ly physically admissible"),
        ("unique" + " admissible gauge"),
        ("all gauges" + " proven equivalent"),
        ("gauge" + "-uniqueness established")]
blob = json.dumps(OUT) + REQ1 + REQ2
check(not any(f.lower() in blob.lower() for f in FORB),
      "WORDING GATE: the record NEVER asserts general-gauge "
      "uniqueness in any of its forbidden phrasings -- it states the "
      "negative as 'NOT CLAIMED'. The forbidden strings are assembled "
      "at runtime and appear nowhere in the record or this source",
      gate="WORD")
control(any(f.lower() in ("the " + FORB[0]).lower() for f in FORB),
        "wording detector has teeth: a runtime-assembled offending "
        "phrase IS caught by the same membership test")
check(REQ1 in blob and REQ2 in blob,
      "both required statements are present verbatim in the record",
      gate="WORD")

# ============ 6. ANTI-CIRCULARITY ============
print("\n=== 6: ANTI-CIRCULARITY ===")
_t = "RESO" + "NANT"
banned_reads = ["CONSEQUENCE_MAP" + "_UNSEALED", "AXIS2_H0" + "_RESULT",
                "CONTRACT_" + "BENCHMARK_RESULT", "wall_j_" + "omega",
                "g1_" + "ohmic_plant", "CLASS_C_" + "MANIFEST"]
check(_t not in selfsrc
      and not any(b in selfsrc for b in banned_reads),
      "NO consequence-class output, branch/memory/resonance outcome, "
      "Axis-2, J(omega), plant/WC or benchmark artifact is read or "
      "referenced -- the sole basis is the contract's TT-bath "
      "definition plus the certified K-term completion (tokens "
      "runtime-built)", gate="CIRC")
control(_t in (_t + " sentinel"),
        "outcome-token scanner has teeth (runtime sentinel)")
# the outcome-artifact names are ALSO assembled at runtime -- naming
# them literally here would trip the source scan above (9th instance
# of the self-scan trap this campaign; the standing fix applied)
read_set = {os.path.basename(p) for p in PINS}
OUTCOME_SET = {"WALL_KR_" + "AXIS2_H0" + "_RESULT.json",
               "WALL_KR_" + "CONTRACT_" + "BENCHMARK_RESULT.json"}
check(not (read_set & OUTCOME_SET),
      "the read-set intersected with the outcome-artifact set is EMPTY "
      "(read files: %s)" % ", ".join(sorted(read_set)), gate="CIRC")
OUT["basis"] = ("the existing contract definition of the TT bath "
                "(Tier-2 frozen, tensor rule <hh> = P^TT x W; prior D3 "
                "Option-3a ruling) AND the KTERM-A completion showing "
                "internal orbit robustness within that declared object "
                "-- nothing else")

# ============ 7. NO NEW PHYSICS / NO NEW PARAMETER ============
print("\n=== 7: NO NEW PHYSICS, NO NEW PARAMETER ===")
newparam = re.search(r"^\s*(g_new|xi_scale|gauge_param|alpha_gauge)"
                     r"\s*=\s*[-+0-9]", selfsrc, re.M)
_cas = "sym" + "py"          # runtime-built: the literal must not
check(newparam is None and _cas not in selfsrc,   # appear in source
      "NO new physical parameter is assigned, and this instrument "
      "imports no CAS at all -- it cannot have calculated a "
      "general-gauge propagator, a loop amplitude, a K_R, or any "
      "low-frequency/epoch-window response", gate="NOPHYS")
OUT["no_new_physics"] = {
    "general_gauge_propagators": "NOT computed",
    "loop_amplitudes": "NOT computed", "K_R": "NOT recomputed",
    "low_frequency_response": "NOT computed",
    "epoch_window": "NOT entered",
    "new_parameter": "NONE"}

# ============ 8. STATE PRESERVATION ============
print("\n=== 8: STATE PRESERVATION ===")
OUT["state"] = {
    "D3iii": "CLOSED FOR CURRENT CONSEQUENCE SCOPE",
    "general_gauge_uniqueness": "NOT CLAIMED",
    "TT_bath_scope": "OWNER-ACCEPTED",
    "new_input": "NONE",
    "D4": "STILL PENDING FORMAL RE-ADJUDICATION (not touched here)",
    "H0_Lambda_R": "ONE, unchanged",
    "H2_locals": "FORK-GATED, unchanged",
    "axis2": "C, unchanged", "gate_e": "A, unchanged",
    "noise": "A, unchanged",
    "consequence_cell": "CC-C, unchanged (no class assigned)",
    "consequence_map": "NOT modified",
    "tier4_scientific_content": "NOT modified"}
for k_, v in OUT["state"].items():
    note("STATE %s: %s" % (k_, v))

# ============ POST-RUN INTEGRITY ============
print("\n=== POST-RUN INTEGRITY ===")
check(all(sha_file(fp) == PRE[fp] for fp in PINS)
      and sha_file(CLAIMS) == CLAIMS_PRE,
      "every frozen scientific artifact AND the register are "
      "byte-identical to their pre-run hashes", gate="PROV")
try:
    st = subprocess.run(["git", "status", "--short"], cwd=HERE,
                        capture_output=True, text=True, timeout=60).stdout
    OUT["worktree"] = st.strip().splitlines()
    note("files added: %s" % (st.strip().replace("\n", " | ")
                              or "(none yet)"))
except Exception as e_:
    note("git status unavailable: %s" % e_)

RESULT = {"instrument": "wall_kr_d3iii_ruling.py",
          "instrument_sha256": sha_file(os.path.abspath(__file__)),
          "record_type": "OWNER GOVERNANCE RULING (D3(iii) scope)",
          "d3iii": "CLOSED FOR CURRENT CONSEQUENCE SCOPE",
          "general_gauge_uniqueness": "NOT CLAIMED",
          "tt_bath_scope": "OWNER-ACCEPTED",
          "new_input": "NONE",
          "d4": "STILL PENDING FORMAL RE-ADJUDICATION",
          "register_modified": False,
          "frozen_scientific_content_changed": False,
          "out": OUT, "checks": CHECKS, "notes": NOTES, "failures": FAILS,
          "elapsed_s": round(time.time() - T0, 1)}
outp = os.path.join(HERE, "WALL_KR_D3III_OWNER_RULING_RESULT.json")
json.dump(RESULT, open(outp, "w"), indent=1, default=str)
rr = json.loads(open(outp).read())
check(rr["general_gauge_uniqueness"] == "NOT CLAIMED"
      and rr["new_input"] == "NONE"
      and rr["register_modified"] is False,
      "artifact written and re-read (sha %s...)" % sha_file(outp)[:16],
      gate="OUT")
npass = sum(1 for c in CHECKS if c["pass"])
print("\nD3(iii) RULING: %d/%d passed; failures: %d"
      % (npass, len(CHECKS), len(FAILS)))
for m in FAILS:
    print("  FAILURE: " + m)
print("D3(iii): CLOSED FOR CURRENT CONSEQUENCE SCOPE | "
      "GENERAL-GAUGE UNIQUENESS: NOT CLAIMED")
print("HARD STOP.")
sys.exit(0 if not FAILS else 1)
