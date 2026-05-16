"""Cross-topology comparison for Stage 5B."""

from typing import Dict, List


def compare_native_attempts(results: List[Dict[str, object]]) -> Dict[str, object]:
    divergences = {result.get("divergence_structure") for result in results}
    scheme_present = all(
        any(step.get("stage") == "scheme_tagging" for step in result.get("evaluation_steps", []))
        for result in results
    )

    differences = []
    if len(divergences) > 1:
        differences.append("divergence_structure_mismatch")
    if not scheme_present:
        differences.append("missing_scheme_metadata")

    if differences:
        status = "inconclusive"
    else:
        status = "consistent"

    return {
        "comparison_type": "cross_topology",
        "status": status,
        "differences": differences,
        "promotes_claims": False,
    }
