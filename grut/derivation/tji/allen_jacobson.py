"""
Allen-Jacobson scalar propagator on Euclidean S⁴.

Phase-1 (this file): Allen-Jacobson propagator formula IMPLEMENTED.
Full 2-loop TJI Laurent extraction to ε⁰ = −100 is DEFERRED — the
hypergeometric ε-expansion of the sunset integral requires Mathematica
+ HypExp.  See S4CurvatureObstacle and tji_on_s4() for the precise
obstacle statement.  The tractable conformally-coupled radial integral
is implemented as a sanity path in tji_conformal_radial_integral().

Reference: B. Allen and T. Jacobson, "Vector two-point functions in
maximally symmetric spaces," Commun. Math. Phys. 103, 669 (1986).

Phase-1 deliverables (implemented here):
  s4_propagator()            — general Allen-Jacobson formula via ₂F₁
  s4_propagator_conformal()  — closed-form for conformally coupled scalar
  s4_propagator_uv_series()  — short-distance (Z→1) expansion
  volume_sphere()            — Vol(S^D) of unit sphere
  spectral_degeneracy()      — multiplicity d_n(D) on S^D
  spectral_eigenvalue()      — λ_n(D) = n(n+D-1)H²
  tji_conformal_radial_integral() — 1D Beta-function sanity path (conf.)
  tji_on_s4()               — raises S4CurvatureObstacle with Step map

Deferred to Mathematica + HypExp:
  Full Laurent expansion of ∫[G_minimal(Z)]³(1-Z²)^{(D-3)/2}dZ around D=4-2ε
  (Step B/C in TJI_PHASE_1_CALCULATION_PLAN.md).  Target ε⁰ = −100.

Euler-channel constraint (OR4 / R_DEFINITION.md):
  On round Euclidean S⁴ (Weyl²=0), only the Euler-density channel is
  protected.  The TJI ε⁰ coefficient must be extracted in the
  Euler channel (R_log_box_R kernel candidate) — not the Weyl or
  Im-log channels, which are blocked without off-shell continuation.
"""

from __future__ import annotations

from fractions import Fraction

import sympy as sp
from sympy import Symbol, gamma, sqrt, pi, hyper, Rational, simplify

EPS = Symbol("eps", positive=True)


# ─────────────────────────────────────────────────────────────────────
# Exceptions
# ─────────────────────────────────────────────────────────────────────

class Phase1Pending(NotImplementedError):
    """Kept for backward compatibility with Phase-0 tests.

    Phase-1 has replaced the propagator stub; tji_on_s4() now raises
    S4CurvatureObstacle instead.  This exception is no longer raised
    by any function in this module.
    """


class S4CurvatureObstacle(NotImplementedError):
    """Raised when a computation requires tools beyond SymPy.

    Specifically: the full 2-loop TJI Laurent extraction on S⁴ needs
    Mathematica + HypExp for the hypergeometric ε-expansion.  The
    exception message names the precise blocking step.
    """


# ─────────────────────────────────────────────────────────────────────
# Internal helpers
# ─────────────────────────────────────────────────────────────────────

def _h_pm(D, m_squared, H_inf):
    """Compute h± = (D−1)/2 ± √[(D−1)²/4 − m²/H²].

    These are the parameters of the Allen-Jacobson ₂F₁.

    For massless scalar (m²=0): h₊ = D−1, h₋ = 0.
    h₋ = 0 causes Γ(h₋) → ∞; use dim-reg (D = 4−2ε) or switch to
    s4_propagator_conformal() for the conformally-coupled case.
    """
    nu = sqrt(Rational(1, 4) * (D - 1) ** 2 - m_squared / H_inf ** 2)
    h_plus = (D - 1) / sp.Integer(2) + nu
    h_minus = (D - 1) / sp.Integer(2) - nu
    return h_plus, h_minus


# ─────────────────────────────────────────────────────────────────────
# Propagator — Phase-1 IMPLEMENTED
# ─────────────────────────────────────────────────────────────────────

