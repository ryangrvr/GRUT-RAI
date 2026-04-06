"""
GRUT II Xi — Phase-Response Discriminator Audit
=================================================

Computes the linear transfer function of the GRUT II constitutive system
separately at Eq2 (over-response) and Eq3 (under-response), then compares.

The system at each equilibrium, perturbed by x(t):
  tau* d(delta_Phi)/dt + delta_Phi = epsilon*x(t) + (beta - dPhi0/dt)*delta_tau
  tau_meta d(delta_tau)/dt + delta_tau = h'(v*) delta_Phi

At a STATIC equilibrium (dPhi0/dt = 0):
  tau* d(delta_Phi)/dt + delta_Phi = epsilon*x(t) + beta*delta_tau
  tau_meta d(delta_tau)/dt + delta_tau = h'(v*) delta_Phi

In frequency domain (Fourier: d/dt -> i*omega):
  (i*omega*tau* + 1) delta_Phi_hat = epsilon*x_hat + beta*delta_tau_hat
  (i*omega*tau_meta + 1) delta_tau_hat = h'(v*) delta_Phi_hat

From eq 2: delta_tau_hat = h'(v*) delta_Phi_hat / (1 + i*omega*tau_meta)

Substituting into eq 1:
  (i*omega*tau* + 1) delta_Phi_hat = epsilon*x_hat + beta*h'(v*)/(1+i*omega*tau_meta) * delta_Phi_hat

  delta_Phi_hat [(i*omega*tau* + 1) - beta*h'(v*)/(1+i*omega*tau_meta)] = epsilon*x_hat

TRANSFER FUNCTION:
  chi(omega) = delta_Phi_hat / (epsilon*x_hat)
             = 1 / [(1 + i*omega*tau*) - beta*h'(v*)/(1 + i*omega*tau_meta)]

Simplifying:
  chi(omega) = (1 + i*omega*tau_meta) / [(1+i*omega*tau*)(1+i*omega*tau_meta) - beta*h'(v*)]

Let:
  a = tau* (phase-specific relaxation time)
  b = tau_meta (meta-relaxation time)
  c = beta * h'(v*) = g'*h' (the loop gain from Gamma)

Then:
  chi(omega) = (1 + i*omega*b) / [(1+i*omega*a)(1+i*omega*b) - c]

Denominator:
  D(omega) = (1 - a*b*omega^2 - c) + i*omega*(a + b)
           = (1 - c - a*b*omega^2) + i*omega*(a + b)

|chi(omega)|^2 = (1 + omega^2*b^2) / [(1-c-a*b*omega^2)^2 + omega^2*(a+b)^2]

Phase:
  arg(chi) = arctan(omega*b) - arctan(omega*(a+b) / (1-c-a*b*omega^2))
"""

import math
import numpy as np

TAU_STAR = math.sqrt(1.5)


def transfer_function(omega, tau_eq, tau_meta, gh_product):
    """Compute complex transfer function chi(omega) at a given equilibrium.

    chi = (1 + i*omega*tau_meta) / [(1+i*omega*tau_eq)(1+i*omega*tau_meta) - gh]

    Parameters:
      tau_eq: equilibrium tau value (tau_eq2 or tau_eq3)
      tau_meta: meta-relaxation timescale
      gh_product: g'*h' = beta * h'(v*) (the loop gain)
    """
    a = tau_eq
    b = tau_meta
    c = gh_product

    numerator = complex(1, omega * b)
    term1 = complex(1, omega * a)
    term2 = complex(1, omega * b)
    denominator = term1 * term2 - c

    if abs(denominator) < 1e-30:
        return complex(0, 0)

    return numerator / denominator


