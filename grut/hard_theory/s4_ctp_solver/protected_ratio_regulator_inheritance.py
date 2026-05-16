"""Assign regulator class to protected symbolic ratios."""

from typing import Dict, List


def _ratio_id(pair: Dict[str, object]) -> str:
    pair_id = pair.get("pair_id")
    if pair_id:
        return str(pair_id)
    left = pair.get("left", {})
    right = pair.get("right", {})
    return f"{left.get('candidate_id')}__{right.get('candidate_id')}"


def assign_ratio_regulator_classes(
    symbolic_entries: List[Dict[str, object]],
    kernel_regulator_classes: List[Dict[str, object]],
) -> List[Dict[str, object]]:
    kernel_map = {
        entry.get("source_type"): entry.get("regulator_class")
        for entry in kernel_regulator_classes
    }

    ratio_classes: List[Dict[str, object]] = []
    for entry in symbolic_entries:
        pair = entry.get("pair", {})
        left = pair.get("left", {})
        right = pair.get("right", {})

        numerator_class = kernel_map.get(
            left.get("source_type"), "regulator_class_unresolved"
        )
        denominator_class = kernel_map.get(
            right.get("source_type"), "regulator_class_unresolved"
        )

        if (
            numerator_class == "dimensional_regularization_symbolic_preserved"
            and denominator_class == "dimensional_regularization_symbolic_preserved"
        ):
            ratio_class = "matched_dimensional_symbolic_preserved"
        else:
            ratio_class = "regulator_mismatch_or_unresolved"

        ratio_classes.append(
            {
                "ratio_id": _ratio_id(pair),
                "numerator_regulator_class": numerator_class,
                "denominator_regulator_class": denominator_class,
                "ratio_regulator_class": ratio_class,
                "promotes_claims": False,
            }
        )

    return ratio_classes
