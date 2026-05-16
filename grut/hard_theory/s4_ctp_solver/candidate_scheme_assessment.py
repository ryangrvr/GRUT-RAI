"""Scheme-safety assessment for candidate structures."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.scheme_invariants import classify_scheme_sensitivity


def assess_candidate_scheme_safety(candidate: Dict[str, object]) -> Dict[str, object]:
    invariant = candidate.get("associated_invariant", "unknown")

    if invariant == "Euler_density":
        classification = classify_scheme_sensitivity("a")
        scheme_sensitivity = "scheme_protected_candidate"
        reason = classification["reason"]
    elif invariant == "Weyl_squared":
        classification = classify_scheme_sensitivity("c")
        scheme_sensitivity = "scheme_protected_candidate"
        reason = classification["reason"]
    elif invariant == "box_R":
        classification = classify_scheme_sensitivity("box_R")
        scheme_sensitivity = "total_derivative_scheme_dependent"
        reason = classification["reason"]
    elif invariant == "R_squared":
        classification = classify_scheme_sensitivity("C_Cosmo")
        scheme_sensitivity = "scheme_fragile"
        reason = classification["reason"]
    elif invariant == "nonlocal_R_log_box_R":
        classification = classify_scheme_sensitivity("C_Final")
        scheme_sensitivity = "scheme_protected_candidate"
        reason = classification["reason"]
    else:
        classification = classify_scheme_sensitivity(str(invariant))
        scheme_sensitivity = "unknown"
        reason = classification["reason"]

    return {
        "candidate_id": candidate.get("candidate_id", "unknown_candidate"),
        "scheme_sensitivity": scheme_sensitivity,
        "reason": reason,
        "can_extract": False,
        "promotes_claims": False,
    }
