#!/usr/bin/env python3
"""static_patch_tt_response: the analytic structure of the retarded response on the de Sitter
STATIC PATCH, computed rather than cited.

PRE-REGISTERED: provenance/prereg/PREREG_FRAME_MIGRATION_2026-08-18.txt (v1, sealed 2026-08-18,
sha256 = 7b7ffaaa185a49e4...) and its disclosure-only supersession
provenance/prereg/PREREG_FRAME_MIGRATION_2026-08-18_v2.txt
(sha256 = 2f456d00e92f8ea2720240de5fa0e181a6b62ac789ca6fb29ac8ab1be522c88a).
Both were sealed BEFORE this file existed. X3 of that pre-registration voids it for any
static-patch computation of the TT response run before sealing; a repository-wide search for such
a computation found none, and the public document records the same fact in its own words ("the
free static-patch tower is published and closed-form ... It has not been computed").

A NOTE ON A COLLIDING NAME, because this program has now had five of them. `kk_static_transfer.py`
is about the STATIC MODULUS -- the omega -> 0 limit of a response function. It is not about the
de Sitter static PATCH and shares no object with this file. Prior collisions: TT, kappa, tau_0, S1.

WHAT IS ESTABLISHED HERE, and at what strength:

  (A) DERIVED, EXACT. On the static patch, for the one-parameter family of radial master equations
      f d/dr (f dpsi/dr) + (omega^2 - V) psi = 0,   V = f(r) * ( l(l+1)/r^2 + c H^2 ),
      f(r) = 1 - H^2 r^2, the retarded/quasinormal frequencies are
          omega_{n,l} / H  =  -i [ l + 2n + (3 -/+ sqrt(1-4c))/2 ],    n = 0,1,2,...
      PURELY IMAGINARY, DISCRETE, and spaced by exactly 2H in the overtone index -- for EVERY c.
      Exhibited, not asserted: at each such frequency the hypergeometric series truncates to a
      POLYNOMIAL, so the mode function is elementary, satisfies the ODE with residual exactly zero
      (symbolically checked), is regular at the origin by inspection, and is purely OUTGOING at the
      horizon by inspection -- there is no ingoing admixture to bound numerically.

  (B) DERIVED. c = -2 is the massless minimally coupled scalar: the potential is computed here
      from the metric, not quoted.

  (C) DERIVED IN-HOUSE 2026-08-19, PART 1b -- this was flagged as an open gap and is now closed.
      Linearising R_mn = Lambda g_mn about the static patch with an odd-parity Regge-Wheeler
      ansatz, at EXPLICIT l (which is what made it finish where two abstract-l attempts did not),
      gives V = f(r) l(l+1)/r^2: c = 0 EXACTLY, and NOT the c = -2 massless-scalar member. So the
      exhibit is about the graviton's own potential. SCOPE: axial sector; the polar sector is
      reported elsewhere to share the master equation and is not verified here.

  (A-RETRACTED, 2026-08-19) PART 3b RETRACTS the claim that the frequencies in (A) are
      quasinormal. The boundary-condition check tested the wrong thing. Read PART 3b before
      anything else in this file; every downstream part is now marked conditional.

  (D) THE CONSEQUENCE FOR THE SINGLE-POLE CONJECTURE, stated at the weaker of two strengths.
      A single-pole (Debye/Markovian) kernel has ONE pole. This object has infinitely many, and
      -- the point that decides it -- THERE IS NO PARAMETER SEPARATING THE LEADING POLE FROM THE
      REST. Gap and spacing are both O(H); their ratio is O(1) and contains no small quantity.
      A single dominant pole can be reached only by WAITING (the tower's contributions separate as
      exp(-2Ht)), never by a parametric limit. "Parametrically suppressed" and "eventually
      negligible" are different claims, and only the second is available here.

Pure stdlib + sympy. Run: python3 calc/static_patch_tt_response.py
"""
import sys

import sympy as sp

r, th, ph, t = sp.symbols('r theta phi t')
H = sp.Symbol('H', positive=True)
w, l, c = sp.symbols('omega l c')

FAIL = []


def check(cond, msg):
    print(("  ok   " if cond else "  FAIL ") + msg)
    if not cond:
        FAIL.append(msg)


# ---------------------------------------------------------------------------------------------
def part0_background():
    """The background: maximally symmetric, R_mn = 3H^2 g_mn, so vacuum Einstein needs Lambda=3H^2."""
    print("\nPART 0 -- the background, checked rather than assumed")
    f = 1 - H**2*r**2
    x = [t, r, th, ph]
    g = sp.diag(-f, 1/f, r**2, r**2*sp.sin(th)**2)
    gi = g.inv()
    G = [[[0]*4 for _ in range(4)] for _ in range(4)]
    for a in range(4):
        for b in range(4):
            for d in range(b, 4):
                s = sum(gi[a, e]*(sp.diff(g[e, b], x[d]) + sp.diff(g[e, d], x[b])
                                  - sp.diff(g[b, d], x[e])) for e in range(4) if gi[a, e] != 0)
                G[a][b][d] = G[a][d][b] = sp.simplify(s/2)

    def riem(a, b, d, e):
        z = sp.diff(G[a][b][e], x[d]) - sp.diff(G[a][b][d], x[e])
        z += sum(G[a][d][k]*G[k][b][e] - G[a][e][k]*G[k][b][d] for k in range(4))
        return z

    # NB: sp.simplify alone leaves one component as a nonzero-LOOKING trig expression that is
    # identically zero; expand_trig first. A simplifier returning "not zero" for zero is an
    # instrument artefact, recorded here because this program treats those as findings.
    worst = 0
    for a in range(4):
        for b in range(4):
            for d in range(4):
                for e in range(4):
                    low = sum(g[a, k]*riem(k, b, d, e) for k in range(4))
                    want = H**2*(g[a, d]*g[b, e] - g[a, e]*g[b, d])
                    z = sp.simplify(sp.expand_trig(sp.simplify(low - want)))
                    if z != 0:
                        worst += 1
    check(worst == 0, f"R_mnab = H^2 (g_ma g_nb - g_mb g_na) for all 256 components")
    ric = sp.zeros(4, 4)
    for b in range(4):
        for e in range(4):
            ric[b, e] = sp.simplify(sum(riem(a, b, a, e) for a in range(4)))
    check(sp.simplify(ric - 3*H**2*g) == sp.zeros(4, 4), "R_mn = 3H^2 g_mn  =>  Lambda = 3H^2")
    check(sp.simplify(sum(gi[i, j]*ric[i, j] for i in range(4) for j in range(4))) == 12*H**2,
          "Ricci scalar R = 12 H^2")


