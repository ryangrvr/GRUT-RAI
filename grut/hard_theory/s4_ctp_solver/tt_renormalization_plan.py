"""Dry-run renormalization plan for TT inversion."""

from typing import Dict, List


def build_tt_renormalization_plan(mapping: Dict[str, object]) -> Dict[str, object]:
    counterterms = mapping.get("counterterms_required", [])
    subtractions_required: List[str] = list(counterterms)

    return {
        "plan_id": "tt_renormalization_dry_run",
        "subtractions_required": subtractions_required,
        "finite_parts": "not_computed",
        "renormalization_performed": False,
        "status": "dry_run_only",
        "promotes_claims": False,
    }
