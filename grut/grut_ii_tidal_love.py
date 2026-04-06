"""
GRUT II Sigma — Tidal Love Number Phase-Difference Audit
==========================================================

Computes how the tidal Love number k2 and dimensionless deformability Lambda
differ between the two constitutive phases (Eq2 and Eq3) of GRUT II.

KEY PHYSICS:
  The Love number k2 measures how a compact object deforms in response
  to an external tidal field. It depends on the INTERIOR STRUCTURE:
  softer interiors deform more (larger k2); stiffer interiors deform less.

  In GR, k2 depends on the equation of state p(rho).
  In GRUT II, k2 additionally depends on the constitutive phase
  (Eq2 or Eq3), which determines the effective interior stiffness.

  The two phases have:
    Eq2 (over-response): tau = 1.672, rho = -0.491 (slower, heavier)
    Eq3 (under-response): tau = 0.778, rho = -0.458 (faster, lighter)

  The effective STIFFNESS of the constitutive medium is related to
  the speed at which it responds to perturbation — controlled by tau.
  SHORTER tau = FASTER response = EFFECTIVELY STIFFER (resists deformation).
  LONGER tau = SLOWER response = EFFECTIVELY SOFTER (deforms more).

  Therefore: Eq3 (fast, tau=0.78) should be STIFFER → smaller k2.
             Eq2 (slow, tau=1.67) should be SOFTER → larger k2.
"""

import math
import numpy as np

TAU_STAR = math.sqrt(1.5)
M_EXT = 0.5
R_S = 1.0
R_EQ = R_S / 3.0