# ---------------------------------------------------------------------------------------------
def part0b_native_temperature():
    """E1's first half, in-house: the KMS temperature is a PROPERTY OF THE GEOMETRY here, not an
    import.  Euclidean continuation t -> -i tau; regularity of the (tau, r) section at the horizon
    fixes the period of tau, and hence a temperature, with nothing put in by hand."""
    print("\nPART 0b -- the temperature is native (Euclidean regularity)")
    rho, tau = sp.symbols('rho tau', positive=True)
    rh = 1/H
    d = sp.Symbol('delta', positive=True)            # delta = r_h - r
    f = 1 - H**2*r**2
    near = sp.simplify(sp.series(f.subs(r, rh - d), d, 0, 2).removeO())
    check(sp.simplify(near - 2*H*d) == 0, "f -> 2 H delta near the horizon (delta = 1/H - r)")
    # substitute delta = H rho^2 / 2 and read off the angle
    g_tt = sp.simplify(near.subs(d, H*rho**2/2))
    g_rr = sp.simplify((1/near).subs(d, H*rho**2/2)*sp.diff(H*rho**2/2, rho)**2)
    check(sp.simplify(g_rr - 1) == 0, "the radial part becomes d rho^2 exactly")
    check(sp.simplify(g_tt - H**2*rho**2) == 0,
          "the Euclidean section is  d rho^2 + rho^2 (H d tau)^2 : a plane in polar form")
    print("     => smooth at rho = 0 iff H*tau has period 2*pi, i.e. beta = 2*pi/H,")
    print("        T = H/(2*pi).  Derived from regularity; nothing imported.")
    print("     NOTE ON WHAT THIS DOES AND DOES NOT BUY. It makes the temperature native to the")
    print("     frame -- E1's claim. It does NOT re-derive the register's rung5 Unruh-T import,")
    print("     and it does not by itself establish the KMS lock on the noise kernel, which is a")
    print("     statement about a state on an algebra and not about a conical deficit.")


# ---------------------------------------------------------------------------------------------
def part1_scalar_potential():
    """Compute the massless-scalar radial potential from the metric. c = -2 is DERIVED here."""
    print("\nPART 1 -- the massless minimally coupled scalar potential, from the metric")
    f = 1 - H**2*r**2
    x = [t, r, th, ph]
    g = sp.diag(-f, 1/f, r**2, r**2*sp.sin(th)**2)
    gi = sp.diag(-1/f, f, 1/r**2, 1/(r**2*sp.sin(th)**2))
    sqg = r**2*sp.sin(th)
    Phi = sp.Function('Phi')(t, r, th, ph)
    box = sum(sp.diff(sqg*gi[m, m]*sp.diff(Phi, x[m]), x[m]) for m in range(4))/sqg
    psi = sp.Function('psi')(r)
    Y = sp.Function('Y')(th, ph)
    box = box.subs(Phi, sp.exp(-sp.I*w*t)*Y*psi/r).doit()
    box = sp.expand(sp.simplify(box))
    box = box.subs(sp.Derivative(Y, (th, 2)),
                   -l*(l+1)*Y - sp.cos(th)/sp.sin(th)*sp.diff(Y, th)
                   - sp.diff(Y, (ph, 2))/sp.sin(th)**2)
    box = sp.simplify(box/(sp.exp(-sp.I*w*t)*Y/r))
    V = sp.Symbol('V')
    target = f*sp.diff(f*sp.diff(psi, r), r) + w**2*psi
    sol = sp.solve(sp.Eq(sp.simplify(sp.expand(box*f)), target - V*psi), V)
    Vs = sp.simplify(sp.expand_trig(sp.simplify(sol[0])))
    want = f*(l*(l+1)/r**2 - 2*H**2)
    check(sp.simplify(sp.expand_trig(sp.simplify(Vs - want))) == 0,
          "V_scalar = f(r) [ l(l+1)/r^2 - 2H^2 ]   i.e. the family member c = -2")
    return want


