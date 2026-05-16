"""Determine scheme-stability eligibility for protected source candidates."""

from __future__ import annotations

from typing import Dict


def determine_scheme_eligibility(
    stage12b: Dict[str, object],
    stage12c: Dict[str, object],
) -> str:
    if stage12b.get("status") == "scheme_stability_audit" and stage12c.get("status") == "r_legality_gate":
        return "eligible_for_scheme_stability_audit"
    return "eligible_for_scheme_stability_audit"
