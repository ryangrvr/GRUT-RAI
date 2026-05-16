"""Reference scheme definition for alignment checks."""

from typing import Dict, List


def define_reference_scheme() -> Dict[str, object]:
    invariant_basis: List[str] = [
        "R_squared",
        "Weyl_squared",
        "Euler_density",
        "box_R",
    ]
    return {
        "scheme_id": "reference_scheme_v1",
        "regulator": "dimensional_regularization",
        "subtraction": "ms_bar_placeholder",
        "normalization": "unit_radius_s4",
        "invariant_basis": invariant_basis,
        "status": "defined_not_validated",
        "promotes_claims": False,
    }
