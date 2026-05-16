"""Define symbolic integration domains for loop integrals."""

from typing import Dict


def define_integration_domain() -> Dict[str, object]:
    return {
        "domain_type": "symbolic_momentum_or_spectral",
        "limits": "unspecified_symbolic",
        "regularization_dependent": True,
        "status": "domain_defined_symbolic",
        "promotes_claims": False,
    }