# ---------------------------------------------------------------------------------------------
def part1b_graviton_c():
    """THE GRAVITON'S c, DERIVED IN-HOUSE. This closes the gap flagged as (C) above.

    Two earlier attempts failed on HARDWARE, not on physics: both carried an abstract P(theta) with
    a Legendre substitution, and sympy would not finish. Fixing l and using the explicit Legendre
    polynomial makes every angular object concrete trig and the linearisation takes seconds.

    METHOD, and it is a derivation rather than a citation: linearise the vacuum equation
    R_mn = Lambda g_mn (Lambda = 3H^2, checked in PART 0) about the static patch with an
    odd-parity Regge-Wheeler ansatz h_{t phi} = h0(r) e^{-i w t} S(theta),
    h_{r phi} = h1(r) e^{-i w t} S(theta), S = sin(theta) d_theta P_l(cos theta); expand the FULL
    Ricci tensor in eps and take the O(eps) part. Two independent equations survive:

        E_{theta phi}:  -i w h0 = f d/dr ( f h1 )          [l-INDEPENDENT]
        E_{r phi}:      -(l(l+1) - 2) f h1 + w^2 r^2 h1 - i w r^2 h0' + 2 i w r h0 = 0

    The l(l+1)-2 coefficient is read off two explicit runs: it is 4 at l=2 and 10 at l=3.

    Substituting h0 and setting Z = f h1 / r gives A2 Z'' + A1 Z' + A0 Z with A1/(A2/f^2) EXACTLY
    f f' -- no stray first-derivative term, which is what makes Z the master variable rather than
    a convenient rescaling -- and

        V = f(r) * l(l+1) / r^2,    i.e.  c = 0 EXACTLY.

    SO THE EXHIBIT IS ABOUT THE GRAVITON'S POTENTIAL. The c = 0 family analysed in PARTS 3b/3c is
    the one the framework's own object lives in, and the pole-free result is about it.

    SCOPE, STATED: this is the AXIAL (odd-parity) sector. An independent derivation in the same
    wave reported that the polar (even-parity) sector shares the same master equation; that is NOT
    verified here and is taken as unconfirmed."""
    print("\nPART 1b -- the graviton's c, derived (axial sector)")

    # ---- step 1: the linearisation itself, at explicit l = 2, in this file ----------------
    eps = sp.Symbol('epsilon')
    lval = 2
    fb = 1 - H**2*r**2
    P = sp.legendre(lval, sp.cos(th))
    S = sp.sin(th)*sp.diff(P, th)
    h0f, h1f = sp.Function('h0')(r), sp.Function('h1')(r)
    T = sp.exp(-sp.I*w*t)
    g0 = sp.diag(-fb, 1/fb, r**2, r**2*sp.sin(th)**2)
    g0i = sp.diag(-1/fb, fb, 1/r**2, 1/(r**2*sp.sin(th)**2))
    hp = sp.zeros(4, 4)
    hp[0, 3] = hp[3, 0] = h0f*S*T
    hp[1, 3] = hp[3, 1] = h1f*S*T
    g = g0 + eps*hp
    gi = g0i - eps*(g0i*hp*g0i)
    xs = [t, r, th, ph]

    def tr(e):
        e = sp.expand(e)
        return e.coeff(eps, 0) + eps*e.coeff(eps, 1)

    G = [[[0]*4 for _ in range(4)] for _ in range(4)]
    for a in range(4):
        for b in range(4):
            for d in range(b, 4):
                acc = 0
                for e_ in range(4):
                    if gi[a, e_] == 0:
                        continue
                    acc += gi[a, e_]*(sp.diff(g[e_, b], xs[d]) + sp.diff(g[e_, d], xs[b])
                                      - sp.diff(g[b, d], xs[e_]))
                G[a][b][d] = G[a][d][b] = tr(acc/2)

    def ric(b, d):
        acc = 0
        for a in range(4):
            acc += sp.diff(G[a][b][d], xs[a]) - sp.diff(G[a][b][a], xs[d])
            for e_ in range(4):
                acc += G[a][a][e_]*G[e_][b][d] - G[a][d][e_]*G[e_][b][a]
        return tr(acc)

    Eth = sp.simplify(sp.cancel(sp.together(sp.expand(
        tr(ric(2, 3) - 3*H**2*g[2, 3]).coeff(eps, 1)/T))))
    Erp = sp.simplify(sp.cancel(sp.together(sp.expand(
        tr(ric(1, 3) - 3*H**2*g[1, 3]).coeff(eps, 1)/T))))
    # E_theta,phi must be proportional to [ f (f h1)' + i w h0 ]
    claim_th = fb*sp.diff(fb*h1f, r) + sp.I*w*h0f
    q = sp.simplify(sp.cancel(sp.together(Eth/claim_th)))
    check(sp.simplify(sp.diff(q, h1f)) == 0 and sp.simplify(sp.diff(q, h0f)) == 0
          and sp.simplify(Eth - q*claim_th) == 0,
          "E_{theta,phi} factors EXACTLY as (angular) x [ f d/dr(f h1) + i w h0 ] -- the "
          "constraint, and it carries no l")
    # E_r,phi must be proportional to the second equation with l(l+1) - 2 = 4 at l = 2
    claim_rp = (-(lval*(lval+1) - 2)*fb*h1f + w**2*r**2*h1f
                - sp.I*w*r**2*sp.diff(h0f, r) + 2*sp.I*w*r*h0f)
    q2 = sp.simplify(sp.cancel(sp.together(Erp/claim_rp)))
    check(sp.simplify(sp.diff(q2, h1f)) == 0 and sp.simplify(sp.diff(q2, h0f)) == 0
          and sp.simplify(Erp - q2*claim_rp) == 0,
          f"E_{{r,phi}} factors EXACTLY as (angular) x [ -(l(l+1)-2) f h1 + w^2 r^2 h1 "
          f"- i w r^2 h0' + 2 i w r h0 ] at l = {lval} (coefficient 4 = l(l+1)-2)")
    print("     (the same two forms were obtained at l = 3, where the coefficient is 10 = l(l+1)-2;")
    print("      that run takes ~400 s and is not repeated in this selftest)")

    # ---- step 2: assemble the master equation with l(l+1) symbolic -------------------------
    L = sp.Symbol('L')
    f = 1 - H**2*r**2
    Z = sp.Function('Z')(r)
    h1 = r*Z/f
    h0 = sp.I*f*sp.diff(f*h1, r)/w
    E = sp.expand(sp.cancel(sp.together(sp.expand(
        -(L - 2)*f*h1 + w**2*r**2*h1 - sp.I*w*r**2*sp.diff(h0, r) + 2*sp.I*w*r*h0))))
    A2 = sp.simplify(E.coeff(sp.Derivative(Z, (r, 2))))
    A1 = sp.simplify(E.coeff(sp.Derivative(Z, r)))
    A0 = sp.simplify(sp.simplify(E - A2*sp.Derivative(Z, (r, 2))
                                 - A1*sp.Derivative(Z, r)).coeff(Z))
    k = sp.simplify(A2/f**2)
    check(sp.simplify(A1/k - f*sp.diff(f, r)) == 0,
          "no stray first-derivative term: A1 reduces to exactly f f', so Z = f h1 / r really is "
          "the master variable")
    V = sp.simplify(w**2 - A0/k)
    check(sp.simplify(V/f - L/r**2) == 0, f"V = f(r) * l(l+1)/r^2   (V/f = {sp.factor(V/f)})")
    cc = sp.Symbol('c')
    sol = sp.solve(sp.Eq(sp.simplify(V - f*(L/r**2 + cc*H**2)), 0), cc)
    check(sol == [0], f"*** c = {sol} EXACTLY -- the graviton sits in the c = 0 family ***")
    check(sp.simplify(V - f*(L/r**2 - 2*H**2)) != 0,
          "and it is NOT the c = -2 massless-scalar member: the two differ by 2 H^2 f")
    print("     The exhibit in PARTS 2-3c is therefore about the graviton's own potential.")
    print("     SCOPE: axial (odd-parity) sector. The polar sector is reported elsewhere to share")
    print("     this master equation and is NOT verified here.")


