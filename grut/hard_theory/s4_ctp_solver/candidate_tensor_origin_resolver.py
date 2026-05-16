"""Resolve tensor_origin_class for coefficient candidates."""

from typing import Dict


_TENSOR_ORIGIN_MAP = {
    "nonlocal_scheme_protected_candidate": "nonlocal_anomaly_tensor_channel",
    "c_final_candidate": "candidate_final_tensor_channel_pending_source_audit",
    "c_cosmo_candidate": "local_cosmological_tensor_channel",
    "scheme_fragile_candidate": "local_scheme_fragile_tensor_channel",
}


def resolve_tensor_origin_class(candidate_key: str) -> str:
    return _TENSOR_ORIGIN_MAP.get(candidate_key, "local_scheme_fragile_tensor_channel")


def apply_tensor_origin_metadata(registry: Dict[str, object]) -> Dict[str, object]:
    candidate_buckets = registry.get("candidate_buckets", {})
    for candidate_key, candidate in candidate_buckets.items():
        if not isinstance(candidate, dict):
            continue
        candidate["tensor_origin_class"] = resolve_tensor_origin_class(candidate_key)
    return registry
