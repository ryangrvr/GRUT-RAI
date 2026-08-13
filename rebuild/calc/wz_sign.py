#!/usr/bin/env python3
"""wz_sign: rung7 in-house attempt -- the dark-energy w(z) and the SIGN of wa (W2).

CLAIM (W2, default-BROKEN): for the passive, causal, KMS-consistent vacuum the shown spine supplies
(rung1 memory + rung2 detailed balance + rung4 KK), w(z) cannot cross the phantom divide (w >= -1),
so DESI's evolving wa<0 (quintom CROSSING) is reachable only by breaking passivity (an inserted
ghost/active component = laundering).

This is the in-house attempt to DERIVE it. Default-BROKEN: report what the constraints actually give --
the SIGN of wa (forced, indeterminate) and whether the phantom-divide CROSSING is forbidden. Derive the
SIGN/no-go, NOT the magnitude (the magnitude rides on the late-time vacuum-energy anchor, which is open).

Pure stdlib. Strictly v5 register (rung1/rung2/rung4 + the mu_linear pure-TT structure); no prior lineage.
"""

OMEGA_M, OMEGA_L = 0.3, 0.7
EPS = 0.05  # an illustrative small dissipative-correction amplitude (its SIGN is the question; |EPS| open)


def H_over_H0(a):
    """Background expansion rate (matter + Lambda); H decreases as a grows."""
    return (OMEGA_M / a ** 3 + OMEGA_L) ** 0.5


def w_of_a(a, sign):
    """Effective dark-energy w(a) = -1 + sign*EPS*(H/H0). The vacuum's EQUILIBRIUM is w=-1 (de Sitter);
    a passive dissipative correction is ONE-SIGNED in (w+1) and shrinks as H->0 (the de Sitter attractor).
      sign = -1  : bulk-viscous reading (passivity/2nd law: zeta>=0 -> Pi=-3 zeta H <= 0) -> w <= -1.
      sign = +1  : phase-lag / energy-loss reading (banked rung7 v5) -> w >= -1.
    """
    return -1.0 + sign * EPS * H_over_H0(a)


def wa_cpl(sign):
    """Extract the CPL slope wa = -dw/da|_{a=1} (w(a) ~ w0 + wa(1-a))."""
    h = 1e-4
    dwda = (w_of_a(1.0 + h, sign) - w_of_a(1.0 - h, sign)) / (2 * h)
    return -dwda


def crosses_minus1(sign):
    """Does w(a) cross the phantom divide -1 over 0<a<=1? (w+1 changes sign?)"""
    vals = [w_of_a(a, sign) + 1.0 for a in (0.05, 0.1, 0.3, 0.5, 0.8, 1.0)]
    return min(vals) < 0 < max(vals)


def main():
    print("=" * 80)
    print("rung7 -- w(z) and the SIGN of wa (W2), in-house, default-BROKEN")
    print("=" * 80)

    print("\n(W1) THE MAP. A relaxing chi(omega) gives an effective DE stress -> w(a) = -1 + (w+1),")
    print("     where (w+1) = Pi/rho is the dissipative pressure correction off the de Sitter equilibrium")
    print("     (w_eq = -1). This is generic EFT-of-dark-energy (Gubitosi-Piazza-Vernizzi); it follows")
    print("     from rung1 (memory) + rung4 (KK). GRUT-specific content is ONLY the passive-causal sign.")

    print("\n(W2) THE SIGN -- two passivity-consistent framings, OPPOSITE wa, NEITHER crosses -1:")
    print("     framing                         w0        wa        crosses w=-1?")
    for name, sign in (("bulk-viscosity (zeta>=0)", -1), ("phase-lag/energy-loss (banked v5)", +1)):
        w0 = w_of_a(1.0, sign)
        print(f"     {name:32}  {w0:+.4f}   {wa_cpl(sign):+.4f}     {crosses_minus1(sign)}")
    print("     => Both are passivity-consistent (one-signed (w+1)); they give OPPOSITE wa")
    print("        (bulk-viscous wa<0 toward-DESI-side; phase-lag wa>0 against). So the SIGN of wa is")
    print("        NOT fixed by passivity alone -- it rides on the SIGN of the trace-sector dissipative")
    print("        coupling to the expansion, which the frequency-space spine does NOT supply.")
    print("     => BUT NEITHER framing CROSSES w=-1: the equilibrium is exactly w=-1 and the passive")
    print("        correction is one-signed, so w stays on ONE side. A CROSSING (w<-1 past -> w>-1 now,")
    print("        DESI's quintom) needs the equilibrium itself off -1 -- a real quintessence/phantom")
    print("        DOF beyond the vacuum (NEC sign-change = a ghost). Passive vacuum cannot.")

    print("\n(mu_linear) THE SOURCED STRUCTURE. The shown response is pure spin-2 transverse-traceless")
    print("     (mu_linear / p_tt_ansatz): the spin-0 / trace sector that would carry a bulk response is")
    print("     annihilated, so zeta_bulk = 0 -> (w+1) = 0 -> w = -1 FLAT. The sourced GRUT vacuum is")
    print("     LambdaCDM at BACKGROUND order, not merely linear order. Any w(z) EVOLUTION requires the")
    print("     trace sector mu_linear's no-go EXCLUDES -- an inserted input.")

    print("\n" + "=" * 80)
    print("VERDICT (default-BROKEN, honest):")
    print("  W2 ROBUST CANDIDATE (default-BROKEN, held to-derive): passive + causal + equil-at-w=-1  =>  NO CROSSING.")
    print("     DESI's quintom crossing (w0>-1 with w<-1 in the past) requires breaking passivity / an")
    print("     inserted off--1 DOF = LAUNDERING. This is a falsifiable-direction NO-GO.")
    print("  W2 INDETERMINATE: the SIGN of wa (which side of -1; wa>0 freezing vs wa<0 apparent-phantom)")
    print("     is framing-dependent -- NOT derivable from passivity alone; needs the de Sitter trace-")
    print("     sector effective stress tensor -> FRONTIER (dark-energy-EFT specialist).")
    print("  W2 SOURCED: w = -1 FLAT (pure-TT, zeta_bulk=0). The only fully-sourced prediction.")
    print("  SIDE vs SLOPE (firewall-corrected): the 2nd law fixes the dissipative branch on the phantom")
    print("     SIDE (w<=-1, which forbids crossing) but NOT the wa SLOPE sign -- sigma=Pi^2/(zeta T) is")
    print("     quadratic in Pi, blind to dPi/dt; the toy's wa<=0 is a zeta=const artifact. So no DESI-ward")
    print("     theorem; the wa sign is genuinely indeterminate (the robust content is the no-crossing SIDE).")
    print("  W3: WOULD convert the harness's asserted negative into a derived no-go IF it graduates (held")
    print("     to-derive); + sourced w=-1 flat; the wa sign stays frontier. NOT a ToE-completion; sign/no-go,")
    print("     not a precise w(z) curve.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
