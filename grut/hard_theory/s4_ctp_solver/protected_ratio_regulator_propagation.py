"""Propagate resolved regulator classes into symbolic ratios."""

from typing import Dict, List


def _ratio_id(pair: Dict[str, object]) -> str:
    pair_id = pair.get("pair_id")
    if pair_id:
        return str(pair_id)
    left = pair.get("left", {})
    right = pair.get("right", {})
    return f"{left.get('candidate_id')}__{right.get('candidate_id')}"


def propagate_ratio_regulator_classes(
    symbolic_ratios: List[Dict[str, object]],
    ratio_regulator_classes: List[Dict[str, object]],
) -> List[Dict[str, object]]:
    ratio_map = {
        entry.get("ratio_id"): entry for entry in ratio_regulator_classes
    }

    refreshed: List[Dict[str, object]] = []
    for ratio in symbolic_ratios:
        pair = ratio.get("pair", {})
        left = dict(pair.get("left", {}))
        right = dict(pair.get("right", {}))
        ratio_id = _ratio_id(pair)
        regulator_info = ratio_map.get(ratio_id, {})

        numerator_class = regulator_info.get("numerator_regulator_class")
        denominator_class = regulator_info.get("denominator_regulator_class")
        ratio_regulator_class = regulator_info.get("ratio_regulator_class")

        if left.get("regulator_class") in (None, "unknown") and numerator_class:
            left["regulator_class"] = numerator_class
        if right.get("regulator_class") in (None, "unknown") and denominator_class:
            right["regulator_class"] = denominator_class

        updated_pair = {
            **pair,
            "left": left,
            "right": right,
        }

        refreshed.append(
            {
                **ratio,
                "pair": updated_pair,
                "ratio_regulator_class": ratio_regulator_class,
                "promotes_claims": False,
            }
        )

    return refreshed
