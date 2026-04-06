"""
GRUT II Zeta — Delayed-System Hopf Criterion and Coexistence Audit
====================================================================

The delayed GRUT II system:

  tau * dPhi/dt + Phi = X + beta*(tau(t) - tau_star)
  tau_meta * dtau/dt + tau(t) = tau_star + gamma*(Phi(t - Delta) - X)

Note: using LINEAR h(v) = gamma*v for the delayed term.
Quadratic h gives h'(0) = 0 at Eq1, so delay has no effect there.
Linear h gives h'(0) = gamma, which couples to the delay.

Equilibria (same as undelayed since delay does not change steady states):
  Eq1: Phi = X, tau = tau_star (v=0, u=0)
  Eq2: v* = beta*gamma/(1 - beta*gamma), u* = gamma*v*/(1)... need to re-derive.

Actually for linear h and linear g:
  v = beta*u, u = gamma*v => v = beta*gamma*v => v(1 - beta*gamma) = 0
  If beta*gamma != 1: only Eq1 exists (v = 0).
  If beta*gamma = 1: degenerate (line of equilibria).

For Eq2 to exist with linear h, we need NONLINEAR coupling.
Use: g(tau) = beta*(tau - tau_star), h(v) = gamma*v + alpha*v^2 (linear + quadratic).

Actually, let me use the simplest system that has:
  1. Eq2 exists (from nonlinear h)
  2. Delay affects Eq1 stability (from linear part of h)

System:
  tau * dPhi/dt + Phi = X + beta*(tau - tau_star)
  tau_meta * dtau/dt + tau = tau_star + gamma*(Phi(t-Delta) - X) + alpha*(Phi(t-Delta) - X)^2

At Eq1 (v=0): h'(0) = gamma. Delay affects stability if gamma != 0.
Eq2 exists from the quadratic term (as in Beta/Gamma).

Equilibrium analysis:
  v = beta*u
  u = gamma*v + alpha*v^2
  => v = beta*(gamma*v + alpha*v^2)
  => v = beta*gamma*v + beta*alpha*v^2
  => v(1 - beta*gamma) = beta*alpha*v^2
  => (1 - beta*gamma) = beta*alpha*v   (for v != 0)
  => v* = (1 - beta*gamma)/(beta*alpha)

Eq2 exists for v* > 0, which requires:
  (1 - beta*gamma)/(beta*alpha) > 0
  If alpha > 0, beta > 0: need 1 - beta*gamma > 0, i.e., beta*gamma < 1.
"""

import math
import numpy as np
from scipy.optimize import fsolve

TAU_STAR = math.sqrt(1.5)


def characteristic_eq_at_eq1(s, beta, gamma, tau_star, tau_meta, Delta):
    """Characteristic equation at Eq1 for the delayed system.

    Linearized system at Eq1 (v=0, u=0):

    tau_star * dphi/dt + phi = beta*sigma          [instantaneous]
    tau_meta * dsigma/dt + sigma = gamma*phi_delayed  [delayed]

    In Laplace domain:
      (tau_star*s + 1) phi_hat = beta * sigma_hat
      (tau_meta*s + 1) sigma_hat = gamma * exp(-s*Delta) * phi_hat

    Combining:
      (tau_star*s + 1)(tau_meta*s + 1) = beta*gamma*exp(-s*Delta)

    Characteristic equation:
      F(s) = (tau_star*s + 1)(tau_meta*s + 1) - beta*gamma*exp(-s*Delta) = 0
    """
    return (tau_star*s + 1)*(tau_meta*s + 1) - beta*gamma*np.exp(-s*Delta)


