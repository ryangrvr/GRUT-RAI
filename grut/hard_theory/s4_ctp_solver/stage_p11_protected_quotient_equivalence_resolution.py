"""Stage P11 protected quotient equivalence resolution."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.stage_p10_symbolic_ratio_classification import (
    run_stage_p10_symbolic_ratio_classification,
)
from grut.hard_theory.s4_ctp_solver.protected_ratio_equivalence_resolver import (
    resolve_ratio_equivalence,
)
from grut.hard_theory.s4_ctp_solver.protected_ratio_equivalence_audit import (
    audit_ratio_equivalence_resolution,
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
                "unique_ratio_exists": False,
                "representative_ratio_id": None,
                "reason": "equivalence_undetermined",
            }
        return {
            "unique_ratio_exists": False,
            "representative_ratio_id": None,
            "reason": "no_equivalence_classes",
        }

    if len(classes) == 1:
        ratio_ids = classes[0].get("ratio_ids", [])
        representative = ratio_ids[0] if ratio_ids else None
        return {
            "unique_ratio_exists": True,
            "representative_ratio_id": representative,
            "reason": "unique_equivalence_class",
        }

    return {
        "unique_ratio_exists": False,
        "representative_ratio_id": None,
        "reason": "multiple_inequivalent_classes",
    }


def run_stage_p11_protected_quotient_equivalence_resolution() -> Dict[str, object]:
    stage_p10 = run_stage_p10_symbolic_ratio_classification()
    ratios = _collect_ratios(stage_p10)

    equivalence_report = resolve_ratio_equivalence(ratios)
    uniqueness = _resolve_uniqueness(equivalence_report)

    audit = audit_ratio_equivalence_resolution(
        ratios,
        equivalence_report,
        uniqueness.get("unique_ratio_exists"),
    )

    return {
        "stage": "P11",
        "status": "protected_quotient_equivalence_resolution",
        "ratios_examined": len(ratios),
        "equivalence_report": equivalence_report,
        "unique_ratio_exists": uniqueness.get("unique_ratio_exists"),
        "representative_ratio_id": uniqueness.get("representative_ratio_id"),
        "can_advance_to_coefficient_symbol_binding": audit.get(
            "can_advance_to_coefficient_symbol_binding"
        ),
        "can_compute_numeric_r": False,
        "can_claim_r": False,
        "promotes_claims": False,
        "audit": audit,
        "stage_p10": stage_p10,
    }
