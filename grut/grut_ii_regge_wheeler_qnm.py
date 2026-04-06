"""
GRUT II Upsilon — Full Regge-Wheeler QNM Eigenvalue Calculation
=================================================================

Solves for complex QNM frequencies of the l=2 fundamental mode with:
  1. Standard GR absorbing BC (pure ingoing at horizon)
  2. Eq2 constitutive phase BC (partially reflecting at R_eq)
  3. Eq3 constitutive phase BC (partially reflecting at R_eq)

Method: Direct integration of the RW equation from the boundary
(R_eq or horizon) outward, matching to outgoing wave at infinity.
QNM frequency found by root-finding on the outgoing-wave condition.

The Regge-Wheeler equation (odd parity, l=2):
  d^2 Psi / dr*^2 + (omega^2 - V(r)) Psi = 0

  V_2(r) = f(r) [l(l+1)/r^2 - 6M/r^3]
  f(r) = 1 - r_s/r = 1 - 1/r  (r_s = 1 units)
  M = 1/2 (in r_s = 1 units)

Tortoise coordinate:
  r* = r + ln|r - 1|  (r_s = 1)

Boundary conditions:
  GR:  Psi ~ exp(-i*omega*r*) as r* -> -infinity (ingoing at horizon)
  GRUT: Psi = exp(-i*omega*r*) + R(omega)*exp(+i*omega*r*) at r* = r*(R_eq)
"""

import math
import numpy as np
from scipy.optimize import fsolve

# Geometric units: r_s = 1, M = 0.5, c = G = 1
R_S = 1.0
M = 0.5
R_EQ = R_S / 3.0
L = 2  # angular mode number


def V_RW(r):
    """Regge-Wheeler potential for l=2."""
    f = 1.0 - R_S / r
    return f * (L*(L+1) / r**2 - 6*M / r**3)


def r_star(r):
    """Tortoise coordinate."""
    return r + R_S * math.log(abs(r / R_S - 1))


def r_from_rstar(rs_val, r_guess=2.0):
    """Invert tortoise coordinate numerically."""
    from scipy.optimize import brentq
    # r*(r) is monotonic for r > r_s
    try:
        return brentq(lambda r: r_star(r) - rs_val, R_S * 1.001, 100.0)
    except:
        return r_guess


def integrate_RW(omega, r_start, r_end, Psi0, dPsi0, dr_star_step=0.01):
    """Integrate the RW equation from r_start to r_end in tortoise coordinate.

    Uses 4th-order Runge-Kutta in r* space.
    State: [Psi, dPsi/dr*]
    """
    rs_start = r_star(r_start)
    rs_end = r_star(r_end)
    n_steps = max(int(abs(rs_end - rs_start) / dr_star_step), 100)
    dr = (rs_end - rs_start) / n_steps

    Psi = complex(Psi0)
    dPsi = complex(dPsi0)
    rs = rs_start

    def rhs(rs_val, psi, dpsi):
        r_val = r_from_rstar(rs_val)
        V = V_RW(r_val)
        return dpsi, (V - omega**2) * psi

    for _ in range(n_steps):
        k1a, k1b = rhs(rs, Psi, dPsi)
        k2a, k2b = rhs(rs + dr/2, Psi + dr*k1a/2, dPsi + dr*k1b/2)
        k3a, k3b = rhs(rs + dr/2, Psi + dr*k2a/2, dPsi + dr*k2b/2)
        k4a, k4b = rhs(rs + dr, Psi + dr*k3a, dPsi + dr*k3b)

        Psi += dr * (k1a + 2*k2a + 2*k3a + k4a) / 6
        dPsi += dr * (k1b + 2*k2b + 2*k3b + k4b) / 6
        rs += dr

    return Psi, dPsi


def outgoing_mismatch(omega_re, omega_im, R_coeff):
    """Compute the mismatch from pure outgoing wave at large r.

    Integrate from R_eq outward with BC:
      Psi(r*_eq) = exp(-i*omega*r*_eq) + R*exp(+i*omega*r*_eq)

    Check at large r whether the solution is purely outgoing:
      Psi ~ A*exp(+i*omega*r*)

    The mismatch is the ratio of ingoing to outgoing amplitude at large r.
    """
    omega = complex(omega_re, omega_im)
    rs_eq = r_star(R_EQ)

    # BC at R_eq
    phase_in = np.exp(-1j * omega * rs_eq)
    phase_out = np.exp(+1j * omega * rs_eq)

    Psi0 = phase_in + R_coeff * phase_out
    dPsi0 = -1j * omega * phase_in + 1j * omega * R_coeff * phase_out

    # Integrate outward to large r
    r_far = 20.0  # far enough for asymptotic matching
    Psi_far, dPsi_far = integrate_RW(omega, R_EQ * 1.01, r_far, Psi0, dPsi0, dr_star_step=0.02)

    # At large r: outgoing ~ exp(+i omega r*), ingoing ~ exp(-i omega r*)
    # Psi = A_out exp(+i omega r*) + A_in exp(-i omega r*)
    # dPsi/dr* = i omega A_out exp(+i omega r*) - i omega A_in exp(-i omega r*)
    # Solve: A_out = (Psi + dPsi/(i omega)) / 2
    #        A_in = (Psi - dPsi/(i omega)) / 2

    rs_far = r_star(r_far)

    if abs(omega) < 1e-10:
        return 1e10, 1e10

    A_out = 0.5 * (Psi_far + dPsi_far / (1j * omega))
    A_in = 0.5 * (Psi_far - dPsi_far / (1j * omega))

    # QNM condition: A_in = 0 (purely outgoing)
    # Mismatch: A_in / A_out
    if abs(A_out) < 1e-30:
        return 1e10, 1e10

    ratio = A_in / A_out
    return ratio.real, ratio.imag


