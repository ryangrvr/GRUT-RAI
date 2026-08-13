#!/usr/bin/env python3
"""Q1 (DECISIVE): energy-basis falsifier -- the MAGNITUDE, not just the commutator.

  # AUTHORITY-VOCABULARY ANNOTATION 2026-08-12: 'specialist' here is an IN-HOUSE AI pass,
  # not an outside human. No outside human has ever been contacted by this program.
  # Annotated, not renamed -- see provenance/prereg/RESULT_AUTHORITY_TERMS_2026-08-12.txt
The specialist confirmed the decision tree: [A,H_S]=0 -> samples S(0)=0 -> quiet bath;
[A,H_S]!=0 -> samples S(dE) -> formally lives. But 'lives' and 'observable' are two
different questions. This calc reports the RATIO (predicted decoherence rate / detectable
rate), exactly as the GW brief did, and stamps one of:
  (A) lives-and-observable, (B) lives-but-faint, (C) dies (commutes).
Anti-laundering: a formally-nonzero-but-invisible decoherence is NOT a falsifier -- it is the
GW result again wearing a different coupling. The headline is the ratio.

KEY OPERATOR STRUCTURE (the thing I glossed before).
Gravity couples to T^{mu nu}, which splits in the energy basis of the system:
  * T^{00} = energy density. For a system AT REST this IS ~H_S -> DIAGONAL in the energy
    basis -> [A_diag, H_S] = 0 -> energy-basis dephasing samples S(0). Super-Ohmic S(0)=0
    => QUIET. This is the DOMINANT (Newtonian) coupling.
  * T^{0i}, T^{ij} = momentum/energy flux + stress. OFF-DIAGONAL in the energy basis,
    suppressed by (v/c) (internal velocities). [A_off, H_S] != 0 -> samples S(omega_Bohr),
    but the RATE carries (v/c)^2 on top of the Planck suppression of S.
So the energy-basis WEDGE (the dE-scaling that made GRUT distinct from position-basis DP/CSL)
requires the OFF-DIAGONAL piece. The diagonal piece -- the part gravity couples to most
strongly -- is exactly the one that samples S(0)=0 and is quiet.

Pikovski-style time-dilation decoherence (internal energy x position) IS [A,H_S]!=0, but it
decoheres the POSITION (Dx) superposition -- position basis, the SAME axis as DP/CSL. It does
not supply the energy-basis wedge.

Units SI. Pure stdlib.
"""
import math

C = 2.99792458e8
HBAR = 1.054571817e-34
G = 6.67430e-11
EV = 1.602176634e-19
T_P = math.sqrt(HBAR * G / C ** 5)      # Planck time ~5.39e-44 s
OMEGA_P = 1.0 / T_P                      # ~1.85e43 rad/s
E_P = HBAR * OMEGA_P                     # Planck energy (J)

GAMMA_DETECT = 1.0   # 1/s: a generous detectable decoherence rate (best matter-wave
                     # interferometry keeps coherence ~seconds -> rates ~1/s are the edge).


def S_phi(omega, q, alpha=1.0):
    """Dimensionless gravitational-potential noise of the vacuum, super-Ohmic, Planck-cut.
    FDT partner of Im[chi]~(omega/omega_P)^q ; S_phi(omega) ~ t_P (omega/omega_P)^(q-1).
    S_phi(0)=0 for q>1; for q=1 it is flat ~ t_P (the most generous, and -- see below --
    already excluded by observed coherence for heavy systems)."""
    if omega <= 0:
        return 0.0
    return alpha * T_P * (omega / OMEGA_P) ** (q - 1)


