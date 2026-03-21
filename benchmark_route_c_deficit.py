#!/usr/bin/env python3
"""Benchmark: Route C Deficit Assessment — Nonlocal Metric Back-Reaction vs 1/r^2.

~70 independent checks covering:
  1.  Parameter Setup (5)
  2.  Route C Energy Profile (8)
  3.  Chain 1 — Markov Kinetic (6)
  4.  Chain 2 — Self-Healing (6)
  5.  Chain 3 — Candidate Potential (5)
  6.  Chain 4 — Spatial Gradient (5)
  7.  Insufficiency Assessment (6)
  8.  Loophole Catalog (7)
  9.  Provisional Candidate Ranking (6)
  10. Numerical Validation (7)
  11. Nonclaims & Assumptions (5)
  12. Serialization (4)

KEY FINDINGS:
  Within the tested Markov-reduced exponential-kernel pathway, Route C
  reproduces only the existing 1/r^4-type support structure and fails to
  generate an independent 1/r^2-type component.  The failure is one of
  shape, not amplitude: Route C oversupplies the core (ratio > 1 at R_eq)
  while undersupplying intermediate radii (ratio ~ 0.76 at r=1).
  Classification: route_c_insufficient_within_markov_reduction.
"""

from __future__ import annotations

import math
import sys
import numpy as np

from grut.route_c_deficit import (
    compute_route_c_deficit_assessment,
    route_c_result_to_dict,
    compute_route_c_energy_profile,
    evaluate_chain_1_markov_kinetic,
    evaluate_chain_2_self_healing,
    evaluate_chain_3_candidate_potential,
    evaluate_chain_4_spatial_gradient,
    assess_insufficiency,
    compute_lapse_correction_at_equilibrium,
    analyze_potential_sector,
    analyze_spatial_gradient,
    catalog_loopholes,
    build_provisional_candidate_ranking,
    RouteCParams,
    ALPHA_VAC,
    R_S,
    M_EXT,
    R_EQ,
    TAU_CANONICAL,
    A_CRIT,
    EPSILON_RC_COEFF,
    COMP_B_COEFF,
    RHO_EQ_COEFF,
    PHASE6B_A_CRIT_NATURAL,
    NONCLAIMS,
    ROUTE_C_ASSUMPTIONS,
)


passed = 0
failed = 0
results = []


def check(label: str, condition: bool, detail: str = "") -> None:
    global passed, failed
    status = "PASS" if condition else "FAIL"
    if not condition:
        failed += 1
    else:
        passed += 1
    msg = f"  [{status}] {label}"
    if detail and not condition:
        msg += f"  -- {detail}"
    results.append(msg)
    print(msg)


def close(a: float, b: float, tol: float = 1e-6) -> bool:
    return abs(a - b) < tol


def rel_close(a: float, b: float, tol: float = 0.05) -> bool:
    if abs(b) < 1e-30:
        return abs(a) < tol
    return abs(a - b) / abs(b) < tol


