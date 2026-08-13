#!/usr/bin/env python3
"""rung3_spectral_structure: the QUANTITATIVE form of rung3's earned-under-determined disposition.

CLAIM (default-BROKEN): the spine test banked that the de Sitter secular growth is CHANNEL-DEPENDENT
(spin-0 potentials Psi,Phi grow ~ ln a; the TT graviton mode function is FROZEN at one loop). Feed that
channel-resolved input through the exact secular-envelope -> low-omega-singularity dictionary and read
off rho(omega)=2 Im G_R(omega) channel by channel. The claim to test: the branch-cut (Class-B) signal
lives in the SPIN-0 channel (a specific non-integrable low-omega singularity) -- NOT the TT channel that
G_R^TT probes; the TT channel is frozen at O(G), carries no such singularity, and its leading dissipation
is O(G^2)~G^2 H^5 -- too weak for the current (un-resummed, O(G), simplest-gauge) computation to settle.
So "earned under-determined" becomes DERIVED: the channel that carries the cut-signal is the wrong one,
and the right channel's dissipation is a higher-order effect below the current resolution.

This does NOT resolve rung3. It stays derived-pending, ledger 0. It derives the quantitative FORM of the
under-determination, not the transport class.

TOY / SCALING. It models responses by their late-time secular ENVELOPES; it is NOT the rigorous
tensor / gauge-invariant self-energy result. Every physical claim inherits: (toy/scaling), (channel
inputs = banked spine-test finding, leading-order/simplest-gauge), (O(G), un-resummed). The single
easiest over-claim -- "frozen TT -> analytic -> Class A" (or "-> Class B") -- is FENCED: frozen at O(G)
means SILENT at O(G) (no distinguishing singularity), not analytic. Both horns stay live.

Refs: spin-0 ~ ln a secular growth (TTW-type, arXiv:2405.00116); TT frozen (Tan-Tsamis-Woodard,
arXiv:2103.08547); null-collision Gamma~G^2 H^5 (banked rung3). Pure stdlib. Strictly v5 register.
"""
import cmath
import math

EULER_GAMMA = 0.5772156649015329


# --------------------------------------------------------------------------------------------------
# Part A -- the spectral dictionary (general, exact).
#
# A causal retarded response G_R(t) (t>=0) whose late-time envelope grows as t^p has the regulated
# one-sided Laplace/Fourier transform
#       G~_R(omega) = int_0^inf dt t^p e^{(i omega - eps) t} = Gamma(p+1) / (eps - i omega)^{p+1},
# and the spectral density rho(omega) = 2 Im G~_R(omega). The eps->0 limit gives the dictionary:
#       rho(omega->0) = 2 Gamma(p+1) sin((p+1) pi/2) * omega^{-(p+1)}          (non-integer p),
# with the integer-p cases (sin = 0) turning into delta-derivative distributions concentrated at 0.
# --------------------------------------------------------------------------------------------------

def laplace_powerlaw(p, w, eps):
    """Exact regulated transform of the envelope t^p: Gamma(p+1)/(eps - i w)^{p+1}."""
    return math.gamma(p + 1.0) / (eps - 1j * w) ** (p + 1.0)


def transform_numeric(p, w, eps, T=120.0, N=24000):
    """Simpson quadrature of int_0^T dt t^p e^{(i w - eps) t} -- to confirm the closed form."""
    if N % 2:
        N += 1
    h = T / N
    total = 0j
    for i in range(N + 1):
        t = i * h
        val = (t ** p) * cmath.exp((1j * w - eps) * t)
        weight = 1.0 if (i == 0 or i == N) else (4.0 if i % 2 else 2.0)
        total += weight * val
    return total * h / 3.0


def rho_powerlaw(p, w, eps):
    """rho(omega) = 2 Im G~_R for the t^p envelope."""
    return 2.0 * laplace_powerlaw(p, w, eps).imag


def transform_lnt(w, eps):
    """Exact regulated transform of the ln(t) envelope: -(gamma + ln(eps - i w))/(eps - i w)."""
    s = eps - 1j * w
    return -(EULER_GAMMA + cmath.log(s)) / s


