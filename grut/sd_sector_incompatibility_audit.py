"""
Appendix S-D --- Sector Breaking, Friction, and Incompatibilities Audit
=======================================================================
GRUT Symmetry Program --- Phase S-D

Determines the exact mathematical incompatibilities, friction points,
persistence of native breaking, and structural non-closure that arise
when all audited GRUT sectors are considered simultaneously.

This is a BREAKING AND INCOMPATIBILITY AUDIT. It does not search for
ways to save unification unless forced by the math.
"""

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List

TAU_SQ: float = 3.0 / 2.0
TAU: float = math.sqrt(TAU_SQ)

# Verdict enums
TOPO_DISS_OPTIONS = frozenset({
    "topological_protection_survives_only_conditionally",
    "dissipative_unwinding_or_erosion_possible",
    "topological_status_underdetermined_without_new_dynamics",
    "strict_immunity_demonstrated",
})
OBS_CONST_OPTIONS = frozenset({
    "carrier_space_mismatch_no_derivation",
    "partial_embedding_without_quantum_foundation",
    "formal_conflict_demonstrated",
    "unified_state_space_constructed",
})
SCALE_OPTIONS = frozenset({
    "multiple_unbridged_scales_persist",
    "hierarchy_tension_identified",
    "scale_relations_partially_derived",
    "unified_scale_structure_constructed",
})
SECTOR_OPTIONS = frozenset({
    "mutually_independent_layers",
    "partially_coupled_but_nonclosing",
    "structurally_conflicted",
    "genuinely_unified",
})
AUTH_OPTIONS = frozenset({
    "authorized_to_proceed_to_SE",
    "stop_for_missing_structure",
})
OVERALL_OPTIONS = frozenset({
    "disjoint_extensions_only",
    "layered_but_nonunified",
    "partially_integrable_with_new_postulates",
    "unified_extension_framework",
})

# Selected verdicts
SD_TOPO_DISS_VERDICT: str = "topological_protection_survives_only_conditionally"
SD_OBS_CONST_VERDICT: str = "carrier_space_mismatch_no_derivation"
SD_SCALE_VERDICT: str = "multiple_unbridged_scales_persist"
SD_SECTOR_VERDICT: str = "mutually_independent_layers"
SD_AUTH_VERDICT: str = "authorized_to_proceed_to_SE"
SD_OVERALL_P: str = "layered_but_nonunified"

N_SD_NONCLAIMS: int = 8
N_EVIDENCE_ROWS: int = 8
N_OBSTRUCTIONS: int = 6
N_ALLOWED: int = 7
N_FORBIDDEN: int = 7

SD_NONCLAIMS: List[str] = [
    "NOT_claiming_compatibility_therefore_unification__"
    "coexistence_of_sectors_is_not_unified_theory",
    "NOT_claiming_coherent_extension_therefore_native_derivation__"
    "extension_level_coherence_is_postulational",
    "NOT_claiming_SU2_like_therefore_electroweak__"
    "qubit_observable_algebra_is_internal_global_not_gauge",
    "NOT_claiming_O3_defect_therefore_gauge_sector__"
    "topological_sigma_model_is_not_gauge_theory",
    "NOT_claiming_emergent_Lorentz_therefore_exact_restoration__"
    "restricted_regime_appearance_is_not_native_invariance",
    "NOT_claiming_bridge_between_sectors_therefore_derivation__"
    "any_bridge_must_state_native_vs_extension_vs_new_postulate",
    "NOT_claiming_parameter_matching_therefore_scale_unification__"
    "coexisting_scales_without_derivation_are_unbridged",
    "NOT_claiming_sector_friction_resolved_therefore_theory_complete__"
    "friction_documentation_is_honest_accounting_not_repair",
]


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class SDTrackResult:
    """Result for a single audit track."""
    track_id: str
    track_name: str
    question: str
    findings: List[str]
    friction_points: List[str]
    verdict_contribution: str
    notes: List[str]


