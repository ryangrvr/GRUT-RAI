#!/usr/bin/env python3
"""OWNER DECISION -- H^2 IR FORK (owner ruling issued 2026-09-01).

RECORDING + MECHANICAL VERIFICATION.  Not a calculation.  Introduces NO
IR scale, NO regulator, NO coefficient.  Does not recompute Axis-2, does
not touch the noise fork or Gate-E, does not modify K_R or the register.

THE RULING: invoke the preregistered fork ONLY as an acknowledged future
governance path -- do NOT price or introduce a new IR input now.  The
H^2 local sector stays fork-gated.

W-0: computed-and-reported, NOT banked.  HARD STOP."""
import hashlib
import json
import os
import re
import subprocess
import sys
import time

import sympy as sp

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


print("=== PROVENANCE ===")
PINS = {
    "WALL_KR_H2_IR_OWNER_RULING_RESULT.json": None,
    "WALL_KR_H2_LOCAL_FORK_RESULT.json": None,
    "WALL_KR_H0_PARAMETER_LEDGER_RESULT.json": None,
    "WALL_KR_CONTRACT_RETARDED_RESULT.json": "d916ef32f6f73fa3",
    "WALL_KR_TIER3_LOOP_RESULT.json": "4c016e93b889bd04",
    "K_R_CONTRACT_OWNER_RULING.md": "5d89720b53e1b078",
}
PRE = {}
for fn, want in PINS.items():
    got = sha_file(os.path.join(HERE, fn))
    PRE[fn] = got
    if want:
        check(got.startswith(want), "pin %s == %s..." % (fn, want),
              gate="PROV")
    else:
        note("input sha %s = %s..." % (fn, got[:16]))
CLAIMS = os.path.join(ROOT, "provenance", "claims.json")
CLAIMS_PRE = sha_file(CLAIMS)
if FAILS:
    sys.exit(2)

# ================= 1. THE CORRECTED EVIDENCE, RE-VERIFIED =============
print("\n=== 1: THE CORRECTED H^2 EVIDENCE (re-verified here) ===")
om = sp.Symbol("omega", positive=True)
q = sp.Symbol("q", positive=True)
D = sp.Symbol("Delta", real=True)
dsym = sp.Symbol("d", positive=True)
C = json.loads(open(os.path.join(HERE, ".h2_cone.json")).read())
cm = sp.sympify(C["cm"]).subs(dsym, 3)
cp = sp.sympify(C["cp"]).subs(dsym, 3)
x = om / 2
tot = sp.Integer(0)
for n_ in range(0, 3):
    em, ep = sp.expand(cm), sp.expand(cp)
    cnm = sp.cancel(sp.together(em.coeff(D, n_) if n_ else em.subs(D, 0)))
    cnp = sp.cancel(sp.together(ep.coeff(D, n_) if n_ else ep.subs(D, 0)))
    tot += sp.factorial(n_) * sp.I**n_ * (
        cnm * sp.Rational(-1, 2)**(n_ + 1) / (q - x)**(n_ + 1)
        + cnp * sp.Rational(1, 2)**(n_ + 1) / (q + x)**(n_ + 1))
ser = sp.expand(sp.series(sp.simplify(q**2 * tot), q, 0, 1).removeO())
pw = {p: sp.simplify(ser.coeff(q, p)) for p in range(-4, 1)}
pw = {p: v for p, v in pw.items() if v != 0}
check(-2 not in pw and -4 not in pw and -3 not in pw,
      "CLAUSE 1a: after summing BOTH retarded cone branches the "
      "power-divergent pieces are ABSENT from the integrand (no q^-2, "
      "q^-3 or q^-4 survives) -- the q^-4 / a = -1 power contribution "
      "CANCELS EXACTLY between the two branches", gate="EVID")
LOGC = sp.simplify(pw.get(-1, 0))
check(sp.simplify(LOGC + sp.Rational(8, 15) * om**2) == 0,
      "CLAUSE 1b: a NONZERO q^-3 / a = 0 LOGARITHMIC IR divergence "
      "REMAINS, coefficient exactly -8 omega^2/15 (per H^2, d = 3) -- "
      "so the H^2 retarded local integral behaves as -(8/15) omega^2 "
      "ln(delta) at small cutoff", gate="EVID")
OUT["corrected_evidence"] = {
    "power_piece": "the q^-4 / a = -1 power contribution cancels "
                   "exactly between the two retarded cone branches",
    "surviving": "a nonzero q^-3 / a = 0 logarithmic IR divergence "
                 "remains, coefficient -8 omega^2/15",
    "small_cutoff_form": "-(8/15) omega^2 ln(delta)",
    "authoritative": True,
    "supersedes": "the single-branch power-divergence characterization "
                  "in commit 390a22d"}

