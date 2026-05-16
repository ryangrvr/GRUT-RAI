"""Compare benchmark finite parts against known values."""

from typing import Dict


def compare_finite_part_to_known(
    result: Dict[str, object],
    benchmark: Dict[str, object],
) -> Dict[str, object]:
    matches = result.get("finite_part") == benchmark.get("known_finite_part")
    return {
        "matches_known_finite_part": matches,
        "comparison_status": "benchmark_pass" if matches else "benchmark_fail",
        "promotes_claims": False,
    }
