#!/usr/bin/env python3
"""WALL A -- THE REGISTERED J(omega) BENCHMARK COMPARISON (J0-J9), under the
owner's 2026-08-30 authorization. THE SEAL IS OPEN: this is the first
instrument in the campaign permitted to read the registered comparator, per
Declaration 4's condition (all preregistered blind verdicts + PV recorded).

PRIMARY RULE: THE FROZEN RESPONSE IS THE INPUT. J(omega) IS ONLY THE
COMPARATOR. Nothing on the response side is refit, altered, windowed, or
normalized by agreement. Disagreement is REPORTED. The s >= 2 gapped result is
NOT massaged toward s = 3: the J5 gate has four verdicts and the instrument
cannot emit "confirmed" from a fit above threshold.

THE REGISTERED BENCHMARK (read from the frozen artifacts, J1 below):
  family: J(w) = w^3 exp(-w/20) (super-Ohmic, s_J = 3); convention
  Im chi = J/w ~ w^2 (response exponent s_resp = s_J - 1); GAPLESS.
  The PRE-REGISTERED decision variable is a CONVERGENCE BOUNDARY (axis 1)
  plus the analytic character axis (axis 2: purely-relaxational vs resonant),
  with the live conflict register-s=3 vs class-A white floor (s_eff -> 0)
  fixed on the artifact's face BEFORE this assembly existed.

W-0: computed-and-reported, NOT banked. HARD STOP after the report: no
response edits, no refits, no s-reclassification, no +1 discharge, no Ward
modification, no new derivations, no repairs.
"""
import hashlib
import json
import math
import os
import sys
import time

import mpmath as mp
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
T0 = time.time()
FAILS = []
CHECKS = []
NOTES = []
REPORT = {}
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


# ================= J0: INPUT INTEGRITY (both sides; no drift) =================
print("=== J0: INPUT INTEGRITY ===")
PINS = {
    "WALL_A_A3_DECLARATIONS.md": "87e2d24d5be6d679",
    "WALL_A_A3_DECLARATIONS_V4_AMENDMENT.md": "f6127ca65ad6636b",
    "WALL_A_A3_REGISTRY.json": "faa977d40f1ba318",
    "wall_a_g1_ohmic_plant.py": "facacda5ef0da0d3",
    "MICROSCOPIC_TARGET_BENCHMARK.md": "f6513b1e551fd9cf",
}
for fn, want in PINS.items():
    check(sha_file(os.path.join(HERE, fn)).startswith(want),
          "pin %s == %s..." % (fn, want), gate="J0")
FRZ = json.loads(open(os.path.join(HERE, "Sigma_R_finite_full.json")).read())
KSHA = "dd77b1943e2068c643f4181438814a378c26bc8693b616be812fa5f5888c4ae1"
check(FRZ["manifest"]["complete_kernel_sha256"] == KSHA,
      "frozen kernel sha dd77b194... (THE INPUT; untouched)", gate="J0")
for fn in ("WALL_A3_4_TT_RESULT.json", "WALL_A4_RESPONSE_DRESSED_RESULT.json",
           "WALL_PV_ROBUSTNESS_RESULT.json"):
    note("input sha %s = %s..." % (fn, sha_file(os.path.join(HERE, fn))[:16]))
if FAILS:
    sys.exit(2)

# ================= J1: RECONSTRUCT THE BENCHMARK (verbatim) =================
print("\n=== J1: THE REGISTERED BENCHMARK, AS FROZEN ===")
BENCH = {
    "family": "J(w) = w^3 * exp(-w / 20)  [PLANT-SUPEROHMIC, s_J = 3]",
    "convention": "Im chi = J(w)/w = w^2 exp(-w/20) (registered friction "
                  "convention; response exponent s_resp = s_J - 1 = 2)",
    "independent_variable": "omega in plant units, validity scale WC = 1.0",
    "mass_conventions": "NONE -- the registered family is GAPLESS (no mass "
                        "parameter; flat-space DOS ~ w^2 => super-Ohmic)",
    "H_dependence": "NONE declared",
    "low_frequency_domain": "probe points (0.3, 0.45, 0.6, 0.75, 0.9) * WC; "
                            "slope tolerance TOL_S = 0.30; convergence "
                            "integral from w_lo = 0.15",
    "asymptotic_law": "Im chi ~ w^2 as w -> 0 (registered s=3 row of the "
                      "convergence table: CONVERGES)",
    "threshold_assumptions": "NONE -- no gap anywhere in the family",
    "decision_variable": "PRE-REGISTERED TWO-AXIS ADJUDICATION: axis 1 = "
                         "low-w spectral class {s>=2, s<=1, NOT-A-POWER-LAW, "
                         "UNRESOLVED} + Re chi(0) convergence; axis 2 = "
                         "{PURELY-RELAXATIONAL, RESONANT, INDETERMINATE} on "
                         "the declared domain",
    "live_conflict": "register s=3 (convergent) vs class-A white floor "
                     "s_eff -> 0 (power divergent) -- opposite sides of the "
                     "boundary; this comparison ADJUDICATES",
}
for k, v in BENCH.items():
    note("J1 %s: %s" % (k, v))


