#!/usr/bin/env python3
"""K_R^(contract) TIER 1 -- THE dS TT-TT-TT CUBIC VERTEX (owner countersign
d5dc33b; declarations D1=1a, D2=2a, D3=3a binding; ONLY Tier 1).

OBJECT: the cubic sector of (1/2kappa^2) sqrt(-g)(R - 2 Lambda), Lambda=3H^2,
around g = a^2(u)(eta + h), frozen chart a^2 = 1 + 2Hu + 3H^2u^2, FULL
gauge-unfixed h (D2 = 2a), three graded plane waves.

REPRESENTATION (charter-binding): three-sector nilpotent graded algebra
(sector key = frozenset of {1,2,3}; eps_i^2 = 0 automatic), phases stripped
(d_mu adds i*p_i_mu per sector member; explicit u-dependence differentiated),
det by the exact cubic trace formula, explicit component loops, stage timers,
20-minute stop rule armed.

GATES G1-G7 with negative controls (see the coordination log, disclosed
before this run). HARD STOP at the Tier-1 boundary. W-0.
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
FAILS = []
CHECKS = []
NOTES = []


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


# ================= S0: CONVENTIONS (frozen; cited) =================
print("=== S0: CONVENTIONS ===")
note("metric mostly-minus; g = a^2(u)(eta + h); chart a^2 = 1+2Hu+3H^2u^2 "
     "(Section D, gated); FULL h (10 comps, D2=2a unfixed); action "
     "(1/2kappa^2) sqrt(-g)(R - 2 Lambda), Lambda = 3H^2; vertex reported "
     "per 1/(2 kappa^2); three plane waves, momenta p1,p2,p3, spatial "
     "conservation imposed only where a gate declares it")
eta = sp.diag(1, -1, -1, -1)
etainv = eta
H, u = sp.symbols("H u")
NH = 3          # keep H^0, H^1, H^2


def hexp(expr):
    """truncate to O(H^2) in the graded chart."""
    return sp.expand(sp.series(sp.expand(expr), H, 0, NH).removeO())


a2 = 1 + 2 * H * u + 3 * H**2 * u**2
a2inv = hexp(1 - 2 * H * u + H**2 * u**2)    # (1+2Hu+3H^2u^2)^-1 to O(H^2)
check(hexp(a2 * a2inv) == 1, "chart gate: a^2 * (a^2)^-1 == 1 through O(H^2)",
      gate="S0")
# run-5 correction (disclosed, DERIVED not assumed): the pipeline's Ricci
# sign convention gives background R(dS) = -12 H^2 (computed exactly on
# a = 1/(1-Hu) with the same Christoffel/Ricci formulas -- executed as the
# Lambda gate below), so the chart-consistent cosmological constant in THIS
# convention is Lambda = R/4 = -3 H^2. Run-4 assumed the textbook +3H^2 and
# the with-Lambda EOM gate failed while the without-Lambda control passed --
# exactly the wrong-sign signature. Convention-internal; physics unchanged.
LAM = -3 * H**2

# LAMBDA GATE (exact, cheap): background R for a = 1/(1-Hu) in THIS
# pipeline's conventions must equal 4*LAM.
_u2, _H2 = sp.symbols("_u2 _H2")
_a = 1 / (1 - _H2 * _u2)
_g = _a**2 * eta
_gi = eta / _a**2
_xs = [_u2] + list(sp.symbols("_zx1 _zx2 _zx3"))
_G = {}
for _l in range(4):
    for _m in range(4):
        for _n in range(4):
            _s = sum(_gi[_l, _r] * (sp.diff(_g[_r, _n], _xs[_m])
                                    + sp.diff(_g[_r, _m], _xs[_n])
                                    - sp.diff(_g[_m, _n], _xs[_r]))
                     for _r in range(4)) / 2
            _G[(_l, _m, _n)] = sp.simplify(_s)
_R = sp.simplify(sum(_gi[_m, _n] * (
    sum(sp.diff(_G[(_l, _m, _n)], _xs[_l])
        - sp.diff(_G[(_l, _m, _l)], _xs[_n])
        + sum(_G[(_l, _l, _r)] * _G[(_r, _m, _n)]
              - _G[(_l, _n, _r)] * _G[(_r, _m, _l)] for _r in range(4))
        for _l in range(4)))
    for _m in range(4) for _n in range(4)))
check(sp.simplify(_R - 4 * LAM.subs(H, _H2)) == 0,
      "LAMBDA GATE (derived in-convention): background R(dS exact) = %s "
      "= 4*Lambda with Lambda = -3H^2 -- the chart-consistent value in the "
      "pipeline's own Ricci sign convention" % _R, gate="S0")

# sectors: keys are frozensets of {1,2,3}; values: dict (mu-structure) ->
# coefficient. We store graded SCALARS as {key: expr} and graded 4x4 tensors
# as {key: Matrix}. Momenta: p[i][mu] symbols; polarisations e[i][mu][nu].
P = {i: [sp.Symbol("p%d_%d" % (i, mu)) for mu in range(4)] for i in (1, 2, 3)}
E = {}
for i in (1, 2, 3):
    M = sp.zeros(4, 4)
    for mu in range(4):
        for nu in range(mu, 4):
            s_ = sp.Symbol("e%d_%d%d" % (i, mu, nu))
            M[mu, nu] = s_
            M[nu, mu] = s_
    E[i] = M
I_ = sp.I
KEYS = [frozenset(s) for s in
        [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]]


def gz():
    return {k: sp.zeros(4, 4) for k in KEYS}


def gs():
    return {k: sp.Integer(0) for k in KEYS}


def madd(A, B):
    return {k: A[k] + B[k] for k in KEYS}


def mmulmat(A, B):
    """graded matrix product with nilpotent truncation."""
    out = gz()
    for ka in KEYS:
        for kb in KEYS:
            if ka & kb:
                continue
            kc = ka | kb
            out[kc] = out[kc] + A[ka] * B[kb]
    return out


def smul(A, B):
    """graded scalar product."""
    out = gs()
    for ka in KEYS:
        for kb in KEYS:
            if ka & kb:
                continue
            out[ka | kb] = out[ka | kb] + sp.expand(A[ka] * B[kb])
    return out


def sscale(A, c):
    return {k: sp.expand(c * A[k]) for k in KEYS}


def mscale(A, c):
    return {k: c * A[k] for k in KEYS}


def d_mu(obj, mu, is_mat):
    """phase-stripped derivative: on sector k adds i*sum_{j in k} p_j_mu;
    plus d/du on the explicit u-dependence when mu == 0."""
    out = gz() if is_mat else gs()
    for k in KEYS:
        ph = sum((P[j][mu] for j in k), sp.Integer(0))
        term = I_ * ph * obj[k]
        if mu == 0:
            term = term + (obj[k].applyfunc(lambda x: sp.diff(x, u))
                           if is_mat else sp.diff(obj[k], u))
        out[k] = term if (is_mat or True) else term
    return out




def is_total_derivative(L1, i_wave, order_H=0):
    """G4/G7b corrected criterion (run-3, disclosed): the linear-sector
    DENSITY need not vanish pointwise -- linearized sqrt(-g)R is a total
    derivative. The executable gate: L1 lies in the image of the divergence
    operator (i p_mu + delta_mu0 d/du) acting on a generous polynomial
    ansatz V^mu (linear in e_i, degree <= 1 in p_i, chart powers of H,u).
    Returns (ok, residual)."""
    pi = P[i_wave]
    ei = E[i_wave]
    tre = sum(eta[m, m] * ei[m, m] for m in range(4))
    # vector structures linear in e
    # run-4 repair (disclosed): the ansatz vectors must be CONTRAVARIANT
    # V^mu (the divergence sums d_mu V^mu index-honestly); run-3 omitted the
    # outer eta-raisings, so the ansatz spanned the wrong vectors and the
    # image test could not close on the pipeline's index-consistent L1.
    base_vecs = []
    for mu in range(4):
        gmu = eta[mu, mu]                      # eta^{mu mu} (diagonal)
        row = []
        row.append(gmu * sum(ei[mu, n] * eta[n, n] * pi[n]
                             for n in range(4)))       # e^{mu nu} p_nu
        row.append(gmu * pi[mu] * tre)                  # p^mu tr e
        row.append(gmu * ei[mu, 0])                     # e^{mu}_0-type
        row.append((1 if mu == 0 else 0) * tre)         # n^mu tr e
        row.append((1 if mu == 0 else 0) * ei[0, 0])    # n^mu e_00
        row.append((1 if mu == 0 else 0)
                   * sum(eta[n, n] * pi[n] * sum(ei[n, r] * eta[r, r] * pi[r]
                         for r in range(4)) for n in range(4)))  # n^mu (pep)
        row.append(gmu * pi[mu] * ei[0, 0])             # p^mu e_00
        row.append(gmu * ei[mu, 0] * pi[0])             # e^{mu}_0 p_0
        row.append((1 if mu == 0 else 0)
                   * sum(ei[0, n] * eta[n, n] * pi[n] for n in range(4)))
        base_vecs.append(row)
    NB = len(base_vecs[0])
    hu_pows = [sp.Integer(1), H * u, H, H**2 * u, H**2 * u**2, H**2 * u**3,
               H * u**2, H**2]
    coeffs = []
    div = sp.Integer(0)
    ci = 0
    for b in range(NB):
        for hp in hu_pows:
            c = sp.Symbol("cV_%d" % ci)
            ci += 1
            coeffs.append(c)
            for mu in range(4):
                term = c * hp * base_vecs[mu][b]
                div = div + I_ * pi[mu] * term
                if mu == 0:
                    div = div + c * sp.diff(hp, u) * base_vecs[0][b]
    resid = sp.expand(hexp(sp.expand(L1 - div)))
    # solve: every monomial in (e, p, u, H) must cancel
    esyms = [ei[m, n] for m in range(4) for n in range(m, 4)]
    eqs = []
    pol = sp.Poly(resid, *(esyms + pi + [u, H]))
    for monom, coef in pol.terms():
        eqs.append(coef)
    sol = sp.solve(eqs, coeffs, dict=True)
    if not sol:
        return False, resid
    return True, sp.Integer(0)

# ================= S1: GRADED-ALGEBRA SELF-TESTS (G1) =================
print("\n=== S1: G1 GRADED-ALGEBRA SELF-TESTS ===")
A_ = gs()
A_[frozenset((1,))] = sp.Symbol("x1")
B_ = gs()
B_[frozenset((1,))] = sp.Symbol("y1")
B_[frozenset((2,))] = sp.Symbol("y2")
Cc = smul(A_, B_)
check(Cc[frozenset((1, 2))] == sp.Symbol("x1") * sp.Symbol("y2")
      and Cc[frozenset((1,))] == 0,
      "G1: nilpotency (eps_1^2 = 0) and cross-sector product exact",
      gate="G1")
T_ = gs()
T_[frozenset((2,))] = u * sp.Symbol("z2")
D0 = d_mu(T_, 0, False)
check(sp.expand(D0[frozenset((2,))]
                - (I_ * P[2][0] * u + 1) * sp.Symbol("z2")) == 0,
      "G1: derivative rule = i p_mu (phase) + d/du (explicit u), verified",
      gate="G1")
control(smul(A_, A_)[frozenset((1,))] == 0 and True,
        "G1 control: eps_1 * eps_1 annihilates (a non-nilpotent bug would "
        "put x1^2 in sector {1})")
stamp("graded algebra verified")


# ================= S2: THE METRIC PIPELINE =================
print("\n=== S2: METRIC -> CHRISTOFFEL -> RICCI -> DENSITY ===")


def build_density(hmats, a2f, a2invf, lam):
    """graded sqrt(-g) (R - 2 lam) / (per 1/2kappa^2 convention) for
    g = a2f * (eta + h), h = sum_i eps_i hmats[i]. Returns graded scalar."""
    hg = gz()
    for i in (1, 2, 3):
        hg[frozenset((i,))] = hmats[i]
    # g_lower = a2f*(eta + h); g_upper = a2invf*(eta - h + h^2 - h^3) (eta
    # raising: h with upper indices = eta h eta etc. -- work with MIXED forms
    # to keep index logic simple: define A = eta^{-1} h (mixed (1,1))
    Amix = {k: etainv * hg[k] for k in KEYS}
    # (1+A)^-1 = 1 - A + A^2 - A^3 (graded; A^4 = 0)
    A2m = mmulmat(Amix, Amix)
    A3m = mmulmat(A2m, Amix)
    inv_series = gz()
    inv_series[frozenset()] = sp.eye(4)
    inv_series = madd(inv_series, mscale(Amix, -1))
    inv_series = madd(inv_series, A2m)
    inv_series = madd(inv_series, mscale(A3m, -1))
    # g^{mu nu} = a2invf * (1+A)^{-1} eta^{-1}
    gup = {k: sp.expand(a2invf) * (inv_series[k] * etainv) for k in KEYS}
    gup = {k: gup[k].applyfunc(hexp) for k in KEYS}
    # g_{mu nu} = a2f (eta + h)
    glo = gz()
    glo[frozenset()] = a2f * eta
    for i in (1, 2, 3):
        glo[frozenset((i,))] = a2f * hmats[i]
    glo = {k: glo[k].applyfunc(hexp) for k in KEYS}
    # sqrt(-g): det(g) = a2f^4 det(eta+h) = a2f^4 * det(eta) * det(1+A)
    trA = {k: sp.expand(sp.trace(Amix[k])) for k in KEYS}
    trA2 = {k: sp.expand(sp.trace(A2m[k])) for k in KEYS}
    trA3 = {k: sp.expand(sp.trace(A3m[k])) for k in KEYS}
    detf = gs()
    detf[frozenset()] = sp.Integer(1)
    detf = {k: detf[k] + trA[k] for k in KEYS}
    half = sp.Rational(1, 2)
    six = sp.Rational(1, 6)
    t2 = smul(trA, trA)
    t3 = smul(smul(trA, trA), trA)
    tt2 = smul(trA, trA2)
    for k in KEYS:
        detf[k] = sp.expand(detf[k] + half * (t2[k] - trA2[k])
                            + six * (t3[k] - 3 * tt2[k] + 2 * trA3[k]))
    # sqrt(det(1+A)) = exp(1/2 ln det) -- cubic-truncated via series:
    # sqrt(1+x) with x = detf - 1 (graded):
    xg = dict(detf)
    xg[frozenset()] = detf[frozenset()] - 1
    x2 = smul(xg, xg)
    x3 = smul(smul(xg, xg), xg)
    sq = gs()
    sq[frozenset()] = sp.Integer(1)
    for k in KEYS:
        sq[k] = sp.expand(sq[k] + half * xg[k] - sp.Rational(1, 8) * x2[k]
                          + sp.Rational(1, 16) * x3[k])
    sqrtg = {k: hexp(sp.expand(sq[k] * a2f**2)) for k in KEYS}
    # Christoffels
    dg = {mu: d_mu(glo, mu, True) for mu in range(4)}
    Gam = {}
    for lam_i in range(4):
        for mu in range(4):
            for nu in range(mu, 4):
                acc = gs()
                for rho in range(4):
                    gr = {k: gup[k][lam_i, rho] for k in KEYS}
                    br = {k: sp.expand(dg[mu][k][rho, nu] + dg[nu][k][rho, mu]
                                       - dg[rho][k][mu, nu]) for k in KEYS}
                    pr = smul(gr, br)
                    for k in KEYS:
                        acc[k] = acc[k] + pr[k]
                Gam[(lam_i, mu, nu)] = {k: hexp(sp.expand(acc[k] / 2))
                                        for k in KEYS}
    def G(l, m_, n_):
        return Gam[(l, m_, n_)] if m_ <= n_ else Gam[(l, n_, m_)]
    stamp("  christoffels built")
    # Ricci: R_{mu nu} = d_lam G^lam_{mu nu} - d_nu G^lam_{mu lam}
    #                    + G^lam_{lam rho} G^rho_{mu nu}
    #                    - G^lam_{nu rho} G^rho_{mu lam}
    Ric = {}
    Gtr = {}
    for rho in range(4):
        acc = gs()
        for lam_i in range(4):
            gg = G(lam_i, lam_i, rho)
            for k in KEYS:
                acc[k] = acc[k] + gg[k]
        Gtr[rho] = acc
    for mu in range(4):
        for nu in range(mu, 4):
            acc = gs()
            for lam_i in range(4):
                t1 = d_mu(G(lam_i, mu, nu), lam_i, False)
                for k in KEYS:
                    acc[k] = acc[k] + t1[k]
            t2_ = d_mu(Gtr[mu] if False else Gtr[mu], nu, False)
            # careful: term 2 is d_nu G^lam_{mu lam} = d_nu Gtr[mu]
            for k in KEYS:
                acc[k] = acc[k] - t2_[k]
            for rho in range(4):
                pr1 = smul(Gtr[rho], G(rho, mu, nu))
                for k in KEYS:
                    acc[k] = acc[k] + pr1[k]
                for lam_i in range(4):
                    pr2 = smul(G(lam_i, nu, rho), G(rho, mu, lam_i))
                    for k in KEYS:
                        acc[k] = acc[k] - pr2[k]
            Ric[(mu, nu)] = {k: hexp(sp.expand(acc[k])) for k in KEYS}
    stamp("  ricci built")
    def Rc(m_, n_):
        return Ric[(m_, n_)] if m_ <= n_ else Ric[(n_, m_)]
    Rsc = gs()
    for mu in range(4):
        for nu in range(4):
            gr = {k: gup[k][mu, nu] for k in KEYS}
            pr = smul(gr, Rc(mu, nu))
            for k in KEYS:
                Rsc[k] = Rsc[k] + pr[k]
    Rsc = {k: hexp(sp.expand(Rsc[k])) for k in KEYS}
    Rm2L = dict(Rsc)
    Rm2L[frozenset()] = sp.expand(Rsc[frozenset()] - 2 * lam)
    dens = smul(sqrtg, Rm2L)
    return {k: hexp(sp.expand(dens[k])) for k in KEYS}


stamp("pipeline defined")

# ================= S3: FLAT STAGE (H = 0) + GATES =================
STAGE_EARLY = sys.argv[1] if len(sys.argv) > 1 else "flat"
if STAGE_EARLY == "ds":
    note("ds stage: flat gates already certified in the flat-stage process; "
         "loading the frozen flat vertex from cache")
print("\n=== S3: FLAT VERTEX + GATES G2-G6 ===")
if STAGE_EARLY == "ds":
    # skip straight to S4 via the stage-split block (V3_FLAT from cache)
    n3 = 0
    V3_FLAT = None
    DENS_FLAT = None
if STAGE_EARLY != "ds":
    t_flat = time.time()
    DENS_FLAT = build_density({i: E[i] for i in (1, 2, 3)},
                              sp.Integer(1), sp.Integer(1), sp.Integer(0))
    V3_FLAT = DENS_FLAT[frozenset((1, 2, 3))]
    n3 = len(sp.Add.make_args(V3_FLAT))
    stamp("flat cubic vertex: %d terms (%.1fs)" % (n3, time.time() - t_flat))
    check(n3 > 50, "flat cubic sector is nontrivial (%d terms -- the "
          "'hundreds of terms' object)" % n3, gate="S3")
    # G4 (run-3 corrected, disclosed): the linear density is a TOTAL
    # DERIVATIVE, not pointwise zero -- linearized sqrt(-g)R around a
    # solution is div V. Gate: divergence-image membership (exact solve).
    ok4, res4 = is_total_derivative(DENS_FLAT[frozenset((1,))], 1)
    check(ok4, "G4 (flat, corrected): the linear sector is EXACTLY a total "
          "derivative (divergence-image solve closes; flat solves the "
          "vacuum EOM at action level)", gate="G4")
    # G2 CONFORMAL EXACT ANCHOR: h_i = 2 phi_i eta (conformal); independent
    # exact route: R(Omega^2 eta) computed non-graded for scalar Omega(x)
    phi = {i: sp.Symbol("phi%d" % i) for i in (1, 2, 3)}
    DENS_CONF = build_density({i: 2 * phi[i] * eta for i in (1, 2, 3)},
                              sp.Integer(1), sp.Integer(1), sp.Integer(0))
    # independent route: exact metric Om^2 eta with Om^2 = 1 + 2*sum(eps phi X)
    # computed via sympy on a diagonal metric with ONE scalar function f(x):
    xs = sp.symbols("x0 x1 x2 x3")
    f = sp.Function("f")(*xs)
    gL = f * eta                      # g_{mu nu} = f * eta (f = Omega^2)
    gU = eta / f
    Gamx = {}
    for l in range(4):
        for m_ in range(4):
            for n_ in range(m_, 4):
                s_ = sp.Integer(0)
                for r in range(4):
                    s_ += gU[l, r] * (sp.diff(gL[r, n_], xs[m_])
                                      + sp.diff(gL[r, m_], xs[n_])
                                      - sp.diff(gL[m_, n_], xs[r]))
                Gamx[(l, m_, n_)] = sp.simplify(s_ / 2)
    def Gx(l, m_, n_):
        return Gamx[(l, m_, n_)] if m_ <= n_ else Gamx[(l, n_, m_)]
    Rx = sp.Integer(0)
    for mu in range(4):
        for nu in range(4):
            acc = sp.Integer(0)
            for l in range(4):
                acc += sp.diff(Gx(l, mu, nu), xs[l]) - sp.diff(Gx(l, mu, l),
                                                               xs[nu])
                for r in range(4):
                    acc += Gx(l, l, r) * Gx(r, mu, nu) - Gx(l, nu, r) * Gx(r, mu, l)
            Rx += gU[mu, nu] * acc
    dens_exact = sp.simplify((-sp.det(gL))**sp.Rational(1, 2) * Rx)
    stamp("  exact conformal density computed (independent route)")
    # expand the exact density with f = 1 + 2(s1+s2+s3) plane-wave scalars,
    # graded: substitute f and derivatives via the graded phases
    s_amp = {i: sp.Symbol("s%d" % i) for i in (1, 2, 3)}
    # build the graded expansion of the exact density by Taylor in the three
    # amplitudes: substitute f -> 1 + t1 + t2 + t3 with t_i carrying phase p_i
    t1_, t2_, t3_ = sp.symbols("t1 t2 t3")
    subs_f = {}
    fexpr = 1 + t1_ + t2_ + t3_
    subs_f[f] = fexpr
    for mu in range(4):
        subs_f[sp.diff(f, xs[mu])] = I_ * (P[1][mu] * t1_ + P[2][mu] * t2_
                                           + P[3][mu] * t3_)
        for nu in range(4):
            subs_f[sp.diff(f, xs[mu], xs[nu])] = -(
                P[1][mu] * P[1][nu] * t1_ + P[2][mu] * P[2][nu] * t2_
                + P[3][mu] * P[3][nu] * t3_)
    dex = dens_exact.subs(subs_f, simultaneous=True)
    dex = sp.expand(sp.series(sp.series(sp.series(sp.expand(dex),
                    t1_, 0, 2).removeO(), t2_, 0, 2).removeO(),
                    t3_, 0, 2).removeO())
    cubic_exact = dex.coeff(t1_, 1).coeff(t2_, 1).coeff(t3_, 1)
    cubic_pipe = DENS_CONF[frozenset((1, 2, 3))].subs(
        {phi[1]: sp.Rational(1, 2), phi[2]: sp.Rational(1, 2),
         phi[3]: sp.Rational(1, 2)})
    diffc = sp.expand(sp.together(cubic_exact - cubic_pipe))
    check(sp.simplify(diffc) == 0,
          "G2 CONFORMAL EXACT ANCHOR: the pipeline's cubic conformal density == "
          "the independent exact R(Omega^2 eta) route, POINTWISE (no IBP "
          "freedom) -- signs, normalization, and the full nonlinear structure "
          "certified at once", gate="G2")
    clear_cache()
    # G3 quadratic anchor: eps1-eps2 sector on TT waves ~ known kinetic form
    q12 = DENS_FLAT[frozenset((1, 2))]
    ttsub = {}
    for i in (1, 2):
        for mu in range(4):
            for nu in range(mu, 4):
                ttsub[sp.Symbol("e%d_%d%d" % (i, mu, nu))] = 0
    ttsub[sp.Symbol("e1_11")] = 1
    ttsub[sp.Symbol("e1_22")] = -1
    ttsub[sp.Symbol("e2_11")] = 1
    ttsub[sp.Symbol("e2_22")] = -1
    q12tt = sp.expand(q12.subs(ttsub))
    # on TT (transverse to z, traceless), the quadratic density reduces to
    # (structure) * (p1.p2); verify proportionality to p1.p2 with momenta along z
    # run-2 gate repair (disclosed): the DENSITY carries EOM-class p^2 terms
    # off-shell (-2p1^2 - 3 p1.p2 - 2p2^2 structure); the physical quadratic
    # sector requires its own conservation p2 = -p1, under which the ratio to
    # p1.p2 must be a pure CONSTANT (run-1's gate omitted conservation -- gate
    # defect; the pipeline was right).
    zsub = {P[1][1]: 0, P[1][2]: 0, P[2][1]: 0, P[2][2]: 0}
    csub = {P[2][0]: -P[1][0], P[2][3]: -P[1][3]}
    q12z = sp.expand(q12tt.subs(zsub).subs(csub))
    p1p2 = sp.expand((P[1][0] * P[2][0] - P[1][3] * P[2][3]).subs(csub))
    ratio = sp.simplify(q12z / p1p2)
    check(sp.simplify(sp.diff(ratio, P[1][0])) == 0
          and sp.simplify(sp.diff(ratio, P[1][3])) == 0,
          "G3 quadratic anchor (conservation-imposed): TT eps1-eps2 density = "
          "CONSTANT x (p1.p2), constant = %s -- the kinetic normalization "
          "RECORDED for the G0 convention chain" % sp.simplify(ratio), gate="G3")
    # G5 symmetry: exchange (e1,p1) <-> (e2,p2) leaves V3 invariant
    swap = {}
    for mu in range(4):
        swap[P[1][mu]] = P[2][mu]
        swap[P[2][mu]] = P[1][mu]
        for nu in range(mu, 4):
            swap[sp.Symbol("e1_%d%d" % (mu, nu))] = sp.Symbol("e2_%d%d" % (mu, nu))
            swap[sp.Symbol("e2_%d%d" % (mu, nu))] = sp.Symbol("e1_%d%d" % (mu, nu))
    sym_ok = sp.expand(V3_FLAT - V3_FLAT.xreplace(swap)) == 0
    check(sym_ok, "G5: full 1 <-> 2 exchange symmetry of the cubic vertex "
          "(EXACT)", gate="G5")
    control(sp.expand((V3_FLAT + P[1][0] * sp.Symbol("e1_01")**1
                       * sp.Symbol("e2_00") * sp.Symbol("e3_00"))
                      - (V3_FLAT + P[1][0] * sp.Symbol("e1_01")
                         * sp.Symbol("e2_00") * sp.Symbol("e3_00")).xreplace(swap))
            != 0, "G5 control: an injected asymmetric term breaks the exchange "
            "symmetry (the gate is not vacuous)")
    stamp("flat gates G2/G3/G4/G5 done")

    # G6 gauge gate: leg 3 pure gauge, legs 1,2 on-shell TT, momentum conservation
    xi = [sp.Symbol("xi%d" % mu) for mu in range(4)]
    gauge3 = sp.zeros(4, 4)
    for mu in range(4):
        for nu in range(4):
            gauge3[mu, nu] = I_ * (P[3][mu] * xi[nu] + P[3][nu] * xi[mu])
    g3sub = {}
    for mu in range(4):
        for nu in range(mu, 4):
            g3sub[sp.Symbol("e3_%d%d" % (mu, nu))] = gauge3[mu, nu]
    Vg = sp.expand(V3_FLAT.xreplace(g3sub))
    # legs 1,2: TT along z, on-shell p^2 = 0, p_z = +-omega
    ons = {sp.Symbol("e1_%d%d" % (m, n)): 0 for m in range(4) for n in range(m, 4)}
    ons.update({sp.Symbol("e2_%d%d" % (m, n)): 0
                for m in range(4) for n in range(m, 4)})
    w1, w2 = sp.symbols("w1 w2", positive=True)
    # run-2 repair: BOTH TT legs in the + polarisation (the run-1 +x pairing
    # can vanish by parity, making gate AND control vacuous -- the missed
    # control exposed exactly this)
    ons[sp.Symbol("e1_11")] = 1
    ons[sp.Symbol("e1_22")] = -1
    ons[sp.Symbol("e2_11")] = 1
    ons[sp.Symbol("e2_22")] = -1
    ons[P[1][0]] = w1
    ons[P[1][1]] = 0
    ons[P[1][2]] = 0
    ons[P[1][3]] = w1
    ons[P[2][0]] = w2
    ons[P[2][1]] = 0
    ons[P[2][2]] = 0
    ons[P[2][3]] = -w2
    ons[P[3][0]] = -(w1 + w2)
    ons[P[3][1]] = 0
    ons[P[3][2]] = 0
    ons[P[3][3]] = -(w1 - w2)
    Vg_os = sp.expand(Vg.subs(ons))
    check(sp.simplify(Vg_os) == 0,
          "G6 GAUGE GATE: pure-gauge leg 3 against two ON-SHELL TT legs with "
          "momentum conservation gives EXACTLY ZERO at density level (total "
          "derivatives die on the conserved ansatz; D2=2a's unfixed vertex is "
          "orbit-consistent)", gate="G6")
    control(sp.simplify(sp.expand(Vg.subs({**ons, P[3][3]: 0}))) != 0,
            "G6 control: breaking momentum conservation revives the gauge "
            "contraction (the zero is load-bearing, not identical)")
    stamp("flat stage complete")

# ================= STAGE SPLIT =================
STAGE = sys.argv[1] if len(sys.argv) > 1 else "flat"
CACHE = os.path.join(HERE, ".tier1_flat_cache.json")
if STAGE == "flat":
    json.dump({"V3_FLAT": sp.srepr(V3_FLAT),
               "flat_terms": n3}, open(CACHE, "w"))
    RESULT = {"stage": "TIER 1 flat stage", "checks": CHECKS,
              "notes": NOTES, "failures": FAILS,
              "elapsed_s": round(time.time() - T0, 1)}
    json.dump(RESULT, open(os.path.join(
        HERE, "WALL_KR_TIER1_FLAT_RESULT.json"), "w"), indent=1, default=str)
    print("\nFLAT STAGE gates: %d/%d passed; failures: %d"
          % (sum(1 for c in CHECKS if c["pass"]), len(CHECKS), len(FAILS)))
    for m in FAILS:
        print("  FAILURE: " + m)
    sys.exit(0 if not FAILS else 1)

# ================= S4: dS STAGE (fresh process; flat loaded from cache) =====
print("\n=== S4: dS STAGE (H-graded through O(H^2)) ===")
_c = json.load(open(CACHE))
V3_FLAT = sp.sympify(_c["V3_FLAT"])
n3 = _c["flat_terms"]
clear_cache()
t_ds = time.time()
DSCACHE = os.path.join(HERE, ".tier1_ds_cache.json")
if os.path.exists(DSCACHE):
    _dc = json.load(open(DSCACHE))
    if _dc.get("lam") == sp.srepr(LAM):
        DENS_DS = {frozenset(eval(k)): sp.sympify(v)
                   for k, v in _dc["sectors"].items()}
        stamp("dS graded density LOADED FROM CACHE")
    else:
        DENS_DS = None
else:
    DENS_DS = None
if DENS_DS is None:
    DENS_DS = build_density({i: E[i] for i in (1, 2, 3)}, a2, a2inv, LAM)
    json.dump({"lam": sp.srepr(LAM),
               "sectors": {repr(tuple(sorted(k))): sp.srepr(v)
                           for k, v in DENS_DS.items()}},
              open(DSCACHE, "w"))
    stamp("dS graded density built + cached (%.1fs)" % (time.time() - t_ds))
V3_DS = DENS_DS[frozenset((1, 2, 3))]
check(sp.expand(V3_DS.subs(H, 0) - V3_FLAT) == 0,
      "G7a: the dS cubic vertex at H = 0 equals the flat vertex EXACTLY "
      "(the D3 flat anchor, per order zero)", gate="G7")
ok7, res7 = is_total_derivative(DENS_DS[frozenset((1,))], 1)
check(ok7, "G7b (corrected): the dS LINEAR sector is EXACTLY a total "
      "derivative through O(H^2) WITH Lambda = 3H^2 (the background EOM in "
      "the chart, at action level -- the real content: the H-dependent "
      "p-independent pieces must cancel against Lambda)", gate="G7")
okc, _ = is_total_derivative(
    build_density({i: E[i] for i in (1, 2, 3)}, a2, a2inv,
                  sp.Integer(0))[frozenset((1,))], 1)
control(not okc, "G7 control: WITHOUT Lambda the dS linear sector is NOT a "
        "total derivative (the divergence-image solve fails -- the EOM gate "
        "has teeth)")
nds = len(sp.Add.make_args(sp.expand(V3_DS)))
note("dS graded cubic vertex: %d terms total through O(H^2)" % nds)
stamp("dS gates done")

# ================= S5: FREEZE + OUTPUT =================
print("\n=== S5: FREEZE ===")
art = {
    "convention": "cubic sector of (1/2kappa^2) sqrt(-g)(R - 2*3H^2), "
                  "g = a^2(u)(eta+h), chart a^2 = 1+2Hu+3H^2u^2, FULL "
                  "unfixed h (D2=2a); three plane waves, phases stripped "
                  "(sector j carries momentum p_j); u explicit; reported "
                  "per 1/(2 kappa^2)",
    "flat_vertex_srepr": sp.srepr(V3_FLAT),
    "ds_vertex_srepr": sp.srepr(sp.expand(V3_DS)),
    "flat_terms": n3,
    "ds_terms": nds,
}
blob = json.dumps(art, sort_keys=True)
VSHA = hashlib.sha256(blob.encode()).hexdigest()
art["vertex_sha256"] = VSHA
RESULT = {
    "stage": "K_R^(contract) TIER 1 -- dS TT-TT-TT vertex",
    "declarations": "D1=1a, D2=2a, D3=3a (countersigned d5dc33b)",
    "vertex_sha256": VSHA,
    "instrument_sha256": hashlib.sha256(
        open(os.path.abspath(__file__), "rb").read()).hexdigest(),
    "checks": CHECKS, "notes": NOTES, "failures": FAILS,
    "elapsed_s": round(time.time() - T0, 1),
    "hard_stop": "TIER 1 BOUNDARY: no Tier-2 mode integration, no K_R "
                 "assembly, no benchmark consequence, no bridge, no "
                 "Ward/Bardeen reinterpretation. Owner inspection required "
                 "before Tier 2.",
}
with open(os.path.join(HERE, "WALL_KR_TIER1_VERTEX_ARTIFACT.json"), "w") as f:
    json.dump(art, f, indent=1)
with open(os.path.join(HERE, "WALL_KR_TIER1_VERTEX_RESULT.json"), "w") as f:
    json.dump(RESULT, f, indent=1, default=str)
print("\n================ SUMMARY (TIER 1) ================")
print("  flat cubic vertex: %d terms; dS graded: %d terms; sha %s..."
      % (n3, nds, VSHA[:16]))
print("gates: %d/%d passed; failures: %d"
      % (sum(1 for c in CHECKS if c["pass"]), len(CHECKS), len(FAILS)))
for m in FAILS:
    print("  FAILURE: " + m)
print("elapsed: %.1fs" % (time.time() - T0))
sys.exit(0 if not FAILS else 1)
