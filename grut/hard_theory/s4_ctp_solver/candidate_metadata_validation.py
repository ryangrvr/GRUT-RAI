"""Validate completed candidate metadata."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.candidate_metadata_schema import (
    required_candidate_metadata_fields,
)


def validate_candidate_metadata(registry: Dict[str, object]) -> Dict[str, object]:
    required_fields = required_candidate_metadata_fields()
    candidate_buckets = registry.get("candidate_buckets", {})

    missing_fields: List[str] = []

    for candidate in candidate_buckets.values():
        if not isinstance(candidate, dict):
            continue
        for field in required_fields:
            if field not in candidate or candidate.get(field) is None:
                missing_fields.append(field)

    return {
        "valid": not missing_fields,
        "missing_fields": sorted(set(missing_fields)),
        "promotes_claims": False,
    }