def J_reg(w):
    return w**3 * mp.e**(-w / 20)


def imchi_reg(w, sign=1, waxis=1, norm=1):
    return sign * norm * J_reg(waxis * w) / (waxis * w) if w > 0 else mp.mpf(0)


# ================= LOAD THE FROZEN RESPONSE (input side) =================
class Gfun(sp.Function):
    nargs = 5


class Rfun(sp.Function):
    nargs = 5


S0 = sp.sympify(FRZ["sectors"]["0"]["srepr"], locals={"Gfun": Gfun,
                                                      "Rfun": Rfun})
got = hashlib.sha256(sp.srepr(sp.expand(S0)).encode()).hexdigest()
check(got == FRZ["sectors"]["0"]["sha256"], "H^0 round-trip sha ok",
      gate="J0")
om, kk, mm, muS = sp.symbols("omega k m mu", positive=True)
kap = sp.Symbol("kappa")


def Es(i, j):
    return sp.Symbol("E_%d%d" % (min(i, j), max(i, j)))


def Ps(i, j):
    return sp.Symbol("P_%d%d" % (min(i, j), max(i, j)))


sub0 = {}
for a in range(4):
    for b in range(a, 4):
        sub0[Es(a, b)] = 0
        sub0[Ps(a, b)] = 0
sub0[Es(1, 1)] = 1
sub0[Es(2, 2)] = -1
sub0[Ps(1, 1)] = 1
sub0[Ps(2, 2)] = -1
TTpp = sp.expand(S0.xreplace(sub0))
NL = sp.Add(*[t for t in sp.Add.make_args(TTpp) if t.atoms(Gfun, Rfun)])
stamp("frozen TT response loaded (chi = NL(TT_++)/P2(+,+), master units)")


def cutpts(K2, m2):
    if K2 <= 4 * m2:
        return None
    r = mp.sqrt(1 - 4 * m2 / K2)
    return ((1 - r) / 2, (1 + r) / 2)


def quad_atom(fam, n_, np_, e_, K2, m2):
    K2, m2 = mp.mpf(K2), mp.mpf(m2)
    pts = cutpts(K2, m2)
    D = lambda y: m2 - y * (1 - y) * K2
    w = lambda y: y**n_ * (1 - y)**np_
    if fam == "G":
        sgn = (-1) ** e_
        f = lambda y: w(y) * (abs(D(y)))**e_ * (-mp.log(abs(D(y)))) \
            * (sgn if (pts and pts[0] < y < pts[1]) else 1)
        re = mp.quad(f, [0, pts[0], pts[1], 1] if pts else [0, 1])
        im = mp.mpf(0)
        if pts:
            im = mp.pi * mp.quad(lambda y: w(y) * (abs(D(y)))**e_ * sgn,
                                 [pts[0], pts[1]])
        return re + mp.mpc(0, 1) * im
    if pts is None:
        return mp.quad(lambda y: w(y) * D(y)**e_, [0, 1])
    def I(eta):
        return mp.quad(lambda y: w(y) * mp.power(mp.mpc(D(y), -eta), e_),
                       [0, pts[0], pts[1], 1])
    eta = mp.mpf("2e-5")
    return (8 * I(eta / 4) - 6 * I(eta / 2) + I(eta)) / 3


def chi_A(wv, kv, m2v):
    """the FROZEN response, evaluated as computed. No fits, no windows."""
    s2 = {om: sp.Float(mp.nstr(mp.mpf(wv), 20), 20), kk: kv, mm: m2v,
          muS: 1, kap: sp.Float(mp.nstr(mp.log(4 * mp.pi) - mp.euler, 25),
                                25)}
    e2 = NL.subs(s2)
    rep = {}
    for A in e2.atoms(Gfun, Rfun):
        K2v = mp.mpf(wv)**2 - mp.mpf(kv)**2
        v = quad_atom(type(A).__name__[0], int(A.args[0]), int(A.args[1]),
                      int(A.args[2]), K2v, mp.mpf(m2v)**2)
        rep[A] = sp.Float(mp.nstr(mp.re(v), 25), 25) \
            + sp.Float(mp.nstr(mp.im(v), 25), 25) * sp.I
    return mp.mpc(complex(sp.N(e2.subs(rep), 25))) / 2   # /P2(+,+) = /2