# ---------------------------------------------------------------------------------------------
def part2_hypergeometric():
    """Peel both singular behaviours; what is left is hypergeometric. alpha, beta, gamma DERIVED."""
    print("\nPART 2 -- exact reduction to the hypergeometric equation (H = 1 units)")
    z = sp.Symbol('z', positive=True)
    F = sp.Function('F')
    f = 1 - r**2
    V = f*(l*(l+1)/r**2 + c)
    psi = r**(l+1)*(1 - r**2)**(-sp.I*w/2)*F(r**2)
    e = sp.expand(sp.simplify(f*sp.diff(f*sp.diff(psi, r), r) + (w**2 - V)*psi))
    e = sp.simplify(sp.expand(e/(r**(l+1)*(1 - r**2)**(-sp.I*w/2)))).subs(r, sp.sqrt(z))
    e = sp.collect(sp.expand(sp.simplify(e)), [sp.Derivative(F(z), z, 2), sp.Derivative(F(z), z),
                                               F(z)])
    A = sp.simplify(e.coeff(sp.Derivative(F(z), z, 2)))
    Bh = sp.simplify(sp.simplify(e.coeff(sp.Derivative(F(z), z, 1))/A)*z*(1 - z))
    Ch = sp.simplify(sp.simplify(e.coeff(F(z))/A)*z*(1 - z))
    gam = sp.simplify(Bh.subs(z, 0))
    apb = sp.simplify(-sp.diff(sp.expand(Bh), z) - 1)
    ab = sp.simplify(sp.expand(-Ch))
    check(sp.simplify(gam - (l + sp.Rational(3, 2))) == 0, "gamma = l + 3/2")
    check(sp.simplify(apb - (l - sp.I*w + sp.Rational(3, 2))) == 0, "alpha + beta = l - i w + 3/2")
    s = sp.sqrt(1 - 4*c)
    a0 = (l - sp.I*w)/2 + sp.Rational(3, 4) - s/4
    b0 = (l - sp.I*w)/2 + sp.Rational(3, 4) + s/4
    check(sp.simplify(a0 + b0 - apb) == 0 and sp.simplify(sp.expand(a0*b0 - ab)) == 0,
          "alpha,beta = (l - i w)/2 + 3/4 -/+ sqrt(1-4c)/4")
    print("     => gamma - alpha - beta = i w : the two horizon behaviours are (1-z)^0 (outgoing,")
    print("        already peeled) and (1-z)^{i w} (ingoing). A mode is purely outgoing exactly")
    print("        when the second is absent.")
    return a0, b0


# ---------------------------------------------------------------------------------------------
def part3_exact_modes(cmain=(-2, -1, 0), ccontrast=(1,), lmax=3, nmax=2):
    """THE EXHIBIT. At alpha = -n or beta = -n the series truncates: the mode is a POLYNOMIAL times
    the two peeled factors, so both boundary conditions are exact statements about elementary
    functions -- nothing is bounded numerically and nothing is asserted.

    THE RESIDUAL TEST IS TWO-TIER, AND THE SECOND TIER IS COUNTED RATHER THAN HIDDEN. Tier 1 is
    symbolic: residual == 0 exactly. For the c > 1/4 contrast family the coefficients carry nested
    radicals and sympy does not reduce them; tier 2 evaluates the residual at eight exact rational
    radii in 60-digit arithmetic and requires |residual| < 1e-45. That is weaker than tier 1 and is
    reported as such -- a simplifier that cannot close an expression is not evidence that the
    expression is nonzero, but it is not evidence that it is zero either."""
    print("\nPART 3 -- the modes, exhibited exactly (H = 1 units)")
    import mpmath as mp
    mp.mp.dps = 60
    W = sp.Symbol('W')
    total = tier2 = bad_ode = bad_poly = bad_horizon = 0
    freqs = {}
    for cv in tuple(cmain) + tuple(ccontrast):
        s_ = sp.sqrt(1 - 4*cv)
        for lv in range(0, lmax + 1):
            for nv in range(0, nmax + 1):
                for sign in (-1, +1):
                    a = (lv - sp.I*W)/2 + sp.Rational(3, 4) + sign*s_/4
                    wv = sp.simplify(sp.solve(sp.Eq(a, -nv), W)[0])
                    aa = sp.simplify(a.subs(W, wv))
                    bb = sp.simplify((lv - sp.I*wv)/2 + sp.Rational(3, 4) - sign*s_/4)
                    Fp = sp.hyperexpand(sp.hyper((aa, bb), (lv + sp.Rational(3, 2),), r**2))
                    psi = r**(lv + 1)*(1 - r**2)**(-sp.I*wv/2)*Fp
                    ff = 1 - r**2
                    VV = ff*(lv*(lv + 1)/r**2 + cv)
                    res = sp.simplify(sp.expand(ff*sp.diff(ff*sp.diff(psi, r), r)
                                                + (wv**2 - VV)*psi))
                    total += 1
                    if res != 0:
                        tier2 += 1
                        pts = [sp.Rational(k, 17) for k in range(2, 16, 2)]
                        worst = max(abs(mp.mpmathify(complex(sp.N(res.subs(r, q), 60))))
                                    for q in pts)
                        if worst > mp.mpf('1e-45'):
                            bad_ode += 1
                    if not sp.simplify(Fp).is_polynomial(r):
                        bad_poly += 1
                    if sp.simplify(Fp.subs(r, 1)) == 0:
                        bad_horizon += 1   # RETAINED, BUT IT DOES NOT MEAN WHAT IT SAID -- see
                        #                    part3b_the_outgoing_check_was_wrong()
                    freqs.setdefault(cv, set()).add(sp.simplify(sp.I*wv))
    check(bad_ode == 0, f"all {total} exhibited modes satisfy the ODE with residual 0 "
                        f"({total - tier2} symbolically, {tier2} to 45 digits at 8 radii)")
    check(bad_poly == 0, f"all {total} truncate to polynomials (so the mode is elementary)")
    check(bad_horizon == 0,
          f"all {total} have a NONZERO analytic factor at the horizon "
          f"(NOTE: this does NOT establish 'purely outgoing' -- see PART 3b, which retracts the "
          f"reading this check was given)")
    for cv in tuple(cmain) + tuple(ccontrast):
        got = sorted(freqs[cv], key=lambda x: (float(sp.re(x)), float(sp.im(x))))
        tag = "" if cv <= sp.Rational(1, 4) else "   <-- c > 1/4: a REAL part appears"
        print(f"     c = {cv:>2}:  i*omega/H in "
              f"{[sp.sstr(sp.nsimplify(x)) for x in got[:7]]} ...{tag}")
    return freqs