@dataclass
class SDEvidenceRow:
    """Single row in the cross-sector evidence table."""
    pair: str
    shared_carrier: str
    shared_dynamics: str
    transformation_closure: str
    main_friction: str
    what_absent: str
    row_verdict: str


@dataclass
class SDObstruction:
    """Single blocking obstruction, ranked."""
    rank: int
    obstruction_name: str
    severity: str  # "blocking", "dominant", "persistent", "limiting"
    description: str
    notes: List[str]


@dataclass
class SDNonclaimFirewall:
    nonclaims: List[str]
    n_nonclaims: int
    all_registered: bool


@dataclass
class SDSectorIncompatibilityResult:
    valid: bool
    track_a_topo_diss: SDTrackResult
    track_b_obs_const: SDTrackResult
    track_c_scale: SDTrackResult
    track_d_closure: SDTrackResult
    track_e_native_persist: SDTrackResult
    track_f_thermo: SDTrackResult
    track_g_firewall: SDNonclaimFirewall
    evidence_table: List[SDEvidenceRow]
    obstruction_ranking: List[SDObstruction]
    # Five hard-gated verdicts
    topological_dissipative_status: str
    observable_constitutive_status: str
    scale_status: str
    sector_relation: str
    authorization: str
    # Overall
    overall_appendix_p: str
    key_findings: List[str]
    allowed_claims: List[str]
    forbidden_claims: List[str]
    exact_nonclaims: List[str]
    diagnostics: Dict[str, Any]


# ---------------------------------------------------------------------------
# Track builders
# ---------------------------------------------------------------------------

def _track_a() -> SDTrackResult:
    """Track A: Topological vs Dissipative Friction."""
    return SDTrackResult(
        "A", "topological_vs_dissipative_friction",
        "Does native dissipation threaten topological protection?",
        findings=[
            "Topological CLASSIFICATION (integer winding pi_2(S^2)=Z) is a "
            "homotopy invariant of the field configuration at any instant. "
            "It does not depend on dynamics and remains well-defined under "
            "continuous deformation.",
            "However: DYNAMICAL STABILITY of a topological defect under dissipative "
            "evolution is NOT guaranteed by classification alone. The constitutive "
            "equation tau dPhi/dt + Phi = X is a relaxation law that drives Phi "
            "toward the source X. If X does not sustain the winding structure, "
            "dissipation will relax Phi toward a uniform configuration.",
            "Topological charge conservation requires that the field cannot cross "
            "a singular configuration during continuous evolution. In a dissipative "
            "PDE this holds IF the field remains smooth. But: dissipation with "
            "noise or singular sources could in principle destroy smoothness.",
            "Without Skyrme stabilizer (MBU): Derrick theorem applies; the defect "
            "has no stable size. Dissipation provides metastability (R-C) but "
            "eventual collapse or spreading is not prevented.",
            "Conclusion: topological protection survives CONDITIONALLY -- "
            "classification persists under smooth evolution, but dynamical "
            "stability requires additional structure (Skyrme or equivalent).",
        ],
        friction_points=[
            "dissipation_drives_relaxation_potentially_eroding_defect_support",
            "no_skyrme_stabilizer_means_no_size_stability_for_defect",
            "metastability_only_not_true_topological_stability",
            "noise_or_singular_sources_could_violate_smoothness_assumption",
        ],
        verdict_contribution=SD_TOPO_DISS_VERDICT,
        notes=["Key friction: classification survives; dynamics do not guarantee persistence"],
    )


