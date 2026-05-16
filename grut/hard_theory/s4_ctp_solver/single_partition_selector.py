"""Select a single approved partition for integration."""

from typing import Dict, List


def _partition_id_from_attempt(attempt: Dict[str, object]) -> str:
    return attempt.get("partition_id") or attempt.get("subintegrand_id") or "unknown_partition"


def select_single_approved_partition(partition_consistency_output: Dict[str, object]) -> Dict[str, object]:
    collected: List[Dict[str, object]] = partition_consistency_output.get(
        "collected", {}
    ).get("collected_attempts", [])

    approved = []
    for attempt in collected:
        if attempt.get("source_stage") in {"10C", "10E"}:
            approved.append(attempt)

    selected = approved[0] if approved else {}
    return {
        "partition_id": _partition_id_from_attempt(selected),
        "selected_count": 1,
        "approval_source": "10F",
        "full_integrand": False,
        "scheme_id": selected.get("scheme_id"),
        "default_regulator": selected.get("default_regulator"),
        "status": "single_partition_selected",
        "promotes_claims": False,
    }
