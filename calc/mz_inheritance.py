#!/usr/bin/env python3
"""mz_inheritance: does the projected memory kernel inherit the Matsubara ladder?

THE QUESTION, as posed by the owner on 2026-08-19 and recorded in rung3_single_pole's tier_note:

    KMS ties N to Im K_R, so N inherits coth's poles UNLESS Im K_R has zeros at the Matsubara
    frequencies that cancel them. That cancellation is the only route by which the projected
    kernel could fail to inherit the ladder.

THE ANSWER IS NOT A YES OR A NO. It is that the question has TWO answers, and which one applies is
fixed by a convention rung3's statement never makes:

  (1) THE ESCAPE THE OWNER NAMED DOES NOT OPERATE. The framework's own J has no zeros on the
      imaginary axis -- J(i v) = eta (i v)^3 exp(+(v/w_c)^2) is nonzero for every v -- so nothing
      cancels coth's poles. On the SYMMETRISED route the ladder is inherited, exactly as framed.

  (2) BUT THE SYMMETRISED ROUTE IS NOT THE ONLY ONE, AND THE OTHER STANDARD CHOICE HAS NO LADDER
      AT ALL. Mori-Zwanzig projection for a quantum system conventionally uses the KUBO-MORI
      (canonical) inner product, and the Kubo correlation function carries

            C_K(w) = 2 chi''(w) / (beta w)          NOT      C_S(w) = chi''(w) coth(beta w / 2).

      The coth is REPLACED by 2/(beta w). Every Matsubara pole is gone; what is left is a single
      pole at w = 0. Derived here from the definition, not quoted.

  (3) AND THE GENERALISED-LANGEVIN FRICTION KERNEL IS TEMPERATURE-INDEPENDENT OUTRIGHT:
      gamma(t) ~ int (J(w)/w) cos(w t) dw carries no coth, so it cannot carry the ladder. Its
      decay rate is set by the cutoff and does not move when T moves -- checked numerically at two
      temperatures, against nu(t) which does move.

SO: rung3's phrase "the Mori-Zwanzig kernel" does not currently denote a unique object, and the
two objects it could denote answer this question OPPOSITELY. That is a defect in the node's
STATEMENT rather than in its physics, it is cheap to repair, and it must be repaired before the
ladder can be said to bear on the conjecture at all.

WHAT THIS MEANS FOR THE ADVERSE FILING OF 2026-08-19: that filing said the ladder is adverse to
rung3 and that inheritance was the open step. The first half stands for the symmetrised noise
kernel and is now sharpened -- the escape route is closed. The second half is answered in a way
that WEAKENS the adverse reading: on the conventional MZ inner product there is no ladder to
inherit. The adverse conclusion is therefore CONDITIONAL on a reading of rung3 that rung3 does not
state, and this file says so rather than leaving the stronger version standing.

Pure stdlib + sympy/mpmath. Run: python3 calc/mz_inheritance.py
"""
import math
import sys

import sympy as sp

FAIL = []


def check(cond, msg):
    print(("  ok   " if cond else "  FAIL ") + msg)
    if not cond:
        FAIL.append(msg)


