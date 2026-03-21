#!/usr/bin/env python3
"""Benchmark: Route C Non-Markov Kernel Test — Spectral Kernels vs 1/r^2.

~57 independent checks covering:
  1.  Setup & Assumptions               (5)
  2.  Markov Baseline Recovery           (6)
  3.  Kernel Class Definitions           (5)
  4.  Source Profile Locking Theorem     (7)
  5.  Two-Pole Kernel Analysis           (5)
  6.  Power-Law Kernel Analysis          (5)
  7.  Spectral Richness Assessment       (5)
  8.  Component B Compatibility          (6)
  9.  Localizability / Promotability     (5)
  10. Final Classification & Nonclaims   (8)
"""

from __future__ import annotations

import math
import sys

from grut.route_c_nonmarkov_kernel import (
    compute_route_c_nonmarkov_assessment,
    route_c_nonmarkov_result_to_dict,
    recover_markov_baseline,
    define_kernel_classes,
    prove_source_profile_locking,
    compute_kernel_support_profiles,
    assess_spectral_richness,
    assess_component_b_compatibility,
    assess_localizability,
    assess_physical_promotability,
    classify_nonmarkov_route_c,
    RouteCNonMarkovParams,
    ALPHA_VAC,
    R_S,
    M_EXT,
    R_EQ,
    TAU_CANONICAL,
    A_CRIT,
    EPSILON_RC_COEFF,
    COMP_B_COEFF,
    RHO_EQ_COEFF,
    N_KERNEL_CLASSES,
    COMPONENT_B_TARGET_EXPONENT,
    LOCKED_SPATIAL_EXPONENT,
    NONCLAIMS,
    NONMARKOV_ASSUMPTIONS,
)


# ================================================================
# Helpers
# ================================================================

_passed = 0
_failed = 0


def check(label: str, condition: bool) -> None:
    global _passed, _failed
    if condition:
        _passed += 1
        print(f"  [PASS] {label}")
    else:
        _failed += 1
        print(f"  [FAIL] {label}")


def close(label: str, a: float, b: float, tol: float = 1e-6) -> None:
    check(label, abs(a - b) < tol)


def rel_close(label: str, a: float, b: float, tol: float = 1e-4) -> None:
    denom = abs(b) if abs(b) > 1e-30 else 1.0
    check(label, abs(a - b) / denom < tol)


# ================================================================
# Main
# ================================================================

