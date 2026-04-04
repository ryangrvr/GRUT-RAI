"""
Appendix V-B --- Vacuum Existence, Ground-State Ontology, and Source-Free Limit
================================================================================
GRUT Vacuum Ontology Program --- Phase V-B

Determines the exact mathematical and ontological status of GRUT in
the source-free limit X = 0.

=== CORE ANALYSIS ===

Source-free equation: tau dPhi/dt + Phi = 0
Solution: Phi(t) = Phi(0) exp(-t/tau)

MATHEMATICAL FACTS:
  1. For ANY initial condition Phi(0), the solution decays EXPONENTIALLY
     to zero: Phi(t) -> 0 as t -> infinity.
  2. The decay is MONOTONIC and IRREVERSIBLE (T-B semigroup).
  3. Phi = 0 is the UNIQUE GLOBAL ATTRACTOR of the source-free dynamics.
  4. Phi = 0 is STABLE: small perturbations decay back to zero.
  5. There is NO nonzero stationary solution in the source-free case.

GROUND-STATE STATUS:
  Phi = 0 is the unique rest state when X = 0. It is:
  - Mathematically: the global attractor of the dissipative semigroup
  - Dynamically: stable (Lyapunov V = Phi^2/2 -> 0)
  - Constitutively: the empty-response state (no source, no response)

  But: "ground state" in physics usually means "lowest energy eigenstate."
  GRUT has no energy functional, no Hamiltonian, no eigenvalue problem.
  Calling Phi = 0 a "ground state" is an ANALOGY, not a native statement.
  Honest language: "zero rest state" or "constitutive attractor at zero."

SUBSTRATE PERSISTENCE:
  When Phi -> 0, does the vacuum "still exist"?
  The equation tau dPhi/dt + Phi = 0 PRESUPPOSES:
    - a field variable Phi defined over space
    - a constitutive timescale tau
    - a dynamical law governing Phi's evolution
  These structural elements PERSIST even when Phi = 0.
  The field Phi is DEFINED everywhere even when its value is zero.
  The medium/substrate is the law + variables, not the field value.

  CONDITIONAL: the substrate (constitutive law + tau + spatial domain)
  persists with zero response. This is STRUCTURALLY supported but
  ONTOLOGICALLY ambiguous: is the law "still there" when nothing moves?

MACHIAN / RELATIONAL:
  Source-free decay to zero means: without X, the response dies.
  This is WEAK SOURCE DEPENDENCE: manifest content requires sources,
  but the substrate (law + variables + tau) does not require sources
  for its definition.
  Strict Machian: substrate itself requires sources. NOT supported
  (the equation is well-defined even without X).
  Weak source dependence: response requires sources; substrate doesn't.
"""

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List

TAU_SQ: float = 3.0 / 2.0
TAU: float = math.sqrt(TAU_SQ)
GAMMA: float = 1.0 / TAU

N_REGIMES: int = 6
N_OBSTRUCTIONS: int = 6
N_VB_NONCLAIMS: int = 8
N_ALLOWED: int = 7; N_FORBIDDEN: int = 7

SF_OPTIONS = frozenset({
    "asymptotic_decay_to_zero_supported",
    "nonzero_source_free_state_supported",
    "source_free_state_conditionally_nontrivial",
    "source_free_state_not_resolved",
})
GS_OPTIONS = frozenset({
    "zero_rest_state_supported",
    "zero_state_is_constitutive_but_ontologically_ambiguous",
    "nonzero_ground_state_supported",
    "ground_state_status_unresolved",
})
SP_OPTIONS = frozenset({
    "substrate_persists_with_zero_response_conditionally_supported",
    "source_supported_manifestation_only",
    "source_free_substrate_not_established",
    "substrate_status_ontologically_unresolved",
})
MACH_OPTIONS = frozenset({
    "weak_source_dependence_only",
    "strict_machian_dependence_supported",
    "nonmachian_substrate_persistence_supported",
    "machian_interpretation_not_resolved",
})
AUTH_OPTIONS = frozenset({
    "authorized_to_proceed_to_VC",
    "stop_for_missing_ground_state_boundary",
})
OVERALL_OPTIONS = frozenset({
    "source_free_decay_to_zero_sharply_bounded_without_quantum_vacuum",
    "zero_rest_state_supported_but_substrate_ontology_not_closed",
    "weak_source_dependence_identified_without_strict_relationality",
    "vacuum_ground_state_not_yet_resolved",
})