def s4_propagator(Z, D=4, m_squared=0, H_inf=1):
    """Allen-Jacobson scalar propagator on S^D of radius 1/H_inf.

    G(Z; D, m², H) = Γ(h₊)Γ(h₋) / [(4π)^(D/2) Γ(D/2)]
                     × ₂F₁(h₊, h₋; D/2; (1+Z)/2)

    where h± = (D−1)/2 ± √[(D−1)²/4 − m²/H²].

    Parameters
    ----------
    Z : float or SymPy expression
        Chordal distance.  Z = 1: coincident points.  Z = −1: antipodal.
    D : int, float, or SymPy expression
        Spacetime dimension.  Use 4−2*EPS for dim-reg.
    m_squared : float or SymPy expression
        Scalar mass squared.  0 for massless (but see warning below).
    H_inf : float or SymPy expression
        Inverse radius of S^D (Hubble scale).  Default: unit sphere.

    Returns
    -------
    SymPy expression G(Z; D, m², H_inf).

    Warning
    -------
    For m_squared = 0 and integer D, h₋ = 0 and Γ(0) is a pole.
    Pass D = 4 − 2*EPS (a SymPy symbol) to obtain the dim-reg form,
    or use s4_propagator_conformal() for the ξ = (D-2)/(4(D-1)) case.

    Reference: Allen-Jacobson, Commun. Math. Phys. 103, 669 (1986).
    """
    h_plus, h_minus = _h_pm(D, m_squared, H_inf)
    prefactor = (
        gamma(h_plus) * gamma(h_minus)
        / ((4 * pi) ** (D / sp.Integer(2)) * gamma(D / sp.Integer(2)))
    )
    G = prefactor * hyper([h_plus, h_minus], [D / sp.Integer(2)], (1 + Z) / sp.Integer(2))
    return G


def s4_propagator_conformal(Z, D=4, H_inf=1):
    """Conformally-coupled scalar propagator on S^D — closed form.

    Conformal coupling: ξ = (D−2)/(4(D−1)).
    Effective mass: m²_eff = ξ·R_curv = D(D−2)H²/4.
    This gives h₊ = D/2, h₋ = (D−2)/2.

    Since ₂F₁(a, b; a; x) = (1−x)^{−b}:

        G_conf(Z; D, H) = Γ((D−2)/2) / (4π)^{D/2} × ((1−Z)/2)^{−(D−2)/2}

    For D = 4−2ε: G_conf = Γ(1−ε) / (4π)^{2−ε} × ((1−Z)/2)^{ε−1}.

    Flat-space limit (H→0, Z→1 with (1−Z)·R² → r²):
        G_conf → 1/(4π² r²) — the standard massless scalar in 4D. ✓

    Parameters
    ----------
    Z : float or SymPy expression
        Chordal distance.
    D : int, float, or SymPy expression
        Spacetime dimension.
    H_inf : float or SymPy expression
        Inverse radius.  Default: unit sphere.

    Returns
    -------
    SymPy expression for G_conf(Z; D).
    """
    h_minus_conf = (D - sp.Integer(2)) / sp.Integer(2)
    return (
        gamma(h_minus_conf)
        / (4 * pi) ** (D / sp.Integer(2))
        * ((1 - Z) / sp.Integer(2)) ** (-h_minus_conf)
    )


