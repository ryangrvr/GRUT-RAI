"""Select multiple approved partitions for cross-partition finite-part checks."""

from typing import Dict, List


def _partition_id_from_attempt(attempt: Dict[str, object]) -> str:
    return attempt.get("partition_id") or attempt.get("subintegrand_id") or "unknown_partition"


def select_cross_partition_finite_partitions(
    stage10f: Dict[str, object],
    stage11c: Dict[str, object],
    stage11d: Dict[str, object],
) -> Dict[str, object]:
    selection_allowed = all(
        [
            stage10f.get("audit", {}).get("status") == "valid",
            stage11c.get("audit", {}).get("status") == "valid",
            stage11c.get("all_benchmarks_pass") is True,
            stage11d.get("audit", {}).get("status") == "valid",
        ]
    )

    collected = stage10f.get("collected", {}).get("collected_attempts", [])
    unique_ids: List[str] = []
    selections: List[Dict[str, object]] = []

    if selection_allowed:
        for attempt in collected:
            partition_id = _partition_id_from_attempt(attempt)
            if partition_id in unique_ids:
                continue
            unique_ids.append(partition_id)
            selections.append(
                {
                    "partition_id": partition_id,
                    "scheme_id": attempt.get("scheme_id"),
                    "default_regulator": attempt.get("default_regulator"),
                    "source_stage": attempt.get("source_stage"),
                    "status": "selected_for_cross_partition_finite",
                    "promotes_claims": False,
                }
            )
            if len(selections) == 3:
                break

    return {
        "selected_partitions": selections,
        "selected_count": len(selections),
        "selection_allowed": selection_allowed,
        "promotes_claims": False,
    }
