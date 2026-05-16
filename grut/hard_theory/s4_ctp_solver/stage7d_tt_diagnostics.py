"""Stage 7D TT inversion diagnostics."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.stage7c_tt_inversion import (
    run_stage7c_tt_inversion,
)
from grut.hard_theory.s4_ctp_solver.tt_inversion_stability import (
    analyze_tt_stability,
)
from grut.hard_theory.s4_ctp_solver.tt_mode_behavior_analysis import (
    analyze_mode_behavior,
)
from grut.hard_theory.s4_ctp_solver.tt_divergence_diagnostics import (
    diagnose_tt_divergence,
)
from grut.hard_theory.s4_ctp_solver.tt_inversion_failure_modes import (
    classify_tt_failure_modes,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def run_stage7d_tt_diagnostics() -> Dict[str, object]:
    stage7c = run_stage7c_tt_inversion()
    inversion_results = stage7c["inversion"]["results"]

    stability = analyze_tt_stability(inversion_results)
    mode_behavior = analyze_mode_behavior(inversion_results)
    divergence = diagnose_tt_divergence(inversion_results)
    comparison = stage7c.get("comparison", {})

    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    failure_mode = classify_tt_failure_modes(
        {
            "stability": stability,
            "divergence": divergence,
            "comparison": comparison,
        }
    )

    return {
        "stage": "7D",
        "status": "tt_inversion_diagnostics",
        "stability": stability.get("stability"),
        "divergence": divergence.get("divergence"),
        "failure_mode": failure_mode.get("failure_mode"),
        "regularization_needed": divergence.get("requires_regularization"),
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
        "stage7c": stage7c,
        "stability_report": stability,
        "mode_behavior": mode_behavior,
        "divergence_report": divergence,
        "failure_report": failure_mode,
        "guard": guard,
    }