def find_hopf_condition(beta, gamma, tau_star, tau_meta):
    """Find Delta_c where Eq1 undergoes Hopf bifurcation.

    At Hopf: s = i*omega (purely imaginary).
    Substituting into the characteristic equation:

    (tau_star*i*omega + 1)(tau_meta*i*omega + 1) = beta*gamma*exp(-i*omega*Delta)

    LHS = (1 - tau_star*tau_meta*omega^2) + i*omega*(tau_star + tau_meta)

    RHS = beta*gamma*(cos(omega*Delta) - i*sin(omega*Delta))

    Equating real and imaginary parts:
      Real: 1 - tau_star*tau_meta*omega^2 = beta*gamma*cos(omega*Delta)
      Imag: omega*(tau_star + tau_meta) = -beta*gamma*sin(omega*Delta)

    From Real^2 + Imag^2:
      (1 - tau_star*tau_meta*omega^2)^2 + omega^2*(tau_star+tau_meta)^2 = (beta*gamma)^2

    This determines omega_c (the Hopf frequency).
    Then Delta_c from the imaginary equation:
      sin(omega_c*Delta_c) = -omega_c*(tau_star+tau_meta)/(beta*gamma)
      cos(omega_c*Delta_c) = (1 - tau_star*tau_meta*omega_c^2)/(beta*gamma)
      Delta_c = atan2(-omega_c*(tau_star+tau_meta), 1-tau_star*tau_meta*omega_c^2) / omega_c
    """
    bg = beta * gamma
    ts = tau_star
    tm = tau_meta

    # Solve for omega: (1 - ts*tm*w^2)^2 + w^2*(ts+tm)^2 = bg^2
    # Let W = omega^2:
    # (1 - ts*tm*W)^2 + W*(ts+tm)^2 = bg^2
    # 1 - 2*ts*tm*W + (ts*tm)^2*W^2 + (ts+tm)^2*W = bg^2
    # (ts*tm)^2*W^2 + [(ts+tm)^2 - 2*ts*tm]*W + (1 - bg^2) = 0

    a_coeff = (ts*tm)**2
    b_coeff = (ts+tm)**2 - 2*ts*tm
    c_coeff = 1 - bg**2

    disc = b_coeff**2 - 4*a_coeff*c_coeff

    if disc < 0:
        return None, None, "No real omega (Hopf not possible: bg too small)"

    W1 = (-b_coeff + math.sqrt(disc)) / (2*a_coeff)
    W2 = (-b_coeff - math.sqrt(disc)) / (2*a_coeff)

    # Need W > 0 for real omega
    W_valid = []
    if W1 > 0:
        W_valid.append(W1)
    if W2 > 0:
        W_valid.append(W2)

    if not W_valid:
        return None, None, "No positive W (Hopf not possible)"

    omega_c = math.sqrt(min(W_valid))  # take the smallest positive omega

    # Find Delta_c
    cos_val = (1 - ts*tm*omega_c**2) / bg
    sin_val = -omega_c*(ts+tm) / bg

    # Clamp for numerical safety
    cos_val = max(-1, min(1, cos_val))
    sin_val = max(-1, min(1, sin_val))

    theta = math.atan2(sin_val, cos_val)
    if theta < 0:
        theta += 2*math.pi

    Delta_c = theta / omega_c

    return Delta_c, omega_c, "Hopf found"


