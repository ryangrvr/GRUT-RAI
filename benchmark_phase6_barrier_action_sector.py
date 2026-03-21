#!/usr/bin/env python3
"""Benchmark: Phase VI — Covariant Barrier Action Sector.

~60 independent checks covering:
  1.  Admissibility (5)
  2.  Route A (3)
  3.  Route B (3)
  4.  Route C (3)
  5.  Route D (3)
  6.  Route Comparison (5)
  7.  Source Degeneracy (8)
  8.  T^Phi Underdetermination (4)
  9.  T^Phi Constraints (4)
  10. Missing Input (5)
  11. Status Ladder (5)
  12. Serialization (4)
  13. Nonclaims (5)
"""

from __future__ import annotations

import json
import sys

from grut.barrier_action_sector import (
    compute_barrier_action_analysis,
    barrier_action_result_to_dict,
    ALPHA_VAC,
    BETA_Q,
    N_ADMISSIBILITY_CONDITIONS,
    ROUTE_A,
    ROUTE_B,
    ROUTE_C,
    ROUTE_D,
    TPHI_STATUS_PHASE_V,
    TPHI_STATUS_PHASE_VI,
    LEVEL_EXACT,
    LEVEL_CONSTITUTIVE_DERIVED,
    LEVEL_CONSTITUTIVE_LAPSE_PROMOTION_OBSTRUCTED,
    SCOPE_STATEMENT,
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


def main() -> int:
    print("=" * 72)
    print("BENCHMARK: Phase VI — Covariant Barrier Action Sector")
    print("=" * 72)

    # Build master result
    r = compute_barrier_action_analysis()
    adm = r.admissibility
    rA = r.route_A
    rB = r.route_B
    rC = r.route_C
    rD = r.route_D
    rc = r.route_comparison
    sd = r.source_degeneracy
    tu = r.tphi_underdetermination
    tc = r.tphi_constraints
    mm = r.minimal_missing
    sl = r.status_ladder
    p5 = r.phase5_reconfirmation

    # ----------------------------------------------------------------
    # 1. Admissibility (5 checks)
    # ----------------------------------------------------------------
    print("\n--- 1. Admissibility ---")
    check("6 conditions", adm.n_conditions == 6)
    check("all have labels",
          all(len(c.label) > 0 for c in adm.conditions))
    check("all have descriptions",
          all(len(c.description) > 10 for c in adm.conditions))
    check("includes covariance",
          any(c.label == "general_covariance" for c in adm.conditions))
    check("includes conservation",
          any(c.label == "combined_conservation" for c in adm.conditions))

    # ----------------------------------------------------------------
    # 2. Route A (3 checks)
    # ----------------------------------------------------------------
    print("\n--- 2. Route A ---")
    check("action-based", rA.action_based)
    check("constitutive limit approximate (not exact)",
          rA.reproduces_constitutive_limit and not rA.constitutive_limit_exact)
    check("requires extra postulate", rA.requires_extra_postulate)

    # ----------------------------------------------------------------
    # 3. Route B (3 checks)
    # ----------------------------------------------------------------
    print("\n--- 3. Route B ---")
    check("action-based", rB.action_based)
    check("constitutive limit exact", rB.constitutive_limit_exact)
    check("gravity coupling NOT resolved",
          not rB.gravity_coupling_resolved)

    # ----------------------------------------------------------------
    # 4. Route C (3 checks)
    # ----------------------------------------------------------------
    print("\n--- 4. Route C ---")
    check("action-based", rC.action_based)
    check("covariant", rC.covariant)
    check("T_phi derivable", rC.T_phi_derivable)

    # ----------------------------------------------------------------
    # 5. Route D (3 checks)
    # ----------------------------------------------------------------
    print("\n--- 5. Route D ---")
    check("NOT action-based", not rD.action_based)
    check("T_phi NOT derivable", not rD.T_phi_derivable)
    check("notes mention non-action",
          any("non-action" in n for n in rD.notes))

    # ----------------------------------------------------------------
    # 6. Route Comparison (5 checks)
    # ----------------------------------------------------------------
    print("\n--- 6. Route Comparison ---")
    check("4 routes", rc.n_routes == 4)
    check("none fully determined",
          rc.any_fully_determined is False)
    check("best candidate = route B",
          rc.best_action_candidate == ROUTE_B)
    check("all action routes require extra",
          rc.all_action_routes_require_extra)
    check("limitations nonempty",
          len(rc.best_candidate_limitations) > 20)

    # ----------------------------------------------------------------
    # 7. Source Degeneracy (8 checks)
    # ----------------------------------------------------------------
    print("\n--- 7. Source Degeneracy Theorem ---")
    check("source = 0 at equilibrium",
          abs(sd.source_at_eq) < 1e-15)
    check("source vanishes", sd.source_vanishes)
    check("self-healing input", sd.self_healing_input)
    check("ODE reduces to trivial",
          sd.equilibrium_ode_reduces_to_trivial)
    check("no dynamical discrimination",
          sd.no_dynamical_discrimination)
    check("6 proof steps", len(sd.proof_steps) == 6)
    check("theorem status = proven",
          sd.theorem_status == "proven")
    check("does NOT claim identical stress-energy",
          sd.does_NOT_claim_identical_stress_energy)

    # ----------------------------------------------------------------
    # 8. T^Phi Underdetermination (4 checks)
    # ----------------------------------------------------------------
    print("\n--- 8. T^Phi Underdetermination ---")
    check("Level A supports Level B", tu.level_A_supports)
    check("Level A does NOT prove Level B",
          tu.level_A_proves_level_B is False)
    check("additional inputs >= 3",
          len(tu.additional_inputs_needed) >= 3)
    check("independent reasons >= 2",
          len(tu.independent_structural_reasons) >= 2)

    # ----------------------------------------------------------------
    # 9. T^Phi Constraints (4 checks)
    # ----------------------------------------------------------------
    print("\n--- 9. T^Phi Constraints ---")
    check("combined conservation", tc.combined_conservation)
    check("spherical symmetry", tc.spherical_symmetry)
    check("3 independent components",
          tc.max_independent_components == 3)
    check("equilibrium energy is matching condition",
          tc.equilibrium_energy_is_matching_condition)

    # ----------------------------------------------------------------
    # 10. Missing Input (5 checks)
    # ----------------------------------------------------------------
    print("\n--- 10. Missing Input ---")
    check("4 candidates", mm.n_candidates == 4)
    check("from existing GRUT = False",
          mm.from_existing_grut is False)
    check("any one may reduce degeneracy",
          mm.any_one_may_reduce_degeneracy)
    check("sufficiency not guaranteed generically",
          mm.sufficiency_not_guaranteed_generically)
    check("full T^Phi likely needs multiple",
          mm.full_tphi_likely_needs_multiple)

    # ----------------------------------------------------------------
    # 11. Status Ladder (5 checks)
    # ----------------------------------------------------------------
    print("\n--- 11. Status Ladder ---")
    check("L1 unchanged", not sl.level_1_changed)
    check("L2 unchanged", not sl.level_2_changed)
    check("L3 unchanged", not sl.level_3_changed)
    check("T^Phi sharpened", sl.tphi_sharpened)
    check("no level weakened", sl.no_level_weakened)

    # ----------------------------------------------------------------
    # 12. Serialization (4 checks)
    # ----------------------------------------------------------------
    print("\n--- 12. Serialization ---")
    d = barrier_action_result_to_dict(r)
    check("dict is dict", isinstance(d, dict))
    check("dict valid", d["valid"] is True)
    s = json.dumps(d)
    d2 = json.loads(s)
    check("JSON roundtrip", d2["valid"] is True)
    check("scope in dict",
          d["source_degeneracy"]["scope_statement"] == SCOPE_STATEMENT)

    # ----------------------------------------------------------------
    # 13. Nonclaims (5 checks)
    # ----------------------------------------------------------------
    print("\n--- 13. Nonclaims ---")
    nc = r.nonclaims
    check("at least 12 nonclaims", len(nc) >= 12)
    check("first nonclaim is guardrail",
          "does NOT derive" in nc[0])
    check("mentions stress-energy caveat",
          any("does NOT claim" in n and "stress-energy" in n for n in nc))
    check("mentions self-healing preserved",
          any("self-healing" in n.lower() for n in nc))
    check("mentions no observational predictions changed",
          any("No observational" in n for n in nc))

    # ----------------------------------------------------------------
    # STATUS REPORT
    # ----------------------------------------------------------------
    print("\n" + "=" * 72)
    print("STATUS REPORT")
    print("=" * 72)
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")
    print(f"  Total:  {passed + failed}")
    print()
    print("  Scope: " + SCOPE_STATEMENT)
    print()
    if failed == 0:
        print("  BENCHMARK: CLEAN")
    else:
        print("  BENCHMARK: FAILED")
        print()
        for line in results:
            if "[FAIL]" in line:
                print(f"    {line.strip()}")
    print("=" * 72)

    return 1 if failed > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
