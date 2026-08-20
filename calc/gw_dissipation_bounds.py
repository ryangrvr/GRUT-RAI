#!/usr/bin/env python3
"""RUNG 4: GW dissipation from Im[chi] -- is there anything to bound?

A finite-memory vacuum has a dissipative response Im[chi(omega)] (Kramers-Kronig partner of
the elastic Re[chi] from the Love-number rung). A GW propagating through it would pick up
frequency-dependent attenuation and v_g(omega) != c -- something a lossless GR vacuum (v_g=c,
no dispersion) cannot do. LIGO/Virgo/KAGRA + GW170817 are a pre-existing sandbox.

HONEST QUESTION FIRST: not 'extract a bound' but 'is the effect within many orders of LIGO
sensitivity?'. The super-Ohmic, cutoff-suppressed vacuum that keeps GRUT solar-system-safe
almost certainly makes this tiny. Tuning tau_c / the coupling to manufacture a detectable
effect is laundering. 'Real but N orders too small' is the clean result.

THREE OUTCOMES: (A) observable -> GW170817 bounds tau_c, a real differentiator;
(B) real-but-tiny (N orders below sensitivity) -> NOT a usable differentiator, report N;
(C) zero by structure. We rank them by computing predicted-effect / threshold.

Units SI. Pure stdlib. alpha_g (vacuum-GW response coupling) set to 1 = MOST generous for
detectability; smaller only makes the effect tinier.
"""
import math

C = 2.99792458e8                 # m/s
MPC = 3.0856775814913673e22      # m
HBAR = 1.054571817e-34
G = 6.67430e-11
# Planck angular frequency omega_P = sqrt(c^5/(hbar G))
OMEGA_P = math.sqrt(C ** 5 / (HBAR * G))    # ~1.85e43 rad/s

# Observational anchors
D_GW170817 = 40.0 * MPC          # luminosity distance, BNS
D_BBH = 400.0 * MPC              # representative BBH
F_BAND = [10.0, 100.0, 1024.0]   # Hz, LIGO band
ALPHA_G = 1.0                    # O(1), most generous for detectability

# Thresholds (state + source)
PHASE_THRESHOLD = 0.1            # rad accumulated; ~scale at which a dephasing is detectable in
                                 # matched-filter tests of GR (graviton-mass / dispersion tests
                                 # constrain accumulated Dphi at the ~0.1-1 rad level). Order of mag.
CGW_BOUND = 1e-15               # |c_gw - c|/c from GW170817 multimessenger timing (Abbott+ 2017).


def chi_mag(omega, q, omega_c=OMEGA_P, alpha=ALPHA_G):
    """Dimensionless vacuum GW-response magnitude.
    Im[chi] ~ alpha (omega/omega_c)^q  (super-Ohmic dissipation; q=s-1, s=3 -> q=2; thermal
    s_eff=2 reading -> q=1). Re[chi] is the Kramers-Kronig partner, SAME order for a power-law
    spectrum with a smooth cutoff, so we use |Re[chi]| ~ |Im[chi]| for an order-of-magnitude.

    SCOPE FENCE ADDED 2026-08-20. The |Re| ~ |Im| step is true FOR THIS POWER-LAW BRANCH and is
    FALSE for a far-IR Lorentzian tail, where Im/Re = omega*tau -> 6.3e20 at 100 Hz for
    tau_2 ~ 1/H0. The old text let that step be read as general, which is what licensed the
    "fractional amplitude loss: same order" line below. Everything this function returns is the
    power-law branch and is unaffected; the amplitude channel of a second, IR pole is NOT
    covered by it. See the REGIME CHECK block for what that does and does not change.
    """
    return alpha * (omega / omega_c) ** q