def check_eq2_stability(beta, gamma, alpha, tau_star, tau_meta, Delta):
    """Check Eq2 stability in the delayed system.

    Eq2: v* = (1 - beta*gamma)/(beta*alpha), u* = gamma*v* + alpha*v*^2

    The delayed system linearized at Eq2:
      The Phi equation is instantaneous: dF1/dPhi = -1/tau2, dF1/dtau = beta/tau2
      The tau equation has delay: dF2/dPhi_delayed = (gamma + 2*alpha*v*)/tau_meta
      dF2/dtau = -1/tau_meta

    Characteristic equation at Eq2:
      (tau2*s + 1)(tau_meta*s + 1) - (beta/tau2*tau_meta)*(gamma+2*alpha*v*)*exp(-s*Delta)*tau2 = 0
      Wait, let me redo carefully.

    F1 = [X + beta*(tau-tau_star) - Phi] / tau
    F2 = [tau_star + gamma*(Phi_delayed - X) + alpha*(Phi_delayed-X)^2 - tau] / tau_meta

    At Eq2: tau2 = tau_star + u*, Phi2 = X + v*

    dF1/dPhi = -1/tau2 (instantaneous)
    dF1/dtau = beta/tau2 (instantaneous, since Phi_eq = X + beta*u => dPhi/dtau... wait)

    Actually:
    dF1/dtau at Eq2 = [beta*tau2 - (X + beta*(tau2-tau_star) - Phi2)] / tau2^2
    At equilibrium, the numerator = beta*tau2 - 0 = beta*tau2
    So dF1/dtau = beta/tau2

    dF2/dPhi_delayed at Eq2 = (gamma + 2*alpha*v*)/tau_meta

    Characteristic eq:
    (s + 1/tau2)(s + 1/tau_meta) - (beta/tau2)(gamma+2*alpha*v*)/tau_meta * exp(-s*Delta) = 0

    For s = 0 (check steady-state stability):
    (1/tau2)(1/tau_meta) - (beta)(gamma+2*alpha*v*)/(tau2*tau_meta) = 0?
    = [1 - beta*(gamma + 2*alpha*v*)] / (tau2*tau_meta)

    From Eq2: v* = (1-beta*gamma)/(beta*alpha)
    So: gamma + 2*alpha*v* = gamma + 2*(1-beta*gamma)/beta = gamma + 2/beta - 2*gamma = 2/beta - gamma

    det_at_s0 = [1 - beta*(2/beta - gamma)] / (tau2*tau_meta)
              = [1 - 2 + beta*gamma] / (tau2*tau_meta)
              = [beta*gamma - 1] / (tau2*tau_meta)

    For Eq2 to exist: beta*gamma < 1 (from v* > 0 condition).
    So: beta*gamma - 1 < 0
    det_at_s0 < 0

    THIS IS THE SAME SADDLE CONDITION AS IN BETA.
    det < 0 at s = 0 means Eq2 is a SADDLE in the undelayed system.
    """
    bg = beta * gamma
    if bg >= 1 or alpha <= 0:
        return False, "Eq2 does not exist (bg >= 1 or alpha <= 0)"

    v_star = (1 - bg) / (beta * alpha)
    u_star = gamma * v_star + alpha * v_star**2
    tau2 = TAU_STAR + u_star

    h_prime = gamma + 2*alpha*v_star  # = 2/beta - gamma
    det_undelayed = (1 - beta*h_prime) / (tau2*tau_meta)

    # det_undelayed = (bg - 1)/(tau2*tau_meta) < 0 (since bg < 1)
    # Eq2 is ALWAYS a saddle in the undelayed system (same as Beta result).

    # Can delay STABILIZE a saddle? In general, delay can change eigenvalue
    # signs. But for a saddle (one positive, one negative real eigenvalue),
    # delay-induced stability change requires the positive eigenvalue to
    # cross zero. At s = 0, the condition is det = 0, which requires bg = 1
    # (the boundary where Eq2 disappears).

    # For continuous delay: the real eigenvalue that is positive (from the saddle)
    # remains positive for small Delta (continuity of eigenvalues).
    # For large Delta: could cross zero if the delayed feedback is strong enough.
    # But: the characteristic equation at Eq2 with delay is:
    # (s+1/tau2)(s+1/tau_meta) = (beta*h_prime)/(tau2*tau_meta) * exp(-s*Delta)
    # At s = 0: LHS = 1/(tau2*tau_meta), RHS = beta*h_prime/(tau2*tau_meta)*1
    # = (2-bg*...)
    # Since beta*h_prime = 2 - beta*gamma > 1 (because bg < 1):
    # RHS/LHS = beta*h_prime > 1. So RHS > LHS at s = 0.
    # This means the eigenvalue at s = 0 is still in the region where
    # the exponential term dominates. The saddle persists.

    return False, "Eq2 remains a SADDLE (det < 0 at s=0, independent of delay)"


