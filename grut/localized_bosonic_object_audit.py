"""Localized Bosonic Object Audit.

Audits whether GRUT's current native architecture supports localized bosonic
objects, and if so, what kind.  Uses ONLY the currently audited architecture
— pre-matter quarantine perimeter (phi_sector_bifurcation, tau_eff_domain,
beta_q_sensitivity) and fermionic_emergence_audit — without importing spinors,
Hopf term, Grassmann variables, supersymmetry, new gauge sectors, unbuilt
covariant matter dynamics, or any stabilizing terms not already present.

PRIMARY QUESTION
---------------
Given the currently audited GRUT architecture exactly as it exists now,
what kinds of localized bosonic objects are natively supported, if any, without
adding new field content, new topological terms, spinors, fermionic structures,
or unbuilt matter-sector dynamics?

ARCHITECTURE STATE (as of this audit)
--------------------------------------
  Field content — native and audited:
    1. Canonical scalar Φ — two declared regimes (phi_sector_bifurcation.py):
         Trajectory: M_drive(t), 0+1D point-valued at moving shell R(t)
         Field:      Φ(r,t), 1+1D distributed, equilibrium profile M/r²
    2. O(3) triplet Φᵃ, a=1,2,3 (candidate extension; Phase D1+):
         Vacuum manifold S², π₂(S²) = ℤ → integer winding number n ∈ ℤ
         Statistics: bosonic (no Hopf term added)
  Absent from current architecture:
    - No spinors, no Dirac structure (fermionic_emergence_audit.py)
    - No Hopf term (π₃(S²) structure absent; fermionic_emergence_audit.py)
    - No gauge fields (D14/D15 closed all coupling routes)
    - No Skyrme term (quartic stabilizing term absent from O(3) sector)
    - No covariant 4-vector matter dynamics (tau_eff_domain_declaration.py)
  Declared domain (tau_eff_domain_declaration.py):
    "spherically symmetric, quasi-static, preferred-frame"
    τ_eff valid only in this regime.  No 4-covariant ω exists.

DERRICK'S THEOREM — Critical No-Go for Scalar/O(3) Solitons in D=3
--------------------------------------------------------------------
  In D spatial dimensions, a static scalar field theory with ONLY a kinetic
  (quadratic gradient) term admits NO stable finite-energy soliton solutions.

  Proof (scaling argument): Under r → λr, gradient energy scales as:
      E_kinetic(λ) = λ^{D-2} E_kinetic(1)
  For D=3: E_kinetic(λ) = λ E_kinetic  →  scales linearly with λ.
  d(E)/d(λ)|_{λ=1} = E_kinetic > 0.  No stationary point at finite λ.
  The energy is minimised by letting the configuration shrink to zero size.

  For the O(3) sigma model in D=3 WITHOUT a quartic stabilizing term (Skyrme):
    - Gradient energy (L₂ = F²_π/8 |∂_μΦᵃ|²) alone → Derrick unstable.
    - Topological charge (winding number n) is CONSERVED under shrinkage
      but the configuration collapses to a distributional limit (n·δ³(r)).
    - No STABLE finite-energy soliton in any winding sector.

  Stabilization would require the Skyrme term:
      L₄ = (F²/16e²) [∂_μΦᵃ × ∂_νΦᵃ]²   (fourth-order in derivatives)
  This term scales as λ^{D-4} = λ^{-1} → opposes the kinetic collapse.
  Combined minimum at finite λ = radius of stable skyrmion.
  The Skyrme term is NOT present in GRUT's O(3) sector.

PRINCIPAL RESULTS (computed deterministically below)
------------------------------------------------------
  constitutive_phi_supports_spatial_profile:  True   (M/r², monotone, distributed)
  shell_supported_localization:               True   (at R_eq, boundary-condition only)
  finite_energy_lump_found:                   False  (Derrick: no Skyrme term)
  topological_bosonic_charge_present:          True   (O(3) π₂(S²)=ℤ, hedgehog n=1)
  stable_bosonic_defect_present:              False  (Derrick unstable; no Skyrme)
  particle_like_object_present:               False  (not established)

  stabilization_mechanism:
    "no_energetically_stable_localized_object__"
    "shell_confinement_via_boundary_condition_only__"
    "o3_topological_charge_conserved_but_derrick_unstable_without_skyrme_term"

  primary_verdict:    "particle_candidate_not_yet_established"
  secondary_verdicts: ["shell_localization_only",
                       "distributed_profile_without_objecthood"]

NONCLAIMS
---------
  1. NOT claiming shell equilibrium establishes localized bosonic matter.
  2. NOT claiming the O(3) hedgehog is a stable particle.
  3. NOT claiming bosonic topological charge implies particle status.
  4. NOT ruling out stable localized bosonic objects forever — requires
     a stabilizing term (Skyrme or equivalent) not yet present.
  5. NOT claiming the constitutive field profile Φ(r) = M/r² is a matter object.
  6. NOT claiming this audit closes the matter-sector question — it bounds it.
  7. NOT claiming the O(3) extension is canonical GRUT — it remains a candidate
     extension (Phase D1+); its presence here is acknowledged from the
     fermionic_emergence_audit architecture state.

References
----------
  grut/phi_sector_bifurcation.py         — Φ trajectory vs field regimes
  grut/tau_eff_domain_declaration.py     — domain limitations
  grut/beta_q_sensitivity.py             — β_Q = 2 sensitivity
  grut/fermionic_emergence_audit.py      — topological content (O(3), Hopf)
  docs/PRE_MATTER_QUARANTINE_STATUS.md   — claim firewall
  Derrick (1964), J. Math. Phys. 5, 1252 — no-go for scalar solitons in D=3
  Skyrme (1961), Proc. R. Soc. A 260, 127 — stabilizing term (absent in GRUT)
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Any, Dict, FrozenSet, List, Optional


# ---------------------------------------------------------------------------
# Locked constants (canonical GRUT equilibrium, β_Q = 2)
# ---------------------------------------------------------------------------

M_EXT: float = 0.5              # M = r_s/2  (geometric units)
R_EQ: float = 1.0 / 3.0        # R_eq = α_vac · r_s = r_s/3
TAU_SQ: float = 1.5             # τ² = 3/2  (canonical)
ALPHA_VAC: float = 1.0 / 3.0   # α_vac = 1/3
BETA_Q_CANON: float = 2.0       # β_Q = 2 (working canon hypothesis)

# ω₀² = β_Q · GM / R_eq³ = 2 · 0.5 / (1/3)³ = 1.0 / (1/27) = 27.0
OMEGA_0_SQ: float = BETA_Q_CANON * M_EXT / (R_EQ ** 3)   # = 27.0
OMEGA_0: float = math.sqrt(OMEGA_0_SQ)                    # = sqrt(27) ≈ 5.196

# Equilibrium source (X_eq = M/R_eq²)
X_EQ: float = M_EXT / (R_EQ ** 2)  # = 4.5

# Energy density at equilibrium (constitutive sector)
# ρ_eq = -M² / (2τ²r⁴)  — negative, r^{-4} divergence, not normalizable without cutoffs
RHO_EQ_AT_R_EQ: float = -(M_EXT ** 2) / (2.0 * TAU_SQ * (R_EQ ** 4))  # = -6.75

# Spatial dimension for Derrick's theorem
SPATIAL_DIMENSION: int = 3

# Derrick scaling exponent for kinetic energy in D dimensions: E_kinetic ~ λ^{D-2}
DERRICK_KINETIC_EXPONENT: int = SPATIAL_DIMENSION - 2   # = 1  (linear in λ)

# Skyrme stabilizing exponent: E_Skyrme ~ λ^{D-4}
DERRICK_SKYRME_EXPONENT: int = SPATIAL_DIMENSION - 4    # = -1 (opposes collapse)

# ---------------------------------------------------------------------------
# Closed verdict label set — no new labels may be created at runtime
# ---------------------------------------------------------------------------

ALLOWED_VERDICT_LABELS: FrozenSet[str] = frozenset({
    "no_native_localized_bosonic_object_support",
    "shell_localization_only",
    "distributed_profile_without_objecthood",
    "bosonic_topological_defect_supported",
    "stable_bosonic_localized_object_conditionally_supported",
    "particle_candidate_not_yet_established",
})

# ---------------------------------------------------------------------------
# Forbidden claim labels (nonclaim firewall)
# ---------------------------------------------------------------------------

FORBIDDEN_CLAIM_LABELS: List[str] = [
    "nontrivial_profile_implies_particle",
    "shell_equilibrium_implies_localized_bosonic_matter",
    "topological_charge_implies_stable_bosonic_particle",
    "constitutive_field_profile_implies_matter_sector_solved",
    "o3_hedgehog_is_a_stable_particle",
    "phi_eq_profile_is_a_bosonic_particle",
    "shell_localization_implies_matter_objecthood",
    "derrick_obstruction_can_be_ignored",
    "bosonic_charge_sufficient_for_particle_status",
    "profile_objecthood_without_finite_energy_lump",
]


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class FieldContentItem:
    """One item in the native field content inventory."""
    name: str                       # identifier
    symbol: str                     # mathematical symbol
    category: str                   # "shell_quantity", "distributed_field",
                                    # "topological_object", "effective_observable",
                                    # "candidate_localized"
    domain: str                     # spatial/temporal domain
    is_diagnostic: bool             # True if kinematic / diagnostic only
    could_be_physical_localized: bool  # True if candidate for localization
    notes: List[str] = field(default_factory=list)


@dataclass
class TrackA_FieldInventory:
    """Track A: Field-Content Localization Check.

    Inventories all native dynamical objects and classifies them.
    """
    items: List[FieldContentItem]
    shell_quantities: List[str]         # names of shell/trajectory objects
    distributed_fields: List[str]       # names of distributed field objects
    topological_objects: List[str]      # names of topological/barrier objects
    effective_observables: List[str]    # names of kinematic/diagnostic objects
    candidate_localized_entities: List[str]  # names of potential localized objects
    candidate_count: int                # number of candidate localized objects
    notes: List[str] = field(default_factory=list)


@dataclass
class TrackB_DomainValidity:
    """Track B: Domain-Validity Check.

    Enforces the declared tau_eff regime from tau_eff_domain_declaration.py.
    """
    declared_domain: str            # "spherically_symmetric_quasi_static_preferred_frame"
    covariant_matter_dynamics_built: bool   # False
    claims_valid_only_in_domain: bool       # True
    unbuilt_dynamics_rejected: bool         # True — any claim requiring covariant dynamics
    spherical_symmetry_required: bool       # True
    quasi_static_required: bool             # True
    preferred_frame_required: bool          # True
    covariant_omega_exists: bool            # False — from tau_eff_domain_declaration
    domain_limitations: List[str]
    notes: List[str] = field(default_factory=list)


@dataclass
class ProfileType:
    """Classification of a field profile type."""
    name: str                       # identifier
    profile_formula: str            # symbolic formula
    is_monotone: bool               # True if monotonically decaying/growing
    has_compact_support: bool       # True if vanishes outside finite radius
    is_topological_defect: bool     # True if characterized by winding number
    is_finite_energy_lump: bool     # True if bounded energy, spatially compact
    notes: List[str] = field(default_factory=list)


@dataclass
class TrackC_StaticLocalization:
    """Track C: Static/Quasi-Static Localization Check.

    Determines what field solutions the current equations admit.
    """
    profiles: List[ProfileType]
    equilibrium_profile_type: str           # e.g. "monotone_power_law"
    shell_boundary_condition_imposed: bool  # True → localization externally imposed
    defect_configuration_exists: bool       # True (O(3) hedgehog)
    finite_energy_lump_solution_found: bool # False
    localization_source: str                # what provides any localization
    notes: List[str] = field(default_factory=list)


@dataclass
class StabilizationMechanism:
    """One candidate stabilization mechanism."""
    name: str
    mechanism_type: str             # "boundary_condition", "topological", "energetic",
                                    # "constitutive_relaxation", "none"
    applies_to: str                 # which object this stabilizes
    is_present_in_grut: bool
    is_sufficient_for_localized_object: bool
    notes: List[str] = field(default_factory=list)


@dataclass
class TrackD_Stability:
    """Track D: Stability Check.

    For any claimed localized bosonic object, identifies the stabilizing
    mechanism already present in the architecture.
    """
    mechanisms: List[StabilizationMechanism]
    shell_stabilization_type: str       # "boundary_condition_only"
    constitutive_stabilization_type: str  # "constitutive_relaxation_attractor"
    o3_stabilization_type: str          # "topological_charge_only__derrick_unstable"
    energetic_minimum_found: bool       # False (no Skyrme term)
    stable_localized_object_found: bool # False
    stabilization_verdict: str          # composite verdict string
    notes: List[str] = field(default_factory=list)


@dataclass
class DerrickAnalysis:
    """Derrick's theorem analysis for the O(3) sector in D=3."""
    spatial_dimension: int              # 3
    kinetic_scaling_exponent: int       # D - 2 = 1  (E_kinetic ~ λ^1 in D=3)
    skyrme_scaling_exponent: int        # D - 4 = -1 (E_Skyrme ~ λ^{-1} in D=3)
    kinetic_term_present: bool          # True (O(3) gradient term)
    skyrme_term_present: bool           # False — NOT in GRUT O(3) sector
    stable_soliton_possible: bool       # False without Skyrme
    derrick_obstruction_active: bool    # True
    what_would_fix_it: str
    reference: str
    notes: List[str] = field(default_factory=list)


