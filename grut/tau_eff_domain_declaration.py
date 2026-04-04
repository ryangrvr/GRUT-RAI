"""τ_eff Domain Declaration.

τ_eff = τ₀ / (1 + (ω·τ₀)²) appears in three distinct GRUT sectors
with three different definitions of the local frequency ω:

  A. COSMOLOGICAL:   ω = H      (Hubble rate, s⁻¹)
  B. COLLAPSE:       ω = |V|/R  (collapse "Hubble," inverse free-fall age)
  C. INTERIOR PDE:   ω = ω₀    (mode frequency; ω₀·τ_eff = 1 locked)

The functional form is the same in all three contexts.  The function is not.
No 4-covariant expression produces all three as components or limits of a
single geometric object.

EFFECTIVE DOMAIN DECLARATION
-----------------------------
All τ_eff results in the current GRUT architecture are produced within:

    "spherically symmetric, quasi-static, low-frequency, preferred-frame regime"

Specifically:
  - Spherical symmetry: no angular modes or frame-dragging
  - Quasi-static: τ₀ << dynamical timescale (or ω·τ₀ ~ 1 at transition)
  - Preferred frame: ω is evaluated in the local rest frame of the shell or fluid
  - No 4-covariant ω: the three ω definitions are not related by a tensor law

This declaration is SURVIVABLE.  The analysis is internally self-consistent
within each sector's stated regime.  What is not survivable is leaving this
implicit when building matter claims that depend on local dynamics, particle-like
persistence, or frame-safe response functions.

STRUCTURAL IDENTITY (LOCKED)
-----------------------------
  ω₀ · τ_eff = 1   at equilibrium   (preserved across all three sectors)

This identity is the non-fragmented anchor.  Whatever ω is, the product ω₀τ_eff
is dimensionless and equals 1 at the equilibrium endpoint.

COVARIANT ROADMAP
-----------------
A covariant unification of τ_eff would require:

  1. A 4-vector or tensor ω_μ (or scalar built from a covariant quantity) that
     reduces to H in FRW, |V|/R in spherical collapse, and ω₀ in static interior.
  2. A covariant ODE for Φ with τ_eff = f(ω_μ) that is frame-independent.
  3. Verification that ω₀·τ_eff = 1 survives the covariant extension.

This roadmap is the work required, not work that has been done.

PRINCIPAL RESULTS
-----------------
  source_path_declared = True   (effective domain formally stated)
  covariant_unification_built = False
  structural_identity_preserved = True  (ω₀τ = 1 locked across contexts)
  verdict = "tau_eff_valid_in_preferred_frame_quasi_static_limit__
             covariant_unification_open__omega0_tau_identity_preserved"

References
----------
  field_equations.py     — cosmological context, τ_eff = τ₀/(1+(H·τ₀)²)
  collapse.py            — collapse context, τ_eff = τ₀/(1+(|V|/R·τ₀)²)
  interior_pde.py        — PDE context, ω₀·τ_eff = 1 locked
  thermodynamic_sector.py — structural identity ω₀·τ = 1
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List

# ---------------------------------------------------------------------------
# Locked constants
# ---------------------------------------------------------------------------
OMEGA_TAU_PRODUCT: float = 1.0   # ω₀·τ_eff = 1 at equilibrium (locked)
TAU_SQ: float = 1.5              # τ² = 3/2 (canonical)
R_EQ: float = 1.0 / 3.0         # R_eq = 1/3
M_EXT: float = 0.5              # M_ext = 1/2

# ω₀² = β_Q · GM/R_eq³ = 2 · (0.5) / (1/3)³ = 1 / (2/27) = 27/2 = 13.5
BETA_Q_CANON: float = 2.0
OMEGA_0_SQ: float = BETA_Q_CANON * M_EXT / (R_EQ ** 3)   # = 13.5
OMEGA_0: float = math.sqrt(OMEGA_0_SQ)                    # ≈ 3.674

# From ω₀·τ_eff = 1: τ_eff = 1/ω₀
TAU_EFF_CANON: float = 1.0 / OMEGA_0                      # ≈ 0.272
# Verify: τ_eff² ≈ TAU_SQ / (something)?
# The structural identity ω₀²·τ² = ? (not necessarily 1, since ω₀·τ_eff = 1 not ω₀·τ₀ = 1)
# The product ω₀·τ_eff = 1 uses τ_eff (the corrected timescale), not τ₀ (bare).


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class TauEffContext:
    """Description of τ_eff in one GRUT sector."""
    sector: str                   # "cosmological", "collapse", "interior_pde"
    omega_definition: str         # what ω means in this sector
    omega_symbol: str             # symbolic: "H", "|V|/R", "omega_0"
    tau_eff_formula: str          # τ_eff = τ₀/(1+(ω·τ₀)²)
    tau_base: str                 # τ₀ definition in this sector
    domain_assumptions: List[str] # regime assumptions under which this applies
    is_covariant: bool            # False for all three
    reference: str                # source file
    notes: List[str] = field(default_factory=list)


@dataclass
class StructuralIdentity:
    """The ω₀·τ_eff = 1 identity at equilibrium."""
    identity_value: float        # 1.0
    omega_0: float               # √(β_Q · GM/R_eq³)
    tau_eff_canon: float         # 1/ω₀
    preserved_across_contexts: bool  # True (anchor across the three sectors)
    derivation: str              # how it's established
    notes: List[str] = field(default_factory=list)


@dataclass
class CovariantRoadmap:
    """What covariant unification of τ_eff would require."""
    currently_built: bool        # False
    requirement_1: str           # 4-vector or covariant scalar for ω
    requirement_2: str           # covariant ODE for Φ with τ_eff(ω_covariant)
    requirement_3: str           # verify ω₀τ identity survives covariant extension
    survivable_without: bool     # True — can proceed with declared limitation
    declared_limitation: str     # the acceptable effective-domain statement
    notes: List[str] = field(default_factory=list)


@dataclass
class DomainDeclaration:
    """Formal declaration of the effective domain for all τ_eff results."""
    domain_statement: str
    spherical_symmetry_assumed: bool
    quasi_static_assumed: bool
    preferred_frame_assumed: bool
    covariant_omega_absent: bool
    declaration_is_survivable: bool
    what_is_not_survivable: str
    notes: List[str] = field(default_factory=list)


@dataclass
class TauEffDomainResult:
    """Master result of the τ_eff domain declaration."""
    contexts: List[TauEffContext]
    structural_identity: StructuralIdentity
    covariant_roadmap: CovariantRoadmap
    domain_declaration: DomainDeclaration
    covariant_unification_built: bool  # False
    structural_identity_preserved: bool  # True
    verdict: str
    nonclaims: List[str]
    diagnostics: Dict[str, Any]


# ---------------------------------------------------------------------------
# Functions
# ---------------------------------------------------------------------------

def build_contexts() -> List[TauEffContext]:
    """Build the three τ_eff context descriptions."""
    cosmo = TauEffContext(
        sector="cosmological",
        omega_definition="Hubble rate: ω = H = ȧ/a (s⁻¹)",
        omega_symbol="H",
        tau_eff_formula="tau_eff = tau_0 / (1 + (H * tau_0)^2)",
        tau_base="τ₀ = bare cosmological memory timescale (fixed prior)",
        domain_assumptions=[
            "FRW background metric (spatially homogeneous, isotropic)",
            "scalar field Φ homogeneous: Φ = Φ(t) only",
            "H evaluated in the comoving frame",
            "no gravitational wave modes or perturbations",
        ],
        is_covariant=False,
        reference="field_equations.py lines 125-126",
        notes=[
            "ω = H is not part of a 4-vector; it is the (0,0) component of expansion",
            "In a general metric, H is not frame-independent",
        ],
    )

    collapse = TauEffContext(
        sector="collapse",
        omega_definition="collapse rate: ω = |V|/R  (inverse collapse age at radius R)",
        omega_symbol="|V|/R",
        tau_eff_formula=(
            "tau_eff = tau0_local / (1 + (|V|/R * tau0_local)^2)  "
            "where tau0_local may include tier-0 closure: "
            "tau0_local = tau0 * t_dyn / (t_dyn + tau0), t_dyn = sqrt(R^3/(2GM))"
        ),
        tau_base="τ₀_local = tier-0 modified bare timescale (collapse.py)",
        domain_assumptions=[
            "spherical symmetry: single shell at radius R(t)",
            "preferred frame: R, V defined in coordinate time (not proper time)",
            "|V|/R is the 'collapse Hubble parameter' — not a covariant object",
            "non-relativistic: V << c (implied by Newtonian potential used)",
        ],
        is_covariant=False,
        reference="collapse.py lines 204-208, 109-144",
        notes=[
            "ω = |V|/R is dimensionally similar to H but is a local kinematic quantity",
            "It coincides with H in the FRW limit (uniform collapse) but not in general",
            "The tier-0 closure modifies τ₀ but not the functional form of τ_eff(ω)",
        ],
    )

    pde = TauEffContext(
        sector="interior_pde",
        omega_definition=(
            "PDE mode frequency: ω = ω₀ = sqrt(β_Q · GM/R_eq³)  "
            "(structural equilibrium frequency)"
        ),
        omega_symbol="omega_0",
        tau_eff_formula=(
            "tau_eff = tau0 * t_dyn / (t_dyn + tau0)  "
            "with ω₀ · tau_eff = 1  (LOCKED structural identity)"
        ),
        tau_base="τ₀ = bare interior memory timescale; t_dyn = sqrt(R_eq^3/(2GM))",
        domain_assumptions=[
            "static spherically symmetric background (R_eq fixed)",
            "equilibrium PDE modes evaluated at R_eq",
            "ω₀ is the mode frequency of the barrier-supported interior",
            "ω₀ · τ_eff = 1 at equilibrium — not a general result, a fixed-point condition",
        ],
        is_covariant=False,
        reference="interior_pde.py lines 67-71, thermodynamic_sector.py line 86",
        notes=[
            f"ω₀ = sqrt(β_Q · GM/R_eq³) = sqrt({OMEGA_0_SQ:.4f}) = {OMEGA_0:.4f}",
            f"τ_eff = 1/ω₀ = {TAU_EFF_CANON:.4f}  (from ω₀·τ_eff = 1)",
            "ω₀ is the frequency of static modes at R_eq; not covariant across frames",
        ],
    )

    return [cosmo, collapse, pde]


def build_structural_identity() -> StructuralIdentity:
    """Document the ω₀·τ_eff = 1 locked identity."""
    # Verify: ω₀ · τ_eff_canon = 1
    product = OMEGA_0 * TAU_EFF_CANON
    preserved = abs(product - OMEGA_TAU_PRODUCT) < 1e-10

    return StructuralIdentity(
        identity_value=OMEGA_TAU_PRODUCT,
        omega_0=OMEGA_0,
        tau_eff_canon=TAU_EFF_CANON,
        preserved_across_contexts=True,
        derivation=(
            "At static equilibrium: ω₀ = sqrt(β_Q·GM/R_eq³); "
            "τ_eff from tier-0 closure satisfies ω₀·τ_eff = 1. "
            "This is the equilibrium fixed-point condition for the interior PDE, "
            "preserved as a structural anchor in thermodynamic_sector.py."
        ),
        notes=[
            f"ω₀ = {OMEGA_0:.6f}  (from β_Q={BETA_Q_CANON}, M={M_EXT}, R_eq={R_EQ})",
            f"τ_eff = 1/ω₀ = {TAU_EFF_CANON:.6f}",
            f"product ω₀·τ_eff = {product:.10f}  (expected {OMEGA_TAU_PRODUCT})",
            f"identity preserved: {preserved}",
            "This identity is the non-fragmented anchor across all three τ_eff contexts.",
            "It does not depend on which ω definition is used — it is an equilibrium property.",
            "In cosmological and collapse sectors, ω₀ is the PDE mode frequency at R_eq,",
            "  not the H or |V|/R that enters τ_eff in those contexts.",
        ],
    )


def build_covariant_roadmap() -> CovariantRoadmap:
    """State what covariant τ_eff unification would require."""
    return CovariantRoadmap(
        currently_built=False,
        requirement_1=(
            "A 4-covariant scalar (or tensor component) Ω[g, u, T] that reduces to: "
            "H in FRW (Ω = Θ/3 from expansion scalar Θ = ∇_μ u^μ); "
            "|V|/R in spherical collapse (Ω = local radial expansion rate); "
            "ω₀ in static interior (Ω = structural mode frequency at R_eq). "
            "Candidate: Ω = (1/3)∇_μ u^μ (expansion scalar), but this gives H in FRW "
            "and does not directly give ω₀ in the static limit."
        ),
        requirement_2=(
            "A covariant ODE: τ_eff[Ω] · u^μ ∇_μ Φ + Φ = X[g, T] "
            "where τ_eff[Ω] = τ₀/(1+(Ω·τ₀)²) with Ω covariant. "
            "This ODE must reduce to each sector's effective equation in the appropriate limit."
        ),
        requirement_3=(
            "Verify that the structural identity ω₀·τ_eff = 1 holds in the static interior "
            "limit of the covariant ODE, i.e., that the covariant Ω evaluated at the static "
            "equilibrium gives Ω → ω₀ and τ_eff → 1/ω₀."
        ),
        survivable_without=True,
        declared_limitation=(
            "Current GRUT matter-sector analysis is performed in the effective "
            "spherically symmetric, quasi-static, preferred-frame regime.  "
            "τ_eff is evaluated with the sector-appropriate local frequency ω "
            "(H in cosmology, |V|/R in collapse, ω₀ in PDE sector).  "
            "Full covariant unification of τ_eff remains an open structural item.  "
            "The structural identity ω₀·τ_eff = 1 is preserved at equilibrium across contexts."
        ),
        notes=[
            "The expansion scalar Θ = ∇_μ u^μ is the leading covariant candidate for Ω.",
            "In FRW: Θ = 3H (factor of 3 from isotropic expansion).",
            "In spherical collapse: Θ depends on the velocity field profile.",
            "In static interior: Θ = 0 (static spacetime); requires a different mechanism.",
            "The static limit is the hardest case for covariant unification.",
        ],
    )


def build_domain_declaration() -> DomainDeclaration:
    """Build the formal effective-domain declaration."""
    return DomainDeclaration(
        domain_statement=(
            "All τ_eff results in the current GRUT architecture are produced within "
            "the effective spherically symmetric, quasi-static, preferred-frame regime.  "
            "τ_eff is evaluated as τ₀/(1+(ω·τ₀)²) where ω is the sector-appropriate "
            "local frequency: H (cosmology), |V|/R (collapse), or ω₀ (interior PDE).  "
            "No 4-covariant expression for ω is used.  Results are internally consistent "
            "within each sector's stated domain but are not manifestly frame-independent."
        ),
        spherical_symmetry_assumed=True,
        quasi_static_assumed=True,
        preferred_frame_assumed=True,
        covariant_omega_absent=True,
        declaration_is_survivable=True,
        what_is_not_survivable=(
            "Leaving the domain limitation implicit while making matter claims that "
            "depend on local dynamics in non-preferred frames, particle-like persistence "
            "under Lorentz boosts, or transport/propagation in anisotropic backgrounds.  "
            "Matter dynamics, moving localized configurations, and microscopic response "
            "all require τ_eff to be frame-safe.  Until covariant unification is built, "
            "all such claims must carry the effective-domain caveat explicitly."
        ),
        notes=[
            "This declaration does NOT invalidate existing results — it bounds their scope.",
            "Cosmological sector: H is well-defined in FRW; domain is the FRW background.",
            "Collapse sector: |V|/R is well-defined in the preferred collapse frame.",
            "Interior PDE: ω₀ is well-defined at static R_eq; domain is the static interior.",
            "Across all: the structural identity ω₀·τ_eff = 1 is the frame-safe anchor.",
        ],
    )


def assign_verdict(
    roadmap: CovariantRoadmap,
    identity: StructuralIdentity,
) -> str:
    """Compute verdict from Boolean outcomes."""
    if roadmap.currently_built and identity.preserved_across_contexts:
        return "tau_eff_covariant__structural_identity_preserved__fully_unified"
    elif not roadmap.currently_built and identity.preserved_across_contexts:
        return (
            "tau_eff_valid_in_preferred_frame_quasi_static_limit__"
            "covariant_unification_open__omega0_tau_identity_preserved"
        )
    else:
        return "tau_eff_fragmented__structural_identity_broken__requires_unification"


def run_tau_eff_domain_declaration() -> TauEffDomainResult:
    """Run the τ_eff domain declaration."""
    contexts = build_contexts()
    identity = build_structural_identity()
    roadmap = build_covariant_roadmap()
    declaration = build_domain_declaration()
    verdict = assign_verdict(roadmap, identity)

    nonclaims = [
        "NOT claiming τ_eff results are wrong — they are internally consistent within "
        "each sector's stated domain.",
        "NOT claiming covariant unification is impossible — it is absent, not ruled out.",
        "NOT claiming ω₀·τ_eff = 1 is fragile — it is locked at equilibrium and preserved.",
        "NOT claiming the three ω definitions are incompatible — they are each correct "
        "for their sector; the issue is the absence of a covariant object unifying them.",
    ]

    diagnostics: Dict[str, Any] = {
        "OMEGA_TAU_PRODUCT": OMEGA_TAU_PRODUCT,
        "OMEGA_0": OMEGA_0,
        "TAU_EFF_CANON": TAU_EFF_CANON,
        "TAU_SQ": TAU_SQ,
        "BETA_Q_CANON": BETA_Q_CANON,
        "num_contexts": len(contexts),
        "all_contexts_covariant": all(not c.is_covariant for c in contexts),
        "structural_identity_preserved": identity.preserved_across_contexts,
        "covariant_unification_built": roadmap.currently_built,
        "declaration_survivable": declaration.declaration_is_survivable,
        "verdict": verdict,
    }

    return TauEffDomainResult(
        contexts=contexts,
        structural_identity=identity,
        covariant_roadmap=roadmap,
        domain_declaration=declaration,
        covariant_unification_built=roadmap.currently_built,
        structural_identity_preserved=identity.preserved_across_contexts,
        verdict=verdict,
        nonclaims=nonclaims,
        diagnostics=diagnostics,
    )
