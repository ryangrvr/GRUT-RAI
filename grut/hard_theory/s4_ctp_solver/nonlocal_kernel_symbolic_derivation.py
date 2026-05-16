"""Symbolic derivation attempt for nonlocal anomaly kernels."""

from typing import Dict, List


def _extract_candidate_terms(stageN2: Dict[str, object]) -> List[str]:
    terms: List[str] = []
    for candidate in stageN2.get("candidate_sources", []):
        term = candidate.get("term")
        if isinstance(term, str) and term:
            terms.append(term)
    return terms


def attempt_symbolic_derivation(
    targets: List[Dict[str, object]],
    stageN2: Dict[str, object],
) -> List[Dict[str, object]]:
    terms = _extract_candidate_terms(stageN2)
    scaffold_only = all(
        candidate.get("scaffold_only") is True for candidate in stageN2.get("candidate_sources", [])
    )

    derived: List[Dict[str, object]] = []
    for target in targets:
        expected_form = target.get("expected_nonlocal_form", "")
        has_expected = any(expected_form in term for term in terms)

        status = "failed_derivation"
        derivation_kind = "none"
        if scaffold_only and terms:
            status = "scaffold_only"
            derivation_kind = "scaffold"
        elif has_expected:
            status = "symbolic_candidate"
            derivation_kind = "symbolic"

        derived.append(
            {
                "source_type": target.get("source_type"),
                "expected_nonlocal_form": expected_form,
                "status": status,
                "derivation_kind": derivation_kind,
                "nonlocal_form_present": has_expected,
                "scaffold_only": status == "scaffold_only",
                "local_counterterm_nonmixing_checked": False,
                "finite_coefficient_extractable": False,
                "promotes_claims": False,
            }
        )

    return derived
