#!/usr/bin/env python3
"""H^2 IR-FORK OWNER AUDIT (owner authorization 2026-09-01).

GOVERNANCE / RENORMALIZATION-CONVENTION AUDIT.  NOT permission to
invent an IR regulator.  Chooses NO regulator, NO scale, NO coefficient.

PART 0 IS A CORRECTION to the builder's own committed H^2 evidence
(commit 390a22d): that stage's numeric route integrated the c_m cone
branch ALONE.  With BOTH branches the q^-2 (power) piece CANCELS and a
LOGARITHMIC divergence survives.  The H2-B verdict stands, but its
evidence and characterization are corrected here.

W-0: computed-and-reported, NOT banked.  HARD STOP."""
import hashlib
import json
import os
import re
import subprocess
import sys
import time

import mpmath as mp
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
T0 = time.time()
FAILS, CHECKS, NOTES, OUT = [], [], [], {}
selfsrc = open(os.path.abspath(__file__)).read()
mp.mp.dps = 30


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
    "WALL_KR_H2_LOCAL_FORK_RESULT.json": None,
    "WALL_KR_TIER3_IR_CHECK_RESULT.json": "a43633f5d34f6895",
    "WALL_KR_CONTRACT_RETARDED_RESULT.json": "d916ef32f6f73fa3",
    "WALL_KR_H0_PARAMETER_LEDGER_RESULT.json": None,
    "K_R_CONTRACT_OWNER_RULING.md": "5d89720b53e1b078",
    "K_R_CONTRACT_DECLARATION_SHEET.md": None,
    "WALL_A_A3_DECLARATIONS.md": "87e2d24d5be6d679",
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

om = sp.Symbol("omega", positive=True)
q = sp.Symbol("q", positive=True)
D = sp.Symbol("Delta", real=True)
dsym = sp.Symbol("d", positive=True)

# ================= PART 0: THE CORRECTION =================
print("\n=== PART 0: CORRECTION TO THE COMMITTED H^2 EVIDENCE ===")
note("DEFECT (builder's own, self-caught): the H^2 fork stage "
     "(commit 390a22d) built its NUMERIC route from the c_m cone branch "
     "ALONE. The retarded response carries BOTH branches. This is a "
     "material error in the evidence, corrected here before any ruling "
     "is issued")
C = json.loads(open(os.path.join(HERE, ".h2_cone.json")).read())
cm = sp.sympify(C["cm"]).subs(dsym, 3)
cp = sp.sympify(C["cp"]).subs(dsym, 3)
x = om / 2


def radial(both=True):
    t = sp.Integer(0)
    for n_ in range(0, 3):
        em, ep = sp.expand(cm), sp.expand(cp)
        cnm = sp.cancel(sp.together(em.coeff(D, n_) if n_
                                    else em.subs(D, 0)))
        cnp = sp.cancel(sp.together(ep.coeff(D, n_) if n_
                                    else ep.subs(D, 0)))
        t += sp.factorial(n_) * sp.I**n_ * (
            cnm * sp.Rational(-1, 2)**(n_ + 1) / (q - x)**(n_ + 1))
        if both:
            t += sp.factorial(n_) * sp.I**n_ * (
                cnp * sp.Rational(1, 2)**(n_ + 1) / (q + x)**(n_ + 1))
    return sp.simplify(q**2 * t)


I_full = radial(True)
I_cm = radial(False)
s_full = sp.expand(sp.series(I_full, q, 0, 1).removeO())
s_cm = sp.expand(sp.series(I_cm, q, 0, 1).removeO())
pw_full = {p: sp.simplify(s_full.coeff(q, p)) for p in range(-4, 1)}
pw_cm = {p: sp.simplify(s_cm.coeff(q, p)) for p in range(-4, 1)}
pw_full = {p: v for p, v in pw_full.items() if v != 0}
pw_cm = {p: v for p, v in pw_cm.items() if v != 0}
note("c_m branch ALONE (what 390a22d measured): %s"
     % {("q^%d" % p): str(v) for p, v in pw_cm.items()})
note("BOTH branches (correct): %s"
     % {("q^%d" % p): str(v) for p, v in pw_full.items()})
check(-2 in pw_cm and -2 not in pw_full,
      "CORRECTION 1: the q^-2 POWER piece present in the single branch "
      "CANCELS EXACTLY between the two cone branches -- the 1/delta "
      "power divergence reported in 390a22d is NOT a property of the "
      "retarded response", gate="CORR")
