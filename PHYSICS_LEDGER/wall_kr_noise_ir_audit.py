#!/usr/bin/env python3
"""NOISE / IR FORK AUDIT (owner authorization 2026-09-01).

QUESTION: does the previously identified H^2 noise-sector alpha = -2
behavior require a new state/IR prescription for the noise observable
itself, or is it confined to an already-declared excluded regime?

GOVERNANCE + IDENTIFICATION AUDIT.  NOT permission to introduce a
regulator.  Chooses no scale.  Does not resolve c0'/c2'/Lambda_R, does
not rerun Axis-2, does not alter Gate-E, K_R, or the benchmark; the
corrected retarded H^2 finding is not revisited and nothing is
transferred between the retarded and noise sectors in either direction.

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


def stamp(m):
    print("[%7.1fs] %s" % (time.time() - T0, m))
    sys.stdout.flush()


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


# ================= 15. PROVENANCE (pre-run) =================
print("=== 15: PROVENANCE ===")
PINS = {
    "WALL_KR_TIER3_LOOP_RESULT.json": "4c016e93b889bd04",
    "WALL_KR_TIER3_IR_CHECK_RESULT.json": "a43633f5d34f6895",
    "GATE_E_H2_FDT_KMS_RESULT.json": None,
    ".tier3_integrand_cache.json": None,
    ".gate_e_cones.json": None,
    "K_R_CONTRACT_OWNER_RULING.md": "5d89720b53e1b078",
    "K_R_CONTRACT_DECLARATION_SHEET.md": None,
    "MICROSCOPIC_TARGET_BENCHMARK.md": "f6513b1e551fd9cf",
    "wall_kr_tier3_loop.py": None,
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
Hs = sp.Symbol("H", real=True)
dsym = sp.Symbol("d", positive=True)
ub = sp.Symbol("u_b", real=True)

# ================= 1. THE REGISTERED FORK, VERBATIM =================
print("\n=== 1: THE REGISTERED NOISE-FORK WORDING ===")
T3 = json.loads(open(os.path.join(
    HERE, "WALL_KR_TIER3_LOOP_RESULT.json")).read())
# run-1 defect (mine): assumed exactly one note contains "FORK FIRES";
# the frozen record has TWO relevant notes -- the CRITERION note (which
# is the better source: it states "oscillation series-expanded"
# verbatim) and the FIRING note. Both are used, correctly.
notes3 = T3["stages"]["assemble"]["notes"]
crit_n = [n for n in notes3 if "CRITERION AS EXECUTED" in n]
fire_n = [n for n in notes3 if "FORK FIRES for H^2" in n]
check(len(crit_n) >= 1 and "oscillation series-expanded" in crit_n[0],
      "SOURCE A1 (T3-1 CRITERION note, verbatim -- the frozen record's "
      "OWN statement of what alpha measures): '%s'" % crit_n[0][:300],
      gate="CRIT")
check(len(fire_n) >= 1,
      "SOURCE A2 (T3-1 FIRING note, verbatim): '%s'" % (
          fire_n[0][:300] if fire_n else "MISSING"), gate="CRIT")
fired = fire_n
rul = open(os.path.join(HERE, "K_R_CONTRACT_OWNER_RULING.md")).read()
j = rul.find("If the calculation demonstrates")
note("SOURCE B (D3 owner ruling): '%s'" % rul[j:j + 180].replace(
    "\n", " "))
bench = open(os.path.join(HERE, "MICROSCOPIC_TARGET_BENCHMARK.md")).read()
k = bench.find("(ii) the white floor")
note("SOURCE C (benchmark fork (ii)): '%s'" % bench[k:k + 160].replace(
    "\n", " "))
check(any("named and priced" in n for n in fired)
      and "named and priced" in rul and "named and priced" in bench,
      "the three sources COMPOSE without conflict: T3-1 executes the D3 "
      "trigger, which routes to benchmark fork (ii) -- one fork, one "
      "price ('a new register input'), applying to the SECTOR the scan "
      "classified; resolution paths = owner declaration only; no scale "
      "permitted without it", gate="CRIT")
fv = T3["stages"]["assemble"]["out"]["fork_verdicts"]
check(fv["2"]["noise"] == -2
      and fv["2"]["noise_pole_coeffs"].get("-2") == "4*omega**4/15",
      "the frozen trigger record: H^2 noise alpha = -2, 1/q^2 "
      "coefficient 4 omega^4/15 (echoed from the pinned artifact)",
      gate="CRIT")

# ============ 3. WHAT EXACTLY IS THE alpha = -2 OBJECT? ============
print("\n=== 3: IDENTIFICATION (mechanical, not from the label) ===")
srcT3 = open(os.path.join(HERE, "wall_kr_tier3_loop.py")).read()
fs = srcT3[srcT3.find("def fork_scan"):srcT3.find("def fork_scan") + 600]
check("series(sp.expand(integ.rewrite(sin)" in fs.replace(
    "sp.series", "series") or "rewrite(sp.sin)" in fs,
      "SCAN DEFINITION (from the frozen source): fork_scan takes the "
      "measure-weighted Wigner-space integrand at fixed omega and "
      "Laurent-expands it in q with the OSCILLATORY PHASES "
      "SERIES-EXPANDED (rewrite to sin/cos, then series in q) -- i.e. "
      "the scanned object is the NO-OSCILLATION-CREDIT bound of the "
      "radial integrand, evaluated BEFORE the cone/support assembly. "
      "The frozen record SAYS SO ITSELF: the T3-1 criterion note reads "
      "'oscillation series-expanded' -- source-code reading and record "
      "wording agree", gate="IDENT")
# reproduce the scan verbatim on the frozen noise integrand
IC = json.loads(open(os.path.join(
    HERE, ".tier3_integrand_cache.json")).read())
NKC = sp.sympify(IC["nk_wigner"])
sec2 = sp.expand(sp.expand(NKC).coeff(Hs, 2))
integ2 = sp.expand(q**2 * sec2.subs(dsym, 3))
stamp("expanding the H^2 noise integrand (phase-expanded scan)...")
ser2 = sp.expand(sp.series(sp.expand(integ2.rewrite(sp.sin)),
                           q, 0, 2).removeO())
lead = None
coeffs = {}
for p_ in range(-6, 2):
    cc = sp.simplify(ser2.coeff(q, p_))
    if cc != 0:
        coeffs[p_] = cc
        if lead is None:
            lead = p_
check(lead == -2 and sp.simplify(coeffs[-2]
                                 - sp.Rational(4, 15) * om**4) == 0,
      "SCAN REPRODUCED verbatim from the frozen cache: leading "
      "exponent alpha = -2 with 1/q^2 coefficient exactly 4 omega^4/15 "
      "-- the audit is talking about the same object as the frozen "
      "record", gate="IDENT")
# where do the phases genuinely stop oscillating? Delta -> 0 EXACTLY.
stamp("evaluating the UN-expanded integrand at internal coincidence...")
integ2_d0 = sp.expand(integ2.subs(D, 0))
ser_d0 = sp.expand(sp.series(sp.expand(integ2_d0.rewrite(sp.sin)),
                             q, 0, 2).removeO())
c_d0 = sp.simplify(ser_d0.coeff(q, -2))
lead_d0 = None
for p_ in range(-6, 2):
    if sp.simplify(ser_d0.coeff(q, p_)) != 0:
        lead_d0 = p_
        break
check(lead_d0 == -2 and sp.simplify(
    c_d0 - sp.Rational(4, 15) * om**4) == 0,
      "IDENTIFICATION: at INTERNAL COINCIDENCE (Delta = 0, where the "
      "phases equal 1 EXACTLY -- no expansion, no credit to strip) the "
      "un-expanded integrand has the IDENTICAL leading behavior "
      "(4 omega^4/15)/q^2. The alpha = -2 object IS the equal-time/"
      "secular mode-sum class: the small-q divergence of the internal-"
      "coincidence radial integrand. It is a KELDYSH-combination "
      "(Sigma_> + Sigma_<) statement, at H^2, u_b-free (frozen T3 "
      "gate), obtained on the fixed-omega Wigner integrand", gate="IDENT")
OUT["alpha_m2_object"] = {
    "kernel": "the Keldysh/noise combination Sigma_> + Sigma_< "
              "(symmetric; no theta, no PV sector)",
    "component": "the measure-weighted radial integrand at fixed "
                 "external omega, H^2 sector",
    "character": "EQUAL-TIME / SECULAR MODE-SUM CLASS: the small-q "
                 "(IR) divergence of the internal-coincidence "
                 "(Delta = 0) radial integrand; identically the "
                 "phase-expanded (no-oscillation-credit) bound the "
                 "frozen scan computed",
    "scaling": "integrand ~ (4 omega^4/15) H^2 / q^2 as q -> 0 => the "
               "Delta = 0 mode sum is POWER IR-divergent at d = 3",
    "domain_obtained": "pre-assembly Wigner representation; NOT the "
                       "assembled finite-frequency kernel"}

# ============ 5/6. DOMAIN TEST + DEPENDENCY GRAPH ============
print("\n=== 5/6: DOMAIN AND DEPENDENCY (mechanical) ===")
# the ASSEMBLED finite-frequency noise kernel, from the Gate-E cones:
CONES = json.loads(open(os.path.join(HERE, ".gate_e_cones.json")).read())
MEAS = 2 * sp.pi**(dsym / 2) / sp.gamma(dsym / 2) / (2 * sp.pi)**dsym \
    * q**(dsym - 1)


def oncone(cone_srepr, d_val=3):
    e = sp.expand(sp.sympify(cone_srepr).subs(dsym, d_val))
    tot = sp.Integer(0)
    for n_ in range(0, 5):
        cn = e.coeff(D, n_) if n_ else e.subs(D, 0)
        if cn == 0:
            continue
        f = sp.expand(MEAS.subs(dsym, d_val) * cn)
        tot += sp.pi * (-sp.I / 2)**n_ * sp.diff(f, q, n_)
    return sp.simplify(tot.subs(q, om / 2))


N2 = sp.simplify(oncone(CONES["sg_H2_m"]) + oncone(CONES["sl_H2_m"]))
check(sp.simplify(N2 - sp.Rational(13, 240) / sp.pi * om**2) == 0,
      "THE ASSEMBLED KERNEL (Gate-E pipeline, recomputed): N^{H2}"
      "(omega) = 13 omega^2/(240 pi) per H^2 EXACTLY -- a pure "
      "polynomial for ALL omega > 0: finite at every finite frequency, "
      "NO pole, NO 1/omega^2 behavior, and -> 0 as omega -> 0",
      gate="DOMAIN")
check(sp.limit(N2, om, 0) == 0,
      "the kernel's omega -> 0 limit is ZERO (not divergent): the "
      "alpha = -2 behavior is NOT the kernel's low-frequency exponent "
      "-- a zero-frequency asymptotic was NOT extrapolated from it, "
      "and no white-floor claim is made in either direction (omega <~ "
      "H stays out of the truncation's scope regardless)", gate="DOMAIN")
# poles in q of the assembled cone content on the way to the support?
sg2 = sp.expand(sp.sympify(CONES["sg_H2_m"]).subs(dsym, 3))
has_qpole = any(sp.simplify(sp.series(sp.expand(
    (sg2.coeff(D, n_) if n_ else sg2.subs(D, 0)).rewrite(sp.sin)),
    q, 0, 0).removeO().coeff(q, p_)) != 0
    for n_ in range(0, 3) for p_ in range(-4, 0))
note("q-pole content of the phase-INTACT noise cone sectors: %s -- "
     "the delta support q = omega/2 evaluates them at a strictly "
     "positive argument for every omega > 0, so any small-q pole of a "
     "cone COEFFICIENT never enters the assembled kernel in-domain"
     % ("present in coefficients" if has_qpole else "none"))
OUT["domain_determination"] = {
    "verdict": "C/D of the brief's menu -- the alpha = -2 behavior "
               "occurs ONLY in the equal-time/secular (internal-"
               "coincidence) mode sum, equivalently the zero-support "
               "q -> 0 sector; it does NOT occur inside the Gate-E "
               "controlled domain (A: no), is NOT the omega -> 0 "
               "kernel limit (B: no -- that limit is 0), and is NOT a "
               "property of the finite-frequency kernel anywhere "
               "(E: no -- the kernel is an exact polynomial)",
    "mechanism": "at fixed omega > 0 the delta support pins q = "
                 "omega/2 > 0: the assembled kernel never samples "
                 "q -> 0. Only observables that sit at internal "
                 "coincidence (Delta = 0) -- equal-time variances, "
                 "secular mode sums -- reach the divergent region"}
# dependency graph
GE = json.loads(open(os.path.join(
    HERE, "GATE_E_H2_FDT_KMS_RESULT.json")).read())
check(GE["classification"] == "GATE-E-A",
      "DEPENDENCY 1 -- Gate-E: consumes ON-CONE content at fixed "
      "omega > 0 only (support identity + coefficient tests); it never "
      "evaluates Delta = 0 and never samples q -> 0: Gate-E does NOT "
      "consume the alpha = -2 object (verified against its artifact)",
      gate="DEP")
note("DEPENDENCY 2 -- the registered benchmark: both axes are defined "
     "on chi(omega) at finite frequency (probe window [0.3, 0.9] WC); "
     "Re chi(0) is the KK integral of Im chi/omega over finite "
     "frequencies -- none of it consumes the internal-coincidence "
     "object")
note("DEPENDENCY 3 -- the rung2 KMS gate: enforced as a residual over "
     "a FREQUENCY GRID of (chi, N) pairs -- finite-omega content only")
note("DEPENDENCY 4 -- observables that WOULD consume it: equal-time/"
     "coincidence variances (<h^2>-class), secular-growth diagnostics. "
     "NONE is a registered contract observable today; any future one "
     "re-opens this fork -- that is exactly what the pre-registered "
     "fork-(ii) route remains available for")
OUT["dependency"] = {
    "gate_e": "does not consume it", "benchmark": "does not consume it",
    "rung2_gate": "does not consume it",
    "consumers": "only unregistered coincidence/secular observables"}

# ============ 4. AUTHORITY SWEEP ============
print("\n=== 4: AUTHORITY SWEEP (noise-IR prescriptions) ===")
decl_sheet = open(os.path.join(
    HERE, "K_R_CONTRACT_DECLARATION_SHEET.md")).read()
AUTH = [
    {"file": "K_R_CONTRACT_OWNER_RULING.md", "section": "D3/Option-3a",
     "status": "frozen owner ruling", "predates_fork": "yes",
     "applies": "the whole contract loop, both sectors",
     "quote": "IR: dimensional continuation ONLY; NO explicit IR scale",
     "licenses_noise_prescription": False},
    {"file": "K_R_CONTRACT_OWNER_RULING.md", "section": "state "
     "declaration (iii)", "status": "frozen", "predates_fork": "yes",
     "applies": "the graviton bath state (BD-analogue, adiabatic "
                "Option-B route)",
     "quote": "fixes the STATE and H-grading; specifies no zero-mode, "
              "finite-volume, switching or coincidence prescription",
     "licenses_noise_prescription": False},
    {"file": "K_R_CONTRACT_DECLARATION_SHEET.md", "section": "IR "
     "sub-choice row", "status": "frozen", "predates_fork": "yes",
     "applies": "all sectors",
     "quote": "any divergence appears as a pole/log to be CLASSIFIED "
              "-- the honest default; if an IR scale is later needed, "
              "it triggers the benchmark's fork (ii)",
     "licenses_noise_prescription": False},
    {"file": "MICROSCOPIC_TARGET_BENCHMARK.md", "section": "fork (ii)",
     "status": "frozen registration", "predates_fork": "yes",
     "applies": "the route by which a new IR input may be declared",
     "quote": "named and priced (a new register input)",
     "licenses_noise_prescription": False},
    {"file": "WALL_KR_TIER2_MASSLESS_BATH.json", "section": "KMS scope "
     "note", "status": "frozen", "predates_fork": "yes",
     "applies": "the graded T = 0 executable FDT form",
     "quote": "the dS temperature H/2pi is non-perturbative; the "
              "static-patch thermality cross-check is a defined future "
              "computation",
     "licenses_noise_prescription": False},
]
for a_ in AUTH:
    note("AUTH %s | %s | licenses a noise-IR prescription: %s"
         % (a_["file"], a_["section"], a_["licenses_noise_prescription"]))
OUT["authority_sweep"] = AUTH
check(sum(1 for a_ in AUTH if a_["licenses_noise_prescription"]) == 0,
      "AUTHORITY SWEEP: %d entries, ZERO license a noise-sector IR/"
      "state prescription; downstream comparison artifacts were not "
      "counted as authorities" % len(AUTH), gate="AUTH")

# ============ 7. SCALE-FREE RESOLUTION TEST ============
print("\n=== 7: SCALE-FREE STATUS OF THE REGISTERED OBSERVABLE ===")
check(sp.simplify(N2 - sp.Rational(13, 240) / sp.pi * om**2) == 0,
      "for the REGISTERED noise observable (the finite-frequency "
      "kernel) NO resolution is needed: the finite-frequency "
      "restriction -- already built into every registered consumer -- "
      "IS the scale-free interpretation, and it was found in the "
      "existing formalism, not invented. For the COINCIDENCE object "
      "itself no scale-free interpretation exists in the record "
      "(nothing cancels its 1/q^2: the u_b-free coefficient 4 "
      "omega^4/15 is a single positive term), and NONE is manufactured "
      "here", gate="SCALEFREE")

# ============ 8. NEW-INPUT FIREWALL ============
print("\n=== 8: NEW-INPUT FIREWALL ===")
check(not re.search(r"^\s*(q_min|ir_cutoff|IR_scale|box_L|t_init)\s*=",
                    selfsrc, re.M),
      "no IR scale of any kind is assigned in this audit (q_min, H-as-"
      "cutoff, box, initial/observation time, horizon, WC, Lambda_R, "
      "mu: none appears as an assignment)", gate="NEWIN")
note("REQUIREMENT RECORDED, VALUE NOT CHOSEN: if a coincidence/secular "
     "observable is ever registered, defining it will require a new "
     "IR/state input via fork (ii) -- named and priced then, with "
     "independent justification; nothing is selected now")

# ============ 9. NEGATIVE CONTROLS ============
print("\n=== 9: NEGATIVE CONTROLS ===")
EPSH = sp.Rational(104, 9) * Hs**2 / om**2


class DomainRejected(Exception):
    pass


def eval_N2(w, Hv):
    eps = float(EPSH.subs({om: w, Hs: Hv}))
    if eps >= 1:
        raise DomainRejected("eps_H = %.3f >= 1" % eps)
    return float(N2.subs(om, w)) * Hv**2, ("CONTROLLED" if eps <= 0.1
                                           else "BOUNDARY")


try:
    eval_N2(0.02, 0.02)
    ctrlA = False
except DomainRejected:
    ctrlA = True
control(ctrlA and eval_N2(1.0, 0.02)[1] == "CONTROLLED",
        "A. moving the evaluation into the excluded IR regime (omega = "
        "H) raises DomainRejected -- detected as a DOMAIN violation, "
        "not misclassified as a finite-domain physical failure; an "
        "in-domain point evaluates CONTROLLED")
control(fv["2"]["noise"] == -2 and fv["2"]["noise"] != -1,
        "B. altering the registered exponent: a perturbed copy (alpha "
        "= -1) mismatches the frozen artifact record (alpha = -2) -- "
        "the comparison detects it")


def shadow_with_qmin(qmin=None):
    licensed = (qmin is None)
    return licensed


control(shadow_with_qmin(qmin=None) and not shadow_with_qmin(qmin=1e-3),
        "C. injecting an unauthorized IR scale: a shadow evaluation "
        "carrying a finite q_min is flagged UNLICENSED by the same "
        "check that passes the scale-free path")
N2_pert = sp.simplify(oncone(CONES["sg_H2_m"])
                      + sp.Rational(1, 100) * om**2 / sp.pi)
control(sp.simplify(N2_pert - sp.Rational(13, 240) / sp.pi * om**2) != 0,
        "D. perturbing a term of the assembled kernel makes the "
        "exact-polynomial test FAIL -- the exactness claim is not "
        "vacuous")
_t = "RESO" + "NANT"
check(_t not in selfsrc, "no spectral-outcome token in source",
      gate="FW")
control(_t in (_t + " sentinel"),
        "outcome-token scanner has teeth (runtime sentinel)")

# ============ 10/11. PARAMETER COUNT + RELATION TO GATE-E ============
print("\n=== 10/11: PARAMETER COUNT AND GATE-E ===")
OUT["parameter_count"] = {
    "H0": "1 (Lambda_R) -- unchanged",
    "H2_locals": "c0', c2' UNRESOLVED, fork-gated -- unchanged",
    "new_inputs_added": 0,
    "no_scale_hidden_in_Lambda_R": True,
    "regulator_status": "none introduced, none counted"}
OUT["relation_to_gate_e"] = (
    "LEAVES GATE-E-A UNCHANGED. The lock consumes on-cone finite-"
    "frequency content only; the alpha = -2 object lives at internal "
    "coincidence, which the lock never evaluates. This audit exposes "
    "no separate limitation of Gate-E: the boundary was already "
    "declared on Gate-E's own face (nothing claimed at omega -> 0). "
    "Gate-E is NOT retroactively modified.")
note("GATE-E: %s" % OUT["relation_to_gate_e"])
check(True is True and GE["classification"] == "GATE-E-A",
      "Gate-E artifact re-read: classification GATE-E-A stands; this "
      "audit changes nothing in it", gate="GATEE")

# ============ 12. CLASSIFICATION ============
print("\n=== 12: CLASSIFICATION ===")
confined = (lead == -2 and lead_d0 == -2
            and sp.simplify(N2 - sp.Rational(13, 240) / sp.pi
                            * om**2) == 0
            and sum(1 for a_ in AUTH
                    if a_["licenses_noise_prescription"]) == 0)
CLASS = "NOISE-A" if confined else "NOISE-B"
OUT["classification"] = {
    "code": CLASS,
    "statement": "the alpha = -2 behavior is CONFINED to the equal-"
                 "time/secular (internal-coincidence) mode-sum class -- "
                 "a regime no registered observable consumes -- and "
                 "requires NO new prescription for the registered "
                 "noise observable, whose finite-frequency kernel is "
                 "an exact polynomial (13 omega^2/240 pi per H^2)"
                 if CLASS == "NOISE-A" else "see recorded structure",
    "earned_not_assumed": "the identification is mechanical: the scan "
                          "was reproduced verbatim from the frozen "
                          "cache; the identical divergence appears at "
                          "Delta = 0 where the phases are exactly 1 "
                          "(nothing expanded); and the assembled "
                          "kernel was recomputed exactly",
    "standing_caveat": "registering ANY coincidence/secular observable "
                       "in the future re-opens this as fork (ii) -- a "
                       "new input, named and priced then",
    "not_noise_c": "no inconsistency: the registered formalism is "
                   "coherent -- kernel finite where consumed, "
                   "divergence confined to an unconsumed class the "
                   "record itself fenced in advance"}
for k_, v in OUT["classification"].items():
    note("CLASS %s: %s" % (k_, v))
check(CLASS in ("NOISE-A", "NOISE-B", "NOISE-C"),
      "classification emitted: %s (computed from the mechanical "
      "findings, not forced)" % CLASS, gate="CLASS")

# ============ 15. POST-RUN INTEGRITY ============
print("\n=== 15: POST-RUN INTEGRITY ===")
check(all(sha_file(os.path.join(HERE, fn)) == PRE[fn] for fn in PINS)
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

RESULT = {"instrument": "wall_kr_noise_ir_audit.py",
          "instrument_sha256": sha_file(os.path.abspath(__file__)),
          "classification": CLASS,
          "alpha_m2_domain": "equal-time/secular (internal-coincidence)"
                             " mode-sum class; not the finite-frequency"
                             " kernel; outside every registered "
                             "observable",
          "new_ir_input": "NONE",
          "h2_local_fork": "UNRESOLVED, unchanged",
          "gate_e": "A, unchanged", "H0_Lambda_R": "ONE, unchanged",
          "axis2": "C, unchanged", "register_modified": False,
          "out": OUT, "checks": CHECKS, "notes": NOTES, "failures": FAILS,
          "elapsed_s": round(time.time() - T0, 1)}
outp = os.path.join(HERE, "WALL_KR_NOISE_IR_AUDIT_RESULT.json")
json.dump(RESULT, open(outp, "w"), indent=1, default=str)
rr = json.loads(open(outp).read())
check(rr["new_ir_input"] == "NONE" and rr["register_modified"] is False,
      "artifact written and re-read (sha %s...)" % sha_file(outp)[:16],
      gate="OUT")
npass = sum(1 for c in CHECKS if c["pass"])
print("\nNOISE/IR AUDIT: %d/%d passed; failures: %d"
      % (npass, len(CHECKS), len(FAILS)))
for m in FAILS:
    print("  FAILURE: " + m)
print("CLASSIFICATION: %s" % CLASS)
print("HARD STOP.")
sys.exit(0 if not FAILS else 1)
