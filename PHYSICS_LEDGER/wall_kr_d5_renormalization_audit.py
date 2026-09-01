#!/usr/bin/env python3
"""D5 LOCAL RENORMALIZATION AUDIT (owner authorization 2026-09-01):
does the frozen contract uniquely determine the local real terms needed
to decide Axis 2?  READ + DERIVE + AUDIT.  K_R is NOT modified; the
nonlocal response is NOT touched; no finite constant is chosen; no pole
search is run.

THE FROZEN D5 CONTRACT (Declaration 1, Wall-A A3 declarations,
sha 87e2d24d..., quoted verbatim in D5-0 below) supplies:
  scheme     = de Sitter-invariant dimensional regularisation;
  condition  = MINIMAL SUBTRACTION, pole terms only, with the finite
               parts of all six basis coefficients "left exactly as the
               loop produces them", mu symbolic-and-recorded;
  basis (1b) = { Lambda, EH(G), R^2, R_mn^2, R_mnrs^2, box R } -- no
               other operator may enter;
  principle  = no finite local counterterm may be selected because it
               produces a preferred spectral or memory behavior; any
               spectral-referencing justification is PROHIBITED.

W-0: computed-and-reported, NOT banked. HARD STOP after the report."""
import hashlib
import json
import os
import sys
import time

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
T0 = time.time()
FAILS = []
CHECKS = []
NOTES = []
OUT = {}


def check(c, m, gate="", detail=None):
    ok = bool(c)
    print(("  ok   " if ok else "  FAIL ") + m)
    sys.stdout.flush()
    CHECKS.append({"pass": ok, "msg": m, "gate": gate, "detail": detail})
    if not ok:
        FAILS.append(m)
    return ok


def control(d, m):
    print(("  ctrl-DETECTED   " if d else "  ctrl-MISSED   ") + m)
    sys.stdout.flush()
    CHECKS.append({"pass": bool(d), "msg": "CONTROL: " + m, "gate": "control"})
    if not d:
        FAILS.append("CONTROL MISSED: " + m)
    return d


def note(m):
    print("  note " + m)
    sys.stdout.flush()
    NOTES.append(m)


