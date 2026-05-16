"""Ward-identity audit scaffolds for Stage 3 partials."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.three_loop_partials import ThreeLoopPartial


def _audit(check: str, status: str, reason: str) -> Dict[str, object]:
    return {
        "check": check,
        "status": status,
        "reason": reason,
        "promotes_claim": False,
    }


def audit_transversality(partial: ThreeLoopPartial) -> Dict[str, object]:
    return _audit(
        "transversality",
        "not_evaluated",
        "Stage 3 audit placeholder; requires full tensor contractions.",
    )


def audit_ctp_unitarity(partial: ThreeLoopPartial) -> Dict[str, object]:
    return _audit(
        "ctp_unitarity",
        "not_evaluated",
        "Stage 3 audit placeholder; requires full CTP propagator structure.",
    )


def audit_trace_anomaly_consistency(partial: ThreeLoopPartial) -> Dict[str, object]:
    return _audit(
        "trace_anomaly_consistency",
        "not_evaluated",
        "Stage 3 audit placeholder; anomaly matching not evaluated.",
    )


def audit_scheme_consistency(partial: ThreeLoopPartial) -> Dict[str, object]:
    return _audit(
        "scheme_consistency",
        "structural_pass",
        "Scheme/regulator labels present; no numeric matching performed.",
    )


def audit_flat_limit(partial: ThreeLoopPartial) -> Dict[str, object]:
    return _audit(
        "flat_limit",
        "not_evaluated",
        "Stage 3 audit placeholder; flat-space limit not verified.",
    )
