"""Stage OR4 formal R definition document and gate."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.r_formal_definition import (
    build_formal_r_definition,
)
from grut.hard_theory.s4_ctp_solver.r_definition_gate import (
    evaluate_formal_r_definition_gate,
)
from grut.hard_theory.s4_ctp_solver.stage_or3_s4_euler_anomaly_projection import (
    run_stage_or3_s4_euler_anomaly_projection,
)
from grut.hard_theory.s4_ctp_solver.stage_or1_resolve_r_route import (
    run_stage_or1_resolve_r_route,
)
from grut.hard_theory.s4_ctp_solver.stage_or1_r1_legacy_definition_mapping import (
    run_stage_or1_r1_legacy_definition_mapping,
)
from grut.hard_theory.s4_ctp_solver.stage_or2_physical_interpretation_constraint import (
    run_stage_or2_physical_interpretation_constraint,
)
from grut.hard_theory.s4_ctp_solver.stage_p11_r2_equivalence_refresh import (
    run_stage_p11_r2_equivalence_refresh,
)
from grut.hard_theory.s4_ctp_solver.stage_p7_protected_scheme_injection import (
    run_stage_p7_protected_scheme_injection,
)


def run_stage_or4_formal_r_definition_gate() -> Dict[str, object]:
    or3_report = run_stage_or3_s4_euler_anomaly_projection()
    or1_report = run_stage_or1_resolve_r_route()
    or1_r1_report = run_stage_or1_r1_legacy_definition_mapping()
    or2_report = run_stage_or2_physical_interpretation_constraint()
    stage_p11_r2 = run_stage_p11_r2_equivalence_refresh()
    stage_p7 = run_stage_p7_protected_scheme_injection()

    formal_definition = build_formal_r_definition()
    gate = evaluate_formal_r_definition_gate(formal_definition, or3_report)

    return {
        "stage": "OR4",
        "status": "formal_r_definition_gate",
        "r_definition_written": True,
        "definition_domain": gate.get("definition_domain"),
        "allowed_kernel_roles": gate.get("allowed_kernel_roles"),
        "blocked_kernel_roles": gate.get("blocked_kernel_roles"),
        "can_advance_to_euler_coefficient_symbol_binding": gate.get(
            "can_advance_to_euler_coefficient_symbol_binding"
        ),
        "can_compute_numeric_r": False,
        "can_claim_r": False,
        "promotes_claims": False,
        "formal_definition": formal_definition,
        "stage_or3": or3_report,
        "stage_or1": or1_report,
        "stage_or1_r1": or1_r1_report,
        "stage_or2": or2_report,
        "stage_p11_r2": stage_p11_r2,
        "stage_p7": stage_p7,
    }