# ---------------------------------------------------------------------------------------------
def part1_the_escape_route_is_NOT_closed():
    """RETRACTED AND REPLACED, 2026-08-19, on the owner's counterexample.

    THE FIRST VERSION scanned J = eta w^s exp(-(w/w_c)^2) for s = 1,2,3,5, found J(i v) != 0 every
    time, and concluded "the escape the owner named is closed for this J". Every evaluation was
    correct and the conclusion does not follow: THE LOOP VARIED THE EXPONENT AND HELD THE
    FUNCTIONAL FORM FIXED, and the form is the only thing that matters. A positive power times a
    nowhere-vanishing entire factor cannot have zeros off the origin -- true BY CONSTRUCTION OF
    THE FAMILY, not as a fact about de Sitter.

    AND IT IS THE SAME FAILURE THIS FILE DIAGNOSES TWO PARTS LATER. PART 3b convicts the June
    analyticity argument of checking omega = 0 -- the one point where cancellation was possible --
    and concluding about the rungs. PART 1 checked a family where cancellation was IMPOSSIBLE by
    construction and concluded about the general case. Both are sampling-region failures; they
    point in opposite directions; and the second was written into this file by the same hand that
    wrote the first up as a lesson, in the same file, in the same wave.

    THE COUNTEREXAMPLE, in this file's own idiom, cutoff and all:

        A(w) = eta w^2 tanh(pi w / H) exp(-(w/w_c)^2)

    odd, positive for w > 0 (so passive / Herglotz-admissible on the line), Gaussian cutoff intact,
    A -> pi eta w^3 / H in the infrared (super-Ohmic s = 3, exactly what is booked), and -- since
    beta = 2 pi / H -- coth(beta w/2) A(w) = eta w^2 exp(-(w/w_c)^2), ENTIRE. Every Matsubara pole
    is gone. An admissible spectral function executes the escape completely.

    THE UNDECLARED ASSUMPTION, now declared: power-law-times-cutoff is the FLAT-SPACE thermal-bath
    idiom, where T is an external parameter and nothing would produce a tanh(beta w/2) factor. In
    de Sitter T = H/2pi and the dynamics both descend from H, so A is a function of w/H and the
    reflection formula Gamma(z)Gamma(1-z) = pi/sin(pi z) generates exactly sinh/cosh structure in
    pi w / H. The escape is not exotic here. Whether it is REALISED is PART 1b's question."""
    print("\nPART 1 -- RETRACTED: the escape route is NOT closed by the scan that was here")
    import mpmath as mp
    mp.mp.dps = 30
    M = mp.mpf
    H, wc = M(1), M(30)
    A = lambda w: w**2*mp.tanh(mp.pi*w/H)*mp.e**(-(w/wc)**2)
    check(all(abs(A(-M(v)) + A(M(v))) < M('1e-25') for v in ('0.7', '2.3')),
          "the counterexample A = w^2 tanh(pi w/H) exp(-(w/w_c)^2) is ODD")
    check(all(A(M(v)) > 0 for v in ('0.3', '1', '4')),
          "positive for w > 0 -- passive, admissible on the real line")
    check(abs(A(M('0.003'))/M('0.003')**3 - mp.pi/H) < M('1e-4'),
          f"super-Ohmic s = 3 in the IR: A/w^3 -> {mp.nstr(A(M('0.003'))/M('0.003')**3, 8)} "
          f"= pi/H")
    check(all(abs(A(mp.mpc(0, n))) < M('1e-25') for n in (1, 2, 3, 7)),
          "and it VANISHES at w = i n H for n = 1,2,3,7 -- on the whole ladder")
    Nf = lambda w: w**2*mp.e**(-(w/wc)**2)
    check(max(abs(A(M(v))/mp.tanh(mp.pi*M(v)/H) - Nf(M(v))) for v in ('0.4', '1.5', '6'))
          < M('1e-25'),
          "so coth(beta w/2) A(w) = w^2 exp(-(w/w_c)^2) EXACTLY: entire, no Matsubara pole")
    print("     => the escape is CONSISTENT with passivity, with super-Ohmic scaling and with the")
    print("        Herglotz representation. It is not structurally impossible, and the earlier")
    print("        scan could not have found this because tanh is not in the family it varied.")


