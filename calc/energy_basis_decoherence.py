#!/usr/bin/env python3
"""KILL-SHOT #2: the falsifier, recomputed in the ENERGY basis.

The old framing -- "689 Hz, parameter-free, cleanly distinct from Diosi-Penrose/CSL" --
was miscast three ways (panel + primary check against Anastopoulos-Hu 2013):
  (1) WRONG AXIS. The AH gravitational-decoherence master equation decoheres in the
      ENERGY eigenbasis; DP and CSL are POSITION-basis spontaneous-localization models.
      They are not competing numbers on one observable -- they are different observables.
  (2) NOT PARAMETER-FREE. The AH rate depends on free 'textures of spacetime' parameters
      beyond the Planck scale.
  (3) 689 Hz IS AN INPUT, NOT A KERNEL OUTPUT. It comes from an added tau_c / cutoff
      scale, not from the AH kernel.

This script does the relocation the panel pointed to: turn the energy-basis structure into
the genuine, citable wedge AH hands you, and state honestly what is predicted vs staked.

WORKING ASSUMPTION (contingent on kill-shot #1): the responsive-vacuum noise kernel is
short-memory (cutoff-set), so its symmetrized spectrum keeps the kill-shot-#1 shape
S(omega) ~ omega^3 e^{-(omega/omega_c)^2} (thermal IR softens omega^3 -> omega^2 below 2T).
The QUALITATIVE wedge below does NOT depend on this; only the spectral SHAPE does.

Units hbar = k_B = omega_c = 1. Pure stdlib.
"""
import math

WC = 1.0


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
    return w ** 3 * math.exp(-(w / WC) ** 2)


def S(w, T=0.0):
    """Kill-shot-#1 noise spectrum. T=0 -> quantum envelope (coth->1)."""
    if w <= 0:
        return 0.0
    return J(w) if T <= 0 else J(w) * coth(w / (2.0 * T))