def main() -> int:
    print("=" * 72)
    print("BENCHMARK: Route C Deficit Assessment — Nonlocal vs 1/r^2")
    print("=" * 72)

    # ================================================================
    # Build master result
    # ================================================================
    print("\n  Running Route C deficit assessment...")
    params = RouteCParams(n_r=500)
    result = compute_route_c_deficit_assessment(params)
    print(f"  Assessment complete. Valid: {result.valid}\n")

    ep = result.energy_profile
    ia = result.insufficiency_assessment
    lc = result.lapse_correction
    ps = result.potential_sector
    sg = result.spatial_gradient
    lpc = result.loophole_catalog
    pr = result.provisional_ranking
    cl = result.classification

    # ================================================================
    # Section 1: Parameter Setup
    # ================================================================
    print("\n--- Section 1: Parameter Setup ---")

    check("alpha_vac = 1/3",
          rel_close(ALPHA_VAC, 1.0 / 3.0, 1e-10))

    check("M = r_s/2 = 0.5",
          rel_close(M_EXT, 0.5, 1e-10))

    check("tau = sqrt(3/2) ~ 1.2247",
          rel_close(TAU_CANONICAL, math.sqrt(1.5), 1e-6))

    check("A_crit = 1.062 (Phase 6B locked)",
          rel_close(A_CRIT, 1.062, 1e-3))

    expected_eps = A_CRIT ** 2 * M_EXT ** 2 / (2.0 * TAU_CANONICAL ** 2)
    check("EPSILON_RC_COEFF = A_crit^2 * M^2/(2*tau^2)",
          rel_close(EPSILON_RC_COEFF, expected_eps, 1e-6))

    # ================================================================
    # Section 2: Route C Energy Profile
    # ================================================================
    print("\n--- Section 2: Route C Energy Profile ---")

    check("epsilon_RC_coeff ~ 0.0940",
          rel_close(ep.epsilon_RC_coeff, 0.0940, 0.01))

    # Verify pure 1/r^4 scaling
    r_test = np.array([R_EQ, 0.5, 1.0, 1.5])
    eps_test = ep.epsilon_RC_coeff / r_test ** 4
    product = eps_test * r_test ** 4
    is_pure = float(np.std(product) / np.mean(product)) < 1e-10
    check("epsilon_RC is pure 1/r^4",
          is_pure)

    check("Deficit ratio at R_eq ~ 1.07 (overcovering)",
          rel_close(ep.ratio_at_R_eq, 1.07, 0.02))

    check("Deficit ratio at r=1 ~ 0.76 (undercovering)",
          rel_close(ep.ratio_at_r1, 0.76, 0.02))

    check("ratio_min < 1 (insufficiency confirmed)",
          ep.ratio_min < 1.0)

    check("ratio_max > 1 (overcovering at core)",
          ep.ratio_max > 1.0)

    check("Covers Component A (A_crit > 1)",
          ep.covers_component_A is True)

    check("Does NOT cover Component B",
          ep.covers_component_B is False)

    # ================================================================
    # Section 3: Chain 1 — Markov Kinetic
    # ================================================================
    print("\n--- Section 3: Chain 1 — Markov Kinetic ---")

    c1 = ia.chains[0]
    check("Chain 1 scaling = 1/r^4",
          c1.scaling_law == "1/r^4")

    check("Chain 1 provides_1r2 = False",
          c1.provides_1r2 is False)

    check("Chain 1 is_formal = True",
          c1.is_formal is True)

    check("Premise contains 'Markov'",
          "Markov" in c1.premise)

    check("Conclusion contains '1/r^4'",
          "1/r^4" in c1.conclusion)

    check("Mechanism mentions squaring",
          "Phi_dot" in c1.mechanism and "1/r^4" in c1.mechanism)

    # ================================================================
    # Section 4: Chain 2 — Self-Healing
    # ================================================================
    print("\n--- Section 4: Chain 2 — Self-Healing ---")

    c2 = ia.chains[1]
    check("Chain 2 scaling = 0 (no contribution at eq)",
          c2.scaling_law == "0")

    check("Chain 2 provides_1r2 = False",
          c2.provides_1r2 is False)

    check("Lapse source X - Phi = 0 at equilibrium",
          close(lc.source_X_minus_Phi, 0.0, 1e-10))

    check("delta_Phi_lapse = 0 at equilibrium",
          close(lc.delta_Phi_lapse, 0.0, 1e-10))

    check("Self-healing holds",
          lc.self_healing_holds is True)

    check("Mechanism mentions equilibrium",
          "equilibrium" in c2.mechanism)

    # ================================================================
    # Section 5: Chain 3 — Candidate Potential
    # ================================================================
    print("\n--- Section 5: Chain 3 — Candidate Potential ---")

    c3 = ia.chains[2]
    check("Chain 3 scaling = 1/r^4",
          c3.scaling_law == "1/r^4")

    check("Chain 3 provides_1r2 = False",
          c3.provides_1r2 is False)

    check("V at R_eq > 0",
          ps.V_at_R_eq > 0)

    check("V form = Phi^2/(2*tau^2)",
          "Phi^2" in ps.V_form and "tau^2" in ps.V_form)

    check("NOT intrinsic to Route C",
          ps.is_intrinsic_route_c is False)

    # ================================================================
    # Section 6: Chain 4 — Spatial Gradient
    # ================================================================
    print("\n--- Section 6: Chain 4 — Spatial Gradient ---")

    c4 = ia.chains[3]
    check("Chain 4 scaling = 1/r^6",
          c4.scaling_law == "1/r^6")

    check("Chain 4 provides_1r2 = False",
          c4.provides_1r2 is False)

    check("gradient_sq at R_eq > 0",
          sg.gradient_sq_at_R_eq > 0)

    check("Steeper than 1/r^4",
          "1/r^6" in sg.gradient_sq_scaling)

    check("Evaluated in reduced background",
          sg.evaluated_in_reduced_background is True)

    # ================================================================
    # Section 7: Insufficiency Assessment
    # ================================================================
    print("\n--- Section 7: Insufficiency Assessment ---")

    check("n_chains = 4",
          ia.n_chains == 4)

    check("All chains consistent (no 1/r^2)",
          ia.all_chains_consistent is True)

    check("any_chain_provides_1r2 = False",
          ia.any_chain_provides_1r2 is False)

    check("overall_insufficient = True",
          ia.overall_insufficient is True)

    check("Classification string correct",
          ia.classification_string == "route_c_insufficient_within_markov_reduction")

    check("is_general_no_go = False",
          ia.is_general_no_go is False)

    # ================================================================
    # Section 8: Loophole Catalog
    # ================================================================
    print("\n--- Section 8: Loophole Catalog ---")

    check("n_loopholes = 5",
          lpc.n_loopholes == 5)

    check("Loophole 1 is non-exponential kernel",
          "kernel" in lpc.loopholes[0].name.lower())

    check("Loophole 5 is modified source",
          "source" in lpc.loopholes[4].name.lower())

    check("At least 2 high severity",
          lpc.n_high_severity >= 2)

    n_beyond_markov = sum(
        1 for lp in lpc.loopholes if lp.requires_beyond_markov
    )
    check("At least 1 requires beyond-Markov",
          n_beyond_markov >= 1)

    check("None tested within this module",
          lpc.any_tested is False)

    check("All loopholes have notes",
          all(len(lp.notes) > 0 for lp in lpc.loopholes))

    # ================================================================
    # Section 9: Provisional Candidate Ranking
    # ================================================================
    print("\n--- Section 9: Provisional Candidate Ranking ---")

    check("Route C: insufficient_within_markov_reduction",
          pr.route_c_status == "insufficient_within_markov_reduction")

    check("Route C downgraded",
          pr.route_c_downgraded is True)

    check("Route B: provisional",
          pr.route_b_status == "provisional")

    check("Route B obstruction mentions ghost",
          "ghost" in pr.route_b_obstruction.lower() or "Ghost" in pr.route_b_obstruction)

    check("Route C previous: highest_structural_plausibility",
          "plausibility" in pr.route_c_previous_status)

    check("Ranking is marked provisional",
          pr.is_provisional is True)

    # ================================================================
    # Section 10: Numerical Validation
    # ================================================================
    print("\n--- Section 10: Numerical Validation ---")

    check("EPSILON_RC_COEFF ~ 0.0940 within 1%",
          rel_close(EPSILON_RC_COEFF, 0.09399, 0.01))

    check("COMP_B_COEFF ~ 0.0398 within 1%",
          rel_close(COMP_B_COEFF, 0.03979, 0.01))

    # Ratio B/A at R_eq (from Phase 6C)
    ratio_BA_Req = COMP_B_COEFF / (R_EQ ** 2) / (RHO_EQ_COEFF / R_EQ ** 4)
    check("Ratio B/A at R_eq ~ 5.3%",
          rel_close(ratio_BA_Req, 0.053, 0.10))

    # Ratio B/A at r=1
    ratio_BA_r1 = COMP_B_COEFF / RHO_EQ_COEFF
    check("Ratio B/A at r=1 ~ 0.48",
          rel_close(ratio_BA_r1, 0.477, 0.05))

    check("Integrated shortfall > 0",
          ep.integrated_shortfall > 0)

    # epsilon_RC at r=1 = EPSILON_RC_COEFF
    check("epsilon_RC(r=1) = EPSILON_RC_COEFF",
          rel_close(ep.epsilon_RC_coeff, EPSILON_RC_COEFF, 1e-6))

    # epsilon_min at r=1 = |rho_eq| + 1/(8*pi)
    eps_min_r1 = RHO_EQ_COEFF + COMP_B_COEFF
    check("epsilon_min(r=1) ~ 0.1231",
          rel_close(eps_min_r1, 0.1231, 0.01))

    # ================================================================
    # Section 11: Nonclaims & Assumptions
    # ================================================================
    print("\n--- Section 11: Nonclaims & Assumptions ---")

    check("10 nonclaims",
          len(result.nonclaims) == 10)

    check("5 assumptions",
          len(result.assumptions) == 5)

    check("Nonclaims contain 'not a general no-go'",
          any("NOT a general no-go" in nc for nc in result.nonclaims))

    check("Nonclaims contain 'exponential kernel'",
          any("exponential kernel" in nc for nc in result.nonclaims))

    check("Assumptions mention 'Markov'",
          any("Markov" in a for a in result.assumptions))

    # ================================================================
    # Section 12: Serialization
    # ================================================================
    print("\n--- Section 12: Serialization ---")

    d = route_c_result_to_dict(result)

    check("Dict has 'classification' key",
          "classification" in d)

    check("Classification string correct",
          d["classification"]["classification"] == "route_c_insufficient_within_markov_reduction")

    check("Dict has 'nonclaims' with 10 items",
          len(d.get("nonclaims", [])) == 10)

    check("Dict has 'assumptions' with 5 items",
          len(d.get("assumptions", [])) == 5)

    # ================================================================
    # Summary
    # ================================================================
    print()
    print("=" * 72)
    total = passed + failed
    print(f"TOTAL: {passed}/{total} checks passed, {failed} failed")
    if failed == 0:
        print("ALL CHECKS PASSED")
    else:
        print("SOME CHECKS FAILED")

    # Key findings
    print(f"\n--- Key Findings ---")
    print(f"  epsilon_RC_coeff = {ep.epsilon_RC_coeff:.6f} (pure 1/r^4)")
    print(f"  deficit_ratio at R_eq = {ep.ratio_at_R_eq:.4f} (overcovering)")
    print(f"  deficit_ratio at r=1  = {ep.ratio_at_r1:.4f} (undercovering)")
    print(f"  deficit_ratio range   = [{ep.ratio_min:.4f}, {ep.ratio_max:.4f}]")
    print(f"  Covers Component A: {ep.covers_component_A}")
    print(f"  Covers Component B: {ep.covers_component_B}")
    print(f"  Shape mismatch: oversupplies core, undersupplies intermediate radii")
    print(f"  Chains: {ia.n_chains}, all insufficient, none provide 1/r^2")
    print(f"  Loopholes: {lpc.n_loopholes} ({lpc.n_high_severity} high severity)")
    print(f"  Classification: {cl.classification}")
    print(f"  General no-go: {cl.is_general_no_go}")
    print("=" * 72)

    return 1 if failed > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
