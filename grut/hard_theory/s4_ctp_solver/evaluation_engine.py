"""Evaluation engine for Stage 4A benchmarks."""

from typing import Dict

import sympy as sp

from grut.hard_theory.s4_ctp_solver.known_results_library import known_results_library


def _extract_expression(computation: object) -> sp.Expr:
    if isinstance(computation, dict) and "expression" in computation:
        return computation["expression"]
    if hasattr(computation, "expression"):
        return getattr(computation, "expression")
    if callable(computation):
        result = computation()
        return _extract_expression(result)
    if isinstance(computation, sp.Expr):
        return computation
    return sp.Symbol("unknown_expression")


def _normalize_symbols(expr: sp.Expr) -> sp.Expr:
    mapping = {sym: sp.Symbol(sym.name) for sym in expr.free_symbols}
    return expr.xreplace(mapping)


def evaluate_with_benchmark_check(computation: object, reference_id: str) -> Dict[str, object]:
    library = known_results_library()
    reference = library.get(reference_id)
    if reference is None:
        return {
            "computation": reference_id,
            "matches_known_result": False,
            "deviation": "unknown_reference",
            "status": "benchmark_fail",
            "promotes_claims": False,
        }

    expr = _normalize_symbols(_extract_expression(computation))
    reference_expr = _normalize_symbols(reference.result_expression)
    epsilon = sp.symbols("epsilon")
    expr_match = sp.simplify(expr - reference_expr) == 0

    pole_ok = True
    log_ok = True
    if "pole" in reference.expected_behavior:
        pole_ok = expr.has(epsilon)
    if "log" in reference.expected_behavior:
        log_ok = expr.has(sp.log)

    matches = expr_match and pole_ok and log_ok
    deviation = "none" if matches else "structure_mismatch"

    return {
        "computation": reference_id,
        "matches_known_result": matches,
        "deviation": deviation,
        "status": "benchmark_pass" if matches else "benchmark_fail",
        "promotes_claims": False,
    }
