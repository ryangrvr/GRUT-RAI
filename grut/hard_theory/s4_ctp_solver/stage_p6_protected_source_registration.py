"""Stage P6 protected source candidate registration."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.stage_p5_counterterm_finite_readiness import (
    run_stage_p5_counterterm_finite_readiness,
)
from grut.hard_theory.s4_ctp_solver.stage_p4_protected_kernel_integration import (
    run_stage_p4_protected_kernel_integration,
)
from grut.hard_theory.s4_ctp_solver.stage12b_scheme_stability_audit import (
    run_stage12b_scheme_stability_audit,
)
from grut.hard_theory.s4_ctp_solver.stage12c_r_legality_gate import (
    run_stage12c_r_legality_gate,
)
from grut.hard_theory.s4_ctp_solver.protected_source_candidate_registry import (
    register_protected_source_candidates,
)
from grut.hard_theory.s4_ctp_solver.protected_source_scheme_eligibility import (
    determine_scheme_eligibility,
)
from grut.hard_theory.s4_ctp_solver.protected_source_registration_audit import (
    audit_protected_source_registration,
)


def run_stage_p6_protected_source_registration() -> Dict[str, object]:
    stage_p5 = run_stage_p5_counterterm_finite_readiness()
    stage_p4 = run_stage_p4_protected_kernel_integration()
    stage12b = run_stage12b_scheme_stability_audit()
    stage12c = run_stage12c_r_legality_gate()

    scheme_status = determine_scheme_eligibility(stage12b, stage12c)

    registered = register_protected_source_candidates(stage_p5, stage_p4, scheme_status)
    audit = audit_protected_source_registration(registered)

    return {
        "stage": "P6",
        "status": "protected_source_candidate_registration",
        "registered_candidates": registered,
        "registered_count": len(registered),
        "rerun_12b_recommended": len(registered) >= 2,
        "r_computation_allowed": False,
        "promotes_claims": False,
        "audit": audit,
        "stage_p5": stage_p5,
        "stage_p4": stage_p4,
        "stage12b": stage12b,
        "stage12c": stage12c,
    }
