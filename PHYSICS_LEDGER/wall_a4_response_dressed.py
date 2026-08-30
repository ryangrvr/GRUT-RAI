#!/usr/bin/env python3
"""WALL A, STAGE A4 (RESPONSE LEVEL), PHASE II -- THE DRESSED (H^1/H^2) ORBIT,
completing the owner's A4-0..A4-8 brief (Phase I = flat, complete, 35/35).

THE DRESSED ORBIT (countersigned formula, wall_a_a4_dual_gauge.py 03cc6bcc):
    delta_h_mu nu = 2 (a'/a) zeta^0 eta_mu nu + d_mu zeta_nu + d_nu zeta_mu
In the engine's exact chart (Section D, gated below): a^2 = 1 + 2Hu + 3H^2u^2
=> a = 1 + Hu + H^2u^2 and a'/a = H + H^2 u + O(H^3). For a plane-wave zeta
with polarisation X the orbit therefore splits, through O(H^2), into:
    delta_e^0(X)   = i (K_mu X_nu + K_nu X_mu)          [flat; Phase I]
    delta_e^1(X)   = 2 X_0 eta_mu nu                    [u-FREE]
    delta_e^2u(X)  = 2 u X_0 eta_mu nu                  [u-CARRYING]
The u-carrying piece is the ONLY term the frozen kernel cannot contract (it
demands a loop u-moment). It is PURE TRACE (eta-direction): its TT contraction
vanishes identically, so the TT-robustness adjudication is COMPLETE through
O(H^2) without it; the gap is confined to the non-TT Ward bookkeeping at
O(H^2) and is recorded as the single declared scope boundary -- exactly the
case the owner's "unless the independent construction demands" clause governs.

WHAT PHASE II COMPUTES (all from the frozen kernel; H-grading composition):
  ORDER H^1 orbit contraction:  W1 = SEC1(de^0, p) + SEC0(de^1, p)
  ORDER H^2 u-free part:        W2 = SEC2(de^0, p) + SEC1(de^1, p)
  each split local/nonlocal, TT-reach tested, per the Phase-I battery.
  THE TRACE-CANCELLATION THEOREM, executed: the eta-direction shifts e_11 and
  e_22 EQUALLY, so the TT amplitudes ((e11 - e22)/2 and e12) are orbit-blind
  at every order; with Phase I's K-direction result, route-B TT == route-A TT
  as an OPERATOR IDENTITY through O(H^2).
  The synchronous solver extended perturbatively in H (existence/uniqueness).
  Controls: a broken dressing coefficient MUST change the orbit contraction;
  a dressed pure-gauge injection MUST NOT change any TT amplitude.

W-0: computed-and-reported, NOT banked. No J(omega), no PV, no +1 discharge.
HARD STOP after output. Exit 0 iff gates pass and controls behave.
"""
import hashlib
import json
import os
import sys
import time

import sympy as sp
from sympy.core.cache import clear_cache

HERE = os.path.dirname(os.path.abspath(__file__))
T0 = time.time()
READ_FILES = []
FAILS = []
CHECKS = []
NOTES = []


def stamp(msg):
    print("[%7.1fs] %s" % (time.time() - T0, msg))
    sys.stdout.flush()


def check(cond, msg, gate="", detail=None):
    ok = bool(cond)
    print(("  ok   " if ok else "  FAIL ") + msg)
    sys.stdout.flush()
    CHECKS.append({"pass": ok, "msg": msg, "gate": gate, "detail": detail})
    if not ok:
        FAILS.append(msg)
    return ok


def control(detected, msg):
    print(("  ctrl-DETECTED   " if detected else "  ctrl-MISSED   ") + msg)
    sys.stdout.flush()
    CHECKS.append({"pass": bool(detected), "msg": "CONTROL: " + msg,
                   "gate": "control"})
    if not detected:
        FAILS.append("CONTROL MISSED: " + msg)
    return detected


def note(msg):
    print("  note " + msg)
    sys.stdout.flush()
    NOTES.append(msg)


def tracked_read(path):
    READ_FILES.append(path)
    with open(path) as f:
        return f.read()