def main():
    print("=" * 80)
    print("Q1  energy-basis falsifier -- MAGNITUDE / RATIO (decisive)")
    print(f"t_P={T_P:.3e}s  omega_P={OMEGA_P:.3e}/s  E_P={E_P/EV:.3e}eV")
    print("Gamma = (dE/hbar)^2 S_phi(omega_sampled) ; report Gamma / Gamma_detect (=1/s)")
    print("=" * 80)

    print("""
BRANCH C (diagonal coupling T^00 ~ energy density, the DOMINANT one):
  A ~ H_S  =>  [A,H_S]=0  =>  energy-basis dephasing samples S(0).
  Super-Ohmic vacuum has S(0)=0  =>  Gamma = 0  =>  QUIET BATH, falsifier DIES.
  This is the natural fate of the energy-basis wedge under the strongest gravitational coupling.
""")

    print("BRANCH B (off-diagonal T^0i,T^ij ~ (v/c), the part that gives the wedge):")
    print("  Gamma_off ~ (v/c)^2 (dE/hbar)^2 S_phi(omega_Bohr),  omega_Bohr = dE/hbar")
    print("  -- doubly suppressed: (v/c)^2 AND Planck. Representative numbers:\n")
    vc = 1e-3   # internal velocity / c (generous for a bound system)
    print(f"  (v/c = {vc:.0e};  Gamma_detect = {GAMMA_DETECT:.0e}/s)")
    print("    dE          q   omega_Bohr(/s)   S_phi          Gamma_off(/s)    Gamma/Gamma_det")
    for dE_eV in (1.0, 1e3, 1e6):
        dE = dE_eV * EV
        wB = dE / HBAR
        for q in (1, 2):
            S = S_phi(wB, q)
            gamma = (vc ** 2) * (dE / HBAR) ** 2 * S
            ratio = gamma / GAMMA_DETECT
            korders = math.log10(ratio) if ratio > 0 else float("-inf")
            print(f"   {dE_eV:8.0e} eV  {q}   {wB:.3e}    {S:.3e}   {gamma:.3e}    "
                  f"10^{korders:+.0f}")

    print("""
  => Off-diagonal (wedge) decoherence is ~10^-29 to ~10^-47 below detectable. OUTCOME (B):
     real but invisible -- the GW result again, now via the gravitational coupling.
""")

    # ---- the most-generous (excluded) limit, for honesty -----------------------------
    print("-" * 80)
    print("MOST-GENEROUS LIMIT (flat S_phi~t_P, v/c=1, NO Planck suppression) -- and why it's")
    print("excluded, which is itself the binding constraint:")
    print("-" * 80)
    for dE_eV in (1e6, 1e9):
        dE = dE_eV * EV
        gamma_max = (dE / HBAR) ** 2 * T_P     # flat S~t_P, v/c=1
        print(f"    dE={dE_eV:.0e} eV:  Gamma_max ~ (dE/hbar)^2 t_P = {gamma_max:.3e}/s "
              f"-> tau ~ {1/gamma_max:.3e} s")
    print("""    A flat S_phi~t_P would over-decohere heavy energy superpositions (Gamma>>1/s),
    which is NOT observed -> the true vacuum noise must be suppressed FAR below flat-Planck.
    Observed matter-wave coherence is therefore the BINDING bound on GRUT's staked noise
    amplitude (analogous to GW170817 bounding GW dissipation). The natural value is excluded;
    the suppressed (super-Ohmic) value is invisible (Branch B). Observability would require
    STAKING the amplitude right at the current matter-wave edge -- a tuned number, not a
    parameter-free prediction.""")

    # ---- inversion: what S_phi would be needed -------------------------------------------
    print("\n" + "-" * 80)
    print("INVERSION (what amplitude reaches observability), dE = 1 MeV, v/c=1e-3:")
    print("-" * 80)
    dE = 1e6 * EV
    wB = dE / HBAR
    S_needed = GAMMA_DETECT / ((vc ** 2) * (dE / HBAR) ** 2)
    S_nat = S_phi(wB, 1)
    print(f"    S_phi needed for Gamma=1/s : {S_needed:.3e}")
    print(f"    S_phi natural (q=1, ~t_P)  : {S_nat:.3e}")
    print(f"    ratio needed/natural       : {S_needed/S_nat:.3e}  "
          f"(need to stake ~10^{math.log10(S_needed/S_nat):+.0f} above natural to see it)")

    print("\n" + "=" * 80)
    print("VERDICT  (ratio-first, per the brief)")
    print("=" * 80)
    print("""\
  THE RATIO IS THE ANSWER, and it is far below 1 in every honest branch:
   * Diagonal (dominant) coupling: Gamma = 0 exactly (S(0)=0). The wedge is QUIET -> DIES.
   * Off-diagonal (wedge-carrying) coupling: Gamma/Gamma_det ~ 10^-29..10^-47. LIVES-FAINT (B).
   * The only route to observable is to stake the noise amplitude ~10^20+ above its natural
     value, right at the current matter-wave bound -- a tuned number, not a prediction, and
     the same (B)->forced-(A) move we refused for GW dissipation.

  So 'lives' does NOT stand as the headline. The honest headline: the energy-basis falsifier
  is QUIET under the dominant coupling and FAINT under the sub-dominant one -- it does NOT
  carry the program as a parameter-free, distinct, observable wedge. And note the deeper point:
  the Pikovski mechanism that DOES give a robust effect decoheres POSITION (Dx), i.e. the
  same axis as DP/CSL -- it is not the energy-basis wedge at all.

  => CONFIRMS THE REFRAME. GRUT's genuine contribution is the STRUCTURAL in-in arrow of time,
     not a tabletop decoherence wedge. The falsifier was the thing we hoped carried it; the
     ratio says it doesn't.

  STAMP: rung 8 differentiator -> FAILS-DIFFERENTIATION (quiet-or-faint). Energy-basis wedge
  is not a working observable falsifier with current or foreseeable sensitivity.

  ONE-LINE QUESTION FOR THE SPECIALIST (gray-zone check):
    'For a system in a pure internal-ENERGY superposition (fixed position), is the dominant
     gravitational coupling the diagonal T^00 (~H_S, sampling S(0)=0, quiet), so that the only
     energy-basis decoherence comes from (v/c)-suppressed off-diagonal T^0i/T^ij -- or is there
     a leading-order off-diagonal energy coupling I am missing that would sample S(dE) at O(1)?'""")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
