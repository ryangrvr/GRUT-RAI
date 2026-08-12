#!/usr/bin/env python3
"""anomaly_c0_map: THE ANSWER CALC (R1) -- does the ACTION assign the interior family's scalar
modulus c0 a value? Object: x_anom := c0_anom / c0(x=1), the DC P0s-projected retarded kernel
induced by the anomaly-sourced conformalon, against the inherited bookkeeping coupling.

VERDICT: NO PIN -- result_face = k-DEPENDENT FORM FACTOR, with a DC ZERO that is scheme-immune IN
FLAT SPACE (the curved-background limit is HALTED, not claimed) and an amplitude AND sign that are
fully scheme-dependent. The anomaly sector realizes the family's dial as a SCALE, not a number:

    x_anom(k) = [1/(3 alpha)] * k^2 / (k^2 + M_sigma^2),   M_sigma^2 = M_P^2/(12 c_R^tot)

(the 1/(3 alpha) is EXPLICIT: the form factor equals x, and "saturates at exactly 1", ONLY at
alpha = 1/3 -- that is the T-BRANS-DICKE numerical collision, not a confirmation of the endpoint;
and the saturation regime sits at/above M_P where the derivative expansion has already broken down).
On the calc's OWN computed sign (c_R^anom < 0 structurally) M_sigma^2 is TACHYONIC and the form
factor does not rise to 1 at all -- it is negative for every sub-Planckian k.

MAGNITUDE, SCOPED (the two statements are NOT interchangeable):
  * the ANOMALY'S OWN contribution over the cosmological band is >=108 decades below every banked
    bound (computed: |x| ~ 1e-123 .. 1e-111, i.e. ~111 decades below EDGE at the worst point);
  * the SCHEME piece is FREE and UNBOUNDED -- with c_R free the form factor CAN reach the window
    (x = EDGE needs c_R ~ 7e110, ordinary f(R)-dark-energy territory). That freedom IS the no-pin
    finding; "R1 cannot reach the window" would contradict the scheme scan and is NOT claimed.

SCOPE SPLIT (KC-CONDITIONAL-LAUNDER, enforced in STEP 5):
  (A) LOCAL, <=4-derivative, FLAT SPACE -- UNCONDITIONAL and carrier-agnostic: the enumeration
      {int sqrt(g), int R, int R^2, int E_4, int C^2} is complete, and EVERY operator reaching P0s
      does so at k^4 (Riem^2 and Ric^2 reach it too -- "only int R^2 reaches P0s" would be false).
  (B) NONLOCAL closure -- CONDITIONAL on rung9a's IF (the conformal mode is the IR carrier). The
      concrete gap, int R box^{-1} R (~k^2 P0s: exactly the constant dial), is closed BY DIMENSIONS
      (its coefficient needs mass^2; a dimensionless anomaly coefficient cannot supply it).
  (C) CURVED BACKGROUND -- HALTED (frontier), no in-house number quoted.

THE COLLAPSE, in one line: the two anomaly vertices each carry box R ~ k^4, which EXACTLY cancels
the 1/k^4 Paneitz propagator, leaving a LOCAL R^2 -- a DIMENSION-4 operator. A dimension-4 operator
cannot shift a dimension-2 (Einstein-order k^2) Poisson coupling by a k-independent fraction. Three
independent legs: (a) DIMENSIONS (the anomaly action has no scale); (b) THE VERTEX (only box R is
linear in h about flat space, so the 1/k^4 propagator never appears in the h-kernel -- and this leg
also defeats the AMM anomalous-dimension escape: 1/k^{4-2eta} between two k^4 vertices gives
k^{4+2eta}); (c) OPERATOR COMPETITION (the EH conformal kinetic term dominates by M_P^2/(c_R k^2)).

CHANNEL FENCE (the induced modification is not a family member): quasi-static f(R) gives
Sigma = 1 IDENTICALLY and eta = (1+2kap)/(1+4kap), while the banked family postulates eta = 1/mu and
Sigma = 1 + x*alpha/2. So the anomaly-induced R^2 is a Sigma-NULL modification -- a DIFFERENT point
in (mu, eta, Sigma) space -- and the magnitude comparison against EDGE (a DESI Sigma_0 LENSING
bound) is CROSS-CHANNEL. Immaterial to the verdict (>=108 decades survives any O(1) mismatch), but
flagged, and guarded in code.

THE ALPHA-POWER AUDIT (the pre-registered confirmation-bias battery -- it did NOT spring):
alpha-power is ZERO, as an OUTPUT of the contraction, not an assumption: b' (the a-anomaly) feeds
P0s ONLY, b (the c-anomaly) feeds P2 ONLY (both machine-verified below), so the ratio alpha = a/c
is the coefficient of NOTHING in this channel. x = alpha^2 is STRUCTURALLY UNREACHABLE on a
tree-level single-exchange topology (it would need a numerator cubic in a; the topology is
homogeneous of total degree <= 1). Any R1 return of x = alpha^2 is an arithmetic error or a
laundered step.

PROVENANCE: built to the spec of the 2026-08-03 four-route R1 derivation reconnaissance
(effective-action / response-function / dimensional-scaling / scheme-structure) plus its
adjudicator, who independently re-derived every crux step in exact rationals at four independent
4-momenta with fit + held-out verification (zero residual). This file is the DEMONSTRATION of a
result already established there, with the guards armed so a future reader cannot re-derive a
spurious constant dial.

============================ PRE-REGISTERED KILL-CONDITIONS (X_FLOOR_MAP) ============================
 KC-NATURALNESS-BY-FIAT   the alpha-power must FALL OUT of the contraction; x=alpha^2 is under
                          maximum suspicion (it is the point that survived the most channels).
 KC-SCHEME-LAUNDERING     the local-term coefficient is a FREE PARAMETER, never "the natural scheme".
 KC-RUNG9B-BACK-DOOR      nothing may transport alpha into the TT amplitude c2. HARD-FAIL guard.
 KC-CONDITIONAL-LAUNDER   rung9a's IF (conformal mode = IR carrier) is an INPUT, never established.
 KC-FIT-NOT-PIN           a k-structured kernel projected onto a best-fit constant x is a FAKE
                          prediction; mismatch banks AS mismatch. HARD guard (STEP 10).
 KC-FRONTIER-TRESPASS     the contested dS/late-time sector is NEVER approximated in-house; HALT.
============================ FOUR NEW TRAPS THIS RECONNAISSANCE PRODUCED =============================
 T-BRANS-DICKE-FALSE-FRIEND   the R^2 completion's UV endpoint mu -> 4/3 is Brans-Dicke
                              1/(2 w_BD + 3) at w_BD = 0 -- NOT a/c. Two different 1/3's. Reading
                              the saturation at x=1 as support for the alpha-identification is
                              coincidence-mining.
 T-OMITTED-EH-CONFORMAL-KIN   dropping the EH k^2 term for sigma manufactures a spurious M_P^2/k^2
                              enhancement. sigma IS the metric trace at fixed G: the term is not
                              optional; dropping it is an inconsistent truncation.
 T-AMPLITUDE-AS-PREDICTION    the k^4 amplitude is degenerate with the free counterterm (the four
                              reconnaissance routes disagreed on it by 16x AND on its sign); it is
                              never quoted as physics.
 T-SCHEME-CARRIER-MISNAMED    the scheme carrier in the SPIN-0 channel is c_R2 (coefficient of
                              int sqrt(g) R^2), NOT int C^2 (which is pure P2 here) and NOT E_4
                              (identically zero here). A scan over the wrong parameter would return
                              a spurious "scheme-immune" verdict.
=====================================================================================================

Pure stdlib (fractions.Fraction for all load-bearing algebra; no floats in the exact sector).
Self-tested; every structural fact is a HARD assert, not a comment. Ledger delta 0: this file
touches no ledger field and fires no tier change.
"""
import contextlib
import io
import math
import os
import sys
from fractions import Fraction as F
from itertools import product

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from mu_linear import ALPHA                      # never hardcode 1/3
import mu_slip_interior as msi                   # EDGE / AUTO_EDGE_EST, never hardcoded
with contextlib.redirect_stdout(io.StringIO()):  # module prints at import (no __main__ guard)
    import conformalon_q2_band as cqb