# ================= J2: COORDINATE MAPPING (documented, no fits) ==============
print("\n=== J2: COORDINATE MAPPING ===")
note("J2 mapping: computed object = Im chi_TT(omega, k, m) in MASTER UNITS "
     "(the frozen engine's convention, = 16 pi^2 x standard loop measure), "
     "chi = NL(TT_++)/P2(+,+). Registered object = Im chi = J/w in plant "
     "units (WC = 1). NO amplitude fit is performed anywhere: magnitudes are "
     "reported as raw values in each side's own units and every ratio is "
     "reported as a raw factor. Frequency axes are both 'omega'; the "
     "registered family carries no k, no m, no H -- the computed response's "
     "k/m dependence is REPORTED, not projected away.")

# ================= J3 + J5: LOW-FREQUENCY / THE s=3 GATE =================
print("\n=== J3 + J5: LOW-FREQUENCY COMPARISON AND THE s=3 GATE ===")
KV, MV = 1, 1
WTH = mp.sqrt(KV**2 + 4 * MV**2)
note("computed threshold at (k, m) = (%d, %d): omega_th = sqrt(k^2 + 4m^2) "
     "= %s (plant-units comparison is structural, not rescaled)"
     % (KV, MV, mp.nstr(WTH, 8)))
probes = [mp.mpf(p) for p in ("0.3", "0.45", "0.6", "0.75", "0.9")]
rows = []
for w in probes:
    a_im = mp.im(chi_A(w, KV, MV))
    r_im = imchi_reg(w)
    rows.append((float(w), float(a_im), float(r_im)))
    note("J3 probe w = %s: computed Im chi = %s ; registered Im chi = %s"
         % (mp.nstr(w, 4), mp.nstr(a_im, 6), mp.nstr(r_im, 6)))
all_zero = all(abs(r[1]) < 1e-25 for r in rows)
all_pos = all(r[2] > 0 for r in rows)
check(all_zero and all_pos,
      "J3: on EVERY registered probe point the computed Im chi is "
      "IDENTICALLY ZERO (gap: all probes < omega_th = %s) while the "
      "registered family is strictly positive -- the registered low-frequency "
      "interval is NOT ACCESSIBLE to the computed response at the frozen "
      "masses; the discrepancy vanishes in NO declared limit (the massless "
      "limit is undeclared and NOT computed)" % mp.nstr(WTH, 6), gate="J3")
REPORT["J3_probe_rows"] = rows
# the plant's own classifier applied to the computed spectrum: slope of a
# spectrum that is identically zero on the probe grid is UNDEFINED:
note("J5: the plant's own slope classifier (probes 0.3-0.9 WC, TOL_S = 0.30) "
     "receives an identically-zero spectrum on its entire probe grid: the "
     "slope is UNDEFINED there -- no s can be measured in the registered IR "
     "domain, and no fit above threshold is permitted to stand in for it.")
S3_VERDICT = ("S3 INAPPLICABLE / GAP OBSCURES REGISTERED IR LIMIT: the "
              "computed response has NO support on the registered "
              "low-frequency domain (Im chi == 0 identically below omega_th "
              "= sqrt(k^2+4m^2)); the registered s_J = 3 power law is "
              "GAPLESS and cannot be confirmed or refuted from the computed "
              "IR, which is empty. NOT converted to s = 3; NOT converted to "
              "a refutation.")
check(True, "J5 verdict: " + S3_VERDICT, gate="J5")
# AXIS 1 of the pre-registered adjudication -- the convergence boundary:
note("AXIS 1 (the pre-registered decision variable): the computed spectral "
     "class is GAPPED -- Im chi = O(w^s) holds for EVERY s as w -> 0+, so "
     "the static integral (2/pi) Int Im chi / w' dw' is IR-CONVERGENT "
     "RIGOROUSLY. On the benchmark's own convergence table the computed "
     "response lands on the CONVERGENT side -- the REGISTER'S side of the "
     "live conflict -- and AGAINST the class-A white floor (s_eff -> 0, "
     "divergent). Class label in the benchmark's own vocabulary: "
     "NOT-A-POWER-LAW (gapped), convergent. The UV end of the literal "
     "integral requires the subtracted representation (n_sub = 3, "
     "established at A3-4); the boundary being adjudicated is the IR one.")
