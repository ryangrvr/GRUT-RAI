"""Compare partial integration result to known benchmark."""

from typing import Dict


def compare_partial_integration_to_known(
    result: Dict[str, object],
    benchmark: Dict[str, object],
) -> Dict[str, object]:
    matches = result.get("result") == benchmark.get("known_result")
    return {
        "matches_known_result": matches,
        "comparison_status": "benchmark_pass" if matches else "benchmark_fail",
        "promotes_claims": False,
    }