def s4_propagator_uv_series(D=4, H_inf=1, uv_var=None):
    """Short-distance (UV / coincidence) expansion of G_conf near Z = 1.

    Let u = (1−Z)/2 → 0⁺.  The conformally coupled propagator is:

        G_conf(u; D) = Γ((D−2)/2) / (4π)^{D/2} × u^{−(D−2)/2}

    For D = 4−2ε: u^{ε−1} = u^{−1} · e^{ε log u}
        = u^{−1} · (1 + ε log u + ε²(log u)²/2 + …)

    This is the leading UV singularity; it governs the 1/ε poles of
    loop integrals on S^D in the conformally coupled sector.

    Parameters
    ----------
    D : SymPy expression
        Spacetime dimension (use 4−2*EPS for dim-reg series).
    H_inf : float or SymPy expression
        Inverse radius.
    uv_var : SymPy Symbol or None
        Symbol for u = (1−Z)/2.  Created as ``u`` if None.

    Returns
    -------
    dict with keys ``u``, ``G_conf_u``, ``h_minus``, and ``D``.
    """
    u = uv_var if uv_var is not None else Symbol("u", positive=True)
    h_minus = (D - sp.Integer(2)) / sp.Integer(2)
    G_conf_u = gamma(h_minus) / (4 * pi) ** (D / sp.Integer(2)) * u ** (-h_minus)
    return {
        "u":         u,
        "G_conf_u":  G_conf_u,
        "h_minus":   h_minus,
        "D":         D,
        "note": (
            "u = (1-Z)/2 → 0 at coincidence. Leading singularity u^{-(D-2)/2}. "
            "For D=4-2ε: u^{ε-1} = u^{-1}·exp(ε log u). "
            "Use this to extract 1/ε poles from sunset integrand."
        ),
    }


# ─────────────────────────────────────────────────────────────────────
# Spectral / geometric helpers
# ─────────────────────────────────────────────────────────────────────

def volume_sphere(D, H_inf=1):
    """Volume of S^D of radius R = 1/H_inf.

        Vol(S^D) = 2π^{(D+1)/2} / Γ((D+1)/2) / H_inf^D

    For D = 4 (unit sphere, H_inf=1): Vol = 8π²/3. ✓
    """
    return (
        2 * pi ** ((D + sp.Integer(1)) / sp.Integer(2))
        / gamma((D + sp.Integer(1)) / sp.Integer(2))
        / H_inf ** D
    )


def spectral_degeneracy(n, D):
    """Degeneracy d_n of eigenvalue n on S^D.

        d_n(D) = (2n + D − 1) Γ(n + D − 1) / (Γ(D) Γ(n + 1))

    For D = 4, n ≥ 1: d_n = (n+1)(n+2)(2n+3)/6.
    For n = 0: d_0 = 1 (the constant eigenfunction, zero mode).
    """
    return (
        (2 * n + D - sp.Integer(1))
        * gamma(n + D - sp.Integer(1))
        / (gamma(D) * gamma(n + sp.Integer(1)))
    )


def spectral_eigenvalue(n, D, H_inf=1):
    """Eigenvalue λ_n of −∇² on S^D of radius 1/H_inf.

        λ_n(D) = n(n + D − 1) H_inf²

    For n = 0: λ_0 = 0 (zero mode — massless propagator singular here).
    """
    return n * (n + D - sp.Integer(1)) * H_inf ** 2


# ─────────────────────────────────────────────────────────────────────
# Tractable sanity path: conformally-coupled radial integral
# ─────────────────────────────────────────────────────────────────────

