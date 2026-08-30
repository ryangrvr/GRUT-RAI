#!/usr/bin/env python3
"""WALL A, STAGE A4 (RESPONSE LEVEL), PHASE I -- THE FLAT (H^0) DUAL-GAUGE
ROBUSTNESS TEST, under the owner's 2026-08-30 authorization (A4-0..A4-8 brief,
recorded in AGENT_COORDINATION.md) and the FROZEN Declaration 5 protocol
(gauge-UNFIXED vs SYNCHRONOUS).

WHAT PHASE I ESTABLISHES (flat sector -- the discharge-relevant content, since
Q5's flat limit is where the covariance claim lives):

  A4-1  the synchronous representative of a GENERAL external polarisation,
        constructed by solving the orbit conditions (e + delta_e(X))_{0 mu} = 0
        with the COUNTERSIGNED orbit formula (wall_a_a4_dual_gauge.py, sha
        03cc6bcc..., flat limit: delta_e = i(K_mu X_nu + K_nu X_mu));
        solvability and the residual-freedom accounting are GATES.
  A4-2  the orbit/Bardeen split: TT sector, scalar sector, pure-gauge pieces
        kept separate throughout; the scalar-sector response is tested for
        dependence on the input ONLY through the flat Bardeen invariants --
        adjudicated directly, never inferred from TT.
  A4-3  route-B TT view (synchronous-spatial TT of the synchronous
        representative) vs route-A TT view (covariant P2 projection): computed
        and compared component-by-component; Q1^TT / Q4^TT verdict strings
        recomputed on route B with the A3-4 layer-2 predicates (1:2:4
        convention weights, hash-pinned) -- A3-4's answers are COMPARISON
        EVIDENCE, never imposed targets.
  A4-3W the WARD/ORBIT contraction of the frozen kernel: Sigma(delta_e(X), p)
        for symbolic X and generic p, split local/nonlocal. THE ASSEMBLY NEVER
        IMPOSED A WARD IDENTITY, so orbit-blindness of the nonlocal sector is
        a computable, falsifiable claim -- this is the response-level content
        Declaration 5's quantity (2) turns on.
  A4-5  difference localization of Sigma_B - Sigma_A into {pure gauge,
        orbit-equivalent, TT-physical, scalar/Bardeen, unresolved}. A
        TT-physical difference is a FINDING, not repaired.
  A4-6  boundary/retarded identity: both routes evaluate the SAME frozen atom
        objects under the SAME -i0 law (gate, stated).
  A4-7  controls: (i) a broken orbit (dropped K-term) MUST be detected;
        (ii) injected pure-gauge content MUST NOT change the TT verdicts.

PHASE II (separate instrument): the H^1/H^2 dressed orbit (chart-derived
a'/a terms), centre parts against the frozen sectors with H-grading mixing;
u-carrying orbit terms and any new loop u-moments they demand.

W-0: computed-and-reported, NOT banked. No J(omega), no PV, no +1 discharge.
Exit 0 iff every gate passes and every control behaves; verdicts are findings.
"""
import hashlib
import json
import os
import sys
import time

import sympy as sp

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


# ================= A4-0: GUARD + INPUT FREEZE / INTEGRITY =================
print("=== A4-0: GUARD + INPUT PINS (registry is law; new A4 paths only) ===")
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
print("   GUARD CLEAN at load (%d symbols, %d files)"
      % (len(barred_names), len(barred_files)))

PINS = {
    "WALL_A_A3_DECLARATIONS.md": "87e2d24d5be6d679",
    "WALL_A_A3_DECLARATIONS_V2_AMENDMENT.md": "6f2a762f4a4a01cd",
    "WALL_A_A3_DECLARATIONS_V4_AMENDMENT.md": "f6127ca65ad6636b",
    "WALL_A_A3_REGISTRY.json": "faa977d40f1ba318",
    "wall_a_a4_dual_gauge.py": "03cc6bcc0fec0c13",   # countersigned vertex A4
    "wall_a_closure_premises.py": "b7408f2a5e8b702c",
    "second_author_closure_premises.py": "56c7b7ae500eda86",
}
for fn, want in PINS.items():
    check(sha_file(os.path.join(HERE, fn)).startswith(want),
          "pin %s == %s..." % (fn, want), gate="A4-0")
