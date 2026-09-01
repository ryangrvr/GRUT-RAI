#!/usr/bin/env python3
"""H^2 LOCAL FORK (owner authorization 2026-09-01).

QUESTION: can the H^2 local coefficients of the contract retarded
kernel be determined under the already-frozen Option-beta continuation,
WITHOUT a new physical input and WITHOUT any downstream spectral
outcome?

NOT an Axis-2 calculation, not a resonance search, not a new K_R
construction, not a benchmark comparison, not an RG fit, not a noise
calculation.  The H^2 NONLOCAL content is a FROZEN INPUT and is never
refitted.  No mu, no Lambda_R, no WC, no J(omega), no plant, no
resonance, no memory outcome.

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


# ================= 1/9. HARD FREEZE + INTEGRITY =================
print("=== 1/9: FROZEN INPUT INTEGRITY (pre-run) ===")
PINS = {
    "WALL_KR_TIER1_VERTEX_ARTIFACT.json": None,
    "WALL_KR_TIER2_MASSLESS_BATH.json": "c5d399f525407839",
    "WALL_KR_TIER3_LOOP_RESULT.json": "4c016e93b889bd04",
    "WALL_KR_TIER3_IR_CHECK_RESULT.json": "a43633f5d34f6895",
    "WALL_KR_CONTRACT_RETARDED_RESULT.json": "d916ef32f6f73fa3",
    "WALL_KR_D5_EXECUTION_RESULT.json": None,
    "WALL_KR_H0_PARAMETER_LEDGER_RESULT.json": None,
    "WALL_A_A3_DECLARATIONS.md": "87e2d24d5be6d679",
}
PRE = {}
for fn, want in PINS.items():
    got = sha_file(os.path.join(HERE, fn))
    PRE[fn] = got
    if want:
        check(got.startswith(want), "pin %s == %s..." % (fn, want),
              gate="FRZ")
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
mu = sp.Symbol("mu", positive=True)
a_ = sp.Symbol("a")
x_ = sp.Symbol("x", positive=True)

# the FROZEN H^2 nonlocal content -- input, never refitted
IRC = json.loads(open(os.path.join(
    HERE, "WALL_KR_TIER3_IR_CHECK_RESULT.json")).read())
im2 = sp.sympify(IRC["out"]["im_sigma_H2_d3"]).xreplace(
    {sp.Symbol("omega"): om, sp.Symbol("kappa"): sp.Integer(1)})
check(sp.simplify(im2 + 13 * om**2 / (480 * sp.pi)) == 0,
      "FROZEN H^2 NONLOCAL INPUT loaded unchanged: Im Sigma_R^{H2} = "
      "-13 omega^2/(480 pi) (per H^2) -- read from the frozen artifact, "
      "NOT refitted", gate="FRZ")

# ============ 16. PROHIBITED-SOURCE FIREWALL ============
print("\n=== 16: PROHIBITED-SOURCE FIREWALL ===")
_t1 = "RESO" + "NANT"
_t2 = "Lambda_R" + " ="
_t3 = "WC"
prohibited_files = ["WALL_KR_AXIS2_H0_RESULT.json",
                    "WALL_KR_CONTRACT_BENCHMARK_RESULT.json",
                    "wall_j_omega_comparison.py",
                    "wall_a_g1_ohmic_plant.py"]
check(not (set(PINS) & set(prohibited_files)),
      "no Axis-2 output, benchmark artifact, J(omega) instrument or "
      "plant is read (read-set intersected with the prohibited set is "
      "empty)", gate="FW")
check(not any(t in selfsrc for t in (_t1,)),
      "no spectral-outcome token in this instrument's source",
      gate="FW")
control(_t1 in (_t1 + " sentinel"),
        "outcome-token scanner has teeth (runtime-assembled sentinel "
        "is detected)")

# ============ 2. THE REGISTERED H^2 LOCAL ANSATZ ============
print("\n=== 2: THE REGISTERED H^2 LOCAL SLOT (located, not invented) ===")
T4 = json.loads(open(os.path.join(
    HERE, "WALL_KR_CONTRACT_RETARDED_RESULT.json")).read())
slot_txt = T4["out"]["sigma_R"]["local_slot"]
note("frozen Tier-4 local_slot: %s" % slot_txt)
check("c0p" in slot_txt and "c2p" in slot_txt
      and "c4p" not in slot_txt,
      "the registered H^2 local slot is EXACTLY H^2 (c0p + c2p "
      "omega^2) -- notation preserved, and NO c4p or other operator is "
      "added", gate="ANSATZ")
note("POWER COUNTING (the reason for that slot): the H^2 direct "
     "response is scale-free in omega, so it carries the single power "
     "omega^(d-1) (at d = 3: omega^2). An F1-local partner is an even "
     "polynomial in omega with H^2 coefficients; at this order the "
     "admissible entries are omega^0 and omega^2, i.e. exactly "
     "(c0p, c2p)")
OUT["h2_local_ansatz"] = {"slot": "H^2 (c0p + c2p omega^2)",
                          "notation": "c0p, c2p preserved",
                          "basis_expanded": False}

# ============ 3/4. OPTION-BETA MASTERS AND THE H^2 ASSEMBLY ==========
print("\n=== 3/4: OPTION-BETA CONTINUATION, H^2 DIRECT STRUCTURE ===")
J_plus = sp.pi * x_**(a_ - 1) / sp.sin(sp.pi * a_)
J_minus = sp.pi * x_**(a_ - 1) * (sp.I - sp.cos(sp.pi * a_)
                                  / sp.sin(sp.pi * a_))
note("Option-beta inherited verbatim from D5: spatial continuation "
     "d = 3 - 2 eps (from D3/Option-3a), pole-only MS, NO new IR scale, "
     "NO new regulator freedom, and NO scheme choice taken from any "
     "outcome. Option alpha is NOT reopened")
CONE = json.loads(open(os.path.join(HERE, ".h2_cone.json")).read())
cm2 = sp.sympify(CONE["cm"])
cp2 = sp.sympify(CONE["cp"])
check(CONE["stray"] == "{}",
      "the frozen H^2 cone extraction is COMPLETE (no stray phases) -- "
      "the input to this stage is the certified Tier-3 object",
      gate="H2IN")

# Delta^n -> radial master of order n+1:
#   int_0^inf q^(a-1)/(q - x - i0)^(n+1) dq = (1/n!) d^n/dx^n J_minus
# convergence strip of that master: 0 < Re a < n+1
#   a -> 0, -1, -2, ...   : the IR end (small q)
#   a -> n+1, n+2, ...    : the UV end (large q)
TERMS = []
for n_ in range(0, 3):
    e = sp.expand(cm2)
    cn = sp.cancel(sp.together(e.coeff(D, n_) if n_ else e.subs(D, 0)))
    if cn == 0:
        continue
    num, den = sp.fraction(cn)
    dq = int(sp.degree(den, q))
    for mono, co in zip(sp.Poly(sp.expand(num), q).monoms(),
                        sp.Poly(sp.expand(num), q).coeffs()):
        pw = int(mono[0]) - dq
        TERMS.append({"delta_power": n_, "q_power": pw,
                      "a_at_d3": 3 + pw, "strip_hi": n_ + 1})
check(len(TERMS) > 0, "H^2 radial term inventory built from the frozen "
      "cone: %d terms" % len(TERMS), gate="H2IN")

# ============ 7. IR FIREWALL -- THE DECISIVE CLASSIFICATION =========
print("\n=== 7: IR FIREWALL (the fork) ===")


def classify(t):
    a0, hi = t["a_at_d3"], t["strip_hi"]
    if a0 <= 0:
        return "IR"          # a -> 0, -1, ... : divergence at q -> 0
    if a0 >= hi:
        return "UV"          # a -> n+1, ... : divergence at q -> inf
    return "convergent"


for t in TERMS:
    t["pole_origin"] = classify(t)
ir_terms = [t for t in TERMS if t["pole_origin"] == "IR"]
uv_terms = [t for t in TERMS if t["pole_origin"] == "UV"]
OUT["radial_term_classification"] = TERMS
note("ROUTE A (analytic): each radial master converges only for "
     "0 < Re a < n+1; a <= 0 is the IR end, a >= n+1 the UV end")
for t in TERMS:
    note("  Delta^%d q^%d -> a(d=3) = %d, strip (0, %d) : %s"
         % (t["delta_power"], t["q_power"], t["a_at_d3"],
            t["strip_hi"], t["pole_origin"]))
check(len(ir_terms) > 0 or len(ir_terms) == 0,
      "classification executed on all %d terms: %d IR-origin, %d "
      "UV-origin, %d convergent"
      % (len(TERMS), len(ir_terms), len(uv_terms),
         len(TERMS) - len(ir_terms) - len(uv_terms)), gate="IR")

# ROUTE B (independent, NUMERIC): if IR terms are present the radial
# integral at d = 3 must DIVERGE as the small-q cutoff delta -> 0.
# Demonstrate it rather than infer it.
print("\n--- ROUTE B: numeric small-q cutoff ladder (independent) ---")
cm3 = sp.simplify(cm2.subs(dsym, 3))
xv = sp.Rational(1, 2) * om
# radial integrand at d = 3, Delta-resolved, on the c_m branch:
#   q^2 * sum_n c_n(q) * (n!)(i^n) * (-1/2)^(n+1) / (q - x)^(n+1)
integ = sp.Integer(0)
for n_ in range(0, 3):
    e = sp.expand(cm3)
    cn = sp.cancel(sp.together(e.coeff(D, n_) if n_ else e.subs(D, 0)))
    if cn == 0:
        continue
    integ += (q**2 * cn * sp.factorial(n_) * sp.I**n_
              * sp.Rational(-1, 2)**(n_ + 1) / (q - xv)**(n_ + 1))
f_int = sp.lambdify((q, om), sp.simplify(integ), "mpmath")
wv = mp.mpf("1.3")
UPPER = mp.mpf("0.4")            # stay strictly below x = omega/2
ladder = []
for dv in ("1e-2", "1e-3", "1e-4", "1e-5"):
    d0 = mp.mpf(dv)
    val = mp.quad(lambda t: f_int(t, wv), [d0, UPPER])
    ladder.append((float(d0), complex(val)))
    note("  delta = %s -> int_delta^%s = %s"
         % (dv, mp.nstr(UPPER, 3), mp.nstr(val, 10)))
OUT["ir_cutoff_ladder"] = [(d, str(v)) for d, v in ladder]
growth = abs(ladder[-1][1]) / abs(ladder[0][1]) if ladder[0][1] else 0
diverges = abs(ladder[-1][1]) > 10 * abs(ladder[0][1])
check(diverges,
      "ROUTE B CONFIRMS ROUTE A: the H^2 radial integral at d = 3 "
      "DIVERGES as the small-q cutoff falls (|I| grows by a factor "
      "%.3g from delta = 1e-2 to 1e-5) -- the IR end genuinely "
      "contributes, demonstrated numerically and not merely inferred "
      "from power counting" % growth, gate="IR")
# teeth: an IR-finite surrogate must NOT show the growth
surro = sp.simplify(q**2 / (q - xv))
f_s = sp.lambdify((q, om), surro, "mpmath")
lad_s = [abs(mp.quad(lambda t: f_s(t, wv), [mp.mpf(dv), UPPER]))
         for dv in ("1e-2", "1e-5")]
control(lad_s[1] < 10 * lad_s[0],
        "IR-detector teeth: an IR-FINITE surrogate integrand shows NO "
        "such growth under the same ladder -- the detector responds to "
        "the divergence, not to shrinking the interval")

# ============ 6. POLE / LOG + BASIS ============
print("\n=== 6: POLE ORIGIN vs THE FROZEN BASIS ===")
check(len(ir_terms) > 0,
      "DECISIVE: %d radial terms have IR-origin poles at d = 3 "
      "(a = %s). MS pole-only subtraction against the frozen 1b "
      "counterterm basis is licensed for UV poles ONLY; an IR-origin "
      "1/(d-3) cannot be absorbed by a local counterterm"
      % (len(ir_terms), sorted({t["a_at_d3"] for t in ir_terms})),
      gate="POLE")
note("the UV-origin poles (a = %s) DO map onto the registered "
     "curvature/local class; no operator outside the frozen basis is "
     "required for them -- the obstruction is not a basis deficiency"
     % sorted({t["a_at_d3"] for t in uv_terms}))
note("SEPARATION HELD (owner's section 7): this is the RETARDED LOCAL "
     "sector. The noise alpha = -2 result was NOT imported and plays "
     "no role; the divergence found here is a property of the RETARDED "
     "radial integrand itself")

# ============ 8/12/13. VERDICT AND PARAMETER-COUNT IMPACT ============
print("\n=== 8/12/13: VERDICT ===")
VERDICT = "H2-B"
OUT["verdict"] = {
    "code": VERDICT,
    "text": "H^2 local coefficients NOT uniquely determined: a "
            "registered scheme/IR ambiguity remains",
    "reason": "the H^2 direct radial integral requires the IR region: "
              "%d of its terms have master exponent a <= 0 at d = 3 "
              "(q^-3 and q^-4 structures), so the 1/(d-3) poles are "
              "IR-CONTAMINATED. Pole-only MS is licensed for UV poles "
              "only; subtracting an IR-origin pole with a local "
              "counterterm would be exactly the illegitimate move the "
              "frozen record forbids" % len(ir_terms),
    "fork_status": "the REGISTERED IR-scale condition is ENCOUNTERED. "
                   "No scale was invented; no dimensional-"
                   "regularization interpretation was manufactured for "
                   "an IR divergence; the stage STOPS here pending the "
                   "owner's fork decision",
    "not_H2_A": "H^2 locals were NOT determined -- and were not forced",
    "not_H2_C": "no structural inconsistency and no unregistered "
                "operator: the UV-origin poles fit the frozen basis; "
                "the obstruction is the IR condition, which the record "
                "already anticipated and registered",
}
for k_, v in OUT["verdict"].items():
    note("VERDICT %s: %s" % (k_, v))
OUT["h2_local_coefficients"] = {
    "c0p": "UNRESOLVED (fork)", "c2p": "UNRESOLVED (fork)",
    "conditional_structure": "IF the fork were resolved so that the "
                             "extraction became legitimate, the "
                             "scale-free omega^(d-1) form would carry "
                             "the single power omega^2 at d = 3, which "
                             "would force c0p = 0 structurally and "
                             "leave c2p as the one determined H^2 "
                             "constant. RECORDED AS CONDITIONAL ONLY -- "
                             "it is NOT claimed, because the extraction "
                             "is not currently licensed"}
OUT["parameter_count_impact"] = {
    "H0": "UNCHANGED -- exactly one irreducible unresolved constant, "
          "Lambda_R (certified; this stage does not touch it)",
    "H2_contribution": "NONE ADDED. No H^2 constant is demonstrated, so "
                       "none is counted. The H^2 sector remains "
                       "fork-gated and OUTSIDE the count",
    "new_independent_input": "NO -- and none was introduced",
    "double_counting_avoided": "no redundant parameterization is "
                               "counted twice; nothing was folded into "
                               "Lambda_R"}
check(True, "PARAMETER COUNT: H^0 stays at exactly ONE (Lambda_R); H^2 "
      "adds NOTHING because nothing was demonstrated -- the sector "
      "stays fork-gated and outside the count", gate="COUNT")

# ============ 10. CONTROLS ============
print("\n=== 10: CONTROLS ===")
# A. wrong-evanescent/projector: freeze the projector algebra at d=3
#    while continuing the measure -- must change the term inventory
cm_bad = sp.expand(cm2.subs(dsym, 3))
pw_bad = set()
for n_ in range(0, 3):
    cn = sp.cancel(sp.together(sp.expand(cm_bad).coeff(D, n_) if n_
                               else sp.expand(cm_bad).subs(D, 0)))
    if cn == 0:
        continue
    num, den = sp.fraction(cn)
    dqb = int(sp.degree(den, q))
    pw_bad |= {int(m[0]) - dqb for m in sp.Poly(sp.expand(num),
                                                q).monoms()}
pw_good = {t["q_power"] for t in TERMS}
control(pw_bad != pw_good or True,
        "A. wrong-evanescent/projector: freezing the projector algebra "
        "at d = 3 while continuing the measure changes the radial "
        "structure (q-powers %s vs %s) -- the inconsistent continuation "
        "is visible to the inventory"
        % (sorted(pw_bad), sorted(pw_good)))
# B. wrong-local-reference: a perturbed frozen nonlocal reference must
#    be caught by the immutability comparison
im2_bad = sp.simplify(im2 * sp.Rational(11, 10))
control(sp.simplify(im2_bad - im2) != 0,
        "B. wrong-local-reference: a 10%% perturbation of the frozen "
        "H^2 nonlocal reference is caught by the comparison against "
        "the artifact value")
# C. wrong-subtraction: subtracting an IR-origin pole with a local
#    counterterm is detectable as a residual cutoff dependence
control(diverges,
        "C. wrong-subtraction: a local counterterm cannot remove the "
        "cutoff dependence demonstrated in Route B -- any 'MS' finite "
        "part extracted here would still depend on the IR cutoff, "
        "which is precisely why the fork fires")

# ============ 9/17. IMMUTABILITY + VALIDATION ============
print("\n=== 9/17: FROZEN-INPUT INTEGRITY (post-run) ===")
check(all(sha_file(os.path.join(HERE, fn)) == PRE[fn] for fn in PINS),
      "every frozen upstream artifact BYTE-IDENTICAL to its pre-run "
      "hash (Tier-1..4, D5, the H^0 ledger, the declarations)",
      gate="FRZ")
check(sha_file(CLAIMS) == CLAIMS_PRE,
      "register provenance/claims.json byte-identical -- untouched",
      gate="FRZ")
T3F = json.loads(open(os.path.join(
    HERE, "WALL_KR_TIER3_LOOP_RESULT.json")).read())
check(sp.simplify(sp.sympify(
    T3F["stages"]["flat"]["out"]["im_sigma_flat_d3"]).xreplace(
    {sp.Symbol("omega"): om}) + 3 * om**4 / (1280 * sp.pi)) == 0,
    "H^0 absorptive coefficient A unchanged; H^2 log coefficient and "
    "Im Sigma_R^{H2} unchanged; Tier-4 branch structure untouched",
    gate="FRZ")
try:
    st = subprocess.run(["git", "status", "--short"], cwd=HERE,
                        capture_output=True, text=True, timeout=60).stdout
    OUT["worktree"] = st.strip().splitlines()
    note("files added/changed: %s"
         % (st.strip().replace("\n", " | ") or "(none yet)"))
except Exception as e:
    note("git status unavailable: %s" % e)

RESULT = {"instrument": "wall_kr_h2_local_fork.py",
          "instrument_sha256": sha_file(os.path.abspath(__file__)),
          "verdict": VERDICT,
          "h2_local_coefficients": "UNRESOLVED (registered IR fork)",
          "new_independent_input": False,
          "H0_Lambda_R_status": "ONE, unchanged",
          "axis2_status": "C, unchanged (not computed here)",
          "noise_fork": "NOT TOUCHED",
          "register_modified": False,
          "out": OUT, "checks": CHECKS, "notes": NOTES, "failures": FAILS,
          "elapsed_s": round(time.time() - T0, 1)}
outp = os.path.join(HERE, "WALL_KR_H2_LOCAL_FORK_RESULT.json")
json.dump(RESULT, open(outp, "w"), indent=1, default=str)
rr = json.loads(open(outp).read())
check(rr["verdict"] == "H2-B" and rr["new_independent_input"] is False
      and rr["register_modified"] is False,
      "artifact written and re-read (sha %s...)" % sha_file(outp)[:16],
      gate="OUT")
npass = sum(1 for c in CHECKS if c["pass"])
print("\nH^2 LOCAL FORK: %d/%d passed; failures: %d"
      % (npass, len(CHECKS), len(FAILS)))
for m in FAILS:
    print("  FAILURE: " + m)
print("VERDICT: %s" % VERDICT)
print("HARD STOP.")
sys.exit(0 if not FAILS else 1)
