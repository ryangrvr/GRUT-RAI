"""Isolate symbolic finite structure for R."""

from typing import Dict


def isolate_r_finite_structure(cancellation: Dict[str, object]) -> Dict[str, object]:
    if cancellation.get("cancellation_valid") is not True:
        return {
            "finite_structure": None,
            "isolation_ok": False,
            "reason": "cancellation_not_valid",
            "promotes_claims": False,
        }

    return {
        "finite_structure": "R_finite_symbolic",
        "isolation_ok": True,
        "reason": "finite_structure_isolated",
        "promotes_claims": False,
    }
