"""Resolve regulator class for protected kernels."""

from typing import Dict, List


def _regulator_present(stage10f: Dict[str, object]) -> bool:
    attempts = stage10f.get("collected", {}).get("collected_attempts", [])
    if not attempts:
        return False
    return all(attempt.get("regulator_present") is True for attempt in attempts)


def resolve_protected_kernel_regulator_class(
    registered_candidates: List[Dict[str, object]],
    stage9c: Dict[str, object],
    stage10f: Dict[str, object],
) -> List[Dict[str, object]]:
    scheme = stage9c.get("scheme", {})
    default_regulator = scheme.get("default_regulator")
    scheme_id = scheme.get("scheme_id")
    regulator_removed = stage10f.get("regulator_check", {}).get("regulator_removed")
    regulator_present = _regulator_present(stage10f)

    resolved = (
        default_regulator == "dimensional_regularization_placeholder"
        and regulator_present is True
        and regulator_removed is False
        and scheme_id == "integrand_regularization_v1"
    )

    regulator_class = (
        "dimensional_regularization_symbolic_preserved"
        if resolved
        else "regulator_class_unresolved"
    )

    kernel_classes: List[Dict[str, object]] = []
    for candidate in registered_candidates:
        kernel_classes.append(
            {
                "protected_source_candidate_id": candidate.get(
                    "protected_source_candidate_id"
                ),
                "source_type": candidate.get("source_type"),
                "kernel_id": candidate.get("kernel_id"),
                "regulator_class": regulator_class,
                "promotes_claims": False,
            }
        )

    return kernel_classes