def rho_lnt(w, eps):
    return 2.0 * transform_lnt(w, eps).imag


def dictionary_entry(p):
    """Analytic low-omega form for envelope t^p. Returns (exponent, coeff, kind, note)."""
    coeff = 2.0 * math.gamma(p + 1.0) * math.sin((p + 1.0) * math.pi / 2.0)
    exponent = -(p + 1.0)
    integer_p = abs(p - round(p)) < 1e-12 and p >= 0
    if integer_p and abs(coeff) < 1e-9:
        # sin((n+1)pi/2)=0 -> the power-law piece is a principal value; the SPECTRAL WEIGHT is a
        # delta-derivative delta^{(n)}(omega) concentrated at omega=0 (a non-decaying / ballistic mode).
        n = int(round(p))
        return (exponent, coeff, "delta-derivative",
                "rho ~ delta^{(%d)}(omega): weight pinned at omega=0 (non-decaying/ballistic)" % n)
    return (exponent, coeff, "power-law",
            "rho ~ %.4f * omega^{%.1f}" % (coeff, exponent))


# --------------------------------------------------------------------------------------------------
# Report
# --------------------------------------------------------------------------------------------------

def part_A():
    print("\n" + "=" * 92)
    print("PART A -- the spectral dictionary  rho(omega->0) = 2 Im int_0^inf dt e^{i omega t} G_R(t)")
    print("=" * 92)
    print(" envelope t^p        low-omega rho(omega)                       kind")
    print(" " + "-" * 80)
    for p, label in ((0.0, "p=0  constant/bounded"),
                     (0.5, "p=0.5  (generic frac.)"),
                     (1.0, "p=1  linear  (= ln a)"),
                     (2.0, "p=2  quadratic")):
        exponent, coeff, kind, note = dictionary_entry(p)
        print(" %-19s %-40s %s" % (label, note, kind))
    print(" ln(t)               rho ~ -2(gamma + ln omega)/omega ~ |ln omega|/omega   log-power")
    print("\n INTEGRABILITY at omega->0 (int_0 rho domega):  p<0 integrable; p=0 marginal (1/omega,")
    print("   log-divergent); p>=1 NON-integrable -> a free-streaming / non-decaying-mode signal. The")
    print("   distributional delta-derivative arises for ODD integer p (sin=0); even integers and non-")
    print("   integers give ordinary (though possibly non-integrable) power laws. The dictionary is the")
    print("   exact, computable core object.")
    print("\n PASSIVITY CAVEAT (the map is a FORMAL scaling transform, not a passive-response guarantee):")
    print("   a causal PASSIVE response obeys omega*rho(omega) >= 0 (KMS / 2nd law). That holds for p<=1")
    print("   (p=0: omega*rho=2>0; p=1: delta'-weight pinned at 0). For p>=2 the transform is SIGN-")
    print("   INDEFINITE (p=2: rho~-4/omega^3 -> omega*rho<0) -- a GROWING/UNSTABLE mode, NOT a passive")
    print("   dissipative response. So only p<=1 entries carry a direct passive-response reading; the")
    print("   physics application below uses only p=1 (spin-0) and the frozen TT channel -- both fine.")

    print("\n NUMERIC CONFIRMATION (Simpson quadrature vs closed form Gamma(p+1)/(eps-i omega)^{p+1}):")
    eps = 0.3
    for p in (0.0, 1.0, 2.0):
        for w in (0.3, 0.7):
            num = transform_numeric(p, w, eps)
            ana = laplace_powerlaw(p, w, eps)
            rel = abs(num - ana) / abs(ana)
            print("   p=%.0f w=%.1f  numeric=% .4f%+.4fj  closed=% .4f%+.4fj  rel.err=%.2e"
                  % (p, w, num.real, num.imag, ana.real, ana.imag, rel))


