"""Build a protected symbolic Euler-channel quotient."""

from typing import Dict, Optional


def _normalize_inputs(
    regulator_class: object,
    projection_domain: Optional[str],
) -> tuple[str, str]:
    if isinstance(regulator_class, dict) and projection_domain is None:
        return (
            "dimensional_regularization_symbolic_preserved",
            "round_s4_euler_channel",
        )

    return (str(regulator_class), projection_domain or "round_s4_euler_channel")


def build_symbolic_euler_quotient(
    regulator_class: object,
    projection_domain: Optional[str] = None,
) -> Dict[str, object]:
    regulator_class_value, projection_domain_value = _normalize_inputs(
        regulator_class,
        projection_domain,
    )
    return {
        "symbolic_ratio_id": "R_Euler_symbolic",
        "numerator_symbol": "C_Euler_num",
        "denominator_symbol": "C_Euler_den",
        "symbolic_form": "C_Euler_num / C_Euler_den",
        "numeric_value": None,
        "physical_value_claimed": False,
        "scheme_protected": True,
        "regulator_class": regulator_class_value,
        "projection_domain": projection_domain_value,
        "promotes_claims": False,
    }