def main() -> None:
    global _passed, _failed

    print("=" * 72)
    print("BENCHMARK: Route C Non-Markov Kernel Test — Spectral Kernels vs 1/r^2")
    print("=" * 72)
    print()

    params = RouteCNonMarkovParams(n_r=500, n_t=200)
    print("  Running non-Markov kernel assessment...")
    result = compute_route_c_nonmarkov_assessment(params)
    print(f"  Assessment complete. Valid: {result.valid}")
    print()

    # ------------------------------------------------------------------
    # Section 1: Setup & Assumptions
    # ------------------------------------------------------------------
    print("--- Section 1: Setup & Assumptions ---")
    close("alpha_vac = 1/3", ALPHA_VAC, 1.0 / 3.0, tol=1e-10)
    close("M = r_s/2 = 0.5", M_EXT, 0.5, tol=1e-10)
    close("tau = sqrt(3/2) ~ 1.2247", TAU_CANONICAL, math.sqrt(1.5), tol=1e-10)
    close("A_crit = 1.062", A_CRIT, 1.062, tol=1e-10)
    rel_close(
        "EPSILON_RC_COEFF = A_crit^2 * M^2 / (2*tau^2)",
        EPSILON_RC_COEFF,
        A_CRIT ** 2 * M_EXT ** 2 / (2.0 * TAU_CANONICAL ** 2),
    )
    print()

    # ------------------------------------------------------------------
    # Section 2: Markov Baseline Recovery
    # ------------------------------------------------------------------
    print("--- Section 2: Markov Baseline Recovery ---")
    mb = result.markov_baseline
    rel_close("epsilon_rc_coeff ~ 0.0940", mb.epsilon_rc_coeff, 0.0940, tol=0.01)
    close("scaling_exponent ~ -4.0", mb.scaling_exponent, -4.0, tol=1e-6)
    check("is_pure_r4 = True", mb.is_pure_r4 is True)
    check("matches_locked_result = True", mb.matches_locked_result is True)
    check("deviation_from_locked < 1e-10", mb.deviation_from_locked < 1e-10)
    check("has notes", len(mb.notes) >= 3)
    print()

    # ------------------------------------------------------------------
    # Section 3: Kernel Class Definitions
    # ------------------------------------------------------------------
    print("--- Section 3: Kernel Class Definitions ---")
    kc = result.kernel_classes
    check("n_kernel_classes = 4", kc.n_kernel_classes == 4)
    check(
        "kernel names include single_exponential",
        "single_exponential" in kc.kernel_names,
    )
    check("kernel names include two_pole", "two_pole" in kc.kernel_names)
    check("kernel names include power_law", "power_law" in kc.kernel_names)
    check(
        "all have spectral representation",
        all(kc.has_spectral_representation),
    )
    print()

    # ------------------------------------------------------------------
    # Section 4: Source Profile Locking Theorem
    # ------------------------------------------------------------------
    print("--- Section 4: Source Profile Locking Theorem ---")
    sl = result.source_locking
    check("source_is_separable = True", sl.source_is_separable is True)
    check("field_response_separable = True", sl.field_response_separable is True)
    check("spatial_scaling_locked = True", sl.spatial_scaling_locked is True)
    close("locked_scaling_exponent = -4.0", sl.locked_scaling_exponent, -4.0, tol=1e-10)
    check("numerical_verification_passed = True", sl.numerical_verification_passed is True)
    check(
        f"max_deviation_from_minus4 < 0.05 (actual: {sl.max_deviation_from_minus4:.2e})",
        sl.max_deviation_from_minus4 < 0.05,
    )
    check(
        "structural_argument contains 'separable'",
        "separable" in sl.structural_argument.lower(),
    )
    print()

    # ------------------------------------------------------------------
    # Section 5: Two-Pole Kernel Analysis
    # ------------------------------------------------------------------
    print("--- Section 5: Two-Pole Kernel Analysis ---")
    two_pole = [p for p in result.kernel_profiles if p.kernel_name == "two_pole"]
    check("two_pole profile found", len(two_pole) == 1)
    if two_pole:
        tp = two_pole[0]
        close("spatial_scaling_exponent ~ -4.0", tp.spatial_scaling_exponent, -4.0, tol=0.01)
        check("temporal_profile_differs = True", tp.temporal_profile_differs is True)
        check("matches_component_b = False", tp.matches_component_b is False)
        check(
            f"exponent_std_across_time < 0.05 (actual: {tp.exponent_std_across_time:.2e})",
            tp.exponent_std_across_time < 0.05,
        )
    print()

    # ------------------------------------------------------------------
    # Section 6: Power-Law Kernel Analysis
    # ------------------------------------------------------------------
    print("--- Section 6: Power-Law Kernel Analysis ---")
    power_law = [p for p in result.kernel_profiles if p.kernel_name == "power_law"]
    check("power_law profile found", len(power_law) == 1)
    if power_law:
        pl = power_law[0]
        close("spatial_scaling_exponent ~ -4.0", pl.spatial_scaling_exponent, -4.0, tol=0.01)
        check("temporal_profile_differs = True", pl.temporal_profile_differs is True)
        check("matches_component_b = False", pl.matches_component_b is False)
        check(
            f"exponent_std_across_time < 0.05 (actual: {pl.exponent_std_across_time:.2e})",
            pl.exponent_std_across_time < 0.05,
        )
    print()

    # ------------------------------------------------------------------
    # Section 7: Spectral Richness Assessment
    # ------------------------------------------------------------------
    print("--- Section 7: Spectral Richness Assessment ---")
    sr = result.spectral_richness
    check("can_change_temporal_profile = True", sr.can_change_temporal_profile is True)
    check("can_change_peak_amplitude = True", sr.can_change_peak_amplitude is True)
    check("can_change_spatial_scaling = False", sr.can_change_spatial_scaling is False)
    check("can_redistribute_radially = False", sr.can_redistribute_radially is False)
    check(
        "history_term_spatial_scaling = '1/r^4'",
        sr.history_term_spatial_scaling == "1/r^4",
    )
    print()

    # ------------------------------------------------------------------
    # Section 8: Component B Compatibility
    # ------------------------------------------------------------------
    print("--- Section 8: Component B Compatibility ---")
    cb = result.component_b_compat
    check("any_matches_component_b = False", cb.any_matches_component_b is False)
    close("best_scaling_exponent ~ -4.0", cb.best_scaling_exponent, -4.0, tol=0.01)
    close("target_exponent = -2.0", cb.target_exponent, -2.0, tol=1e-10)
    close("gap_to_target ~ 2.0", cb.gap_to_target, 2.0, tol=0.01)
    check("n_kernel_results = 4", len(cb.kernel_results) == 4)
    check(
        "all kernel_results have matches_component_b = False",
        all(kr["matches_component_b"] is False for kr in cb.kernel_results),
    )
    print()

    # ------------------------------------------------------------------
    # Section 9: Localizability / Promotability
    # ------------------------------------------------------------------
    print("--- Section 9: Localizability / Promotability ---")
    lz = result.localizability
    pr = result.promotability
    check("nonlocal_in_time = True", lz.nonlocal_in_time is True)
    check("local_in_space = True", lz.local_in_space is True)
    check("any_kernel_promotable = False", pr.any_kernel_promotable is False)
    check(
        "obstruction = 'source_profile_locking'",
        pr.obstruction == "source_profile_locking",
    )
    check(
        "remaining_loophole = 'modified_source_law'",
        pr.remaining_loophole == "modified_source_law",
    )
    print()

    # ------------------------------------------------------------------
    # Section 10: Final Classification & Nonclaims
    # ------------------------------------------------------------------
    print("--- Section 10: Final Classification & Nonclaims ---")
    cl = result.classification
    check(
        "classification = nonmarkov_route_c_insufficient_for_component_b",
        cl.classification == "nonmarkov_route_c_insufficient_for_component_b",
    )
    check("source_profile_locking_proven = True", cl.source_profile_locking_proven is True)
    check("n_kernel_classes_tested = 4", cl.n_kernel_classes_tested == 4)
    check("all_tested_insufficient = True", cl.all_tested_insufficient is True)
    check("10 nonclaims", len(result.nonclaims) == 10)
    check("10 assumptions", len(result.assumptions) == 10)
    check(
        "nonclaims mention 'NOT prove Route C physically incorrect'",
        any("NOT prove Route C physically incorrect" in nc for nc in result.nonclaims),
    )
    # Serialization
    d = route_c_nonmarkov_result_to_dict(result)
    check(
        "serialization dict classification correct",
        d["classification"]["classification"]
        == "nonmarkov_route_c_insufficient_for_component_b",
    )
    print()

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    total = _passed + _failed
    print("=" * 72)
    print(f"TOTAL: {_passed}/{total} checks passed, {_failed} failed")
    if _failed == 0:
        print("ALL CHECKS PASSED")
    else:
        print("SOME CHECKS FAILED")
    print()

    # Key findings
    print("--- Key Findings ---")
    print(f"  Markov baseline coeff: {mb.epsilon_rc_coeff:.4e}")
    print(f"  Markov exponent: {mb.scaling_exponent:.6f}")
    print(f"  Markov matches locked: {mb.matches_locked_result}")
    print(f"  Source locking proven: {sl.spatial_scaling_locked}")
    print(f"  Max deviation from -4.0: {sl.max_deviation_from_minus4:.2e}")
    print(f"  Per-kernel exponents: {sl.per_kernel_exponents}")
    print(f"  Any matches Component B: {cb.any_matches_component_b}")
    print(f"  Best scaling exponent: {cb.best_scaling_exponent:.4f}")
    print(f"  Gap to target: {cb.gap_to_target:.4f}")
    print(f"  Can change spatial scaling: {sr.can_change_spatial_scaling}")
    print(f"  Can change temporal profile: {sr.can_change_temporal_profile}")
    print(f"  Any kernel promotable: {pr.any_kernel_promotable}")
    print(f"  Obstruction: {pr.obstruction}")
    print(f"  Remaining loophole: {pr.remaining_loophole}")
    print(f"  Classification: {cl.classification}")
    print("=" * 72)

    sys.exit(0 if _failed == 0 else 1)


if __name__ == "__main__":
    main()
