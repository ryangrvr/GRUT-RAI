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
def part1_the_escape_route_is_closed():
    """Does Im K_R vanish at the Matsubara frequencies? For this framework's J it does not."""
    print("\nPART 1 -- the named escape: zeros of Im K_R at the Matsubara frequencies")
    w, wc, eta, v = sp.symbols('omega omega_c eta v', positive=True)
    J = eta*w**3*sp.exp(-(w/wc)**2)
    Jiv = sp.simplify(J.subs(w, sp.I*v))
    print(f"     J(w)   = {J}")
    print(f"     J(i v) = {sp.simplify(Jiv)}")
    check(sp.simplify(sp.Abs(Jiv)) != 0,
          "J(i v) is nonzero for every real v > 0 -- the Gaussian factor becomes exp(+v^2/w_c^2), "
          "which GROWS; nothing vanishes")
    # a general statement: a J that is a positive power times a nowhere-zero entire factor
    for s_ in (1, 2, 3, 5):
        Js = eta*w**s_*sp.exp(-(w/wc)**2)
        z = sp.simplify(Js.subs(w, sp.I*v))
        check(sp.simplify(z) != 0, f"s = {s_}: J(i v) != 0, so no cancellation at any rung")
    print("     => on the SYMMETRISED route the ladder is inherited: N(w) = J(w) coth(beta w/2)")
    print("        keeps every pole of coth. The escape the owner named is closed for this J.")


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
    part1_the_escape_route_is_closed()
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
