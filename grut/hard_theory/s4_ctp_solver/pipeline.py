"""Pipeline assembly for the S4 CTP scaffold."""

from dataclasses import dataclass
from typing import Dict, Tuple

from grut.hard_theory.s4_ctp_solver.diagrams import diagram_placeholder


@dataclass(frozen=True)
class PipelineStatus:
    tier: str
    message: str


class S4CTPPipeline:
    """Stage 1 pipeline scaffold for S4 CTP diagram bookkeeping."""

    def __init__(self) -> None:
        self._status = PipelineStatus(
            tier="scaffold",
            message="Stage 1 verified scaffolding only; no computation performed.",
        )

    def status(self) -> PipelineStatus:
        return self._status

    def assemble_metadata(self) -> Dict[str, str]:
        return {
            "tier": self._status.tier,
            "message": self._status.message,
            "promote_allowed": "no",
        }

    def required_ingredients(self, loop_order: int) -> Tuple[str, ...]:
        if loop_order == 1:
            return ("propagators", "vertices", "scheme", "regulator")
        if loop_order == 2:
            return ("propagators", "vertices", "diagram_bookkeeping", "scheme", "regulator")
        if loop_order == 3:
            return (
                "propagators",
                "vertices",
                "diagram_bookkeeping",
                "ward_identities",
                "scheme",
                "regulator",
            )
        return ("propagators", "vertices", "scheme", "regulator")

    def diagram(self, loop_order: int):
        return diagram_placeholder(loop_order)

    def promote_to_computed(self) -> None:
        raise RuntimeError("Stage 1 scaffold cannot be promoted to computed.")

    def run_stage2_benchmarks(self) -> Dict[str, object]:
        """Run Stage 2 benchmark reproduction checks (no new physics)."""
        from grut.hard_theory.s4_ctp_solver.heat_kernel import (
            scalar_heat_kernel_coefficients,
            s4_invariants,
            euler_density_s4,
        )
        from grut.hard_theory.s4_ctp_solver.anomaly_1loop_scalar import (
            scalar_anomaly_coefficients,
            scalar_trace_anomaly_s4,
        )
        from grut.hard_theory.s4_ctp_solver.anomaly_1loop_weyl import (
            weyl_anomaly_coefficients,
            weyl_trace_anomaly_s4,
        )
        from grut.hard_theory.s4_ctp_solver.anomaly_1loop_gauge import (
            gauge_anomaly_coefficients,
            gauge_trace_anomaly_s4,
        )
        from grut.hard_theory.s4_ctp_solver.flatspace_loop_checks import (
            one_loop_scalar_bubble_structure,
            dim_reg_terms,
        )
        import sympy as sp

        radius_a = sp.symbols("a", positive=True)
        invariants = s4_invariants(radius_a)
        hk = scalar_heat_kernel_coefficients()
        scalar_coeffs = scalar_anomaly_coefficients()
        weyl_coeffs = weyl_anomaly_coefficients()
        gauge_coeffs = gauge_anomaly_coefficients()
        bubble = one_loop_scalar_bubble_structure()
        dim_reg = dim_reg_terms()

        checks = {
            "s4_invariants": invariants,
            "heat_kernel": hk,
            "scalar_anomaly": scalar_coeffs,
            "weyl_anomaly": weyl_coeffs,
            "gauge_anomaly": gauge_coeffs,
            "scalar_anomaly_s4": scalar_trace_anomaly_s4(radius_a),
            "weyl_anomaly_s4": weyl_trace_anomaly_s4(radius_a),
            "gauge_anomaly_s4": gauge_trace_anomaly_s4(radius_a),
            "euler_density_s4": euler_density_s4(radius_a),
            "flatspace_bubble": bubble.expression,
            "dim_reg": dim_reg,
        }

        all_pass = all(
            getattr(obj, "status", "benchmarked") == "benchmarked"
            for obj in (scalar_coeffs, weyl_coeffs, gauge_coeffs, bubble)
        )

        return {
            "stage": 2,
            "status": "benchmarked" if all_pass else "incomplete",
            "checks": checks,
            "label": "benchmarked",
        }

    def run_stage3_partials(self) -> Dict[str, object]:
        """Run Stage 3 controlled partials (speculative/internal only)."""
        from grut.hard_theory.s4_ctp_solver.diagram_topologies import stage3_topologies
        from grut.hard_theory.s4_ctp_solver.asymptotic_expansions import (
            large_radius_expansion,
            small_curvature_expansion,
            heat_kernel_truncated_expansion,
            flat_limit_projection,
        )
        from grut.hard_theory.s4_ctp_solver.ward_audit import (
            audit_transversality,
            audit_ctp_unitarity,
            audit_trace_anomaly_consistency,
            audit_scheme_consistency,
            audit_flat_limit,
        )
        from grut.hard_theory.s4_ctp_solver.stage3_audit import run_stage3_partial_audit

        topologies = stage3_topologies()
        partials = []
        for idx, topo in enumerate(topologies):
            if idx % 4 == 0:
                partials.append(large_radius_expansion(topo, order=2))
            elif idx % 4 == 1:
                partials.append(small_curvature_expansion(topo, order=2))
            elif idx % 4 == 2:
                partials.append(heat_kernel_truncated_expansion(topo, max_a_n=2))
            else:
                partials.append(flat_limit_projection(topo))

        audits = []
        for partial in partials:
            audits.extend(
                [
                    audit_transversality(partial),
                    audit_ctp_unitarity(partial),
                    audit_trace_anomaly_consistency(partial),
                    audit_scheme_consistency(partial),
                    audit_flat_limit(partial),
                ]
            )

        gate = run_stage3_partial_audit(partials)

        return {
            "stage": 3,
            "status": "speculative_internal",
            "partials": partials,
            "audits": audits,
            "gate": gate,
            "label": "speculative_internal",
        }

    def run_stage3b_s4_ingredients(self) -> Dict[str, object]:
        """Run Stage 3B S4 ingredient benchmarks (no 3-loop evaluation)."""
        import sympy as sp

        from grut.hard_theory.s4_ctp_solver.s4_spectral_basis import (
            scalar_spectral_mode_record,
        )
        from grut.hard_theory.s4_ctp_solver.s4_green_functions import (
            scalar_green_truncated,
        )
        from grut.hard_theory.s4_ctp_solver.propagator_benchmarks import (
            benchmark_scalar_conformal_s4,
            benchmark_scalar_minimal_zero_mode_warning,
            benchmark_flat_large_radius_limit_structure,
        )
        from grut.hard_theory.s4_ctp_solver.diagram_topologies import stage3_topologies
        from grut.hard_theory.s4_ctp_solver.contraction_engine import (
            symbolic_contract_topology_with_propagators,
        )

        radius = sp.symbols("a", positive=True)
        spectral_modes = [scalar_spectral_mode_record(l, radius) for l in range(3)]
        green_truncation = scalar_green_truncated(max_l=3, radius=radius)
        benchmarks = [
            benchmark_scalar_conformal_s4(radius),
            benchmark_scalar_minimal_zero_mode_warning(radius),
            benchmark_flat_large_radius_limit_structure(),
        ]

        contractions = []
        for topo in stage3_topologies():
            contractions.append(
                symbolic_contract_topology_with_propagators(
                    topo, ("scalar_conformal", "ghost", "graviton")
                )
            )

        return {
            "stage": "3B",
            "status": "ingredient_benchmarked_scaffold",
            "spectral_basis": spectral_modes,
            "green_truncation": green_truncation,
            "benchmarks": benchmarks,
            "contractions": contractions,
            "can_compute_3loop": False,
            "promotes_claims": False,
        }

    def run_stage3c_tensor_audit(self) -> Dict[str, object]:
        """Run Stage 3C tensor harmonic and Ward structural audit."""
        import sympy as sp

        from grut.hard_theory.s4_ctp_solver.s4_tensor_spectrum import tensor_mode_records
        from grut.hard_theory.s4_ctp_solver.tt_projector import (
            tt_projector_record,
            check_projector_structural_identities,
        )
        from grut.hard_theory.s4_ctp_solver.graviton_decomposition import (
            decompose_metric_perturbation_record,
        )
        from grut.hard_theory.s4_ctp_solver.ward_tensor_checks import (
            audit_tensor_ward_structure,
            audit_ctp_branch_consistency,
            audit_graviton_decomposition_consistency,
        )
        from grut.hard_theory.s4_ctp_solver.stage3c_tensor_audit import (
            run_stage3c_tensor_audit,
        )

        radius = sp.symbols("a", positive=True)
        spectra = tensor_mode_records(2, radius)
        projector = tt_projector_record()
        projector_checks = check_projector_structural_identities(projector)
        decomposition = decompose_metric_perturbation_record()
        ward_checks = {
            "tensor": audit_tensor_ward_structure(),
            "ctp": audit_ctp_branch_consistency(),
            "decomposition": audit_graviton_decomposition_consistency(),
        }
        gate = run_stage3c_tensor_audit()

        return {
            "stage": "3C",
            "status": "tensor_structural_audit",
            "spectra": spectra,
            "tt_projector": projector,
            "tt_projector_checks": projector_checks,
            "decomposition": decomposition,
            "ward_checks": ward_checks,
            "gate": gate,
            "can_compute_3loop": False,
            "promotes_claims": False,
        }

    def run_stage3d_scheme_audit(self) -> Dict[str, object]:
        """Run Stage 3D renormalization and scheme-consistency audit."""
        from grut.hard_theory.s4_ctp_solver.counterterms import counterterm_registry
        from grut.hard_theory.s4_ctp_solver.divergence_structure import (
            create_divergence_record,
            associate_counterterms,
        )
        from grut.hard_theory.s4_ctp_solver.scheme_invariants import (
            classify_scheme_sensitivity,
        )
        from grut.hard_theory.s4_ctp_solver.renormalization_audit import (
            audit_counterterm_coverage,
            audit_divergence_has_counterterm,
            audit_scheme_metadata_consistency,
            audit_scheme_invariant_claim,
            audit_forbidden_promotion_after_renormalization,
        )
        from grut.hard_theory.s4_ctp_solver.stage3d_scheme_audit import (
            run_stage3d_scheme_audit,
        )

        registry = counterterm_registry()
        divergence_records = [
            create_divergence_record(1, regulator="dim_reg", scheme="ms_bar"),
            create_divergence_record(2, regulator="dim_reg", scheme="ms_bar"),
            create_divergence_record(3, regulator="dim_reg", scheme="ms_bar"),
        ]
        divergence_records[0] = associate_counterterms(
            divergence_records[0], ["Euler_density_counterterm", "Weyl_squared_counterterm"]
        )

        classifications = {
            name: classify_scheme_sensitivity(name)
            for name in ("a", "c", "box_R", "C_Cosmo", "C_Final", "R_ratio")
        }

        audits = {
            "counterterms": audit_counterterm_coverage(registry),
            "divergences": [audit_divergence_has_counterterm(rec) for rec in divergence_records],
            "scheme_metadata": audit_scheme_metadata_consistency(divergence_records),
            "scheme_invariants": [
                audit_scheme_invariant_claim(record) for record in classifications.values()
            ],
            "forbidden_promotion": audit_forbidden_promotion_after_renormalization(
                divergence_records
            ),
        }

        gate = run_stage3d_scheme_audit()

        return {
            "stage": "3D",
            "status": "renormalization_scheme_audit",
            "counterterms": registry,
            "divergences": divergence_records,
            "classifications": classifications,
            "audits": audits,
            "gate": gate,
            "can_compute_3loop": False,
            "promotes_claims": False,
        }

    def run_stage3e_crosscheck_audit(self) -> Dict[str, object]:
        """Run Stage 3E independent cross-check harness."""
        from grut.hard_theory.s4_ctp_solver.crosscheck_registry import crosscheck_registry
        from grut.hard_theory.s4_ctp_solver.crosscheck_audit import run_crosscheck
        from grut.hard_theory.s4_ctp_solver.stage3e_crosscheck_audit import (
            run_stage3e_crosscheck_audit,
        )

        registry = crosscheck_registry()
        results = {key: run_crosscheck(key) for key in registry.keys()}
        gate = run_stage3e_crosscheck_audit()

        return {
            "stage": "3E",
            "status": "crosscheck_audit",
            "registry": registry,
            "crosschecks": results,
            "gate": gate,
            "can_compute_3loop": False,
            "promotes_claims": False,
        }

    def run_stage3f_external_audit(self) -> Dict[str, object]:
        """Run Stage 3F external audit and reproducibility bundle."""
        from grut.hard_theory.s4_ctp_solver.audit_manifest import build_audit_manifest
        from grut.hard_theory.s4_ctp_solver.capability_matrix import build_capability_matrix
        from grut.hard_theory.s4_ctp_solver.refusal_report import generate_refusal_report
        from grut.hard_theory.s4_ctp_solver.reproducibility_bundle import (
            build_reproducibility_bundle,
        )
        from grut.hard_theory.s4_ctp_solver.summary_report import build_summary_report
        from grut.hard_theory.s4_ctp_solver.stage3f_external_audit import (
            run_stage3f_external_audit,
        )

        manifest = build_audit_manifest()
        matrix = build_capability_matrix()
        refusal = generate_refusal_report("compute_full_3loop_s4_ctp")
        bundle = build_reproducibility_bundle()
        summary = build_summary_report()
        gate = run_stage3f_external_audit()

        return {
            "stage": "3F",
            "status": "external_audit_ready",
            "audit_manifest": manifest,
            "capability_matrix": matrix,
            "refusal_report": refusal,
            "reproducibility_bundle": bundle,
            "summary_report": summary,
            "gate": gate,
            "can_compute_3loop": False,
            "promotes_claims": False,
        }

    def run_stage4a_benchmark_evaluation(self) -> Dict[str, object]:
        """Run Stage 4A benchmark integral evaluation."""
        from grut.hard_theory.s4_ctp_solver.stage4a_benchmark_evaluation import (
            run_stage4a_benchmark_evaluation,
        )

        report = run_stage4a_benchmark_evaluation()
        return {
            "stage": "4A",
            "status": "benchmark_evaluation",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage4b_subset_evaluation(self) -> Dict[str, object]:
        """Run Stage 4B controlled subset evaluation."""
        from grut.hard_theory.s4_ctp_solver.stage4b_subset_evaluation import (
            run_stage4b_subset_evaluation,
        )

        report = run_stage4b_subset_evaluation()
        return {
            "stage": "4B",
            "status": "subset_evaluation",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage4c_s4_subset_evaluation(self) -> Dict[str, object]:
        """Run Stage 4C curved S4 scalar subset evaluation."""
        from grut.hard_theory.s4_ctp_solver.stage4c_s4_subset_evaluation import (
            run_stage4c_s4_subset_evaluation,
        )

        report = run_stage4c_s4_subset_evaluation()
        return {
            "stage": "4C",
            "status": "curved_subset_evaluation",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage4d_tensor_subset_evaluation(self) -> Dict[str, object]:
        """Run Stage 4D tensor subset structure evaluation."""
        from grut.hard_theory.s4_ctp_solver.stage4d_tensor_subset_evaluation import (
            run_stage4d_tensor_subset_evaluation,
        )

        report = run_stage4d_tensor_subset_evaluation()
        return {
            "stage": "4D",
            "status": "tensor_subset_structural",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage4e_mixed_subset_evaluation(self) -> Dict[str, object]:
        """Run Stage 4E mixed scalar-tensor subset evaluation."""
        from grut.hard_theory.s4_ctp_solver.stage4e_mixed_subset_evaluation import (
            run_stage4e_mixed_subset_evaluation,
        )

        report = run_stage4e_mixed_subset_evaluation()
        return {
            "stage": "4E",
            "status": "mixed_subset_evaluation",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage5a_native_attempt(self) -> Dict[str, object]:
        """Run Stage 5A constrained native attempt."""
        from grut.hard_theory.s4_ctp_solver.stage5a_native_attempt import (
            run_stage5a_native_attempt,
        )

        report = run_stage5a_native_attempt()
        return {
            "stage": "5A",
            "status": "native_attempt",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage5b_native_multi(self) -> Dict[str, object]:
        """Run Stage 5B multi-topology native attempts."""
        from grut.hard_theory.s4_ctp_solver.stage5b_native_multi import (
            run_stage5b_native_multi,
        )

        report = run_stage5b_native_multi()
        return {
            "stage": "5B",
            "status": "multi_native_attempt",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage5c_tensor_native(self) -> Dict[str, object]:
        """Run Stage 5C tensor-native attempt."""
        from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
            run_stage5c_tensor_native,
        )

        report = run_stage5c_tensor_native()
        return {
            "stage": "5C",
            "status": "tensor_native_attempt",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage5d_candidate_readiness(self) -> Dict[str, object]:
        """Run Stage 5D candidate extraction readiness audit."""
        from grut.hard_theory.s4_ctp_solver.stage5d_candidate_readiness import (
            run_stage5d_candidate_readiness,
        )

        report = run_stage5d_candidate_readiness()
        return {
            "stage": "5D",
            "status": "candidate_extraction_readiness",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage5e_extraction_dry_run(self) -> Dict[str, object]:
        """Run Stage 5E legal extraction criteria and dry-run report."""
        from grut.hard_theory.s4_ctp_solver.stage5e_extraction_dry_run import (
            run_stage5e_extraction_dry_run,
        )

        report = run_stage5e_extraction_dry_run()
        return {
            "stage": "5E",
            "status": "extraction_dry_run",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage6a_scheme_alignment(self) -> Dict[str, object]:
        """Run Stage 6A targeted closure for scheme alignment."""
        from grut.hard_theory.s4_ctp_solver.stage6a_scheme_alignment import (
            run_stage6a_scheme_alignment,
        )

        report = run_stage6a_scheme_alignment()
        return {
            "stage": "6A",
            "status": "scheme_alignment_partial",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage6b_multi_blocker_harness(self) -> Dict[str, object]:
        """Run Stage 6B multi-blocker closure harness."""
        from grut.hard_theory.s4_ctp_solver.stage6b_multi_blocker_harness import (
            run_stage6b_multi_blocker_harness,
        )

        report = run_stage6b_multi_blocker_harness()
        return {
            "stage": "6B",
            "status": "multi_blocker_closure_harness",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage6c_scalar_propagator(self) -> Dict[str, object]:
        """Run Stage 6C scalar propagator closure subproblem."""
        from grut.hard_theory.s4_ctp_solver.stage6c_scalar_propagator import (
            run_stage6c_scalar_propagator,
        )

        report = run_stage6c_scalar_propagator()
        return {
            "stage": "6C",
            "status": "scalar_propagator_closure_partial",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage6d_ghost_propagator(self) -> Dict[str, object]:
        """Run Stage 6D ghost propagator closure subproblem."""
        from grut.hard_theory.s4_ctp_solver.stage6d_ghost_propagator import (
            run_stage6d_ghost_propagator,
        )

        report = run_stage6d_ghost_propagator()
        return {
            "stage": "6D",
            "status": "ghost_propagator_closure_partial",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage6e_harmonic_benchmark(self) -> Dict[str, object]:
        """Run Stage 6E harmonic sector benchmark."""
        from grut.hard_theory.s4_ctp_solver.stage6e_harmonic_benchmark import (
            run_stage6e_harmonic_benchmark,
        )

        report = run_stage6e_harmonic_benchmark()
        return {
            "stage": "6E",
            "status": "harmonic_sector_benchmark",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage6f_tt_propagator(self) -> Dict[str, object]:
        """Run Stage 6F TT propagator scaffold."""
        from grut.hard_theory.s4_ctp_solver.stage6f_tt_propagator import (
            run_stage6f_tt_propagator,
        )

        report = run_stage6f_tt_propagator()
        return {
            "stage": "6F",
            "status": "tt_propagator_scaffold",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage6g_spectral_strategy(self) -> Dict[str, object]:
        """Run Stage 6G spectral inversion strategy."""
        from grut.hard_theory.s4_ctp_solver.stage6g_spectral_strategy import (
            run_stage6g_spectral_strategy,
        )

        report = run_stage6g_spectral_strategy()
        return {
            "stage": "6G",
            "status": "spectral_inversion_strategy",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage7a_scalar_inversion(self) -> Dict[str, object]:
        """Run Stage 7A scalar spectral inversion benchmark."""
        from grut.hard_theory.s4_ctp_solver.stage7a_scalar_inversion import (
            run_stage7a_scalar_inversion,
        )

        report = run_stage7a_scalar_inversion()
        return {
            "stage": "7A",
            "status": "scalar_inversion_benchmark",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage7b_ghost_vector_inversion(self) -> Dict[str, object]:
        """Run Stage 7B ghost/vector spectral inversion benchmark."""
        from grut.hard_theory.s4_ctp_solver.stage7b_ghost_vector_inversion import (
            run_stage7b_ghost_vector_inversion,
        )

        report = run_stage7b_ghost_vector_inversion()
        return {
            "stage": "7B",
            "status": "ghost_vector_inversion_benchmark",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage7c_tt_inversion(self) -> Dict[str, object]:
        """Run Stage 7C TT truncated inversion attempt."""
        from grut.hard_theory.s4_ctp_solver.stage7c_tt_inversion import (
            run_stage7c_tt_inversion,
        )

        report = run_stage7c_tt_inversion()
        return {
            "stage": "7C",
            "status": "tt_truncated_inversion_attempt",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage7d_tt_diagnostics(self) -> Dict[str, object]:
        """Run Stage 7D TT inversion diagnostics."""
        from grut.hard_theory.s4_ctp_solver.stage7d_tt_diagnostics import (
            run_stage7d_tt_diagnostics,
        )

        report = run_stage7d_tt_diagnostics()
        return {
            "stage": "7D",
            "status": "tt_inversion_diagnostics",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage7e_tt_regularization(self) -> Dict[str, object]:
        """Run Stage 7E TT regularization layer."""
        from grut.hard_theory.s4_ctp_solver.stage7e_tt_regularization import (
            run_stage7e_tt_regularization,
        )

        report = run_stage7e_tt_regularization()
        return {
            "stage": "7E",
            "status": "tt_regularized_inversion",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage7f_tt_renormalization_dry_run(self) -> Dict[str, object]:
        """Run Stage 7F TT renormalization dry-run."""
        from grut.hard_theory.s4_ctp_solver.stage7f_tt_renormalization_dry_run import (
            run_stage7f_tt_renormalization_dry_run,
        )

        report = run_stage7f_tt_renormalization_dry_run()
        return {
            "stage": "7F",
            "status": "tt_renormalization_dry_run",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage7g_finite_part_audit(self) -> Dict[str, object]:
        """Run Stage 7G finite-part eligibility audit."""
        from grut.hard_theory.s4_ctp_solver.stage7g_finite_part_audit import (
            run_stage7g_finite_part_audit,
        )

        report = run_stage7g_finite_part_audit()
        return {
            "stage": "7G",
            "status": "finite_part_eligibility_audit",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage7h_finite_part_repair_plan(self) -> Dict[str, object]:
        """Run Stage 7H finite-part blocker repair plan."""
        from grut.hard_theory.s4_ctp_solver.stage7h_finite_part_repair_plan import (
            run_stage7h_finite_part_repair_plan,
        )

        report = run_stage7h_finite_part_repair_plan()
        return {
            "stage": "7H",
            "status": "finite_part_blocker_repair_plan",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage7i_convergence_repair(self) -> Dict[str, object]:
        """Run Stage 7I convergence control repair attempt."""
        from grut.hard_theory.s4_ctp_solver.stage7i_convergence_repair import (
            run_stage7i_convergence_repair,
        )

        report = run_stage7i_convergence_repair()
        return {
            "stage": "7I",
            "status": "convergence_control_repair_attempt",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage7j_tensor_contraction_readiness(self) -> Dict[str, object]:
        """Run Stage 7J tensor contraction readiness diagnostics."""
        from grut.hard_theory.s4_ctp_solver.stage7j_tensor_contraction_readiness import (
            run_stage7j_tensor_contraction_readiness,
        )

        report = run_stage7j_tensor_contraction_readiness()
        return {
            "stage": "7J",
            "status": "tensor_contraction_readiness",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage7k_tensor_contraction_repair(self) -> Dict[str, object]:
        """Run Stage 7K tensor contraction structure repair."""
        from grut.hard_theory.s4_ctp_solver.stage7k_tensor_contraction_repair import (
            run_stage7k_tensor_contraction_repair,
        )

        report = run_stage7k_tensor_contraction_repair()
        return {
            "stage": "7K",
            "status": "tensor_contraction_repair",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage8a_tensor_contraction_sandbox(self) -> Dict[str, object]:
        """Run Stage 8A tensor contraction sandbox."""
        from grut.hard_theory.s4_ctp_solver.stage8a_tensor_contraction_sandbox import (
            run_stage8a_tensor_contraction_sandbox,
        )

        report = run_stage8a_tensor_contraction_sandbox()
        return {
            "stage": "8A",
            "status": "tensor_contraction_sandbox",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage8b_local_contractions(self) -> Dict[str, object]:
        """Run Stage 8B diagram-local tensor contractions."""
        from grut.hard_theory.s4_ctp_solver.stage8b_local_contractions import (
            run_stage8b_local_contractions,
        )

        report = run_stage8b_local_contractions()
        return {
            "stage": "8B",
            "status": "diagram_local_contraction_partial",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage8c_controlled_fragment_contractions(self) -> Dict[str, object]:
        """Run Stage 8C controlled fragment contractions."""
        from grut.hard_theory.s4_ctp_solver.stage8c_controlled_fragment_contractions import (
            run_stage8c_controlled_fragment_contractions,
        )

        report = run_stage8c_controlled_fragment_contractions()
        return {
            "stage": "8C",
            "status": "controlled_fragment_contraction_partial",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage8d_diagram_skeleton(self) -> Dict[str, object]:
        """Run Stage 8D diagram skeleton structural contraction."""
        from grut.hard_theory.s4_ctp_solver.stage8d_diagram_skeleton import (
            run_stage8d_diagram_skeleton,
        )

        report = run_stage8d_diagram_skeleton()
        return {
            "stage": "8D",
            "status": "diagram_skeleton_structural_contraction",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage9a_propagator_attachment(self) -> Dict[str, object]:
        """Run Stage 9A propagator symbolic attachment."""
        from grut.hard_theory.s4_ctp_solver.stage9a_propagator_attachment import (
            run_stage9a_propagator_attachment,
        )

        report = run_stage9a_propagator_attachment()
        return {
            "stage": "9A",
            "status": "propagator_symbolic_attachment",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage9b_loop_integrand_scaffold(self) -> Dict[str, object]:
        """Run Stage 9B loop integrand scaffold."""
        from grut.hard_theory.s4_ctp_solver.stage9b_loop_integrand_scaffold import (
            run_stage9b_loop_integrand_scaffold,
        )

        report = run_stage9b_loop_integrand_scaffold()
        return {
            "stage": "9B",
            "status": "loop_integrand_scaffold",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage9c_regularized_integrand(self) -> Dict[str, object]:
        """Run Stage 9C regularized integrand scaffold."""
        from grut.hard_theory.s4_ctp_solver.stage9c_regularized_integrand import (
            run_stage9c_regularized_integrand,
        )

        report = run_stage9c_regularized_integrand()
        return {
            "stage": "9C",
            "status": "regularized_integrand_scaffold",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage9d_integration_dry_run(self) -> Dict[str, object]:
        """Run Stage 9D integration dry-run plan."""
        from grut.hard_theory.s4_ctp_solver.stage9d_integration_dry_run import (
            run_stage9d_integration_dry_run,
        )

        report = run_stage9d_integration_dry_run()
        return {
            "stage": "9D",
            "status": "integration_dry_run_plan",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage10a_partial_integration_benchmark(self) -> Dict[str, object]:
        """Run Stage 10A controlled partial integration benchmark."""
        from grut.hard_theory.s4_ctp_solver.stage10a_partial_integration_benchmark import (
            run_stage10a_partial_integration_benchmark,
        )

        report = run_stage10a_partial_integration_benchmark()
        return {
            "stage": "10A",
            "status": "controlled_partial_integration_benchmark",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage10b_native_subintegrand_dry_run(self) -> Dict[str, object]:
        """Run Stage 10B native sub-integrand dry run."""
        from grut.hard_theory.s4_ctp_solver.stage10b_native_subintegrand_dry_run import (
            run_stage10b_native_subintegrand_dry_run,
        )

        report = run_stage10b_native_subintegrand_dry_run()
        return {
            "stage": "10B",
            "status": "native_subintegrand_dry_run",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage10c_multi_subintegrand_consistency(self) -> Dict[str, object]:
        """Run Stage 10C multi-subintegrand consistency check."""
        from grut.hard_theory.s4_ctp_solver.stage10c_multi_subintegrand_consistency import (
            run_stage10c_multi_subintegrand_consistency,
        )

        report = run_stage10c_multi_subintegrand_consistency()
        return {
            "stage": "10C",
            "status": "multi_subintegrand_consistency",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage10d_integrand_partition_map(self) -> Dict[str, object]:
        """Run Stage 10D native integrand partition map."""
        from grut.hard_theory.s4_ctp_solver.stage10d_integrand_partition_map import (
            run_stage10d_integrand_partition_map,
        )

        report = run_stage10d_integrand_partition_map()
        return {
            "stage": "10D",
            "status": "native_integrand_partition_map",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage10e_eligible_partition_dry_runs(self) -> Dict[str, object]:
        """Run Stage 10E eligible partition dry-runs."""
        from grut.hard_theory.s4_ctp_solver.stage10e_eligible_partition_dry_runs import (
            run_stage10e_eligible_partition_dry_runs,
        )

        report = run_stage10e_eligible_partition_dry_runs()
        return {
            "stage": "10E",
            "status": "eligible_partition_dry_runs",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage10f_partition_consistency_audit(self) -> Dict[str, object]:
        """Run Stage 10F partition consistency audit."""
        from grut.hard_theory.s4_ctp_solver.stage10f_partition_consistency_audit import (
            run_stage10f_partition_consistency_audit,
        )

        report = run_stage10f_partition_consistency_audit()
        return {
            "stage": "10F",
            "status": "partition_consistency_audit",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage11a_single_partition_integration(self) -> Dict[str, object]:
        """Run Stage 11A single partition integration attempt."""
        from grut.hard_theory.s4_ctp_solver.stage11a_single_partition_integration import (
            run_stage11a_single_partition_integration,
        )

        report = run_stage11a_single_partition_integration()
        return {
            "stage": "11A",
            "status": "single_partition_integration_attempt",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage11b_subtraction_dry_run(self) -> Dict[str, object]:
        """Run Stage 11B divergence subtraction dry-run."""
        from grut.hard_theory.s4_ctp_solver.stage11b_subtraction_dry_run import (
            run_stage11b_subtraction_dry_run,
        )

        report = run_stage11b_subtraction_dry_run()
        return {
            "stage": "11B",
            "status": "divergence_subtraction_dry_run",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage11c_finite_part_benchmark_gate(self) -> Dict[str, object]:
        """Run Stage 11C finite-part benchmark gate."""
        from grut.hard_theory.s4_ctp_solver.stage11c_finite_part_benchmark_gate import (
            run_stage11c_finite_part_benchmark_gate,
        )

        report = run_stage11c_finite_part_benchmark_gate()
        return {
            "stage": "11C",
            "status": "finite_part_benchmark_gate",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage11d_native_finite_part_attempt(self) -> Dict[str, object]:
        """Run Stage 11D native finite-part attempt."""
        from grut.hard_theory.s4_ctp_solver.stage11d_native_finite_part_attempt import (
            run_stage11d_native_finite_part_attempt,
        )

        report = run_stage11d_native_finite_part_attempt()
        return {
            "stage": "11D",
            "status": "native_partition_finite_part_attempt",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage11e_cross_partition_finite_consistency(self) -> Dict[str, object]:
        """Run Stage 11E cross-partition finite-part consistency."""
        from grut.hard_theory.s4_ctp_solver.stage11e_cross_partition_finite_consistency import (
            run_stage11e_cross_partition_finite_consistency,
        )

        report = run_stage11e_cross_partition_finite_consistency()
        return {
            "stage": "11E",
            "status": "cross_partition_finite_part_consistency",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage12a_coefficient_assembly_dry_run(self) -> Dict[str, object]:
        """Run Stage 12A coefficient assembly dry-run."""
        from grut.hard_theory.s4_ctp_solver.stage12a_coefficient_assembly_dry_run import (
            run_stage12a_coefficient_assembly_dry_run,
        )

        report = run_stage12a_coefficient_assembly_dry_run()
        return {
            "stage": "12A",
            "status": "coefficient_assembly_dry_run",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage12b_scheme_stability_audit(self) -> Dict[str, object]:
        """Run Stage 12B scheme-stability audit."""
        from grut.hard_theory.s4_ctp_solver.stage12b_scheme_stability_audit import (
            run_stage12b_scheme_stability_audit,
        )

        report = run_stage12b_scheme_stability_audit()
        return {
            "stage": "12B",
            "status": "scheme_stability_audit",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage12c_r_legality_gate(self) -> Dict[str, object]:
        """Run Stage 12C R legality gate."""
        from grut.hard_theory.s4_ctp_solver.stage12c_r_legality_gate import (
            run_stage12c_r_legality_gate,
        )

        report = run_stage12c_r_legality_gate()
        return {
            "stage": "12C",
            "status": "r_legality_gate",
            "report": report,
            "can_run_stage12d": report.get("r_legal") is True,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }

    def run_stage12d_r_extraction_attempt(self) -> Dict[str, object]:
        """Run Stage 12D controlled R extraction attempt."""
        from grut.hard_theory.s4_ctp_solver.stage12d_r_extraction_attempt import (
            run_stage12d_r_extraction_attempt,
        )

        report = run_stage12d_r_extraction_attempt()
        return {
            "stage": "12D",
            "status": "r_extraction_attempt",
            "report": report,
            "can_compute_full_3loop": False,
            "promotes_claims": False,
        }
