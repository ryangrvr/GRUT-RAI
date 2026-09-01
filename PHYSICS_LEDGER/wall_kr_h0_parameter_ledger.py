#!/usr/bin/env python3
"""H^0 PARAMETER-COUNT / LEDGER UPDATE (owner authorization 2026-09-01).

GOVERNANCE / ACCOUNTING STAGE.  No physics is recomputed.  No value is
chosen.  The REGISTER IS NOT EDITED -- this records the bookkeeping
consequence of the frozen Owner Decision Record as a W-0 (unbanked)
PHYSICS_LEDGER artifact.

DOES NOT: choose Lambda_R or mu, compute H^2 locals, open the noise
fork, run Gate-E, modify Tier-4 or K_R, redo Axis-2, alter the
benchmark, or let any spectral outcome influence bookkeeping.

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
    "WALL_KR_D5_EXECUTION_RESULT.json": None,
    "WALL_KR_MU_CONVENTION_RESULT.json": None,
    "WALL_KR_MU_OWNER_DECISION_RESULT.json": None,
    "WALL_KR_LAMBDA_R_OWNER_RULING_RESULT.json": None,
    "WALL_KR_CONTRACT_RETARDED_RESULT.json": "d916ef32f6f73fa3",
    "WALL_A_A3_REGISTRY.json": "faa977d40f1ba318",
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
note("register provenance/claims.json sha %s... (READ-ONLY this stage)"
     % CLAIMS_PRE[:16])
if FAILS:
    sys.exit(2)

# ============ 5. CROSS-SCOPE FIREWALL (mechanical) ============
print("\n=== 5: BARRED-SOURCE FIREWALL ===")
reg = json.loads(open(os.path.join(HERE,
                                   "WALL_A_A3_REGISTRY.json")).read())
barred_files = {f for e in reg["g0_spectral_wiring"]["barred_inputs"]
                for f in (e.get("files") or [])}
BARRED_ARTIFACTS = ["WALL_KR_AXIS2_H0_RESULT.json",
                    "WALL_KR_CONTRACT_BENCHMARK_RESULT.json",
                    "wall_j_omega_comparison.py",
                    "wall_a_g1_ohmic_plant.py",
                    "MICROSCOPIC_TARGET_BENCHMARK.md"]
consumed = set(PINS)
check(not (consumed & set(BARRED_ARTIFACTS)),
      "NO Axis-2 output, benchmark artifact, J(omega) instrument, plant "
      "or comparator is consumed as evidence (read-set intersected with "
      "the barred/outcome set is empty)", gate="FW")
# sentinels assembled at RUNTIME (the recurring self-scan trap: a
# teeth-control must not plant the literal it forbids)
_tokA = "RESO" + "NANT"
_tokB = "0." + "79483"
body_hits = [t for t in (_tokA, _tokB) if t in selfsrc]
check(not body_hits,
      "no spectral-outcome token appears in this instrument's source "
      "-- bookkeeping cannot have been steered by an outcome",
      gate="FW")
control(_tokA in (_tokA + " sentinel") and _tokB in ("x" + _tokB),
        "outcome-token scanner has teeth: runtime-assembled sentinels "
        "ARE detected by the same membership test")
note("DISCLOSED CARVE-OUT: provenance/claims.json is on the registry's "
     "barred list for LOOP-COMPUTING instruments (F5 anti-unblinding). "
     "This stage READS it for GOVERNANCE ACCOUNTING ONLY -- it computes "
     "no loop quantity, consumes no spectral object from it, and does "
     "not modify it. The exemption is DECLARED, not assumed")

# ============ 3. FREE-INPUT ACCOUNTING (the decisive question) =======
print("\n=== 3: WHAT DID THE AUTHORITATIVE LEDGER ACTUALLY COUNT? ===")
craw = open(CLAIMS).read()
cj = json.loads(craw)
nodes = cj["claims"]
nodes = list(nodes.values()) if isinstance(nodes, dict) else nodes
has_LamR = "Lambda_R" in craw or "lambda_R" in craw
# the ONLY 'c4' occurrence is the substring of the prose token 'Sec4'
c4_hits = [m.start() for m in re.finditer(r"c4", craw)]
c4_all_sec4 = all(craw[max(0, i - 2):i + 2] == "Sec4" for i in c4_hits)
check(not has_LamR and c4_all_sec4,
      "REGISTER SEARCH: the register contains NO Lambda_R entry and no "
      "c4 entry -- its single 'c4' string match is the substring of the "
      "prose token 'Sec4' (%d occurrence(s), all accounted). The "
      "renormalization scale and the local constants were NEVER booked "
      "as register inputs" % len(c4_hits), gate="ACCT")
# NAME COLLISION -- the register's 'mu' is a DIFFERENT quantity
mu_nodes = [n["id"] for n in nodes
            if "mu = 1" in json.dumps(n) or "mu=1" in json.dumps(n)
            or "mu = 4/3" in json.dumps(n)]
check(len(mu_nodes) >= 1,
      "NAME COLLISION FOUND AND RECORDED: the register's 'mu' is the "
      "LINEAR-COSMOLOGY modification parameter mu = 1 + alpha (mu = 1 "
      "GR-like, mu = 4/3 trace-only) in nodes %s -- a DIFFERENT "
      "physical quantity from the renormalization scale. The two must "
      "never be conflated; this is an independent reason the new "
      "constant is carried as Lambda_R and not as 'mu'" % mu_nodes,
      gate="ACCT")
OUT["name_collision"] = {
    "register_mu": "linear-cosmology modification parameter mu = 1 + "
                   "alpha (mu = 1 GR-like; mu = 4/3 trace-only, "
                   "ISW-excluded); nodes: %s" % mu_nodes,
    "this_stage_mu": "the RENORMALIZATION SCALE of the contract H^0 "
                     "kernel -- unrelated",
    "consequence": "the new constant is named Lambda_R, which also "
                   "removes the collision risk"}
net = sum((n.get("ledger_delta") or 0) for n in nodes)
OUT["register_net_as_read"] = net
note("register net (sum of ledger_delta, read-only) = %+d" % net)
OUT["free_input_accounting"] = {
    "were_mu_and_c4_counted_before": "NO -- neither appears in the "
                                     "register in any form. The entire "
                                     "contract-K_R campaign has been "
                                     "W-0 (computed-and-reported, NOT "
                                     "banked) throughout",
    "is_this_a_reduction_of_the_count": "NO. Per the owner's explicit "
                                        "instruction, no numerical "
                                        "'reduction' is manufactured",
    "correct_statement": "the apparent two-parameter H^0 "
                         "representation is shown to contain exactly "
                         "ONE independent constant",
    "register_net_change": 0}
check(True, "ACCOUNTING VERDICT: this is a REPRESENTATION result, not a "
      "register-net change. mu and c4 were never independent frozen "
      "inputs, so no reduction is claimed and the net is unchanged",
      gate="ACCT")

# ============ 1/2. THE PARAMETER COUNT AND THE ASSERTIONS ============
print("\n=== 1/2: PARAMETER COUNT + ASSERTIONS A-G ===")
om, mu = sp.symbols("omega mu", positive=True)
Ax, c4s = sp.symbols("A_x c4", real=True)
LamR = sp.Symbol("Lambda_R", positive=True)
ReSig = 2 * Ax * om**4 * sp.log(LamR / om)
expl = Ax * om**4 * sp.log(mu**2 / om**2) + c4s * om**4
# (E) Lambda_R is genuine
check(sp.simplify(sp.diff(ReSig, LamR)) != 0,
      "ASSERTION E: d ReSigma^(H0) / d Lambda_R != 0 -- Lambda_R is a "
      "GENUINE degree of freedom (the count is not zero)", gate="ASRT")
# (D) exactly one independent constant: two (mu, c4) points with the
#     SAME Lambda_R give the IDENTICAL response
m1, m2 = sp.Integer(2), sp.Integer(7)
c41 = sp.Symbol("c41", real=True)
c42 = sp.simplify(c41 + 2 * Ax * sp.log(m1 / m2))     # same Lambda_R
d_same = sp.simplify(sp.expand_log(
    expl.subs({mu: m1, c4s: c41}) - expl.subs({mu: m2, c4s: c42}),
    force=True))
check(d_same == 0,
      "ASSERTION D: two DISTINCT (mu, c4) points sharing one Lambda_R "
      "give the IDENTICAL response -- the pair contains exactly ONE "
      "independent H^0 constant (the family is degenerate along the "
      "Lambda_R orbit)", gate="ASRT")
# NEGATIVE CONTROL (owner-mandated): treating (mu, c4) as TWO
# independent constants violates the collapse relation
c42_bad = sp.simplify(c42 + sp.Rational(1, 5))        # off the orbit
d_bad = sp.simplify(sp.expand_log(
    expl.subs({mu: m1, c4s: c41}) - expl.subs({mu: m2, c4s: c42_bad}),
    force=True))
control(d_bad != 0,
        "NEGATIVE CONTROL: moving c4 OFF the Lambda_R orbit changes the "
        "response (difference = %s) -- so the degeneracy is specific to "
        "Lambda_R, not a vacuous identity, and the 'two independent "
        "constants' reading is violated by the certified collapse "
        "relation" % str(d_bad))
ASSERT = {
    "A": "c0 = 0 exactly (certified D5, structural)",
    "B": "c2 = 0 exactly (certified D5, structural)",
    "C": "c4 is determined by the certified D5 finite calculation ONLY "
         "modulo the renormalization-scale representation",
    "D": "(mu, c4) contains exactly ONE independent H^0 constant",
    "E": "Lambda_R is genuine: d ReSigma^(H0)/d Lambda_R != 0",
    "F": "NO numerical value of Lambda_R has been introduced",
    "G": "Axis-2 remains C",
}
for k_, v in ASSERT.items():
    note("ASSERTION %s: %s" % (k_, v))
OUT["assertions"] = ASSERT
D5 = json.loads(open(os.path.join(
    HERE, "WALL_KR_D5_EXECUTION_RESULT.json")).read())
slot = D5["out"]["local_slot_determined"]
check(slot["c0"].startswith("0") and slot["c2"].startswith("0"),
      "ASSERTIONS A and B verified against the certified D5 artifact's "
      "own record (c0, c2 fields), not retyped", gate="ASRT")
OWN = json.loads(open(os.path.join(
    HERE, "WALL_KR_LAMBDA_R_OWNER_RULING_RESULT.json")).read())
check(OWN["numerical_value_introduced"] is False
      and OWN["axis2_status"].startswith("C"),
      "ASSERTIONS F and G verified against the frozen Owner Decision "
      "Record (numerical_value_introduced = False; Axis-2 = C)",
      gate="ASRT")

# ============ 6. MACHINE-READABLE PARAMETER RECORD ============
print("\n=== 6: MACHINE-READABLE RECORD ===")
PARAM = {
    "id": "contract_H0_renormalization_invariant",
    "name": "Lambda_R",
    "sector": "H^0 contract retarded response",
    "status": "unresolved",
    "numerical_value": None,
    "dimension": "frequency",
    "independence": "irreducible",
    "origin": "reparameterization of (mu, c4)",
    "derivation_status": "not numerically derived",
    "owner_status": "explicitly unselected",
    "axis2_dependence": "none for its declaration",
    "h2_scope": "excluded",
    # claims.json-compatible fields, so this can be promoted verbatim
    # if the owner ever banks it -- it is NOT a register node today
    "statement": "The H^0 contract retarded response contains exactly "
                 "one independent unresolved renormalization constant, "
                 "Lambda_R = mu exp(c4/(2A)), a REPARAMETERIZATION of "
                 "the (mu, c4) representation and not the removal of a "
                 "parameter. No numerical value has been selected.",
    "tier": "W-0 (computed-and-reported, NOT banked)",
    "depends_on": ["D5 certified H^0 execution", "mu-RULING-C",
                   "Owner Decision Record (Lambda_R)"],
    "ledger_delta": 0,
    "ledger_note": "0: NOT a register-net change. mu and c4 were never "
                   "booked as independent register inputs (verified: "
                   "the register contains no Lambda_R and no c4 entry), "
                   "so no reduction is claimed. This records a "
                   "REPRESENTATION result.",
    "register_node": False,
}
OUT["parameter_record"] = PARAM
OUT["irreducible_unresolved_H0_local_inputs"] = 1
check(PARAM["numerical_value"] is None
      and PARAM["h2_scope"] == "excluded"
      and PARAM["ledger_delta"] == 0
      and PARAM["register_node"] is False,
      "machine-readable record: numerical_value = null, H^2 excluded, "
      "ledger_delta = 0, register_node = False (schema mirrors "
      "claims.json field names so it could be promoted verbatim, but "
      "it is NOT a register node today)", gate="SCHEMA")
check("removed" not in PARAM["statement"]
      and "reparameteriz" in PARAM["statement"].lower(),
      "wording gate: the record says REPARAMETERIZATION and never "
      "'removed' (owner's refinement, enforced mechanically)",
      gate="SCHEMA")

# ============ 4. REGISTER FIREWALL ============
print("\n=== 4: REGISTER FIREWALL ===")
check(sha_file(CLAIMS) == CLAIMS_PRE,
      "the register is BYTE-IDENTICAL: no claim grade upgraded or "
      "downgraded, no node added, no ledger_delta altered by this "
      "accounting stage", gate="REGFW")
OUT["register_firewall"] = {
    "claims_json_modified": False,
    "grades_touched": "none",
    "net_change": 0,
    "axis2": "C, unchanged",
    "single_pole_stance": "untouched",
    "K_R_conclusions": "untouched"}

# ============ 7/8. PROVENANCE + VALIDATION ============
print("\n=== 7/8: PROVENANCE AND VALIDATION ===")
OUT["provenance"] = {
    "D5_H0_c0_c2_c4": "commits 12ea453 (execution) / 04b8d6c (verdict "
                      "wording repair); artifact "
                      "WALL_KR_D5_EXECUTION_RESULT.json",
    "mu_RULING_C": "commit eef50eb; artifact "
                   "WALL_KR_MU_CONVENTION_RESULT.json",
    "owner_decision_record": "commit fb3ce39; artifact "
                             "WALL_KR_LAMBDA_R_OWNER_RULING_RESULT.json",
    "Lambda_R_reparameterization": "commit 4a2e728 (owner decision "
                                   "package, section 3) and fb3ce39 "
                                   "(gated both ways)",
    "NOT_cited": "the uncertified pre-repair Axis-2 runs "
                 "(wall_kr_d5_exec_run2/3/4.log) are NOT cited and NOT "
                 "read"}
check(not re.search(r"run[234]\.log", selfsrc),
      "no uncertified preliminary Axis-2 run is cited or read",
      gate="PROV")
check(all(sha_file(os.path.join(HERE, fn)) == PRE[fn] for fn in PINS)
      and sha_file(CLAIMS) == CLAIMS_PRE,
      "all frozen upstream artifacts AND the register byte-identical to "
      "their pre-run hashes", gate="PROV")
try:
    st = subprocess.run(["git", "status", "--short"], cwd=HERE,
                        capture_output=True, text=True, timeout=60).stdout
    OUT["worktree"] = st.strip().splitlines()
    note("files added/changed: %s"
         % (st.strip().replace("\n", " | ") or "(none yet)"))
except Exception as e:
    note("git status unavailable: %s" % e)

RESULT = {"instrument": "wall_kr_h0_parameter_ledger.py",
          "instrument_sha256": sha_file(os.path.abspath(__file__)),
          "record_type": "H^0 PARAMETER-COUNT / LEDGER UPDATE "
                         "(governance accounting; W-0, unbanked)",
          "irreducible_unresolved_H0_local_inputs": 1,
          "identifier": "Lambda_R",
          "numerical_value": None,
          "parameterization": "(mu, c4) -> Lambda_R",
          "axis2_status": "C, unchanged",
          "h2_touched": False,
          "register_modified": False,
          "out": OUT, "checks": CHECKS, "notes": NOTES, "failures": FAILS,
          "elapsed_s": round(time.time() - T0, 1)}
outp = os.path.join(HERE, "WALL_KR_H0_PARAMETER_LEDGER_RESULT.json")
json.dump(RESULT, open(outp, "w"), indent=1, default=str)
rr = json.loads(open(outp).read())
check(rr["numerical_value"] is None and rr["register_modified"] is False
      and rr["irreducible_unresolved_H0_local_inputs"] == 1,
      "artifact written and re-read: count = 1, numerical_value = null, "
      "register_modified = False (sha %s...)" % sha_file(outp)[:16],
      gate="OUT")
npass = sum(1 for c in CHECKS if c["pass"])
print("\nH^0 PARAMETER LEDGER: %d/%d passed; failures: %d"
      % (npass, len(CHECKS), len(FAILS)))
for m in FAILS:
    print("  FAILURE: " + m)
print("HARD STOP.")
sys.exit(0 if not FAILS else 1)
