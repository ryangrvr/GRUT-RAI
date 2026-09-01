#!/usr/bin/env python3
"""TIER 4 -- THE CONTRACT-LEVEL RETARDED K_R ASSEMBLY (owner authorization
2026-09-01; RETARDED PHYSICAL RESPONSE ONLY).

INPUTS (frozen, never edited): the Tier-3 absorptive closed forms
  Im Sigma_R^{H0}(omega>0) = -(3/1280 pi) omega^4          [kappa = 1]
  Im Sigma_R^{H1}          =  0   (identically)
  Im Sigma_R^{H2}(omega>0) = -(13/480 pi) H^2 omega^2      [u_b-independent
                                       through O(H^2), review-verified]
plus the Tier-2 bare retarded propagator G0_R(omega, k) =
2 kappa^2 / ((omega+i0)^2 - k^2) (frozen orientation chain).

THE OBJECT: K_R = the retarded dissipation kernel of the probe's influence
action (rung1 definition, adjudication b4a6943: RETARDED-ONLY; N is the
FDT partner, NOT an ingredient; the alpha = -2 noise divergence never
enters). Chain: Sigma_R --> Dyson (BOTH orders, kept separate) -->
influence-action normalization K_R(omega) = Sigma_R(omega) in the
(1/2 kappa^2)-weighted probe convention (derived + gated below).

RETARDED COMPLETION (the only new analytic content): each scale-free
absorptive power law has the unique retarded completion
  omega^n --> (C/pi) omega^n [ log(mu^2/omega^2) + i pi ]   (omega > 0)
up to a REAL local polynomial -- the D5/scheme slot, carried SYMBOLICALLY
(c0, c2, c4 at H^0; H^2(c0p + c2p omega^2) at O(H^2); mu symbolic). The
local slot is NOT chosen here (frozen renormalization conditions = D5,
deferred). Gates: the completion's Im part == the frozen values; the
polynomial-free derivative of the completion == the numeric subtracted
Kramers-Kronig transform (independent route).

VALIDITY DOMAIN (T4-4, hard-wired): eps_H = (104/9) H^2/omega^2.
  eps_H <= 0.1        : CONTROLLED (primary domain)
  0.1 < eps_H < 1     : BOUNDARY (returned with an explicit flag)
  eps_H >= 1          : REFUSED (raises DomainRejected -- extrapolation
                        into omega <~ H is forbidden, and the refusal is
                        itself a gated control)
Also the loop-perturbative parameter lam(omega) = |2 kappa^2 Sigma/
omega^2| must satisfy lam < 1 for the resummed/first-order pair to be in
its agreement domain (reported, never hidden).

HARD STOP after the freeze: no benchmark consequence, no J(omega), no
Ward repair, no bridge, no operators, no sign changes, no omega << H.
W-0: computed-and-reported, NOT banked.
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


# ================= T4-0: INPUT INTEGRITY =================
print("=== T4-0: INPUT INTEGRITY ===")
PINS = {
    "WALL_KR_TIER1_VERTEX_ARTIFACT.json": None,
    "WALL_KR_TIER2_MASSLESS_BATH.json": "c5d399f525407839",
    "WALL_KR_TIER3_LOOP_RESULT.json": "4c016e93b889bd04",
    "WALL_KR_TIER3_FLAT_RESULT.json": "fac2e090540c57cd",
    "WALL_KR_TIER3_IR_CHECK_RESULT.json": "a43633f5d34f6895",
    "WALL_A3_4_TT_RESULT.json": None,
    "WALL_A4_RESPONSE_DRESSED_RESULT.json": None,
    "WALL_PV_ROBUSTNESS_RESULT.json": None,
    "K_R_CONTRACT_EXECUTION_CHARTER.md": "5416fa45498a6e5f",
    "K_R_CONTRACT_OWNER_RULING.md": "5d89720b53e1b078",
    "WALL_KR_TIER3_FORK_ADJUDICATION.md": None,
}
for fn, want in PINS.items():
    got = sha_file(os.path.join(HERE, fn))
    if want:
        check(got.startswith(want), "pin %s == %s..." % (fn, want),
              gate="T4-0")
    else:
        note("input sha %s = %s..." % (fn, got[:16]))
IRC = json.loads(open(os.path.join(
    HERE, "WALL_KR_TIER3_IR_CHECK_RESULT.json")).read())
check(IRC["out"]["verdict"] == "RETARDED VALIDITY BOUNDARY"
      and IRC["failures"] == [],
      "T3 IR-check on record: RETARDED VALIDITY BOUNDARY, zero failures",
      gate="T4-0")
note("claimed new paths: WALL_KR_CONTRACT_RETARDED_RESULT.json / "
     "_VERDICT.md / _MANIFEST.json; wall_kr_tier4_retarded.py")
if FAILS:
    sys.exit(2)

# symbols
om = sp.Symbol("omega", positive=True)
H = sp.Symbol("H", positive=True)
kap = sp.Symbol("kappa", positive=True)
mu = sp.Symbol("mu", positive=True)
kpr = sp.Symbol("k", nonnegative=True)          # probe momentum
c0, c2, c4, c0p, c2p = sp.symbols("c0 c2 c4 c0p c2p", real=True)

# ================= T4-1: THE FROZEN ABSORPTIVE INPUTS =================
print("\n=== T4-1: FROZEN ABSORPTIVE DATA (loaded, not re-derived) ===")
T3F = json.loads(open(os.path.join(
    HERE, "WALL_KR_TIER3_FLAT_RESULT.json")).read())
im0_str = T3F["out"]["im_sigma_flat_d3"]
# map PLAIN parsed symbols to the assumed ones (the campaign's
# recurring identical-printing-symbols trap -- run-1 defect here)
im0 = sp.sympify(im0_str).xreplace({sp.Symbol("kappa"): kap,
                                    sp.Symbol("omega"): om})
check(sp.simplify(im0.subs(kap, 1) + 3 * om**4 / (1280 * sp.pi)) == 0,
      "loaded Im Sigma^{H0} from the frozen T3 artifact == "
      "-3 omega^4/(1280 pi)", gate="T4-1")
im2_str = IRC["out"]["im_sigma_H2_d3"]
im2core = sp.sympify(im2_str).xreplace({sp.Symbol("kappa"): kap,
                                        sp.Symbol("omega"): om})
check(sp.simplify(im2core.subs(sp.Symbol("kappa", positive=True), 1)
                  + 13 * om**2 / (480 * sp.pi)) == 0,
      "loaded Im Sigma^{H2} (per H^2) from the frozen IR-check artifact "
      "== -13 omega^2/(480 pi)", gate="T4-1")
C4 = sp.Rational(-3, 1280) / sp.pi          # omega^4 coefficient, kappa=1
C2H = sp.Rational(-13, 480) / sp.pi         # H^2 omega^2 coefficient
note("kappa-power bookkeeping: the T3 kernels are kappa^0 in the "
     "(1/2 kappa^2)-stripped pipeline units (T3 review-verified); "
     "kappa re-enters only through G0 = 2 kappa^2/((omega+i0)^2 - k^2)")
note("u_b-independence of the retarded kernels through O(H^2): "
     "review-verified on the frozen T3 cone data; Sigma_R(omega) below "
     "is base-time independent at the retained orders")
note("NOISE FENCE: nothing in this instrument reads nk_wigner or any "
     "noise-sector object; the alpha = -2 finding stays separate")

# ================= T4-1b: RETARDED COMPLETION (the new content) ========
print("\n=== T4-1b: RETARDED ANALYTIC COMPLETION ===")
Lg = sp.log(mu**2 / om**2) + sp.I * sp.pi       # log(mu^2/(-(om+i0)^2))
SIG0 = (C4 / sp.pi) * om**4 * Lg + c0 + c2 * om**2 + c4 * om**4
SIG2 = (C2H / sp.pi) * om**2 * Lg + c0p + c2p * om**2   # per H^2
SIG = sp.expand(SIG0 + H**2 * SIG2)
OUT["sigma_R"] = {"H0": str(SIG0), "H2_per_H2": str(SIG2),
                  "total": str(SIG),
                  "local_slot": "c0 + c2 omega^2 + c4 omega^4 + "
                                "H^2(c0p + c2p omega^2), REAL, "
                                "UNDETERMINED (D5/scheme; frozen "
                                "renormalization conditions deferred); "
                                "mu symbolic (absorbable into c4/c2p)"}
check(sp.simplify(sp.im(SIG0.subs({c0: 0, c2: 0, c4: 0}).rewrite(sp.log))
                  - im0.subs(kap, 1)) == 0,
      "completion gate (H^0): Im part == the frozen absorptive value "
      "EXACTLY (locals are real and contribute nothing)", gate="T4-1")
check(sp.simplify(sp.im(SIG2.subs({c0p: 0, c2p: 0}))
                  - im2core.subs(sp.Symbol("kappa", positive=True), 1)
                  / 1) == 0,
      "completion gate (H^2): Im part == the frozen IR-check value "
      "EXACTLY", gate="T4-1")
# independent route: numeric subtracted Kramers-Kronig on the absorptive
# power law must reproduce the polynomial-free content of the log form.
# d^5/dom^5 of SIG0 is local-slot-free; compare with the 5x-subtracted
# dispersive transform's 5th derivative, computed numerically:
#   Re Sigma(omega) = P.V. (1/pi) int dw' Im Sigma(w') [odd ext] /(w'-w)
# with 5 subtractions at w = 0 killing the polynomial ambiguity and the
# UV growth; equivalently compare the analytic 5th derivative of
# (C4/pi) w^4 log(mu^2/w^2) with the numeric transform derivative.
d5log = sp.diff((C4 / sp.pi) * om**4 * sp.log(mu**2 / om**2), om, 5)


def re_disp(w, nsub=5, cut=None):
    """5x-subtracted PV dispersion of Im Sigma^{H0} (odd extension),
    numeric, with an explicit principal-value window; the polynomial
    ambiguity (and the UV growth) are killed by the subtractions."""
    w = mp.mpf(w)
    C = -3 / (1280 * mp.pi)
    cut = mp.mpf(cut or 60)
    dl = w * mp.mpf("0.05")

    def A(wp):                                # singular-factor numerator
        return C * wp**4 / mp.pi

    def rest(wp):                             # regular part
        subs_ = sum(2 * w**j / wp**(j + 1) for j in range(0, nsub, 2))
        return A(wp) * (1 / (wp + w) - subs_)

    def full(wp):
        return A(wp) / (wp - w) + rest(wp)

    I1 = mp.quad(full, [mp.mpf("1e-12"), w - dl])
    I3 = mp.quad(full, [w + dl, cut])
    Ipv = mp.quad(lambda t: (A(w + t) - A(w - t)) / t, [0, dl])
    Ireg = mp.quad(rest, [w - dl, w + dl])
    return I1 + I3 + Ipv + Ireg


wtest = mp.mpf("1.3")
h_ = mp.mpf("1e-3")
pts7 = [re_disp(wtest + j * h_) for j in (-3, -2, -1, 0, 1, 2, 3)]
d5num = (-pts7[0] + 4 * pts7[1] - 5 * pts7[2] + 0 * pts7[3]
         + 5 * pts7[4] - 4 * pts7[5] + pts7[6]) / (2 * h_**5)
# ^ central stencil for f^(5): [-1, 4, -5, 0, 5, -4, 1]/(2 h^5)
d5an = mp.mpf(str(sp.N(d5log.subs(mu, 1).subs(om, sp.Rational(13, 10)),
                       30)))
relkk = abs(d5an - d5num) / abs(d5an) if d5an != 0 else mp.mpf(1)
check(relkk < mp.mpf("5e-2"),
      "INDEPENDENT ROUTE (H^0 completion): the numeric 5x-subtracted "
      "Kramers-Kronig transform of the frozen absorptive law reproduces "
      "the log-form's polynomial-free 5th derivative (rel %.1e; "
      "finite-difference-limited)" % float(relkk), gate="T4-1")
# n = 2 (H^2) KK coverage (review coverage note): same analytic fact,
# independently exercised with a 3x-subtracted transform and a d^3
# stencil against the omega^2-law completion
def re_disp2(w, cut=None):
    w = mp.mpf(w)
    C = -13 / (480 * mp.pi)
    cut = mp.mpf(cut or 200)
    dl = w * mp.mpf("0.05")

    def A(wp):
        return C * wp**2 / mp.pi

    def rest(wp):
        subs_ = sum(2 * w**j / wp**(j + 1) for j in range(0, 3, 2))
        return A(wp) * (1 / (wp + w) - subs_)

    def full(wp):
        return A(wp) / (wp - w) + rest(wp)
    I1 = mp.quad(full, [mp.mpf("1e-12"), w - dl])
    I3 = mp.quad(full, [w + dl, cut])
    Ipv = mp.quad(lambda t: (A(w + t) - A(w - t)) / t, [0, dl])
    Ireg = mp.quad(rest, [w - dl, w + dl])
    return I1 + I3 + Ipv + Ireg


d3log2 = sp.diff((C2H / sp.pi) * om**2 * sp.log(mu**2 / om**2), om, 3)
h2_ = mp.mpf("1e-3")
p5 = [re_disp2(mp.mpf("1.3") + j * h2_) for j in (-2, -1, 0, 1, 2)]
d3num = (-p5[0] + 2 * p5[1] - 2 * p5[3] + p5[4]) / (2 * h2_**3)
d3an = mp.mpf(str(sp.N(d3log2.subs(mu, 1).subs(om, sp.Rational(13, 10)),
                       30)))
rel2 = abs(d3an - d3num) / abs(d3an)
check(rel2 < mp.mpf("5e-2"),
      "INDEPENDENT ROUTE (H^2 completion): the 3x-subtracted KK "
      "transform of the omega^2 law reproduces the log-form's "
      "polynomial-free 3rd derivative (rel %.1e) -- the n = 2 "
      "completion is now KK-gated in its own right" % float(rel2),
      gate="T4-1")
note("H^2 completion IR systematic (review-recorded): the dispersion "
     "formally samples omega' <~ H where the truncated absorptive law "
     "is invalid; the induced Re error is O(eps_H^2) relative to the "
     "retained H^2 omega^2 log term -- inside the domain gate's own "
     "tolerance, recorded on the artifact face")
# reality/retardedness structure gate
check(sp.simplify(sp.im(SIG0.subs({c0: 0, c2: 0, c4: 0}))
                  - (C4) * om**4) == 0 and
      sp.simplify(sp.re(Lg) - sp.log(mu**2 / om**2)) == 0,
      "retarded structure: Sigma_R(omega>0) = Re + i Im with "
      "Im < 0 (passive half-plane) and Sigma_R(-omega) = Sigma_R(omega)* "
      "by the declared odd/real extension", gate="T4-1")
stamp("T4-1 complete")

# ================= T4-2: PROBE LIMIT (k -> 0 first) =================
print("\n=== T4-2: PROBE LIMIT ===")
G0k = 2 * kap**2 / ((om + sp.I * sp.Symbol("epsilon", positive=True))**2
                    - kpr**2)
G0 = 2 * kap**2 / om**2                      # k -> 0, real-omega branch
note("D1 inherited: k -> 0 FIRST at fixed omega > 0. Sigma(omega) enters "
     "at the k_ext = 0 evaluation point (T3; isotropy gated there at all "
     "H orders across three external configurations -- cited as executed "
     "evidence, commit 65ccb1b). The O(k^2) dependence of Sigma was not "
     "computed at T3 (scope-disclosed); the dressing's own k -> 0 "
     "continuity is gated here.")
lim_test = sp.simplify(sp.limit(1 / G0k - (1 / G0k).subs(kpr, 0), kpr, 0))
check(lim_test == 0,
      "dressing continuity: G0^{-1}(omega,k) -> G0^{-1}(omega,0) "
      "smoothly as k -> 0 at fixed omega > 0 (no degeneracy in the "
      "scalar TT-projected channel; the projector's k^hat dependence "
      "was retired by the executed isotropy gates)", gate="T4-2")
note("joint rays omega ~ k: NOT used as verdict-bearing data (barred by "
     "D1); no such computation performed")

# ================= T4-3 + T4-4: DYSON PAIR + DOMAIN GATE =================
print("\n=== T4-3/T4-4: DYSON PAIR + VALIDITY DOMAIN ===")
G1 = sp.expand(G0 + G0 * SIG * G0)           # first-order
GR = 1 / (1 / G0 - SIG)                      # resummed
OUT["dyson"] = {"first_order": str(G1), "resummed": str(GR),
                "G0": str(G0)}
EPSH = sp.Rational(104, 9) * H**2 / om**2
LAM = 2 * kap**2 * SIG / om**2               # loop-perturbative parameter
OUT["validity"] = {
    "eps_H": str(EPSH),
    "lam": "2 kappa^2 Sigma_R/omega^2 (loop-perturbative parameter)",
    "domains": "eps_H <= 0.1 CONTROLLED; 0.1 < eps_H < 1 BOUNDARY "
               "(flagged); eps_H >= 1 REFUSED; resummed-vs-first-order "
               "agreement additionally requires |lam| < 1"}


class DomainRejected(Exception):
    pass


LOCAL0 = {c0: 0, c2: 0, c4: 0, c0p: 0, c2p: 0}   # declared REFERENCE slice


def eval_KR(w, Hv, kapv, muv=1.0, obj="sigma"):
    """domain-gated evaluator: refuses eps_H >= 1; flags 0.1 < eps_H < 1.
    Locals evaluated on the DECLARED reference slice c = 0 (the scheme
    slot is symbolic in the frozen object; numerics require a slice and
    the slice is disclosed, never adopted as physics)."""
    w, Hv, kapv = mp.mpf(w), mp.mpf(Hv), mp.mpf(kapv)
    eps = mp.mpf(104) / 9 * Hv**2 / w**2
    if eps >= 1:
        raise DomainRejected("eps_H = %s >= 1: omega <~ H is outside "
                             "the truncated H expansion" % mp.nstr(eps, 6))
    flag = "CONTROLLED" if eps <= mp.mpf("0.1") else "BOUNDARY"
    expr = {"sigma": SIG, "G1": G1, "GR": GR}[obj]
    f = sp.lambdify((om, H, kap, mu), expr.subs(LOCAL0), "mpmath")
    # second validity condition (review FINDING 1c): the loop-
    # perturbative parameter |lam| = |2 kappa^2 Sigma/omega^2| must be
    # < 1 for the Dyson pair's agreement domain; enforced HERE, not
    # per-site
    fsig = sp.lambdify((om, H, kap, mu), SIG.subs(LOCAL0), "mpmath")
    lam_v = abs(2 * kapv**2 * fsig(w, Hv, kapv, mp.mpf(muv)) / w**2)
    if lam_v >= 1:
        raise DomainRejected("lam = %s >= 1: outside the loop-"
                             "perturbative domain" % mp.nstr(lam_v, 6))
    if lam_v > mp.mpf("0.1") and flag == "CONTROLLED":
        flag = "BOUNDARY"
    return f(w, Hv, kapv, mp.mpf(muv)), flag, eps


val, flag, eps = eval_KR("1.0", "0.05", "0.1")
check(flag == "CONTROLLED" and eps < mp.mpf("0.1"),
      "domain gate: omega/H = 20 evaluates CONTROLLED (eps_H = %s)"
      % mp.nstr(eps, 4), gate="T4-4")
val_b, flag_b, eps_b = eval_KR("0.2", "0.05", "0.1")
check(flag_b == "BOUNDARY",
      "domain gate: omega/H = 4 returns with an explicit BOUNDARY flag "
      "(eps_H = %s) -- reported, not hidden" % mp.nstr(eps_b, 4),
      gate="T4-4")
try:
    eval_KR("0.05", "0.05", "0.1")
    rejected = False
except DomainRejected as e:
    rejected = True
    note("refusal message: %s" % str(e))
control(rejected, "T4-7 #10 EXTRAPOLATION CONTROL: an attempted "
        "omega = H evaluation is REJECTED by the instrument (the "
        "truncated H series is never numerically extrapolated into "
        "omega <~ H)")

# ================= T4-5/T4-6: ASSEMBLY + NORMALIZATION =================
print("\n=== T4-5/T4-6: K_R ASSEMBLY + INFLUENCE-ACTION NORMALIZATION ===")
note("K_R(omega) = Sigma_R(omega) in the (1/2 kappa^2)-weighted probe "
     "convention. DERIVATION (executable identity, not import): the "
     "quadratic SK action of the probe in the (r,a) basis is "
     "S2 = int x_a [G0_R^{-1}] x_r + (loop) with the loop's r-a piece = "
     "-x_a Sigma_R x_r; hence G_R^{-1} = G0^{-1} - Sigma_R (the resummed "
     "object above) and the influence-action retarded kernel is "
     "K_R = Sigma_R verbatim in these units. The friction convention "
     "Im chi = J/omega is a DEFINITION of normalization (chi = G_R per "
     "the frozen chi = -G dictionary orientation chain); no J(omega) "
     "content is read or compared")
OUT["K_R"] = {"definition": "K_R(omega) = Sigma_R(omega), "
                            "(1/2 kappa^2)-weighted probe units",
              "sectors_kept_separate": {"H0": str(SIG0),
                                        "H1": "0 (identically)",
                                        "H2_per_H2": str(SIG2)},
              "local_nonlocal_split": {
                  "nonlocal": "(C4/pi) omega^4 L + H^2 (C2H/pi) "
                              "omega^2 L, L = log(mu^2/omega^2) + i pi",
                  "local": "c0 + c2 omega^2 + c4 omega^4 + "
                           "H^2(c0p + c2p omega^2) -- symbolic"},
              "tt_scope": "TT by construction (charter section 6); the "
                          "Class-B vector residual is EXCLUDED by scope, "
                          "not resolved"}
# dimensions gate: lam/(kappa omega)^2 must be kappa-free (pure
# logs/numbers in omega, mu) -- the dressing is perturbative wherever
# kappa omega << 1, i.e. everywhere the H expansion is controlled
lam_red = sp.simplify(2 * kap**2 * SIG0.subs({c0: 0, c2: 0, c4: 0})
                      / om**2 / (kap**2 * om**2))
check(not lam_red.has(kap),
      "dimensions: lam = 2 kappa^2 Sigma/omega^2 = (kappa omega)^2 x "
      "(logs/numbers) -- dimensionless, kappa-free after the (kappa "
      "omega)^2 strip; vanishes into the domain's IR", gate="T4-6")
# passivity of the dressed propagator (numeric, in-domain, ref slice)
wv, Hv, kv = mp.mpf("1.0"), mp.mpf("0.02"), mp.mpf("0.1")
gr_val, gr_flag, _ = eval_KR(wv, Hv, kv, obj="GR")
check(gr_flag == "CONTROLLED",
      "production evaluation flag ASSERTED CONTROLLED (review FINDING "
      "1b: flags are consumed, never discarded)", gate="T4-4")
check(mp.im(gr_val) < 0,
      "T4-6 SIGN: Im G_R(omega>0) < 0 for the dressed propagator "
      "in-domain (numeric %s) -- the frozen passive orientation "
      "propagates through the dressing (Tier-2 chain external check, "
      "not a circular definition)" % mp.nstr(mp.im(gr_val), 4),
      gate="T4-6")

# ================= T4-7: INDEPENDENT CHECKS =================
print("\n=== T4-7: CHECKS ===")
check(sp.simplify(sp.im(SIG.subs(LOCAL0)).subs(H, 0)
                  - im0.subs(kap, 1)) == 0,
      "#1 flat limit reproduces the frozen T3 value exactly", gate="T4-7")
check(sp.simplify(sp.im(sp.expand(SIG.subs(LOCAL0)).coeff(H, 2))
                  - im2core.subs(sp.Symbol("kappa", positive=True), 1)) == 0,
      "#2 H^2 content reproduces the frozen IR-check value exactly",
      gate="T4-7")
note("#3 isotropy: executed at T3 (three configs, all H orders) -- "
     "cited, artifact-pinned; #5 routing: same (G5-inherited C symmetry "
     "gate)")
# #4 retarded/advanced: the advanced completion flips the i pi branch
SIGA = (C4 / sp.pi) * om**4 * (sp.log(mu**2 / om**2) - sp.I * sp.pi)
check(sp.simplify(SIGA - sp.conjugate(SIG0.subs({c0: 0, c2: 0, c4: 0})
                                      ).rewrite(sp.log)) == 0,
      "#4 retarded/advanced: Sigma_A = Sigma_R* on the real axis "
      "(branch flip = conjugation; upper/lower half-plane pair)",
      gate="T4-7")
# #7 first-order vs resummed distinction, ON THE SHIPPED OBJECTS
# (review FINDING 3: the first version proved the identity on a
# parallel toy and never touched the real pair; repaired)
sig_sym = sp.Symbol("Sig")
GRs = 1 / (om**2 / (2 * kap**2) - sig_sym)
G1s = sp.expand(2 * kap**2 / om**2 + (2 * kap**2 / om**2)**2 * sig_sym)
check(sp.simplify(GR - GRs.subs(sig_sym, SIG)) == 0
      and sp.simplify(sp.expand(G1 - G1s.subs(sig_sym, SIG))) == 0,
      "#7a the SHIPPED G_R and G_1 are exactly the Dyson forms of the "
      "assembled Sigma (toy-to-real tie, both objects)", gate="T4-7")
ser = sp.series(GRs, sig_sym, 0, 3).removeO()
check(sp.simplify(ser - G1s - (2 * kap**2 / om**2)**3 * sig_sym**2) == 0,
      "#7b Dyson pair: G_R - G_1 = G0^3 Sigma^2 + O(Sigma^3) EXACTLY "
      "(symbolic; the agreement domain is |lam| << 1, REPORTED per the "
      "frozen charter)", gate="T4-7")
g1_val, g1_flag, _ = eval_KR(wv, Hv, kv, obj="G1")
gr_ref, _, _ = eval_KR(wv, Hv, kv, obj="GR")
rel17 = abs(g1_val - gr_ref) / abs(gr_ref)
check(rel17 < mp.mpf("1e-5") and g1_flag == "CONTROLLED",
      "#7c the first-order object is EXERCISED numerically in-domain: "
      "|G_1 - G_R|/|G_R| = %s ~ lam^2 (agreement domain confirmed; G1 "
      "no longer ships uncertified)" % mp.nstr(rel17, 3), gate="T4-7")
# #8 wrong retarded sign control
SIG_bad = (C4 / sp.pi) * om**4 * (sp.log(mu**2 / om**2) - sp.I * sp.pi)
GR_bad = 1 / (1 / G0 - SIG_bad)
f_bad = sp.lambdify((om, H, kap, mu), GR_bad, "mpmath")
control(mp.im(f_bad(wv, Hv, kv, 1)) > 0,
        "#8 wrong-retarded-sign: flipping the branch flips "
        "Im G_R > 0 -- detected by the passivity gate")
# #9 wrong symmetry factor control
SIG_x2 = 2 * SIG0.subs({c0: 0, c2: 0, c4: 0})
control(sp.simplify(sp.im(SIG_x2) - im0.subs(kap, 1)) != 0,
        "#9 wrong-symmetry-factor: a doubled Sigma fails the frozen "
        "flat-anchor identity -- detected")
# #11 independent numeric evaluation of K_R at fixed omega/H >> 1:
# route A = the assembled log-form; route B = frozen absorptive value +
# numeric subtracted dispersion (independent of the log identity)
wv2 = mp.mpf("1.3")
sig_A, sig_flag, _ = eval_KR(wv2, mp.mpf("0.01"), mp.mpf("0.1"),
                             obj="sigma")
check(sig_flag == "CONTROLLED", "evaluation #11 flag ASSERTED "
      "CONTROLLED", gate="T4-4")
imB = -3 * wv2**4 / (1280 * mp.pi) \
    - mp.mpf(str(0.01))**2 * 13 * wv2**2 / (480 * mp.pi)
# Re route B: subtracted dispersion (H0 piece; polynomial-free content
# compared through the 5th-derivative gate above -- here compare Im
# directly and Re modulo the declared local slot):
relB = abs(mp.im(sig_A) - imB) / abs(imB)
check(relB < mp.mpf("1e-20"),
      "#11 numeric evaluation integrity: Im K_R(omega/H = 130) "
      "through the domain-gated evaluator chain == direct arithmetic "
      "on the frozen absorptive data (rel %s); the Re part's "
      "polynomial-free content is independently covered by the "
      "Kramers-Kronig gate, and its local slot is symbolic by "
      "construction" % mp.nstr(relB, 3), gate="T4-7")

# ================= T4-8: ANALYTIC STRUCTURE =================
print("\n=== T4-8: ANALYTIC STRUCTURE (contract object only) ===")
note("BRANCH STRUCTURE (unconditional): the gapless two-graviton "
     "continuum gives a branch point at omega = 0 with a cut along the "
     "real axis (the log in the completion); no gap, no threshold at "
     "finite omega. This is one-loop branch structure, present in BOTH "
     "Dyson forms.")
note("POLE STRUCTURE (classified, not assumed): G0^{-1} has the double "
     "zero at omega = 0 (the massless graviton). In the resummed "
     "denominator D = omega^2/(2 kappa^2) - Sigma_R: (i) whether the "
     "omega = 0 pole survives is decided by the LOCAL slot (c0 = 0 "
     "preserves it; c0 != 0 shifts it) -- a D5/renormalization-condition "
     "question, DEFERRED, recorded parametrically; (ii) additional "
     "zeros require |2 kappa^2 Sigma/omega^2| ~ 1, which in the "
     "reference slice needs (kappa omega)^2 |log| ~ 1 -- OUTSIDE the "
     "EFT/perturbative domain; no in-domain pole exists.")
# executable real-axis denominator bound (review FINDING 2 repair:
# this is a POINTWISE-PLUS-INTERVAL bound on the REAL frequency
# segment, NOT a Rouche/contour statement -- the complex-plane no-zero
# claim stays parametric prose. Conditions stated AND frozen into the
# artifact: reference slice c = 0, kappa = 0.1 units, mu = 1,
# CONTROLLED band only.)
lam_f = sp.lambdify((om, H, kap, mu),
                    sp.Abs(2 * kap**2 * SIG.subs(LOCAL0) / om**2),
                    "mpmath")
lam_max = 0
grid = [(w, h2) for w in ("0.3", "0.6", "1.0", "2.0", "4.0")
        for h2 in ("0.0", "0.02", "0.05")]
for w, h2 in grid:
    if mp.mpf(104) / 9 * mp.mpf(h2)**2 / mp.mpf(w)**2 > mp.mpf("0.1"):
        continue
    lam_max = max(lam_max, lam_f(mp.mpf(w), mp.mpf(h2), mp.mpf("0.1"), 1))
# INTERVAL bound on [0.3, 4] (H = 0 worst case within the slice): each
# |lam| piece is (kappa om)^2 x (|log(1/om^2)| + pi) x |C|-numbers, and
# both factors are bounded by their endpoint/turning values on the
# segment; an executable sup bound, no sampling gap:
wlo, whi, kv8 = sp.Rational(3, 10), sp.Integer(4), sp.Rational(1, 10)
logmax = sp.Max(sp.Abs(sp.log(1 / wlo**2)), sp.Abs(sp.log(1 / whi**2)))
# sup over the segment of |lam| = 2 kappa^2 om^2 |L| x
# [3/1280 pi^2 + (H/om)^2 13/480 pi^2]; in the CONTROLLED band
# (H/om)^2 <= 0.1 x 9/104, and om^2(|log|+pi) is maximized at whi with
# logmax -- an executable sup bound with the H^2 band INCLUDED (the
# first draft wrongly called H = 0 the worst case; H^2 ADDS)
lam_sup = sp.N(2 * kv8**2 * whi**2 * (logmax + sp.pi)
               * (sp.Rational(3, 1280) / sp.pi**2
                  + sp.Rational(9, 1040) * sp.Rational(13, 480)
                  / sp.pi**2), 10)
check(lam_max < mp.mpf("0.05") and float(lam_sup) < 0.05,
      "IN-DOMAIN REAL-AXIS DENOMINATOR BOUND (pointwise grid max |lam| "
      "= %s AND an executable interval sup bound %s on omega in "
      "[0.3, 4], CONTROLLED H^2 band included) -- CONDITIONS: reference "
      "slice c = 0, kappa = 0.1 units, mu = 1; the resummed "
      "denominator cannot vanish on that real segment. NOT a "
      "Rouche/contour statement; the complex-plane and general-slice "
      "no-pole statements remain PARAMETRIC (the local slot is "
      "undetermined) and no pole claim is made"
      % (mp.nstr(lam_max, 3), str(lam_sup)), gate="T4-8")
note("second sheet: the log's continuation (L -> L - 2 pi i) is "
     "recorded as the declared second-sheet map; second-sheet zeros of "
     "D sit at (kappa omega)^2 ~ 1/|log| -- out of domain; NOT "
     "certified as physical poles (certification machinery would be "
     "required and no in-domain candidate exists). The matter-sector "
     "pole result is NOT imported and NOT assumed.")
OUT["analytic_structure"] = {
    "branch": "branch point omega = 0, real-axis cut (gapless "
              "two-graviton continuum); one-loop in both Dyson forms",
    "poles": "omega = 0 graviton pole preserved iff c0 = 0 (D5 "
             "condition, deferred, parametric). No additional zeros of "
             "the resummed denominator ON THE REAL CONTROLLED SEGMENT, "
             "CONDITIONAL ON: reference slice c = 0, kappa = 0.1 units, "
             "mu = 1 (executable pointwise + interval bound). The "
             "general-slice and complex-plane statements are PARAMETRIC "
             "ONLY (the local slot is undetermined; the (kappa omega)^2 "
             "|log| ~ 1 candidates are outside the EFT domain). NO pole "
             "claim is made; nothing is certified",
    "second_sheet": "L -> L - 2 pi i declared; no in-domain content"}

# ================= T4-9: WARD BOOKKEEPING =================
print("\n=== T4-9: WARD ===")
ward = T3F["out"].get("ward_diagnostic_H0", "")
# provenance cross-check (review FINDING 5): the same record must appear
# in the PINNED merged T3 artifact -- the ward string is provenance-locked
# through two independently hashed files, not merely nonempty
T3M = json.loads(open(os.path.join(
    HERE, "WALL_KR_TIER3_LOOP_RESULT.json")).read())
ward_m = T3M["stages"]["flat"]["out"].get("ward_diagnostic_H0", "")
check(str(ward) == str(ward_m) and len(str(ward)) > 0
      and str(ward) != "0",
      "T3 Ward record carried: the H^0 gauge-image contraction is "
      "NONZERO (class: SAME CLASS as the T3 finding; the graviton-loop "
      "analogue of the Class-B structure persists). K_R is TT-scoped by "
      "the frozen charter (section 6): the residual is EXCLUDED by "
      "construction, NOT resolved, NOT repaired, and K_R was NOT "
      "altered to change it", gate="T4-9")
OUT["ward"] = {"classification": "same class (nonzero gauge-image "
               "contraction at H^0, carried from the frozen T3 record)",
               "disposition": "EXCLUDED from K_R by TT scope; separate "
                              "unresolved finding"}

# ================= T4-10: FREEZE =================
print("\n=== T4-10: FREEZE ===")
RESULT = {"instrument": "wall_kr_tier4_retarded.py",
          "instrument_sha256": sha_file(os.path.abspath(__file__)),
          "authorization": "owner 2026-09-01: TIER 4 CONTRACT-LEVEL "
                           "RETARDED K_R ASSEMBLY ONLY",
          "out": OUT, "checks": CHECKS, "notes": NOTES,
          "failures": FAILS,
          "elapsed_s": round(time.time() - T0, 1),
          "hard_stop": "no benchmark consequence, no J(omega), no Ward "
                       "repair, no bridge, no added operators, no sign "
                       "changes, no omega << H extrapolation, no noise "
                       "import. Next stage: owner/reviewer adjudication."}
outp = os.path.join(HERE, "WALL_KR_CONTRACT_RETARDED_RESULT.json")
json.dump(RESULT, open(outp, "w"), indent=1, default=str)
h1 = sha_file(outp)
reread = json.loads(open(outp).read())
h2 = sha_file(outp)
check(h1 == h2 and reread["instrument"] == "wall_kr_tier4_retarded.py",
      "artifact written, re-read, re-hashed identically (sha %s...)"
      % h1[:16], gate="T4-10")
MAN = {"artifact": "WALL_KR_CONTRACT_RETARDED_RESULT.json",
       "artifact_sha256": h1,
       "inputs": {fn: sha_file(os.path.join(HERE, fn))
                  for fn in PINS},
       "instrument_sha256": sha_file(os.path.abspath(__file__)),
       "date": "2026-09-01"}
manp = os.path.join(HERE, "WALL_KR_CONTRACT_RETARDED_MANIFEST.json")
json.dump(MAN, open(manp, "w"), indent=1)
print("manifest: %s (sha %s...)" % (manp, sha_file(manp)[:16]))
npass = sum(1 for c in CHECKS if c["pass"])
print("\nTIER 4 RETARDED K_R: %d/%d passed; failures: %d"
      % (npass, len(CHECKS), len(FAILS)))
for m in FAILS:
    print("  FAILURE: " + m)
print("HARD STOP: the retarded contract K_R record is frozen pending "
      "owner adjudication.")
sys.exit(0 if not FAILS else 1)
