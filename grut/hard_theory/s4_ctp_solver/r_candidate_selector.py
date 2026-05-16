"""Select candidate coefficient pairs for R legality checks."""

from typing import Dict, List, Tuple


def _classification_entries(classifications: object) -> List[Dict[str, object]]:
    if isinstance(classifications, dict):
        entries = classifications.get("classifications", [])
        return entries if isinstance(entries, list) else []
    if isinstance(classifications, list):
        return classifications
    return []


def _stage11e_attempts(stage11e: Dict[str, object]) -> List[Dict[str, object]]:
    attempts = stage11e.get("attempts", {})
    results = attempts.get("results", []) if isinstance(attempts, dict) else []
    return results if isinstance(results, list) else []


def _find_partition_records(
    partition_ids: List[object], stage11e: Dict[str, object]
) -> List[Dict[str, object]]:
    if not partition_ids:
        return []
    records = []
    for result in _stage11e_attempts(stage11e):
        if result.get("partition_id") in partition_ids:
            records.append(result)
    return records


def _unique_value(values: List[object]) -> object:
    unique = {value for value in values if value is not None}
    return unique.pop() if len(unique) == 1 else None


def _derive_renorm_structure_id(
    bucket: Dict[str, object], stage11e: Dict[str, object]
) -> object:
    explicit = bucket.get("renorm_structure_id") or bucket.get(
        "renormalization_structure_id"
    )
    if explicit:
        return explicit

    partitions = bucket.get("source_partitions")
    partition_ids = partitions if isinstance(partitions, list) else []
    records = _find_partition_records(partition_ids, stage11e)
    scheme_id = _unique_value([record.get("scheme_id") for record in records])
    regulator = _unique_value([record.get("default_regulator") for record in records])
    if scheme_id and regulator:
        return f"{scheme_id}:{regulator}"
    return None


def _derive_regulator_dependence(
    bucket: Dict[str, object], stage11e: Dict[str, object]
) -> object:
    if bucket.get("regulator_dependence_class"):
        return bucket.get("regulator_dependence_class")
    partitions = bucket.get("source_partitions")
    partition_ids = partitions if isinstance(partitions, list) else []
    records = _find_partition_records(partition_ids, stage11e)
    regulator = _unique_value([record.get("default_regulator") for record in records])
    return regulator


def _derive_protection_class(candidate_key: str, bucket: Dict[str, object]) -> str:
    explicit = bucket.get("protection_class")
    if isinstance(explicit, str):
        return explicit
    if candidate_key == "nonlocal_scheme_protected_candidate":
        return "nonlocal"
    return "local"


def _build_candidate_metadata(
    candidate_key: str, bucket: Dict[str, object], stage11e: Dict[str, object]
) -> Dict[str, object]:
    return {
        "candidate_key": candidate_key,
        "candidate_id": bucket.get("candidate_id"),
        "renorm_structure_id": _derive_renorm_structure_id(bucket, stage11e),
        "tensor_origin_class": bucket.get("tensor_origin_class"),
        "loop_order": bucket.get("loop_order"),
        "regulator_dependence_class": _derive_regulator_dependence(bucket, stage11e),
        "counterterm_contamination": bucket.get("counterterm_contamination", False),
        "protection_class": _derive_protection_class(candidate_key, bucket),
        "cancellation_ready": bucket.get("cancellation_ready", {}),
        "source_partitions": bucket.get("source_partitions", []),
    }


def _is_scheme_stable(entry: Dict[str, object]) -> bool:
    return entry.get("classification") == "scheme_protected"


def _is_nonlocal_or_anomaly(candidate: Dict[str, object]) -> bool:
    return candidate.get("protection_class") in {"nonlocal", "anomaly_protected"}


def _shares_renorm_structure(numerator: Dict[str, object], denominator: Dict[str, object]) -> bool:
    num_structure = numerator.get("renorm_structure_id")
    den_structure = denominator.get("renorm_structure_id")
    return bool(num_structure) and num_structure == den_structure


def identify_r_candidate_pairs(
    classifications: object,
    registry: Dict[str, object],
    stage11e: Dict[str, object],
) -> Dict[str, object]:
    entries = _classification_entries(classifications)
    bucket_map = registry.get("candidate_buckets", {})

    candidates: List[Dict[str, object]] = []
    for entry in entries:
        candidate_key = entry.get("candidate_key")
        bucket = bucket_map.get(candidate_key)
        if isinstance(bucket, dict):
            metadata = _build_candidate_metadata(candidate_key, bucket, stage11e)
            metadata["scheme_stable"] = _is_scheme_stable(entry)
            metadata["classification"] = entry.get("classification")
            metadata["classification_reason"] = entry.get("reason")
            candidates.append(metadata)

    candidate_pairs: List[Dict[str, object]] = []
    for numerator in candidates:
        for denominator in candidates:
            if numerator["candidate_key"] == denominator["candidate_key"]:
                continue

            stable = numerator.get("scheme_stable") and denominator.get("scheme_stable")
            nonlocal_ok = _is_nonlocal_or_anomaly(numerator) and _is_nonlocal_or_anomaly(
                denominator
            )
            renorm_ok = _shares_renorm_structure(numerator, denominator)

            if not stable:
                status = "rejected"
                reason = "scheme_stability_failed"
            elif not nonlocal_ok:
                status = "rejected"
                reason = "nonlocal_or_anomaly_required"
            elif not renorm_ok:
                status = "rejected"
                reason = "renorm_structure_mismatch"
            else:
                status = "eligible"
                reason = "eligible_pair"

            candidate_pairs.append(
                {
                    "numerator": numerator,
                    "denominator": denominator,
                    "selection_status": status,
                    "reason": reason,
                    "scheme_stable": stable,
                    "nonlocal_or_anomaly_protected": nonlocal_ok,
                    "renorm_structure_shared": renorm_ok,
                }
            )

    return {
        "candidate_pairs": candidate_pairs,
        "promotes_claims": False,
    }