import operator_basis as ob                      # the repo's own 3d projector algebra

IDX = list(product(range(4), repeat=2))
ETA = [[F(-1 if m == 0 else 0) if m == n and m == 0 else (F(1) if m == n else F(0))
        for n in range(4)] for m in range(4)]


# ------------------------------------------------------------------ STEP 1: exact 4d engine
def theta_omega(k, k2):
    """theta_mn = eta_mn - k_m k_n / k^2 (transverse), omega = kk/k^2 (longitudinal)."""
    th = [[ETA[m][n] - F(k[m] * k[n], 1) / k2 for n in range(4)] for m in range(4)]
    om = [[F(k[m] * k[n], 1) / k2 for n in range(4)] for m in range(4)]
    return th, om


def up(k):
    """raise an index with eta = diag(-1,1,1,1)."""
    return [(-k[0] if i == 0 else k[i]) for i in range(4)]


def raise2(M):
    """M^{mn} = eta^{ma} eta^{nb} M_ab  (eta diagonal, so just sign factors)."""
    return [[(F(-1) if m == 0 else F(1)) * (F(-1) if n == 0 else F(1)) * M[m][n]
             for n in range(4)] for m in range(4)]


def mixed(Mu, h):
    """(M . h)^m_n = M^{ma} h_an."""
    return [[sum(Mu[m][a] * h[a][n] for a in range(4)) for n in range(4)] for m in range(4)]


def forms(h, th, om):
    """All five quadratic forms at once, with indices raised CORRECTLY:
       returns (P2, P1, P0s, P0w, MIX, hh)."""
    hu = raise2(h)
    Th = mixed(raise2(th), h)          # theta^{ma} h_an
    Om = mixed(raise2(om), h)          # omega^{ma} h_an
    tsc = sum(Th[m][m] for m in range(4))          # theta^{mn} h_mn
    osc = sum(Om[m][m] for m in range(4))          # omega^{mn} h_mn
    P0s = F(1, 3) * tsc * tsc
    P0w = osc * osc
    MIX = tsc * osc
    P1 = F(2) * sum(Th[m][n] * Om[n][m] for m in range(4) for n in range(4))
    hh_ = sum(hu[m][n] * h[m][n] for m, n in IDX)
    P2 = hh_ - P1 - P0s - P0w
    return P2, P1, P0s, P0w, MIX, hh_


def hP0sh(h, th):
    hu = raise2(h)
    tsc = sum(th[m][n] * hu[m][n] for m, n in IDX)
    return F(1, 3) * tsc * tsc


def hP2h(h, th, om, k2):
    return forms(h, th, om)[0]


def hP1h(h, th, om, k2):
    return forms(h, th, om)[1]


def hP0wh(h, om):
    hu = raise2(h)
    osc = sum(om[m][n] * hu[m][n] for m, n in IDX)
    return osc * osc


def hMIXh(h, th, om):
    """the P0s<->P0w TRANSFER quadratic form; its VANISHING is the Ward statement."""
    return forms(h, th, om)[4]


def hh(h, k2):
    hu = raise2(h)
    return sum(hu[m][n] * h[m][n] for m, n in IDX)


def decompose(qform, k, k2, hs):
    """Fit a quadratic form Q(h) on {P2, P1, P0s, P0w, MIX} by exact linear solve over hs, then
    VERIFY on ALL samples with exact zero residual (fit + held-out; never fit-only)."""
    th, om = theta_omega(k, k2)
    rows, rhs = [], []
    for h in hs:
        P2, P1, P0s, P0w, MIX, _ = forms(h, th, om)
        rows.append([P2, P1, P0s, P0w, MIX])
        rhs.append(qform(h, k, k2))
    sol = _solve_exact(rows, rhs)
    if sol is None:
        return None
    for i in range(len(hs)):
        if sum(sol[j] * rows[i][j] for j in range(len(sol))) != rhs[i]:
            return None
    return sol


def _solve_exact(rows, rhs):
    """Exact Gauss-Jordan over Fraction on an overdetermined system; returns None if singular."""
    ncol = len(rows[0])
    A = [r[:] + [rhs[i]] for i, r in enumerate(rows)]
    piv_rows, used = [], [False] * len(A)
    for col in range(ncol):
        pr = next((i for i in range(len(A)) if not used[i] and A[i][col] != 0), None)
        if pr is None:
            return None
        used[pr] = True
        piv_rows.append(pr)
        pv = A[pr][col]
        A[pr] = [v / pv for v in A[pr]]
        for i in range(len(A)):
            if i != pr and A[i][col] != 0:
                f = A[i][col]
                A[i] = [A[i][j] - f * A[pr][j] for j in range(ncol + 1)]
    sol = [F(0)] * ncol
    for c, r in enumerate(piv_rows):
        sol[c] = A[r][ncol]
    return sol


# ------------------------------------------------------------------ linearized curvature (exact)
def lin_R(h, k, k2):
    """R^(1) = k^2 theta^{mn} h_mn  (d_m d_n -> -k_m k_n; verified against the standard form)."""
    ku = up(k)
    return k2 * sum((ETA[m][n] - F(ku[m] * ku[n], 1) / k2) * h[m][n] for m, n in IDX)