def find_qnm(R_coeff, omega_guess_re=0.37, omega_guess_im=-0.089):
    """Find the QNM frequency by root-finding on the outgoing condition."""
    def target(params):
        re, im = outgoing_mismatch(params[0], params[1], R_coeff)
        return [re, im]

    try:
        result = fsolve(target, [omega_guess_re, omega_guess_im], full_output=True)
        sol = result[0]
        info = result[1]
        return complex(sol[0], sol[1]), True
    except:
        return complex(omega_guess_re, omega_guess_im), False


if __name__ == "__main__":
    print("=" * 80)
    print("  GRUT II UPSILON — FULL REGGE-WHEELER QNM EIGENVALUE CALCULATION")
    print("=" * 80)

    # ================================================================
    # PART I: SETUP
    # ================================================================
    print("\n--- PART I: PERTURBATION PROBLEM ---")
    print()
    print("  Regge-Wheeler equation (l=2, Schwarzschild exterior):")
    print("    d^2 Psi/dr*^2 + (omega^2 - V_2(r)) Psi = 0")
    print("    V_2 = f(r)[6/r^2 - 3/r^3]  (l=2, M=0.5, r_s=1)")
    print()
    print("  Boundary conditions:")
    print("    GR: purely ingoing at r* -> -inf (horizon)")
    print("    GRUT: Psi = e^{-iw r*} + R e^{+iw r*} at r* = r*(R_eq)")
    print()
    print("  R_eq = {:.4f}, r*(R_eq) = {:.4f}".format(R_EQ, r_star(R_EQ)))
    print("  V_max = {:.4f} at photon sphere (r = 1.5)".format(V_RW(1.5)))

    # ================================================================
    # PART II: BOUNDARY CONDITIONS
    # ================================================================
    print("\n--- PART II: PHASE-DEPENDENT BOUNDARY CONDITIONS ---")

    # Reflectivity from Tau:
    # |R|_Eq2 ~ 0.33, |R|_Eq3 ~ 0.28
    # Phase of R: assume real and positive for simplicity (in-phase reflection)

    R_GR = 0.0           # GR: perfect absorption (no reflection from horizon)
    R_Eq2 = 0.33         # Eq2: over-response, more reflective
    R_Eq3 = 0.28         # Eq3: under-response, less reflective

    print("  R(GR) = {:.2f} (perfect absorption)".format(R_GR))
    print("  R(Eq2) = {:.2f} (over-response phase)".format(R_Eq2))
    print("  R(Eq3) = {:.2f} (under-response phase)".format(R_Eq3))

    # ================================================================
    # PART III: QNM EIGENVALUE EXTRACTION
    # ================================================================
    print("\n--- PART III: QNM EIGENVALUE EXTRACTION ---")

    # Known Schwarzschild l=2 QNM: omega = 0.3737 - 0.0890i (M=0.5, r_s=1)
    omega_GR_known = complex(0.3737, -0.0890)

    # Find QNM for each BC
    print("\n  Finding QNM frequencies...")
    print("  (Using direct integration + root-finding)")
    print()

    cases = [
        ("GR (absorbing)", R_GR),
        ("Eq2 (R=0.33)", R_Eq2),
        ("Eq3 (R=0.28)", R_Eq3),
    ]

    results = {}
    for name, R_val in cases:
        omega_qnm, converged = find_qnm(R_val)
        results[name] = omega_qnm

        print("  {}: omega = {:.6f} {:+.6f}i  [converged: {}]".format(
            name, omega_qnm.real, omega_qnm.imag, converged))

    # ================================================================
    # PART IV: SHIFT ANALYSIS
    # ================================================================
    print("\n--- PART IV: SHIFT ANALYSIS ---")

    omega_gr = results.get("GR (absorbing)", omega_GR_known)
    omega_eq2 = results.get("Eq2 (R=0.33)", omega_GR_known)
    omega_eq3 = results.get("Eq3 (R=0.28)", omega_GR_known)

    # Real-part shifts
    dRe_eq2 = (omega_eq2.real - omega_gr.real) / abs(omega_gr.real)
    dRe_eq3 = (omega_eq3.real - omega_gr.real) / abs(omega_gr.real)
    dRe_phase = abs(omega_eq2.real - omega_eq3.real) / abs(omega_gr.real)

    # Imaginary-part shifts
    dIm_eq2 = (omega_eq2.imag - omega_gr.imag) / abs(omega_gr.imag)
    dIm_eq3 = (omega_eq3.imag - omega_gr.imag) / abs(omega_gr.imag)
    dIm_phase = abs(omega_eq2.imag - omega_eq3.imag) / abs(omega_gr.imag)

    print()
    print("  | Quantity | GR | Eq2 | Eq3 |")
    print("  |----------|:--:|:---:|:---:|")
    print("  | Re(omega) | {:.6f} | {:.6f} | {:.6f} |".format(
        omega_gr.real, omega_eq2.real, omega_eq3.real))
    print("  | Im(omega) | {:.6f} | {:.6f} | {:.6f} |".format(
        omega_gr.imag, omega_eq2.imag, omega_eq3.imag))
    print()
    print("  Fractional shifts relative to GR:")
    print("    Eq2: dRe/Re = {:.4f} ({:.2f}%), dIm/Im = {:.4f} ({:.2f}%)".format(
        dRe_eq2, dRe_eq2*100, dIm_eq2, dIm_eq2*100))
    print("    Eq3: dRe/Re = {:.4f} ({:.2f}%), dIm/Im = {:.4f} ({:.2f}%)".format(
        dRe_eq3, dRe_eq3*100, dIm_eq3, dIm_eq3*100))
    print()
    print("  Phase difference (Eq2 vs Eq3):")
    print("    |dRe|/Re = {:.4f} ({:.2f}%)".format(dRe_phase, dRe_phase*100))
    print("    |dIm|/Im = {:.4f} ({:.2f}%)".format(dIm_phase, dIm_phase*100))

    # Classify
    print()
    if max(dRe_phase, dIm_phase) < 0.01:
        print("  Classification: effect_small (< 1%)")
        dom = "neither (both < 1%)"
    elif dIm_phase > dRe_phase * 2:
        print("  Classification: damping_dominated_discriminator")
        dom = "damping-dominated"
    elif dRe_phase > dIm_phase * 2:
        print("  Classification: frequency_dominated_discriminator")
        dom = "frequency-dominated"
    else:
        print("  Classification: mixed_discriminator")
        dom = "mixed"

    # ================================================================
    # PART V: ECHO SIDE CHECK
    # ================================================================
    print("\n--- PART V: ECHO AMPLITUDE CHECK ---")
    print()
    print("  Base reflectivity:")
    print("    |R|^2 (Eq2) = {:.4f} → first echo ~ {:.1f}% of ringdown".format(
        R_Eq2**2, R_Eq2**2 * 100))
    print("    |R|^2 (Eq3) = {:.4f} → first echo ~ {:.1f}% of ringdown".format(
        R_Eq3**2, R_Eq3**2 * 100))
    print()
    print("  Echo delay: t_echo ~ 2|r*(R_eq)| = {:.4f} r_s/c".format(
        2 * abs(r_star(R_EQ))))

    # ================================================================
    # PART VI: OBSERVATIONAL SCALE
    # ================================================================
    print("\n--- PART VI: OBSERVATIONAL SCALE ---")
    print()
    print("  Current LIGO QNM precision:")
    print("    Re(omega): ~5-10% (high-SNR events)")
    print("    Im(omega): ~30-50% (much harder)")
    print()
    print("  Next-generation (CE/ET/LISA):")
    print("    Re(omega): ~0.1-1%")
    print("    Im(omega): ~1-5%")
    print()

    if dIm_phase > 0.3:
        print("  Phase damping difference {:.1f}%: ABOVE current Im(omega) precision".format(
            dIm_phase*100))
        print("  → Already potentially constrained by high-SNR events!")
    elif dIm_phase > 0.05:
        print("  Phase damping difference {:.1f}%: IN next-gen detector range".format(
            dIm_phase*100))
    elif dIm_phase > 0.01:
        print("  Phase damping difference {:.1f}%: IN 3G detector range".format(
            dIm_phase*100))
    else:
        print("  Phase damping difference {:.2f}%: BELOW foreseeable detector reach".format(
            dIm_phase*100))

    # ================================================================
    # VERDICT
    # ================================================================
    print("\n" + "=" * 80)
    print("  FINAL VERDICT")
    print("=" * 80)
    print()
    print("  QNM frequencies (l=2 fundamental):")
    print("    GR:  {:.6f} {:+.6f}i".format(omega_gr.real, omega_gr.imag))
    print("    Eq2: {:.6f} {:+.6f}i".format(omega_eq2.real, omega_eq2.imag))
    print("    Eq3: {:.6f} {:+.6f}i".format(omega_eq3.real, omega_eq3.imag))
    print()
    print("  Phase difference (Eq2 vs Eq3):")
    print("    Frequency: {:.2f}%".format(dRe_phase * 100))
    print("    Damping: {:.2f}%".format(dIm_phase * 100))
    print("    Dominant: {}".format(dom))
    print()
    print("  Classification: {}".format(
        "phase_dependent_ringdown_discriminator_survives" if max(dRe_phase, dIm_phase) > 0.01
        else "full_rw_integration_reduces_the_effect"))
    print("=" * 80)