REPORT["axis1"] = "GAPPED / IR-CONVERGENT (register's side of the boundary; "\
    "white floor refuted at this scope); class = NOT-A-POWER-LAW"

# ================= AXIS 2: RELAXATIONAL vs RESONANT (rung7-relevant) ========
# RUN-2 CORRECTION (disclosed; run-1 artifacts preserved): run 1 tested the
# NONLOCAL part alone and returned RESONANT (1 crossing). Diagnosis before
# report found: (a) the nonlocal crossing is PINNED TO THE LIGHT CONE -- it
# tracks omega = k at every tested momentum (k = 1/2, 1, 2), a spacelike/
# timelike sign structure, not a dynamical resonance, and it exits the domain
# as k -> 0 (the registered family's k-free setting); (b) the FULL MS-fixed
# response (local + nonlocal, the frozen physical object, whose scheme was
# fixed BLIND before any spectral question was asked) is SINGLE-SIGNED across
# the entire domain. The verdict-bearing object is the full frozen response.
# CAVEAT carried to the owner: the axis-2 verdict inherits the local sector's
# scheme freedom (a degree-2 polynomial could alter crossing structure); MS
# was frozen blind, so no counterterm was SELECTED for this behavior -- but
# the scheme-sensitivity of axis 2 is recorded as a limitation. The
# benchmark's true pipeline object (K_R) remains unbuilt (its own
# "OBSTRUCTED AT WALL A" note; Sigma now exists, G_R -> K_R does not).
print("\n=== AXIS 2: Re chi crossing test (full response + nonlocal) ===")
LOCp = sp.Add(*[t for t in sp.Add.make_args(TTpp)
                if not t.atoms(Gfun, Rfun)])


def re_of(expr, wv, kv):
    s2 = {om: sp.Float(mp.nstr(mp.mpf(wv), 20), 20), kk: kv, mm: MV,
          muS: 1, kap: sp.Float(mp.nstr(mp.log(4 * mp.pi) - mp.euler, 25),
                                25)}
    e2 = expr.subs(s2)
    rep = {}
    for A in e2.atoms(Gfun, Rfun):
        K2v = mp.mpf(wv)**2 - mp.mpf(kv)**2
        v = quad_atom(type(A).__name__[0], int(A.args[0]), int(A.args[1]),
                      int(A.args[2]), K2v, mp.mpf(MV)**2)
        rep[A] = sp.Float(mp.nstr(mp.re(v), 25), 25) \
            + sp.Float(mp.nstr(mp.im(v), 25), 25) * sp.I
    return mp.re(mp.mpc(complex(sp.N(e2.subs(rep), 25)))) / 2


grid = [WTH * mp.mpf(f) / 20 for f in range(1, 20)]
full_vals = [(float(w), float(re_of(TTpp, w, KV))) for w in grid]
nl_vals = [(float(w), float(re_of(NL, w, KV))) for w in grid]
def crossings_of(vals):
    s = [1 if v > 0 else (-1 if v < 0 else 0) for _, v in vals]
    return sum(1 for i in range(len(s) - 1) if s[i] * s[i + 1] < 0)
cr_full = crossings_of(full_vals)
cr_nl = crossings_of(nl_vals)
# light-cone tracking gate for the nonlocal crossing:
track = []
for kv2 in (sp.Rational(1, 2), 2):
    kn = mp.mpf(sp.Rational(kv2))
    lo = re_of(NL, kn * mp.mpf("0.98"), kv2)
    hi = re_of(NL, kn * mp.mpf("1.02"), kv2)
    track.append(bool(lo < 0 < hi))
check(all(track), "AXIS 2 diagnosis: the NONLOCAL sign change TRACKS THE "
      "LIGHT CONE (brackets omega = k at k = 1/2 and k = 2) -- it is the "
      "spacelike/timelike boundary, not a dynamical resonance, and exits "
      "the domain as k -> 0", gate="axis2")
axis2 = ("PURELY-RELAXATIONAL (full MS-fixed response: %d crossings on the "
         "declared domain; the nonlocal part's single crossing is the light "
         "cone, k-tracking, domain-exiting as k -> 0)" % cr_full) \
    if cr_full == 0 else "RESONANT (%d crossings of the FULL response)" % cr_full
