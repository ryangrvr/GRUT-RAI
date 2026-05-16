"""Rules for protected quotient equivalence resolution."""

from typing import Dict


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


def compare_ratio_equivalence(
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

    if left_sig.get("source_family") != right_sig.get("source_family"):
        return {
            "status": "inequivalent",
            "reason": "source_family_mismatch",
            "promotes_claims": False,
        }

    if left_sig.get("kernel_family") != right_sig.get("kernel_family"):
        return {
            "status": "inequivalent",
            "reason": "kernel_family_mismatch",
            "promotes_claims": False,
        }

    if left_sig.get("nonlocal_form_class") != right_sig.get("nonlocal_form_class"):
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


def signature_for_ratio(ratio: Dict[str, object]) -> Dict[str, object]:
    return _pair_signature(ratio.get("pair", {}))
