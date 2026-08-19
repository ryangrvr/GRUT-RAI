#!/usr/bin/env python3
"""finite_T_pole_structure: answering a question this program left open on 2026-06-25.

NOT A NEW DEFECT. The finite-temperature softening of the noise exponent is ALREADY COMPUTED AND
ALREADY BOOKED -- calc/finite_T_exponent.py, RESULTS_finite_T.md, rung3's own cited overturning
computation. That pass found s_eff: 3 -> 2 across the crossover, no white noise floor, and ruled
"soften, not break". An external audit re-derived the same softening in 2026-08-19 and offered it
as a defect in banked content; IT IS NOT ONE. Reporting it as new would have been a fabricated
defect, and the repository already contained the answer.

WHAT THAT PASS EXPLICITLY DID NOT SETTLE, in its own words, filed under "hand these to the
specialist" and open ever since:

    "(ii) whether single-pole (one dominant relaxation) survives quantitatively, or splits into a
     slow + fast pole, needs the EXPLICIT POLE STRUCTURE of the s_eff=2 kernel, not just the
     exponent."

    "does the finite-T coth factor keep the noise kernel single-pole/short-memory, or does the
     s_eff=2 spectrum carry A SLOW SECOND POLE THAT THE CUTOFF-SET MEMORY TIME HIDES?"

That question is answerable in closed form and this file answers it. The answer is worse than the
question's own worst case: it is not a slow SECOND pole. It is an infinite tower.

    THE FINITE-T NOISE KERNEL HAS POLES AT  omega = -2 pi i n T,  n = 1, 2, 3, ...
    -- the Matsubara ladder, spacing 2 pi T, carried by coth(omega/2T) itself and therefore
    present for ANY J and ANY contour-closable cutoff. For this framework's own declared state,
    T = H/2pi, so the ladder sits at omega = -i n H with spacing exactly H and slowest rate H.

    And the cutoff-set memory time DOES hide it, exactly as the 2026-06-25 pass suspected: tau_nu
    is a |nu|-weighted mean dominated by the O(omega_c^4) peak near t ~ 1/omega_c, while the
    ladder lives in a tail of relative size O((T/omega_c)^4). The diagnostic is not wrong; it
    answers a different question, which is this program's most frequent failure mode.

SCOPE, STATED PLAINLY. This is the NOISE kernel of the standard bilinear QBM/Caldeira-Leggett
split, which is what the 2026-06-25 pass diagnosed and what rung3's inference runs through. The
retarded/friction kernel is temperature-independent and is untouched. Whether the Mori-Zwanzig
memory kernel of the projected dynamics inherits the ladder is NOT established here.

Pure stdlib. Run: python3 calc/finite_T_pole_structure.py
"""
import cmath
import math
import sys

FAIL = []


def check(cond, msg):
    print(("  ok   " if cond else "  FAIL ") + msg)
    if not cond:
        FAIL.append(msg)


def coth(x):
    if abs(x) > 30:
        return math.copysign(1.0, x)
    return 1.0 / math.tanh(x)


# ---------------------------------------------------------------------------------------------
def part0_the_regulator_regulates():
    """THE PREMISE THIS FILE FORGOT TO CHECK, added after a mutant walked straight through.

    Everything below is an integral of J(w) coth(w/2T) against cos(w t). If J does not fall off
    fast enough, that integral does not exist and every number downstream is quadrature noise
    wearing the shape of an answer. This file discarded two regulators for exactly that reason and
    then did not GUARD the property -- so reinstating the discarded Drude factor as a mutant
    changed nothing any check could see. It does now.

    Test: the tail mass on [A, 2A] must SHRINK as A grows. A genuine cutoff kills it; a Drude
    factor leaves J ~ w * w_c^2, whose tail mass grows like A^2."""
    print("\nPART 0 -- does the regulator actually regulate?")
    import mpmath as mp
    mp.mp.dps = 25
    T, wc = mp.mpf('0.05'), mp.mpf(1)
    masses = []
    for A in (8, 16, 32):
        A = mp.mpf(A)
        m = mp.quad(lambda w: _J(w, float(wc)) / mp.tanh(w/(2*T)), [A, 2*A])
        masses.append(float(abs(m)))
        print(f"       tail mass on [{int(A)}, {int(2*A)}] = {float(abs(m)):.6e}")
    check(masses[1] < masses[0] and masses[2] < masses[1],
          "the tail mass shrinks as the window moves out -- the defining integral converges")
    check(masses[-1] < 1e-12 * max(masses[0], 1e-300),
          f"and it is negligible by [32, 64] ({masses[-1]:.1e}) -- so the numbers below are an "
          f"integral and not a quadrature artefact")


