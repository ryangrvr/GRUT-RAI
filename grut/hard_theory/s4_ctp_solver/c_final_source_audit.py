"""Audit c_final_candidate source partitions for protection eligibility."""

from typing import Dict, List


_PROTECTED_SCHEME_CLASSES = {
    "scheme_protected",
    "scheme_protected_candidate",
    "scheme_protected_benchmarked",
    "nonlocal_scheme_protected",
}


def _stage11e_attempts(stage11e: Dict[str, object]) -> List[Dict[str, object]]:
    attempts = stage11e.get("attempts", {})
    results = attempts.get("results", []) if isinstance(attempts, dict) else []
    return results if isinstance(results, list) else []


def _find_partition_records(
    partition_ids: List[str], stage11e: Dict[str, object]
) -> List[Dict[str, object]]:
    if not partition_ids:
        return []
    records: List[Dict[str, object]] = []
    for result in _stage11e_attempts(stage11e):
        if result.get("partition_id") in partition_ids:
            records.append(result)
    return records


def _source_is_nonlocal(source: Dict[str, object]) -> bool:
    if source.get("locality_class") == "nonlocal":
        return True
    return source.get("protection_class") in {"nonlocal", "anomaly_protected"}


def _source_is_anomaly_protected(source: Dict[str, object]) -> bool:
    if source.get("protection_class") == "anomaly_protected":
        return True
    return source.get("anomaly_protected") is True


def _source_is_scheme_protected(source: Dict[str, object]) -> bool:
    for key in ("invariant_class", "scheme_sensitivity", "classification", "scheme_class"):
        if source.get(key) in _PROTECTED_SCHEME_CLASSES:
            return True
    return False


def _source_has_regulator_preserved(
    source: Dict[str, object], candidate: Dict[str, object]
) -> bool:
    status = source.get("regulator_dependence_class") or candidate.get(
        "regulator_dependence_class"
    )
    return status == "symbolic_regulator_preserved"


def audit_c_final_sources(
    registry: Dict[str, object], stage11e: Dict[str, object]
) -> Dict[str, object]:
    candidate = registry.get("candidate_buckets", {}).get("c_final_candidate", {})
    source_partitions = candidate.get("source_partitions", [])
    partition_ids = source_partitions if isinstance(source_partitions, list) else []

    records = _find_partition_records(partition_ids, stage11e)
    record_map = {record.get("partition_id"): record for record in records}

    audited_sources: List[Dict[str, object]] = []
    disqualifying_sources: List[Dict[str, object]] = []

    for partition_id in partition_ids:
        source = record_map.get(partition_id, {"partition_id": partition_id})
        reasons: List[str] = []

        if record_map.get(partition_id) is None:
            reasons.append("source_record_missing")

        if not _source_is_nonlocal(source):
            reasons.append("source_not_nonlocal")
        if not _source_is_anomaly_protected(source):
            reasons.append("source_not_anomaly_protected")
        if not _source_is_scheme_protected(source):
            reasons.append("source_not_scheme_protected")
        if not _source_has_regulator_preserved(source, candidate):
            reasons.append("source_regulator_not_preserved")

        qualifies = not reasons
        audited_sources.append(
            {
                "partition_id": partition_id,
                "qualifies": qualifies,
                "reasons": reasons,
                "promotes_claims": False,
            }
        )

        if reasons:
            disqualifying_sources.append(
                {
                    "partition_id": partition_id,
                    "reasons": reasons,
                    "promotes_claims": False,
                }
            )

    return {
        "source_count": len(partition_ids),
        "c_final_sources": audited_sources,
        "disqualifying_sources": disqualifying_sources,
        "promotes_claims": False,
    }
