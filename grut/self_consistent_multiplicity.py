"""
GRUT-IV Alpha — Self-Consistent Fixed-Point Multiplicity Search
================================================================

The constitutive equation with self-consistent source:

    tau dPhi/dt + Phi = X(Phi)

where X depends on Phi through the Einstein equations:

    X(r) = m(r) / r^2
    dm/dr = 4 pi r^2 rho(Phi)
    rho(Phi) = Phi^2/(2 tau^2) - Phi X / tau

At equilibrium (dPhi/dt = 0): Phi = X(Phi).

This is a SELF-CONSISTENT fixed-point equation. X depends on Phi
through the metric (Einstein eqs + T^Phi). Phi depends on X through
the constitutive law.

The loop: Phi -> rho(Phi) -> m(r) -> X(r) -> Phi_eq = X

If this loop has MULTIPLE self-consistent fixed points, the
unique-attractor theorem is broken by the ARCHITECTURE ITSELF.

WHAT THIS MODULE DOES:
  1. Formulates the self-consistent fixed-point equation Phi = X(Phi)
  2. Solves it numerically at each radius
  3. Tests whether multiple solutions exist
  4. If multiple solutions: characterizes the basin structure
"""

import math
import numpy as np
from typing import List, Tuple

# Constants (geometric units, r_s = 1)
TAU_SQ = 1.5
TAU = math.sqrt(TAU_SQ)
M_EXT = 0.5  # exterior mass
R_S = 1.0
R_EQ = R_S / 3.0  # equilibrium radius
R_EXT = 2.0 * R_S


def rho_constitutive(Phi, X, tau_sq=TAU_SQ):
    """Energy density at given Phi and source X.

    rho = V(Phi) - Phi*J = Phi^2/(2 tau^2) - Phi*X/tau

    Note: this is the FULL rho, not just the equilibrium value.
    At Phi = X: rho_eq = -X^2/(2 tau^2)
    """
    return Phi**2 / (2 * tau_sq) - Phi * X / math.sqrt(tau_sq)


def self_consistent_X(Phi_profile, r_grid, M_ext=M_EXT):
    """Compute X(r) = m(r)/r^2 self-consistently from Phi profile.

    Given Phi(r), compute:
      rho(r) from the constitutive energy density
      m(r) by integrating dm/dr = 4 pi r^2 rho from R_ext inward
      X(r) = m(r) / r^2
    """
    n = len(r_grid)

    # First compute rho(r) self-consistently
    # At each r: X_current = m(r)/r^2, rho = Phi^2/(2tau^2) - Phi*X/tau
    # But X depends on m which depends on rho which depends on X...
    # We need to iterate.

    # Start with X = M_ext/r^2 (Schwarzschild)
    X = M_ext / r_grid**2

    for iteration in range(50):
        # Compute rho from current Phi and X
        rho = Phi_profile**2 / (2 * TAU_SQ) - Phi_profile * X / TAU

        # Integrate mass inward from R_ext
        m = np.zeros(n)
        # Find index closest to R_ext
        i_ext = np.argmin(np.abs(r_grid - R_EXT))
        m[i_ext] = M_ext

        for i in range(i_ext - 1, -1, -1):
            dr = r_grid[i+1] - r_grid[i]
            r_mid = 0.5 * (r_grid[i] + r_grid[i+1])
            rho_mid = 0.5 * (rho[i] + rho[i+1])
            dm = 4 * math.pi * r_mid**2 * rho_mid * dr
            m[i] = m[i+1] - dm

        # Update X
        X_new = np.where(r_grid > 1e-10, m / r_grid**2, 0)

        # Check convergence
        if np.max(np.abs(X_new - X)) < 1e-10:
            break
        X = X_new

    return X, m