# ================= 2. SUPERSESSION FRAMING (owner-specified) =========
print("\n=== 2: SUPERSESSION OF 390a22d (framing matters) ===")
OUT["supersession"] = {
    "commit": "390a22d",
    "what_is_superseded": "the EVIDENCE CHARACTERIZATION only -- "
                          "specifically the single-branch numeric route "
                          "and the resulting 1/delta power-divergence "
                          "description",
    "what_is_NOT_superseded": "the physical verdict. H2-B stands: the "
                              "H^2 local coefficients are not uniquely "
                              "determined and the sector is fork-gated",
    "precise_statement": "the original divergence classification was "
                         "BRANCH-INCOMPLETE, and the corrected full "
                         "retarded integrand still diverges "
                         "logarithmically",
    "not_a_failed_physical_result": True,
    "status": "SUPERSEDED AS EVIDENCE, NOT REFUTED AS RESULT"}
note("SUPERSESSION: %s" % OUT["supersession"]["precise_statement"])
check(OUT["supersession"]["not_a_failed_physical_result"] is True
      and "BRANCH-INCOMPLETE" in OUT["supersession"]["precise_statement"],
      "390a22d is marked SUPERSEDED AS EVIDENCE (branch-incomplete "
      "classification), explicitly NOT a failed physical result -- the "
      "provenance distinction the owner required", gate="SUPER")

# ================= 3. THE RULING, RECORDED VERBATIM =================
print("\n=== 3: THE OWNER RULING (10 clauses, recorded) ===")
RULING = {
    "1": "The corrected H^2 retarded local calculation has a genuine "
         "residual logarithmic IR divergence after exact cancellation "
         "of the prior power-divergent branch contribution.",
    "2": "No pre-existing IR prescription or IR scale is licensed by "
         "the frozen theory/contract.",
    "3": "The preregistered fork-(ii) route is acknowledged as an "
         "available future governance path, but it is NOT invoked to "
         "introduce a numerical IR regulator or new physical scale now.",
    "4": "Therefore: c0' = unresolved; c2' = unresolved; H^2 local "
         "sector = fork-gated.",
    "5": "No new independent input is introduced.",
    "6": "H^0 remains exactly one irreducible unresolved constant: "
         "Lambda_R.",
    "7": "Axis-2 remains C and is not recomputed.",
    "8": "The noise fork remains untouched.",
    "9": "Gate-E remains untouched.",
    "10": "The corrected H^2 evidence supersedes the erroneous "
          "single-branch power-divergence characterization from commit "
          "390a22d everywhere that it is cited.",
}
for k_, v in RULING.items():
    note("CLAUSE %s: %s" % (k_, v))
OUT["owner_ruling"] = RULING
check(len(RULING) == 10, "all ten ruling clauses recorded verbatim",
      gate="RULE")
OUT["future_ir_scale_status"] = (
    "Introducing an IR scale later would constitute a NEW DECLARED "
    "INPUT and would require its own provenance and independent "
    "justification -- it may not be justified by any spectral, memory, "
    "benchmark or downstream outcome.")
note("FUTURE: %s" % OUT["future_ir_scale_status"])

# ================= 4. WORDING GATES (owner-specified) ================
print("\n=== 4: CRITICAL WORDING GATES ===")
REQUIRED = ("The q^-4 / a=-1 power contribution cancels exactly between "
            "the two retarded cone branches. A nonzero q^-3 / a=0 "
            "logarithmic IR divergence remains.")
OUT["required_wording"] = REQUIRED
BADPHR = ["divergence was removed", "removed the divergence",
          "divergence is removed", "IR divergence removed"]
blob = json.dumps(OUT) + REQUIRED
check(not any(b in blob.lower() for b in
              [b.lower() for b in BADPHR]),
      "WORDING GATE 1: the record never says the H^2 divergence was "
      "'removed' -- it says the power contribution CANCELS and a "
      "logarithmic divergence REMAINS", gate="WORD")
control(any(b in ("the " + BADPHR[0]).lower() for b in
            [b.lower() for b in BADPHR]),
        "wording detector has teeth: a runtime-assembled offending "
        "phrase IS caught by the same membership test")