check(True, "AXIS 2 verdict (full frozen response, scheme caveat recorded): "
      + axis2, gate="axis2",
      detail={"full": full_vals, "nonlocal": nl_vals,
              "nl_crossings": cr_nl})
REPORT["axis2"] = axis2
REPORT["axis2_caveats"] = ("local-sector scheme freedom (degree-2 "
                           "polynomial) can alter crossing structure -- MS "
                           "frozen blind, nothing selected; K_R pipeline "
                           "object unbuilt")
stamp("axes adjudicated")

# ================= J4: ANALYTIC STRUCTURE =================
print("\n=== J4: ANALYTIC STRUCTURE ===")
J4 = {
    "branch_point": "computed: omega_th = sqrt(k^2 + 4m^2), square-root cut "
                    "opening (beta = sqrt(1-4m^2/K^2)); registered: NONE "
                    "(entire function x exponential cutoff)",
    "threshold": "computed: hard two-particle threshold; registered: none",
    "gap": "computed: YES (mass gap 2m at k = 0); registered: GAPLESS",
    "logarithms": "computed: yes (bubble logs, from the frozen atoms); "
                  "registered: none",
    "low_frequency_expansion": "computed: identically zero below threshold "
                               "(no expansion exists); registered: w^2 - "
                               "w^3/20 + ...",
    "verdict": "DIFFERENT ANALYTIC CLASSES. Not the same exact function; "
               "not the same asymptotic class; any numerical similarity "
               "could exist only on a finite window above threshold and "
               "would carry no structural weight (none is claimed).",
}
for k, v in J4.items():
    note("J4 %s: %s" % (k, v))
check(True, "J4: analytic-structure comparison recorded -- DIFFERENT "
      "ANALYTIC CLASSES (structural, not a curve comparison)", gate="J4")
REPORT["J4"] = J4

# ================= J6 + J8: SCALES, MASSES, MOMENTA, RESOLUTION ==============
print("\n=== J6 + J8: NORMALIZATION / SCALING / ROBUSTNESS ===")
w_ref = WTH * mp.mpf("1.5")
a_ref = mp.im(chi_A(w_ref, KV, MV))
r_ref = imchi_reg(w_ref)
note("J6 reference magnitudes at w = 1.5*omega_th: computed = %s (master "
     "units); registered = %s (plant units); RAW ratio = %s -- reported as a "
     "factor, NOT absorbed anywhere (no fitted coupling is authorized by the "
     "frozen benchmark)" % (mp.nstr(a_ref, 6), mp.nstr(r_ref, 6),
                            mp.nstr(a_ref / r_ref, 6)))
sc = []
for (kv2, mv2) in ((1, sp.Rational(1, 2)), (2, 1)):
    wth2 = mp.sqrt(mp.mpf(kv2)**2 + 4 * mp.mpf(sp.Rational(mv2))**2)
    below = abs(mp.im(chi_A(wth2 * mp.mpf("0.97"), kv2, mv2)))
    above = abs(mp.im(chi_A(wth2 * mp.mpf("1.2"), kv2, mv2)))
    sc.append((str(kv2), str(mv2), float(wth2), float(below), float(above)))
    check(below < 1e-25 and above > 1e-10,
          "J6/J8 threshold scaling at (k, m) = (%s, %s): gap edge tracks "
          "sqrt(k^2 + 4m^2) = %s exactly (Im: %.1e below, %.3e above) -- "
          "the computed threshold scales with m and k as the two-particle "
          "cut demands; the registered family has no such scale"
          % (kv2, mv2, mp.nstr(wth2, 6), below, above), gate="J6")
REPORT["scaling"] = sc
# resolution robustness: the probe-grid conclusion at double resolution
fine = [mp.mpf(3) / 20 + mp.mpf(3) / 40 * i for i in range(11)]
all_zero_fine = all(abs(mp.im(chi_A(w, KV, MV))) < 1e-25 for w in fine
                    if w < WTH)
check(all_zero_fine, "J8: doubling the low-frequency grid resolution changes "
      "nothing (Im chi == 0 at every sub-threshold point) -- the J3 "
      "conclusion is resolution-independent", gate="J8")
note("J8 H-dependence: the registered family declares NONE; the computed "
     "response carries frozen H^1 (imaginary class, T4-fenced) and H^2 "
     "sectors -- REPORTED as computed, not compared (no registered "
     "counterpart exists).")

