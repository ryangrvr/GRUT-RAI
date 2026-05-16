"""Scheme alignment reporting."""

from typing import Dict, List


def generate_scheme_alignment_report(
    scheme: Dict[str, object],
    aligned_results: List[Dict[str, object]],
    consistency: Dict[str, object],
) -> Dict[str, object]:
    stable_structures = list(consistency.get("consistent_terms", []))
    fragile_structures = list(consistency.get("fragile_terms", []))
    unresolved_issues: List[str] = []

    if consistency.get("inconsistent_terms"):
        unresolved_issues.append("protected_invariants_inconsistent")
    if not aligned_results:
        unresolved_issues.append("no_aligned_results")

    return {
        "report_type": "scheme_alignment",
        "status": "scheme_alignment_partial",
        "scheme_definition": scheme,
        "aligned_results": aligned_results,
        "consistency": consistency,
        "stable_structures": stable_structures,
        "fragile_structures": fragile_structures,
        "unresolved_issues": unresolved_issues,
        "can_support_extraction": False,
        "promotes_claims": False,
    }