def part_B():
    print("\n" + "=" * 92)
    print("PART B -- apply the dictionary channel by channel  (inputs = banked spine-test finding,")
    print("          leading-order / simplest-gauge; TOY/SCALING)")
    print("=" * 92)

    print("\n TT / spin-2 channel (GRUT's transport object rho_TT = 2 Im G_R^TT) -- THE DERIVED CONTENT:")
    print("   mode function FROZEN at O(G) (no secular envelope) -> NO secular-growth singularity in")
    print("   rho_TT at O(G) -> the leading O(G) TT dissipation VANISHES -> eta_TT = O(G^2) or higher.")
    print("   FENCE (the single easiest over-claim): 'frozen at O(G)' = SILENT at O(G) (no distinguishing")
    print("   singularity), NOT 'analytic / Class A' AND NOT 'Class B'. A frozen mode is equally")
    print("   consistent with a razor-thin O(G^2) pole OR with a trivial no-response -- both horns live.")

    print("\n SPIN-0 channel (potentials Psi,Phi) -- a WRONG-CHANNEL check, not a cut-establishment:")
    print("   grow ~ ln a = H t (TTW-type, arXiv:2405.00116).")
    print("   SCALING ASSUMPTION (toy, load-bearing): TAKE the field/correlator secular envelope ~ ln a")
    print("   as the retarded-response envelope; ln a is LINEAR in cosmic time (a=e^{Ht}) -> p=1.")
    dictionary_entry(1.0)  # p=1 -> delta'(omega) (odd integer)
    print("   IF one takes that bare envelope at FACE VALUE and runs the dictionary -> rho ~ delta'(omega)")
    print("   (non-integrable, weight pinned at 0; the '1/omega^2' gloss is loose). One might call it")
    print("   'Class-B-like' -- BUT this face-value continuation is EXACTLY the secular-log=>cut shortcut")
    print("   the register's 3rd/symmetric correction RETRACTED: the real omega->0 continuation of the")
    print("   ASSEMBLED object has NOT been done, so the secular log establishes NO cut. AND it is the")
    print("   WRONG CHANNEL (not what G_R^TT probes). So the naive signal, even at face value, sits in")
    print("   the wrong channel and says NOTHING about rho_TT.")


def part_C():
    print("\n" + "=" * 92)
    print("PART C -- order-counting coherence check (NOT a precise eta)")
    print("=" * 92)
    print("   frozen-TT at O(G)              =>  leading TT dissipation eta_TT is O(G^2) or higher")
    print("   banked null-collision estimate =>  Gamma ~ G^2 H^5  (also O(G^2); dim/order-of-magnitude,")
    print("                                      NOT a computed rate)")
    print("   -> BOTH say the TT dissipation is a G^2 effect, extraordinarily weak. The pole-vs-cut")
    print("      distinction (a razor-thin Lorentzian of width ~Gamma~G^2 H^5  vs  a free-streaming")
    print("      branch cut) lives at O(G^2) -- BELOW the resolution of the current O(G), un-resummed,")
    print("      simplest-gauge computation. Consistency at leading nonzero order (both ~G^2) is the")
    print("      coherence check; it is NOT a computation of eta and does NOT pick a horn.")


