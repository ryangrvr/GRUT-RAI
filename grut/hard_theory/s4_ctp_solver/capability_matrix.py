"""Capability matrix for Stage 3F external audit."""

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class CapabilityRow:
    capability: str
    status: str
    evidence: str
    test_reference: str
    promotes_claims: bool


def build_capability_matrix() -> List[CapabilityRow]:
    return [
        CapabilityRow(
            capability="represent S4 geometry",
            status="available",
            evidence="conventions module",
            test_reference="tests/hard_theory/s4_ctp_solver/test_s4_ctp_scaffold.py",
            promotes_claims=False,
        ),
        CapabilityRow(
            capability="reproduce 1-loop anomaly coefficients",
            status="benchmarked",
            evidence="Stage 2 anomaly modules",
            test_reference="tests/hard_theory/s4_ctp_solver/test_stage2_benchmarks.py",
            promotes_claims=False,
        ),
        CapabilityRow(
            capability="represent 3-loop topologies",
            status="speculative_internal",
            evidence="diagram_topologies",
            test_reference="tests/hard_theory/s4_ctp_solver/test_stage3_partials.py",
            promotes_claims=False,
        ),
        CapabilityRow(
            capability="create scalar Green spectral truncation",
            status="benchmarked",
            evidence="s4_green_functions",
            test_reference="tests/hard_theory/s4_ctp_solver/test_stage3b_s4_ingredients.py",
            promotes_claims=False,
        ),
        CapabilityRow(
            capability="represent tensor harmonic placeholders",
            status="scaffold_only",
            evidence="tensor_harmonics",
            test_reference="tests/hard_theory/s4_ctp_solver/test_stage3b_s4_ingredients.py",
            promotes_claims=False,
        ),
        CapabilityRow(
            capability="audit Ward identities structurally",
            status="scaffold_only",
            evidence="ward_tensor_checks",
            test_reference="tests/hard_theory/s4_ctp_solver/test_stage3c_tensor_ward.py",
            promotes_claims=False,
        ),
        CapabilityRow(
            capability="track counterterms/schemes",
            status="scaffold_only",
            evidence="counterterms/divergence_structure",
            test_reference="tests/hard_theory/s4_ctp_solver/test_stage3d_renormalization_scheme.py",
            promotes_claims=False,
        ),
        CapabilityRow(
            capability="cross-check routes",
            status="scaffold_only",
            evidence="crosscheck_audit",
            test_reference="tests/hard_theory/s4_ctp_solver/test_stage3e_crosschecks.py",
            promotes_claims=False,
        ),
        CapabilityRow(
            capability="compute full 3-loop S4 CTP action",
            status="not_available",
            evidence="explicitly forbidden in ladder",
            test_reference="",
            promotes_claims=False,
        ),
    ]
