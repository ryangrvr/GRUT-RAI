"""Native attempt audit for Stage 5A."""

from typing import Dict, List


def audit_native_attempt(result: Dict[str, object]) -> Dict[str, object]:
    steps = result.get("evaluation_steps", [])
    step_names = {step.get("stage") for step in steps}
    required = {
        "spectral_setup",
        "scalar_subset_evaluation",
        "scheme_tagging",
        "divergence_tracking",
        "cross_check",
        "ward_placeholder",
    }
    missing = sorted(required - step_names)

    issues: List[str] = []
    if missing:
        issues.append("missing_steps")

    scheme_present = any(step.get("stage") == "scheme_tagging" for step in steps)
    ward_present = any(step.get("stage") == "ward_placeholder" for step in steps)

    valid = not missing and scheme_present and ward_present

    return {
        "audit": "native_attempt",
        "status": "valid_attempt" if valid else "invalid_attempt",
        "issues": issues,
        "promotion_blocked": True,
        "can_promote_to_computed": False,
    }
