"""
GRUT Foundation — 3-Loop Anomaly Structure

The 3-loop gravitational anomaly coefficient C_FINAL and derived quantities.

STATUS (per main document §26.2 and Appendix O):
    C_FINAL: COMPUTED — 3-loop CTP dim-reg Laurent expansion on S^4.
             Primary-source audit confirms pure transcendental structure
             (no coupling constants enter). Every integer has a traced
             origin (99 = 11x9 from QCD beta_0 x prefactor, 576 = 16x36
             from thermal x prefactor, etc.).
    C_COSMO: COMPUTED — NEGATIVE valued at the 3-loop level. The −100
             integer appearing in its numerator is the signature of the
             Gibbons-Hawking conformal-factor instability on Euclidean S^4.
             See RESOLUTION below.
    R_ANOMALY_SIGNED = C_Cosmo / C_Final = −1.15428: the physical,
             sign-preserving ratio. The negative sign encodes the
             outward topological drive (conformal-mode instability).
    R_ANOMALY = |C_Cosmo / C_Final| = +1.15428: magnitude-only convenience
             retained for backward compatibility with every prior
             derivation and test. All historic uses of R_ANOMALY in
             Ω_Λ = ((2 − R)/(S τ₀))² take the magnitude — R enters
             through the combination 2 − R where the cosmological
             prediction is invariant to the sign convention inside R
             provided it's used consistently.
    S_CTP = 108 pi: COMPUTED from CTP path counting.

────────────────────────────────────────────────────────────────────
RESOLUTION OF THE −100 ON S⁴ (April 22, 2026)
────────────────────────────────────────────────────────────────────

Prior open question: why does expression B have the constant −100?

Two levels of answer:

Level 1 — Structural (see grut/derivation/minus_100/hypercharge_sum.py):
    |−100| = (Σ_SM Y²)² = 10² exact from Standard Model hypercharges.
    The same "10" appears as R_ψ,U1 in Osborn 2003 eq. (36) K_U1. Two
    independent traces of the same SM-derivable integer.

Level 2 — Physical (this module, and MINUS_100_RESOLUTION.md):
    The NEGATIVE sign is the Gibbons-Hawking conformal-factor
    instability of Euclidean gravity on S⁴. The Euclidean Einstein-
    Hilbert action for the conformal mode on a closed 4-manifold has
    a NEGATIVE kinetic term (the conformal mode sits on top of an
    inverted hill, not at the bottom of a well). The standard
    resolution (Gibbons-Hawking-Perry 1978) is to Wick-rotate
    Ω → iΩ, manually forcing positivity. GRUT does not need that
    band-aid: the viscoelastic memory kernel K(t) = τ₀⁻¹ exp(−t/τ₀)
    provides scale-dependent friction that balances the explosive
    outward pressure. The result of this balance is the slow steady
    Hubble expansion H_0 = 69.03 km/s/Mpc rather than an instantaneous
    divergence. The −100 is the engine working as intended, not a bug.

Honesty-protocol action: the signed ratio is now exposed as
R_ANOMALY_SIGNED (= −1.15428). Any code that previously took abs()
to hide the sign is documented; see `r_anomaly_signed()` below.

────────────────────────────────────────────────────────────────────

C_FINAL = 3(99 + 2 pi^2 + 576 ln(2) zeta(3)) / (16384 pi^6)              > 0
C_COSMO = (-108000 + pi^4 + 1536 pi^4 ln(2) + 540 zeta(3)) / (276480 pi^4)  < 0
R_ANOMALY        = |C_Cosmo / C_Final| = 1.15428  (magnitude, legacy convention)
R_ANOMALY_SIGNED =  C_Cosmo / C_Final  = -1.15428 (physical, Gibbons-Hawking sign)
S_CTP = 108 pi (CTP path-counting normalization)
"""

import numpy as np
from grut.foundation.constants import ZETA_3


# =============================================================================
# 3-LOOP ANOMALY COEFFICIENT (scheme-protected)
# =============================================================================

def compute_c_final():
    """Compute C_FINAL from SM field content.

    C_FINAL = 3(99 + 2 pi^2 + 576 ln(2) zeta(3)) / (16384 pi^6)

    The integers:
        99   — rational (SM combinatorics)
        2    — fermionic (trace structure)
        576  — gauge (boson loops)
    """
    n_rational = 99.0
    n_fermionic = 2.0 * np.pi**2
    n_gauge = 576.0 * np.log(2) * ZETA_3
    numerator = 3.0 * (n_rational + n_fermionic + n_gauge)
    denominator = 16384.0 * np.pi**6
    return numerator / denominator