def main():
    print("=" * 78)
    print("KILL-SHOT #2  the falsifier, recomputed in the ENERGY basis")
    print("CONTINGENT ON #1 for the spectral shape; the energy-vs-position WEDGE is not.")
    print("=" * 78)

    print("""
STRUCTURE.  System couples to the responsive vacuum via the operator gravity sees -- the
mass-energy / stress operator A (A ~ H_S in the 'gravity couples to energy' limit).
Born-Markov reduction of the in-in influence action gives, for the coherence between two
energy eigenstates |n>,|m> split by Delta E = hbar*omega_nm:

    Gamma(Delta E)  =  (1/hbar^2) |A_nm|^2  S(omega_nm),     omega_nm = Delta E / hbar

i.e. the decoherence rate SAMPLES THE VACUUM NOISE SPECTRUM AT THE BOHR FREQUENCY of the
energy gap. This is the AH energy-basis result. Two consequences fall straight out:
""")

    # ---- (A) the spectral shape of decoherence vs energy gap ---------------------------
    print("-" * 78)
    print("(A) DECOHERENCE SHAPE g(x) = S(x*omega_c)/peak   vs   x = Delta E / (hbar omega_c)")
    print("    [the 'finite-bandwidth feature' -- correctly located in ENERGY-GAP space]")
    print("-" * 78)
    # quantum envelope g(x) ~ x^3 e^{-x^2}; peak at x=sqrt(3/2)
    xpk = math.sqrt(1.5)
    gpk = J(xpk)
    xs = [0.05, 0.1, 0.25, 0.5, xpk, 2.0, 3.0, 4.0]
    print("       x = dE/hbar wc     g(x)=Gamma/Gamma_peak     local slope d ln g/d ln x")
    for x in xs:
        g = J(x) / gpk
        h = 1e-4
        slope = (math.log(J(x * (1 + h))) - math.log(J(x * (1 - h)))) / (2 * h)
        tag = "  <- PEAK" if abs(x - xpk) < 1e-6 else ""
        print(f"     {x:10.4f}        {g:10.4f}              {slope:+8.3f}{tag}")
    # FWHM
    half = gpk * 0.5
    def Jm(x):
        return J(x) - half
    def bisect(a, b):
        for _ in range(80):
            c = 0.5 * (a + b)
            if Jm(a) * Jm(c) <= 0:
                b = c
            else:
                a = c
        return 0.5 * (a + b)
    xlo = bisect(1e-4, xpk)
    xhi = bisect(xpk, 8.0)
    print(f"\n    peak at  Delta E = {xpk:.3f} hbar*omega_c   (NOT a fixed lab frequency)")
    print(f"    FWHM     Delta E in [{xlo:.3f}, {xhi:.3f}] hbar*omega_c   (width {xhi-xlo:.3f})")
    print("    rise: g ~ x^3 (quantum) or x^2 (thermal IR, contingent on #1); S(0)=0 so")
    print("    SMALL energy gaps are SUPPRESSED -- decoherence GROWS then cuts off at ~omega_c.")

    # ---- (B) the experimental wedge: energy basis vs position basis --------------------
    print("\n" + "-" * 78)
    print("(B) THE WEDGE  --  how the rate scales, GRUT-AH (energy) vs DP/CSL (position)")
    print("    This is INDEPENDENT of kill-shot #1. It is the real differentiator.")
    print("-" * 78)
    print("""
                         vary Delta E (fixed Delta x)      vary Delta x (fixed Delta E)
    GRUT-AH (energy) :   Gamma ~ S(Delta E/hbar)           Gamma ~ const  (no Delta x dep, leading order)
    DP / CSL (posn)  :   Gamma ~ const  (no Delta E dep)   Gamma ~ (Delta x)^2

    => Orthogonal dependences. The discriminating experiment holds one knob fixed and
       sweeps the other:
         * same Delta x, two internal-energy splittings  -> GRUT responds, DP/CSL flat
         * same Delta E, two spatial separations          -> DP/CSL responds, GRUT flat
       A molecular / clock-state interferometer can vary Delta E and Delta x independently.
""")
    # illustrative normalized table (scalings only; absolute kappa, lambda are unknown inputs)
    print("    Illustrative normalized rates (energy-basis uses g(x); position uses (dx)^2):")
    print("      dE/hbar wc   dx/ell    Gamma_energy/peak   Gamma_position(~(dx/ell)^2)")
    for dE, dx in [(0.1, 1.0), (0.1, 3.0), (xpk, 1.0), (xpk, 3.0), (3.0, 1.0), (3.0, 3.0)]:
        ge = J(dE) / gpk
        gp = dx ** 2
        print(f"      {dE:8.3f}    {dx:5.1f}     {ge:14.4f}      {gp:12.3f}")
    print("    Read the columns: Gamma_energy moves with dE and ignores dx; Gamma_position")
    print("    moves with dx and ignores dE. No overlap -> a clean qualitative falsifier.")

    # ---- (C) honest accounting ---------------------------------------------------------
    print("\n" + "-" * 78)
    print("(C) PARAMETER ACCOUNTING  --  what is predicted vs staked")
    print("-" * 78)
    print("""
    PREDICTED (parameter-free, up to one overall normalization):
      - the energy-basis structure itself (decohere in energy, not position)
      - the SHAPE g(x): suppressed at small gap (S(0)=0), rise, peak at ~hbar*omega_c, cutoff
      - the orthogonal Delta E vs Delta x scaling wedge (B)
    STAKED INPUTS (declare on the ledger, do NOT call parameter-free):
      - the overall amplitude / coupling normalization (kappa) -> survives MICROSCOPE/Donadi bounds
      - the cutoff scale omega_c that sets the PEAK energy gap (this is what '689 Hz' really was:
        one chosen scale, not a kernel output). Retire '689 Hz parameter-free'; keep omega_c as
        a single staked scale with a PREDICTED shape around it.
""")

    # ---- (D) BMV backup: recompute / withdraw ------------------------------------------
    print("-" * 78)
    print("(D) BMV ENTANGLEMENT-WITNESS BACKUP  --  withdrawn pending recompute")
    print("-" * 78)
    print("""
    BMV (Bose et al / Marletto-Vedral) generates entanglement via the POSITION-dependent
    gravitational phase between two masses -- the witness lives in the which-path (position)
    basis. An ENERGY-basis decoherer does NOT obviously degrade a position-basis entanglement
    witness: at leading order it commutes with the which-path observable and may leave the
    witness intact. So the earlier 'finite-bandwidth mediator => reduced BMV witness' claim is
    NOT established for an energy-basis kernel. WITHDRAW it as a backup until the witness is
    computed from the AH energy-basis kernel acting on the BMV position d.o.f. (open task).
""")

    print("=" * 78)
    print("VERDICT  (lead; for the specialist. Energy-basis wedge is the firmer ground.)")
    print("=" * 78)
    print("""\
  * The falsifier is RELOCATED, not dead. The crown-jewel observable is no longer a 689 Hz
    line on the collapse-models' own (position) axis; it is the ENERGY-basis signature:
    decoherence that scales with the energy gap Delta E and ignores the spatial size Delta x,
    the qualitative OPPOSITE of DP/CSL. That is a cleaner differentiator than a competing
    number, and it is INDEPENDENT of kill-shot #1.
  * The spectral shape g(Delta E) (suppressed-rise-peak-cutoff) is parameter-free up to
    normalization and is CONTINGENT on #1 (it uses the short-memory S(omega) shape). If the
    pole-structure check changes S, the shape changes; the wedge does not.
  * '689 Hz, parameter-free' is RETIRED: re-expressed as the staked cutoff scale omega_c (the
    peak location) plus a predicted shape. Amplitude + omega_c are the two staked inputs.
  * The BMV backup is WITHDRAWN pending a position-basis witness calculation.

  OPEN ITEMS FOR THE SPECIALIST:
   (i)   the exact coupling operator A and its matrix elements |A_nm| (gravity couples to the
         full stress tensor, not exactly H_S) -- fixes whether small gaps are pure-dephasing
         suppressed (samples S(0)=0) or transition-driven (samples S(omega_nm)).
   (ii)  the physical value of omega_c: if it truly sits near sub-kHz, atomic/molecular gaps
         (omega = Delta E/hbar >> omega_c) are exponentially cutoff-suppressed -- is the
         vacuum-memory scale really that low, and what experiment then has access?
   (iii) the BMV witness under an energy-basis decoherer (does it degrade at all?).

  ONE-LINE QUESTION FOR THE SPECIALIST:
    'For gravity coupling to the stress tensor (not exactly H_S), does the energy-basis
     decoherence of a Delta-E superposition sample S(omega = Delta E/hbar) (transition-driven,
     nonzero) or S(0)=0 (pure-dephasing, suppressed) -- i.e. is the responsive vacuum a
     decohering or a quiet bath for static energy superpositions?'""")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
