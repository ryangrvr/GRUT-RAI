"""
Allen-Jacobson scalar propagator on Euclidean S⁴ — INTERFACE STUB.

Phase-0 (this module): interface signature + documentation ONLY. The
actual propagator evaluation is the core Phase-1 task and is NOT
implemented here.

Reference: B. Allen and T. Jacobson, "Vector two-point functions in
maximally symmetric spaces," Commun. Math. Phys. 103, 669 (1986).

What the Phase-1 implementation needs to produce:

    G(x, x'; D, m²) = propagator for a massless (or mass-m) scalar on
                     Euclidean S⁴ of radius 1/H_inf, expressed in terms
                     of the geodesic distance σ(x, x') or equivalently
                     the chordal distance Z(x, x') = cos(H_inf · d).

The Allen-Jacobson form on S^D:

    G(Z) = Γ(h_+) Γ(h_−) / [(4π)^(D/2) Γ(D/2)] × F(h_+, h_−; D/2; (1+Z)/2)

where F is the Gauss hypergeometric ₂F₁ and

    h_± = (D−1)/2 ± √((D−1)²/4 − m²/H_inf²)

For D = 4 − 2ε and m² = 0 on S⁴: h_+ = 3 − 2ε, h_− = 2ε (from the
massless limit). F becomes a specific hypergeometric series.

The Phase-1 task: evaluate three such propagators in a 2-loop sunset
topology on S⁴ and extract the finite ε⁰ rational. The target is −100
(per V7 §26.2.6 / Correction #16); a successful derivation would
upgrade V8 §12's R value from CONDITIONAL to fully COMPUTED.

Obstacles to anticipate (Phase-0 identified):
1. SymPy may not close the hypergeometric integrals symbolically;
   specialist tooling (Mathematica + xAct, or a custom curved-space
   integration layer) may be required.
2. Hartle-Hawking thermal state at T_GH = H_inf/(2π) modifies the
   propagator via periodic identification — the specific form needs
   to be worked out.
3. The CTP sign flip (forward vs. backward branch on S⁴) enters the
   3-loop anomaly coefficient in a specific way that must be tracked
   through the calculation.

See `theory/derivation/TJI_PHASE_1_CALCULATION_PLAN.md` for the full
specification.
"""

from __future__ import annotations


class Phase1Pending(NotImplementedError):
    """Raised by any Allen-Jacobson function that requires Phase-1
    implementation. Message includes the specific Phase-1 task that
    needs to land before the function can return."""


def s4_propagator(Z, D=4, m_squared=0, H_inf=1.0):
    """Scalar propagator on Euclidean S⁴ at dimension D.

    ALL arguments are symbolic or numeric. The function is a stub —
    raises Phase1Pending. The Phase-1 implementation must return a
    SymPy expression in the chordal distance Z and the dimension D.

    Parameters
    ----------
    Z : SymPy expression or float
        Chordal distance Z(x, x') = cos(H_inf · d(x, x')) where d is
        the geodesic distance. Z = 1 at coincident points, Z = −1 at
        antipodal points.
    D : int or SymPy expression
        Spacetime dimension. Use D = 4 − 2ε (SymPy symbol) for
        dimensional regularization.
    m_squared : float or SymPy expression
        Scalar mass squared. Use 0 for massless (charged-lepton case).
    H_inf : float
        S⁴ Hubble scale (inverse radius). Set by GRUT's f(R) = 2−R
        cosmological formula; for the TJI calculation this is a
        parametric input.

    Raises
    ------
    Phase1Pending
        Phase-1 work required. The exact task and reference (Allen-
        Jacobson 1986) are documented in TJI_PHASE_1_CALCULATION_PLAN.md.

    Expected return (once implemented)
    ----------------------------------
    SymPy expression G(Z, D, m_squared, H_inf) suitable for multiplication
    into a 2-loop sunset integrand.
    """
    raise Phase1Pending(
        "Allen-Jacobson S^4 propagator evaluation is Phase-1 work. "
        "Required: implement G(Z, D, m²) = Γ(h_+)Γ(h_−)/[(4π)^(D/2) Γ(D/2)] "
        "× ₂F₁(h_+, h_−; D/2; (1+Z)/2) where h_± = (D−1)/2 ± "
        "√((D−1)²/4 − m²/H_inf²). Reference: Allen-Jacobson, Commun. "
        "Math. Phys. 103, 669 (1986). See "
        "theory/derivation/TJI_PHASE_1_CALCULATION_PLAN.md."
    )


def tji_on_s4(D, k_squared, indices, H_inf=1.0):
    """The curved-space analog of TJI[D, k², indices] on Euclidean S⁴.

    STUB. Raises Phase1Pending. Phase-1 must implement:

    1. Compose three Allen-Jacobson propagators into the 2-loop sunset
       topology with the specified Tarcer indices.
    2. Integrate over two loop momenta → equivalently, integrate over
       two internal positions on S⁴ with the S⁴ volume measure.
    3. Use the symmetric position x = x' = north pole (by S⁴ isometry)
       to reduce the double position-space integral to an integral
       over one S⁴-invariant angle.
    4. Laurent-expand around D = 4 − 2ε, extract ε⁰ finite rational.

    Target finite rational: −100, per V7 §26.2.6 (as −(Σ_SM Y²)²).

    Returns (once implemented)
    --------------------------
    SymPy expression — the Laurent expansion of TJI on S⁴, suitable for
    coefficient extraction analogous to
    grut.derivation.tji.flat_space.laurent_expansion_raw().
    """
    raise Phase1Pending(
        "TJI on Euclidean S⁴ is the core Phase-1 deliverable. The "
        "flat-space analog is implemented in "
        "grut.derivation.tji.flat_space. Curved-space requires the "
        "Allen-Jacobson propagator (see s4_propagator) and S⁴ "
        "integration measure. See TJI_PHASE_1_CALCULATION_PLAN.md."
    )


def interface_spec() -> dict:
    """Return a machine-readable description of the Phase-1 interface
    that Phase-0 has specified. Used by regression tests to verify
    the interface is stable across refactors before Phase-1 lands."""
    return {
        "module":                 "grut.derivation.tji.allen_jacobson",
        "propagator_function":    "s4_propagator",
        "propagator_signature":   ("Z", "D", "m_squared", "H_inf"),
        "integral_function":      "tji_on_s4",
        "integral_signature":     ("D", "k_squared", "indices", "H_inf"),
        "implementation_status":  "STUB — Phase-1 pending",
        "raises":                 "Phase1Pending on every call",
        "reference":              "Allen-Jacobson, Commun. Math. Phys. 103, 669 (1986)",
        "phase_1_plan":           "theory/derivation/TJI_PHASE_1_CALCULATION_PLAN.md",
        "target_finite_rational": -100,
        "target_interpretation":  "−(Σ_SM Y²)², V7 §26.2.6 / Correction #16",
    }
