"""Symbolic construction of R from candidate pair."""

from typing import Dict


def build_symbolic_r(pair: Dict[str, object]) -> Dict[str, object]:
    numerator = pair.get("numerator", {})
    denominator = pair.get("denominator", {})

    return {
        "symbolic_ratio": "R_symbolic",
        "numerator": {
            "candidate_key": numerator.get("candidate_key"),
            "candidate_id": numerator.get("candidate_id"),
            "scheme_tags": numerator.get("renorm_structure_id"),
            "regulator": numerator.get("regulator_dependence_class"),
            "cancellation_ready": numerator.get("cancellation_ready", {}),
            "dimensionless": numerator.get("dimensionless"),
        },
        "denominator": {
            "candidate_key": denominator.get("candidate_key"),
            "candidate_id": denominator.get("candidate_id"),
            "scheme_tags": denominator.get("renorm_structure_id"),
            "regulator": denominator.get("regulator_dependence_class"),
            "cancellation_ready": denominator.get("cancellation_ready", {}),
            "dimensionless": denominator.get("dimensionless"),
        },
        "scheme_tags": pair.get("renorm_structure_shared"),
        "regulator_dependence": numerator.get("regulator_dependence_class"),
        "promotes_claims": False,
    }
