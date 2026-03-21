#!/usr/bin/env python3
"""Benchmark: Route B g_- Energy Density — CTP Antisymmetry Analysis.

~56 independent checks covering:
  1.  Setup & Assumptions (5)
  2.  Energy Definition Choice (4)
  3.  CTP Antisymmetry Derivation (7)
  4.  Quadratic Action Structure (6)
  5.  Energy Density — 4 Definitions (6)
  6.  Mixed Channel Residue (5)
  7.  Component B Compatibility (5)
  8.  Projection Sensitivity (4)
  9.  Physical Admissibility (4)
  10. Final Classification (5)
  11. Nonclaims & Serialization (5)

KEY FINDINGS:
  The standalone diagonal quadratic g_- action is ABSENT by CTP antisymmetry.
  Four energy definitions all give null for the standalone diagonal sector.
  The mixed g_+ * g_- cross-coupling survives and remains the sole
  unresolved Route B residue.
  Classification: gminus_diagonal_quadratic_energy_absent__mixed_channel_unresolved.
"""

from __future__ import annotations

import math
import sys

from grut.route_b_gminus_energy import (
    compute_route_b_gminus_energy_assessment,
    route_b_gminus_result_to_dict,
    derive_ctp_antisymmetry,
    analyze_quadratic_gminus_action,
    evaluate_energy_definitions,
    analyze_mixed_channel_residue,
    assess_component_b_compatibility,
    assess_projection_sensitivity,
    assess_physical_admissibility,
    classify_gminus_energy,
    RouteBGMinusParams,
    ALPHA_VAC,
    R_S,
    M_EXT,
    R_EQ,
    TAU_CANONICAL,
    A_CRIT,
    PHI_GOLDEN,
    CTP_ANTISYMMETRY_ORDER,
    NONCLAIMS,
    GMINUS_ASSUMPTIONS,
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
    print("BENCHMARK: Route B g_- Energy Density — CTP Antisymmetry Analysis")
    print("=" * 72)

    # ================================================================
    # Build master result
    # ================================================================
    print("\n  Running Route B g_- energy density assessment...")
    params = RouteBGMinusParams(n_r=500)
    result = compute_route_b_gminus_energy_assessment(params)
    print(f"  Assessment complete. Valid: {result.valid}\n")

    ctp = result.ctp_antisymmetry
    qa = result.quadratic_action
    ed = result.energy_density
    mc = result.mixed_channel
    co = result.compatibility
    pr = result.projection
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

    check("CTP_ANTISYMMETRY_ORDER = 2",
          CTP_ANTISYMMETRY_ORDER == 2)

    # ================================================================
    # Section 2: Energy Definition Choice
    # ================================================================
    print("\n--- Section 2: Energy Definition Choice ---")

    edef = result.energy_definition

    check("4 definitions tested",
          edef.n_definitions == 4)

    check("All require quadratic action",
          edef.all_require_quadratic_action is True)

    check("Scope is standalone diagonal sector only",
          edef.scope == "standalone_diagonal_sector_only")

    check("Has notes",
          len(edef.notes) >= 2)

    # ================================================================
    # Section 3: CTP Antisymmetry Derivation
    # ================================================================
    print("\n--- Section 3: CTP Antisymmetry Derivation ---")

    check("Even orders killed include 0, 2, 4",
          0 in ctp.even_orders_killed and 2 in ctp.even_orders_killed
          and 4 in ctp.even_orders_killed)

    check("Odd orders survive include 1, 3",
          1 in ctp.odd_orders_survive and 3 in ctp.odd_orders_survive)

    check("Diagonal quadratic coefficient = 0 (exact)",
          ctp.diagonal_quadratic_coefficient == 0.0)

    check("Copy 1 quadratic coefficient = +1/8",
          close(ctp.copy_1_quadratic_coefficient, 1.0 / 8.0, 1e-15))

    check("Copy 2 quadratic coefficient = +1/8",
          close(ctp.copy_2_quadratic_coefficient, 1.0 / 8.0, 1e-15))

    check("Cancellation is exact",
          ctp.cancellation_exact is True)

    check("Numerical verification passed",
          ctp.numerical_verification_passed is True)

    # ================================================================
    # Section 4: Quadratic Action Structure
    # ================================================================
    print("\n--- Section 4: Quadratic Action Structure ---")

    check("Diagonal quadratic action = 0",
          qa.diagonal_quadratic_action_zero is True)

    check("Cross-coupling exists",
          qa.cross_coupling_exists is True)

    check("Cross-coupling vanishes in physical limit",
          qa.cross_coupling_vanishes_in_physical_limit is True)

    check("Cross-coupling is linear in g_-",
          qa.cross_coupling_linear_in_gminus is True)

    check("Net diagonal sign = 0 (absent, not wrong-sign)",
          qa.net_diagonal_sign == 0)

    check("Upgrade from wrong-sign to absent",
          qa.upgrade_from_wrong_sign_to_absent is True)

    # ================================================================
    # Section 5: Energy Density — 4 Definitions
    # ================================================================
    print("\n--- Section 5: Energy Density — 4 Definitions (Standalone Diagonal) ---")

    check("Quadratic EH: zero",
          ed.quadratic_eh_result == "zero")

    check("Canonical Hamiltonian: zero",
          ed.canonical_hamiltonian_result == "zero")

    check("Isaacson: zero",
          ed.isaacson_result == "zero")

    check("Perturbation theory: not applicable",
          ed.perturbation_theory_result == "not_applicable")

    check("No definitions giving nonzero",
          ed.n_definitions_giving_nonzero == 0)

    check("Consensus: energy structurally absent",
          ed.standalone_diagonal_consensus == "energy_structurally_absent")

    # ================================================================
    # Section 6: Mixed Channel Residue
    # ================================================================
    print("\n--- Section 6: Mixed Channel Residue ---")

    check("Cross-coupling exists",
          mc.cross_coupling_exists is True)

    check("Linear in g_-",
          mc.linear_in_gminus is True)

    check("Vanishes in physical limit",
          mc.vanishes_in_physical_limit is True)

    check("Is remaining Route B residue",
          mc.is_remaining_route_b_residue is True)

    check("Effective energy not computed",
          mc.effective_energy_computed is False)

    # ================================================================
    # Section 7: Component B Compatibility
    # ================================================================
    print("\n--- Section 7: Component B Compatibility ---")

    check("Standalone diagonal NOT compatible",
          co.standalone_diagonal_compatible is False)

    check("Mixed channel compatible = undetermined",
          co.mixed_channel_compatible == "undetermined")

    check("Computed compatible = False",
          co.computed_compatible is False)

    check("Overall status = unresolved_but_narrowed",
          co.overall_status == "unresolved_but_narrowed")

    check("Has notes",
          len(co.notes) >= 3)

    # ================================================================
    # Section 8: Projection Sensitivity
    # ================================================================
    print("\n--- Section 8: Projection Sensitivity ---")

    check("Standalone diagonal projection = moot",
          pr.standalone_diagonal_projection == "moot")

    check("Mixed channel projection = pre_projection_only",
          pr.mixed_channel_projection == "pre_projection_only")

    check("Mixed boundary sensitive = undetermined",
          pr.mixed_channel_boundary_sensitive == "undetermined")

    check("Has notes",
          len(pr.notes) >= 3)

    # ================================================================
    # Section 9: Physical Admissibility
    # ================================================================
    print("\n--- Section 9: Physical Admissibility ---")

    check("Standalone diagonal admissible = not_applicable",
          ad.standalone_diagonal_admissible == "not_applicable")

    check("Mixed channel admissible = undetermined",
          ad.mixed_channel_admissible == "undetermined")

    check("Energy exists = False (standalone diagonal)",
          ad.energy_exists is False)

    check("Has notes",
          len(ad.notes) >= 3)

    # ================================================================
    # Section 10: Final Classification
    # ================================================================
    print("\n--- Section 10: Final Classification ---")

    check("Classification correct",
          cl.classification ==
          "gminus_diagonal_quadratic_energy_absent__mixed_channel_unresolved")

    check("is_full_route_b_no_go = False",
          cl.is_full_route_b_no_go is False)

    check("standalone_diagonal_closed = True",
          cl.standalone_diagonal_closed is True)

    check("mixed_channel_unresolved = True",
          cl.mixed_channel_unresolved is True)

    check("residue_reduced = True",
          cl.residue_reduced is True)

    # ================================================================
    # Section 11: Nonclaims & Serialization
    # ================================================================
    print("\n--- Section 11: Nonclaims & Serialization ---")

    check("10 nonclaims",
          len(result.nonclaims) == 10)

    check("8 assumptions",
          len(result.assumptions) == 8)

    check("Nonclaims mention mixed g_+ * g_-",
          any("mixed g_+ * g_-" in nc for nc in result.nonclaims))

    d = route_b_gminus_result_to_dict(result)

    check("Dict has 'classification' key",
          "classification" in d)

    check("Dict classification string correct",
          d["classification"]["classification"] ==
          "gminus_diagonal_quadratic_energy_absent__mixed_channel_unresolved")

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
    print(f"  Diagonal quadratic coefficient = {ctp.diagonal_quadratic_coefficient}")
    print(f"  (+1/8) - (1/8) = {ctp.copy_1_quadratic_coefficient - ctp.copy_2_quadratic_coefficient}")
    print(f"  CTP cancellation exact: {ctp.cancellation_exact}")
    print(f"  Numerical verification: {ctp.numerical_verification_passed} "
          f"(residual {ctp.numerical_verification_max_residual:.2e})")
    print(f"  Energy definitions tested: {ed.n_definitions_tested}")
    print(f"  Definitions giving nonzero: {ed.n_definitions_giving_nonzero}")
    print(f"  Standalone diagonal consensus: {ed.standalone_diagonal_consensus}")
    print(f"  Mixed channel exists: {mc.cross_coupling_exists}")
    print(f"  Mixed channel residue: {mc.is_remaining_route_b_residue}")
    print(f"  Overall status: {co.overall_status}")
    print(f"  is_full_route_b_no_go: {cl.is_full_route_b_no_go}")
    print(f"  standalone_diagonal_closed: {cl.standalone_diagonal_closed}")
    print(f"  mixed_channel_unresolved: {cl.mixed_channel_unresolved}")
    print(f"  Classification: {cl.classification}")
    print("=" * 72)

    return 1 if failed > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