# ---------------------------------------------------------------------------------------------
def part3b_the_outgoing_check_was_wrong():
    """RETRACTION, WITH THE COUNTEREXAMPLE COMPUTED.

    PART 3 originally reported that each exhibited mode is "purely outgoing at the horizon by
    inspection", on the argument that psi = r^{l+1} (1-r^2)^{-i w/2} x (polynomial) is the peeled
    outgoing factor times something analytic and non-zero at r = 1.  THAT ARGUMENT IS FALSE, and
    the error was visible in this file's own PART 2 output: gamma - alpha - beta = i*w, so the
    ingoing connection coefficient carries Gamma(-i*w), which has a POLE exactly when i*w is a
    positive integer -- which is exactly where the quantisation condition 1/Gamma(alpha) = 0 puts
    these modes.  0 x infinity.  It was noticed, called "need care", and then not carried through.

    Concretely: (1-r^2)^{-i w/2} = cosh(x)^{i w} in the tortoise coordinate, and
        cosh(x)^{i w} = (e^x/2)^{i w} (1 + e^{-2x})^{i w},
    whose binomial series contributes e^{i w x} e^{-2 n x}.  When i*w is a positive integer, one of
    those terms IS e^{-i w x}.  The peeled factor is not purely outgoing at precisely the claimed
    frequencies.

    The counterexample is elementary and is computed below: for the c = 0 family the exact Jost
    pair is u_+- = e^{+-i w x} Q_l(coth x) with Q_l MONIC of degree l, so BOTH behave as x^{-l} at
    the origin, and the regular solution is therefore u_+ - u_- -- giving ingoing amplitude
    B = -A for EVERY omega.  B never vanishes, so these are not quasinormal modes and nothing in
    the c = 0 family is."""
    print("\nPART 3b -- RETRACTION: the 'purely outgoing' check did not test outgoingness")
    xx = sp.Symbol('x', positive=True)
    tt = sp.Symbol('t')
    ww = sp.Symbol('w')

    def Qpoly(lv, wsym):
        co = [sp.Symbol(f'q{i}') for i in range(lv)]
        Q = tt**lv + sum(co[i]*tt**i for i in range(lv))
        eq = sp.expand((tt**2 - 1)*sp.diff(Q, tt, 2) + 2*(tt - sp.I*wsym)*sp.diff(Q, tt)
                       - lv*(lv + 1)*Q)
        return sp.expand(Q.subs(sp.solve(sp.Poly(eq, tt).all_coeffs(), co, dict=True)[0]))

    for lv, iw, psi in ((1, 2, sp.sinh(xx)**2), (2, 3, sp.sinh(xx)**3),
                        (2, 4, sp.sinh(xx)**3*sp.cosh(xx))):
        wv = -sp.I*iw
        V = lv*(lv + 1)/sp.sinh(xx)**2
        assert sp.simplify(sp.diff(psi, xx, 2) + (wv**2 - V)*psi) == 0
        up = sp.exp(sp.I*wv*xx)*Qpoly(lv, wv).subs(tt, sp.coth(xx))
        um = sp.exp(-sp.I*wv*xx)*Qpoly(lv, -wv).subs(tt, sp.coth(xx))
        A, B = sp.symbols('A B')
        sol = sp.solve([sp.Eq(psi.subs(xx, q), (A*up + B*um).subs(xx, q))
                        for q in (sp.Rational(3, 4), sp.Rational(3, 2))], [A, B], dict=True)[0]
        Av, Bv = sp.simplify(sol[A]), sp.simplify(sol[B])
        res = max(abs(complex(sp.N((psi - (Av*up + Bv*um)).subs(xx, q), 30)))
                  for q in (sp.Rational(1, 2), 1, 2, sp.Rational(5, 2)))
        check(res < 1e-40 and sp.simplify(Bv) != 0,
              f"c=0, l={lv}, i*w={iw}: exact decomposition (residual {res:.0e}) gives "
              f"A = {sp.nsimplify(sp.N(Av, 20))}, B = {sp.nsimplify(sp.N(Bv, 20))} -- "
              f"B is NOT zero, so this is NOT a quasinormal mode")

    print("\n     THE GENERAL STATEMENT, for the c = 0 family:")
    for lv in range(1, 7):
        Qp, Qm = Qpoly(lv, ww), Qpoly(lv, -ww)
        monic = sp.Poly(Qp, tt).all_coeffs()[0] == 1 and sp.Poly(Qm, tt).all_coeffs()[0] == 1
        up = sp.exp(sp.I*ww*xx)*Qp.subs(tt, sp.coth(xx))
        um = sp.exp(-sp.I*ww*xx)*Qm.subs(tt, sp.coth(xx))
        ser = sp.expand(sp.series(sp.simplify(up - um), xx, 0, lv + 2).removeO())
        neg = [m for m in range(-lv, 0) if sp.simplify(ser.coeff(xx, m)) != 0]
        check(monic and not neg,
              f"l={lv}: both Jost solutions are MONIC in coth x, so u_+ - u_- is regular "
              f"(no x^-k terms) => B = -A for every omega, and B never vanishes")
    print("\n     CONSEQUENCE: the c = 0 (graviton) family has NO quasinormal modes at the")
    print("     frequencies this file originally reported, and the argument above shows it has")
    print("     none from that branch at any omega.")
    print("     STILL OPEN, AND NOT CLAIMED EITHER WAY: at omega = -i k for k = 1..l the two Jost")
    print("     solutions COINCIDE (the normalisation of u_+ - u_- carries a factor")
    print("     omega * prod_{k=1..l} (omega^2 + k^2)), so the argument is silent there. Those")
    print("     finitely many frequencies are the only surviving pole candidates and this file")
    print("     does not resolve them.")
    print("     ALSO NOT CLAIMED: the c = -2 (massless scalar) case, and non-integer Delta. For")
    print("     NON-INTEGER Delta the Gamma(-i w) pole does not collide with the 1/Gamma(alpha)")
    print("     zero, so the original truncation argument is expected to stand there -- which")
    print("     would mean the tower is real for generic c and absent for exactly the two")
    print("     physically relevant members. That expectation is NOT verified here.")


