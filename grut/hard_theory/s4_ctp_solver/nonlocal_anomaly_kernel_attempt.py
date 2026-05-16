"""Attempt to identify a non-scaffold nonlocal anomaly kernel."""

from typing import Dict, List


def attempt_nonlocal_anomaly_kernel(stageN2: Dict[str, object]) -> Dict[str, object]:
    candidates = stageN2.get("candidate_sources", [])

    kernel_candidates: List[Dict[str, object]] = []
    for candidate in candidates:
        if candidate.get("scaffold_only") is True:
            continue
        indicators = candidate.get("indicators", {})
        if indicators.get("nonlocal_kernel") or indicators.get("imaginary_log"):
            kernel_candidates.append(candidate)

    kernel_found = bool(kernel_candidates)
    missing_reasons: List[str] = []
    if not candidates:
        missing_reasons.append("no_candidate_sources")
    elif not kernel_candidates:
        missing_reasons.append("only_scaffold_sources")

    return {
        "kernel_found": kernel_found,
        "kernel_candidates": kernel_candidates,
        "missing_reasons": missing_reasons,
        "promotes_claims": False,
    }
