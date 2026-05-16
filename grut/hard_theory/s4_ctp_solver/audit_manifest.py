"""Audit manifest for Stage 3F external review."""

from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class AuditStageEntry:
    stage_id: str
    status: str
    implemented_modules: List[str]
    test_file: str
    allowed_claim_tier: str
    explicitly_forbidden_claims: List[str]
    promotion_requirements: List[str]
    current_limitations: List[str]


def build_audit_manifest() -> Dict[str, AuditStageEntry]:
    return {
        "Stage 1": AuditStageEntry(
            stage_id="Stage 1",
            status="scaffold",
            implemented_modules=["conventions", "diagrams", "pipeline"],
            test_file="tests/hard_theory/s4_ctp_solver/test_s4_ctp_scaffold.py",
            allowed_claim_tier="scaffold",
            explicitly_forbidden_claims=["fully_evaluated", "derived", "evaluated"],
            promotion_requirements=["propagators", "vertices", "scheme", "regulator"],
            current_limitations=["no evaluated diagrams", "no propagator kernels"],
        ),
        "Stage 2": AuditStageEntry(
            stage_id="Stage 2",
            status="benchmarked",
            implemented_modules=[
                "heat_kernel",
                "anomaly_1loop_scalar",
                "anomaly_1loop_weyl",
                "anomaly_1loop_gauge",
            ],
            test_file="tests/hard_theory/s4_ctp_solver/test_stage2_benchmarks.py",
            allowed_claim_tier="benchmarked",
            explicitly_forbidden_claims=["fully_evaluated", "full_3loop"],
            promotion_requirements=["independent replication"],
            current_limitations=["benchmarks only", "no new physics"],
        ),
        "Stage 3": AuditStageEntry(
            stage_id="Stage 3",
            status="speculative_internal",
            implemented_modules=[
                "diagram_topologies",
                "three_loop_partials",
                "asymptotic_expansions",
                "ward_audit",
            ],
            test_file="tests/hard_theory/s4_ctp_solver/test_stage3_partials.py",
            allowed_claim_tier="speculative_internal",
            explicitly_forbidden_claims=["fully_evaluated", "verified"],
            promotion_requirements=["full tensor contraction", "ward verification"],
            current_limitations=["partial expansions", "no evaluated integrals"],
        ),
        "Stage 3B": AuditStageEntry(
            stage_id="Stage 3B",
            status="ingredient_benchmarked_scaffold",
            implemented_modules=[
                "s4_spectral_basis",
                "s4_green_functions",
                "propagator_benchmarks",
                "contraction_engine",
            ],
            test_file="tests/hard_theory/s4_ctp_solver/test_stage3b_s4_ingredients.py",
            allowed_claim_tier="ingredient_benchmarked_scaffold",
            explicitly_forbidden_claims=["fully_evaluated", "full_3loop"],
            promotion_requirements=["explicit S4 propagators"],
            current_limitations=["truncated spectra", "placeholders for tensor modes"],
        ),
        "Stage 3C": AuditStageEntry(
            stage_id="Stage 3C",
            status="tensor_structural_audit",
            implemented_modules=[
                "s4_tensor_spectrum",
                "tt_projector",
                "graviton_decomposition",
                "ward_tensor_checks",
            ],
            test_file="tests/hard_theory/s4_ctp_solver/test_stage3c_tensor_ward.py",
            allowed_claim_tier="tensor_structural_audit",
            explicitly_forbidden_claims=["fully_evaluated", "evaluated"],
            promotion_requirements=["explicit TT spectrum", "projector kernel"],
            current_limitations=["structural checks only"],
        ),
        "Stage 3D": AuditStageEntry(
            stage_id="Stage 3D",
            status="renormalization_scheme_audit",
            implemented_modules=[
                "counterterms",
                "divergence_structure",
                "scheme_invariants",
                "renormalization_audit",
            ],
            test_file="tests/hard_theory/s4_ctp_solver/test_stage3d_renormalization_scheme.py",
            allowed_claim_tier="renormalization_scheme_audit",
            explicitly_forbidden_claims=["fully_evaluated", "renormalized_coefficients"],
            promotion_requirements=["explicit subtraction", "finite parts"],
            current_limitations=["no renormalized coefficients"],
        ),
        "Stage 3E": AuditStageEntry(
            stage_id="Stage 3E",
            status="crosscheck_audit",
            implemented_modules=[
                "crosscheck_registry",
                "crosscheck_routes",
                "consistency_metrics",
                "crosscheck_audit",
            ],
            test_file="tests/hard_theory/s4_ctp_solver/test_stage3e_crosschecks.py",
            allowed_claim_tier="crosscheck_audit",
            explicitly_forbidden_claims=["fully_evaluated", "fully_verified"],
            promotion_requirements=["fully evaluated routes"],
            current_limitations=["partial/inconclusive comparisons"],
        ),
    }
