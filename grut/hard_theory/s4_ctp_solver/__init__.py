"""GRUT-RAI v3 Hard-Theory Benchmark: S4 CTP Solver scaffolding."""

from grut.hard_theory.s4_ctp_solver.conventions import S4Geometry, s4_volume
from grut.hard_theory.s4_ctp_solver.ctp_fields import keldysh_basis, inverse_keldysh
from grut.hard_theory.s4_ctp_solver.propagators import (
    PropagatorPlaceholder,
    graviton_propagator_placeholder,
    ghost_propagator_placeholder,
    matter_propagator_placeholder,
    kernel_placeholders,
)
from grut.hard_theory.s4_ctp_solver.diagrams import Diagram
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline
from grut.hard_theory.s4_ctp_solver.diagram_topologies import DiagramTopology
from grut.hard_theory.s4_ctp_solver.three_loop_partials import ThreeLoopPartial
from grut.hard_theory.s4_ctp_solver.s4_spectral_basis import ScalarSpectralMode
from grut.hard_theory.s4_ctp_solver.s4_green_functions import ScalarGreenTruncation
from grut.hard_theory.s4_ctp_solver.s4_tensor_spectrum import TensorSpectralRecord
from grut.hard_theory.s4_ctp_solver.tt_projector import TTProjectorRecord
from grut.hard_theory.s4_ctp_solver.counterterms import CountertermRecord
from grut.hard_theory.s4_ctp_solver.divergence_structure import DivergenceRecord
from grut.hard_theory.s4_ctp_solver.crosscheck_registry import CrosscheckQuantity
from grut.hard_theory.s4_ctp_solver.crosscheck_routes import RouteResult
from grut.hard_theory.s4_ctp_solver.audit_manifest import AuditStageEntry
from grut.hard_theory.s4_ctp_solver.capability_matrix import CapabilityRow
from grut.hard_theory.s4_ctp_solver.summary_report import build_summary_report
from grut.hard_theory.s4_ctp_solver.known_results_library import KnownResult
from grut.hard_theory.s4_ctp_solver.toy_integrals_flat import ToyIntegralResult
from grut.hard_theory.s4_ctp_solver.toy_integrals_curved import CurvedToyResult
from grut.hard_theory.s4_ctp_solver.three_loop_subset_flat import SubsetTopology
from grut.hard_theory.s4_ctp_solver.three_loop_subset_s4_scalar import S4SubsetTopology
from grut.hard_theory.s4_ctp_solver.three_loop_subset_s4_tensor import S4TensorSubsetTopology
from grut.hard_theory.s4_ctp_solver.three_loop_subset_s4_mixed import S4MixedSubsetTopology
from grut.hard_theory.s4_ctp_solver.native_attempt_topology import NativeAttemptTopology
from grut.hard_theory.s4_ctp_solver.native_attempt_topology_set import NativeAttemptTopologyEntry
from grut.hard_theory.s4_ctp_solver.native_attempt_tensor_deep import TensorNativeAttemptTopology
from grut.hard_theory.s4_ctp_solver.tensor_native_report import render_tensor_native_report
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import enforce_tensor_placeholder_guard
from grut.hard_theory.s4_ctp_solver.blocker_registry import register_blockers
from grut.hard_theory.s4_ctp_solver.blocker_dependency_graph import (
    build_blocker_dependency_graph,
    graph_is_acyclic,
    graph_edges,
)
from grut.hard_theory.s4_ctp_solver.blocker_closure_plan import build_blocker_closure_plan
from grut.hard_theory.s4_ctp_solver.blocker_progress_audit import run_blocker_progress_audit
from grut.hard_theory.s4_ctp_solver.stage6b_multi_blocker_harness import (
    run_stage6b_multi_blocker_harness,
)
from grut.hard_theory.s4_ctp_solver.s4_scalar_propagator_closed_form import (
    build_conformal_scalar_propagator_closed_form,
)
from grut.hard_theory.s4_ctp_solver.scalar_propagator_validation import (
    validate_conformal_scalar_propagator,
    compare_spectral_to_closed_form,
)
from grut.hard_theory.s4_ctp_solver.scalar_propagator_convergence import (
    diagnose_scalar_spectral_convergence,
)
from grut.hard_theory.s4_ctp_solver.scalar_propagator_blocker_update import (
    update_full_s4_propagator_blocker_scalar_only,
)
from grut.hard_theory.s4_ctp_solver.stage6c_scalar_propagator import (
    run_stage6c_scalar_propagator,
)
from grut.hard_theory.s4_ctp_solver.s4_ghost_operator import define_ghost_operator
from grut.hard_theory.s4_ctp_solver.s4_ghost_propagator import (
    build_ghost_propagator_structure,
)
from grut.hard_theory.s4_ctp_solver.ghost_propagator_validation import (
    validate_ghost_propagator,
)
from grut.hard_theory.s4_ctp_solver.ghost_propagator_blocker_update import (
    update_ghost_blocker_status,
)
from grut.hard_theory.s4_ctp_solver.stage6d_ghost_propagator import (
    run_stage6d_ghost_propagator,
)
from grut.hard_theory.s4_ctp_solver.s4_harmonic_spectra import (
    define_s4_harmonic_spectra,
)
from grut.hard_theory.s4_ctp_solver.s4_vector_harmonics import (
    build_vector_harmonics_structure,
)
from grut.hard_theory.s4_ctp_solver.s4_tensor_harmonics_extended import (
    extend_tensor_harmonics,
)
from grut.hard_theory.s4_ctp_solver.harmonic_consistency_checks import (
    check_harmonic_consistency,
)
from grut.hard_theory.s4_ctp_solver.stage6e_harmonic_benchmark import (
    run_stage6e_harmonic_benchmark,
)
from grut.hard_theory.s4_ctp_solver.s4_tt_operator import define_tt_operator
from grut.hard_theory.s4_ctp_solver.s4_tt_projector_extended import extend_tt_projector
from grut.hard_theory.s4_ctp_solver.s4_tt_propagator_scaffold import (
    build_tt_propagator_scaffold,
)
from grut.hard_theory.s4_ctp_solver.tt_propagator_validation import (
    validate_tt_scaffold,
)
from grut.hard_theory.s4_ctp_solver.tt_propagator_blocker_update import (
    update_tt_blocker_status,
)
from grut.hard_theory.s4_ctp_solver.stage6f_tt_propagator import (
    run_stage6f_tt_propagator,
)
from grut.hard_theory.s4_ctp_solver.s4_tt_mode_decomposition import (
    define_tt_mode_decomposition,
)
from grut.hard_theory.s4_ctp_solver.s4_tt_eigenvalues import define_tt_eigenvalues
from grut.hard_theory.s4_ctp_solver.s4_tt_degeneracies import define_tt_degeneracies
from grut.hard_theory.s4_ctp_solver.s4_tt_zero_mode_handling import (
    define_zero_mode_strategy,
)
from grut.hard_theory.s4_ctp_solver.s4_tt_inversion_strategy import (
    define_spectral_inversion_strategy,
)
from grut.hard_theory.s4_ctp_solver.stage6g_spectral_strategy import (
    run_stage6g_spectral_strategy,
)
from grut.hard_theory.s4_ctp_solver.tt_regularization_schemes import (
    define_regularization_schemes,
)
from grut.hard_theory.s4_ctp_solver.tt_regularized_inversion import (
    perform_regularized_tt_inversion,
)
from grut.hard_theory.s4_ctp_solver.tt_regularization_comparison import (
    compare_regularization_results,
)
from grut.hard_theory.s4_ctp_solver.tt_regularization_audit import (
    audit_regularized_inversion,
)
from grut.hard_theory.s4_ctp_solver.stage7e_tt_regularization import (
    run_stage7e_tt_regularization,
)
from grut.hard_theory.s4_ctp_solver.tt_divergence_to_counterterms import (
    map_tt_divergences_to_counterterms,
)
from grut.hard_theory.s4_ctp_solver.tt_renormalization_plan import (
    build_tt_renormalization_plan,
)
from grut.hard_theory.s4_ctp_solver.tt_scheme_alignment_check import (
    check_tt_scheme_alignment,
)
from grut.hard_theory.s4_ctp_solver.tt_renormalization_audit import (
    audit_tt_renormalization_dry_run,
)
from grut.hard_theory.s4_ctp_solver.stage7f_tt_renormalization_dry_run import (
    run_stage7f_tt_renormalization_dry_run,
)
from grut.hard_theory.s4_ctp_solver.finite_part_requirements import (
    define_finite_part_requirements,
)
from grut.hard_theory.s4_ctp_solver.finite_part_readiness_checks import (
    evaluate_finite_part_readiness,
)
from grut.hard_theory.s4_ctp_solver.finite_part_blockers import (
    identify_finite_part_blockers,
)
from grut.hard_theory.s4_ctp_solver.finite_part_eligibility_decision import (
    decide_finite_part_eligibility,
)
from grut.hard_theory.s4_ctp_solver.stage7g_finite_part_audit import (
    run_stage7g_finite_part_audit,
)
from grut.hard_theory.s4_ctp_solver.tt_convergence_metrics import (
    compute_tt_convergence_metrics,
)
from grut.hard_theory.s4_ctp_solver.tt_convergence_thresholds import (
    define_convergence_thresholds,
)
from grut.hard_theory.s4_ctp_solver.tt_convergence_repair import (
    evaluate_convergence_repair,
)
from grut.hard_theory.s4_ctp_solver.tt_convergence_audit import (
    audit_convergence_repair,
)
from grut.hard_theory.s4_ctp_solver.stage7i_convergence_repair import (
    run_stage7i_convergence_repair,
)

