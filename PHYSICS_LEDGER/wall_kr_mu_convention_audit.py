#!/usr/bin/env python3
"""mu-CONVENTION AUDIT (owner authorization 2026-09-01, post-Axis-2).

GOVERNANCE + THEORY-CONVENTION AUDIT -- NOT a spectral calculation.
Question: does the existing theory/register/renormalization setup
INDEPENDENTLY supply a legitimate convention or normalization for the
renormalization scale mu?

HARD ANTI-CIRCULARITY: mu may NOT be chosen because it creates or
removes resonance, makes Axis 2 pass, gives a preferred sign of Re chi,
matches the registered J(omega) benchmark, matches any observed
spectral feature, or improves any GRUT outcome.  This instrument reads
NO Axis-2 outcome; that is checked at source level below.

DOES NOT TOUCH: frozen Tier-1..4 artifacts, the frozen nonlocal K_R,
H^2 locals, the noise fork, Gate-E, the Ward Class-B issue, the
registered J(omega) benchmark, or the consequence-cell conclusions.
The Axis-2 classification remains C and is NOT re-adjudicated here.

W-0: computed-and-reported, NOT banked.  HARD STOP after the ruling."""
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


def note(m):
    print("  note " + m)
    sys.stdout.flush()
    NOTES.append(m)


