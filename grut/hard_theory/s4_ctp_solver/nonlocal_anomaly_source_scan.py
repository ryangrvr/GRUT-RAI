"""Scan aligned terms and candidates for nonlocal anomaly-channel sources."""

from typing import Dict, Iterable, List, Tuple


_PROTECTED_INVARIANTS = {"nonlocal_R_log_box_R"}
_REJECTED_INVARIANTS = {"R_squared", "box_R"}


def _normalize(text: str) -> str:
    return "".join(text.lower().split())


def _is_weyl_log_box(term: str) -> bool:
    normalized = _normalize(term)
    return "weyl" in normalized and "log" in normalized and "box" in normalized


def _is_nonlocal_kernel(term: str) -> bool:
    normalized = _normalize(term)
    return "nonlocal" in normalized and "kernel" in normalized and (
        "r" in normalized or "curvature" in normalized
    )


def _term_is_rejected(invariant: str, term: str) -> Tuple[bool, str | None]:
    if invariant in _REJECTED_INVARIANTS:
        return True, "local_counterterm"
    normalized = _normalize(term)
    if "r^2" in normalized or "r_squared" in normalized:
        return True, "local_counterterm"
    if "einstein" in normalized or "hilbert" in normalized:
        return True, "local_einstein_hilbert"
    if "cosmo" in normalized:
        return True, "local_cosmological"
    return False, None


def _aligned_candidates(aligned_results: Iterable[Dict[str, object]]) -> List[Dict[str, object]]:
    candidates: List[Dict[str, object]] = []
    for result in aligned_results:
        topology_id = result.get("topology_id", "unknown_topology")
        for term in result.get("aligned_terms", []):
            invariant = term.get("invariant", "unknown")
            term_text = term.get("term", "")

            rejected, reason = _term_is_rejected(invariant, term_text)
            if rejected:
                continue

            is_protected = invariant in _PROTECTED_INVARIANTS
            is_weyl = _is_weyl_log_box(term_text)
            is_kernel = _is_nonlocal_kernel(term_text)

            if not any([is_protected, is_weyl, is_kernel]):
                continue

            candidates.append(
                {
                    "source_id": topology_id,
                    "source_kind": "aligned_term",
                    "invariant": invariant,
                    "term": term_text,
                    "evidence": "aligned_term",
                    "promotes_claims": False,
                }
            )
    return candidates


def _candidate_structures(candidates: Iterable[Dict[str, object]]) -> List[Dict[str, object]]:
    results: List[Dict[str, object]] = []
    for candidate in candidates:
        invariant = candidate.get("associated_invariant", "unknown")
        symbolic_form = candidate.get("symbolic_form", "")

        rejected, reason = _term_is_rejected(invariant, symbolic_form)
        if rejected:
            continue

        is_protected = invariant in _PROTECTED_INVARIANTS
        is_weyl = _is_weyl_log_box(symbolic_form)
        is_kernel = _is_nonlocal_kernel(symbolic_form)

        if not any([is_protected, is_weyl, is_kernel]):
            continue

        results.append(
            {
                "source_id": candidate.get("candidate_id", "unknown_candidate"),
                "source_kind": "candidate_structure",
                "invariant": invariant,
                "term": symbolic_form,
                "evidence": "candidate_structure",
                "promotes_claims": False,
            }
        )
    return results


def find_nonlocal_anomaly_sources(
    alignment_report: Dict[str, object],
    candidate_report: Dict[str, object],
) -> Dict[str, object]:
    aligned_results = alignment_report.get("aligned_results", [])
    candidate_structures = candidate_report.get("candidates", [])

    sources = _aligned_candidates(aligned_results)
    sources.extend(_candidate_structures(candidate_structures))

    protected_sources_found = len(sources)
    return {
        "protected_sources_found": protected_sources_found,
        "candidate_sources": sources,
        "promotes_claims": False,
    }