def find_fixed_points_at_radius(r, m_background=M_EXT, n_search=1000):
    """Find ALL fixed points of Phi = X(Phi) at a given radius.

    At a single radius r, the self-consistent equation is:

      Phi = X(Phi) where X depends on m(r) which depends on rho(Phi)

    For a simplified single-radius analysis:
      The enclosed mass at r depends on the energy density integrated
      from r to R_ext. At a single radius, we can model this as:

      m(r) = M_ext - integral_r^R_ext 4 pi r'^2 rho(Phi, X) dr'

    For the self-consistent single-point problem, we need the
    INTEGRATED effect of Phi on m. Let's define:

      Delta_m(Phi) = integral_r^R_ext 4 pi r'^2 [rho(Phi) - rho_Schw] dr'

    where rho_Schw = 0 (vacuum Schwarzschild). Then:
      m(r) = M_ext - Delta_m(Phi)
      X(r) = m(r) / r^2 = (M_ext - Delta_m(Phi)) / r^2

    For a shell from r to R_ext with uniform Phi:
      Delta_m = 4 pi * integral_r^R_ext r'^2 rho(Phi, X) dr'

    The integral depends on X which depends on m which depends on Delta_m.
    Self-consistency: Phi = X = (M_ext - Delta_m(Phi)) / r^2

    Let's compute Delta_m as a function of Phi for uniform-Phi shell:
      rho(Phi, X) = Phi^2/(2 tau^2) - Phi X / tau

    With X = (M_ext - Delta_m) / r^2 and Delta_m depending on the integral
    of rho which depends on X...

    For the SINGLE-RADIUS approximation, assume Phi is uniform in the shell
    [r, R_ext] and compute the self-consistent X:

      rho(Phi) = Phi^2/(2 tau^2) - Phi * X / tau
      Delta_m = (4 pi / 3) * (R_ext^3 - r^3) * rho
      X = (M_ext - Delta_m) / r^2

    Substituting:
      X = [M_ext - (4pi/3)(R_ext^3 - r^3)(Phi^2/(2tau^2) - Phi X / tau)] / r^2

    This is an equation for X given Phi. Solve:
      r^2 X = M_ext - V_shell * (Phi^2/(2tau^2) - Phi X / tau)
      r^2 X = M_ext - V_shell Phi^2/(2tau^2) + V_shell Phi X / tau
      r^2 X - V_shell Phi X / tau = M_ext - V_shell Phi^2/(2tau^2)
      X (r^2 - V_shell Phi / tau) = M_ext - V_shell Phi^2/(2tau^2)
      X = [M_ext - V_shell Phi^2/(2tau^2)] / [r^2 - V_shell Phi / tau]

    Fixed point: Phi = X, so:
      Phi = [M_ext - V_shell Phi^2/(2tau^2)] / [r^2 - V_shell Phi / tau]
      Phi (r^2 - V_shell Phi / tau) = M_ext - V_shell Phi^2/(2tau^2)
      Phi r^2 - V_shell Phi^2 / tau = M_ext - V_shell Phi^2/(2tau^2)
      Phi r^2 = M_ext - V_shell Phi^2/(2tau^2) + V_shell Phi^2/tau
      Phi r^2 = M_ext + V_shell Phi^2 [1/tau - 1/(2tau^2)]
      Phi r^2 = M_ext + V_shell Phi^2 (2tau - 1)/(2tau^2)

    This is a QUADRATIC in Phi:
      V_shell (2tau - 1)/(2tau^2) Phi^2 - r^2 Phi + M_ext = 0

    For tau = sqrt(3/2) ~ 1.2247:
      2tau - 1 = 2*1.2247 - 1 = 1.4494
      (2tau-1)/(2tau^2) = 1.4494 / 3.0 = 0.4831

    So: 0.4831 V_shell Phi^2 - r^2 Phi + M_ext = 0

    The DISCRIMINANT determines whether there are 0, 1, or 2 solutions:
      Delta = r^4 - 4 * 0.4831 * V_shell * M_ext
            = r^4 - 1.9325 * V_shell * M_ext
    """
    V_shell = (4 * math.pi / 3) * (R_EXT**3 - r**3)

    coeff_a = (2*TAU - 1) / (2*TAU_SQ) * V_shell  # coefficient of Phi^2
    coeff_b = -r**2                                  # coefficient of Phi
    coeff_c = M_EXT                                  # constant

    discriminant = coeff_b**2 - 4 * coeff_a * coeff_c

    solutions = []

    if coeff_a == 0:
        # Linear: one solution
        if coeff_b != 0:
            solutions.append(-coeff_c / coeff_b)
    elif discriminant > 0:
        # Two real solutions
        sqrt_disc = math.sqrt(discriminant)
        Phi_1 = (-coeff_b + sqrt_disc) / (2 * coeff_a)
        Phi_2 = (-coeff_b - sqrt_disc) / (2 * coeff_a)
        solutions.append(Phi_1)
        solutions.append(Phi_2)
    elif discriminant == 0:
        # One real solution (degenerate)
        Phi_0 = -coeff_b / (2 * coeff_a)
        solutions.append(Phi_0)
    # else: discriminant < 0 → no real solutions

    return solutions, discriminant, coeff_a, coeff_b, coeff_c


