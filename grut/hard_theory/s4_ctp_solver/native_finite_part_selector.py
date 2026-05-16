"""Select a native partition for a finite-part attempt."""

from typing import Dict


def select_native_partition_for_finite_part(
    stage11a: Dict[str, object],
    stage11b: Dict[str, object],
    stage11c: Dict[str, object],
) -> Dict[str, object]:
    selection_allowed = all(
        [
            stage11a.get("audit", {}).get("status") == "valid",
            stage11b.get("audit", {}).get("status") == "valid",
            stage11c.get("audit", {}).get("status") == "valid",
            stage11c.get("all_benchmarks_pass") is True,
        ]
    )

    partition_id = stage11a.get("selection", {}).get("partition_id")

    return {
        "partition_id": partition_id,
        "selected_count": 1,
        "selection_allowed": selection_allowed,
        "status": "native_partition_selected_for_finite_part",
        "scheme_id": stage11a.get("selection", {}).get("scheme_id"),
        "default_regulator": stage11a.get("selection", {}).get("default_regulator"),
        "promotes_claims": False,
    }
