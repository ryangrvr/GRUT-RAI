"""
GRUT-IV Beta — Stability, Global Branch, and Basin Audit
==========================================================

Tests whether the multiple fixed points from GRUT-IV Alpha are:
  1. Both dynamically stable (local stability)
  2. Part of global radial solution branches (not just local roots)
  3. Structurally stable (persist under parameter variation)
  4. Associated with nontrivial basin structure

THE KEY EQUATION:

  tau dPhi/dt + Phi = X(Phi)

where X(Phi) is determined self-consistently through:
  rho(Phi, X) = Phi^2/(2tau^2) - Phi*X/tau
  dm/dr = 4*pi*r^2 * rho
  X = m/r^2

Linearized stability: dPhi'/dt = [(X'(Phi*) - 1)/tau] * dPhi
  Stable if X'(Phi*) < 1
  Unstable if X'(Phi*) > 1
"""

import math
import numpy as np
from typing import List, Tuple

TAU_SQ = 1.5
TAU = math.sqrt(TAU_SQ)
M_EXT = 0.5
R_S = 1.0
R_EQ = R_S / 3.0
R_EXT = 2.0 * R_S


def find_roots_and_stability(r):
    """Find fixed points and their stability at radius r.

    Self-consistent equation (from Alpha):
      a*Phi^2 + b*Phi + c = 0
    where:
      a = (2*tau - 1)/(2*tau^2) * V_shell
      b = -r^2
      c = M_ext

    Stability requires computing X'(Phi) at each root.

    From X = [M_ext - V_shell * rho(Phi, X)] / r^2 and self-consistency:
      X(Phi) = [M_ext - V_shell * (Phi^2/(2tau^2) - Phi*X(Phi)/tau)] / r^2

    Implicit differentiation:
      dX/dPhi = [-V_shell * (Phi/tau^2 - X/tau - Phi*(dX/dPhi)/tau)] / r^2

    Solving for dX/dPhi:
      r^2 dX/dPhi = -V_shell Phi/tau^2 + V_shell X/tau + V_shell Phi dX/dPhi / tau
      r^2 dX/dPhi - V_shell Phi dX/dPhi / tau = -V_shell Phi/tau^2 + V_shell X/tau
      dX/dPhi (r^2 - V_shell Phi / tau) = V_shell (X/tau - Phi/tau^2)
      dX/dPhi = V_shell (X - Phi/tau) / (tau (r^2 - V_shell Phi / tau))

    At the fixed point Phi* = X*:
      dX/dPhi = V_shell (Phi* - Phi*/tau) / (tau (r^2 - V_shell Phi* / tau))
              = V_shell Phi* (1 - 1/tau) / (tau (r^2 - V_shell Phi* / tau))
              = V_shell Phi* (tau - 1) / (tau^2 (r^2 - V_shell Phi* / tau))

    Stability condition: X'(Phi*) < 1
    """
    V_shell = (4 * math.pi / 3) * (R_EXT**3 - r**3)

    # Quadratic coefficients
    a = (2*TAU - 1) / (2*TAU_SQ) * V_shell
    b = -r**2
    c = M_EXT

    disc = b**2 - 4*a*c

    results = []

    if disc < 0:
        return results  # No real roots

    if a == 0:
        if b != 0:
            Phi_star = -c / b
            if Phi_star > 0:
                results.append({"Phi": Phi_star, "stable": True, "dXdPhi": 0, "type": "degenerate"})
        return results

    sqrt_disc = math.sqrt(disc)
    roots = [(-b + sqrt_disc) / (2*a), (-b - sqrt_disc) / (2*a)]

    for Phi_star in roots:
        if Phi_star <= 0:
            continue

        # Compute dX/dPhi at the fixed point
        denominator = TAU_SQ * (r**2 - V_shell * Phi_star / TAU)
        if abs(denominator) < 1e-20:
            dXdPhi = float('inf')
        else:
            dXdPhi = V_shell * Phi_star * (TAU - 1) / denominator

        # Stability: the linearized equation is
        # tau dPhi'/dt = (X'(Phi*) - 1) Phi'
        # Eigenvalue: lambda = (X'(Phi*) - 1) / tau
        # Stable if lambda < 0, i.e., X'(Phi*) < 1

        eigenvalue = (dXdPhi - 1) / TAU
        stable = eigenvalue < 0

        if stable:
            ftype = "stable_attractor"
        elif abs(eigenvalue) < 1e-10:
            ftype = "marginal"
        else:
            ftype = "unstable"

        results.append({
            "Phi": Phi_star,
            "dXdPhi": dXdPhi,
            "eigenvalue": eigenvalue,
            "stable": stable,
            "type": ftype,
        })

    return results


