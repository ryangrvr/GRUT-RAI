"""Build candidate registry for coefficient assembly dry-run."""

from typing import Dict, List


def build_coefficient_candidate_registry(
    partition_finite_results: List[Dict[str, object]],
) -> Dict[str, object]:
    source_partitions = [result.get("partition_id") for result in partition_finite_results]

    candidate_buckets = {
        "c_final_candidate": {
            "candidate_id": "c_final_candidate_v1",
            "source_partitions": source_partitions,
            "status": "candidate_not_physical",
            "physical_coefficient_computed": False,
            "promotes_claims": False,
        },
        "c_cosmo_candidate": {
            "candidate_id": "c_cosmo_candidate_v1",
            "source_partitions": source_partitions,
            "status": "candidate_not_physical",
            "physical_coefficient_computed": False,
            "promotes_claims": False,
        },
        "scheme_fragile_candidate": {
            "candidate_id": "scheme_fragile_candidate_v1",
            "source_partitions": source_partitions,
            "status": "candidate_not_physical",
            "physical_coefficient_computed": False,
            "promotes_claims": False,
        },
        "nonlocal_scheme_protected_candidate": {
            "candidate_id": "nonlocal_scheme_protected_candidate_v1",
            "source_partitions": source_partitions,
            "status": "candidate_not_physical",
            "physical_coefficient_computed": False,
            "promotes_claims": False,
        },
    }

    return {
        "registry_id": "coefficient_candidate_registry_v1",
        "candidate_buckets": candidate_buckets,
        "promotes_claims": False,
    }
