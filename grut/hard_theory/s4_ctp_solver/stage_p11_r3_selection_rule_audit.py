"""Stage P11-R3 protected quotient selection rule audit."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.stage_p11_r2_equivalence_refresh import (
    run_stage_p11_r2_equivalence_refresh,
)
from grut.hard_theory.s4_ctp_solver.stageN2_imaginary_causal_sector_audit import (
    run_stageN2_imaginary_causal_sector_audit,
)
from grut.hard_theory.s4_ctp_solver.stage_p5_counterterm_finite_readiness import (
    run_stage_p5_counterterm_finite_readiness,
)
from grut.hard_theory.s4_ctp_solver.stage_p7_protected_scheme_injection import (
    run_stage_p7_protected_scheme_injection,
)
from grut.hard_theory.s4_ctp_solver.stage_p8_r_legality_with_protected_kernels import (
    run_stage_p8_r_legality_with_protected_kernels,
)
from grut.hard_theory.s4_ctp_solver.protected_quotient_selection_rules import (
    evaluate_selection_rules,
    collect_ratio_ids,
)
from grut.hard_theory.s4_ctp_solver.protected_quotient_selection_report import (
    assemble_selection_report,
)
from grut.hard_theory.s4_ctp_solver.protected_quotient_selection_audit import (
    audit_selection_rules,
)


def _collect_ratios(stage_p11_r2: Dict[str, object]) -> List[Dict[str, object]]:
    return stage_p11_r2.get("refreshed_ratios", [])


def _build_assumptions(stage_n2: Dict[str, object]) -> Dict[str, object]:
    assumptions = dict(stage_n2.get("assumptions", {}) or {})
    if "ctp_causal_priority" not in assumptions:
        assumptions["ctp_causal_priority"] = stage_n2.get("protected_sources_found", 0) > 0
    if "imaginary_real_bridge" not in assumptions:
        assumptions["imaginary_real_bridge"] = bool(
            stage_n2.get("ctp_to_curvature_projection")
        )
    if "curvature_sector_target" not in assumptions:
        assumptions["curvature_sector_target"] = False
    if "r_definition" not in assumptions:
        assumptions["r_definition"] = stage_n2.get("r_definition")
    return assumptions


def run_stage_p11_r3_selection_rule_audit() -> Dict[str, object]:
    stage_p11_r2 = run_stage_p11_r2_equivalence_refresh()
    stage_n2 = run_stageN2_imaginary_causal_sector_audit()
    stage_p5 = run_stage_p5_counterterm_finite_readiness()
    stage_p7 = run_stage_p7_protected_scheme_injection()
    stage_p8 = run_stage_p8_r_legality_with_protected_kernels()

    ratios = _collect_ratios(stage_p11_r2)
    assumptions = _build_assumptions(stage_n2)

    rule_reports = evaluate_selection_rules(ratios, assumptions)
    selection_report = assemble_selection_report(ratios, rule_reports)
    audit = audit_selection_rules(ratios, rule_reports)

    selection_rule_found = selection_report.get("selection_rule_found") is True
    selected_ratio_id = selection_report.get("selected_ratio_id")

    return {
        "stage": "P11-R3",
        "status": "protected_quotient_selection_rule_audit",
        "selection_rule_found": selection_rule_found,
        "selected_ratio_id": selected_ratio_id,
        "unresolved_ratio_ids": selection_report.get("unresolved_ratio_ids"),
        "next_required_action": selection_report.get("next_required_action"),
        "can_compute_numeric_r": False,
        "can_claim_r": False,
        "promotes_claims": False,
        "rule_reports": rule_reports,
        "audit": audit,
        "ratio_ids": collect_ratio_ids(ratios),
        "stage_p11_r2": stage_p11_r2,
        "stage_n2": stage_n2,
        "stage_p5": stage_p5,
        "stage_p7": stage_p7,
        "stage_p8": stage_p8,
    }