def main():
    print("=" * 92)
    print("rung3 SPECTRAL STRUCTURE -- quantitative form of earned-under-determined (default-BROKEN, TOY)")
    print("=" * 92)
    part_A()
    part_B()
    part_C()

    print("\n" + "=" * 92)
    print("VERDICT (default-BROKEN, honest; TOY/SCALING; does NOT graduate rung3):")
    print("=" * 92)
    print("  DERIVED (quantitative form of earned-under-determined) -- carried by the TT channel:")
    print("   1. The TT channel (GRUT's transport object) is FROZEN at O(G): no low-omega growth-")
    print("      singularity; its leading dissipation is O(G^2) or higher ~ G^2 H^5, consistent at")
    print("      leading nonzero order with the null-collision estimate.")
    print("   2. So the pole-vs-cut fork sits at O(G^2), a RAZOR'S EDGE below the current O(G) resolution")
    print("      -- 'under-determined' is now DERIVED (quantitatively located), not asserted.")
    print("   3. WRONG-CHANNEL check: the spin-0 ln-a growth, taken at face value (the shortcut the 3rd")
    print("      correction RETRACTED -> establishes NO cut), would map to a non-integrable delta'(omega)")
    print("      -- but that is the WRONG channel (not what G_R^TT probes) and says nothing about rho_TT.")
    print("  FENCES (both directions):")
    print("   - TOY/SCALING: envelopes only; NOT the tensor/gauge-invariant self-energy. Every claim.")
    print("   - Channel inputs (spin-0 secular, TT frozen) = banked spine-test finding, LO/simplest-gauge;")
    print("     if the true growth differs (e.g. mixed ln(aHr) terms) the channel assignment shifts --")
    print("     report the ambiguity, do not paper it.")
    print("   - Frozen-TT does NOT collapse to Class A OR Class B. Silent at O(G); both horns live.")
    print("   - rung3 STAYS derived-pending, ledger 0. This derives the FORM, not the class.")

    ok = _selftest()
    print("\n  SELFTEST: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


# --------------------------------------------------------------------------------------------------
# Test -- verify the dictionary transforms and their omega->0 limits.
# --------------------------------------------------------------------------------------------------

def _selftest():
    ok = True

    # (1) numeric transform reproduces the closed form (the dictionary's core object).
    for p in (0.0, 1.0, 2.0):
        for w in (0.3, 0.7):
            num = transform_numeric(p, w, 0.3)
            ana = laplace_powerlaw(p, w, 0.3)
            if abs(num - ana) / abs(ana) > 2e-3:
                print("   [FAIL] transform p=%.0f w=%.1f rel.err too large" % (p, w)); ok = False

    # (2) p=0 -> rho -> 2/omega as eps->0 (at fixed omega).
    w = 0.3
    if abs(rho_powerlaw(0.0, w, 3e-3) - 2.0 / w) / (2.0 / w) > 1e-2:
        print("   [FAIL] p=0 does not approach 2/omega"); ok = False

    # (3) generic non-integer p: rho ~ omega^{-(p+1)} -- check the log-log slope for p=0.5.
    p = 0.5
    ws = [0.05, 0.4]
    rr = [rho_powerlaw(p, x, 1e-4) for x in ws]
    slope = (math.log(rr[1]) - math.log(rr[0])) / (math.log(ws[1]) - math.log(ws[0]))
    if abs(slope - (-(p + 1.0))) > 2e-2:
        print("   [FAIL] p=0.5 slope %.3f != %.3f" % (slope, -(p + 1.0))); ok = False

    # (4) p=1 -> delta'(omega): int rho_eps(omega) g(omega) domega -> +2 pi g'(0), g(w)=sin w e^{-w^2},
    #     g'(0)=1. Signature = positive, monotone-increasing in |I| as eps->0, approaching 2 pi from
    #     below (never overshooting) -- the ballistic delta-derivative, distinct from any power law.
    def g(x):
        return math.sin(x) * math.exp(-x * x)

    def integ(eps, L=10.0, Nn=40000):
        h = 2 * L / Nn
        s = 0.0
        for i in range(Nn + 1):
            x = -L + i * h
            weight = 1.0 if (i == 0 or i == Nn) else (4.0 if i % 2 else 2.0)
            s += weight * rho_powerlaw(1.0, x, eps) * g(x)
        return s * h / 3.0

    vals = [integ(e) for e in (0.2, 0.1, 0.05, 0.03)]
    two_pi = 2.0 * math.pi
    monotone = all(vals[i] < vals[i + 1] for i in range(len(vals) - 1))
    positive = all(v > 0 for v in vals)
    approaches = 0.85 * two_pi < vals[-1] < 1.02 * two_pi
    if not (monotone and positive and approaches):
        print("   [FAIL] p=1 delta'-signature: vals=%s (2pi=%.3f)" % (vals, two_pi)); ok = False

    # (5) ln t -> rho ~ -2(gamma + ln omega)/omega.
    for w in (0.05, 0.2):
        approx = -2.0 * (EULER_GAMMA + math.log(w)) / w
        if abs(rho_lnt(w, 1e-5) - approx) / abs(approx) > 1e-2:
            print("   [FAIL] ln t at w=%.2f" % w); ok = False

    return ok


if __name__ == "__main__":
    raise SystemExit(main())
