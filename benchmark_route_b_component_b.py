#!/usr/bin/env python3
"""Benchmark: Route B Component B Test — Pre-Projection Doubled-Field.

~70 independent checks covering:
  1.  Parameter Setup (5)
  2.  Post-Projection Equivalence (8)
  3.  Phi_- Sector Analysis (7)
  4.  g_- Sector Analysis (5)
  5.  Dissipative Kernel Analysis (5)
  6.  Candidate Carrier Catalog (7)
  7.  Obstruction Catalog (6)
  8.  Component B Assessment (6)
  9.  Numerical Validation (7)
  10. Nonclaims & Assumptions (5)
  11. Classification & Ranking (5)
  12. Serialization (4)

KEY FINDINGS:
  Post-projection Route B is IDENTICAL to Route C (pure 1/r^4).
  Computed pre-projection sectors (Phi_-, S_diss) are pathological or
  projection-killed.  The g_- / doubled-metric sector remains uncomputed
  and is the key unresolved channel.
  Classification: route_b_post_projection_insufficient__preprojection_unresolved.
"""

from __future__ import annotations

import math
import sys
import numpy as np

from grut.route_b_component_b import (
    compute_route_b_component_b_assessment,
    route_b_result_to_dict,
    analyze_post_projection_equivalence,
    analyze_phi_minus_sector,
    analyze_g_minus_sector,
    analyze_dissipative_kernel,
    build_candidate_carrier_catalog,
    build_obstruction_catalog,
    assess_component_b_support,
    classify_route_b_component_b,
    RouteBParams,
    ALPHA_VAC,
    R_S,
    M_EXT,
    R_EQ,
    TAU_CANONICAL,
    A_CRIT,
    EPSILON_RC_COEFF,
    COMP_B_COEFF,
    RHO_EQ_COEFF,
    PHI_GOLDEN,
    NONCLAIMS,
    ROUTE_B_ASSUMPTIONS,
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
    print("BENCHMARK: Route B Component B Test — Pre-Projection Doubled-Field")
    print("=" * 72)

    # ================================================================
    # Build master result
    # ================================================================
    print("\n  Running Route B Component B assessment...")
    params = RouteBParams(n_r=500)
    result = compute_route_b_component_b_assessment(params)
    print(f"  Assessment complete. Valid: {result.valid}\n")

    pp = result.post_projection
    pm = result.phi_minus_sector
    gm = result.g_minus_sector
    dk = result.dissipative_kernel
    cc = result.carrier_catalog
    oc = result.obstruction_catalog
    asmt = result.assessment
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

    check("PHI_GOLDEN = (1+sqrt(5))/2",
          rel_close(PHI_GOLDEN, (1.0 + math.sqrt(5.0)) / 2.0, 1e-10))

    # ================================================================
    # Section 2: Post-Projection Equivalence
    # ================================================================
    print("\n--- Section 2: Post-Projection Equivalence ---")

    check("Post-proj epsilon_coeff ~ 0.0940",
          rel_close(pp.epsilon_RC_coeff, 0.0940, 0.01))

    expected_coeff = A_CRIT ** 2 * M_EXT ** 2 / (2.0 * TAU_CANONICAL ** 2)
    check("Post-proj coeff = A_crit^2 * M^2/(2*tau^2)",
          rel_close(pp.epsilon_RC_coeff, expected_coeff, 1e-6))

    check("Identical to Route C",
          pp.identical_to_route_c is True)

    check("Deficit ratio at R_eq ~ 1.07 (overcovering)",
          rel_close(pp.ratio_at_R_eq, 1.07, 0.02))

    check("Deficit ratio at r=1 ~ 0.76 (undercovering)",
          rel_close(pp.ratio_at_r1, 0.76, 0.02))

    check("Does NOT provide Component B",
          pp.provides_component_B is False)

    check("Shape mismatch description exists",
          len(pp.shape_mismatch) > 50)

    check("Has notes",
          len(pp.notes) >= 3)

    # ================================================================
    # Section 3: Phi_- Sector Analysis
    # ================================================================
    print("\n--- Section 3: Phi_- Sector Analysis ---")

    check("Simple growth rate = 1/tau",
          rel_close(pm.simple_growth_rate, 1.0 / TAU_CANONICAL, 1e-6))

    check("Full KG growth rate = phi/tau ~ 1.32",
          rel_close(pm.full_kg_growth_rate, PHI_GOLDEN / TAU_CANONICAL, 1e-4))

    check("Decay rate = 1/(phi*tau) ~ 0.50",
          rel_close(pm.full_kg_decay_rate, 1.0 / (PHI_GOLDEN * TAU_CANONICAL), 1e-4))

    check("Kinetic sign = -1 (wrong-sign)",
          pm.kinetic_sign == -1)

    check("Is ghost",
          pm.is_ghost is True)

    check("Spatial profile NOT geometric",
          pm.spatial_profile_geometric is False)

    check("Does NOT provide Component B",
          pm.provides_component_B is False)

    # ================================================================
    # Section 4: g_- Sector Analysis
    # ================================================================
    print("\n--- Section 4: g_- Sector Analysis ---")

    check("Wrong-sign Einstein-Hilbert",
          gm.wrong_sign_eh is True)

    check("Consistent truncation (g_- = 0)",
          gm.consistent_truncation is True)

    check("Energy density NOT computed",
          gm.energy_density_computed is False)

    check("Status = uncomputed_and_projection_sensitive",
          gm.status == "uncomputed_and_projection_sensitive")

    check("Is key unresolved channel",
          gm.is_key_unresolved_channel is True)

    # ================================================================
    # Section 5: Dissipative Kernel Analysis
    # ================================================================
    print("\n--- Section 5: Dissipative Kernel Analysis ---")

    check("S_diss at physical limit = 0",
          close(dk.s_diss_at_physical_limit, 0.0, 1e-15))

    check("Vanishes in physical limit",
          dk.vanishes_in_physical_limit is True)

    check("Pre-projection ghost-coupled",
          dk.pre_projection_ghost_coupled is True)

    check("Does NOT provide Component B",
          dk.provides_component_B is False)

    check("Has notes",
          len(dk.notes) >= 3)

    # ================================================================
    # Section 6: Candidate Carrier Catalog
    # ================================================================
    print("\n--- Section 6: Candidate Carrier Catalog ---")

    check("n_carriers = 5",
          cc.n_carriers == 5)

    check("n_physical = 0",
          cc.n_physical == 0)

    check("n_uncomputed = 2 (g_- energy + delta S/delta g_-)",
          cc.n_uncomputed == 2)

    check("n_projected_observable = 1",
          cc.n_projected_observable == 1)

    check("n_computed_sector = 2",
          cc.n_computed_sector == 2)

    check("n_formal_variation_channel = 2",
          cc.n_formal_variation_channel == 2)

    check("Carrier 4 is uncomputed_and_projection_sensitive",
          cc.carriers[3].projection_status == "projection_sensitive")

    # ================================================================
    # Section 7: Obstruction Catalog
    # ================================================================
    print("\n--- Section 7: Obstruction Catalog ---")

    check("n_obstructions = 5",
          oc.n_obstructions == 5)

    check("n_high_severity = 3",
          oc.n_high_severity == 3)

    check("n_medium_severity = 2",
          oc.n_medium_severity == 2)

    check("Obstruction 1 is structural",
          oc.obstructions[0].obstruction_type == "structural")

    check("Obstruction 5 is gap (uncomputed sector)",
          oc.obstructions[4].obstruction_type == "gap")

    check("All obstructions have descriptions",
          all(len(o.description) > 20 for o in oc.obstructions))

    # ================================================================
    # Section 8: Component B Assessment
    # ================================================================
    print("\n--- Section 8: Component B Assessment ---")

    check("Post-projection NOT sufficient",
          asmt.post_projection_sufficient is False)

    check("Computed pre-projection NOT sufficient",
          asmt.computed_preprojection_sufficient is False)

    check("Uncomputed sector remains",
          asmt.uncomputed_sector_remains is True)

    check("Uncomputed sector = g_minus_doubled_metric",
          asmt.uncomputed_sector_name == "g_minus_doubled_metric")

    check("NOT a general no-go",
          asmt.is_general_no_go is False)

    check("Classification string correct",
          asmt.classification_string ==
          "route_b_post_projection_insufficient__preprojection_unresolved")

    # ================================================================
    # Section 9: Numerical Validation
    # ================================================================
    print("\n--- Section 9: Numerical Validation ---")

    check("EPSILON_RC_COEFF ~ 0.0940 within 1%",
          rel_close(EPSILON_RC_COEFF, 0.09399, 0.01))

    check("COMP_B_COEFF ~ 0.0398 within 1%",
          rel_close(COMP_B_COEFF, 0.03979, 0.01))

    # Phi_- growth rates
    check("Simple growth rate ~ 0.8165",
          rel_close(pm.simple_growth_rate, 0.8165, 0.01))

    check("Full KG growth rate ~ 1.3211",
          rel_close(pm.full_kg_growth_rate, 1.3211, 0.01))

    check("Decay rate ~ 0.5049",
          rel_close(pm.full_kg_decay_rate, 0.5049, 0.01))

    # Post-projection deficit ratios match Route C exactly
    check("Post-proj ratio at R_eq matches Route C (1.071)",
          rel_close(pp.ratio_at_R_eq, 1.071, 0.01))

    check("Post-proj ratio at r=1 matches Route C (0.763)",
          rel_close(pp.ratio_at_r1, 0.763, 0.01))

    # ================================================================
    # Section 10: Nonclaims & Assumptions
    # ================================================================
    print("\n--- Section 10: Nonclaims & Assumptions ---")

    check("10 nonclaims",
          len(result.nonclaims) == 10)

    check("6 assumptions",
          len(result.assumptions) == 6)

    check("Nonclaims mention g_- unresolved",
          any("g_- sector" in nc for nc in result.nonclaims))

    check("Nonclaims mention CTP boundary",
          any("CTP boundary" in nc for nc in result.nonclaims))

    check("Assumptions mention physical-limit projection",
          any("physical-limit projection" in a or "physical limit" in a
              for a in result.assumptions))

    # ================================================================
    # Section 11: Classification & Ranking
    # ================================================================
    print("\n--- Section 11: Classification & Ranking ---")

    check("Classification string correct",
          cl.classification ==
          "route_b_post_projection_insufficient__preprojection_unresolved")

    check("Post-projection status = insufficient",
          cl.post_projection_status == "insufficient")

    check("g_minus status = unresolved",
          cl.g_minus_status == "unresolved")

    check("Is provisional",
          cl.is_provisional is True)

    check("NOT a general no-go",
          cl.is_general_no_go is False)

    # ================================================================
    # Section 12: Serialization
    # ================================================================
    print("\n--- Section 12: Serialization ---")

    d = route_b_result_to_dict(result)

    check("Dict has 'classification' key",
          "classification" in d)

    check("Classification string in dict",
          d["classification"]["classification"] ==
          "route_b_post_projection_insufficient__preprojection_unresolved")

    check("Dict has 'nonclaims' with 10 items",
          len(d.get("nonclaims", [])) == 10)

    check("Dict has 'assumptions' with 6 items",
          len(d.get("assumptions", [])) == 6)

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
    print(f"  Post-proj epsilon_coeff = {pp.epsilon_RC_coeff:.6f} (identical to Route C)")
    print(f"  deficit_ratio at R_eq = {pp.ratio_at_R_eq:.4f} (overcovering)")
    print(f"  deficit_ratio at r=1  = {pp.ratio_at_r1:.4f} (undercovering)")
    print(f"  Phi_- growth (simple) = {pm.simple_growth_rate:.6f} (1/tau)")
    print(f"  Phi_- growth (full)   = {pm.full_kg_growth_rate:.6f} (phi/tau)")
    print(f"  S_diss at phys limit  = {dk.s_diss_at_physical_limit} (exact 0)")
    print(f"  g_- computed:         {gm.energy_density_computed}")
    print(f"  g_- status:           {gm.status}")
    print(f"  Carriers: {cc.n_carriers} total, {cc.n_physical} physical, {cc.n_uncomputed} uncomputed")
    print(f"  General no-go:        {asmt.is_general_no_go}")
    print(f"  Classification:       {cl.classification}")
    print("=" * 72)

    return 1 if failed > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
