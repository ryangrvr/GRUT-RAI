"""Scheme-sensitivity classification for GRUT-relevant quantities."""

from typing import Dict


def classify_scheme_sensitivity(quantity_name: str) -> Dict[str, object]:
    normalized = quantity_name.strip()
    if normalized == "a":
        return {
            "quantity": "a",
            "classification": "scheme_protected_benchmarked",
            "reason": "1-loop Euler anomaly coefficient is scheme-protected.",
        }
    if normalized == "c":
        return {
            "quantity": "c",
            "classification": "scheme_protected_benchmarked",
            "reason": "1-loop Weyl anomaly coefficient is scheme-protected.",
        }
    if normalized == "b" or normalized == "box_R":
        return {
            "quantity": "box_R",
            "classification": "scheme_dependent_total_derivative",
            "reason": "□R is scheme-dependent and total-derivative.",
        }
    if normalized == "C_Cosmo":
        return {
            "quantity": "C_Cosmo",
            "classification": "scheme_fragile_local",
            "reason": "Local cosmological coefficient is scheme-fragile.",
        }
    if normalized == "C_Final":
        return {
            "quantity": "C_Final",
            "classification": "scheme_protected_candidate",
            "reason": "Nonlocal coefficient may be scheme-protected.",
        }
    if normalized == "R_ratio":
        return {
            "quantity": "R_ratio",
            "classification": "depends_on_scheme_alignment",
            "reason": "Meaningful only if numerator/denominator are scheme-aligned.",
        }
    return {
        "quantity": normalized,
        "classification": "unknown",
        "reason": "No scheme classification recorded.",
    }
