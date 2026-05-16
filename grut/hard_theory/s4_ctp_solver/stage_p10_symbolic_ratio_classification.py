"""Stage P10 symbolic protected ratio classification."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.stage_p9_controlled_symbolic_r_attempt import (
    run_stage_p9_controlled_symbolic_r_attempt,
)
from grut.hard_theory.s4_ctp_solver.stage_p8_r_legality_with_protected_kernels import (
    run_stage_p8_r_legality_with_protected_kernels,
)
from grut.hard_theory.s4_ctp_solver.stage_p7_protected_scheme_injection import (
    run_stage_p7_protected_scheme_injection,
)
from grut.hard_theory.s4_ctp_solver.stage_p5_counterterm_finite_readiness import (
    run_stage_p5_counterterm_finite_readiness,
)
from grut.hard_theory.s4_ctp_solver.protected_ratio_classifier import (
    classify_symbolic_ratio,
)
from grut.hard_theory.s4_ctp_solver.protected_ratio_degeneracy_analysis import (
    analyze_ratio_degeneracy,
)
from grut.hard_theory.s4_ctp_solver.protected_ratio_uniqueness import (
    analyze_ratio_uniqueness,
)
from grut.hard_theory.s4_ctp_solver.protected_ratio_audit import (
    audit_symbolic_ratio_classification,
)


def _collect_candidates(stage_p9: Dict[str, object]) -> List[Dict[str, object]]:
    candidates: List[Dict[str, object]] = []
    candidates.extend(stage_p9.get("symbolic_candidates", []))
    candidates.extend(stage_p9.get("blocked_pairs", []))
    return candidates


def run_stage_p10_symbolic_ratio_classification() -> Dict[str, object]:
    stage_p9 = run_stage_p9_controlled_symbolic_r_attempt()
    stage_p8 = run_stage_p8_r_legality_with_protected_kernels()
    stage_p7 = run_stage_p7_protected_scheme_injection()
    stage_p5 = run_stage_p5_counterterm_finite_readiness()

    scheme_candidates = stage_p7.get("scheme_protected_candidates", [])
    readiness_candidates = stage_p5.get("readiness_candidates", [])

    classified: List[Dict[str, object]] = []
    for entry in _collect_candidates(stage_p9):
        classified.append(
            classify_symbolic_ratio(entry, scheme_candidates, readiness_candidates)
        )

    valid_symbolic_ratios = [
        entry
        for entry in classified
        if entry.get("classification") == "valid_symbolic_ratio_candidate"
    ]
    blocked_symbolic_ratios = [
        entry
        for entry in classified
        if entry.get("classification") != "valid_symbolic_ratio_candidate"
    ]

    degeneracy_report = analyze_ratio_degeneracy(valid_symbolic_ratios)
    uniqueness_report = analyze_ratio_uniqueness(valid_symbolic_ratios, degeneracy_report)

    audit = audit_symbolic_ratio_classification(
        valid_symbolic_ratios, blocked_symbolic_ratios, uniqueness_report.get("unique_ratio_exists")
    )

    return {
        "stage": "P10",
        "status": "symbolic_protected_ratio_classification",
        "ratios_examined": len(classified),
        "valid_symbolic_ratios": valid_symbolic_ratios,
        "blocked_symbolic_ratios": blocked_symbolic_ratios,
        "unique_ratio_exists": uniqueness_report.get("unique_ratio_exists"),
        "representative_ratio_id": uniqueness_report.get("representative_ratio_id"),
        "can_advance_to_coefficient_symbol_binding": audit.get(
            "can_advance_to_coefficient_symbol_binding"
        ),
        "can_compute_numeric_r": False,
        "can_claim_r": False,
        "promotes_claims": False,
        "degeneracy_report": degeneracy_report,
        "uniqueness_report": uniqueness_report,
        "audit": audit,
        "stage_p9": stage_p9,
        "stage_p8": stage_p8,
        "stage_p7": stage_p7,
        "stage_p5": stage_p5,
    }
