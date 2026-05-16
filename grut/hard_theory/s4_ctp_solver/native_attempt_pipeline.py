"""Native attempt pipeline orchestration for Stage 5A."""

from typing import Dict, List

import sympy as sp

from grut.hard_theory.s4_ctp_solver.native_attempt_topology import NativeAttemptTopology
from grut.hard_theory.s4_ctp_solver.s4_spectral_basis import scalar_spectral_mode_record
from grut.hard_theory.s4_ctp_solver.s4_subset_evaluation_engine import evaluate_s4_subset
from grut.hard_theory.s4_ctp_solver.three_loop_subset_s4_scalar import s4_scalar_subset_topologies
from grut.hard_theory.s4_ctp_solver.scheme_invariants import classify_scheme_sensitivity
from grut.hard_theory.s4_ctp_solver.divergence_structure import create_divergence_record
from grut.hard_theory.s4_ctp_solver.crosscheck_audit import run_crosscheck


def _step(name: str, input_data: object, output: object, status: str, limitations: List[str]) -> Dict[str, object]:
    return {
        "stage": name,
        "input": input_data,
        "output": output,
        "status": status,
        "limitations": limitations,
    }


def run_native_attempt_pipeline(
    topology: NativeAttemptTopology, parameters: Dict[str, object]
) -> List[Dict[str, object]]:
    radius = parameters.get("radius", sp.symbols("a", positive=True))

    spectral = scalar_spectral_mode_record(0, radius)
    spectral_step = _step(
        "spectral_setup",
        {"l": 0, "radius": radius},
        spectral,
        "partial",
        ["spectral truncation", "no convergence proof"],
    )

    scalar_topologies = s4_scalar_subset_topologies(l_max=2)
    scalar_subset = evaluate_s4_subset(scalar_topologies[0], radius)
    scalar_step = _step(
        "scalar_subset_evaluation",
        {"topology": scalar_topologies[0].topology_id},
        scalar_subset,
        "partial",
        ["no full contraction", "scalar sector only"],
    )

    scheme_tag = classify_scheme_sensitivity("C_Cosmo")
    scheme_step = _step(
        "scheme_tagging",
        {"quantity": "C_Cosmo"},
        scheme_tag,
        "structural",
        ["scheme dependence unresolved"],
    )

    divergence = create_divergence_record(3, regulator="dim_reg", scheme="ms_bar")
    divergence_step = _step(
        "divergence_tracking",
        {"loop_order": 3},
        divergence,
        "tracked",
        ["no subtraction"],
    )

    cross_check = run_crosscheck("scalar_1loop_effective_action")
    cross_step = _step(
        "cross_check",
        {"quantity": "scalar_1loop_effective_action"},
        cross_check,
        "structural",
        ["cross-check partial"],
    )

    ward_step = _step(
        "ward_placeholder",
        {"topology": topology.topology_id},
        {"status": "structural"},
        "structural",
        ["ward placeholder", "ctp placeholder"],
    )

    return [
        spectral_step,
        scalar_step,
        scheme_step,
        divergence_step,
        cross_step,
        ward_step,
    ]