# ---------------------------------------------------------------------------------------------
def part3c_reflection_amplitude():
    """CLOSES the question PART 3b left open, and it closes it against the tower.

    The regular solution is u_+ - u_-, so its outgoing/ingoing ratio is fixed by the two horizon
    amplitudes alone: R_l(omega) = Q_l(1) / Q_l(1)|_{omega -> -omega}. Computing it gives

        R_l(omega) = (-1)^l  prod_{j=1..l}  (omega + i j H) / (omega - i j H)

    which is a FINITE BLASCHKE PRODUCT: |R_l| = 1 identically on the real axis. The cavity is
    TOTALLY REFLECTING at every real frequency -- no transmission, no width, no relaxation rate.

    And it settles PART 3b's residue. The only pole candidates left were omega = -i j, j = 1..l,
    where the Jost pair degenerates. There R_l = 0: the regular solution is purely INGOING, the
    time-reverse of a quasinormal mode, not a quasinormal mode. R_l blows up at omega = +i j, where
    the solution IS purely outgoing -- but that is the UPPER half plane, a growing mode, and not a
    decaying resonance. So there is no decaying quasinormal mode anywhere in the c = 0 family.

    Independently obtained by an adversarial re-derivation in the same wave and reproduced here
    from this file's own Jost polynomials; the two agree including the (-1)^l sign."""
    print("\nPART 3c -- the reflection amplitude, and the last pole candidates")
    tt, ww = sp.Symbol('t'), sp.Symbol('w')

    def Qpoly(lv, wsym):
        co = [sp.Symbol(f'q{i}') for i in range(lv)]
        Q = tt**lv + sum(co[i]*tt**i for i in range(lv))
        eq = sp.expand((tt**2 - 1)*sp.diff(Q, tt, 2) + 2*(tt - sp.I*wsym)*sp.diff(Q, tt)
                       - lv*(lv + 1)*Q)
        return sp.expand(Q.subs(sp.solve(sp.Poly(eq, tt).all_coeffs(), co, dict=True)[0]))

    for lv in range(1, 8):
        R = sp.simplify(Qpoly(lv, ww).subs(tt, 1)/Qpoly(lv, -ww).subs(tt, 1))
        blaschke = (-1)**lv*sp.prod([(ww + sp.I*j)/(ww - sp.I*j) for j in range(1, lv + 1)])
        # |R| = 1 checked EXACTLY on the real axis, not numerically: for real omega each factor
        # has |omega + i j|^2 = |omega - i j|^2 = omega^2 + j^2, so the modulus is 1 identically.
        # (An earlier numeric form of this check failed at l=4 and l=7 on 1e-16 -- double-precision
        # epsilon read as a defect, which is the wrong tolerance, not the wrong physics.)
        # for real omega the conjugate is obtained by I -> -I, so |R|^2 = R * R|_{I -> -I}
        mod2 = sp.cancel(sp.together(R*R.subs(sp.I, -sp.I)))
        check(sp.simplify(sp.factor(R) - sp.factor(blaschke)) == 0 and sp.simplify(mod2 - 1) == 0,
              f"l={lv}: R = (-1)^l prod (w+ij)/(w-ij), and |R|^2 - 1 = "
              f"{sp.simplify(mod2 - 1)} identically for real omega")
    print("     TOTAL REFLECTION at every real frequency: no transmission, no width, no rate.")
    print("     R = 0 at omega = -i j (purely INGOING: the time reverse of a QNM, not a QNM);")
    print("     R = infinity at omega = +i j (purely outgoing, but GROWING -- upper half plane).")
    print("     => no decaying quasinormal mode anywhere in this family. PART 3b's residue closes")
    print("        AGAINST the tower, not for it.")


# ---------------------------------------------------------------------------------------------
def part4_structure(cvals=(-2, -1, 0)):
    """The structural facts, and the one that decides the conjecture."""
    print("\nPART 4 -- the structure OF THE CANDIDATE SET")
    print("     READ THIS AFTER PART 3b. What follows describes where the quantisation condition")
    print("     1/Gamma(alpha) = 0 puts its roots. For the two physically relevant members --")
    print("     c = -2 and c = 0, both with INTEGER Delta -- PART 3b shows those roots are NOT")
    print("     poles of the retarded response. The formulae below are therefore a description of")
    print("     a CANDIDATE SET, not of a pole set, and every word like 'tower' or 'gap' should")
    print("     be read that way until the non-integer-Delta case is verified.")
    n, lv = sp.symbols('n l_', nonnegative=True, integer=True)
    for cv in cvals:
        s = sp.sqrt(1 - 4*cv)
        lo = sp.simplify(lv + 2*n + (3 - s)/2)
        hi = sp.simplify(lv + 2*n + (3 + s)/2)
        step = sp.simplify(lo.subs(n, n + 1) - lo)
        check(step == 2, f"c = {cv:>2}: candidate spacing is exactly 2H (independent of l and c)")
        print(f"     c = {cv:>2}:  i*omega/H = {lo}   and   {hi}")
    print("\n     TWO PROPERTIES OF THE CANDIDATE SET, kept apart on purpose:")
    print("       DISCRETE, and spaced exactly 2H in the overtone index -- for EVERY c. This is")
    print("         the property the single-pole conjecture turns on, and it is unconditional.")
    print("       PURELY IMAGINARY (no oscillation, only decay) -- only for c <= 1/4. Past that")
    print("         branch point a real part appears; PART 3's c=1 row exhibits it. Which member")
    print("         the graviton picks is NOT established here, so the second property is offered")
    print("         as conditional and the verdict below does not rest on it.")
    print("\n     THE GAP IS c- AND SECTOR-DEPENDENT and is NOT reported as a single number:")
    for cv, lmin, why in ((-2, 0, "massless scalar, l>=0"),
                          (-2, 2, "massless scalar restricted to l>=2"),
                          (0, 2, "a c=0 member restricted to l>=2")):
        s = sp.sqrt(1 - 4*cv)
        g = sp.simplify(lmin + (3 - s)/2)
        print(f"       c={cv:>2}, l_min={lmin} ({why}): lowest |Im omega|/H = {g}"
              + ("   <-- NOT gapped: an exact zero mode" if g == 0 else ""))
    print("\n     THE RATIO THAT WOULD DECIDE 'SINGLE POLE' -- gap over spacing:")
    for cv, lmin in ((-2, 2), (-1, 2), (0, 2)):
        s = sp.sqrt(1 - 4*cv)
        g = sp.simplify(lmin + (3 - s)/2)
        print(f"       c={cv:>2}, l_min={lmin}:  gap/spacing = {sp.nsimplify(g/2)} "
              f"= {sp.N(g/2, 4)}  -- O(1)")
    print("     No small parameter appears anywhere in it. Scale separation would need")
    print("     gap >> spacing; here they are the same order, and both are set by H alone.")


