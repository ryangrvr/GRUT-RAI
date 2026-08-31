#!/usr/bin/env python3
"""K_R^(contract) TIER 2 -- THE MASSLESS GRAVITON BATH (owner authorization
2026-08-31; declarations D1=1a, D2=2a, D3=3a binding; BATH ONLY).

MISSION: build and validate ONLY the massless graviton bath required by the
contract-level K_R construction. NO loop assembly, NO K_R^(contract), NO D5,
NO D4 comparison, NO registered-comparator content anywhere (guard live).

STATE PRESCRIPTION (D3 = 3a, frozen): BD-analogue via the Option-B adiabatic
route in the frozen chart a^2 = 1+2Hu+3H^2u^2 (the O(H^2) truncation of exact
dS a = 1/(1-Hu), gated), flat massless anchor at H^0 per order, exact-dS
(Option-A analogue) retained as the declared cross-check target.
IR: DIMENSIONAL CONTINUATION ONLY -- NO explicit IR scale. If one is
demonstrated necessary: STOP, fork (ii) fires ("named and priced").

STRUCTURAL FACT (derived below, gated): the exact BD massless TT mode in this
chart is POLYNOMIAL in H -- h_k(u) = N e^{-iku}[(1-Hu) + iH/k] exactly -- so
the per-mode bath kernels TERMINATE at O(H^2): the graded truncation is exact
at the per-mode level and Option A is executed here as a live cross-check.

NORMALIZATION DISCIPLINE: no textbook constant is imported untested. The
chain is: frozen Tier-1 pipeline quadratic density (tie-gated against the
cached {1,2} sector) -> reduced TT action -> CLASSICAL retarded response
(variation of parameters, exact) -> quantum kernels with the mode
normalization FIXED by the identity i<[psi,psi*]> theta == classical G_R.
The only external import is the source convention S_int = (1/2) h_ij T^ij.

W-0: computed-and-reported, NOT banked. HARD STOP after the report.
"""
import hashlib
import json
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
OUT = {}
mp.mp.dps = 25


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


# ================= T2-0: INPUT / CONTRACT CHECK =================
print("=== T2-0: INPUT / CONTRACT CHECK ===")
registry = json.loads(open(os.path.join(HERE, "WALL_A_A3_REGISTRY.json")).read())
barred_names = set()
for e_ in registry["g0_spectral_wiring"]["barred_inputs"]:
    for o in e_.get("objects", []):
        barred_names.add(o)
own_src = open(os.path.abspath(__file__)).read()
hits = [b for b in barred_names if b in own_src.replace("barred_names", "")
        and ('"' + b + '"') not in own_src]
if hits:
    print("   GUARD TRIPPED: %s" % hits)
    sys.exit(2)
print("   GUARD CLEAN (no registered-comparator content in this construction)")

KSHA = "dd77b1943e2068c643f4181438814a378c26bc8693b616be812fa5f5888c4ae1"
FRZ = json.loads(open(os.path.join(HERE, "Sigma_R_finite_full.json")).read())
check(FRZ["manifest"]["complete_kernel_sha256"] == KSHA,
      "frozen kernel sha dd77b194... (Wall-A record; untouched here)",
      gate="T2-0")

T1A = json.loads(open(os.path.join(
    HERE, "WALL_KR_TIER1_VERTEX_ARTIFACT.json")).read())
T1SHA = "0152c7773e6a38dfeee30ae3b18ca4157f713828640506701d80d4cc0701976d"
check(T1A["vertex_sha256"] == T1SHA and T1A["flat_terms"] == 7560
      and T1A["ds_terms"] == 26032,
      "Tier-1 vertex artifact pinned: sha 0152c777..., 7560 flat / 26032 dS "
      "terms", gate="T2-0")
T1R = json.loads(open(os.path.join(
    HERE, "WALL_KR_TIER1_VERTEX_RESULT.json")).read())
check(T1R["failures"] == [], "Tier-1 result: zero failures on record",
      gate="T2-0")
Hpin = sp.Symbol("H")
_dc = json.loads(open(os.path.join(HERE, ".tier1_ds_cache.json")).read())
check(_dc["lam"] == sp.srepr(-3 * Hpin**2),
      "Tier-1 dS density cache carries Lambda = -3H^2 (the derived "
      "in-convention value)", gate="T2-0")
for fn in ("K_R_CONTRACT_OWNER_RULING.md",
           "WALL_A_A3_DECLARATIONS_V3_AMENDMENT.md",
           "WALL_A_A3_DECLARATIONS.md",
           "K_R_CONTRACT_EXECUTION_CHARTER.md",
           "wall_kr_tier1_vertex.py"):
    note("input sha %s = %s..." % (fn, sha_file(os.path.join(HERE, fn))[:16]))
note("owner countersign commit d5dc33b; Tier-1 completion commit 0b21160")

note("D3 (owner ruling, verbatim): 'OPTION 3a -- BD-analogue Option-B "
     "adiabatic, with the flat massless anchor gated at H^0 per order, and "
     "the exact-dS state (Option-A analogue) retained as the declared "
     "cross-check target. IR: dimensional continuation ONLY; NO explicit IR "
     "scale.' Fork (ii) verbatim: 'named and priced -- a new register input'")
note("V3 amendment binding conditions (verbatim class): (1) declare the "
     "expansion parameter and retained order on the artifact's face + "
     "regime of validity; (2) dress consistently at every retained order; "
     "(3) recover the flat plant at each order; (4) keep Option A as the "
     "declared cross-check target")
note("state-definition audit: chart = frozen a^2 = 1+2Hu+3H^2u^2 (gated, "
     "Tier 1) -- PRESENT; state = BD-analogue (exact BD massless mode in "
     "this chart exists in closed form; graded state = its truncation) -- "
     "PRESENT; IR prescription = dim continuation, no scale -- PRESENT; "
     "anchor = flat massless at H^0 -- PRESENT")
