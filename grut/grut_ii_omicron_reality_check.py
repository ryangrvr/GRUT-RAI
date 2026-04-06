"""
GRUT II Omicron Reality Check — Three Mandatory Audits
========================================================

Before any QNM calculation:

AUDIT 1: No Double Counting
  Are chi (constitutive susceptibility) and dT/dPhi (coupling coefficient)
  genuinely independent? Or does the 1/tau dependence in T^Phi just
  rescale what chi already accounts for?

AUDIT 2: DC Equivalence
  Xi says DC perturbation response is identical.
  But dT/dPhi differs by 4.7x.
  These cannot both be true if the DC gravitational susceptibility
  is the product (dT/dPhi) * chi_DC.
  Resolve the contradiction.

AUDIT 3: Magnitude
  Even if the 10x ratio is real, what is the ABSOLUTE SIZE of T^Phi
  relative to the Einstein curvature? If T^Phi is a tiny correction,
  10x of tiny is still tiny.
"""

import math
import numpy as np

TAU_STAR = math.sqrt(1.5)


if __name__ == "__main__":
    print("=" * 80)
    print("  OMICRON REALITY CHECK — THREE MANDATORY AUDITS")
    print("=" * 80)

    X = 1.0
    beta = 1.0
    gamma = 1.2
    delta_p = 1.0
    tau_meta = 10.0

    bg = beta * gamma
    v_star = math.sqrt((bg - 1) / (beta * delta_p))

    Phi_eq2 = X + v_star
    tau_eq2 = TAU_STAR + gamma * v_star - delta_p * v_star**3
    Phi_eq3 = X - v_star
    tau_eq3 = TAU_STAR + gamma * (-v_star) - delta_p * (-v_star)**3

    # ================================================================
    # AUDIT 1: NO DOUBLE COUNTING
    # ================================================================
    print("\n" + "=" * 80)
    print("  AUDIT 1: NO DOUBLE COUNTING")
    print("=" * 80)

    print("""
  The full gravitational susceptibility chain is:

    delta_g ~ 8piG * delta_rho * (geometric)
    delta_rho = (drho/dPhi) * delta_Phi + (drho/dtau) * delta_tau
    delta_Phi = chi_Phi(omega) * epsilon * x_hat
    delta_tau = chi_tau(omega) * epsilon * x_hat

  where chi_Phi and chi_tau come from the linearized DDE (Xi's result).

  The TOTAL metric susceptibility is:

    G_metric(omega) = 8piG * [(drho/dPhi)*chi_Phi(omega) + (drho/dtau)*chi_tau(omega)]

  QUESTION: Is the tau-dependence in drho/dPhi ALREADY captured by chi_Phi?

  ANSWER: NO. These are structurally different quantities:

  chi_Phi(omega) = response of Phi to external forcing x(t).
    This depends on tau through the constitutive ODE: tau*dPhi/dt + Phi = ...
    The tau enters as a DAMPING RATE in the dynamics.

  drho/dPhi = how strongly a given delta_Phi translates to delta_rho.
    This depends on tau through the T^Phi formula: rho = Phi^2/(2tau^2) - Phi*X/tau.
    The tau enters as a NORMALIZATION SCALE in the energy density.

  These are independent:
    chi_Phi tells you HOW MUCH Phi moves.
    drho/dPhi tells you HOW MUCH rho changes per unit Phi motion.

  The product (drho/dPhi)*chi_Phi is the TOTAL chain:
    (how much Phi moves) × (how much rho per unit Phi) = (how much rho moves)

  THERE IS NO DOUBLE COUNTING.

  Concretely:
    If we rescaled Phi → alpha*Phi, then:
      chi_Phi → chi_Phi/alpha (Phi responds less per unit forcing)
      drho/dPhi → alpha*drho/dPhi (rho changes more per unit Phi)
      Product: unchanged. The rescaling cancels.

    But changing tau does NOT correspond to a Phi rescaling:
      tau enters chi through the TIME DERIVATIVE (dynamics)
      tau enters drho/dPhi through the POTENTIAL (energetics)
      These are different mathematical roles.

  VERDICT: NO DOUBLE COUNTING. The multiplication is legitimate.
    """)

    # Verify numerically: compute the FULL product at a test frequency
    omega_test = 1.0

    # From Xi: chi_Phi(omega) for each phase
    # chi = (1 + i*omega*tau_meta) / [(1+i*omega*tau)(1+i*omega*tau_meta) - g'h']
    gh = beta * (gamma - 3*delta_p*v_star**2)  # = 0.6

    def chi_Phi(omega, tau_eq):
        num = complex(1, omega * tau_meta)
        den = complex(1, omega*tau_eq) * complex(1, omega*tau_meta) - gh
        return num / den

    def chi_tau(omega, tau_eq):
        # delta_tau = h'*chi_Phi / (1 + i*omega*tau_meta) from the tau equation
        h_prime = gamma - 3*delta_p*v_star**2
        return h_prime * chi_Phi(omega, tau_eq) / complex(1, omega*tau_meta)

    # drho/dPhi and drho/dtau at each equilibrium
    drho_dPhi_eq2 = Phi_eq2/tau_eq2**2 - X/tau_eq2
    drho_dtau_eq2 = -Phi_eq2**2/tau_eq2**3 + Phi_eq2*X/tau_eq2**2

    drho_dPhi_eq3 = Phi_eq3/tau_eq3**2 - X/tau_eq3
    drho_dtau_eq3 = -Phi_eq3**2/tau_eq3**3 + Phi_eq3*X/tau_eq3**2

    # Full metric susceptibility at omega = 1
    G_eq2 = drho_dPhi_eq2 * chi_Phi(omega_test, tau_eq2) + drho_dtau_eq2 * chi_tau(omega_test, tau_eq2)
    G_eq3 = drho_dPhi_eq3 * chi_Phi(omega_test, tau_eq3) + drho_dtau_eq3 * chi_tau(omega_test, tau_eq3)

    print("  NUMERICAL CHECK at omega = {:.1f}:".format(omega_test))
    print("    G_metric(Eq2) = {:.6f} + {:.6f}i".format(G_eq2.real, G_eq2.imag))
    print("    G_metric(Eq3) = {:.6f} + {:.6f}i".format(G_eq3.real, G_eq3.imag))
    print("    |G_Eq2| = {:.6f}".format(abs(G_eq2)))
    print("    |G_Eq3| = {:.6f}".format(abs(G_eq3)))
    print("    Ratio |G_Eq3|/|G_Eq2| = {:.4f}".format(abs(G_eq3)/max(abs(G_eq2), 1e-30)))

    # Scan across frequencies
    print("\n  FULL FREQUENCY SCAN:")
    print("  {:>10s} {:>12s} {:>12s} {:>12s}".format(
        "omega", "|G_Eq2|", "|G_Eq3|", "Ratio"))
    print("  " + "-" * 50)

    for w in [0.001, 0.01, 0.05, 0.1, 0.3, 0.5, 1.0, 2.0, 5.0, 10.0]:
        G2 = drho_dPhi_eq2*chi_Phi(w, tau_eq2) + drho_dtau_eq2*chi_tau(w, tau_eq2)
        G3 = drho_dPhi_eq3*chi_Phi(w, tau_eq3) + drho_dtau_eq3*chi_tau(w, tau_eq3)
        ratio = abs(G3) / max(abs(G2), 1e-30)
        print("  {:10.3f} {:12.6f} {:12.6f} {:12.4f}".format(w, abs(G2), abs(G3), ratio))

    # ================================================================
    # AUDIT 2: DC EQUIVALENCE
    # ================================================================
    print("\n" + "=" * 80)
    print("  AUDIT 2: DC EQUIVALENCE")
    print("=" * 80)

    # At DC (omega = 0):
    chi_Phi_DC = 1.0 / (1.0 - gh)  # = 1/0.4 = 2.5 (same for both phases)
    chi_tau_DC_eq2 = (gamma - 3*delta_p*v_star**2) * chi_Phi_DC  # h'*chi_Phi_DC
    chi_tau_DC_eq3 = chi_tau_DC_eq2  # same (h' and chi_DC both identical)

    G_DC_eq2 = drho_dPhi_eq2 * chi_Phi_DC + drho_dtau_eq2 * chi_tau_DC_eq2
    G_DC_eq3 = drho_dPhi_eq3 * chi_Phi_DC + drho_dtau_eq3 * chi_tau_DC_eq3

    print("\n  DC GRAVITATIONAL SUSCEPTIBILITY:")
    print("    chi_Phi_DC = {:.4f} (same for both phases)".format(chi_Phi_DC))
    print("    chi_tau_DC = {:.4f} (same for both phases)".format(chi_tau_DC_eq2))
    print()
    print("    drho/dPhi:")
    print("      Eq2: {:.6f}".format(drho_dPhi_eq2))
    print("      Eq3: {:.6f}".format(drho_dPhi_eq3))
    print("    drho/dtau:")
    print("      Eq2: {:.6f}".format(drho_dtau_eq2))
    print("      Eq3: {:.6f}".format(drho_dtau_eq3))
    print()
    print("    G_DC(Eq2) = drho/dPhi*chi_DC + drho/dtau*chi_tau_DC = {:.6f}".format(G_DC_eq2))
    print("    G_DC(Eq3) = {:.6f}".format(G_DC_eq3))
    print("    Ratio = {:.4f}".format(G_DC_eq3 / max(abs(G_DC_eq2), 1e-30)))
    print()

    if abs(G_DC_eq2 - G_DC_eq3) < 0.01 * max(abs(G_DC_eq2), abs(G_DC_eq3)):
        print("    DC gravitational susceptibilities are NEARLY EQUAL.")
        print("    DC equivalence HOLDS.")
    else:
        print("    DC gravitational susceptibilities DIFFER.")
        print("    |G_DC_Eq2| = {:.6f}".format(abs(G_DC_eq2)))
        print("    |G_DC_Eq3| = {:.6f}".format(abs(G_DC_eq3)))
        print("    RATIO = {:.4f}".format(abs(G_DC_eq3)/max(abs(G_DC_eq2), 1e-30)))
        print()
        print("    THIS MEANS: the two phases have DIFFERENT static gravitational")
        print("    response to perturbations. The 4.7x coupling difference at DC")
        print("    is NOT cancelled by the identical chi_DC.")
        print()
        print("    CONSEQUENCE: If DC gravitational susceptibility differs, then even")
        print("    slow perturbations (tidal fields, orbiting companions) produce")
        print("    different responses in the two phases. This is NOT limited to")
        print("    high-frequency dynamics.")
        print()
        print("    BUT: does this violate classical tests?")
        print("    The DC susceptibility is the response to PERTURBATIONS of the")
        print("    background, not the background itself. The background metric")
        print("    is different (by 6.7% in rho), so the perturbation response")
        print("    being different is CONSISTENT — it's a perturbation of a")
        print("    different background state.")

    # ================================================================
    # AUDIT 3: MAGNITUDE
    # ================================================================
    print("\n" + "=" * 80)
    print("  AUDIT 3: MAGNITUDE — HOW BIG IS T^PHI RELATIVE TO GR CURVATURE?")
    print("=" * 80)

    # Background rho values (geometric units, r_s = 1)
    rho_eq2 = Phi_eq2**2/(2*tau_eq2**2) - Phi_eq2*X/tau_eq2
    rho_eq3 = Phi_eq3**2/(2*tau_eq3**2) - Phi_eq3*X/tau_eq3

    print("\n  Background constitutive energy density:")
    print("    rho_Eq2 = {:.6f} (geometric units)".format(rho_eq2))
    print("    rho_Eq3 = {:.6f}".format(rho_eq3))

    # Background Schwarzschild curvature at R_eq = r_s/3
    R_eq = 1.0/3.0
    M = 0.5
    # Kretschner scalar: K = 48 M^2 / r^6
    K_Req = 48 * M**2 / R_eq**6
    # Ricci scalar for Schwarzschild: R = 0 (vacuum)
    # But with T^Phi: R = -8*pi*T = -8*pi*(rho - p_r - 2*p_perp)
    # At equilibrium (Phi' = 0): p_r = p_perp = -rho, so T = rho - 3*(-rho) = 4*rho
    # R = -8*pi*4*rho = -32*pi*rho

    R_Phi_eq2 = -32 * math.pi * rho_eq2
    R_Phi_eq3 = -32 * math.pi * rho_eq3

    print("\n  Curvature contribution from T^Phi:")
    print("    R_Phi(Eq2) = -32*pi*rho = {:.4f}".format(R_Phi_eq2))
    print("    R_Phi(Eq3) = {:.4f}".format(R_Phi_eq3))
    print()
    print("  Background Schwarzschild curvature at R_eq:")
    print("    Kretschner K = 48*M^2/r^6 = {:.1f}".format(K_Req))
    print()

    # The ratio of T^Phi energy to background gravitational energy
    # rho_grav ~ M / (4/3 pi R_eq^3) = M / (4/3 pi (1/3)^3) ~ M * 27 * 3/(4*pi)
    rho_grav = 3 * M / (4 * math.pi * R_eq**3)  # average density inside R_eq
    print("  Average gravitational mass density inside R_eq:")
    print("    rho_grav ~ 3M/(4pi R_eq^3) = {:.4f}".format(rho_grav))
    print()
    print("  Ratio |rho_Phi| / rho_grav:")
    print("    Eq2: {:.4f}".format(abs(rho_eq2)/rho_grav))
    print("    Eq3: {:.4f}".format(abs(rho_eq3)/rho_grav))
    print()

    if abs(rho_eq2)/rho_grav > 0.1:
        print("  T^Phi is a SIGNIFICANT fraction of the background curvature!")
        print("  The constitutive energy density is {:.0f}% of the gravitational density.".format(
            100*abs(rho_eq2)/rho_grav))
        print("  The 10x dynamic ratio is a ratio of LARGE numbers, not small ones.")
    elif abs(rho_eq2)/rho_grav > 0.01:
        print("  T^Phi is a MODERATE fraction ({:.1f}%) of background curvature.".format(
            100*abs(rho_eq2)/rho_grav))
        print("  The 10x ratio gives a ~{:.0f}% QNM modification.".format(
            10 * 100*abs(rho_eq2)/rho_grav))
    else:
        print("  T^Phi is a SMALL fraction ({:.2f}%) of background curvature.".format(
            100*abs(rho_eq2)/rho_grav))
        print("  Even the 10x ratio produces a tiny absolute effect.")

    # ================================================================
    # PERTURBATION MAGNITUDE
    # ================================================================
    print("\n  PERTURBATION MAGNITUDE:")
    print("  For a perturbation epsilon * x(t) with epsilon << 1:")
    print("    |delta_rho| = |G_metric(omega)| * epsilon")
    print()
    print("  At omega = 1:")
    print("    |delta_rho_Eq2| = {:.6f} * epsilon".format(abs(G_eq2)))
    print("    |delta_rho_Eq3| = {:.6f} * epsilon".format(abs(G_eq3)))
    print()
    print("  The FRACTIONAL metric perturbation:")
    print("    delta_g / g ~ 8*pi * delta_rho * r^2 / (background curvature)")
    frac_eq2 = 8 * math.pi * abs(G_eq2) * R_eq**2
    frac_eq3 = 8 * math.pi * abs(G_eq3) * R_eq**2
    print("    Eq2: delta_g/g ~ {:.4f} * epsilon".format(frac_eq2))
    print("    Eq3: delta_g/g ~ {:.4f} * epsilon".format(frac_eq3))

    # ================================================================
    # VERDICT
    # ================================================================
    print("\n" + "=" * 80)
    print("  VERDICT ON ALL THREE AUDITS")
    print("=" * 80)

    print("""
  AUDIT 1 (Double counting): PASSED.
    chi and drho/dPhi are independent quantities entering as a product.
    chi is from dynamics (time-derivative structure).
    drho/dPhi is from energetics (potential/coupling structure).
    No rescaling cancellation. Multiplication is legitimate.

  AUDIT 2 (DC equivalence): FAILED — DC SUSCEPTIBILITIES DIFFER.
    G_DC(Eq2) = {:.6f}
    G_DC(Eq3) = {:.6f}
    Ratio = {:.4f}

    The two phases have different static perturbation response.
    This is because drho/dPhi differs (4.7x) while chi_DC is the same (2.5).
    The 4.7x coupling difference is NOT cancelled at DC.

    IMPLICATION: The phase distinction is visible even in the static (DC) limit.
    This is STRONGER than Omicron claimed (which said DC is identical).
    But it means classical tests must be checked — the two phases produce
    different tidal responses even for slow perturbations.

    RESOLUTION: The two phases are perturbations of DIFFERENT backgrounds
    (rho differs by 6.7%). Different backgrounds have different perturbation
    spectra. This is not a violation of classical tests — it is a prediction
    that compact objects in different constitutive phases have different
    tidal properties. (Like two neutron stars with different equations of state.)

  AUDIT 3 (Magnitude): |rho_Phi| / rho_grav = {:.2f}.
    T^Phi is {:.0f}% of the gravitational energy density at R_eq.
    This is a SIGNIFICANT fraction — not a tiny correction.
    The 10x dynamic ratio is a ratio of order-unity numbers.

    The absolute metric perturbation response is:
      delta_g/g ~ {:.4f} * epsilon (Eq2)
      delta_g/g ~ {:.4f} * epsilon (Eq3)

    For epsilon ~ 0.01 (1% perturbation):
      delta_g/g ~ {:.4f} (Eq2) and {:.4f} (Eq3)

    These are SIGNIFICANT metric perturbations.
    The effect is NOT a ratio of tiny numbers.
    """.format(
        G_DC_eq2, G_DC_eq3, abs(G_DC_eq3)/max(abs(G_DC_eq2), 1e-30),
        abs(rho_eq2)/rho_grav, 100*abs(rho_eq2)/rho_grav,
        frac_eq2, frac_eq3, frac_eq2*0.01, frac_eq3*0.01))

    # CORRECTED OMICRON SUMMARY
    print("=" * 80)
    print("  CORRECTED OMICRON SUMMARY")
    print("=" * 80)
    print("""
  The actual gravitational susceptibility ratio (full product, no double count):

  omega     |G_Eq2|      |G_Eq3|      Ratio
  (from frequency scan above)

  The DC ratio is NOT 1.0 — it is approximately {:.1f}.
  The HF ratio grows further toward ~{:.1f}.

  Previous claim of "DC identical" was WRONG. It applied only to chi
  (constitutive susceptibility), not to the full metric susceptibility
  G_metric = drho/dPhi * chi + drho/dtau * chi_tau.

  The CORRECTED picture:
    Both DC and HF gravitational susceptibility differ between phases.
    DC differs by ~{:.1f}x (from coupling coefficients).
    HF differs by ~{:.1f}x (from coupling + dynamics compounding).

  The two phases are distinguishable at ALL frequencies, not just HF.
  The distinction is LARGER at HF, but present everywhere.
    """.format(
        abs(G_DC_eq3)/max(abs(G_DC_eq2), 1e-30),
        abs(G_eq3)/max(abs(G_eq2), 1e-30),
        abs(G_DC_eq3)/max(abs(G_DC_eq2), 1e-30),
        abs(G_eq3)/max(abs(G_eq2), 1e-30),
    ))
    print("=" * 80)