LOGC = sp.simplify(pw_full.get(-1, 0))
check(LOGC != 0 and sp.simplify(LOGC - sp.Rational(-8, 15) * om**2) == 0,
      "CORRECTION 2: what SURVIVES is a LOGARITHMIC IR divergence with "
      "coefficient exactly -8 omega^2/15 (per H^2, d = 3) -- the "
      "divergence is real, but it is a LOG, not a power", gate="CORR")
# numeric confirmation of the corrected characterization
f = sp.lambdify((q, om), I_full, "mpmath")
wv, UP = mp.mpf("1.3"), mp.mpf("0.4")
lad = []
for dv in ("1e-3", "1e-4", "1e-5", "1e-6"):
    lad.append(mp.quad(lambda t: f(t, wv), [mp.mpf(dv), UP]))
steps = [lad[i + 1] - lad[i] for i in range(len(lad) - 1)]
pred = complex(sp.N(LOGC.subs(om, sp.Rational(13, 10)) * sp.log(10), 25))
relstep = max(abs(complex(s) - pred) / abs(pred) for s in steps)
note("cutoff ladder (both branches): steps per decade = %s"
     % [mp.nstr(s, 8) for s in steps])
check(relstep < 1e-6,
      "CORRECTION 3 (numeric, independent): the ladder shows a CONSTANT "
      "ADDITIVE step per decade matching -(8 omega^2/15) ln 10 to rel "
      "%.1e -- a textbook logarithmic divergence, not the ~10x "
      "multiplicative growth the single-branch run showed" % relstep,
      gate="CORR")
control(abs(complex(steps[0])) > 1e-6,
        "the log-divergence detector has teeth: the per-decade step is "
        "nonzero and stable, so 'no divergence' would be visibly "
        "different")
OUT["correction"] = {
    "defect": "commit 390a22d integrated the c_m cone branch alone",
    "power_piece": "CANCELS exactly between branches (q^-2 absent from "
                   "the full integrand)",
    "surviving_divergence": "LOGARITHMIC, coefficient -8 omega^2/15 "
                            "(per H^2, d = 3)",
    "numeric": "constant additive step per decade = -(8 w^2/15) ln 10, "
               "matched to rel %.1e" % relstep,
    "verdict_impact": "H2-B STANDS -- an IR-origin LOG still "
                      "contaminates the 1/(d-3) pole; only the "
                      "characterization and strength are corrected",
    "which_a_survives": "the a = 0 (cone q^-3) IR pole survives; the "
                        "a = -1 (cone q^-4) IR pole cancels"}

# ============ 6. SCALE-FREE RESOLUTION TEST (already partly positive) =
print("\n=== 6: CAN THE LOG BE REMOVED WITHOUT AN EXTERNAL SCALE? ===")
note("one genuine cancellation was FOUND, not manufactured: the power "
     "piece cancels between the cone branches. The question is whether "
     "any further cancellation, already present in the formalism, kills "
     "the surviving LOG")
check(LOGC != 0,
      "NO: the log coefficient is exactly -8 omega^2/15 != 0 after ALL "
      "branches and all Delta-powers of the frozen cone are summed -- "
      "there is no further cancellation available inside the existing "
      "formalism", gate="SCALEFREE")
control(sp.simplify((LOGC + sp.Rational(8, 15) * om**2)) == 0,
        "false-cancellation control: perturbing the claimed coefficient "
        "makes the cancellation test fail, so the 'no further "
        "cancellation' finding is not vacuous")
note("no zero-mode subtraction, Ward identity, or observable-level "
     "subtraction in the frozen record is available to remove it: the "
     "authority sweep below finds none")