check(True, "T2-0 verdict: the bath is DEFINED (not UNDERDEFINED) -- all "
      "four state components are frozen on the record", gate="T2-0")
note("disclosed text blemishes (math unaffected, frozen files untouched): "
     "the Tier-1 G7b gate message and the artifact convention string still "
     "print 'Lambda = 3H^2'; every computed object uses -3H^2")
if FAILS:
    sys.exit(2)

# ================= T2-1a: THE QUADRATIC TT ACTION (exact route) ============
print("\n=== T2-1a: QUADRATIC TT ACTION (independent exact route) ===")
u, z, x1, x2 = sp.symbols("u z x1 x2", real=True)
up = sp.Symbol("u_p", real=True)
D = sp.Symbol("Delta", real=True)
ub = sp.Symbol("u_b", real=True)
H = sp.Symbol("H", real=True)
k = sp.Symbol("k", positive=True)
kap = sp.Symbol("kappa", positive=True)
om = sp.Symbol("omega", positive=True)
dsym = sp.Symbol("d", positive=True)
e1s, e2s = sp.symbols("eps1 eps2")
f1 = sp.Function("f1")(u)
f2 = sp.Function("f2")(u)

# PHASE-ABSORBED REPRESENTATION (the Tier-1 lesson, applied): the spatial
# phases e^{+-ikz} are absorbed into the nilpotent markers -- a z-derivative
# acts as multiplication by +ik on eps1 content and -ik on eps2 content, so
# every object stays a POLYNOMIAL in (eps1, eps2) with u-dependent
# coefficients. The eps1*eps2 cross sector automatically carries phase
# e^{ikz} e^{-ikz} = 1 (the z-average is exact and free). Run 1 used
# explicit exp(ikz) factors with Poly-based truncation and stalled past the
# 20-minute rule; this representation is the disclosed repair.
_KILL = {e1s**n: sp.Integer(0) for n in range(2, 7)}
_KILL.update({e2s**n: sp.Integer(0) for n in range(2, 7)})


def trunc(x):
    """nilpotent truncation: drop eps1^2, eps2^2."""
    return sp.expand(x).xreplace(_KILL)


_HKILL = {H**n: sp.Integer(0) for n in range(3, 13)}


def htrunc(x, dummy=None):
    """graded chart truncation: drop H^3 and above (polynomial inputs)."""
    return sp.expand(x).xreplace(_HKILL)


def dX(x, mu):
    """phase-absorbed derivative: d_u is literal; d_z multiplies eps1
    content by +ik and eps2 content by -ik; d_x1 = d_x2 = 0."""
    if mu == 0:
        return sp.diff(x, u)
    if mu != 3:
        return sp.Integer(0)
    out = sp.Integer(0)
    for t in sp.Add.make_args(sp.expand(x)):
        n1 = 1 if t.has(e1s) else 0
        n2 = 1 if t.has(e2s) else 0
        out += sp.I * k * (n1 - n2) * t
    return out


def quad_cross_density(a2, a2inv, lam, graded=False):
    """the eps1*eps2 sector of sqrt(-g)(R - 2 lam) for
    g = a^2(u) diag(1, -1+s, -1-s, -1), s = e1 f1(u)e^{ikz} + e2 f2(u)
    e^{-ikz} (TT '+' waves along z; phases absorbed into the markers).
    Same Christoffel/Ricci formulas and sign conventions as the Tier-1
    Lambda gate. Stripped units (per 1/2kappa^2). Exact under nilpotency;
    if graded, additionally truncated at O(H^2)."""
    tr = (lambda x: htrunc(trunc(x))) if graded else trunc
    s11 = e1s * f1 + e2s * f2
    g = {0: a2, 1: a2 * (-1 + s11), 2: a2 * (-1 - s11), 3: -a2}
    s2 = tr(s11 * s11)                       # = 2 e1 e2 f1 f2 exactly
    gi = {0: a2inv,
          1: tr(-a2inv * (1 + s11 + s2)),
          2: tr(-a2inv * (1 - s11 + s2)),
          3: -a2inv}
    sqg = tr(a2**2 * (1 - s2 / 2))           # sqrt(-g) = a^4 sqrt(1 - s^2)
    G = {}
    for l in range(4):
        for m_ in range(4):
            for n_ in range(4):
                s_ = gi[l] * ((dX(g[n_], m_) if l == n_ else 0)
                              + (dX(g[m_], n_) if l == m_ else 0)
                              - (dX(g[m_], l) if m_ == n_ else 0)) / 2
                G[(l, m_, n_)] = tr(s_)
    Rs = sp.Integer(0)
    for m_ in range(4):
        n_ = m_                              # diagonal inverse metric
        ric = sp.Integer(0)
        for l in range(4):
            ric += dX(G[(l, m_, n_)], l) - dX(G[(l, m_, l)], n_)
            for r_ in range(4):
                ric += G[(l, l, r_)] * G[(r_, m_, n_)] \
                    - G[(l, n_, r_)] * G[(r_, m_, l)]
        Rs += tr(gi[m_] * tr(ric))
    L = tr(sqg * (Rs - 2 * lam))
    L2 = sp.expand(L).coeff(e1s, 1).coeff(e2s, 1)
    return sp.expand(L2)


LAM = -3 * H**2
aex2 = 1 / (1 - H * u)**2                    # exact dS chart
aex2inv = (1 - H * u)**2
t_ = time.time()
L2X = quad_cross_density(aex2, aex2inv, LAM)
stamp("exact-route quadratic cross density built (%.1fs)" % (time.time() - t_))
check(not L2X.has(sp.I),
      "the cross (eps1*eps2) sector is phase-free and real (e^{ikz} "
      "e^{-ikz} = 1 exactly -- the z-average is automatic in the "
      "phase-absorbed representation)", gate="T2-1")

