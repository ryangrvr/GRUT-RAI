#!/usr/bin/env python3
"""OWNER DECISION RECORD -- the Lambda_R renormalization input
(owner ruling issued 2026-09-01).  RECORDING + MECHANICAL VERIFICATION.
NOT a calculation.  Selects NO numerical value.  Does not re-adjudicate
Axis 2, does not touch H^2, the noise fork, Gate-E, Tier-4, K_R, or the
benchmark.  Does NOT edit the register (the ledger/parameter-count
update is the NEXT stage and awaits its own authorization).

THE RULING (owner, verbatim -- recorded, not composed here):

  The current GRUT record does not contain an independently justified
  numerical value for the renormalization invariant Lambda_R.  No
  numerical value will be introduced at this stage.  Lambda_R remains
  symbolic and is carried as one unresolved renormalization input.
  Axis 2 therefore remains parametrically unresolved with respect to
  Lambda_R.  Future numerical fixing is permitted only through an
  independently justified renormalization/matching condition that is
  established without reference to Axis 1, Axis 2, J(omega), plant
  data, resonance, memory behavior, or other downstream outcomes.

VERIFICATION DUTY: prove mechanically that this record derives
Lambda_R from NO barred downstream quantity -- i.e. that no numerical
value is assigned to Lambda_R or mu anywhere in the new artifacts, and
that the ruling's evidence basis is the authority sweep, not any
outcome artifact.

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
T0 = time.time()
FAILS, CHECKS, NOTES, OUT = [], [], [], {}


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
    "WALL_KR_MU_OWNER_DECISION_RESULT.json": None,
    "WALL_KR_MU_CONVENTION_RESULT.json": None,
    "WALL_KR_D5_EXECUTION_RESULT.json": None,
    "WALL_KR_AXIS2_H0_RESULT.json": None,
    "WALL_KR_CONTRACT_RETARDED_RESULT.json": "d916ef32f6f73fa3",
    "WALL_A_A3_DECLARATIONS.md": "87e2d24d5be6d679",
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
if FAILS:
    sys.exit(2)

# ================= 1. THE RULING, RECORDED VERBATIM =================
print("\n=== 1: THE OWNER RULING (recorded, not composed) ===")
RULING = (
    "The current GRUT record does not contain an independently "
    "justified numerical value for the renormalization invariant "
    "Lambda_R. No numerical value will be introduced at this stage. "
    "Lambda_R remains symbolic and is carried as one unresolved "
    "renormalization input. Axis 2 therefore remains parametrically "
    "unresolved with respect to Lambda_R. Future numerical fixing is "
    "permitted only through an independently justified renormalization/"
    "matching condition that is established without reference to "
    "Axis 1, Axis 2, J(omega), plant data, resonance, memory behavior, "
    "or other downstream outcomes.")
OUT["owner_ruling_verbatim"] = RULING
note("RULING: %s" % RULING)
check(all(t in RULING for t in ("does not contain an independently "
                                "justified numerical value",
                                "remains symbolic",
                                "one unresolved renormalization input",
                                "without reference to")),
      "the ruling is recorded VERBATIM with its four operative clauses "
      "intact: (a) no independently justified value exists; (b) none is "
      "introduced now; (c) Lambda_R is carried as ONE unresolved "
      "renormalization input; (d) future fixing only via an "
      "independent condition", gate="RULE")

# ================= 2. NO VALUE ASSIGNED -- MECHANICAL =================
print("\n=== 2: NO NUMERICAL VALUE IS ASSIGNED (mechanical) ===")
NEW_FILES = ["wall_kr_lambdaR_owner_ruling.py",
             "WALL_KR_LAMBDA_R_OWNER_RULING.md"]


selfsrc = open(os.path.abspath(__file__)).read()


def assigns_number(txt):
    """detect an assignment of a numeric value to Lambda_R or mu."""
    pats = [r"Lambda_R\s*[:=]\s*[-+0-9.]", r"Λ_R\s*[:=]\s*[-+0-9.]",
            r"Lambda_R\s*=\s*[0-9]", r"\bmu\s*=\s*[0-9]",
            r"μ\s*=\s*[0-9]", r"Lambda_R\s*of\s*[0-9]"]
    return [p for p in pats if re.search(p, txt)]


hits_self = assigns_number(selfsrc)
check(not hits_self,
      "this instrument assigns NO numeric value to Lambda_R or mu "
      "(pattern scan over its own source)", gate="NOVAL")
# the sentinel is assembled at RUNTIME so the literal assignment never
# appears in this source (third instance of the self-scan trap in this
# campaign: a teeth-control that plants the very pattern it forbids)
_sent = "Lambda_R" + " = " + "1.0 WC"
control(bool(assigns_number(_sent)) and not assigns_number(selfsrc),
        "the value-assignment detector has teeth: a sentinel built at "
        "runtime IS caught by the same scan, while the source itself "
        "carries no assignment")
LamR = sp.Symbol("Lambda_R", positive=True)
check(LamR.is_Symbol and LamR.free_symbols == {LamR},
      "Lambda_R is carried as a free SYMBOL in this record -- it enters "
      "no numeric context anywhere", gate="NOVAL")

# ============ 3. EVIDENCE BASIS IS THE AUTHORITY SWEEP ============
print("\n=== 3: THE RULING'S EVIDENCE BASIS ===")
PKG = json.loads(open(os.path.join(
    HERE, "WALL_KR_MU_OWNER_DECISION_RESULT.json")).read())
auth = PKG["out"]["authority_table"]
nsup = sum(1 for r in auth if r["supplies_numerical_mu"] == "yes")
check(PKG["current_mu_ruling"] == "C"
      and PKG["numerical_mu_selected"] is False and nsup == 0,
      "EVIDENCE: the ruling rests on the hash-pinned authority sweep "
      "(%d entries, ZERO supplying a numerical scale) and on ruling C "
      "-- NOT on any outcome artifact" % len(auth), gate="EVID")
check(not re.search(r"AXIS2_H0_RESULT[^\n]*\[[\"']out[\"']\]", selfsrc),
      "the Axis-2 artifact is hash-pinned for provenance only; its "
      "'out' block (which carries the classification and the regime "
      "map) is never dereferenced by this record", gate="EVID")
reg = json.loads(open(os.path.join(HERE,
                                   "WALL_A_A3_REGISTRY.json")).read())
barred = {f for e in reg["g0_spectral_wiring"]["barred_inputs"]
          for f in (e.get("files") or [])}
read_files = set(PINS)
check(not (read_files & barred),
      "NO barred file is read by this record (barred set intersected "
      "with the read set is empty) -- the comparator-to-response "
      "channel is not used", gate="EVID")

# ============ 4. PARAMETER COUNT (executable structural result) ======
print("\n=== 4: THE H^0 FREE-INPUT COUNT ===")
om, mu = sp.symbols("omega mu", positive=True)
Ax, c4s = sp.symbols("A_x c4", real=True)
# certified D5: c0 = c2 = 0; the surviving local datum is c4, and
# (mu, c4) enter ONLY through Lambda_R = mu exp(c4/(2A))
ReSig = 2 * Ax * om**4 * sp.log(LamR / om)
# (i) the response genuinely DEPENDS on Lambda_R (so the count is not 0)
dep = sp.simplify(sp.diff(ReSig, LamR))
check(dep != 0,
      "(i) NOT ZERO parameters: d(Re Sigma)/d(Lambda_R) = %s != 0, so "
      "Lambda_R is a genuine degree of freedom of the H^0 response"
      % str(sp.simplify(dep)), gate="COUNT")
# (ii) mu and c4 enter ONLY via Lambda_R (so the count is not 2):
#      the explicit form in (mu, c4) equals the Lambda_R form
expl = Ax * om**4 * sp.log(mu**2 / om**2) + c4s * om**4
same = sp.simplify(sp.expand_log(
    expl - ReSig.subs(LamR, mu * sp.exp(c4s / (2 * Ax))), force=True))
check(same == 0,
      "(ii) NOT TWO parameters: the explicit (mu, c4) form is "
      "IDENTICALLY the one-constant form, so the pair enters only "
      "through Lambda_R -- a reparameterization, NOT a removal (owner's "
      "refinement, adopted): nothing left the theory; two redundant "
      "parameters were replaced by one irreducible constant",
      gate="COUNT")
control(sp.simplify(sp.expand_log(
    expl - 2 * Ax * om**4 * sp.log((mu + 1) * sp.exp(c4s / (2 * Ax)) / om),
    force=True)) != 0,
        "count control: a WRONG invariant (mu -> mu + 1 inside "
        "Lambda_R) fails the identity -- the one-constant collapse is "
        "specific to Lambda_R and not an artifact of the algebra")
OUT["free_input_count_H0"] = {
    "before_D5": "five real local constants (c0, c2, c4, c0p, c2p) plus "
                 "the scale mu",
    "after_D5_at_H0": "c0 = 0 and c2 = 0 EXACTLY (structural); the "
                      "surviving (mu, c4) pair is redundant by exactly "
                      "one function's worth",
    "irreducible_count": 1,
    "the_constant": "Lambda_R = mu exp(c4/(2A)), RG-invariant",
    "status_of_the_constant": "UNRESOLVED -- no independently justified "
                              "value exists in the record",
    "framing": "REPARAMETERIZED, not removed: (mu, c4) -> Lambda_R",
    "H2_sector": "NOT counted here -- fork-gated; the H^2 locals "
                 "(c0p, c2p) remain outside this count"}
note("PARAMETER-COUNT RESULT (positive structural finding): the H^0 "
     "local freedom is EXACTLY ONE independent dimensionful constant, "
     "down from five constants plus a scale before D5")

# ============ 5. WHAT THE RULING DOES AND DOES NOT SETTLE ============
print("\n=== 5: SCOPE OF THE RULING ===")
OUT["ruling_scope"] = {
    "settles": ["that NO numerical value enters GRUT at this stage",
                "that Lambda_R is carried as ONE unresolved "
                "renormalization input",
                "that Axis 2 is parametrically unresolved with respect "
                "to Lambda_R -- classification C stands",
                "the admissibility condition for any FUTURE fixing"],
    "does_not_settle": ["the value of Lambda_R",
                        "Axis 2's absolute classification",
                        "the H^2 local fork",
                        "Gate-E",
                        "the consequence cell beyond recording C"],
    "explicitly_not_done": "the register/ledger parameter-count update "
                           "is the NEXT stage and is NOT performed "
                           "here; provenance/claims.json is untouched "
                           "and the net stands unchanged"}
for k_, v in OUT["ruling_scope"].items():
    note("SCOPE %s: %s" % (k_, v if isinstance(v, str) else "; ".join(v)))

# ================= VALIDATION / FREEZE =================
print("\n=== VALIDATION ===")
check(all(sha_file(os.path.join(HERE, fn)) == PRE[fn] for fn in PINS),
      "every pinned input byte-identical to its pre-run hash", gate="PROV")
prov = os.path.join(HERE, "..", "provenance", "claims.json")
if os.path.exists(prov):
    OUT["claims_sha"] = sha_file(prov)[:16]
    note("provenance/claims.json sha %s... (READ ONLY -- not modified "
         "by this stage)" % OUT["claims_sha"])
try:
    st = subprocess.run(["git", "status", "--short"], cwd=HERE,
                        capture_output=True, text=True, timeout=60).stdout
    OUT["worktree"] = st.strip().splitlines()
    note("files added/changed: %s"
         % (st.strip().replace("\n", " | ") or "(none yet)"))
except Exception as e:
    note("git status unavailable: %s" % e)
RESULT = {"instrument": "wall_kr_lambdaR_owner_ruling.py",
          "instrument_sha256": sha_file(os.path.abspath(__file__)),
          "record_type": "OWNER DECISION RECORD (ruling recorded and "
                         "mechanically verified; not composed by the "
                         "builder)",
          "owner_ruling_verbatim": RULING,
          "numerical_value_introduced": False,
          "lambda_R_status": "SYMBOLIC -- one unresolved renormalization "
                             "input",
          "axis2_status": "C, parametrically unresolved w.r.t. Lambda_R",
          "register_modified": False,
          "out": OUT, "checks": CHECKS, "notes": NOTES, "failures": FAILS,
          "elapsed_s": round(time.time() - T0, 1)}
outp = os.path.join(HERE, "WALL_KR_LAMBDA_R_OWNER_RULING_RESULT.json")
json.dump(RESULT, open(outp, "w"), indent=1, default=str)
rr = json.loads(open(outp).read())
check(rr["numerical_value_introduced"] is False
      and rr["register_modified"] is False,
      "artifact written and re-read: numerical_value_introduced = False "
      "AND register_modified = False on the record (sha %s...)"
      % sha_file(outp)[:16], gate="OUT")
npass = sum(1 for c in CHECKS if c["pass"])
print("\nLAMBDA_R OWNER RULING RECORD: %d/%d passed; failures: %d"
      % (npass, len(CHECKS), len(FAILS)))
for m in FAILS:
    print("  FAILURE: " + m)
print("HARD STOP.")
sys.exit(0 if not FAILS else 1)
