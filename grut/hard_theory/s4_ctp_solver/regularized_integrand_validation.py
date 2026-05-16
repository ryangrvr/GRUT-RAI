"""Validation for regularized integrand scaffold."""

from typing import Dict, List


def validate_regularized_integrand(result: Dict[str, object]) -> Dict[str, object]:
    issues: List[str] = []

    scheme = result.get("scheme")
    if not scheme:
        issues.append("missing_regulator_scheme")

    if not result.get("regulator_factor"):
        issues.append("missing_regulator_factor")

    if not result.get("divergence_tags"):
        issues.append("missing_divergence_tags")

    if result.get("integration_performed") is not False:
        issues.append("integration_performed")

    if result.get("amplitude_computed") is not False:
        issues.append("amplitude_computed")

    if result.get("finite_part_computed") is not False:
        issues.append("finite_part_computed")

    status = "valid_regularized_scaffold" if not issues else "invalid_regularized_scaffold"

    return {
        "validation": "regularized_integrand",
        "status": status,
        "issues": issues,
        "promotes_claims": False,
    }
