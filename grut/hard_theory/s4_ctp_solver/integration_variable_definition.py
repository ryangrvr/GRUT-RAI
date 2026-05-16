"""Define symbolic integration variables for the dry-run plan."""

from typing import Dict, List


def define_integration_variables() -> Dict[str, object]:
    variables: List[str] = ["k1", "k2", "k3"]
    return {
        "variables": variables,
        "dimension": "d-dimensional_placeholder",
        "status": "defined_symbolic",
        "promotes_claims": False,
    }