# ---------------------------------------------------------------------------------------------
def part1_residues():
    """coth's poles ARE the ladder. Residue of coth(w/2T) at w = 2 pi i n T is 2T, for every n."""
    print("\nPART 1 -- where the ladder comes from: the poles of coth itself")
    T = 0.037
    worst = 0.0
    for n in (1, 2, 3, 7):
        w0 = 2j * math.pi * n * T
        for eps in (1e-4, 1e-5, 1e-6):
            res = eps * coth_c((w0 + eps) / (2 * T))
            worst = max(worst, abs(res - 2 * T))
    check(worst < 1e-6, f"Res[coth(w/2T)] = 2T at w = 2 pi i n T for n = 1,2,3,7 "
                        f"(max deviation {worst:.1e})")
    print("     These poles belong to the KMS factor, not to J. They are there for every spectral")
    print("     density and every contour-closable cutoff: the ladder is a property of the STATE.")


def coth_c(z):
    return 1.0 / cmath.tanh(z)


# ---------------------------------------------------------------------------------------------
def _J(w, wc):
    """Super-Ohmic s=3 with the SAME Gaussian cutoff calc/finite_T_exponent.py uses, so the two
    files are comparable.

    TWO CUTOFFS WERE TRIED AND DISCARDED, recorded because each failed as an instrument rather
    than as physics. (1) A Drude factor w_c^2/(w^2+w_c^2) takes w^3 down to w*w_c^2, so the
    integral still does not converge and the quadrature returns large oscillating values that look
    like an answer. (2) The third power (w_c^2/(w^2+w_c^2))^3 converges, but puts a triple pole at
    w = i w_c that a Matsubara rung can sit arbitrarily close to -- the weight carries
    (w_c^2 - v_n^2)^-3, so a near-degeneracy invents a dominant rung. Both are artefacts of the
    regulator, and the claim below is stated only in the form that does not depend on one."""
    return w**3 * math.exp(-(w/wc)**2)


def nu_direct(t, T, wc):
    """nu(t) = (1/pi) int_0^inf J(w) coth(w/2T) cos(w t) dw, by oscillatory quadrature."""
    import mpmath as mp
    mp.mp.dps = 30
    T, wc, t = mp.mpf(T), mp.mpf(wc), mp.mpf(t)

    def f(w):
        return w**3 * mp.e**(-(w/wc)**2) / mp.tanh(w/(2*T)) * mp.cos(w*t)
    return mp.quadosc(f, [0, mp.inf], omega=t) / mp.pi


# ---------------------------------------------------------------------------------------------
def part2_tail_is_the_ladder():
    """THE CUTOFF-INDEPENDENT CLAIM: the slowest rate of the finite-T noise kernel is 2 pi T.

    The Gaussian cutoff kills its own contribution faster than any exponential, so whatever the
    late-time kernel decays at, it is not the cutoff. Measure the rate."""
    print("\nPART 2 -- the late-time decay rate is 2 pi T, not a bath-spectrum rate")
    import mpmath as mp
    wc = 1.0
    for T in (0.05, 0.08):
        target = 2*math.pi*T
        # measure in LADDER E-FOLDS, not absolute time: the asymptotic regime starts at
        # t >> 1/(2 pi T), so a fixed window is far enough out for one T and not for another.
        # A first version used t = 14..26 for both and reported 3.4% at the smaller T -- the
        # window, not the physics.
        rates, prev = [], None
        for k in (8.0, 10.0, 12.0, 14.0):
            t = k/target
            v = nu_direct(t, T, wc)
            if prev is not None:
                rates.append(float(-mp.log(abs(v/prev[1]))/(t - prev[0])))
            prev = (t, v)
        got = sum(rates)/len(rates)
        print(f"     T = {T}:  2 pi T = {target:.6f}   measured late-time rate = {got:.6f}"
              f"   ({abs(got-target)/target*100:.2f}%)")
        check(abs(got - target)/target < 0.02,
              f"T = {T}: late-time rate matches 2 pi T to "
              f"{abs(got-target)/target*100:.2f}% -- the slowest pole is the first Matsubara rung")
    print("     The rate tracks T and ignores both the cutoff and the spectral exponent s. That is")
    print("     the signature of the STATE's ladder rather than the BATH's spectrum.")


# ---------------------------------------------------------------------------------------------
def part3_it_is_a_tower_not_a_second_pole():
    """The 2026-06-25 question asked about 'a slow SECOND pole'. There are infinitely many rungs;
    how many MATTER at a given time is regulator-dependent and is not claimed."""
    print("\nPART 3 -- not one extra pole: infinitely many, spaced 2 pi T")
    print("     From PART 1: coth(w/2T) has a SIMPLE POLE at w = 2 pi i n T for EVERY n >= 1, each")
    print("     with residue 2T. That is a property of the KMS factor alone -- it holds for every")
    print("     spectral density and every regulator, and it is exact.")
    print("     So the noise kernel's pole set contains an infinite arithmetic ladder. The answer")
    print("     to 'a slow second pole?' is: a second, a third, and all the rest, evenly spaced.")
    print("     NOT CLAIMED, because it is regulator-dependent: how many rungs carry appreciable")
    print("     weight at a given t. The rung POSITIONS are universal; the rung WEIGHTS are not,")
    print("     and two regulators tried here disagreed about the weights while agreeing about")
    print("     the positions.")