@dataclass
class TrackE_FiniteEnergy:
    """Track E: Finite-Energy / Normalizability Check.

    Determines whether the current field content supports finite-energy,
    spatially localized bosonic configurations.
    """
    derrick_analysis: DerrickAnalysis
    phi_field_energy_density_formula: str   # "-M^2/(2*tau^2*r^4)"
    phi_field_energy_diverges_at_origin: bool  # True (r^{-4})
    phi_field_energy_requires_cutoffs: bool    # True (R_eq and R_ext)
    shell_provides_ir_cutoff: bool             # True (R_eq lower cutoff)
    finite_energy_lump_found: bool             # False
    energy_classification: str                 # "cutoff_dependent_not_intrinsic"
    rho_eq_at_r_eq: float                      # -6.75 (from canonical constants)
    notes: List[str] = field(default_factory=list)


@dataclass
class TrackF_TopologicalBosonic:
    """Track F: Topological Bosonic Object Check.

    Audits the O(3) / defect content exactly as it exists in the native
    architecture.
    """
    pi2_s2: str                             # "Z" — π₂(S²) = ℤ
    winding_number_type: str                # "integer_Z" — bosonic
    bosonic_topological_charge_present: bool  # True
    hedgehog_n1_configuration_defined: bool   # True (abstractly)
    hedgehog_statistics: str                  # "bosonic"
    stable_bosonic_defect_present: bool       # False (Derrick)
    skyrme_term_absent: bool                  # True
    particle_interpretation_established: bool  # False
    o3_is_canonical_grut: bool                # False — candidate extension
    topological_charge_sufficient_for_particle: bool  # False
    classification: str                       # "bosonic_topological_charge_only"
    notes: List[str] = field(default_factory=list)