def scan_radii_stability():
    """Scan stability across radii."""
    r_values = np.linspace(R_EQ + 0.01, R_EXT - 0.01, 200)
    all_results = []

    for r in r_values:
        roots = find_roots_and_stability(r)
        all_results.append((r, roots))

    return all_results


def global_branch_test():
    """Test whether the two roots form continuous branches across radii.

    If at adjacent radii the roots connect smoothly, they form branches.
    If a root appears/disappears (bifurcation), record the bifurcation point.
    """
    r_values = np.linspace(R_EQ + 0.01, R_EXT - 0.01, 500)
    branch_high = []  # higher Phi root
    branch_low = []   # lower Phi root
    bifurcation_r = None

    for r in r_values:
        roots = find_roots_and_stability(r)
        physical = [rt for rt in roots if rt["Phi"] > 0]

        if len(physical) == 0:
            branch_high.append((r, None, None))
            branch_low.append((r, None, None))
        elif len(physical) == 1:
            branch_high.append((r, None, None))
            branch_low.append((r, physical[0]["Phi"], physical[0]["stable"]))
        else:
            # Sort by Phi value
            physical.sort(key=lambda x: x["Phi"])
            branch_low.append((r, physical[0]["Phi"], physical[0]["stable"]))
            branch_high.append((r, physical[1]["Phi"], physical[1]["stable"]))

            if bifurcation_r is None:
                bifurcation_r = r

    return branch_high, branch_low, bifurcation_r


def structural_stability_test():
    """Test persistence of multiplicity under parameter variation."""
    # Vary tau^2 from 1.0 to 2.0 (canonical is 1.5)
    # Vary M_ext from 0.3 to 0.7 (canonical is 0.5)
    results = []

    for tau_sq in [1.0, 1.2, 1.5, 1.8, 2.0, 2.5, 3.0]:
        tau = math.sqrt(tau_sq)
        for M in [0.3, 0.4, 0.5, 0.6, 0.7]:
            # Check at r = 1.85 (where Alpha found multiplicity)
            r = 1.85
            V_shell = (4 * math.pi / 3) * (R_EXT**3 - r**3)
            a = (2*tau - 1) / (2*tau_sq) * V_shell
            b = -r**2
            c = M
            disc = b**2 - 4*a*c
            n_physical = 0
            if disc >= 0 and a != 0:
                sqrt_d = math.sqrt(disc)
                r1 = (-b + sqrt_d) / (2*a)
                r2 = (-b - sqrt_d) / (2*a)
                if r1 > 0: n_physical += 1
                if r2 > 0: n_physical += 1

            results.append({
                "tau_sq": tau_sq,
                "M": M,
                "disc": disc,
                "n_physical": n_physical,
            })

    return results