def tji_conformal_radial_integral(D=None, H_inf=1):
    """1D radial integral for the conformally-coupled sunset on S^D.

    The 2-loop sunset (3 parallel propagators, k²=0) in position space
    reduces by S^D isometry to a single integral over geodesic angle:

        I = Ω_{D-1} ∫₋₁¹ [G_conf(Z; D)]³ (1−Z²)^{(D-3)/2} dZ

    Using G_conf(Z; D) = C(D) · ((1−Z)/2)^{−(D−2)/2} with C(D) = Γ((D−2)/2)/(4π)^{D/2}:

        integrand powers: α = (D−3)/2 − 3(D−2)/2 = (−2D+3)/2,  β = (D−3)/2

        I = C(D)³ · Ω_{D-1} · 2^{α+β+1} · B(α+1, β+1)

        B(α+1, β+1) = Γ(α+1) Γ(β+1) / Γ(α+β+2)

    For D = 4−2ε:
        α = (−5+4ε)/2,  β = (1−2ε)/2
        α+1 = (−3+4ε)/2,  β+1 = (3−2ε)/2,  α+β+2 = ε
        Γ(α+β+2) = Γ(ε) → 1/ε as ε→0  →  B ~ ε · Γ(−3/2) · Γ(3/2)

    Physical interpretation: the conformally-coupled TJI vanishes at
    D = 4 (ε = 0).  This is expected — the conformal vacuum energy on
    S⁴ is zero at leading order.  The ε-correction is computable.

    This is a SANITY CHECK path; the physical −100 target uses minimal
    coupling with SM Yukawa species sum.  See tji_on_s4() obstacle.

    Parameters
    ----------
    D : SymPy expression or None
        Spacetime dimension.  Default: 4 − 2*EPS (dim-reg).
    H_inf : float or SymPy expression
        Inverse radius.

    Returns
    -------
    dict with symbolic integral, key intermediate expressions,
    and a diagnostic note.
    """
    if D is None:
        D = 4 - 2 * EPS

    C_D = gamma((D - sp.Integer(2)) / sp.Integer(2)) / (4 * pi) ** (D / sp.Integer(2))

    alpha = (D - sp.Integer(3)) / sp.Integer(2) - 3 * (D - sp.Integer(2)) / sp.Integer(2)  # = (−2D+3)/2
    beta  = (D - sp.Integer(3)) / sp.Integer(2)

    # ∫₋₁¹ (1-Z)^α (1+Z)^β dZ = 2^{α+β+1} B(α+1, β+1)
    exp_sum = alpha + beta + sp.Integer(1)                        # = (−D+2)/2
    B_int   = (2 ** exp_sum
               * gamma(alpha + sp.Integer(1))
               * gamma(beta  + sp.Integer(1))
               / gamma(alpha + beta + sp.Integer(2)))

    Omega_Dm1 = 2 * pi ** (D / sp.Integer(2)) / gamma(D / sp.Integer(2))  # Ω_{D-1}

    I_symbolic = C_D ** 3 * Omega_Dm1 * B_int

    return {
        "D":                    D,
        "H_inf":                H_inf,
        "C_D":                  C_D,
        "alpha_power":          alpha,           # power of (1-Z) in integrand
        "beta_power":           beta,            # power of (1+Z) in integrand
        "exp_sum":              exp_sum,         # α+β+1 = (2-D)/2
        "B_integral":           B_int,
        "Omega_Dm1":            Omega_Dm1,
        "I_conformal":          I_symbolic,
        "key_result":           (
            "For D=4-2ε: B_integral ~ ε·Γ(-3/2)·Γ(3/2)/2 → 0 as ε→0. "
            "Conformally-coupled TJI vanishes at D=4 (expected). "
            "The ε-correction is computable from the Laurent expansion."
        ),
        "note": (
            "SANITY PATH ONLY — not the physical −100 target. "
            "Physical result requires minimal coupling + SM Yukawa species sum. "
            "Minimal coupling blocked by h₋→0 zero-mode singularity; "
            "see tji_on_s4() S4CurvatureObstacle."
        ),
    }


# ─────────────────────────────────────────────────────────────────────
# TJI on S⁴ — Phase-1 obstacle documented
# ─────────────────────────────────────────────────────────────────────