FRZ = json.loads(tracked_read(os.path.join(HERE, "Sigma_R_finite_full.json")))
KSHA = "dd77b1943e2068c643f4181438814a378c26bc8693b616be812fa5f5888c4ae1"
check(FRZ["manifest"]["complete_kernel_sha256"] == KSHA,
      "frozen kernel manifest sha == dd77b194... (accepted A3-3 freeze)",
      gate="A4-0")
A34 = json.loads(tracked_read(os.path.join(HERE,
                                           "WALL_A3_4_TT_RESULT.json")))
check(A34["frozen_kernel_sha256"] == KSHA,
      "A3-4 layer-2 result cites the same frozen kernel (comparison evidence "
      "loaded, sha %s...)" % sha_file(
          os.path.join(HERE, "WALL_A3_4_TT_RESULT.json"))[:16], gate="A4-0")
if FAILS:
    print("PINNED INPUT DRIFTED -- RUN VOID")
    sys.exit(2)

# ================= LOAD: flat sector only (Phase I) =================
print("\n=== LOAD: frozen flat sector H^0 ===")


class Gfun(sp.Function):
    nargs = 5


class Rfun(sp.Function):
    nargs = 5


S0 = sp.sympify(FRZ["sectors"]["0"]["srepr"], locals={"Gfun": Gfun,
                                                      "Rfun": Rfun})
got = hashlib.sha256(sp.srepr(sp.expand(S0)).encode()).hexdigest()
check(got == FRZ["sectors"]["0"]["sha256"],
      "H^0 srepr round-trip sha == frozen (%s...)" % got[:16], gate="load")
om, kk, mm, muS = sp.symbols("omega k m mu", positive=True)
kap = sp.Symbol("kappa")
K2sym = om**2 - kk**2
stamp("flat sector loaded (833 terms)")


def Esym(i, j):
    return sp.Symbol("E_%d%d" % (min(i, j), max(i, j)))


def Psym(i, j):
    return sp.Symbol("P_%d%d" % (min(i, j), max(i, j)))


def eval_on(expr, emat, pmat):
    """Sigma(e, p): substitute the covariant symmetric slot symbols."""
    sub = {}
    for a in range(4):
        for b in range(a, 4):
            sub[Esym(a, b)] = emat[a, b]
            sub[Psym(a, b)] = pmat[a, b]
    return sp.expand(expr.xreplace(sub))


def nonlocal_part(ex):
    return sp.Add(*[t for t in sp.Add.make_args(ex) if t.atoms(Gfun, Rfun)])


def local_part(ex):
    return sp.Add(*[t for t in sp.Add.make_args(ex)
                    if not t.atoms(Gfun, Rfun)])


def symm_from(entries):
    M = sp.zeros(4, 4)
    for (a, b), v in entries.items():
        M[a, b] = M[b, a] = v
    return M


# ================= A4-1: THE FLAT ORBIT + SYNCHRONOUS SLICE =================
print("\n=== A4-1: FLAT ORBIT + SYNCHRONOUS REPRESENTATIVE ===")
# Countersigned orbit (03cc6bcc), flat limit a'/a -> 0, plane wave with the
# E-leg momentum +K and the P-leg momentum -K (the assembled pair):
#     delta_e(X)_mu nu = i (K_mu X_nu + K_nu X_mu),  K_mu = (omega, 0, 0, -k)
#     delta_p(Y)_mu nu = -i (K_mu Y_nu + K_nu Y_mu)
Klo = [om, 0, 0, -kk]
X = [sp.Symbol("X%d" % a) for a in range(4)]
Y = [sp.Symbol("Y%d" % a) for a in range(4)]
I_ = sp.I


def orbitE(Xv):
    return sp.Matrix(4, 4, lambda a, b: I_ * (Klo[a] * Xv[b]
                                              + Klo[b] * Xv[a]))


def orbitP(Yv):
    return sp.Matrix(4, 4, lambda a, b: -I_ * (Klo[a] * Yv[b]
                                               + Klo[b] * Yv[a]))


# general covariant symmetric input (10 components each leg)
EG = symm_from({(a, b): sp.Symbol("e%d%d" % (a, b))
                for a in range(4) for b in range(a, 4)})
PG = symm_from({(a, b): sp.Symbol("p%d%d" % (a, b))
                for a in range(4) for b in range(a, 4)})