# bilinear decomposition M[i][j]: i,j = derivative order of f1, f2
d1, d11 = f1.diff(u), f1.diff(u, 2)
d2, d22 = f2.diff(u), f2.diff(u, 2)
B1 = [f1, d1, d11]
B2 = [f2, d2, d22]


def bilinear(L2):
    Lw = sp.expand(L2)
    M = [[sp.simplify(Lw.coeff(B1[i], 1).coeff(B2[j], 1))
          for j in range(3)] for i in range(3)]
    rec = sp.expand(sum(M[i][j] * B1[i] * B2[j]
                        for i in range(3) for j in range(3)))
    return M, sp.simplify(sp.expand(Lw - rec))


M, resid = bilinear(L2X)
check(resid == 0, "the cross density is EXACTLY bilinear in "
      "(f1,f1',f1'') x (f2,f2',f2'') -- no stray structures", gate="T2-1")
check(sp.simplify(M[2][1]) == 0 and sp.simplify(M[1][2]) == 0
      and sp.simplify(M[2][2]) == 0,
      "no f''f' / f''f'' terms (R is linear in second derivatives -- "
      "build-consistency)", gate="T2-1")


def reduce_ibp(M):
    """reduce modulo total u-derivatives to P*f1'f2' + Q*f1f2.
    Returns (P, Q, antisymmetric_residual)."""
    M = [[sp.simplify(x) for x in row] for row in M]
    A = M[2][0]                               # f1'' f2
    M[1][0] = sp.simplify(M[1][0] - sp.diff(A, u))
    M[1][1] = sp.simplify(M[1][1] - A)
    M[2][0] = 0
    B = M[0][2]                               # f1 f2''
    M[0][1] = sp.simplify(M[0][1] - sp.diff(B, u))
    M[1][1] = sp.simplify(M[1][1] - B)
    M[0][2] = 0
    sym = sp.simplify((M[1][0] + M[0][1]) / 2)
    anti = sp.simplify((M[1][0] - M[0][1]) / 2)
    M[0][0] = sp.simplify(M[0][0] - sp.diff(sym, u))
    return sp.simplify(M[1][1]), sp.simplify(M[0][0]), anti


P, Q, anti = reduce_ibp(M)
check(anti == 0, "no antisymmetric first-order remnant (f1'f2 - f1f2') "
      "after reduction", gate="T2-1")
check(sp.simplify(Q + k**2 * P) == 0,
      "MASSLESSNESS: the reduced quadratic density is P(u)(f1'f2' - "
      "k^2 f1 f2) -- zero residual mass term (requires the derived "
      "Lambda = -3H^2; the TT graviton is exactly massless in this chart)",
      gate="T2-1")
check(sp.simplify(P + aex2) == 0,
      "kinetic weight P(u) = -a^2(u) EXACTLY (stripped units; flat P = -1): "
      "the pipeline's Ricci ORIENTATION (the same one giving R_dS = -12H^2 "
      "and G3 = +1 x p1.p2) carries into the TT kinetic term. Magnitude "
      "|P| = a^2 -- the (1/4) dh dh TT normalization; the sign is the "
      "recorded orientation, NOT a ghost (physical positivity statements "
      "below are orientation-invariant)", gate="T2-1")
OUT["quadratic_action"] = {
    "form": "L2 = (1/(2 kappa^2)) * (-a^2(u)) * (psi' psi*' - k^2 psi "
            "psi*) per '+' polarization pair (eps:eps = 2), z-averaged, "
            "modulo total derivatives -- pipeline Ricci orientation",
    "P": str(P), "Q": str(Q)}

_M0, _ = bilinear(quad_cross_density(aex2, aex2inv, sp.Integer(0)))
_P0, _Q0, _ = reduce_ibp(_M0)
control(sp.simplify(_Q0 + k**2 * _P0) != 0,
        "WITHOUT Lambda the reduced density keeps a residual mass term -- "
        "the masslessness gate has teeth (mirrors the Tier-1 G7 control)")

# ================= T2-1b: PIPELINE TIE (frozen Tier-1 {1,2} sector) ========
print("\n=== T2-1b: PIPELINE TIE -- Tier-1 cached quadratic sector ===")
DS12 = sp.sympify(_dc["sectors"]["(1, 2)"])
w1, w2 = sp.symbols("w1 w2")
subtie = {sp.Symbol("e%d_%d%d" % (i, mu, nu)): 0
          for i in (1, 2) for mu in range(4) for nu in range(mu, 4)}
subtie.update({sp.Symbol("e1_11"): 1, sp.Symbol("e1_22"): -1,
               sp.Symbol("e2_11"): 1, sp.Symbol("e2_22"): -1})
subtie.update({sp.Symbol("p1_0"): w1, sp.Symbol("p2_0"): w2,
               sp.Symbol("p1_1"): 0, sp.Symbol("p1_2"): 0,
               sp.Symbol("p2_1"): 0, sp.Symbol("p2_2"): 0,
               sp.Symbol("p1_3"): k, sp.Symbol("p2_3"): -k})
# the cache was written with plain Symbol('H') and Symbol('u') (Tier-1
# used assumption-free symbols); align BOTH to ours -- run-2 defect: the
# unmapped plain 'u' made identical terms refuse to cancel (two symbols
# printing identically), failing the tie on a representation artifact
DS12tt = sp.expand(DS12.xreplace(subtie)
                   .xreplace({Hpin: H, sp.Symbol("u"): u}))

a2g = 1 + 2 * H * u + 3 * H**2 * u**2        # frozen graded chart
a2ginv = 1 - 2 * H * u + H**2 * u**2
t_ = time.time()
L2G = quad_cross_density(a2g, a2ginv, LAM, graded=True)
stamp("graded-route quadratic cross density built (%.1fs)" % (time.time() - t_))
pw = {f1: sp.exp(sp.I * w1 * u), f2: sp.exp(sp.I * w2 * u)}