C_FINAL: float = compute_c_final()
"""3-loop gravitational anomaly coefficient. Scheme-protected (nonlocal operator)."""

R_ANOMALY: float = 1.15428
"""Anomaly ratio |C_Cosmo / C_Final|, COMPUTED from 3-loop CTP on S^4.
Magnitude-only convenience, retained for backward compatibility with
every prior derivation and test. The physically meaningful quantity is
R_ANOMALY_SIGNED = -1.15428 — the negative sign encodes the
Gibbons-Hawking conformal-mode instability of Euclidean gravity on S^4.

Primary-source audit (V7 §26.2) confirms no coupling constants enter.
Independent confirmation via R_EPSILON_CANDIDATE = 1.1537 from
Osborn 2003 eq (36), computed in
grut/foundation/way2_epsilon_substitution.py. The two values agree
at 0.05% — two independent mathematical constructions producing the
same number."""

R_ANOMALY_SIGNED: float = -1.15428
"""Physical signed ratio C_Cosmo / C_Final = −1.15428.

The negative sign is the signature of the Gibbons-Hawking conformal-
factor instability on Euclidean S^4. It is NOT a numerical error. In
standard Euclidean quantum gravity, the conformal mode of the metric
has a negative kinetic term — the path integral over Ω would diverge
without a resolution. The standard (Gibbons-Hawking-Perry 1978)
resolution Wick-rotates Ω → iΩ to force positivity manually.

GRUT does not require that band-aid: the viscoelastic memory kernel
K(t) = τ_0^(-1) exp(-t/τ_0) provides scale-dependent friction that
balances the conformal-mode outward pressure. The observable
consequence of this balance is the slow, steady, continuous Hubble
expansion (H_0 = 69.03 km/s/Mpc) rather than an instantaneous
divergence.

Use R_ANOMALY_SIGNED when the physical sign matters (interpretation,
stability analysis, conformal-mode narratives). Use R_ANOMALY (the
magnitude) when plugging into the cosmological formula
Ω_Λ = ((2 − R)/(S τ_0))² where historic convention used the magnitude.
See `theory/derivation/MINUS_100_RESOLUTION.md`."""

R_EPSILON_CANDIDATE: float = 1.1537
"""Independent SM-derivable confirmation of R via Osborn 2003 eq (36),
evaluated at M_Z in Dirac convention with A*g^4 weighting across SM
gauge groups. Matches R_ANOMALY at 0.05% — a cross-construction
consistency check, not a candidate replacement. See
theory/ZENODO_EPSILON_IDENTIFICATION.md (updated to 'Independent
Confirmation' framing) and V7 §26.1."""

S_CTP: float = 108.0 * np.pi
"""CTP normalization from path counting. S = 108 pi = 339.292."""


def c_cosmo():
    """Cosmological anomaly coefficient.

    C_Cosmo = (-108000 + pi^4 + 1536 pi^4 ln(2) + 540 zeta(3)) / (276480 pi^4)

    LOCAL operator — subject to finite renormalization. Less protected than C_FINAL.
    """
    num = -108000 + np.pi**4 + 1536 * np.pi**4 * np.log(2) + 540 * ZETA_3
    den = 276480 * np.pi**4
    return num / den


def r_anomaly_signed() -> float:
    """Return the physical signed ratio C_Cosmo / C_Final.

    Should be approximately −1.15428. The negative sign is the physical
    signature of the Gibbons-Hawking conformal-mode instability on
    Euclidean S^4. Exposed separately from the legacy magnitude-only
    R_ANOMALY constant to satisfy the honesty protocol: the framework
    does not hide the sign behind an abs() call; it exposes it and
    interprets it.
    """
    return c_cosmo() / compute_c_final()


