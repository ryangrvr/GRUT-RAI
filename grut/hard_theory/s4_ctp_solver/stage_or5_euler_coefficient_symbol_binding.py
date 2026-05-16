"""Stage OR5 Euler coefficient symbol binding."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.euler_symbolic_coefficient_binding import (
    bind_euler_coefficient_symbols,
)
from grut.hard_theory.s4_ctp_solver.euler_binding_audit import (
    audit_euler_binding,
)
from grut.hard_theory.s4_ctp_solver.stage_or4_formal_r_definition_gate import (
    run_stage_or4_formal_r_definition_gate,
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


def run_stage_or5_euler_coefficient_symbol_binding() -> Dict[str, object]:
    or4_report = run_stage_or4_formal_r_definition_gate()
    or3_report = or4_report.get("stage_or3") or run_stage_or3_s4_euler_anomaly_projection()
    stage_p7 = or4_report.get("stage_p7") or run_stage_p7_protected_scheme_injection()
    stage_p8 = run_stage_p8_r_legality_with_protected_kernels()
    stage_p11_r2 = run_stage_p11_r2_equivalence_refresh()

    binding_report = bind_euler_coefficient_symbols(or4_report, or3_report, stage_p7)
    audit = audit_euler_binding(binding_report)

    return {
        "stage": "OR5",
        "status": "euler_coefficient_symbol_binding",
        "bindings": binding_report.get("bindings", []),
        "binding_complete": binding_report.get("binding_complete"),
        "symbolic_ratio_form": binding_report.get("symbolic_ratio_form"),
        "can_advance_to_symbolic_euler_extraction": binding_report.get(
            "can_advance_to_symbolic_euler_extraction"
        ),
        "can_compute_numeric_r": False,
        "can_claim_r": False,
        "promotes_claims": False,
        "binding_audit": audit,
        "stage_or4": or4_report,
        "stage_or3": or3_report,
        "stage_p7": stage_p7,
        "stage_p8": stage_p8,
        "stage_p11_r2": stage_p11_r2,
    }