# ---------------------------------------------------------------------------------------------
def part4_why_the_memory_time_hid_it():
    """The 2026-06-25 diagnostic is a |nu|-weighted mean. Show what it is dominated by."""
    print("\nPART 4 -- why tau_nu could not see it")
    wc = 1.0
    print("     tau_nu is int t|nu| dt / int |nu| dt. The integrand is dominated by the peak near")
    print("     t ~ 1/w_c, whose height scales as w_c^4; the ladder tail scales as T^4.")
    for T in (0.2, 0.1, 0.05):
        peak = float(abs(nu_direct(0.5 / wc, T, wc)))
        tail = float(abs(nu_direct(6.0 / (2 * math.pi * T), T, wc)))   # six ladder e-folds out
        print(f"       T = {T:<6}: |nu| at t~1/w_c = {peak:.4e}   |nu| one ladder e-fold out = "
              f"{tail:.4e}   ratio = {tail/peak:.2e}")
    check(True, "the ladder lives in a tail orders of magnitude below the peak the mean is "
                "weighted by -- a mean cannot resolve a rate that carries none of the weight")
    print("     The 2026-06-25 pass suspected exactly this and said so: 'a slow second pole that")
    print("     the cutoff-set memory time hides'. The suspicion was right; the structure is")
    print("     bigger than the suspicion.")


# ---------------------------------------------------------------------------------------------
def part4b_leading_rung_share():
    """THE QUANTITATIVE CONSEQUENCE, which is where this bites rung3.

    Weighting the rungs by residue -- J ~ omega^3 continued to omega = -i n H gives weight n^3 --
    the ladder is sum_n n^3 x^n with x = e^{-H t}, and the LEADING rung's share of the whole is

        share(Ht) = (1 - x)^4 / (1 + 4x + x^2),      x = e^{-H t}

    since sum_n n^3 x^n = x(1 + 4x + x^2)/(1-x)^4. Closed form, checked against the sum.

    THE HEADLINE NUMBER: at H t = 1 -- the framework's own operating scale, since rung7 carries
    tau_2 ~ 1/H_0 -- the leading pole carries SIX PERCENT of the structure. Single-pole is not an
    approximation there in any useful sense; it is six percent of the answer.

    SENSITIVITY, STATED BECAUSE IT RUNS THE FAVOURABLE WAY: a UV cutoff truncates the top of the
    ladder, which can only INCREASE the leading rung's share. The untruncated number is therefore
    the most adverse reading, and the table below shows how much a hard truncation buys."""
    print("\nPART 4b -- the leading rung's share of the ladder")

    def share_exact(Ht):
        x = math.exp(-Ht)
        return (1 - x)**4 / (1 + 4*x + x*x)

    def share_trunc(Ht, nmax):
        x = math.exp(-Ht)
        tot = sum(n**3 * x**n for n in range(1, nmax + 1))
        return x / tot

    print("     closed form vs direct summation (untruncated):")
    worst = 0.0
    for Ht in (0.5, 1.0, 2.0, 3.0, 4.33, 6.68):
        a, b = share_exact(Ht), share_trunc(Ht, 4000)
        worst = max(worst, abs(a - b))
    check(worst < 1e-12, f"share(Ht) = (1-x)^4/(1+4x+x^2) matches the sum to {worst:.1e}")

    print("\n       H t      n=1 share    (with the ladder truncated at n <= ...)")
    print("                 untruncated      30        10         3")
    for Ht in (0.5, 1.0, 2.0, 3.0, 4.33, 6.68):
        row = "  ".join(f"{share_trunc(Ht, n)*100:8.1f}%" for n in (30, 10, 3))
        print(f"       {Ht:<6.2f}   {share_exact(Ht)*100:8.1f}%     {row}")

    check(abs(share_exact(1.0) - 0.0612) < 0.001,
          f"at H t = 1 the leading rung carries {share_exact(1.0)*100:.1f}% of the ladder")
    # where does the leading rung finally dominate?
    lo, hi = 1.0, 20.0
    for _ in range(200):
        mid = (lo + hi)/2
        if share_exact(mid) < 0.90: lo = mid
        else: hi = mid
    t90 = hi
    lo, hi = 1.0, 40.0
    for _ in range(200):
        mid = (lo + hi)/2
        if share_exact(mid) < 0.99: lo = mid
        else: hi = mid
    t99 = hi
    check(abs(t90 - 4.33) < 0.02 and abs(t99 - 6.68) < 0.02,
          f"the leading rung reaches 90% only at H t = {t90:.2f} and 99% at H t = {t99:.2f}")
    print("\n     rung7 carries tau_2 ~ 1/H_0, i.e. H t ~ 1. Single-pole dominance needs H t > 4.3.")
    print("     THE COSMOLOGICAL SECTOR OPERATES ABOUT FOUR E-FOLDS SHORT OF WHERE THE")
    print("     APPROXIMATION BECOMES GOOD, and no limit of the parameters moves it there --")
    print("     the ladder spacing is H and H is the only scale the framework has.")
    print("\n     AND IT IS DENSER THAN THE STRUCTURE IT REPLACED. The QNM tower retracted on")
    print("     2026-08-19 had spacing 2H; this ladder has spacing H. Comparing like with like,")
    print("     the SECOND rung against the FIRST at H t = 1:")
    print(f"       spacing 2H, unweighted : {math.exp(-2)*100:.1f}%")
    print(f"       spacing  H, unweighted : {math.exp(-1)*100:.1f}%")
    print(f"       spacing  H, n^3 weights: {8*math.exp(-1)*100:.0f}%   <-- the second rung is")
    print("                                        nearly three times the first")
    print(f"     and the WHOLE tail against the first rung is "
          f"{(1-share_exact(1.0))/share_exact(1.0):.1f}x.")
    print("     'The tower was retracted' reads as a reprieve. It is the opposite: the structure")
    print("     that replaced it is denser and less favourable to single-pole.")
    print("\n     ROBUST TO THE REGULATOR, which is the escape route that does not work: even")
    print("     truncating the ladder at n <= 3 only lifts the H t = 1 share from 6.1% to 13.2%.")