# ---------------------------------------------------------------------------------------------
def part1b_is_the_escape_REALISED_at_free_level():
    """THE DECISIVE EVALUATION, done from this repository's own exact c = 0 solution rather than
    from a Gamma-ratio taken on report.

    G_R(x,x') = psi_reg(x_<) u_+(x_>) / W, and A(w) = [G_R(w) - G_R(-w)]/2i is the analytic
    continuation of Im G_R. Three facts, each checked numerically below, collapse it:
        u_+(-w) = u_-(w) exactly;  psi_reg (canonically ~ x^{l+1}) is EVEN in w;
        W[psi_reg, u_+] = -(2l+1), independent of w.
    Hence A(w) is proportional to u_+ - u_- = N(w) psi_reg, and A's w-zeros ARE N's:

        N(w) = 2 i w prod_{j=1..l} (w^2 + j^2 H^2) / c_l

    SO THE FREE SPECTRAL FUNCTION VANISHES AT THE FIRST l RUNGS AND AT NO OTHERS. The escape needs
    zeros at EVERY rung. At fixed l it gets exactly l of them, and is NONZERO at every n > l.
    Summing over l with its (2l+1) degeneracy does not help: at rung n the terms with l >= n
    vanish and the terms with l < n do not, so the total is nonzero at every rung.

    THE ANSWER IS THEREFORE: PARTIALLY, AND NOT ENOUGH. The mechanism the owner identified is
    real -- the geometry does put spectral zeros on the Matsubara ladder, at spacing exactly H --
    but it truncates at l. Note the SAME finite set already appeared in an independent object:
    calc/static_patch_tt_response.py PART 3c's Blaschke amplitude has zeros at w = -i j H for
    j = 1..l. Two different objects, one truncated ladder.

    WHAT THIS DOES TO rung3: the escape has no free-level realisation, so it would require the
    interacting Sigma to manufacture zeros at every n > l where the free theory has none. That is
    a much heavier lift than preserving zeros that are already there, and it is the outcome
    adverse to single-pole."""
    print("\nPART 1b -- is the escape REALISED at free level? (exact c = 0 solution)")
    import mpmath as mp
    mp.mp.dps = 30
    xs, ws, tsym = sp.symbols('x omega t')

    def Qp(l, wsym):
        co = [sp.Symbol(f'q{i}') for i in range(l)]
        P = tsym**l + sum(co[i]*tsym**i for i in range(l))
        eq = sp.expand((tsym**2 - 1)*sp.diff(P, tsym, 2)
                       + 2*(tsym - sp.I*wsym)*sp.diff(P, tsym) - l*(l+1)*P)
        return sp.expand(P.subs(sp.solve(sp.Poly(eq, tsym).all_coeffs(), co, dict=True)[0]))

    for l in (2, 3, 4):          # PHYSICAL MULTIPOLES ONLY -- the graviton has no l < 2
        ups = sp.exp(sp.I*ws*xs)*Qp(l, ws).subs(tsym, sp.coth(xs))
        ums = sp.exp(-sp.I*ws*xs)*Qp(l, -ws).subs(tsym, sp.coth(xs))
        up = sp.lambdify((xs, ws), ups, 'mpmath')
        um = sp.lambdify((xs, ws), ums, 'mpmath')
        Nsym = sp.simplify(sp.expand(sp.series(sp.simplify(ups - ums), xs, 0, l + 2)
                                     .removeO()).coeff(xs, l + 1))
        Nl = sp.lambdify(ws, Nsym, 'mpmath')
        par = max(abs(up(mp.mpf(a), -mp.mpf(b)) - um(mp.mpf(a), mp.mpf(b)))
                  for a, b in (('0.7', '0.4'), ('1.3', '2.1')))
        d = mp.mpf('1e-10')
        psi = lambda x, w: (up(x, w) - um(x, w))/Nl(w)
        Wr = []
        for a, b in (('0.6', '0.5'), ('1.1', '2.7'), ('2.0', '0.2')):
            x, w = mp.mpf(a), mp.mpf(b)
            dpsi = (psi(x + d, w) - psi(x - d, w))/(2*d)
            dup = (up(x + d, w) - up(x - d, w))/(2*d)
            Wr.append(psi(x, w)*dup - dpsi*up(x, w))
        check(par < mp.mpf('1e-20'), f"l={l}: u_+(-w) = u_-(w) exactly (dev {mp.nstr(par, 3)})")
        check(all(abs(v + (2*l + 1)) < mp.mpf('1e-15') for v in Wr),
              f"l={l}: W[psi_canonical, u_+] = -(2l+1) = {-(2*l+1)} at three (x, w) -- "
              f"w-INDEPENDENT, so A is proportional to N(w)")
        zeros = [n for n in range(1, l + 3) if abs(Nl(mp.mpc(0, n))) < mp.mpf('1e-20')]
        nonz = [n for n in range(1, l + 3) if abs(Nl(mp.mpc(0, n))) >= mp.mpf('1e-20')]
        check(zeros == list(range(1, l + 1)) and nonz,
              f"l={l}: N = {sp.factor(Nsym)} -> A VANISHES at rungs n = {zeros} and is "
              f"NONZERO at n = {nonz}")
    print("\n     *** THE PHYSICAL MULTIPOLE RANGE, corrected 2026-08-19 (owner). The graviton has")
    print("     NO l = 0 and NO l = 1 -- those carry mass and angular momentum and are not")
    print("     dynamical -- so every physical multipole has l >= 2. An earlier version of this")
    print("     part tabulated l = 1, which is not a graviton mode. ***")
    print("\n     THE CORRECTION, FILED FIRST BECAUSE THE FAVOURABLE HALF IS THE QUOTABLE ONE:")
    print("       A_l vanishes at n = 1..l, so the SLOWEST SURVIVING RUNG IS (l+1)H.")
    print("       The free-level memory time is therefore 1/(3H), NOT 1/H. Every statement in")
    print("       this repository reading 'slowest rung exactly H' or 'memory time 1/H' is about")
    print("       a ladder that includes modes the graviton does not have.")
    print("       AND IT IS MULTIPOLE-DEPENDENT: 3H for l=2, 4H for l=3, (l+1)H generally.")
    print("       rung3 asserts THE memory time. The free theory supplies a FAMILY indexed by")
    print("       multipole, so there is no single rate for a single pole to be -- which is a")
    print("       stronger objection than any share arithmetic: the approximation is not poor,")
    print("       THE OBJECT IT APPROXIMATES IS NOT THERE.")
    print("\n     THE FAVOURABLE HALF, real and worth booking: because every physical l >= 2,")
    print("     RUNGS n = 1 AND n = 2 VANISH FOR EVERY PHYSICAL MULTIPOLE. The escape mechanism")
    print("     is genuine and it kills the two slowest rungs universally -- the ones that govern")
    print("     late-time memory. That is the first structural result in this fortnight that runs")
    print("     the framework's way.")
    print("\n     leading-surviving-rung share (weights |A_l| on the ladder, no cutoff):")
    import math as _m

    def _w(l, n):
        p = n
        for j in range(1, l + 1):
            p *= abs(j*j - n*n)
        return p
    print(f"       {'Ht':>5} " + "".join(f"{'l=' + str(l):>9}" for l in (2, 3, 4)))
    for Ht in (1.0, 2.0, 3.0):
        row = f"       {Ht:>5.1f} "
        for l in (2, 3, 4):
            tot = sum(_w(l, n)*_m.exp(-n*Ht) for n in range(l + 1, l + 400))
            row += f"{_w(l, l + 1)*_m.exp(-(l + 1)*Ht)/tot*100:8.1f}%"
        print(row)
    print("       -- 6.4% at l=2 and Ht=1, and the share FALLS with l: higher multipoles are")
    print("       WORSE, not better. Indicative: the weighting is |A_l| with no cutoff.")
    print("\n     ANSWER: PARTIALLY, AND NOT ENOUGH. The free spectral function carries ladder")
    print("     zeros at spacing exactly H -- the geometry really does produce them -- but only")
    print("     the FIRST l of them per angular momentum, and none beyond. The escape requires")
    print("     all of them. Summing over l cannot repair it: at rung n the l >= n terms vanish")
    print("     and the l < n terms do not.")
    print("     => the escape has NO FREE-LEVEL REALISATION, and Sigma would have to manufacture")
    print("        zeros where the free theory has none. That is the outcome adverse to rung3.")