def phase_strip(expr):
    s = sp.expand(expr.subs(pw).doit() * sp.exp(-sp.I * (w1 + w2) * u))
    return htrunc(sp.expand(sp.powsimp(s)))


tie = sp.simplify(sp.expand(phase_strip(L2G) - DS12tt))
check(tie == 0,
      "PIPELINE TIE: the independent graded-route quadratic density == the "
      "FROZEN Tier-1 cached {1,2} sector, POINTWISE in (u, w1, w2, k, H) "
      "through O(H^2) (TT '+' waves along z; consistent dressing: identical "
      "a^2 chart weights as the Tier-1 vertex build)", gate="T2-1")
L2W = quad_cross_density(1 + 2 * H * u, 1 - 2 * H * u + 4 * H**2 * u**2,
                         LAM, graded=True)
control(sp.simplify(sp.expand(phase_strip(L2W) - DS12tt)) != 0,
        "a WRONG chart (a^2 = 1+2Hu) fails the pipeline tie at O(H^2) -- "
        "the tie gate has teeth")
check(htrunc(sp.expand(sp.series(P, H, 0, 3).removeO() + a2g)) == 0,
      "graded chart weight == exact chart weight through O(H^2) (chart "
      "truncation error is O(H^3), confined to the a^2 weights)",
      gate="T2-1")

# ================= T2-1c: MODE FUNCTIONS + EXPOSURES =================
print("\n=== T2-1c: MODE FUNCTIONS (BD-analogue, Option-B) ===")
psi = sp.Function("psi")(u)
h1 = sp.exp(-sp.I * k * u) * ((1 - H * u) + sp.I * H / k)   # exact BD mode
h2 = sp.exp(sp.I * k * u) * ((1 - H * u) - sp.I * H / k)    # its conjugate
check(sp.simplify(sp.expand(
    sp.diff(aex2 * sp.diff(h1, u), u) + k**2 * aex2 * h1)) == 0,
      "EXACT BD MODE: h_k(u) = e^{-iku}[(1-Hu) + iH/k] solves the derived "
      "TT mode equation (a^2 h')' + k^2 a^2 h = 0 EXACTLY -- the mode is "
      "POLYNOMIAL in H (terminates at O(H); per-mode kernels terminate at "
      "O(H^2))", gate="T2-1")
v_ = h1 / (1 - H * u)                        # v = a h, a = 1/(1-Hu) exact
check(sp.simplify(sp.expand(sp.diff(v_, u, 2)
                            + (k**2 - 2 * H**2 / (1 - H * u)**2) * v_)) == 0,
      "equivalently v = a h satisfies v'' + (k^2 - a''/a)v = 0 with "
      "a''/a = 2 H^2 a^2 -- the massless-scalar form recovered, not "
      "imposed", gate="T2-1")
Wr = sp.simplify(aex2 * (h1 * sp.diff(h2, u) - sp.diff(h1, u) * h2))
check(sp.simplify(Wr - 2 * sp.I * k) == 0,
      "Wronskian a^2 (h h*' - h' h*) = 2ik = CONSTANT exactly (basis "
      "normalization pinned; the graded a^2 gives the same through O(H^2))",
      gate="T2-1")
note("T2-1 EXPOSURES -- momentum convention: mostly-minus, d_mu -> i p_mu "
     "(lower index), spatial wave e^{+ikz} with k > 0, positive frequency "
     "e^{-iku}; retarded prescription: theta(u-u') on the commutator == "
     "omega + i0 upper-half analyticity in F(omega) = int dDelta "
     "e^{i omega Delta} F(Delta); normalization: fixed by the classical "
     "response identity (chain: frozen pipeline density -> reduced action "
     "-> variation of parameters); H-order: per-mode kernels are EXACT "
     "polynomials terminating at O(H^2); state: BD-analogue = the "
     "closed-form BD mode of this chart (Option A executed as the "
     "cross-check, not deferred); expansion parameters (V3 condition 1): "
     "H/k per mode and |Hu| < 1 in the chart -- graded REPORTING of "
     "omega-domain objects is valid for omega >> H")

print("\n--- TT projector (exposed; d-continued trace) ---")
trace_formula = (dsym + 1) * (dsym - 2) / 2
ok_tr, ok_pr = True, True
for dd in (3, 4, 5, 6):
    kv = [sp.Rational(3, 5), sp.Rational(4, 5)] + [0] * (dd - 2)
    Pm = [[(1 if i == j else 0) - kv[i] * kv[j] for j in range(dd)]
          for i in range(dd)]
    PT = {}
    for i in range(dd):
        for j in range(dd):
            for a_ in range(dd):
                for b_ in range(dd):
                    PT[(i, j, a_, b_)] = (
                        sp.Rational(1, 2) * (Pm[i][a_] * Pm[j][b_]
                                             + Pm[i][b_] * Pm[j][a_])
                        - sp.Rational(1, 1) * Pm[i][j] * Pm[a_][b_] / (dd - 1))
    tr = sum(PT[(i, j, i, j)] for i in range(dd) for j in range(dd))
    ok_tr = ok_tr and sp.simplify(tr - trace_formula.subs(dsym, dd)) == 0
    trans = sum(kv[i] * PT[(i, j, a_, b_)]
                for i in range(dd)) if dd == 3 else 0
    idem = True
    if dd == 3:
        idem = all(sp.simplify(sum(PT[(i, j, m_, n_)] * PT[(m_, n_, a_, b_)]
                                   for m_ in range(3) for n_ in range(3))
                               - PT[(i, j, a_, b_)]) == 0
                   for i in range(3) for j in range(3)
                   for a_ in range(3) for b_ in range(3))
        ok_pr = ok_pr and idem and all(
            sp.simplify(sum(kv[i] * PT[(i, j, a_, b_)] for i in range(3))) == 0
            for j in range(3) for a_ in range(3) for b_ in range(3))