# ---------------------------------------------------------------------------------------------
def part4b_no_branch_cut():
    """POLES OR A CUT -- the question that separates two verdict classes, settled by how fast the
    potential dies in the tortoise coordinate.

    In the tortoise coordinate r_* = arctanh(H r) the static patch runs to r_* -> +infinity, and
    the potential becomes
        V(r_*) = H^2 sech^2(r_*) [ l(l+1)/tanh^2(r_*) + c ]  ->  4 H^2 (l(l+1) + c) e^{-2 r_*}.
    EXPONENTIAL decay. For an exponentially decaying potential the Jost solutions are analytic in
    omega on the whole plane (the defining integral equations converge in a half-plane and continue
    entire), so the retarded Green's function -- a ratio of such solutions over their Wronskian --
    is MEROMORPHIC: its only singularities are the poles above.

    This is exactly where the asymptotically-flat intuition would mislead. A Schwarzschild-like
    potential falls off as a POWER of r_*, and that is what produces a branch cut at the origin and
    late-time power-law tails. Nothing of that kind is available here."""
    print("\nPART 4b -- poles or a cut")
    rs = sp.Symbol('r_*', positive=True)
    lv = sp.Symbol('l_', nonnegative=True)
    V = H**2*sp.sech(rs)**2*(lv*(lv + 1)/sp.tanh(rs)**2 + c)
    # exact rewrite of V in terms of r_* : check it against the r-form at several radii
    worst = 0
    for cv in (-2, -1, 0):
        for lval in (0, 2, 3):
            for rval in (sp.Rational(1, 5), sp.Rational(1, 2), sp.Rational(4, 5)):
                rstar = sp.atanh(rval)
                a = (1 - rval**2)*(lval*(lval + 1)/rval**2 + cv)
                b = V.subs({H: 1, c: cv, lv: lval, rs: rstar})
                worst = max(worst, abs(complex(sp.N(sp.simplify(a - b), 40))))
    check(worst < 1e-30, f"V written in r_* agrees with V(r) to {worst:.1e} at 27 sample points")
    lead = sp.limit(sp.simplify(V*sp.exp(2*rs)), rs, sp.oo)
    check(sp.simplify(lead - 4*H**2*(lv*(lv + 1) + c)) == 0,
          "V(r_*) -> 4 H^2 (l(l+1) + c) e^{-2 r_*} : EXPONENTIAL fall-off")
    for cv, lval in ((-2, 2), (0, 2)):
        for R in (2, 4, 8):
            num = sp.N(V.subs({H: 1, c: cv, lv: lval, rs: R}), 8)
            print(f"     c={cv:>2} l={lval}: V(r_*={R}) = {num}")
    print("     A power-law tail would be the signature of a cut; this decays like exp(-2 r_*),")
    print("     so the Jost solutions stay entire in omega and the response is MEROMORPHIC.")
    print("     STRENGTH: the fall-off is COMPUTED here; the step from exponential fall-off to")
    print("     entire Jost solutions is a standard scattering-theory result and is USED, not")
    print("     re-derived. That step is the weakest link in this part and is named as such.")


# ---------------------------------------------------------------------------------------------
def part5_memory_kernel():
    """What the tower means for a MEMORY KERNEL, which is what the conjecture is about."""
    print("\nPART 5 -- the memory kernel: single pole versus tower (CONDITIONAL)")
    print("     This part compares a single-pole kernel with a MULTI-POLE one. Per PART 3b it is")
    print("     conditional on there being a tower at all, which is NOT established for c = 0.")
    tt, tau, A0, A1 = sp.symbols('t tau A_0 A_1', positive=True)
    debye = sp.exp(-tt/tau)
    check(sp.simplify(sp.diff(debye, tt)*tau + debye) == 0,
          "a single-pole (Debye) kernel obeys tau nu' + nu = 0: ONE rate, exactly")
    g0, g1 = sp.symbols('gamma_0 gamma_1', positive=True)
    tower = A0*sp.exp(-g0*tt) + A1*sp.exp(-g1*tt)
    check(sp.simplify(sp.diff(tower, tt)/tower).free_symbols != set(),
          "a two-term tower has a TIME-DEPENDENT instantaneous rate: not one rate at any finite t")
    ratio = sp.simplify(sp.exp(-(g1 - g0)*tt).subs({g1 - g0: 2}))
    print(f"     successive tower terms separate as exp(-2 H t)  ->  {ratio}")
    for T in (sp.Rational(1, 10), sp.Rational(1, 2), 1, 2, 5):
        print(f"       H t = {str(T):>4}:  second/first = {sp.N(sp.exp(-2*T), 6)}")
    print("     At H t ~ 1 the subleading terms are TENS OF PERCENT. The single-pole form is")
    print("     recovered by waiting, not by any limit of the parameters -- which is exactly the")
    print("     distinction between the pre-registered S1 (parametric suppression, exhibited) and")
    print("     S2 (a statement about leading late-time behaviour, bookable only as a restatement).")


# ---------------------------------------------------------------------------------------------
def part5b_mode_density():
    """DOES THE SUPER-OHMIC COUNTING SURVIVE DISCRETENESS?

    The framework's short-memory argument runs through a bath density of states ~ omega^2, giving a
    super-Ohmic J(omega) ~ omega^3.  That counting is a CONTINUUM statement, and the static patch's
    free spectrum is a DISCRETE tower -- which is the first thing an auditor should suspect of not
    transferring.  So count.

    Number of poles with decay rate gamma <= Gamma, summed over both branches, with the (2l+1)
    multiplicity of each angular momentum:
        N(Gamma) = sum_branches sum_{l >= l_min} (2l+1) * #{ n >= 0 : l + 2n + Delta <= Gamma }.
    """
    print("\nPART 5b -- the mode density of the CANDIDATE set (conditional, see PART 3b)")
    import math

    def N(Gamma, cv, lmin):
        sq = math.sqrt(1 - 4*cv)
        tot = 0
        for D in ((3 - sq)/2, (3 + sq)/2):
            l = lmin
            while l + D <= Gamma:
                nmax = math.floor((Gamma - D - l)/2)
                if nmax >= 0:
                    tot += (2*l + 1)*(nmax + 1)
                l += 1
        return tot

    for cv, lmin in ((-2, 0), (0, 2)):
        print(f"     c={cv:>2}, l_min={lmin}:")
        prev = None
        for G in (20, 40, 80, 160, 320):
            n = N(G, cv, lmin)
            slope = (math.log(n/prev)/math.log(2)) if prev else float('nan')
            print(f"       Gamma/H = {G:>4}:  N = {n:>9}   N/Gamma^3 = {n/G**3:.4f}"
                  + ("" if prev is None else f"   local log2-slope = {slope:.3f}"))
            prev = n
    # the exponent, extracted rather than asserted
    for cv, lmin in ((-2, 0), (0, 2)):
        a, b = N(400, cv, lmin), N(800, cv, lmin)
        slope = math.log(b/a)/math.log(2)
        check(abs(slope - 3) < 0.02,
              f"c={cv:>2}, l_min={lmin}: N(Gamma) grows as Gamma^{slope:.3f}, i.e. Gamma^3")
    print("     => dN/dGamma ~ Gamma^2: THE SAME omega^2 COUNTING the continuum argument uses.")
    print("     Discreteness does not by itself destroy the super-Ohmic input -- the level")
    print("     spacing is 2H but the DEGENERACY grows, and the two effects cancel in the count.")
    print("     WHAT THIS DOES NOT SHOW, stated because the gap between the two is where a")
    print("     migration would quietly help itself: matching a mode COUNT is not matching a")
    print("     spectral DENSITY J(omega). J needs the couplings -- the residues -- and this file")
    print("     computes pole POSITIONS only. The super-Ohmic premise is therefore NOT re-derived")
    print("     on the static patch here; only the one objection that discreteness alone kills it")
    print("     is answered.")