# ================= J7: BLIND SANITY CONTROLS =================
print("\n=== J7: CONTROLS (defined from the benchmark side only) ===")
control(imchi_reg(mp.mpf("0.5"), sign=-1) < 0,
        "benchmark sign reversal flips the registered Im chi negative -- a "
        "passivity-violating comparator is DETECTABLE")
control(abs(imchi_reg(mp.mpf("0.5"), waxis=2) - imchi_reg(mp.mpf("0.5")))
        > abs(imchi_reg(mp.mpf("0.5"))) * mp.mpf("0.5"),
        "frequency-axis corruption (w -> 2w) shifts the registered values by "
        "O(1) -- DETECTED")
wth_bad = WTH * mp.mpf("0.7")
control(abs(mp.im(chi_A(wth_bad * mp.mpf("1.05"), KV, MV))) < 1e-25,
        "threshold corruption: a claimed threshold at 0.7*omega_th would "
        "predict nonzero Im at 0.735*omega_th; the computed response is ZERO "
        "there -- a wrong threshold CANNOT be slipped past the gap edge")
control(abs(imchi_reg(mp.mpf("0.5"), norm=10) / imchi_reg(mp.mpf("0.5"))
            - 10) < mp.mpf("1e-20"),
        "normalization corruption (x10) appears as exactly the factor 10 in "
        "the raw ratio -- nothing absorbs it")

# ================= J9 + VERDICT + HARD STOP =================
print("\n=== J9: THE FOUR QUESTIONS, KEPT SEPARATE ===")
J9 = {
    "A_internally_robust": "YES -- established (A3-4 + A4 + PV), not "
                           "re-adjudicated here",
    "B_Q1_Q4_Q5": "YES -- established, untouched",
    "C_matches_registered_J": "NO -- at the frozen masses the computed "
        "response and the registered family are in DIFFERENT ANALYTIC "
        "CLASSES (gapped two-particle cut vs gapless power law); the "
        "registered IR domain is empty of computed support. SEPARATELY: on "
        "the benchmark's own PRE-REGISTERED decision variable (the "
        "convergence boundary) the computed response lands on the "
        "CONVERGENT side -- the register's side of the live conflict, "
        "against the class-A white floor -- and axis 2 returned %s."
        % ("PURELY-RELAXATIONAL" if "PURELY" in REPORT["axis2"]
           else REPORT["axis2"]),
    "D_meaning": "NOT ANSWERED HERE -- the preregistered protocol assigns "
                 "the ledger consequences (the benchmark's axis table) to "
                 "the OWNER's adjudication; this instrument only fills the "
                 "table in.",
}
for k, v in J9.items():
    note("J9 %s: %s" % (k, v))
RESULT = {
    "stage": "J(omega) benchmark comparison (J0-J9)",
    "frozen_kernel_sha256": KSHA,
    "instrument_sha256": hashlib.sha256(
        open(os.path.abspath(__file__), "rb").read()).hexdigest(),
    "pins": PINS,
    "benchmark_as_frozen": BENCH,
    "s3_verdict": S3_VERDICT,
    "report": REPORT,
    "J9": J9,
    "checks": CHECKS, "notes": NOTES, "failures": FAILS,
    "elapsed_s": round(time.time() - T0, 1),
    "hard_stop": "no response edits, no refits, no s-reclassification, no "
                 "+1 discharge, no Ward modification, no repairs. Owner "
                 "adjudication of the benchmark's ledger table required.",
}
with open(os.path.join(HERE, "WALL_J_OMEGA_COMPARISON_RESULT.json"),
          "w") as f:
    json.dump(RESULT, f, indent=1, default=str)
print("\n================ SUMMARY (J COMPARISON) ================")
print("  J5 (s=3 gate): S3 INAPPLICABLE / GAP OBSCURES REGISTERED IR LIMIT")
print("  AXIS 1: GAPPED, IR-CONVERGENT -- the register's side of the "
      "pre-registered boundary; white floor refuted at this scope")
print("  AXIS 2: %s" % REPORT["axis2"])
print("  J4: DIFFERENT ANALYTIC CLASSES (gapped cut vs gapless power law)")
print("  J9-C: does the computed response match the registered J(omega)? "
      "NO at the frozen masses -- reported as found")
print("gates: %d/%d passed; failures: %d"
      % (sum(1 for c in CHECKS if c["pass"]), len(CHECKS), len(FAILS)))
for m in FAILS:
    print("  FAILURE: " + m)
print("elapsed: %.1fs" % (time.time() - T0))
sys.exit(0 if not FAILS else 1)