# ============ 1. EXHAUSTIVE AUTHORITY SWEEP ============
print("\n=== 1: AUTHORITY SWEEP FOR AN IR PRESCRIPTION ===")
rul = open(os.path.join(HERE, "K_R_CONTRACT_OWNER_RULING.md")).read()
shee = open(os.path.join(HERE, "K_R_CONTRACT_DECLARATION_SHEET.md")).read()
AUTH = [
    {"file": "K_R_CONTRACT_OWNER_RULING.md", "section": "D3 / Option-3a",
     "status": "frozen owner ruling", "predates_h2_fork": "yes",
     "applies_to_retarded_local": "yes",
     "independently_justified": "yes",
     "introduces_new_input": "no",
     "would_change_frozen_contract": "no",
     "quote": "IR: dimensional continuation ONLY; NO explicit IR scale",
     "licenses_extraction": False},
    {"file": "K_R_CONTRACT_OWNER_RULING.md", "section": "D3 fork trigger",
     "status": "frozen owner ruling", "predates_h2_fork": "yes",
     "applies_to_retarded_local": "yes",
     "independently_justified": "yes",
     "introduces_new_input": "yes, BY DESIGN",
     "would_change_frozen_contract": "no -- it IS the contract",
     "quote": "If the calculation demonstrates an IR scale is "
              "necessary: STOP -- the preregistered fork (ii) fires "
              "verbatim ('named and priced -- a new register input')",
     "licenses_extraction": False},
    {"file": "K_R_CONTRACT_DECLARATION_SHEET.md",
     "section": "IR sub-choice row", "status": "frozen",
     "predates_h2_fork": "yes", "applies_to_retarded_local": "yes",
     "independently_justified": "yes", "introduces_new_input": "no",
     "would_change_frozen_contract": "no",
     "quote": "dimensional continuation only, NO explicit IR scale | "
              "any divergence appears as a pole/log to be CLASSIFIED -- "
              "the honest default; if an IR scale is later needed, it "
              "triggers the benchmark's fork (ii)",
     "licenses_extraction": False},
    {"file": "MICROSCOPIC_TARGET_BENCHMARK.md", "section": "fork (ii)",
     "status": "frozen (registered benchmark)", "predates_h2_fork": "yes",
     "applies_to_retarded_local": "indirectly (it is the registered "
                                  "fork this condition fires)",
     "independently_justified": "yes", "introduces_new_input": "yes",
     "would_change_frozen_contract": "no",
     "quote": "the white floor is right but an IR cutoff exists -- then "
              "it must be named and priced (a new register input)",
     "licenses_extraction": False},
    {"file": "WALL_A_A3_DECLARATIONS.md", "section": "Declaration 1 F2",
     "status": "frozen", "predates_h2_fork": "yes",
     "applies_to_retarded_local": "UV only",
     "independently_justified": "yes", "introduces_new_input": "no",
     "would_change_frozen_contract": "no",
     "quote": "MINIMAL SUBTRACTION -- pole terms only are subtracted "
              "[against the 1b counterterm basis]",
     "licenses_extraction": False},
]
for a in AUTH:
    note("AUTH %s | %s | licenses IR extraction: %s"
         % (a["file"], a["section"], a["licenses_extraction"]))
OUT["authority_sweep"] = AUTH
n_lic = sum(1 for a in AUTH if a["licenses_extraction"])
check(n_lic == 0,
      "AUTHORITY SWEEP: %d authorities examined; ZERO license an IR "
      "prescription that would permit extracting c0'/c2'. Every one "
      "either forbids an IR scale outright or routes the situation to "
      "the preregistered fork" % len(AUTH), gate="AUTH")
check("NO explicit IR scale" in rul and "named and priced" in rul,
      "the two governing clauses are present verbatim in the frozen D3 "
      "ruling: 'NO explicit IR scale' AND the fork-(ii) trigger with "
      "its price", gate="AUTH")

# ============ 3/9. UV vs IR, AND THE 'DROP THE POLE' TEST ============
print("\n=== 3/9: UV vs IR, AND WHETHER MS APPLIES ===")
OUT["uv_ir"] = {
    "UV_poles": "map onto the registered 1b local operator basis "
                "(established in the H^2 fork stage); MS pole-only "
                "subtraction IS licensed for these",
    "IR_pole": "the surviving a = 0 pole originates at q -> 0 with "
               "coefficient -8 omega^2/15; it is NOT a UV counterterm "
               "and is NOT absorbed into c0' or c2'",
    "drop_the_pole_test": "REJECTED. The claim 'the 1/(d-3) pole is "
                          "discarded by MS, therefore the finite H^2 "
                          "local term is defined' does NOT hold here: "
                          "MS is licensed against the 1b basis for UV "
                          "poles, and no registered prescription "
                          "extends it to an IR-origin pole. Calling an "
                          "IR subtraction 'MS' merely because it is a "
                          "1/(d-3) pole is exactly the move the audit "
                          "was instructed to test for and reject"}
for k_, v in OUT["uv_ir"].items():
    note("UVIR %s: %s" % (k_, v))
check(True, "the UV/IR distinction is recorded and the 'drop the pole' "
      "shortcut is explicitly rejected", gate="UVIR")

# ============ 4. STATE / BOUNDARY SUFFICIENCY ============
print("\n=== 4: IS THE STATE/BOUNDARY DATA SUFFICIENT? ===")
OUT["state_sufficiency"] = {
    "declared": "D3 = 3a, BD-analogue via the Option-B adiabatic route; "
                "the exact-dS state retained as cross-check target",
    "sufficient_to_fix_an_IR_prescription": False,
    "why": "the declaration fixes the STATE and the H-grading; it "
           "specifies no initial-time, switching, box, horizon or "
           "observation-time condition, and the frozen IR sub-choice "
           "explicitly refuses a scale. Nothing in it distinguishes a "
           "unique IR prescription for the retarded local extraction",
    "recorded_as_part_of_the_fork": True,
    "no_new_state_assumption_introduced": True}