if __name__ == "__main__":
    print("=" * 80)
    print("  GRUT-IV BETA — STABILITY, GLOBAL BRANCH, AND BASIN AUDIT")
    print("=" * 80)

    # ================================================================
    # PART I: LOCAL STABILITY TEST
    # ================================================================
    print("\n" + "=" * 80)
    print("  PART I: LOCAL STABILITY OF EACH ROOT")
    print("=" * 80)

    print("\n  Stability condition: X'(Phi*) < 1  =>  stable attractor")
    print("  Eigenvalue: lambda = (X'(Phi*) - 1) / tau")
    print()

    print("  {:>8s} {:>10s} {:>10s} {:>10s} {:>12s} {:>15s}".format(
        "r/r_s", "Phi*", "X'(Phi*)", "eigenval", "stable?", "type"))
    print("  " + "-" * 70)

    all_results = scan_radii_stability()
    n_two_stable = 0
    n_one_stable_one_unstable = 0

    for r, roots in all_results:
        if len(roots) < 2:
            continue
        for rt in roots:
            print("  {:8.4f} {:10.6f} {:10.4f} {:10.4f} {:>12s} {:>15s}".format(
                r, rt["Phi"], rt["dXdPhi"], rt["eigenvalue"],
                "YES" if rt["stable"] else "NO", rt["type"]))

        stables = [rt for rt in roots if rt["stable"]]
        if len(stables) == 2:
            n_two_stable += 1
        elif len(stables) == 1:
            n_one_stable_one_unstable += 1

    print("\n  SUMMARY:")
    print("  Radii with 2 stable attractors: {}".format(n_two_stable))
    print("  Radii with 1 stable + 1 unstable: {}".format(n_one_stable_one_unstable))

    # ================================================================
    # PART II: GLOBAL BRANCH STRUCTURE
    # ================================================================
    print("\n" + "=" * 80)
    print("  PART II: GLOBAL BRANCH STRUCTURE")
    print("=" * 80)

    branch_hi, branch_lo, bif_r = global_branch_test()

    print("\n  Bifurcation radius: r = {:.4f} r_s".format(bif_r if bif_r else 0))
    print()

    # Print branch structure near bifurcation
    print("  {:>8s} {:>12s} {:>8s} {:>12s} {:>8s}".format(
        "r/r_s", "Phi_low", "stable?", "Phi_high", "stable?"))
    print("  " + "-" * 55)

    for i in range(len(branch_lo)):
        r_lo, phi_lo, s_lo = branch_lo[i]
        _, phi_hi, s_hi = branch_hi[i]

        if phi_lo is None and phi_hi is None:
            continue

        if abs(r_lo - bif_r) < 0.1 or (phi_hi is not None):
            print("  {:8.4f} {:>12s} {:>8s} {:>12s} {:>8s}".format(
                r_lo,
                "{:.6f}".format(phi_lo) if phi_lo is not None else "—",
                "Y" if s_lo else "N" if s_lo is not None else "—",
                "{:.6f}".format(phi_hi) if phi_hi is not None else "—",
                "Y" if s_hi else "N" if s_hi is not None else "—"))

    # Count radii with two branches
    n_two_branch = sum(1 for _, phi, _ in branch_hi if phi is not None)
    print("\n  Radii with two branches: {} / {}".format(n_two_branch, len(branch_hi)))

    # ================================================================
    # PART III: STRUCTURAL STABILITY
    # ================================================================
    print("\n" + "=" * 80)
    print("  PART III: STRUCTURAL STABILITY UNDER PARAMETER VARIATION")
    print("=" * 80)

    ss_results = structural_stability_test()

    print("\n  At r = 1.85 r_s:")
    print("  {:>8s} {:>6s} {:>10s} {:>10s}".format("tau^2", "M", "discrim", "N_phys"))
    print("  " + "-" * 40)

    n_multi = 0
    for res in ss_results:
        marker = " <--" if res["n_physical"] >= 2 else ""
        print("  {:8.2f} {:6.2f} {:10.4f} {:10d}{}".format(
            res["tau_sq"], res["M"], res["disc"], res["n_physical"], marker))
        if res["n_physical"] >= 2:
            n_multi += 1

    print("\n  Parameter points with multiplicity: {} / {}".format(
        n_multi, len(ss_results)))
    print("  Multiplicity is {}".format(
        "STRUCTURALLY STABLE (persists across parameter variation)"
        if n_multi > len(ss_results) // 3 else
        "CONDITIONALLY STABLE (persists in a parameter subregion)" if n_multi > 0 else
        "STRUCTURALLY UNSTABLE (vanishes under parameter variation)"))

    # ================================================================
    # PART IV-V: BASIN AND PROBABILITY
    # ================================================================
    print("\n" + "=" * 80)
    print("  PART IV-V: BASIN STRUCTURE AND PROBABILITY RELEVANCE")
    print("=" * 80)

    # For the basin analysis: the state space is Phi(r=r_test) for the
    # self-consistent equation at a given radius.
    # The two attractors divide the real line into basins.
    # The unstable fixed point (if it exists) is the basin boundary.

    # At r = 1.85:
    r_test = 1.85
    roots = find_roots_and_stability(r_test)
    physical = [rt for rt in roots if rt["Phi"] > 0]
    physical.sort(key=lambda x: x["Phi"])

    if len(physical) >= 2:
        print("\n  At r = {:.2f} r_s:".format(r_test))
        for i, rt in enumerate(physical):
            print("    Root {}: Phi* = {:.6f}, X'={:.4f}, eigenvalue={:.4f}, {}".format(
                i+1, rt["Phi"], rt["dXdPhi"], rt["eigenvalue"], rt["type"]))

        stables = [rt for rt in physical if rt["stable"]]
        unstables = [rt for rt in physical if not rt["stable"]]

        if len(stables) == 2:
            print("\n  TWO STABLE ATTRACTORS. Basin boundary exists between them.")
            # The basin boundary is where the flow reverses direction
            # For tau dPhi/dt + Phi = X(Phi), the flow is:
            # dPhi/dt = (X(Phi) - Phi) / tau
            # The boundary is at Phi where X(Phi) = Phi (the unstable fixed point)
            # But if there's no unstable FP between the two stables, the dynamics
            # would need to be analyzed more carefully.
            print("  Need to find the unstable fixed point between the two stables.")
            print("  If the quadratic has only 2 roots and both are stable,")
            print("  there MUST be an unstable equilibrium between them")
            print("  (by the intermediate value theorem for the flow).")
            print()
            print("  However: the quadratic Phi = X(Phi) has EXACTLY 2 roots.")
            print("  If both are stable, there is no third root to serve as")
            print("  the basin boundary. This is a contradiction for a 1D flow")
            print("  (in 1D, stable and unstable must alternate).")
            print()
            print("  RESOLUTION: In a 1D autonomous ODE, if there are exactly")
            print("  2 fixed points and the flow is continuous, one MUST be stable")
            print("  and one MUST be unstable. Two stables is impossible without")
            print("  an unstable between them.")
            print()
            print("  THEREFORE: one of the two 'stable' classifications may be wrong,")
            print("  or there is a third fixed point we are missing (e.g., at Phi < 0")
            print("  or at Phi = infinity).")

        elif len(stables) == 1 and len(unstables) == 1:
            stable_root = stables[0]
            unstable_root = unstables[0]
            print("\n  ONE STABLE + ONE UNSTABLE.")
            print("  Stable attractor: Phi* = {:.6f}".format(stable_root["Phi"]))
            print("  Unstable fixed point: Phi* = {:.6f}".format(unstable_root["Phi"]))
            print()
            print("  The unstable root is NOT an attractor.")
            print("  ALL initial conditions (above and below the unstable root)")
            print("  flow toward the SINGLE stable attractor.")
            print()
            print("  In the 1D flow tau dPhi/dt = X(Phi) - Phi:")
            print("    For Phi > Phi_unstable: flow depends on sign of X(Phi) - Phi")
            print("    For Phi < Phi_unstable: flow depends on sign of X(Phi) - Phi")
            print()

            # Verify by checking the flow direction
            print("  Flow direction check:")
            Phi_test_values = np.linspace(0.01, max(rt["Phi"] for rt in physical) * 1.5, 20)
            V_shell = (4 * math.pi / 3) * (R_EXT**3 - r_test**3)
            for Phi_t in Phi_test_values:
                # X(Phi) from the self-consistent relation
                # From the quadratic derivation:
                # X = [M - V_shell * rho(Phi, X)] / r^2
                # With Phi fixed, solve for X:
                # r^2 X = M - V_shell(Phi^2/(2tau^2) - Phi X / tau)
                # r^2 X + V_shell Phi X / tau = M - V_shell Phi^2/(2tau^2)
                # X(r^2 + V_shell Phi/tau) = M - V_shell Phi^2/(2tau^2)
                denom = r_test**2 + V_shell * Phi_t / TAU
                if abs(denom) > 1e-20:
                    X_of_Phi = (M_EXT - V_shell * Phi_t**2 / (2*TAU_SQ)) / denom
                else:
                    X_of_Phi = 0

                flow = (X_of_Phi - Phi_t) / TAU
                direction = "→ right" if flow > 0 else "← left" if flow < 0 else "= zero"
                marker = " ***" if abs(flow) < 0.01 else ""
                print("    Phi={:.4f}: X(Phi)={:.4f}, flow={:+.4f} {}{}".format(
                    Phi_t, X_of_Phi, flow, direction, marker))

            print()
            print("  BASIN STRUCTURE:")
            print("  If the unstable root separates two flow regions, one flowing to")
            print("  the stable root and one flowing to Phi → infinity or Phi → 0,")
            print("  then there is ONE attractor basin (the stable root) and one")
            print("  'escape' region. This is NOT two competing basins.")
            print()
            print("  For genuine multiplicity, we need TWO STABLE attractors with")
            print("  an unstable fixed point between them. The 1D quadratic gives")
            print("  at most 2 roots; alternating stability means 1 stable + 1 unstable.")
            print()
            print("  VERDICT ON MULTIPLICITY:")
            print("  The self-consistent equation has ONE STABLE ATTRACTOR at each radius.")
            print("  The second root is unstable. Initial conditions either converge to")
            print("  the stable root or escape to Phi → ∞ (or negative Phi).")
            print("  This is NOT the multi-basin structure needed for probability.")

    # ================================================================
    # FINAL VERDICT
    # ================================================================
    print("\n" + "=" * 80)
    print("  FINAL VERDICT")
    print("=" * 80)

    # Count the actual stability pattern across all radii
    n_1s_1u = 0
    n_2s = 0
    n_other = 0
    for r, roots in all_results:
        physical = [rt for rt in roots if rt["Phi"] > 0]
        if len(physical) < 2:
            continue
        stables = sum(1 for rt in physical if rt["stable"])
        if stables == 2:
            n_2s += 1
        elif stables == 1:
            n_1s_1u += 1
        else:
            n_other += 1

    print()
    print("  Multi-root radii stability pattern:")
    print("    1 stable + 1 unstable: {}".format(n_1s_1u))
    print("    2 stable: {}".format(n_2s))
    print("    Other: {}".format(n_other))

    if n_2s > 0:
        print("""
  WARNING: {} radii show 2 stable roots. In a 1D autonomous flow, this is
  IMPOSSIBLE without an intermediate unstable root. Either:
  (a) the stability calculation has an error, or
  (b) the effective flow is not truly 1D (the full radial problem couples
      different radii), or
  (c) the single-radius approximation is breaking down.

  This REQUIRES the full radial profile analysis (Part II) to resolve.
""".format(n_2s))

    if n_1s_1u > 0 and n_2s == 0:
        print("""
  RESULT: multiple_roots_but_single_attractor.

  The self-consistent equation Phi = X(Phi) has two roots at radii
  r > {:.2f} r_s. But the stability analysis shows ONE is stable and
  ONE is unstable at every multi-root radius. This is the standard
  pattern for a 1D flow with a quadratic fixed-point equation.

  The unstable root is a REPELLER, not a second attractor. All initial
  conditions either converge to the single stable root or escape.
  There is ONE basin, not two.

  XX Alpha's unique-attractor obstruction is NOT broken. The self-consistent
  nonlinearity produces a second ROOT but not a second ATTRACTOR.
  The probability question remains closed.

  COST: still zero (no new postulates were needed for this analysis).
  RESULT: the self-consistent architecture does NOT produce multiple basins.
""".format(bif_r if bif_r else 0))

    print("=" * 80)
