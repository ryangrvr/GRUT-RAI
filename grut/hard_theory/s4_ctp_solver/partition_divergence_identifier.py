"""Identify divergences for a single partition dry-run."""

from typing import Dict, List


def identify_partition_divergences(stage11a_result: Dict[str, object]) -> Dict[str, object]:
    partition_id = stage11a_result.get("selection", {}).get("partition_id")
    divergences: List[str] = ["epsilon_pole_placeholder", "log_divergence_placeholder"]

    return {
        "partition_id": partition_id,
        "divergences_identified": divergences,
        "regulator_active": True,
        "status": "divergences_identified_structural",
        "promotes_claims": False,
    }