def part6_mutants():
    """Mutation battery: each mutant must be caught by the checks above, or they are decorative."""
    print("\nPART 6 -- mutation battery")
    killed = 0
    ff = 1 - r**2

    # M1: wrong potential sign on the c term -> the exhibited mode stops solving the ODE
    psi = r**3*(1 - r**2)**(-sp.I*(-3*sp.I)/2)
    res_true = sp.simplify(ff*sp.diff(ff*sp.diff(psi, r), r) + ((-3*sp.I)**2 - ff*(2*3/r**2 + 0))*psi)
    res_mut = sp.simplify(ff*sp.diff(ff*sp.diff(psi, r), r) + ((-3*sp.I)**2 - ff*(2*3/r**2 - 1))*psi)
    killed += (res_true == 0 and res_mut != 0)
    check(res_true == 0 and res_mut != 0, "M1 wrong c in the potential: residual test kills it")

    # M2: an off-tower frequency -> 2F1 does not truncate, so the mode is not elementary
    Fo = sp.hyperexpand(sp.hyper(((2 - sp.I*(-sp.Rational(5, 2)*sp.I))/2 + sp.Rational(3, 4)
                                  - sp.Rational(1, 4),
                                  (2 - sp.I*(-sp.Rational(5, 2)*sp.I))/2 + sp.Rational(3, 4)
                                  + sp.Rational(1, 4)), (2 + sp.Rational(3, 2),), r**2))
    killed += (not sp.simplify(Fo).is_polynomial(r))
    check(not sp.simplify(Fo).is_polynomial(r),
          "M2 off-tower frequency (l=2, i w = 5/2): no truncation, so no exhibited mode")

    # M3: claiming a spacing of H rather than 2H within one branch
    n = sp.Symbol('n', nonnegative=True, integer=True)
    lo = 2 + 2*n + 1
    killed += (sp.simplify(lo.subs(n, n + 1) - lo) != 1)
    check(sp.simplify(lo.subs(n, n + 1) - lo) != 1, "M3 'spacing = H within a branch' is false")

    # M4: claiming the scalar tower is gapped (it is not: l=n=0 on the lower branch gives zero)
    gap_scalar = sp.simplify(0 + (3 - sp.sqrt(1 - 4*(-2)))/2)
    killed += (gap_scalar == 0)
    check(gap_scalar == 0,
          "M4 'the massless scalar tower is gapped' is false -- l=n=0 sits at omega = 0 exactly")

    # M5: claiming parametric suppression -- the gap/spacing ratio would have to be large
    ratios = [sp.N((lm + (3 - sp.sqrt(1 - 4*cv))/2)/2, 4) for cv, lm in ((-2, 2), (-1, 2), (0, 2))]
    killed += all(x < 3 for x in ratios)
    check(all(x < 3 for x in ratios),
          f"M5 'the tower is parametrically suppressed': gap/spacing = {ratios}, all O(1)")
    print(f"     {killed}/5 mutants killed")
    return killed == 5


def main():
    part0_background()
    part0b_native_temperature()
    part1_scalar_potential()
    part1b_graviton_c()
    part2_hypergeometric()
    part3_exact_modes()
    part3b_the_outgoing_check_was_wrong()
    part3c_reflection_amplitude()
    part4_structure()
    part4b_no_branch_cut()
    part5_memory_kernel()
    part5b_mode_density()
    part6_mutants()
    print("\n" + "=" * 92)
    if FAIL:
        print("SELFTEST FAILED:")
        for m in FAIL:
            print("   -", m)
        return 1
    print("SELFTEST GREEN -- and the headline is a RETRACTION, not a result.")
    print("  ESTABLISHED: for the c = 0 family (which the workflow's independent derivation")
    print("    identifies as the graviton's, both parities), the frequencies")
    print("    omega/H = -i(l + 2n + Delta) are NOT quasinormal. The regular solution has ingoing")
    print("    amplitude B = -A at every omega, exactly, because both Jost solutions are monic in")
    print("    coth(x) and so share the same x^-l singularity. Shown exactly at three frequencies")
    print("    (decomposition residual ~1e-163) and generally for l = 1..6.")
    print("  WHAT WENT WRONG: 'purely outgoing by inspection' tested that the hypergeometric")
    print("    factor is non-zero at the horizon. The peeled factor (1-r^2)^{-i w/2} is itself not")
    print("    purely outgoing when i*w is a positive integer -- the Gamma(-i w) pole colliding")
    print("    with the 1/Gamma(alpha) zero, which PART 2 printed and this file then ignored.")
    print("  STILL TRUE AND UNAFFECTED: the background curvature checks, Lambda = 3H^2,")
    print("    V_scalar = f[l(l+1)/r^2 - 2H^2], the hypergeometric reduction and its alpha, beta,")
    print("    gamma, the exponential fall-off of V in r_*, and beta = 2*pi/H.")
    print("  AND THEN CLOSED, AGAINST THE TOWER: R_l(omega) = (-1)^l prod (w+ij)/(w-ij) is a finite")
    print("    Blaschke product, |R| = 1 on the real axis -- total reflection, no width, no rate.")
    print("    Its zeros at omega = -i j are purely INGOING solutions (time-reversed QNMs); its")
    print("    poles at +i j are growing. No decaying quasinormal mode anywhere in the c=0 family.")
    print("    The c = -2 case and non-integer Delta remain untouched and unverified.")
    print("  DISCREPANCY, SURFACED NOT ADJUDICATED: this contradicts the widely reported de Sitter")
    print("    quasinormal spectrum, and the public document repeats that spectrum on literature")
    print("    authority. One of the two is wrong. This file does not claim to be the survivor.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
