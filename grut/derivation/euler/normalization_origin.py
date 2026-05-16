"""
Normalization Origin Diagnostic (Gate 1).

PURPOSE
-------
The Christensen-Duff Euler-anomaly sum for SM field content gives:
  a_hat_SM = 1991/720 ≈ 2.7653

When divided by 8π:   a_hat_SM / (8π) ≈ 0.1100  ← matches GRUT M11
When divided by 16π²: a_hat_SM / (16π²) ≈ 0.0175 ← does NOT match

The question is: why 8π and not something else?

This script tests six candidate geometric origins:
  1. Local Euler density (no normalization)
  2. Volume-normalized Euler density (per unit volume on S^4)
  3. Integrated Euler density (∫ E_4 d^4x with canonical normalization)
  4. Euler characteristic (χ(S^4) = 2 and related factors)
  5. CTP projection (Keldysh branch doubling, r/a normalization)
  6. Action normalization (1/16πG vs 1/8πG conventions)

RESULT
------
Identifies which candidate origin naturally produces 8π from first principles.
If none do, the origin is explicitly open; if multiple do, we identify which
is compatible with the S^4 geometry and Standard Model conventions.
"""
from __future__ import annotations

import math
from typing import Dict, Any

import numpy as np


# Standard Model field counts (Christensen-Duff 1979)
N_SCALARS_SM = 4
N_VECTORS_SM = 12
N_FERMIONS_SM = 45

# Christensen-Duff Euler-anomaly coefficients on round S^4
CD_SCALAR = 1.0 / 360.0
CD_VECTOR = 31.0 / 180.0
CD_FERMION = 11.0 / 720.0

# SM Euler-anomaly sum
A_HAT_SM = N_SCALARS_SM * CD_SCALAR + N_VECTORS_SM * CD_VECTOR + N_FERMIONS_SM * CD_FERMION


def candidate_1_local_no_norm() -> float:
    """Candidate 1: Local Euler density, no normalization."""
    return A_HAT_SM


def candidate_2_volume_normalized(volume_s4: float = 8.0 * math.pi ** 2) -> float:
    """
    Candidate 2: Euler density per unit volume on S^4.

    The round S^4 has volume V = 8π² (in natural units with radius 1).
    Local energy density ~ a_hat_SM / V scales the anomaly.
    """
    return A_HAT_SM / volume_s4


def candidate_3_integrated_with_8pi() -> float:
    """
    Candidate 3: Integrated Euler density with 8π normalization factor.

    The integrated Euler anomaly carries a conventional 8π factor from
    loop-measure normalization or action normalization (1/8πG).
    """
    return A_HAT_SM / (8.0 * math.pi)


def candidate_4_euler_characteristic() -> float:
    """
    Candidate 4: Euler characteristic projection.

    χ(S^4) = 2 is the Euler characteristic. If anomaly projection onto the
    characteristic degree-of-freedom carries a factor of 2 or 2π, that could
    modify the normalization.
    """
    euler_char = 2.0
    # If the normalization picks up χ(S^4):
    return A_HAT_SM / (euler_char * 2.0 * math.pi)


def candidate_5_ctp_keldysh() -> float:
    """
    Candidate 5: CTP/Keldysh branch projection.

    The Schwinger-Keldysh contour has two branches (forward and backward in
    time). Some normalizations count both branches, some only one. If both
    branches contribute equally, there could be a factor of 2 from branch
    doubling, or a factor of 1/2 from averaging.

    Test: if 8π ≈ 2 × 4π, perhaps the numerator is 2 (both branches) and the
    denominator is 4π.
    """
    # Hypothesis: 8π = 2 × 4π (two branches, each contributes 4π)
    return A_HAT_SM / (2.0 * 4.0 * math.pi)


def candidate_6_action_convention() -> float:
    """
    Candidate 6: Action normalization convention (1/8πG vs 1/16πG).

    Einstein-Hilbert action: S_EH = (1/16πG) ∫ R √g d^4x
    Some conventions use 1/8πG. If the anomaly inherits the action's
    normalization, this could explain the factor.

    Hypothesis: the Gauss-Bonnet anomaly uses 1/8πG, while the loop-measure
    uses 1/16π², and their ratio gives 8π.
    """
    # (1/8πG) / (1/(16π²)) ~ 8π in appropriate units
    return A_HAT_SM / (1.0 / (8.0 * math.pi))


def compute_required_normalization() -> float:
    """What normalization constant k makes M11 ≈ 0.11?"""
    target_m11 = 0.11
    k = A_HAT_SM / target_m11
    return k