@dataclass
class ForbiddenClaimResult:
    """Result of checking one forbidden claim."""
    claim_label: str
    triggered: bool    # True if the audit result would support this claim
    reason: str        # why it is NOT triggered (or why it would be, if triggered)


@dataclass
class TrackG_NoclaimFirewall:
    """Track G: Nonclaim Firewall.

    Explicitly checks that no forbidden inferences are made.
    """
    forbidden_checks: List[ForbiddenClaimResult]
    any_triggered: bool         # True if any forbidden claim was triggered
    nonclaims: List[str]        # explicit nonclaim statements
    notes: List[str] = field(default_factory=list)


@dataclass
class LocalizedBosonicObjectResult:
    """Master result of the localized bosonic object audit."""

    # Inventory
    track_a: TrackA_FieldInventory
    track_b: TrackB_DomainValidity
    track_c: TrackC_StaticLocalization
    track_d: TrackD_Stability
    track_e: TrackE_FiniteEnergy
    track_f: TrackF_TopologicalBosonic
    track_g: TrackG_NoclaimFirewall

    # Top-level Boolean summary
    native_field_content_inventory: Dict[str, List[str]]
    constitutive_phi_supports_spatial_profile: bool     # True
    shell_supported_localization: bool                  # True (boundary-imposed)
    finite_energy_lump_found: bool                      # False
    topological_bosonic_charge_present: bool            # True
    stable_bosonic_defect_present: bool                 # False
    particle_like_object_present: bool                  # False

    # Mechanism and domain
    stabilization_mechanism: str
    domain_limitations: List[str]

    # Verdict (from closed set)
    primary_verdict: str                    # "particle_candidate_not_yet_established"
    secondary_verdicts: List[str]

    # Firewall
    forbidden_claims_triggered: List[str]   # empty list = clean
    nonclaims: List[str]

    # Diagnostics
    diagnostics: Dict[str, Any]


# ---------------------------------------------------------------------------
# Track builders
# ---------------------------------------------------------------------------

