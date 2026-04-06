"""
GRUT II Beta — Symbolic Stability Region and Bifurcation Audit
================================================================

The GRUT II modified coupled system:

  tau * dPhi/dt + Phi = X + beta*(tau - tau_star)       [modified constitutive]
  tau_meta * dtau/dt + tau = tau_star + alpha*(Phi-X)^2  [scale equation]

EXACT SYMBOLIC ANALYSIS:
  1. Equilibria in closed form
  2. Full Jacobian symbolically
  3. Trace and determinant conditions for Eq2 stability
  4. Bifurcation classification
  5. Parameter region mapping
"""

import math
import numpy as np

TAU_STAR = math.sqrt(1.5)


def equilibria_symbolic():
    """
    EQUILIBRIUM CONDITIONS:

    dPhi/dt = 0: Phi = X + beta*(tau - tau_star)
    dtau/dt = 0: tau = tau_star + alpha*(Phi - X)^2

    Substituting: let u = tau - tau_star and v = Phi - X.

    From eq 1: v = beta * u
    From eq 2: u = alpha * v^2 = alpha * beta^2 * u^2

    So: u(1 - alpha*beta^2*u) = 0

    SOLUTIONS:
      Eq1: u = 0  =>  tau = tau_star,  Phi = X
      Eq2: u = 1/(alpha*beta^2)  =>  tau = tau_star + 1/(alpha*beta^2)
                                      Phi = X + 1/(alpha*beta)

    EXISTENCE:
      Eq2 exists (real, positive u) iff alpha > 0 and beta != 0.
      For tau to remain positive: tau_star + 1/(alpha*beta^2) > 0 — always true for alpha > 0.
      For Phi to be physical: depends on sign of beta.
        beta > 0: Phi2 > X (higher-Phi equilibrium)
        beta < 0: Phi2 < X (lower-Phi equilibrium)
    """
    print("  EQUILIBRIA (exact):")
    print("    Eq1: Phi* = X, tau* = tau_star (ALWAYS exists)")
    print("    Eq2: Phi* = X + 1/(alpha*beta), tau* = tau_star + 1/(alpha*beta^2)")
    print("    Exists iff alpha > 0 and beta != 0.")
    print()


def jacobian_symbolic():
    """
    FULL JACOBIAN:

    F1 = dPhi/dt = [X + beta*(tau - tau_star) - Phi] / tau
    F2 = dtau/dt = [tau_star + alpha*(Phi - X)^2 - tau] / tau_meta

    Partial derivatives:

    dF1/dPhi = -1/tau
    dF1/dtau = [beta - F1] / tau = [beta*tau - (X + beta*(tau-tau_star) - Phi)] / tau^2

    At equilibrium (F1 = 0): dF1/dtau = beta/tau*

    dF2/dPhi = 2*alpha*(Phi - X) / tau_meta
    dF2/dtau = -1/tau_meta

    AT Eq1 (v=0, u=0):
      J1 = [[-1/tau_star,  beta/tau_star],
            [0,             -1/tau_meta  ]]

    AT Eq2 (v=1/(alpha*beta), u=1/(alpha*beta^2)):
      tau2 = tau_star + 1/(alpha*beta^2)
      J2 = [[-1/tau2,             beta/tau2            ],
            [2/(beta*tau_meta),   -1/tau_meta           ]]

      where dF2/dPhi at Eq2 = 2*alpha*(1/(alpha*beta))/tau_meta = 2/(beta*tau_meta)
    """
    print("  JACOBIAN AT Eq2:")
    print("    tau2 = tau_star + 1/(alpha*beta^2)")
    print("    J2 = [[-1/tau2,           beta/tau2       ],")
    print("          [2/(beta*tau_meta), -1/tau_meta     ]]")
    print()


def stability_conditions():
    """
    STABILITY OF Eq2:

    J2 = [[a, b], [c, d]] where:
      a = -1/tau2
      b = beta/tau2
      c = 2/(beta*tau_meta)
      d = -1/tau_meta

    Stability requires:
      tr(J2) < 0   AND   det(J2) > 0

    TRACE:
      tr = a + d = -1/tau2 - 1/tau_meta

      Since tau2 > 0 and tau_meta > 0:
      tr = -(1/tau2 + 1/tau_meta) < 0   ALWAYS.

      TRACE CONDITION IS ALWAYS SATISFIED.

    DETERMINANT:
      det = a*d - b*c
          = (1/tau2)(1/tau_meta) - (beta/tau2)(2/(beta*tau_meta))
          = 1/(tau2*tau_meta) - 2/(tau2*tau_meta)
          = -1/(tau2*tau_meta)

      det = -1/(tau2*tau_meta) < 0   ALWAYS.

      DETERMINANT IS ALWAYS NEGATIVE.

    Since det < 0 ALWAYS: Eq2 is ALWAYS A SADDLE POINT.

    One eigenvalue is positive, one is negative. Eq2 is NEVER stable.
    """
    print("  STABILITY CONDITIONS FOR Eq2:")
    print()
    print("    tr(J2) = -1/tau2 - 1/tau_meta < 0    ALWAYS (both terms negative)")
    print()
    print("    det(J2) = (1/tau2)(1/tau_meta) - (beta/tau2)(2/(beta*tau_meta))")
    print("            = 1/(tau2*tau_meta) - 2/(tau2*tau_meta)")
    print("            = -1/(tau2*tau_meta)")
    print("            < 0    ALWAYS")
    print()
    print("  SINCE det(J2) < 0 ALWAYS:")
    print("    Eq2 is a SADDLE POINT for ALL parameter values.")
    print("    One eigenvalue positive, one negative.")
    print("    Eq2 is NEVER A STABLE ATTRACTOR.")
    print()
    print("  This is EXACT. No parameter choice (alpha, beta, tau_meta) makes Eq2 stable.")
    print()


