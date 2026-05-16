"""Stage P11-R2 equivalence refresh with propagated regulator classes."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.stage_p11_r1_regulator_class_resolution import (
    run_stage_p11_r1_regulator_class_resolution,
)
from grut.hard_theory.s4_ctp_solver.stage_p10_symbolic_ratio_classification import (
    run_stage_p10_symbolic_ratio_classification,
)
from grut.hard_theory.s4_ctp_solver.protected_ratio_regulator_propagation import (
    propagate_ratio_regulator_classes,
)
from grut.hard_theory.s4_ctp_solver.protected_ratio_equivalence_refresh import (
    refresh_ratio_equivalence,
)
from grut.hard_theory.s4_ctp_solver.protected_ratio_equivalence_refresh_audit import (
    audit_equivalence_refresh,
)


def _collect_ratios(stage_p10: Dict[str, object]) -> List[Dict[str, object]]:
    ratios: List[Dict[str, object]] = []
    ratios.extend(stage_p10.get("valid_symbolic_ratios", []))
    ratios.extend(stage_p10.get("blocked_symbolic_ratios", []))
    return ratios


def _resolve_uniqueness(equivalence_report: Dict[str, object]) -> Dict[str, object]:
    classes = equivalence_report.get("equivalence_classes", [])
    unresolved = equivalence_report.get("unresolved", [])

    if not classes:
        if unresolved:
            return {
                "unique_equivalence_class_exists": False,
                "representative_ratio_id": None,
                "reason": "equivalence_undetermined",
            }
        return {
            "unique_equivalence_class_exists": False,
            "representative_ratio_id": None,
            "reason": "no_equivalence_classes",
        }

    if len(classes) == 1:
        ratio_ids = classes[0].get("ratio_ids", [])
        representative = ratio_ids[0] if ratio_ids else None
        return {
            "unique_equivalence_class_exists": True,
            "representative_ratio_id": representative,
            "reason": "unique_equivalence_class",
        }

    return {
        "unique_equivalence_class_exists": False,
        "representative_ratio_id": None,
        "reason": "multiple_inequivalent_classes",
    }


def run_stage_p11_r2_equivalence_refresh() -> Dict[str, object]:
    stage_p11_r1 = run_stage_p11_r1_regulator_class_resolution()
    stage_p10 = run_stage_p10_symbolic_ratio_classification()

    ratios = _collect_ratios(stage_p10)
    refreshed_ratios = propagate_ratio_regulator_classes(
        ratios,
        stage_p11_r1.get("ratio_regulator_classes", []),
    )

    equivalence_report = refresh_ratio_equivalence(refreshed_ratios)
    uniqueness = _resolve_uniqueness(equivalence_report)

    audit = audit_equivalence_refresh(
        refreshed_ratios,
        equivalence_report,
        uniqueness.get("unique_equivalence_class_exists"),
    )

    return {
        "stage": "P11-R2",
        "status": "equivalence_refresh",
        "equivalence_classes": equivalence_report.get("equivalence_classes", []),
        "unique_equivalence_class_exists": uniqueness.get(
            "unique_equivalence_class_exists"
        ),
        "representative_ratio_id": uniqueness.get("representative_ratio_id"),
        "can_advance_to_coefficient_symbol_binding": audit.get(
            "can_advance_to_coefficient_symbol_binding"
        ),
        "can_compute_numeric_r": False,
        "can_claim_r": False,
        "promotes_claims": False,
        "equivalence_report": equivalence_report,
        "audit": audit,
        "stage_p11_r1": stage_p11_r1,
        "stage_p10": stage_p10,
        "refreshed_ratios": refreshed_ratios,
    }