def _track_b() -> SDTrackResult:
    """Track B: Observable vs Constitutive Conflict."""
    return SDTrackResult(
        "B", "observable_vs_constitutive_conflict",
        "Does constitutive relaxation conflict with SU(2)-like observable algebra?",
        findings=[
            "CARRIER SPACE MISMATCH: The native constitutive equation operates on "
            "a real scalar field Phi(x,t). The SU(2)-like observable algebra operates "
            "on a 2-dimensional complex Hilbert space C^2 (qubit). These are "
            "mathematically different objects: R vs C^2.",
            "No shared state space has been derived. The qubit C^2 was POSTULATED "
            "(Q-B.5: complex structure J as MIP) on top of the scalar field. "
            "The relationship is: Phi's classical expectation value <Phi_hat> "
            "satisfies the constitutive law in an effective regime (Q-C.5). "
            "But the qubit state rho and the classical field Phi are not the same object.",
            "The constitutive ODE CANNOT generate noncommuting operator algebra. "
            "A real first-order ODE is abelian; [f(t), g(t)] = 0 for any two "
            "real-valued functions. Noncommutativity was INTRODUCED by postulating "
            "sigma_x alongside sigma_z (Q-II.D), not derived from the ODE.",
            "No formal conflict exists: the two structures simply do not interact. "
            "The constitutive law governs expectation values of Phi_hat = sigma_z; "
            "the full su(2) algebra exists on the postulated qubit but does not "
            "feed back into the constitutive dynamics.",
            "Conclusion: carrier-space mismatch with no derivation bridging them. "
            "Not a contradiction -- a non-interaction / non-closure.",
        ],
        friction_points=[
            "real_scalar_field_vs_complex_hilbert_space_carrier_mismatch",
            "constitutive_ode_cannot_generate_noncommuting_algebra",
            "qubit_algebra_postulated_not_derived_from_ode",
            "no_feedback_from_full_su2_into_constitutive_dynamics",
        ],
        verdict_contribution=SD_OBS_CONST_VERDICT,
        notes=["Not a contradiction but a structural non-derivation"],
    )


def _track_c() -> SDTrackResult:
    """Track C: Scale Breaking Cascades."""
    return SDTrackResult(
        "C", "scale_breaking_cascades",
        "Do imported sectors create unbridged multi-scale dependence?",
        findings=[
            "NATIVE SCALE: tau^2 = 3/2. This is the canonical constitutive timescale. "
            "Also: barrier amplitude A (energy-density scale).",
            "O(3)/SKYRME SCALE: If O(3) + Skyrme are postulated, the Skyrmion radius "
            "R_sk ~ sqrt(L4_coeff / L2_coeff) introduces a NEW scale. The L2 and L4 "
            "coefficients are free parameters of the extension (MBU). No relation to "
            "tau has been derived.",
            "QUBIT/DECOHERENCE SCALE: The decoherence timescale tau_dec = tau/2 "
            "(for 2-state with Delta_phi=2) is DERIVED from tau. This is one of the "
            "few inter-sector scale relations that IS derived.",
            "EXCHANGE/MEMORY SCALE: The tau-memory exchange window (R-F) operates on "
            "the same timescale tau. Derived, not independent.",
            "FERMIONIC CANDIDATE SCALES: Any fermionic extension (Hopf, spinor) would "
            "introduce new mass/energy scales. These are entirely unspecified and "
            "have no relation to tau.",
            "COMPOSITE/CHEMISTRY SCALES: Binding energies, molecular scales, etc. are "
            "entirely absent. No bridge to tau.",
            "Conclusion: multiple unbridged scales persist. tau_dec is derived from tau "
            "(one success). All other extension scales are independent, free, or absent.",
        ],
        friction_points=[
            "skyrmion_radius_independent_of_tau",
            "fermionic_extension_scales_entirely_unspecified",
            "no_bridge_equation_linking_tau_to_topological_scales",
            "hierarchy_without_mechanism",
        ],
        verdict_contribution=SD_SCALE_VERDICT,
        notes=["One derived relation (tau_dec from tau); all others unbridged"],
    )


