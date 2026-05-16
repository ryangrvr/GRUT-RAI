"""Scan for imaginary/causal sector indicators in aligned terms and candidates."""

from typing import Dict, Iterable, List, Tuple


_REJECTED_INVARIANTS = {"R_squared", "box_R"}


def _normalize(text: str) -> str:
    return "".join(text.lower().split())


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
    if "scalar" in normalized and "slice" in normalized:
        return True, "local_scalar_slice"
    return False, None


def _imaginary_indicators(term: str) -> Dict[str, bool]:
    normalized = _normalize(term)
    has_im_log = "log(-" in normalized and ("box" in normalized or "□" in term)
    has_i_eps = "iε" in normalized or "i\\epsilon" in normalized or "i*epsilon" in normalized
    has_imag = "imag" in normalized or "im(" in normalized or "imaginary" in normalized
    has_branch = any(token in normalized for token in ["branch", "cut", "discontinuity"])
    has_absorptive = "absorptive" in normalized
    has_keldysh = any(token in normalized for token in ["keldysh", "ctp", "schwinger"])
    has_causal = any(token in normalized for token in ["causal", "retarded", "advanced"])
    has_dissipative = any(token in normalized for token in ["dissipative", "decoherence"])
    has_kernel = "kernel" in normalized and "nonlocal" in normalized

    return {
        "imaginary_log": has_im_log,
        "i_epsilon": has_i_eps,
        "imaginary_marker": has_imag,
        "branch_cut": has_branch,
        "absorptive": has_absorptive,
        "keldysh_ctp": has_keldysh,
        "causal_terms": has_causal,
        "dissipative": has_dissipative,
        "nonlocal_kernel": has_kernel,
    }


def _has_any_indicator(indicators: Dict[str, bool]) -> bool:
    return any(indicators.values())


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

            indicators = _imaginary_indicators(term_text)
            if not _has_any_indicator(indicators):
                continue

            candidates.append(
                {
                    "source_id": topology_id,
                    "source_kind": "aligned_term",
                    "invariant": invariant,
                    "term": term_text,
                    "indicators": indicators,
                    "evidence_tag": "imaginary_sector_scaffold",
                    "scaffold_only": True,
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

        indicators = _imaginary_indicators(symbolic_form)
        if not _has_any_indicator(indicators):
            continue

        results.append(
            {
                "source_id": candidate.get("candidate_id", "unknown_candidate"),
                "source_kind": "candidate_structure",
                "invariant": invariant,
                "term": symbolic_form,
                "indicators": indicators,
                "evidence_tag": "imaginary_sector_scaffold",
                "scaffold_only": True,
                "promotes_claims": False,
            }
        )
    return results


def find_imaginary_causal_sources(
    alignment_report: Dict[str, object],
    candidate_report: Dict[str, object],
) -> Dict[str, object]:
    aligned_results = alignment_report.get("aligned_results", [])
    candidate_structures = candidate_report.get("candidates", [])

    sources = _aligned_candidates(aligned_results)
    sources.extend(_candidate_structures(candidate_structures))

    return {
        "protected_sources_found": len(sources),
        "candidate_sources": sources,
        "promotes_claims": False,
    }