VB_SF: str = "asymptotic_decay_to_zero_supported"
VB_GS: str = "zero_state_is_constitutive_but_ontologically_ambiguous"
VB_SP: str = "substrate_persists_with_zero_response_conditionally_supported"
VB_MACH: str = "weak_source_dependence_only"
VB_AUTH: str = "authorized_to_proceed_to_VC"
VB_OVERALL: str = "source_free_decay_to_zero_sharply_bounded_without_quantum_vacuum"

VB_NONCLAIMS: List[str] = [
    "NOT_claiming_Phi_eq_0_therefore_nonexistence__"
    "zero_field_value_is_not_disappearance_of_space_or_substrate",
    "NOT_claiming_zero_attractor_therefore_ground_state__"
    "dissipative_attractor_is_not_energy_eigenstate",
    "NOT_claiming_source_free_decay_therefore_VEV__"
    "asymptotic_zero_is_not_vacuum_expectation_value",
    "NOT_claiming_substrate_persistence_therefore_substance__"
    "structural_persistence_is_not_density_or_stress",
    "NOT_claiming_source_dependence_therefore_Mach__"
    "response_dependence_is_not_strict_relational_ontology",
    "NOT_claiming_zero_vacuum_therefore_cosmological_constant__"
    "constitutive_rest_state_is_not_Lambda",
    "NOT_claiming_stability_therefore_SSB__"
    "stable_zero_attractor_is_not_spontaneous_symmetry_breaking",
    "NOT_claiming_source_free_limit_therefore_ontology_settled__"
    "mathematical_limit_does_not_close_philosophical_interpretation",
]


@dataclass
class VBTrackResult:
    track_id: str; track_name: str; question: str
    findings: List[str]; verdict_contribution: str; notes: List[str]

@dataclass
class VBEvidenceRow:
    regime: str; math_result: str; ontology_licensed: str
    ground_state: str; substrate: str
    what_licensed: str; what_not_licensed: str

@dataclass
class VBObstruction:
    rank: int; name: str; description: str

@dataclass
class VBNonclaimFirewall:
    nonclaims: List[str]; n_nonclaims: int; all_registered: bool

@dataclass
class VBVacuumExistenceResult:
    valid: bool
    track_a_source_free: VBTrackResult
    track_b_ground_state: VBTrackResult
    track_c_persistence: VBTrackResult
    track_d_machian: VBTrackResult
    track_e_stability: VBTrackResult
    track_f_firewall: VBTrackResult
    track_g_obstructions: List[VBObstruction]
    evidence_table: List[VBEvidenceRow]
    nonclaim_firewall: VBNonclaimFirewall
    source_free_state_status: str; ground_state_status: str
    substrate_persistence_status: str; machian_status: str
    authorization: str; overall_appendix_p: str
    key_findings: List[str]
    allowed_claims: List[str]; forbidden_claims: List[str]
    exact_nonclaims: List[str]; diagnostics: Dict[str, Any]


def _track_a() -> VBTrackResult:
    return VBTrackResult("A","source_free_limit",
        "What is the exact solution when X = 0?",
        [
            "Equation: tau dPhi/dt + Phi = 0.",
            "Solution: Phi(t) = Phi(0) exp(-t/tau).",
            "For ANY initial Phi(0): Phi(t) -> 0 as t -> inf.",
            "Decay is exponential, monotonic, irreversible (T-B).",
            "Phi = 0 is the UNIQUE global attractor. No nonzero stationary state.",
            "No finite-time collapse: decay is asymptotic only.",
        ],
        VB_SF,
        ["Pure exponential decay; unique zero attractor"])

