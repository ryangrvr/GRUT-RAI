"""Integrate P3 nonlocal candidates into P2 kernel records."""

from __future__ import annotations

from copy import deepcopy
from typing import Dict, List


def _build_p3_candidate_map(stage_p3: Dict[str, object]) -> Dict[str, Dict[str, object]]:
    mapping: Dict[str, Dict[str, object]] = {}
    for entry in stage_p3.get("candidates_constructed", []):
        target = entry.get("target")
        candidate = entry.get("candidate", {})
        if isinstance(target, str) and target:
            mapping[target] = candidate
    return mapping


def _integrate_candidate(
    base_candidate: Dict[str, object],
    p3_candidate: Dict[str, object],
) -> Dict[str, object]:
    updated = deepcopy(base_candidate)
    updated["status"] = "symbolic_candidate"
    updated["derivation_kind"] = "symbolic"
    updated["scaffold_only"] = False
    updated["nonlocal_form_present"] = True
    updated["local_counterterm_nonmixing_checked"] = False
    updated["finite_coefficient_extractable"] = False
    updated["coefficient"] = "symbolic_uncomputed"
    updated["nonlocal_form"] = p3_candidate.get("nonlocal_form")
    if not updated.get("expected_nonlocal_form"):
        updated["expected_nonlocal_form"] = p3_candidate.get("nonlocal_form")
    updated["promotes_claims"] = False
    return updated


def integrate_nonlocal_kernels(
    stage_p2: Dict[str, object],
    stage_p3: Dict[str, object],
) -> List[Dict[str, object]]:
    p3_map = _build_p3_candidate_map(stage_p3)

    p2_entries: List[Dict[str, object]] = []
    p2_entries.extend(stage_p2.get("accepted_kernels", []))
    p2_entries.extend(stage_p2.get("failed_kernels", []))

    integrated: List[Dict[str, object]] = []
    for entry in p2_entries:
        source_type = entry.get("source_type")
        base_candidate = entry.get("candidate", {})
        candidate = deepcopy(base_candidate)

        p3_candidate = p3_map.get(source_type)
        if p3_candidate:
            candidate = _integrate_candidate(base_candidate, p3_candidate)

        integrated.append(
            {
                "source_type": source_type,
                "candidate": candidate,
                "regulator_check": deepcopy(entry.get("regulator_check", {})),
                "ward_ctp_check": deepcopy(entry.get("ward_ctp_check", {})),
                "promotes_claims": False,
            }
        )

    return integrated
