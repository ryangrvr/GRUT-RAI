"""Audit for loop integration dry-run plan."""

from typing import Dict


def audit_integration_dry_run(plan: Dict[str, object]) -> Dict[str, object]:
    variables = plan.get("variables") or {}
    domain = plan.get("domain") or {}
    ordering = plan.get("ordering") or {}
    regulator = plan.get("regulator_handling") or {}

    variables_ok = bool(variables.get("variables"))
    domain_ok = domain.get("status") == "domain_defined_symbolic"
    ordering_ok = ordering.get("status") == "ordering_defined"
    regulator_ok = regulator.get("status") == "regulator_strategy_defined"

    no_integration = plan.get("integration_performed") is False
    no_amplitude = plan.get("amplitude_computed") is False
    no_finite_parts = plan.get("finite_part_computed") is False
    no_extraction = plan.get("extraction_performed") is False
    no_r_extract = plan.get("r_extracted") is False

    guard = plan.get("guard", {})
    guard_ok = guard.get("guard") == "tensor_placeholder_guard"

    all_defined = all([variables_ok, domain_ok, ordering_ok, regulator_ok])
    status = (
        "valid"
        if all(
            [
                all_defined,
                no_integration,
                no_amplitude,
                no_finite_parts,
                no_extraction,
                no_r_extract,
                guard_ok,
            ]
        )
        else "invalid"
    )

    return {
        "audit": "integration_dry_run",
        "status": status,
        "can_advance_to_controlled_integration": all_defined,
        "can_compute_finite_parts": False,
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
    }