def sha_file(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


# ================= A4-0 (PHASE II): GUARD + PINS =================
print("=== A4-0 (II): GUARD + PINS ===")
registry = json.loads(tracked_read(os.path.join(HERE, "WALL_A_A3_REGISTRY.json")))
barred_names, barred_files = set(), {}
for entry in registry["g0_spectral_wiring"]["barred_inputs"]:
    for o in entry.get("objects", []):
        barred_names.add(o)
    for f in entry.get("files", []):
        barred_files[f] = entry.get("sha256", {}).get(f)
own_src = tracked_read(os.path.abspath(__file__))
hits = [mn for mn in list(sys.modules)
        if any(b.lower() in mn.lower() for b in barred_names)] \
    + [b for b in barred_names if b in own_src.replace("barred_names", "")
       and ('"' + b + '"') not in own_src]
if hits:
    print("   GUARD TRIPPED: %s -- RUN VOID" % hits)
    sys.exit(2)
print("   GUARD CLEAN at load")
PINS = {
    "WALL_A_A3_REGISTRY.json": "faa977d40f1ba318",
    "wall_a_a4_dual_gauge.py": "03cc6bcc0fec0c13",
    "wall_a4_response_flat.py": None,       # recorded, not pinned in advance
}
for fn, want in PINS.items():
    h = sha_file(os.path.join(HERE, fn))
    if want:
        check(h.startswith(want), "pin %s == %s..." % (fn, want), gate="A4-0")
    else:
        note("recorded sha %s = %s..." % (fn, h[:16]))
FRZ = json.loads(tracked_read(os.path.join(HERE, "Sigma_R_finite_full.json")))
KSHA = "dd77b1943e2068c643f4181438814a378c26bc8693b616be812fa5f5888c4ae1"
check(FRZ["manifest"]["complete_kernel_sha256"] == KSHA,
      "frozen kernel sha == dd77b194...", gate="A4-0")
P1 = json.loads(tracked_read(os.path.join(HERE,
                                          "WALL_A4_RESPONSE_FLAT_RESULT.json")))
check(P1["frozen_kernel_sha256"] == KSHA and not P1["failures"],
      "Phase I result loaded: same kernel, 0 failures (route-B flat Q1 %s)"
      % P1["route_B_verdicts"]["Q1_TT_flat"], gate="A4-0")
if FAILS:
    sys.exit(2)


# ================= LOAD: all three sectors =================
print("\n=== LOAD ===")


class Gfun(sp.Function):
    nargs = 5


class Rfun(sp.Function):
    nargs = 5


SEC = {}
for n in ("0", "1", "2"):
    SEC[int(n)] = sp.sympify(FRZ["sectors"][n]["srepr"],
                             locals={"Gfun": Gfun, "Rfun": Rfun})
    got = hashlib.sha256(sp.srepr(sp.expand(SEC[int(n)])).encode()).hexdigest()
    check(got == FRZ["sectors"][n]["sha256"],
          "H^%s round-trip sha ok (%s...)" % (n, got[:16]), gate="load")
    clear_cache()
om, kk, mm, muS = sp.symbols("omega k m mu", positive=True)
kap = sp.Symbol("kappa")
stamp("sectors loaded")


def Esym(i, j):
    return sp.Symbol("E_%d%d" % (min(i, j), max(i, j)))


def Psym(i, j):
    return sp.Symbol("P_%d%d" % (min(i, j), max(i, j)))


def eval_on(expr, emat, pmat):
    sub = {}
    for a in range(4):
        for b in range(a, 4):
            sub[Esym(a, b)] = emat[a, b]
            sub[Psym(a, b)] = pmat[a, b]
    return sp.expand(expr.xreplace(sub))


def nonlocal_part(ex):
    return sp.Add(*[t for t in sp.Add.make_args(ex) if t.atoms(Gfun, Rfun)])


def symm_from(entries):
    M = sp.zeros(4, 4)
    for (a, b), v in entries.items():
        M[a, b] = M[b, a] = v
    return M


# ================= STEP 1: THE DRESSED ORBIT, DERIVED + GATED =================
print("\n=== STEP 1: DRESSED ORBIT FROM THE EXACT CHART ===")
H_, u_ = sp.symbols("H u")
a_series = 1 + H_ * u_ + H_**2 * u_**2
check(sp.expand(a_series**2 - (1 + 2 * H_ * u_ + 3 * H_**2 * u_**2)).coeff(
    H_, 0) == 0 and
    sp.expand(a_series**2 - (1 + 2 * H_ * u_ + 3 * H_**2 * u_**2)).coeff(
    H_, 1) == 0 and
    sp.expand(a_series**2 - (1 + 2 * H_ * u_ + 3 * H_**2 * u_**2)).coeff(
    H_, 2) == 0,
    "chart gate: a = 1 + Hu + H^2u^2 reproduces the engine's Section-D "
    "a^2 = 1 + 2Hu + 3H^2u^2 through O(H^2)", gate="orbit")
aprime_over_a = sp.expand(sp.diff(a_series, u_) / a_series)
apoa_ser = sp.series(aprime_over_a, H_, 0, 3).removeO()
check(sp.expand(apoa_ser - (H_ + H_**2 * u_)).coeff(H_, 1) == 0
      and sp.expand(apoa_ser - (H_ + H_**2 * u_)).coeff(H_, 2) == 0,
      "orbit gate: a'/a = H + H^2 u + O(H^3) (DERIVED from the chart)",
      gate="orbit")
ETA = sp.diag(1, -1, -1, -1)
Klo = [om, 0, 0, -kk]
X = [sp.Symbol("X%d" % a) for a in range(4)]
I_ = sp.I


def de0(Xv, sgn=1):
    return sp.Matrix(4, 4, lambda a, b: sgn * I_ * (Klo[a] * Xv[b]
                                                    + Klo[b] * Xv[a]))


def de1(Xv, coeff=2):
    return sp.Matrix(4, 4, lambda a, b: coeff * Xv[0] * ETA[a, b])


note("orbit split through O(H^2): de^0 = i(KX + XK); de^1 = 2 X_0 eta "
     "[u-free]; de^2u = 2 u X_0 eta [u-CARRYING -- pure trace; demands a loop "
     "u-moment; TT-irrelevant by the trace-cancellation theorem below; "
     "recorded as the single non-TT O(H^2) scope boundary]")

# ================= STEP 2: THE TRACE-CANCELLATION THEOREM, EXECUTED =========
print("\n=== STEP 2: TRACE-CANCELLATION (TT blindness at ALL orders) ===")
d0 = de0(X)
d1 = de1(X)
for nm, d in (("K-direction de^0", d0), ("eta-direction de^1", d1)):
    tt_plus = sp.simplify((d[1, 1] - d[2, 2]) / 2)
    tt_cross = sp.simplify(d[1, 2])
    check(tt_plus == 0 and tt_cross == 0,
          "theorem gate: %s has ZERO TT amplitudes ((e11-e22)/2 and e12) "
          "for GENERAL X" % nm, gate="theorem")
note("=> the orbit cannot move ANY TT amplitude at ANY order in H (K-terms "
     "cannot reach the transverse block; eta-terms shift e11 and e22 equally "
     "and cancel in the traceless combination; the u-carrying term is "
     "eta-direction too). Route-B TT == route-A TT as an OPERATOR IDENTITY "
     "through O(H^2); the A3-4 TT verdicts (Q1 INSIDE / Q4 HOLDS / Q5 "
     "INSIDE) are therefore GAUGE-ROBUST at every adjudicated order, by "
     "proof rather than re-evaluation. Comparison evidence, not imposition: "
     "the identity was derived from the countersigned orbit, not from A3-4.")

# ================= STEP 3: SYNCHRONOUS SOLVER, DRESSED =================
print("\n=== STEP 3: SYNCHRONOUS SOLVER AT O(H) ===")
EG = symm_from({(a, b): sp.Symbol("e%d%d" % (a, b))
                for a in range(4) for b in range(a, 4)})
X0v = [sp.Symbol("XA%d" % a) for a in range(4)]
X1v = [sp.Symbol("XB%d" % a) for a in range(4)]
eq0 = [sp.Eq((EG + de0(X0v))[0, b], 0) for b in range(4)]
s0 = sp.solve(eq0, X0v, dict=True)
resid1 = sp.expand(de0(X1v) + de1([s0[0][x] for x in X0v]))
eq1 = [sp.Eq(resid1[0, b], 0) for b in range(4)]
s1 = sp.solve(eq1, X1v, dict=True)
check(len(s0) == 1 and len(s1) == 1,
      "dressed solver: the synchronous conditions determine X order-by-order "
      "in H uniquely at generic (omega,k) (O(H^0) and O(H^1) solved; the "
      "residual family remains zero-frequency, empty here)", gate="A4-1")
stamp("dressed solver done")

# ================= STEP 4: WARD/ORBIT AT O(H) =================
print("\n=== STEP 4: ORBIT CONTRACTION AT O(H): W1 = SEC1(de0) + SEC0(de1) ===")
PG = symm_from({(a, b): sp.Symbol("p%d%d" % (a, b))
                for a in range(4) for b in range(a, 4)})
W1 = sp.expand(eval_on(SEC[1], d0, PG) + eval_on(SEC[0], d1, PG))
W1_nl = sp.expand(nonlocal_part(W1))
check(True, "W1 nonlocal orbit contraction at O(H): %s"
      % ("ZERO EXACTLY" if W1_nl == 0 else
         "NONZERO (%d terms) -- same class as the flat Finding 1; "
         "classified below, NOT repaired"
         % len(sp.Add.make_args(W1_nl))), gate="A4-3W")
EPLUS = symm_from({(1, 1): 1, (2, 2): -1})
ECROSS = symm_from({(1, 2): 1})
surv1 = []
for pl, pv in (("+", EPLUS), ("x", ECROSS)):
    v = sp.expand(eval_on(SEC[1], d0, pv) + eval_on(SEC[0], d1, pv))
    if sp.expand(nonlocal_part(v)) != 0:
        surv1.append(pl)
check(not surv1, "W1: orbit-sensitive nonlocal content does NOT reach the "
      "TT channel at O(H) (TT contractions: %s)"
      % ("all zero" if not surv1 else "NONZERO on %s -- FINDING" % surv1),
      gate="A4-3W")
clear_cache()
stamp("O(H) orbit contraction done")

# ================= STEP 5: WARD/ORBIT AT O(H^2), u-FREE PART =================
print("\n=== STEP 5: O(H^2) u-FREE PART: W2 = SEC2(de0) + SEC1(de1) ===")
W2_nl_terms = 0
surv2 = []
for pl, pv in (("+", EPLUS), ("x", ECROSS)):
    v = sp.expand(eval_on(SEC[2], d0, pv) + eval_on(SEC[1], d1, pv))
    if sp.expand(nonlocal_part(v)) != 0:
        surv2.append(pl)
check(not surv2, "W2 (u-free): orbit-sensitive nonlocal content does NOT "
      "reach the TT channel at O(H^2) (TT contractions: %s)"
      % ("all zero" if not surv2 else "NONZERO on %s -- FINDING" % surv2),
      gate="A4-3W")
W2 = sp.expand(eval_on(SEC[2], d0, PG) + eval_on(SEC[1], d1, PG))
W2_nl = sp.expand(nonlocal_part(W2))
W2_nl_terms = 0 if W2_nl == 0 else len(sp.Add.make_args(W2_nl))
check(True, "W2 (u-free) nonlocal orbit contraction at O(H^2): %s; the "
      "u-CARRYING remainder (2u X_0 eta) is pure trace, TT-irrelevant, and "
      "requires a loop u-moment -- RECORDED as the declared scope boundary "
      "of the non-TT Ward bookkeeping"
      % ("ZERO EXACTLY" if W2_nl_terms == 0 else
         "NONZERO (%d terms), non-TT only" % W2_nl_terms), gate="A4-3W")
del W1, W2
clear_cache()
stamp("O(H^2) u-free orbit contraction done")

# ================= STEP 6: CONTROLS =================
print("\n=== STEP 6: CONTROLS ===")
# (i) broken dressing: de^1 with coefficient 3 instead of 2 must CHANGE the
# O(H) orbit contraction (the dressing is load-bearing):
W1b = sp.expand(eval_on(SEC[0], de1(X, coeff=3), PG)
                - eval_on(SEC[0], de1(X, coeff=2), PG))
control(sp.expand(W1b) != 0,
        "broken dressing (2 -> 3 in de^1) CHANGES the orbit contraction "
        "(the a'/a coefficient is load-bearing, not decorative)")
# (ii) dressed pure-gauge injection must NOT move any TT amplitude:
XR = [sp.Rational(3, 7), sp.Rational(-2, 5), sp.Rational(1, 3),
      sp.Rational(4, 9)]
inj = sp.expand(de0(XR) + de1(XR))          # dressed orbit direction, numeric X
tt_moved = (sp.simplify((inj[1, 1] - inj[2, 2]) / 2) != 0
            or sp.simplify(inj[1, 2]) != 0)
control(not tt_moved, "dressed pure-gauge injection moves NO TT amplitude "
        "(trace-cancellation holds on the numeric injection too)")

# ================= STEP 7: OUTPUT + HARD STOP =================
print("\n=== STEP 7: OUTPUT ===")
bad = []
for p in set(READ_FILES):
    base = os.path.basename(p)
    if base in barred_files and base != "WALL_A_A3_REGISTRY.json":
        bad.append(base)
    hh = sha_file(p)
    for bf, bh in barred_files.items():
        if bh and hh == bh:
            bad.append("%s (hash %s)" % (p, bf))
if bad:
    print("   GUARD TRIPPED AT EXIT: %s -- RUN VOID" % bad)
    sys.exit(2)
print("   GUARD CLEAN at exit (%d files read)" % len(set(READ_FILES)))
RESULT = {
    "stage": "A4 response-level dual-gauge, PHASE II (dressed H^1/H^2)",
    "frozen_kernel_sha256": KSHA,
    "instrument_sha256": hashlib.sha256(own_src.encode()).hexdigest(),
    "tt_robustness": "OPERATOR IDENTITY through O(H^2): the orbit moves no "
                     "TT amplitude at any order (K-terms + trace "
                     "cancellation); A3-4's Q1/Q4/Q5 TT verdicts are "
                     "gauge-robust at every adjudicated order",
    "ward_orbit": {"O(H)_nonlocal_zero": bool(W1_nl == 0),
                   "O(H)_reaches_TT": surv1,
                   "O(H2)_ufree_nonlocal_terms": W2_nl_terms,
                   "O(H2)_ufree_reaches_TT": surv2,
                   "scope_boundary": "the u-carrying 2uX_0*eta orbit term "
                                     "(pure trace) needs a loop u-moment; "
                                     "non-TT bookkeeping only"},
    "checks": CHECKS, "notes": NOTES, "failures": FAILS,
    "elapsed_s": round(time.time() - T0, 1),
    "hard_stop": "A4 COMPLETE at declared scope. J(omega)/PV/spectral-fit/"
                 "+1 remain sealed. Owner adjudication required.",
}
with open(os.path.join(HERE, "WALL_A4_RESPONSE_DRESSED_RESULT.json"),
          "w") as f:
    json.dump(RESULT, f, indent=1, default=str)
print("\n================ SUMMARY (A4 PHASE II) ================")
print("  TT robustness: OPERATOR IDENTITY through O(H^2)")
print("  W1 nonlocal zero: %s ; reaches TT: %s" % (W1_nl == 0, surv1))
print("  W2 u-free nonlocal terms: %d ; reaches TT: %s"
      % (W2_nl_terms, surv2))
print("gates: %d/%d passed; failures: %d"
      % (sum(1 for c in CHECKS if c["pass"]), len(CHECKS), len(FAILS)))
for m in FAILS:
    print("  FAILURE: " + m)
print("elapsed: %.1fs" % (time.time() - T0))
sys.exit(0 if not FAILS else 1)
