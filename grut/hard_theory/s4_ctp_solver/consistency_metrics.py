"""Consistency metrics for Stage 3E cross-checks."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.crosscheck_routes import RouteResult


def _result(comparison: str, status: str, reason: str) -> Dict[str, object]:
    return {
        "comparison": comparison,
        "status": status,
        "reason": reason,
        "promotes_claims": False,
    }


def compare_symbolic_forms(route_result_a: RouteResult, route_result_b: RouteResult) -> Dict[str, object]:
    if route_result_a.expression == route_result_b.expression:
        return _result("symbolic_forms", "consistent", "expressions match")
    return _result("symbolic_forms", "inconclusive", "expressions not identical")


def compare_limit_behavior(route_result_a: RouteResult, route_result_b: RouteResult) -> Dict[str, object]:
    if "flat_limit" in (route_result_a.route, route_result_b.route):
        return _result("limit_behavior", "inconclusive", "limit check not evaluated")
    return _result("limit_behavior", "inconclusive", "no explicit limit comparison")


def compare_scheme_metadata(route_result_a: RouteResult, route_result_b: RouteResult) -> Dict[str, object]:
    if route_result_a.scheme != route_result_b.scheme or route_result_a.regulator != route_result_b.regulator:
        return _result("scheme_metadata", "inconsistent", "scheme/regulator mismatch")
    return _result("scheme_metadata", "consistent", "scheme/regulator match")