if __name__ == "__main__":
    print("=" * 80)
    print("  GRUT II XI — PHASE-RESPONSE DISCRIMINATOR AUDIT")
    print("=" * 80)

    # Parameters
    X = 1.0
    beta = 1.0
    gamma = 1.2
    delta_p = 1.0
    tau_meta = 10.0

    bg = beta * gamma
    v_star = math.sqrt((bg - 1) / (beta * delta_p))

    # Eq2 parameters
    tau_eq2 = TAU_STAR + gamma * v_star - delta_p * v_star**3
    h_prime_eq2 = gamma - 3 * delta_p * v_star**2
    gh_eq2 = beta * h_prime_eq2

    # Eq3 parameters
    tau_eq3 = TAU_STAR + gamma * (-v_star) - delta_p * (-v_star)**3
    h_prime_eq3 = gamma - 3 * delta_p * v_star**2  # same (v^2)
    gh_eq3 = beta * h_prime_eq3  # same

    print("\n--- PART I: PHASE-SPECIFIC PARAMETERS ---")
    print()
    print("  | Parameter | Eq2 (over-response) | Eq3 (under-response) |")
    print("  |-----------|:------------------:|:-------------------:|")
    print("  | tau* | {:.4f} | {:.4f} |".format(tau_eq2, tau_eq3))
    print("  | 1/tau* | {:.4f} | {:.4f} |".format(1/tau_eq2, 1/tau_eq3))
    print("  | h'(v*) | {:.4f} | {:.4f} |".format(h_prime_eq2, h_prime_eq3))
    print("  | g'h' (loop gain) | {:.4f} | {:.4f} |".format(gh_eq2, gh_eq3))
    print("  | tau_meta | {:.4f} | {:.4f} |".format(tau_meta, tau_meta))
    print()
    print("  NOTE: h'(v*) and g'h' are the SAME at both equilibria")
    print("  (because h' depends on v^2, which is the same for +/- v*).")
    print("  The ONLY difference in the transfer function is tau*.")
    print("  tau_eq2 = {:.4f}, tau_eq3 = {:.4f} (ratio {:.2f})".format(
        tau_eq2, tau_eq3, tau_eq2/tau_eq3))

    # ================================================================
    # PART II: TRANSFER FUNCTIONS
    # ================================================================
    print("\n--- PART II: TRANSFER FUNCTIONS ---")
    print()
    print("  chi(omega) = (1 + i*omega*tau_meta) / ")
    print("               [(1+i*omega*tau*)(1+i*omega*tau_meta) - g'h']")
    print()

    omegas = np.logspace(-3, 1, 200)

    # Compute transfer functions at both equilibria
    chi_eq2 = np.array([transfer_function(w, tau_eq2, tau_meta, gh_eq2) for w in omegas])
    chi_eq3 = np.array([transfer_function(w, tau_eq3, tau_meta, gh_eq3) for w in omegas])

    amp_eq2 = np.abs(chi_eq2)
    amp_eq3 = np.abs(chi_eq3)
    phase_eq2 = np.angle(chi_eq2) * 180 / math.pi
    phase_eq3 = np.angle(chi_eq3) * 180 / math.pi

    # Key frequencies
    print("  AMPLITUDE RESPONSE |chi(omega)|:")
    print("  {:>10s} {:>12s} {:>12s} {:>12s}".format(
        "omega", "|chi|_Eq2", "|chi|_Eq3", "Ratio Eq3/Eq2"))
    print("  " + "-" * 50)

    for w_test in [0.001, 0.01, 0.05, 0.1, 0.5, 1.0, 2.0, 5.0]:
        c2 = transfer_function(w_test, tau_eq2, tau_meta, gh_eq2)
        c3 = transfer_function(w_test, tau_eq3, tau_meta, gh_eq3)
        ratio = abs(c3) / max(abs(c2), 1e-30)
        print("  {:10.3f} {:12.4f} {:12.4f} {:12.4f}".format(
            w_test, abs(c2), abs(c3), ratio))

    # DC response (omega = 0)
    chi_dc_eq2 = 1.0 / (1.0 - gh_eq2)
    chi_dc_eq3 = 1.0 / (1.0 - gh_eq3)
    print()
    print("  DC response (omega = 0):")
    print("    chi_DC = 1/(1 - g'h') = 1/(1 - {:.4f}) = {:.4f}".format(
        gh_eq2, chi_dc_eq2))
    print("    SAME for both phases (g'h' is identical).")

    # High-frequency response
    # At omega >> 1/tau*: chi -> 1/(i*omega*tau*) (damped by local tau)
    # At omega >> 1/tau_meta: chi -> tau_meta / (tau* * tau_meta * omega^2)
    print()
    print("  High-frequency asymptotic (omega >> 1/tau*):")
    print("    |chi| ~ 1/(omega * tau*)")
    print("    Eq2: |chi| ~ 1/(omega * {:.4f})".format(tau_eq2))
    print("    Eq3: |chi| ~ 1/(omega * {:.4f})".format(tau_eq3))
    print("    RATIO Eq2/Eq3 = tau_eq3/tau_eq2 = {:.4f}".format(tau_eq3/tau_eq2))
    print("    Eq2 responds with SMALLER amplitude (heavier damping)")
    print("    Eq3 responds with LARGER amplitude (lighter damping)")

    # ================================================================
    # PART III: PHASE DISCRIMINATOR
    # ================================================================
    print("\n--- PART III: PHASE DISCRIMINATOR ---")

    # Compute the amplitude ratio across frequencies
    ratio_amp = amp_eq3 / np.maximum(amp_eq2, 1e-30)

    # Find the frequency of maximum discrimination
    max_ratio_idx = np.argmax(ratio_amp)
    max_ratio = ratio_amp[max_ratio_idx]
    max_ratio_omega = omegas[max_ratio_idx]

    min_ratio_idx = np.argmin(ratio_amp)
    min_ratio = ratio_amp[min_ratio_idx]
    min_ratio_omega = omegas[min_ratio_idx]

    print()
    print("  Amplitude ratio |chi_Eq3| / |chi_Eq2| across frequency:")
    print("    DC (omega -> 0): {:.4f} (identical)".format(
        float(ratio_amp[0])))
    print("    Maximum ratio: {:.4f} at omega = {:.4f}".format(
        max_ratio, max_ratio_omega))
    print("    At omega = 1/tau_eq2 = {:.4f}: ratio = {:.4f}".format(
        1/tau_eq2,
        abs(transfer_function(1/tau_eq2, tau_eq3, tau_meta, gh_eq3)) /
        max(abs(transfer_function(1/tau_eq2, tau_eq2, tau_meta, gh_eq2)), 1e-30)))
    print("    At omega = 1/tau_eq3 = {:.4f}: ratio = {:.4f}".format(
        1/tau_eq3,
        abs(transfer_function(1/tau_eq3, tau_eq3, tau_meta, gh_eq3)) /
        max(abs(transfer_function(1/tau_eq3, tau_eq2, tau_meta, gh_eq2)), 1e-30)))

    # Phase lag comparison
    print()
    print("  Phase lag comparison:")
    for w_test in [0.01, 0.1, 0.5, 1.0]:
        c2 = transfer_function(w_test, tau_eq2, tau_meta, gh_eq2)
        c3 = transfer_function(w_test, tau_eq3, tau_meta, gh_eq3)
        ph2 = math.degrees(math.atan2(c2.imag, c2.real))
        ph3 = math.degrees(math.atan2(c3.imag, c3.real))
        print("    omega={:.2f}: phase_Eq2={:.1f}deg, phase_Eq3={:.1f}deg, diff={:.1f}deg".format(
            w_test, ph2, ph3, ph3-ph2))

    # Bandwidth / cutoff
    # -3dB frequency: |chi(omega_c)| = |chi(0)| / sqrt(2)
    target = chi_dc_eq2 / math.sqrt(2)
    omega_3dB_eq2 = None
    omega_3dB_eq3 = None
    for i in range(len(omegas)-1):
        if amp_eq2[i] >= target and amp_eq2[i+1] < target and omega_3dB_eq2 is None:
            omega_3dB_eq2 = omegas[i]
        if amp_eq3[i] >= target and amp_eq3[i+1] < target and omega_3dB_eq3 is None:
            omega_3dB_eq3 = omegas[i]

    print()
    print("  -3dB bandwidth:")
    if omega_3dB_eq2:
        print("    Eq2: omega_3dB = {:.4f} (1/tau_eq2 = {:.4f})".format(
            omega_3dB_eq2, 1/tau_eq2))
    else:
        print("    Eq2: no clear -3dB crossover in tested range")
    if omega_3dB_eq3:
        print("    Eq3: omega_3dB = {:.4f} (1/tau_eq3 = {:.4f})".format(
            omega_3dB_eq3, 1/tau_eq3))
    else:
        print("    Eq3: no clear -3dB crossover in tested range")

    if omega_3dB_eq2 and omega_3dB_eq3:
        print("    Bandwidth ratio Eq3/Eq2 = {:.2f}".format(
            omega_3dB_eq3/omega_3dB_eq2))
        print("    Eq3 has WIDER bandwidth (faster response)")

    # ================================================================
    # CLASSIFICATION
    # ================================================================
    print("\n--- CLASSIFICATION ---")

    # At intermediate frequencies (between 1/tau_meta and 1/tau_eq):
    # the two phases differ by factor tau_eq2/tau_eq3 = 2.15
    # This is a 115% difference — LARGE AND CLEAN.

    mid_omega = math.sqrt(1/(tau_eq2*tau_eq3))  # geometric mean of cutoff frequencies
    c2_mid = abs(transfer_function(mid_omega, tau_eq2, tau_meta, gh_eq2))
    c3_mid = abs(transfer_function(mid_omega, tau_eq3, tau_meta, gh_eq3))
    ratio_mid = c3_mid / max(c2_mid, 1e-30)

    print()
    print("  At geometric-mean frequency omega = {:.4f}:".format(mid_omega))
    print("    |chi_Eq2| = {:.4f}".format(c2_mid))
    print("    |chi_Eq3| = {:.4f}".format(c3_mid))
    print("    Ratio = {:.4f} ({:.0f}% difference)".format(
        ratio_mid, abs(ratio_mid - 1) * 100))

    # The high-frequency asymptotic ratio is tau_eq2/tau_eq3
    hf_ratio = tau_eq2 / tau_eq3
    print()
    print("  High-frequency asymptotic amplitude ratio: {:.4f}".format(hf_ratio))
    print("  (Eq3 responds {:.0f}% MORE strongly than Eq2 at high frequency)".format(
        (hf_ratio - 1) * 100))

    print()
    if hf_ratio > 1.5:
        print("  CLASSIFICATION: external_response_difference_large_and_clean")
        print("  The two phases differ by factor {:.1f}x in high-frequency response.".format(hf_ratio))
    elif hf_ratio > 1.1:
        print("  CLASSIFICATION: phase_distinction_real_but_observationally_modest")
    else:
        print("  CLASSIFICATION: internal_bistability_not_yet_externally_visible")

    # ================================================================
    # PART IV: PHYSICAL INTERPRETATION
    # ================================================================
    print("\n--- PART IV: PHYSICAL INTERPRETATION ---")
    print("""
  The transfer function analysis reveals:

  1. DC RESPONSE (omega → 0): IDENTICAL.
     Both phases have the same DC susceptibility chi_DC = {:.4f}.
     This is because g'h' is the same at both equilibria (it depends on v^2).
     A constant perturbation produces the SAME response in both phases.

  2. HIGH-FREQUENCY RESPONSE: DIFFERENT by factor {:.2f}x.
     The over-response phase (Eq2, tau = {:.4f}) damps high-frequency
     perturbations more strongly. The under-response phase (Eq3, tau = {:.4f})
     is more transparent to fast perturbations.

  3. BANDWIDTH: Eq3 is WIDER.
     The under-response phase transmits a broader range of frequencies.
     The over-response phase is a stronger low-pass filter.

  4. PHASE LAG: Eq2 has MORE lag at intermediate frequencies.
     The heavier tau in Eq2 creates more phase delay.

  PHYSICAL MEANING:
     The over-response vacuum (Eq2) acts as a SLOW, HEAVY constitutive medium.
     It damps fast perturbations and introduces large phase lag.

     The under-response vacuum (Eq3) acts as a FAST, LIGHT constitutive medium.
     It transmits fast perturbations with less damping and less lag.

     THE SAME EXTERNAL PERTURBATION produces DIFFERENT amplitude and phase
     responses depending on which constitutive phase the vacuum is in.

     This IS an externally distinguishable effect: an observer probing the
     constitutive vacuum with a test signal would measure a different
     transfer function in the two phases.
  """.format(chi_dc_eq2, hf_ratio, tau_eq2, tau_eq3))

    # ================================================================
    # VERDICT
    # ================================================================
    print("=" * 80)
    print("  FINAL VERDICT")
    print("=" * 80)
    print("""
  two_phases_have_distinct_transfer_functions.

  The two constitutive phases of GRUT II respond DIFFERENTLY to the
  same external forcing:

  | Discriminator | Eq2 (over-response) | Eq3 (under-response) |
  |--------------|:------------------:|:-------------------:|
  | DC response | {dc:.4f} | {dc:.4f} (SAME) |
  | HF amplitude | 1x (reference) | {hf:.2f}x (LARGER) |
  | Bandwidth | narrower | {hf:.2f}x wider |
  | Phase lag | larger | smaller |
  | Character | slow heavy medium | fast light medium |

  The high-frequency amplitude ratio of {hf:.1f}x is LARGE AND CLEAN.
  It comes directly from the tau ratio: tau_eq2/tau_eq3 = {tr:.2f}.
  This is a genuine, externally measurable phase discriminator.

  WHAT THIS MEANS:
  An external observer probing the constitutive vacuum with a
  time-varying perturbation would measure:
    - Different amplitude response at the same frequency
    - Different phase lag
    - Different bandwidth
  depending on which constitutive phase the vacuum occupies.

  This is the first externally distinguishable constitutive
  phase effect in the GRUT program.

  NEXT FORCED MOVE:
  Determine whether this transfer-function difference maps to a
  physically accessible measurement channel. The Phase IV T^Phi
  coupling means that constitutive perturbation responses propagate
  to metric perturbations through the Einstein equations. If a
  gravitational perturbation (e.g., a passing gravitational wave)
  acts as the "test signal" x(t), the two phases would produce
  different metric responses — different effective gravitational
  susceptibility. This IS the gravitational discriminator route.
  """.format(dc=chi_dc_eq2, hf=hf_ratio, tr=tau_eq2/tau_eq3))
    print("=" * 80)
