"""Eligibility classification for native integrand partitions."""

from typing import Dict


def classify_partition_eligibility(partition: Dict[str, object]) -> Dict[str, object]:
    partition_type = partition.get("partition_type")
    if partition_type == "tested_minimal":
        eligibility = "already_tested"
        reason = "tested_minimal"
    elif partition_type == "eligible_future":
        eligibility = "eligible_for_dry_run"
        reason = "eligible_future"
    elif partition_type == "blocked":
        eligibility = "blocked_by_dependencies"
        reason = "tensor_contraction_dependencies"
    elif partition_type == "forbidden_full_diagram":
        eligibility = "forbidden_until_full_pipeline"
        reason = "full_pipeline_required"
    else:
        eligibility = "unknown"
        reason = "unrecognized_partition_type"

    return {
        "partition_id": partition.get("partition_id"),
        "eligibility": eligibility,
        "reason": reason,
        "can_integrate_now": False,
        "promotes_claims": False,
    }
