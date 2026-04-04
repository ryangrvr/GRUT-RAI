"""Skyrme Term Nativity Audit.

The Appendix M audit (localized_bosonic_object_audit.py) established that the
only missing ingredient between 'particle_candidate_not_yet_established' and a
stable bosonic localized object is the Skyrme term L₄.  This module asks the
strictly bounded question:

  PRIMARY QUESTION
  ----------------
  Does an L₄-type stabilizing term arise naturally from GRUT's existing
  constitutive, topological, and action-sector architecture, or would adding
  it be external patchwork?

This question has a precise meaning:
  NATIVE:   L₄ can be derived — not merely asserted — from current GRUT
            mechanisms, without introducing new free parameters not already
            fixed by the architecture.
  PATCHWORK: L₄ must be imported as an additional postulate or free-parameter
             term not constrained by the existing architecture.

The honest intermediate case is also encoded:
  MOTIVATED-BUT-UNBUILT: L₄ is the natural next-order term in a derivation
  chain that GRUT is on track to construct, but that chain is not yet complete.

THE SKYRME TERM
---------------
  L₄ = (1/16e²) [∂_μΦᵃ × ∂_νΦᵃ]²
     = (1/16e²) (|∂_μΦᵃ|² |∂_νΦᵃ|² − (∂_μΦᵃ · ∂_νΦᵃ)²)

  This is a quartic-in-gradients O(3)-invariant term in the O(3) nonlinear
  sigma model action.  Under Derrick rescaling r → λr in D=3:
      E₂[φ_λ] = λ^{D-2} E₂ = λ E₂
      E₄[φ_λ] = λ^{D-4} E₄ = λ^{-1} E₄   ← opposes collapse

  Stationarity: dE/dλ|_{λ=1} = E₂ − E₄ = 0  →  E₄ = E₂ at the soliton.
  This is the Bogomol'ny-type relation for a stable skyrmion radius.

  The Skyrme coupling e is a new free parameter (mass dimension −1 in units
  where f_π = 1).  It sets the size and binding energy of the skyrmion.

CRITICAL DISTINCTION: Field-Space Quartic vs. Gradient Quartic
--------------------------------------------------------------
  Phase D1+ (defect_admissibility.py) contains the Mexican hat potential:
      V(Φ) = −(1/2)μ²|Φ|² + (1/4)λ|Φ|⁴

  This is quartic IN FIELD SPACE, not quartic IN GRADIENTS.
  Under Derrick rescaling in D=3:
      E_V[φ_λ] = λ^D E_V = λ³ E_V   ← POSITIVE scaling, same sign as E₂

  dE/dλ|_{λ=1} = E₂ + 3E_V > 0 always (both terms positive).
  The Mexican hat potential does NOT stabilize against Derrick collapse.
  The hedgehog in Phase D1+ remains Derrick-unstable with or without V(Φ).

FIVE DERIVATION ROUTES AUDITED
-------------------------------
  Route 1 — Constitutive ODE gradient expansion
    The relaxation ODE τ_eff·dΦ/dt + Φ = X is first-order and linear.
    Higher-order gradient (Burnett) expansion: temporal corrections only at
    leading order; quartic spatial gradients require specific anisotropic
    gradient structure not present in the spherically-symmetric quasi-static
    architecture.
    Status: NOT ESTABLISHED.

  Route 2 — Galley CTP effective action
    In the CTP formalism, integrating out the minus sector (g_- sector)
    can generate higher-derivative terms in the effective action.  The g_-
    source vanishes at equilibrium (g_minus_closure_audit.py: static source
    closed).  The fluctuation-level CTP computation around equilibrium has
    not been done.  In fluid EFT, CTP integration produces viscous terms;
    in scalar EFT it can produce (∇Φ)⁴ terms at one loop.
    Whether GRUT's specific CTP architecture produces L₄ is uncomputed.
    Status: OPEN BUT UNBUILT.

  Route 3 — O(3) derivative expansion
    The O(3) nonlinear sigma model is the leading-order term in a systematic
    derivative expansion of an O(3)-symmetric EFT.  The unique next-order
    (4-derivative) O(3)-invariant term IS the Skyrme term L₄ (up to total
    derivatives and equations of motion).  This is a structural fact of the
    O(3) EFT, not a GRUT-specific derivation.
    CONDITION: the O(3) sector must first be established as canonical GRUT
    (currently: Phase D1+ candidate extension, not canon).
    IF O(3) is established from GRUT canon, L₄ is the natural, unique,
    unavoidable next-order term — not a free addition.
    Status: CONDITIONALLY OPEN — strongest route; conditioned on O(3) nativity.

  Route 4 — Phase D1+ Mexican hat potential (field-space quartic)
    The λ|Φ|⁴ potential in defect_admissibility.py is quartic in field-space.
    Under Derrick scaling: E_V ~ λ³ (same sign as E₂), so dE/dλ = E₂ + 3E_V > 0.
    The hedgehog remains Derrick-unstable with or without V(Φ).
    The field-space quartic does NOT constitute or generate an L₄-type gradient
    quartic.  These are structurally distinct objects.
    Status: NOT ESTABLISHED AS SKYRME ANALOG — different term, different physics.

  Route 5 — Barrier action underdetermination
    The Equilibrium Source Degeneracy Theorem (barrier_action_sector.py):
    "the equilibrium constitutive primitives alone do not identify a unique
    barrier action."  This underdetermination means L₄ is COMPATIBLE with the
    barrier action space but is NOT REQUIRED by it.  The theorem permits L₄
    without generating it.
    Status: OPEN BUT UNDETERMINED — permits, does not derive.

NATIVITY CRITERIA (all three must pass for "native" verdict)
------------------------------------------------------------
  N1 — DERIVABILITY:
    L₄ can be derived from current GRUT mechanisms without additional postulates.
    Result: FAILS — no derivation route is established.  Route 3 is the
    closest, but it requires O(3) nativity as a prerequisite.

  N2 — PARAMETER-FREE:
    Adding L₄ does not introduce new free parameters.
    Result: FAILS — the Skyrme coupling e is a new free parameter not fixed by
    any current GRUT constant (α_vac, β_Q, τ², M_ext, R_eq, ω₀).
    Route 3 note: IF O(3) is established and IF e can be expressed in terms of
    GRUT parameters, this criterion might be satisfied — but neither is done.

  N3 — ARCHITECTURAL ORIGIN:
    L₄ arises from GRUT's specific constitutive/topological structure (not just
    from general EFT universality arguments).
    Result: FAILS — Route 3 is a general O(3) EFT argument; the Skyrme term is
    the next-order term in ANY O(3) sigma model, not specifically in GRUT's O(3).
    The GRUT-specific architecture has not been shown to require or select L₄
    over other possible 4-derivative terms (e.g., (∂²Φᵃ)² or topological terms).

PATCHWORK CLASSIFICATION
------------------------
  The nativity assessment drives a patchwork classification:
    derives_from_native_architecture:   False (no derivation established)
    motivated_but_unbuilt:              True  (Route 3 gives structural motivation)
    compatible_but_ad_hoc:              True  (adding e as free param would be ad hoc)
    incompatible_with_prior_doctrine:   False (adding L₄ violates no prior audit)

  Patchwork verdict: "motivated_but_unbuilt__adding_l4_without_o3_nativity_would_be_ad_hoc"

  The distinction:
    - Adding L₄ after establishing O(3) from GRUT canon: motivated, not ad hoc.
    - Adding L₄ before establishing O(3) from GRUT canon: compatible but ad hoc.
    - Current state: O(3) is Phase D1+ candidate (not canon); therefore L₄ is
      currently in the "ad hoc if added now" category.

DOCTRINE COMPATIBILITY CHECK
-----------------------------
  Adding L₄ to the O(3) sector would:
    Preserve O(3) symmetry:          True  (L₄ is O(3)-invariant by construction)
    Preserve spherical symmetry:     True  (L₄ in hedgehog ansatz is spherically sym.)
    Introduce spinors:               False
    Introduce gauge fields:          False
    Violate tau_eff domain:          False (quasi-static; L₄ is a static term)
    Violate beta_Q hypothesis:       False (L₄ independent of barrier exponent)
    Violate Phi bifurcation:         False (applies to O(3), not trajectory/field Phi)
    Change theory class:             False (Skyrme model is O(3) sigma model + L₄)
    Introduce new free parameter:    True  (e: Skyrme coupling, unfixed by GRUT)
    Compatible with prior doctrine:  True

PRINCIPAL RESULTS
-----------------
  native_skyrme_support_found:              False
  strongest_route:                          "o3_derivative_expansion" (Route 3)
  o3_derivative_expansion_conditionally_open: True
  ctp_route_open_but_unbuilt:               True
  mexican_hat_not_skyrme_analog:            True
  barrier_underdetermination_permits_l4:    True
  skyrme_coupling_e_fixed_by_grut:          False  (free parameter)
  all_nativity_criteria_pass:               False
  doctrine_compatible:                      True
  theory_class_preserved:                   True
  patchwork_classification:                 "motivated_but_unbuilt"

  primary_verdict:   "no_native_skyrme_support_found"
  secondary_verdict: "effective_skyrme_analog_possible"

NONCLAIMS
---------
  1. NOT ruling out that GRUT can eventually derive L₄ — Route 3 (O(3) derivative
     expansion) is a coherent path: establish O(3) from GRUT canon, then L₄ is
     the unique natural next-order term.
  2. NOT claiming the Mexican hat potential in Phase D1+ is a Skyrme-type stabilizer.
     V(Φ) = λ|Φ|⁴ is field-space quartic; L₄ is gradient quartic.  Different objects.
  3. NOT claiming the Skyrme coupling e cannot eventually be expressed in GRUT
     parameters — this is an open question, not a closed negative.
  4. NOT claiming L₄ is incompatible with prior doctrine — it is compatible.
     The verdict is about nativity (derived vs imported), not compatibility.
  5. NOT claiming CTP cannot generate L₄ — it can in general EFT; whether GRUT's
     specific CTP architecture does so is an open computation, not a closed question.

References
----------
  grut/localized_bosonic_object_audit.py  — Appendix M: primary Derrick analysis
  grut/defect_admissibility.py            — Phase D1+: O(3) hedgehog, Mexican hat V
  grut/barrier_action_sector.py           — Equilibrium Source Degeneracy Theorem
  grut/fermionic_emergence_audit.py       — O(3) homotopy content, Hopf absent
  grut/phi_sector_bifurcation.py          — Phi bifurcation (trajectory vs field)
  grut/tau_eff_domain_declaration.py      — domain constraints
  grut/g_minus_closure_audit.py           — CTP g_- sector: source closed at equilibrium
  Skyrme (1961), Proc. R. Soc. A 260, 127 — original Skyrme term
  Adkins, Nappi, Witten (1983), Nucl. Phys. B 228, 552 — skyrmion quantization
  Derrick (1964), J. Math. Phys. 5, 1252  — no-go theorem for scalar solitons
  Weinberg (1979), Physica A 96, 327      — EFT derivative expansion systematics
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Any, Dict, FrozenSet, List, Optional


# ---------------------------------------------------------------------------
# Locked constants (from canonical GRUT equilibrium, β_Q = 2)
# ---------------------------------------------------------------------------

M_EXT: float = 0.5
R_EQ: float = 1.0 / 3.0
TAU_SQ: float = 1.5
ALPHA_VAC: float = 1.0 / 3.0
BETA_Q_CANON: float = 2.0

OMEGA_0_SQ: float = BETA_Q_CANON * M_EXT / (R_EQ ** 3)   # = 27.0
OMEGA_0: float = math.sqrt(OMEGA_0_SQ)                    # = sqrt(27)

X_EQ: float = M_EXT / (R_EQ ** 2)   # = 4.5

# Spatial dimension for Derrick analysis (from Appendix M)
SPATIAL_DIMENSION: int = 3

# Derrick scaling exponents under r → λr in D=3
DERRICK_KINETIC_EXPONENT: int = SPATIAL_DIMENSION - 2     # = 1  (E₂ ~ λ)
DERRICK_POTENTIAL_EXPONENT: int = SPATIAL_DIMENSION       # = 3  (E_V ~ λ³)
DERRICK_SKYRME_EXPONENT: int = SPATIAL_DIMENSION - 4      # = -1 (E₄ ~ λ⁻¹, stabilizing)

# O(3) derivative-expansion orders
O3_KINETIC_DERIVATIVE_ORDER: int = 2    # L₂: (∂_μΦᵃ)²
O3_SKYRME_DERIVATIVE_ORDER: int = 4     # L₄: [∂_μΦᵃ × ∂_νΦᵃ]²

# Skyrme coupling constant — NOT fixed by GRUT architecture
SKYRME_COUPLING_E: Optional[float] = None    # free parameter, value unknown
SKYRME_COUPLING_FIXED_BY_GRUT: bool = False  # must remain False in current architecture

# ---------------------------------------------------------------------------
# Closed verdict label set
# ---------------------------------------------------------------------------

ALLOWED_NATIVITY_VERDICTS: FrozenSet[str] = frozenset({
    "no_native_skyrme_support_found",
    "effective_skyrme_analog_possible",
    "native_higher_gradient_stabilizer_conditionally_supported",
    "requires_external_extension",
})

# Route status vocabulary
ALLOWED_ROUTE_STATUSES: FrozenSet[str] = frozenset({
    "established",
    "conditionally_open",
    "open_but_unbuilt",
    "not_established",
    "unexplored",
    "not_skyrme_analog",
    "compatible_but_undetermined",
})

# Patchwork classification vocabulary
ALLOWED_PATCHWORK_CLASSES: FrozenSet[str] = frozenset({
    "derives_from_native_architecture",
    "motivated_but_unbuilt",
    "compatible_but_ad_hoc",
    "incompatible_with_prior_doctrine",
})


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class DerivationRoute:
    """One candidate route for generating an L₄-type term from GRUT architecture."""
    route_id: int                       # 1..5
    name: str                           # short identifier
    source_module: str                  # GRUT module providing the basis
    mechanism: str                      # how L₄ might arise from this source
    status: str                         # from ALLOWED_ROUTE_STATUSES
    is_established: bool                # True only if derivation is complete
    is_open: bool                       # True if derivation is possible but unbuilt
    prerequisite_unmet: Optional[str]   # what must happen first (if conditionally_open)
    skyrme_coupling_derivable: bool     # whether e can be fixed from this route
    notes: List[str] = field(default_factory=list)


@dataclass
class DerrickScalingComparison:
    """Derrick scaling comparison between field-space quartic and gradient quartic.

    Clarifies that V = λ|Φ|⁴ (Mexican hat) is NOT the Skyrme term L₄.
    """
    spatial_dimension: int              # 3
    kinetic_exponent: int               # D - 2 = 1  (E₂ ~ λ¹)
    potential_exponent: int             # D = 3      (E_V ~ λ³)
    skyrme_exponent: int               # D - 4 = -1 (E₄ ~ λ⁻¹)
    mexican_hat_stabilizes: bool        # False — dE/dλ = E₂ + 3E_V > 0
    skyrme_stabilizes: bool             # True — dE/dλ = E₂ − E₄ = 0 at minimum
    derrick_stationarity_condition_kinetic_potential: str  # E₂ + 3E_V > 0 → no min
    derrick_stationarity_condition_kinetic_skyrme: str     # E₂ − E₄ = 0 → stable min
    verdict: str                        # "field_space_quartic_is_not_skyrme_analog"
    notes: List[str] = field(default_factory=list)


@dataclass
class NativityCriterion:
    """One nativity criterion for L₄."""
    criterion_id: int                   # 1, 2, 3
    name: str                           # N1/N2/N3
    description: str                    # what this criterion requires
    passes: bool                        # True if current architecture satisfies it
    reason_for_failure: Optional[str]   # if not passes
    conditional_path: Optional[str]     # what would make it pass in future
    notes: List[str] = field(default_factory=list)


@dataclass
class DoctrineCompatibilityCheck:
    """Check whether adding L₄ would violate any prior GRUT audit verdict."""
    preserves_o3_symmetry: bool         # True — L₄ is O(3)-invariant
    preserves_spherical_symmetry: bool  # True
    introduces_spinors: bool            # False
    introduces_gauge_fields: bool       # False
    violates_tau_eff_domain: bool       # False
    violates_beta_q_hypothesis: bool    # False
    violates_phi_bifurcation: bool      # False
    changes_theory_class: bool          # False (stays in O(3) sigma model class)
    introduces_new_free_parameter: bool # True — Skyrme coupling e
    compatible_with_prior_doctrine: bool  # True
    doctrine_impact_summary: str
    notes: List[str] = field(default_factory=list)


@dataclass
class PatchworkAssessment:
    """Assessment of whether adding L₄ would be native or patchwork."""
    derives_from_native_architecture: bool   # False
    motivated_but_unbuilt: bool              # True (Route 3: O(3) derivative expansion)
    compatible_but_ad_hoc: bool              # True (if added before O(3) nativity)
    incompatible_with_prior_doctrine: bool   # False
    patchwork_verdict: str                   # from ALLOWED_PATCHWORK_CLASSES
    condition_for_motivated_status: str      # what makes it "motivated" rather than ad hoc
    what_would_prevent_ad_hoc: str           # steps required before L₄ is not patchwork
    notes: List[str] = field(default_factory=list)


@dataclass
class SkyrmeTermNativityResult:
    """Master result of the Skyrme term nativity audit."""

    # Five derivation routes
    routes: List[DerivationRoute]

    # Derrick scaling comparison (Mexican hat vs Skyrme)
    derrick_comparison: DerrickScalingComparison

    # Three nativity criteria
    nativity_criteria: List[NativityCriterion]

    # Doctrine compatibility
    doctrine_check: DoctrineCompatibilityCheck

    # Patchwork assessment
    patchwork: PatchworkAssessment

    # Top-level Boolean summary
    native_skyrme_support_found: bool           # False
    any_route_established: bool                 # False
    any_route_conditionally_open: bool          # True (Route 3)
    any_route_open_but_unbuilt: bool            # True (Routes 2, 5)
    mexican_hat_is_not_skyrme_analog: bool      # True (critical distinction)
    skyrme_coupling_fixed_by_grut: bool         # False
    all_nativity_criteria_pass: bool            # False
    doctrine_compatible: bool                   # True

    # Strongest route
    strongest_route_name: str                   # "o3_derivative_expansion"
    strongest_route_status: str                 # "conditionally_open"

    # Verdicts
    primary_verdict: str                        # "no_native_skyrme_support_found"
    secondary_verdict: str                      # "effective_skyrme_analog_possible"

    # Nonclaims and diagnostics
    nonclaims: List[str]
    forbidden_inferences: List[str]
    diagnostics: Dict[str, Any]


# ---------------------------------------------------------------------------
# Route builders
# ---------------------------------------------------------------------------

def build_route_1_constitutive_gradient_expansion() -> DerivationRoute:
    """Route 1: Higher-order gradient expansion of the constitutive ODE."""
    return DerivationRoute(
        route_id=1,
        name="constitutive_gradient_expansion",
        source_module="tau_eff_domain_declaration.py / action_principle.py",
        mechanism=(
            "The constitutive ODE tau_eff * dPhi/dt + Phi = X is first-order.  "
            "A Burnett-type expansion to higher order might generate gradient-correction "
            "terms.  In kinetic theory, second-order Burnett yields temporal corrections.  "
            "Quartic spatial gradient terms (L_4-type) would require a specific anisotropic "
            "spatial structure not present in the spherically-symmetric quasi-static "
            "architecture.  The ODE is linear in Phi, so self-interaction terms (like "
            "the Skyrme product [d_mu Phi^a x d_nu Phi^a]^2) cannot arise from a "
            "linear first-order relaxation equation alone."
        ),
        status="not_established",
        is_established=False,
        is_open=False,
        prerequisite_unmet=(
            "A nonlinear constitutive ODE (or second-order gradient expansion) with "
            "specific anisotropic structure.  The current linear first-order ODE cannot "
            "generate quartic gradient self-interactions."
        ),
        skyrme_coupling_derivable=False,
        notes=[
            "ODE: tau_eff * dPhi/dt + Phi = X  (linear, first-order).",
            "Burnett expansion: second temporal derivative tau^2 * d^2Phi/dt^2 + ... ",
            "This gives temporal corrections, not quartic spatial gradients.",
            "Skyrme term requires: field triplet Phi^a AND [d_mu Phi^a x d_nu Phi^a]^2.",
            "The canonical/constitutive sector has a single scalar Phi, not a triplet.",
            "Route closed: constitutive sector operates in canonical scalar regime.",
        ],
    )


def build_route_2_ctp_effective_action() -> DerivationRoute:
    """Route 2: Higher-derivative terms from Galley CTP g_- sector."""
    return DerivationRoute(
        route_id=2,
        name="ctp_effective_action",
        source_module="grut/g_minus_closure_audit.py / Galley CTP structure",
        mechanism=(
            "In the Galley CTP (closed-time-path) formalism, the physical effective "
            "action is obtained by integrating out the relative sector (g_-, minus sector).  "
            "In fluid EFT and dissipative scalar theories, this CTP integration can "
            "generate higher-derivative kinetic terms at loop level.  The g_- source "
            "T^Phi_1 - T^Phi_2 vanishes at static equilibrium (g_minus_closure_audit.py: "
            "static source closed).  The fluctuation-level effective action — obtained by "
            "expanding around equilibrium and integrating out g_- fluctuations — could "
            "in principle produce quartic kinetic terms (omega^4 / Gamma^2) that "
            "in the static limit might reduce to L_4-type gradient terms."
        ),
        status="open_but_unbuilt",
        is_established=False,
        is_open=True,
        prerequisite_unmet=(
            "One-loop effective action from g_- sector around equilibrium must be "
            "computed.  This requires: (1) the propagator for g_- fluctuations; "
            "(2) the coupling of g_- to the O(3) sector or to gradient terms; "
            "(3) verification that the resulting term has the Skyrme tensor structure "
            "[d_mu Phi^a x d_nu Phi^a]^2 rather than a different quartic combination."
        ),
        skyrme_coupling_derivable=False,
        notes=[
            "g_- source vanishes at static equilibrium (g_minus_closure_audit.py).",
            "At equilibrium: condition_2 'no homogeneous modes' is likely_false.",
            "Fluctuations around equilibrium: g_- homogeneous modes may be present.",
            "CTP effective action can produce (∇Φ)^4 terms in scalar EFT at one loop.",
            "Whether the specific Skyrme tensor structure emerges requires computation.",
            "If it does: Skyrme coupling e would be expressed in terms of GRUT damping.",
            "This is the most physically deep route — but entirely unbuilt.",
            "Reference path: Galley (2013) CTP; Grozdanov & Kaplis (2016) dissipative EFT.",
        ],
    )


def build_route_3_o3_derivative_expansion() -> DerivationRoute:
    """Route 3: O(3) derivative expansion — Skyrme is the unique next-order term.

    This is the STRONGEST and most structurally motivated route.
    """
    return DerivationRoute(
        route_id=3,
        name="o3_derivative_expansion",
        source_module="grut/defect_admissibility.py (Phase D1+) / O(3) EFT",
        mechanism=(
            "The O(3) nonlinear sigma model (L_2 = F_pi^2/8 |d_mu Phi^a|^2) is the "
            "LEADING-ORDER term in a systematic derivative expansion of any O(3)-symmetric "
            "EFT.  By the Weinberg counting (1979), the next-order 4-derivative term in "
            "the O(3) EFT is UNIQUE (up to total derivatives and equations of motion): "
            "it is the Skyrme term L_4 = (1/16e^2)[d_mu Phi^a x d_nu Phi^a]^2.  "
            "This uniqueness follows from the Bianchi identity for the O(3) current and "
            "the requirement of O(3) invariance at 4-derivative order.  "
            "Therefore: IF the O(3) sector in GRUT (Phase D1+) is established as the "
            "leading term in a GRUT derivative expansion, then L_4 is not a free "
            "addition — it is the natural, unavoidable, structurally required next term.  "
            "The question is not 'should we add L_4' but 'can we derive it from GRUT?'"
        ),
        status="conditionally_open",
        is_established=False,
        is_open=True,
        prerequisite_unmet=(
            "O(3) nativity from GRUT canon.  Currently O(3) is a candidate extension "
            "(Phase D1+), not derived from canonical GRUT.  The prerequisite chain is: "
            "(1) Derive the O(3) sector from GRUT's canonical scalar architecture or "
            "identify it as the EFT description of GRUT's topological sector; "
            "(2) Establish the EFT power counting that makes L_2 the leading term; "
            "(3) The Skyrme term L_4 then follows automatically as the next-order term.  "
            "Additionally: the Skyrme coupling e must be expressed in terms of GRUT "
            "parameters (alpha_vac, beta_Q, tau^2, M_ext) to satisfy the N2 criterion."
        ),
        skyrme_coupling_derivable=False,
        notes=[
            "Structural uniqueness of L_4: the ONLY 4-derivative O(3)-invariant term.",
            "Other 4-derivative terms either vanish on-shell, are total derivatives,",
            "or reduce to L_4 by O(3) Bianchi identity.",
            "If O(3) canon established: L_4 is not patchwork — it is required by the EFT.",
            "The Skyrme coupling e = f_pi / (4 * pi * r_skyrmion) — not yet from GRUT.",
            "Matching e to GRUT parameters: needs O(3) EFT matching to GRUT observables.",
            "Possibly e is related to: tau^2 = 1.5, omega_0^2 = 27, R_eq = 1/3.",
            "This is the path that makes L_4 motivated rather than ad hoc.",
            "Reference: Skyrme (1961); Adkins, Nappi, Witten (1983); Weinberg (1979).",
        ],
    )


def build_route_4_mexican_hat_potential() -> DerivationRoute:
    """Route 4: Phase D1+ Mexican hat potential — NOT a Skyrme analog.

    This route explicitly tests whether the existing λ|Φ|⁴ potential in
    defect_admissibility.py provides Skyrme-type stabilization.  It does not.
    """
    return DerivationRoute(
        route_id=4,
        name="mexican_hat_potential_field_space_quartic",
        source_module="grut/defect_admissibility.py",
        mechanism=(
            "Phase D1+ contains the Mexican hat symmetry-breaking potential: "
            "V(Phi) = -(1/2)mu^2|Phi|^2 + (1/4)lambda|Phi|^4.  "
            "This is QUARTIC IN FIELD SPACE (not in gradients).  "
            "Derrick scaling analysis in D=3: under r -> lambda*r, "
            "E_V[phi_lambda] = lambda^D E_V = lambda^3 E_V (positive exponent).  "
            "Total energy: E(lambda) = lambda E_2 + lambda^3 E_V.  "
            "dE/dlambda|_{lambda=1} = E_2 + 3 E_V > 0 (both terms positive).  "
            "No stationary point: configuration still collapses toward lambda -> 0.  "
            "The Mexican hat potential does NOT stabilize the hedgehog against Derrick "
            "collapse.  It sets the vacuum manifold S^2 (required for winding) but "
            "provides no energetic minimum at finite soliton size.  "
            "The Skyrme term is GRADIENT quartic: L_4 = [d_mu Phi^a x d_nu Phi^a]^2."
        ),
        status="not_skyrme_analog",
        is_established=False,
        is_open=False,
        prerequisite_unmet=None,
        skyrme_coupling_derivable=False,
        notes=[
            "V(Phi) = (lambda/4)|Phi|^4: quartic in field-space (phi^4 potential).",
            "L_4 = [d_mu Phi^a x d_nu Phi^a]^2: quartic in spacetime gradients.",
            "These are structurally different: one is a potential, one is a kinetic term.",
            "Derrick for V: E_V -> lambda^3 E_V  (positive, worsens instability).",
            "Derrick for L_4: E_4 -> lambda^{-1} E_4 (negative, stabilizes).",
            f"D=3: potential exponent = {SPATIAL_DIMENSION} (positive).",
            f"D=3: Skyrme exponent = {SPATIAL_DIMENSION - 4} (negative = stabilizing).",
            "Mexican hat in Phase D1+: sets vacuum manifold S^2 — necessary for winding.",
            "But S^2 vacuum manifold + kinetic term: STILL Derrick unstable.",
            "S^2 vacuum manifold + kinetic term + Skyrme term: STABLE (skyrmion).",
            "Hedgehog in defect_admissibility.py: Derrick unstable despite Mexican hat.",
            "FORBIDDEN INFERENCE: lambda|Phi|^4 implies Skyrme stabilization.",
        ],
    )


def build_route_5_barrier_underdetermination() -> DerivationRoute:
    """Route 5: Barrier action underdetermination — compatible but undetermined."""
    return DerivationRoute(
        route_id=5,
        name="barrier_action_underdetermination",
        source_module="grut/barrier_action_sector.py",
        mechanism=(
            "The Equilibrium Source Degeneracy Theorem (barrier_action_sector.py): "
            "'the equilibrium constitutive primitives alone do not identify a unique "
            "barrier action.'  The space of admissible barrier actions contains all "
            "terms compatible with the GRUT symmetries and equilibrium conditions.  "
            "The Skyrme term L_4 is ONE such compatible term — it is O(3)-invariant, "
            "spherically symmetric, and does not violate the equilibrium condition.  "
            "However, the underdetermination means L_4 is PERMITTED, not REQUIRED.  "
            "The barrier action theorem permits L_4 without generating it from "
            "equilibrium primitives.  This is 'compatible but undetermined.'"
        ),
        status="compatible_but_undetermined",
        is_established=False,
        is_open=True,
        prerequisite_unmet=(
            "A non-equilibrium or off-shell constraint that selects L_4 from the space "
            "of compatible barrier actions.  The equilibrium source degeneracy theorem "
            "explicitly says equilibrium primitives do not provide this selection.  "
            "An off-shell closure condition or a UV completion argument would be needed."
        ),
        skyrme_coupling_derivable=False,
        notes=[
            "Theorem: equilibrium primitives do not uniquely determine barrier action.",
            "Consequence: L_4 is in the space of compatible actions (not excluded).",
            "But the theorem does not select L_4 over other compatible actions.",
            "Adding L_4 would be consistent with the degeneracy theorem.",
            "But it would require an additional postulate to select L_4 specifically.",
            "The Skyrme coupling e is one of the free parameters in the underdetermined space.",
            "T^Phi underdetermination: even with L_4, T^Phi still requires closure input.",
            "This route: permits L_4, does not derive it.",
        ],
    )


def build_derrick_comparison() -> DerrickScalingComparison:
    """Build the Derrick scaling comparison between Mexican hat and Skyrme."""
    return DerrickScalingComparison(
        spatial_dimension=SPATIAL_DIMENSION,
        kinetic_exponent=DERRICK_KINETIC_EXPONENT,
        potential_exponent=DERRICK_POTENTIAL_EXPONENT,
        skyrme_exponent=DERRICK_SKYRME_EXPONENT,
        mexican_hat_stabilizes=False,
        skyrme_stabilizes=True,
        derrick_stationarity_condition_kinetic_potential=(
            "dE/d(lambda)|_{lambda=1} = E_2 + 3*E_V > 0  (always; no minimum)"
        ),
        derrick_stationarity_condition_kinetic_skyrme=(
            "dE/d(lambda)|_{lambda=1} = E_2 - E_4 = 0  (minimum at E_4 = E_2)"
        ),
        verdict="field_space_quartic_is_not_skyrme_analog__derrick_still_active_with_mexican_hat",
        notes=[
            f"D = {SPATIAL_DIMENSION}: Derrick scaling exponents:",
            f"  E_2 (kinetic gradient): lambda^{DERRICK_KINETIC_EXPONENT}  (positive → collapse)",
            f"  E_V (field-space quartic, Mexican hat): lambda^{DERRICK_POTENTIAL_EXPONENT}  (positive → worsens)",
            f"  E_4 (Skyrme, gradient quartic): lambda^{DERRICK_SKYRME_EXPONENT}  (negative → stabilizes)",
            "Mexican hat dE/dlambda = E_2 + 3*E_V: ALWAYS positive, no stationary point.",
            "Skyrme dE/dlambda = E_2 - E_4: ZERO at skyrmion radius, stable minimum.",
            "The Mexican hat sets the vacuum manifold (needed for winding).",
            "The Skyrme term sets the soliton size (needed for stability).",
            "Both are necessary for a stable hedgehog; current O(3) has only the Mexican hat.",
            "CRITICAL: lambda|Phi|^4 (field) and [d_mu Phi^a x d_nu Phi^a]^2 (gradient)",
            "have OPPOSITE Derrick scaling — they are not analogs.",
        ],
    )


def build_nativity_criteria(routes: List[DerivationRoute]) -> List[NativityCriterion]:
    """Build the three nativity criteria."""

    any_established = any(r.is_established for r in routes)
    any_coupling_derivable = any(r.skyrme_coupling_derivable for r in routes)

    n1 = NativityCriterion(
        criterion_id=1,
        name="N1_derivability",
        description=(
            "L₄ can be derived from current GRUT mechanisms without additional "
            "postulates beyond what is already established."
        ),
        passes=any_established,
        reason_for_failure=(
            None if any_established else
            "No derivation route is fully established.  Route 3 (O(3) derivative "
            "expansion) is the strongest but requires O(3) nativity as a prerequisite "
            "— and O(3) itself is a candidate extension (Phase D1+), not canon.  "
            "Route 2 (CTP) and Route 5 (barrier underdetermination) are open but "
            "unbuilt.  Route 1 (constitutive ODE) is closed.  Route 4 (Mexican hat) "
            "is not a Skyrme analog."
        ),
        conditional_path=(
            "Establish O(3) nativity from GRUT canon, then invoke Route 3: "
            "the Skyrme term is the unique next-order O(3)-invariant 4-derivative term."
        ),
        notes=[
            "N1 fails because no route reaches 'established' status.",
            "Route 3 would pass N1 IF O(3) canon is first established.",
            "Route 2 would pass N1 IF CTP one-loop computation is done.",
        ],
    )

    n2 = NativityCriterion(
        criterion_id=2,
        name="N2_parameter_free",
        description=(
            "Adding L₄ does not introduce new free parameters not fixed by the "
            "existing GRUT architecture (specifically, the Skyrme coupling e must "
            "be expressible in terms of current GRUT constants)."
        ),
        passes=any_coupling_derivable,
        reason_for_failure=(
            None if any_coupling_derivable else
            "The Skyrme coupling constant e is a new free parameter not fixed by "
            "any current GRUT constant (alpha_vac = 1/3, beta_Q = 2, tau^2 = 1.5, "
            "M_ext = 0.5, R_eq = 1/3, omega_0 = sqrt(27)).  No route currently "
            "derives e from GRUT parameters.  Route 3 offers a conditional path: "
            "if O(3) EFT matching is completed, e might be expressible in terms of "
            "GRUT's characteristic scales (e.g., e ~ 1/(alpha_vac * omega_0 * tau))."
        ),
        conditional_path=(
            "Complete Route 3 (O(3) nativity) AND the EFT matching step that expresses "
            "e in terms of GRUT parameters.  This might give e ~ f(alpha_vac, tau, omega_0)."
        ),
        notes=[
            "N2 is the strictest criterion: any new free parameter is disqualifying.",
            "The Skyrme coupling e sets: skyrmion size ~ e/f_pi, binding energy ~ f_pi/e.",
            "GRUT has no identified f_pi-analog or e-analog in current architecture.",
            "Conditionally: e could be expressed in terms of GRUT scales after matching.",
            f"Possible relation (speculative, not established): e ~ 1/(OMEGA_0 * TAU_SQ) = "
            f"1/({OMEGA_0:.4f} * {TAU_SQ}) = {1.0 / (OMEGA_0 * TAU_SQ):.6f}.",
        ],
    )

    all_pass = any_established and any_coupling_derivable

    n3 = NativityCriterion(
        criterion_id=3,
        name="N3_architectural_origin",
        description=(
            "L₄ arises from GRUT's specific constitutive/topological structure, "
            "not merely from general O(3) EFT universality arguments that would "
            "apply to any O(3) sigma model regardless of GRUT specifics."
        ),
        passes=False,
        reason_for_failure=(
            "Route 3 (O(3) derivative expansion) is a general EFT argument: the Skyrme "
            "term is the next-order term in ANY O(3) sigma model, not specifically in "
            "GRUT's O(3).  This makes Route 3 'motivated' but not GRUT-specific.  "
            "For N3 to pass, GRUT's specific architecture (tau_eff, barrier, Galley CTP, "
            "alpha_vac = 1/3, beta_Q = 2) would need to select L_4 over other possible "
            "4-derivative terms or determine the coefficient e from GRUT parameters.  "
            "Route 2 (CTP) is the most architecturally specific route — it uses GRUT's "
            "g_- structure directly — but is unbuilt."
        ),
        conditional_path=(
            "Route 2 (CTP computation) would satisfy N3 if the g_- fluctuation sector "
            "can be shown to produce specifically L_4 (not just any quartic gradient term).  "
            "This would require the Skyrme tensor structure [d_mu Phi^a x d_nu Phi^a]^2 "
            "to emerge from the GRUT-specific CTP coupling."
        ),
        notes=[
            "N3 distinguishes GRUT-specific origin from generic EFT universality.",
            "Route 3 is EFT-universal: applies to any O(3) sigma model.",
            "Route 2 is GRUT-specific: uses GRUT's CTP structure.",
            "Current state: the GRUT-specific route (Route 2) is unbuilt.",
            "N3 would pass if Route 2 produces L_4 from GRUT's g_- sector.",
        ],
    )

    return [n1, n2, n3]


def build_doctrine_compatibility() -> DoctrineCompatibilityCheck:
    """Check whether adding L₄ would violate any prior GRUT audit verdict."""
    return DoctrineCompatibilityCheck(
        preserves_o3_symmetry=True,
        preserves_spherical_symmetry=True,
        introduces_spinors=False,
        introduces_gauge_fields=False,
        violates_tau_eff_domain=False,
        violates_beta_q_hypothesis=False,
        violates_phi_bifurcation=False,
        changes_theory_class=False,
        introduces_new_free_parameter=True,
        compatible_with_prior_doctrine=True,
        doctrine_impact_summary=(
            "Adding L_4 to the O(3) sector is COMPATIBLE with all prior GRUT audit "
            "verdicts.  It does not: change the symmetry class (stays O(3) sigma model), "
            "introduce spinors (fermionic_emergence_audit: clean), violate the tau_eff "
            "domain (L_4 is a static term; quasi-static domain applies), violate beta_Q "
            "hypothesis (L_4 is independent of the barrier exponent), or contradict the "
            "Phi bifurcation (L_4 applies to the O(3) triplet Phi^a, not trajectory/field "
            "Phi).  The one impact: introduces the Skyrme coupling e as a new free parameter, "
            "which would need to become a new working hypothesis (like beta_Q = 2)."
        ),
        notes=[
            "O(3) invariance: L_4 = [d_mu Phi^a x d_nu Phi^a]^2 is manifestly O(3)-inv.",
            "Spherical symmetry: L_4 in the hedgehog ansatz respects SO(3) rotation.",
            "tau_eff domain: L_4 contributes to static energy density, not tau_eff ODE.",
            "beta_Q: the Skyrme term does not involve the barrier exponent.",
            "Phi bifurcation: L_4 lives in the O(3) triplet Phi^a sector (not the",
            "  constitutive scalar Phi(r,t) or trajectory M_drive(t)).",
            "Theory class: O(3) sigma model with L_4 = Skyrme model (same class).",
            "New parameter e: would need to be added as working hypothesis with status",
            "  analogous to beta_Q = 2 (assumed, sensitivity mapped).",
        ],
    )


def build_patchwork_assessment(
    routes: List[DerivationRoute],
    criteria: List[NativityCriterion],
) -> PatchworkAssessment:
    """Assess whether adding L₄ would be native or patchwork."""

    any_established = any(r.is_established for r in routes)
    route3 = next(r for r in routes if r.name == "o3_derivative_expansion")
    motivated = route3.is_open and not route3.is_established

    return PatchworkAssessment(
        derives_from_native_architecture=any_established,
        motivated_but_unbuilt=motivated,
        compatible_but_ad_hoc=True,
        incompatible_with_prior_doctrine=False,
        patchwork_verdict="motivated_but_unbuilt",
        condition_for_motivated_status=(
            "The O(3) derivative expansion (Route 3) gives L_4 motivated status IF: "
            "(1) the O(3) sector is established from GRUT canon (not just Phase D1+); "
            "(2) the EFT power counting is shown to be valid in GRUT's regime; "
            "(3) the Skyrme coupling e is expressed in GRUT parameters (N2 criterion).  "
            "Under these conditions, L_4 is not a free addition but the structural "
            "next-order term in GRUT's O(3) EFT — motivated, not ad hoc."
        ),
        what_would_prevent_ad_hoc=(
            "Before L_4 is added, the prerequisite chain must be completed: "
            "(1) O(3) nativity audit: demonstrate O(3) arises from GRUT canon "
            "    (or formally establish it as a first-class extension); "
            "(2) EFT counting: show L_2 is leading order in GRUT's derivative expansion; "
            "(3) Skyrme coupling: express e in terms of GRUT constants "
            "    (alpha_vac, tau^2, omega_0, R_eq) or designate e as a new canon parameter "
            "    with a worked sensitivity analysis (analogous to beta_Q_sensitivity.py); "
            "(4) Derrick verification: confirm skyrmion radius is consistent with R_eq "
            "    and the GRUT quasi-static domain."
        ),
        notes=[
            "Current patchwork classification: motivated_but_unbuilt.",
            "This is distinct from 'compatible_but_ad_hoc' (which applies if added now,",
            "  before O(3) nativity is established).",
            "And distinct from 'derives_from_native_architecture' (which requires full",
            "  derivation — not yet achieved).",
            "The patchwork question has a clear answer: adding L_4 NOW would be ad hoc.",
            "Adding L_4 AFTER O(3) nativity and coupling matching would NOT be patchwork.",
            "The prerequisite chain has at most 4 steps — it is not indefinitely deferred.",
        ],
    )


def assign_verdicts(
    routes: List[DerivationRoute],
    criteria: List[NativityCriterion],
    doctrine: DoctrineCompatibilityCheck,
) -> tuple[str, str]:
    """Assign primary and secondary verdicts from the closed label set.

    Deterministic rules (strictest compatible verdict):
      1. If all nativity criteria pass AND derivation established:
             native_higher_gradient_stabilizer_conditionally_supported
      2. If no route open and criteria fail:
             no_native_skyrme_support_found  (with 'requires_external_extension' secondary)
      3. If any route conditionally open (Route 3) but criteria fail:
             no_native_skyrme_support_found  (primary)
             effective_skyrme_analog_possible (secondary)
      4. If derivation established but parameter not fixed:
             native_higher_gradient_stabilizer_conditionally_supported

    Default: no_native_skyrme_support_found.
    """
    all_criteria_pass = all(c.passes for c in criteria)
    any_established = any(r.is_established for r in routes)
    any_conditionally_open = any(r.status == "conditionally_open" for r in routes)
    any_open = any(r.is_open for r in routes)

    if all_criteria_pass and any_established:
        primary = "native_higher_gradient_stabilizer_conditionally_supported"
        secondary = "effective_skyrme_analog_possible"
    elif any_conditionally_open or any_open:
        primary = "no_native_skyrme_support_found"
        secondary = "effective_skyrme_analog_possible"
    else:
        primary = "no_native_skyrme_support_found"
        secondary = "requires_external_extension"

    assert primary in ALLOWED_NATIVITY_VERDICTS, (
        f"Primary verdict '{primary}' not in allowed set"
    )
    assert secondary in ALLOWED_NATIVITY_VERDICTS, (
        f"Secondary verdict '{secondary}' not in allowed set"
    )

    return primary, secondary


def _build_nonclaims() -> List[str]:
    return [
        "NOT ruling out that GRUT can eventually derive L_4 natively — Route 3 "
        "(O(3) derivative expansion) is a coherent path: once O(3) is established "
        "from GRUT canon, L_4 is the unique natural next-order term.",

        "NOT claiming the Mexican hat potential V = lambda|Phi|^4 in Phase D1+ "
        "is a Skyrme-type stabilizer.  Field-space quartic (potential) and gradient "
        "quartic (Skyrme) have opposite Derrick scaling and are structurally distinct.",

        "NOT claiming the Skyrme coupling e cannot eventually be expressed in terms "
        "of GRUT parameters — this is an open question, not a closed negative.",

        "NOT claiming L_4 is incompatible with prior GRUT doctrine.  It is compatible.  "
        "The verdict is about derivability and nativity, not compatibility.",

        "NOT claiming the CTP route (Route 2) cannot generate L_4 — in scalar EFT, "
        "CTP integration can produce quartic kinetic terms.  Whether GRUT's specific "
        "g_- sector does so is an open computation, not a closed question.",

        "NOT claiming that adding L_4 now would be internally contradictory.  It would "
        "be 'compatible_but_ad_hoc' in current state, not 'incompatible_with_doctrine'.",

        "NOT claiming that a Skyrme-stabilized hedgehog cannot exist in GRUT — it can, "
        "once the prerequisite chain (O(3) nativity, coupling matching) is completed.",
    ]


def _build_forbidden_inferences() -> List[str]:
    return [
        "mexican_hat_potential_implies_skyrme_stabilization",
        "lambda_phi4_is_l4_gradient_quartic",
        "field_space_quartic_stabilizes_derrick",
        "barrier_underdetermination_derives_l4",
        "o3_topological_charge_implies_skyrme_term_present",
        "l4_compatible_therefore_l4_native",
        "adding_l4_is_patchwork_therefore_impossible",
        "no_native_support_means_l4_is_excluded_forever",
    ]


def run_skyrme_term_nativity_audit() -> SkyrmeTermNativityResult:
    """Run the Skyrme term nativity audit.

    Returns a deterministic SkyrmeTermNativityResult with all five derivation
    routes assessed, three nativity criteria evaluated, doctrine compatibility
    checked, patchwork classification assigned, and primary/secondary verdicts
    from the closed label set.
    """
    routes = [
        build_route_1_constitutive_gradient_expansion(),
        build_route_2_ctp_effective_action(),
        build_route_3_o3_derivative_expansion(),
        build_route_4_mexican_hat_potential(),
        build_route_5_barrier_underdetermination(),
    ]

    derrick_comparison = build_derrick_comparison()
    criteria = build_nativity_criteria(routes)
    doctrine = build_doctrine_compatibility()
    patchwork = build_patchwork_assessment(routes, criteria)

    primary, secondary = assign_verdicts(routes, criteria, doctrine)

    # Top-level summary booleans
    native_skyrme_support_found = any(r.is_established for r in routes)
    any_route_established = any(r.is_established for r in routes)
    any_route_conditionally_open = any(r.status == "conditionally_open" for r in routes)
    any_route_open_but_unbuilt = any(r.status == "open_but_unbuilt" for r in routes)
    all_nativity_criteria_pass = all(c.passes for c in criteria)

    route3 = next(r for r in routes if r.name == "o3_derivative_expansion")

    diagnostics: Dict[str, Any] = {
        "M_EXT": M_EXT,
        "R_EQ": R_EQ,
        "TAU_SQ": TAU_SQ,
        "ALPHA_VAC": ALPHA_VAC,
        "BETA_Q_CANON": BETA_Q_CANON,
        "OMEGA_0_SQ": OMEGA_0_SQ,
        "OMEGA_0": OMEGA_0,
        "SPATIAL_DIMENSION": SPATIAL_DIMENSION,
        "DERRICK_KINETIC_EXPONENT": DERRICK_KINETIC_EXPONENT,
        "DERRICK_POTENTIAL_EXPONENT": DERRICK_POTENTIAL_EXPONENT,
        "DERRICK_SKYRME_EXPONENT": DERRICK_SKYRME_EXPONENT,
        "O3_KINETIC_DERIVATIVE_ORDER": O3_KINETIC_DERIVATIVE_ORDER,
        "O3_SKYRME_DERIVATIVE_ORDER": O3_SKYRME_DERIVATIVE_ORDER,
        "SKYRME_COUPLING_E": SKYRME_COUPLING_E,
        "SKYRME_COUPLING_FIXED_BY_GRUT": SKYRME_COUPLING_FIXED_BY_GRUT,
        "native_skyrme_support_found": native_skyrme_support_found,
        "any_route_established": any_route_established,
        "any_route_conditionally_open": any_route_conditionally_open,
        "any_route_open_but_unbuilt": any_route_open_but_unbuilt,
        "all_nativity_criteria_pass": all_nativity_criteria_pass,
        "mexican_hat_is_not_skyrme_analog": True,
        "barrier_underdetermination_permits_l4": True,
        "doctrine_compatible": doctrine.compatible_with_prior_doctrine,
        "theory_class_preserved": not doctrine.changes_theory_class,
        "introduces_new_free_parameter": doctrine.introduces_new_free_parameter,
        "patchwork_verdict": patchwork.patchwork_verdict,
        "strongest_route_name": route3.name,
        "strongest_route_status": route3.status,
        "num_routes": len(routes),
        "num_nativity_criteria": len(criteria),
        "primary_verdict": primary,
        "secondary_verdict": secondary,
    }

    return SkyrmeTermNativityResult(
        routes=routes,
        derrick_comparison=derrick_comparison,
        nativity_criteria=criteria,
        doctrine_check=doctrine,
        patchwork=patchwork,
        native_skyrme_support_found=native_skyrme_support_found,
        any_route_established=any_route_established,
        any_route_conditionally_open=any_route_conditionally_open,
        any_route_open_but_unbuilt=any_route_open_but_unbuilt,
        mexican_hat_is_not_skyrme_analog=True,
        skyrme_coupling_fixed_by_grut=SKYRME_COUPLING_FIXED_BY_GRUT,
        all_nativity_criteria_pass=all_nativity_criteria_pass,
        doctrine_compatible=doctrine.compatible_with_prior_doctrine,
        strongest_route_name=route3.name,
        strongest_route_status=route3.status,
        primary_verdict=primary,
        secondary_verdict=secondary,
        nonclaims=_build_nonclaims(),
        forbidden_inferences=_build_forbidden_inferences(),
        diagnostics=diagnostics,
    )
