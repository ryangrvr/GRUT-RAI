"""Uniqueness analysis for protected symbolic ratios."""

from typing import Dict, List


def analyze_ratio_uniqueness(
    valid_ratios: List[Dict[str, object]],
    degeneracy_report: Dict[str, object],
) -> Dict[str, object]:
    classes = degeneracy_report.get("classes", [])

    if not valid_ratios:
        return {
            "unique_ratio_exists": False,
            "equivalence_class": None,
            "representative_ratio_id": None,
            "degeneracy_count": 0,
            "reason": "no_valid_quotient",
            "promotes_claims": False,
        }

    if len(classes) == 1:
        ratio_ids = classes[0].get("ratio_ids", [])
        representative = ratio_ids[0] if ratio_ids else valid_ratios[0].get("ratio_id")
        reason = "unique_equivalence_class"
        if len(ratio_ids) > 1:
            reason = "multiple_equivalent_quotients"
        return {
            "unique_ratio_exists": True,
            "equivalence_class": classes[0].get("equivalence_class_id"),
            "representative_ratio_id": representative,
            "degeneracy_count": classes[0].get("count", len(ratio_ids)),
            "reason": reason,
            "promotes_claims": False,
        }

    return {
        "unique_ratio_exists": False,
        "equivalence_class": None,
        "representative_ratio_id": None,
        "degeneracy_count": len(classes),
        "reason": "multiple_inequivalent_quotients",
        "promotes_claims": False,
    }
