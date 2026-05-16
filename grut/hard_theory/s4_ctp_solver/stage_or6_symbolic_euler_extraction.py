"""Stage OR6 symbolic Euler quotient extraction."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.stage_or4_formal_r_definition_gate import (
    run_stage_or4_formal_r_definition_gate,
)
from grut.hard_theory.s4_ctp_solver.stage_or5_euler_coefficient_symbol_binding import (
    run_stage_or5_euler_coefficient_symbol_binding,
)
from grut.hard_theory.s4_ctp_solver.stage_or3_s4_euler_anomaly_projection import (
    run_stage_or3_s4_euler_anomaly_projection,
)
from grut.hard_theory.s4_ctp_solver.stage_p7_protected_scheme_injection import (
    run_stage_p7_protected_scheme_injection,
)
from grut.hard_theory.s4_ctp_solver.stage_p8_r_legality_with_protected_kernels import (
    run_stage_p8_r_legality_with_protected_kernels,
)
from grut.hard_theory.s4_ctp_solver.stage_p11_r2_equivalence_refresh import (
    run_stage_p11_r2_equivalence_refresh,
)
from grut.hard_theory.s4_ctp_solver.stage12b_scheme_stability_audit import (
    run_stage12b_scheme_stability_audit,
)
from grut.hard_theory.s4_ctp_solver.symbolic_euler_extraction_rules import (
    evaluate_projection_guard,
)
from grut.hard_theory.s4_ctp_solver.symbolic_euler_scheme_guard import (
    evaluate_scheme_guard,
)
from grut.hard_theory.s4_ctp_solver.symbolic_euler_quotient import (
    build_symbolic_euler_quotient,
)
from grut.hard_theory.s4_ctp_solver.symbolic_euler_extraction_audit import (
    audit_symbolic_euler_extraction,
)


def run_stage_or6_symbolic_euler_extraction(use_cached: bool = True) -> Dict[str, object]:
    if use_cached:
        or5_report = run_stage_or5_euler_coefficient_symbol_binding()
        or4_report = or5_report.get("stage_or4", {})
        or3_report = or5_report.get("stage_or3") or or4_report.get("stage_or3", {})
        stage_p7 = or5_report.get("stage_p7", {})
        stage_p8 = or5_report.get("stage_p8", {})
        stage_p11_r2 = or5_report.get("stage_p11_r2", {})
        stage12b = or5_report.get("stage12b", {})
    else:
        or4_report = run_stage_or4_formal_r_definition_gate()
        or5_report = run_stage_or5_euler_coefficient_symbol_binding()
        or3_report = or4_report.get("stage_or3") or run_stage_or3_s4_euler_anomaly_projection()

        stage_p7 = or4_report.get("stage_p7") or run_stage_p7_protected_scheme_injection()
        stage_p8 = run_stage_p8_r_legality_with_protected_kernels()
        stage_p11_r2 = run_stage_p11_r2_equivalence_refresh()
        stage12b = run_stage12b_scheme_stability_audit()

    projection_guard = evaluate_projection_guard(or4_report, or3_report)
    scheme_guard = evaluate_scheme_guard(
        or5_report.get("bindings", []),
        stage_p7,
        stage_p8,
        stage_p11_r2,
        projection_guard.get("projection_domain"),
    )

    symbolic_ratio = None
    if projection_guard.get("projection_guard_passed") and scheme_guard.get("scheme_guard_passed"):
        symbolic_ratio = build_symbolic_euler_quotient(
            scheme_guard.get("regulator_class"),
            projection_guard.get("projection_domain"),
        )

    audit = audit_symbolic_euler_extraction(symbolic_ratio or {}, scheme_guard)

    symbolic_extraction_complete = bool(symbolic_ratio) and audit.get("status") == "pass"

    return {
        "stage": "OR6",
        "status": "symbolic_euler_extraction",
        "symbolic_ratio": symbolic_ratio,
        "scheme_guard_passed": scheme_guard.get("scheme_guard_passed"),
        "projection_guard_passed": projection_guard.get("projection_guard_passed"),
        "symbolic_extraction_complete": symbolic_extraction_complete,
        "can_advance_to_numeric_stability_audit": symbolic_extraction_complete,
        "can_compute_numeric_r": False,
        "can_claim_r": False,
        "promotes_claims": False,
        "scheme_guard": scheme_guard,
        "projection_guard": projection_guard,
        "symbolic_extraction_audit": audit,
        "stage_or4": or4_report,
        "stage_or5": or5_report,
        "stage_or3": or3_report,
        "stage_p7": stage_p7,
        "stage_p8": stage_p8,
        "stage_p11_r2": stage_p11_r2,
        "stage12b": stage12b,
        "use_cached": use_cached,
    }
