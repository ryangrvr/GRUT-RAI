"""Allen-Jacobson parameter branches for Gate 3 kernel definition.

This module exists to prevent underdefined Gate 3 retries.  It defines the
candidate h_+/h_- branches for

    2F1(h_plus, h_minus; D/2; u)

and provides a conformal benchmark reduction check before the 3-loop cube
integral is attempted.
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp


@dataclass(frozen=True)
class AJBranchSpec:
    """Concrete branch specification for the Allen-Jacobson kernel."""

    branch: str
    h_plus: sp.Expr
    h_minus: sp.Expr
    status: str
    notes: str
    purpose: str
    promotion_status: str


@dataclass(frozen=True)
class AJBranchSelection:
    """Resolved branch selection object passed into Gate 3 handoff."""

    branch_id: str
    purpose: str
    promotion_status: str


_ALLOWED_BRANCH_IDS = {
    "conformal_closed_form",
    "massive_regulated",
    "hminus_direct_limit",
    "hminus_derivative_regularized",
    "mmc_massless",
}


def dimension_from_epsilon(epsilon: sp.Symbol | None = None) -> sp.Expr:
    """Return dim-reg dimension D = 4 - 2 epsilon."""
    eps = epsilon if epsilon is not None else sp.Symbol("epsilon")
    return sp.Integer(4) - sp.Integer(2) * eps


def validate_m2_over_h2(m2_over_h2_str: str) -> tuple[bool, str]:
    """Validate GATE3_M2_OVER_H2 as positive rational/decimal string.

    Returns (is_valid, error_message).
    """
    if not m2_over_h2_str:
        return False, "GATE3_M2_OVER_H2 is empty or unset"

    # Try to parse as numeric
    try:
        val = float(m2_over_h2_str)
    except ValueError:
        return False, f"GATE3_M2_OVER_H2='{m2_over_h2_str}' is not numeric"

    if val <= 0:
        return False, f"GATE3_M2_OVER_H2={val} must be positive"

    return True, ""


def h_pm_massive(D: sp.Expr, m2_over_h2: sp.Expr) -> tuple[sp.Expr, sp.Expr]:
    """Massive scalar branch h_±(D, m^2/H^2)."""
    nu = sp.sqrt((D - 1) ** 2 / 4 - m2_over_h2)
    h_plus = (D - 1) / 2 + nu
    h_minus = (D - 1) / 2 - nu
    return h_plus, h_minus


def h_pm_conformal_scalar(D: sp.Expr) -> tuple[sp.Expr, sp.Expr]:
    """Conformally coupled scalar branch: h_+ = D/2, h_- = (D-2)/2."""
    return D / 2, (D - 2) / 2


def h_pm_massless_minimal(D: sp.Expr) -> tuple[sp.Expr, sp.Expr]:
    """Massless minimally coupled branch: h_+ = D-1, h_- = 0."""
    return D - 1, sp.Integer(0)


def allen_jacobson_kernel(u: sp.Expr, D: sp.Expr, h_plus: sp.Expr, h_minus: sp.Expr) -> sp.Expr:
    """Return the AJ hypergeometric kernel 2F1(h_+, h_-; D/2; u)."""
    return sp.hyper([h_plus, h_minus], [D / 2], u)


def conformal_closed_form_kernel(u: sp.Expr, D: sp.Expr) -> sp.Expr:
    """Known conformal closed form: 2F1(a, b; a; u) = (1-u)^(-b)."""
    return (1 - u) ** (-(D - 2) / 2)


def verify_conformal_kernel_reduction(u: sp.Expr | None = None, D: sp.Expr | None = None) -> sp.Expr:
    """Return simplified mismatch between AJ conformal branch and closed form.

    A correct reduction gives exactly 0.
    """
    u_sym = u if u is not None else sp.Symbol("u")
    D_sym = D if D is not None else sp.Symbol("D")
    h_plus, h_minus = h_pm_conformal_scalar(D_sym)
    aj = allen_jacobson_kernel(u_sym, D_sym, h_plus, h_minus)
    closed = conformal_closed_form_kernel(u_sym, D_sym)
    return sp.simplify(sp.expand_func(aj) - closed)


def build_branch_table(
    D: sp.Expr | None = None,
    m2_over_h2: sp.Expr | None = None,
) -> list[AJBranchSpec]:
    """Build the explicit AJ branch table used by Gate 3 preflight."""
    D_sym = D if D is not None else sp.Symbol("D")
    mu2 = m2_over_h2 if m2_over_h2 is not None else sp.Symbol("m2_over_h2")

    conf_hp, conf_hm = h_pm_conformal_scalar(D_sym)
    massive_hp, massive_hm = h_pm_massive(D_sym, mu2)
    mmc_hp, mmc_hm = h_pm_massless_minimal(D_sym)

    return [
        AJBranchSpec(
            branch="conformal_closed_form",
            h_plus=conf_hp,
            h_minus=conf_hm,
            status="benchmark",
            notes="Closed-form reduction must pass before nonlinear branches.",
            purpose="benchmark only",
            promotion_status="not target",
        ),
        AJBranchSpec(
            branch="massive_regulated",
            h_plus=massive_hp,
            h_minus=massive_hm,
            status="candidate",
            notes="Primary analytic branch h_±(D,m^2/H^2).",
            purpose="candidate regulator branch",
            promotion_status="possible",
        ),
        AJBranchSpec(
            branch="hminus_direct_limit",
            h_plus=mmc_hp,
            h_minus=mmc_hm,
            status="blocked until validated",
            notes="Direct h_- = 0 substitution can hide finite-term structure.",
            purpose="target-like but singular risk",
            promotion_status="blocked until validated",
        ),
        AJBranchSpec(
            branch="hminus_derivative_regularized",
            h_plus=sp.Symbol("h_plus_reg"),
            h_minus=sp.Symbol("h_minus_reg"),
            status="investigate",
            notes="Preferred target candidate: derivative/regularized h_- -> 0 branch.",
            purpose="likely best target candidate",
            promotion_status="investigate",
        ),
        AJBranchSpec(
            branch="mmc_massless",
            h_plus=mmc_hp,
            h_minus=mmc_hm,
            status="likely blocked",
            notes="Zero-mode / IR singular structure in massless minimally coupled branch.",
            purpose="zero-mode problematic",
            promotion_status="blocked",
        ),
    ]


def branch_table_rows(
    D: sp.Expr | None = None,
    m2_over_h2: sp.Expr | None = None,
) -> list[dict[str, str]]:
    """Return branch table in serializable string form for reports/docs."""
    rows: list[dict[str, str]] = []
    for spec in build_branch_table(D=D, m2_over_h2=m2_over_h2):
        rows.append(
            {
                "branch": spec.branch,
                "h_plus": str(spec.h_plus),
                "h_minus": str(spec.h_minus),
                "status": spec.status,
                "notes": spec.notes,
                "purpose": spec.purpose,
                "promotion_status": spec.promotion_status,
            }
        )
    return rows


def allowed_branch_ids() -> list[str]:
    """Return sorted list of allowed branch IDs for external guards."""
    return sorted(_ALLOWED_BRANCH_IDS)


def select_branch(branch_id: str, *, D: sp.Expr | None = None, m2_over_h2: sp.Expr | None = None) -> AJBranchSelection:
    """Validate and return a concrete branch selection object."""
    if branch_id not in _ALLOWED_BRANCH_IDS:
        joined = ", ".join(allowed_branch_ids())
        raise ValueError(f"invalid branch_id '{branch_id}'. allowed: {joined}")

    for spec in build_branch_table(D=D, m2_over_h2=m2_over_h2):
        if spec.branch == branch_id:
            return AJBranchSelection(
                branch_id=spec.branch,
                purpose=spec.purpose,
                promotion_status=spec.promotion_status,
            )

    raise ValueError(f"branch_id '{branch_id}' could not be resolved")