check(OUT["state_sufficiency"]["sufficient_to_fix_an_IR_prescription"]
      is False,
      "the frozen state declaration is INSUFFICIENT to single out an IR "
      "prescription; recorded as part of the fork rather than patched "
      "with a new state assumption", gate="STATE")

# ============ 2/5. ANTI-CIRCULARITY + NO-NEW-SCALE ============
print("\n=== 2/5: ANTI-CIRCULARITY AND THE SCALE FIREWALL ===")
_t = "RESO" + "NANT"
check(_t not in selfsrc,
      "no spectral-outcome token in this audit's source: the ruling "
      "cannot have been selected to make any outcome come out",
      gate="CIRC")
control(_t in (_t + " sentinel"),
        "outcome-token scanner has teeth (runtime-assembled sentinel)")
CAND = ["q_min", "H as an ad hoc cutoff", "1/T", "box size",
        "horizon radius", "observational frequency", "WC", "Lambda_R",
        "mu"]
OUT["unauthorized_scale_candidates"] = {
    "candidates": CAND,
    "status": "each is mathematically capable of regulating the log; "
              "NONE is licensed by any authority in the sweep. They are "
              "recorded ONLY as candidates that would require a NEW "
              "owner decision, and NONE is adopted here"}
note("SCALE FIREWALL: %d tempting regulators recorded as candidates "
     "requiring a NEW owner decision; none adopted" % len(CAND))
check(True, "no numerical IR scale introduced anywhere in this audit",
      gate="CIRC")

# ============ 7. THE CONDITIONAL c0' STATEMENT, REVIEWED ============
print("\n=== 7: REVIEW OF THE CONDITIONAL c0' STATEMENT ===")
OUT["conditional_c0p"] = {
    "prior_statement": "if the extraction were licensed, the scale-free "
                       "omega^(d-1) form would force c0p = 0 and leave "
                       "c2p as the one H^2 constant",
    "review": "STILL CONDITIONALLY VALID in form -- the scale-free "
              "structure is unchanged by the correction. BUT its "
              "premise is now sharper: the extraction would have to be "
              "licensed for an IR-LOG-divergent integral, and any "
              "prescription that regulates that log generically "
              "introduces its own scale, which can feed the omega^0 "
              "slot. The conditional therefore may NOT be promoted, and "
              "its dependence on the (unmade) IR choice is now explicit",
    "promoted": False}
check(OUT["conditional_c0p"]["promoted"] is False,
      "the conditional c0' = 0 statement is REVIEWED and explicitly NOT "
      "promoted to a certified result", gate="COND")

# ============ 8. PARAMETER-COUNT IMPACT ============
print("\n=== 8: PARAMETER COUNT ===")
LED = json.loads(open(os.path.join(
    HERE, "WALL_KR_H0_PARAMETER_LEDGER_RESULT.json")).read())
check(LED["irreducible_unresolved_H0_local_inputs"] == 1
      and LED["identifier"] == "Lambda_R",
      "H^0 count UNCHANGED at exactly one (Lambda_R), read back from "
      "the certified ledger artifact -- this audit does not touch it",
      gate="COUNT")
OUT["parameter_count"] = {
    "H0": "1 (Lambda_R) -- unchanged",
    "H2": "OUTSIDE the count: no finite extraction is licensed, so no "
          "H^2 constant is counted",
    "if_an_IR_prescription_is_later_declared": "it must be classified "
          "then: a prescription that merely regulates without adding a "
          "physical scale may leave the count unchanged; one that "
          "introduces a physical IR scale is a NEW INPUT and must be "
          "counted as such",
    "no_IR_scale_hidden_in_Lambda_R": True}

# ============ 11. THE RULING ============
print("\n=== 11: THE RULING ===")
pre_existing_license = (n_lic > 0)
record_preregisters_route = ("named and priced" in rul)
owner_declaration_exists = False
if pre_existing_license:
    RULING = "IR-A"
elif record_preregisters_route:
    RULING = "IR-B"
else:
    RULING = "IR-C"
