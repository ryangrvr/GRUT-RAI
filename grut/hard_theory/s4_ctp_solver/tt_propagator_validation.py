"""Validation checks for TT propagator scaffold (structural)."""

from typing import Dict


def validate_tt_scaffold(
    scaffold: Dict[str, object],
    operator: Dict[str, object],
    projector: Dict[str, object],
) -> Dict[str, object]:
    structure = scaffold.get("structure", "")
    properties = projector.get("properties", [])
    operator_structure = str(operator.get("structure", ""))

    checks = {
        "projector_applied": "P_TT" in structure,
        "transverse_property": "transverse" in properties,
        "traceless_property": "traceless" in properties,
        "no_scalar_reduction": operator.get("type") == "rank_2_tensor",
        "lichnerowicz_structure": "Box_g" in operator_structure,
    }

    status = "structural_validated" if all(checks.values()) else "fail"

    return {
        "validation": "tt_scaffold",
        "status": status,
        "checks": checks,
        "promotes_claims": False,
    }
