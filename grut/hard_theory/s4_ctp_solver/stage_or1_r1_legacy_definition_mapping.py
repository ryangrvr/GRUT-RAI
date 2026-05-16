"""Stage OR1-R1 legacy definition to protected kernel mapping."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.stage_or1_resolve_r_route import (
    run_stage_or1_resolve_r_route,
)
from grut.hard_theory.s4_ctp_solver.r_route_definition_history import (
    build_r_definition_history,
)
from grut.hard_theory.s4_ctp_solver.stage12a_coefficient_assembly_dry_run import (
    run_stage12a_coefficient_assembly_dry_run,
)
from grut.hard_theory.s4_ctp_solver.stage_p7_protected_scheme_injection import (
    run_stage_p7_protected_scheme_injection,
)
from grut.hard_theory.s4_ctp_solver.stage_p11_r2_equivalence_refresh import (
    run_stage_p11_r2_equivalence_refresh,
)
from grut.hard_theory.s4_ctp_solver.legacy_r_definition_mapper import (
    extract_legacy_definitions,
)
from grut.hard_theory.s4_ctp_solver.protected_kernel_role_assignment import (
    assign_protected_kernel_roles,
)
from grut.hard_theory.s4_ctp_solver.legacy_mapping_audit import (
    audit_legacy_definition_mapping,
)


def _map_roles(
    definition: Dict[str, object],
    role_assignments: Dict[str, object],
) -> Dict[str, object]:
    numerator_role = definition.get("numerator_role")
    denominator_role = definition.get("denominator_role")

    role_map = {
        "C_Final": role_assignments.get("c_final_candidates", []),
        "C_Cosmo": role_assignments.get("c_cosmo_candidates", []),
        "forward_anomaly": role_assignments.get("ctp_causal_candidates", []),
        "backward_anomaly": role_assignments.get("ctp_causal_candidates", []),
    }

    numerator_candidates = role_map.get(numerator_role, [])
    denominator_candidates = role_map.get(denominator_role, [])

    if numerator_role not in role_map:
        numerator_candidates = []
    if denominator_role not in role_map:
        denominator_candidates = []

    return {
        "numerator_candidates": numerator_candidates,
        "denominator_candidates": denominator_candidates,
    }


def _mapping_status(mapping: Dict[str, object], definition: Dict[str, object]) -> Dict[str, object]:
    numerator = mapping.get("numerator_candidates", [])
    denominator = mapping.get("denominator_candidates", [])

    if numerator and denominator:
        return {"mapping_status": "complete", "blocking_reason": None}

    if not numerator and not denominator:
        return {
            "mapping_status": "blocked",
            "blocking_reason": "no_mapped_candidates",
        }

    numerator_role = definition.get("numerator_role")
    denominator_role = definition.get("denominator_role")

    if numerator_role == "C_Cosmo" or denominator_role == "C_Cosmo":
        return {
            "mapping_status": "blocked",
            "blocking_reason": "c_cosmo_mapping_missing",
        }

    if not numerator:
        return {
            "mapping_status": "partial",
            "blocking_reason": "missing_numerator_mapping",
        }

    return {
        "mapping_status": "partial",
        "blocking_reason": "missing_denominator_mapping",
    }


def run_stage_or1_r1_legacy_definition_mapping() -> Dict[str, object]:
    or1_report = run_stage_or1_resolve_r_route()
    definition_history = build_r_definition_history()
    stage12a = run_stage12a_coefficient_assembly_dry_run()
    stage_p7 = run_stage_p7_protected_scheme_injection()
    stage_p11_r2 = run_stage_p11_r2_equivalence_refresh()

    legacy_definitions = extract_legacy_definitions(definition_history)
    role_assignments = assign_protected_kernel_roles(stage_p7, stage12a)

    mapped_routes: List[Dict[str, object]] = []
    blocked_routes: List[Dict[str, object]] = []

    for definition in legacy_definitions:
        mapping = _map_roles(definition, role_assignments)
        status = _mapping_status(mapping, definition)

        record = {
            "legacy_definition": definition.get("legacy_definition"),
            "numerator_role": definition.get("numerator_role"),
            "denominator_role": definition.get("denominator_role"),
            "mapped_numerator_candidates": mapping.get("numerator_candidates", []),
            "mapped_denominator_candidates": mapping.get("denominator_candidates", []),
            "mapping_status": status.get("mapping_status"),
            "blocking_reason": status.get("blocking_reason"),
            "manual_selection": False,
            "promotes_claims": False,
        }

        if record["mapping_status"] == "complete":
            mapped_routes.append(record)
        else:
            blocked_routes.append(record)

    mapping_complete = bool(mapped_routes)
    audit = audit_legacy_definition_mapping(mapped_routes, blocked_routes, role_assignments)

    return {
        "stage": "OR1-R1",
        "status": "legacy_definition_mapping",
        "mapping_complete": mapping_complete,
        "mapped_routes": mapped_routes,
        "blocked_routes": blocked_routes,
        "unique_route_selected": False,
        "can_rerun_or1": mapping_complete,
        "can_compute_numeric_r": False,
        "can_claim_r": False,
        "promotes_claims": False,
        "audit": audit,
        "legacy_definitions": legacy_definitions,
        "role_assignments": role_assignments,
        "stage_or1": or1_report,
        "stage12a": stage12a,
        "stage_p7": stage_p7,
        "stage_p11_r2": stage_p11_r2,
    }
