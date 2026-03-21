#!/usr/bin/env python3
"""Benchmark: Phase V — Constitutive-to-Metric Lapse Obstruction Analysis.

~70 independent checks covering:
  1.  Insufficiency Theorem (12)
  2.  Effective NEC (7)
  3.  Lapse Direction (8)
  4.  T^Phi Status (5)
  5.  Proxy Classification (8)
  6.  Status Ladder (6)
  7.  Self-Healing (5)
  8.  Phase IV Reconfirmation (3)
  9.  Beta Scan (7)
  10. Serialization (5)
  11. Nonclaims (6)
"""

from __future__ import annotations

import json
import math
import sys

from grut.covariant_interior import (
    compute_covariant_interior_analysis,
    covariant_interior_result_to_dict,
    build_insufficiency_theorem,
    scan_A_eff_vs_beta,
    _compactness,
    _h_of_x,
    _g_of_beta,
    _A_eff_from_constitutive,
    ALPHA_VAC,
    BETA_Q,
    ALPHA_VAC_CRITICAL,
    SCOPE_STATEMENT,
    LEVEL_EXACT,
    LEVEL_CONSTITUTIVE_DERIVED,
    LEVEL_UNRESOLVED,
    LEVEL_CONSTITUTIVE_LAPSE_PROMOTION_OBSTRUCTED,
    LEVEL_CONSTITUTIVE_SURROGATE,
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
    print("BENCHMARK: Phase V — Constitutive-to-Metric Lapse Obstruction")
    print("=" * 72)

    # Build master result
    r = compute_covariant_interior_analysis()
    ip = r.insufficiency_theorem
    nec = r.effective_nec
    ld = r.lapse_direction
    ts = r.tphi_status
    pc = r.proxy_classification
    sl = r.status_ladder
    sh = r.self_healing
    p4 = r.phase4_reconfirmation
    scan = r.beta_scan

    # ----------------------------------------------------------------
    # 1. Insufficiency Theorem (12 checks)
    # ----------------------------------------------------------------
    print("\n--- 1. Insufficiency Theorem ---")
    check("alpha satisfies bound", ip.alpha_vac_satisfies_bound)
    check("ln_alpha_abs correct",
          abs(ip.ln_alpha_abs - abs(math.log(ALPHA_VAC))) < 1e-12)
    check("2L >= 1", ip.two_L_ge_one)
    check("h positive for all x", ip.h_positive_for_all_x)
    check("g positive for all beta", ip.g_positive_for_all_beta)
    check("A_eff negative for all finite beta",
          ip.A_eff_negative_for_all_finite_beta)
    check("theorem status = proven", ip.theorem_status == "proven")
    check("scope statement verbatim", ip.scope_statement == SCOPE_STATEMENT)
    check("sample A_eff all < 0",
          all(a < 0 for a in ip.sample_A_eff_values))
    check("sample g all > 0",
          all(g > 0 for g in ip.sample_g_values))
    check("sample h all > 0",
          all(h > 0 for h in ip.sample_h_values))
    check("proof has 9 steps", len(ip.proof_steps) == 9)

    # ----------------------------------------------------------------
    # 2. Effective NEC (7 checks)
    # ----------------------------------------------------------------
    print("\n--- 2. Effective NEC ---")
    check("compactness = 3",
          abs(nec.compactness - 3.0) < 1e-12)
    check("is sub-horizon", nec.is_sub_horizon)
    check("A_eff = -1", abs(nec.A_eff - (-1.0)) < 1e-12)
    check("derivation level = constitutive",
          nec.derivation_level == "constitutive")
    check("NEC-violating support indicated",
          nec.nec_violating_support_indicated)
    check("rho+P sign = negative",
          nec.rho_plus_P_sign_effective == "negative")
    check("notes mention NOT covariant theorem",
          any("NOT a covariant theorem" in n for n in nec.notes))

    # ----------------------------------------------------------------
    # 3. Lapse Direction (8 checks)
    # ----------------------------------------------------------------
    print("\n--- 3. Lapse Direction ---")
    check("A_schw = -2", abs(ld.A_schw - (-2.0)) < 1e-12)
    check("g_tt_schw = 2 (positive)", abs(ld.g_tt_schw - 2.0) < 1e-12)
    check("t is spacelike in Schwarzschild", ld.t_is_spacelike_schw)
    check("r is timelike in Schwarzschild", ld.r_is_timelike_schw)
    check("A_eff = -1", abs(ld.A_eff - (-1.0)) < 1e-12)
    check("constitutive does NOT restore timelike",
          not ld.constitutive_restores_timelike)
    check("naive redshift fails", ld.naive_redshift_fails)
    check("requires adapted chart", ld.requires_adapted_chart_or_covariant)

    # ----------------------------------------------------------------
    # 4. T^Phi Status (5 checks)
    # ----------------------------------------------------------------
    print("\n--- 4. T^Phi Status ---")
    check("not Lagrangian-derived", not ts.is_lagrangian_derived)
    check("is schematic", ts.is_schematic)
    check("mapping underdetermined", ts.mapping_underdetermined)
    check("missing items >= 3", len(ts.missing_for_metric) >= 3)
    check("reason nonempty", len(ts.underdetermination_reason) > 20)

    # ----------------------------------------------------------------
    # 5. Proxy Classification (8 checks)
    # ----------------------------------------------------------------
    print("\n--- 5. Proxy Classification ---")
    check("psi = 1/3", abs(pc.psi_proxy - 1.0 / 3.0) < 1e-12)
    check("level 1 = exact", pc.level_1_status == LEVEL_EXACT)
    check("level 2 = constitutive_derived",
          pc.level_2_status == LEVEL_CONSTITUTIVE_DERIVED)
    check("level 3 (IV) = unresolved",
          pc.level_3_status_phase_iv == LEVEL_UNRESOLVED)
    check("level 3 (V) = obstructed",
          pc.level_3_status_phase_v
          == LEVEL_CONSTITUTIVE_LAPSE_PROMOTION_OBSTRUCTED)
    check("classification = constitutive_surrogate",
          pc.classification == LEVEL_CONSTITUTIVE_SURROGATE)
    check("cannot promote", not pc.can_be_promoted_to_true_lapse)
    check("cannot exclude", not pc.can_be_excluded)

    # ----------------------------------------------------------------
    # 6. Status Ladder (6 checks)
    # ----------------------------------------------------------------
    print("\n--- 6. Status Ladder ---")
    check("L1 unchanged", not sl.level_1_changed)
    check("L2 unchanged", not sl.level_2_changed)
    check("L3 changed", sl.level_3_changed)
    check("L3 before = unresolved", sl.level_3_before == LEVEL_UNRESOLVED)
    check("L3 after = obstructed",
          sl.level_3_after == LEVEL_CONSTITUTIVE_LAPSE_PROMOTION_OBSTRUCTED)
    check("no level weakened", sl.no_level_weakened)

    # ----------------------------------------------------------------
    # 7. Self-Healing (5 checks)
    # ----------------------------------------------------------------
    print("\n--- 7. Self-Healing ---")
    check("source vanishes", sh.source_vanishes)
    check("independent of metric", sh.independent_of_metric)
    check("independent of A_eff", sh.independent_of_A_eff)
    check("independent of NEC", sh.independent_of_nec)
    check("preserved", sh.preserved)

    # ----------------------------------------------------------------
    # 8. Phase IV Reconfirmation (3 checks)
    # ----------------------------------------------------------------
    print("\n--- 8. Phase IV Reconfirmation ---")
    check("all preserved", p4.all_preserved)
    check("level 1 preserved", p4.level_1_preserved)
    check("level 2 preserved", p4.level_2_preserved)

    # ----------------------------------------------------------------
    # 9. Beta Scan (7 checks)
    # ----------------------------------------------------------------
    print("\n--- 9. Beta Scan ---")
    check("scan length = 8", len(scan) == 8)
    check("all A_eff negative", all(e.A_eff_is_negative for e in scan))
    check("all g > 0", all(e.g_of_beta > 0 for e in scan))
    check("all h > 0", all(e.h_of_x > 0 for e in scan))
    check("canon A_eff = -1",
          abs([e for e in scan if abs(e.beta_Q - 2.0) < 0.01][0].A_eff
              - (-1.0)) < 1e-12)
    # Monotonicity
    g_decreasing = all(scan[i].g_of_beta > scan[i + 1].g_of_beta
                       for i in range(len(scan) - 1))
    check("g(beta) decreasing with beta", g_decreasing)
    A_increasing = all(scan[i].A_eff < scan[i + 1].A_eff
                       for i in range(len(scan) - 1))
    check("A_eff(beta) increasing toward 0-", A_increasing)

    # ----------------------------------------------------------------
    # 10. Serialization (5 checks)
    # ----------------------------------------------------------------
    print("\n--- 10. Serialization ---")
    d = covariant_interior_result_to_dict(r)
    check("dict is dict", isinstance(d, dict))
    check("dict valid", d["valid"] is True)
    s = json.dumps(d)
    d2 = json.loads(s)
    check("JSON roundtrip", d2["valid"] is True)
    check("scope in dict",
          d["insufficiency_theorem"]["scope_statement"] == SCOPE_STATEMENT)
    check("obstruction flag in dict",
          d["obstruction_is_about_constitutive_ansatz"] is True)

    # ----------------------------------------------------------------
    # 11. Nonclaims (6 checks)
    # ----------------------------------------------------------------
    print("\n--- 11. Nonclaims ---")
    nc = r.nonclaims
    check("at least 12 nonclaims", len(nc) >= 12)
    check("first nonclaim is guardrail",
          "does NOT prove" in nc[0])
    check("nonclaim mentions constitutive ansatz",
          any("CONSTITUTIVE POST-NEWTONIAN" in n.upper() for n in nc))
    check("nonclaim mentions NEC qualification",
          any("NOT a covariant theorem" in n for n in nc))
    check("nonclaim mentions self-healing preserved",
          any("PRESERVED" in n for n in nc))
    check("obstruction_is_about_constitutive_ansatz flag",
          r.obstruction_is_about_constitutive_ansatz is True)

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