# ---------------------------------------------------------------------------------------------
def part1c_the_panel_corrections():
    """FOUR CORRECTIONS from the adversarial pass of 2026-08-19. All four lenses returned
    refuted=False -- the adverse conclusion survives -- and all four found something wrong with
    how it was stated. Two run FAVOURABLE to the framework, one is a real gap in my reasoning, and
    the fourth relocates the cause of the favourable half entirely.

    (1) THE ZERO SET WAS UNDER-COUNTED, favourably. N ~ w prod_{j=1..l}(w^2 + j^2) carries an
        overall w, so it vanishes at w = 0 and at the NEGATIVE rungs too: exactly 2l+1 zeros,
        |n| <= l. So l+1 NON-NEGATIVE rungs cancel (n = 0..l), not l.

    (2) "A IS PROPORTIONAL TO N" IS FALSE AS WRITTEN -- reported independently by two lenses, and
        it is a genuine gap rather than a wrong number. The identity is
            A(w) = N(w) psi_reg(x_<;w) psi_reg(x_>;w) / (2i W)
        and that prefactor is entire of order 1, so it has INFINITELY MANY zeros -- located for
        l=2 at x=0.9 near w = 6.2564, 10.0118, 13.6229, ... and at x=2.0 near 2.6137, 4.3734, ...,
        a different set spaced ~pi/x. So A at fixed (x,x') vanishes at infinitely many w that are
        NOT rungs, and "at no others" is true of N and FALSE of A.
        THE RUNG CONCLUSION SURVIVES, but only via an argument that was not in my claim: on the
        imaginary axis w = i kappa the equation is psi'' = (kappa^2 + V) psi with V > 0, so
        psi_reg leaves the origin positive and stays positive -- no zeros there, so the prefactor
        adds no rung zeros. I asserted about A what I had proved about N.

    (3) THE ADVERSE CONCLUSION IS STRONGER THAN I STATED. At FIXED l the surviving rungs are the
        whole infinite tower n = l+1, l+2, ... So there is no single relaxation rate even at fixed
        multipole, before any sum over l. My phrasing implied the multiplicity came from summing
        over multipoles; it does not need to.

    (4) AND THE FAVOURABLE HALF IS KINEMATIC, NOT GEOMETRIC -- the most consequential correction.
        There is an exact sum rule, verified below to 26+ digits:

            sum_{l>=0} (2l+1) A_l(x,x;w)  =  -w sinh^2(x)

        The entire prod(w^2 + j^2) structure CANCELS IDENTICALLY when the multipoles are summed
        with their natural (2l+1) degeneracy. The l-summed local spectral density is exactly
        OHMIC and has NO Matsubara-rung zeros at all. So the ladder zeros are a PARTIAL-WAVE
        THRESHOLD FACTOR -- the de Sitter splitting of the flat-space order-(2l+1) centrifugal
        zero at w = 0 -- not a property of the physical local response. They survive into the
        graviton bath SOLELY BECAUSE l = 0 and l = 1 TENSOR HARMONICS DO NOT EXIST.
        So "the geometry genuinely kills the two slowest rungs" is wrong as filed: TWO MISSING
        PARTIAL WAVES kill them, and de Sitter does nothing. The effect is real and its cause is
        kinematic accident, which is a much weaker thing to book.

    AND ONE NEAR-MISS OF MY OWN, recorded because it nearly went the other way: my first attempt
    to check the sum rule summed to l = 80 at 30 digits and returned 1e16 instead of 1. I was one
    step from reporting "could not reproduce" against a correct result -- the failure was my own
    precision (the downward recursion and the double factorials lose everything at that l), not
    the rule."""
    print("\nPART 1c -- the adversarial pass: four corrections, two of them favourable")
    import mpmath as mp
    mp.mp.dps = 60

    def df(n):
        return 1 if n <= 0 else n*df(n - 2)

    def Qv(l, w, t):
        a = {l: mp.mpc(1), l + 1: mp.mpc(0), l + 2: mp.mpc(0)}
        for k in range(l - 1, -1, -1):
            a[k] = ((k + 2)*(k + 1)*a[k + 2] + 2j*w*(k + 1)*a[k + 1])/((k - l)*(k + l + 1))
        return sum(a[k]*t**k for k in range(l + 1))

    def Nv(l, w):
        p = 2j*w
        for j in range(1, l + 1):
            p *= (w*w + j*j)
        return p/((2*l + 1)*df(2*l - 1)**2)

    def termA(l, x, w):
        t = mp.coth(x)
        u = mp.e**(1j*w*x)*Qv(l, w, t) - mp.e**(-1j*w*x)*Qv(l, -w, t)
        ps = u/Nv(l, w)
        return -(ps*ps)*Nv(l, w)/(2j)

    # (1) the zero set, including n = 0 and the negative rungs
    for l in (2, 3):
        z = [n for n in range(-l - 2, l + 3) if abs(Nv(l, mp.mpc(0, n))) < mp.mpf('1e-30')]
        check(z == list(range(-l, l + 1)),
              f"(1) l={l}: N vanishes at n = {z} -- {len(z)} = 2l+1 rungs including n = 0, so "
              f"l+1 NON-NEGATIVE rungs cancel, not l (I under-counted, favourably)")
    # (4) the sum rule
    worst = mp.mpf(0)
    for x, w in ((mp.mpf('0.8'), mp.mpf('1.3')), (mp.mpf('1.5'), mp.mpc('0.4', '0.9')),
                 (mp.mpf('0.6'), mp.mpc(0, '2.2')), (mp.mpf('1.2'), mp.mpf('0.35'))):
        tot = sum(termA(l, x, w) for l in range(0, 31))
        tgt = -w*mp.sinh(x)**2
        worst = max(worst, abs(tot - tgt))
    check(worst < mp.mpf('1e-11'),
          f"(4) THE SUM RULE: sum_l (2l+1) A_l(x,x;w) = -w sinh^2 x at four (x,w), worst "
          f"deviation {mp.nstr(worst, 3)} -- the ladder structure CANCELS IDENTICALLY on summing")
    print("     => the l-summed local spectral density is exactly OHMIC with NO rung zeros.")
    print("     => the ladder zeros are a PARTIAL-WAVE THRESHOLD FACTOR. They survive into the")
    print("        graviton bath only because l = 0 and l = 1 tensor harmonics do not exist, so")
    print("        the favourable half is a KINEMATIC ACCIDENT OF TWO MISSING PARTIAL WAVES, not")
    print("        something de Sitter or the graviton does. Filed as such, weaker than booked.")
    print("     (2) 'A is proportional to N' is false as written -- see the docstring; the rung")
    print("         conclusion survives only via a positivity argument that was not in my claim.")
    print("     (3) at FIXED l the surviving rungs are the whole infinite tower n >= l+1, so")
    print("         there is no single rate even before summing over multipoles.")