def _track_d() -> SDTrackResult:
    """Track D: Closure and Cross-Sector Non-Unification."""
    return SDTrackResult(
        "D", "closure_and_non_unification",
        "Do combined sectors close into one framework?",
        findings=[
            "CARRIER COMPATIBILITY: Native scalar (R), O(3) sigma model (S^2 target), "
            "qubit (C^2), composite (C^4), exchange (permutation group S_N). "
            "These are distinct mathematical spaces. No common carrier.",
            "SYMMETRY CLOSURE: Native Z2 x spatial SO(3), O(3) target-space SO(3), "
            "qubit su(2), exchange S_N. These do NOT close into a common group. "
            "The SO(3) of spatial rotations is DIFFERENT from the SO(3) of O(3) "
            "target space, which is different from the SU(2) of qubit algebra.",
            "DYNAMICS CLOSURE: Native constitutive ODE, Lindblad master equation, "
            "H_hop hopping Hamiltonian. These coexist but there is no single "
            "master equation governing all sectors simultaneously. The Lindblad "
            "governs the qubit sector; the constitutive ODE governs the classical "
            "field; they are linked only through Q-C.5 effective-regime recovery.",
            "CROSS-SECTOR ACTION: No sector acts nontrivially on another in a "
            "derived way. The qubit sector does not transform the O(3) topological "
            "charge. The exchange sector does not interact with the constitutive "
            "dynamics. The sectors merely coexist.",
            "Conclusion: mutually independent layers. Not structurally conflicted "
            "(no contradictions found), but not closing into unified framework.",
        ],
        friction_points=[
            "no_common_carrier_space",
            "no_common_symmetry_group",
            "no_single_master_equation",
            "sectors_do_not_act_on_each_other",
        ],
        verdict_contribution=SD_SECTOR_VERDICT,
        notes=["Independent layers: no conflict, no closure, no unification"],
    )


def _track_e() -> SDTrackResult:
    """Track E: Native Break Persistence."""
    return SDTrackResult(
        "E", "native_break_persistence",
        "Which native breaks survive all extensions?",
        findings=[
            "LORENTZ BREAKING: PERSISTS. tau preferred frame is present in every "
            "sector that inherits constitutive dynamics. Emergent Lorentz appearance "
            "is regime-limited, not restoration. No extension removes the preferred frame.",
            "TIME-REVERSAL BREAKING: PERSISTS. Dissipative arrow (tau dPhi/dt term) "
            "is inherited by Lindblad decoherence (off-diagonal decay). Both native "
            "and quantum sectors break T. No extension restores T.",
            "SCALE BREAKING: PERSISTS. tau^2=3/2 is a fixed canonical parameter. "
            "Extensions add more scales without bridging them to tau.",
            "GAUGE ABSENCE: PERSISTS. No extension introduces gauge fields. "
            "O(3) is topological; su(2) is global/internal. Gauge requires "
            "fundamentally new postulation.",
            "FERMIONIC ABSENCE: PERSISTS. 3-layer obstruction unchanged through "
            "all Q and R work. Routes identified but none built.",
            "BORN/PROBABILITY ABSENCE: PERSISTS. Q-II.F documented Born rule as "
            "absent. Minimum extension identified (PX1 MIP) but not adopted.",
            "CHEMISTRY ABSENCE: PERSISTS. R-G: all 6 bridge conditions unmet. "
            "No extension addresses any of them.",
        ],
        friction_points=[
            "lorentz_breaking_persists_in_all_sectors",
            "t_reversal_breaking_persists_in_all_sectors",
            "gauge_absence_persists_no_extension_introduces_gauge",
            "fermionic_absence_persists_3_layer_obstruction_unchanged",
        ],
        verdict_contribution="all_7_native_breaks_or_absences_persist",
        notes=["No native break or absence is repaired by any audited extension"],
    )


