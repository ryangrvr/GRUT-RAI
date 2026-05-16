"""Assign protected kernel candidates to legacy coefficient roles."""

from typing import Dict, List


_C_FINAL_ALLOWED_SOURCES = {
    "R_log_box_R",
    "Weyl_log_box_Weyl",
}

_C_COSMO_ALLOWED_SOURCES = {
    "C_Cosmo_log_box_Cosmo",
}

_CTP_CAUSAL_SOURCES = {
    "Im_log_minus_box_i_epsilon",
    "CTP_Keldysh_causal_response_kernel",
}


def _registered_candidates(stage_p7: Dict[str, object]) -> List[Dict[str, object]]:
    stage_p6 = stage_p7.get("stage_p6", {})
    return list(stage_p6.get("registered_candidates", []))


def _scheme_protected_ids(stage_p7: Dict[str, object]) -> set[str]:
    return {
        entry.get("candidate_id")
        for entry in stage_p7.get("scheme_protected_candidates", [])
        if entry.get("candidate_id")
    }


def _eligible_nonlocal(candidate: Dict[str, object]) -> bool:
    return (
        candidate.get("nonlocal_form_present") is True
        and candidate.get("counterterm_nonmixing_verified") is True
        and candidate.get("finite_extractability") is True
        and candidate.get("coefficient_value") is None
    )


def assign_protected_kernel_roles(
    stage_p7: Dict[str, object],
    stage12a: Dict[str, object],
) -> Dict[str, object]:
    protected_ids = _scheme_protected_ids(stage_p7)

    candidates: List[Dict[str, object]] = []
    for entry in _registered_candidates(stage_p7):
        candidate_id = entry.get("protected_source_candidate_id")
        candidates.append(
            {
                "candidate_id": candidate_id,
                "source_type": entry.get("source_type"),
                "kernel_id": entry.get("kernel_id"),
                "nonlocal_form_present": entry.get("nonlocal_form_present") is True,
                "counterterm_nonmixing_verified": entry.get("counterterm_nonmixing_verified")
                is True,
                "finite_extractability": entry.get("finite_extractability") is True,
                "coefficient_value": entry.get("coefficient_value"),
                "scheme_protected": candidate_id in protected_ids,
                "promotes_claims": False,
            }
        )

    c_final_candidates = [
        candidate
        for candidate in candidates
        if candidate.get("scheme_protected")
        and candidate.get("source_type") in _C_FINAL_ALLOWED_SOURCES
        and _eligible_nonlocal(candidate)
    ]

    c_cosmo_candidates = [
        candidate
        for candidate in candidates
        if candidate.get("scheme_protected")
        and candidate.get("source_type") in _C_COSMO_ALLOWED_SOURCES
        and _eligible_nonlocal(candidate)
    ]

    ctp_causal_candidates = [
        candidate
        for candidate in candidates
        if candidate.get("scheme_protected")
        and candidate.get("source_type") in _CTP_CAUSAL_SOURCES
        and _eligible_nonlocal(candidate)
    ]

    return {
        "candidates": candidates,
        "c_final_candidates": c_final_candidates,
        "c_cosmo_candidates": c_cosmo_candidates,
        "ctp_causal_candidates": ctp_causal_candidates,
        "explicit_cosmo_kernel_present": bool(c_cosmo_candidates),
        "candidate_registry": stage12a.get("registry", {}),
        "promotes_claims": False,
    }