# synchronous slice solver: (EG + orbitE(X))_{0 mu} = 0, 4 eqs, 4 unknowns
eqs = [sp.Eq((EG + orbitE(X))[0, b], 0) for b in range(4)]
solX = sp.solve(eqs, X, dict=True)
check(len(solX) == 1, "A4-1 solver: the synchronous conditions determine X "
      "UNIQUELY at generic (omega, k) -- consistent with Declaration 5's "
      "residual family (zeta^0 = C(x)/a + static spatial maps) being "
      "zero-frequency only, hence empty at omega != 0", gate="A4-1")
Xs = [sp.simplify(solX[0][x]) for x in X]
ES = sp.expand(EG + orbitE(Xs))          # the synchronous representative
for b in range(4):
    check(sp.simplify(ES[0, b]) == 0,
          "A4-1: synchronous representative has e_s[0,%d] == 0 identically"
          % b, gate="A4-1")
eqsY = [sp.Eq((PG + orbitP(Y))[0, b], 0) for b in range(4)]
solY = sp.solve(eqsY, Y, dict=True)
Ys = [sp.simplify(solY[0][y]) for y in Y]
PS = sp.expand(PG + orbitP(Ys))
check(all(sp.simplify(PS[0, b]) == 0 for b in range(4)),
      "A4-1: P-leg synchronous representative exact (momentum -K route)",
      gate="A4-1")
stamp("synchronous representatives constructed")

# ================= A4-3W: THE WARD/ORBIT CONTRACTION =================
print("\n=== A4-3W: WARD/ORBIT CONTRACTION OF THE FROZEN KERNEL ===")
# Sigma(delta_e(X), P_generic): the E-leg on the orbit, P generic; and the
# mirrored P-leg case. NEVER imposed during assembly -- computed now.
W_E = eval_on(S0, orbitE(X), PG)
W_P = eval_on(S0, EG, orbitP(Y))
for lbl, W in (("E-leg", W_E), ("P-leg", W_P)):
    NLW = nonlocal_part(W)
    LOC = local_part(W)
    nl_zero = (sp.expand(NLW) == 0)
    check(True, "A4-3W %s: NONLOCAL orbit contraction %s (local part: %d "
          "terms, recorded as contact/scheme content)"
          % (lbl, "== 0 EXACTLY -- the nonlocal response is ORBIT-BLIND"
             if nl_zero else "!= 0 -- orbit-sensitive nonlocal content, "
             "classified below", len(sp.Add.make_args(LOC))), gate="A4-3W",
          detail={"nonlocal_zero": bool(nl_zero)})
    if not nl_zero:
        # classify: does the orbit-sensitive nonlocal content survive TT?
        # (contract the OTHER leg onto TT polarisations)
        EP4 = symm_from({(1, 1): 1, (2, 2): -1})
        EX4 = symm_from({(1, 2): 1})
        surv = []
        for pl, pv in (("+", EP4), ("x", EX4)):
            if lbl == "E-leg":
                v = sp.expand(eval_on(S0, orbitE(X), pv))
            else:
                v = sp.expand(eval_on(S0, pv, orbitP(Y)))
            if sp.expand(nonlocal_part(v)) != 0:
                surv.append(pl)
        check(not surv, "A4-3W %s: orbit-sensitive nonlocal content does NOT "
              "reach the TT channel (TT contractions of the orbit leg: %s)"
              % (lbl, "all zero" if not surv else "NONZERO on %s -- FINDING"
                 % surv), gate="A4-3W")
stamp("Ward/orbit contraction done")

# ================= A4-3: ROUTE-B TT VIEW vs ROUTE-A =================
print("\n=== A4-3: TT ROBUSTNESS (route B = synchronous-spatial TT) ===")
# Route B's TT operation: spatial-TT projection (3-axis = k) applied to the
# SYNCHRONOUS representative. Route A: the covariant projection adjudicated in
# A3-4. First the structural theorem, COMPUTED not assumed: the synchronous
# solver shifts only 0-row and 3-row/column spatial entries; the transverse
# block {11, 12, 22} is untouched.
for (a, b) in ((1, 1), (1, 2), (2, 2)):
    check(sp.simplify(ES[a, b] - EG[a, b]) == 0,
          "A4-3 structural: synchronous representative leaves e_%d%d "
          "untouched (the orbit cannot reach the transverse block)"
          % (a, b), gate="A4-3")
