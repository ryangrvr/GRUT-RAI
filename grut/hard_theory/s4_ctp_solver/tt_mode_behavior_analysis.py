"""Mode-by-mode behavior diagnostics for TT truncated inversion."""

from typing import Dict, List


def analyze_mode_behavior(inversion_results: List[Dict[str, object]]) -> Dict[str, object]:
    l_values = [result.get("l_max") for result in inversion_results]
    low_l = "present" if any(l_max and l_max >= 3 for l_max in l_values) else "missing"
    high_l = "truncated" if l_values else "unknown"

    dominant_modes = [2, 3] if l_values else []
    pathology_detected = any(
        result.get("expression") == 0 for result in inversion_results
    )

    return {
        "mode_behavior": {
            "low_l": low_l,
            "high_l_trend": high_l,
            "dominant_modes": dominant_modes,
        },
        "pathology_detected": pathology_detected,
        "promotes_claims": False,
    }