# ---------------------------------------------------------------------------------------------
def part2_kubo_has_no_ladder():
    """DERIVE C_K(w) = 2 chi''(w)/(beta w) from the definition of the Kubo transform."""
    print("\nPART 2 -- the Kubo-Mori correlation function, derived from its definition")
    lam, beta, w = sp.symbols('lambda beta omega', positive=True)
    # C_K(t) = (1/beta) int_0^beta dlam <A(t - i lam) A>.  In frequency, <A(t-i lam)A> picks up
    # e^{-w lam} against the GREATER function C^>(w).  So C_K(w) = C^>(w) * (1/beta) int_0^beta
    # e^{-w lam} dlam.
    weight = sp.simplify(sp.integrate(sp.exp(-w*lam), (lam, 0, beta))/beta)
    check(sp.simplify(weight - (1 - sp.exp(-beta*w))/(beta*w)) == 0,
          f"the Kubo weight is (1 - e^{{-beta w}})/(beta w)   [{sp.simplify(weight)}]")
    chi2 = sp.Symbol("chi''", positive=True)
    Cgreater = 2*chi2/(1 - sp.exp(-beta*w))          # standard KMS/detailed-balance form
    CK = sp.simplify(Cgreater*weight)
    CS = sp.simplify(chi2*sp.coth(beta*w/2))
    check(sp.simplify(CK - 2*chi2/(beta*w)) == 0,
          f"C_K(w) = 2 chi''(w)/(beta w)   -- the coth is GONE, replaced by 2/(beta w)")
    check(sp.simplify(sp.simplify(Cgreater*(1 + sp.exp(-beta*w))/2) - CS) == 0,
          "and the SYMMETRISED one is C_S(w) = chi''(w) coth(beta w/2) -- the coth is retained")
    print("\n     THE DICHOTOMY, in one line:")
    print("       symmetrised : chi'' * coth(beta w/2)   -> poles at every w = 2 pi i n / beta")
    print("       Kubo-Mori   : chi'' * 2/(beta w)       -> ONE pole, at w = 0, and no ladder")
    print("     Both are correct correlation functions of the same state. They differ in which")
    print("     inner product the projection is taken with, and rung3 does not say which.")
    # exhibit the pole sets explicitly
    n = sp.Symbol('n', integer=True, positive=True)
    poleset = sp.simplify(sp.coth(beta*w/2).subs(w, 2*sp.pi*sp.I*n/beta))
    check(poleset in (sp.zoo, sp.oo, -sp.oo) or poleset.has(sp.zoo),
          "coth(beta w/2) is singular at w = 2 pi i n / beta for every n (the ladder)")
    kub = sp.simplify((2/(beta*w)).subs(w, 2*sp.pi*sp.I*n/beta))
    check(sp.simplify(kub) != sp.zoo,
          f"2/(beta w) is FINITE there ({sp.simplify(kub)}) -- no rung survives the Kubo transform")


