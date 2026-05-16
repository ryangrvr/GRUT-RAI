"""Register protected source candidates from readiness outputs."""

from __future__ import annotations

from typing import Dict, List


def _kernel_id_from(candidate: Dict[str, object], source_type: str) -> str:
    kernel_id = candidate.get("kernel_id")
    if isinstance(kernel_id, str) and kernel_id:
        return kernel_id
    return f"{source_type}_kernel"


def _nonlocal_present(candidate: Dict[str, object]) -> bool:
    if candidate.get("nonlocal_form_present") is True:
        return True
    form = candidate.get("nonlocal_form")
    return isinstance(form, str) and bool(form.strip())


def register_protected_source_candidates(
    stage_p5: Dict[str, object],
    stage_p4: Dict[str, object],
    scheme_status: str,
) -> List[Dict[str, object]]:
    p4_candidates = {entry.get("source_type"): entry.get("candidate", {}) for entry in stage_p4.get("integrated_candidates", [])}

    registered: List[Dict[str, object]] = []
    for record in stage_p5.get("readiness_candidates", []):
        source_type = record.get("source_type")
        candidate = record.get("candidate", {})
        p4_candidate = p4_candidates.get(source_type, {})
        kernel_id = _kernel_id_from(candidate, source_type)

        nonlocal_present = _nonlocal_present(p4_candidate) or _nonlocal_present(candidate)

        registered.append(
            {
                "protected_source_candidate_id": f"protected_{source_type}_candidate",
                "source_type": source_type,
                "kernel_id": kernel_id,
                "nonlocal_form_present": nonlocal_present,
                "counterterm_nonmixing_verified": record.get("nonmixing", {}).get(
                    "counterterm_nonmixing_verified"
                )
                is True,
                "finite_extractability": record.get("finite_extractability", {}).get(
                    "finite_extractability"
                )
                is True,
                "coefficient_value": None,
                "scheme_protection_status": scheme_status,
                "physical_coefficient_claimed": False,
                "promotes_claims": False,
            }
        )

    return registered