def lin_G_contract(h, k, k2):
    """-h^{mn} G^(1)_mn, the EH quadratic form (up to the overall Lagrangian normalization)."""
    ku = up(k)
    tr = sum((F(-1) if m == 0 else F(1)) * h[m][m] for m in range(4))
    # G^(1)_mn = 1/2[ -k^a k_m h_an - k^a k_n h_am + k^2 h_mn + k_m k_n h + eta_mn(k^a k^b h_ab - k^2 h) ]
    kkh = sum(ku[a] * ku[b] * h[a][b] for a, b in IDX)
    G = [[F(0)] * 4 for _ in range(4)]
    for m, n in IDX:
        t1 = -sum(ku[a] * F(k[m], 1) * h[a][n] for a in range(4))
        t2 = -sum(ku[a] * F(k[n], 1) * h[a][m] for a in range(4))
        t3 = k2 * h[m][n]
        t4 = F(k[m] * k[n], 1) * tr
        t5 = ETA[m][n] * (kkh - k2 * tr)
        G[m][n] = F(1, 2) * (t1 + t2 + t3 + t4 + t5)
    s = F(0)
    for m, n in IDX:
        sm = F(-1) if m == 0 else F(1)
        sn = F(-1) if n == 0 else F(1)
        s += sm * sn * h[m][n] * G[m][n]
    return -s


def lin_riemann(h, k):
    """R^(1)_{mnrs} = (1/2)(d_n d_r h_ms + d_m d_s h_nr - d_n d_s h_mr - d_m d_r h_ns),
    with d_a d_b -> -k_a k_b. Built explicitly -- B1: this must be COMPUTED, not asserted."""
    K = [F(k[i]) for i in range(4)]
    R = [[[[F(0)] * 4 for _ in range(4)] for _ in range(4)] for _ in range(4)]
    for m, n, r, s in product(range(4), repeat=4):
        R[m][n][r][s] = F(1, 2) * (-K[n] * K[r] * h[m][s] - K[m] * K[s] * h[n][r]
                                   + K[n] * K[s] * h[m][r] + K[m] * K[r] * h[n][s])
    return R


def lin_ricci(Riem):
    """R^(1)_mn = eta^{rs} R^(1)_{r m s n}."""
    ric = [[F(0)] * 4 for _ in range(4)]
    for m, n in IDX:
        s = F(0)
        for r in range(4):
            sr = F(-1) if r == 0 else F(1)
            s += sr * Riem[r][m][r][n]
        ric[m][n] = s
    return ric


def _sq_full(T4):
    """R^{mnrs} R_{mnrs} with eta = diag(-1,1,1,1)."""
    s = F(0)
    for m, n, r, q in product(range(4), repeat=4):
        sg = (F(-1) if m == 0 else F(1)) * (F(-1) if n == 0 else F(1)) * \
             (F(-1) if r == 0 else F(1)) * (F(-1) if q == 0 else F(1))
        s += sg * T4[m][n][r][q] * T4[m][n][r][q]
    return s


def _sq_two(T2):
    s = F(0)
    for m, n in IDX:
        sg = (F(-1) if m == 0 else F(1)) * (F(-1) if n == 0 else F(1))
        s += sg * T2[m][n] * T2[m][n]
    return s


def qf_Riem2(h, k, k2):
    return _sq_full(lin_riemann(h, k))


def qf_Ric2(h, k, k2):
    return _sq_two(lin_ricci(lin_riemann(h, k)))


def qf_E4(h, k, k2):
    """Gauss-Bonnet: Riem^2 - 4 Ric^2 + R^2. TOPOLOGICAL in d=4 -- the vanishing is a genuine
    CANCELLATION between the three pieces, not O(h) counting (T5)."""
    Riem = lin_riemann(h, k)
    r = lin_R(h, k, k2)
    return _sq_full(Riem) - F(4) * _sq_two(lin_ricci(Riem)) + r * r


def qf_C2(h, k, k2):
    """Weyl-squared: Riem^2 - 2 Ric^2 + (1/3) R^2."""
    Riem = lin_riemann(h, k)
    r = lin_R(h, k, k2)
    return _sq_full(Riem) - F(2) * _sq_two(lin_ricci(Riem)) + F(1, 3) * r * r


def qf_trace_sq(h, k, k2):
    """(tr h)^2 -- the NAIVE pure-trace vertex squared (the Ward-violating pitfall, T7)."""
    tr = sum((F(-1) if m == 0 else F(1)) * h[m][m] for m in range(4))
    return tr * tr


def qf_R2(h, k, k2):
    """(R^(1))^2 -- the quadratic form of int sqrt(g) R^2 about flat space."""
    r = lin_R(h, k, k2)
    return r * r


# ------------------------------------------------------------------ B3: the ANSWER, computed
def M_sigma_sq(cR_tot, MP2=1.0):
    """M_sigma^2 = M_P^2 / (12 c_R^tot). NOTE the sign: c_R^tot < 0 gives a TACHYONIC M_sigma^2
    (T4) -- the branch the calc's OWN computed c_R^anom sits on."""
    if cR_tot == 0:
        return None
    return MP2 / (12.0 * cR_tot)


def x_anom(k_over_MP, cR_tot, alpha=ALPHA):
    """THE ANSWER, as a function (B3 -- it was previously only a print string).
    x_anom(k) = [1/(3 alpha)] * k^2 / (k^2 + M_sigma^2).
    The 1/(3 alpha) is EXPLICIT per T2: the family's mu = 1 + x*alpha and quasi-static f(R) gives
    mu - 1 = (1/3) k^2/(k^2 + M_sigma^2); x = (mu-1)/alpha. It equals the bare form factor (and so
    'saturates at exactly 1') ONLY at alpha = 1/3 -- that is the T-BRANS-DICKE numerical collision,
    NOT a confirmation of the endpoint."""
    Ms2 = M_sigma_sq(cR_tot)
    if Ms2 is None:
        return None
    k2 = k_over_MP ** 2
    den = k2 + Ms2
    if den == 0:
        return float("inf")
    return (1.0 / (3.0 * alpha)) * k2 / den


def mu_eta_Sigma_fR(kap):
    """Quasi-static f(R) observables (B7): mu = (1+4kap)/(1+3kap), eta = (1+2kap)/(1+4kap),
    Sigma = mu(1+eta)/2 = 1 IDENTICALLY. The anomaly-induced R^2 is a Sigma-NULL modification --
    it is NOT a member of the banked interior family (which postulates eta = 1/mu, Sigma = 1+x*alpha/2)."""
    mu = (1.0 + 4.0 * kap) / (1.0 + 3.0 * kap)
    eta = (1.0 + 2.0 * kap) / (1.0 + 4.0 * kap)
    return mu, eta, mu * (1.0 + eta) / 2.0