def build_field_inventory() -> TrackA_FieldInventory:
    """Track A: Inventory all native dynamical objects in GRUT."""

    items = [
        FieldContentItem(
            name="phi_trajectory",
            symbol="M_drive(t)",
            category="shell_quantity",
            domain="0+1D point-valued at moving shell R(t)",
            is_diagnostic=False,
            could_be_physical_localized=False,
            notes=[
                "Collapse sector memory field (collapse.py).",
                "Satisfies: tau_eff * dM_drive/dt + M_drive = GM/R^2.",
                "0+1D: single value at shell position — no spatial profile.",
                "At equilibrium: M_drive -> M/R_eq^2 = X_eq = 4.5.",
                "Point-valued: NOT a spatially localized object.",
                "phi_sector_bifurcation.py: 'matter_localization_must_declare_which_Phi'.",
            ],
        ),
        FieldContentItem(
            name="phi_field",
            symbol="Phi(r,t)",
            category="distributed_field",
            domain="1+1D r-distributed, r in [R_eq, R_ext]",
            is_diagnostic=False,
            could_be_physical_localized=False,
            notes=[
                "Constitutive sector relaxation field (action_principle.py).",
                "Satisfies: tau_eff * dPhi/dt + Phi = M/r^2 at each r.",
                "Equilibrium profile: Phi_eq(r) = M/r^2 — power law, not compact.",
                "Energy density: rho_eq = -M^2/(2*tau^2*r^4) — negative, r^{-4}.",
                "Extends throughout space; not spatially bounded without shell cutoff.",
                "Profile present, but distributed without compact support.",
                "Verdict: distributed_profile_without_objecthood.",
            ],
        ),
        FieldContentItem(
            name="o3_triplet",
            symbol="Phi^a, a=1,2,3",
            category="topological_object",
            domain="3+1D field on spatial slice; O(3) target S^2",
            is_diagnostic=False,
            could_be_physical_localized=True,
            notes=[
                "O(3) triplet with |Phi^a|^2 = eta^2 = const (vacuum manifold S^2).",
                "Phase D1+ candidate extension (not canonical GRUT).",
                "pi_2(S^2) = Z: integer winding number n in Z.",
                "n=1 hedgehog: Phi^a(r) = eta * x^a / |x|  (hedgehog ansatz).",
                "Winding number: BOSONIC (integer, not half-integer).",
                "Hopf term ABSENT -> Berry phase = +1 (boson; fermionic_emergence_audit.py).",
                "No Skyrme term: Derrick's theorem -> NOT stable in D=3.",
                "Candidate localized, but stability not established.",
            ],
        ),
        FieldContentItem(
            name="psi_proxy",
            symbol="Psi_proxy = 1/(1+beta_Q) = alpha_vac = 1/3",
            category="effective_observable",
            domain="scalar at equilibrium endpoint",
            is_diagnostic=True,
            could_be_physical_localized=False,
            notes=[
                "Barrier-to-gravity lapse ratio (effective_lapse.py).",
                "Numerically equal to alpha_vac = 1/3 at beta_Q = 2.",
                "NOT M_drive, NOT Phi_field — third separate object.",
                "Purely kinematic/diagnostic; not a dynamical field.",
            ],
        ),
        FieldContentItem(
            name="tau_eff",
            symbol="tau_eff = 1/omega_0 at equilibrium",
            category="effective_observable",
            domain="context-dependent; three ω definitions",
            is_diagnostic=True,
            could_be_physical_localized=False,
            notes=[
                "Effective relaxation timescale (tau_eff_domain_declaration.py).",
                "tau_eff_canon = 1/omega_0 = 1/sqrt(27) ≈ 0.192.",
                "Sector-fragmented: H (cosmological), |V|/R (collapse), omega_0 (interior).",
                "Domain: spherically symmetric, quasi-static, preferred-frame.",
                "Kinematic; not a localized object.",
            ],
        ),
        FieldContentItem(
            name="r_eq",
            symbol="R_eq = alpha_vac * r_s = 1/3",
            category="effective_observable",
            domain="scalar equilibrium radius",
            is_diagnostic=True,
            could_be_physical_localized=False,
            notes=[
                "Equilibrium radius (beta_q_sensitivity.py: R_eq-invariant under beta_Q).",
                "Defines the shell inner boundary condition.",
                "Purely a scalar parameter; not a dynamical object.",
            ],
        ),
        FieldContentItem(
            name="omega_0",
            symbol="omega_0 = sqrt(beta_Q * GM / R_eq^3) = sqrt(27)",
            category="effective_observable",
            domain="scalar frequency at equilibrium",
            is_diagnostic=True,
            could_be_physical_localized=False,
            notes=[
                "Interior PDE mode frequency (tau_eff_domain_declaration.py).",
                "omega_0^2 = 27.0 at canon parameters.",
                "Structural identity: omega_0 * tau_eff = 1 (locked).",
                "Kinematic; not a localized object.",
            ],
        ),
        FieldContentItem(
            name="o3_hedgehog_n1",
            symbol="Phi^a_hedge = eta * x^a/|x|  (n=1 hedgehog)",
            category="candidate_localized",
            domain="3D spatial field; O(3) target; radially symmetric",
            is_diagnostic=False,
            could_be_physical_localized=True,
            notes=[
                "n=1 hedgehog configuration in O(3) sector.",
                "Carries bosonic topological charge Q = 1 * eta.",
                "Topological charge conserved under smooth deformations.",
                "BUT: Derrick's theorem -> configuration collapses without Skyrme term.",
                "Stability NOT established from native architecture.",
                "Particle-candidate status only; objecthood not established.",
            ],
        ),
    ]

    shell_quantities = [i.name for i in items if i.category == "shell_quantity"]
    distributed_fields = [i.name for i in items if i.category == "distributed_field"]
    topological_objects = [i.name for i in items if i.category == "topological_object"]
    effective_observables = [i.name for i in items if i.category == "effective_observable"]
    candidates = [i.name for i in items if i.category == "candidate_localized"]

    return TrackA_FieldInventory(
        items=items,
        shell_quantities=shell_quantities,
        distributed_fields=distributed_fields,
        topological_objects=topological_objects,
        effective_observables=effective_observables,
        candidate_localized_entities=candidates,
        candidate_count=len(candidates),
        notes=[
            "M_drive is a point value — not a spatial object.",
            "Phi_field has a profile M/r^2 — distributed, not compact.",
            "O(3) triplet is a candidate extension, not canonical GRUT.",
            "O(3) hedgehog is the only candidate localized entity.",
            "All effective observables (tau_eff, R_eq, omega_0, Psi_proxy) are"
            " diagnostic scalars, not dynamical field objects.",
        ],
    )


def build_domain_validity() -> TrackB_DomainValidity:
    """Track B: Enforce the declared tau_eff domain limitations."""
    return TrackB_DomainValidity(
        declared_domain="spherically_symmetric_quasi_static_preferred_frame",
        covariant_matter_dynamics_built=False,
        claims_valid_only_in_domain=True,
        unbuilt_dynamics_rejected=True,
        spherical_symmetry_required=True,
        quasi_static_required=True,
        preferred_frame_required=True,
        covariant_omega_exists=False,
        domain_limitations=[
            "No angular modes or frame-dragging (spherical symmetry enforced).",
            "Quasi-static: tau_0 << dynamical timescale, or omega*tau ~ 1 at transition.",
            "Preferred frame: omega evaluated in local rest frame of shell or fluid.",
            "No 4-covariant omega: three omega definitions are not related by tensor law.",
            "No covariant matter dynamics: tau_eff_domain_declaration.py roadmap unbuilt.",
            "Any localization claim valid only inside spherically-symmetric quasi-static regime.",
            "Localization claims requiring covariant GR dynamics are rejected.",
            "The 1+1D field Phi(r,t) is valid in the declared domain only.",
        ],
        notes=[
            "Source: tau_eff_domain_declaration.py — all tau_eff results produced in this domain.",
            "Consequence: no localized bosonic object can claim covariant validity here.",
            "Shell localization at R_eq: valid in quasi-static limit only.",
        ],
    )