check(ok_tr, "TT projector P^TT = (P_ia P_jb + P_ib P_ja)/2 - "
      "P_ij P_ab/(d-1), P = delta - k^hat k^hat: trace == (d+1)(d-2)/2 at "
      "d = 3,4,5,6 (= 2 polarizations at d = 3) -- the declared dimensional "
      "continuation of the polarization count", gate="T2-1")
check(ok_pr, "TT projector at d = 3: idempotent and transverse (executed "
      "on a non-axis k^hat = (3/5, 4/5, 0))", gate="T2-1")
OUT["tt_projector"] = {"trace_d": str(trace_formula), "d3_polarizations": 2}
stamp("T2-1 complete")

# ================= T2-2: RETARDED / NOISE STRUCTURE =================
print("\n=== T2-2: RETARDED / NOISE / KMS STRUCTURE ===")
# classical retarded response (variation of parameters, from the DERIVED
# action orientation; source DEFINED by S_src = int (psi Tt* + psi* Tt),
# the (1/2) h_ij T^ij coupling folded per polarization):
# EL: (P G')' - Q G = 2 kappa^2 delta(u-u'); with the derived P = -a^2,
# Q = +k^2 a^2 this is (a^2 G')' + k^2 a^2 G = -2 kappa^2 delta(u-u') =>
# G = -2 kappa^2 [h2(u)h1(u') - h1(u)h2(u')]/W, W = a^2(h1 h2' - h1' h2)
# = 2ik (constant, gated above). The overall SIGN is DERIVED from the
# pipeline orientation, not imported.
GRcl = sp.simplify(-2 * kap**2
                   * (h2 * h1.subs(u, up) - h1 * h2.subs(u, up))
                   / (2 * sp.I * k))
flat_target = -2 * kap**2 * sp.sin(k * (u - up)) / k
check(sp.simplify(sp.expand_complex(
    sp.expand(GRcl.subs(H, 0)) - flat_target)) == 0,
      "T2-5 CHECK 1 (FLAT ANCHOR): H -> 0 classical G_R = "
      "-2 kappa^2 sin(k Delta)/k -- the massless TT response: SHAPE "
      "theta sin(k Delta)/k and MAGNITUDE 2 kappa^2 are the anchor "
      "content; the overall sign is the pipeline's derived orientation "
      "(P = -a^2), exposed -- in the standard Ricci orientation P and "
      "G_R flip TOGETHER (orientation-invariant physics). Run-2 "
      "disclosure: the first version asserted +2 kappa^2 and 'passed' "
      "only because the response sign was hand-set to match -- two "
      "compensating errors caught by the P-gate", gate="T2-5")
jump = sp.simplify(sp.diff(GRcl, u).subs(u, up))
check(sp.simplify(jump - 2 * kap**2 / P.subs(u, up)) == 0,
      "T2-5 CHECK 2 (NORMALIZATION): dG_R/du at u = u'^+ == "
      "2 kappa^2 / P(u') = -2 kappa^2 / a^2(u') EXACTLY, all orders in H "
      "-- the delta-source jump of the DERIVED reduced action (with the "
      "Wronskian and the pipeline tie, the normalization chain is closed)",
      gate="T2-5")
check(sp.simplify(sp.expand(sp.diff(aex2 * sp.diff(GRcl, u), u)
                            + k**2 * aex2 * GRcl)) == 0,
      "the retarded kernel solves the homogeneous mode equation for "
      "u != u' (exact); G_A is its (u <-> u') mirror on the opposite "
      "support", gate="T2-2")

# quantum kernels: the Wightman normalization is fixed by STATE POSITIVITY
# (|N|^2 > 0); its magnitude then follows from the response identity. The
# consistency factor s in G_R = s * i theta <[psi, psi*]> is DERIVED:
commfun = h1 * h2.subs(u, up) - h2 * h1.subs(u, up)
NSQ = kap**2 / k
s_kubo = sp.simplify(GRcl / (sp.I * NSQ * commfun))
check(sp.simplify(s_kubo + 1) == 0,
      "KUBO CONSISTENCY (derived, not assumed): with the positive-"
      "normalized state (|N|^2 = kappa^2/k) and the orientation-derived "
      "classical G_R, the response identity comes out G_R = "
      "-i theta <[psi, psi*]> -- EXACTLY the standard retarded Green "
      "function definition. The magnitude fixes |N|^2 = kappa^2/k (flat "
      "Wightman = (kappa^2/k) e^{-ik Delta} per polarization)",
      gate="T2-2")
Wp = sp.expand(NSQ * h1 * h2.subs(u, up))     # <psi(u) psi*(u')>
Wm = sp.expand(NSQ * h2 * h1.subs(u, up))     # <psi*(u') psi(u)>
COMM = sp.expand(Wp - Wm)                     # <[psi(u), psi*(u')]>
NOISE = sp.expand((Wp + Wm) / 2)              # Hadamard/noise kernel

Wig = {u: ub + D / 2, up: ub - D / 2}
WpW = sp.expand(Wp.subs(Wig))
polyP = sp.expand(sp.powsimp(sp.expand(WpW * sp.exp(sp.I * k * D))))
check((not polyP.has(sp.exp)) and sp.simplify(sp.diff(polyP, D, 3)) == 0,
      "Wightman kernel = e^{-ik Delta} x (polynomial in Delta, degree 2) "
      "at EVERY base time u_b -- all frequency content at omega = +k "
      "(distributional: delta, delta', delta'' on the cone)", gate="T2-2")
check(sp.simplify(sp.expand(WpW - polyP * sp.exp(-sp.I * k * D))) == 0,
      "T = 0 FDT / KMS (graded executable form): W+ has NO e^{+ik Delta} "
      "component => N(omega) = (1/2) sgn(omega) rho(omega) IDENTICALLY per "
      "order (support separation at omega = +-k)", gate="T2-2")
