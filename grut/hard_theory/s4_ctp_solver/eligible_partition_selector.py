"""Select eligible partitions for dry runs."""

from typing import Dict, List


def select_eligible_partitions(partition_map: Dict[str, object]) -> Dict[str, object]:
    partitions: List[Dict[str, object]] = partition_map.get("partitions", [])
    eligible = [
        partition
        for partition in partitions
        if partition.get("partition_type") == "eligible_future"
    ]
    blocked = [
        partition
        for partition in partitions
        if partition.get("partition_type") == "blocked"
    ]
    forbidden = [
        partition
        for partition in partitions
        if partition.get("partition_type") == "forbidden_full_diagram"
    ]

    blocked_skipped = all(partition not in eligible for partition in blocked)
    forbidden_skipped = all(partition not in eligible for partition in forbidden)

    return {
        "selected_partitions": eligible,
        "blocked_skipped": blocked_skipped,
        "forbidden_skipped": forbidden_skipped,
        "promotes_claims": False,
    }