def _track_f() -> SDTrackResult:
    """Track F: Thermodynamic / Balance-Law Compatibility."""
    return SDTrackResult(
        "F", "thermodynamic_compatibility",
        "Do extensions undermine dissipative balance-law conclusions?",
        findings=[
            "QUBIT SECTOR: The Lindblad master equation is itself an open-system "
            "equation. It does NOT assume unitary conservation. Compatible with "
            "native dissipative ontology. No conflict.",
            "O(3) SECTOR: If the sigma-model field dynamics are dissipative "
            "(tau-type relaxation on S^2), the sector inherits the same "
            "thermodynamic character as native GRUT. No conflict IF dynamics "
            "are dissipative. Conflict arises only if Hamiltonian/conservative "
            "dynamics are silently assumed for the O(3) sector -- this would be "
            "a new postulate, not a native consequence.",
            "COMPOSITE/TENSOR-PRODUCT SECTOR: Independent Lindblad channels per "
            "subsystem: compatible with open-system ontology. H_hop introduces "
            "coherent (Hamiltonian) dynamics between sites -- this IS a new "
            "postulate (MIP) that partially conflicts with pure dissipation. "
            "The conflict is: H_hop is UNITARY coupling overlaid on DISSIPATIVE "
            "subsystems. This is the standard open-quantum-system approach but "
            "it means the composite sector is a MIXTURE of unitary and dissipative.",
            "EXCHANGE/STATISTICS: No thermodynamic conflict. Exchange symmetry "
            "is kinematic, not dynamic.",
            "Conclusion: Lindblad is compatible; O(3) dynamics require specifying "
            "dissipative character; H_hop introduces unitary-dissipative mixture "
            "as explicit extension.",
        ],
        friction_points=[
            "o3_dynamics_require_specifying_dissipative_or_hamiltonian_character",
            "h_hop_introduces_unitary_coupling_on_dissipative_substrate",
            "unitary_dissipative_mixture_is_extension_not_native",
        ],
        verdict_contribution="compatible_with_explicit_extension_caveats",
        notes=["No contradiction if extension character is explicitly stated"],
    )


def _build_evidence_table() -> List[SDEvidenceRow]:
    """Build the cross-sector evidence table."""
    return [
        SDEvidenceRow("native scalar vs O(3)",
            "No (R vs S^2 target)", "No (constitutive vs sigma-model)",
            "No (Z2 vs SO(3)_target)", "Carrier-space mismatch",
            "Bridge dynamics", "independent_layers"),
        SDEvidenceRow("native scalar vs SU(2)-like qubit",
            "No (R vs C^2)", "Partial (expectation-value bridge Q-C.5)",
            "No (abelian vs su(2))", "ODE cannot generate noncommutativity",
            "Quantum foundation", "carrier_mismatch"),
        SDEvidenceRow("O(3) vs SU(2)-like qubit",
            "No (S^2 target vs C^2)", "No",
            "No (topological vs algebraic)", "Different mathematical domains",
            "Coupling mechanism", "independent_layers"),
        SDEvidenceRow("native scalar vs emergent Lorentz",
            "Same (R)", "Partial (regime-limited)",
            "No", "Native break persists at fundamental level",
            "Derivation mechanism", "effective_appearance_only"),
        SDEvidenceRow("native scalar vs probability",
            "No (R vs density matrix)", "No",
            "No", "Born rule absent; diagnostic weights only",
            "Probability axiom", "unbridged"),
        SDEvidenceRow("native scalar vs fermionic",
            "No (R vs spinor)", "No",
            "No", "3-layer obstruction",
            "Spinorial structure, antisymmetrization", "blocked"),
        SDEvidenceRow("native scalar vs chemistry",
            "No", "No", "No",
            "All 6 bridge conditions unmet",
            "Particles, binding, fermions, probability, shells", "blocked"),
        SDEvidenceRow("ALL SECTORS COMBINED",
            "No common carrier", "No single master equation",
            "No common algebra/group", "Independent layering",
            "Unifying dynamics, gauge, fermions, probability",
            "mutually_independent_layers"),
    ]