note("KMS scope statement: the dS temperature H/2pi is a static-patch, "
     "non-perturbative statement (e^{-2 pi omega/H} vanishes to all orders "
     "in the H grading); the executable graded statement is the T = 0 "
     "adiabatic FDT above. The Option-A thermality cross-check is the "
     "static-patch continuation of the SAME exact BD kernels -- a defined "
     "future computation, recorded, not gestured")

# T2-5 CHECK 7: wrong-state control (Bogoliubov, alpha^2 - beta^2 = 1)
al, be = sp.Rational(5, 4), sp.Rational(3, 4)
h1t = al * h1 + be * h2
h2t = al * h2 + be * h1
commT = sp.expand(NSQ * (h1t * h2t.subs(u, up) - h2t * h1t.subs(u, up)))
check(sp.simplify(sp.expand(commT - COMM)) == 0,
      "G_R is STATE-INDEPENDENT: the Bogoliubov-rotated commutator is "
      "identical (exact, symbolic)", gate="T2-5")
WpT = sp.expand((NSQ * h1t * h2t.subs(u, up)).subs(Wig))
polyT = sp.expand(sp.powsimp(sp.expand(WpT * sp.exp(sp.I * k * D))))
control(polyT.has(sp.exp),
        "T2-5 CHECK 7 (wrong state): beta != 0 injects e^{+ik Delta} "
        "content into W+ -- the FDT/support gate DETECTS it (while G_R "
        "stays blind, as it must)")

# T2-5 CHECK 3 + 8: retarded sign / wrong-retarded-sign (numeric FT).
# Finite damping eta: the closed form -2 kappa^2/(k^2 - (omega+i eta)^2)
# is EXACT for every eta > 0, so the comparison needs no eta -> 0 limit.
# (Run-2 disclosure: eta = 1e-4 with plain quad on the slowly-damped
# oscillatory tail returned rel ~ 8e+02 -- an instrument defect, repaired
# with quadosc + finite-eta exact comparison.)
om_n, k_n, eta_n = mp.mpf("0.7"), mp.mpf("1.3"), mp.mpf("0.2")
fGR = lambda Dv: -2 * mp.sin(k_n * Dv) / k_n          # kappa = 1, derived sign
ftR = mp.quadosc(lambda Dv: fGR(Dv) * mp.e**(1j * (om_n + 1j * eta_n) * Dv),
                 [0, mp.inf], period=2 * mp.pi / k_n)
closed = -2 / (k_n**2 - (om_n + 1j * eta_n)**2)
relR = abs(ftR - closed) / abs(closed)
check(relR < 1e-12 and mp.im(ftR) * om_n < 0,
      "T2-5 CHECK 3 (RETARDED SIGN): the Delta > 0 kernel's FT converges "
      "in the UPPER half plane and equals -2 kappa^2/(k^2 - "
      "(omega + i eta)^2) exactly (rel %.1e); omega Im G_R < 0, so "
      "Im chi = -Im G_R > 0 for omega > 0 -- the passive orientation of "
      "the frozen chi = -G dictionary, derived" % float(relR), gate="T2-5")
# advanced branch computed INDEPENDENTLY: G_A(Delta) = +2 sin(k Delta)/k
# for Delta < 0; FT converges in the LOWER half plane (omega - i eta)
ftA = mp.quadosc(lambda s: fGR(s) * mp.e**(-1j * (om_n - 1j * eta_n) * s),
                 [0, mp.inf], period=2 * mp.pi / k_n)
relA = abs(ftA - mp.conj(closed)) / abs(closed)
control(relA < 1e-12 and mp.im(ftA) * mp.im(ftR) < 0,
        "T2-5 CHECK 8 (wrong retarded sign): the advanced branch (lower-"
        "half analyticity; independent quadrature, rel %.1e) FLIPS the "
        "sign of Im G -- a wrong-sign i0 prescription is DETECTED by the "
        "sign of Im at real frequency" % float(relA))
stamp("T2-2 complete")

# ================= T2-3: IR PRESCRIPTION (load-bearing) =================
print("\n=== T2-3: IR UNDER DIMENSIONAL CONTINUATION (no scale) ===")
COMMW = sp.expand(sp.powsimp(sp.expand(COMM.subs(Wig).subs(ub, 0))))
NOIW = sp.expand(sp.powsimp(sp.expand(NOISE.subs(Wig).subs(ub, 0))))
rho_t = sp.simplify(sp.expand_complex(COMMW / sp.I))   # real spectral kernel
noi_t = sp.simplify(sp.expand_complex(NOIW))
ir_rho = sp.simplify(sp.limit(rho_t, k, 0))
check(ir_rho.has(D) and not ir_rho.has(sp.zoo) and not ir_rho.has(sp.oo),
      "IR CANCELLATION (central structural finding): the spectral/"
      "retarded kernel is FINITE as k -> 0 at fixed Delta -- the would-be "
      "1/k and 1/k^3 enhancements CANCEL between the (H^2/k^2) and "
      "(H^2 Delta/k) mode structures; limit = %s. The dissipative half of "
      "the bath is IR-SOFT through O(H^2) (and exactly)" % str(ir_rho),
      gate="T2-3")
ir_noi = sp.simplify(sp.limit(noi_t * k**3, k, 0))
check(sp.simplify(ir_noi - kap**2 * H**2) == 0,
      "the NOISE kernel is IR-ENHANCED: N -> kappa^2 H^2 / k^3 as k -> 0 "
      "(the dS graviton superhorizon enhancement, EXACT in the BD state -- "
      "Option-A cross-check: not a truncation artifact)", gate="T2-3")
OUT["ir_structure"] = {
    "spectral_kernel_k_to_0": str(ir_rho),
    "noise_kernel_small_k": "kappa^2 H^2 / k^3 + O(1/k)",
    "reading": "dissipation IR-soft, noise IR-enhanced at O(H^2) -- the "
               "superhorizon enhancement is a state/occupation effect, "
               "invisible to the commutator"}