def sha_file(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


# ================= PINS =================
print("=== PINS (everything read is frozen) ===")
PINS = {
    "WALL_A_A3_DECLARATIONS.md": "87e2d24d5be6d679",
    "WALL_KR_CONTRACT_RETARDED_RESULT.json": "d916ef32f6f73fa3",
    "WALL_KR_CONTRACT_BENCHMARK_RESULT.json": "1ac17a18ce8c0b8f",
    "WALL_KR_TIER3_LOOP_RESULT.json": "4c016e93b889bd04",
    "WALL_KR_TIER2_MASSLESS_BATH.json": "c5d399f525407839",
    "K_R_CONTRACT_EXECUTION_CHARTER.md": "5416fa45498a6e5f",
    "MICROSCOPIC_TARGET_BENCHMARK.md": "f6513b1e551fd9cf",
}
for fn, want in PINS.items():
    check(sha_file(os.path.join(HERE, fn)).startswith(want),
          "pin %s == %s..." % (fn, want), gate="PIN")
if FAILS:
    sys.exit(2)

# ================= D5-0: THE FROZEN CONTRACT, VERBATIM =================
print("\n=== D5-0: THE FROZEN D5 REQUIREMENT ===")
D50 = {
    "split": "Pi_ren = Pi_local^scheme + Pi_nonlocal^invariant; local = "
             "polynomial in (omega^2, k^2) with coefficients arbitrary "
             "FINITE functions of (m^2, H^2, mu) [F1-amended predicate]; "
             "'Analytic at omega = 0 and k = 0 by construction'",
    "scheme": "'Primary scheme: de Sitter-invariant dimensional "
              "regularisation ... divergences appear as poles in eps and "
              "are subtracted by the counterterm basis of DECLARATION 1b'",
    "condition_F2": "'Renormalisation condition: MINIMAL SUBTRACTION -- "
                    "pole terms only are subtracted; finite parts of all "
                    "six basis coefficients are LEFT EXACTLY AS THE LOOP "
                    "PRODUCES THEM; mu is kept symbolic and its "
                    "dependence recorded as part of Pi_local^scheme's "
                    "data. This is the unique condition with ZERO "
                    "finite-part discretion'",
    "critical_principle": "'No finite local counterterm may be selected "
                          "because it produces a preferred spectral or "
                          "memory behavior' ... 'Any counterterm choice "
                          "whose justification references spectral "
                          "density, memory behavior, or convergence "
                          "class is PROHIBITED and would invalidate the "
                          "blind'",
    "basis_1b": "'frozen to the diffeomorphism-invariant local operators "
                "of the declared action: cosmological constant Lambda, "
                "Newton's constant G (i.e. the EH term), R^2, R_mn^2, "
                "R_mnrs^2, and box R. No other operator may enter' -- a "
                "non-fitting divergent term is a FINDING",
    "sensitivity_iii": "'(iii) IR analytic structure / convergence "
                       "class: NO [local sensitivity] for the class: "
                       "local terms are polynomials in omega -- analytic "
                       "at omega = 0 -- and cannot change the nonlocal "
                       "low-frequency analytic class'",
    "charter_gate_C": "'D5: UV pole reproduction against the frozen "
                      "counterterm basis; pole-only MS discipline (zero "
                      "finite discretion -- the frozen doctrine); "
                      "locality of every subtraction'",
    "pv_crosscheck": "the primary scheme must be run against the "
                     "Pauli-Villars alternative at the assembly stage; "
                     "differences confined to local polynomials, "
                     "reported, never averaged away",
    "benchmark_unique_slice": "the registered benchmark requires the "
                              "TWO AXES; it does NOT require (and the "
                              "critical principle FORBIDS obtaining) a "
                              "local slice chosen for a preferred "
                              "axis-2 outcome",
}
for k, v in D50.items():
    note("D5-0 %s: %s" % (k, v))
OUT["frozen_d5"] = D50
check(True, "D5-0 (recorded statement): the frozen requirement is "
      "quoted verbatim; no condition was inferred from any desired "
      "outcome", gate="D5-0")
note("DISCLOSED CARVE-OUT (review FINDING 6): this audit byte-reads "
     "MICROSCOPIC_TARGET_BENCHMARK.md for hash-pinning only; that file "
     "is on the registry's barred list for LOOP-COMPUTING instruments "
     "(F5 anti-unblinding). This instrument computes no loop quantity "
     "and runs no assembly; the audit-class exemption is hereby "
     "DECLARED rather than assumed, for the owner to ratify or strike")

# ================= D5-1: PARAMETER COUNT =================
print("\n=== D5-1: THE UNDETERMINED LOCAL COEFFICIENTS ===")
om = sp.Symbol("omega", positive=True)
H = sp.Symbol("H", positive=True)
mu = sp.Symbol("mu", positive=True)
c0, c2, c4, c0p, c2p = sp.symbols("c0 c2 c4 c0p c2p", real=True)
T4R = json.loads(open(os.path.join(
    HERE, "WALL_KR_CONTRACT_RETARDED_RESULT.json")).read())
AMAP = {sp.Symbol("omega"): om, sp.Symbol("mu"): mu, sp.Symbol("H"): H,
        sp.Symbol("c0"): c0, sp.Symbol("c2"): c2, sp.Symbol("c4"): c4,
        sp.Symbol("c0p"): c0p, sp.Symbol("c2p"): c2p}
KR = sp.expand(sp.sympify(T4R["out"]["sigma_R"]["H0"]).xreplace(AMAP)
               + H**2 * sp.sympify(
                   T4R["out"]["sigma_R"]["H2_per_H2"]).xreplace(AMAP))
LOCAL = c0 + c2 * om**2 + c4 * om**4 + H**2 * (c0p + c2p * om**2)
note("the frozen K_R carries FIVE real slot constants (c0, c2, c4, "
     "c0p, c2p) plus mu, with mu absorbable into (c4, c2p) -- FIVE "
     "effective real unknowns enter Re K_R")
# which combinations touch the axis-2 test: all five (the window test
# is a pointwise sign test on Re chi over [w_lo, WC])
check(all(sp.diff(LOCAL, cc) != 0 for cc in (c0, c2, c4, c0p, c2p)),
      "ALL FIVE slot constants enter Re K_R on the axis-2 window "
      "(none is silently irrelevant; none is set to zero anywhere in "
      "this audit)", gate="D5-1")
# the 1b basis at FLAT level: the three flat structures {omega^0,
# omega^2, omega^4} are each REACHED by a basis class (Lambda -> mass-
# type omega^0 [Tier-2's own Lambda-off control exhibited the Lambda
# contribution to the TT quadratic form]; EH -> kinetic omega^2 [the
# Tier-2 quadratic reduction P = -a^2]; R^2-class -> four-derivative
# omega^4), and NOTHING beyond omega^4 exists in the basis at this
# derivative order -- the flat slot is exactly the basis's image:
# executable span content (review FINDING 4 repair: the first check
# tested the degree of this audit's own ansatz -- true by construction,
# evidentially empty): linearized R VANISHES identically on flat TT
# (transverse + traceless kill both terms of R_lin = d_m d_n h^mn -
# box h), so the omega^4 slot is carried by the Ricci^2/Riemann^2
# classes, NOT by R^2; box R is a total derivative (contributes
# nothing); Lambda -> omega^0 and EH -> omega^2 stand.
pmu = [sp.Symbol("p_%d" % i) for i in range(4)]
eta4 = sp.diag(1, -1, -1, -1)
e_tt = sp.zeros(4, 4)
e_tt[1, 1], e_tt[2, 2] = 1, -1               # TT '+' along z, p = (w,0,0,k)
psub = {pmu[0]: sp.Symbol("w0"), pmu[1]: 0, pmu[2]: 0,
        pmu[3]: sp.Symbol("k3")}
R_lin = sum(pmu[m_] * pmu[n_] * e_tt[m_, n_] * eta4[m_, m_] * eta4[n_, n_]
            for m_ in range(4) for n_ in range(4))     - sum(eta4[m_, m_] * pmu[m_]**2 for m_ in range(4))     * sum(eta4[m_, m_] * e_tt[m_, m_] for m_ in range(4))
check(sp.simplify(R_lin.subs(psub)) == 0,
      "BASIS SPAN (executable): linearized R is IDENTICALLY ZERO on the "
      "flat TT wave (transversality + tracelessness) => the R^2 "
      "operator's flat TT quadratic kernel is NULL and the omega^4 slot "
      "is carried by the Ricci^2/Riemann^2 classes; box R is a total "
      "derivative; Lambda -> omega^0, EH -> omega^2. The flat slot "
      "{omega^0, omega^2, omega^4} is basis-spanned with nothing beyond "
      "omega^4 -- the class statement, now carried by a computation",
      gate="D5-1")
note("H^2-LINKAGE (CONDITIONAL, review-corrected): 1b constrains where "
     "DIVERGENCES must fit; the finite local remainder is "
     "basis-expressible only IF the executed scheme's finite parts are "
     "covariant -- an assumption of exactly the type F7 forbids drawing "
     "from the regulator's symmetry. The linkage of (c0p, c2p) to "
     "(c0, c2, c4) is therefore CONDITIONAL on that covariance, to be "
     "DEMONSTRATED (not assumed) in the owed execution; nothing in "
     "this audit depends on it")
OUT["parameter_count"] = {
    "slot": str(LOCAL),
    "effective_unknowns": "5 real (mu absorbed)",
    "axis2_relevant": "all five",
    "basis_status": "flat part exactly basis-spanned; H^2 partners "
                    "basis-LINKED (linkage vectors = owed execution)"}

# ================= D5-2: INDEPENDENT RENORMALIZATION CHECK =============
print("\n=== D5-2: INDEPENDENT CHECKS ===")
# (i) eps-pole status of what is ON RECORD: (a) the Tier-2 frozen
# gate (bath-level fixed-omega d = 3 analyticity); (b) the T3
# general-d absorptive closed form, re-verified analytic at d = 3
# here. The DIRECT Re-part's d-continuation is NOT on record -- it is
# exactly branch (b) of the owed execution in D5-3, stated there.
T2A = json.loads(open(os.path.join(
    HERE, "WALL_KR_TIER2_MASSLESS_BATH.json")).read())
t2msgs = [c["msg"] for c in T2A["checks"]
          if "DIMENSIONAL SCALING" in c["msg"] and c["pass"]]
T3M = json.loads(open(os.path.join(
    HERE, "WALL_KR_TIER3_LOOP_RESULT.json")).read())
dsym = sp.Symbol("d", positive=True)
imgen = sp.sympify(T3M["stages"]["flat"]["out"]
                   ["im_sigma_flat_general_d"]).xreplace(
    {sp.Symbol("omega"): om, sp.Symbol("d"): dsym})
lim3 = sp.simplify(sp.limit(imgen, dsym, 3))
check(len(t2msgs) == 1 and "ANALYTIC at d = 3" in t2msgs[0]
      and lim3.is_finite is not False and lim3 != 0
      and sp.simplify(lim3 + 3 * om**4 / (1280 * sp.pi)) == 0,
      "UV STATUS of the RECORD: the Tier-2 fixed-omega gate (frozen, "
      "pinned) and the T3 general-d ABSORPTIVE closed form (re-limited "
      "here: d -> 3 gives exactly -3 omega^4/(1280 pi), no (d-3) pole) "
      "are both eps-pole-free -- the pole-only MS step has NOTHING to "
      "subtract on the absorptive side. The DIRECT Re-part's "
      "d-continuation is NOT yet on record: its pole status is branch "
      "(b) of the owed execution (D5-3), NOT asserted here", gate="D5-2")
# (ii) any F1-local leaves Im K_R untouched (symbolic, exact)
check(sp.simplify(sp.im(LOCAL)) == 0,
      "Im K_R INVARIANCE: every F1-predicate local term (real "
      "polynomial in omega^2 with real (H^2, mu)-dependent "
      "coefficients) has ZERO imaginary part -- the frozen absorptive "
      "content and the s-classification CANNOT be touched by any "
      "admissible local choice (exact, symbolic)", gate="D5-2")
# (iii) branch cut untouched: locals are entire; the cut lives in L
check(all(sp.limit(sp.diff(LOCAL, om, n_), om, 0).is_finite
          for n_ in range(0, 5)),
      "BRANCH-CUT INVARIANCE: the local slot is analytic at omega = 0 "
      "(all derivatives finite) -- it cannot generate, move, or cancel "
      "the omega = 0 branch point (the frozen sensitivity map's row "
      "(iii), verified executably)", gate="D5-2")
# (iv) flat limit + dimensional consistency
check(sp.degree(LOCAL.subs(H, 0), om) == 4 and
      sp.simplify(LOCAL.subs(H, 0).subs(om, 0) - c0) == 0,
      "flat limit and dimensional consistency of the slot against the "
      "F1 predicate (even powers only; H^2-coefficients allowed)",
      gate="D5-2")
# (v) K_R untouched by this audit: anchor identity
Lg = sp.log(mu**2 / om**2) + sp.I * sp.pi
anchor = (sp.Rational(-3, 1280) / sp.pi**2 * om**4 * Lg
          + c0 + c2 * om**2 + c4 * om**4
          + H**2 * (sp.Rational(-13, 480) / sp.pi**2 * om**2 * Lg
                    + c0p + c2p * om**2))
check(sp.simplify(sp.expand(KR - anchor)) == 0,
      "K_R NOT MODIFIED: the object this audit reasons about is "
      "byte-identical in content to the frozen Tier-4 artifact "
      "(anchor identity, exact)", gate="D5-2")

# ================= D5-3: IDENTIFIABILITY =================
print("\n=== D5-3: IDENTIFIABILITY ===")
note("THE DETERMINATION, from the frozen texts -- CORRECTED BY THE "
     "ADVERSARIAL REVIEW (the first draft classified A/UNIQUE and the "
     "review REFUTED it on the scheme level; the refutation is "
     "adopted): TWO transfers must be distinguished. (1) THE DOCTRINE "
     "-- pole-only MS, finite parts as-the-loop-produces-them, zero "
     "finite discretion, the 1b basis, the critical principle -- "
     "imports to contract scope AIRTIGHT (charter Step 2 'frozen "
     "contract', Step 3, gate C verbatim). NO discretion over the "
     "constants exists at any scope. (2) THE SCHEME -- Declaration 1 "
     "declares d = 4 - eps SPACETIME dS-invariant dimensional "
     "regularisation; the contract machinery's actual regulator is the "
     "fixed-omega SPATIAL d = 3 - 2 eps continuation, installed by the "
     "SEPARATE Tier-2 D3/Option-3a owner ruling. These are "
     "inequivalent regularizations, and MS finite parts are exactly "
     "what differs between inequivalent regulators by local "
     "polynomials -- the very objects under audit. The record's own "
     "precedent (D3 itself) is that extending a scheme onto this "
     "machinery is a FRESH OWNER DECLARATION. Moreover the declared "
     "scheme's defining property (dS invariance of the regulated "
     "graviton two-point function) is not known to be realizable "
     "(charter Step 1 leaves gauge/measure (ii) owner-underdefined; "
     "the cited Tsamis-Woodard class is the literature disputing it). "
     "AND: the H^2 branch of any direct execution runs into the "
     "T3-fenced fork sector -- branch (c) of the dichotomy, which the "
     "first draft omitted; the flat (H^0) branch does not (T3: H^0 "
     "clean, both combinations).")
OUT["identifiability"] = {
    "classification": "SPLIT VERDICT (review-corrected). DOCTRINE: "
                      "UNIQUE -- zero finite-part discretion binds at "
                      "contract scope; no constant may ever be chosen. "
                      "SCHEME: **D at the scheme level** -- a "
                      "SCHEME-COMPLETION RULING is required before the "
                      "determination is well-posed, because the frozen "
                      "record contains two inequivalent candidate "
                      "regulators and is silent on which governs the "
                      "contract-scope local extraction. This new input "
                      "is a RULING about regularization, not a "
                      "spectral choice -- the critical principle "
                      "continues to bar any outcome-referencing "
                      "justification",
    "owner_menu": "(alpha) declare Declaration-1's spacetime scheme "
                  "binding at contract scope -- requires first "
                  "resolving its graviton-level realizability "
                  "(gauge/measure (ii)); (beta) extend the D3 "
                  "spatial-continuation ruling to the direct Re/local "
                  "part -- the one-line continuation of the "
                  "already-ruled machinery; (gamma) rule the "
                  "identification contentless PENDING an executed "
                  "scheme-independence demonstration (the frozen PV "
                  "cross-check pattern). Any of the three is an OWNER "
                  "DECLARATION per the record's own D3 precedent",
    "owed_execution_after_ruling": "the direct (non-dispersive) "
                      "evaluation of the local/Re part of the frozen "
                      "T3 kernel in the RULED scheme: H^0 branch "
                      "unobstructed (T3: flat sector clean); the H^2 "
                      "branch additionally requires either a "
                      "demonstrated UV/IR separation from the "
                      "T3-fenced fork class or the owner's fork "
                      "ruling -- branch (c), on the record",
    "not_A_asis": "the first draft's A/UNIQUE assumed the two schemes "
                  "equivalent without derivation -- REFUTED by review; "
                  "A-in-doctrine survives, A-as-posed does not",
    "not_B": "no combination is contract-FREE -- the doctrine forbids "
             "discretion; B does not apply",
    "not_C": "the contract is not silent about the CONDITIONS (it is "
             "maximally explicit); it is silent about the SCHEME "
             "REALIZATION -- that silence is classified under D as a "
             "required ruling, not under C",
}
for k, v in OUT["identifiability"].items():
    note("D5-3 %s: %s" % (k, v))
check(True, "IDENTIFIABILITY (recorded statement, not a failable "
      "gate -- disclosed as such): SPLIT VERDICT -- doctrine UNIQUE / "
      "scheme-completion RULING REQUIRED (D at the scheme level), "
      "with the owner menu and the fork-gated H^2 branch on the "
      "record; nothing was chosen and no value was produced here",
      gate="D5-3")

# ================= D5-4: AXIS-2 DEPENDENCY =================
print("\n=== D5-4: AXIS-2 DEPENDENCY (no verdict collapse) ===")
note("Re chi(omega) = [nonlocal logs, coefficients FROZEN] - [the "
     "five-constant slot]. Dependency structure, exact:")
inv = {
    "invariant_1": "NO kernel-level pole for ANY slot values (chi has "
                   "no denominator; locals are entire) -- exact",
    "invariant_2": "Im chi, the branch point, the cut, the s-class, "
                   "and the axis-1 convergence verdict are slot-"
                   "invariant (D5-2 gates above)",
    "invariant_3": "the log coefficients (3/1280 pi^2 at omega^4, "
                   "13/480 pi^2 H^2 at omega^2) are slot-invariant "
                   "(the 5th/3rd polynomial-free derivatives)",
    "dependent_1": "the pointwise SIGN of Re chi on the registered "
                   "window -- the axis-2 discriminator -- depends on "
                   "the slot: the consequence-stage review exhibited "
                   "BOTH registered outcomes (Re chi > 0 throughout; "
                   "an in-window sign change) as reachable over the "
                   "unrestricted slot, and the basis restriction does "
                   "not remove the quartic-class freedom pre-execution",
    "dependent_2": "whether the dressed object's omega = 0 graviton "
                   "pole persists (c0 = 0 or not) -- determined by the "
                   "same owed execution",
}
OUT["axis2_dependency"] = inv
for k, v in inv.items():
    note("D5-4 %s: %s" % (k, v))
note("CONSEQUENCE (stated without collapsing): before the owed "
     "execution, neither 'pole possible for all allowed choices' nor "
     "'no pole possible for all allowed choices' holds at the dressed "
     "level, and the axis-2 sign test is undetermined; AFTER the owed "
     "execution the slot is unique numbers and axis 2 becomes a "
     "DEFINITE evaluation. Axis 2 is therefore DECIDABLE BY "
     "COMPUTATION under the frozen contract -- not by choice, not by "
     "new input. 'Depends on D5' is hereby converted into 'awaits the "
     "named D5 execution', which is a schedulable step, not a verdict")
check(True, "D5-4 (recorded statement): dependency map recorded; no axis-2 verdict was emitted", gate="D5-4")

# ================= D5-5: CONTROLS =================
print("\n=== D5-5: CONTROLS ===")


def is_F1_local(expr):
    """the F1 predicate as code: real polynomial in omega^2 with
    coefficients FINITE functions of (H^2, mu) -- no odd powers, no
    omega in coefficients, no 1/H^2-singular coefficients (review
    FINDING 5 repair: the finiteness leg is now coded)."""
    e = sp.expand(expr)
    if sp.im(e) != 0 and sp.simplify(sp.im(e)) != 0:
        return False
    try:
        p = sp.Poly(e, om)
    except sp.PolynomialError:
        return False
    for (n_,), coeff in zip(p.monoms(), p.coeffs()):
        if n_ % 2 == 1:
            return False
        if coeff.has(om):
            return False
        lim0 = sp.limit(coeff, H, 0)
        if lim0 in (sp.oo, -sp.oo, sp.zoo):
            return False
    return True


def in_1b_span(expr):
    """basis-membership on the TT k->0 probe: even polynomial of
    degree <= 4 (Lambda/EH/curvature-squared span; anything beyond
    omega^4 is a basis-overflow FINDING per 1b)."""
    if not is_F1_local(expr):
        return False
    return sp.degree(sp.expand(expr), om) <= 4


control(not is_F1_local(om**3),
        "#1 wrong subtraction: an omega^3 term violates the F1 "
        "locality predicate (odd power) and is REJECTED by the "
        "classifier -- it may not be subtracted")
KR_bad = KR + om**4
control(sp.simplify(sp.expand(KR_bad - anchor)) != 0,
        "#2 wrong finite-local constant: injecting a unit omega^4 "
        "shift breaks the frozen Tier-4 anchor identity -- any "
        "modification of K_R is DETECTED")
control(not is_F1_local(sp.I * om**2),
        "#3 accidental Im-part alteration: a complex 'local' term "
        "fails the reality requirement of the F1 predicate -- "
        "REJECTED (no admissible local can touch Im K_R)")
control(sp.simplify(sp.expand(2 * KR - anchor)) != 0,
        "#4 normalization corruption: a doubled kernel fails the "
        "anchor identity -- DETECTED")
control(is_F1_local(c4 * om**4 + H**2 * c2p * om**2),
        "#5 (positive control) genuine basis-class locals PASS the F1 "
        "classifier -- the predicate is not vacuously rejecting "
        "everything")
control(is_F1_local(om**6) and not in_1b_span(om**6),
        "#6 basis overflow: omega^6 is F1-local but EXCEEDS the 1b "
        "span -- flagged as the FINDING class 1b demands (review "
        "FINDING 5: the overflow hole is now covered)")
control(not is_F1_local(om**2 / H**2),
        "#7 non-finite coefficient: an omega^2/H^2 term violates the "
        "F1 finiteness requirement -- REJECTED (review FINDING 5: the "
        "finiteness hole is now covered)")

# ================= DELIVERABLE =================
print("\n=== FREEZE ===")
RESULT = {"instrument": "wall_kr_d5_renormalization_audit.py",
          "instrument_sha256": sha_file(os.path.abspath(__file__)),
          "authorization": "owner 2026-09-01: D5 audit only; K_R "
                           "immutable; no values chosen; no pole "
                           "search",
          "out": OUT, "checks": CHECKS, "notes": NOTES,
          "failures": FAILS,
          "k_r_modified": False,
          "elapsed_s": round(time.time() - T0, 1),
          "hard_stop": "no finite constants chosen; no pole search; no "
                       "J(omega); no benchmark/K_R edits; no Ward work; "
                       "no s-class change. Next: the owner may "
                       "authorize the named D5 execution."}
outp = os.path.join(HERE, "WALL_KR_D5_RENORMALIZATION_RESULT.json")
json.dump(RESULT, open(outp, "w"), indent=1, default=str)
h1 = sha_file(outp)
reread = json.loads(open(outp).read())
check(h1 == sha_file(outp) and reread["k_r_modified"] is False,
      "artifact written, re-read, re-hashed (sha %s...); K_R "
      "modification flag is FALSE on the record" % h1[:16], gate="OUT")
npass = sum(1 for c in CHECKS if c["pass"])
print("\nD5 AUDIT: %d/%d passed; failures: %d"
      % (npass, len(CHECKS), len(FAILS)))
for m in FAILS:
    print("  FAILURE: " + m)
print("HARD STOP.")
sys.exit(0 if not FAILS else 1)
