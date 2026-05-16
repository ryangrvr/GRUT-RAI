"""Audit for TT renormalization dry-run."""

from typing import Dict


def audit_tt_renormalization_dry_run(
    plan: Dict[str, object], scheme_check: Dict[str, object]
) -> Dict[str, object]:
    no_subtraction = plan.get("renormalization_performed") is False
    no_finite_parts = plan.get("finite_parts") == "not_computed"
    counterterms_tracked = bool(plan.get("subtractions_required"))
    scheme_present = "scheme_alignment" in scheme_check

    status = (
        "valid_dry_run"
        if all([no_subtraction, no_finite_parts, counterterms_tracked, scheme_present])
        else "invalid"
    )

    return {
        "audit": "tt_renormalization_dry_run",
        "status": status,
        "renormalization_performed": False,
        "finite_parts_computed": False,
        "promotes_claims": False,
    }