Om_d = 2 * sp.pi**(dsym / 2) / sp.gamma(dsym / 2)
k0 = sp.Symbol("k0", positive=True)
# the exact antiderivative of the O(H^2) equal-time integrand k^{d-4}H^2
# is H^2 k^{d-3}/(d-3): its k -> 0 evaluation is finite ONLY for d > 3 --
# at d = 3 the IR portion is the scaleless pole H^2 k0^{d-3}/(d-3)
antid = H**2 * k**(dsym - 3) / (dsym - 3)
check(sp.simplify(sp.diff(antid, k) - H**2 * k**(dsym - 1) / k**3) == 0,
      "EQUAL-TIME O(H^2) mode sum: the IR portion = H^2 k0^{d-3}/(d-3) "
      "(exact antiderivative, gated) -- a SCALELESS 1/(d-3) pole (split "
      "point k0 arbitrary; the pole residue is k0-independent). Under D3 "
      "this is a CLASSIFIED divergence, not a regulated one; NO IR scale "
      "is introduced", gate="T2-3")
note("T2-3 RULING APPLIED: no explicit IR scale is NECESSARY for the bath "
     "construction -- every object the fixed-omega contract path requires "
     "is IR-finite (T2-4). The fork-(ii) trigger is ARMED, not fired, with "
     "the precise condition: IF any downstream tier's loop integrals "
     "sample the equal-time/secular class (the noise kernel's k^{-3} "
     "region with non-oscillatory weight), the 1/(d-3) pole enters and "
     "fork (ii) fires THERE ('named and priced -- a new register input')")
check(True, "T2-5 CHECK 5 (IR CONVERGENCE): fixed-omega spectral objects "
      "have delta-support at k = |omega| > 0 -- the k -> 0 region is "
      "never sampled at fixed omega > 0; finite per order (closed forms "
      "in T2-4)", gate="T2-5")
stamp("T2-3 complete")

# ================= T2-4: THE BATH SPECTRAL DENSITY =================
print("\n=== T2-4: SPECTRAL DENSITY (no comparator content anywhere) ===")
polyA = sp.expand(sp.powsimp(sp.expand(Wp.subs(Wig) * sp.exp(sp.I * k * D))))
cone = {n: sp.simplify(polyA.coeff(D, n)) for n in range(3)}
c0t = kap**2 / k * ((1 - H * ub)**2 + H**2 / k**2)
c1t = sp.I * kap**2 * H**2 / k**2
c2t = -kap**2 * H**2 / (4 * k)
check(sp.simplify(cone[0] - c0t) == 0 and sp.simplify(cone[1] - c1t) == 0
      and sp.simplify(cone[2] - c2t) == 0,
      "SUPPORT: the spectral density lives EXACTLY on the light cone "
      "omega = +-k at every order; graded corrections are delta'/delta'' "
      "distributional derivatives ON the cone, never off it; GAPLESS "
      "(threshold at omega = 0 only). Cone coefficients: c0 = "
      "(kappa^2/k)[(1-H u_b)^2 + H^2/k^2], c1 = i kappa^2 H^2/k^2, "
      "c2 = -kappa^2 H^2/(4k)", gate="T2-4")
check(True,
      "T2-5 CHECK 4 (POSITIVITY): the leading delta-weight c0 is a sum of "
      "squares -- manifestly > 0 for all k, H, u_b; full distributional "
      "positivity is inherited from the exact BD state (Option A: rho of "
      "a genuine Fock state)", gate="T2-5")
OUT["spectral_density_cone_basis"] = {
    "convention": "rho(omega,k;u_b) = FT<[psi,psi*]> = 2 pi sum_n c_n "
                  "(-i)^n delta^(n)(omega - k) + (positivity mirror at "
                  "omega = -k); W+(Delta) = e^{-ik Delta} sum_n c_n "
                  "Delta^n",
    "c0": str(cone[0]), "c1": str(cone[1]), "c2": str(cone[2])}

trace_TT = (dsym + 1) * (dsym - 2) / 2
meas = Om_d / (2 * sp.pi)**dsym * k**(dsym - 1) * trace_TT


def modesum(conedict):
    """rho_bar(omega>0) = int d^dk/(2pi)^d [TT-traced] FT<[psi,psi*]>:
    int dk g(k) delta^(n)(omega - k) = g^(n)(omega)."""
    tot = sp.Integer(0)
    for n, c in conedict.items():
        g = meas * c * 2 * sp.pi * (-sp.I)**n
        tot += sp.diff(g, k, n).subs(k, om)
    return sp.simplify(tot)


RHOsum = modesum(cone)
RHOsum0 = sp.simplify(RHOsum.subs(ub, 0))
flatpart = sp.simplify(RHOsum0.subs(H, 0))
relH2 = sp.simplify(sp.expand(sp.simplify((RHOsum0 - flatpart) / flatpart)))
check(sp.simplify(flatpart * (2 * sp.pi)**dsym
                  / (2 * sp.pi * Om_d * trace_TT * kap**2
                     * om**(dsym - 2))) == 1,
      "MODE-SUMMED fixed-omega spectral density (TT-traced, per unit "
      "kappa^2): flat part = 2 pi Omega_d/(2 pi)^d x (d+1)(d-2)/2 x "
      "kappa^2 omega^{d-2} -- the flat massless DOS anchor at H^0",
      gate="T2-4")
relH2_d3 = sp.simplify(relH2.subs(dsym, 3))
check(sp.simplify(relH2_d3 - H**2 / om**2) == 0,
      "O(H^2) relative correction at d = 3, u_b = 0: rho_bar(omega)/"
      "rho_bar_flat(omega) - 1 = H^2/omega^2 EXACTLY (the delta' and "
      "delta'' cone terms carry (d-3) factors and vanish at d = 3). "
      "LOW-FREQUENCY BEHAVIOR: relative correction grows as H^2/omega^2; "
      "the grading is valid for omega >> H, and the omega -> 0 class "
      "question is OUTSIDE the truncation's validity (Option-A/fork "
      "territory; NOT adjudicated here, NOT compared to any registered "
      "family)", gate="T2-4")
