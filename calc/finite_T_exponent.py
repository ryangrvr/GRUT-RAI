#!/usr/bin/env python3
"""KILL-SHOT #1: does finite temperature break single-pole?

The single-pole graduation rests on: omega = c|k| massless fast modes
=> DOS ~ omega^2 => spectral density J(omega) ~ omega^3 (s=3 super-Ohmic)
=> short memory => single (Markovian-like) pole.

  # AUTHORITY-VOCABULARY ANNOTATION 2026-08-12: 'specialist' here is an IN-HOUSE AI pass,
  # not an outside human. No outside human has ever been contacted by this program.
  # Annotated, not renamed -- see provenance/prereg/RESULT_AUTHORITY_TERMS_2026-08-12.txt
The specialist's worry: the FDT/KMS thermal factor coth(hbar*omega/2kT) ~ 2kT/(hbar*omega)
at low frequency multiplies the *noise* spectrum down by one power of omega, softening
the effective exponent and possibly restoring LONG memory in the regime that counts.

This script does the standard open-systems (Caldeira-Leggett / QBM) calculation and asks,
honestly, where it lands. Units hbar = k_B = omega_c = 1. Pure stdlib.

Two kernels must be kept distinct:
  * FRICTION / damping kernel gamma(t): set by J(omega)/omega, TEMPERATURE-INDEPENDENT.
  * NOISE kernel nu(t): symmetrized noise S(omega,T) = J(omega) coth(omega/2T), T-DEPENDENT.
The single-pole / memory question is about the noise kernel, since that is what drives
the observable decoherence and the w(z) response. We diagnose it three ways:
  (1) effective local exponent s_eff(omega) = d ln S / d ln omega,
  (2) the DC noise floor S(omega->0)  [nonzero floor == long memory],
  (3) the noise memory time tau_nu(T)  [does it diverge with T, or stay ~1/omega_c?].
"""
import math

WC = 1.0          # UV cutoff (units of omega_c)
ETA = 1.0         # coupling normalization


def coth(x):
    ax = abs(x)
    if ax == 0:
        return math.inf
    if ax > 20:
        return math.copysign(1.0, x)
    if ax < 1e-8:
        return 1.0 / x
    return 1.0 / math.tanh(x)


def J(w):
    """Super-Ohmic s=3 spectral density with a smooth Gaussian UV cutoff."""
    return ETA * w ** 3 * math.exp(-(w / WC) ** 2)


def S(w, T):
    """Symmetrized (Keldysh) noise spectrum, FDT/KMS-locked."""
    if T <= 0:
        return J(w)                       # zero-T limit: coth(omega/0+) -> 1 for omega>0
    return J(w) * coth(w / (2.0 * T))


def s_eff(w, T, h=1e-4):
    """Local logarithmic slope d ln S / d ln omega."""
    w1, w2 = w * (1 - h), w * (1 + h)
    s1, s2 = S(w1, T), S(w2, T)
    return (math.log(s2) - math.log(s1)) / (math.log(w2) - math.log(w1))


def noise_kernel_memory_time(T, wmax=8.0, nw=4000, tmax=25.0, nt=240):
    """tau_nu = <t> weighted by |nu(t)|, with nu(t) = (1/pi) int S(omega) cos(omega t) domega."""
    dw = wmax / nw
    ws = [(i + 0.5) * dw for i in range(nw)]
    Ss = [S(w, T) for w in ws]
    num = den = 0.0
    prev_t = 0.0
    abs_nu_prev = None
    dt = tmax / nt
    for j in range(nt + 1):
        t = j * dt
        acc = 0.0
        for w, sw in zip(ws, Ss):
            acc += sw * math.cos(w * t)
        nu = acc * dw / math.pi
        a = abs(nu)
        # trapezoid accumulation of int|nu|dt and int t|nu|dt
        if abs_nu_prev is not None:
            num += 0.5 * (prev_t * abs_nu_prev + t * a) * dt
            den += 0.5 * (abs_nu_prev + a) * dt
        abs_nu_prev = a
        prev_t = t
    return num / den if den > 0 else float("nan")