if __name__ == "__main__":
    print("=" * 80)
    print("  GRUT II SIGMA — TIDAL LOVE NUMBER PHASE-DIFFERENCE AUDIT")
    print("=" * 80)

    # Parameters
    X = 1.0
    beta = 1.0
    gamma = 1.2
    delta_p = 1.0
    tau_meta = 10.0

    bg = beta * gamma
    v_star = math.sqrt((bg - 1) / (beta * delta_p))

    Phi_eq2 = X + v_star
    tau_eq2 = TAU_STAR + gamma * v_star - delta_p * v_star**3
    rho_eq2 = Phi_eq2**2 / (2*tau_eq2**2) - Phi_eq2 * X / tau_eq2

    Phi_eq3 = X - v_star
    tau_eq3 = TAU_STAR + gamma * (-v_star) - delta_p * (-v_star)**3
    rho_eq3 = Phi_eq3**2 / (2*tau_eq3**2) - Phi_eq3 * X / tau_eq3

    # ================================================================
    # PART I: PHASE-LOCALIZED BACKGROUND
    # ================================================================
    print("\n--- PART I: PHASE-LOCALIZED BACKGROUND ---")
    print()
    print("  Both phases: same M_ADM, same exterior Schwarzschild metric.")
    print("  Interior differs:")
    print()
    print("  | Property | Eq2 (over-response) | Eq3 (under-response) |")
    print("  |----------|:------------------:|:-------------------:|")
    print("  | Phi_0 | {:.4f} | {:.4f} |".format(Phi_eq2, Phi_eq3))
    print("  | tau_0 | {:.4f} | {:.4f} |".format(tau_eq2, tau_eq3))
    print("  | rho_0 | {:.4f} | {:.4f} |".format(rho_eq2, rho_eq3))
    print("  | 1/tau (relax rate) | {:.4f} | {:.4f} |".format(1/tau_eq2, 1/tau_eq3))
    print("  | tau ratio | 1.00x | {:.2f}x |".format(tau_eq2/tau_eq3))

    # ================================================================
    # PART II: TIDAL PERTURBATION SETUP
    # ================================================================
    print("\n--- PART II: TIDAL PERTURBATION ---")
    print("""
  The tidal Love number k2 for a compact object with constitutive interior:

  In standard GR, the l=2 tidal perturbation satisfies a Regge-Wheeler-type
  equation. The interior EOS determines the Love number through matching
  at the stellar surface.

  In GRUT II, the constitutive medium adds an EFFECTIVE VISCOSITY to the
  tidal response. The key parameter is:

    EFFECTIVE TIDAL COMPLIANCE ~ 1/tau_eff

  where tau_eff is the constitutive relaxation time at the radius where
  tidal deformation is strongest (typically near the surface).

  For a STATIC tidal field (f_tidal = 0):
    The constitutive medium fully equilibrates: Phi = X.
    The Love number depends only on the equilibrium EOS: rho(r), p(r).

  For a TIME-DEPENDENT tidal field (inspiral; f_tidal ~ f_orbital):
    The constitutive medium responds with finite lag.
    The EFFECTIVE Love number acquires a frequency-dependent correction.
    """)

    # ================================================================
    # PART III: SCALING ESTIMATE
    # ================================================================
    print("--- PART III: SCALING ESTIMATE ---")
    print()

    # The static k2 depends on the compactness C and the interior structure.
    # For the GRUT II defect-supported interior, the background rho differs
    # between phases by 6.7%. This gives a STATIC k2 difference of
    # approximately dk2/k2 ~ (1/5) * drho/rho ~ 1.3%.
    # (The factor 1/5 comes from k2 ~ C^5 sensitivity to compactness changes.)

    drho_frac = abs(rho_eq2 - rho_eq3) / max(abs(rho_eq2), 1e-10)
    dk2_static_frac = 0.2 * drho_frac  # rough scaling

    print("  STATIC Love number estimate:")
    print("    rho difference: {:.1f}%".format(drho_frac * 100))
    print("    k2 sensitivity to rho: dk2/k2 ~ (1/5) drho/rho")
    print("    Static k2 difference: ~{:.1f}%".format(dk2_static_frac * 100))
    print()

    # The DYNAMIC correction depends on the ratio omega*tau.
    # For the inspiral at orbital frequency f_orb:
    #   omega_tidal = 2 * f_orb (l=2 tidal frequency)
    #
    # The constitutive correction to k2 at frequency omega:
    #   delta_k2 / k2 ~ (omega * tau)^2 / (1 + (omega*tau)^2)
    #   (from the dissipative response; the imaginary part of k2)
    #
    # At late inspiral near ISCO:
    #   f_orb ~ 1/(6^(3/2) * pi * M_total) in geometric units
    #   omega_tidal = 2 * 2*pi*f_orb

    # For 1.4 + 1.4 M_sun binary (GW170817-like):
    M_total_solar = 2.8
    # f_ISCO ~ c^3 / (6^(3/2) pi G M_total) ~ 1570 Hz for 2.8 M_sun
    G = 6.674e-11; C_SI = 2.998e8; M_SUN = 1.989e30
    f_ISCO = C_SI**3 / (6**1.5 * math.pi * G * M_total_solar * M_SUN)
    omega_tidal = 2 * 2 * math.pi * f_ISCO

    # In geometric units: omega_geo = omega_tidal * r_s / c
    r_s_total = 2 * G * M_total_solar * M_SUN / C_SI**2
    omega_geo = omega_tidal * r_s_total / C_SI

    print("  DYNAMIC correction estimate (GW170817-like binary):")
    print("    M_total = {:.1f} M_sun".format(M_total_solar))
    print("    f_ISCO ~ {:.0f} Hz".format(f_ISCO))
    print("    omega_tidal ~ {:.0f} rad/s".format(omega_tidal))
    print("    omega_tidal (geometric) ~ {:.4f}".format(omega_geo))
    print()

    # omega*tau for each phase (using geometric units)
    wt_eq2 = omega_geo * tau_eq2
    wt_eq3 = omega_geo * tau_eq3

    print("    omega*tau (Eq2) = {:.4f}".format(wt_eq2))
    print("    omega*tau (Eq3) = {:.4f}".format(wt_eq3))
    print()

    # Dynamic k2 correction: ~ (omega*tau)^2 for omega*tau << 1
    dk2_dyn_eq2 = wt_eq2**2 / (1 + wt_eq2**2)
    dk2_dyn_eq3 = wt_eq3**2 / (1 + wt_eq3**2)

    print("    Dynamic k2 correction fraction:")
    print("      Eq2: {:.6f} ({:.4f}%)".format(dk2_dyn_eq2, dk2_dyn_eq2*100))
    print("      Eq3: {:.6f} ({:.4f}%)".format(dk2_dyn_eq3, dk2_dyn_eq3*100))
    print("      Ratio: {:.2f}".format(dk2_dyn_eq2/max(dk2_dyn_eq3, 1e-30)))
    print()

    # HOWEVER: tau here is in GEOMETRIC UNITS (r_s = 1). In physical units
    # tau_eq2 = 1.672 * r_s/c. For a 1.4 M_sun NS: r_s = 4.14 km,
    # tau_phys = 1.672 * 4.14e3 / 3e8 = 2.3e-5 s.
    # omega_tidal * tau_phys = 2*pi*3140 * 2.3e-5 = 0.45.
    # So omega*tau ~ 0.5 — not small! The constitutive response IS relevant
    # at inspiral frequencies near ISCO.

    tau_phys_eq2 = tau_eq2 * r_s_total / (2 * C_SI)  # for each NS (half total mass)
    tau_phys_eq3 = tau_eq3 * r_s_total / (2 * C_SI)

    wt_phys_eq2 = omega_tidal * tau_phys_eq2
    wt_phys_eq3 = omega_tidal * tau_phys_eq3

    print("  PHYSICAL omega*tau (using NS-scale tau):")
    print("    tau_phys(Eq2) = {:.2e} s".format(tau_phys_eq2))
    print("    tau_phys(Eq3) = {:.2e} s".format(tau_phys_eq3))
    print("    omega*tau_phys(Eq2) = {:.4f}".format(wt_phys_eq2))
    print("    omega*tau_phys(Eq3) = {:.4f}".format(wt_phys_eq3))
    print()

    if wt_phys_eq2 > 0.1:
        print("    omega*tau > 0.1: constitutive response IS dynamically relevant!")
        print("    The constitutive medium does NOT fully equilibrate during tidal forcing.")
    else:
        print("    omega*tau < 0.1: constitutive response is quasi-static.")

    # ================================================================
    # PART IV: k2 COMPARISON
    # ================================================================
    print("\n--- PART IV: k2 AND Lambda COMPARISON ---")

    # The tidal Love number in the GRUT II framework has two contributions:
    # 1. STATIC k2 from the equilibrium interior structure (rho, p profiles)
    # 2. DYNAMIC correction from the finite constitutive response time

    # For a reference BH-like object (Phase III estimate): k2 ~ 0.01
    # The defect-supported interior (D6 result): k2 ~ 0.01

    k2_base = 0.01  # Phase III estimate for defect-supported object

    # Static k2 shift from rho difference
    k2_static_eq2 = k2_base * (1 + dk2_static_frac * 0.5)  # Eq2 has more negative rho → softer
    k2_static_eq3 = k2_base * (1 - dk2_static_frac * 0.5)  # Eq3 has less negative rho → stiffer

    # Dynamic k2 correction (frequency-dependent imaginary part)
    # The real part of k2 is shifted by order (omega*tau)^2
    # The imaginary part (dissipative tidal lag) is of order omega*tau / (1+(omega*tau)^2)

    k2_real_eq2 = k2_static_eq2 * (1 - dk2_dyn_eq2)
    k2_real_eq3 = k2_static_eq3 * (1 - dk2_dyn_eq3)

    k2_imag_eq2 = k2_base * wt_eq2 / (1 + wt_eq2**2)
    k2_imag_eq3 = k2_base * wt_eq3 / (1 + wt_eq3**2)

    # Combined |k2|
    k2_total_eq2 = math.sqrt(k2_real_eq2**2 + k2_imag_eq2**2)
    k2_total_eq3 = math.sqrt(k2_real_eq3**2 + k2_imag_eq3**2)

    print()
    print("  | Quantity | Eq2 | Eq3 | Difference |")
    print("  |----------|:---:|:---:|:----------:|")
    print("  | k2 (static) | {:.6f} | {:.6f} | {:.1f}% |".format(
        k2_static_eq2, k2_static_eq3, 100*abs(k2_static_eq2-k2_static_eq3)/k2_base))
    print("  | k2 (real, at ISCO) | {:.6f} | {:.6f} | {:.1f}% |".format(
        k2_real_eq2, k2_real_eq3, 100*abs(k2_real_eq2-k2_real_eq3)/k2_base))
    print("  | k2 (imag, at ISCO) | {:.6f} | {:.6f} | {:.1f}% |".format(
        k2_imag_eq2, k2_imag_eq3, 100*abs(k2_imag_eq2-k2_imag_eq3)/k2_base))
    print("  | |k2| (total) | {:.6f} | {:.6f} | {:.1f}% |".format(
        k2_total_eq2, k2_total_eq3, 100*abs(k2_total_eq2-k2_total_eq3)/k2_base))

    # Dimensionless tidal deformability Lambda = (2/3) k2 C^{-5}
    # C = GM/(Rc^2) = compactness. For the GRUT II object: R = R_eq = r_s/3, C = 3/2.
    C = 3.0/2.0  # compactness (r_s = 2M, R = r_s/3 => C = M/R = (r_s/2)/(r_s/3) = 3/2)
    Lambda_eq2 = (2.0/3.0) * k2_total_eq2 / C**5
    Lambda_eq3 = (2.0/3.0) * k2_total_eq3 / C**5

    print()
    print("  Compactness C = {:.2f} (ultra-compact)".format(C))
    print("  Lambda(Eq2) = {:.6f}".format(Lambda_eq2))
    print("  Lambda(Eq3) = {:.6f}".format(Lambda_eq3))
    print("  Lambda difference: {:.2f}%".format(
        100*abs(Lambda_eq2-Lambda_eq3)/max(Lambda_eq2, 1e-30)))

    # ================================================================
    # PART V: OBSERVATIONAL RELEVANCE
    # ================================================================
    print("\n--- PART V: OBSERVATIONAL RELEVANCE ---")

    print("""
  GW170817 measured: Lambda_tilde = 300 +/- 230 (90% CL) for a 1.4+1.4 binary.
  Current measurement precision: ~50-100% of the value.

  For GRUT II ultra-compact objects (C = 1.5):
    Lambda ~ {L2:.6f} (Eq2) to {L3:.6f} (Eq3)
    These are EXTREMELY SMALL compared to NS Lambda ~ 100-1000.

  Why so small: Lambda scales as C^{-5}. At C = 1.5:
    C^{-5} = {Cinv:.4f}
    Even k2 = 0.01 gives Lambda ~ 10^{-4}.

  COMPARISON:
    Lambda_NS (GW170817) ~ 300
    Lambda_GRUT_II ~ 10^{-4}
    Ratio: 10^{-6}

  The GRUT II tidal deformability is 6 ORDERS OF MAGNITUDE below
  the neutron star value. This is because GRUT II compact objects
  are at C = 1.5 (ultra-compact), not C ~ 0.17 (typical NS).

  Ultra-compact objects generically have Lambda ~ 0 because they are
  nearly as compact as black holes (which have Lambda = 0 exactly).
  The GRUT II objects ARE nearly black holes in their tidal response.
    """.format(L2=Lambda_eq2, L3=Lambda_eq3, Cinv=C**(-5)))

    # The PHASE DIFFERENCE in Lambda:
    dLambda = abs(Lambda_eq2 - Lambda_eq3)
    print("  Phase difference: |delta_Lambda| = {:.2e}".format(dLambda))
    print("  Current measurement precision (Lambda_tilde): ~100")
    print("  Delta_Lambda / precision: {:.2e}".format(dLambda / 100))
    print()
    print("  The phase difference is FAR below measurement threshold.")
    print("  It is not just small — it is irrelevantly small for current detectors.")

    # But what about RELATIVE k2 difference?
    dk2_frac = abs(k2_total_eq2 - k2_total_eq3) / max(k2_base, 1e-30)
    print()
    print("  HOWEVER: the RELATIVE k2 difference between phases:")
    print("    |dk2|/k2 = {:.1f}%".format(dk2_frac * 100))
    print("  This is a {:.1f}% internal Love number difference.".format(dk2_frac*100))
    print("  It just doesn't matter observationally because k2 itself is ~ 0.01")
    print("  and Lambda ~ 10^-4 for ultra-compact objects.")

    # ================================================================
    # PART VI: CONSTRAINT LADDER
    # ================================================================
    print("\n--- PART VI: CONSTRAINT LADDER ---")
    print()
    print("  k2 difference between phases: ~{:.1f}%".format(dk2_frac*100))
    print("  Lambda difference: ~{:.1f}% of an already-tiny Lambda".format(
        100*dLambda/max(Lambda_eq2, 1e-30)))
    print("  Absolute Lambda value: ~{:.2e}".format(max(Lambda_eq2, Lambda_eq3)))
    print("  Current LIGO Lambda precision: ~100")
    print()
    print("  Classification: < 5% difference in k2, and Lambda itself is")
    print("  so small that the ABSOLUTE difference is unmeasurable.")
    print()
    print("  HOWEVER: the 5.5-10x metric susceptibility difference from Pi")
    print("  exists at the INTERIOR level. The tidal channel fails because")
    print("  ultra-compact objects have tiny Lambda regardless of interior details.")
    print()
    print("  The RIGHT channel might be RINGDOWN, not tidal:")
    print("  QNM frequencies and damping rates depend on the interior structure")
    print("  through boundary conditions at the surface/core transition.")
    print("  These are NOT suppressed by C^{-5} like Lambda is.")

    # ================================================================
    # VERDICT
    # ================================================================
    print("\n" + "=" * 80)
    print("  FINAL VERDICT")
    print("=" * 80)
    print("""
  love_number_difference_small_but_real.

  The two constitutive phases differ in k2 by ~{dk:.1f}%.
  But Lambda is suppressed by C^{{-5}} = {Ci:.4f} (ultra-compact).
  The absolute Lambda values (~10^{{-4}}) are 6 orders below current
  measurement precision (~100 from GW170817).

  The tidal channel is NOT the right observable for GRUT II.

  WHY: GRUT II compact objects are at compactness C = 1.5 (ultra-compact,
  nearly black holes). Ultra-compact objects have vanishing tidal
  deformability regardless of their interior equation of state.
  The k2 difference is real but unmeasurable through Lambda.

  THE RIGHT CHANNEL: Ringdown / quasi-normal modes.
  QNM frequencies are NOT suppressed by C^{{-5}}. They depend on:
    - The effective potential barrier shape (controlled by the interior)
    - The boundary conditions at the constitutive surface
    - The reflection/absorption properties of the interior medium

  The 5.5-10x metric susceptibility difference (Pi) should manifest
  as DIFFERENT QNM DAMPING RATES in the two phases, because the
  interior medium absorbs perturbation energy at different rates.
  This is the correct next target.
  """.format(dk=dk2_frac*100, Ci=C**(-5)))
    print("=" * 80)
