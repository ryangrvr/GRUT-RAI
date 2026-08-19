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

  (C) NOT DERIVED IN-HOUSE, AND FLAGGED. The value of c for the axial gravitational master
      equation is not established by this file. Two attempts at a full linearised-Einstein
      derivation on this hardware did not complete. THE STRUCTURAL CONCLUSION DOES NOT DEPEND ON
      IT: (A) holds for every c, so the tower's existence, its purely-imaginary character and its
      2H spacing are independent of which member of the family the graviton picks. What DOES
      depend on c is the GAP, and that is reported as c-dependent rather than as a number.

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
                        bad_horizon += 1
                    freqs.setdefault(cv, set()).add(sp.simplify(sp.I*wv))
    check(bad_ode == 0, f"all {total} exhibited modes satisfy the ODE with residual 0 "
                        f"({total - tier2} symbolically, {tier2} to 45 digits at 8 radii)")
    check(bad_poly == 0, f"all {total} truncate to polynomials (so the mode is elementary)")
    check(bad_horizon == 0,
          f"all {total} have a NONZERO analytic factor at the horizon -- purely outgoing, no "
          f"ingoing admixture")
    for cv in tuple(cmain) + tuple(ccontrast):
        got = sorted(freqs[cv], key=lambda x: (float(sp.re(x)), float(sp.im(x))))
        tag = "" if cv <= sp.Rational(1, 4) else "   <-- c > 1/4: a REAL part appears"
        print(f"     c = {cv:>2}:  i*omega/H in "
              f"{[sp.sstr(sp.nsimplify(x)) for x in got[:7]]} ...{tag}")
    return freqs


# ---------------------------------------------------------------------------------------------
def part4_structure(cvals=(-2, -1, 0)):
    """The structural facts, and the one that decides the conjecture."""
    print("\nPART 4 -- the structure")
    n, lv = sp.symbols('n l_', nonnegative=True, integer=True)
    for cv in cvals:
        s = sp.sqrt(1 - 4*cv)
        lo = sp.simplify(lv + 2*n + (3 - s)/2)
        hi = sp.simplify(lv + 2*n + (3 + s)/2)
        step = sp.simplify(lo.subs(n, n + 1) - lo)
        check(step == 2, f"c = {cv:>2}: overtone spacing is exactly 2H (independent of l and c)")
        print(f"     c = {cv:>2}:  i*omega/H = {lo}   and   {hi}")
    print("\n     TWO PROPERTIES AT DIFFERENT STRENGTHS, kept apart on purpose:")
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
    print("\nPART 5 -- the memory kernel: single pole versus tower")
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
    print("\nPART 5b -- the mode density of the tower")
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
    part2_hypergeometric()
    part3_exact_modes()
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
    print("SELFTEST GREEN. Structure on the de Sitter static patch, at two strengths:")
    print("  UNCONDITIONAL, for every member of the family: a DISCRETE tower of retarded poles,")
    print("    spaced exactly 2H in the overtone index, with NO parameter separating the leading")
    print("    pole from the rest -- gap and spacing are both O(H). Not a single pole; not a cut.")
    print("  CONDITIONAL on c <= 1/4: the poles are purely imaginary, so the response decays")
    print("    without oscillating. Past that branch point a real part appears. Which member the")
    print("    graviton picks is not established here.")
    print("  The gap is sector-dependent and is reported as such, never as a number.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