def main():
    print("=" * 78)
    print("KILL-SHOT #1  finite-T spectral exponent   (hbar = kB = omega_c = 1)")
    print("J(omega) = omega^3 exp(-(omega/omega_c)^2)   [s = 3 super-Ohmic]")
    print("S(omega,T) = J(omega) coth(omega/2T)   [FDT/KMS-locked noise]")
    print("=" * 78)

    Ts = [1e-3, 0.1, 1.0, 10.0, 100.0]
    probes = [1e-3, 1e-2, 1e-1, 5e-1]

    print("\n(1) effective local exponent s_eff(omega) = d lnS / d ln omega")
    print("    crossover expected at omega* = 2T  (coth ~ 2T/omega below it)")
    header = "      T       omega*=2T " + "".join(f"  s_eff(w={p:<6g})" for p in probes)
    print(header)
    ir_exp = {}
    for T in Ts:
        row = f"  {T:9.3g}  {2*T:9.3g}  "
        vals = []
        for p in probes:
            vals.append(s_eff(p, T))
        row += "".join(f"   {v:11.3f}" for v in vals)
        print(row)
        # IR plateau exponent: slope between the two smallest probes
        ir_exp[T] = (math.log(S(probes[1], T)) - math.log(S(probes[0], T))) / \
                    (math.log(probes[1]) - math.log(probes[0]))

    print("\n(2) DC noise floor  S(omega->0)   [nonzero floor == long memory / white noise]")
    print("      T        S(1e-4)        IR slope (two smallest probes)")
    for T in Ts:
        print(f"  {T:9.3g}   {S(1e-4, T):12.5e}        {ir_exp[T]:6.3f}")

    print("\n(3) noise memory time tau_nu(T)   [diverges with T => long memory; saturates => short]")
    print("      T        tau_nu (units of 1/omega_c)")
    taus = {}
    for T in Ts:
        taus[T] = noise_kernel_memory_time(T)
        print(f"  {T:9.3g}   {taus[T]:8.4f}")
    tmin, tmax = min(taus.values()), max(taus.values())
    print(f"\n    tau_nu spread across T in [{min(Ts)},{max(Ts)}]: "
          f"{tmin:.3f} .. {tmax:.3f}  (ratio {tmax/tmin:.2f}x)")

    print("\n" + "-" * 78)
    print("PHYSICAL SCALES  -- which T and omega actually apply, per rung")
    print("-" * 78)
    hbar = 1.054571817e-34
    kB = 1.380649e-23
    # Tabletop falsifier (rung 8): T = lab/environment temperature
    for Tlab in (1.0, 0.01):
        w_th = 2 * kB * Tlab / hbar                       # omega* = 2kT/hbar
        w_689 = 2 * math.pi * 689.0
        print(f"  lab T={Tlab:>5} K : omega*=2kT/hbar = {w_th:.3e} rad/s ; "
              f"689 Hz = {w_689:.3e} rad/s ; ratio omega/omega* = {w_689/w_th:.2e}")
    print("    => the 689 Hz tabletop sits DEEP below omega* (omega << 2T): THERMAL regime, s_eff -> 2.")
    H0 = 2.20e-18                                          # Hubble rate, s^-1
    w_star_dS = H0 / math.pi                               # omega* = 2 T_dS = 2*(H/2pi) = H/pi
    print(f"  de Sitter   : T_dS=hbar H/2pi kB ; omega*=H/pi = {w_star_dS:.3e} rad/s ; "
          f"cosmo omega ~ H = {H0:.3e} ; ratio = {H0/w_star_dS:.2f}")
    print("    => cosmology (rung 7) sits at the CROSSOVER (omega ~ omega*): s_eff between 2 and 3.")

    print("\n" + "=" * 78)
    print("VERDICT  (a lead to verify with the live specialist, NOT a settled result)")
    print("=" * 78)
    print("""\
  * The thermal coth factor softens the noise IR exponent by exactly ONE power:
    s = 3 (quantum, omega >> 2T)  ->  s_eff = 2 (thermal, omega << 2T).
    One coth power cannot reach s_eff < 1, so with an s=3 start the bath lands at
    s_eff = 2: still SUPER-OHMIC, one notch above the Ohmic (s=1) boundary.
  * The DC noise floor S(omega->0) -> 0 as omega^2 at every T>0 (table 2). A bath
    with NO zero-frequency noise power is short-memory; the long-memory signature
    (a nonzero white floor, as in Ohmic s=1, or a divergence, as in sub-Ohmic) does
    NOT appear. tau_nu (table 3) stays set by the UV cutoff 1/omega_c, not by T.
  * So at the level of the standard QBM/Caldeira-Leggett calculation with a smooth
    cutoff: finite T SOFTENS single-pole (s:3->2) and GROWS the noise amplitude
    (~T), but does NOT BREAK it. The specialist's 'pushes toward Ohmic/sub-Ohmic'
    is directionally right and stops one notch short of Ohmic.

  WHAT THIS DOES NOT SETTLE (hand these to the specialist):
   (i)  It assumes the standard bilinear QBM coupling and the friction/noise split.
        If GRUT's coupling differs, or if the OBSERVABLE memory is governed by a
        different kernel combination, s_eff = 2 vs 3 could matter more.
   (ii) s_eff = 2 is closer to the Ohmic boundary than s = 3; whether single-pole
        (one dominant relaxation) survives quantitatively, or splits into a slow +
        fast pole, needs the explicit pole structure of the s_eff=2 kernel, not just
        the exponent.
   (iii) The de Sitter temperature is tiny, so cosmology (rung 7) sits AT the
        crossover, where s_eff drifts between 2 and 3 across the band -- the w(z)
        shape will depend on exactly where. The tabletop (rung 8) is deep thermal.

  ONE-LINE QUESTION FOR THE SPECIALIST (same shape as the DOS question):
    'For an s=3 super-Ohmic bath with a smooth UV cutoff, does the finite-T coth
     factor (S ~ omega^2 in the thermal IR, S(0)=0) keep the noise kernel
     single-pole/short-memory, or does the s_eff=2 spectrum carry a slow second pole
     that the cutoff-set memory time hides?'""")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