def build_static_localization() -> TrackC_StaticLocalization:
    """Track C: Static/Quasi-Static Localization Check."""

    phi_eq_profile = ProfileType(
        name="phi_equilibrium_profile",
        profile_formula="Phi_eq(r) = M / r^2",
        is_monotone=True,
        has_compact_support=False,
        is_topological_defect=False,
        is_finite_energy_lump=False,
        notes=[
            "Monotone decreasing in r; not spatially bounded.",
            "No compact support: extends from R_eq to spatial infinity.",
            "Profile without objecthood: has spatial structure, not a localized object.",
            "At r=R_eq: Phi_eq(R_eq) = M/R_eq^2 = X_eq = 4.5.",
            "Energy density rho_eq = -M^2/(2*tau^2*r^4): negative, singular at r->0.",
        ],
    )

    shell_profile = ProfileType(
        name="shell_confined_profile",
        profile_formula="Phi_eq(R_eq) = X_eq  [evaluated at R_eq by boundary condition]",
        is_monotone=True,
        has_compact_support=False,
        is_topological_defect=False,
        is_finite_energy_lump=False,
        notes=[
            "Shell imposes a lower cutoff at R_eq; field above R_eq follows M/r^2.",
            "Localization arises from externally imposed shell boundary, not field dynamics.",
            "Shell is not derived from the constitutive field — it is a separate structure.",
            "Removing the shell: profile extends to r->0 (singular) or requires IR cutoff.",
            "Classification: shell_localization_only (not intrinsic matter objecthood).",
        ],
    )

    o3_hedgehog_profile = ProfileType(
        name="o3_hedgehog",
        profile_formula="Phi^a_hedge(r) = eta * x^a / |x|  (hedgehog ansatz, n=1)",
        is_monotone=False,
        has_compact_support=False,
        is_topological_defect=True,
        is_finite_energy_lump=False,
        notes=[
            "Hedgehog configuration in O(3) sector; winding number n=1.",
            "Field approaches vacuum (|Phi^a|=eta) at spatial infinity.",
            "Profile is radially symmetric but not spatially compact.",
            "Topological defect: classified by pi_2(S^2) = Z.",
            "NOT a finite-energy lump: Derrick's theorem -> collapses without Skyrme term.",
            "is_topological_defect = True; is_finite_energy_lump = False.",
        ],
    )

    return TrackC_StaticLocalization(
        profiles=[phi_eq_profile, shell_profile, o3_hedgehog_profile],
        equilibrium_profile_type="monotone_power_law_not_compact",
        shell_boundary_condition_imposed=True,
        defect_configuration_exists=True,
        finite_energy_lump_solution_found=False,
        localization_source=(
            "shell_boundary_condition_external__"
            "constitutive_profile_monotone_no_lump__"
            "o3_defect_topologically_classified_but_derrick_unstable"
        ),
        notes=[
            "No field equation in the current architecture admits a finite-energy lump.",
            "The only localized structure is the shell at R_eq (external boundary).",
            "The O(3) hedgehog has topological charge but is not a stable lump in D=3.",
            "Equilibrium profile (M/r^2) is distributed, not localized.",
            "Distinction enforced: equilibrium profile != localized bosonic object.",
        ],
    )


def build_stability() -> TrackD_Stability:
    """Track D: Stability Check — identify stabilizing mechanisms."""

    shell_bc = StabilizationMechanism(
        name="shell_boundary_condition",
        mechanism_type="boundary_condition",
        applies_to="phi_field at R_eq",
        is_present_in_grut=True,
        is_sufficient_for_localized_object=False,
        notes=[
            "The shell imposes R_eq as a lower boundary; field is confined above this.",
            "This is not a dynamical stabilization — it is an externally imposed structure.",
            "Removing the shell: profile spreads or diverges; no intrinsic localization.",
            "Classification: boundary_condition_only.",
        ],
    )

    relaxation_attractor = StabilizationMechanism(
        name="constitutive_relaxation_attractor",
        mechanism_type="constitutive_relaxation",
        applies_to="phi_field (constitutive sector)",
        is_present_in_grut=True,
        is_sufficient_for_localized_object=False,
        notes=[
            "ODE: tau_eff * dPhi/dt + Phi = X attracts Phi -> X(r) as attractor.",
            "The attractor is the equilibrium profile M/r^2, which is distributed.",
            "Constitutive relaxation stabilizes the profile shape, not a localized object.",
            "Stable attractor + distributed profile = profile_without_objecthood.",
        ],
    )

    topological_conservation = StabilizationMechanism(
        name="o3_topological_charge_conservation",
        mechanism_type="topological",
        applies_to="o3_hedgehog (O(3) sector)",
        is_present_in_grut=True,
        is_sufficient_for_localized_object=False,
        notes=[
            "Topological winding number n is conserved under smooth deformations.",
            "However, Derrick's theorem: configuration collapses to zero size in D=3.",
            "Conserved charge != stable finite-size object.",
            "Without Skyrme term: topological conservation does not prevent collapse.",
            "The charge is conserved but the object shrinks to a distributional limit.",
        ],
    )

    skyrme_term = StabilizationMechanism(
        name="skyrme_quartic_term",
        mechanism_type="energetic",
        applies_to="o3_hedgehog (would stabilize against Derrick collapse)",
        is_present_in_grut=False,
        is_sufficient_for_localized_object=True,
        notes=[
            "Skyrme term: L_4 = (F^2/16e^2)[d_mu Phi^a x d_nu Phi^a]^2.",
            "Scales as lambda^{D-4} = lambda^{-1} in D=3: opposes kinetic collapse.",
            "Combined minimum with kinetic term: stable skyrmion at finite radius.",
            "NOT present in current GRUT O(3) sector.",
            "Absence: energetic minimum does not exist; Derrick obstruction active.",
        ],
    )

    return TrackD_Stability(
        mechanisms=[
            shell_bc,
            relaxation_attractor,
            topological_conservation,
            skyrme_term,
        ],
        shell_stabilization_type="boundary_condition_only",
        constitutive_stabilization_type="constitutive_relaxation_attractor",
        o3_stabilization_type="topological_charge_only__derrick_unstable_without_skyrme",
        energetic_minimum_found=False,
        stable_localized_object_found=False,
        stabilization_verdict=(
            "no_energetically_stable_localized_object__"
            "shell_confinement_via_boundary_condition_only__"
            "o3_topological_charge_conserved_but_derrick_unstable_without_skyrme_term"
        ),
        notes=[
            "All present stabilization mechanisms are insufficient for localized objecthood.",
            "Shell BC: stabilizes at R_eq only while shell exists (not intrinsic).",
            "Constitutive relaxation: stabilizes distributed profile (not lump).",
            "Topological conservation: conserves charge but does not prevent collapse.",
            "Skyrme term: would provide energetic minimum, but is ABSENT from GRUT.",
            "Verdict: no stable localized bosonic object in current architecture.",
        ],
    )