def tji_on_s4(D, k_squared, indices, H_inf=1.0):
    """The curved-space TJI[D, k², indices] on Euclidean S⁴.

    Phase-1 status: OBSTACLE at Step B/C — raises S4CurvatureObstacle.

    The Allen-Jacobson propagator (s4_propagator) is IMPLEMENTED above.
    The 2-loop sunset integral from propagator to ε⁰ Laurent coefficient
    is blocked by the following three steps:

        Step A — hypergeometric product:
            [G_min(Z)]³ = [₂F₁(h₊, h₋; D/2; (1+Z)/2)]³ is a triple
            hypergeometric.  SymPy cannot close this when h₋ → 0
            (massless limit on S⁴).  Requires Mathematica + HypExp.

        Step B — radial integration:
            ∫₋₁¹ [G_min(Z)]³ (1−Z²)^{(D-3)/2} dZ is a Mellin-type
            integral with Z-dependent hypergeometric series in the
            integrand.  Tractable for conformally coupled (closed-form
            G); blocked for minimal coupling without HypExp.

        Step C — Laurent expansion and ε⁰ extraction:
            After Step B, Laurent-expand around D = 4−2ε and extract
            the ε⁰ finite rational.  Target: −100 = −(Σ_SM Y²)²
            (V7 §26.2.6 / Correction #16).  The species sum (Σ_SM Y² = 10)
            enters via the matter-loop SM Yukawa weighting.

    Euler-channel constraint (OR4 / R_DEFINITION.md):
        On round S⁴ (Weyl² = 0), the result must be read off in the
        Euler-density channel (R_log_box_R kernel).  Weyl and Im-log
        channels are blocked without off-shell continuation.

    Raises
    ------
    S4CurvatureObstacle
        With a description of the first blocking step.
        See TJI_PHASE_1_CALCULATION_PLAN.md §3 for the full plan.
    """
    if indices != ((1, 0), (1, 0), (1, 0)):
        raise S4CurvatureObstacle(
            "tji_on_s4: only Tarcer indices ((1,0),(1,0),(1,0)) are "
            "planned for Phase-1.  Higher indices require IBP reduction "
            "on S⁴ before the Allen-Jacobson form can be applied."
        )
    raise S4CurvatureObstacle(
        "tji_on_s4: Allen-Jacobson propagator (s4_propagator) is IMPLEMENTED. "
        "The 2-loop sunset Laurent extraction is blocked at Step A/B: "
        "hypergeometric ε-expansion of [₂F₁(h₊,h₋;D/2;(1+Z)/2)]³ "
        "integrated against (1−Z²)^{(D-3)/2} requires Mathematica + HypExp. "
        "For the conformally-coupled sanity path see tji_conformal_radial_integral(). "
        "Target: ε⁰ = −100 = −(Σ_SM Y²)². "
        "Euler-channel constraint: extract coefficient in R_log_box_R channel only. "
        "Reference: TJI_PHASE_1_CALCULATION_PLAN.md, Section 3."
    )


def interface_spec() -> dict:
    """Machine-readable Phase-1 interface spec.

    Used by regression tests to verify the interface remains stable
    and to document the current implementation status.
    """
    return {
        "module":                  "grut.derivation.tji.allen_jacobson",
        "propagator_function":     "s4_propagator",
        "propagator_signature":    ("Z", "D", "m_squared", "H_inf"),
        "integral_function":       "tji_on_s4",
        "integral_signature":      ("D", "k_squared", "indices", "H_inf"),
        "implementation_status":   (
            "Phase-1: propagator IMPLEMENTED (Allen-Jacobson formula + "
            "conformally-coupled closed form + UV series). "
            "TJI 2-loop Laurent extraction DEFERRED to Mathematica + HypExp."
        ),
        "raises":                  "S4CurvatureObstacle from tji_on_s4 (obstacle documented)",
        "reference":               "Allen-Jacobson, Commun. Math. Phys. 103, 669 (1986)",
        "phase_1_plan":            "theory/derivation/TJI_PHASE_1_CALCULATION_PLAN.md",
        "target_finite_rational":  -100,
        "target_interpretation":   "−(Σ_SM Y²)², V7 §26.2.6 / Correction #16",
        "propagator_status":       (
            "IMPLEMENTED: s4_propagator (general ₂F₁), "
            "s4_propagator_conformal (closed form), "
            "s4_propagator_uv_series (short-distance expansion)."
        ),
        "tji_obstacle":            (
            "Step A/B: [₂F₁(h₊,h₋;D/2;z)]³ × (1−Z²)^{(D-3)/2} Laurent expansion "
            "around D=4-2ε requires Mathematica + HypExp. "
            "Conformally-coupled sanity path in tji_conformal_radial_integral(). "
            "Euler-channel constraint: read ε⁰ in R_log_box_R channel only (OR4)."
        ),
    }
