"""Detect repeated symbolic structures across native attempts."""

from typing import Dict, Iterable, List, Tuple

import sympy as sp

from grut.hard_theory.s4_ctp_solver.candidate_structure_registry import (
    create_candidate_record,
)


def _stringify(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    if isinstance(value, sp.Basic):
        return str(value)
    return str(value)


def _normalize_form(text: str) -> str:
    return "".join(text.lower().split())


def _infer_invariant(normalized: str) -> str:
    if "euler" in normalized:
        return "Euler_density"
    if "weyl" in normalized:
        return "Weyl_squared"
    if "box_r" in normalized or "boxr" in normalized or "□r" in normalized:
        return "box_R"
    if "r_squared" in normalized or "r^2" in normalized:
        return "R_squared"
    if "r_log_box_r" in normalized or "rlogboxr" in normalized:
        return "nonlocal_R_log_box_R"
    return "unknown"


def _extract_structures(result: Dict[str, object]) -> Iterable[Tuple[str, str]]:
    topology_id = str(result.get("topology_id", "unknown_topology"))
    fields = ["expression", "divergence_structure", "combined_structure"]
    for field in fields:
        if field in result:
            text = _stringify(result[field])
            if text:
                yield topology_id, text


def detect_candidate_structures(native_attempt_results: List[Dict[str, object]]) -> Dict[str, object]:
    occurrences: Dict[str, Dict[str, object]] = {}

    for result in native_attempt_results:
        for topology_id, symbolic_form in _extract_structures(result):
            normalized = _normalize_form(symbolic_form)
            entry = occurrences.setdefault(
                normalized,
                {"count": 0, "topologies": set(), "symbolic_form": symbolic_form},
            )
            entry["count"] += 1
            entry["topologies"].add(topology_id)

    candidates: List[Dict[str, object]] = []
    for idx, (normalized, entry) in enumerate(occurrences.items(), start=1):
        if entry["count"] < 2:
            continue
        associated_invariant = _infer_invariant(normalized)
        candidates.append(
            create_candidate_record(
                candidate_id=f"candidate_{idx}",
                source_topologies=sorted(entry["topologies"]),
                symbolic_form=entry["symbolic_form"],
                associated_invariant=associated_invariant,
                scheme_sensitivity="unknown",
                occurrence_count=entry["count"],
            )
        )

    status = "candidates_detected" if candidates else "no_candidates_detected"

    return {
        "status": status,
        "candidates": candidates,
        "promotes_claims": False,
    }