if __name__ == "__main__":
    print("=" * 80)
    print("  GRUT-IV ALPHA — SELF-CONSISTENT FIXED-POINT MULTIPLICITY SEARCH")
    print("  Does Phi = X(Phi) have multiple solutions?")
    print("=" * 80)

    print("\n--- THE SELF-CONSISTENT FIXED-POINT EQUATION ---")
    print("  tau dPhi/dt + Phi = X(Phi)")
    print("  At equilibrium: Phi = X(Phi)")
    print("  X = [M - Delta_m(Phi)] / r^2")
    print("  Delta_m depends on rho(Phi, X) integrated over shell")
    print("  Self-consistency yields a QUADRATIC in Phi:")
    print("    a*Phi^2 + b*Phi + c = 0")
    print("  where a = (2tau-1)/(2tau^2) * V_shell")
    print("        b = -r^2")
    print("        c = M_ext")
    print()
    print("  tau = {:.4f}".format(TAU))
    print("  (2tau-1)/(2tau^2) = {:.4f}".format((2*TAU-1)/(2*TAU_SQ)))
    print("  M_ext = {:.4f}".format(M_EXT))

    print("\n--- RADIUS SCAN: FIXED POINTS AT EACH r ---")
    print("{:>8s} {:>10s} {:>10s} {:>12s} {:>12s} {:>12s} {:>8s}".format(
        "r/r_s", "V_shell", "discrim", "Phi_1", "Phi_2", "X_Schw", "N_sol"))
    print("-" * 75)

    r_values = np.linspace(R_EQ + 0.01, R_EXT - 0.01, 50)

    multiplicity_found = False

    for r in r_values:
        sols, disc, a, b, c = find_fixed_points_at_radius(r)
        X_schw = M_EXT / r**2
        n_sol = len([s for s in sols if s > 0])  # physical solutions (Phi > 0)

        sol_strs = []
        for s in sols:
            sol_strs.append("{:.6f}".format(s))

        if n_sol >= 2:
            multiplicity_found = True
            marker = " <-- MULTIPLE"
        else:
            marker = ""

        print("{:8.4f} {:10.4f} {:10.4f} {:>12s} {:>12s} {:12.6f} {:8d}{}".format(
            r, (4*math.pi/3)*(R_EXT**3 - r**3), disc,
            sol_strs[0] if len(sol_strs) > 0 else "—",
            sol_strs[1] if len(sol_strs) > 1 else "—",
            X_schw, n_sol, marker))

    print("\n--- DISCRIMINANT ANALYSIS ---")
    print("  Discriminant = r^4 - 4 * a_coeff * M_ext")
    print("  = r^4 - {:.4f} * V_shell".format(4 * (2*TAU-1)/(2*TAU_SQ) * M_EXT))
    print()

    # Find the critical radius where discriminant = 0
    # disc = r^4 - 1.9325 * V_shell(r) * 0.5
    # V_shell = (4pi/3)(R_ext^3 - r^3) = (4pi/3)(8 - r^3) for R_ext = 2
    # disc = r^4 - 0.9663 * (4pi/3)(8 - r^3)
    # disc = r^4 - 4.051 * (8 - r^3)
    # disc = r^4 + 4.051 r^3 - 32.41

    coeff = (2*TAU-1)/(2*TAU_SQ) * M_EXT
    print("  Key coefficient: 4*a*c = 4 * {:.4f} * V_shell * {:.4f}".format(
        (2*TAU-1)/(2*TAU_SQ), M_EXT))

    # Check discriminant sign at boundaries
    r_min_test = R_EQ + 0.01
    r_max_test = R_EXT - 0.01
    _, disc_min, _, _, _ = find_fixed_points_at_radius(r_min_test)
    _, disc_max, _, _, _ = find_fixed_points_at_radius(r_max_test)
    print("  Discriminant at r = {:.3f}: {:.4f}".format(r_min_test, disc_min))
    print("  Discriminant at r = {:.3f}: {:.4f}".format(r_max_test, disc_max))

    # Check if both solutions are physical (Phi > 0)
    print("\n--- PHYSICAL SOLUTION COUNT ---")
    print("  For MULTIPLE fixed points, we need TWO solutions with Phi > 0.")
    print()

    two_physical = 0
    one_physical = 0
    zero_physical = 0

    for r in r_values:
        sols, disc, a, b, c = find_fixed_points_at_radius(r)
        physical = [s for s in sols if s > 0]
        if len(physical) >= 2:
            two_physical += 1
        elif len(physical) == 1:
            one_physical += 1
        else:
            zero_physical += 1

    print("  Radii with 2 physical solutions: {}".format(two_physical))
    print("  Radii with 1 physical solution:  {}".format(one_physical))
    print("  Radii with 0 physical solutions: {}".format(zero_physical))

    # Detailed look at a radius with two solutions
    if two_physical > 0:
        print("\n--- DETAILED ANALYSIS OF MULTIPLICITY POINT ---")
        for r in r_values:
            sols, disc, a, b, c = find_fixed_points_at_radius(r)
            physical = [s for s in sols if s > 0]
            if len(physical) >= 2:
                print("  r = {:.4f} r_s:".format(r))
                print("    Solution 1: Phi = {:.6f}".format(physical[0]))
                print("    Solution 2: Phi = {:.6f}".format(physical[1]))
                X_schw = M_EXT / r**2
                print("    Schwarzschild X = {:.6f}".format(X_schw))
                print("    Ratio Phi_1/Phi_2 = {:.4f}".format(physical[0]/physical[1]))

                # Check stability of each
                # The fixed point Phi_eq = X(Phi_eq) is stable if dX/dPhi < 1 at that point
                # From the quadratic: dX/dPhi = d/dPhi [(M - V_shell rho(Phi,X)) / r^2]
                # This requires implicit differentiation through the self-consistency

                # Simple check: which solution is the "Schwarzschild-like" one?
                print("    Distance to Schwarzschild:")
                print("      |Phi_1 - X_Schw| = {:.6f}".format(abs(physical[0] - X_schw)))
                print("      |Phi_2 - X_Schw| = {:.6f}".format(abs(physical[1] - X_schw)))
                break

    print("\n" + "=" * 80)
    print("  VERDICT")
    print("=" * 80)

    if two_physical > 0:
        print("""
  MULTIPLE SELF-CONSISTENT FIXED POINTS FOUND.

  The self-consistent equation Phi = X(Phi), derived from the GRUT
  constitutive law coupled to Einstein gravity through Phase 4 T^Phi,
  is a QUADRATIC in Phi. The quadratic has TWO real positive solutions
  at {} of {} tested radii.

  This means: the GRUT architecture, when made fully self-consistent
  (Phi determines T^Phi determines metric determines X determines Phi),
  naturally produces MULTIPLE EQUILIBRIA.

  The unique-attractor theorem (XX Alpha) applied to the LINEAR equation
  tau dPhi/dt + Phi = X with X FIXED. When X depends on Phi through
  the Einstein equations, the effective equation is NONLINEAR and the
  unique-attractor result DOES NOT APPLY.

  This is the structural break the program has been searching for since
  Book XX. It comes not from noise, not from new postulates, not from
  CTP doubling — but from the SELF-CONSISTENCY of the existing architecture.

  COST: ZERO. No new postulates. No new parameters. The self-consistent
  loop Phi <-> X(Phi) uses only the constitutive equation (Book II),
  the Phase 4 T^Phi (locked), and the Einstein equations (GR).

  WHAT THIS OPENS: If the equilibrium landscape has multiple basins,
  the basin volumes define a NATURAL MEASURE — probability from
  deterministic self-consistent dynamics.
""".format(two_physical, len(r_values)))
    else:
        print("""
  NO MULTIPLICITY FOUND in the single-radius uniform-shell approximation.
  The self-consistent quadratic has at most one physical (Phi > 0) solution
  at every tested radius.

  The unique-attractor theorem survives the self-consistency test.
  The program is genuinely terminal.
""")
    print("=" * 80)
