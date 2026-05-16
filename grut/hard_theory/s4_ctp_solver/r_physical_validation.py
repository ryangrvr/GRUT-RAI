"""Validate physical properties of isolated R structure."""

from typing import Dict


def validate_r_physical_properties(
    symbolic_r: Dict[str, object], cancellation: Dict[str, object]
) -> Dict[str, object]:
    numerator = symbolic_r.get("numerator", {})
    denominator = symbolic_r.get("denominator", {})

    dimensionless_ok = (
        numerator.get("dimensionless") is True and denominator.get("dimensionless") is True
    )
    scheme_metadata_present = bool(
        symbolic_r.get("scheme_tags")
        and numerator.get("scheme_tags")
        and denominator.get("scheme_tags")
    )
    scheme_invariant = cancellation.get("scheme_dependence_cancelled") is True
    regulator_independent = cancellation.get("regulator_dependence_cancelled") is True

    valid = (
        dimensionless_ok
        and scheme_metadata_present
        and scheme_invariant
        and regulator_independent
    )
    reason = "physical_checks_pass" if valid else "physical_checks_failed"

    return {
        "dimensionless": dimensionless_ok,
        "scheme_metadata_present": scheme_metadata_present,
        "scheme_invariant": scheme_invariant,
        "regulator_independent": regulator_independent,
        "valid": valid,
        "reason": reason,
        "promotes_claims": False,
    }
