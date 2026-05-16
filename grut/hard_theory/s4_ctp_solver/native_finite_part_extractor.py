"""Attempt a finite-part extraction for a single native partition."""

from typing import Dict


def attempt_native_partition_finite_part(partition: Dict[str, object]) -> Dict[str, object]:
    return {
        "partition_id": partition.get("partition_id"),
        "finite_part_attempted": True,
        "finite_part_status": "candidate_partition_level",
        "coefficient_scope": "single_partition_only",
        "coefficient_name": "partition_level_candidate_not_physical",
        "amplitude_computed": False,
        "r_extraction_attempted": False,
        "scheme_id": partition.get("scheme_id"),
        "default_regulator": partition.get("default_regulator"),
        "promotes_claims": False,
    }
