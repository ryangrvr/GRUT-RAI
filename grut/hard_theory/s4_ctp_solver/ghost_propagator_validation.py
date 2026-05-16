"""Validation utilities for ghost propagator structure."""

from typing import Dict


def validate_ghost_propagator(record: Dict[str, object], operator: Dict[str, object]) -> Dict[str, object]:
    structure = str(operator.get("structure", ""))
    checks = {
        "laplacian_structure": "Box_g" in structure,
        "curvature_dependence": "R" in structure,
        "gauge_consistency_placeholder": operator.get("gauge") == "de_donder_placeholder",
        "index_structure_preserved": record.get("index_structure") == "vector",
        "no_scalar_reduction": record.get("index_structure") != "scalar",
    }

    status = "structural_validated" if all(checks.values()) else "fail"

    return {
        "validation": "ghost_s4",
        "status": status,
        "checks": checks,
        "promotes_claims": False,
    }
