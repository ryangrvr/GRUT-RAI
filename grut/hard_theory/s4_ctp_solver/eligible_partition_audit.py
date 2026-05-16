"""Audit for eligible partition dry-runs."""

from typing import Dict, List


def audit_eligible_partition_dry_runs(
    selection: Dict[str, object],
    attempts: Dict[str, object],
    consistency: Dict[str, object],
    guard: Dict[str, object],
) -> Dict[str, object]:
    selected: List[Dict[str, object]] = selection.get("selected_partitions", [])
    only_eligible = all(
        partition.get("partition_type") == "eligible_future" for partition in selected
    )
    blocked_skipped = selection.get("blocked_skipped") is True
    forbidden_skipped = selection.get("forbidden_skipped") is True

    attempt_list = attempts.get("attempts", [])
    no_amplitude = attempts.get("amplitude_computed") is False and all(
        attempt.get("amplitude_computed") is False for attempt in attempt_list
    )
    no_finite_parts = attempts.get("finite_parts_computed") is False and all(
        attempt.get("finite_part_computed") is False for attempt in attempt_list
    )

    consistent = consistency.get("consistent") is True
    guard_ok = guard.get("guard") == "tensor_placeholder_guard"

    status = (
        "valid"
        if all(
            [
                only_eligible,
                blocked_skipped,
                forbidden_skipped,
                no_amplitude,
                no_finite_parts,
                consistent,
                guard_ok,
            ]
        )
        else "invalid"
    )

    return {
        "audit": "eligible_partition_dry_runs",
        "status": status,
        "can_advance_to_partition_consistency_audit": status == "valid",
        "can_compute_finite_parts": False,
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
    }
