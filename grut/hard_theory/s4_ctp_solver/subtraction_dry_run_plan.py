"""Build a subtraction dry-run plan for a single partition."""

from typing import Dict, List


def build_subtraction_dry_run_plan(mapping: Dict[str, object]) -> Dict[str, object]:
    planned: List[str] = mapping.get("mapped_counterterms", [])

    return {
        "plan_id": "single_partition_subtraction_dry_run",
        "subtractions_planned": planned,
        "subtractions_performed": False,
        "regulator_removed": False,
        "finite_part_computed": False,
        "status": "dry_run_only",
        "promotes_claims": False,
    }