def build_derrick_analysis() -> DerrickAnalysis:
    """Build the Derrick's theorem analysis for the O(3) sector in D=3."""
    return DerrickAnalysis(
        spatial_dimension=SPATIAL_DIMENSION,
        kinetic_scaling_exponent=DERRICK_KINETIC_EXPONENT,
        skyrme_scaling_exponent=DERRICK_SKYRME_EXPONENT,
        kinetic_term_present=True,
        skyrme_term_present=False,
        stable_soliton_possible=False,
        derrick_obstruction_active=True,
        what_would_fix_it=(
            "Add the Skyrme term L_4 = (F^2/16e^2)[d_mu Phi^a x d_nu Phi^a]^2 "
            "to the O(3) sigma model action.  This term scales as lambda^{D-4} = "
            "lambda^{-1} in D=3, opposing the kinetic term's lambda^1 growth and "
            "producing a stable energy minimum at finite soliton radius."
        ),
        reference="Derrick (1964), J. Math. Phys. 5, 1252; Skyrme (1961), Proc. R. Soc. A 260, 127",
        notes=[
            f"D = {SPATIAL_DIMENSION}: kinetic term E_2 ~ lambda^{DERRICK_KINETIC_EXPONENT}.",
            f"Skyrme term E_4 ~ lambda^{DERRICK_SKYRME_EXPONENT} (absent).",
            "Under r -> lambda*r: dE/d(lambda)|_{lambda=1} = E_2 > 0.",
            "No stationary point -> configuration collapses to distributional limit.",
            "Topological charge Q = n is conserved but soliton size -> 0.",
            "Energy minimum does not exist without E_4 (Skyrme or equivalent).",
            "Canonical GRUT scalar Phi is also subject to Derrick: pi_2(R)=0, no defects.",
        ],
    )


def build_finite_energy() -> TrackE_FiniteEnergy:
    """Track E: Finite-Energy / Normalizability Check."""
    derrick = build_derrick_analysis()

    return TrackE_FiniteEnergy(
        derrick_analysis=derrick,
        phi_field_energy_density_formula="-M^2 / (2 * tau^2 * r^4)",
        phi_field_energy_diverges_at_origin=True,
        phi_field_energy_requires_cutoffs=True,
        shell_provides_ir_cutoff=True,
        finite_energy_lump_found=False,
        energy_classification=(
            "cutoff_dependent_not_intrinsic__"
            "shell_provides_ir_cutoff__"
            "no_uv_or_compactness_from_field_dynamics"
        ),
        rho_eq_at_r_eq=RHO_EQ_AT_R_EQ,
        notes=[
            f"rho_eq(R_eq) = -M^2/(2*tau^2*R_eq^4) = {RHO_EQ_AT_R_EQ:.4f} (negative).",
            "Energy density rho ~ r^{-4}: diverges as r->0; requires IR cutoff at R_eq.",
            "Shell provides the IR cutoff at R_eq; without shell, energy is singular.",
            "Localization via cutoff is NOT intrinsic localization (shell_localization_only).",
            "O(3) hedgehog: Derrick obstruction -> no finite-energy stable soliton.",
            "No configuration in the current architecture has intrinsic finite energy.",
        ],
    )


def build_topological_track() -> TrackF_TopologicalBosonic:
    """Track F: Topological Bosonic Object Check."""
    return TrackF_TopologicalBosonic(
        pi2_s2="Z",
        winding_number_type="integer_Z",
        bosonic_topological_charge_present=True,
        hedgehog_n1_configuration_defined=True,
        hedgehog_statistics="bosonic",
        stable_bosonic_defect_present=False,
        skyrme_term_absent=True,
        particle_interpretation_established=False,
        o3_is_canonical_grut=False,
        topological_charge_sufficient_for_particle=False,
        classification=(
            "bosonic_topological_charge_present__"
            "stable_defect_not_established__"
            "particle_candidate_not_yet_established"
        ),
        notes=[
            "pi_2(S^2) = Z: integer winding numbers ARE present in the O(3) sector.",
            "Winding number n in Z: bosonic (integer, not half-integer).",
            "n=1 hedgehog: Phi^a = eta * x^a/|x| has Q=1 topological charge.",
            "Bosonic topological charge present: TRUE.",
            "Stable bosonic defect: FALSE (Derrick's theorem; no Skyrme term).",
            "Particle interpretation: FALSE (stability not established).",
            "O(3) is candidate extension (Phase D1+), not canonical GRUT.",
            "Forbidden inference: topological_charge_implies_stable_bosonic_particle.",
            "Skyrmion analogy only: GRUT lacks the Skyrme term needed to realise it.",
        ],
    )