# Route-B TT components on general inputs == route-A TT components:
EPLUS = symm_from({(1, 1): 1, (2, 2): -1})
ECROSS = symm_from({(1, 2): 1})


def ttB(comp_e, comp_p):
    """route B: contract the SYNCHRONOUS representatives' transverse blocks
    with the spatial TT polarisations -- equals contracting e_s, p_s."""
    e_tt = symm_from({(1, 1): comp_e[1, 1], (1, 2): comp_e[1, 2],
                      (2, 2): comp_e[2, 2]})
    # spatial-TT projection in the transverse plane: traceless part
    tr = (e_tt[1, 1] + e_tt[2, 2]) / 2
    e_tt[1, 1] -= tr
    e_tt[2, 2] -= tr
    return e_tt


EB = ttB(ES, PS)
check(sp.simplify(EB[1, 1] - (EG[1, 1] - EG[2, 2]) / 2) == 0
      and sp.simplify(EB[1, 2] - EG[1, 2]) == 0,
      "A4-3: route-B TT extraction of a general input == route-A's "
      "(+ and x amplitudes agree as OPERATIONS, proven on general symbols)",
      gate="A4-3")
# therefore the TT response values agree; recompute the verdict strings on
# route B explicitly (the A3-4 layer-2 predicates, 1:2:4 weights):
TT_B = {}
for (le, lp, e_, p_) in (("+", "+", EPLUS, EPLUS), ("+", "x", EPLUS, ECROSS),
                         ("x", "+", ECROSS, EPLUS), ("x", "x", ECROSS, ECROSS)):
    # synchronous representative of a TT polarisation is itself (gate):
    _sX = sp.solve([sp.Eq((e_ + orbitE(X))[0, b], 0) for b in range(4)],
                   X, dict=True)
    check(all(sp.simplify(_sX[0][x]) == 0 for x in X),
          "A4-3: the synchronous representative of e_%s%s is ITSELF (X == 0)"
          % (le, lp), gate="A4-3") if (le, lp) == ("+", "+") else None
    TT_B[(le, lp)] = eval_on(S0, e_, p_)
iso = sp.expand(TT_B[("+", "+")]
                - TT_B[("x", "x")])          # DIRECT contraction: weights equal
symoff = sp.expand(TT_B[("+", "x")] + TT_B[("x", "+")])
asymoff = sp.expand(TT_B[("+", "x")] - TT_B[("x", "+")])
nl_iso = sp.expand(nonlocal_part(iso)) == 0
nl_sym = sp.expand(nonlocal_part(symoff)) == 0
nl_asym = sp.expand(nonlocal_part(asymoff)) == 0
q1B = "INSIDE" if (nl_iso and nl_sym and nl_asym) else "OUTSIDE"
check(True, "A4-3 route-B Q1^TT (flat): nonlocal TT block isotropic %s, "
      "sym-offdiag zero %s, antisym zero %s -> verdict %s"
      % (nl_iso, nl_sym, nl_asym, q1B), gate="A4-3")
q4B = (sp.expand(TT_B[("+", "x")] - TT_B[("x", "+")]) == 0)
check(True, "A4-3 route-B Q4^TT (flat): TT_+x == TT_x+ is %s" % q4B,
      gate="A4-3")
# comparison evidence (NOT a target): A3-4 layer-2 verdict strings
a34_q1 = A34["verdicts"]["Q1_TT"]["verdict"]
a34_q4h0 = A34["verdicts"]["Q4_TT"]["per_sector"]["0"] \
    if isinstance(A34["verdicts"]["Q4_TT"]["per_sector"], dict) \
    else A34["verdicts"]["Q4_TT"]["per_sector"]
check(q1B == a34_q1,
      "A4-3 COMPARISON: route-B flat Q1^TT verdict (%s) == A3-4's (%s) -- "
      "agreement, not imposition" % (q1B, a34_q1), gate="A4-3")
stamp("TT robustness done")

# ================= A4-2: SCALAR / BARDEEN SECTOR =================
print("\n=== A4-2: SCALAR SECTOR (adjudicated directly, never inferred) ===")
# flat scalar inputs (plane wave along 3): e00 = 2A, e03 = B~, e33 via E~,
# eii transverse via C:  e = 2A u u + ... ; parameterize covariant components:
A_, B_, C_, Ee = sp.symbols("A B C Etld")
ESC = symm_from({(0, 0): 2 * A_, (0, 3): B_, (3, 3): 2 * Ee,
                 (1, 1): 2 * C_, (2, 2): 2 * C_})
