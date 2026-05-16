"""Classify coefficient candidates by scheme stability."""

from typing import Dict, List, Iterable


_PROTECTED_TAGS = {
    "scheme_protected",
    "scheme_protected_candidate",
    "scheme_protected_benchmarked",
    "nonlocal_scheme_protected",
}


def _as_list(value: object) -> List[object]:
    if isinstance(value, list):
        return value
    if value is None:
        return []
    return [value]


def _string_terms(bucket: Dict[str, object]) -> List[str]:
    for key in ("source_terms", "source_invariants", "source_structures"):
        value = bucket.get(key)
        if isinstance(value, list) and all(isinstance(term, str) for term in value):
            return list(value)
    return []


def _structured_sources(bucket: Dict[str, object]) -> List[Dict[str, object]]:
    for key in ("sources", "source_candidates"):
        value = bucket.get(key)
        if isinstance(value, list) and all(isinstance(item, dict) for item in value):
            return list(value)
    return []


def _is_nonlocal_term(term: str) -> bool:
    return "nonlocal" in term or "R_log_box_R" in term


def _sources_all_nonlocal(bucket: Dict[str, object]) -> bool:
    terms = _string_terms(bucket)
    if terms:
        return all(_is_nonlocal_term(term) for term in terms)
    return False


def _sources_all_protected(bucket: Dict[str, object]) -> bool:
    terms = _string_terms(bucket)
    if terms:
        return all(_is_nonlocal_term(term) for term in terms)

    sources = _structured_sources(bucket)
    if not sources:
        return False

    def _source_is_protected(source: Dict[str, object]) -> bool:
        sensitivity = source.get("scheme_sensitivity")
        classification = source.get("classification")
        return sensitivity in _PROTECTED_TAGS or classification in _PROTECTED_TAGS

    return all(_source_is_protected(source) for source in sources)


def _classify_bucket(candidate_key: str, bucket: Dict[str, object]) -> Dict[str, object]:
    candidate_id = bucket.get("candidate_id")
    source_partitions = _as_list(bucket.get("source_partitions"))

    if candidate_key == "nonlocal_scheme_protected_candidate":
        classification = "scheme_protected"
        reason = "nonlocal_candidate_assumed_scheme_protected"
    elif candidate_key == "c_final_candidate":
        if _sources_all_nonlocal(bucket):
            classification = "conditionally_scheme_protected"
            reason = "nonlocal_sources_only"
        else:
            classification = "scheme_fragile"
            reason = "nonlocal_sources_required"
    elif candidate_key == "c_cosmo_candidate":
        if _sources_all_protected(bucket):
            classification = "scheme_protected"
            reason = "all_sources_scheme_protected"
        else:
            classification = "scheme_fragile"
            reason = "sources_not_all_protected"
    elif candidate_key == "scheme_fragile_candidate":
        classification = "scheme_fragile"
        reason = "explicitly_scheme_fragile"
    else:
        classification = "scheme_fragile"
        reason = "unrecognized_candidate_key"

    return {
        "candidate_key": candidate_key,
        "candidate_id": candidate_id,
        "classification": classification,
        "reason": reason,
        "source_partitions": source_partitions,
        "promotes_claims": False,
    }


def classify_coefficient_candidates(registry: Dict[str, object]) -> Dict[str, object]:
    candidate_buckets = registry.get("candidate_buckets", {})
    classifications: List[Dict[str, object]] = []

    for candidate_key, bucket in candidate_buckets.items():
        if isinstance(bucket, dict):
            classifications.append(_classify_bucket(candidate_key, bucket))

    return {
        "classifications": classifications,
        "promotes_claims": False,
    }