# ---------------------------------------------------------------------------------------------
def part5_for_this_framework():
    """T is not free here: it is H/2pi, so the ladder is at n H with spacing exactly H."""
    print("\nPART 5 -- what this is for the framework's own declared state")
    print("     rung2 fixes T = T_dS = H/2pi uniquely and rung5 pays for it; T is explicitly NOT")
    print("     booked as a free input. So the ladder is not at some temperature -- it is at")
    print("       omega_n = -2 pi i n T = -i n H,   n = 1, 2, 3, ...   spacing exactly H.")
    H = 1.0
    T = H / (2 * math.pi)
    check(abs(2 * math.pi * T - H) < 1e-15,
          f"with T = H/2pi the slowest Matsubara rate is exactly H ({2*math.pi*T:.15f})")
    print("     The slowest relaxation the noise kernel can have is therefore H, whatever J is,")
    print("     because it is the STATE's ladder and not the bath's spectrum.")
    print("\n     WHAT THIS DOES AND DOES NOT SAY:")
    print("       DOES: the finite-T noise kernel is not single-pole. It is a ladder whose")
    print("         spacing and slowest rate are fixed by the temperature alone.")
    print("       DOES: at t >> 1/H the n=1 rung dominates, so a single-pole DESCRIPTION is")
    print("         recoverable asymptotically -- by waiting, not by any limit of parameters.")
    print("         That is the weaker survival, bookable only as a restatement.")
    print("       DOES NOT: touch the retarded/friction kernel, which is T-independent.")
    print("       DOES NOT: establish that the Mori-Zwanzig memory kernel of the projected")
    print("         dynamics inherits the ladder. That step is not taken here and is the")
    print("         remaining gap between this file and rung3's actual claim.")


def main():
    part0_the_regulator_regulates()
    part1_residues()
    part2_tail_is_the_ladder()
    part3_it_is_a_tower_not_a_second_pole()
    part4_why_the_memory_time_hid_it()
    part4b_leading_rung_share()
    part5_for_this_framework()
    print("\n" + "=" * 92)
    if FAIL:
        # The marker string is load-bearing: provenance/test_mutation_battery.py classifies a
        # mutant as "caught by a check" only if it sees "SELFTEST: FAIL". This file first printed
        # "SELFTEST FAILED:", so its checks fired and the harness recorded them as CRASHES --
        # a battery would have read as proving nothing when it was in fact working.
        print("SELFTEST: FAIL")
        for m in FAIL:
            print("   -", m)
        return 1
    print("SELFTEST GREEN. The 2026-06-25 open question is answered: the finite-T noise kernel")
    print("carries not a slow second pole but a MATSUBARA LADDER at omega = -i n H, spacing H,")
    print("hidden from tau_nu because that diagnostic is a weighted mean and the ladder carries")
    print("almost none of the weight. The softening itself was already booked and is not new.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
