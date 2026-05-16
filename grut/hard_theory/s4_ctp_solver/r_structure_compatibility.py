"""Check structural compatibility of candidate coefficient pairs."""

from typing import Dict


def check_r_structure_compatibility(pair: Dict[str, object]) -> Dict[str, object]:
    numerator = pair.get("numerator", {})
    denominator = pair.get("denominator", {})

    def _get(field: str) -> object:
        return numerator.get(field), denominator.get(field)

    tensor_origin = _get("tensor_origin_class")
    if not tensor_origin[0] or not tensor_origin[1]:
        return {
            "compatible": False,
            "reason": "missing_tensor_origin_class",
            "promotes_claims": False,
        }
    if tensor_origin[0] != tensor_origin[1]:
        return {
            "compatible": False,
            "reason": "tensor_origin_mismatch",
            "promotes_claims": False,
        }

    loop_order = _get("loop_order")
    if loop_order[0] is None or loop_order[1] is None:
        return {
            "compatible": False,
            "reason": "missing_loop_order",
            "promotes_claims": False,
        }
    if loop_order[0] != loop_order[1]:
        return {
            "compatible": False,
            "reason": "loop_order_mismatch",
            "promotes_claims": False,
        }

    regulator_dependence = _get("regulator_dependence_class")
    if not regulator_dependence[0] or not regulator_dependence[1]:
        return {
            "compatible": False,
            "reason": "missing_regulator_dependence",
            "promotes_claims": False,
        }
    if regulator_dependence[0] != regulator_dependence[1]:
        return {
            "compatible": False,
            "reason": "regulator_dependence_mismatch",
            "promotes_claims": False,
        }

    if numerator.get("counterterm_contamination") or denominator.get(
        "counterterm_contamination"
    ):
        return {
            "compatible": False,
            "reason": "counterterm_contamination",
            "promotes_claims": False,
        }

    return {
        "compatible": True,
        "reason": "structure_compatible",
        "promotes_claims": False,
    }