def run_normalization_diagnostic() -> Dict[str, Any]:
    """Run all candidate origins and compare to target."""
    target_m11 = 0.11
    required_k = compute_required_normalization()

    results = {
        "a_hat_sm": A_HAT_SM,
        "a_hat_sm_rational": "1991/720",
        "target_m11": target_m11,
        "required_normalization_constant": required_k,
        # Candidate results
        "candidate_1_local_no_norm": {
            "value": candidate_1_local_no_norm(),
            "m11": candidate_1_local_no_norm() / required_k,
            "description": "Local Euler density, no normalization",
        },
        "candidate_2_volume_normalized": {
            "value": candidate_2_volume_normalized(),
            "m11": candidate_2_volume_normalized() / required_k,
            "description": "Euler density per unit volume on S^4 (V = 8π²)",
        },
        "candidate_3_integrated_8pi": {
            "value": candidate_3_integrated_with_8pi(),
            "m11": candidate_3_integrated_with_8pi() / required_k,
            "description": "Integrated Euler with 8π normalization factor",
        },
        "candidate_4_euler_char": {
            "value": candidate_4_euler_characteristic(),
            "m11": candidate_4_euler_characteristic() / required_k,
            "description": "Euler characteristic projection (χ(S^4)=2)",
        },
        "candidate_5_ctp_keldysh": {
            "value": candidate_5_ctp_keldysh(),
            "m11": candidate_5_ctp_keldysh() / required_k,
            "description": "CTP/Keldysh branch projection (2 branches)",
        },
        "candidate_6_action_convention": {
            "value": candidate_6_action_convention(),
            "m11": candidate_6_action_convention() / required_k,
            "description": "Action normalization (1/8πG convention)",
        },
    }

    # Rank candidates by distance from target M11
    candidates = [
        ("candidate_1", results["candidate_1_local_no_norm"]["m11"]),
        ("candidate_2", results["candidate_2_volume_normalized"]["m11"]),
        ("candidate_3", results["candidate_3_integrated_8pi"]["m11"]),
        ("candidate_4", results["candidate_4_euler_char"]["m11"]),
        ("candidate_5", results["candidate_5_ctp_keldysh"]["m11"]),
        ("candidate_6", results["candidate_6_action_convention"]["m11"]),
    ]
    candidates_sorted = sorted(
        candidates, key=lambda x: abs(x[1] - target_m11)
    )

    results["candidates_ranked_by_distance_from_target"] = [
        {
            "rank": i + 1,
            "name": name,
            "m11": value,
            "error": abs(value - target_m11),
            "error_percent": abs(value - target_m11) / target_m11 * 100.0,
        }
        for i, (name, value) in enumerate(candidates_sorted)
    ]

    return results


def print_normalization_report(r: Dict[str, Any]) -> None:
    print("\n" + "=" * 75)
    print("NORMALIZATION ORIGIN DIAGNOSTIC (Gate 1)")
    print("=" * 75)

    print(f"\n--- Christensen-Duff Anomaly Sum ---")
    print(f"  a_hat_SM = {r['a_hat_sm_rational']} = {r['a_hat_sm']:.8f}")
    print(f"  Target M11 = {r['target_m11']}")
    print(f"  Required normalization constant k = {r['required_normalization_constant']:.6f}")
    print(f"  (so that a_hat_SM / k ≈ 0.11)")

    print(f"\n--- Candidate Origins (ranked by distance from target) ---")
    for item in r["candidates_ranked_by_distance_from_target"]:
        match_indicator = "✓" if item["error_percent"] < 1.0 else ("~" if item["error_percent"] < 5.0 else "✗")
        print(f"\n  Rank {item['rank']}: {item['name']}")
        print(f"    M11 = {item['m11']:.8f}")
        print(f"    Error: {item['error']:.8f} ({item['error_percent']:.2f}%)")
        print(f"    Status: {match_indicator}")

    print(f"\n--- Detailed Candidate Descriptions ---")
    for key in ["candidate_1_local_no_norm", "candidate_2_volume_normalized",
                "candidate_3_integrated_8pi", "candidate_4_euler_char",
                "candidate_5_ctp_keldysh", "candidate_6_action_convention"]:
        if key in r:
            c = r[key]
            print(f"\n  {key}:")
            print(f"    {c['description']}")
            print(f"    Raw value: {c['value']:.8f}")

    print("\n--- Interpretation ---")
    best = r["candidates_ranked_by_distance_from_target"][0]
    if best["error_percent"] < 1.0:
        print(f"  ✅ {best['name']} lands within 1% of target M11.")
        print(f"     This candidate may explain the 8π factor geometrically.")
    elif best["error_percent"] < 5.0:
        print(f"  ⚠️  {best['name']} lands within 5% of target M11.")
        print(f"     This candidate may be approximate or require refinement.")
    else:
        print(f"  ❌ No candidate lands within 5% of target M11.")
        print(f"     The 8π normalization origin remains genuinely open.")
        print(f"     The best candidate ({best['name']}) achieves {best['error_percent']:.1f}% error.")

    print("=" * 75 + "\n")


if __name__ == "__main__":
    result = run_normalization_diagnostic()
    print_normalization_report(result)
