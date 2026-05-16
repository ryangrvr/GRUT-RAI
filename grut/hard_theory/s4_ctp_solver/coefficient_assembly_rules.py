"""Define coefficient assembly rules (dry-run only)."""

from typing import Dict


def define_coefficient_assembly_rules() -> Dict[str, object]:
    return {
        "rules_id": "coefficient_assembly_rules_v1",
        "physical_coefficients_allowed": False,
        "r_extraction_allowed": False,
        "promotes_claims": False,
    }
