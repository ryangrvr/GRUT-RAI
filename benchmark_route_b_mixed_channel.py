#!/usr/bin/env python3
"""Benchmark: Mixed g_+ * g_- Cross-Coupling Channel Analysis.

~55 independent checks covering:
  1.  Setup & Assumptions (5)
  2.  Mixed Channel Definition (5)
  3.  Surviving Quadratic Structure (7)
  4.  Induced Source / Source Chain (7)
  5.  Shape / Scaling Compatibility (7)
  6.  Projection Sensitivity (5)
  7.  Physical Admissibility (6)
  8.  Final Classification (7)
  9.  Nonclaims & Serialization (6)

KEY FINDINGS:
  The mixed g_+ * g_- cross-coupling channel is insufficient for Component B
  within the tested perturbative Galley CTP framework.  Four pathologies
  (IC-dependent, ghost-sourced, CTP-killed, projection-killed) jointly
  disqualify it.  All tested classical Route B channels are now classified.
  Classification: mixed_channel_insufficient_within_tested_galley_framework.
"""

from __future__ import annotations

import math
import sys

from grut.route_b_mixed_channel import (
    compute_route_b_mixed_channel_assessment,
    route_b_mixed_result_to_dict,
    define_mixed_channel,
    derive_mixed_quadratic_structure,
    analyze_induced_source,
    assess_shape_compatibility,
    assess_mixed_projection_sensitivity,
    assess_mixed_physical_admissibility,
    classify_mixed_channel,
    make_radial_grid,
    RouteBMixedParams,
    ALPHA_VAC,
    R_S,
    M_EXT,
    R_EQ,
    TAU_CANONICAL,
    A_CRIT,
    PHI_GOLDEN,
    CTP_ANTISYMMETRY_ORDER,
    N_IC_PROFILES,
    COMPONENT_B_SCALING,
    NONCLAIMS,
    MIXED_ASSUMPTIONS,
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
    print("BENCHMARK: Mixed g_+ * g_- Cross-Coupling Channel Analysis")
    print("=" * 72)

    # ================================================================
    # Build master result
    # ================================================================
    print("\n  Running mixed channel assessment...")
    params = RouteBMixedParams(n_r=500)
    result = compute_route_b_mixed_channel_assessment(params)
    print(f"  Assessment complete. Valid: {result.valid}\n")

    defn = result.definition
    qs = result.quadratic_structure
    src = result.induced_source
    shp = result.shape
    proj = result.projection
    ad = result.admissibility
    cl = result.classification

    # ================================================================
    # Section 1: Setup & Assumptions
    # ================================================================
    print("\n--- Section 1: Setup & Assumptions ---")

    check("alpha_vac = 1/3",
          rel_close(ALPHA_VAC, 1.0 / 3.0, 1e-10))

    check("M = r_s/2 = 0.5",
          rel_close(M_EXT, 0.5, 1e-10))

    check("tau = sqrt(3/2) ~ 1.2247",
          rel_close(TAU_CANONICAL, math.sqrt(1.5), 1e-6))

    check("PHI_GOLDEN = (1+sqrt(5))/2",
          rel_close(PHI_GOLDEN, (1.0 + math.sqrt(5.0)) / 2.0, 1e-10))

    check("COMPONENT_B_SCALING = -2.0",
          COMPONENT_B_SCALING == -2.0)

    # ================================================================
    # Section 2: Mixed Channel Definition
    # ================================================================
    print("\n--- Section 2: Mixed Channel Definition ---")

    check("Object name is delta^2_S_EH(h_+, h_-)",
          defn.object_name == "delta^2_S_EH(h_+, h_-)")

    check("Is bilinear",
          defn.is_bilinear is True)

    check("Is self-adjoint",
          defn.is_self_adjoint is True)

    check("Is only surviving quadratic term",
          defn.is_only_surviving_quadratic is True)

    check("Diagonal h_-^2 absent (from CTP antisymmetry)",
          defn.diagonal_h_minus_squared_absent is True)

    # ================================================================
    # Section 3: Surviving Quadratic Structure
    # ================================================================
    print("\n--- Section 3: Surviving Quadratic Structure ---")

    check("Mixed term survives",
          qs.mixed_term_survives is True)

    check("Analytical coefficient = 2.0",
          close(qs.analytical_coefficient, 2.0, 1e-15))

    check("Numerical verification passed",
          qs.numerical_verification_passed is True)

    check("Numerical residual < 1e-4",
          qs.numerical_verification_max_residual < 1e-4,
          f"residual = {qs.numerical_verification_max_residual:.2e}")

    check("Is self-adjoint",
          qs.is_self_adjoint is True)

    check("Has notes",
          len(qs.notes) >= 5)

    check("Analytical coefficient is exactly 2",
          qs.analytical_coefficient == 2.0)

    # ================================================================
    # Section 4: Induced Source / Source Chain
    # ================================================================
    print("\n--- Section 4: Induced Source / Source Chain ---")

    check("Source chain identified",
          src.source_chain_identified is True)

    check("h_- EOM is linearized Einstein",
          src.h_minus_eom_is_linearized_einstein is True)

    check("Source is T_tilde[Phi_-]",
          src.source_is_t_tilde_phi_minus is True)

    check("T_tilde is bilinear in Phi_eq and Phi_-",
          src.t_tilde_is_bilinear_in_phi_eq_phi_minus is True)

    check("Is ghost-sourced",
          src.is_ghost_sourced is True)

    check("Is IC-dependent",
          src.is_ic_dependent is True)

    check("Profiles differ between ICs",
          src.profiles_differ is True)

    # ================================================================
    # Section 5: Shape / Scaling Compatibility
    # ================================================================
    print("\n--- Section 5: Shape / Scaling Compatibility ---")

    check("Is IC-dependent",
          shp.is_ic_dependent is True)

    check("Does NOT match Component B",
          shp.matches_component_b is False)

    check("Radial profiles differ",
          shp.radial_profiles_differ is True)

    check("Profile 1 exponent != -2 (not Component B)",
          abs(shp.profile_1_best_fit_exponent - COMPONENT_B_SCALING) > 0.5,
          f"exponent = {shp.profile_1_best_fit_exponent:.2f}")

    check("Profile 2 exponent != -2 (not Component B)",
          abs(shp.profile_2_best_fit_exponent - COMPONENT_B_SCALING) > 0.5,
          f"exponent = {shp.profile_2_best_fit_exponent:.2f}")

    check("Profile exponents differ from each other",
          abs(shp.profile_1_best_fit_exponent - shp.profile_2_best_fit_exponent) > 0.3,
          f"diff = {abs(shp.profile_1_best_fit_exponent - shp.profile_2_best_fit_exponent):.2f}")

    check("Has structural argument",
          len(shp.structural_argument) > 50)

    # ================================================================
    # Section 6: Projection Sensitivity
    # ================================================================
    print("\n--- Section 6: Projection Sensitivity ---")

    check("Does NOT survive physical limit",
          proj.survives_physical_limit is False)

    check("Does NOT survive CTP boundary",
          proj.survives_ctp_boundary is False)

    check("Is pre-projection only",
          proj.is_pre_projection_only is True)

    check("Has physical limit argument",
          len(proj.physical_limit_argument) > 20)

    check("Has CTP boundary argument",
          len(proj.ctp_boundary_argument) > 20)

    # ================================================================
    # Section 7: Physical Admissibility
    # ================================================================
    print("\n--- Section 7: Physical Admissibility ---")

    check("NOT physically admissible",
          ad.is_physically_admissible is False)

    check("4 pathology channels",
          ad.n_pathology_channels == 4)

    check("Jointly disqualifying",
          ad.jointly_disqualifying is True)

    check("Pathology: IC-dependent",
          ad.pathology_ic_dependent is True)

    check("Pathology: ghost-sourced",
          ad.pathology_ghost_sourced is True)

    check("Pathology: CTP-killed AND projection-killed",
          ad.pathology_ctp_killed is True and ad.pathology_projection_killed is True)

    # ================================================================
    # Section 8: Final Classification
    # ================================================================
    print("\n--- Section 8: Final Classification ---")

    check("Classification correct",
          cl.classification ==
          "mixed_channel_insufficient_within_tested_galley_framework")

    check("Route B classical channels closed",
          cl.route_b_classical_channels_closed is True)

    check("All tested channels classified",
          cl.all_tested_channels_classified is True)

    check("Framework scope = perturbative_galley_ctp_framework",
          cl.framework_scope == "perturbative_galley_ctp_framework")

    check("Post-projection status = insufficient",
          cl.post_projection_status == "insufficient")

    check("g_- diagonal status = absent",
          cl.gminus_diagonal_status == "absent")

    check("g_- mixed status = insufficient_within_tested_framework",
          cl.gminus_mixed_status == "insufficient_within_tested_framework")

    # ================================================================
    # Section 9: Nonclaims & Serialization
    # ================================================================
    print("\n--- Section 9: Nonclaims & Serialization ---")

    check("10 nonclaims",
          len(result.nonclaims) == 10)

    check("10 assumptions",
          len(result.assumptions) == 10)

    check("Nonclaims mention 'tested classical Route B residue'",
          any("tested classical Route B residue" in nc for nc in result.nonclaims))

    check("Nonclaims mention 'EOM-level argument'",
          any("EOM-level argument" in nc for nc in result.nonclaims))

    d = route_b_mixed_result_to_dict(result)

    check("Dict has 'classification' key",
          "classification" in d)

    check("Dict classification string correct",
          d["classification"]["classification"] ==
          "mixed_channel_insufficient_within_tested_galley_framework")

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
    print(f"  Mixed term survives: {qs.mixed_term_survives}")
    print(f"  Analytical coefficient: {qs.analytical_coefficient}")
    print(f"  Numerical verification: {qs.numerical_verification_passed} "
          f"(residual {qs.numerical_verification_max_residual:.2e})")
    print(f"  Profiles differ: {src.profiles_differ}")
    print(f"  IC-dependent: {src.is_ic_dependent}")
    print(f"  Ghost-sourced: {src.is_ghost_sourced}")
    print(f"  Profile 1 scaling (large r): {src.profile_1_dominant_scaling_large_r:.2f}")
    print(f"  Profile 2 scaling (large r): {src.profile_2_dominant_scaling_large_r:.2f}")
    print(f"  Profile 1 best-fit exponent: {shp.profile_1_best_fit_exponent:.2f}")
    print(f"  Profile 2 best-fit exponent: {shp.profile_2_best_fit_exponent:.2f}")
    print(f"  Matches Component B: {shp.matches_component_b}")
    print(f"  Survives physical limit: {proj.survives_physical_limit}")
    print(f"  Survives CTP boundary: {proj.survives_ctp_boundary}")
    print(f"  Physically admissible: {ad.is_physically_admissible}")
    print(f"  Pathology channels: {ad.n_pathology_channels}")
    print(f"  Jointly disqualifying: {ad.jointly_disqualifying}")
    print(f"  Route B channels closed: {cl.route_b_classical_channels_closed}")
    print(f"  Classification: {cl.classification}")
    print("=" * 72)

    return 1 if failed > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
