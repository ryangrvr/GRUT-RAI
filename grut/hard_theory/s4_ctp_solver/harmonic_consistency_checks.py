"""Harmonic decomposition consistency checks (structural)."""

from typing import Dict, List


def check_harmonic_consistency(
    spectra: Dict[str, object],
    vector_structure: Dict[str, object],
    tensor_structure: Dict[str, object],
) -> Dict[str, object]:
    issues: List[str] = []

    scalar_modes = spectra.get("scalar_modes", [])
    vector_modes = spectra.get("vector_modes", [])
    tensor_modes = spectra.get("tensor_modes", [])

    if not scalar_modes:
        issues.append("missing_scalar_modes")
    if not vector_modes:
        issues.append("missing_vector_modes")
    if not tensor_modes:
        issues.append("missing_tensor_modes")

    components = vector_structure.get("components", [])
    if "transverse" not in components or "longitudinal" not in components:
        issues.append("vector_decomposition_incomplete")

    tensor_components = tensor_structure.get("components", [])
    if "TT_placeholder" not in tensor_components:
        issues.append("tt_placeholder_missing")

    status = "consistent" if not issues else "incomplete"

    return {
        "consistency": "harmonic_decomposition",
        "status": status,
        "issues": issues,
        "promotes_claims": False,
    }