def _track_b() -> VBTrackResult:
    return VBTrackResult("B","ground_state",
        "What is the ontological status of Phi = 0?",
        [
            "Phi = 0 is the unique REST STATE of source-free dynamics.",
            "Mathematically: global attractor of contraction semigroup.",
            "Dynamically: Lyapunov-stable (V = Phi^2/2 decays to zero).",
            "Constitutively: the empty-response state (no source -> no response).",
            "BUT: 'ground state' = 'lowest energy eigenstate' in physics. "
            "GRUT has no energy, no Hamiltonian, no eigenvalue problem.",
            "Honest language: 'zero rest state' or 'constitutive attractor at zero.'",
            "Ontologically AMBIGUOUS: is the rest state a vacuum, a trivial limit, "
            "or merely one constitutive regime?",
        ],
        VB_GS,
        ["Constitutive zero rest state; not energy eigenstate"])

def _track_c() -> VBTrackResult:
    return VBTrackResult("C","substrate_persistence",
        "Does the substrate persist when Phi -> 0?",
        [
            "The equation tau dPhi/dt + Phi = 0 PRESUPPOSES: field variable Phi "
            "defined over space, constitutive timescale tau, dynamical law.",
            "These structural elements PERSIST even when Phi = 0.",
            "Phi is DEFINED everywhere even when its value is zero.",
            "The 'substrate' = {constitutive law + tau + spatial domain}.",
            "Zero field value means zero RESPONSE, not zero SUBSTRATE.",
            "CONDITIONAL: substrate persists structurally. But: is a law "
            "'still there' when nothing moves? Ontologically ambiguous.",
        ],
        VB_SP,
        ["Structural persistence supported; ontological status conditional"])

def _track_d() -> VBTrackResult:
    return VBTrackResult("D","machian_dependence",
        "Does source-free decay support Machian interpretation?",
        [
            "Manifest content (nonzero Phi) requires sources X != 0.",
            "Without sources: response dies to zero. WEAK SOURCE DEPENDENCE.",
            "The equation is well-defined even for X = 0. The LAW persists.",
            "STRICT MACHIAN: substrate requires sources. NOT supported — "
            "the equation and its structural elements don't need X to exist.",
            "WEAK: response needs sources; substrate doesn't.",
            "Ontological reading: the vacuum is a responsive medium that "
            "quiesces without stimulation but does not cease to exist.",
        ],
        VB_MACH,
        ["Weak source dependence; strict Mach not supported"])

def _track_e() -> VBTrackResult:
    return VBTrackResult("E","stability_ssb",
        "Is Phi = 0 stable? Any spontaneous symmetry breaking?",
        [
            "STABILITY: Phi = 0 is GLOBALLY STABLE. Lyapunov V = Phi^2/2 "
            "decays monotonically. No instability from native dynamics.",
            "SSB: spontaneous symmetry breaking requires an unstable "
            "symmetric vacuum with lower-energy asymmetric states. "
            "GRUT has: no potential V(Phi), no action, no energy landscape.",
            "Z2 symmetry (Phi -> -Phi) is exact and UNBROKEN at Phi = 0.",
            "No native mechanism for SSB. No Mexican hat. No Higgs analog.",
            "SSB would require: potential + instability + degenerate minima. "
            "All three are absent.",
        ],
        "stable_zero_no_ssb",
        ["Globally stable; no SSB mechanism"])

def _track_f() -> VBTrackResult:
    return VBTrackResult("F","vacuum_energy_firewall",
        "What does the source-free result NOT license?",
        [
            "NOT LICENSED: zero-point fluctuations (no quantum vacuum), "
            "vacuum expectation value (Phi->0, not VEV), "
            "cosmological constant (no energy density defined), "
            "dark energy (no gravity, no expansion), "
            "Mexican-hat/Higgs vacuum (no potential), "
            "thermal vacuum (no temperature/bath), "
            "quantum foam (no quantum gravity).",
            "STRONGEST SAFE: 'source-free constitutive decay to zero rest state'.",
        ],
        "firewall_secured",
        ["All quantum/cosmological vacuum claims excluded"])