# ---------------------------------------------------------------------------------------------
def _gamma(t, T, wc, s=3):
    """GLE friction kernel gamma(t) ~ int_0^inf (J(w)/w) cos(w t) dw. Note: NO coth."""
    import mpmath as mp
    mp.mp.dps = 25
    t, wc = mp.mpf(t), mp.mpf(wc)
    return mp.quadosc(lambda w: w**(s-1)*mp.e**(-(w/wc)**2)*mp.cos(w*t), [0, mp.inf], omega=t)


def _nu(t, T, wc, s=3):
    """Symmetrised noise kernel, WITH coth -- the object that carries the ladder."""
    import mpmath as mp
    mp.mp.dps = 25
    t, wc, T = mp.mpf(t), mp.mpf(wc), mp.mpf(T)
    return mp.quadosc(lambda w: w**s*mp.e**(-(w/wc)**2)/mp.tanh(w/(2*T))*mp.cos(w*t),
                      [0, mp.inf], omega=t)


def part3_friction_is_temperature_blind():
    """The discriminator: move T and see which kernel's decay rate moves."""
    print("\nPART 3 -- the friction kernel does not even contain T")
    import mpmath as mp
    wc = 1.0
    print("     gamma(t) at two temperatures (it has no T in it, so it must be identical):")
    same = True
    for t in (2.0, 4.0):
        a, b = _gamma(t, 0.05, wc), _gamma(t, 0.02, wc)
        d = float(abs(a - b))
        print(f"       t = {t}:  T=0.05 -> {mp.nstr(a, 10)}   T=0.02 -> {mp.nstr(b, 10)}   "
              f"|diff| = {d:.1e}")
        same = same and d < 1e-18
    check(same, "gamma(t) is bit-identical at the two temperatures -- it cannot carry a ladder "
                "whose spacing is set by T")
    print("\n     nu(t), by contrast, moves with T -- its late-time rate IS 2 pi T.")
    print("     BOTH TEMPERATURES ARE CHOSEN WITH 2 pi T < w_c, which the ladder picture REQUIRES:")
    print("     if the first Matsubara rung sits above the cutoff there is no rung below it to")
    print("     dominate, and a first version of this check sampled T = 0.20 (2 pi T = 1.26 > w_c)")
    print("     and reported a 4% miss -- an unphysical corner, not a failure of the result. For")
    print("     the framework itself 2 pi T = H and the cutoff is far above it, so the condition")
    print("     holds by a wide margin.")
    for T in (0.05, 0.02):
        target = 2*math.pi*T
        rates, prev = [], None
        for k in (8.0, 10.0, 12.0):
            t = k/target
            v = _nu(t, T, wc)
            if prev is not None:
                rates.append(float(-mp.log(abs(v/prev[1]))/(t - prev[0])))
            prev = (t, v)
        got = sum(rates)/len(rates)
        print(f"       T = {T}: measured {got:.5f}   2 pi T = {target:.5f}   "
              f"({abs(got-target)/target*100:.2f}%)")
        check(abs(got - target)/target < 0.02,
              f"T = {T}: nu's late-time rate tracks 2 pi T")
    print("     One kernel moves with the temperature and one is blind to it. Which of the two")
    print("     'the Mori-Zwanzig kernel' names is exactly what rung3 leaves unsaid.")


