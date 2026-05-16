"""
M[1,5] Component Sensitivity and Provenance Audit.

Purpose
-------
Quantify which decomposition component has enough leverage to move
R from the diagram-assembly baseline toward R_target.

This module perturbs each component independently within fixed uncertainty bands,
rebuilds M[1,5] = x*kappa, runs live V5 evolution, and reports delta-R.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Dict, List

from grut.derivation.euler.m15_diagram_origin_derivation import (
    DiagramContribution,
    build_independent_decomposition,
)
from grut.derivation.euler.m15_required_coefficient_scan import (
    build_v5_with_m15_coefficient,
    evolve_euler_channel,
)

R_TARGET_TREE = math.sqrt(4.0 / 3.0)
R_TARGET_LOOP = 1.15428


@dataclass(frozen=True)
class ComponentScenarioResult:
    component: str
    perturbation: str
    x_value: float
    r_value: float
    beta_eff: float
    delta_r_vs_baseline: float
    error_vs_tree_percent: float
    error_vs_loop_percent: float


def component_x_contributions(terms: List[DiagramContribution]) -> Dict[str, float]:
    return {term.name: term.contribution_to_x() for term in terms}


def total_x(terms: List[DiagramContribution]) -> float:
    return sum(component_x_contributions(terms).values())


def evaluate_x(x_value: float) -> Dict[str, float]:
    matrix = build_v5_with_m15_coefficient(m15_coefficient=x_value)
    r_value, beta_eff = evolve_euler_channel(matrix)
    return {
        "x_value": x_value,
        "r_value": r_value,
        "beta_eff": beta_eff,
        "error_vs_tree_percent": abs(r_value - R_TARGET_TREE) / R_TARGET_TREE * 100.0,
        "error_vs_loop_percent": abs(r_value - R_TARGET_LOOP) / R_TARGET_LOOP * 100.0,
    }


def perturb_single_component(
    base_x_terms: Dict[str, float],
    component_name: str,
    factor: float,
) -> float:
    perturbed = dict(base_x_terms)
    perturbed[component_name] = base_x_terms[component_name] * factor
    return sum(perturbed.values())


def run_component_sensitivity_audit() -> Dict[str, object]:
    terms = build_independent_decomposition()
    base_x_terms = component_x_contributions(terms)
    base_x = sum(base_x_terms.values())
    baseline_metrics = evaluate_x(base_x)

    perturbation_plan = {
        "M_box": [(0.95, "-5%"), (1.05, "+5%")],
        "M_triangle": [(0.95, "-5%"), (1.05, "+5%")],
        "M_bubble": [(0.50, "-50%"), (1.50, "+50%")],
        "M_counterterm": [(0.50, "-50%"), (1.50, "+50%"), (0.0, "remove")],
        "M_S4_projection": [(0.50, "-50%"), (1.50, "+50%"), (0.0, "remove")],
    }

    scenarios: List[ComponentScenarioResult] = []
    for component_name, variations in perturbation_plan.items():
        for factor, label in variations:
            x_trial = perturb_single_component(base_x_terms, component_name, factor)
            trial = evaluate_x(x_trial)
            scenarios.append(
                ComponentScenarioResult(
                    component=component_name,
                    perturbation=label,
                    x_value=x_trial,
                    r_value=trial["r_value"],
                    beta_eff=trial["beta_eff"],
                    delta_r_vs_baseline=trial["r_value"] - baseline_metrics["r_value"],
                    error_vs_tree_percent=trial["error_vs_tree_percent"],
                    error_vs_loop_percent=trial["error_vs_loop_percent"],
                )
            )

    residual_to_close = R_TARGET_TREE - baseline_metrics["r_value"]
    leverage_rank = sorted(
        scenarios,
        key=lambda s: abs(s.delta_r_vs_baseline),
        reverse=True,
    )

    closest = min(scenarios, key=lambda s: abs(R_TARGET_TREE - s.r_value))
    enough_leverage = [
        s for s in scenarios if abs(s.delta_r_vs_baseline) >= abs(residual_to_close)
    ]

    return {
        "base_x_terms": base_x_terms,
        "base_x": base_x,
        "baseline": baseline_metrics,
        "residual_to_close": residual_to_close,
        "scenarios": scenarios,
        "leverage_rank": leverage_rank,
        "closest_to_target": closest,
        "enough_leverage": enough_leverage,
    }


def print_component_sensitivity_report(result: Dict[str, object]) -> None:
    baseline = result["baseline"]
    scenarios = result["scenarios"]
    leverage_rank = result["leverage_rank"]
    closest = result["closest_to_target"]
    enough_leverage = result["enough_leverage"]
    assert isinstance(baseline, dict)
    assert isinstance(scenarios, list)
    assert isinstance(leverage_rank, list)
    assert isinstance(enough_leverage, list)

    print("\n" + "=" * 110)
    print("M[1,5] COMPONENT SENSITIVITY / PROVENANCE AUDIT")
    print("=" * 110)
    print("\nGoal: identify which component can close residual from diagram baseline to R_target")
    print(f"Baseline x_derived: {result['base_x']:.6f}")
    print(f"Baseline R:         {baseline['r_value']:.9f}")
    print(f"Target R_tree:      {R_TARGET_TREE:.9f}")
    print(f"Residual to close:  {result['residual_to_close']:+.9f}")

    print("\n" + "-" * 110)
    print("BASE COMPONENT CONTRIBUTIONS (x-units)")
    print("-" * 110)
    for name, x_val in result["base_x_terms"].items():
        print(f"{name:<16} {x_val:+.6f}")

    print("\n" + "-" * 110)
    print("SCENARIO TABLE")
    print("-" * 110)
    print(
        f"{'Component':<16} {'Perturbation':<12} {'x':<10} {'R':<12} {'ΔR vs base':<12} {'Err vs 1.15470':<15} {'Err vs 1.15428':<15}"
    )
    print("-" * 110)
    for s in scenarios:
        assert isinstance(s, ComponentScenarioResult)
        print(
            f"{s.component:<16} {s.perturbation:<12} {s.x_value:<10.6f} {s.r_value:<12.6f} {s.delta_r_vs_baseline:<+12.6f} {s.error_vs_tree_percent:<15.4f} {s.error_vs_loop_percent:<15.4f}"
        )

    print("\n" + "-" * 110)
    print("LEVERAGE RANK (ABS(ΔR))")
    print("-" * 110)
    for idx, s in enumerate(leverage_rank[:8], start=1):
        assert isinstance(s, ComponentScenarioResult)
        print(f"{idx:>2}. {s.component:<16} {s.perturbation:<12} ΔR={s.delta_r_vs_baseline:+.6f}")

    print("\n" + "-" * 110)
    print("CLOSURE ASSESSMENT")
    print("-" * 110)
    print(
        f"Closest single-perturbation case: {closest.component} {closest.perturbation}, R={closest.r_value:.6f}, "
        f"|R-R_target|={abs(closest.r_value - R_TARGET_TREE):.6f}"
    )

    if enough_leverage:
        print("Single-component perturbations with enough raw leverage to close full residual:")
        for s in enough_leverage:
            print(f"- {s.component} {s.perturbation}: ΔR={s.delta_r_vs_baseline:+.6f}")
    else:
        print("No single tested perturbation closes full residual; likely requires combined shifts.")

    print("=" * 110 + "\n")


if __name__ == "__main__":
    audit = run_component_sensitivity_audit()
    print_component_sensitivity_report(audit)