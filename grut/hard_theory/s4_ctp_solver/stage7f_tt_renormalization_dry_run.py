"""Stage 7F TT renormalization dry-run."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.stage7e_tt_regularization import (
    run_stage7e_tt_regularization,
)
from grut.hard_theory.s4_ctp_solver.tt_divergence_to_counterterms import (
    map_tt_divergences_to_counterterms,
)
from grut.hard_theory.s4_ctp_solver.tt_renormalization_plan import (
    build_tt_renormalization_plan,
)
from grut.hard_theory.s4_ctp_solver.tt_scheme_alignment_check import (
    check_tt_scheme_alignment,
)
from grut.hard_theory.s4_ctp_solver.tt_renormalization_audit import (
    audit_tt_renormalization_dry_run,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def run_stage7f_tt_renormalization_dry_run() -> Dict[str, object]:
    stage7e = run_stage7e_tt_regularization()
    regularized_results = stage7e.get("regularized", [])

    mapping = map_tt_divergences_to_counterterms(regularized_results)
    plan = build_tt_renormalization_plan(mapping)
    scheme_check = check_tt_scheme_alignment(plan)
    audit = audit_tt_renormalization_dry_run(plan, scheme_check)
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())

    return {
        "stage": "7F",
        "status": "tt_renormalization_dry_run",
        "counterterms_mapped": True,
        "renormalization_performed": False,
        "finite_parts_computed": False,
        "scheme_alignment": scheme_check.get("scheme_alignment"),
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
        "stage7e": stage7e,
        "mapping": mapping,
        "plan": plan,
        "scheme_check": scheme_check,
        "audit": audit,
        "guard": guard,
    }
