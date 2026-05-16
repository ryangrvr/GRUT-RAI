"""Run symbolic dry-runs for eligible partitions."""

from typing import Dict, List


def run_eligible_partition_dry_runs(
    selected_partitions: List[Dict[str, object]],
) -> Dict[str, object]:
    attempts: List[Dict[str, object]] = []
    for partition in selected_partitions:
        attempts.append(
            {
                "partition_id": partition.get("partition_id"),
                "partition_type": partition.get("partition_type"),
                "integration_attempted": True,
                "integration_completed": "symbolic",
                "finite_part_computed": False,
                "result": "symbolic_regulated_expression",
                "regulator_present": True,
                "amplitude_computed": False,
                "scheme_id": partition.get("scheme_id"),
                "default_regulator": partition.get("default_regulator"),
                "status": "eligible_partition_dry_run",
                "promotes_claims": False,
            }
        )

    return {
        "attempts": attempts,
        "attempted_count": len(attempts),
        "finite_parts_computed": False,
        "amplitude_computed": False,
        "status": "eligible_partition_dry_runs",
        "promotes_claims": False,
    }
