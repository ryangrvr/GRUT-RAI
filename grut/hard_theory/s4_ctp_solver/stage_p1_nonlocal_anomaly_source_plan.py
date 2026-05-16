"""Stage P1 nonlocal anomaly source generation plan."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.stage12g_r_route_terminal_audit import (
    run_stage12g_r_route_terminal_audit,
)
from grut.hard_theory.s4_ctp_solver.stage12c_r5_protected_source_audit import (
    run_stage12c_r5_protected_source_audit,
)
from grut.hard_theory.s4_ctp_solver.stageN2_imaginary_causal_sector_audit import (
    run_stageN2_imaginary_causal_sector_audit,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    run_stage5c_tensor_native,
)
from grut.hard_theory.s4_ctp_solver.stage6a_scheme_alignment import (
    run_stage6a_scheme_alignment,
)
from grut.hard_theory.s4_ctp_solver.nonlocal_anomaly_source_requirements import (
    required_source_types,
    build_source_requirement,
)
from grut.hard_theory.s4_ctp_solver.nonlocal_anomaly_derivation_plan import (
    build_nonlocal_anomaly_derivation_plan,
)
from grut.hard_theory.s4_ctp_solver.protected_source_acceptance_tests import (
    protected_source_acceptance_tests,
)


def run_stage_p1_nonlocal_anomaly_source_plan() -> Dict[str, object]:
    stage12g = run_stage12g_r_route_terminal_audit()
    stage12c_r5 = run_stage12c_r5_protected_source_audit()
    stageN2 = run_stageN2_imaginary_causal_sector_audit()
    stage5c = run_stage5c_tensor_native()
    stage6a = run_stage6a_scheme_alignment()

    source_types = required_source_types()
    requirements = [build_source_requirement(source_type) for source_type in source_types]
    derivation_plan = build_nonlocal_anomaly_derivation_plan()
    acceptance_tests = protected_source_acceptance_tests()

    return {
        "stage": "P1",
        "status": "nonlocal_anomaly_source_generation_plan",
        "source_types_defined": source_types,
        "requirements": requirements,
        "derivation_plan": derivation_plan,
        "acceptance_tests": acceptance_tests,
        "protected_source_derived": False,
        "r_computation_allowed": False,
        "next_required_action": "derive_nonlocal_anomaly_kernel",
        "promotes_claims": False,
        "stage12g": stage12g,
        "stage12c_r5": stage12c_r5,
        "stageN2": stageN2,
        "stage5c": stage5c,
        "stage6a": stage6a,
    }
