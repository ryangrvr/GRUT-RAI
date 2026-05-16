"""Stage 12B scheme-stability audit for coefficient candidates."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.stage12a_coefficient_assembly_dry_run import (
    run_stage12a_coefficient_assembly_dry_run,
)
from grut.hard_theory.s4_ctp_solver.coefficient_scheme_classifier import (
    classify_coefficient_candidates,
)
from grut.hard_theory.s4_ctp_solver.scheme_stability_rules import (
    define_scheme_stability_rules,
)
from grut.hard_theory.s4_ctp_solver.scheme_stability_audit import (
    audit_scheme_stability,
)
from grut.hard_theory.s4_ctp_solver.r_route_legality import (
    assess_r_route_legality,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def run_stage12b_scheme_stability_audit() -> Dict[str, object]:
    stage12a = run_stage12a_coefficient_assembly_dry_run()
    registry = stage12a.get("registry", {})

    classifications = classify_coefficient_candidates(registry)
    rules = define_scheme_stability_rules()
    audit = audit_scheme_stability(classifications, rules)
    r_route = assess_r_route_legality(audit)
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())

    return {
        "stage": "12B",
        "status": "scheme_stability_audit",
        "stable_candidate_count": len(audit.get("stable_candidates", [])),
        "fragile_candidate_count": len(audit.get("fragile_candidates", [])),
        "r_route_status": r_route.get("r_route_status"),
        "can_compute_c_final": False,
        "can_compute_c_cosmo": False,
        "can_compute_r": False,
        "can_extract": False,
        "promotes_claims": False,
        "stage12a": stage12a,
        "classifications": classifications,
        "rules": rules,
        "audit": audit,
        "r_route": r_route,
        "guard": guard,
    }
