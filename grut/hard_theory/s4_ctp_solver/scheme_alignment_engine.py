"""Align native attempt structures to a reference scheme basis."""

from typing import Dict, List

import sympy as sp


def _stringify(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    if isinstance(value, sp.Basic):
        return str(value)
    return str(value)


def _normalize(text: str) -> str:
    return "".join(text.lower().split())


def _infer_invariant(normalized: str) -> str:
    if "euler" in normalized:
        return "Euler_density"
    if "weyl" in normalized:
        return "Weyl_squared"
    if "box_r" in normalized or "boxr" in normalized:
        return "box_R"
    if "r_squared" in normalized or "r^2" in normalized:
        return "R_squared"
    if "r_log_box_r" in normalized or "rlogboxr" in normalized:
        return "nonlocal_R_log_box_R"
    return "unknown"


def _tag_scheme(invariant: str) -> str:
    if invariant in {"Euler_density", "Weyl_squared", "nonlocal_R_log_box_R"}:
        return "scheme_protected_candidate"
    if invariant == "box_R":
        return "total_derivative_scheme_dependent"
    if invariant == "R_squared":
        return "scheme_fragile"
    return "unknown"


def align_to_scheme(native_attempt_result: Dict[str, object], scheme: Dict[str, object]) -> Dict[str, object]:
    fields = [
        "expression",
        "divergence_structure",
        "combined_structure",
        "ctp_imaginary_scaffold",
    ]
    aligned_terms: List[Dict[str, str]] = []
    scheme_tags: List[str] = []

    for field in fields:
        if field not in native_attempt_result:
            continue
        term = _stringify(native_attempt_result[field])
        if not term:
            continue
        normalized = _normalize(term)
        invariant = _infer_invariant(normalized)
        scheme_tag = _tag_scheme(invariant)
        aligned_terms.append(
            {
                "term": term,
                "invariant": invariant,
                "scheme_tag": scheme_tag,
            }
        )
        scheme_tags.append(scheme_tag)

    return {
        "topology_id": native_attempt_result.get("topology_id", "unknown_topology"),
        "scheme_id": scheme.get("scheme_id"),
        "aligned_terms": aligned_terms,
        "scheme_tags": scheme_tags,
        "status": "aligned_structural",
        "promotes_claims": False,
    }