# ------------------------------------------------------------------ sample h's
def _samples(seed=12345, n=22):
    """Deterministic pseudo-random symmetric rational h's (no float, no random module)."""
    hs, s = [], seed
    for _ in range(n):
        h = [[F(0)] * 4 for _ in range(4)]
        for m in range(4):
            for n in range(m, 4):
                s = (1103515245 * s + 12345) % 2147483648
                v = F((s % 21) - 10, 1 + (s // 21) % 7)
                h[m][n] = v
                h[n][m] = v
        hs.append(h)
    return hs


KS = [(1, 2, 3, 0), (2, 1, 0, 4), (0, 3, 0, 0), (1, 1, 2, 1)]   # four independent 4-momenta


def _k2(k):
    return F(-k[0] * k[0] + k[1] * k[1] + k[2] * k[2] + k[3] * k[3], 1)


# ------------------------------------------------------------------ main
def main():
    print("=" * 98)
    print("R1 -- THE ANSWER CALC: does the anomaly action assign the interior modulus c0 a value?")
    print("=" * 98)
    hs = _samples(n=16)
    KSOK = [k for k in KS if _k2(k) != 0]

    # ---------------------------------------------------------------- STEP 2 (all rows COMPUTED)
    print("\nSTEP 2 -- THE STRUCTURE TABLE, EVERY ROW COMPUTED (exact rationals, four independent")
    print("4-momenta, fit + held-out verification with zero residual). This is the spine:")
    ROWS = (("-h.G^(1)      [EH]", lin_G_contract, 1),
            ("(R^(1))^2     [int R^2]", qf_R2, 2),
            ("Riem^2", qf_Riem2, 2),
            ("Ric^2", qf_Ric2, 2),
            ("int E_4       [a-anomaly]", qf_E4, 2),
            ("int C^2       [c-anomaly]", qf_C2, 2),
            ("(tr h)^2      [naive vertex]", qf_trace_sq, 0))
    tab = {}
    for name, qf, div in ROWS:
        rows = []
        for k in KSOK:
            k2 = _k2(k)
            sol = decompose(qf, k, k2, hs)
            assert sol is not None, f"decomposition FAILED for {name} at k={k}"
            rows.append(tuple(c / (k2 ** div) for c in sol))
        assert all(r == rows[0] for r in rows), f"{name}: coefficients are k-DEPENDENT: {rows}"
        tab[name] = rows[0]
        P2, P1, P0s, P0w, MIX = rows[0]
        u = {0: "1  ", 1: "k^2", 2: "k^4"}[div]
        print(f"   {name:28s} = {u} * [ {str(P2):>4} P2 + {P1} P1 + {str(P0s):>3} P0s"
              f" + {P0w} P0w + {MIX} MIX ]")
    eh, r2 = tab["-h.G^(1)      [EH]"], tab["(R^(1))^2     [int R^2]"]
    e4, c2 = tab["int E_4       [a-anomaly]"], tab["int C^2       [c-anomaly]"]
    print(f"   => THE GR LOCK: P0s/P2 = {eh[2] / eh[0]} exactly -- independently reproduces the")
    print("      register's banked linearized-EH decomposition (1/2)k^2[P^(2) - 2P^(0,s)].")
    print(f"   => int R^2 is PURE SPIN-0 (P2 = {r2[0]});  int C^2 has NO SPIN-0 CARRIER (P0s = {c2[2]});")
    print(f"      int E_4 is IDENTICALLY ZERO in every structure {tuple(str(x) for x in e4)}.")
    print("      E_4's vanishing is a genuine CANCELLATION (T5), not O(h) counting -- verified from")
    print(f"      the pieces: P2: {tab['Riem^2'][0]} - 4*{tab['Ric^2'][0]} + {r2[0]} = {e4[0]};"
          f"  P0s: {tab['Riem^2'][2]} - 4*{tab['Ric^2'][2]} + {r2[2]} = {e4[2]}.")
    print("   => WARD: P1 = P0w = MIX = 0 in every DIFF-INVARIANT form above (the vanishing of the")
    print("      P0s<->P0w TRANSFER term IS the Ward statement) -- and note the NAIVE vertex row")
    print(f"      carries P0w = {tab['(tr h)^2      [naive vertex]'][3]} and MIX ="
          f" {tab['(tr h)^2      [naive vertex]'][4]}: it is WARD-VIOLATING and is NOT the induced kernel.")

    # ---------------------------------------------------------------- STEP 3 (vertex guard)
    print("\nSTEP 3 -- THE sigma-h VERTEX + THE RUNG9B BACK-DOOR GUARD (hard fail):")
    hsig = [[F(2) * ETA[m][n] for n in range(4)] for m in range(4)]
    for k in KSOK:
        k2 = _k2(k)
        th, om = theta_omega(k, k2)
        P2, P1, P0s, P0w, MIX, _ = forms(hsig, th, om)
        assert P2 == 0 and P1 == 0, f"RUNG9B BACK-DOOR: sigma has spin-2/vector content at k={k}"
        assert P0s == 12 and P0w == 4, f"vertex normalization wrong at k={k}"
    print("   h_mn = 2 sigma eta_mn: P2 = 0 and P1 = 0 IDENTICALLY (exact, all four k);")
    print("   P0s = 12 sigma^2, P0w = 4 sigma^2 => sigma is PURE spin-0: the alpha->TT back-door is")
    print("   KINEMATICALLY SHUT AT THE VERTEX. (Version-I freeze untouched.)")
    print("   FENCE (T19): this guard alone is WEAK -- it is blind to an index-raising bug (the")
    print("   sigma direction is degenerate). Only the STEP 2 decompose over GENERIC h catches that;")
    print("   that is the load-bearing check.")

    # ---------------------------------------------------------------- STEP 4 (collapse, computed inputs)
    print("\nSTEP 4 -- THE COLLAPSE THEOREM (its two premises are now STEP-2 rows, not prose):")
    print("   S_anom = N int[ sigma Delta_4 sigma + lam (E_4 - (2/3) box R) sigma ],")
    print("     N = Q^2/(16 pi^2), lam = 1/2  (sourced: calc/delta4_stability.py docstring)")
    print(f"   PREMISE 1 [COMPUTED above]: int E_4 flat quadratic form = 0 in every structure.")
    print(f"   PREMISE 2 [COMPUTED above]: int C^2 P0s coefficient = {c2[2]} (no spin-0 carrier).")
    print("   => the ONLY O(h) vertex is J^(1) = -(2 lam/3) box R^(1) ~ k^4 * (spin-0);")
    print("   => Delta_4^{-1} -> box^{-2} ~ 1/k^4 is EXACTLY CANCELLED by the two vertices;")
    print("   => S_eff^(2) = -(N lam^2/9) int (R^(1))^2 : LOCAL, a pure R^2, NO IR enhancement.")
    N_pref = cqb.Q2_SM / (16.0 * math.pi ** 2)
    LAM = 0.5
    cR_anom = -(N_pref * LAM ** 2) / 9.0
    print(f"   Q^2_SM = {cqb.Q2_SM:.4f} (imported) -> N = {N_pref:.6f} -> c_R^anom = {cR_anom:.4e}")
    print("   [CONVENTION WARNING: conformalon_q2_band.py's inline note says '1/(4pi)^2 absorbed'")
    print("    while RESULTS_conformalon.md / delta4_stability.py carry an explicit 16 pi^2 -- a")
    print("    factor ~158. Immaterial here (>=108-decade margin) but must be settled before ANY")
    print("    amplitude-level use of Q^2.]")

    # ---------------------------------------------------------------- STEP 5: the scope split (B4)
    print("\nSTEP 5 -- THE SCOPE SPLIT (B4; KC-CONDITIONAL-LAUNDER, now ENFORCED):")
    print("   (A) LOCAL, <=4-derivative, FLAT SPACE -- UNCONDITIONAL. The enumeration")
    print("       {int sqrt(g), int R, int R^2, int E_4, int C^2} is COMPLETE for local <=4-derivative")
    print("       diff invariants and CARRIER-AGNOSTIC: it does not use rung9a's IF at all.")
    print(f"       Every operator reaching P0s does so at k^4 (T6: Riem^2 P0s = {tab['Riem^2'][2]} and")
    print(f"       Ric^2 P0s = {tab['Ric^2'][2]} also reach it -- 'only int R^2 reaches P0s' would be FALSE;")
    print("       the true statement is the k^4 one). int R IS the EH k^2 term; int sqrt(g) is")
    print("       tadpole-locked. NO local <=4-derivative operator supplies a k-INDEPENDENT dial.")
    print("   (B) NONLOCAL closure -- CONDITIONAL on rung9a's IF (the conformal mode is the IR")
    print("       carrier). R1's object IS the anomaly-sourced Riegert conformalon, so adopting the")
    print("       Riegert form inherits that conditional. THE CONCRETE GAP: int R box^{-1} R has")
    print("       quadratic form ~ k^2 * P0s -- degenerate in k-scaling with EH, i.e. exactly the")
    print("       constant dial this calc says cannot exist. IT IS CLOSED BY DIMENSIONS, not by the")
    print("       Riegert choice: that operator's coefficient carries DIMENSION mass^2, which a")
    print("       DIMENSIONLESS anomaly coefficient cannot supply. (This simultaneously STRENGTHENS")
    print("       the R1/rung3 boundary below: mass^2 is what massive matter -- rung3's bath -- has.)")

    # ---------------------------------------------------------------- STEP 6/7: the ANSWER, computed
    print("\nSTEP 6/7 -- THE KERNEL AND THE ANSWER (B3: now COMPUTED, not printed):")
    print("   K^{0s}(k) = (M_P^2/4) k^2 + 3 c_R^tot k^4,   c_R^tot = c_R^scheme + c_R^anom")
    print("   GUARD (T-OMITTED-EH-CONFORMAL-KIN, re-homed per T16): the k^2 term is RETAINED. The")
    print("   rebuttal to the AMM IR-fixed-point escape is LEG (b), not 'inconsistent truncation':")
    print("   even granting an anomalous dimension eta on the sigma propagator (1/k^{4-2eta}), the")
    print("   two box-R vertices give k^4 * k^{-(4-2eta)} * k^4 = k^{4+2eta} -- nowhere near k^2.")
    print(f"   x_anom(k) = [1/(3 alpha)] * k^2/(k^2 + M_sigma^2),  M_sigma^2 = M_P^2/(12 c_R^tot)")
    print(f"   The 1/(3 alpha) is EXPLICIT (T2): with alpha = {ALPHA:.4f} the prefactor is"
          f" {1/(3*ALPHA):.4f}; the")
    print("   'saturates at exactly x = 1' statement holds ONLY at alpha = 1/3 -- that is the")
    print("   T-BRANS-DICKE numerical collision, NOT a confirmation of the endpoint.")
    Ms2_anom = M_sigma_sq(cR_anom)
    print(f"   FOR THE CALC'S OWN COMPUTED SIGN (T4): c_R^anom = {cR_anom:.4e} < 0 is STRUCTURALLY")
    print(f"   negative (N > 0), so M_sigma^2 = {Ms2_anom:.3f} M_P^2 is TACHYONIC: on this branch the")
    print("   form factor does NOT rise to 1 -- it is NEGATIVE for all sub-Planckian k and")
    print("   approaches 1 from ABOVE past a pole. The 'rises and saturates' picture is the")
    print("   c_R > 0 branch only, and c_R^tot's sign is FREE (STEP 8).")
    for kt in (1e-3, 1.0):
        print(f"      x_anom(k = {kt:g} M_P, c_R = c_R^anom) = {x_anom(kt, cR_anom):+.4e}")
    print("   TWO INDEPENDENT ROUTES, genuinely cross-checked in _selftest (B3: the old check was")
    print("   an algebraic tautology): (a) the KERNEL RATIO 12 c_R k^2/M_P^2 and (b) the f(R)")
    print("   SCALARON MATCHING mu = (1+4kap)/(1+3kap) with kap = (k/a)^2 f_RR/f_R, f_RR = 4c_R/M_P^2.")
    print("   They agree to machine precision at four (k, c_R) points spanning both signs.")

    # ---------------------------------------------------------------- STEP 8: the scheme scan (B5)
    print("\nSTEP 8 -- SCHEME SCAN, c_R^scheme FREE and NEVER SET (B5: sign/magnitude fixed, and the")
    print("flip is now STRADDLED):")
    print("   c_R^scheme        c_R^tot         sign     x_anom(k->0)")
    SCAN = [-1e12, -1e-3, -1e-4, 0.0, 1e-4, 9.7285e-4, 1e-3, 1e12]
    dc_all_zero = True
    for cs in SCAN:
        tot = cs + cR_anom
        xdc = x_anom(0.0, tot) if tot != 0 else None
        if xdc is not None and xdc != 0.0:
            dc_all_zero = False
        sg = "0" if tot == 0 else ("+" if tot > 0 else "-")
        print(f"   {cs:+.4e}    {tot:+.4e}     {sg}       "
              f"{'undefined' if xdc is None else f'{abs(xdc):.1f} (exact)'}")
    assert dc_all_zero, "DC zero FAILED somewhere in the scheme scan"
    print(f"   THE FLIP IS STRADDLED: sign(c_R^tot) changes between c_R^scheme = +1e-4 and")
    print(f"   +9.7285e-4 (= -c_R^anom). ==> EXPORT: SIGN_ORIENTATION_NOT_SUPPLIED_BY_R1.")
    print("   (i)  the k^4 AMPLITUDE is scheme-dependent with NO protected value: the protected")
    print("        b'-piece and the FREE int R^2 counterterm land on the IDENTICAL structure.")
    print("   (ii) the SIGN is free -- see the straddle above.")
    print("   (iii) x_anom(k->0) = 0 for EVERY c_R^scheme in the scan: THE DC ZERO IS SCHEME-IMMUNE")
    print("        (COMPUTED across the scan, not asserted at a point).")
    print("   FENCE (T1): this is a FLAT-SPACE statement. The curved-background DC limit is HALTED")
    print("   (STEP 13), NOT claimed zero.")

    # ---------------------------------------------------------------- STEP 9: alpha-power (computed)
    print("\nSTEP 9 -- THE ALPHA-POWER AUDIT (both halves now rest on COMPUTED rows):")
    print(f"   b' (a-anomaly) enters ONLY through the box-R vertex -> R^2 -> P0s (P2 = {r2[0]});")
    print(f"   b  (c-anomaly) enters through int C^2 -> P2 ONLY (P0s = {c2[2]}).")
    print("   SCOPE (T13): this is the statement about the LOCAL C^2 counterterm (and the nonlocal")
    print("   C ln(box) C, which shares its P2 structure). The WZ vertex b*sigma*C^2 is O(sigma h^2)")
    print("   -- CUBIC, contributing nothing to the tree-level h two-point kernel.")
    print("   => alpha = a/c is THE COEFFICIENT OF NOTHING in this channel: net dynamical")
    print("      alpha-power = 0, an OUTPUT of the contraction. (The denominator's alpha^1 is")
    print("      purely DEFINITIONAL -- it is how the family normalizes x.)")
    print(f"   x_anom(DC) = 0 != alpha ({ALPHA:.4f}), != alpha^2 ({ALPHA**2:.4f}), != alpha^3.")
    print("   alpha^2 is STRUCTURALLY UNREACHABLE on a tree-level single-exchange topology.")
    print("   DIRECTIONAL GUARD: any R1 return of x = alpha^2 is an arithmetic error or a laundered")
    print("   step. TRAPS (recorded, not evidence): T-BRANS-DICKE-FALSE-FRIEND (4/3 = BD 1/(2w+3) at")
    print("   w=0, NOT a/c); and the x=1 saturation is the alpha=1/3 collision (T2), not a")
    print("   confirmation -- and it lives at/above M_P where the derivative expansion has already")
    print(f"   broken down (T3: |c_R| in [1e-3, 1] gives M_sigma in "
          f"[{math.sqrt(abs(M_sigma_sq(1.0))):.3f}, {math.sqrt(abs(M_sigma_sq(1e-3))):.3f}] M_P).")

    # ---------------------------------------------------------------- STEP 10: guards (T12, B7)
    print("\nSTEP 10 -- THE TWO PROJECTION GUARDS (both ARMED, both exercised on physical bands):")
    _fit_not_pin(cR_anom)
    _channel_guard()

    # ---------------------------------------------------------------- STEP 11: FDT (fenced)
    print("\nSTEP 11 -- ABSORPTIVE / FDT LEG (estimate-grade, FENCED):")
    print("   Im K^{0s} = 0: the induced kernel is a REAL POLYNOMIAL in k^2 -- no branch cut, so the")
    print("   KMS relation is VACUOUS (0 = 0), not merely degenerate as at rung9b. CONSEQUENCE: the")
    print("   anomaly action supplies NO dissipative spin-0 channel at quadratic order.")
    print("   FENCE: leading-order FLAT-SPACE statement about the ANOMALY action -- NOT a rung3 Pi_0")
    print("   result. COVERAGE FENCE (T20): all four test momenta are SPACELIKE and omega is never")
    print("   varied; the omega->0/k->0 commutation is an INFERENCE from polynomial analyticity, not")
    print("   a scanned result.")

    # ---------------------------------------------------------------- STEP 12: magnitude (B6)
    print("\nSTEP 12 -- MAGNITUDE, RE-SCOPED (B6 -- the two sections are now consistent):")
    print("   THE ANOMALY'S OWN CONTRIBUTION (c_R = c_R^anom, computed above):")
    KTAB = (("H0", 5.9e-61), ("100 H0", 5.9e-59), ("0.001 Mpc^-1", 1.3e-58),
            ("0.01 Mpc^-1", 1.3e-57), ("0.1 Mpc^-1", 1.3e-56), ("1 Mpc^-1", 1.3e-55))
    worst = 0.0
    for label, kk in KTAB:
        xv = x_anom(kk, cR_anom)
        worst = max(worst, abs(xv))
        print(f"      k/a = {label:14s}  x_anom = {xv:+.3e}")
    dec = math.log10(msi.EDGE / worst)
    print(f"   => the LARGEST magnitude over the cosmological band is {worst:.2e},")
    print(f"      i.e. {dec:.1f} DECADES below the loosest banked window edge EDGE ="
          f" {msi.EDGE:.3f} (imported).")
    print("   THE SCHEME PIECE IS FREE AND UNBOUNDED -- so the honest statement is NOT 'R1 cannot")
    print("   reach the window' (that would contradict STEP 8). It is:")
    print("      *** the ANOMALY'S OWN contribution is >=%d decades below every banked bound;" % int(dec))
    print("          the scheme piece is free, which IS the no-pin finding. ***")
    print("   For completeness, the c_R a FREE counterterm would need to reach each target at")
    print("   k/a = 0.1 Mpc^-1 (this is ordinary f(R)-dark-energy territory, which DESI constrains):")
    for tgt, nm in ((msi.EDGE, "EDGE"), (msi.AUTO_EDGE_EST, "TT-auto gate"), (ALPHA ** 2, "alpha^2")):
        k0 = 1.3e-56
        need = _cR_for(tgt, k0)
        print(f"      x = {tgt:.3f} ({nm:12s}) needs c_R ~ {need:.2e}")

    # ---------------------------------------------------------------- STEP 13: halts (T11)
    print("\nSTEP 13 -- HALT MARKERS (printed as NON-results; the halt is NOT crossed, T11):")
    print("   CURVED BACKGROUND: on FRW/dS, E_4^(1) and (C^2)^(1) are NONZERO, so the protected")
    print("   sector no longer decouples and Delta_4^{-1} carries the CONTESTED late-time Green's")
    print("   function. HALT -- KC-FRONTIER-TRESPASS. NO in-house power count is quoted here: two")
    print("   independent in-house counts of the FRW correction DISAGREE about its k-structure, so")
    print("   the honest output is the halt, not a number.")
    print("   The sharpened dispatch question attaches to SPECIALIST_BRIEF_2 (no new brief): does")
    print("   the curved-background nonlocality regenerate a k^2-or-softer P0s structure at a")
    print("   NON-GR ratio to P2 that survives omega->0?")
    print("   DISPATCH OPTIONALITY is routed to X_FLOOR_MAP's INDEPENDENT pre-registration ('D3")
    print("   requires no dispatch to complete') -- NOT to any in-house estimate of the halted sector.")

    # ---------------------------------------------------------------- STEP 14/15: verdict + register
    print("\nSTEP 14 -- VERDICT BLOCK (the file does NOT self-declare bankability, T17):")
    print("   result_face = K-DEPENDENT FORM FACTOR")
    print("     co-result: the DC ZERO is SCHEME-IMMUNE (in flat space; curved is HALTED)")
    print("     co-result: the AMPLITUDE and the SIGN are fully SCHEME-DEPENDENT")
    print("   GRADE SPLIT (the actual deliverable):")
    print("     (A) local <=4-derivative, flat space -> DERIVED, UNCONDITIONAL, carrier-agnostic")
    print("     (B) nonlocal closure               -> CONDITIONAL on rung9a's IF, with the")
    print("         int R box^{-1} R gap closed BY DIMENSIONS (argument-grade)")
    print("     (C) curved background              -> HALTED (frontier), not claimed")
    print("   X_FLOOR_MAP's PARTIAL-PIN RIDER, quoted in full (T8 -- the RESULTS doc must match):")
    print("     \"R1's partial-pin outcome (x_anom = 0 scheme-immune) pins only that the anomaly")
    print("      does not source the interior -- the fiat becomes better-motivated, stays a fiat;")
    print("      no tier change.\"")
    print("   PREDICATE MATCH IS PARTIAL (T9): the rider was pre-registered for 'x_anom = 0")
    print("   scheme-immune'; the actual return is a FORM FACTOR whose DC limit is scheme-immunely")
    print("   zero while amplitude and sign are scheme-dependent. Both route to the same weaker")
    print("   consequence (no tier change), but the match is partial and is stated as such.")
    print("   Ledger delta 0; no tier field touched. EXPLICIT NON-CLAIMS: does NOT establish")
    print("   Pi_0 = 0; does NOT fire D1; no claim that 'x = 0 is forced' or that p_tt is vindicated.")

    print("\nSTEP 15 -- REGISTER-FACING OUTPUT (two PROPOSED edits, both flagged, neither applied):")
    print("   PROPOSED EDIT 1 (the heavier one, B8) -- to rung9b_bridge (settled-negative, FROZEN):")
    print("     its PRIMARY obstruction is 'projector orthogonality: trace = spin-0, TT = spin-2'.")
    print("     The computed a/c SECTOR-SPLIT REFINES it rather than refuting it: the anomaly has")
    print(f"     BOTH carriers -- b' -> P0s (k^4) and b -> P2 (k^4, P0s = {c2[2]}) -- so the coarse")
    print("     'the anomaly is spin-0, P^TT is spin-2, done' is too blunt; what actually blocks the")
    print("     bridge is that the RATIO a/c is the coefficient of NEITHER. This is a STRENGTHENING")
    print("     of rung9b, and it is now COMPUTED. Routed as an explicit proposed edit -- overseer's.")
    print("   PROPOSED EDIT 2 -- to eft_operator_basis finding (iv): its second clause 'the anomaly")
    print("     leaves TT unaffected' is FALSE at TWO-POINT level (int C^2 is pure P2). The")
    print("     ONE-POINT clause (<T^mu_mu> is spin-0) STANDS. Correct reason it transports nothing")
    print("     into c2 (T14 -- the old reason was a non sequitur): what reaches P2 is b ALONE,")
    print("     never the ratio a/c, so the rung9b bridge object (alpha as the DC normalization of")
    print("     K^R) is untouched; and the C^2 structure is k^4, not the k^2 of the response kernel.")
    print("   THE R1/rung3 BOUNDARY (T17, weakened to what is argued): NO non-analytic DC spin-0")
    print("   structure arises in this local/flat sector; a scheme-immune normalization would need")
    print("   one, and the dimensional argument (STEP 5B) says it needs a mass^2 -- which massive")
    print("   matter supplies and a dimensionless anomaly coefficient cannot. That points at rung3's")
    print("   Pi_0. ARGUED-GRADE, not proven; the calc does not adjudicate its own bankability.")
    print("   NOTE: the anomaly action DOES carry non-analytic structure (C^2 ln(box) C^2) -- in the")
    print("   P2 channel, which is why it cannot help here.")

    ok = _selftest(hs, KSOK, cR_anom, tab)
    print(f"\n  SELFTEST: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


def _cR_for(x_target, k_over_MP, alpha=ALPHA):
    """Solve x_anom(k, c_R) = x_target for c_R (B6: the reach of the FREE counterterm)."""
    f = 3.0 * alpha * x_target
    if f >= 1.0:
        return float("inf")
    Ms2 = k_over_MP ** 2 * (1.0 - f) / f
    return 1.0 / (12.0 * Ms2)


def _fit_not_pin(cR_tot, band=(5.9e-61, 1.3e-55)):
    """KC-FIT-NOT-PIN, ARMED (T12: an assert, exercised on the PHYSICAL cosmological band)."""
    lo, hi = band
    xlo, xhi = abs(x_anom(lo, cR_tot)), abs(x_anom(hi, cR_tot))
    ratio = xhi / xlo
    assert ratio > 10.0, "FIT-NOT-PIN guard vacuous: x is nearly constant over the physical band"
    print(f"   [FIT-NOT-PIN] best-fit constant x over the PHYSICAL band k/a in"
          f" [{lo:.1e}, {hi:.1e}] M_P: REFUSED.")
    print(f"      |x| runs {xlo:.2e} -> {xhi:.2e}, a factor {ratio:.1e} across the band; the")
    print("      k-exponent is +2 relative to the family's k-INDEPENDENT dial. A constant-x")
    print("      modification cannot approximate this. THE MISMATCH BANKS AS MISMATCH.")


def _channel_guard():
    """B7 (NEW GUARD -- KC-FIT-NOT-PIN's observable-channel analogue): the induced R^2 is not a
    member of the banked interior family at all. Assert the Sigma-null mismatch rather than
    silently projecting mu-channel onto a Sigma-channel bound."""
    print("   [CHANNEL GUARD, new] the family postulates eta = 1/mu and Sigma = 1 + x*alpha/2;")
    print("   quasi-static f(R) gives eta = (1+2kap)/(1+4kap) and Sigma = 1 IDENTICALLY:")
    for kap in (0.1, 1.0, 1e6):
        mu, eta, Sig = mu_eta_Sigma_fR(kap)
        assert abs(Sig - 1.0) < 1e-12, "f(R) Sigma is not identically 1 -- channel guard broken"
        print(f"      kap = {kap:>8g}:  f(R) (mu, eta, Sigma) = ({mu:.5f}, {eta:.5f}, {Sig:.5f})"
              f"   vs family at same mu: eta = {1/mu:.5f}, Sigma = {1 + (mu-1)/2:.5f}")
    print("   => THE ANOMALY-INDUCED R^2 IS A Sigma-NULL MODIFICATION: it is NOT a point of the")
    print("   banked interior family, it is a DIFFERENT point in (mu, eta, Sigma) space. Since the")
    print("   binding window edge EDGE is a DESI Sigma_0 LENSING bound, that bound has ZERO grip on")
    print("   this modification -- which does NOT rescue a pin (the mu-channel magnitude is >=108")
    print("   decades down regardless), but the comparison is cross-channel and is flagged as such.")


def _selftest(hs, KSOK, cR_anom, tab):
    """Mutation-resistant (B3): every load-bearing NUMBER is checked, not just the exact sector."""
    ok = True
    def chk(c, m):
        nonlocal ok
        if not c:
            print(f"   [FAIL] {m}")
            ok = False
    # --- the exact structure table, re-derived independently of main()'s cache
    for k in KSOK:
        k2 = _k2(k)
        eh = [c / k2 for c in decompose(lin_G_contract, k, k2, hs)]
        r2 = [c / k2 ** 2 for c in decompose(qf_R2, k, k2, hs)]
        c2 = [c / k2 ** 2 for c in decompose(qf_C2, k, k2, hs)]
        e4 = [c / k2 ** 2 for c in decompose(qf_E4, k, k2, hs)]
        rm = [c / k2 ** 2 for c in decompose(qf_Riem2, k, k2, hs)]
        rc = [c / k2 ** 2 for c in decompose(qf_Ric2, k, k2, hs)]
        chk(eh[2] / eh[0] == F(-2), f"GR LOCK broken at k={k}")
        chk(eh[1] == 0 and eh[3] == 0 and eh[4] == 0, f"EH Ward violated at k={k}")
        chk(r2 == [F(0), F(0), F(3), F(0), F(0)], f"int R^2 != 3 k^4 P0s at k={k}: {r2}")
        chk(c2 == [F(1, 2), F(0), F(0), F(0), F(0)], f"int C^2 != (1/2)k^4 P2 at k={k}: {c2}")
        chk(all(c == 0 for c in e4), f"int E_4 not identically zero at k={k}: {e4}")
        chk(rm[2] == 1 and rc[2] == 1, f"Riem^2/Ric^2 P0s coefficients at k={k}")
        # E_4 must also vanish POINTWISE, not merely in decomposition
        chk(all(qf_E4(h, k, k2) == 0 for h in hs), f"int E_4 nonzero pointwise at k={k}")
        # the sigma vertex
        th, om = theta_omega(k, k2)
        hsig = [[F(2) * ETA[m][n] for n in range(4)] for m in range(4)]
        P2, P1, P0s, _, _, _ = forms(hsig, th, om)
        chk(P2 == 0 and P1 == 0 and P0s == 12, f"sigma vertex guard at k={k}")
    # --- THE ANSWER's numbers (this is what the mutation test defeated before)
    chk(abs(cR_anom - (-(cqb.Q2_SM / (16 * math.pi ** 2)) * 0.25 / 9)) < 1e-15,
        "c_R^anom is not the computed value")
    chk(cR_anom < 0, "c_R^anom must be structurally negative (N > 0)")
    # DC zero across the WHOLE scan, at genuinely varied c_R, computed not hardcoded
    for cs in (-1e12, -1e-3, -1e-4, 1e-4, 9.7285e-4, 1e-3, 1e12):
        tot = cs + cR_anom
        if tot == 0:
            continue
        chk(x_anom(0.0, tot) == 0.0, f"DC zero failed at c_R^scheme={cs}")
    # the form factor must genuinely be k^2-structured (defeats a constant-x mutant)
    x1, x2 = abs(x_anom(1e-58, cR_anom)), abs(x_anom(1e-57, cR_anom))
    chk(90.0 < x2 / x1 < 110.0, f"x is not k^2-scaling in the cosmological regime: ratio {x2/x1}")
    # magnitude sanity: the cosmological band must be >= 50 decades below EDGE (defeats a
    # magnitude-table mutant); the true value is ~108-122 decades
    worst = max(abs(x_anom(kk, cR_anom)) for kk in (5.9e-61, 1.3e-55))
    chk(math.log10(msi.EDGE / worst) > 50.0, f"magnitude implausible: worst = {worst}")
    # x_anom must NOT land on the pre-registered suspicious points anywhere in the band
    for kk in (5.9e-61, 1.3e-58, 1.3e-55):
        for bad in (ALPHA, ALPHA ** 2):
            chk(abs(abs(x_anom(kk, cR_anom)) - bad) > 1e-3,
                f"x_anom landed on a directional-guard point at k={kk}")
    # f(R) quasi-static form: mu - 1 = kap/(1 + 3 kap)  (equivalently (1/3)k^2/(k^2 + M_sigma^2),
    # since k^2/M_sigma^2 = 3 kap) -- and Sigma = 1 identically (the B7 channel fact)
    for kap in (0.1, 1.0, 100.0):
        mu, _, Sig = mu_eta_Sigma_fR(kap)
        chk(abs(Sig - 1.0) < 1e-12, "f(R) Sigma != 1")
        chk(abs((mu - 1.0) - kap / (1.0 + 3.0 * kap)) < 1e-12, f"f(R) mu form at kap={kap}")
    # THE REAL CROSS-CHECK (replaces the old tautology, B3(c)): the KERNEL-RATIO route and the
    # f(R)-MATCHING route are computed INDEPENDENTLY and must agree.
    for kk, cR in ((1e-3, 1e-2), (1e-2, 5.0), (0.3, -1e-3), (1e-58, cR_anom)):
        kap = 4.0 * cR * kk ** 2                       # kap = (k/a)^2 f_RR/f_R, f_RR = 4 c_R/M_P^2
        if abs(1.0 + 3.0 * kap) < 1e-30:
            continue
        x_fR = ((mu_eta_Sigma_fR(kap)[0]) - 1.0) / ALPHA
        x_ker = x_anom(kk, cR)
        chk(abs(x_fR - x_ker) < 1e-9 * max(1.0, abs(x_ker)),
            f"kernel-ratio and f(R) routes DISAGREE at k={kk}, c_R={cR}: {x_ker} vs {x_fR}")
    # imports really imported
    chk(abs(ALPHA - 1.0 / 3.0) < 1e-15, "ALPHA import")
    chk(msi.EDGE > 0.5 and cqb.Q2_SM > 1.0, "imports")
    return ok


if __name__ == "__main__":
    raise SystemExit(main())