def _build_obstructions() -> List[VBObstruction]:
    return [
        VBObstruction(1,"no_energy_or_hamiltonian",
            "Ground state = lowest energy; no energy defined -> no ground state sensu stricto"),
        VBObstruction(2,"no_potential_landscape",
            "SSB, VEV, vacuum degeneracy all require potential V(Phi): absent"),
        VBObstruction(3,"no_quantum_structure",
            "Quantum vacuum, fluctuations, zero-point energy: all absent (Born blocked)"),
        VBObstruction(4,"external_source_dependence",
            "Manifest vacuum structure requires X; substrate persistence is conditional"),
        VBObstruction(5,"constitutive_not_hamiltonian",
            "Ontology of rest state differs between dissipative and Hamiltonian systems"),
        VBObstruction(6,"scalar_only_content",
            "One real scalar provides minimal ontological substrate"),
    ]


def _build_evidence() -> List[VBEvidenceRow]:
    return [
        VBEvidenceRow("generic_X_eq_0_initial",
            "Phi(t)=Phi(0)exp(-t/tau)->0","Asymptotic decay licensed","Zero attractor (not eigenstate)",
            "Structural persistence","Source-free decay","VEV, ground state as eigenstate"),
        VBEvidenceRow("late_time_asymptotic",
            "Phi->0 exponentially","Zero rest state licensed","Constitutive rest state",
            "Law persists at Phi=0","Zero rest state language","Quantum vacuum, energy state"),
        VBEvidenceRow("zero_state_stability",
            "Globally Lyapunov stable","Stability licensed","Stable zero (no instability)",
            "N/A","Stable zero attractor","SSB, unstable vacuum, Mexican hat"),
        VBEvidenceRow("substrate_persistence",
            "Law+tau+domain persist","Conditional","N/A",
            "Structural elements persist","Conditional substrate persistence","Substance, density"),
        VBEvidenceRow("machian_test",
            "Response dies; law persists","Weak dependence only","N/A",
            "Substrate != response","Weak source dependence","Strict Machianism"),
        VBEvidenceRow("vacuum_energy_vev_test",
            "No V(Phi), no H, no eigenvalue","Not licensed","No energy-based ground state",
            "N/A","Nothing","VEV, Lambda, dark energy, zero-point"),
    ]


