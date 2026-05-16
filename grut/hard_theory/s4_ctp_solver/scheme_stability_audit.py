"""Audit scheme stability of coefficient candidates."""

from typing import Dict, List


def _classification_entries(classifications: object) -> List[Dict[str, object]]:
    if isinstance(classifications, dict):
        entries = classifications.get("classifications", [])
        return entries if isinstance(entries, list) else []
    if isinstance(classifications, list):
        return classifications
    return []


def audit_scheme_stability(
    classifications: object, rules: Dict[str, object]
) -> Dict[str, object]:
    entries = _classification_entries(classifications)

    stable_candidates = [
        entry for entry in entries if entry.get("classification") == "scheme_protected"
    ]
    fragile_candidates = [
        entry for entry in entries if entry.get("classification") == "scheme_fragile"
    ]
    blocked_candidates = [
        entry
        for entry in entries
        if entry.get("classification") not in {"scheme_protected", "scheme_fragile"}
    ]

    stable_keys = {entry.get("candidate_key") for entry in stable_candidates}
    all_r_inputs_stable = (
        "c_final_candidate" in stable_keys
        and "c_cosmo_candidate" in stable_keys
        and not fragile_candidates
        and not blocked_candidates
    )

    return {
        "audit": "scheme_stability",
        "stable_candidates": stable_candidates,
        "fragile_candidates": fragile_candidates,
        "blocked_candidates": blocked_candidates,
        "all_r_inputs_stable": all_r_inputs_stable,
        "rules_id": rules.get("rules_id"),
        "promotes_claims": False,
    }
