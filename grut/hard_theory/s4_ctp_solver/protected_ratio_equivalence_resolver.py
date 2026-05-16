"""Resolve equivalence classes for protected symbolic ratios."""

from typing import Dict, List, Tuple

from grut.hard_theory.s4_ctp_solver.protected_ratio_equivalence_rules import (
    compare_ratio_equivalence,
    signature_for_ratio,
)


def _ratio_id(ratio: Dict[str, object]) -> str:
    ratio_id = ratio.get("ratio_id")
    if ratio_id:
        return str(ratio_id)
    pair = ratio.get("pair", {})
    left = pair.get("left", {})
    right = pair.get("right", {})
    return f"{left.get('candidate_id')}__{right.get('candidate_id')}"


def resolve_ratio_equivalence(
    ratios: List[Dict[str, object]],
) -> Dict[str, object]:
    classes: Dict[Tuple[object, ...], List[str]] = {}
    entries: List[Dict[str, object]] = []
    unresolved: List[Dict[str, object]] = []

    for ratio in ratios:
        ratio_id = _ratio_id(ratio)
        signature = signature_for_ratio(ratio)
        regulator_class = signature.get("regulator_class")
        if not regulator_class or regulator_class == "unknown":
            unresolved.append(
                {
                    "ratio_id": ratio_id,
                    "reason": "regulator_class_unknown",
                    "signature": signature,
                    "promotes_claims": False,
                }
            )
            continue

        key = (
            signature.get("source_family"),
            signature.get("kernel_family"),
            signature.get("nonlocal_form_class"),
            signature.get("regulator_class"),
            signature.get("numerator_role"),
            signature.get("denominator_role"),
        )
        classes.setdefault(key, []).append(ratio_id)
        entries.append(
            {
                "ratio_id": ratio_id,
                "signature": signature,
                "equivalence_class_id": str(key),
                "promotes_claims": False,
            }
        )

    class_summaries = [
        {
            "equivalence_class_id": str(key),
            "ratio_ids": ratio_ids,
            "count": len(ratio_ids),
            "promotes_claims": False,
        }
        for key, ratio_ids in classes.items()
    ]

    comparisons: List[Dict[str, object]] = []
    for i, left_ratio in enumerate(ratios):
        for right_ratio in ratios[i + 1 :]:
            result = compare_ratio_equivalence(left_ratio, right_ratio)
            comparisons.append(
                {
                    "left_ratio_id": _ratio_id(left_ratio),
                    "right_ratio_id": _ratio_id(right_ratio),
                    "status": result.get("status"),
                    "reason": result.get("reason"),
                    "promotes_claims": False,
                }
            )

    return {
        "equivalence_classes": class_summaries,
        "entries": entries,
        "comparisons": comparisons,
        "unresolved": unresolved,
        "promotes_claims": False,
    }
