"""Audit for native integrand partition map."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.native_integrand_partition import (
    TESTED_SUBINTEGRAND_IDS,
)


def _classifications_valid(classifications: List[Dict[str, object]]) -> bool:
    return all(entry.get("can_integrate_now") is False for entry in classifications)


def _tested_ids_match(partitions: List[Dict[str, object]]) -> bool:
    tested_ids = [
        partition.get("partition_id")
        for partition in partitions
        if partition.get("partition_type") == "tested_minimal"
    ]
    return set(tested_ids) == set(TESTED_SUBINTEGRAND_IDS)


def audit_partition_map(
    partitions: List[Dict[str, object]],
    classifications: List[Dict[str, object]],
    graph: Dict[str, object],
    guard: Dict[str, object],
) -> Dict[str, object]:
    partitions_mapped = all(
        partition.get("status") == "partition_mapped" for partition in partitions
    )
    integrations_performed = any(
        partition.get("integration_performed") is True for partition in partitions
    )
    full_integrand_used = any(
        partition.get("full_integrand_used") is True for partition in partitions
    )
    classifications_ok = _classifications_valid(classifications)
    graph_ok = graph.get("acyclic") is True
    tested_ids_ok = _tested_ids_match(partitions)
    guard_ok = guard.get("guard") == "tensor_placeholder_guard"

    status = (
        "valid"
        if all(
            [
                partitions_mapped,
                not integrations_performed,
                not full_integrand_used,
                classifications_ok,
                graph_ok,
                tested_ids_ok,
                guard_ok,
            ]
        )
        else "invalid"
    )

    can_advance = graph_ok and classifications_ok and tested_ids_ok

    return {
        "audit": "native_integrand_partition_map",
        "status": status,
        "partitions_mapped": partitions_mapped,
        "integrations_performed": False,
        "full_integrand_used": False,
        "can_advance_to_partition_dry_runs": can_advance,
        "can_compute_finite_parts": False,
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
    }