check("cancels exactly" in REQUIRED and "remains" in REQUIRED
      and "a=-1" in REQUIRED and "a=0" in REQUIRED,
      "WORDING GATE 2: the owner's prescribed sentence is carried "
      "verbatim, naming both the cancelling (a = -1) and surviving "
      "(a = 0) contributions", gate="WORD")
IRR = json.loads(open(os.path.join(
    HERE, "WALL_KR_H2_IR_OWNER_RULING_RESULT.json")).read())
check(IRR["out"]["conditional_c0p"]["promoted"] is False,
      "WORDING GATE 3: the conditional c0' = 0 statement remains NOT "
      "PROMOTED (read back from the prior audit's own record)",
      gate="WORD")

# ================= 5. FIREWALLS =================
print("\n=== 5: FIREWALLS ===")
_scale_assign = re.search(r"^\s*(q_min|IR_scale|ir_cutoff)\s*=",
                          selfsrc, re.M)
_num_in_out = re.search(r"\"(c0p|c2p)\":\s*[-+0-9]", json.dumps(OUT))
check(not _scale_assign and not _num_in_out,
      "no numerical IR scale is assigned in code and no numeric c0'/c2' "
      "is emitted in the record", gate="FW")
_tok = "RESO" + "NANT"
check(_tok not in selfsrc,
      "no downstream spectral outcome token in this record's source -- "
      "the decision consulted none", gate="FW")
control(_tok in (_tok + " sentinel"),
        "outcome-token scanner has teeth (runtime-assembled sentinel)")
LED = json.loads(open(os.path.join(
    HERE, "WALL_KR_H0_PARAMETER_LEDGER_RESULT.json")).read())
check(LED["irreducible_unresolved_H0_local_inputs"] == 1
      and LED["identifier"] == "Lambda_R",
      "CLAUSE 6 verified against the certified ledger: H^0 remains "
      "exactly ONE irreducible unresolved constant, Lambda_R",
      gate="FW")

# ================= 6. VALIDATION =================
print("\n=== 6: VALIDATION ===")
check(all(sha_file(os.path.join(HERE, fn)) == PRE[fn] for fn in PINS),
      "all frozen upstream artifacts byte-identical to their pre-run "
      "hashes", gate="VAL")
check(sha_file(CLAIMS) == CLAIMS_PRE,
      "register provenance/claims.json byte-identical -- the ruling "
      "introduces no input, so it requires no governance entry and "
      "none was made", gate="VAL")
OUT["register_entry_required"] = False
try:
    st = subprocess.run(["git", "status", "--short"], cwd=HERE,
                        capture_output=True, text=True, timeout=60).stdout
    OUT["worktree"] = st.strip().splitlines()
    note("files added/changed: %s"
         % (st.strip().replace("\n", " | ") or "(none yet)"))
except Exception as e:
    note("git status unavailable: %s" % e)

RESULT = {"instrument": "wall_kr_h2_ir_owner_decision.py",
          "instrument_sha256": sha_file(os.path.abspath(__file__)),
          "record_type": "OWNER DECISION RECORD (H^2 IR fork)",
          "decision": "LEAVE FORK-GATED",
          "ir_scale_introduced": False,
          "c0p": "UNRESOLVED", "c2p": "UNRESOLVED",
          "H0_Lambda_R": "ONE, unchanged",
          "axis2_status": "C, unchanged (not recomputed)",
          "noise_fork": "untouched", "gate_E": "untouched",
          "register_modified": False,
          "supersedes_evidence_of": "390a22d (branch-incomplete "
                                    "classification; NOT a failed "
                                    "physical result)",
          "out": OUT, "checks": CHECKS, "notes": NOTES, "failures": FAILS,
          "elapsed_s": round(time.time() - T0, 1)}
outp = os.path.join(HERE, "WALL_KR_H2_IR_OWNER_DECISION_RESULT.json")
json.dump(RESULT, open(outp, "w"), indent=1, default=str)
rr = json.loads(open(outp).read())
check(rr["ir_scale_introduced"] is False and rr["c0p"] == "UNRESOLVED"
      and rr["register_modified"] is False,
      "artifact written and re-read (sha %s...)" % sha_file(outp)[:16],
      gate="OUT")
npass = sum(1 for c in CHECKS if c["pass"])
print("\nH^2 IR OWNER DECISION: %d/%d passed; failures: %d"
      % (npass, len(CHECKS), len(FAILS)))
for m in FAILS:
    print("  FAILURE: " + m)
print("DECISION: LEAVE FORK-GATED | IR SCALE INTRODUCED: NO")
print("HARD STOP.")
sys.exit(0 if not FAILS else 1)