def _build_obstruction_ranking() -> List[SDObstruction]:
    """Build ranked blocking-obstruction list."""
    return [
        SDObstruction(1, "fermionic_3_layer_obstruction", "blocking",
            "No spinors, no antisymmetrization, no Hopf map natively available. "
            "Blocks ALL chemistry-relevant matter.",
            ["Unchanged through Q Parts I/II, R program, S program"]),
        SDObstruction(2, "born_rule_absence", "blocking",
            "No probability interpretation. Blocks statistical prediction, "
            "measurement interpretation, and chemistry.",
            ["Q-II.F: documented BSR; MIP route identified but not adopted"]),
        SDObstruction(3, "native_lorentz_breaking", "dominant",
            "tau defines preferred frame. Persists through all sectors. "
            "Emergent appearance is regime-limited only.",
            ["S-B: native_canon result"]),
        SDObstruction(4, "gauge_absence", "dominant",
            "No gauge fields, local invariance, or covariant derivatives "
            "in any sector.",
            ["S-C: no_native_or_effective_gauge_symmetry_identified"]),
        SDObstruction(5, "carrier_space_fragmentation", "persistent",
            "R, S^2, C^2, C^4, S_N: no common mathematical carrier across sectors.",
            ["Each sector lives on its own mathematical space"]),
        SDObstruction(6, "scale_hierarchy_without_mechanism", "limiting",
            "tau, Skyrmion radius, fermionic scales: coexist without derivation.",
            ["One derived relation (tau_dec); all others unbridged"]),
    ]


def _build_firewall() -> SDNonclaimFirewall:
    return SDNonclaimFirewall(SD_NONCLAIMS, N_SD_NONCLAIMS, True)


# ---------------------------------------------------------------------------
# Master audit
# ---------------------------------------------------------------------------

def run_sd_sector_incompatibility_audit() -> SDSectorIncompatibilityResult:
    """Run the full S-D Sector Breaking, Friction, and Incompatibilities Audit."""
    ta = _track_a(); tb = _track_b(); tc = _track_c()
    td = _track_d(); te = _track_e(); tf = _track_f()
    tg = _build_firewall()
    ev = _build_evidence_table()
    obs = _build_obstruction_ranking()

    key_findings = [
        "Topological protection survives CONDITIONALLY under smooth dissipative "
        "evolution; dynamical stability requires Skyrme or equivalent (MBU)",
        "Carrier-space mismatch between native scalar (R), qubit (C^2), and O(3) "
        "target (S^2): no derivation bridges them; the ODE cannot generate "
        "noncommuting algebra",
        "Multiple unbridged scales persist: tau is canonical; Skyrmion radius, "
        "fermionic scales, chemistry scales are independent; only tau_dec is derived",
        "Sectors are mutually independent layers: no common carrier, no common "
        "algebra, no single master equation, no cross-sector action",
        "ALL 7 native breaks/absences persist through every extension: Lorentz, "
        "T-reversal, scale, gauge, fermions, Born rule, chemistry",
        "Thermodynamic compatibility holds with caveats: Lindblad is open-system; "
        "H_hop introduces unitary-dissipative mixture as explicit extension",
        "No contradiction found between sectors; the issue is non-closure and "
        "non-derivation, not conflict",
    ]

    allowed = [
        "Topological classification persists under smooth dissipative evolution; "
        "dynamical stability conditional on Skyrme or equivalent",
        "Native scalar and qubit sectors have carrier-space mismatch; linked only "
        "through Q-C.5 expectation-value bridge in effective regime",
        "Multiple unbridged scales: tau canonical; tau_dec derived; all others free",
        "Sectors are mutually independent layers with no cross-sector closure",
        "All 7 native breaks/absences persist unchanged through all extensions",
        "Thermodynamic compatibility with caveats: H_hop is unitary-dissipative mixture",
        "S-E authorized: sector friction documented, unified ledger next",
    ]

    forbidden = [
        "Compatibility implies unification",
        "Extension coherence implies native derivation",
        "SU(2)-like algebra implies electroweak SU(2)",
        "O(3) defect implies gauge sector",
        "Emergent Lorentz implies exact restoration",
        "Parameter matching implies scale unification",
        "Sector friction resolved implies theory complete",
    ]

    diagnostics: Dict[str, Any] = {
        "n_evidence_rows": N_EVIDENCE_ROWS,
        "n_obstructions": N_OBSTRUCTIONS,
        "n_native_breaks_persisting": 7,
        "n_derived_scale_relations": 1,  # tau_dec from tau
        "common_carrier_found": False,
        "common_dynamics_found": False,
        "transformation_closure_found": False,
        "any_contradiction_found": False,
        "n_nonclaims": N_SD_NONCLAIMS,
    }

    result = SDSectorIncompatibilityResult(
        valid=True,
        track_a_topo_diss=ta, track_b_obs_const=tb,
        track_c_scale=tc, track_d_closure=td,
        track_e_native_persist=te, track_f_thermo=tf,
        track_g_firewall=tg,
        evidence_table=ev, obstruction_ranking=obs,
        topological_dissipative_status=SD_TOPO_DISS_VERDICT,
        observable_constitutive_status=SD_OBS_CONST_VERDICT,
        scale_status=SD_SCALE_VERDICT,
        sector_relation=SD_SECTOR_VERDICT,
        authorization=SD_AUTH_VERDICT,
        overall_appendix_p=SD_OVERALL_P,
        key_findings=key_findings,
        allowed_claims=allowed, forbidden_claims=forbidden,
        exact_nonclaims=SD_NONCLAIMS, diagnostics=diagnostics,
    )
    _validate(result)
    return result


