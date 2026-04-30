"""Conformal-mode scalar — the KS 2011 derivation of α_vac.

This module hardens the GRUT claim:

    α_vac = 1/3 IS the trace-anomaly ratio a/c of a single real
    conformally-coupled scalar field in 4D, given the postulate
    that the gravitational conformal mode is the IR carrier of
    the vacuum's responsive susceptibility.

Reference: Komargodski-Schwimmer 2011 ("On Renormalization Group Flows
in Four Dimensions"), Christensen-Duff 1980, Duff 1994 ("Twenty Years
of the Weyl Anomaly").

The framework already specifies α_vac = 1/3 in `closure_protocol.py`
(historical provenance: v6.0 back-derivation from observed 15.47%
boost; v11 App H "α = 1/d" rationalization). This module supplies
the physical derivation: the per-species trace-anomaly coefficients
in the KS / Christensen-Duff convention give a/c = 1/3 EXACTLY for
a single real conformally-coupled scalar.

Postulate (the conditional that makes this a derivation):
    The gravitational conformal mode acts as the IR carrier of the
    vacuum's response. Under this identification, the framework's
    α_vac is the trace-anomaly ratio a/c of the IR carrier.

KS / Christensen-Duff per-species (a, c) coefficients in 4D:
    real conformally-coupled scalar:  (a, c) = (1, 3)   ⇒ a/c = 1/3
    Weyl fermion:                     (a, c) = (11/2, 9)
    gauge field:                      (a, c) = (62, 36)

These are the per-species coefficients in the convention where the
trace anomaly is written ⟨T^μ_μ⟩ = a · E_4 - c · W² + (trivial), and
the per-species values are normalized so a/c is dimensionless and
convention-independent. The framework's α_vac = 1/3 is the SCALAR
species' ratio, exact.
"""

from __future__ import annotations

from fractions import Fraction


# ─────────────────────────────────────────────────────────────────────
# Per-species trace-anomaly coefficients (KS 2011 / Christensen-Duff)
# ─────────────────────────────────────────────────────────────────────

A_REAL_SCALAR: Fraction = Fraction(1, 1)
"""Euler-density (a) coefficient for a single real conformally-coupled scalar."""

C_REAL_SCALAR: Fraction = Fraction(3, 1)
"""Weyl² (c) coefficient for a single real conformally-coupled scalar."""

A_WEYL_FERMION: Fraction = Fraction(11, 2)
"""Euler-density (a) coefficient for a single Weyl fermion."""

C_WEYL_FERMION: Fraction = Fraction(9, 1)
"""Weyl² (c) coefficient for a single Weyl fermion."""

A_GAUGE_BOSON: Fraction = Fraction(62, 1)
"""Euler-density (a) coefficient for a single gauge boson (4 polarizations)."""

C_GAUGE_BOSON: Fraction = Fraction(36, 1)
"""Weyl² (c) coefficient for a single gauge boson."""


# ─────────────────────────────────────────────────────────────────────
# Theorem-level derivation: a/c for a single real scalar IS 1/3
# ─────────────────────────────────────────────────────────────────────

def a_over_c_real_scalar() -> Fraction:
    """Trace-anomaly ratio a/c for a single real conformally-coupled scalar.

    Theorem (KS 2011 / Christensen-Duff 1980 / Duff 1994):

        a/c|_{single real conformally-coupled scalar} = 1/3 EXACTLY

    Proof: substitute the per-species coefficients (a, c) = (1, 3).
    """
    return A_REAL_SCALAR / C_REAL_SCALAR


def alpha_vac_from_conformal_mode_scalar() -> Fraction:
    """α_vac derived under the conformal-mode-scalar identification.

    Postulate: the gravitational conformal mode is the IR carrier of
    the vacuum's responsive susceptibility.

    Then α_vac = a/c for the IR carrier = a/c for a single real
    conformally-coupled scalar = 1/3.
    """
    return a_over_c_real_scalar()


