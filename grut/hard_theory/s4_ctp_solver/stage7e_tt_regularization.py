"""Stage 7E TT regularized spectral inversion."""

from typing import Dict, List

import sympy as sp

from grut.hard_theory.s4_ctp_solver.stage7c_tt_inversion import (
    run_stage7c_tt_inversion,
)
from grut.hard_theory.s4_ctp_solver.tt_regularization_schemes import (
    define_regularization_schemes,
)
from grut.hard_theory.s4_ctp_solver.tt_regularized_inversion import (
    perform_regularized_tt_inversion,
)
from grut.hard_theory.s4_ctp_solver.tt_regularization_comparison import (
    compare_regularization_results,
)
from grut.hard_theory.s4_ctp_solver.tt_regularization_audit import (
    audit_regularized_inversion,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def run_stage7e_tt_regularization() -> Dict[str, object]:
    stage7c = run_stage7c_tt_inversion()
    schemes = define_regularization_schemes()
    epsilon = sp.symbols("epsilon", positive=True)

    regularized: List[Dict[str, object]] = []
    for scheme in schemes["schemes"]:
        regularized.append(
            perform_regularized_tt_inversion(l_max=10, epsilon=epsilon, scheme=scheme)
        )

    comparison = compare_regularization_results(regularized)
    audit = audit_regularized_inversion({"regularized": regularized, "comparison": comparison})
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())

    return {
        "stage": "7E",
        "status": "tt_regularized_inversion",
        "regularization_applied": True,
        "stability_improved": comparison.get("stability_improved"),
        "structure_preserved": comparison.get("structure_preserved"),
        "convergence_observed": comparison.get("convergence_observed"),
        "regularization_required": True,
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
        "stage7c": stage7c,
        "schemes": schemes,
        "regularized": regularized,
        "comparison": comparison,
        "audit": audit,
        "guard": guard,
    }
