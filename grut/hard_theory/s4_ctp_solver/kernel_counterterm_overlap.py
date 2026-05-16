"""Assess overlap between nonlocal kernels and local counterterm basis."""

from __future__ import annotations

from typing import Dict, List

_LOCAL_COUNTERTERMS = [
    "cosmological_constant",
    "Einstein_Hilbert",
    "R_squared",
    "Ricci_squared",
    "Riemann_squared",
    "Weyl_squared",
    "Euler_density",
    "box_R",
]


def _extract_form(candidate: Dict[str, object]) -> str:
    form = candidate.get("nonlocal_form")
    if isinstance(form, str) and form:
        return form
    expected = candidate.get("expected_nonlocal_form")
    return expected if isinstance(expected, str) else ""


def _has_nonlocal_signature(text: str) -> bool:
    normalized = text.lower()
    return any(token in normalized for token in ["log", "branch", "imag", "epsilon"])


def _overlap_terms(form: str) -> List[str]:
    normalized = form.lower()
    overlaps: List[str] = []

    if "r log" in normalized:
        overlaps.extend(["R_squared", "box_R", "Einstein_Hilbert"])
    if "weyl log" in normalized:
        overlaps.append("Weyl_squared")
    if "ricci" in normalized and "log" in normalized:
        overlaps.append("Ricci_squared")
    if "riemann" in normalized and "log" in normalized:
        overlaps.append("Riemann_squared")

    return [term for term in overlaps if term in _LOCAL_COUNTERTERMS]


def evaluate_counterterm_overlap(candidate: Dict[str, object]) -> Dict[str, object]:
    form = _extract_form(candidate)
    overlap_terms = _overlap_terms(form)
    nonlocal_preserved = _has_nonlocal_signature(form)

    return {
        "kernel_id": candidate.get("kernel_id"),
        "overlaps_local_counterterms": bool(overlap_terms),
        "overlap_terms": overlap_terms,
        "nonlocal_structure_preserved": nonlocal_preserved,
        "promotes_claims": False,
    }