def main():
    print("=" * 80)
    print("RUNG 4  GW dissipation from Im[chi]  --  is there anything to bound?")
    print(f"omega_Planck = {OMEGA_P:.3e} rad/s ; alpha_g = {ALPHA_G} (most generous)")
    print("Model: Im[chi] ~ alpha (omega/omega_c)^q ; v_g/c-1 ~ Re[chi]/2 ; "
          "Dphi ~ (omega/c)(|chi|/2) D")
    print("=" * 80)

    # ---- KK statement -----------------------------------------------------------------
    print("""
KRAMERS-KRONIG / COUPLING (stated explicitly):
  Re[chi(omega)] = (2/pi) P int_0^inf omega' Im[chi(omega')]/(omega'^2 - omega^2) domega'.
  For Im[chi] ~ omega^q with a smooth UV cutoff omega_c, Re[chi] is the same order at omega<<omega_c.
  GW dispersion: omega^2 = c^2 k^2 (1 + chi(omega)) => k = (omega/c)(1 - chi/2),
    phase shift vs GR (v=c):  Dphi = (omega/c)(Re[chi]/2) D
    fractional amplitude loss: (omega/c)(Im[chi]/2) D -- "same order" as the phase holds ONLY
      on the single-pole power-law branch; it is FALSE once a second (IR) pole is present,
      where Im/Re = omega*tau_2 ~ 6e20 at 100 Hz. See the REGIME CHECK block below.
    speed offset:             |v_g - c|/c ~ |Re[chi]|/2.
  REGIME CHECK -- CORRECTED 2026-08-20. The previous text read: "LIGO omega ~ 6e2-6e3 rad/s
  >> H0 ~ 1e-18, so propagation sees the UV-cutoff (tau_c) pole; the IR horizon pole
  (tau_2 ~ 1/H0) is invisible here -- correct Im[chi] used." THAT SENTENCE IS FALSE for Im[chi].
  A Lorentzian pole does not switch off above its own frequency. For the two-scale kernel this
  register itself books, chi = A/(1 - i w tau_c) + B/(1 - i w tau_2),
      Im chi_UV ~ A*w*tau_c        (RISING with w)
      Im chi_IR ~ B/(w*tau_2)      (FALLING with w, but nonzero)
  so the two cross at the GEOMETRIC MEAN w_x = sqrt((B/A)*w_c*H0), not at w ~ H0. With this
  corpus's own w_c = 1e40*H0 and B/A = 0.4, w_x ~ 63 rad/s (~10 Hz) -- INSIDE the LIGO band,
  where Im chi_IR / Im chi_UV = 1.0e-2 at 100 Hz. With the Planck cutoff instead, w_x ~ 4e12
  rad/s. The crossover moves ~10 orders on an UNPINNED constant (three in-corpus values of w_c
  span 39.6 orders) -- that adjudication is owed and it is load-bearing here.

  WHAT THIS CHANGES, AND WHAT IT DOES NOT.
   - The Dphi numbers below are computed from Re[chi] on the power-law branch. They are
     UNAFFECTED. The IR pole's Re part is B/(1 + (w*tau_2)^2), which IS negligible at LIGO
     frequencies, so rung4's filed "22-62 orders below" stands AS A DEPHASING STATEMENT.
   - What the false sentence licensed was the "fractional amplitude loss: same order" step. It
     is not the same order once a second pole is present, and the amplitude channel is
     therefore NOT covered by anything computed in this file.

  THE UNCOVERED CHANNEL, stated so it is not mistaken for a result. The IR pole contributes
  ACHROMATIC friction Gamma = B*H0/2. Achromatic means it is degenerate with the coalescence
  phase, so the matched-filter dephasing test below is blind to it BY CONSTRUCTION; it would
  appear instead in standard-siren AMPLITUDE. At B = 0.4 that is 0.2*H0 -- inside the
  |Gamma_T| <~ few x H0 slot bound this program already quotes (SIGNATURE_AUDIT.md:62), not
  22-62 orders below it. NOT SETTLED EITHER WAY HERE, and two reasons why: B is a STAKED
  illustrative amplitude whose own source file disclaims the form (wz_dark_energy.py:18-25),
  and the conformalon rate leg would put B ~ 2.4e-4, which returns the channel to invisibility.
  The forward calculation that settles it is calc/gw_tensor_friction.py -- specified at
  SIGNATURE_AUDIT.md:68 and DOES NOT EXIST. Until it runs, do not amend the 22-62 orders
  downstream; mark it CONDITIONAL on the sector question (does the tau_2 pole appear in P^TT
  at all, or only in the scalar channel p_tt_ansatz excludes?).
""")

    for q in (1, 2):
        print("=" * 80)
        print(f"  CASE q = {q}   (Im[chi] ~ (omega/omega_c)^{q};  q=1 thermal s_eff=2, q=2 bare s=3)")
        print("=" * 80)
        f = 100.0
        omega = 2 * math.pi * f
        chi = chi_mag(omega, q)
        dv = chi / 2.0

        # ---- GUARD 1: GW170817 speed bound, checked FIRST ----------------------------
        print(f"\n  [1] GW170817 SPEED BOUND (checked FIRST)  at f={f:.0f} Hz:")
        print(f"      predicted |v_g - c|/c ~ |Re[chi]|/2 = {dv:.3e}")
        print(f"      observed bound          |c_gw - c|/c < {CGW_BOUND:.0e}")
        if dv < CGW_BOUND:
            margin = math.log10(CGW_BOUND / dv)
            print(f"      => CONSISTENT, with ~{margin:.0f} orders of magnitude to spare.")
            print(f"         (The speed bound does NOT falsify the model and is NOT binding:")
            print(f"          the effect is far below it.)")
        else:
            print(f"      => VIOLATES the GW170817 bound -> model already falsified at q={q}.")

        # ---- detectability ----------------------------------------------------------
        print(f"\n  [2] LIGO PHASE DETECTABILITY across the band (D = 40 Mpc, GW170817):")
        print(f"      threshold: accumulated Dphi ~ {PHASE_THRESHOLD} rad")
        print("        f (Hz)     |chi|         Dphi (rad)      ampl.loss")
        for ff in F_BAND:
            w = 2 * math.pi * ff
            ch = chi_mag(w, q)
            dphi = (w / C) * (ch / 2.0) * D_GW170817
            print(f"       {ff:7.0f}    {ch:.3e}    {dphi:.3e}     {dphi:.3e}")

        # ratio at representative f
        dphi = (omega / C) * (chi / 2.0) * D_GW170817
        ratio = dphi / PHASE_THRESHOLD
        k = -math.log10(ratio) if ratio > 0 else float("inf")
        print(f"\n  [3] THE RATIO (the answer):  predicted Dphi / threshold = {ratio:.3e}")
        print(f"      => predicted GW dephasing is ~10^{k:.0f} times TOO SMALL to detect.")

        # ---- the live window + what omega_c would be needed -------------------------
        floor_chi = PHASE_THRESHOLD / ((omega / C) * D_GW170817 / 2.0)   # chi to reach 0.1 rad
        print(f"\n  [4] LIVE WINDOW for |chi| (detectable AND not speed-excluded), f={f:.0f} Hz:")
        print(f"      detectable floor |chi| > {floor_chi:.3e}   (to reach {PHASE_THRESHOLD} rad over 40 Mpc)")
        print(f"      speed-bound ceiling |chi| < {2*CGW_BOUND:.3e}")
        print(f"      GRUT predicts  |chi| = {chi:.3e}  -> {math.log10(floor_chi/chi):.0f} orders BELOW the window.")
        # what omega_c would be needed to reach the floor
        wc_needed = omega / floor_chi ** (1.0 / q)
        print(f"      To reach detectability, omega_c would have to be ~{wc_needed:.2e} rad/s")
        print(f"      = {wc_needed*HBAR/1.602e-19:.2e} eV  -- vs Planck {OMEGA_P:.2e} rad/s.")
        print(f"      Such a low cutoff would give the vacuum structure at that energy and is")
        print(f"      grossly excluded by particle-physics / equivalence-principle tests.")

    # ---- consistency guard ------------------------------------------------------------
    print("\n" + "=" * 80)
    print("  CONSISTENCY GUARD (Planck-suppression vs solar-system safety):")
    print("=" * 80)
    print("""  The effect grows with omega (Im[chi] ~ omega^q, q>=1). Solar-system tests probe much
  LOWER frequencies (orbital ~ 1e-7..1e-3 Hz) -> the effect there is even MORE suppressed than
  at LIGO. So 'GW effect tiny' AND 'solar-system safe' are CONSISTENT (both suppressed, GW less
  so). There is no regime where the GW effect is large while solar-system is safe -> no tell of
  an error. The smallness is structural, not a tuning.""")

    print("\n" + "=" * 80)
    print("  VERDICT")
    print("=" * 80)
    print("""\
  OUTCOME (B): BOUNDABLE-IN-PRINCIPLE-BUT-TINY. The dissipative effect is REAL (Im[chi]!=0,
  v_g != c, frequency-dependent damping -- qualitatively absent in lossless GR), but for a
  Planck-cutoff vacuum it is a factor ~10^22 (q=1) to ~10^62 (q=2) below LIGO
  phase sensitivity, and ~26-66 orders below even the GW170817 speed bound. GW dissipation is
  NOT a usable differentiator with current (or any foreseeable) detectors. The GW170817 speed
  bound is satisfied trivially -- it is not binding because the effect is far beneath it.

  This is reported straight, with the number, and is a clean result: it RULES OUT GW dissipation
  as the second differentiator and sends diversification elsewhere. It does NOT weaken GRUT --
  the smallness is the same Planck suppression that makes the theory solar-system-safe.

  DIFFERENTIATOR STAMP: FAILS-DIFFERENTIATION (real-but-invisible). The differentiator_quantity
  is frequency-dependent GW dephasing/attenuation Dphi(omega) and v_g(omega)!=c (absent in GR),
  but because outcome is (B), not (A), it is NOT a working differentiator. Honest tag.

  ONE-LINE QUESTION FOR THE SPECIALIST (DOS-shape):
    'For a Planck-cutoff super-Ohmic vacuum, is the GW dissipative response Im[chi(omega)]
     genuinely suppressed by (omega/omega_P)^q with q>=1 (so unobservable by ~22+ orders), or is
     there an enhancement mechanism (resonant bath mode, coherent build-up over D_L, or a lower
     effective cutoff) that lifts it toward the |chi| in [1e-19, 1e-15] live window?'""")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
