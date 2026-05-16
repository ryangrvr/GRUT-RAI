"""Omni stage OR1 for resolving the protected R route end-to-end."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.stage12g_r_route_terminal_audit import (
    run_stage12g_r_route_terminal_audit,
)
from grut.hard_theory.s4_ctp_solver.stage12c_r1_legality_repair import (
    run_stage12c_r1_legality_repair,
)
from grut.hard_theory.s4_ctp_solver.stage12c_r2_metadata_completion import (
    run_stage12c_r2_metadata_completion,
)
from grut.hard_theory.s4_ctp_solver.stage12c_r3_complete_missing_metadata import (
    run_stage12c_r3_complete_missing_metadata,
)
from grut.hard_theory.s4_ctp_solver.stage12c_r4_rerun_legality_after_metadata import (
    run_stage12c_r4_rerun_legality_after_metadata,
)
from grut.hard_theory.s4_ctp_solver.stage12c_r5_protected_source_audit import (
    run_stage12c_r5_protected_source_audit,
)
from grut.hard_theory.s4_ctp_solver.stage_p1_nonlocal_anomaly_source_plan import (
    run_stage_p1_nonlocal_anomaly_source_plan,
)
from grut.hard_theory.s4_ctp_solver.stage_p2_nonlocal_anomaly_kernel_attempt import (
    run_stage_p2_nonlocal_anomaly_kernel_attempt,
)
from grut.hard_theory.s4_ctp_solver.stage_p2_nonlocal_kernel_derivation import (
    run_stage_p2_nonlocal_kernel_derivation,
)
from grut.hard_theory.s4_ctp_solver.stage_p3_nonlocal_form_construction import (
    run_stage_p3_nonlocal_form_construction,
)
from grut.hard_theory.s4_ctp_solver.stage_p4_protected_kernel_integration import (
    run_stage_p4_protected_kernel_integration,
)
from grut.hard_theory.s4_ctp_solver.stage_p11_r3_selection_rule_audit import (
    run_stage_p11_r3_selection_rule_audit,
)
from grut.hard_theory.s4_ctp_solver.r_route_definition_history import (
    build_r_definition_history,
)
from grut.hard_theory.s4_ctp_solver.r_selection_principle_audit import (
    build_r_selection_principle_audit,
)
from grut.hard_theory.s4_ctp_solver.r_route_degeneracy_resolution import (
    resolve_r_route_degeneracy,
)
from grut.hard_theory.s4_ctp_solver.r_route_decision_report import (
    build_r_route_decision_report,
)


def _collect_ratios(stage_p11_r3: Dict[str, object]) -> List[Dict[str, object]]:
    stage_p11_r2 = stage_p11_r3.get("stage_p11_r2", {})
    ratios = stage_p11_r2.get("refreshed_ratios", [])
    return list(ratios)


def _selection_report(stage_p11_r3: Dict[str, object]) -> Dict[str, object]:
    return {
        "selection_rule_found": stage_p11_r3.get("selection_rule_found") is True,
        "selected_ratio_ids": [
            ratio_id
            for ratio_id in [stage_p11_r3.get("selected_ratio_id")]
            if ratio_id
        ],
    }


def run_stage_or1_resolve_r_route() -> Dict[str, object]:
    stage12g = run_stage12g_r_route_terminal_audit()
    stage12c_r1 = run_stage12c_r1_legality_repair()
    stage12c_r2 = run_stage12c_r2_metadata_completion()
    stage12c_r3 = run_stage12c_r3_complete_missing_metadata()
    stage12c_r4 = run_stage12c_r4_rerun_legality_after_metadata()
    stage12c_r5 = run_stage12c_r5_protected_source_audit()

    stage_p1 = run_stage_p1_nonlocal_anomaly_source_plan()
    stage_p2_attempt = run_stage_p2_nonlocal_anomaly_kernel_attempt()
    stage_p2_derivation = run_stage_p2_nonlocal_kernel_derivation()
    stage_p3 = run_stage_p3_nonlocal_form_construction()
    stage_p4 = run_stage_p4_protected_kernel_integration()

    stage_p11_r3 = run_stage_p11_r3_selection_rule_audit()
    stage_p11_r2 = stage_p11_r3.get("stage_p11_r2", {})
    stage_p11_r1 = stage_p11_r2.get("stage_p11_r1", {})
    stage_p10 = stage_p11_r2.get("stage_p10", {})
    stage_p9 = stage_p10.get("stage_p9", {})
    stage_p8 = stage_p10.get("stage_p8", {})
    stage_p7 = stage_p10.get("stage_p7", {})
    stage_p5 = stage_p10.get("stage_p5", {})

    ratios = _collect_ratios(stage_p11_r3)
    definition_history = build_r_definition_history()
    selection_report = _selection_report(stage_p11_r3)

    selection_audit = build_r_selection_principle_audit(
        ratios,
        definition_history,
        selection_report,
    )
    degeneracy = resolve_r_route_degeneracy(
        selection_audit,
        definition_history,
        stage_p11_r2,
    )
    decision_report = build_r_route_decision_report(
        definition_history,
        selection_audit,
        degeneracy,
    )

    return {
        **decision_report,
        "status": decision_report.get("status"),
        "r_definition_history": definition_history,
        "selection_audit": selection_audit,
        "degeneracy_resolution": degeneracy,
        "stage12g": stage12g,
        "stage12c_r1": stage12c_r1,
        "stage12c_r2": stage12c_r2,
        "stage12c_r3": stage12c_r3,
        "stage12c_r4": stage12c_r4,
        "stage12c_r5": stage12c_r5,
        "stage_p1": stage_p1,
        "stage_p2_attempt": stage_p2_attempt,
        "stage_p2_derivation": stage_p2_derivation,
        "stage_p3": stage_p3,
        "stage_p4": stage_p4,
        "stage_p5": stage_p5,
        "stage_p7": stage_p7,
        "stage_p8": stage_p8,
        "stage_p9": stage_p9,
        "stage_p10": stage_p10,
        "stage_p11_r1": stage_p11_r1,
        "stage_p11_r2": stage_p11_r2,
        "stage_p11_r3": stage_p11_r3,
        "can_compute_numeric_r": False,
        "can_claim_r": False,
        "promotes_claims": False,
    }