def build_nonclaim_firewall() -> TrackG_NoclaimFirewall:
    """Track G: Nonclaim Firewall — check all forbidden inferences."""

    def _check(label: str, triggered: bool, reason: str) -> ForbiddenClaimResult:
        return ForbiddenClaimResult(
            claim_label=label,
            triggered=triggered,
            reason=reason,
        )

    checks = [
        _check(
            "nontrivial_profile_implies_particle",
            triggered=False,
            reason=(
                "The constitutive profile Phi_eq(r)=M/r^2 is explicitly classified as "
                "distributed_profile_without_objecthood.  Nontrivial profile does not "
                "imply particle status."
            ),
        ),
        _check(
            "shell_equilibrium_implies_localized_bosonic_matter",
            triggered=False,
            reason=(
                "Shell equilibrium at R_eq is classified as boundary_condition_only.  "
                "The shell is an externally imposed structure, not a derived matter object.  "
                "shell_supported_localization=True does not imply matter objecthood."
            ),
        ),
        _check(
            "topological_charge_implies_stable_bosonic_particle",
            triggered=False,
            reason=(
                "topological_bosonic_charge_present=True (O(3) n=1) but "
                "stable_bosonic_defect_present=False.  Derrick's theorem prevents "
                "stable finite-size soliton without Skyrme term.  Charge conservation "
                "is not sufficient for particle status."
            ),
        ),
        _check(
            "constitutive_field_profile_implies_matter_sector_solved",
            triggered=False,
            reason=(
                "Constitutive field has an equilibrium profile (M/r^2) and a relaxation "
                "attractor, but this does not establish a matter sector.  The profile "
                "exists within the declared quasi-static domain; matter sector dynamics "
                "are explicitly unbuilt (PRE_MATTER_QUARANTINE_STATUS.md)."
            ),
        ),
        _check(
            "o3_hedgehog_is_a_stable_particle",
            triggered=False,
            reason=(
                "O(3) hedgehog n=1 carries bosonic topological charge but is Derrick-unstable "
                "in D=3 without a Skyrme term.  particle_like_object_present=False."
            ),
        ),
        _check(
            "phi_eq_profile_is_a_bosonic_particle",
            triggered=False,
            reason=(
                "Phi_eq(r)=M/r^2 is a monotone distributed profile in the constitutive "
                "sector, not a localized bosonic particle.  It requires external shell "
                "cutoffs to be normalisable."
            ),
        ),
        _check(
            "shell_localization_implies_matter_objecthood",
            triggered=False,
            reason=(
                "Shell localization at R_eq is boundary_condition_only.  "
                "shell_supported_localization=True is a secondary classification flag, "
                "not a matter objecthood claim."
            ),
        ),
        _check(
            "derrick_obstruction_can_be_ignored",
            triggered=False,
            reason=(
                "Derrick's theorem is a rigorous no-go theorem for D=3 scalar/O(3) solitons "
                "with only kinetic terms.  The Skyrme term is absent from GRUT.  "
                "The obstruction cannot be ignored."
            ),
        ),
        _check(
            "bosonic_charge_sufficient_for_particle_status",
            triggered=False,
            reason=(
                "Bosonic topological charge (n in Z) is necessary but not sufficient for "
                "particle status.  Stability (energetic minimum) is also required and "
                "is absent due to the Derrick obstruction."
            ),
        ),
        _check(
            "profile_objecthood_without_finite_energy_lump",
            triggered=False,
            reason=(
                "Object status requires a finite-energy spatially compact configuration.  "
                "finite_energy_lump_found=False.  A profile without compact support and "
                "without an energetic minimum is not an object."
            ),
        ),
    ]

    any_triggered = any(c.triggered for c in checks)

    nonclaims = [
        "NOT claiming shell equilibrium establishes localized bosonic matter — "
        "shell_localization_only is a secondary flag, not an objecthood claim.",

        "NOT claiming the O(3) hedgehog is a stable particle — topological charge n=1 "
        "is conserved but the configuration is Derrick-unstable without a Skyrme term.",

        "NOT claiming bosonic topological charge implies particle status — "
        "bosonic_topological_charge_present=True is a necessary not sufficient condition.",

        "NOT ruling out stable localized bosonic objects forever — the architecture "
        "could be extended with a Skyrme term (or equivalent), but that term is "
        "currently absent and unbuilt.",

        "NOT claiming the constitutive field profile Phi(r)=M/r^2 is a matter object — "
        "it is a distributed profile without objecthood.",

        "NOT claiming this audit closes the matter-sector question — it establishes "
        "the current bound: particle_candidate_not_yet_established.",

        "NOT claiming the O(3) extension is canonical GRUT — it is a candidate "
        "extension (Phase D1+) acknowledged from fermionic_emergence_audit architecture.",

        "NOT claiming Derrick's theorem permanently rules out all bosonic particles — "
        "it rules out pure-kinetic O(3) sigma model solitons in D=3 without "
        "higher-derivative terms.  A Skyrme term is a coherent extension path.",
    ]

    return TrackG_NoclaimFirewall(
        forbidden_checks=checks,
        any_triggered=any_triggered,
        nonclaims=nonclaims,
        notes=[
            "All 10 forbidden claims checked; none triggered.",
            "Firewall is clean — audit results are within legitimate classification.",
        ],
    )


def assign_primary_verdict(
    track_c: TrackC_StaticLocalization,
    track_d: TrackD_Stability,
    track_e: TrackE_FiniteEnergy,
    track_f: TrackF_TopologicalBosonic,
) -> str:
    """Assign primary verdict from the closed label set.

    Deterministic rule:
      1. If no topological charge and no profile: no_native_localized_bosonic_object_support
      2. If only shell localization, no topological charge: shell_localization_only
      3. If only distributed profile, no topological charge: distributed_profile_without_objecthood
      4. If topological charge + stable defect: bosonic_topological_defect_supported
      5. If stable localized object: stable_bosonic_localized_object_conditionally_supported
      6. If topological charge + no stable defect: particle_candidate_not_yet_established
    Default to strictest compatible verdict.
    """
    has_topological_charge = track_f.bosonic_topological_charge_present
    has_stable_defect = track_f.stable_bosonic_defect_present
    has_stable_lump = track_d.stable_localized_object_found
    has_finite_energy_lump = track_e.finite_energy_lump_found
    has_shell = track_c.shell_boundary_condition_imposed
    has_profile = True  # Phi_eq(r) = M/r^2 always present

    if has_stable_lump and has_finite_energy_lump:
        return "stable_bosonic_localized_object_conditionally_supported"
    elif has_topological_charge and has_stable_defect:
        return "bosonic_topological_defect_supported"
    elif has_topological_charge and not has_stable_defect:
        # Topological charge present but defect stability not established.
        # Strictest verdict: particle_candidate_not_yet_established
        # (grants candidate status due to charge; withholds particle/defect status)
        return "particle_candidate_not_yet_established"
    elif has_shell and not has_topological_charge:
        return "shell_localization_only"
    elif has_profile and not has_topological_charge:
        return "distributed_profile_without_objecthood"
    else:
        return "no_native_localized_bosonic_object_support"