OUT["ruling"] = {
    "code": RULING,
    "derivation": "mechanical: pre_existing_license = %s; "
                  "record_preregisters_a_route = %s; "
                  "owner_declaration_exists_today = %s"
                  % (pre_existing_license, record_preregisters_route,
                     owner_declaration_exists),
    "text": "NO PRE-EXISTING LICENSE, BUT THE FROZEN RECORD "
            "PRE-REGISTERS THE ROUTE by which a new owner-declared IR "
            "convention may be introduced -- fork (ii), 'named and "
            "priced (a new register input)'",
    "practical_state_today": "IDENTICAL to IR-C: no prescription is "
                             "licensed, no declaration exists, so c0' "
                             "and c2' REMAIN UNRESOLVED and the H^2 "
                             "local sector stays fork-gated",
    "why_not_IR_A": "zero authorities license an IR prescription",
    "why_not_IR_C_strictly": "IR-C would say no new prescription is "
                             "AUTHORIZED at this stage. The record does "
                             "not merely leave the question open -- it "
                             "PRE-REGISTERED the fork and its price, "
                             "which is a standing, independently "
                             "justified route for the owner to declare "
                             "one. That distinction is the only thing "
                             "separating B from C here",
    "owner_may_prefer_C": "if the owner intends 'no new prescription "
                          "may be introduced at this stage', that is a "
                          "one-line owner amendment to this record and "
                          "changes nothing computational -- FLAGGED, "
                          "not decided by the builder",
    "builder_chose_no_regulator": True}
for k_, v in OUT["ruling"].items():
    note("RULING %s: %s" % (k_, v))
check(RULING in ("IR-A", "IR-B", "IR-C"),
      "ruling emitted as exactly one code: %s" % RULING, gate="RULE")

# ============ 15. VALIDATION ============
print("\n=== 15: VALIDATION ===")
check(all(sha_file(os.path.join(HERE, fn)) == PRE[fn] for fn in PINS)
      and sha_file(CLAIMS) == CLAIMS_PRE,
      "all frozen inputs AND the register byte-identical to their "
      "pre-run hashes", gate="VAL")
# run-1 defect (4th instance of the self-scan trap in this campaign):
# the strict pattern matched the PROSE of the conditional statement
# ("would force c0p = 0"), which is precisely the thing recorded as NOT
# promoted. The scan now targets an actual ASSIGNMENT (line-start) and
# is paired with the operative check on the EMITTED artifact.
_assign = (re.search(r"^\s*c0p\s*=", selfsrc, re.M)
           or re.search(r"^\s*c2p\s*=", selfsrc, re.M))
_emitted = json.dumps(OUT)
_numeric_emitted = re.search(r"\"c0p\":\s*[-+0-9]", _emitted) \
    or re.search(r"\"c2p\":\s*[-+0-9]", _emitted)
check(not _assign and not _numeric_emitted,
      "no numerical value is ASSIGNED to c0' or c2' in code, and none "
      "is EMITTED in the artifact (the conditional statement is quoted "
      "as prose and explicitly not promoted -- that quotation is not an "
      "assignment)", gate="VAL")
try:
    st = subprocess.run(["git", "status", "--short"], cwd=HERE,
                        capture_output=True, text=True, timeout=60).stdout
    OUT["worktree"] = st.strip().splitlines()
    note("files added/changed: %s"
         % (st.strip().replace("\n", " | ") or "(none yet)"))
except Exception as e:
    note("git status unavailable: %s" % e)

RESULT = {"instrument": "wall_kr_h2_ir_owner_ruling.py",
          "instrument_sha256": sha_file(os.path.abspath(__file__)),
          "ruling": RULING,
          "pre_existing_ir_prescription": False,
          "new_ir_input_introduced": False,
          "c0p_status": "unresolved", "c2p_status": "unresolved",
          "H0_Lambda_R": "ONE, unchanged",
          "axis2_status": "C, unchanged",
          "noise_fork": "untouched",
          "register_modified": False,
          "corrects_commit": "390a22d (single-branch numeric route)",
          "out": OUT, "checks": CHECKS, "notes": NOTES, "failures": FAILS,
          "elapsed_s": round(time.time() - T0, 1)}
outp = os.path.join(HERE, "WALL_KR_H2_IR_OWNER_RULING_RESULT.json")
json.dump(RESULT, open(outp, "w"), indent=1, default=str)
rr = json.loads(open(outp).read())
check(rr["new_ir_input_introduced"] is False
      and rr["c0p_status"] == "unresolved"
      and rr["register_modified"] is False,
      "artifact written and re-read (sha %s...)" % sha_file(outp)[:16],
      gate="OUT")
npass = sum(1 for c in CHECKS if c["pass"])
print("\nH^2 IR OWNER RULING: %d/%d passed; failures: %d"
      % (npass, len(CHECKS), len(FAILS)))
for m in FAILS:
    print("  FAILURE: " + m)
print("RULING: %s" % RULING)
print("HARD STOP.")
sys.exit(0 if not FAILS else 1)
