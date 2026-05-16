"""Select candidate pairs from scheme-protected sources."""

from __future__ import annotations

from typing import Dict, List


def _registered_map(stage_p6: Dict[str, object]) -> Dict[str, Dict[str, object]]:
    return {
        entry.get("protected_source_candidate_id"): entry
        for entry in stage_p6.get("registered_candidates", [])
    }


def select_protected_pairs(
    stage_p7: Dict[str, object],
    stage_p6: Dict[str, object],
) -> List[Dict[str, object]]:
    protected = stage_p7.get("scheme_protected_candidates", [])
    registered = _registered_map(stage_p6)

    candidates: List[Dict[str, object]] = []
    for entry in protected:
        candidate_id = entry.get("candidate_id")
        registered_entry = registered.get(candidate_id)
        if not registered_entry:
            continue

        candidates.append(
            {
                "candidate_id": candidate_id,
                "source_type": registered_entry.get("source_type"),
                "kernel_id": registered_entry.get("kernel_id"),
                "nonlocal_form_present": registered_entry.get("nonlocal_form_present"),
                "counterterm_nonmixing_verified": registered_entry.get(
                    "counterterm_nonmixing_verified"
                ),
                "finite_extractability": registered_entry.get("finite_extractability"),
                "coefficient_value": registered_entry.get("coefficient_value"),
                "scheme_protected": True,
                "regulator_class": "unknown",
                "source_family": "nonlocal_kernel",
                "promotes_claims": False,
            }
        )

    pairs: List[Dict[str, object]] = []
    for idx, left in enumerate(candidates):
        for right in candidates[idx + 1 :]:
            pairs.append(
                {
                    "pair_id": f"{left.get('candidate_id')}__{right.get('candidate_id')}",
                    "left": left,
                    "right": right,
                    "promotes_claims": False,
                }
            )

    return pairs