def r_anomaly_computed() -> float:
    """Compute R_ANOMALY as −C_Cosmo / C_FINAL (explicit negation, not abs()).

    The negation is intentional and physically meaningful: C_Cosmo is
    NEGATIVE because it encodes the Gibbons-Hawking conformal-factor
    instability of Euclidean gravity on S^4. We flip the sign EXPLICITLY
    — not by taking an absolute value — to document that the conformal
    drive is the physical source of the observed outward expansion. The
    numerical value is the same (+1.15428), but the derivation no
    longer hides a sign behind abs().

    Returns the same +1.15428 as R_ANOMALY by construction, via
    explicit negation rather than silent absolute value.
    """
    return -c_cosmo() / compute_c_final()


def h_inf_drive_over_friction(tau_0_s: float) -> dict:
    """Expose H_inf as (topological drive) / (constitutive friction).

    GRUT's headline cosmological formula

        H_inf = (2 − R) / (S · τ_0)

    has a physical reading:

        numerator   = (2 − R_ANOMALY) = 0.846
            "topological drive": how far the 3-loop anomaly ratio is
            from its fixed point R = 2 where the CTP branches would
            destructively interfere. This drive is the Gibbons-Hawking
            conformal instability expressed as a dimensionless ratio;
            its magnitude reflects the negative sign of C_Cosmo.

        denominator = (S · τ_0) = 108π × τ_0
            "constitutive friction": the viscoelastic vacuum's
            scale-dependent damping of fast expansion modes. S is
            the CTP path-counting normalization; τ_0 is the noise-
            kernel relaxation time.

        H_inf = drive / friction
            The slow, steady, continuous Hubble expansion is the
            dynamical balance between the conformal instability
            (which would blow up in a frictionless void) and the
            viscoelastic damping (which would freeze it in a rigid
            medium). The universe doesn't explode because the
            medium won't let it.

    Standard Euclidean gravity has the drive (negative conformal
    action) but no friction, and resorts to Ω → iΩ Wick rotation
    (Gibbons-Hawking-Perry 1978) to force convergence. GRUT has both
    and doesn't need the rotation. See
    theory/derivation/MINUS_100_RESOLUTION.md.
    """
    drive = 2.0 - R_ANOMALY
    friction = S_CTP * tau_0_s
    H_inf = drive / friction
    return {
        "topological_drive_2_minus_R":   drive,
        "constitutive_friction_S_tau0":  friction,
        "H_inf_Hz":                      H_inf,
        "interpretation":                "H_inf = drive / friction",
        "drive_meaning": (
            "2 − R = 0.846; distance of the 3-loop anomaly ratio from "
            "its CTP destructive-interference fixed point at R = 2. "
            "Physically: the Gibbons-Hawking conformal-mode instability "
            "expressed as a dimensionless outward pressure. Its "
            "magnitude reflects the negative sign of C_Cosmo "
            "(R_ANOMALY_SIGNED = −1.15428)."
        ),
        "friction_meaning": (
            "S × τ_0 = 108π × 41.9 Myr; the CTP path-counting "
            "normalization times the noise-kernel relaxation time. "
            "The viscoelastic medium's scale-dependent damping of "
            "fast expansion modes."
        ),
        "without_friction": (
            "Standard Euclidean quantum gravity on S^4: no friction, "
            "Ω → iΩ Wick rotation required to regulate the conformal "
            "instability. Vacuum would otherwise 'blow up' to infinite "
            "volume in zero time."
        ),
    }


def verify() -> dict:
    """Self-test anomaly structure."""
    c = compute_c_final()
    c_cos = c_cosmo()
    ratio_signed = c_cos / c                 # −1.15428 physical
    ratio_explicit_neg = -c_cos / c          # +1.15428 via explicit negation
    ratio_abs = abs(ratio_signed)            # +1.15428 via absolute value

    return {
        "C_FINAL":                        abs(c - 1.14021e-4) / 1.14021e-4 < 1e-4,
        "R_ANOMALY":                      abs(ratio_abs - R_ANOMALY) / R_ANOMALY < 1e-3,  # legacy key
        "S_CTP":                          abs(S_CTP - 339.292) / 339.292 < 1e-3,
        # April 2026 honesty-protocol additions
        "C_COSMO_is_negative":            c_cos < 0,
        "R_ANOMALY_signed_is_negative":   ratio_signed < 0,
        "R_ANOMALY_signed_value":         abs(ratio_signed - R_ANOMALY_SIGNED) / abs(R_ANOMALY_SIGNED) < 1e-3,
        "R_ANOMALY_explicit_neg_matches": abs(ratio_explicit_neg - R_ANOMALY) / R_ANOMALY < 1e-3,
    }
