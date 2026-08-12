#!/usr/bin/env python3
"""ARROW OF TIME: is the in-in time-asymmetry intrinsic to the dynamics, or imported?

This is the make-or-break leg. We test it on the exactly-solvable independent-boson /
pure-dephasing model -- the same super-Ohmic finite-memory bath, where the decoherence
function is known in closed form, so we can see *exactly* where any arrow enters.

For a qubit coupled to a bath of oscillators (pure dephasing), with a FACTORIZED initial
state rho_S ⊗ rho_B (bath thermal at T), the coherence decays as |L(t)| = exp(-Gamma(t)) with
    Gamma(t) = sum_k [J(w_k)/w_k^2] (1 - cos(w_k t)) coth(w_k / 2T) dw       (Breuer-Petruccione)
J(w) = w^3 exp(-(w/wc)^2) is GRUT's super-Ohmic bath. Units hbar=kB=wc=1. Pure stdlib.

Three things this exposes:
  (1) TIME SYMMETRY: Gamma(t) = Gamma(-t) exactly (it depends on 1-cos(w t), even in t).
      The microscopic dynamics carry NO preferred direction.
  (2) RECURRENCE: with finitely many modes Gamma(t) is periodic -> |L(t)| decays then RETURNS
      to 1 at t_rec = 2pi/dw. The 'decay' is reversible; irreversibility is NOT in the dynamics.
  (3) INITIAL-STATE DEPENDENCE: the decay is set by coth(w/2T) -- i.e. by the assumed bath
      state -- and by taking the continuum (many-mode) limit. Both are assumptions about the
      INITIAL CONDITION and the bath, not features of the equations of motion.
If the arrow lives only in (i) the factorized thermal initial state and (ii) the continuum
limit, it is IMPORTED, not intrinsic.
"""
import math

WC = 1.0


def coth(x):
    if x <= 0:
        return 1.0          # zero-T limit coth(w/0+) -> 1 for w>0
    if x > 20:
        return 1.0
    if x < 1e-8:
        return 1.0 / x
    return 1.0 / math.tanh(x)


def J(w):
    return w ** 3 * math.exp(-(w / WC) ** 2)


def gamma(t, T, N, wmax=6.0):
    dw = wmax / N
    g = 0.0
    for k in range(1, N + 1):
        w = k * dw
        coth_factor = 1.0 if T <= 0 else coth(w / (2.0 * T))   # T=0: zero-T limit coth->1
        g += (J(w) / w ** 2) * (1.0 - math.cos(w * t)) * coth_factor * dw
    return g


def L(t, T, N, wmax=6.0):
    return math.exp(-gamma(t, T, N, wmax))


def main():
    print("=" * 78)
    print("ARROW OF TIME -- where does the in-in time-asymmetry enter?")
    print("independent-boson dephasing, super-Ohmic bath J(w)=w^3 e^{-(w/wc)^2}")
    print("=" * 78)

    T, N, wmax = 2.0, 64, 6.0
    t_rec = 2 * math.pi / (wmax / N)     # exact recurrence period of the discrete spectrum

    # (1) time symmetry
    print("\n(1) TIME SYMMETRY of the dynamics:  Gamma(t) vs Gamma(-t)")
    print("      t      Gamma(t)     Gamma(-t)     equal?")
    for t in (1.0, 2.5, 4.0):
        gp, gm = gamma(t, T, N), gamma(-t, T, N)
        print(f"   {t:5.1f}   {gp:9.5f}   {gm:9.5f}     {abs(gp-gm) < 1e-12}")
    print("    => Gamma is EVEN in t. The equations of motion pick no direction of time.")

    # (2) recurrence
    print(f"\n(2) RECURRENCE (N={N} modes, exact period t_rec = 2pi/dw = {t_rec:.2f}):")
    print("      t         |L(t)|     ")
    for frac in (0.0, 0.05, 0.15, 0.4, 0.7, 0.95, 1.0):
        t = frac * t_rec
        bar = "#" * int(40 * L(t, T, N))
        print(f"   {t:7.2f}    {L(t, T, N):7.4f}  {bar}")
    print(f"    => |L| decays toward 0 then RETURNS to {L(t_rec, T, N):.4f} at t_rec.")
    print("       The decoherence is REVERSIBLE -- not a fundamental arrow.")

    # (3a) recurrence time grows with N -> continuum limit is where irreversibility 'emerges'
    print("\n(3a) CONTINUUM LIMIT: recurrence time vs number of modes")
    print("      N      t_rec = 2pi N / wmax")
    for n in (16, 64, 256, 1024):
        print(f"   {n:5d}    {2*math.pi*n/wmax:10.1f}")
    print("    => t_rec -> infinity as N -> infinity. Monotone (irreversible) decay exists")
    print("       ONLY in the many-mode/thermodynamic limit -- an assumption, not dynamics.")

    # (3b) initial-state dependence
    print("\n(3b) INITIAL-STATE DEPENDENCE: the decay is set by the assumed bath state (T)")
    print("      t      |L| (T=0, vacuum)   |L| (T=5, hot)")
    for t in (1.0, 2.0, 3.0):
        print(f"   {t:5.1f}      {L(t,0.0,N):12.4f}      {L(t,5.0,N):10.4f}")
    print("    => different initial bath state -> different decay. The arrow's strength is")
    print("       fixed by the ASSUMED initial condition (coth = the bath's occupation).")

    print("\n" + "=" * 78)
    print("VERDICT  (lead; the human specialist is the firewall)")
    print("=" * 78)
    print("""\
  The microscopic dephasing dynamics are TIME-SYMMETRIC (Gamma even in t) and RECURRENT
  (reversible). No arrow lives in the equations of motion. A monotone, irreversible arrow
  appears ONLY when we add two INPUTS:
    (i)  the FACTORIZED, thermal initial state rho_S ⊗ rho_B -- an uncorrelated, low-entropy
         initial condition (the Feynman-Vernon assumption), which sets coth(w/2T); and
    (ii) the continuum / thermodynamic limit (N -> infinity), which pushes recurrence to
         infinity.
  Both are assumptions about the INITIAL CONDITION and the bath -- not consequences of the
  in-in dynamics. So on this exactly-solvable model the arrow is IMPORTED via the initial
  condition (source #2), exactly as braced. The CTP contour and the retarded/iε choice are
  downstream bookkeeping; the entropy gradient is put in by hand at t0.

  ANTI-LAUNDERING (the guard that matters): the factorized thermal initial state is
  'physically natural' -- and it is STILL an assumed low-entropy initial condition. 'Natural'
  is precisely how the Past Hypothesis gets smuggled past review. Marked, not laundered:
  GRUT does NOT derive the arrow; it LOCATES exactly where the arrow is assumed -- the
  factorization condition -- and refuses to call that 'derived.' That is the floor, and it is
  a real, honest contribution to the Albert/Price/Carroll problem: here is the precise object
  you must assume, named, not hidden.

  CEILING (not closed by this toy): could a genuinely NON-factorized, dynamically-generated
  initial correlation seed the gradient without assuming it? This model cannot, and removing
  factorization generically destroys the clean derivation -- the standard bind. Hand to the
  specialist; do not self-certify the ceiling shut.

  ONE-LINE QUESTION FOR THE SPECIALIST:
    'In the in-in/Feynman-Vernon treatment of a finite-memory bath, does the thermodynamic
     arrow trace to anything other than the factorized (uncorrelated, low-entropy) initial
     state rho_S ⊗ rho_B -- i.e. is there any route to irreversibility that does not assume an
     initial low-entropy/Stosszahlansatz condition somewhere?'""")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