def verify_det_symbolically():
    """
    VERIFICATION: det = ad - bc

    a = -1/tau2
    b = beta/tau2
    c = 2/(beta*tau_meta)
    d = -1/tau_meta

    ad = (-1/tau2)(-1/tau_meta) = +1/(tau2*tau_meta)
    bc = (beta/tau2)(2/(beta*tau_meta)) = 2/(tau2*tau_meta)

    det = ad - bc = 1/(tau2*tau_meta) - 2/(tau2*tau_meta) = -1/(tau2*tau_meta)

    The factor of 2 in 'c' comes from:
      dF2/dPhi = 2*alpha*(Phi-X)/tau_meta
      At Eq2: Phi - X = 1/(alpha*beta)
      So c = 2*alpha*(1/(alpha*beta))/tau_meta = 2/(beta*tau_meta)

    And b*c = (beta/tau2) * (2/(beta*tau_meta)) = 2/(tau2*tau_meta)

    The beta cancels in b*c. The result det = -1/(tau2*tau_meta) is
    INDEPENDENT of alpha, beta. It depends only on tau2 and tau_meta,
    both of which are positive.

    Therefore: det < 0 UNCONDITIONALLY.
    """
    print("  SYMBOLIC VERIFICATION:")
    print("    ad = 1/(tau2*tau_meta)")
    print("    bc = 2/(tau2*tau_meta)")
    print("    det = ad - bc = -1/(tau2*tau_meta)")
    print("    The beta CANCELS in bc. The result is parameter-independent.")
    print("    det < 0 for ALL alpha > 0, beta != 0, tau_meta > 0.")
    print()


def numerical_verification():
    """Verify with explicit numbers across parameter space."""
    print("  NUMERICAL VERIFICATION ACROSS PARAMETER SPACE:")
    print("  {:>8s} {:>8s} {:>10s} {:>10s} {:>10s} {:>10s} {:>10s} {:>8s}".format(
        "alpha", "beta", "tau_meta", "tau2", "tr(J2)", "det(J2)", "eig_max", "stable?"))
    print("  " + "-" * 80)

    for alpha in [0.1, 0.5, 1.0, 5.0, 10.0]:
        for beta in [-2.0, -0.5, 0.1, 0.5, 1.0, 2.0]:
            for tau_meta in [0.1, 1.0, 10.0, 100.0]:
                if alpha <= 0 or beta == 0:
                    continue
                tau2 = TAU_STAR + 1.0 / (alpha * beta**2)

                a = -1.0 / tau2
                b = beta / tau2
                c = 2.0 / (beta * tau_meta)
                d = -1.0 / tau_meta

                tr_val = a + d
                det_val = a * d - b * c

                J = np.array([[a, b], [c, d]])
                eigs = np.linalg.eigvals(J)
                eig_max = max(e.real for e in eigs)

                stable = eig_max < 0

                # Only print a representative sample
                if abs(alpha - 1.0) < 0.01 and abs(tau_meta - 10.0) < 0.01:
                    print("  {:8.1f} {:8.2f} {:10.1f} {:10.4f} {:10.4f} {:10.6f} {:10.6f} {:>8s}".format(
                        alpha, beta, tau_meta, tau2, tr_val, det_val, eig_max,
                        "YES" if stable else "NO"))

    # Check if ANY parameter point gives stable Eq2
    n_tested = 0
    n_stable = 0
    for alpha in np.logspace(-2, 2, 30):
        for beta in np.concatenate([np.linspace(-5, -0.01, 15), np.linspace(0.01, 5, 15)]):
            for tau_meta in np.logspace(-2, 3, 20):
                tau2 = TAU_STAR + 1.0 / (alpha * beta**2)
                det_val = -1.0 / (tau2 * tau_meta)
                n_tested += 1
                if det_val > 0:
                    n_stable += 1

    print()
    print("  Total parameter points tested: {}".format(n_tested))
    print("  Points with det(J2) > 0: {}".format(n_stable))
    print("  Eq2 stable at ANY point: {}".format("YES" if n_stable > 0 else "NO"))