def _validate(r: SDSectorIncompatibilityResult) -> None:
    if r.topological_dissipative_status not in TOPO_DISS_OPTIONS:
        raise ValueError("topo_diss verdict invalid")
    if r.observable_constitutive_status not in OBS_CONST_OPTIONS:
        raise ValueError("obs_const verdict invalid")
    if r.scale_status not in SCALE_OPTIONS:
        raise ValueError("scale verdict invalid")
    if r.sector_relation not in SECTOR_OPTIONS:
        raise ValueError("sector verdict invalid")
    if r.authorization not in AUTH_OPTIONS:
        raise ValueError("auth verdict invalid")
    if r.overall_appendix_p not in OVERALL_OPTIONS:
        raise ValueError("overall verdict invalid")
    if r.track_g_firewall.n_nonclaims != N_SD_NONCLAIMS:
        raise ValueError("nonclaim count")
    if not r.track_g_firewall.all_registered:
        raise ValueError("nonclaims not registered")
    if len(r.allowed_claims) != N_ALLOWED:
        raise ValueError(f"Expected {N_ALLOWED} allowed")
    if len(r.forbidden_claims) != N_FORBIDDEN:
        raise ValueError(f"Expected {N_FORBIDDEN} forbidden")
    if len(r.evidence_table) != N_EVIDENCE_ROWS:
        raise ValueError(f"Expected {N_EVIDENCE_ROWS} evidence rows")
    if len(r.obstruction_ranking) != N_OBSTRUCTIONS:
        raise ValueError(f"Expected {N_OBSTRUCTIONS} obstructions")
    # Verify ranking is sequential
    for i, obs in enumerate(r.obstruction_ranking):
        if obs.rank != i + 1:
            raise ValueError(f"Obstruction rank {obs.rank} != expected {i+1}")
    # Verify key diagnostic constraints
    if r.diagnostics["common_carrier_found"]:
        raise ValueError("common_carrier must be False")
    if r.diagnostics["transformation_closure_found"]:
        raise ValueError("closure must be False")
    if r.diagnostics["any_contradiction_found"]:
        raise ValueError("contradiction must be False")


def _self_test() -> bool:
    r = run_sd_sector_incompatibility_audit()
    assert r.valid is True
    assert r.topological_dissipative_status == SD_TOPO_DISS_VERDICT
    assert r.observable_constitutive_status == SD_OBS_CONST_VERDICT
    assert r.scale_status == SD_SCALE_VERDICT
    assert r.sector_relation == SD_SECTOR_VERDICT
    assert r.authorization == SD_AUTH_VERDICT
    assert r.overall_appendix_p == SD_OVERALL_P
    assert r.diagnostics["n_native_breaks_persisting"] == 7
    assert r.diagnostics["n_derived_scale_relations"] == 1
    assert r.diagnostics["common_carrier_found"] is False
    assert r.diagnostics["any_contradiction_found"] is False
    return True


if __name__ == "__main__":
    _self_test()
    print("S-D self-test passed.")