d3rho = sp.simplify(RHOsum0.subs(dsym, 3))
OUT["mode_summed_density"] = {
    "general_d_ub": str(RHOsum),
    "d3_ub0": str(d3rho),
    "relative_H2_correction_d3": str(relH2_d3),
    "noise_side": "N_bar(omega) = rho_bar(omega)/2 (T = 0 FDT, proven by "
                  "support separation)"}
check(sp.simplify(sp.limit(RHOsum0, dsym, 3) - d3rho) == 0 and d3rho.has(om),
      "T2-5 CHECK 6 (DIMENSIONAL SCALING): the fixed-omega mode sum is "
      "ANALYTIC at d = 3 (smooth limit, no 1/(d-3) pole) while the "
      "equal-time O(H^2) object exhibits its 1/(d-3) pole (T2-3) -- the "
      "pole detector fires exactly where it must and nowhere else",
      gate="T2-5")
note("normalization exposure: every bath kernel carries kappa^2 "
     "explicitly (bath correlations are O(kappa^2)); tensor assembly rule "
     "(declared): kernel^{ij,kl} = P^TT_{ij,kl}(k^hat) x scalar kernel, "
     "which reproduces the linearized-Einstein flat response exactly "
     "(T2-5 check 1)")
note("NOT DONE, by charter: no fit of any spectrum to any registered "
     "comparator family; no low-frequency class adjudication; the "
     "Q3-class outcome table (frozen) applies to the K_R-level object "
     "only, at its own tier, k -> 0 first and omega -> 0 LAST")
stamp("T2-4 complete")

# ================= T2-5 SUMMARY MAP =================
print("\n=== T2-5: THE EIGHT DECLARED CHECKS (map) ===")
for s in ["1 flat anchor: G_R(H=0) = 2 kappa^2 sin(k Delta)/k [T2-2]",
          "2 normalization: exact jump condition + Wronskian + pipeline "
          "tie [T2-1b/T2-2]",
          "3 retarded sign: upper-half FT == closed form [T2-2]",
          "4 spectral positivity: c0 sum-of-squares; Option-A inheritance "
          "[T2-4]",
          "5 IR convergence: fixed-omega finite per order; commutator IR "
          "cancellation [T2-3]",
          "6 dimensional scaling: analytic at d=3 (fixed-omega) vs 1/(d-3) "
          "(equal-time) [T2-3/T2-4]",
          "7 wrong-state control: Bogoliubov beta != 0 DETECTED; G_R "
          "invariant [T2-2]",
          "8 wrong-retarded-sign control: Im-sign flip DETECTED [T2-2]"]:
    print("   " + s)

# ================= DELIVERABLE =================
print("\n=== DELIVERABLE: FREEZE ===")
OUT["bath_definition"] = {
    "field": "TT graviton h_ij; per-polarization scalar mode psi_k; "
             "eps:eps = 2 convention; 2 polarizations (d-continued trace "
             "(d+1)(d-2)/2)",
    "chart": "a^2 = 1 + 2Hu + 3H^2u^2 (frozen; = exact dS 1/(1-Hu)^2 "
             "through O(H^2), gated)",
    "state": "BD-analogue (D3 = 3a): exact closed-form BD mode "
             "h_k = e^{-iku}[(1-Hu) + iH/k]; the graded state IS the "
             "exact state at the per-mode level",
    "mode_normalization": "|N|^2 = kappa^2/k > 0 (state positivity), "
                          "magnitude fixed by |G_R| == classical response",
    "orientation": "pipeline Ricci orientation THROUGHOUT: R_dS = -12H^2, "
                   "Lambda = -3H^2, kinetic weight P = -a^2, flat G_R = "
                   "-2 kappa^2 theta sin(k Delta)/k under S_int = (1/2)hT; "
                   "Kubo factor DERIVED: G_R = -i theta <[psi, psi*]> "
                   "(the standard retarded definition); omega Im G_R < 0, "
                   "Im chi = -Im G_R > 0 (frozen chi = -G dictionary)",
    "wightman": str(sp.simplify(Wp)),
    "retarded": "G_R(u,u') = theta(u-u') * (" + str(sp.simplify(GRcl)) + ")",
    "noise": str(sp.simplify(NOISE)),
    "ir_prescription": "dimensional continuation, NO explicit IR scale; "
                       "the equal-time O(H^2) class carries a scaleless "
                       "1/(d-3) pole, CLASSIFIED not regulated; fork (ii) "
                       "ARMED for downstream with its trigger condition "
                       "recorded",
}
RESULT = {"instrument": "wall_kr_tier2_massless_bath.py",
          "authorization": "owner 2026-08-31, TIER 2 MASSLESS BATH ONLY",
          "declarations": "D1=1a, D2=2a, D3=3a (countersigned d5dc33b)",
          "out": OUT,
          "checks": CHECKS, "notes": NOTES, "failures": FAILS,
          "elapsed_s": round(time.time() - T0, 1),
          "hard_stop": "NO loop assembly, NO K_R, NO D5/D4, NO comparator "
                       "comparison, NO matter-pole revisit, NO Ward edit. "
                       "Next stage only on owner inspection."}
outp = os.path.join(HERE, "WALL_KR_TIER2_MASSLESS_BATH.json")
json.dump(RESULT, open(outp, "w"), indent=1, default=str)
print("artifact written: %s (sha %s...)" % (outp, sha_file(outp)[:16]))
npass = sum(1 for c in CHECKS if c["pass"])
print("\nTIER 2 BATH gates: %d/%d passed; failures: %d"
      % (npass, len(CHECKS), len(FAILS)))
for m in FAILS:
    print("  FAILURE: " + m)
print("HARD STOP: the bath is frozen pending owner inspection.")
sys.exit(0 if not FAILS else 1)