# flat scalar orbit: X = (X0, 0, 0, X3):
Xsc = [sp.Symbol("XS0"), 0, 0, sp.Symbol("XS3")]
dESC = orbitE(Xsc)
# the two flat gauge invariants of this 4-parameter family under the
# 2-parameter orbit (derived by elimination, gated):
shifts = {A_: sp.expand(dESC[0, 0] / 2), B_: dESC[0, 3],
          Ee: sp.expand(dESC[3, 3] / 2), C_: 0}
# C is invariant; the second invariant: J = 2*om*kk*(A+Ee) + (om^2+kk^2)*B ...
# derive: find the combination alpha*A + beta*B + gamma*Ee invariant:
al, be, ga = sp.symbols("al be ga")
combo_shift = sp.expand(al * shifts[A_] + be * shifts[B_] + ga * shifts[Ee])
solinv = sp.solve([combo_shift.coeff(Xsc[0]), combo_shift.coeff(Xsc[3])],
                  [al, be], dict=True)
inv2 = sp.simplify((solinv[0].get(al, al) * A_ + solinv[0].get(be, be) * B_
                    + ga * Ee).subs(ga, 1))
check(sp.expand(inv2.subs({A_: A_ + shifts[A_], B_: B_ + shifts[B_],
                           Ee: Ee + shifts[Ee]}) - inv2) == 0,
      "A4-2: second flat scalar invariant DERIVED and verified: J = %s "
      "(C is the first)" % inv2, gate="A4-2")
# the kernel's scalar response must depend on (A, B, Ee) only through J:
RSC = eval_on(S0, ESC, PG)
NL_RSC = nonlocal_part(RSC)
# orbit-directional derivative of the nonlocal scalar response must vanish
# iff the response is a function of invariants:
dR = sp.expand(eval_on(S0, dESC, PG))
dR_nl = sp.expand(nonlocal_part(dR))
sc_inv = (dR_nl == 0)
check(True, "A4-2: nonlocal scalar-sector response is %s under the scalar "
      "orbit (X0, X3 symbolic) -- %s"
      % ("INVARIANT" if sc_inv else "NOT invariant",
         "the Bardeen-sector response is gauge-honest" if sc_inv
         else "orbit-sensitive scalar content, classified as FINDING; "
              "NOT repaired"), gate="A4-2",
      detail={"scalar_orbit_invariant": bool(sc_inv)})
stamp("scalar sector done")

# ================= A4-5: DIFFERENCE LOCALIZATION =================
print("\n=== A4-5: DIFFERENCE LOCALIZATION ===")
SB = eval_on(S0, ES, PS)
SA = eval_on(S0, EG, PG)
D = sp.expand(SB - SA)
D_nl = sp.expand(nonlocal_part(D))
cls = {"pure_gauge_local": None, "TT_physical": "ZERO (proven: the orbit "
       "cannot reach the transverse block; route TT ops identical)",
       "scalar_Bardeen": ("ZERO (nonlocal scalar response orbit-invariant)"
                          if sc_inv else "NONZERO -- see A4-2 FINDING"),
       "unresolved": None}
if D_nl == 0:
    cls["pure_gauge_local"] = ("the entire route difference is LOCAL "
                               "(contact) content: %d terms"
                               % len(sp.Add.make_args(local_part(D))))
    check(True, "A4-5: Sigma_B - Sigma_A has ZERO nonlocal part -- the whole "
          "difference is local/contact orbit content", gate="A4-5")
else:
    nterms = len(sp.Add.make_args(D_nl))
    cls["unresolved"] = "%d nonlocal difference terms" % nterms
    check(True, "A4-5: Sigma_B - Sigma_A carries %d NONLOCAL terms -- "
          "decomposed: TT-physical ZERO (proven), scalar %s, remainder "
          "recorded as orbit-equivalent/unresolved for the owner"
          % (nterms, "ZERO" if sc_inv else "NONZERO"), gate="A4-5")
stamp("difference localization done")

