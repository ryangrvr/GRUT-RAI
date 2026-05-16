"""Validation for loop-integrand scaffold."""

from typing import Dict, List


ALLOWED_PROPAGATOR_STATUS = {"symbolic_only", "scaffold_not_evaluated"}


def validate_loop_integrand_scaffold(integrand: Dict[str, object]) -> Dict[str, object]:
    issues: List[str] = []
    components = integrand.get("components", {})

    if not components.get("propagators"):
        issues.append("missing_propagators")
    if not components.get("vertices"):
        issues.append("missing_vertices")
    if not components.get("index_flow"):
        issues.append("missing_index_flow")
    if not components.get("symmetry_factor"):
        issues.append("missing_symmetry_factor")
    if not components.get("regulator"):
        issues.append("missing_regulator")
    if not components.get("scheme"):
        issues.append("missing_scheme")
    if not components.get("loop_variables"):
        issues.append("missing_loop_variables")

    vertices = components.get("vertices", [])
    if any(vertex.get("placeholder") is not True for vertex in vertices):
        issues.append("vertex_not_placeholder")

    propagators = components.get("propagators", [])
    for propagator in propagators:
        status = propagator.get("evaluation_status")
        if status not in ALLOWED_PROPAGATOR_STATUS:
            issues.append("propagator_not_symbolic")
            break

    if integrand.get("integration_performed") is not False:
        issues.append("integration_performed")
    if integrand.get("propagators_evaluated") is not False:
        issues.append("propagators_evaluated")
    if integrand.get("amplitude_computed") is not False:
        issues.append("amplitude_computed")
    if integrand.get("finite_part_computed") is not False:
        issues.append("finite_part_computed")

    status = "valid_integrand_scaffold" if not issues else "invalid_integrand_scaffold"

    return {
        "validation": "loop_integrand_scaffold",
        "status": status,
        "issues": issues,
        "promotes_claims": False,
    }
