"""Stage OR3 S4 Euler-anomaly projection bridge."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline
from grut.hard_theory.s4_ctp_solver.stage_p7_protected_scheme_injection import (
    run_stage_p7_protected_scheme_injection,
)
from grut.hard_theory.s4_ctp_solver.stage_p8_r_legality_with_protected_kernels import (
    run_stage_p8_r_legality_with_protected_kernels,
)
from grut.hard_theory.s4_ctp_solver.stage_p11_r2_equivalence_refresh import (
    run_stage_p11_r2_equivalence_refresh,
)
from grut.hard_theory.s4_ctp_solver.stage_or1_resolve_r_route import (
    run_stage_or1_resolve_r_route,
)
from grut.hard_theory.s4_ctp_solver.stage_or1_r1_legacy_definition_mapping import (
    run_stage_or1_r1_legacy_definition_mapping,
)
from grut.hard_theory.s4_ctp_solver.stage_or2_physical_interpretation_constraint import (
    run_stage_or2_physical_interpretation_constraint,
)
from grut.hard_theory.s4_ctp_solver.s4_euler_projection_identities import (
    build_s4_euler_identities,
)
from grut.hard_theory.s4_ctp_solver.protected_kernel_euler_alignment import (
    build_kernel_projections,
)
from grut.hard_theory.s4_ctp_solver.euler_projection_selection_rule import (
    select_euler_projection_route,
)


def _collect_ratios(stage_p11_r2: Dict[str, object]) -> List[Dict[str, object]]:
    return list(stage_p11_r2.get("refreshed_ratios", []))


def run_stage_or3_s4_euler_anomaly_projection() -> Dict[str, object]:
    stage2 = S4CTPPipeline().run_stage2_benchmarks()
    stage_p7 = run_stage_p7_protected_scheme_injection()
    stage_p8 = run_stage_p8_r_legality_with_protected_kernels()
    stage_p11_r2 = run_stage_p11_r2_equivalence_refresh()

    or1 = run_stage_or1_resolve_r_route()
    or1_r1 = run_stage_or1_r1_legacy_definition_mapping()
    or2 = run_stage_or2_physical_interpretation_constraint()

    s4_identities = build_s4_euler_identities()
    kernel_projections = build_kernel_projections(stage_p7, s4_identities)

    ratios = _collect_ratios(stage_p11_r2)
    selection = select_euler_projection_route(
        ratios,
        kernel_projections,
        ctp_to_euler_bridge=False,
        off_shell_continuation=False,
    )

    selected_route = selection.get("selected_route")
    unique_route_selected = selection.get("unique_route_selected") is True

    euler_channel_available = any(
        entry.get("projects_to_euler_channel") is True and entry.get("survives_on_s4")
        for entry in kernel_projections
    )

    can_advance = unique_route_selected
    blocking_reason = selection.get("blocking_reason")
    next_required_action = "advance_to_symbol_binding" if can_advance else "write_explicit_r_definition"

    return {
        "stage": "OR3",
        "status": "s4_euler_anomaly_projection",
        "s4_weyl_zero": s4_identities.get("s4_weyl_zero"),
        "euler_channel_available": euler_channel_available,
        "kernel_projections": kernel_projections,
        "selected_route": selected_route,
        "unique_route_selected": unique_route_selected,
        "can_advance_to_symbol_binding": can_advance,
        "can_compute_numeric_r": False,
        "can_claim_r": False,
        "blocking_reason": blocking_reason,
        "next_required_action": next_required_action,
        "promotes_claims": False,
        "s4_identities": s4_identities,
        "stage2": stage2,
        "stage_p7": stage_p7,
        "stage_p8": stage_p8,
        "stage_p11_r2": stage_p11_r2,
        "stage_or1": or1,
        "stage_or1_r1": or1_r1,
        "stage_or2": or2,
        "route_evaluations": selection.get("evaluated_routes"),
    }
