"""Helper report for c_final_candidate source metadata."""

from typing import Dict, List


def _stage11e_attempts(stage11e: Dict[str, object]) -> List[Dict[str, object]]:
    attempts = stage11e.get("attempts", {})
    results = attempts.get("results", []) if isinstance(attempts, dict) else []
    return results if isinstance(results, list) else []


def build_c_final_source_metadata_report(
    registry: Dict[str, object], stage11e: Dict[str, object]
) -> Dict[str, object]:
    candidate = registry.get("candidate_buckets", {}).get("c_final_candidate", {})
    source_partitions = candidate.get("source_partitions", [])
    partition_ids = source_partitions if isinstance(source_partitions, list) else []

    records = _stage11e_attempts(stage11e)
    record_map = {record.get("partition_id"): record for record in records}

    sources: List[Dict[str, object]] = []
    for partition_id in partition_ids:
        record = record_map.get(partition_id)
        sources.append(
            {
                "partition_id": partition_id,
                "stage11e_present": record is not None,
                "stage11e_record": record if record is not None else None,
                "locality_class": (record or {}).get("locality_class", "unknown"),
                "protection_class": (record or {}).get("protection_class", "unknown"),
                "anomaly_protected": (record or {}).get("anomaly_protected", "unknown"),
                "scheme_sensitivity": (record or {}).get("scheme_sensitivity", "unknown"),
                "invariant_class": (record or {}).get("invariant_class", "unknown"),
                "regulator_dependence_class": (record or {}).get(
                    "regulator_dependence_class", "unknown"
                ),
                "candidate_context": {
                    "candidate_id": candidate.get("candidate_id"),
                    "candidate_locality_class": candidate.get("locality_class"),
                    "candidate_invariant_class": candidate.get("invariant_class"),
                    "candidate_tensor_origin_class": candidate.get(
                        "tensor_origin_class"
                    ),
                },
                "promotes_claims": False,
            }
        )

    return {
        "source_count": len(partition_ids),
        "source_metadata": sources,
        "promotes_claims": False,
    }
