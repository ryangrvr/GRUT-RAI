"""Degeneracy analysis for protected symbolic ratios."""

from typing import Dict, List, Tuple


def _nonlocal_form_class(source_type: object) -> str:
    text = str(source_type or "").lower()
    if "im_log" in text:
        return "im_log"
    if "weyl_log" in text:
        return "weyl_log"
    if "r_log" in text:
        return "r_log"
    return "unknown"


def _kernel_family(source_type: object) -> str:
    text = str(source_type or "").lower()
    if "weyl" in text:
        return "weyl"
    if "r_log" in text or "r_" in text:
        return "r"
    if "im_log" in text:
        return "im"
    return "unknown"


def _signature(pair: Dict[str, object]) -> Dict[str, object]:
    left = pair.get("left", {})
    right = pair.get("right", {})

    return {
        "source_family": (left.get("source_family"), right.get("source_family")),
        "kernel_family": (
            _kernel_family(left.get("source_type")),
            _kernel_family(right.get("source_type")),
        ),
        "regulator_class": left.get("regulator_class"),
        "nonlocal_form_class": (
            _nonlocal_form_class(left.get("source_type")),
            _nonlocal_form_class(right.get("source_type")),
        ),
        "numerator_role": left.get("source_type"),
        "denominator_role": right.get("source_type"),
        "cancellation_pattern": (
            bool(left.get("counterterm_nonmixing_verified"))
            and bool(left.get("finite_extractability")),
            bool(right.get("counterterm_nonmixing_verified"))
            and bool(right.get("finite_extractability")),
        ),
    }


def _signature_key(signature: Dict[str, object]) -> Tuple[object, ...]:
    return (
        signature.get("source_family"),
        signature.get("kernel_family"),
        signature.get("regulator_class"),
        signature.get("nonlocal_form_class"),
        signature.get("numerator_role"),
        signature.get("denominator_role"),
        signature.get("cancellation_pattern"),
    )


def analyze_ratio_degeneracy(valid_ratios: List[Dict[str, object]]) -> Dict[str, object]:
    entries: List[Dict[str, object]] = []
    classes: Dict[Tuple[object, ...], List[str]] = {}

    for ratio in valid_ratios:
        pair = ratio.get("pair", {})
        signature = _signature(pair)
        key = _signature_key(signature)
        ratio_id = ratio.get("ratio_id")
        entries.append(
            {
                "ratio_id": ratio_id,
                "signature": signature,
                "equivalence_class_id": str(key),
                "promotes_claims": False,
            }
        )
        classes.setdefault(key, []).append(ratio_id)

    class_summaries = [
        {
            "equivalence_class_id": str(key),
            "ratio_ids": ids,
            "count": len(ids),
            "promotes_claims": False,
        }
        for key, ids in classes.items()
    ]

    return {
        "degeneracy_count": len(class_summaries),
        "classes": class_summaries,
        "entries": entries,
        "promotes_claims": False,
    }
