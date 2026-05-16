"""Refresh equivalence resolution with propagated regulator classes."""

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


def _trace_weyl_compatible(left: Dict[str, object], right: Dict[str, object]) -> bool:
    families = {_kernel_family(left.get("source_type")), _kernel_family(right.get("source_type"))}
    return families == {"r", "weyl"}


def _symbolic_projection_compatible(left: Dict[str, object], right: Dict[str, object]) -> bool:
    return (
        left.get("source_family") == right.get("source_family")
        and left.get("scheme_protected") is True
        and right.get("scheme_protected") is True
    )


def _pair_signature(pair: Dict[str, object]) -> Dict[str, object]:
    left = pair.get("left", {})
    right = pair.get("right", {})
    return {
        "source_family": (left.get("source_family"), right.get("source_family")),
        "kernel_family": (
            _kernel_family(left.get("source_type")),
            _kernel_family(right.get("source_type")),
        ),
        "nonlocal_form_class": (
            _nonlocal_form_class(left.get("source_type")),
            _nonlocal_form_class(right.get("source_type")),
        ),
        "regulator_class": left.get("regulator_class"),
        "numerator_role": left.get("source_type"),
        "denominator_role": right.get("source_type"),
    }


def _ratio_id(ratio: Dict[str, object]) -> str:
    ratio_id = ratio.get("ratio_id")
    if ratio_id:
        return str(ratio_id)
    pair = ratio.get("pair", {})
    left = pair.get("left", {})
    right = pair.get("right", {})
    return f"{left.get('candidate_id')}__{right.get('candidate_id')}"


def compare_refreshed_equivalence(
    left_ratio: Dict[str, object],
    right_ratio: Dict[str, object],
) -> Dict[str, object]:
    left_pair = left_ratio.get("pair", {})
    right_pair = right_ratio.get("pair", {})

    left_sig = _pair_signature(left_pair)
    right_sig = _pair_signature(right_pair)

    left_reg = left_sig.get("regulator_class")
    right_reg = right_sig.get("regulator_class")

    if not left_reg or not right_reg or left_reg == "unknown" or right_reg == "unknown":
        return {
            "status": "undetermined",
            "reason": "regulator_class_unknown",
            "promotes_claims": False,
        }

    left_pair_data = left_pair.get("left", {})
    right_pair_data = left_pair.get("right", {})
    compare_left = right_pair.get("left", {})
    compare_right = right_pair.get("right", {})

    if not _symbolic_projection_compatible(left_pair_data, right_pair_data):
        return {
            "status": "inequivalent",
            "reason": "symbolic_projection_incompatible",
            "promotes_claims": False,
        }

    if not _symbolic_projection_compatible(compare_left, compare_right):
        return {
            "status": "inequivalent",
            "reason": "symbolic_projection_incompatible",
            "promotes_claims": False,
        }

    if left_sig.get("source_family") != right_sig.get("source_family"):
        return {
            "status": "inequivalent",
            "reason": "source_family_mismatch",
            "promotes_claims": False,
        }

    if left_sig.get("kernel_family") != right_sig.get("kernel_family"):
        if not _trace_weyl_compatible(left_pair_data, right_pair_data):
            return {
                "status": "inequivalent",
                "reason": "kernel_family_mismatch",
                "promotes_claims": False,
            }

    if left_sig.get("nonlocal_form_class") != right_sig.get("nonlocal_form_class"):
        if not _trace_weyl_compatible(left_pair_data, right_pair_data):
            return {
                "status": "inequivalent",
                "reason": "nonlocal_form_class_mismatch",
                "promotes_claims": False,
            }

    if left_sig.get("numerator_role") != right_sig.get("numerator_role"):
        return {
            "status": "inequivalent",
            "reason": "numerator_role_mismatch",
            "promotes_claims": False,
        }

    if left_sig.get("denominator_role") != right_sig.get("denominator_role"):
        return {
            "status": "inequivalent",
            "reason": "denominator_role_mismatch",
            "promotes_claims": False,
        }

    if left_reg != right_reg:
        return {
            "status": "inequivalent",
            "reason": "regulator_class_mismatch",
            "promotes_claims": False,
        }

    return {
        "status": "equivalent",
        "reason": "equivalence_signature_match",
        "promotes_claims": False,
    }


def refresh_ratio_equivalence(ratios: List[Dict[str, object]]) -> Dict[str, object]:
    classes: Dict[Tuple[object, ...], List[str]] = {}
    entries: List[Dict[str, object]] = []
    unresolved: List[Dict[str, object]] = []

    for ratio in ratios:
        ratio_id = _ratio_id(ratio)
        signature = _pair_signature(ratio.get("pair", {}))
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
            result = compare_refreshed_equivalence(left_ratio, right_ratio)
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
