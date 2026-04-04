"""
GRUT-RAI Unified Program State
================================

Machine-usable cross-sector state representation implementing
the GRUT-RAI Unified Sector-Intent Charter.

This module is the single source of truth for GRUT-RAI's understanding
of where the program stands across all sectors.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import List, Dict, Optional


# =====================================================================
# Enums
# =====================================================================

class AuthorityTier(str, Enum):
    """Canon authority tiers (C0-C6)."""
    PUBLIC_CANON = "C0"
    VALIDATED_BASELINE = "C1"
    STRONG_FRONTIER = "C2"
    CONDITIONAL_FRONTIER = "C3"
    EXPLORATORY = "C4"
    FAILED = "C5"
    NONCLAIM = "C6"


class SectorStatus(str, Enum):
    """Sector operational status."""
    FROZEN = "frozen"
    ACTIVE = "active"
    FRONTIER = "frontier"
    FAILED = "failed"
    BLOCKED = "blocked"


class RealityClass(str, Enum):
    """Reality-touching output classes (R1-R7)."""
    STRUCTURAL_THEOREM = "R1"
    CLOSED_SYSTEM = "R2"
    NUMERICAL_BRANCH = "R3"
    SIGNATURE_MAP = "R4"
    COMPARISON_READY = "R5"
    EMPIRICAL_CONFRONTATION = "R6"
    HEURISTIC_ANALOGY = "R7"


class ToEStatus(str, Enum):
    """Theory of Everything status."""
    ACTIVE = "active"
    RETIRED = "retired"
    CONDITIONALLY_REOPENABLE = "conditionally_reopenable"


# =====================================================================
# Dataclasses
# =====================================================================

@dataclass
class RealityOutput:
    """A reality-touching output with its classification."""
    description: str
    class_code: RealityClass
    authority_tier: AuthorityTier
    comparison_ready: bool = False


@dataclass
class SectorState:
    """State of a single program sector."""
    name: str
    backbone_relation: str
    authority_tier: AuthorityTier
    status: SectorStatus
    validated_content: List[str] = field(default_factory=list)
    conditional_content: List[str] = field(default_factory=list)
    open_content: List[str] = field(default_factory=list)
    failed_content: List[str] = field(default_factory=list)
    nonclaims: List[str] = field(default_factory=list)
    reality_outputs: List[RealityOutput] = field(default_factory=list)
    dependencies: List[str] = field(default_factory=list)
    next_step: str = ""
    changes_identity: bool = False


@dataclass
class CostLedger:
    """Program cost accounting."""
    committed_postulates: int = 16
    committed_parameters: int = 11
    committed_fields: int = 1
    committed_dof: int = 6
    bridges_committed: int = 5
    hypothetical_ggb_postulates: int = 17
    hypothetical_ggb_parameters: int = 12
    hypothetical_ggb_fields: int = 2
    hypothetical_ggb_dof: int = 8
    zero_cost_targets: int = 26


@dataclass
class FailedRoute:
    """A route tested and found to fail."""
    name: str
    book: str
    reason: str
    sector: str
    permanently_failed: bool = False


@dataclass
class Nonclaim:
    """Something the program explicitly does not claim."""
    claim: str
    reason: str
    permanent: bool = True


@dataclass
class SectorHandoff:
    """A result handed from one sector to another."""
    from_sector: str
    to_sector: str
    content: str
    authority_inherited: AuthorityTier
    conditions_carried: List[str] = field(default_factory=list)


@dataclass
class ProgramIdentity:
    """The whole-program identity."""
    identity_statement: str
    public_canon_layer: str
    validated_baseline_layer: str
    active_frontier_layer: str
    toe_status: ToEStatus
    gravity_identity: str


@dataclass
class SchemaMeta:
    """Schema metadata."""
    schema_version: str = "1.9.0"
    last_updated: str = "2026-04"
    last_book: str = "XVI_Beta_WeakField"
    charter_version: str = "1.0"


@dataclass
class ProgramState:
    """Complete cross-sector program state."""
    identity: ProgramIdentity
    sectors: Dict[str, SectorState] = field(default_factory=dict)
    cost: CostLedger = field(default_factory=CostLedger)
    failed_routes: List[FailedRoute] = field(default_factory=list)
    nonclaims: List[Nonclaim] = field(default_factory=list)
    handoffs: List[SectorHandoff] = field(default_factory=list)
    meta: SchemaMeta = field(default_factory=SchemaMeta)
    corrections: List[str] = field(default_factory=list)

    def to_json(self, indent: int = 2) -> str:
        """Serialize to JSON."""
        return json.dumps(asdict(self), indent=indent, default=str)


# =====================================================================
# Current program state (canonical)
# =====================================================================

def build_current_state() -> ProgramState:
    """Build the canonical current program state after Book XVI Beta."""

    identity = ProgramIdentity(
        identity_statement=(
            "GRUT is a dissipative-vacuum-response constitutive architecture "
            "(tau dPhi/dt + Phi = X) with one irreducible structural claim: "
            "the constitutive dissipation, coupled to Einstein gravity, predicts "
            "a specific equilibrium energy-momentum rho_eq = -X^2/(2tau^2), "
            "w = -1, NEC-saturated (Phase 4, xAct-verified). This is derived "
            "from one postulate with one free parameter (tau). The claim "
            "survives adversarial math and cannot be reduced to GR + matter. "
            "Adverse consequences (worsened interiors, anti-acceleration) are "
            "the predictions. Five bridge extensions produce matter through "
            "biology (26 zero-cost targets). Compact-object frontier collapsed "
            "(XVI Alpha sign error). Next: constrain tau from observation."
        ),
        public_canon_layer="Omni-ToE v3; Phase I-III locked; NIS-certified packets",
        validated_baseline_layer=(
            "Books IV-X biology-side scaffold (16/11/1/6); "
            "matter-within-GR gravity; locked numerical results (tov_interior.py)"
        ),
        active_frontier_layer=(
            "Equilibrium T^Phi (rho_eq = -X^2/(2tau^2)) is REDUCIBLE to GR + "
            "massive scalar at equilibrium and OBSERVATIONALLY SILENT at all "
            "physical tau values (XVI Beta weak-field: corrections 10^-16 or "
            "smaller). Structural novelty is DYNAMICS ONLY (native dissipation, "
            "Lyapunov, time-reversal breaking). GGB UNCOMMITTED. Compact-object "
            "frontier COLLAPSED (XVI Alpha). Surplus = 0."
        ),
        toe_status=ToEStatus.CONDITIONALLY_REOPENABLE,
        gravity_identity="Matter/organization theory within standard Einstein gravity",
    )

    # --- Sectors ---

    vacuum = SectorState(
        name="vacuum_constitutive",
        backbone_relation="tau dPhi/dt + Phi = X (native core)",
        authority_tier=AuthorityTier.PUBLIC_CANON,
        status=SectorStatus.FROZEN,
        validated_content=[
            "First-order dissipative scalar ODE",
            "Forward semigroup S(t) = exp(-t/tau)",
            "Lyapunov V = (1/2)(Phi - X_ss)^2",
            "tau^2 = 3/2 (Diamond Lock)",
        ],
        nonclaims=["Not a fundamental law; effective constitutive description"],
    )

    matter = SectorState(
        name="matter_biology",
        backbone_relation="tau dPhi/dt + Phi = X -> O(3) solitons -> SU(2) composites -> HIC -> carrier -> CCBG",
        authority_tier=AuthorityTier.VALIDATED_BASELINE,
        status=SectorStatus.FROZEN,
        validated_content=[
            "Five bridges: matter, gauge, HIC, carrier, CCBG",
            "M4/D4/L4/A4-stabilized",
            "T2 robust + T3 conditional transport",
            "26 zero-cost upper-stack targets",
            "Carrier barrier stabilized (W0 + IX Alpha)",
        ],
        nonclaims=[
            "Life", "Origin-of-life solved", "Open-ended evolution",
            "ATP equivalence", "Active transport (full)",
        ],
        next_step="Resumable from Book X terminal for broader T3/T4/metabolic regulation",
    )

    gravitational = SectorState(
        name="gravitational",
        backbone_relation="G_munu = 8piG T^Phi_munu (GGB architecture); T^Phi from Phase 4 xAct",
        authority_tier=AuthorityTier.STRONG_FRONTIER,
        status=SectorStatus.FRONTIER,
        validated_content=[
            "Matter-within-GR identity (XI Beta; C1)",
            "Binary-pulsar compatibility via GR (XI Alpha)",
            "Scalar-only static TOV WORSENS interior (XIII Gamma; LOCKED)",
        ],
        conditional_content=[
            "GGB design (XI Delta; uncommitted)",
            "D1-D10 combined f > 0 (proxy + fixed BG + defect essential)",
            "Binary-pulsar tau consistency (XII Gamma; tau ~ 1e-5 s)",
        ],
        failed_content=[
            "Native scalar gravity (XI Alpha: structural failure)",
            "Emergent gravity (W1: no route in canon)",
            "GW-sector surplus (XII Beta: tensor = GR; scalar invisible)",
            "Dark-energy replacement (XII Alpha: rho_eq < 0 anti-accelerating)",
            "Scalar-only singularity resolution (XIII Gamma: scalar worsens)",
            "Scalar-only structural predictions (XIII Gamma: all three incorrect)",
        ],
        nonclaims=[
            "Native gravity derivation", "Sixth-bridge commitment",
            "Restored ToE", "Cosmological closure", "GW surplus",
            "Permanent singularity resolution (scalar-only)",
        ],
        dependencies=["vacuum_constitutive", "source_defect"],
        next_step="Full combined scalar+defect self-consistent TOV integration",
        changes_identity=True,
    )

    cosmological = SectorState(
        name="cosmological",
        backbone_relation="Friedmann + T^Phi; three-regime H*tau dynamics",
        authority_tier=AuthorityTier.CONDITIONAL_FRONTIER,
        status=SectorStatus.FRONTIER,
        validated_content=[],
        conditional_content=[
            "Dynamical cosmological regulator (three-regime H*tau transition; XII Alpha revised)",
            "Early-universe modification at T ~ 1e12 K (XII Gamma)",
        ],
        failed_content=[
            "Dark-energy replacement (XII Alpha: rho_eq < 0)",
            "Late-universe cosmological modification",
        ],
        nonclaims=["Dark energy solution", "Cosmological closure", "Late-universe modification"],
        dependencies=["vacuum_constitutive", "gravitational"],
        next_step="Perturbation-sector development; early-universe phenomenology",
    )

    strong_field = SectorState(
        name="strong_field_compact",
        backbone_relation="Modified TOV (Phase 4 D); two-component A+B support; portal coupling",
        authority_tier=AuthorityTier.FAILED,
        status=SectorStatus.FROZEN,
        validated_content=[
            "Static scalar-only TOV: f = -17.71 (WORSENS interior; LOCKED tov_interior.py)",
            "Phase 4 T^Phi components fully specified",
            "Modified TOV system is CLOSED (four coupled ODEs)",
            "Phase 4 sign error CORRECTED: mass INCREASES inward, not decreases (tov_interior.py LOCKED)",
            "D7/D8 sign error IDENTIFIED (XVI Alpha): m_eff = M + Sigma should be M - Sigma",
            "Self-consistent A_eff ~ 0.1, not 2 (XVI Alpha quasi_static_rate.py)",
            "Proper-time rate = 1/tau ALWAYS (no amplification mechanism)",
        ],
        conditional_content=[],
        open_content=[],
        failed_content=[
            "Scalar-only singularity resolution (XIII Gamma: scalar WORSENS)",
            "Scalar-only Buchdahl relaxation (XIII Gamma: incorrect sign; RETRACTED)",
            "Scalar-only two-zone architecture (XIII Gamma: incorrect; RETRACTED)",
            "Scalar-only non-monotonic mass profile (XIII Gamma: mass increases inward; RETRACTED)",
            "'rho_eq < 0 reduces interior mass' (XIII Delta: RETRACTED; Phase 4 sign error)",
            "D7/D8 source amplification A_eff ~ 2 (XVI Alpha: SIGN ERROR; m_eff = M + Sigma wrong)",
            "D1-D10 combined f > 0 (XVI Alpha: artifact of D7/D8 sign error)",
            "XV Beta f >> 0 at all lambda (XVI Alpha: artifact of sign error; SC f ~ 0.7)",
            "Equilibrium path (XVI Alpha: singular; m_eq diverges at r ~ 0.75)",
            "Transient path (XVI Alpha: A_SC ~ 0.1; processing negligible)",
            "Conditional surpluses (XVI Alpha: ALL COLLAPSED)",
        ],
        nonclaims=[
            "Permanent singularity resolution (scalar-only)",
            "Demonstrated singularity resolution (XVI Alpha: proxy invalidated)",
            "Black-hole replacement",
            "Comparison-ready M-R curves",
            "Scalar-only structural predictions (all retracted by XIII Delta)",
            "D7/D8 source amplification (XVI Alpha: sign error)",
            "Compact-object metric support (XVI Alpha: surplus collapsed)",
        ],
        dependencies=["vacuum_constitutive", "gravitational", "source_defect"],
        next_step="FROZEN. New mechanism required for metric support. No identified path.",
    )

    source_defect = SectorState(
        name="source_defect",
        backbone_relation="O(3) hedgehog: Phi_a = eta f(r) x_hat_a; curvature trigger; portal Phi^2|Phi_vec|^2",
        authority_tier=AuthorityTier.STRONG_FRONTIER,
        status=SectorStatus.FRONTIER,
        validated_content=[
            "Hedgehog BVP converges (D2)",
            "Component B tail eta^2/r^2 (D1-D2)",
            "Portal coupling Phi^2|Phi_vec|^2 as unique interaction (D8)",
        ],
        conditional_content=[
            "Companion model viability (D6-D7)",
            "Self-consistent Picard iteration (D9; proxy closure)",
            "Kretschmann trigger (D10; degenerate with Weyl in vacuum)",
        ],
        nonclaims=["Cosmological analogue (hedgehog requires spatial center; FRW has none)"],
        dependencies=["vacuum_constitutive"],
        next_step="Full coupled scalar+defect TOV on self-consistent background",
    )

    grut_rai = SectorState(
        name="grut_rai",
        backbone_relation="Unified Sector-Intent Charter; Canon/Authority Architecture; Interpretation/Response Contract",
        authority_tier=AuthorityTier.VALIDATED_BASELINE,
        status=SectorStatus.ACTIVE,
        validated_content=[
            "Unified charter (this document set)",
            "Six authority tiers (C0-C6)",
            "Seven reality-touching classes (R1-R7)",
            "Eight drift-prevention rules",
            "Interpretation and response contracts",
        ],
        next_step="Wire doctrine into response pipeline; enforce in future books",
    )

    sectors = {
        s.name: s for s in [vacuum, matter, gravitational, cosmological,
                            strong_field, source_defect, grut_rai]
    }

    # --- Failed Routes ---

    failed_routes = [
        FailedRoute("Native scalar gravity", "XI Alpha",
                    "Scalar (spin-0) != tensor (spin-2); no GW; screened potential",
                    "gravitational", permanently_failed=True),
        FailedRoute("Emergent gravity from canon", "W1",
                    "Zero mechanisms; three firewalled analogies",
                    "gravitational", permanently_failed=True),
        FailedRoute("Dark-energy replacement", "XII Alpha",
                    "rho_eq < 0 is anti-accelerating; w = -1 wrong sign",
                    "cosmological", permanently_failed=True),
        FailedRoute("GW-sector surplus", "XII Beta",
                    "Tensor = GR; scalar invisible; tau unconstrained",
                    "gravitational", permanently_failed=True),
        FailedRoute("Scalar-only singularity resolution", "XIII Gamma",
                    "Static scalar TOV WORSENS interior (f = -17.71); Phase 4 sign error corrected",
                    "strong_field_compact", permanently_failed=True),
        FailedRoute("Scalar-only structural predictions", "XIII Gamma",
                    "Buchdahl relaxation, two-zone, mass deficit ALL incorrect for scalar-only",
                    "strong_field_compact", permanently_failed=True),
        FailedRoute("D7/D8 source amplification (A_eff ~ 2)", "XVI Alpha",
                    "Sign error: m_eff = M + Sigma should be M - Sigma (Birkhoff); SC A_eff ~ 0.1",
                    "strong_field_compact", permanently_failed=True),
        FailedRoute("D1-D10 combined metric support", "XVI Alpha",
                    "Depended on D7/D8 A_eff ~ 2; sign error invalidates; f ~ 0.7 (SC) not >> 0",
                    "strong_field_compact", permanently_failed=True),
        FailedRoute("Equilibrium compact-object path", "XVI Alpha",
                    "Self-consistent equilibrium mass singular at r ~ 0.75; path not viable",
                    "strong_field_compact", permanently_failed=True),
    ]

    # --- Nonclaims ---

    nonclaims = [
        Nonclaim("Theory of Everything",
                 "ToE label retired (XI Beta); conditionally reopenable",
                 permanent=False),
        Nonclaim("Native gravity derivation",
                 "Structural failure (XI Alpha); scalar != tensor",
                 permanent=True),
        Nonclaim("Life",
                 "Multiple biology-side boundaries uncrossed",
                 permanent=True),
        Nonclaim("Dark energy solution",
                 "rho_eq < 0 anti-accelerating (XII Alpha)",
                 permanent=True),
        Nonclaim("GW-sector beyond-GR surplus",
                 "Tensor = GR; scalar invisible (XII Beta)",
                 permanent=True),
        Nonclaim("Permanent singularity resolution (scalar-only)",
                 "Scalar worsens interior (XIII Gamma)",
                 permanent=True),
    ]

    corrections = [
        "XIII Gamma: Phase 4 sign error corrected — mass INCREASES inward (tov_interior.py LOCKED)",
        "XIII Gamma: Static scalar-only TOV WORSENS interior (f = -17.71 vs A_Schw = -2.0)",
        "XIII Delta: 4 claims RETRACTED (mass reduction, Buchdahl, two-zone, mass profile)",
        "XIII Delta: 3 claims DOWNGRADED (singularity resolution, remnant, signatures)",
        "XIII Delta: Surplus portfolio revised to 0 demonstrated + 2 conditional + 0 GW",
        "XIII Delta: Dual-track compact-object path selected (combined equilibrium + transient collapse)",
        "XVI Alpha: D7/D8 SIGN ERROR — m_eff = M + Sigma should be M - Sigma (Birkhoff theorem)",
        "XVI Alpha: Self-consistent A_eff = 0.11 (not 2.0); proxy overpredicts by 17x",
        "XVI Alpha: XV Beta f >> 0 is ARTIFACT of sign error; SC f ~ 0.7",
        "XVI Alpha: Conditional surpluses COLLAPSE from 2-3 to 0",
        "XVI Alpha: Proper-time rate = 1/tau ALWAYS; no rate amplification mechanism",
        "XVI Alpha: Equilibrium mass ODE SINGULAR (confirms XIII Gamma, tov_interior.py)",
    ]

    return ProgramState(
        identity=identity,
        sectors=sectors,
        cost=CostLedger(),
        failed_routes=failed_routes,
        nonclaims=nonclaims,
        meta=SchemaMeta(),
        corrections=corrections,
    )


# =====================================================================
# Convenience
# =====================================================================

def get_current_state_json(indent: int = 2) -> str:
    """Return the current program state as JSON."""
    return build_current_state().to_json(indent=indent)


if __name__ == "__main__":
    print(get_current_state_json())
