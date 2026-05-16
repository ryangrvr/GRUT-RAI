"""Stage 7J tensor contraction readiness diagnostics."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.stage7c_tt_inversion import (
    run_stage7c_tt_inversion,
)
from grut.hard_theory.s4_ctp_solver.stage7e_tt_regularization import (
    run_stage7e_tt_regularization,
)
from grut.hard_theory.s4_ctp_solver.tt_index_structure import (
    analyze_tt_index_structure,
)
from grut.hard_theory.s4_ctp_solver.tt_contraction_rules import (
    define_tt_contraction_rules,
)
from grut.hard_theory.s4_ctp_solver.tt_projector_consistency import (
    check_tt_projector_consistency,
)
from grut.hard_theory.s4_ctp_solver.tt_contraction_readiness import (
    evaluate_contraction_readiness,
)
from grut.hard_theory.s4_ctp_solver.tt_contraction_audit import (
    audit_contraction_readiness,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def run_stage7j_tensor_contraction_readiness() -> Dict[str, object]:
    stage7c = run_stage7c_tt_inversion()
    stage7e = run_stage7e_tt_regularization()
    tt_results = stage7c.get("inversion", {}).get("results", [])
    tt_results.extend(stage7e.get("regularized", []))

    index_structure = analyze_tt_index_structure(tt_results)
    rules = define_tt_contraction_rules()
    projector_check = check_tt_projector_consistency(tt_results)
    readiness = evaluate_contraction_readiness(index_structure, rules, projector_check)
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    audit = audit_contraction_readiness({**readiness, "guard": guard})

    return {
        "stage": "7J",
        "status": "tensor_contraction_readiness",
        "readiness": readiness.get("readiness"),
        "blocker": "tensor_contractions_not_resolved",
        "blocker_closed": False,
        "can_compute_finite_parts": False,
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
        "stage7c": stage7c,
        "stage7e": stage7e,
        "index_structure": index_structure,
        "rules": rules,
        "projector_check": projector_check,
        "readiness_report": readiness,
        "audit": audit,
        "guard": guard,
    }