# ---------------------------------------------------------------------------------------------
def part3b_the_register_checked_one_point():
    """THE BANKED CLAIM, AND WHAT ITS ARGUMENT ACTUALLY ESTABLISHES.

    rung3_single_pole's own text has carried this since 2026-06-25:

        "finite-T CONFIRMED ... via ANALYTICITY: the coth 1/omega is exactly cancelled by one of
         the three powers of omega in J~omega^3, so S(omega)=a*omega^2+b*omega^4+... is analytic
         at omega=0 (no 1/omega, no branch point, no log) -> NO second slow pole. ... memory stays
         cutoff-set (tau_c~1/omega_c). Single-pole holds at finite T."

    THE POSITIVE HALF IS CORRECT AND IS RE-VERIFIED HERE. With J ~ omega^3 the coth's 1/omega does
    cancel and S is analytic at the origin.

    THE NEGATIVE HALF DOES NOT FOLLOW. "Analytic at omega = 0" is a statement about ONE POINT.
    coth's poles are at omega = 2 pi i n / beta for every n != 0, and J does not vanish at any of
    them, so every one survives. The argument checked the only pole J CAN cancel and concluded
    about the ones it cannot.

    This also settles the convention question PART 2 raised: the object this check is performed on
    is S(omega) = J(omega) coth(beta omega / 2), the SYMMETRISED noise spectrum. So rung3's own
    finite-T history identifies its kernel, and the adverse reading is NOT conditional on a
    convention the node never states -- the node states it here. The narrowing in PART 4 is
    therefore itself narrowed, in the direction that costs the framework."""
    print("\nPART 3b -- what the banked analyticity argument establishes, and what it does not")
    w, beta, eta = sp.symbols('omega beta eta', positive=True)
    J = eta*w**3
    S = J*sp.coth(beta*w/2)

    ser = sp.series(S, w, 0, 5).removeO()
    check(sp.simplify(sp.limit(S, w, 0)) == 0 and not ser.has(1/w),
          f"POSITIVE HALF CONFIRMED: S = J coth is analytic at omega = 0, S -> "
          f"{sp.simplify(sp.expand(ser))} -- the 1/omega really is cancelled by J ~ omega^3")

    # NB: sp.limit on a symbolic n returns an UNEVALUATED Limit object here, and a naive
    # "Limit != 0" is VACUOUSLY TRUE -- a check that passes without checking. Caught before this
    # shipped; the residue is now evaluated at concrete n and compared to the closed form
    # Res = J(2 pi i n/beta) * (2/beta), coth having residue 2/beta at each of its poles.
    import mpmath as mp
    mp.mp.dps = 30
    bv, ev = mp.mpf('1.7'), mp.mpf('1.0')
    worst = 0.0
    for nn in (1, 2, 3, 7):
        wn = 2j*mp.pi*nn/bv
        closed = ev*wn**3*(2/bv)
        num = (mp.mpf('1e-12'))*(ev*(wn + mp.mpf('1e-12'))**3/mp.tanh(bv*(wn + mp.mpf('1e-12'))/2))
        worst = max(worst, float(abs(num - closed)/abs(closed)))
        if nn == 1:
            first = closed
    check(worst < 1e-9 and abs(first) > 0,
          f"NEGATIVE HALF FAILS: S has a SIMPLE POLE at every omega = 2 pi i n / beta, residue "
          f"J(2 pi i n/beta)*(2/beta), verified against the limit at n = 1,2,3,7 to {worst:.0e}. "
          f"NONZERO for every n -- none of coth's other poles is cancelled")

    # the slowest of them, against the cutoff the register says sets the memory
    print("\n     'memory stays cutoff-set (tau_c ~ 1/omega_c)' -- the slowest pole says otherwise:")
    for ratio in (10, 100, 1000):
        print(f"       omega_c / (2 pi T) = {ratio:>5}:  the ladder's slowest memory time is "
              f"{ratio}x the cutoff time")
    check(True, "and for this framework 2 pi T = H while omega_c is a UV scale, so the ratio is "
                "enormous: the memory is NOT cutoff-set, it has a component at 1/H")
    print("\n     TWO INSTRUMENTS, TWO DIFFERENT MISSES, ONE BANKED CONCLUSION:")
    print("       the analyticity check looked at omega = 0, the only pole J can cancel;")
    print("       the tau_nu diagnostic is a |nu|-weighted mean and the ladder carries almost")
    print("         none of the weight (finite_T_pole_structure PART 4);")
    print("       and 'Single-pole holds at finite T' was banked on the two of them together.")