def alpha_vac_postulate_statement() -> str:
    """Return the postulate that conditions the derivation.

    Surfaced explicitly so the registry's tier upgrade from anchored
    to computed reflects what's been hardened: the postulate is named,
    the algebra under the postulate is verified.
    """
    return (
        "Postulate: the gravitational conformal mode is the IR carrier "
        "of the vacuum's responsive susceptibility. Under this "
        "identification, α_vac IS the trace-anomaly ratio a/c of the "
        "IR carrier, which by Komargodski-Schwimmer 2011 / Christensen-"
        "Duff 1980 equals 1/3 exactly for a single real conformally-"
        "coupled scalar in 4D."
    )


# ─────────────────────────────────────────────────────────────────────
# General-species ratio (so SM cross-checks can use the same machinery)
# ─────────────────────────────────────────────────────────────────────

def a_total(n_0: int, n_half: int, n_1: int) -> Fraction:
    """Total Euler-density coefficient a for (n_0, n_½, n_1) species."""
    return (
        A_REAL_SCALAR * n_0
        + A_WEYL_FERMION * n_half
        + A_GAUGE_BOSON * n_1
    )


def c_total(n_0: int, n_half: int, n_1: int) -> Fraction:
    """Total Weyl² coefficient c for (n_0, n_½, n_1) species."""
    return (
        C_REAL_SCALAR * n_0
        + C_WEYL_FERMION * n_half
        + C_GAUGE_BOSON * n_1
    )


def a_over_c(n_0: int, n_half: int, n_1: int) -> Fraction:
    """Trace-anomaly ratio a/c for (n_0, n_½, n_1) species content."""
    return a_total(n_0, n_half, n_1) / c_total(n_0, n_half, n_1)


# ─────────────────────────────────────────────────────────────────────
# Cross-checks against the Standard Model (Path D)
# ─────────────────────────────────────────────────────────────────────

def a_over_c_sm_majorana() -> Fraction:
    """SM with Majorana neutrinos: 4 scalars + 45 Weyl + 12 gauge.

    Should yield 1991/1698 ≈ 1.17256, matching closure_protocol.py.
    """
    return a_over_c(n_0=4, n_half=45, n_1=12)


def a_over_c_sm_dirac() -> Fraction:
    """SM with Dirac neutrinos: 4 scalars + 48 Weyl (3 ν_R added) + 12 gauge.

    Should yield 253/219 ≈ 1.15525, matching closure_protocol.py and the
    Dirac-leaning falsifiable posture in the GRUT ToE.
    """
    return a_over_c(n_0=4, n_half=48, n_1=12)


def verify() -> dict:
    """Self-test the conformal-mode-scalar derivation chain."""
    from grut.foundation.closure_protocol import (
        ALPHA_VAC,
        A_OVER_C_SM_MAJORANA,
        A_OVER_C_SM_DIRAC,
    )

    return {
        # Theorem: real scalar a/c = 1/3 exactly
        "real_scalar_a_over_c_is_one_third": (
            a_over_c_real_scalar() == Fraction(1, 3)
        ),
        # Hardened claim: ALPHA_VAC matches the conformal-mode-scalar value
        "alpha_vac_matches_conformal_mode_scalar": (
            float(alpha_vac_from_conformal_mode_scalar()) == ALPHA_VAC
        ),
        # Path D cross-checks reproduce closure_protocol values exactly
        "a_over_c_sm_majorana_matches": (
            float(a_over_c_sm_majorana()) == A_OVER_C_SM_MAJORANA
        ),
        "a_over_c_sm_dirac_matches": (
            float(a_over_c_sm_dirac()) == A_OVER_C_SM_DIRAC
        ),
        # Algebraic identity check on the SM Majorana number
        "a_over_c_sm_majorana_is_1991_1698": (
            a_over_c_sm_majorana() == Fraction(1991, 1698)
        ),
        # Algebraic identity check on the SM Dirac number
        "a_over_c_sm_dirac_is_253_219": (
            a_over_c_sm_dirac() == Fraction(253, 219)
        ),
        # Per-species coefficients are integers / simple rationals
        "real_scalar_coefs_locked": (
            A_REAL_SCALAR == 1 and C_REAL_SCALAR == 3
        ),
        "weyl_fermion_coefs_locked": (
            A_WEYL_FERMION == Fraction(11, 2) and C_WEYL_FERMION == 9
        ),
        "gauge_boson_coefs_locked": (
            A_GAUGE_BOSON == 62 and C_GAUGE_BOSON == 36
        ),
    }