__all__ = [
    "S4Geometry",
    "s4_volume",
    "keldysh_basis",
    "inverse_keldysh",
    "PropagatorPlaceholder",
    "graviton_propagator_placeholder",
    "ghost_propagator_placeholder",
    "matter_propagator_placeholder",
    "kernel_placeholders",
    "Diagram",
    "S4CTPPipeline",
    "DiagramTopology",
    "ThreeLoopPartial",
    "ScalarSpectralMode",
    "ScalarGreenTruncation",
    "TensorSpectralRecord",
    "TTProjectorRecord",
    "CountertermRecord",
    "DivergenceRecord",
    "CrosscheckQuantity",
    "RouteResult",
    "AuditStageEntry",
    "CapabilityRow",
    "build_summary_report",
    "KnownResult",
    "ToyIntegralResult",
    "CurvedToyResult",
    "SubsetTopology",
    "S4SubsetTopology",
    "S4TensorSubsetTopology",
    "S4MixedSubsetTopology",
    "NativeAttemptTopology",
    "NativeAttemptTopologyEntry",
    "TensorNativeAttemptTopology",
    "render_tensor_native_report",
    "enforce_tensor_placeholder_guard",
    "register_blockers",
    "build_blocker_dependency_graph",
    "graph_is_acyclic",
    "graph_edges",
    "build_blocker_closure_plan",
    "run_blocker_progress_audit",
    "run_stage6b_multi_blocker_harness",
    "build_conformal_scalar_propagator_closed_form",
    "validate_conformal_scalar_propagator",
    "compare_spectral_to_closed_form",
    "diagnose_scalar_spectral_convergence",
    "update_full_s4_propagator_blocker_scalar_only",
    "run_stage6c_scalar_propagator",
    "define_ghost_operator",
    "build_ghost_propagator_structure",
    "validate_ghost_propagator",
    "update_ghost_blocker_status",
    "run_stage6d_ghost_propagator",
    "define_s4_harmonic_spectra",
    "build_vector_harmonics_structure",
    "extend_tensor_harmonics",
    "check_harmonic_consistency",
    "run_stage6e_harmonic_benchmark",
    "define_tt_operator",
    "extend_tt_projector",
    "build_tt_propagator_scaffold",
    "validate_tt_scaffold",
    "update_tt_blocker_status",
    "run_stage6f_tt_propagator",
    "define_tt_mode_decomposition",
    "define_tt_eigenvalues",
    "define_tt_degeneracies",
    "define_zero_mode_strategy",
    "define_spectral_inversion_strategy",
    "run_stage6g_spectral_strategy",
    "define_regularization_schemes",
    "perform_regularized_tt_inversion",
    "compare_regularization_results",
    "audit_regularized_inversion",
    "run_stage7e_tt_regularization",
    "map_tt_divergences_to_counterterms",
    "build_tt_renormalization_plan",
    "check_tt_scheme_alignment",
    "audit_tt_renormalization_dry_run",
    "run_stage7f_tt_renormalization_dry_run",
    "define_finite_part_requirements",
    "evaluate_finite_part_readiness",
    "identify_finite_part_blockers",
    "decide_finite_part_eligibility",
    "run_stage7g_finite_part_audit",
    "compute_tt_convergence_metrics",
    "define_convergence_thresholds",
    "evaluate_convergence_repair",
    "audit_convergence_repair",
    "run_stage7i_convergence_repair",
]