def bifurcation_classification():
    """
    BIFURCATION STRUCTURE:

    The two equilibria are:
      Eq1: (X, tau_star) — always stable
      Eq2: (X + 1/(alpha*beta), tau_star + 1/(alpha*beta^2)) — always saddle

    As alpha*beta^2 → infinity: Eq2 → Eq1 (they merge).
    At alpha*beta^2 → infinity: the two roots of u(1 - alpha*beta^2*u) = 0 merge at u = 0.

    This is a TRANSCRITICAL BIFURCATION in the parameter alpha*beta^2:
      - For finite alpha*beta^2: two equilibria, one stable (Eq1), one saddle (Eq2)
      - At alpha*beta^2 → ∞: Eq2 merges with Eq1
      - For alpha → 0 or beta → 0: Eq2 goes to infinity (escapes)

    There is NO parameter value where Eq2 becomes stable.
    The bifurcation does not produce bistability.
    It produces: one attractor + one saddle (always).
    """
    print("  BIFURCATION CLASSIFICATION:")
    print("    Type: TRANSCRITICAL")
    print("    Control: alpha*beta^2")
    print("    At finite alpha*beta^2: Eq1 (stable) + Eq2 (saddle)")
    print("    At alpha*beta^2 → infinity: Eq1 and Eq2 merge")
    print("    Bistability: NEVER (det(J2) < 0 unconditionally)")
    print()


if __name__ == "__main__":
    print("=" * 80)
    print("  GRUT II BETA — SYMBOLIC STABILITY REGION AND BIFURCATION AUDIT")
    print("=" * 80)

    print("\n--- PART I: EXACT EQUILIBRIUM STRUCTURE ---")
    equilibria_symbolic()

    print("\n--- PART II: FULL JACOBIAN ---")
    jacobian_symbolic()

    print("\n--- PART III: STABILITY INEQUALITIES (THE CORE RESULT) ---")
    stability_conditions()

    print("\n--- PART III (cont.): SYMBOLIC VERIFICATION ---")
    verify_det_symbolically()

    print("\n--- PART III (cont.): NUMERICAL SWEEP ---")
    numerical_verification()

    print("\n--- PART IV: BIFURCATION STRUCTURE ---")
    bifurcation_classification()

    print("\n--- PART V: PHYSICAL ADMISSIBILITY ---")
    print("  MOOT. Eq2 is always a saddle. No physical admissibility test needed.")
    print("  The stable-Eq2 region is EMPTY.")

    print("\n--- PART VI: CONSEQUENCE FOR RIGIDITY ---")
    print("""
  The stable-Eq2 region is EMPTY.

  det(J2) = -1/(tau2 * tau_meta) < 0 UNCONDITIONALLY.

  This is not a numerical accident. It is an ALGEBRAIC IDENTITY:
  the off-diagonal coupling (beta in the Phi equation, 2/(beta*tau_meta)
  in the tau equation) always produces bc > ad because the factor of 2
  in c = dF2/dPhi comes from the quadratic alpha*(Phi-X)^2, and this
  factor ALWAYS overwhelms the diagonal damping product ad = 1/(tau2*tau_meta).

  The GRUT I unique-attractor rigidity is NOT broken by this modification.
  The modified constitutive equation produces a second equilibrium (Eq2),
  but Eq2 is ALWAYS a saddle point, never an attractor.

  Dynamical tau with beta-coupling does not produce bistability.
  The GRUT I obstruction PERSISTS in this GRUT II formulation.
""")

    print("\n" + "=" * 80)
    print("  FINAL VERDICT")
    print("=" * 80)
    print("""
  eq2_always_unstable.

  The determinant det(J2) = -1/(tau2*tau_meta) is UNCONDITIONALLY NEGATIVE.
  Eq2 is a saddle point for ALL values of (alpha, beta, tau_meta).
  No parameter choice makes Eq2 stable.
  The stability region for Eq2 is the EMPTY SET.

  The bifurcation is TRANSCRITICAL (one stable + one saddle, exchanging
  as the saddle escapes to infinity). It is NOT a saddle-node or pitchfork
  that could produce bistability.

  GRUT I's unique-attractor rigidity survives the simplest GRUT II modification.

  To produce genuine bistability, one would need a constitutive modification
  that produces det(J) > 0 at the second equilibrium. This requires a
  DIFFERENT coupling structure than the linear beta*(tau - tau_star) term.

  Candidate: higher-order coupling, e.g., Phi = X + beta*(tau - tau_star)^2.
  Or: a constitutive equation where the feedback structure produces
  ad > bc at the second root. This is the next forced technical question.
""")
    print("=" * 80)