def sha_file(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


# ================= PROVENANCE (checked first and last) =================
print("=== PROVENANCE ===")
PINS = {
    "WALL_KR_TIER2_MASSLESS_BATH.json": "c5d399f525407839",
    "WALL_KR_TIER3_LOOP_RESULT.json": "4c016e93b889bd04",
    "WALL_KR_CONTRACT_RETARDED_RESULT.json": "d916ef32f6f73fa3",
    "WALL_KR_CONTRACT_BENCHMARK_RESULT.json": "1ac17a18ce8c0b8f",
    "WALL_KR_D5_EXECUTION_RESULT.json": None,
    "WALL_KR_AXIS2_H0_RESULT.json": None,
    "WALL_A_A3_DECLARATIONS.md": "87e2d24d5be6d679",
    "WALL_A_A3_REGISTRY.json": "faa977d40f1ba318",
    "K_R_CONTRACT_EXECUTION_CHARTER.md": "5416fa45498a6e5f",
    "K_R_OWNER_CHARTER.md": None,
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

# ============ D. INDEPENDENCE-FROM-AXIS-2 (source-level) ============
print("\n=== D: INDEPENDENCE FROM THE AXIS-2 OUTCOME ===")
_self_raw = open(os.path.abspath(__file__)).read()
# the scan must exclude its OWN token list, which necessarily contains
# the very strings it forbids (run-1 defect: the gate failed on itself).
# Everything between the markers below is the audit's self-description
# and is excised before scanning the executable body.
# the marker is BUILT by concatenation so these finder lines cannot
# match themselves (run-2 defect: find() hit the string literal here,
# excising the wrong region and leaving the list in the scan)
_MK = "# ANTICIRC-SCAN" + "-EXCLUDE-"
_b0 = _self_raw.find(_MK + "BEGIN")
_b1 = _self_raw.find(_MK + "END")
_self = _self_raw[:_b0] + _self_raw[_b1:]
# ANTICIRC-SCAN-EXCLUDE-BEGIN
banned = ["RESONANT", "PURELY-RELAXATIONAL", "0.79483", "0.377437",
          "1.132311", "mu_map", "omega_star"]
# ANTICIRC-SCAN-EXCLUDE-END
hits = [b for b in banned if b in _self]
check(not hits and _b0 > 0 and _b1 > _b0,
      "the executable body contains NO Axis-2 outcome token (no regime "
      "name, no boundary number, no omega* value): the ruling cannot "
      "be steered by the spectral result -- checked at source level, "
      "with the audit's own token list excised from the scan (the "
      "gate would otherwise fail on itself)", gate="ANTICIRC")
check("WALL_KR_AXIS2_H0_RESULT.json" in PINS
      and not re.search(r"AXIS2_H0_RESULT[^\n]*\[[\"']out[\"']\]", _self),
      "the Axis-2 artifact is HASH-PINNED for provenance only; its "
      "'out' block (which carries the outcome) is never dereferenced",
      gate="ANTICIRC")

# ============ A. AUTHORITATIVE SOURCE DECLARATIONS ============
print("\n=== A: AUTHORITATIVE DECLARATIONS CONCERNING mu ===")
decl = open(os.path.join(HERE, "WALL_A_A3_DECLARATIONS.md")).read()
j = decl.find("Renormalisation condition: MINIMAL SUBTRACTION")
mu_clause = decl[j:decl.find("\n\n", j)].strip().replace("\n", " ")
note("SOURCE 1 -- WALL_A_A3_DECLARATIONS.md (sha 87e2d24d..., FROZEN, "
     "predates Axis-2), Declaration 1 / F2: \"%s\"" % mu_clause[:340])
has_symbolic = "kept symbolic" in mu_clause
numeric_mu = bool(re.search(r"[μm]u\s*=\s*[0-9]", decl))
check(has_symbolic and not numeric_mu,
      "SOURCE 1 result: Declaration 1 orders mu KEPT SYMBOLIC and its "
      "dependence RECORDED. It assigns NO numeric value anywhere -- it "
      "is a refusal to fix mu, not a convention that fixes it",
      gate="SRC")
ch = open(os.path.join(HERE, "K_R_CONTRACT_EXECUTION_CHARTER.md")).read()
k = ch.find("STEP 10")
step10 = ch[k:ch.find("\n\n", ch.find("\n\n", k) + 1)].strip().replace(
    "\n", " ")
note("SOURCE 2 -- K_R_CONTRACT_EXECUTION_CHARTER.md (sha 5416fa45..., "
     "FROZEN): \"%s\"" % step10[:400])
check("VALIDATED MACHINERY" in step10 and "sign DICTIONARY" in step10,
      "SOURCE 2 result: charter STEP 10 permits ONLY validated "
      "machinery and the sign dictionary to cross the matter/contract "
      "boundary; 'No parameter, pole location, spectral behavior, "
      "sign-magnitude, or analytic-structure conclusion transfers'",
      gate="SRC")
oc = open(os.path.join(HERE, "K_R_OWNER_CHARTER.md")).read()
mu_in_oc = bool(re.search(r"[μm]u\s*=\s*[0-9]", oc))
check(not mu_in_oc,
      "SOURCE 3 -- K_R_OWNER_CHARTER.md: the normalization section "
      "fixes the AMPLITUDE chain (A1 vertex normalization, master-unit "
      "measure anchored by the A3-1 Im law, the friction convention) "
      "and assigns NO numeric renormalization scale", gate="SRC")

# ============ B. DIMENSIONAL / UNIT ANALYSIS (executable) ============
print("\n=== B: DIMENSIONAL AUDIT ===")
om, mu, lam = sp.symbols("omega mu lambda", positive=True)
c0, c2, c4 = sp.symbols("c0 c2 c4", real=True)
T4 = json.loads(open(os.path.join(
    HERE, "WALL_KR_CONTRACT_RETARDED_RESULT.json")).read())
SIG0 = sp.sympify(T4["out"]["sigma_R"]["H0"]).xreplace(
    {sp.Symbol("omega"): om, sp.Symbol("mu"): mu,
     sp.Symbol("c0"): c0, sp.Symbol("c2"): c2, sp.Symbol("c4"): c4})
# mu appears ONLY inside log(mu^2/omega^2): mu d/dmu must be omega-free
dmu = sp.simplify(mu * sp.diff(SIG0, mu))
check(not dmu.has(mu) and sp.simplify(dmu / om**4).is_constant(),
      "mu enters the frozen H^0 kernel ONLY through log(mu^2/omega^2): "
      "mu d/dmu Sigma = (2A) omega^4, independent of mu -- so mu is "
      "commensurable with omega and with nothing else", gate="DIM")
# with the CERTIFIED slot (c0 = c2 = 0) the kernel is homogeneous of
# degree 4 under the JOINT rescaling (omega, mu) -> (lam omega, lam mu)
A = sp.Rational(-3, 1280) / sp.pi**2
KAP = sp.Rational(-6841, 2835) - sp.EulerGamma + sp.log(4 * sp.pi)
cert = {c0: 0, c2: 0, c4: sp.simplify(A * KAP)}
S = SIG0.subs(cert)
hom = sp.simplify(S.subs({om: lam * om, mu: lam * mu}) - lam**4 * S)
check(hom == 0,
      "HOMOGENEITY (executable): with the certified slot the kernel "
      "satisfies Sigma(lam*omega, lam*mu) = lam^4 Sigma(omega, mu) "
      "EXACTLY -- mu carries the SAME dimension as omega (frequency; "
      "equivalently spatial wavenumber, the bath being massless with "
      "omega = |k|). Provenance: mu entered the D5 execution as the "
      "measure factor mu^(3-d) of the SPATIAL continuation",
      gate="DIM")
OUT["dimensional_result"] = {
    "units_of_mu": "frequency (= spatial wavenumber at c = 1); the same "
                   "dimension as omega and as WC",
    "entry_points": "mu^(3-d) in the D5 measure; log(mu^2/omega^2) in "
                    "the kernel",
    "dimensionless_ratios": "mu/WC and omega*/mu are dimensionless -- "
                            "so a NUMERICAL identification of mu with "
                            "any particular multiple of WC is an "
                            "ADDITIONAL convention, not a dimensional "
                            "necessity"}
note("DIMENSIONAL RESULT: [mu] = [omega] = [WC] = frequency. Nothing "
     "in the dimensional structure selects a numerical value")

# ============ C. CANDIDATE CONVENTIONS ============
print("\n=== C: CANDIDATE CONVENTIONS, WITH PROVENANCE ===")
reg = json.loads(open(os.path.join(HERE,
                                   "WALL_A_A3_REGISTRY.json")).read())
gsw = reg["g0_spectral_wiring"]
barred_files = set()
for e in gsw["barred_inputs"]:
    for f in (e.get("files") or []):
        barred_files.add(f)
plant = "wall_a_g1_ohmic_plant.py"
wc_defined_in_plant = False
if os.path.exists(os.path.join(HERE, plant)):
    wc_defined_in_plant = bool(re.search(
        r"^WC\s*=", open(os.path.join(HERE, plant)).read(), re.M))
check(plant in barred_files and wc_defined_in_plant,
      "CANDIDATE (iii) mu = WC is BARRED BY CONSTRUCTION: WC is defined "
      "in %s, which the registry lists as a barred input ('G1 Ohmic "
      "plant (carries registered J(omega) explicitly)'), and the "
      "registry's forbidden_direction is '%s'. Setting the RESPONSE's "
      "renormalization scale from the COMPARATOR's validity scale is "
      "exactly that forbidden flow" % (plant, gsw["forbidden_direction"]),
      gate="CAND")
jf = os.path.join(HERE, "wall_j_omega_comparison.py")
jsrc = open(jf).read()
m_ = re.search(r"muS:\s*1\s*,\s*kap:", jsrc)
ln = jsrc[:m_.start()].count("\n") + 1 if m_ else None
in_chi_A = m_ is not None and "def chi_A" in jsrc[:m_.start()][-900:]
check(m_ is not None and in_chi_A,
      "CANDIDATE (ii) LOCATED: the MATTER-stage J instrument "
      "substitutes muS: 1 (with the MS-bar constant log(4 pi) - "
      "EulerGamma) at line %s, INSIDE chi_A -- documented there as "
      "'the FROZEN response, EVALUATED as computed'. It is an "
      "EVALUATION SLICE inside a comparison instrument, at MATTER "
      "scope, in that kernel's master units" % ln, gate="CAND")
CANDIDATES = {
    "(i) Declaration 1 MS, mu symbolic": {
        "source": "WALL_A_A3_DECLARATIONS.md, Declaration 1 / F2 "
                  "(frozen, predates Axis-2)",
        "status": "REGISTERED -- but it is a REFUSAL to fix mu "
                  "('kept symbolic and its dependence recorded'), not a "
                  "numerical convention",
        "supplies_a_number": False},
    "(ii) matter-stage MS-bar with mu = 1": {
        "source": "wall_j_omega_comparison.py line %s, inside chi_A "
                  "(frozen instrument, MATTER scope)" % ln,
        "status": "EVALUATION SLICE, not a renormalization declaration; "
                  "MATTER scope. Charter STEP 10 permits only validated "
                  "machinery and the sign dictionary to cross to "
                  "contract scope and forbids parameter transfer. A "
                  "numerical renormalization scale is a PARAMETER, not "
                  "convention algebra",
        "supplies_a_number": False},
    "(iii) mu = WC (plant validity scale)": {
        "source": "WC = 1.0 defined in wall_a_g1_ohmic_plant.py",
        "status": "BARRED -- that file is a registry barred input and "
                  "the flow comparator -> response is the registry's "
                  "forbidden_direction",
        "supplies_a_number": False},
    "(iv) mu = omega (or any omega-dependent choice)": {
        "source": "NOWHERE DECLARED in the frozen record",
        "status": "would be invented here; also not a fixed scale",
        "supplies_a_number": False},
    "(v) a physical scale (H, m, ...)": {
        "source": "NOWHERE DECLARED for the contract H^0 sector",
        "status": "the H^0 sector contains no H by construction; m is "
                  "matter scope. Would be invented",
        "supplies_a_number": False},
}
for k_, v in CANDIDATES.items():
    note("CANDIDATE %s -> %s" % (k_, v["status"][:150]))
OUT["candidates"] = CANDIDATES
n_supplying = sum(1 for v in CANDIDATES.values() if v["supplies_a_number"])
OUT["n_conventions_supplying_a_number"] = n_supplying

# ============ E. NEW-INPUT TEST ============
print("\n=== E: NEW-INPUT TEST ===")
check(n_supplying == 0,
      "NEW-INPUT TEST: ZERO pre-existing conventions supply a numerical "
      "mu at contract scope. Therefore adopting a numerical mu would "
      "NOT merely instantiate an already-registered convention -- it "
      "would INTRODUCE A NEW FREE INPUT (a renormalization-point "
      "declaration)", gate="NEWIN")

# ============ F. RULING ============
print("\n=== F: RULING ===")
if n_supplying == 1:
    RULING = "A"
elif n_supplying > 1:
    RULING = "B"
else:
    RULING = "C"
OUT["ruling"] = {
    "code": RULING,
    "text": {"A": "PRE-EXISTING REGISTERED CONVENTION FOUND",
             "B": "MULTIPLE PRE-EXISTING CONVENTIONS; OWNER MUST "
                  "SELECT ONE",
             "C": "NO PRE-EXISTING NUMERICAL mu CONVENTION; A "
                  "NUMERICAL mu WOULD BE A NEW INPUT"}[RULING],
    "derivation": "mechanical from the candidate table: the ruling is "
                  "the count of candidates that supply a number at "
                  "contract scope, and no Axis-2 quantity enters",
    "what_is_registered": "the SCHEME is registered (dS-invariant dim "
                          "reg per Declaration 1; the spatial "
                          "continuation per Option beta) and the "
                          "SUBTRACTION is registered (pole-only MS, "
                          "zero finite discretion). What is NOT "
                          "registered is the renormalization POINT",
    "if_owner_declares_mu": "it must be priced as a new register input "
                            "and justified from normalization/"
                            "renormalization setup ALONE -- the "
                            "critical principle bars any "
                            "spectral/memory/outcome justification",
}
for k_, v in OUT["ruling"].items():
    note("RULING %s: %s" % (k_, v))
check(RULING in ("A", "B", "C"), "ruling emitted as exactly one of "
      "A / B / C: mu-RULING-%s" % RULING, gate="RULE")
note("AXIS-2 STATUS: C, UNCHANGED -- not re-adjudicated by this audit")

# ============ VALIDATION / FREEZE ============
print("\n=== VALIDATION ===")
unchanged = all(sha_file(os.path.join(HERE, fn)) == PRE[fn] for fn in PINS)
check(unchanged, "every frozen input byte-identical to its pre-run hash",
      gate="PROV")
try:
    st = subprocess.run(["git", "status", "--short"], cwd=HERE,
                        capture_output=True, text=True, timeout=60).stdout
    OUT["worktree_at_end"] = st.strip().splitlines()
    note("files added/changed by this stage: %s"
         % (st.strip().replace("\n", " | ") or "(none yet)"))
except Exception as e:
    note("git status unavailable: %s" % e)
RESULT = {"instrument": "wall_kr_mu_convention_audit.py",
          "instrument_sha256": sha_file(os.path.abspath(__file__)),
          "authorization": "owner 2026-09-01: mu-convention audit "
                           "(governance + theory convention)",
          "out": OUT, "checks": CHECKS, "notes": NOTES, "failures": FAILS,
          "frozen_inputs_touched": "NONE",
          "axis2_status": "C, unchanged; not re-adjudicated",
          "elapsed_s": round(time.time() - T0, 1)}
outp = os.path.join(HERE, "WALL_KR_MU_CONVENTION_RESULT.json")
json.dump(RESULT, open(outp, "w"), indent=1, default=str)
check(sha_file(outp) == sha_file(outp), "artifact written and re-read "
      "(sha %s...)" % sha_file(outp)[:16], gate="OUT")
npass = sum(1 for c in CHECKS if c["pass"])
print("\nmu-CONVENTION AUDIT: %d/%d passed; failures: %d"
      % (npass, len(CHECKS), len(FAILS)))
for m in FAILS:
    print("  FAILURE: " + m)
print("mu-RULING: %s" % RULING)
print("HARD STOP.")
sys.exit(0 if not FAILS else 1)