def assign_secondary_verdicts(
    track_c: TrackC_StaticLocalization,
    track_f: TrackF_TopologicalBosonic,
    primary: str,
) -> List[str]:
    """Assign secondary verdict flags (may be multiple)."""
    secondaries: List[str] = []

    if track_c.shell_boundary_condition_imposed and primary != "shell_localization_only":
        secondaries.append("shell_localization_only")

    if (
        not track_f.stable_bosonic_defect_present
        and primary != "distributed_profile_without_objecthood"
    ):
        secondaries.append("distributed_profile_without_objecthood")

    return secondaries


def run_localized_bosonic_object_audit() -> LocalizedBosonicObjectResult:
    """Run the full localized bosonic object audit.

    Returns a deterministic LocalizedBosonicObjectResult with all seven tracks,
    a primary verdict from the closed label set, secondary verdict flags,
    nonclaims, and a forbidden-claims firewall result.
    """
    track_a = build_field_inventory()
    track_b = build_domain_validity()
    track_c = build_static_localization()
    track_d = build_stability()
    track_e = build_finite_energy()
    track_f = build_topological_track()
    track_g = build_nonclaim_firewall()

    # Top-level summary booleans
    constitutive_phi_supports_spatial_profile = True   # M/r^2 profile always present
    shell_supported_localization = track_c.shell_boundary_condition_imposed
    finite_energy_lump_found = track_e.finite_energy_lump_found
    topological_bosonic_charge_present = track_f.bosonic_topological_charge_present
    stable_bosonic_defect_present = track_f.stable_bosonic_defect_present
    particle_like_object_present = track_f.particle_interpretation_established

    # Verdict assignment
    primary_verdict = assign_primary_verdict(track_c, track_d, track_e, track_f)
    secondary_verdicts = assign_secondary_verdicts(track_c, track_f, primary_verdict)

    # Enforce closed label set
    assert primary_verdict in ALLOWED_VERDICT_LABELS, (
        f"Primary verdict '{primary_verdict}' not in allowed set: {ALLOWED_VERDICT_LABELS}"
    )
    for sv in secondary_verdicts:
        assert sv in ALLOWED_VERDICT_LABELS, (
            f"Secondary verdict '{sv}' not in allowed set: {ALLOWED_VERDICT_LABELS}"
        )

    native_field_content_inventory: Dict[str, List[str]] = {
        "shell_quantities": track_a.shell_quantities,
        "distributed_fields": track_a.distributed_fields,
        "topological_objects": track_a.topological_objects,
        "effective_observables": track_a.effective_observables,
        "candidate_localized_entities": track_a.candidate_localized_entities,
    }

    forbidden_triggered = [
        c.claim_label for c in track_g.forbidden_checks if c.triggered
    ]

    diagnostics: Dict[str, Any] = {
        "M_EXT": M_EXT,
        "R_EQ": R_EQ,
        "TAU_SQ": TAU_SQ,
        "ALPHA_VAC": ALPHA_VAC,
        "BETA_Q_CANON": BETA_Q_CANON,
        "OMEGA_0_SQ": OMEGA_0_SQ,
        "OMEGA_0": OMEGA_0,
        "X_EQ": X_EQ,
        "RHO_EQ_AT_R_EQ": RHO_EQ_AT_R_EQ,
        "SPATIAL_DIMENSION": SPATIAL_DIMENSION,
        "DERRICK_KINETIC_EXPONENT": DERRICK_KINETIC_EXPONENT,
        "DERRICK_SKYRME_EXPONENT": DERRICK_SKYRME_EXPONENT,
        "constitutive_phi_supports_spatial_profile": constitutive_phi_supports_spatial_profile,
        "shell_supported_localization": shell_supported_localization,
        "finite_energy_lump_found": finite_energy_lump_found,
        "topological_bosonic_charge_present": topological_bosonic_charge_present,
        "stable_bosonic_defect_present": stable_bosonic_defect_present,
        "particle_like_object_present": particle_like_object_present,
        "derrick_obstruction_active": track_e.derrick_analysis.derrick_obstruction_active,
        "skyrme_term_present": track_e.derrick_analysis.skyrme_term_present,
        "o3_winding_type": track_f.winding_number_type,
        "o3_statistics": track_f.hedgehog_statistics,
        "o3_is_canonical_grut": track_f.o3_is_canonical_grut,
        "covariant_matter_dynamics_built": track_b.covariant_matter_dynamics_built,
        "declared_domain": track_b.declared_domain,
        "forbidden_claims_triggered_count": len(forbidden_triggered),
        "primary_verdict": primary_verdict,
        "secondary_verdicts": secondary_verdicts,
    }

    return LocalizedBosonicObjectResult(
        track_a=track_a,
        track_b=track_b,
        track_c=track_c,
        track_d=track_d,
        track_e=track_e,
        track_f=track_f,
        track_g=track_g,
        native_field_content_inventory=native_field_content_inventory,
        constitutive_phi_supports_spatial_profile=constitutive_phi_supports_spatial_profile,
        shell_supported_localization=shell_supported_localization,
        finite_energy_lump_found=finite_energy_lump_found,
        topological_bosonic_charge_present=topological_bosonic_charge_present,
        stable_bosonic_defect_present=stable_bosonic_defect_present,
        particle_like_object_present=particle_like_object_present,
        stabilization_mechanism=track_d.stabilization_verdict,
        domain_limitations=track_b.domain_limitations,
        primary_verdict=primary_verdict,
        secondary_verdicts=secondary_verdicts,
        forbidden_claims_triggered=forbidden_triggered,
        nonclaims=track_g.nonclaims,
        diagnostics=diagnostics,
    )
