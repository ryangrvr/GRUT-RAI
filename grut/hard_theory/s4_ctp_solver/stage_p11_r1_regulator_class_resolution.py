"""Stage P11-R1 regulator class resolution for protected ratios."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.stage_p7_protected_scheme_injection import (
    run_stage_p7_protected_scheme_injection,
)
from grut.hard_theory.s4_ctp_solver.stage_p8_r_legality_with_protected_kernels import (
    run_stage_p8_r_legality_with_protected_kernels,
)
from grut.hard_theory.s4_ctp_solver.stage_p9_controlled_symbolic_r_attempt import (
    run_stage_p9_controlled_symbolic_r_attempt,
)
from grut.hard_theory.s4_ctp_solver.stage_p10_symbolic_ratio_classification import (
    run_stage_p10_symbolic_ratio_classification,
)
from grut.hard_theory.s4_ctp_solver.stage9c_regularized_integrand import (
    run_stage9c_regularized_integrand,
)
from grut.hard_theory.s4_ctp_solver.stage10f_partition_consistency_audit import (
    run_stage10f_partition_consistency_audit,
)
from grut.hard_theory.s4_ctp_solver.protected_kernel_regulator_class import (
    resolve_protected_kernel_regulator_class,
)
from grut.hard_theory.s4_ctp_solver.protected_ratio_regulator_inheritance import (
    assign_ratio_regulator_classes,
)
from grut.hard_theory.s4_ctp_solver.protected_regulator_class_audit import (
    audit_regulator_class_resolution,
)


def _collect_symbolic_entries(stage_p9: Dict[str, object]) -> List[Dict[str, object]]:
    entries: List[Dict[str, object]] = []
    entries.extend(stage_p9.get("symbolic_candidates", []))
    entries.extend(stage_p9.get("blocked_pairs", []))
    return entries


def run_stage_p11_r1_regulator_class_resolution() -> Dict[str, object]:
    stage_p7 = run_stage_p7_protected_scheme_injection()
    stage_p8 = run_stage_p8_r_legality_with_protected_kernels()
    stage_p9 = run_stage_p9_controlled_symbolic_r_attempt()
    stage_p10 = run_stage_p10_symbolic_ratio_classification()
    stage9c = run_stage9c_regularized_integrand()
    stage10f = run_stage10f_partition_consistency_audit()

    registered_candidates = stage_p7.get("stage_p6", {}).get("registered_candidates", [])
    kernel_regulator_classes = resolve_protected_kernel_regulator_class(
        registered_candidates,
        stage9c,
        stage10f,
    )

    symbolic_entries = _collect_symbolic_entries(stage_p9)
    ratio_regulator_classes = assign_ratio_regulator_classes(
        symbolic_entries,
        kernel_regulator_classes,
    )

    audit = audit_regulator_class_resolution(
        kernel_regulator_classes,
        ratio_regulator_classes,
        symbolic_entries,
    )

    regulator_classes_resolved = audit.get("regulator_classes_resolved") is True

    return {
        "stage": "P11-R1",
        "status": "regulator_class_resolution",
        "kernel_regulator_classes": kernel_regulator_classes,
        "ratio_regulator_classes": ratio_regulator_classes,
        "regulator_classes_resolved": regulator_classes_resolved,
        "rerun_p11_recommended": regulator_classes_resolved,
        "can_compute_numeric_r": False,
        "can_claim_r": False,
        "promotes_claims": False,
        "audit": audit,
        "stage_p7": stage_p7,
        "stage_p8": stage_p8,
        "stage_p9": stage_p9,
        "stage_p10": stage_p10,
        "stage9c": stage9c,
        "stage10f": stage10f,
    }