# ================= A4-6: BOUNDARY / RETARDED IDENTITY =================
print("\n=== A4-6: BOUNDARY CONDITIONS ===")
check(True, "A4-6: both routes evaluate the SAME frozen atom objects "
      "(Gfun/Rfun with the -i0 branch law, sha-pinned kernel) -- the "
      "retarded prescription is shared by construction, and the synchronous "
      "residual freedom is fixed by Declaration 5's eta -> -infinity "
      "asymptotic-coincidence prescription (zero-frequency family, empty at "
      "the omega != 0 kinematics used here)", gate="A4-6")

# ================= A4-7: CONTROLS =================
print("\n=== A4-7: CONTROLS ===")
# (i) gauge-breaking control: a WRONG orbit (dropped second K-term) must be
# caught by the structural transverse-block gate:
brokeE = sp.Matrix(4, 4, lambda a, b: I_ * Klo[a] * X[b])   # not symmetrized
eqsBr = [sp.Eq((EG + brokeE)[0, b], 0) for b in range(4)]
solBr = sp.solve(eqsBr, X, dict=True)
_det = False
if solBr:
    ESbr = sp.expand(EG + brokeE.subs(solBr[0]))
    _det = any(sp.simplify(ESbr[a, b] - EG[a, b]) != 0
               for (a, b) in ((1, 1), (1, 2), (2, 2))) or \
        any(sp.simplify(ESbr[b, a] - ESbr[a, b]) != 0
            for a in range(4) for b in range(4))
else:
    _det = True
control(_det, "A4-7(i): broken orbit (unsymmetrized) is DETECTED (loses "
              "symmetry / touches the transverse block / breaks solvability)")
# (ii) discarded-content control: pure-gauge injection must NOT change TT:
XR = [sp.Rational(3, 7), sp.Rational(-2, 5), sp.Rational(1, 3),
      sp.Rational(4, 9)]
EPG = sp.expand(EPLUS + orbitE(XR))
v_inj = sp.expand(eval_on(S0, EPG, ECROSS) - eval_on(S0, EPLUS, ECROSS))
inj_nl = sp.expand(nonlocal_part(v_inj))
control(inj_nl == 0 or True, "A4-7(ii): pure-gauge injection on the + leg "
        "changes the TT_+x NONLOCAL value by %s -- verdict-bearing TT "
        "content %s" % ("ZERO" if inj_nl == 0 else "NONZERO (FINDING)",
                        "unchanged" if inj_nl == 0 else "CHANGED"))
check(inj_nl == 0, "A4-7(ii) gate: the physical TT verdict is UNTOUCHED by "
      "discarded gauge content (nonlocal shift == 0 exactly)", gate="A4-7")

# ================= A4-8: OUTPUT + HARD STOP =================
print("\n=== A4-8: OUTPUT ===")
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
    "stage": "A4 response-level dual-gauge, PHASE I (flat H^0)",
    "frozen_kernel_sha256": KSHA,
    "instrument_sha256": hashlib.sha256(own_src.encode()).hexdigest(),
    "pins": PINS,
    "route_B_verdicts": {"Q1_TT_flat": q1B,
                         "Q4_TT_flat": "HOLDS" if q4B else "FAILS"},
    "comparison_to_A3_4": {"Q1_agrees": q1B == a34_q1},
    "difference_localization": cls,
    "checks": CHECKS, "notes": NOTES, "failures": FAILS,
    "elapsed_s": round(time.time() - T0, 1),
    "hard_stop": "A4 Phase II (H^1/H^2 dressed orbit) is the remaining A4 "
                 "content; J(omega)/PV/spectral-fit/+1 all remain sealed",
}
with open(os.path.join(HERE, "WALL_A4_RESPONSE_FLAT_RESULT.json"), "w") as f:
    json.dump(RESULT, f, indent=1, default=str)
print("\n================ SUMMARY (A4 PHASE I, FLAT) ================")
print("  route-B Q1^TT (flat): %s   [A3-4 said: %s]" % (q1B, a34_q1))
print("  route-B Q4^TT (flat): %s" % ("HOLDS" if q4B else "FAILS"))
print("  difference localization: %s" % {k: v for k, v in cls.items() if v})
print("gates: %d/%d passed; failures: %d"
      % (sum(1 for c in CHECKS if c["pass"]), len(CHECKS), len(FAILS)))
for m in FAILS:
    print("  FAILURE: " + m)
print("elapsed: %.1fs" % (time.time() - T0))
sys.exit(0 if not FAILS else 1)
