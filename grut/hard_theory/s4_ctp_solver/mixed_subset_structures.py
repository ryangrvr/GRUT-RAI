"""Mixed subset symbolic structures for Stage 4E."""

from dataclasses import dataclass
from typing import Dict

import sympy as sp

from grut.hard_theory.s4_ctp_solver.three_loop_subset_s4_mixed import S4MixedSubsetTopology


@dataclass(frozen=True)
class MixedSubsetStructure:
    scalar_part_reference: str
    tensor_structure_reference: str
    coupling_structure: sp.Expr
    index_structure: sp.Expr
    scheme_metadata: Dict[str, str]
    status: str


def build_mixed_structure(topology: S4MixedSubsetTopology) -> MixedSubsetStructure:
    return MixedSubsetStructure(
        scalar_part_reference="stage4c_scalar_subset",
        tensor_structure_reference="stage4d_tensor_structure",
        coupling_structure=sp.Symbol("g_scalar_tensor"),
        index_structure=sp.Symbol("C_mixed_mu_nu"),
        scheme_metadata={"scheme": "ms_bar", "regulator": "dim_reg"},
        status="mixed_symbolic_structure",
    )
