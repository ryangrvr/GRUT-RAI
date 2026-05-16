"""
M[1,5] Discrete Provenance Variants Audit.

Purpose
-------
Test only named, defensible S^4 projection and counterterm conventions,
then rank which variant pair lands closest to R_target.

No continuous tuning is used.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Dict, List

from grut.derivation.euler.m15_diagram_origin_derivation import build_independent_decomposition
from grut.derivation.euler.m15_required_coefficient_scan import (
    build_v5_with_m15_coefficient,
    evolve_euler_channel,
)

R_TARGET_TREE = math.sqrt(4.0 / 3.0)
R_TARGET_LOOP = 1.15428


@dataclass(frozen=True)
class ProjectionVariant:
    name: str
    meaning: str
    multiplier: float


@dataclass(frozen=True)
class CountertermVariant:
    name: str
    meaning: str
    multiplier: float


@dataclass(frozen=True)
class VariantResult:
    projection_variant: str
    counterterm_variant: str
    x_value: float
    r_value: float
    beta_eff: float
    error_vs_tree_percent: float
    error_vs_loop_percent: float


def projection_variants() -> List[ProjectionVariant]:
    """Named, discrete S^4 projection alternatives."""
    vol_s4 = 8.0 * math.pi**2 / 3.0
    return [
        ProjectionVariant(
            name="baseline",
            meaning="current S^4 projection",
            multiplier=1.0,
        ),
        ProjectionVariant(
            name="Euler-characteristic normalized",
            meaning="uses chi(S^4)=2 normalization",
            multiplier=2.0,
        ),
        ProjectionVariant(
            name="volume-normalized",
            meaning="divides by Vol(S^4)=8*pi^2/3 factor where appropriate",
            multiplier=1.0 / vol_s4,
        ),
        ProjectionVariant(
            name="branch-projected",
            meaning="includes CTP/Keldysh branch factor",
            multiplier=0.5,
        ),
        ProjectionVariant(
            name="round-sphere-only",
            meaning="enforces Weyl^2=0, Euler-only projection",
            multiplier=0.0,
        ),
    ]


def counterterm_variants() -> List[CountertermVariant]:
    """Named, discrete counterterm alternatives."""
    return [
        CountertermVariant(
            name="baseline subtraction",
            meaning="current counterterm",
            multiplier=1.0,
        ),
        CountertermVariant(
            name="half subtraction",
            meaning="tests scheme-minimal counterterm",
            multiplier=0.5,
        ),
        CountertermVariant(
            name="no finite subtraction",
            meaning="counterterm removes pole only",
            multiplier=0.0,
        ),
        CountertermVariant(
            name="Euler-protected subtraction",
            meaning="subtracts only scheme-fragile local part",
            multiplier=0.25,
        ),
        CountertermVariant(
            name="full subtraction",
            meaning="current or stronger local subtraction",
            multiplier=1.5,
        ),
    ]


def _base_x_terms() -> Dict[str, float]:
    terms = build_independent_decomposition()
    return {term.name: term.contribution_to_x() for term in terms}


def _x_with_variants(
    base_x_terms: Dict[str, float],
    p_variant: ProjectionVariant,
    c_variant: CountertermVariant,
) -> float:
    x_terms = dict(base_x_terms)
    x_terms["M_S4_projection"] = x_terms["M_S4_projection"] * p_variant.multiplier
    x_terms["M_counterterm"] = x_terms["M_counterterm"] * c_variant.multiplier
    return sum(x_terms.values())


def _evaluate_x(x_value: float) -> tuple[float, float, float, float]:
    matrix = build_v5_with_m15_coefficient(m15_coefficient=x_value)
    r_value, beta_eff = evolve_euler_channel(matrix)
    err_tree = abs(r_value - R_TARGET_TREE) / R_TARGET_TREE * 100.0
    err_loop = abs(r_value - R_TARGET_LOOP) / R_TARGET_LOOP * 100.0
    return r_value, beta_eff, err_tree, err_loop


def run_variant_audit() -> Dict[str, object]:
    """Run full discrete variant grid and classify result."""
    base_x_terms = _base_x_terms()
    base_x = sum(base_x_terms.values())
    base_r, base_beta, base_err_tree, base_err_loop = _evaluate_x(base_x)

    results: List[VariantResult] = []
    for pv in projection_variants():
        for cv in counterterm_variants():
            x_value = _x_with_variants(base_x_terms, pv, cv)
            r_value, beta_eff, err_tree, err_loop = _evaluate_x(x_value)
            results.append(
                VariantResult(
                    projection_variant=pv.name,
                    counterterm_variant=cv.name,
                    x_value=x_value,
                    r_value=r_value,
                    beta_eff=beta_eff,
                    error_vs_tree_percent=err_tree,
                    error_vs_loop_percent=err_loop,
                )
            )

    ranked = sorted(results, key=lambda item: abs(item.r_value - R_TARGET_TREE))
    near_threshold_percent = 0.75
    near_target = [item for item in ranked if item.error_vs_tree_percent <= near_threshold_percent]

    # Dominance diagnostic: compare marginal ranges across the two variant axes.
    counter_marginals = {}
    for cv in counterterm_variants():
        values = [r.r_value for r in results if r.counterterm_variant == cv.name]
        counter_marginals[cv.name] = sum(values) / len(values)
    counter_range = max(counter_marginals.values()) - min(counter_marginals.values())

    projection_marginals = {}
    for pv in projection_variants():
        values = [r.r_value for r in results if r.projection_variant == pv.name]
        projection_marginals[pv.name] = sum(values) / len(values)
    projection_range = max(projection_marginals.values()) - min(projection_marginals.values())

    counterterm_dominates = counter_range > 1.5 * projection_range

    classification = classify_audit_outcome(
        ranked=ranked,
        near_target=near_target,
        counterterm_dominates=counterterm_dominates,
    )

    return {
        "base_x": base_x,
        "base_r": base_r,
        "base_beta": base_beta,
        "base_error_vs_tree_percent": base_err_tree,
        "base_error_vs_loop_percent": base_err_loop,
        "results": results,
        "ranked": ranked,
        "near_target": near_target,
        "counter_range": counter_range,
        "projection_range": projection_range,
        "counterterm_dominates": counterterm_dominates,
        "classification": classification,
    }


def classify_audit_outcome(
    ranked: List[VariantResult],
    near_target: List[VariantResult],
    counterterm_dominates: bool,
) -> Dict[str, str]:
    """Classification rules requested for discrete provenance gate."""
    if counterterm_dominates:
        return {
            "outcome": "counterterm choice dominates",
            "meaning": "scheme-dependence prevents promotion",
        }

    if len(near_target) == 1:
        return {
            "outcome": "named variant lands near target",
            "meaning": "provenance candidate",
        }

    if len(near_target) > 1:
        return {
            "outcome": "multiple variants land near target",
            "meaning": "ambiguity remains",
        }

    best = ranked[0]
    if best.error_vs_tree_percent <= 1.5:
        return {
            "outcome": "only continuous tuning lands near target",
            "meaning": "not resolved",
        }

    return {
        "outcome": "all variants miss",
        "meaning": "residual lives elsewhere",
    }


def print_variant_audit_report(audit: Dict[str, object]) -> None:
    ranked = audit["ranked"]
    near_target = audit["near_target"]
    classification = audit["classification"]
    assert isinstance(ranked, list)
    assert isinstance(near_target, list)
    assert isinstance(classification, dict)

    print("\n" + "=" * 120)
    print("M[1,5] PROJECTION / COUNTERTERM DISCRETE VARIANT AUDIT")
    print("=" * 120)
    print("\nQuestion: is the residual explained by defensible discrete conventions, without tuning?")
    print(f"Baseline x: {audit['base_x']:.6f}")
    print(f"Baseline R: {audit['base_r']:.9f}  (err vs 1.15470: {audit['base_error_vs_tree_percent']:.4f}%)")
    print(f"Counter marginal range in R:  {audit['counter_range']:.6f}")
    print(f"Projection marginal range in R:{audit['projection_range']:.6f}")
    print(f"Counterterm dominates? {audit['counterterm_dominates']}")

    print("\n" + "-" * 120)
    print("TOP 12 VARIANTS BY CLOSENESS TO R_TARGET")
    print("-" * 120)
    print(
        f"{'Rank':<6} {'Projection variant':<32} {'Counterterm variant':<30} {'x':<10} {'R':<12} {'Err vs 1.15470%':<16} {'Err vs 1.15428%':<16}"
    )
    print("-" * 120)
    for idx, row in enumerate(ranked[:12], start=1):
        assert isinstance(row, VariantResult)
        print(
            f"{idx:<6} {row.projection_variant:<32} {row.counterterm_variant:<30} {row.x_value:<10.6f} "
            f"{row.r_value:<12.6f} {row.error_vs_tree_percent:<16.4f} {row.error_vs_loop_percent:<16.4f}"
        )

    print("\n" + "-" * 120)
    print("NEAR-TARGET VARIANTS (ERR <= 0.75%)")
    print("-" * 120)
    if near_target:
        for row in near_target:
            assert isinstance(row, VariantResult)
            print(
                f"- {row.projection_variant} + {row.counterterm_variant}: "
                f"R={row.r_value:.6f}, err={row.error_vs_tree_percent:.4f}%"
            )
    else:
        print("- none")

    print("\n" + "-" * 120)
    print("CLASSIFICATION")
    print("-" * 120)
    print(f"Outcome: {classification['outcome']}")
    print(f"Meaning: {classification['meaning']}")
    print("=" * 120 + "\n")


if __name__ == "__main__":
    result = run_variant_audit()
    print_variant_audit_report(result)