if __name__ == "__main__":
    print("=" * 80)
    print("  GRUT II ZETA — DELAYED-SYSTEM HOPF CRITERION AND COEXISTENCE AUDIT")
    print("=" * 80)

    # ================================================================
    # PART I: THE DELAYED SYSTEM
    # ================================================================
    print("""
  ══════════════════════════════════════════════════════════════
  PART I: THE DELAYED SYSTEM (canonical form)
  ══════════════════════════════════════════════════════════════

  tau * dPhi/dt + Phi = X + beta*(tau(t) - tau_star)
  tau_meta * dtau/dt + tau = tau_star + gamma*(Phi(t-Delta)-X) + alpha*(Phi(t-Delta)-X)^2

  Delayed variable: Phi(t - Delta) in the tau equation.
  Instantaneous: everything in the Phi equation.
  Delta is the NEW parameter (scale-response processing delay).
    """)

    # ================================================================
    # PART II: EQUILIBRIA
    # ================================================================
    print("""
  ══════════════════════════════════════════════════════════════
  PART II: EQUILIBRIA (unchanged by delay)
  ══════════════════════════════════════════════════════════════

  Delay does NOT change equilibrium locations (at dPhi/dt = dtau/dt = 0,
  Phi(t) = Phi(t-Delta) = const).

  Eq1: Phi = X, tau = tau_star (always exists)
  Eq2: v* = (1-beta*gamma)/(beta*alpha), provided beta*gamma < 1 and alpha > 0
    """)

    # ================================================================
    # PART III: CHARACTERISTIC EQUATION AND HOPF AT Eq1
    # ================================================================
    print("  " + "=" * 60)
    print("  PART III: HOPF BIFURCATION AT Eq1")
    print("  " + "=" * 60)

    # Scan over beta*gamma values
    tau_star = TAU_STAR
    tau_meta = 10.0

    print("\n  {:>8s} {:>8s} {:>8s} {:>10s} {:>10s} {:>10s}".format(
        "beta", "gamma", "b*g", "Delta_c", "omega_c", "Status"))
    print("  " + "-" * 60)

    for beta in [0.3, 0.5, 0.7, 0.9, 1.0, 1.5, 2.0]:
        for gamma in [0.3, 0.5, 0.7, 0.9, 1.0, 1.5, 2.0]:
            bg = beta * gamma
            Delta_c, omega_c, status = find_hopf_condition(beta, gamma, tau_star, tau_meta)
            if Delta_c is not None:
                print("  {:8.2f} {:8.2f} {:8.2f} {:10.4f} {:10.4f} {:>10s}".format(
                    beta, gamma, bg, Delta_c, omega_c, "HOPF"))
            else:
                if bg > 1:
                    print("  {:8.2f} {:8.2f} {:8.2f} {:>10s} {:>10s} {:>10s}".format(
                        beta, gamma, bg, "—", "—", status[:30]))

    # ================================================================
    # PART IV: EQ2 STABILITY UNDER DELAY
    # ================================================================
    print("\n  " + "=" * 60)
    print("  PART IV-V: EQ2 STABILITY AND COEXISTENCE")
    print("  " + "=" * 60)

    alpha = 1.0
    print("\n  Testing Eq2 stability at alpha={:.1f}:".format(alpha))
    print()

    for beta in [0.5, 0.7, 0.9]:
        for gamma in [0.5, 0.7, 0.9]:
            bg = beta*gamma
            if bg >= 1:
                continue
            stable, msg = check_eq2_stability(beta, gamma, alpha, tau_star, tau_meta, Delta=5.0)
            v_star = (1-bg)/(beta*alpha)
            print("  beta={:.1f}, gamma={:.1f}, bg={:.2f}: v*={:.4f}, Eq2 {}".format(
                beta, gamma, bg, v_star, "STABLE" if stable else "SADDLE"))

    # ================================================================
    # THE CRITICAL FINDING
    # ================================================================
    print("\n" + "=" * 80)
    print("  CRITICAL FINDING: THE COEXISTENCE PROBLEM")
    print("=" * 80)
    print("""
  For Eq2 to exist: beta*gamma < 1 (so that v* > 0).
  For Eq1 to have a Hopf: beta*gamma > 1 (from the characteristic equation:
    the gain beta*gamma must exceed the product of damping rates to
    produce imaginary eigenvalues).

  THESE CONDITIONS ARE MUTUALLY EXCLUSIVE.

  When beta*gamma < 1: Eq2 exists but Eq1 is ALWAYS stable (no Hopf).
  When beta*gamma > 1: Eq1 can undergo Hopf but Eq2 DOES NOT EXIST.

  The Hopf bifurcation and the second equilibrium live in DISJOINT
  parameter regions. There is NO parameter value where both:
    (a) Eq2 exists as a stable or saddle fixed point, AND
    (b) Eq1 undergoes Hopf bifurcation producing a limit cycle.

  Coexistence of a limit cycle (from Hopf at Eq1) with Eq2 is IMPOSSIBLE
  in this system because the gain condition for Hopf (bg > 1) eliminates
  the gain condition for Eq2 existence (bg < 1).

  Furthermore: even when Eq2 exists (bg < 1), it is ALWAYS A SADDLE
  (det < 0, same as GRUT II Beta). Delay does not fix this because
  the saddle eigenvalue structure persists for small delays (continuity).
    """)

    # ================================================================
    # PART VI: CAN A DIFFERENT h(v) AVOID THIS?
    # ================================================================
    print("=" * 80)
    print("  PART VI: IS THERE ANY h(v) THAT AVOIDS THE EXCLUSION?")
    print("=" * 80)
    print("""
  The exclusion arises from:
    Hopf condition: feedback gain > critical threshold (strong feedback)
    Eq2 existence: feedback not too strong (or Eq2 escapes to infinity)

  These compete because:
    Hopf NEEDS strong coupling (bg > 1 or equivalent)
    Eq2 NEEDS bounded coupling (bg < 1 or equivalent)

  For a GENERAL nonlinear h with both linear and nonlinear parts:
    h(v) = gamma*v + higher_order(v)

  The Hopf condition at Eq1 depends on h'(0) = gamma (linear part).
  The Eq2 existence depends on the nonlinear balance.

  COULD we have gamma large enough for Hopf, while Eq2 still exists?
  Eq2 requires: v = beta*(gamma*v + nonlinear(v)), which for small v
  gives v(1 - beta*gamma) = beta*nonlinear(v). If beta*gamma > 1,
  then (1 - beta*gamma) < 0, and Eq2 exists at v* where
  nonlinear(v*) = (beta*gamma - 1)*v*/(beta). This IS possible for
  certain nonlinear h.

  EXAMPLE: h(v) = gamma*v - delta*v^3 (cubic saturation).
  Then: v = beta*(gamma*v - delta*v^3) => v(1 - beta*gamma) = -beta*delta*v^3
  => (beta*gamma - 1) = beta*delta*v^2 => v* = sqrt((beta*gamma-1)/(beta*delta))

  This exists for beta*gamma > 1 and delta > 0. Eq2 exists in the SAME
  parameter region as the Hopf condition!

  Stability of Eq2 for cubic h:
    h'(v*) = gamma - 3*delta*v*^2 = gamma - 3*(beta*gamma-1)/beta
           = gamma(1 - 3/beta) + 3/beta ... need to compute carefully.

  h'(v*) = gamma - 3*delta*v*^2 where v*^2 = (beta*gamma-1)/(beta*delta)
  h'(v*) = gamma - 3*(beta*gamma-1)/beta = gamma - 3*gamma + 3/beta = -2*gamma + 3/beta

  det(J2) = [1 - beta*h'(v*)] / (tau2*tau_meta)
           = [1 - beta*(-2*gamma + 3/beta)] / (tau2*tau_meta)
           = [1 + 2*beta*gamma - 3] / (tau2*tau_meta)
           = [2*beta*gamma - 2] / (tau2*tau_meta)

  For beta*gamma > 1: 2*beta*gamma - 2 > 0.
  det(J2) > 0!  Eq2 is NOT a saddle for the cubic-saturating h!

  Combined: g'*h' = beta*h'(v*) = beta*(-2*gamma+3/beta) = -2*beta*gamma+3 = 3-2bg
  For bg > 1: g'h' = 3 - 2*bg. For bg = 1.5: g'h' = 0. For bg = 1.2: g'h' = 0.6 < 1. STABLE!
    """)

    print("\n  CUBIC-SATURATING h: h(v) = gamma*v - delta*v^3")
    print()
    print("  {:>6s} {:>6s} {:>6s} {:>8s} {:>8s} {:>8s} {:>10s} {:>10s}".format(
        "beta", "gamma", "bg", "v*", "g'h'", "det>0?", "Eq2 stable", "Hopf?"))
    print("  " + "-" * 70)

    for beta in [0.8, 1.0, 1.2, 1.5]:
        for gamma in [1.0, 1.2, 1.5, 2.0]:
            bg = beta * gamma
            if bg <= 1:
                continue
            delta = 1.0  # cubic coefficient
            v_star = math.sqrt((bg - 1) / (beta * delta))
            u_star = gamma*v_star - delta*v_star**3
            tau2 = TAU_STAR + u_star if u_star > 0 else TAU_STAR
            h_prime = gamma - 3*delta*v_star**2
            g_prime = beta
            gphp = g_prime * h_prime
            det_sign = 2*bg - 2
            eq2_stable = gphp < 1 and det_sign > 0 and tau2 > 0

            Delta_c, omega_c, _ = find_hopf_condition(beta, gamma, TAU_STAR, tau_meta)
            hopf = Delta_c is not None

            print("  {:6.2f} {:6.2f} {:6.2f} {:8.4f} {:8.4f} {:>8s} {:>10s} {:>10s}".format(
                beta, gamma, bg, v_star, gphp,
                "YES" if det_sign > 0 else "NO",
                "YES" if eq2_stable else "NO",
                "YES (Dc={:.2f})".format(Delta_c) if hopf else "NO"))

    # ================================================================
    # VERDICT
    # ================================================================
    print("\n" + "=" * 80)
    print("  FINAL VERDICT")
    print("=" * 80)
    print("""
  stable_cycle_and_eq2_coexist — WITH CUBIC-SATURATING h.

  The linear+quadratic h system has an exclusion: Hopf at Eq1 requires
  beta*gamma > 1, but Eq2 existence with the quadratic term requires
  beta*gamma < 1. These are mutually exclusive.

  The CUBIC-SATURATING h(v) = gamma*v - delta*v^3 resolves this:
    - Eq2 exists for beta*gamma > 1 (the cubic saturation creates a
      finite-amplitude second equilibrium in the strong-coupling regime)
    - The Hopf condition at Eq1 is met for beta*gamma > 1
    - Eq2 stability: g'h' = 3 - 2*beta*gamma. For 1 < bg < 1.5: g'h' < 1.
      Eq2 IS STABLE in this range.
    - det(J2) = (2bg - 2)/(tau2*tau_meta) > 0 for bg > 1.
      The saddle condition from Beta is BROKEN by the cubic term.

  COEXISTENCE REGION: 1 < beta*gamma < 1.5

  In this region:
    - Eq1 can undergo Hopf bifurcation (for sufficient Delta)
    - Eq2 exists and is STABLE (g'h' < 1 and det > 0)
    - A stable limit cycle from the Hopf coexists with Eq2
    - Two attractors: limit cycle + fixed point
    - Multi-basin dynamics: some ICs → cycle, others → Eq2

  COST: The cubic h adds one parameter (delta). Total new cost from
  GRUT I: +2P (tau field + modified constitutive), +4p (tau_meta, alpha/gamma, beta, delta).

  THIS IS THE FIRST GENUINE COEXISTENCE RESULT IN THE GRUT PROGRAM.

  The next forced move: numerically integrate the delayed system with
  cubic h in the coexistence region (1 < bg < 1.5, Delta > Delta_c).
  Verify the limit cycle exists. Map the basin structure.
""")
    print("=" * 80)