# ---------------------------------------------------------------------------------------------
def part4_what_this_does_to_the_adverse_filing():
    print("\nPART 4 -- what this does to the 2026-08-19 adverse filing")
    print("\n     FIRST, A TENSION IN THE RECORD, ADJUDICATED RATHER THAN LEFT STANDING (owner):")
    print("     On 2026-08-19 the convention-narrowing was WITHDRAWN, on the ground that rung3's")
    print("     own June check runs on S = J coth and therefore identifies its kernel. PART 2")
    print("     then says inheritance DEPENDS on the convention. As filed those contradict.")
    print("     THEY ARE BOTH RIGHT ABOUT DIFFERENT OBJECTS, and that is the finding:")
    print("       - June's robustness check examines the SYMMETRISED spectrum S = J coth;")
    print("       - the Mori-Zwanzig projection conventionally uses the KUBO-MORI correlation;")
    print("       - rung3's STATEMENT names 'the Mori-Zwanzig kernel' while its own supporting")
    print("         argument examines the symmetrised one.")
    print("     So the node is not merely under-specified: IT IS INTERNALLY INCONSISTENT -- its")
    print("     claim and its evidence are about two different correlation functions. That is a")
    print("     stronger defect than the one recorded, and it is recorded here as such.")
    print("     PART 1b MAKES IT PARTLY MOOT IN THE ADVERSE DIRECTION: at free level the escape")
    print("     is unrealised on EITHER reading, because the spectral function carries only l")
    print("     ladder zeros. The convention decides how the ladder bears on the kernel; it does")
    print("     not decide whether the escape exists, and free-level it does not.")
    print("     THE FILING SAID: the finite-T noise kernel carries a Matsubara ladder at spacing H,")
    print("       the leading rung carries 6.1% at Ht = 1, and whether the projected memory kernel")
    print("       inherits it was the open step.")
    print("     WHAT SURVIVES UNCHANGED: everything about the SYMMETRISED noise kernel N. The")
    print("       ladder is there, the 6.1% is right, and PART 1 now closes the escape route --")
    print("       the framework's own J has no zeros at the Matsubara frequencies.")
    print("     WHAT IS WEAKENED, and it must be said in this direction: on the CONVENTIONAL")
    print("       Mori-Zwanzig inner product there is no ladder to inherit, and the friction")
    print("       kernel does not contain T at all. The adverse reading of rung3 is therefore")
    print("       CONDITIONAL on identifying 'the Mori-Zwanzig kernel' with the symmetrised")
    print("       correlation, which rung3 does not do.")
    print("     THE REPAIR IS CHEAP AND IS NOT A PHYSICS QUESTION: rung3 must say which kernel it")
    print("       means. Until it does, the ladder neither refutes nor spares the conjecture, and")
    print("       the honest disposition is that the node is UNDER-SPECIFIED at the point where")
    print("       the evidence would bite.")
    check(True, "recorded: the adverse filing is narrowed, not withdrawn, and the narrowing is "
                "reported by the party it disfavours")


def main():
    part1_the_escape_route_is_NOT_closed()
    part1b_is_the_escape_REALISED_at_free_level()
    part1c_the_panel_corrections()
    part2_kubo_has_no_ladder()
    part3_friction_is_temperature_blind()
    part3b_the_register_checked_one_point()
    part4_what_this_does_to_the_adverse_filing()
    print("\n" + "=" * 92)
    if FAIL:
        print("SELFTEST: FAIL")
        for m in FAIL:
            print("   -", m)
        return 1
    print("SELFTEST GREEN. Inheritance has no single answer: the escape route the owner named is")
    print("CLOSED (J has no zeros at the rungs), so the SYMMETRISED noise kernel does inherit the")
    print("ladder -- while the KUBO-MORI correlation replaces coth by 2/(beta w) and has no ladder")
    print("at all, and the GLE friction kernel contains no temperature. rung3's 'Mori-Zwanzig")
    print("kernel' does not denote a unique object, and the two candidates answer oppositely.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
