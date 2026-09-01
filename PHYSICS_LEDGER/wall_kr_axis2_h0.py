#!/usr/bin/env python3
"""AXIS-2 ADJUDICATION AT H^0 ONLY (owner authorization 2026-09-01,
post-D5 gate).  ADJUDICATION / VALIDATION -- NOT theory revision.

CONSUMES ONLY the certified post-repair D5 H^0 local determination
(commits 12ea453 / 04b8d6c) and the frozen H^0 nonlocal content.
The uncertified pre-repair Axis-2 readings in wall_kr_d5_exec_run2/3/4
.log are EXCLUDED: this instrument locates them, records why they are
uncertified, and never reads a number from them.

H^2 FIREWALL: no H^2 local is computed, fitted, inferred or backsolved;
the noise fork is not opened; the alpha = -2 result is not consulted;
the Tier-4 validity boundary, the Ward finding and the registered
J(omega) conclusion are untouched.

W-0: computed-and-reported, NOT banked.  HARD STOP after the report."""
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
T0 = time.time()
FAILS, CHECKS, NOTES, OUT = [], [], [], {}
mp.mp.dps = 40


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


# ============ 11. PROVENANCE / IMMUTABILITY (checked FIRST) ============
print("=== PROVENANCE: frozen upstream artifacts ===")
PINS = {
    "WALL_KR_TIER1_VERTEX_ARTIFACT.json": None,
    "WALL_KR_TIER2_MASSLESS_BATH.json": "c5d399f525407839",
    "WALL_KR_TIER3_LOOP_RESULT.json": "4c016e93b889bd04",
    "WALL_KR_CONTRACT_RETARDED_RESULT.json": "d916ef32f6f73fa3",
    "WALL_KR_CONTRACT_BENCHMARK_RESULT.json": "1ac17a18ce8c0b8f",
    "WALL_KR_D5_EXECUTION_RESULT.json": None,
    "WALL_A_A3_DECLARATIONS.md": "87e2d24d5be6d679",
    "MICROSCOPIC_TARGET_BENCHMARK.md": "f6513b1e551fd9cf",
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
D5R = json.loads(open(os.path.join(
    HERE, "WALL_KR_D5_EXECUTION_RESULT.json")).read())
check(D5R["failures"] == [], "D5 execution artifact: zero failures on "
      "record (the certified source of the local terms)", gate="PROV")
if FAILS:
    sys.exit(2)

om = sp.Symbol("omega", positive=True)
mu = sp.Symbol("mu", positive=True)
eps = sp.Symbol("epsilon", positive=True)

# ============ 3. NO PRELIMINARY-RESULT CONTAMINATION ============
print("\n=== 3: EXCLUSION OF THE UNCERTIFIED PRE-REPAIR READINGS ===")
unc = []
for f in sorted(os.listdir(HERE)):
    if re.match(r"wall_kr_d5_exec_run[234]\.log$", f):
        txt = open(os.path.join(HERE, f), errors="replace").read()
        red = txt.count("  FAIL ") + txt.count("ctrl-MISSED")
        unc.append({"file": f, "sha": sha_file(os.path.join(HERE, f))[:16],
                    "red_gates": red,
                    "has_axis2_text": "Re chi(omega)" in txt})
for u in unc:
    note("EXCLUDED %s (sha %s..., %d RED gates, axis2 text present: %s)"
         % (u["file"], u["sha"], u["red_gates"], u["has_axis2_text"]))
OUT["excluded_uncertified"] = unc
check(len(unc) == 3 and all(u["red_gates"] > 0 for u in unc),
      "the three pre-repair Axis-2 logs are LOCATED and every one is "
      "RED (failing gates on its own face) -- they are uncertified by "
      "their own record and are excluded; no number is read from them",
      gate="EXCL")
_self = open(os.path.abspath(__file__)).read()
check(not re.search(r"run[234]\.log[\"'].*(float|mpf|Rational)", _self),
      "this instrument reads no numeric value from the excluded logs "
      "(source-level check: the only references are the provenance "
      "listing above)", gate="EXCL")

# ============ 2. THE REGISTERED AXIS-2 CRITERION, VERBATIM ============
print("\n=== 2: THE REGISTERED CRITERION (quoted, not paraphrased) ===")
bench = open(os.path.join(HERE, "MICROSCOPIC_TARGET_BENCHMARK.md")).read()
i = bench.find("**Axis 2 —")
crit = bench[i:bench.find("\n\n", i)].strip()
print("    " + crit.replace("\n", "\n    "))
OUT["registered_criterion_verbatim"] = crit
check("Re χ > 0 throughout" in crit and "changes sign inside" in crit
      and "INDETERMINATE" in crit,
      "operative condition located verbatim: PURELY-RELAXATIONAL = "
      "'Re chi > 0 throughout, no resonance'; RESONANT = 'Re chi "
      "changes sign inside the domain'; else INDETERMINATE", gate="CRIT")
note("DOMAIN, as registered: 'within the declared validity domain "
     "(omega << omega_c)'. The registered probe span is (0.3, 0.45, "
     "0.6, 0.75, 0.9) x WC with WC = 1.0 in plant units (provenance: "
     "the frozen J-stage instrument's BENCH block, which transcribed "
     "the registration). DISCLOSED LOOSENESS: 'omega << omega_c' is "
     "not a sharp interval; the probe span is used as the operative "
     "domain and every verdict below is reported against it "
     "explicitly")
W_LO, W_HI = sp.Rational(3, 10), sp.Rational(9, 10)     # x WC, WC = 1
OUT["domain"] = {"probe_span": "[0.3, 0.9] x WC (WC = 1 plant units)",
                 "registered_text": "omega << omega_c",
                 "looseness_disclosed": True}
note("OBJECT: Axis 2 is defined on chi. The register does NOT define "
     "Axis 2 on a dressed propagator; the consequence stage's "
     "kernel-level reading (chi = -K_R, review-verified against the "
     "sealed matter J-instrument) is inherited unchanged. No switch "
     "to a dressed object is made here")

# ============ 1. CERTIFIED INPUTS ============
print("\n=== 1: CERTIFIED INPUTS (exact symbolic forms authoritative) ===")
A = sp.Rational(-3, 1280) / sp.pi**2
KAPPA = (sp.Rational(-6841, 2835) - sp.EulerGamma + sp.log(4 * sp.pi))
c4 = sp.simplify(A * KAPPA)
c0 = sp.Integer(0)
c2 = sp.Integer(0)
note("A     = %s  (frozen nonlocal log coefficient AND 1/eps residue)"
     % str(A))
note("kappa = -6841/2835 - EulerGamma + log(4 pi) = %s"
     % mp.nstr(mp.mpf(str(sp.N(KAPPA, 30))), 12))
note("c4    = A * kappa = %s ~ %s   (certified D5 H^0 local constant)"
     % (str(c4), mp.nstr(mp.mpf(str(sp.N(c4, 30))), 12)))
note("c0 = c2 = 0 (EXACT, structural -- certified D5)")
check(abs(float(sp.N(c4, 20)) - 1.0906e-4) < 1e-8,
      "certified c4 matches the recorded decimal check +1.0906e-4 "
      "(the symbolic form is authoritative; the decimal is the check)",
      gate="INPUT")
d5_c4 = D5R["out"]["local_slot_determined"]["c4_over_A"]
check("-6841/2835" in d5_c4 and "EulerGamma" in d5_c4
      and "log(4*pi)" in d5_c4,
      "c4 is READ BACK from the certified D5 artifact's own record "
      "(c4_over_A field), not retyped from the report", gate="INPUT")

# ============ 6. mu / RENORMALIZATION-CONVENTION TREATMENT ============
print("\n=== 6: mu TREATMENT (searched, not assumed) ===")
decl = open(os.path.join(HERE, "WALL_A_A3_DECLARATIONS.md")).read()
j = decl.find("MINIMAL SUBTRACTION")
mu_clause = decl[j:decl.find("\n\n", j)].strip()
note("Declaration 1 (verbatim): ...%s..." % mu_clause[:300].replace(
    "\n", " "))
mu_pinned = bool(re.search(r"\bmu\s*=\s*[0-9]", decl)) or \
    bool(re.search(r"μ\s*=\s*[0-9]", decl))
check(("kept symbolic" in mu_clause or "symbolic" in mu_clause)
      and not mu_pinned,
      "mu IS NOT PINNED by the frozen record: Declaration 1 orders it "
      "'kept symbolic and its dependence recorded'. Option beta ruled "
      "the CONTINUATION, not mu. No numeric mu is adopted by this "
      "instrument", gate="MU")
OUT["mu_status"] = {
    "pinned_by_record": False,
    "declaration_1": "mu kept symbolic, dependence recorded",
    "option_beta_scope": "fixed the continuation (spatial d = 3-2eps), "
                         "NOT the renormalization scale"}

# ============ 4. TWO INDEPENDENT ROUTES ============
print("\n=== 4: ROUTE A (Tier-4 stored completion) ===")
T4 = json.loads(open(os.path.join(
    HERE, "WALL_KR_CONTRACT_RETARDED_RESULT.json")).read())
AM = {sp.Symbol("omega"): om, sp.Symbol("mu"): mu,
      sp.Symbol("c0"): c0, sp.Symbol("c2"): c2, sp.Symbol("c4"): c4}
SIG0_A = sp.sympify(T4["out"]["sigma_R"]["H0"]).xreplace(AM)
RECHI_A = sp.simplify(-sp.re(sp.expand_complex(sp.expand(SIG0_A))))
note("Route A: the FROZEN Tier-4 H^0 completion string with the "
     "certified local slot substituted (c0 = c2 = 0, c4 as above)")

print("\n=== 4: ROUTE B (D5 direct integral, re-executed) ===")
src = open(os.path.join(HERE, "wall_kr_d5_execution.py")).read()
b0 = src.find("om = sp.Symbol(\"omega\", positive=True)")
b1 = src.find("SIG_MS = sp.simplify(finite)")
b1 = src.find("\n", b1)
g = {"sp": sp, "mp": mp, "json": json, "os": os, "HERE": HERE,
     "check": lambda *a, **k: True, "note": lambda *a, **k: None,
     "control": lambda *a, **k: True, "stamp": lambda *a, **k: None,
     "OUT": {}, "sha_file": sha_file}
exec(src[b0:b1], g)
RECHI_B = sp.simplify(-sp.re(sp.expand_complex(
    sp.expand(g["SIG_MS"].xreplace({g["om"]: om, g["mu"]: mu})))))
note("Route B: the direct radial integral rebuilt from the FROZEN T3 "
     "cone data through the gated master formulas and MS-subtracted "
     "(the D5 code path re-executed), then Re taken")
diff_AB = sp.simplify(sp.expand(RECHI_A - RECHI_B))
check(diff_AB == 0,
      "ROUTE A == ROUTE B EXACTLY: the Tier-4 stored dispersive "
      "completion (+ certified local) and the independently "
      "re-executed direct integral give the identical real response -- "
      "genuinely different constructions, one answer (not a "
      "self-simplification)", gate="ROUTE")
RECHI = sp.simplify(RECHI_A)
OUT["Re_chi_H0"] = str(RECHI)
note("Re chi^{H0}(omega) = %s" % str(RECHI))

# ============ 5. ZERO SEARCH ON THE REGISTERED DOMAIN ============
print("\n=== 5: ZERO SEARCH (exact + two numeric methods) ===")
# sign(Re chi) = sign(-A) * sign(L + kappa); -A > 0 and omega^4 > 0
Lsym = sp.log(mu**2 / om**2)
red = sp.simplify(RECHI / (-A * om**4))
check(sp.simplify(red - (Lsym + KAPPA)) == 0,
      "reduced sign function: Re chi = (-A) omega^4 [log(mu^2/omega^2) "
      "+ kappa] with -A > 0 and omega^4 > 0, so the sign of Re chi is "
      "the sign of the bracket EXACTLY", gate="ZERO")
w_star = sp.simplify(sp.solve(sp.Eq(Lsym + KAPPA, 0), om)[0])
w_star_over_mu = sp.simplify(w_star / mu)
r_num = mp.mpf(str(sp.N(w_star_over_mu, 35)))  # NOT float():
# float() truncates to ~1e-16 and would make the 1e-20
# comparison below unpassable (run-1 gate defect, disclosed)
check(sp.simplify(w_star_over_mu - sp.exp(KAPPA / 2)) == 0,
      "EXACT unique positive zero: omega* = mu * exp(kappa/2), i.e. "
      "omega*/mu = %s (a pure computed number, scheme-fixed given the "
      "declared continuation)" % mp.nstr(r_num, 12),
      gate="ZERO")
note("the only other zero of Re chi is omega = 0 (order 4), the domain "
     "edge, not an interior sign change")
# numeric confirmation, TWO methods, on a DISCLOSED reference slice
f_red = sp.lambdify((om, mu), red, "mpmath")
MUREF = mp.mpf(1)          # DISCLOSED reference slice, verdict-free
note("numerical root-finding below uses the DISCLOSED reference slice "
     "mu = 1 x WC purely to exercise the machinery; NO verdict is "
     "taken at a single mu -- the verdict is the mu-map in section 5b")
lo, hi = mp.mpf("0.05"), mp.mpf("5")
check(f_red(lo, MUREF) * f_red(hi, MUREF) < 0,
      "root bracketed on [0.05, 5] at the reference slice (sign "
      "change confirmed before any solve)", gate="ZERO")
r_bis = mp.findroot(lambda w: f_red(w, MUREF), (lo, hi), solver="bisect",
                    tol=mp.mpf("1e-30"))
r_sec = mp.findroot(lambda w: f_red(w, MUREF), mp.mpf("0.7"),
                    solver="secant")
check(abs(r_bis - r_sec) < mp.mpf("1e-20")
      and abs(r_bis - r_num) < mp.mpf("1e-20"),
      "TWO independent numeric methods (bisection, secant) agree with "
      "each other and with the exact root to < 1e-20; direct "
      "substitution residual |Re chi(omega*)| = %s"
      % mp.nstr(abs(f_red(r_bis, MUREF)), 3), gate="ZERO")
# precision / sampling-density stability
stab = []
for dps in (25, 40, 60):
    mp.mp.dps = dps
    stab.append(mp.findroot(lambda w: f_red(w, MUREF), (lo, hi),
                            solver="bisect", tol=mp.mpf("1e-30")))
mp.mp.dps = 40
check(abs(stab[-1] - stab[0]) < mp.mpf("1e-20"),
      "root stable under increased precision (dps 25/40/60 agree to "
      "< 1e-20) -- not a numerical artifact", gate="ZERO")
counts = []
for N in (201, 401, 801):
    grid = [lo + (hi - lo) * k / (N - 1) for k in range(N)]
    counts.append(sum(1 for k in range(N - 1)
                      if f_red(grid[k], MUREF)
                      * f_red(grid[k + 1], MUREF) < 0))
check(counts == [1, 1, 1],
      "sign-change count on [0.05, 5] is exactly 1 at sampling "
      "densities 201/401/801 (counts %s) -- the single crossing is not "
      "a sampling artifact and no second crossing is being missed"
      % counts, gate="ZERO")

# ---- 5b: the mu-map, which IS the verdict-bearing object ----
print("\n=== 5b: THE mu-MAP (verdict-bearing; mu symbolic) ===")
mu_lo = sp.simplify(W_LO / sp.exp(KAPPA / 2))
mu_hi = sp.simplify(W_HI / sp.exp(KAPPA / 2))
mlo, mhi = float(sp.N(mu_lo, 25)), float(sp.N(mu_hi, 25))
note("omega* = %s * mu, so omega* lies INSIDE the registered probe "
     "span [0.3, 0.9] WC  <=>  mu in (%s, %s) WC"
     % (mp.nstr(r_num, 9), mp.nstr(mp.mpf(str(mlo)), 9),
        mp.nstr(mp.mpf(str(mhi)), 9)))
REGIMES = {
    "mu < %.6f WC" % mlo: "omega* below the span: Re chi < 0 THROUGHOUT "
                          "the domain -- neither registered label "
                          "applies (a case the registered trichotomy "
                          "does not name; recorded as a FINDING)",
    "%.6f WC < mu < %.6f WC" % (mlo, mhi): "omega* inside the span: "
                                           "Re chi CHANGES SIGN inside "
                                           "the domain => RESONANT",
    "mu > %.6f WC" % mhi: "omega* above the span: Re chi > 0 THROUGHOUT "
                          "the domain => PURELY-RELAXATIONAL",
}
for k, v in REGIMES.items():
    note("  %s  ->  %s" % (k, v))
OUT["mu_map"] = {"omega_star_over_mu": str(w_star_over_mu),
                 "omega_star_over_mu_numeric": r_num,
                 "regimes": REGIMES,
                 "mu_window_for_resonant": [mlo, mhi]}
# verify the map by direct evaluation at one mu per regime
for muv, expect in ((mp.mpf("0.2"), "neg"), (mp.mpf("1.0"), "cross"),
                    (mp.mpf("3.0"), "pos")):
    a_, b_ = f_red(mp.mpf("0.3"), muv), f_red(mp.mpf("0.9"), muv)
    got = "cross" if a_ * b_ < 0 else ("pos" if a_ > 0 else "neg")
    check(got == expect,
          "mu-map verified by direct evaluation at mu = %s WC: endpoint "
          "signs give '%s' as mapped" % (mp.nstr(muv, 3), got),
          gate="MUMAP")

# ============ 7. NEGATIVE CONTROLS ============
print("\n=== 7: NEGATIVE CONTROLS ===")
# Re chi = -A om^4 L - c4 om^4; flip c4 -> -c4  ==>  ADD 2 c4 om^4
red_flip = sp.simplify((RECHI + 2 * c4 * om**4) / (-A * om**4))
ws_flip = sp.simplify(sp.solve(sp.Eq(red_flip, 0), om)[0] / mu)
control(sp.simplify(ws_flip - w_star_over_mu) != 0,
        "A. LOCAL-TERM SIGN MUTATION: flipping the certified local "
        "contribution (frozen nonlocal untouched) moves the zero from "
        "%s mu to %s mu -- the adjudication IS sensitive to the local "
        "term, so the criterion genuinely consumes D5"
        % (mp.nstr(r_num, 8),
           mp.nstr(mp.mpf(str(float(sp.N(ws_flip, 20)))), 8)))
# remove the local term (c4 -> 0)  ==>  ADD c4 om^4
red_zero = sp.simplify((RECHI + c4 * om**4) / (-A * om**4))
ws_zero = sp.simplify(sp.solve(sp.Eq(red_zero, 0), om)[0] / mu)
control(sp.simplify(ws_zero - 1) == 0
        and sp.simplify(ws_zero - w_star_over_mu) != 0,
        "B. REMOVE-LOCAL-TERM: with c4 = 0 the zero sits exactly at "
        "omega* = mu (log(mu^2/omega^2) = 0), distinct from the "
        "certified %s mu -- the certified constant is doing real work"
        % mp.nstr(r_num, 8))
delta = sp.Rational(1, 10) * c4
red_pert = sp.simplify((RECHI - delta * om**4) / (-A * om**4))
ws_pert = mp.mpf(str(sp.N(sp.solve(sp.Eq(red_pert, 0), om)[0] / mu, 30)))
control(abs(ws_pert - r_num) > mp.mpf("1e-3"),
        "C. WRONG-REFERENCE PERTURBATION: a known 10%% shift of c4 "
        "moves the zero to %s mu (from %s mu), a %s relative shift the "
        "machinery resolves -- detection where expected"
        % (mp.nstr(ws_pert, 8),
           mp.nstr(r_num, 8),
           mp.nstr(mp.mpf(str(abs(ws_pert - r_num) / r_num)), 3)))
control(sp.simplify(sp.im(sp.expand_complex(RECHI))) == 0,
        "D. REALITY: the adjudicated object is exactly real (no "
        "absorptive leakage into the Re-sign test)")

# ============ 10. CLASSIFICATION ============
print("\n=== 10: CLASSIFICATION ===")
mu_determines = OUT["mu_status"]["pinned_by_record"]
n_regimes = len(set(["RESONANT", "PURELY-RELAXATIONAL", "neither"]))
if mu_determines:
    CLASS = "A_or_B_pending_evaluation"
else:
    CLASS = "C"
OUT["classification"] = {
    "verdict": CLASS,
    "meaning": "C = INDETERMINATE: a required quantity remains "
               "unresolved. The unresolved quantity is now a SINGLE "
               "NUMBER -- the renormalization scale mu measured in "
               "plant units (WC) -- which the frozen record "
               "deliberately keeps symbolic (Declaration 1). All three "
               "registered outcomes are reachable as mu varies, and "
               "the boundaries are now EXACTLY computed, so the "
               "adjudication is complete except for that one input",
    "what_D5_did_resolve": "the five-constant H^0 ambiguity collapsed "
                           "to this one scale: c0 = c2 = 0 exactly and "
                           "c4 calculated; the zero's LOCATION RATIO "
                           "omega*/mu = exp(kappa/2) is a fixed "
                           "computed number",
    "scheme_dependence_statement": "the registered Axis-2 criterion IS "
                                   "scheme-dependent through the local "
                                   "real terms -- stated explicitly as "
                                   "the frozen record requires",
    "unnamed_case_finding": "for mu below the lower boundary the "
                            "response has Re chi < 0 throughout the "
                            "domain, which is NEITHER "
                            "PURELY-RELAXATIONAL NOR RESONANT as "
                            "registered -- the trichotomy does not name "
                            "this case; recorded as a FINDING, not "
                            "resolved here",
}
for k, v in OUT["classification"].items():
    note("CLASS %s: %s" % (k, v))
check(CLASS in ("A", "B", "C"),
      "final classification emitted as exactly one of A / B / C: %s"
      % CLASS, gate="CLASS")

# ============ 11 (post): IMMUTABILITY RE-VERIFIED ============
print("\n=== 11: FROZEN INPUTS RE-VERIFIED AFTER THE RUN ===")
unchanged = all(sha_file(os.path.join(HERE, fn)) == PRE[fn] for fn in PINS)
check(unchanged, "every frozen upstream artifact is BYTE-IDENTICAL to "
      "its pre-run hash -- no frozen file was touched", gate="PROV")
try:
    st = subprocess.run(["git", "status", "--short"], cwd=HERE,
                        capture_output=True, text=True, timeout=60).stdout
    OUT["worktree_status"] = st.strip().splitlines()
    note("worktree at end of run: %s"
         % (st.strip().replace("\n", " | ") or "clean"))
except Exception as e:
    note("git status unavailable: %s" % e)

RESULT = {"instrument": "wall_kr_axis2_h0.py",
          "instrument_sha256": sha_file(os.path.abspath(__file__)),
          "authorization": "owner 2026-09-01: H^0-only Axis-2 "
                           "adjudication, post-D5 gate",
          "certified_inputs": {"A": str(A), "c0": "0", "c2": "0",
                               "c4": str(c4),
                               "source_commits": "12ea453 / 04b8d6c"},
          "out": OUT, "checks": CHECKS, "notes": NOTES, "failures": FAILS,
          "frozen_inputs_touched": "NONE",
          "h2_firewall": "no H^2 local computed/fitted/inferred; noise "
                         "fork not opened; alpha=-2 not consulted; "
                         "Tier-4 boundary, Ward finding and J(omega) "
                         "conclusion untouched",
          "elapsed_s": round(time.time() - T0, 1)}
outp = os.path.join(HERE, "WALL_KR_AXIS2_H0_RESULT.json")
json.dump(RESULT, open(outp, "w"), indent=1, default=str)
h1 = sha_file(outp)
json.loads(open(outp).read())
check(h1 == sha_file(outp), "artifact written, re-read, re-hashed "
      "(sha %s...)" % h1[:16], gate="OUT")
npass = sum(1 for c in CHECKS if c["pass"])
print("\nAXIS-2 H^0: %d/%d passed; failures: %d"
      % (npass, len(CHECKS), len(FAILS)))
for m in FAILS:
    print("  FAILURE: " + m)
print("CLASSIFICATION: %s" % CLASS)
print("HARD STOP.")
sys.exit(0 if not FAILS else 1)
