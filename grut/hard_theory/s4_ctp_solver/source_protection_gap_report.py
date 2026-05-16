"""Report protection requirement gaps for c_final_candidate sources."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.source_protection_requirements import (
    build_source_protection_requirement,
)


def _stage11e_attempts(stage11e: Dict[str, object]) -> List[Dict[str, object]]:
    attempts = stage11e.get("attempts", {})
    results = attempts.get("results", []) if isinstance(attempts, dict) else []
    return results if isinstance(results, list) else []


def _partition_ids_from_registry(stage12a: Dict[str, object]) -> List[str]:
    registry = stage12a.get("registry", {})
    candidate = registry.get("candidate_buckets", {}).get("c_final_candidate", {})
    source_partitions = candidate.get("source_partitions", [])
    return source_partitions if isinstance(source_partitions, list) else []


def build_source_protection_gap_report(
    stage12c_r5: Dict[str, object],
    stage10d: Dict[str, object],
    stage11e: Dict[str, object],
    stage12a: Dict[str, object],
) -> Dict[str, object]:
    disqualifying = stage12c_r5.get("disqualifying_sources", [])
    source_ids = [entry.get("partition_id") for entry in disqualifying]
    source_ids = [source_id for source_id in source_ids if source_id]

    if not source_ids:
        source_ids = _partition_ids_from_registry(stage12a)

    partitions = stage10d.get("partitions", [])
    partition_map = {entry.get("partition_id"): entry for entry in partitions}

    records = _stage11e_attempts(stage11e)
    record_map = {record.get("partition_id"): record for record in records}

    requirements: List[Dict[str, object]] = []
    for source_id in source_ids:
        record = record_map.get(source_id, {})
        _ = partition_map.get(source_id, {})
        requirements.append(build_source_protection_requirement(source_id, record))

    return {
        "sources": requirements,
        "source_count": len(requirements),
        "promotes_claims": False,
    }
