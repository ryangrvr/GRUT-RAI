#!/usr/bin/env python3
"""Benchmark: Phase VII — Testing EOS / Potential Closure from beta_Q.

~65 independent checks covering:
  1.  EOS Admissibility (5)
  2.  Conditional Sequence (5)
  3.  Anisotropy (5)
  4.  Candidate Potential (5)
  5.  Degeneracy Reduction (6)
  6.  NEC Compatibility (5)
  7.  Lapse Impact (4)
  8.  Phase VI Reconfirmation (4)
  9.  Status Ladder (5)
  10. Master Result (5)
  11. Serialization (4)
  12. Nonclaims (5)
  13. Primary Questions Q1-Q7 (7)
"""

from __future__ import annotations

import json
import sys

from grut.barrier_eos_potential import (
    compute_eos_potential_analysis,
    eos_potential_result_to_dict,
    ALPHA_VAC,
    BETA_Q,
    ROUTE_A,
    ROUTE_B,
    ROUTE_C,
    TPHI_STATUS_PHASE_VI,
    TPHI_STATUS_PHASE_VII,
    SCOPE_STATEMENT,
    ClosureClassification,
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
    print("BENCHMARK: Phase VII — Testing EOS / Potential Closure from beta_Q")
    print("=" * 72)

    # Build master result
    r = compute_eos_potential_analysis()
    ea = r.eos_admissibility
    seq = r.conditional_sequence
    aa = r.anisotropy
    cp = r.candidate_potential
    dr = r.degeneracy_assessment
    nc = r.nec_compatibility
    la = r.lapse_impact
    p6 = r.phase6_reconfirmation
    sl = r.status_ladder

    # ----------------------------------------------------------------
    # 1. EOS Admissibility (5 checks)
    # ----------------------------------------------------------------
    print("\n--- 1. EOS Admissibility ---")
    check("beta_Q NOT eos exponent", ea.beta_Q_is_eos_exponent is False)
    check("beta_Q IS stiffness exponent", ea.beta_Q_is_stiffness_exponent)
    check("conditional mapping exists", ea.conditional_mapping_exists)
    check("omega_0^2 exact", ea.omega_0_sq_exact)
    check("requires isotropy", ea.requires_isotropy)

    # ----------------------------------------------------------------
    # 2. Conditional Sequence (5 checks)
    # ----------------------------------------------------------------
    print("\n--- 2. Conditional Sequence ---")
    check("5 steps", seq.n_steps == 5)
    check("step 1 exact", seq.steps[0].is_exact)
    check("step 2 conditional", not seq.steps[1].is_exact)
    check("not fully exact", seq.sequence_is_fully_exact is False)
    check("has terminal anisotropy block",
          seq.has_terminal_anisotropy_block)

    # ----------------------------------------------------------------
    # 3. Anisotropy (5 checks)
    # ----------------------------------------------------------------
    print("\n--- 3. Anisotropy ---")
    check("cosmo isotropic", aa.cosmo_sector_isotropic)
    check("collapse anisotropic", aa.collapse_sector_anisotropic)
    check("single w insufficient for collapse",
          aa.single_w_insufficient_for_collapse)
    check("collapse needs wr and wperp",
          aa.collapse_needs_wr_and_wperp)
    check("cosmo single w sufficient",
          aa.cosmo_single_w_sufficient)

    # ----------------------------------------------------------------
    # 4. Candidate Potential (5 checks)
    # ----------------------------------------------------------------
    print("\n--- 4. Candidate Potential ---")
    check("Phi^2 form", "Phi^2" in cp.form)
    check("NOT unique", cp.is_unique is False)
    check("Route A specific", cp.route == ROUTE_A)
    check("free 2 -> 1", cp.n_free_before == 2 and cp.n_free_after == 1)
    check("w at equilibrium = -1",
          abs(cp.w_at_equilibrium - (-1.0)) < 1e-15)

    # ----------------------------------------------------------------
    # 5. Degeneracy Reduction (6 checks)
    # ----------------------------------------------------------------
    print("\n--- 5. Degeneracy Reduction ---")
    check("reduces Route A", dr.reduces_route_a)
    check("NOT reduces Route B", dr.reduces_route_b is False)
    check("NOT reduces Route C", dr.reduces_route_c is False)
    check("NOT fully breaks", dr.fully_breaks_degeneracy is False)
    check("source degeneracy NOT broken",
          dr.source_degeneracy_broken is False)
    check("classification = partially_closing",
          dr.closure_classification
          == ClosureClassification.PARTIALLY_CLOSING.value)

    # ----------------------------------------------------------------
    # 6. NEC Compatibility (5 checks)
    # ----------------------------------------------------------------
    print("\n--- 6. NEC Compatibility ---")
    check("w = -1", abs(nc.w_at_equilibrium - (-1.0)) < 1e-15)
    check("rho + p = 0",
          abs(nc.rho_plus_p_at_equilibrium) < 1e-15)
    check("NEC marginal", nc.nec_marginal_at_equilibrium)
    check("compatible (Route A isotropic scope)",
          nc.candidate_v_compatible_with_nec)
    check("no conflict", nc.no_conflict)

    # ----------------------------------------------------------------
    # 7. Lapse Impact (4 checks)
    # ----------------------------------------------------------------
    print("\n--- 7. Lapse Impact ---")
    check("no improvement", la.improves_lapse_determination is False)
    check("obstruction persists", la.obstruction_lifted is False)
    check("T^Phi still constitutive", la.tphi_still_constitutive)
    check("phase V obstruction unchanged",
          la.phase_v_obstruction_unchanged)

    # ----------------------------------------------------------------
    # 8. Phase VI Reconfirmation (4 checks)
    # ----------------------------------------------------------------
    print("\n--- 8. Phase VI Reconfirmation ---")
    check("source degeneracy preserved",
          p6.source_degeneracy_preserved)
    check("T^Phi underdetermination preserved",
          p6.tphi_underdetermination_preserved)
    check("route assessment preserved",
          p6.route_assessment_preserved)
    check("all preserved", p6.all_preserved)

    # ----------------------------------------------------------------
    # 9. Status Ladder (5 checks)
    # ----------------------------------------------------------------
    print("\n--- 9. Status Ladder ---")
    check("L1 unchanged", not sl.level_1_changed)
    check("L2 unchanged", not sl.level_2_changed)
    check("L3 unchanged", not sl.level_3_changed)
    check("T^Phi unchanged", not sl.tphi_changed)
    check("no level weakened", sl.no_level_weakened)

    # ----------------------------------------------------------------
    # 10. Master Result (5 checks)
    # ----------------------------------------------------------------
    print("\n--- 10. Master Result ---")
    check("valid", r.valid)
    check("classification = admissible_but_nonunique",
          r.closure_classification
          == ClosureClassification.ADMISSIBLE_BUT_NONUNIQUE.value)
    check("all components present",
          all([
              r.eos_admissibility is not None,
              r.conditional_sequence is not None,
              r.anisotropy is not None,
              r.candidate_potential is not None,
              r.degeneracy_assessment is not None,
              r.nec_compatibility is not None,
              r.lapse_impact is not None,
          ]))
    check("diagnostics populated",
          len(r.diagnostics) >= 15)
    check("approx status nonempty",
          len(r.approx_status) > 50)

    # ----------------------------------------------------------------
    # 11. Serialization (4 checks)
    # ----------------------------------------------------------------
    print("\n--- 11. Serialization ---")
    d = eos_potential_result_to_dict(r)
    check("dict is dict", isinstance(d, dict))
    check("dict valid", d["valid"] is True)
    s = json.dumps(d)
    d2 = json.loads(s)
    check("JSON roundtrip", d2["valid"] is True)
    check("scope in dict",
          d["closure_classification"] == "admissible_but_nonunique")

    # ----------------------------------------------------------------
    # 12. Nonclaims (5 checks)
    # ----------------------------------------------------------------
    print("\n--- 12. Nonclaims ---")
    ncs = r.nonclaims
    check("at least 15 nonclaims", len(ncs) >= 15)
    check("first nonclaim is guardrail",
          "does NOT" in ncs[0])
    check("mentions anisotropy",
          any("anisotropic" in n.lower() for n in ncs))
    check("mentions lapse persists",
          any("lapse" in n.lower() and "persist" in n.lower()
              for n in ncs))
    check("mentions no predictions changed",
          any("No observational" in n for n in ncs))

    # ----------------------------------------------------------------
    # 13. Primary Questions Q1-Q7 (7 checks)
    # ----------------------------------------------------------------
    print("\n--- 13. Primary Questions ---")
    # Q1: Is beta_Q an EOS exponent?
    check("Q1: beta_Q is NOT an EOS exponent",
          ea.beta_Q_is_eos_exponent is False
          and ea.beta_Q_is_stiffness_exponent is True)
    # Q2: Does mapping require isotropy?
    check("Q2: requires isotropy / perfect-fluid",
          ea.requires_isotropy and ea.requires_perfect_fluid)
    # Q3: If collapse anisotropic, need w_r and w_perp?
    check("Q3: collapse needs (w_r, w_perp) not single w",
          aa.collapse_needs_wr_and_wperp
          and aa.single_w_insufficient_for_collapse)
    # Q4: Under what assumptions does w_Phi determine V?
    check("Q4: conditional mapping exists with 3 conditional steps",
          seq.n_conditional_forward == 3
          and cp.not_from_beta_Q_alone)
    # Q5: Does V reduce degeneracy?
    check("Q5: V partially reduces (Route A only), NOT breaks",
          dr.reduces_route_a
          and not dr.fully_breaks_degeneracy
          and not dr.source_degeneracy_broken)
    # Q6: Does closure conflict with Phase V NEC?
    check("Q6: no NEC conflict (Route A isotropic scope)",
          nc.no_conflict
          and nc.scope_is_isotropic_route_a_only
          and nc.not_full_collapse_nec_analysis)
    # Q7: Does closure improve lapse?
    check("Q7: lapse obstruction UNCHANGED",
          la.improves_lapse_determination is False
          and la.obstruction_lifted is False
          and la.phase_v_obstruction_unchanged)

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
