"""Classify injected protected source candidates for scheme stability."""

from __future__ import annotations

from typing import Dict, List


def classify_protected_scheme_candidates(
    injected: List[Dict[str, object]],
    rules: Dict[str, object],
) -> Dict[str, object]:
    classifications: List[Dict[str, object]] = []

    for candidate in injected:
        eligible = (
            candidate.get("locality_class") == "nonlocal"
            and candidate.get("invariant_class")
            == "anomaly_protected_nonlocal_kernel"
            and candidate.get("counterterm_nonmixing_verified") is True
            and candidate.get("finite_extractability") is True
            and candidate.get("coefficient_value") is None
        )

        classification = "scheme_protected" if eligible else "scheme_fragile"
        reason = "nonlocal_anomaly_candidate" if eligible else "ineligible_nonlocal"
        candidate_key = (
            "nonlocal_scheme_protected_candidate" if eligible else "scheme_fragile_candidate"
        )

        classifications.append(
            {
                "candidate_key": candidate_key,
                "candidate_id": candidate.get("candidate_id"),
                "classification": classification,
                "reason": reason,
                "source_partitions": [],
                "promotes_claims": False,
            }
        )

    return {
        "classifications": classifications,
        "rules_id": rules.get("rules_id"),
        "promotes_claims": False,
    }