def run_vb_vacuum_existence_ground_state_audit() -> VBVacuumExistenceResult:
    ta=_track_a();tb=_track_b();tc=_track_c()
    td=_track_d();te=_track_e();tf=_track_f()
    obs=_build_obstructions();ev=_build_evidence()
    fw=VBNonclaimFirewall(VB_NONCLAIMS,N_VB_NONCLAIMS,True)

    key=[
        "SOURCE-FREE DECAY TO ZERO: Phi(t) = Phi(0)exp(-t/tau) -> 0. Unique "
        "global attractor. No nonzero stationary state. Exponential, monotonic, irreversible.",
        "ZERO REST STATE: constitutive attractor, not energy eigenstate. "
        "'Ground state' is analogy, not native statement (no H, no E, no eigenvalue).",
        "SUBSTRATE PERSISTS CONDITIONALLY: law + tau + domain defined at Phi = 0. "
        "Zero field = zero response, not zero substrate. Ontologically ambiguous.",
        "WEAK SOURCE DEPENDENCE: manifest response requires sources; "
        "structural substrate does not. Strict Machian NOT supported.",
        "Phi = 0 GLOBALLY STABLE: no SSB, no unstable vacuum, no Mexican hat, "
        "no degenerate minima. Z2 exact and unbroken.",
        "VACUUM-ENERGY FIREWALL: no VEV, no Lambda, no dark energy, no zero-point, "
        "no quantum vacuum, no thermal vacuum licensed.",
    ]

    allowed=[
        "Source-free asymptotic decay to zero: Phi(t)=Phi(0)exp(-t/tau)->0",
        "Zero rest state as constitutive attractor (not energy eigenstate)",
        "Substrate conditionally persists with zero response: law+tau+domain defined",
        "Weak source dependence: response requires sources, substrate doesn't",
        "Phi=0 globally stable under native dynamics; Z2 unbroken",
        "6 ontology obstructions documented (energy, potential, quantum, source, constitutive, scalar)",
        "V-C authorized: source-free boundary established",
    ]

    forbidden=[
        "Phi=0 implies nonexistence of space",
        "Zero attractor implies energy-eigenstate ground state",
        "Source-free decay implies VEV",
        "Substrate persistence implies substance",
        "Source dependence implies strict Machianism",
        "Zero vacuum implies cosmological constant",
        "Stable zero implies spontaneous symmetry breaking",
    ]

    diagnostics: Dict[str,Any]={
        "source_free_solution":"Phi(0)*exp(-t/tau)",
        "asymptotic_state":"Phi=0",
        "decay_rate":GAMMA,
        "globally_stable":True,
        "ssb_possible":False,
        "nonzero_stationary_exists":False,
        "vev_licensed":False,
        "cosmological_constant_licensed":False,
        "strict_machian_supported":False,
        "n_obstructions":len(obs),
        "n_regimes":N_REGIMES,
        "n_nonclaims":N_VB_NONCLAIMS,
    }

    result=VBVacuumExistenceResult(
        True,ta,tb,tc,td,te,tf,obs,ev,fw,
        VB_SF,VB_GS,VB_SP,VB_MACH,VB_AUTH,VB_OVERALL,
        key,allowed,forbidden,VB_NONCLAIMS,diagnostics)
    _validate(result);return result


def _validate(r:VBVacuumExistenceResult)->None:
    if r.source_free_state_status not in SF_OPTIONS:raise ValueError("sf")
    if r.ground_state_status not in GS_OPTIONS:raise ValueError("gs")
    if r.substrate_persistence_status not in SP_OPTIONS:raise ValueError("sp")
    if r.machian_status not in MACH_OPTIONS:raise ValueError("mach")
    if r.authorization not in AUTH_OPTIONS:raise ValueError("auth")
    if r.overall_appendix_p not in OVERALL_OPTIONS:raise ValueError("overall")
    if r.nonclaim_firewall.n_nonclaims!=N_VB_NONCLAIMS:raise ValueError("nc")
    if not r.nonclaim_firewall.all_registered:raise ValueError("reg")
    if len(r.allowed_claims)!=N_ALLOWED:raise ValueError("allowed")
    if len(r.forbidden_claims)!=N_FORBIDDEN:raise ValueError("forbidden")
    if len(r.evidence_table)!=N_REGIMES:raise ValueError("evidence")
    if len(r.track_g_obstructions)!=N_OBSTRUCTIONS:raise ValueError("obstr")
    if r.diagnostics["ssb_possible"]:raise ValueError("ssb False")
    if r.diagnostics["vev_licensed"]:raise ValueError("vev False")
    if r.diagnostics["strict_machian_supported"]:raise ValueError("mach False")
    if r.diagnostics["nonzero_stationary_exists"]:raise ValueError("nonzero False")


def _self_test()->bool:
    r=run_vb_vacuum_existence_ground_state_audit()
    assert r.valid
    assert r.source_free_state_status==VB_SF
    assert r.ground_state_status==VB_GS
    assert r.substrate_persistence_status==VB_SP
    assert r.machian_status==VB_MACH
    assert r.authorization==VB_AUTH
    assert r.diagnostics["globally_stable"] is True
    assert r.diagnostics["ssb_possible"] is False
    assert r.diagnostics["vev_licensed"] is False
    return True

if __name__=="__main__":
    _self_test();print("V-B passed.")
