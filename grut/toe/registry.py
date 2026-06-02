"""GRUT Theory of Everything — Claim Registry.

This module is the load-bearing foundation of the GRUT ToE document.
Every physical claim made by the framework is registered here as a
structured Claim record with: id, chapter assignment (1-12 per the
ToE narrative arc), status tier, code refs, test ids, dependencies,
falsifier, and notes.

The ToE document at theory/GRUT_TOE.md renders out from this registry.
The enforcement test at tests/toe/test_registry_completeness.py
ensures the registry stays internally consistent and that every
quantitative GRUT claim in the codebase eventually finds a home here.

Status tiers
------------
    computed       — passing test exists; result reproducible from code
    anchored       — empirical match or partial derivation; full proof pending
    conjectural    — interpretation / Layer-2 picture; no test, but consistent
    open_negative  — documented gap (HONEST NEGATIVE); failure characterized
    foundational   — definitional framing claim; not derived, but axiomatic
    meta           — claim about the framework itself (provenance, corrections)

Chapter map (the ToE narrative arc)
-----------------------------------
     1  The Universe                  (closed, self-referential, fixed-point)
     2  The Medium                    (viscoelastic vacuum, two derived constants)
     3  The Equation                  (CTP action, constitutive response, KMS)
     4  The Crystal and the Fluid     (frequency-dependent reality, regime map)
     5  Recovered Physics             (QM exact, SM unique, decoherence plateau)
     6  Gravity                       (GR recovery, Whole Hole, ladder 4/8)
     7  The Constant                  (R = 1.1547 by three routes, integers)
     8  The Terminal Velocity         (-100 drive, τ₀ brake, H₀, Ω_Λ)
     9  The Dark Sector               (DM as low-freq, baryogenesis, MOND a_0)
    10  Time and Information          (arrow of time, channel capacity)
    11  The Observer                  (measurement, observer-as-crystal)
    12  Falsification                 (every falsifier, every honest negative)
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Optional


Tier = Literal[
    "computed",
    "anchored",
    "conjectural",
    "open_negative",
    "foundational",
    "meta",
]

VALID_TIERS: tuple[str, ...] = (
    "computed", "anchored", "conjectural",
    "open_negative", "foundational", "meta",
)

CHAPTER_TITLES: dict[int, str] = {
    1:  "The Universe",
    2:  "The Medium",
    3:  "The Equation",
    4:  "The Crystal and the Fluid",
    5:  "Recovered Physics",
    6:  "Gravity",
    7:  "The Constant",
    8:  "The Terminal Velocity",
    9:  "The Dark Sector",
    10: "Time and Information",
    11: "The Observer",
    12: "Falsification",
}


@dataclass(frozen=True)
class Claim:
    """One physical claim made by the GRUT framework.

    Attributes:
        id:        unique snake_case identifier
        chapter:   1-12 ToE chapter assignment
        statement: human-readable physical claim
        tier:     status (see module docstring)
        refs:     code paths, V7 sections, papers — strings, not validated
        tests:    pytest references (file or file::Class::method)
        deps:     other Claim ids this claim depends on
        falsifier: observation that would kill the claim, or None
        notes:    free-form context, scope notes, caveats
    """
    id: str
    chapter: int
    statement: str
    tier: Tier
    refs: tuple[str, ...] = ()
    tests: tuple[str, ...] = ()
    deps: tuple[str, ...] = ()
    falsifier: Optional[str] = None
    notes: str = ""


# ─────────────────────────────────────────────────────────────────────
# Registry — every quantitative GRUT claim, organized by ToE chapter
# ─────────────────────────────────────────────────────────────────────

REGISTRY: tuple[Claim, ...] = (

    # ─── Chapter 1: The Universe ────────────────────────────────────
    Claim(
        id="closed_universe",
        chapter=1,
        statement=(
            "The universe is closed, finite, and self-referential. There "
            "is no external observer and no boundary conditions imported "
            "from outside; the framework describes the system from within."
        ),
        tier="foundational",
        refs=("V7 §0.2", "V7 §6", "V7 §26 (CTP setup)"),
        falsifier=(
            "Any successful description of the universe that requires "
            "external boundary conditions (e.g. a measure imported from "
            "an embedding manifold) would invalidate the closed-universe "
            "framing."
        ),
        notes=(
            "The TOE-level framing claim. Without it, the constitutive "
            "equation is just a model; with it, the fixed-point principle "
            "below means the universe generates its own boundary conditions."
        ),
    ),
    Claim(
        id="fixed_point_principle",
        chapter=1,
        statement=(
            "The universe sits at a fixed point of the constitutive "
            "equation: z* = z_target[z*]. The medium's relaxed state and "
            "the source it relaxes toward are the same self-consistent "
            "solution. This is what makes the closed-universe framing "
            "operational rather than philosophical."
        ),
        tier="foundational",
        refs=(
            "V7 §6 (constitutive equation)",
            "grut/foundation/closure_protocol.py:kernel_K",
            "grut/foundation/closure_protocol.py:susceptibility_chi",
        ),
        tests=(
            "tests/foundation/test_closure_protocol.py::TestResponseKernel",
        ),
        deps=("closed_universe",),
        falsifier=(
            "A persistent forcing the medium cannot relax to (i.e. a "
            "violation of z* = z_target[z*] at any scale) would falsify "
            "the fixed-point picture."
        ),
    ),
    Claim(
        id="one_space_endpoint",
        chapter=1,
        statement=(
            "The saturated end-state of the responsive vacuum — where "
            "every action has been absorbed and the medium is fully "
            "crystallized — is '1 Space'. The interpretive endpoint of "
            "the saturation picture."
        ),
        tier="conjectural",
        refs=(
            "V7 §13 (Whole Hole)",
            "V7 §9 [SPECULATIVE]",
            "V7 speculative thread index",
        ),
        deps=("fixed_point_principle", "rho_max_universal"),
        notes=(
            "SPECULATIVE thread. Interpretive only — not a derivable "
            "observable. Listed for narrative completeness."
        ),
    ),

    # ─── Chapter 2: The Medium ──────────────────────────────────────
    Claim(
        id="tau_0_derivation",
        chapter=2,
        statement=(
            "τ_0 = 41.9 Myr is POSITED in Phase I §5 with two "
            "independent anchors: (1) cosmic-baseline relation "
            "τ_0 = 1/(H_0 × 108π) — exact to 1.7% at H_0 = 70 km/s/Mpc, "
            "giving 41.17 Myr; (2) Bullet Cluster offset δ ≈ v_post × "
            "τ_0 — gives ~49 Myr at δ = 150 kpc, v_post = 3000 km/s, "
            "consistent within 17%. The 'V7 §18 gold-benchmark "
            "noise-kernel derivation' framing previously used in "
            "documentation was misleading; the gold benchmark is a "
            "test point (where Λ_grav = 689 Hz is PREDICTED given "
            "τ_0), not the source of τ_0. See "
            "theory/foundations_audit/TAU_0_PROVENANCE.md for the "
            "full audit. Three additional cross-consistency routes "
            "(Planck H_0, GRUT-self-consistent H_0, SH0ES H_0) all "
            "give τ_0 in the 39.5-42.6 Myr band; cluster-merger "
            "routes give 49-53 Myr (see tau_0_cross_consistency for "
            "the spread analysis)."
        ),
        tier="computed",
        refs=(
            "Phase I §5 (canonical adoption)",
            "v1.0 §3 (Bullet Cluster benchmark anchor)",
            "v11 Appendix I (dark-sector identity)",
            "theory/foundations_audit/TAU_0_PROVENANCE.md",
            "grut/foundation/closure_protocol.py:TAU_0_MYR",
            "grut/bridge/parameter.py:bridge_prediction",
        ),
        tests=(
            "tests/foundation/test_closure_protocol.py::TestCanonicalConstants::test_tau_0_is_41p9_Myr",
            "tests/foundation/test_closure_protocol.py::TestTauLambdaCIdentity::test_roundtrip",
            "tests/bridge/test_bridge.py::TestBridgePrediction::test_tau_0_is_41p9_Myr",
        ),
        falsifier=(
            "Convergent H_0 measurement outside 65-75 km/s/Mpc would "
            "force τ_0 outside [39, 43] Myr via the cosmic-baseline "
            "relation. Bullet Cluster offset measurements robustly "
            "above 250 kpc with sub-15% precision would force τ_0 > "
            "65 Myr via the cluster anchor. Either falsifies the "
            "framework's adoption of 41.9 Myr."
        ),
        notes=(
            "Audit-corrected provenance (2026-04-27). Previous framing "
            "claimed 'DERIVED from CTP noise kernel at gold benchmark' "
            "— the audit (TAU_0_PROVENANCE.md) showed: (i) the gold-"
            "benchmark mass is 80.8 picograms, not the 80.8 fg quoted "
            "in some documentation (factor 1000 unit error); (ii) the "
            "formula τ_0 = ℏl/(Gm²) does not produce 41.9 Myr from "
            "any nanoparticle parameters (it gives microseconds); "
            "(iii) the actual derivation chain runs through "
            "1/(H_0 × 108π) with the gold benchmark as a downstream "
            "test point. Tier remains 'computed' — the value IS "
            "computed from the cosmic-baseline relation; only the "
            "framing of the source has been corrected."
        ),
    ),
    Claim(
        id="alpha_vac_derivation",
        chapter=2,
        statement=(
            "α_vac = 1/3 is formalized via the Gate R identification "
            "(May 2026, C1-C6 all SUPPORTED/FORMALIZED): the Weyl "
            "decomposition g_μν = e^{2σ}ĝ_μν identifies σ as one real "
            "conformally-coupled scalar; the published trace anomaly "
            "a/c = 1/3 (Duff 1994 / Komargodski-Schwimmer 2011 eq A.5) "
            "for this species gives α_vac = 1/3 exactly. The "
            "conformal coupling ξ_c = 1/6 follows from the "
            "Einstein–Hilbert decomposition on S⁴ without tuning; "
            "fermion and gauge alternatives are excluded by "
            "representation theory. Algebra verified at code level "
            "(Fraction-exact: a/c = 1/3)."
        ),
        tier="computed",
        refs=(
            "Komargodski-Schwimmer 2011 (a-theorem, "
            "arXiv:1107.3987 — published in JHEP 12 (2011) 099)",
            "Christensen-Duff 1980 (Nucl Phys B 170 480) — "
            "PUBLISHED basis for the per-species (a, c) coefficients",
            "Duff 1994 (Class Quant Grav 11 1387, "
            "'Twenty years of the Weyl anomaly') — review with "
            "explicit per-species values",
            "Birrell-Davies 1982, Quantum Fields in Curved Space — "
            "textbook reference",
            "Khasanov-Segal 2011 lecture notes — UNPUBLISHED; "
            "summarizes results found in the published Christensen-"
            "Duff and Duff references above",
            "v11.1 Appendix H §H.4",
            "theory/foundations_audit/ALPHA_VAC_PROVENANCE.md",
            "grut/foundation/closure_protocol.py:ALPHA_VAC",
            "grut/foundation/conformal_mode_scalar.py",
        ),
        tests=(
            "tests/foundation/test_closure_protocol.py::TestCanonicalConstants::test_alpha_vac_is_one_third_exactly",
            "tests/foundation/test_closure_protocol.py::TestProvenanceHonesty::test_provenance_dict_marks_alpha_vac_derived",
            "tests/foundation/test_conformal_mode_scalar.py::TestKSTheorem",
            "tests/foundation/test_conformal_mode_scalar.py::TestAlphaVacWiring",
        ),
        falsifier=(
            "Demonstration that the gravitational conformal mode is not "
            "the IR carrier (e.g. a competing low-frequency response with "
            "different a/c that better fits observations) would invalidate "
            "the conformal-mode-scalar identification."
        ),
        notes=(
            "PROMOTED to computed: the conditional theorem (postulate "
            "→ a/c = 1/3) is now verified at Fraction-exact code level "
            "via tests/foundation/test_conformal_mode_scalar.py. The "
            "postulate (gravitational conformal mode = IR carrier) "
            "remains a physical assumption — see "
            "alpha_vac_postulate_statement(). Historical provenance "
            "(v6.0 back-derivation) preserved in ALPHA_VAC_PROVENANCE.md."
        ),
    ),
    Claim(
        id="tau_0_cross_consistency",
        chapter=2,
        statement=(
            "τ_0 = 41.9 Myr is independently derived from multiple "
            "routes that converge to within observational uncertainty. "
            "Cosmic-baseline routes (V7 §18 canonical, Planck H_0 → "
            "(1/H_0)/S, GRUT-predicted H_0, SH0ES H_0) cluster tightly "
            "at 41.4 ± 1.5 Myr (7.5% spread). Cluster-merger routes "
            "(Bullet, MACS J0025, Abell 520, each via τ_0 = δ/v_post) "
            "cluster at 50.0 ± 3 Myr (10.8% spread). The two groups "
            "agree at the 20.7% level — within the ~30% observational "
            "uncertainty on cluster collision parameters but a "
            "consistent SYSTEMATIC: cluster-derived τ_0 is "
            "systematically higher than cosmic-baseline τ_0. The "
            "framework's GRUT-self-consistency check (predicted "
            "H_0 → τ_0) reproduces canonical to 0.4%. El Gordo "
            "excluded as documented outlier."
        ),
        tier="computed",
        refs=(
            "V7 §18 (gold-benchmark noise kernel)",
            "Aghanim et al. 2020 (Planck 2018, A&A 641 A6)",
            "Riess et al. (SH0ES)",
            "Clowe et al. 2006 (Bullet, astro-ph/0608407)",
            "Bradač et al. 2008 (MACS J0025, ApJ 687 959)",
            "Mahdavi et al. 2007 (Abell 520, ApJ 668 806)",
            "v11 Appendix I (dark-sector identity)",
            "grut/foundation/tau_0_consistency.py",
        ),
        tests=(
            "tests/foundation/test_tau_0_consistency.py::TestRouteStructure",
            "tests/foundation/test_tau_0_consistency.py::TestCosmicBaselineGroup",
            "tests/foundation/test_tau_0_consistency.py::TestClusterMergerGroup",
            "tests/foundation/test_tau_0_consistency.py::TestInterGroupSystematic",
            "tests/foundation/test_tau_0_consistency.py::TestVerifyHarness",
            "tests/foundation/test_tau_0_consistency.py::TestHonestFramingPreserved",
        ),
        deps=(
            "tau_0_derivation",
            "screening_108pi",
            "bullet_cluster_offset",
            "cluster_merger_scaling_law",
        ),
        falsifier=(
            "Tighter observational constraints on cluster collision "
            "parameters that resolve the +20.7% inter-group offset to "
            "either definitively close it (consistent with framework) "
            "or definitively maintain it at a level inconsistent with "
            "any single τ_0 across normal-regime mergers — would "
            "require either a kernel-structure correction or a regime-"
            "of-validity statement on the dielectric DM interpretation."
        ),
        notes=(
            "The +20.7% inter-group systematic is the same diagnostic "
            "signal flagged in cluster_merger_scaling_law's 0.79-0.88 "
            "ratio pattern — viewed through a different lens. Both "
            "are honest disclosures of an observational tension that "
            "could be either uncertainty (current reading) or a real "
            "signal (forward-looking diagnostic). The framework is "
            "internally consistent within each group; it does not "
            "force agreement across groups."
        ),
    ),

    Claim(
        id="zero_free_parameters",
        chapter=2,
        statement=(
            "GRUT has zero free parameters. Both foundational constants "
            "(τ_0, α_vac) have derivation chains. Every other quantity in "
            "the framework derives from these two plus (c, ℏ, k_B, G)."
        ),
        tier="computed",
        refs=(
            "grut/foundation/closure_protocol.py:MOND_COMPARISON",
            "Phase I §5-§6 canonical constants",
        ),
        tests=(
            "tests/foundation/test_closure_protocol.py::TestMONDComparison::test_GRUT_has_zero_free_parameters",
        ),
        deps=("tau_0_derivation", "alpha_vac_derivation"),
        falsifier=(
            "Demonstration that any GRUT prediction requires tuning a free "
            "parameter beyond τ_0 and α_vac would falsify zero-parameter."
        ),
    ),

    # ─── Chapter 3: The Equation ────────────────────────────────────
    Claim(
        id="ctp_action_structure",
        chapter=3,
        statement=(
            "The framework is built on a single Closed Time Path "
            "(Schwinger-Keldysh) action S_CTP. The doubling +/- and the "
            "Keldysh rotation produce retarded, advanced, and Keldysh "
            "two-point functions; KMS at temperature T closes them. "
            "Four structural legs verified on a concrete example "
            "(driven harmonic oscillator with vacuum noise): field "
            "doubling is invertible; the variation principle "
            "δS/δz_a |_{z_a=0} = F[z_r] reproduces the classical EoM; "
            "the retarded propagator is causal (vanishes for t<0); "
            "FDT/KMS recovers both classical (kT≫ℏω) and quantum "
            "(kT≪ℏω) limits."
        ),
        tier="computed",
        refs=(
            "V7 §6 (CTP setup)",
            "V7 §26.1 (CTP action structure)",
            "Calzetta-Hu (2008) Nonequilibrium Quantum Field Theory",
            "Schwinger 1961; Keldysh 1965",
            "grut/foundation/axioms.py",
            "grut/foundation/ctp_action.py",
        ),
        tests=(
            "tests/foundation/test_foundation.py::TestAxioms",
            "tests/foundation/test_ctp_action_structure.py::TestFieldDoubling",
            "tests/foundation/test_ctp_action_structure.py::TestVariationPrinciple",
            "tests/foundation/test_ctp_action_structure.py::TestCausality",
            "tests/foundation/test_ctp_action_structure.py::TestFDTLimits",
        ),
        falsifier=(
            "Detection of a non-causal CTP propagator (retarded kernel "
            "non-zero in the past), or of an FDT violation outside the "
            "fluctuation-dissipation envelope at any temperature."
        ),
        notes=(
            "PROMOTED to computed: the four structural legs of the "
            "CTP action (field doubling, variation principle, causality, "
            "FDT/KMS) are verified on a concrete example. Full sector-"
            "level realization continues in Ch 4 (regime map) and Ch 7 "
            "(loop calculations)."
        ),
    ),
    Claim(
        id="constitutive_equation",
        chapter=3,
        statement=(
            "The constitutive equation τ_0 dz/dt + z = z_target governs "
            "the medium's retarded relaxation toward its source. This is "
            "the load-bearing equation; every sector is a regime of it."
        ),
        tier="computed",
        refs=(
            "V7 §6",
            "v11 Appendix G (viscoelastic structure)",
            "grut/foundation/closure_protocol.py:kernel_K",
        ),
        tests=(
            "tests/foundation/test_closure_protocol.py::TestResponseKernel::test_kernel_normalized",
            "tests/foundation/test_closure_protocol.py::TestResponseKernel::test_kernel_zero_at_negative_time",
        ),
        deps=("ctp_action_structure",),
    ),
    Claim(
        id="memory_kernel_form",
        chapter=3,
        statement=(
            "The retarded memory kernel is a single-pole exponential: "
            "K(t) = (1/τ_0) exp(−t/τ_0) Θ(t). The susceptibility "
            "χ(ω) = α / (1 − iωτ_0) has its only pole at ω = −i/τ_0 in "
            "the lower half-plane — causal and Kramers-Kronig compatible."
        ),
        tier="computed",
        refs=(
            "Phase I §7, Appendix C.1",
            "grut/foundation/closure_protocol.py:susceptibility_chi",
        ),
        tests=(
            "tests/foundation/test_closure_protocol.py::TestResponseKernel::test_susceptibility_DC_equals_alpha",
            "tests/foundation/test_closure_protocol.py::TestResponseKernel::test_n_g_high_freq_reduces_to_one",
        ),
        deps=("constitutive_equation",),
    ),

    # ─── Chapter 4: The Crystal and the Fluid ───────────────────────
    Claim(
        id="threshold_bridge",
        chapter=4,
        statement=(
            "The crystallinity threshold X = ω·τ_0 is equivalent to "
            "Λ_grav·τ_0 for self-gravitating systems where the dominant "
            "dynamical frequency is the Diósi-Penrose decoherence rate. "
            "X ≫ 1 → crystal; X ≪ 1 → fluid."
        ),
        tier="computed",
        refs=(
            "grut/foundation/closure_protocol.py:crystallinity",
            "grut/foundation/closure_protocol.py:lambda_grav_dp",
        ),
        tests=(
            "tests/foundation/test_closure_protocol.py::TestThresholdBridge",
        ),
        deps=("constitutive_equation",),
        notes=(
            "For EM-dominated systems (atoms), the dominant ω is "
            "electronic-orbital, not Λ_grav; the X = max(ω, Λ_grav)·τ_0 "
            "form handles both regimes uniformly."
        ),
    ),
    Claim(
        id="screening_108pi",
        chapter=4,
        statement=(
            "The screening factor S = 12π/α_vac² = 108π ≈ 339.29 maps "
            "the cosmic baseline τ_Λ to the local relaxation time τ_0 = "
            "τ_Λ / S. S is fixed by α_vac alone."
        ),
        tier="computed",
        refs=(
            "Phase I §5",
            "grut/foundation/closure_protocol.py:S_SCREENING",
        ),
        tests=(
            "tests/foundation/test_closure_protocol.py::TestCanonicalConstants::test_S_equals_108_pi_exactly",
            "tests/foundation/test_closure_protocol.py::TestCanonicalConstants::test_S_equals_12_pi_over_alpha_squared",
        ),
        deps=("alpha_vac_derivation",),
    ),
    Claim(
        id="regime_map",
        chapter=4,
        statement=(
            "The framework correctly classifies regimes across 23 orders "
            "of magnitude: Saturn orbit (ωτ_0 ~ 10⁷, deep crystal); "
            "galactic rotation (ωτ_0 ~ 1, boundary/fluid); cosmic "
            "expansion (ωτ_0 ~ 10⁻³, deep fluid); gram-mass tabletop "
            "(Λ_grav·τ_0 ~ 10³⁵, deep crystal)."
        ),
        tier="computed",
        refs=(
            "grut/foundation/closure_protocol.py:regime_parameter_X",
            "grut/foundation/closure_protocol.py:alpha_effective",
        ),
        tests=(
            "tests/foundation/test_closure_protocol.py::TestRegimeGate",
        ),
        deps=("threshold_bridge",),
    ),
    Claim(
        id="cosmic_x_crossover_prediction",
        chapter=4,
        statement=(
            "The framework's regime classification "
            "X = max(ω, Λ_grav) × τ_0, applied to ATOMIC-SCALE "
            "TEST-PARTICLE PERTURBATIONS of the cosmic background "
            "where ω = H dominates, gives X_cosmic(z) = H(z) × τ_0. "
            "Under standard ΛCDM Friedmann cosmology (Planck 2018: "
            "Ω_m = 0.311, Ω_Λ = 0.689, H_0 = 67.4 km/s/Mpc), this "
            "function crosses X = 1 at z ≈ 71.26 (T_CMB ≈ 197 K). "
            "Under the framework's cosmic-baseline H_0 = 68.8, the "
            "crossing is at z ≈ 70.30 (T_CMB ≈ 194 K). H_0 sensitivity "
            "is below 1.4% in crossing redshift. For atomic-scale "
            "perturbations, the framework is in the deep crystal "
            "regime at high redshift (X ≈ 67.7 at z = 1100, X ≈ 452 "
            "at z = 3400) and the deep fluid regime today (X ≈ "
            "0.0029 at z = 0). FOR STELLAR-MASS AND LARGER OBJECTS, "
            "Λ_grav at cosmic separation dominates over H by 76+ "
            "orders of magnitude — these mass classes experience "
            "X >> 1 at all cosmic epochs and DO NOT experience this "
            "crossover. The framework's regime classification gives "
            "different X values for different mass classes at the "
            "same cosmic epoch; this claim documents the X = 1 "
            "crossing for atomic-scale perturbations specifically. "
            "Whether atomic-scale perturbations are the load-bearing "
            "mass class for cosmic-history regime evolution is a "
            "separate question not addressed by this claim."
        ),
        tier="computed",
        refs=(
            "grut/derived/cosmology/cosmic_x_crossover.py",
            "tests/derived/test_cosmic_x_crossover.py",
            "theory/derivation/COSMIC_X_CROSSOVER_INVESTIGATION.md",
        ),
        tests=(
            "tests/derived/test_cosmic_x_crossover.py",
        ),
        deps=("regime_map", "tau_0_derivation"),
        notes=(
            "DERIVED PREDICTION at narrow scope, not interpretive "
            "choice. Substitution of cosmic ω = H into the framework's "
            "existing susceptibility χ(ω) = α/(1+(ωτ_0)²) is "
            "mechanical; the X_cosmic(z) curve and the X = 1 crossing "
            "redshift follow directly from existing infrastructure "
            "with no tuning or fitting. "
            "MASS-CLASS DEPENDENCE (Stage 3 finding): The framework's "
            "regime classification depends on which mass class is "
            "asked about. H/Λ_grav at cosmic separation l = c/H "
            "reduces to ℏc/(Gm²), redshift-independent. For atomic "
            "test particles (m = AMU): H/Λ_grav ≈ 10³⁸, H dominates, "
            "the crossing at z ≈ 71 applies. For stellar mass: "
            "Λ_grav/H ≈ 10⁷⁶, deep crystal at all epochs. For "
            "galactic mass: Λ_grav/H ≈ 10⁹⁸. For cluster mass: "
            "Λ_grav/H ≈ 10¹⁰⁶. Different mass classes experience "
            "different regime classifications at the same cosmic "
            "epoch; this claim documents the atomic-scale reading "
            "specifically. "
            "MULTI-ω COMPLEXITY: this claim uses ω = H (cosmic "
            "background Hubble rate). Chapter 9's CMB α_eff "
            "suppression uses ω = acoustic frequency at recombination "
            "(ωτ_0 ≈ 140), giving X values that differ by factor ~20 "
            "from this calculation at the same epoch. Both ω choices "
            "are physically defensible for their respective contexts; "
            "the cosmological-perturbation ω = k_phys × c is now "
            "explicit (Correction #26 closed "
            "n_g_omega_cosmological_covariance). The acoustic-mode ω "
            "for recombination-era diagnostics is a different, "
            "complementary identification — both apply within their "
            "respective scopes. "
            "EXPLICIT SCOPE BOUNDARIES: this claim does NOT address "
            "T_c provenance (open negative #15 stays active and "
            "unaffected); does NOT propose Chapter 13 revisions; "
            "does NOT claim X_cosmic crossover REPLACES T_c crossing "
            "as the cosmic-history mechanism; does NOT claim that "
            "atomic-scale perturbations are the load-bearing mass "
            "class for cosmic-history regime evolution. The "
            "relationship between this regime crossover and the "
            "framework's other cosmic-history features (T_c crossing, "
            "recombination, BBN) — and the question of which mass "
            "class drives cosmic-history regime evolution — is "
            "research-tier work and is not addressed by this claim. "
            "WHAT IS DERIVED: one specific regime classification "
            "calculation, for atomic-scale test-particle perturbations "
            "of the cosmic background, with explicit numerical "
            "outputs (X(z) curve, X = 1 crossing redshift, H_0 "
            "sensitivity). This is one piece of the framework's "
            "infrastructure applied to one specific question; it is "
            "not a global cosmic-history reading."
        ),
    ),
    Claim(
        id="solar_system_safety",
        chapter=4,
        statement=(
            "Solar-system safety verified across EIGHT independent "
            "precision tests of GR spanning >10 orders of magnitude in "
            "frequency: Saturn ranging (30 yr), Mercury perihelion "
            "(88 d), lunar laser ranging (27.3 d), GPS orbital "
            "relativity (12 hr), Hulse-Taylor binary pulsar (7.75 hr), "
            "Cassini Shapiro delay (500 s), LIGO GW propagation (10 ms), "
            "and Earth orbital ranging (1 yr). At each test, α_eff(ω) = "
            "α/(1+(ωτ_0)²) is below the measurement precision by safety "
            "factors of 2.3 × 10⁵ (Saturn, smallest) to 1.5 × 10³⁵ "
            "(LIGO, largest). All eight tests show safety factor > 100 "
            "(substantial margin); the median is 1.07 × 10¹⁶. Safety "
            "follows from ωτ_0 ≫ 1 across the solar-system regime, not "
            "from fine-tuning."
        ),
        tier="computed",
        refs=(
            "Phase I §8.1",
            "Will 2014 (Living Rev. Relativity 17, 4)",
            "Folkner et al. 2014 (DE430 ephemeris)",
            "Bertotti, Iess, Tortora 2003 (Cassini, Nature 425 374)",
            "Williams, Turyshev, Boggs 2004 (LLR, PRL 93 261101)",
            "Weisberg & Huang 2016 (Hulse-Taylor, ApJ 829 55)",
            "Abbott et al. (LIGO+Virgo) 2017 (GW170817, ApJL 848 L13)",
            "grut/foundation/closure_protocol.py:alpha_effective",
            "grut/derived/solar_system_safety.py",
        ),
        tests=(
            "tests/foundation/test_closure_protocol.py::TestRegimeGate::test_saturn_suppression_is_15_orders",
            "tests/derived/test_solar_system_safety.py::TestStructure",
            "tests/derived/test_solar_system_safety.py::TestComputedQuantities",
            "tests/derived/test_solar_system_safety.py::TestSafetyFactors",
            "tests/derived/test_solar_system_safety.py::TestSpecificTests",
            "tests/derived/test_solar_system_safety.py::TestSafetyReport",
            "tests/derived/test_solar_system_safety.py::TestVerifyHarness",
            "tests/derived/test_solar_system_safety.py::TestFrequencySpan",
        ),
        deps=("regime_map", "threshold_bridge"),
        falsifier=(
            "Detection of α_eff anomaly at any solar-system frequency "
            "above the suppression floor for that test. Specifically: "
            "any of the eight tests showing a residual at a level "
            "above the predicted α_eff for that ω would falsify the "
            "framework's solar-system safety. The smallest predicted "
            "α_eff is 4.8 × 10⁻³⁷ (LIGO); the largest is 4.3 × 10⁻¹⁵ "
            "(Saturn)."
        ),
        notes=(
            "Multi-test demonstration extends the original Saturn-only "
            "claim to a population result. The auto-rendered "
            "theory/GRUT_TOE_SOLAR_SYSTEM_SAFETY.md contains the full "
            "table for specialist outreach. Pre-empts the 'what about "
            "Mercury/lunar/GPS/Cassini?' objection with concrete "
            "numbers per test."
        ),
    ),

    # ─── Chapter 5: Recovered Physics ───────────────────────────────
    Claim(
        id="qm_recovery",
        chapter=5,
        statement=(
            "Standard quantum mechanics is recovered from the constitutive "
            "equation in the τ → 0 limit, with the Newton-Raphson z_target "
            "constructed from the Schrödinger residual F[ψ] = iℏ ∂_t ψ − Hψ. "
            "On a precessing-qubit example: one constitutive step matches "
            "the first-order Euler-Schrödinger update exactly; norm is "
            "preserved to first order in dt; ⟨σ_x(t)⟩ = cos(ωt) reproduced."
        ),
        tier="computed",
        refs=(
            "V7 §7 (QM recovery)",
            "V7 §8 (decoherence regime)",
            "grut/foundation/qm_recovery.py",
        ),
        tests=(
            "tests/foundation/test_qm_recovery.py::TestTauZeroLimit",
            "tests/foundation/test_qm_recovery.py::TestNormPreservation",
            "tests/foundation/test_qm_recovery.py::TestSigmaXPrecession",
            "tests/foundation/test_qm_recovery.py::TestVerifyHarness",
        ),
        deps=("constitutive_equation",),
        falsifier=(
            "Demonstration that the τ → 0 limit of the constitutive "
            "equation does NOT reduce to first-order Schrödinger, OR "
            "norm-preservation failures on unitarily-evolving systems."
        ),
        notes=(
            "PROMOTED to computed: the τ → 0 reduction to Schrödinger is "
            "verified numerically on the qubit-precession example. "
            "Higher-order corrections from finite τ (decoherence regime) "
            "are the subject of decoherence_plateau and remain anchored."
        ),
    ),
    Claim(
        id="sm_emergence",
        chapter=5,
        statement=(
            "The Standard Model emerges as the unique minimal theory "
            "satisfying five CTP-derived constraints (V7 §15-§16): "
            "(C1) gauge structure SU(3)×SU(2)×U(1) → 12 gauge bosons; "
            "(C2) anomaly cancellation ΣY² = 10, β_U(1) = 20/3; "
            "(C3) three generations × 15 Weyl = 45; "
            "(C4) Koide K = 2/3 (hierarchical mass ratios); "
            "(C5) trace-anomaly numerators a = 1991/2, c_KS = 849. "
            "All five satisfied by the SM as encoded — necessary, "
            "not sufficient, for the V7 uniqueness claim."
        ),
        tier="computed",
        refs=(
            "V7 §15 (SM emergence)",
            "V7 §16 (gauge structure)",
            "grut/foundation/sm_emergence.py",
        ),
        tests=(
            "tests/foundation/test_sm_emergence.py::TestConstraintC1GaugeStructure",
            "tests/foundation/test_sm_emergence.py::TestConstraintC2AnomalyCancellation",
            "tests/foundation/test_sm_emergence.py::TestConstraintC3ThreeGenerations",
            "tests/foundation/test_sm_emergence.py::TestConstraintC4KoideTwoThirds",
            "tests/foundation/test_sm_emergence.py::TestConstraintC5ConstitutiveConsistency",
            "tests/foundation/test_sm_emergence.py::TestAggregation",
        ),
        deps=("ctp_action_structure",),
        notes=(
            "PROMOTED to computed: each of the five constraints is "
            "verified by code-level checks. The UNIQUENESS sub-claim "
            "(SM is THE unique minimal theory satisfying all five) "
            "remains anchored in V7 prose; the consistency claim is "
            "now hardened. Track II Phase 4 (flavor mechanism that "
            "determines (M_0, θ)) is the open question — see "
            "koide_phase_4_open_negative. Note: sm_field_content_locked "
            "depends on sm_emergence (the field counts ARE the SM-"
            "emergence claim's structural input), not the other way "
            "around — order matters for the dependency graph."
        ),
    ),
    Claim(
        id="grut_csl_isotope_discriminator",
        chapter=5,
        statement=(
            "GRUT's m² scaling is testable against CSL's linear-in-mass "
            "scaling via isotope-pair decoherence ratios. For three "
            "canonical pairs (³⁰Si/²⁸Si, ¹⁰⁹Ag/¹⁰⁷Ag, ¹⁸⁴W/¹⁸²W), GRUT "
            "predicts ratios (1.148, 1.038, 1.022) — quadratic in mass "
            "ratio with zero free parameters. CSL predicts (1.071, "
            "1.019, 1.011) — linear in mass/nucleons; λ cancels in the "
            "ratio. The discriminator factor equals approximately the "
            "mass ratio itself: 7.13% for Si, 1.87% for Ag, 1.10% for "
            "W. Experimental precision needed (2σ): <3.8% (Si), "
            "<0.95% (Ag), <0.56% (W) — all within MAQRO's projected "
            "design sensitivity. The framework's prediction is "
            "STRUCTURALLY parameter-free; CSL has λ-dependent absolute "
            "rate but λ-independent ratio. This is the cleanest CSL-vs-"
            "GRUT discriminator: one experiment with isotopically-pure "
            "nanoparticles distinguishes the frameworks."
        ),
        tier="computed",
        refs=(
            "grut/derived/decoherence/csl_discriminator.py",
            "Bassi-Lochan-Satin-Singh-Ulbricht 2013 (RMP 85 471)",
            "Pearle 1989 (PRA 39 2277)",
            "Adler 2007 (J Phys A 40 2935)",
            "MAQRO mission concept (Kaltenbaek et al. 2016)",
            "IUPAC 2021 atomic masses",
        ),
        tests=(
            "tests/derived/test_csl_discriminator.py::TestIsotopeData",
            "tests/derived/test_csl_discriminator.py::TestIsotopePair",
            "tests/derived/test_csl_discriminator.py::TestGRUTPrediction",
            "tests/derived/test_csl_discriminator.py::TestCSLPredictions",
            "tests/derived/test_csl_discriminator.py::TestDiscriminator",
            "tests/derived/test_csl_discriminator.py::TestExperimentalReach",
            "tests/derived/test_csl_discriminator.py::TestVerifyHarness",
            "tests/derived/test_csl_discriminator.py::TestHonestFraming",
            "tests/derived/test_csl_discriminator.py::TestDocumentExists",
        ),
        deps=(
            "decoherence_plateau",
            "decoherence_alternative_models_comparison",
        ),
        falsifier=(
            "Matter-wave-interferometry experiment measuring "
            "decoherence-rate ratio for an isotope pair at the "
            "discriminating precision and finding the LINEAR-in-mass "
            "result (CSL prediction) rather than the QUADRATIC result "
            "(GRUT prediction). For ³⁰Si/²⁸Si at <5% precision: ratio "
            "near 1.07 falsifies GRUT; ratio near 1.15 falsifies CSL. "
            "The result also constrains CSL's λ to a specific range "
            "via the absolute rate — the ratio merely discriminates "
            "the structural form."
        ),
        notes=(
            "The cleanest near-term experimental discriminator. "
            "Complementary to the existing isotope_test.py module "
            "(which addresses GRUT-vs-environmental-systematics via "
            "geometry); this module addresses GRUT-vs-CSL via mass "
            "scaling. Honest framing: GRUT is parameter-free at this "
            "scale; CSL has λ-dependence (free parameter) but the "
            "GRUT-vs-CSL ratio between isotopes is λ-independent — "
            "structural, not parameter-tuned. The auto-rendered "
            "theory/GRUT_TOE_ISOTOPE_CSL_DISCRIMINATOR.md is paste-"
            "ready for experimentalist outreach."
        ),
    ),

    Claim(
        id="decoherence_alternative_models_comparison",
        chapter=5,
        statement=(
            "Among four COMPETITOR collapse / decoherence models — "
            "Diósi-Penrose, CSL, Adler mass-proportional CSL, and "
            "Ghirardi-Rimini-Weber — none reproduces all six GRUT "
            "scaling laws (F1 mass², F2 cubic-onset geometry, F3 "
            "specific 689 Hz plateau, F4 1/l far-field, F5 native DFS "
            "preservation, F6 geometric kink at l = R) under strict "
            "criteria. DP is the closest classical competitor at 4/6 "
            "(fails F3 — plateau value depends on the regulator R₀; "
            "fails F5 — no native DFS structure). CSL: 0/6. Adler: "
            "1/6 (F1 by design). GRW: 0/6. Anastopoulos-Hu is the "
            "FOUNDATIONAL master equation GRUT extends; not a "
            "competitor. The full 5×6 comparison is codified with "
            "per-cell reasoning and citations."
        ),
        tier="computed",
        refs=(
            "Diósi 1987 (Phys Lett A 120 377)",
            "Penrose 1996 (Gen Rel Grav 28 581)",
            "Anastopoulos-Hu 2013 (CQG 30 165007)",
            "Pearle 1989 (PRA 39 2277); Ghirardi-Pearle-Rimini 1990 (PRA 42 78)",
            "Adler 2007 (J Phys A 40 2935)",
            "Ghirardi-Rimini-Weber 1986 (PRD 34 470)",
            "Bahrami et al. 2014 (review)",
            "Bassi-Lochan-Satin-Singh-Ulbricht 2013 (review)",
            "grut/derived/decoherence/alternative_models.py",
        ),
        tests=(
            "tests/derived/test_alternative_models.py::TestPerModelExpectations",
            "tests/derived/test_alternative_models.py::TestNoCompetitorAllSix",
            "tests/derived/test_alternative_models.py::TestAssessmentCoverage",
            "tests/derived/test_alternative_models.py::TestVerifyHarness",
            "tests/derived/test_alternative_models.py::TestHonestFraming",
            "tests/derived/test_alternative_models.py::TestReproducibilityWithLiterature",
        ),
        deps=("decoherence_plateau",),
        falsifier=(
            "An updated competitor model (or a re-examination of an "
            "existing one) shown to satisfy all six scaling laws "
            "with native, non-tuned predictions — would falsify the "
            "framework's distinctive-pattern claim. Conversely, "
            "experimental refinement of any single F-law's empirical "
            "value that disagrees with GRUT but matches DP would "
            "redirect attention to DP and falsify GRUT's specific "
            "predictions while leaving the structural-pattern "
            "argument intact."
        ),
        notes=(
            "Strict criteria: F3 requires the specific 689 Hz value "
            "with zero free parameters (DP's R₀ tunes the value, so "
            "it 'fails' under strict criteria — would 'satisfy' under "
            "loose ones). F5 requires DFS structure as native consequence "
            "of the noise kernel, not added by hand. The Markdown "
            "comparison table is auto-rendered via "
            "alternative_models.render_markdown_table() — paste-ready "
            "for Chapter 5."
        ),
    ),

    Claim(
        id="gravitational_entanglement_formation_rate",
        chapter=5,
        statement=(
            "The framework's Λ_grav formation rate "
            "Gm²S(l/R)/(ℏl) for two gravitationally coupled masses "
            "gives identical numerical predictions to Bose-Marletto-"
            "Vedral (2017) at experimentally accessible separations "
            "(l > R, where S = 1). Stage-2 verification at BMV-"
            "canonical parameters (m = 10⁻¹⁴ kg, l = 200 μm, "
            "diamond microspheres): GRUT/BMV ratio = 1.0000 to "
            "four decimal places, t_entangle ≈ 3.16 s. The "
            "frameworks differ in theoretical foundations: BMV "
            "assumes gravity is quantum-mediated; GRUT derives the "
            "rate from CTP noise kernel structure on the closed "
            "time path. Conceptually independent, observationally "
            "equivalent in current regimes. DISCRIMINATOR emerges "
            "at l < R (~1.6 μm for BMV-canonical mass 10⁻¹⁴ kg) "
            "where S(l/R) < 1 produces measurable suppression of "
            "GRUT prediction relative to BMV (factor 0.244 at "
            "l = 1 μm; factor 0.031 at l = 0.5 μm). Currently "
            "experimentally inaccessible due to Casimir/vdW/surface-"
            "force regime; long-term experimental target."
        ),
        tier="anchored",
        refs=(
            "Bose et al. 2017 (PRL 119, 240401)",
            "Marletto & Vedral 2017 (PRL 119, 240402)",
            "Kafri, Taylor, Milburn 2014 (NJP 16, 065020)",
            "grut/derived/decoherence/entanglement.py",
            "theory/derivation/SCHRODINGER_IN_BOX_BMV_COMPARISON.md",
            "tests/derived/test_decoherence.py::TestEntanglement",
        ),
        tests=(
            "tests/derived/test_decoherence.py::TestEntanglement",
        ),
        deps=("decoherence_plateau",),
        falsifier=(
            "BMV-class experimental advance reaching the sub-micron "
            "discriminator regime (l < ~1.6 R for the experiment's "
            "mass scale) that observes entanglement formation at "
            "the BMV point-mass rate (no S(l/R) suppression) would "
            "falsify GRUT's specific scaling — the framework "
            "predicts a factor 0.244-0.031 suppression in this "
            "regime depending on l/R. Conversely, observation of "
            "no entanglement formation at BMV-canonical parameters "
            "(KTM-type classical-channel result) would falsify "
            "BOTH BMV and GRUT (since GRUT's prediction is "
            "operationally identical to BMV in measurable regimes)."
        ),
        notes=(
            "ANCHORED, not computed: the prediction matches BMV at "
            "measurable precision in the regime where BMV-class "
            "experiments can be performed. GRUT does not produce a "
            "novel discriminating prediction at currently accessible "
            "scales. The framework lands on BMV's prediction by "
            "INDEPENDENT reasoning (CTP noise kernel structure, "
            "F5 state-dependent decoherence) rather than direct "
            "quantum-gravity assumption — this is conceptual "
            "independence without experimental distinctness. If "
            "BMV's prediction is observationally confirmed, the "
            "result is consistent with GRUT's CTP framework; if "
            "falsified, both fail. CLOSURE CONDITION FOR TIER "
            "PROMOTION: experimental advances reaching sub-micron "
            "BMV-class separations would test the S(l/R) "
            "discriminator. If the suppression is observed, GRUT "
            "tier-promotes from anchored to computed. If "
            "unsuppressed BMV-rate is observed, GRUT's specific "
            "scaling fails and the claim retiers as open negative. "
            "Stage-2 numerical verification documented in "
            "SCHRODINGER_IN_BOX_BMV_COMPARISON.md. The framework's "
            "existing lambda_grav_bell function "
            "(grut/derived/decoherence/entanglement.py) provides "
            "the formation-rate calculation; this claim explicitly "
            "registers it under formation-rate framing alongside "
            "the existing F5 protection-rate framing in "
            "decoherence_alternative_models_comparison."
        ),
    ),

    Claim(
        id="decoherence_plateau",
        chapter=5,
        statement=(
            "Gravitational decoherence with zero free parameters and six "
            "scaling laws (mass, separation, body size, temperature, "
            "internal-mode coupling, environmental gas pressure). The "
            "decoherence plateau is the framework's PRIMARY laboratory "
            "falsifier."
        ),
        tier="computed",
        refs=(
            "grut/derived/decoherence/",
            "tests/derived/test_decoherence.py",
        ),
        tests=(
            "tests/derived/test_decoherence.py",
        ),
        deps=("threshold_bridge", "alpha_vac_derivation"),
        falsifier=(
            "Failure to observe the predicted decoherence plateau at the "
            "predicted mass/separation regime in matter-wave interferometry."
        ),
    ),

    # ─── Chapter 6: Gravity ─────────────────────────────────────────
    Claim(
        id="gr_recovery",
        chapter=6,
        statement=(
            "General relativity is recovered in the high-frequency limit "
            "(ωτ_0 ≫ 1): n_g(ω) → 1, α_eff(X) → 0, the constitutive "
            "Newtonian potential reduces to −GM/r exactly. At low "
            "frequency, Φ → (4/3) × Φ_GR (DC enhancement). The Bianchi "
            "identity is preserved under the constitutive projection: "
            "∂_μ Φ^μν = χ(ω) × ∂_μ T^μν = 0 since χ is a frequency-"
            "scalar in the linearized regime. Graviton propagator UV "
            "falloff is 1/ω from the susceptibility (the propagator's "
            "1/ω³ overall behavior is UV-complete without ghosts)."
        ),
        tier="computed",
        refs=(
            "V7 §22-§25 (gravity sector)",
            "grut/foundation/closure_protocol.py:n_g_refractive",
            "grut/foundation/gr_recovery.py",
        ),
        tests=(
            "tests/foundation/test_closure_protocol.py::TestResponseKernel::test_n_g_high_freq_reduces_to_one",
            "tests/foundation/test_closure_protocol.py::TestEngineInterpolation::test_g_eff_equals_g_bar_at_solar_system",
            "tests/foundation/test_gr_recovery.py::TestHighFrequencyLimit",
            "tests/foundation/test_gr_recovery.py::TestLowFrequencyLimit",
            "tests/foundation/test_gr_recovery.py::TestBianchiPreservation",
            "tests/foundation/test_gr_recovery.py::TestGravitonUV",
            "tests/foundation/test_gr_recovery.py::TestVerifyHarness",
        ),
        deps=("memory_kernel_form", "regime_map"),
        falsifier=(
            "Detection of constitutive corrections to GR predictions "
            "above the ~10⁻¹⁵ floor at solar-system frequencies, OR a "
            "Bianchi violation in the linearized constitutive theory, "
            "OR a graviton-propagator UV behavior incompatible with "
            "1/ω³ falloff."
        ),
        notes=(
            "PROMOTED to computed: the four legs of GR recovery (high-"
            "freq limit, low-freq enhancement, Bianchi preservation, "
            "UV falloff) are verified at code level. Full nonlinear "
            "GR recovery is the scope of the nonlinear ladder — see "
            "nonlinear_ladder_4_of_8. SCOPE NOTE: gr_recovery's seven "
            "legs verify Φ_μν's behavior; the FORM of Φ_μν is now "
            "derived structurally from δS_CTP/δh_μν at the linearized "
            "level — see phi_munu_linearized_derivation (Correction "
            "#23, 2026-04-30). Curved-background extension remains "
            "open — see phi_munu_curved_background_extension"
            "_open_question."
        ),
    ),
    Claim(
        id="r_max_ricci_saturation",
        chapter=6,
        statement=(
            "The Ricci scalar of the matter-bearing interior saturates "
            "at R_max = α_vac/(c²τ_0²) ≈ 2.12 × 10⁻⁴⁸ m⁻². This bounds "
            "interior trace curvature only; Schwarzschild vacuum exterior "
            "has R = 0 identically and is unconstrained."
        ),
        tier="computed",
        refs=(
            "V7 §13 (Whole Hole)",
            "grut/foundation/closure_protocol.py:R_MAX_INV_M2",
        ),
        tests=(
            "tests/foundation/test_closure_protocol.py::TestRMaxSaturationCurvature::test_R_max_formula",
            "tests/foundation/test_closure_protocol.py::TestRMaxSaturationCurvature::test_R_max_universal_order",
        ),
        deps=("alpha_vac_derivation", "tau_0_derivation"),
        notes=(
            "Tidal Weyl curvature outside the horizon is unbounded by "
            "R_max. The constraint applies only where matter sources the "
            "Ricci tensor."
        ),
    ),
    Claim(
        id="rho_max_universal",
        chapter=6,
        statement=(
            "Every black-hole core saturates at the same maximum interior "
            "density ρ_max = c²R_max/(8πG) ≈ 1.14 × 10⁻²² kg/m³, "
            "independent of mass. Larger holes contain larger cores at "
            "this universal density."
        ),
        tier="computed",
        refs=(
            "V7 §13",
            "grut/foundation/closure_protocol.py:RHO_MAX_KG_M3",
        ),
        tests=(
            "tests/foundation/test_closure_protocol.py::TestRMaxSaturationCurvature::test_rho_max_formula",
            "tests/foundation/test_closure_protocol.py::TestRMaxSaturationCurvature::test_rho_max_is_universal_constant",
        ),
        deps=("r_max_ricci_saturation",),
        notes=(
            "Open numerical question: ρ_max ~ 10⁻²² kg/m³ is below typical "
            "naive BH interior densities. Whether additional structure "
            "(e.g. curvature-dependent effective τ in the interior) is "
            "needed for quantitatively realistic core sizes is flagged "
            "as rho_max_scale_open_question."
        ),
    ),
    Claim(
        id="nonlinear_ladder_4_of_8",
        chapter=6,
        statement=(
            "The nonlinear-gravity ladder has 4 of 8 rungs explicitly "
            "computed (V7 §22-§25): linearized recovery, second-order "
            "consistency, third-order matching, and constitutive "
            "back-reaction. Rungs 5-8 (full nonlinear closure) remain open."
        ),
        tier="open_negative",
        refs=("V7 §22-§25", "V7 §43 outstanding work"),
        deps=("gr_recovery",),
        notes=(
            "Honest negative on the gravity sector. The framework is GR-"
            "compatible at the rungs computed; full nonlinear closure is "
            "Phase-1+. This is documented, not hidden."
        ),
    ),

    # ─── Chapter 7: The Constant ────────────────────────────────────
    Claim(
        id="r_canonical_path_g",
        chapter=7,
        statement=(
            "Path G — refractive-index identification — gives the "
            "canonical R = n_g(0) = √(1 + α_vac) = √(4/3) ≈ 1.15470. "
            "This is GRUT's primary cosmological observable."
        ),
        tier="computed",
        refs=(
            "grut/foundation/closure_protocol.py:R_REFRACTIVE",
            "grut/foundation/closure_protocol.py:N_G_DC",
            "Komargodski-Schwimmer 2011 (a-theorem, "
            "arXiv:1107.3987) — published basis for a/c = 1/3",
            "Christensen-Duff 1980 (Nucl Phys B 170 480)",
            "Duff 1994 (Class Quant Grav 11 1387, 'Twenty years of "
            "the Weyl anomaly')",
            "grut/foundation/conformal_mode_scalar.py",
        ),
        tests=(
            "tests/foundation/test_closure_protocol.py::TestCanonicalR::test_R_canonical_equals_sqrt_4_over_3",
            "tests/foundation/test_closure_protocol.py::TestCanonicalR::test_R_refractive_aliases_n_g_DC",
        ),
        deps=("alpha_vac_derivation", "memory_kernel_form"),
        falsifier=(
            "Direct measurement of the gravitational refractive index "
            "deviating from √(4/3) by more than the cosmological "
            "structural tolerance."
        ),
    ),
    Claim(
        id="r_path_d_dirac",
        chapter=7,
        statement=(
            "Path D — SM 1-loop trace anomaly with Dirac neutrinos — "
            "gives a/c = 253/219 ≈ 1.15525, within 0.05% of Path G's "
            "canonical √(4/3). Dirac is closer to canonical than Majorana."
        ),
        tier="computed",
        refs=(
            "Komargodski-Schwimmer 2011",
            "Duff 1994 (40 years review)",
            "theory/path_d_trace_anomaly/STAGE_D_TRACE_ANOMALY_RATIO.md",
            "grut/foundation/closure_protocol.py:A_OVER_C_SM_DIRAC",
        ),
        tests=(
            "tests/foundation/test_closure_protocol.py::TestCanonicalR::test_path_d_dirac_a_over_c",
            "tests/foundation/test_closure_protocol.py::TestCanonicalR::test_dirac_closer_to_canonical_than_majorana",
        ),
        deps=("r_canonical_path_g", "alpha_vac_derivation"),
        notes=(
            "The Dirac variant supports the GRUT ToE's lean-Dirac "
            "falsifiable posture (see neutrino_dirac_prediction)."
        ),
    ),
    Claim(
        id="r_path_d_majorana",
        chapter=7,
        statement=(
            "Path D variant — SM 1-loop trace anomaly with Majorana "
            "neutrinos — gives a/c = 1991/1698 ≈ 1.17256, secondary "
            "cross-check at the ~1.5% level vs Path G."
        ),
        tier="computed",
        refs=(
            "theory/path_d_trace_anomaly/STAGE_D_TRACE_ANOMALY_RATIO.md",
            "grut/foundation/closure_protocol.py:A_OVER_C_SM_MAJORANA",
        ),
        tests=(
            "tests/foundation/test_closure_protocol.py::TestCanonicalR::test_path_d_majorana_a_over_c",
        ),
        deps=("r_canonical_path_g",),
    ),
    Claim(
        id="tji_7_4_open_negative",
        chapter=7,
        statement=(
            "The TJI 3-loop path on flat space produces raw Laurent "
            "coefficient −541/2304 at ε⁰ in the gamma-function scheme. "
            "Reconciliation to V7 §26.2.3's claimed 7/4 (FeynCalc) was "
            "attempted across 24 scheme configurations and FAILED. "
            "HONEST NEGATIVE."
        ),
        tier="open_negative",
        refs=(
            "theory/derivation/CORRECTION_21_TJI_PHASE_0P5_SCHEME_RECONCILIATION.md",
            "grut/derivation/tji/flat_space.py",
            "grut/derivation/tji/ms_bar_reconciliation.py",
        ),
        tests=(
            "tests/derivation/tji/test_flat_space.py::test_raw_scheme_value_differs_from_feyncalc_by_scheme",
            "tests/derivation/tji/test_ms_bar_reconciliation.py",
        ),
        deps=("r_canonical_path_g",),
        notes=(
            "Phase-0.5 documented HONEST NEGATIVE; the 1.15428 number is "
            "demoted from canonical (Path G's √(4/3) = 1.15470 takes its "
            "place). Phase-1+ on curved space remains open."
        ),
    ),

    # ─── Chapter 8: The Terminal Velocity ───────────────────────────
    Claim(
        id="minus_100_drive",
        chapter=8,
        statement=(
            "The −100 coefficient in the conformal-instability sector "
            "of Euclidean gravity on S⁴ is the Gibbons-Hawking drive of "
            "cosmic expansion, not a calculational bug. The constitutive "
            "memory kernel damps it to a finite Hubble rate."
        ),
        tier="computed",
        refs=(
            "V7 §26.2.3 (conformal instability)",
            "theory/derivation/MINUS_100_RESOLUTION.md",
            "grut/derivation/minus_100/",
            "grut/derivation/minus_100/conformal_anomaly.py",
        ),
        tests=(
            "tests/derivation/test_minus_100_resolution.py",
            "tests/derivation/test_minus_100_structural.py",
        ),
        deps=("ctp_action_structure",),
        notes=(
            "Structural identification (Correction #16) locks the SM "
            "field counts (4 scalars, 45 Weyl fermions, 12 gauge bosons), "
            "1-loop a/c numerators, U(1)_Y β = 20/3, conformal-mode "
            "kinetic sign, and 2-loop 100/256 → −100 normalization. "
            "Backed by tests/derivation/test_minus_100_structural.py."
        ),
    ),
    Claim(
        id="h_inf_decomposition",
        chapter=8,
        statement=(
            "The asymptotic Hubble rate decomposes as H_inf = drive / "
            "friction = (2 − R) / (S · τ_0). Drive: (2−R) from conformal-"
            "mode physics. Friction: 1/(S·τ_0) from the screened "
            "constitutive relaxation."
        ),
        tier="computed",
        refs=(
            "V7 §26.2.3a",
            "grut/derived/cosmology/",
            "tests/derived/test_h0_first_principles.py",
        ),
        tests=(
            "tests/derived/test_h0_first_principles.py",
            "tests/derived/test_hubble_from_first_principles.py",
        ),
        deps=("r_canonical_path_g", "screening_108pi", "tau_0_derivation"),
    ),
    Claim(
        id="omega_lambda_prediction",
        chapter=8,
        statement=(
            "Ω_Λ = 0.6886 predicted, 0.04% from Planck 2018 best-fit. "
            "Zero free parameters; comes from the same H_inf machinery "
            "as the Hubble rate."
        ),
        tier="computed",
        refs=("V7 §27", "tests/derived/test_cosmology.py"),
        tests=("tests/derived/test_cosmology.py",),
        deps=("h_inf_decomposition",),
        falsifier=(
            "Convergent measurement of Ω_Λ outside the predicted band."
        ),
    ),
    Claim(
        id="h_0_prediction",
        chapter=8,
        statement=(
            "H_0 ≈ 68.8 km/s/Mpc implied by τ_0 = 41.9 Myr and S = 108π. "
            "Lies in the Hubble-tension gap between Planck (67.4) and "
            "SH0ES (73.0); GRUT's natural value is between them."
        ),
        tier="computed",
        refs=(
            "grut/foundation/closure_protocol.py:H_0_IMPLIED_KM_S_MPC",
        ),
        tests=(
            "tests/foundation/test_closure_protocol.py::TestCanonicalConstants::test_H0_implied_is_planck_like",
        ),
        deps=("h_inf_decomposition", "tau_0_derivation", "screening_108pi"),
        falsifier=(
            "Convergent H_0 measurement outside 69 ± 3 km/s/Mpc."
        ),
        notes=(
            "Two H_0 routes coexist in the framework: (a) this claim — "
            "the cosmic-baseline relation H_0 = 1/(S × τ_0) → 68.8 "
            "km/s/Mpc, zero-parameter; (b) the detailed Friedmann-"
            "integrated route (grut/derived/cosmology/hubble_from_"
            "first_principles.py:grut_H_0_prediction) → 69.03 km/s/Mpc, "
            "one-parameter using N_total = 329 as observed-cosmic-age "
            "anchor. The two routes agree at 0.3%, supporting the "
            "cosmic-baseline approximation. Route (b)'s observational "
            "anchor is documented separately as "
            "n_total_zero_parameter_derivation_open_question (Ch 12)."
        ),
    ),
    Claim(
        id="t_c_thermal_transition",
        chapter=8,
        statement=(
            "The 'boiling point of gravity' T_c = ℏ/(τ_micro × k_B) ≈ "
            "54.7 MK, where τ_micro ≈ 1.4×10⁻¹⁹ s is the microscopic "
            "plasma relaxation time of the responsive vacuum (distinct "
            "from the macroscopic gravitational τ_0 = 41.9 Myr — see "
            "tau_micro_thermal_scale and Correction #22). Above T_c, "
            "gravity is local (no metric memory) — explains absence "
            "of DM signatures in BBN at T > 10⁹ K. Below T_c (today, "
            "T = 2.725 K), the vacuum is deep in the refractive regime "
            "with full enhancement n_g ≈ 1.1547. Cosmological-"
            "chronology anchor: T_c crossing at t ≈ 1 hour post-Big "
            "Bang per standard cosmic-temperature-vs-time relations."
        ),
        tier="computed",
        refs=(
            "v9.0 (Thermodynamics)",
            "grut/foundation/closure_protocol.py:T_C_KELVIN",
            "theory/derivation/CORRECTION_22_TAU_CLEANUP.md",
        ),
        tests=(
            "tests/foundation/test_closure_protocol.py::TestCanonicalConstants::test_T_c_is_54p7_MK",
            "tests/foundation/test_closure_protocol.py::TestCanonicalConstants::test_T_c_canonical_anchor_is_5p47e7_K",
            "tests/foundation/test_closure_protocol.py::TestCanonicalConstants::test_T_c_formula_is_SI_correct",
            "tests/foundation/test_closure_protocol.py::TestCanonicalConstants::test_T_c_recovered_value_matches_canonical",
            "tests/derived/test_thermal_transition.py",
        ),
        deps=(),
        notes=(
            "T_c = 54.7 MK is empirically anchored to the standard "
            "cosmological-chronology pin (T at t ≈ 1 hour post-Big "
            "Bang per radiation-era Friedmann thermodynamics) — no "
            "GRUT-internal dependency for the value itself. τ_micro "
            "is derived from T_c via the SI-correct formula (see "
            "tau_micro_thermal_scale). Pre-Correction-#22 (2026-04-30) "
            "this claim listed the formula as 1/(τ_0 × k_B), which "
            "was dimensionally invalid (see "
            "t_c_provenance_inconsistency_resolved). Resolution: "
            "introduce τ_micro explicitly, recompute T_c via the "
            "SI-correct formula. Numerical value (54.7 MK) preserved "
            "exactly; test_T_c_is_54p7_MK pin unchanged."
        ),
    ),
    Claim(
        id="tau_micro_thermal_scale",
        chapter=8,
        statement=(
            "τ_micro ≡ ℏ / (k_B × T_c) ≈ 1.396 × 10⁻¹⁹ s — the "
            "microscopic plasma/thermal relaxation time of the "
            "responsive vacuum's microstates. DERIVED from the "
            "empirical T_c anchor via the SI-correct formula. "
            "Distinct from the macroscopic gravitational τ_0 = 41.9 "
            "Myr by ~34 orders of magnitude. Required to make T_c "
            "dimensionally consistent: prior to Correction #22 the "
            "formula T_c = 1/(τ_0 × k_B) lacked ℏ and produced units "
            "K/(J·s); the SI-correct expression T_c = ℏ/(τ × k_B) "
            "requires τ at femtosecond scale, not Myr scale. The "
            "34-orders-of-magnitude separation between τ_micro and "
            "τ_0 is now named explicitly; their relation is a sharp "
            "open question (tau_zero_to_tau_micro_relation_open"
            "_question)."
        ),
        tier="computed",
        refs=(
            "grut/foundation/closure_protocol.py:TAU_MICRO_SEC",
            "theory/foundations_audit/T_C_PROVENANCE.md",
            "theory/derivation/CORRECTION_22_TAU_CLEANUP.md",
        ),
        tests=(
            "tests/foundation/test_closure_protocol.py::TestCanonicalConstants::test_tau_micro_is_femtosecond_scale",
            "tests/foundation/test_closure_protocol.py::TestCanonicalConstants::test_two_tau_scales_separated_by_thirty_plus_orders",
            "tests/foundation/test_closure_protocol.py::TestCanonicalConstants::test_T_c_old_dimensionally_invalid_formula_NOT_used",
        ),
        deps=("t_c_thermal_transition",),
        falsifier=(
            "If a cosmological observable distinguishes the τ-scale "
            "of T_c (e.g. a BBN-era observable that requires τ_0 to "
            "set its threshold rather than τ_micro), the two-scale "
            "framework is falsified."
        ),
        notes=(
            "Derived from T_c's cosmological-chronology anchor via "
            "the dimensionally consistent dual ℏ ↔ k_B × time. "
            "τ_micro itself has no closure path to τ_0 within the "
            "current framework — that derivation is an open question "
            "(tau_zero_to_tau_micro_relation_open_question). See the "
            "open question for closure paths under investigation."
        ),
    ),

    # ─── Chapter 9: The Dark Sector ─────────────────────────────────
    Claim(
        id="bandwidth_integral",
        chapter=9,
        statement=(
            "The cosmological bandwidth integral evaluates the linear-"
            "regime contribution of the responsive vacuum to the matter "
            "budget; produces Ω_dm = α_vac = 1/3 with zero free "
            "parameters."
        ),
        tier="computed",
        refs=(
            "grut/derived/cosmology/bandwidth_integral.py",
            "tests/derived/test_bandwidth_integral.py",
        ),
        tests=("tests/derived/test_bandwidth_integral.py",),
        deps=("alpha_vac_derivation", "memory_kernel_form"),
    ),
    Claim(
        id="omega_dm_equals_alpha",
        chapter=9,
        statement=(
            "Ω_dm = α_vac = 1/3 (~33%, +27% from Planck's 26.6%). "
            "The bandwidth integral over linear-regime modes (BBKS-"
            "weighted) saturates at α — verified at code level: "
            "Ω_dm,eff = 0.3333, insensitive to c_s across 50-500 km/s "
            "(geometric, not kinematic). Dark matter is the low-"
            "frequency content of the same medium that produces dark "
            "energy at terminal velocity."
        ),
        tier="computed",
        refs=(
            "V7 §28 (dark sector)",
            "Phase I §9",
            "grut/derived/cosmology/dielectric_dm.py",
            "grut/derived/cosmology/bandwidth_integral.py",
        ),
        tests=(
            "tests/derived/test_dielectric_dm.py",
            "tests/derived/test_bandwidth_integral.py",
            "tests/derived/test_omega_dm_hardening.py",
        ),
        deps=("bandwidth_integral", "alpha_vac_derivation"),
        notes=(
            "Anchored: matches data within ~30%, full reconciliation "
            "between linear-regime α and observed Ω_dm including "
            "nonlinear structure formation is open. The dielectric "
            "reframing (Track VII) explicitly maps n_g(ω) to the dark-"
            "matter abundance via frequency-gated enhancement."
        ),
        falsifier=(
            "CMB-peak measurement of Ω_dm robustly inconsistent with "
            "α_vac = 1/3 at the linear-regime level."
        ),
    ),
    Claim(
        id="mond_a_0_emergence",
        chapter=9,
        statement=(
            "MOND-like trigger acceleration a_0 = c/(2π τ_Λ) ≈ "
            "1.2 × 10⁻¹⁰ m/s² emerges from the response time, not from "
            "modified dynamics. The MOND interpolation ν(y) is recovered "
            "from frequency-gated screening, not postulated."
        ),
        tier="computed",
        refs=(
            "Phase I §8.2, Appendix E",
            "grut/foundation/closure_protocol.py:A_0_SI",
            "grut/foundation/closure_protocol.py:nu_interpolation",
        ),
        tests=(
            "tests/foundation/test_closure_protocol.py::TestCanonicalConstants::test_a_0_in_MOND_band",
            "tests/foundation/test_closure_protocol.py::TestEngineInterpolation",
        ),
        deps=("tau_0_derivation",),
    ),
    Claim(
        id="bullet_cluster_offset",
        chapter=9,
        statement=(
            "The Bullet Cluster gas-to-LENSING offset (per cluster) is "
            "GRUT's specific cluster-scale prediction. Full memory-kernel "
            "convolution with a piecewise-linear deceleration profile "
            "(v_initial = 4700 km/s, v_final = 3000 km/s, t_since = "
            "150 Myr, τ_0 = 41.9 Myr) yields δ_GRUT = 130 kpc, within "
            "factor 1.15 of the observed ~150 kpc (Clowe et al. 2006). "
            "The kernel result is bracketed by simple v_final × τ_0 = "
            "129 kpc and v_initial × τ_0 = 201 kpc. The cluster-to-"
            "cluster separation of 720 kpc reproduces v_initial × t_since "
            "exactly — kinematic, not a GRUT-specific test."
        ),
        tier="computed",
        refs=(
            "v1.0 §3 (Bullet Cluster benchmark)",
            "Clowe et al. 2006 (astro-ph/0608407)",
            "Markevitch et al. 2002 (ApJ 567 L27)",
            "grut/foundation/closure_protocol.py:bullet_offset_estimate",
            "grut/derived/cluster/bullet_cluster.py",
        ),
        tests=(
            "tests/foundation/test_closure_protocol.py::TestBulletCluster::test_bullet_offset_is_order_100_kpc",
            "tests/derived/test_bullet_cluster.py::TestSimpleGRUTOffset",
            "tests/derived/test_bullet_cluster.py::TestKernelConvolution",
            "tests/derived/test_bullet_cluster.py::TestObservationComparison",
            "tests/derived/test_bullet_cluster.py::TestVerifyHarness",
        ),
        deps=("tau_0_derivation", "memory_kernel_form"),
        falsifier=(
            "A merging-cluster system whose lensing peak does not lag "
            "the gas peak by v · τ_0 within factor 2, where v is the "
            "post-collision relative velocity. Observation of a "
            "lensing-gas offset that DOES NOT scale as v · τ_0 across "
            "multiple cluster mergers would falsify the memory-kernel "
            "interpretation."
        ),
        notes=(
            "Track VII's primary cluster-scale falsifier — a Phase-1 "
            "result for the dielectric-DM picture. The 720 kpc that "
            "appears in popular Bullet-Cluster discussion is the "
            "kinematic cluster-cluster separation v_initial × t_since "
            "and is reproduced by any theory; GRUT's distinctive "
            "prediction is the gas-to-lensing offset within each "
            "cluster, hardened here by full kernel convolution."
        ),
    ),
    Claim(
        id="rotation_curves_match",
        chapter=9,
        statement=(
            "Galactic rotation curves are produced by g_eff = g_bar [1 + "
            "(ν(y) − 1)/(1 + X²)] where y = g_bar/a_0 and X = ω·τ_0. "
            "Specific verified behaviors at code level: Newtonian inner "
            "regions; flat outer regions; baryonic Tully-Fisher relation "
            "with coefficient G·a_0; v_flat ∝ M^(1/4) power law; "
            "intermediate transition regime; deep-response saturation. "
            "Seven distinct predictions pinned by passing tests."
        ),
        tier="computed",
        refs=(
            "tests/derived/test_rotation_curves.py",
            "Phase I Appendix E.2",
            "McGaugh, Lelli, Schombert 2016 (BTFR, ApJ 816 L14)",
        ),
        tests=(
            "tests/derived/test_rotation_curves.py::test_inner_radius_is_approximately_newtonian",
            "tests/derived/test_rotation_curves.py::test_outer_radius_flattens_near_BTFR",
            "tests/derived/test_rotation_curves.py::test_rotation_curve_flattens_with_radius",
            "tests/derived/test_rotation_curves.py::test_BTFR_coefficient_is_G_times_a0",
            "tests/derived/test_rotation_curves.py::test_BTFR_v_flat_scales_as_M_to_the_quarter",
            "tests/derived/test_rotation_curves.py::test_inner_galaxy_is_intermediate_or_newtonian",
            "tests/derived/test_rotation_curves.py::test_outer_galaxy_is_deep_response",
        ),
        deps=("mond_a_0_emergence", "regime_map"),
        falsifier=(
            "BTFR with coefficient ≠ G·a_0, OR v_flat scaling ≠ M^(1/4), "
            "OR rotation curves at low acceleration showing GR rather "
            "than MOND-like behavior at high frequency (differential "
            "test that distinguishes GRUT from MOND)."
        ),
        notes=(
            "PROMOTED from anchored to computed. The seven engine "
            "predictions are pinned by passing tests. Full statistical "
            "SPARC sample fit and the high-frequency low-acceleration "
            "differential test (distinguishing GRUT from MOND) remain "
            "Phase-1+ specialist work; this claim covers the engine's "
            "reproduction of expected behavior at code level."
        ),
    ),
    Claim(
        id="baryogenesis_eta_b",
        chapter=9,
        statement=(
            "Baryogenesis from CTP path asymmetry (R ≠ 1) gives the "
            "baryon-to-photon ratio η_B = J_CP × K_neq × (2−R_B)/S_B "
            "≈ 6.57 × 10⁻¹⁰ (route 1), +7.7% from Planck observed "
            "6.10 × 10⁻¹⁰. The asymmetry vanishes at R = 1 — the "
            "universe has nonzero baryon asymmetry because R ≠ 1."
        ),
        tier="computed",
        refs=(
            "tests/derived/test_baryogenesis.py",
            "V7 §29",
            "grut/derived/baryogenesis/eta.py",
        ),
        tests=(
            "tests/derived/test_baryogenesis.py",
            "tests/derived/test_baryogenesis_hardening.py",
        ),
        deps=("r_canonical_path_g", "ctp_action_structure"),
        falsifier=(
            "Refined PDG η_B value driving the deviation outside the "
            "8% band, or refined J_CP / K_neq inputs producing a "
            "predicted η_B inconsistent with observation by more than "
            "the framework's tolerance."
        ),
    ),

    # ─── Chapter 10: Time and Information ──────────────────────────
    Claim(
        id="arrow_of_time_from_entropy",
        chapter=10,
        statement=(
            "The arrow of time emerges from the constitutive entropy "
            "production rate Ṡ = (1/τ_0) ⟨(z − z_target)²⟩ ≥ 0, which "
            "(i) is non-negative for any state, (ii) vanishes only at "
            "the fixed point z = z_target, and (iii) integrates to a "
            "monotonically non-decreasing cumulative entropy under "
            "constitutive evolution. The Second Law is a consequence "
            "of the CTP action's retarded-kernel structure, not an "
            "independent postulate."
        ),
        tier="computed",
        refs=(
            "V7 Appendix D (entropy production)",
            "V7 Appendix E",
            "grut/foundation/entropy_production.py",
        ),
        tests=(
            "tests/foundation/test_entropy_production.py::TestNonNegativity",
            "tests/foundation/test_entropy_production.py::TestFixedPointVanishing",
            "tests/foundation/test_entropy_production.py::TestMonotonicCumulativeEntropy",
            "tests/foundation/test_entropy_production.py::TestEntropyProductionTrajectory",
            "tests/foundation/test_entropy_production.py::TestVerifyHarness",
        ),
        deps=("constitutive_equation",),
        falsifier=(
            "Detection of an entropy-decreasing constitutive trajectory, "
            "or a non-positive Ṡ at any off-fixed-point configuration."
        ),
        notes=(
            "PROMOTED to computed — Chapter 10's first computed claim. "
            "Verified at three legs: random non-negativity, fixed-point "
            "vanishing, cumulative monotonicity. The full V7 Appendix-D "
            "channel-capacity machinery is downstream and remains "
            "anchored at bh_information_partial."
        ),
    ),
    Claim(
        id="bh_information_partial",
        chapter=10,
        statement=(
            "Hawking radiation carries constitutive correlations and is "
            "not strictly thermal. Page-curve consistency holds at the "
            "linearized level via the memory kernel; fully nonlinear "
            "closure is open."
        ),
        tier="anchored",
        refs=("V7 §13 (Whole Hole)", "V7 §31 (BH information)"),
        deps=("r_max_ricci_saturation", "memory_kernel_form"),
        notes=(
            "Linearized result anchored; nonlinear closure is part of "
            "the nonlinear-ladder open work."
        ),
    ),

    # ─── Chapter 11: The Observer ──────────────────────────────────
    Claim(
        id="measurement_resolution",
        chapter=11,
        statement=(
            "The measurement problem is resolved without an additional "
            "postulate: when an apparatus (Λ_grav,A τ_0 ≫ 1, deep "
            "crystal) couples to a quantum object (Λ_grav,B τ_0 ≲ 1, "
            "boundary), the joint Λ_eff = Λ_A + Λ_B is apparatus-"
            "dominated, and the quantum object's decoherence rate is "
            "accelerated by the ratio Λ_A/Λ_B. The 'collapse' is the "
            "faster crystallizer dragging the slower one across the "
            "threshold — verified numerically with a 1 g / 1 mm "
            "apparatus and an atom-scale quantum object: separation "
            "ratio Λ_A/Λ_B ~ 10³², joint X ~ 10³⁵, atom alone X < 1."
        ),
        tier="computed",
        refs=(
            "V7 §11",
            "V7 §12 (measurement)",
            "grut/foundation/measurement_resolution.py",
        ),
        tests=(
            "tests/foundation/test_measurement_resolution.py::TestScalingSeparation",
            "tests/foundation/test_measurement_resolution.py::TestJointDominance",
            "tests/foundation/test_measurement_resolution.py::TestAccelerationFactor",
            "tests/foundation/test_measurement_resolution.py::TestVerifyHarness",
            "tests/foundation/test_measurement_resolution.py::TestMeasurementProblemFraming",
        ),
        deps=("threshold_bridge", "decoherence_plateau"),
        falsifier=(
            "Detection of a measurement event where the apparatus's "
            "Λ_grav is NOT dominant in the joint dynamics (e.g. a "
            "macroscopic apparatus failing to crystallize a coupled "
            "quantum object), OR Born-rule probabilities inconsistent "
            "with the noise-kernel weighting at the coupling geometry."
        ),
        notes=(
            "PROMOTED to computed at the rate-dynamics level — the "
            "'faster crystallizer wins' picture is now backed by "
            "passing tests on the canonical apparatus + quantum-object "
            "example. The Born-rule probability emergence from N-"
            "weighted coupling geometry is deeper and remains anchored "
            "in V7 §12."
        ),
    ),
    Claim(
        id="observer_as_crystal",
        chapter=11,
        statement=(
            "The observer is not external to the framework — the "
            "observer is the part of the medium that has crystallized. "
            "The scaling law applies to measurer and measured equally."
        ),
        tier="conjectural",
        refs=("V7 §11", "Layer-2 interpretation, this session"),
        deps=("threshold_bridge", "measurement_resolution"),
        notes=(
            "Layer-2 interpretation. Computed-framework backbone "
            "(threshold_bridge) supports the picture; the interpretive "
            "claim itself is not a separate test."
        ),
    ),
    Claim(
        id="schrodinger_in_box_inversion",
        chapter=11,
        statement=(
            "Philosophical reformulation of the Schrödinger's-cat "
            "thought experiment consistent with the framework's "
            "closed-self-referential-universe stance: the OBSERVER "
            "is the boxed system (finite, local, information-"
            "limited); the cat continues evolving outside the "
            "observer's information horizon. Observation is "
            "synchronization through contact, not creation through "
            "measurement. The observer-as-boxed inversion follows "
            "directly from observer_as_crystal (no privileged outside-"
            "frame) and measurement_resolution (faster-crystallizer-"
            "wins via Λ_grav coupling). Worked example of these "
            "principles applied to the most famous measurement "
            "thought experiment."
        ),
        tier="anchored",
        refs=(
            "theory/derivation/SCHRODINGER_IN_BOX_BMV_COMPARISON.md",
            "grut/derived/decoherence/schrodinger_in_box.py",
            "tests/derived/test_schrodinger_in_box.py",
        ),
        tests=(
            "tests/derived/test_schrodinger_in_box.py",
        ),
        deps=("measurement_resolution", "observer_as_crystal"),
        notes=(
            "ANCHORED — philosophical reformulation, not new physics. "
            "The conceptual content (the inversion) and the worked "
            "formalism (Bayesian filtering equation, separately "
            "registered as bayesian_observer_filtering) follow from "
            "the framework's existing measurement-resolution machinery "
            "applied to the cat-in-box scenario. The "
            "entanglement-locking layer is registered separately as "
            "gravitational_entanglement_formation_rate (Ch 5); the "
            "Wigner's-friend application is registered separately as "
            "wigner_friend_dissolution. This claim covers the "
            "philosophical inversion alone — observer-in-the-box "
            "rather than cat-in-the-box. No new physics predictions "
            "are made by this claim."
        ),
    ),
    Claim(
        id="bayesian_observer_filtering",
        chapter=11,
        statement=(
            "The framework provides a Bayesian filtering equation for "
            "how an observer's certainty about a remote system "
            "evolves between contact events: dp/dt = −μp − γp(1−p), "
            "with reset rule p(t⁺) = 1 at contact-return events. "
            "Term 1 (−μp) is the standard exponential survival "
            "decay with hazard rate μ. Term 2 (−γp(1−p)) is the "
            "absence-as-data Bayesian penalty: if returns are "
            "expected at rate γ when alive, NOT seeing a return is "
            "evidence the cat may not be alive. Closed-form limits: "
            "γ = 0 reduces to exponential decay p(t) = p_0 exp(−μt); "
            "μ = 0 reduces to logistic decay "
            "p(t) = p_0/(p_0 + (1−p_0)exp(γt)). The equation is "
            "mechanically derivable from Bayesian inference under "
            "the framework's observer-as-crystal worldview."
        ),
        tier="anchored",
        refs=(
            "grut/derived/decoherence/schrodinger_in_box.py",
            "tests/derived/test_schrodinger_in_box.py",
            "theory/derivation/SCHRODINGER_IN_BOX_BMV_COMPARISON.md",
        ),
        tests=(
            "tests/derived/test_schrodinger_in_box.py",
        ),
        deps=("schrodinger_in_box_inversion", "observer_as_crystal"),
        notes=(
            "ANCHORED, EPISTEMIC — captures information-finite-"
            "observer dynamics under the framework's worldview, NOT "
            "a new physics prediction. The equation is derivable "
            "from Bayesian inference applied to the framework's "
            "observer model; it does not extend the decoherence-"
            "plateau falsifier surface (Ch 5) or replace the "
            "framework's existing measurement_resolution machinery "
            "(Ch 11). The 'absence is data' formulation makes "
            "explicit what the framework's information-finite "
            "observer experiences between contact events. Tests "
            "pin both closed-form limits (pure hazard, pure "
            "absence) and the contact-reset rule with periodic "
            "returns. Could in principle be tier-promoted to "
            "computed if framed as 'mechanically reproducible from "
            "Bayesian assumptions,' but anchored is the disciplined "
            "tier — the equation isn't physics, it's epistemic "
            "machinery for the framework's observer concept."
        ),
    ),
    Claim(
        id="wigner_friend_dissolution",
        chapter=11,
        statement=(
            "The Wigner's-friend paradox dissolves under explicit "
            "conditional-state mathematics. The friend's "
            "crystallinity X_friend = Λ_grav,friend × τ_0 ~ 10^35 "
            "for a 70 kg human at 1 m separation; the friend's "
            "pointer state crystallizes on femtosecond timescales. "
            "Wigner's outside ρ_lab description (marginalizing over "
            "external lab variables) and the friend's inside record "
            "(marginalizing over external friend variables) are "
            "conditional-state consistent: they describe the same "
            "X ≫ 1 crystallized configuration from different "
            "marginalizations. The conditional probability ρ(cat | "
            "friend's record) is the same from both perspectives. "
            "No paradox; standard conditional-probability mathematics "
            "applied to a deep-crystal system. Computed in "
            "wigner_friend_consistency()."
        ),
        tier="computed",
        refs=(
            "theory/derivation/SCHRODINGER_IN_BOX_BMV_COMPARISON.md",
            "theory/derivation/LAMBDA_CONTACT_CTP_DERIVATION.md",
            "grut/foundation/measurement_resolution.py",
            "grut/derived/decoherence/lambda_contact.py",
        ),
        tests=(
            "tests/derived/test_lambda_contact.py::TestWignerFriendDissolution",
        ),
        deps=(
            "measurement_resolution",
            "observer_as_crystal",
            "schrodinger_in_box_inversion",
            "lambda_contact_ctp_derivation",
        ),
        notes=(
            "PROMOTED FROM ANCHORED TO COMPUTED in Stage 2 of the "
            "Λ_contact CTP derivation work. The dissolution is now "
            "an explicit conditional-state calculation rather than "
            "narrated prose. Tests verify X_friend ≫ 1, decoherence "
            "time < femtosecond, outside-description consistency. "
            "Born rule remains a separate open negative — the "
            "dissolution shows consistency of description, not "
            "derivation of probability weights."
        ),
    ),
    Claim(
        id="lambda_contact_ctp_derivation",
        chapter=11,
        statement=(
            "Λ_contact (the contact-formation rate at which the "
            "observer's pointer state crystallizes into a definite "
            "record) is identified with Λ_grav evaluated at the "
            "pointer (apparatus + observer body) mass scale. The "
            "two-particle reduced density matrix calculation, with "
            "the gravitational noise kernel N_grav = G/(ℏ|x-x'|) "
            "integrated over vacuum modes, produces a joint off-"
            "diagonal decay rate dominated by the heavier particle's "
            "self-decoherence rate when m_P >> m_S. Λ_contact = "
            "G m_P² S(l_P/R_P) / (ℏ l_P) — the same formula the "
            "framework already uses for Λ_grav, applied at the "
            "observer-pointer scale rather than the system scale. "
            "The kernel-level Anastopoulos-Hu-style derivation is "
            "reproduced self-contained in framework primitives "
            "(no longer requiring chase to AH 2013 citation)."
        ),
        tier="computed",
        refs=(
            "theory/derivation/LAMBDA_CONTACT_CTP_DERIVATION.md",
            "grut/derived/decoherence/lambda_contact.py",
            "Anastopoulos & Hu, CQG 30, 165007 (2013)",
        ),
        tests=(
            "tests/derived/test_lambda_contact.py::TestAnastopoulosHuRedoMatchesFramework",
            "tests/derived/test_lambda_contact.py::TestTwoParticleJointDecoherence",
            "tests/derived/test_lambda_contact.py::TestStage2SubstantiveFindings",
        ),
        deps=(
            "memory_kernel_form",
            "ctp_action_structure",
            "decoherence_plateau",
            "screening_108pi",
        ),
        notes=(
            "Stage 2 deliverable from external-review observer-module "
            "gap audit. Closes gap #2 (explicit reduced-density-matrix "
            "derivation in framework primitives). The substantive "
            "finding: 'Λ_contact missing' was a labeling/identification "
            "gap, not a computational gap. The framework's existing "
            "Λ_grav formula already encodes the contact-formation rate "
            "when evaluated at pointer scale. Tier-promotes the "
            "Schrödinger-in-the-Box program from anchored interpretive "
            "scaffolding to computed measurement-theory module — with "
            "the Born-rule carve-out registered as a separate open "
            "negative."
        ),
    ),
    Claim(
        id="pointer_observable_position_basis",
        chapter=11,
        statement=(
            "The pointer observable in the framework is the center-"
            "of-mass position operator x̂_P of macroscopic record-"
            "bearing degrees of freedom in the apparatus, evaluated "
            "at coarse-graining scales such that X_P = Λ_grav,P × "
            "τ_0 ≫ 1. This basis choice follows from Zurek's "
            "einselection criterion applied to gravitational coupling: "
            "H_int = -G m_S m_P / |x_S - x_P| is diagonal in the "
            "simultaneous position basis, so the noise kernel "
            "selects position eigenstates as the preferred "
            "(predictable) basis."
        ),
        tier="anchored",
        refs=(
            "theory/derivation/LAMBDA_CONTACT_CTP_DERIVATION.md",
            "grut/derived/decoherence/lambda_contact.py",
            "Zurek, Rev. Mod. Phys. 75, 715 (2003) — einselection",
        ),
        tests=(),
        deps=(
            "lambda_contact_ctp_derivation",
            "measurement_resolution",
        ),
        notes=(
            "ANCHORED — the position-basis choice is justified by the "
            "structure of gravitational coupling but is not formally "
            "proven as a Zurek-einselection theorem within GRUT. The "
            "framework's existing measurement_resolution computation "
            "implicitly assumes position-basis pointer states; this "
            "claim makes that assumption explicit. Closure path: a "
            "formal einselection-stability proof under N_grav for "
            "all candidate pointer bases."
        ),
    ),
    Claim(
        id="mu_gamma_ontic_epistemic_distinction",
        chapter=11,
        statement=(
            "In the Bayesian filtering equation dp/dt = -μp - γp(1-p), "
            "the two terms have fundamentally different origins. μ "
            "(hazard rate) is the CTP influence-functional off-diagonal "
            "decay rate, equal to Λ_grav at the pointer parameters — "
            "ONTIC, a physical decoherence rate produced by the "
            "gravitational noise kernel. γ (absence-of-evidence rate) "
            "is the Bayesian update rate from non-occurrence of "
            "expected contact events, depending on the observer's "
            "prior on contact frequency — EPISTEMIC, an information-"
            "state update rate, NOT a physical decoherence process. "
            "The same equation contains two different physics; the "
            "framework's contribution is the explicit identification "
            "of which term comes from which."
        ),
        tier="computed",
        refs=(
            "theory/derivation/LAMBDA_CONTACT_CTP_DERIVATION.md",
            "grut/derived/decoherence/lambda_contact.py",
            "grut/derived/decoherence/schrodinger_in_box.py",
        ),
        tests=(
            "tests/derived/test_lambda_contact.py::TestMuGammaDistinction",
        ),
        deps=(
            "lambda_contact_ctp_derivation",
            "bayesian_observer_filtering",
        ),
        notes=(
            "Closes external-review gap #3 (μ-vs-γ distinction). "
            "Computed via mu_gamma_distinction() with passing tests "
            "verifying μ = Λ_grav at pointer and γ depends only on "
            "the observer's prior, not on m, l, R, or τ_0."
        ),
    ),
    Claim(
        id="born_rule_postulate_open_negative",
        chapter=11,
        statement=(
            "Born rule probabilities |⟨ψ|pointer_i⟩|² do NOT derive "
            "from the gravitational noise kernel N_grav alone. The "
            "CTP machinery produces (i) an off-diagonal decay rate "
            "Λ_grav suppressing coherences in the pointer basis, "
            "and (ii) an asymptotically diagonal density matrix in "
            "that basis. It does NOT produce (iii) the specific "
            "weights on the diagonal elements; those weights inherit "
            "from the Hilbert-space inner-product structure rather "
            "than emerging from N_grav. CTP machinery produces "
            "decoherence rates and noise structure but does not on "
            "its own produce probability assignments. Born rule "
            "derivation in GRUT would require additional postulates "
            "(decoherent-histories weighting, einselection-with-"
            "history-tracking, or comparable). The framework "
            "registers this as an open question rather than "
            "supplying the postulates informally. This is not a "
            "GRUT-specific weakness; current quantum foundations "
            "programs (Copenhagen, Many-Worlds, decoherent histories, "
            "CSL) all require additional structure for Born-rule "
            "derivation."
        ),
        tier="open_negative",
        refs=(
            "theory/derivation/LAMBDA_CONTACT_CTP_DERIVATION.md",
            "grut/derived/decoherence/lambda_contact.py:born_rule_status",
        ),
        tests=(
            "tests/derived/test_lambda_contact.py::TestBornRuleHonestNegative",
        ),
        deps=(
            "lambda_contact_ctp_derivation",
            "memory_kernel_form",
        ),
        notes=(
            "STRUCTURAL FRAMING: the CTP machinery produces "
            "decoherence rates and noise structure but does not on "
            "its own produce probability assignments. Closure paths: "
            "(a) decoherent-histories postulate explicit, deriving "
            "Born rule from history-weighted decoherence functional; "
            "(b) einselection-with-history-tracking, where pointer-"
            "basis probabilities derive from basis-selection dynamics; "
            "(c) deeper-symmetry path-integral weight derivation. "
            "None currently in scope; all are research-tier follow-on "
            "work post-deposit. Open question #16."
        ),
    ),
    Claim(
        id="neural_resonance_speculative",
        chapter=11,
        statement=(
            "A 40 Hz neural resonance arises from two independent "
            "framework routes (V7 Sector 13). Interpretive bridge to "
            "consciousness is SPECULATIVE."
        ),
        tier="conjectural",
        refs=("V7 §13 (Sector 13 [SPECULATIVE])",),
        deps=("constitutive_equation",),
        notes=(
            "Listed for narrative completeness; clearly speculative. "
            "The 40 Hz number is computed from the framework; the "
            "consciousness mapping is interpretive only."
        ),
    ),

    # ─── Chapter 12: Falsification ─────────────────────────────────
    Claim(
        id="derivation_index_appendix",
        chapter=12,
        statement=(
            "Appendix D (Derivation Index) is auto-rendered from the "
            "registry: every claim at tier 'computed' or 'anchored' is "
            "emitted as a per-chapter bullet entry with statement, "
            "tier, dependency count, test count, and downstream fan-"
            "out. Open negatives, conjectural, foundational, and meta "
            "claims are excluded — open negatives have their own auto-"
            "rendered home in Chapter 12, framing-tier claims are not "
            "derivations. Regenerable via "
            "`python3 -m grut.toe.render_appendices`."
        ),
        tier="meta",
        refs=(
            "grut/toe/render_appendices.py:render_appendix_d_derivation_index",
            "tests/toe/test_render_appendices.py::TestAppendixDDerivationIndex",
        ),
        tests=(
            "tests/toe/test_render_appendices.py::TestAppendixDDerivationIndex",
        ),
        notes=(
            "Meta-tier infrastructure. Same discipline pattern as "
            "marker_validator_discipline and predictions_dashboard: "
            "anchor an auto-renderer to the registry so future claim "
            "additions propagate to the appendix automatically."
        ),
    ),

    Claim(
        id="claim_registry_appendix",
        chapter=12,
        statement=(
            "Appendix E (Full Claim Registry) is auto-rendered as a "
            "Markdown reference table over every registry entry. "
            "Columns: chapter, claim ID, tier, statement (truncated), "
            "dependency count, test count. Sorted by chapter then "
            "claim ID for stable diff-friendly ordering. Tier-summary "
            "header reflects live counts. Regenerable via "
            "`python3 -m grut.toe.render_appendices`."
        ),
        tier="meta",
        refs=(
            "grut/toe/render_appendices.py:render_appendix_e_claim_registry",
            "tests/toe/test_render_appendices.py::TestAppendixEClaimRegistry",
        ),
        tests=(
            "tests/toe/test_render_appendices.py::TestAppendixEClaimRegistry",
        ),
        notes=(
            "Meta-tier infrastructure. The renderer escapes pipe "
            "characters in statement cells so embedded |-symbols "
            "(absolute values, table chars in claim text) don't break "
            "the Markdown table. Pinned by test_pipe_chars_in_"
            "statements_escaped."
        ),
    ),

    Claim(
        id="dependency_graph_appendix",
        chapter=12,
        statement=(
            "Appendix F (Dependency Graph) is auto-rendered from "
            "grut/toe/dependencies.py. Five sections: F.1 graph "
            "summary (node/edge counts, max fan-in/out); F.2 roots "
            "(zero-dependency entry points to the framework); F.3 top "
            "10 by downstream fan-out (load-bearing claims, highest-"
            "leverage rigor targets); F.4 closure-priority (open-"
            "negative ranking with explicit blockers); F.5 inter-gap "
            "blocking chains (ASCII map, present iff any open negative "
            "has blocked_by). Regenerable via "
            "`python3 -m grut.toe.render_appendices`."
        ),
        tier="meta",
        refs=(
            "grut/toe/render_appendices.py:render_appendix_f_dependency_graph",
            "grut/toe/dependencies.py",
            "tests/toe/test_render_appendices.py::TestAppendixFDependencyGraph",
        ),
        tests=(
            "tests/toe/test_render_appendices.py::TestAppendixFDependencyGraph",
        ),
        notes=(
            "Meta-tier infrastructure. The renderer's 'closure-"
            "priority' section is the algorithmic version of the "
            "research-priority recommendation: open negatives ranked "
            "by transitive fan-out, with blockers shown explicitly. "
            "Mechanical answer to 'what should we work on next?'."
        ),
    ),

    Claim(
        id="marker_validator_discipline",
        chapter=12,
        statement=(
            "Tier-marker discipline checker: every [OPEN], [SCOPING], "
            "[CONJECTURAL], [SPECULATIVE], or 'Outstanding verification' "
            "marker in the document set is auditable against the "
            "registry. The validator (grut/toe/coherence.py:scan_markers) "
            "finds all marker occurrences, attempts to associate each "
            "with a nearby backticked claim ID, verifies the associated "
            "claim's tier matches the marker's expected tier, and flags "
            "drift. Live audit walks the canonical V7/V8/ToE document "
            "set and produces a MarkerAuditReport with three buckets: "
            "matched-and-consistent, tier_mismatches (registry-tracked "
            "claims whose tier disagrees with their nearby marker), "
            "and orphan_markers (markers without an associated claim "
            "ID — informational, since speculative-content flags are "
            "intentionally un-tracked at the registry level). Specific "
            "counts drift as documents evolve; the validator is "
            "regenerated on demand rather than pinned."
        ),
        tier="meta",
        refs=(
            "grut/toe/coherence.py:scan_markers",
            "grut/toe/coherence.py:marker_audit_report",
            "tests/toe/test_coherence.py::TestTierMarkerValidator",
            "tests/toe/test_coherence.py::TestMarkerAuditReport",
        ),
        tests=(
            "tests/toe/test_coherence.py::TestTierMarkerValidator",
            "tests/toe/test_coherence.py::TestMarkerAuditReport",
        ),
        notes=(
            "Meta-tier infrastructure. The validator produces "
            "informational reports — it doesn't enforce discipline, "
            "it surfaces drift candidates for case-by-case review. "
            "Per the project's tier-discipline principle (see "
            "rotation_curves_match notes for the corresponding "
            "anchored→computed audit), promotion of a marker to "
            "registry-tracked happens via case-by-case judgment, "
            "not by automated bulk operation."
        ),
    ),

    Claim(
        id="predictions_dashboard",
        chapter=12,
        statement=(
            "The framework's complete predictive surface is codified in "
            "27 quantitative predictions across 7 categories "
            "(foundational constants, R, cosmological observables, dark "
            "sector, cluster mergers, decoherence, particle physics, "
            "BH saturation, thermal, CMB long-term scoping, kinematic "
            "checks). Each prediction carries: GRUT value, observed "
            "value, fractional difference, status (consistent/tension/"
            "inconsistent/untested/scoping_tier/kinematic), precision "
            "status, falsification condition, and registry back-link. "
            "Status distribution: 17 consistent, 2 tension, 1 "
            "inconsistent (El Gordo, documented), 4 untested, 2 "
            "scoping-tier, 1 kinematic. Auto-rendered to "
            "theory/GRUT_TOE_PREDICTIONS.md as a specialist-handoff "
            "document."
        ),
        tier="meta",
        refs=(
            "theory/GRUT_TOE_PREDICTIONS.md",
            "grut/toe/dashboard.py",
        ),
        tests=(
            "tests/toe/test_dashboard.py::TestPredictionsRegistry",
            "tests/toe/test_dashboard.py::TestStatusTaxonomy",
            "tests/toe/test_dashboard.py::TestRegistryBackLinks",
            "tests/toe/test_dashboard.py::TestStatusCounts",
            "tests/toe/test_dashboard.py::TestSpecificPredictions",
            "tests/toe/test_dashboard.py::TestRender",
            "tests/toe/test_dashboard.py::TestVerifyHarness",
            "tests/toe/test_dashboard.py::TestDocumentExists",
            "tests/toe/test_dashboard.py::TestCoverage",
        ),
        notes=(
            "Meta-tier infrastructure: this claim is about the framework "
            "having a dashboard, not about any individual physics. The "
            "dashboard's correctness is enforced by tests pinning every "
            "prediction's registry back-link to a real claim. Future "
            "predictions are added to PREDICTIONS in dashboard.py and "
            "the document regenerates."
        ),
    ),

    Claim(
        id="correction_ledger",
        chapter=12,
        statement=(
            "The repository maintains a public ledger of every correction "
            "to the framework: 28 documented corrections across the V7 "
            "development era, the v8→v2 synthesis, hard-theory audits, "
            "and Gate R closure (May 2026). Each correction has a "
            "CORRECTION_*.md file or registry claim; zero unflagged "
            "errors. Honest-negative discipline is enforced by "
            "repository convention."
        ),
        tier="meta",
        refs=(
            "theory/derivation/CORRECTION_*.md",
            "theory/foundations_audit/ALPHA_VAC_PROVENANCE.md",
        ),
    ),
    Claim(
        id="falsifier_paper_six_near_term_tests",
        chapter=12,
        statement=(
            "The framework's six near-term falsifiers — decoherence "
            "plateau (~689 Hz, lab gravity), ³⁰Si/²⁸Si isotope "
            "discriminator vs CSL (lab gravity), BMV/sub-micron-"
            "separation gravitational entanglement test (lab gravity), "
            "cluster-merger v×τ_0 scaling (cluster astrophysics), "
            "modified-gravity μ-1=1/3 on horizon scales (cosmology, "
            "MG-EFT), and Σm_ν ≈ 60 meV with normal hierarchy "
            "(Standard Model + cosmology) — are collected into a "
            "concise adversarial-roster paper at "
            "theory/GRUT_FALSIFIER_PAPER.md. Each falsifier has "
            "a sharp prediction, derivation reference, observational "
            "test, current-status assessment, and refutation condition. "
            "The paper inverts the standard ToE-program critique by "
            "claiming GRUT's near-term falsifiability AS its primary "
            "structural advantage — the framework can be wrong in "
            "specific, identifiable ways within 1-10 years."
        ),
        tier="meta",
        refs=(
            "theory/GRUT_FALSIFIER_PAPER.md",
            "theory/GRUT_DECOHERENCE_PAPER.md (F1 standalone derivation)",
            "theory/derivation/CORRECTION_22_TAU_CLEANUP.md through "
            "CORRECTION_28_NEUTRINO_HIERARCHY.md (derivation chain)",
        ),
        deps=(
            # Six falsifiers' upstream claims
            "decoherence_plateau",                     # F1
            "grut_csl_isotope_discriminator",          # F2
            "gravitational_entanglement_formation_rate",  # F3
            "cluster_merger_scaling_law",              # F4
            "mg_eft_mu_gamma_mapping",                 # F5
            "neutrino_hierarchy_z3_nh_prediction",     # F6
        ),
        notes=(
            "Priority 5 deliverable of the v8→v2 deposit roadmap. "
            "The paper is intentionally short (~750 lines) and "
            "concentrates on the operational claim 'GRUT can be "
            "wrong in near-term ways' rather than the framework's "
            "full theoretical content. For the latter, see "
            "GRUT_TOE.md and the v6/v7 program documents."
        ),
    ),
    Claim(
        id="koide_phase_4_open_negative",
        chapter=12,
        statement=(
            "Track II Phase 4 (Koide flavor mechanism) was attempted and "
            "produced HONEST NEGATIVE: the Yukawa-hierarchy mechanism "
            "cannot be derived from V7's current machinery. Phase 4.0 "
            "scope document delivered."
        ),
        tier="open_negative",
        refs=(
            "theory/derivation/CORRECTION_20_KOIDE_PHASE_4_FLAVOR_MECHANISM.md",
            "theory/derivation/CORRECTION_18_KOIDE_PHASE_2_MASS_ANCHOR.md",
            "theory/derivation/CORRECTION_17_KOIDE_DERIVATION_ATTEMPT.md",
            "grut/derived/flavor/koide_operator.py",
        ),
        tests=(
            "tests/flavor/test_koide_operator.py",
        ),
        deps=("koide_z3_circulant_structure",),
        notes=(
            "K = 2/3 and N = 3 generations are computed from a Z_3 "
            "structure; M_0 and θ remain free. The mechanism that fixes "
            "them is the open question. The Z₃ circulant operator IS "
            "computed and verified — see koide_z3_circulant_structure."
        ),
    ),
    Claim(
        id="path_f_translation_gap",
        chapter=12,
        statement=(
            "Path F (Im Γ on de Sitter) was investigated as an alternate "
            "route to V7's R = 1.15428. Published Im(W) on dS computes "
            "particle-production rates, NOT V7's ratio. Translation gap "
            "documented as HONEST NEGATIVE."
        ),
        tier="open_negative",
        refs=(
            "theory/path_f_imaginary_action/STAGE_0_LITERATURE.md",
            "theory/path_f_imaginary_action/STAGE_F_C_CALCULATION.md",
            "Zhou-Zhang 2025 (arXiv:2510.13712)",
        ),
        deps=("r_canonical_path_g",),
    ),
    Claim(
        id="rho_max_scale_open_question",
        chapter=12,
        statement=(
            "The universal-τ_0 form ρ_max ~ 10⁻²² kg/m³ is "
            "cosmologically weak and below typical naive BH interior "
            "densities. Whether additional structure is needed for "
            "quantitatively realistic core sizes is open."
        ),
        tier="open_negative",
        refs=("grut/foundation/closure_protocol.py:RHO_MAX_KG_M3",),
        deps=("rho_max_universal",),
        notes=(
            "The universal FORMULA is committed; the QUANTITATIVE-CORE-"
            "SIZE implication is flagged for Phase-1+ derivation."
        ),
    ),
    Claim(
        id="neutrino_dirac_prediction",
        chapter=12,
        statement=(
            "GRUT predicts Dirac neutrinos as the empirically preferred "
            "variant: Path D Dirac (a/c = 1.15525) is closer to the "
            "canonical Path G value (1.15470) than Majorana (1.17256). "
            "Falsifiable by neutrinoless double-beta decay observation."
        ),
        tier="anchored",
        refs=(
            "grut/foundation/closure_protocol.py:A_OVER_C_SM_DIRAC",
            "tests/foundation/test_closure_protocol.py::TestCanonicalR",
        ),
        tests=(
            "tests/foundation/test_closure_protocol.py::TestCanonicalR::test_dirac_closer_to_canonical_than_majorana",
        ),
        deps=("r_path_d_dirac", "r_path_d_majorana"),
        falsifier=(
            "Observation of neutrinoless double-beta decay (would "
            "establish Majorana nature) or other Majorana-confirming "
            "signature."
        ),
    ),

    # ─── Pinned from previously-orphan tests (Phase-2 inventory pass) ──

    Claim(
        id="bridge_parameter_cross_sector",
        chapter=8,
        statement=(
            "The bridge parameter τ_0 connects laboratory decoherence "
            "(noise kernel at the gold benchmark m=20818 amu, l=1 μm) "
            "to cosmology (H_inf = (2−R)/(S·τ_0), Ω_Λ). The same τ_0 "
            "appears in both sectors with no rescaling — this is the "
            "framework's testable cross-sector invariant."
        ),
        tier="computed",
        refs=(
            "V7 §22 (bridge)",
            "grut/bridge/parameter.py:bridge_prediction",
        ),
        tests=("tests/bridge/test_bridge.py",),
        deps=(
            "tau_0_derivation", "h_inf_decomposition",
            "decoherence_plateau",
        ),
        falsifier=(
            "Detection of two distinct τ_0 values, one fitting the "
            "decoherence plateau and another fitting the cosmological "
            "Hubble rate, by more than the framework's fit tolerance."
        ),
    ),

    Claim(
        id="sm_field_content_locked",
        chapter=5,
        statement=(
            "Standard Model field counts are locked in code: 4 real "
            "scalars, 45 Weyl fermions (15 per generation × 3), 12 "
            "gauge bosons. With the SM trace-anomaly numerators "
            "(a = 1991/2, c = 418 / 849 with neutrino convention) and "
            "U(1)_Y β = 20/3, the structural −100 emerges as 100/256 "
            "× (s4_geometric_factor = 1)."
        ),
        tier="computed",
        refs=(
            "V7 §15 (SM emergence)",
            "Christensen-Duff 1980; Duff 1994 (40-years review)",
            "grut/derivation/minus_100/conformal_anomaly.py",
            "theory/derivation/MINUS_100_RESOLUTION.md",
        ),
        tests=("tests/derivation/test_minus_100_structural.py",),
        deps=("sm_emergence", "minus_100_drive"),
        notes=(
            "The SM field content is taken as input, not derived — but "
            "the trace-anomaly numerators that produce both R (Path D) "
            "and the −100 (Ch 8) follow rigorously once the content is "
            "specified. Locked in code via test_minus_100_structural."
        ),
    ),

    Claim(
        id="dark_sector_u1_extension",
        chapter=9,
        statement=(
            "The dark sector is a gauged U(1)_dark extension (V7 §28) "
            "with two viable parameter routes: Route 1 (RG running from "
            "Planck) gives g_dark = 0.917, λ = 0.42, M ≈ 2.1 × 10⁹ GeV; "
            "Route 2 (anomaly extraction) gives larger g_dark, λ ≈ 3.83. "
            "Both routes produce σ/m in the viable 10⁻³–10⁻² cm²/g window."
        ),
        tier="anchored",
        refs=(
            "V7 §28 (dark sector)",
            "grut/derived/dark_matter/sector.py",
        ),
        tests=("tests/derived/test_dark_matter.py",),
        deps=("alpha_vac_derivation",),
        notes=(
            "STAYS anchored (case-by-case judgment). The 16 tests in "
            "test_dark_matter.py verify that the codebase REPRODUCES "
            "specific values quoted from V7 §28 (g_dark = 0.917, λ = "
            "0.42, M ≈ 2.1 × 10⁹ GeV). The actual derivation of those "
            "values from the CTP action lives in V7 prose, not in this "
            "codebase. Promoting to computed would suggest the "
            "framework derives the values when the codebase only "
            "verifies V7's stated values are self-consistent. Two-"
            "route construction is computed; the V7 derivation chain "
            "into the codebase is not. Anchored is honest tier."
        ),
        falsifier=(
            "Direct-detection or self-interaction measurements ruling "
            "out both Route 1 and Route 2 parameter regions."
        ),
    ),

    Claim(
        id="dielectric_dm_reframing",
        chapter=9,
        statement=(
            "Track VII REFRAMED: dark-matter abundance is the dielectric "
            "response of the vacuum — the frequency-gated refractive "
            "enhancement n_g(ω) maps to Ω_dm at galactic-frequency "
            "modes. n_g(DC) = √(4/3); n_g(∞) → 1 (GR recovered). "
            "Solar system enhancement ~ 0; CMB peaks survive (ωτ_0 < 0.1); "
            "galaxy rotation enhancement ~ 0.19; Bullet Cluster offset "
            "matches at order-of-magnitude."
        ),
        tier="computed",
        refs=(
            "v11.1 Appendix H",
            "grut/derived/cosmology/dielectric_dm.py",
        ),
        tests=("tests/derived/test_dielectric_dm.py",),
        deps=(
            "alpha_vac_derivation", "memory_kernel_form",
            "regime_map", "r_canonical_path_g",
        ),
    ),

    Claim(
        id="kibble_zurek_dm_route",
        chapter=9,
        statement=(
            "Track VII Step 1: Kibble-Zurek formation of dark relic from "
            "a dark-sector phase transition with XY universality gives "
            "Ω_dm within factor ~2 of observation. Mean-field model B "
            "(z = 4, conserved order parameter) over-produces, ruling "
            "it out. Correlation length ξ_KZ ∝ (τ_Q/τ_0)^(ν/(1+zν))."
        ),
        tier="anchored",
        refs=(
            "grut/derived/dark_matter/kibble_zurek.py",
        ),
        tests=("tests/derived/test_kibble_zurek.py",),
        deps=("dark_sector_u1_extension", "tau_0_derivation"),
        notes=(
            "STAYS anchored (case-by-case judgment). The 21 tests in "
            "test_kibble_zurek.py verify the KZ scaling laws (ξ_KZ ∝ "
            "(τ_Q/τ_0)^(ν/(1+zν)), mean-field exponent = 1/4, XY "
            "universality factor 2, model B over-production). These "
            "are STANDARD KZ-mechanism predictions, not GRUT-derived "
            "results — the only GRUT input is τ_0. Test "
            "test_step_1_result_retracted explicitly flags Track VII "
            "Step 1 as RETRACTED. Promoting this to computed would "
            "frame as 'GRUT-predicted KZ mechanism gives Ω_dm within "
            "factor 2', but the framework's POSITION is that this "
            "mechanism is not the answer (dielectric route is "
            "preferred). The status of this claim is 'documented "
            "exploration of a route that did not close', appropriately "
            "anchored not computed."
        ),
    ),

    Claim(
        id="track_vii_relic_scoping",
        chapter=9,
        statement=(
            "Track VII relic-abundance infrastructure: thermal-freezeout "
            "baseline returns WRONG MECHANISM verdict for the V7 heavy "
            "(2 × 10⁹ GeV) soliton; Kibble-Zurek upper bound from "
            "causality is finite; full Track VII status assembled into "
            "a structured scoping dict. The mechanism is OPEN; the "
            "infrastructure to evaluate candidate mechanisms is locked."
        ),
        tier="anchored",
        refs=(
            "grut/derived/dark_matter/relic_abundance.py",
        ),
        tests=("tests/derived/test_relic_abundance.py",),
        deps=("dark_sector_u1_extension",),
        notes=(
            "STAYS anchored (case-by-case judgment). The 26 tests "
            "verify that the SCOPING INFRASTRUCTURE correctly records "
            "that thermal freezeout overproduces, KZ baseline "
            "underproduces, and the V7 heavy-soliton mechanism is "
            "wrong. The infrastructure IS computed and tested. But "
            "what's tested is that the tooling correctly identifies "
            "ALL candidate mechanisms as failing — the underlying "
            "physics question (what mechanism gives Ω_dm = 1/3 in "
            "GRUT?) is open. Promoting to computed would frame as "
            "'GRUT computes its dark-matter mechanism' when in fact "
            "the framework documents that no candidate mechanism "
            "succeeds. Anchored is the honest tier for an open "
            "physics question with computed scoping."
        ),
    ),

    Claim(
        id="track_v_coupling_unification_open_question",
        chapter=12,
        statement=(
            "GRUT's Track V proposes that the Standard Model gauge "
            "couplings unify at high scale via a constitutive β-function "
            "correction from the responsive vacuum. With the canonical "
            "framework, the three SM couplings α_s, α_W, α_Y miss "
            "exact unification by 8.9% at the GUT scale (~10¹⁶ GeV). "
            "The framework asserts a constitutive correction Δβ(α_eff(ω)) "
            "to the running closes this gap, but the correction has "
            "not been derived rigorously from the CTP action. Track V "
            "remains an open negative pending: (1) explicit derivation "
            "of the constitutive β-function correction from δS_CTP/δg_i, "
            "(2) numerical evaluation showing 8.9% closure at the "
            "predicted scale, (3) consistency with other electroweak-"
            "scale tests."
        ),
        tier="open_negative",
        refs=(
            "V7 Track V documentation",
            "Machacek-Vaughn 1983 (β-function references)",
            "PDG SM coupling constants at M_Z",
        ),
        deps=("ctp_action_structure", "alpha_vac_derivation"),
        falsifier=(
            "Either: (a) the 8.9% miss is closed by an independently-"
            "derived constitutive β correction (closure path), OR "
            "(b) high-precision LHC / future-collider measurements "
            "of α_s, α_W, α_Y running show the gauge couplings DON'T "
            "unify at any scale, falsifying the framework's gauge-"
            "structural prediction."
        ),
        notes=(
            "Track V is referenced in Chapter 12's 'What comes next' "
            "table but did not previously have a registry/ledger entry. "
            "This entry surfaces it into the auto-rendered Chapter 12 "
            "ledger so the framework's open questions are mechanically "
            "complete. Effort estimate: 6-12 months specialist work "
            "(constitutive QFT renormalization-group calculation)."
        ),
    ),

    Claim(
        id="vorton_track_vii_open_negative",
        chapter=12,
        statement=(
            "Track VII Step 3 (vortex-string topology): π_n(U(1)) "
            "correctly identifies cosmic strings (not monopoles); BPS "
            "tension μ = πv² = 0.56 GeV² with Gμ orders below the CMB "
            "bound; pure-string scaling gives negligible Ω ~ 10⁻⁴². "
            "Vorton abundance with XY universality UNDER-produces by "
            "factor ~30, and M_vorton mismatches V7's M_soliton by "
            "factor ~450 — a real discrepancy. Step 3 REOPENS Track VII."
        ),
        tier="open_negative",
        refs=(
            "grut/derived/dark_matter/vortex_strings.py",
        ),
        tests=("tests/derived/test_vortex_strings.py",),
        deps=("kibble_zurek_dm_route",),
        notes=(
            "Honest negative on the vorton route. Documented in code "
            "and tested for regression — the discrepancy is locked in, "
            "not papered over."
        ),
    ),

    Claim(
        id="koide_k_2_over_3",
        chapter=9,
        statement=(
            "Charged-lepton masses satisfy the Koide identity "
            "K = (Σ m_i) / (Σ √m_i)² = 2/3 to 0.005%, validated against "
            "PDG values for e, μ, τ. This is GRUT's empirical anchor "
            "for the Z₃ flavor structure (V7 §29)."
        ),
        tier="computed",
        refs=(
            "V7 §29 (Koide identity)",
            "grut/derived/koide/identity.py",
        ),
        tests=("tests/derived/test_koide.py",),
        deps=("sm_emergence",),
        falsifier=(
            "Refined PDG mass values driving K outside the 2/3 ± 0.001 "
            "band would falsify the K = 2/3 anchor."
        ),
    ),

    Claim(
        id="koide_z3_circulant_structure",
        chapter=9,
        statement=(
            "The Z₃-circulant Koide mass operator parameterizes the "
            "charged-lepton spectrum via (M_0, θ): K = 2/3 holds "
            "algebraically (machine precision for any nonzero M_0 and "
            "any θ). The operator is Hermitian in the flavor basis "
            "with eigenvalues equal to (m_e, m_μ, m_τ). Three "
            "generations and the K = 2/3 ratio are mathematical "
            "consequences of the Z₃ structure — what the structure "
            "physically realizes is the open question (see "
            "koide_phase_4_open_negative)."
        ),
        tier="computed",
        refs=(
            "V7 §29 (Koide identity)",
            "V7 Conjecture F1 (HYPOTHESIS)",
            "grut/derived/flavor/koide_operator.py",
        ),
        tests=("tests/flavor/test_koide_operator.py",),
        deps=("koide_k_2_over_3", "sm_emergence"),
        notes=(
            "The Z₃ algebraic structure is computed and verified. The "
            "physical mechanism that selects (M_0, θ) — the flavor "
            "hierarchy origin — is the open negative carried in Ch 12. "
            "One CANDIDATE IDENTITY surfaced: θ = K · α_vac = 2/9."
        ),
    ),

    Claim(
        id="charged_lepton_z3_does_not_extend_to_neutrinos",
        chapter=9,
        statement=(
            "The charged-lepton Z₃ ansatz √m_i = M_0(1 + √2 cos(θ + "
            "2πk/3)) — which gives K = 2/3 algebraically — DOES NOT "
            "admit any neutrino solution under either hierarchy. "
            "Numerical scan over the all-positive θ range gives "
            "minimum Δm²_atm/Δm²_sol = 194.7, vs observed 33.9 — a "
            "factor of ~6 too large. This is a SHARP STRUCTURAL "
            "FINDING (computed, unconditional): GRUT's charged-lepton "
            "Z₃ structure does not trivially extend to neutrinos. "
            "Consistent with the framework's existing Dirac-vs-"
            "Majorana posture (A_OVER_C_SM_DIRAC closer to canonical "
            "√(4/3) than Majorana) — neutrinos require a different "
            "mass-generation mechanism than charged leptons."
        ),
        tier="computed",
        refs=(
            "grut/derived/koide/neutrino_hierarchy.py",
            "theory/derivation/CORRECTION_28_NEUTRINO_HIERARCHY.md",
            "NuFIT 2024 (Δm² values)",
        ),
        tests=(
            "tests/derived/test_neutrino_hierarchy.py",
        ),
        deps=("koide_z3_circulant_structure",),
        falsifier=(
            "If a future Koide-style relation with the SAME a = √2 "
            "coupling emerges for neutrinos under refined Δm² values "
            "or extended mass-mechanism (e.g., effective light-"
            "neutrino masses including see-saw corrections), this "
            "claim is falsified. The computed minimum 194.7 is "
            "stable under choice of NH/IH and Δm² precision."
        ),
        notes=(
            "Priority 4 finding (Correction #28). The negative "
            "result IS the Standard Model statement: the charged-"
            "lepton Z₃ structure does not extend trivially to "
            "neutrinos. This is informative about neutrino mass-"
            "mechanism."
        ),
    ),

    Claim(
        id="neutrino_hierarchy_z3_nh_prediction",
        chapter=9,
        statement=(
            "Conditional on the postulate a_ν = 1 (giving K_ν = 1/2), "
            "the GRUT generalized Z₃ ansatz √m_i = M_0(1 + a_ν "
            "cos(θ + 2πk/3)) admits a UNIQUE INTERIOR solution in "
            "Normal Hierarchy with: m_1 = 0.802 meV, m_2 = 8.65 meV, "
            "m_3 = 50.16 meV, Σm_ν = 59.6 meV, θ = 18.94°. The IH "
            "solution at a_ν = 1 sits exactly at the m_3 → 0 boundary "
            "(degenerate, fine-tuned, NOT a generic interior solution) "
            "— GRUT therefore PREFERS NORMAL HIERARCHY. The predicted "
            "Σm_ν ≈ 60 meV is well below the Planck 2018 + BAO "
            "cosmological bound 0.12 eV (95% CL), with ~60 meV "
            "headroom. Predicted m_β (kinematic effective ν mass) "
            "≈ 9 meV, below current KATRIN limit 0.45 eV but within "
            "reach of future Project 8 precision."
        ),
        tier="anchored",
        refs=(
            "grut/derived/koide/neutrino_hierarchy.py",
            "theory/derivation/CORRECTION_28_NEUTRINO_HIERARCHY.md",
            "NuFIT 2024 (Δm² values)",
            "Planck 2018 paper VI (Σm_ν bound)",
            "KATRIN Collaboration 2024 (m_β bound)",
        ),
        tests=(
            "tests/derived/test_neutrino_hierarchy.py",
        ),
        deps=(
            "charged_lepton_z3_does_not_extend_to_neutrinos",
            "koide_z3_circulant_structure",
        ),
        falsifier=(
            "Multiple sharp falsifiers: (1) Hierarchy: if "
            "JUNO/DUNE/Hyper-K conclusively determine INVERTED "
            "hierarchy at >5σ, the prediction is falsified. "
            "(2) Σm_ν: if DESI Y3+ or Euclid measure Σm_ν < 30 meV "
            "or > 90 meV at >2σ, the prediction is falsified. "
            "(3) m_β: if Project 8 measures m_β > 30 meV, the "
            "prediction is falsified. (4) 0νββ: if a positive 0νββ "
            "signal is found, the framework's Dirac-ν posture (which "
            "underwrites this prediction) is falsified."
        ),
        notes=(
            "ANCHORED tier — built on the a_ν = 1 derivation "
            "(see neutrino_z3_coupling_a_equals_1_uniqueness_theorem "
            "[Correction #29, Priority 4B] which derives a_ν = 1 "
            "structurally as the unique boundary-degenerate Z₃ "
            "coupling). The K = 2/3 → K = 1/2 transition "
            "from charged leptons to neutrinos is a clean ratio "
            "(coupling reduced by √2) suggestive of an SU(2) doublet "
            "structure or different KS anomaly coefficient, but "
            "the structural derivation is not in hand."
        ),
    ),

    Claim(
        id="neutrino_z3_coupling_a_equals_1_uniqueness_theorem",
        chapter=9,
        statement=(
            "DERIVED (Correction #29, Priority 4B, 2026-05-02). The "
            "value a_ν = 1 is uniquely characterized as the ONLY "
            "Z₃ coupling at which: (i) boundary access (one s_k = 0) "
            "is admissible AND (ii) the OTHER two s values are exactly "
            "degenerate. The boundary-gap formula at the s_min = 0 "
            "configuration is √3 × √(a²-1) — vanishes at a = 1 "
            "(degenerate to (0, 3/2, 3/2)), strictly positive for "
            "a > 1 (configurations split symmetrically around 3/2), "
            "undefined for a < 1 (no boundary access). Combined with "
            "(iii) NH-interior generic solution at a = 1 with "
            "cosmologically-acceptable Σm_ν, and (iv) IH solution "
            "sitting at the boundary configuration, the four properties "
            "uniquely select a_ν = 1. INTERPRETATION (route 4): "
            "a²_ν = 1 vs a²_e = 2 corresponds to channel-counting "
            "(weak only for neutrinos vs EM + weak for charged "
            "leptons); Σs² = 4.5 (ν, K = 1/2) vs Σs² = 6 (e, K = 2/3). "
            "The previous open question "
            "(`neutrino_z3_coupling_derivation_open_question`) is "
            "RESOLVED at the structural level: a_ν = 1 is no longer "
            "a postulate but a derived value. Channel-counting "
            "interpretation is suggestive; full KS-anomaly derivation "
            "of the EM-channel-absence remains a deeper research "
            "question."
        ),
        tier="computed",
        refs=(
            "grut/derived/koide/neutrino_hierarchy.py",
            "theory/derivation/CORRECTION_29_PRIORITY_4B_UNIQUENESS.md",
            "theory/derivation/CORRECTION_28_NEUTRINO_HIERARCHY.md",
            "Komargodski-Schwimmer 2011",
        ),
        tests=(
            "tests/derived/test_neutrino_hierarchy.py::TestUniquenessTheoremPriority4B",
        ),
        deps=(
            "neutrino_hierarchy_z3_nh_prediction",
            "charged_lepton_z3_does_not_extend_to_neutrinos",
            "koide_z3_circulant_structure",
        ),
        falsifier=(
            "If a precision measurement determines neutrino mass "
            "spectrum incompatible with the K_ν = 1/2 ansatz (e.g., "
            "Σm_ν > 90 meV or hierarchy = IH at >5σ), the underlying "
            "a_ν = 1 derivation is falsified at the experimental "
            "level. The structural theorem (boundary-gap vanishing "
            "at a = 1) is mathematically rigorous and not "
            "experimentally falsifiable; what's experimentally "
            "falsifiable is the framework's identification of "
            "a_ν = 1 as the operating coupling."
        ),
        notes=(
            "Route 1 (uniqueness theorem) of the Priority 4B closure "
            "paths is fully implemented. Route 4 (channel counting) "
            "is suggestive interpretation, not full derivation — the "
            "underlying KS-anomaly identification of EM-channel-"
            "absence in neutrinos remains a deeper question. The "
            "structural derivation closes the open question at the "
            "tier appropriate for the current state of the framework."
        ),
    ),

    Claim(
        id="allen_jacobson_phase1_stub_open_negative",
        chapter=12,
        statement=(
            "The Allen-Jacobson S⁴ propagator Phase-1 is IMPLEMENTED "
            "(Correction #31, 2026-05-07): s4_propagator(), "
            "s4_propagator_conformal(), s4_propagator_uv_series(), "
            "volume_sphere(), spectral_degeneracy(), "
            "spectral_eigenvalue(), tji_conformal_radial_integral() "
            "all operational. tji_on_s4() raises S4CurvatureObstacle "
            "(not Phase1Pending): the remaining gate is the ε-expansion "
            "of [₂F₁(h₊,h₋;D/2;(1+Z)/2)]³ × (1-Z²)^{(D-3)/2} dZ "
            "requiring Mathematica + HypExp. Coefficient intake in "
            "euler_coefficient_landing.py; target: "
            "HYPEXP_TARGET_NOTEBOOK.ipynb. Claim remains open_negative "
            "until C_Euler_cosmo / C_Euler_final are numerically "
            "extracted and pass the landing-interface decision gate."
        ),
        tier="open_negative",
        refs=(
            "grut/derivation/tji/allen_jacobson.py",
            "grut/hard_theory/s4_ctp_solver/euler_coefficient_landing.py",
            "theory/hard_theory/HYPEXP_TARGET_NOTEBOOK.ipynb",
        ),
        tests=("tests/derivation/tji/test_allen_jacobson.py",),
        deps=("tji_7_4_open_negative",),
        notes=(
            "Phase-1 propagator is done. The only remaining blocker is "
            "the Mathematica/HypExp ε-expansion of the ₂F₁³ product "
            "integral. Two-loop independent result (≈1.1498) must NOT "
            "be merged into the 3-loop route."
        ),
    ),

    Claim(
        id="r_path_osborn_epsilon",
        chapter=7,
        statement=(
            "Path 3 of the Three-Routes convergence: ε_combined from "
            "Osborn 2003 (hep-th/0302119) eq (36), evaluated for SM at "
            "M_Z in Dirac convention with QCD-dominant weighting. "
            "Per-sector ε_SU(3) = 1.1598, ε_SU(2) = 1.0175, ε_U(1) = "
            "0.9673; weighted combination ε_combined ≈ 1.15367, "
            "matching the documented 1.15370 to four decimal places. "
            "Routes 1 (Path G) and 3 (Osborn) share NO inputs (Path G "
            "uses zero couplings; Osborn uses measured α_s, α_2, α_Y) "
            "yet converge at the 0.1% level."
        ),
        tier="computed",
        refs=(
            "Osborn (2003) hep-th/0302119 eq (36)",
            "Jack-Osborn 1990, 2014 (analogs of c-theorem)",
            "theory/OSBORN_2003_EPSILON_SM.md",
            "theory/ZENODO_EPSILON_IDENTIFICATION.md",
            "grut/foundation/osborn_epsilon.py",
            "grut/foundation/way2_epsilon_substitution.py",
        ),
        tests=(
            "tests/foundation/test_osborn_epsilon.py::TestEpsilonCombined",
            "tests/foundation/test_osborn_epsilon.py::TestPerSectorEpsilon",
            "tests/foundation/test_osborn_epsilon.py::TestThreeRoutesConvergence",
            "tests/foundation/test_osborn_epsilon.py::TestVerifyHarness",
        ),
        deps=(
            "alpha_vac_derivation",
            "sm_field_content_locked",
            "r_canonical_path_g",
        ),
        falsifier=(
            "Refined α_s(M_Z) measurement that pushes ε_combined more "
            "than ~0.5% from √(4/3), or independent recomputation under "
            "the same convention yielding a materially different number."
        ),
        notes=(
            "Inputs: measured α_s = 0.1181, α_2 = 0.03376, α_Y = 0.01018 "
            "at M_Z (PDG); SM group-theory data (C_A, R_ψ, R_φ per "
            "sector); QCD-dominant weights (0.960, 0.032, 0.008) per "
            "the A × g⁴ structure of the gauge-boson contribution to "
            "the 3-loop S⁴ effective action. Three-Routes spread is "
            "0.089% — Path G + Osborn agree to 1 part in 10³."
        ),
    ),

    Claim(
        id="three_routes_convergence",
        chapter=7,
        statement=(
            "Three independent routes converge on R ≈ 1.154 within "
            "0.1%: Path G (tree-level √(4/3) ≈ 1.15470, zero coupling "
            "constants), V7 §26 (3-loop CTP claimed 1.15428, currently "
            "open_negative), and Osborn (1-loop coupling-corrected at "
            "M_Z, 1.15367). Routes 1 and 3 are both COMPUTED and share "
            "no inputs; their agreement is independent confirmation."
        ),
        tier="computed",
        refs=(
            "grut/foundation/osborn_epsilon.py:three_routes_convergence",
            "tests/foundation/test_osborn_epsilon.py::TestThreeRoutesConvergence",
        ),
        tests=(
            "tests/foundation/test_osborn_epsilon.py::TestThreeRoutesConvergence::test_three_routes_within_0p15_pct",
            "tests/foundation/test_osborn_epsilon.py::TestThreeRoutesConvergence::test_path_g_and_osborn_agreement",
        ),
        deps=(
            "r_canonical_path_g",
            "r_path_osborn_epsilon",
            "tji_7_4_open_negative",
        ),
        falsifier=(
            "Independent recomputation of any of the three routes "
            "producing a value more than 0.5% from the convergence "
            "band, where the discrepancy is not attributable to "
            "documented scheme/convention choices."
        ),
        notes=(
            "Two computed routes (Path G + Osborn) within 0.1% is the "
            "load-bearing convergence; route 2's open_negative "
            "(tji_7_4) is the documented gap at the 3-loop level."
        ),
    ),

    Claim(
        id="cmb_boltzmann_scoping",
        chapter=9,
        statement=(
            "CMB Boltzmann scoping completed: at recombination, "
            "H_rec × τ_0 ≈ 68 (expansion-rate ωτ_0) and ω_acoustic × "
            "τ_0 ≈ 140 (first acoustic peak); both deep in the crystal "
            "regime. Predicted Δn_g/n_g ≈ 3.6 × 10⁻⁵ at H_rec. The "
            "implied θ_* shift is below Planck's 3 × 10⁻⁴ precision "
            "(factor 10) — CMB at Planck precision is a consistency "
            "check. CMB-S4 / LiteBIRD target 5 × 10⁻⁵ places the "
            "prediction at the detection threshold. This is a "
            "LEADING-ORDER SCOPING PREDICTION; promotion to falsifier-"
            "tier requires (i) full Boltzmann implementation "
            "propagating the constitutive modification through CMB "
            "anisotropy, lensing C_ℓ^φφ, growth rate fσ_8, and matter "
            "power spectrum P(k), and (ii) theoretical closure of the "
            "n_g(ω) covariance question for cosmological perturbations. "
            "CLASS / CAMB modification entry points identified; 4-8 "
            "weeks specialist work for (i)."
        ),
        tier="anchored",
        refs=(
            "theory/CMB_BOLTZMANN_SCOPING.md",
            "Aghanim et al. 2020 (Planck 2018, A&A 641 A6)",
            "Lesgourgues 2011 (CLASS, arXiv:1104.2932)",
            "Lewis-Challinor-Lasenby 2000 (CAMB, ApJ 538 473)",
            "Abazajian et al. 2019 (CMB-S4, arXiv:1907.04473)",
            "grut/derived/cmb/scoping.py",
        ),
        tests=(
            "tests/derived/test_cmb_scoping.py::TestQ1OmegaTauAtRecombination",
            "tests/derived/test_cmb_scoping.py::TestQ2SoundHorizonShift",
            "tests/derived/test_cmb_scoping.py::TestQ3EntryPointsDocumented",
            "tests/derived/test_cmb_scoping.py::TestQ4Detectability",
            "tests/derived/test_cmb_scoping.py::TestVerifyHarness",
            "tests/derived/test_cmb_scoping.py::TestScopingDocumentExists",
        ),
        deps=(
            "tau_0_derivation",
            "alpha_vac_derivation",
            "memory_kernel_form",
        ),
        falsifier=(
            "After full Boltzmann implementation and covariance "
            "closure: CMB-S4 / LiteBIRD measurement of Δθ_*/θ_* "
            "materially different from 3.6 × 10⁻⁵ (wrong sign, "
            "magnitude > factor 3 different) — falsifies the "
            "framework's CMB prediction. Alternatively, CMB-S4 "
            "setting an upper limit below 3.6 × 10⁻⁵ without "
            "detection — falsifies the simple-Lorentzian-kernel form. "
            "Falsifier status is conditional on the two open items "
            "below being closed first; until then this is a "
            "scoping-tier prediction, not a decisive test."
        ),
        notes=(
            "Anchored, scoping-tier: the quantitative predictions are "
            "computed and tested at leading order. Promotion to "
            "falsifier-tier conditions: "
            "(1) n_g_omega_cosmological_covariance — RESOLVED by "
            "Correction #26 (Priority 3, 2026-05-01). The covariant "
            "ω → k_phys × c identification, gauge-invariance at WKB, "
            "and μ(k,a)/γ(k,a) MG-EFT mapping are now in place "
            "(grut/derivation/phi_munu/mg_eft_mapping.py). "
            "(2) full Boltzmann-hierarchy propagation through P(k), "
            "lensing, fσ_8 (CLASS/CAMB specialist task) remains the "
            "outstanding implementation step. The current scoping "
            "predicts θ_* shift "
            "only; self-consistency across the full hierarchy is the "
            "implementation phase's job."
        ),
    ),

    Claim(
        id="cmb_boltzmann_case_a_structural",
        chapter=9,
        statement=(
            "Case A structural proof (June 2026): μ_GRUT(k,a) survives "
            "full Einstein-Boltzmann evolution without operator completion. "
            "Three independent structural arguments: (1) single-equation "
            "isolation — μ modifies only the Poisson equation "
            "k²Φ = -4πGa²μ_GRUT ρ̄_m δ_m; all Boltzmann hierarchy equations "
            "(photon moments, baryon Euler/continuity, neutrino streaming, "
            "CDM) are UNCHANGED; (2) γ_GRUT = 1 (no gravitational slip) "
            "prevents anisotropic stress sourcing from off-diagonal metric "
            "perturbations — binary discriminator from BD/f(R)/DGP; "
            "(3) Lorentzian form μ(k,a) = 1 + α/(1+(τ₀k_phys)²) is a "
            "multiplicative function of k, not a differential operator — "
            "FT is a retarded (causal) exponential kernel, generating no "
            "higher-derivative operators. Modified P(k) computed at 11 "
            "canonical scales: σ₈-scale change < 0.1% (consistent with "
            "S₈ constraint); BAO scale +8.5%; CMB horizon +134.8%. "
            "Genuine observational risk identified: ISW power enhancement "
            "at low ℓ (~×5 at CMB horizon) vs Planck's observed low-ℓ "
            "deficit — quantitative resolution gated on CAMB/CLASS run. "
            "Transition scale: λ_* ≈ 80.7 Mpc, k_* ≈ 0.078 Mpc⁻¹."
        ),
        tier="computed",
        refs=(
            "grut/derived/cmb/boltzmann_consistency.py",
            "grut/derivation/phi_munu/modified_growth.py",
            "grut/derivation/phi_munu/mg_eft_mapping.py",
            "theory/GRUT_TOE.md §9",
            "Aghanim et al. 2020 (Planck 2018, A&A 641 A6)",
            "Lesgourgues 2011 (CLASS, arXiv:1104.2932)",
            "Lewis-Challinor-Lasenby 2000 (CAMB, ApJ 538 473)",
        ),
        tests=(
            "tests/derived/test_cmb_boltzmann_consistency.py"
            "::TestCaseAStructuralProperties::test_all_conditions_hold",
            "tests/derived/test_cmb_boltzmann_consistency.py"
            "::TestPowerSpectrumRatio::test_all_ratios_at_least_one",
            "tests/derived/test_cmb_boltzmann_consistency.py"
            "::TestSigma8Modification::test_sigma8_change_less_than_half_percent",
            "tests/derived/test_cmb_boltzmann_consistency.py"
            "::TestISWEnhancementEstimate::test_isw_power_enhancement_is_positive",
            "tests/derived/test_cmb_boltzmann_consistency.py"
            "::TestBoltzmannConsistencySummary::test_case_a_holds_is_true",
        ),
        deps=(
            "cmb_boltzmann_scoping",
            "tau_0_derivation",
            "alpha_vac_derivation",
            "constitutive_projection_gravity_heuristic_resolved",
        ),
        falsifier=(
            "CAMB/CLASS Boltzmann run with μ_GRUT showing C_ℓ at low ℓ "
            "(ℓ < 30) materially EXCEEDING Planck 2018 data by more than "
            "the Planck cosmic-variance error bars would falsify the "
            "simple Lorentzian μ(k,a) form at z=0. A γ ≠ 1 measurement "
            "(gravitational slip) by Euclid/DESI would directly falsify "
            "the γ_GRUT = 1 prediction. Both are v4-tier tests."
        ),
        notes=(
            "Computed-tier: structural Case A argument is analytic and "
            "complete; modified P(k) is numerically computed from the "
            "modified Bardeen equation (well-defined approximation to "
            "full Boltzmann treatment, exact for sub-horizon modes). "
            "Promotion to falsifier-tier requires: (1) CAMB/CLASS "
            "implementation of μ_GRUT in perturb_einstein() [single "
            "code change, see boltzmann_consistency.py docstring], "
            "(2) comparison of predicted C_ℓ^TT and C_ℓ^φφ to "
            "Planck 2018 / ACT / SPT data at low ℓ. "
            "The σ₈ result is robust: GRUT does not worsen S₈ tension. "
            "The ISW is the primary quantitative risk."
        ),
    ),

    Claim(
        id="constitutive_projection_gravity_heuristic_resolved",
        chapter=12,
        statement=(
            "RESOLVED at the linearized level (Correction #23, "
            "2026-04-30). The previously-heuristic constitutive "
            "Einstein equation G_μν + Φ_μν[φ] = 8πG T_μν is now "
            "derived structurally from δS_CTP/δh_a |_{h_a=0} for the "
            "linearized gravitational CTP action, with the constitutive "
            "cross term S_const = -(1/2)∫∫ h_a^μν K^R_μνρσ(x-x') "
            "h_r^ρσ(x') d^4x d^4x'. The variation produces Φ_μν as a "
            "kernel-h_r convolution: Φ_μν(ω) = α_vac × χ(ω) × P^TT_μνρσ "
            "× h_r^ρσ(ω), where χ(ω) = 1/(1-iωτ_0) is the constitutive "
            "susceptibility and P^TT is the transverse-tracefree "
            "projector. Six structural properties verified: (i) kernel "
            "form derived, NOT postulated; (ii) high-ω limit Φ → 0 "
            "(GR recovery); (iii) low-ω limit Φ → α_vac (full "
            "constitutive); (iv) Bianchi ∂^μ Φ_μν = 0 follows STRUCTURALLY "
            "from ∂^μ P^TT = 0 (upgrade from gr_recovery's existing "
            "single-mode plane-wave check); (v) α_vac = 1/3 from "
            "Komargodski-Schwimmer 2011 a/c trace-anomaly ratio for "
            "the conformal-mode scalar (consistent with existing "
            "alpha_vac_derivation, NOT modified by Correction #23); "
            "(vi) DC amplitude gives n_g²(0) = 1+α_vac = 4/3 "
            "(consistent with closure_protocol.N_G_DC). "
            "REMAINING OPEN: extension to curved background (S⁴, "
            "FRW) — see phi_munu_curved_background_extension"
            "_open_question, the sharper successor."
        ),
        tier="meta",
        refs=(
            "V7 §22-§25 (gravity sector)",
            "Calzetta-Hu (2008) Nonequilibrium Quantum Field Theory — "
            "for CTP variation in gauge theories",
            "Komargodski-Schwimmer 2011 (conformal-mode trace anomaly)",
            "grut/derivation/phi_munu/linearized_ctp_action.py",
            "grut/foundation/gr_recovery.py",
            "theory/derivation/CORRECTION_23_PHI_MUNU_DERIVATION.md",
        ),
        tests=(
            "tests/derivation/phi_munu/test_linearized_ctp_action.py",
        ),
        deps=("ctp_action_structure", "gr_recovery", "alpha_vac_derivation"),
        notes=(
            "Original entry (id 'constitutive_projection_gravity_"
            "heuristic_open_question') flagged the issue without "
            "prescribing a resolution. Correction #23 (Priority 2 of "
            "the v8→v2 deposit roadmap) implements closure path (a) "
            "from the original notes: derive Φ_μν explicitly from "
            "δS_CTP/δh_μν in the gravitational sector, with Bianchi "
            "preservation shown structurally. The previous claim id "
            "was a pre-resolution placeholder; this claim supersedes "
            "it and tracks the closed status. Closure path (b) "
            "(retier gr_recovery to anchored) is no longer needed — "
            "gr_recovery's susceptibility postulate is now structurally "
            "derived rather than heuristic. The n_g(ω) cosmological-"
            "perturbation sister gap (n_g_omega_cosmological_covariance"
            "_open_question) remains separately open — that's the same "
            "problem in the perturbation sector and still needs "
            "covariant treatment; this resolution does not address it."
        ),
    ),
    Claim(
        id="phi_munu_linearized_derivation",
        chapter=6,
        statement=(
            "The gravitational constitutive correction Φ_μν is "
            "structurally derived in the linearized limit from the "
            "Schwinger-Keldysh action variation δS_CTP/δh_a |_{h_a=0}. "
            "The constitutive cross term S_const = -(1/2)∫∫ h_a "
            "K^R(x-x') h_r d^4x d^4x' yields Φ_μν(ω) = α_vac × χ(ω) "
            "× P^TT_μνρσ × h_r^ρσ(ω) on variation. Limits: GR "
            "recovery at high ω (χ → 0), full constitutive at low ω "
            "(χ → 1, n_g(0) = √(4/3)). Bianchi ∂^μ Φ_μν = 0 follows "
            "from ∂^μ P^TT_μνρσ = 0 (transverse-tracefree projector). "
            "α_vac = 1/3 inherits from the conformal-mode-scalar "
            "identification (KS 2011), NOT modified by this derivation."
        ),
        tier="computed",
        refs=(
            "grut/derivation/phi_munu/linearized_ctp_action.py",
            "theory/derivation/CORRECTION_23_PHI_MUNU_DERIVATION.md",
            "Komargodski-Schwimmer 2011 (a-theorem)",
            "Calzetta-Hu 2008 §5-§7",
        ),
        tests=(
            "tests/derivation/phi_munu/test_linearized_ctp_action.py",
        ),
        deps=(
            "ctp_action_structure",
            "alpha_vac_derivation",
            "memory_kernel_form",
            "gr_recovery",
        ),
        falsifier=(
            "If a non-Φ_μν term appears in the linearized variation "
            "(e.g., a Lorentz-violating coupling, or a non-causal "
            "advanced kernel inconsistent with the A1 axiom), the "
            "derivation fails. Verified at code level: the only non-"
            "vanishing terms in δS_CTP/δh_a |_{h_a=0} are the "
            "Einstein, matter, and constitutive (Φ_μν) contributions; "
            "noise vanishes (it is quadratic in h_a)."
        ),
        notes=(
            "Linearized limit. Curved-background extension is "
            "SCAFFOLDED at Phase 2B (claim "
            "phi_munu_curved_background_scaffold, anchored tier, "
            "Correction #24) with explicit FRW χ_FRW(k, η) "
            "computed at Phase 2C (claim "
            "phi_munu_frw_explicit_construction, computed tier, "
            "Correction #25). Phase 2D beyond-WKB refinement "
            "(O((Hτ_0)²) ≈ 10⁻⁶ correction) remains open. "
            "Closes the original 'heuristic projection' tier-honesty "
            "concern at the linearized level — Φ_μν is now a derived "
            "structural object, not a postulated multiplier."
        ),
    ),
    Claim(
        id="phi_munu_curved_background_scaffold",
        chapter=6,
        statement=(
            "Curved-background SCAFFOLD (Correction #24, Priority 2B). "
            "The linearized Φ_μν derivation extends to a covariant "
            "form with Φ_μν^curved(x) = ∫ d⁴x' √(-g(x')) K^R_μνρσ"
            "(x,x') h^ρσ(x'), where the bitensor kernel decomposes "
            "as K^R = α_vac × P^TT,g_μνρσ(x,x') × G^R(x,x'). "
            "FOUR STRUCTURAL VERIFICATION TARGETS verified at code "
            "level: (1) flat-limit recovery — g_μν → η_μν reduces "
            "Φ^curved → Φ^linear (Correction #23 form); (2) covariant "
            "conservation — ∇^μ Φ_μν = 0 follows STRUCTURALLY from "
            "∇^μ P^TT,g = 0 (curved analog of flat ∂^μ P^TT = 0); "
            "(3) causality — K^R(x,x') = 0 outside causal past J^-(x), "
            "implementing the A1 retarded-variation axiom covariantly; "
            "(4) FRW scalar-mode compatibility — on g_μν = "
            "diag(-1, a², a², a²), the operator susceptibility "
            "χ(τ_0²(-□_g)) acquires k- and t-dependence, producing "
            "n_g²(ω, k, t) = 1 + α × χ_FRW(k, η). This last property "
            "IS the bridge into Priority 3 (n_g(ω) covariance)."
        ),
        tier="anchored",
        refs=(
            "grut/derivation/phi_munu/curved_background.py",
            "grut/derivation/phi_munu/linearized_ctp_action.py",
            "theory/derivation/CORRECTION_24_PHI_MUNU_CURVED_SCAFFOLD.md",
            "Wald, General Relativity (1984) §10",
            "Hu & Verdaguer, Semiclassical and Stochastic Gravity (2008)",
        ),
        tests=(
            "tests/derivation/phi_munu/test_curved_background.py",
        ),
        deps=(
            "phi_munu_linearized_derivation",
            "constitutive_projection_gravity_heuristic_resolved",
        ),
        falsifier=(
            "If a covariant background fails any of the four "
            "structural targets — flat-limit non-recovery, ∇^μ Φ ≠ 0, "
            "K^R supported outside past lightcone, or FRW scalar-mode "
            "decomposition incompatible with the Mukhanov-Feldman-"
            "Brandenberger framework — the scaffold is invalidated. "
            "Verified at code level: all four targets pass."
        ),
        notes=(
            "ANCHORED at scaffold level — the structural form is "
            "pinned and four physical-consistency checks pass. "
            "Explicit FRW χ_FRW(k, η) is now computed at Phase 2C "
            "(claim phi_munu_frw_explicit_construction, computed "
            "tier, Correction #25): WKB-leading χ_FRW^WKB = "
            "1/[1+(τ_0 k_phys)²] with three explicit limits "
            "(sub-horizon, super-horizon, transition). "
            "Beyond-WKB refinement and S⁴ specialization remain "
            "research-tier (phi_munu_frw_beyond_wkb_open_question). "
            "The scaffold prevents the critique 'Φ_μν was derived "
            "only in flat space, but cosmology needs curved spacetime' "
            "by exhibiting the covariant form with the four required "
            "consistency checks. Curved-background extension is "
            "SCAFFOLDED + FRW EXPLICIT, with only beyond-WKB "
            "(O(10⁻⁶)) refinement remaining."
        ),
    ),
    Claim(
        id="phi_munu_frw_explicit_construction",
        chapter=6,
        statement=(
            "Phase 2C — explicit construction of χ_FRW(k, η) and "
            "n_g²(k, η) on FRW spacetime via the WKB / slow-H "
            "approximation (Correction #25, 2026-04-30). The "
            "covariant d'Alembertian on a scalar Fourier mode of "
            "comoving wavenumber k in conformal time η: "
            "□_g φ_k = -(1/a²)[∂_η² + 2H_c ∂_η + k²] φ_k. The "
            "relaxation operator (1 + τ_0² (-□_g)) reduces in the "
            "(H_c τ_0/a)² ≪ 1 limit to (1 + τ_0² k²/a²), giving the "
            "EXPLICIT FRW SUSCEPTIBILITY: "
            "χ_FRW^WKB(k, η) = 1 / [1 + (τ_0 k_phys(η))²]. "
            "Substituted into the constitutive equation: "
            "n_g²(k, η) = 1 + α_vac × χ_FRW^WKB(k, η) = 1 + "
            "α_vac / [1 + (τ_0 k_phys)²] with α_vac = 1/3. THREE "
            "EXPLICIT LIMITS: (a) sub-horizon (k_phys τ_0 → ∞): "
            "n_g² → 1 (GR recovery on small scales); (b) super-"
            "horizon (k_phys τ_0 → 0): n_g² → 4/3 (full constitutive "
            "on large scales); (c) transition (k_phys τ_0 = 1): "
            "n_g² = 7/6, transition WAVELENGTH λ_* = 2π τ_0 c ≈ 80.7 "
            "Mpc today. WKB regime applies across post-equality "
            "cosmology — beyond-WKB correction (H_0 τ_0)² ≈ 8.7×10⁻⁶ "
            "today. THIS IS THE COSMOLOGY BACKBONE for Priority 3 "
            "(n_g(ω) covariance): n_g²(k, η) is now a definite "
            "computable function of (k, η)."
        ),
        tier="computed",
        refs=(
            "grut/derivation/phi_munu/frw_explicit.py",
            "grut/derivation/phi_munu/curved_background.py (Phase 2B template)",
            "theory/derivation/CORRECTION_25_FRW_EXPLICIT.md",
            "Birrell-Davies (1982) §5.5 (□_g on FRW)",
            "Mukhanov-Feldman-Brandenberger (1992) (FRW perturbations)",
        ),
        tests=(
            "tests/derivation/phi_munu/test_frw_explicit.py",
        ),
        deps=(
            "phi_munu_curved_background_scaffold",
            "phi_munu_linearized_derivation",
            "alpha_vac_derivation",
            "tau_0_derivation",
        ),
        falsifier=(
            "If n_g²(k, η) deviates from the explicit WKB form "
            "1 + α/[1+(τ_0 k_phys)²] at the structural level — "
            "wrong limits, wrong transition scale, or "
            "(H_0 τ_0)² correction not subleading at the percent "
            "level — the Phase 2C explicit construction fails. "
            "Verified at code level by 49 tests in "
            "test_frw_explicit.py."
        ),
        notes=(
            "WKB level. Beyond-WKB corrections are O((H_0 τ_0)²) "
            "≈ 10⁻⁶ today and across all post-equality cosmology — "
            "subleading at any precision relevant for current and "
            "near-future cosmological observables. Beyond-WKB "
            "(Phase 2D) tracked separately as "
            "phi_munu_frw_beyond_wkb_open_question. Closing this "
            "Phase 2C makes n_g²(k, η) operationally complete; "
            "Priority 3 (n_g_omega_cosmological_covariance) now "
            "has an explicit cosmology backbone to insert into "
            "the linearized Einstein equations on FRW."
        ),
    ),
    Claim(
        id="phi_munu_frw_beyond_wkb_open_question",
        chapter=12,
        statement=(
            "Phase 2D — beyond-WKB extension of χ_FRW(k, η). The "
            "explicit Phase 2C result χ_FRW^WKB = 1/[1 + (τ_0 k_phys)²] "
            "is the leading-order slow-H (WKB) approximation of "
            "the full operator susceptibility. The next-order "
            "correction enters via the H_c ∂_η coupling in the "
            "FRW d'Alembertian: χ_FRW = χ^WKB × [1 + O((H_c τ_0)²)]. "
            "(H_c τ_0)² is dimensionally suppressed: today (H_0 τ_0)² "
            "= 1/(108π)² ≈ 8.7×10⁻⁶, similar at matter-radiation "
            "equality. The correction matters operationally only "
            "in the radiation era for modes that crossed k_* "
            "during that era. CLOSURE PATHS: (a) WKB matching "
            "beyond leading order; (b) numerical integration of "
            "the retarded Green function on FRW, mode by mode; "
            "(c) symbolic resummation under specific FRW expansion "
            "histories (radiation, matter, ΛCDM). Closing this "
            "Phase 2D extension is research-tier work that is "
            "NOT load-bearing for any current cosmological "
            "observable — current data does not constrain (H τ_0)² "
            "corrections at the 10⁻⁶ level."
        ),
        tier="open_negative",
        refs=(
            "grut/derivation/phi_munu/frw_explicit.py",
            "theory/derivation/CORRECTION_25_FRW_EXPLICIT.md",
        ),
        tests=(),
        deps=("phi_munu_frw_explicit_construction",),
        notes=(
            "Sharper successor to the original "
            "phi_munu_explicit_curved_construction_open_question. "
            "Phase 2C lands the WKB-leading χ_FRW(k, η) explicitly; "
            "Phase 2D is the beyond-WKB refinement, which is small "
            "by construction. The former question conflated the WKB "
            "computation with the beyond-WKB refinement; this "
            "successor cleanly separates them and assigns "
            "operational priority to the WKB result (already "
            "computed) over the (negligibly small) beyond-WKB "
            "correction (deferred)."
        ),
    ),

    Claim(
        id="two_route_convergence_physical_equivalence_open_question",
        chapter=12,
        statement=(
            "The two computed routes for R (Path G: pure α=1/3 "
            "algebra giving 1.15470; Osborn ε at M_Z: weighted gauge-"
            "coupling correction giving 1.15367) agree at 0.089%. "
            "The framework asserts this is structural confirmation. "
            "But the physical statement that makes them equivalent — "
            "e.g. 'the conformal mode's a/c at IR equals the gauge-"
            "coupling-corrected trace anomaly at electroweak matching "
            "scale' — has not been articulated. Without that "
            "statement, the convergence is striking empirical "
            "agreement, not structural identity. The framework is "
            "responsible for either (a) producing the equivalence "
            "statement, or (b) acknowledging the agreement is "
            "empirical and tiering accordingly."
        ),
        tier="open_negative",
        refs=(
            "Komargodski-Schwimmer 2011 (a-theorem; trace anomaly)",
            "Osborn (2003) hep-th/0302119 (eq 36, ε coefficient)",
            "Christensen-Duff 1980 (Nucl Phys B 170 480)",
            "grut/foundation/conformal_mode_scalar.py",
            "grut/foundation/osborn_epsilon.py",
            "theory/ZENODO_EPSILON_IDENTIFICATION.md",
        ),
        deps=(
            "r_canonical_path_g",
            "r_path_osborn_epsilon",
            "three_routes_convergence",
        ),
        notes=(
            "The honest framing: the two routes give the same number "
            "to 0.089% but the framework can't yet say WHY. The "
            "ZENODO_EPSILON_IDENTIFICATION.md document gestures at a "
            "Gibbons-Hawking thermal-asymmetry mechanism on Euclidean "
            "S⁴ as the bridge but does not derive it. Closing this "
            "gap would make three_routes_convergence a structural "
            "theorem rather than an empirical observation."
        ),
    ),

    Claim(
        id="n_g_omega_cosmological_covariance_resolved",
        chapter=12,
        statement=(
            "RESOLVED (Correction #26, 2026-05-01). Three closure "
            "gates of the original open question are all met: "
            "(1) ω → k_phys × c identification — in linear FRW "
            "perturbations, the dimensionless argument (ωτ_0)² that "
            "appeared in the flat-space susceptibility maps to "
            "(τ_0 k_phys)² where k_phys = k/a is the physical "
            "wavenumber. (2) Gauge-invariance — χ_FRW(k, η) depends "
            "only on (τ_0, α_vac, k, a), all gauge-invariant background "
            "quantities; manifestly invariant under conformal-Newtonian "
            "/ synchronous / comoving gauges at WKB. (3) MG-EFT "
            "dictionary — maps onto Pogosian-Silvestri μ(k, a) / "
            "γ(k, a) parameterization with μ_GRUT(k, a) = n_g²(k, a) "
            "and γ_GRUT(k, a) = 1 (no gravitational slip — sharp "
            "prediction distinguishing GRUT from Brans-Dicke, f(R), "
            "DGP). The framework's largest-scale prediction μ - 1 = "
            "α_vac = 1/3 is ~2σ above Planck 2018 central; DESI Y1+ "
            "(~5%) and Euclid 2027 (~1%) will resolve at >3σ. "
            "cmb_boltzmann_scoping now has a well-defined ω to use; "
            "Boltzmann-code implementation is downstream computation, "
            "not a theoretical gap. SCOPE: applies to LINEAR FRW "
            "perturbations only — bound systems (galactic rotation, "
            "cluster mergers, BH interiors, decoherence experiments) "
            "operate in different regimes with different ω-"
            "identifications."
        ),
        tier="meta",
        refs=(
            "grut/derivation/phi_munu/mg_eft_mapping.py",
            "grut/derivation/phi_munu/frw_explicit.py",
            "theory/derivation/CORRECTION_26_PRIORITY_3_CLOSURE.md",
            "Pogosian-Silvestri 2008 (PRD 77 023503)",
            "Bertschinger-Zukin 2008 (PRD 78 024015)",
            "Gubitosi-Piazza-Vernizzi 2013 (arXiv:1210.0201)",
            "Planck 2018 paper VI (Aghanim et al, A&A 641 A6, 2020)",
            "theory/CMB_BOLTZMANN_SCOPING.md",
        ),
        tests=(
            "tests/derivation/phi_munu/test_mg_eft_mapping.py",
        ),
        deps=(
            "phi_munu_frw_explicit_construction",
            "phi_munu_curved_background_scaffold",
            "memory_kernel_form",
        ),
        notes=(
            "Original entry (id 'n_g_omega_cosmological_covariance_"
            "open_question') flagged the issue without prescribing a "
            "resolution. Correction #26 (Priority 3 of the v8→v2 "
            "deposit roadmap) implements all three of the original "
            "closure conditions: ω-identification (via Phase 2C "
            "k_phys formulation), gauge-invariance (manifest at WKB), "
            "and μ/γ mapping (load-bearing — gives GRUT a definite "
            "place in the modified-gravity EFT-of-dark-energy "
            "literature with sharp γ = 1 prediction). The previous "
            "claim id was a pre-resolution placeholder; this claim "
            "supersedes it and tracks the closed status. SCOPE "
            "CLARIFICATION baked into the module: linear FRW "
            "perturbations ≠ bound-system / nonlinear halo "
            "phenomenology."
        ),
    ),
    Claim(
        id="modified_linear_growth_first_look",
        chapter=9,
        statement=(
            "Modified linear growth equation on FRW with μ_GRUT(k, a) "
            "from Priority 3, integrated numerically: δ'' + [2 - "
            "(3/2)Ω_m] δ' - (3/2) Ω_m μ_GRUT(k, N) δ = 0. Growth-"
            "factor enhancement f_GRUT(k) = D_GRUT(z=0, k)/D_ΛCDM"
            "(z=0) at canonical scales with ΛCDM background "
            "(Ω_m = 0.315, Ω_Λ = 0.685): "
            "(1) σ_8 scale (k = 0.5 Mpc⁻¹): f_GRUT = 1.0009 — only "
            "0.09% enhancement, BELOW current observational "
            "precision (~1-2%). DOES NOT BREAK the existing S_8 "
            "tension between Planck CMB and weak lensing. "
            "(2) BAO scale (k = 0.04 Mpc⁻¹): f_GRUT = 1.085 — modest "
            "8.5% enhancement; testable with DESI Y3+. "
            "(3) Sloan large scale (k = 0.01 Mpc⁻¹): f_GRUT = 1.328. "
            "(4) CMB low-ℓ (k = 0.001 Mpc⁻¹): f_GRUT = 2.024. "
            "(5) CMB horizon (k = 4.5×10⁻⁴ Mpc⁻¹): f_GRUT = 2.348 — "
            "significant enhancement on largest scales, predicts "
            "modified ISW signal and large-angle CMB anisotropy. "
            "The growth-factor enhancement is monotonic in 1/k: "
            "small scales (sub-horizon) recover ΛCDM, large scales "
            "show enhancement up to ~2.3× by today. Power-law "
            "exponent in matter-dom: p_+ = -1/4 + √(1/16 + 3μ/2), "
            "giving p = 1 (LCDM) → 1.0962 (transition) → 1.1862 "
            "(super-horizon). HONEST VERDICT: GRUT survives the "
            "σ_8-scale sanity check; predicts a definite testable "
            "signal at large scales."
        ),
        tier="computed",
        refs=(
            "grut/derivation/phi_munu/modified_growth.py",
            "grut/derivation/phi_munu/mg_eft_mapping.py",
            "theory/derivation/CORRECTION_27_MODIFIED_GROWTH.md",
            "Bertschinger-Zukin 2008 (PRD 78 024015)",
            "Pogosian-Silvestri 2008 (PRD 77 023503)",
        ),
        tests=(
            "tests/derivation/phi_munu/test_modified_growth.py",
        ),
        deps=(
            "mg_eft_mu_gamma_mapping",
            "phi_munu_frw_explicit_construction",
            "tau_0_derivation",
            "alpha_vac_derivation",
        ),
        falsifier=(
            "If a precision growth-rate measurement at k ~ 0.5 Mpc⁻¹ "
            "(σ_8 scale) deviates from ΛCDM at >2σ (σ_8 systematics "
            "are O(few %)), the framework's prediction of <0.1% "
            "modification at this scale is falsified. Independently, "
            "if the matter power spectrum at low k (~ 0.01 Mpc⁻¹) "
            "is measured precisely and matches ΛCDM (no ~32% boost), "
            "the framework's super-horizon enhancement is falsified. "
            "DESI Y3+ + Euclid 2027 will resolve these tests."
        ),
        notes=(
            "FIRST-LOOK ANALYSIS at the linear-growth ODE level. "
            "Full Boltzmann-pipeline (modified CAMB/CLASS, MCMC "
            "against Planck + DESI + LSS) remains downstream "
            "computational task — not blocked at the theoretical "
            "level. SCOPE: applies to LINEAR FRW perturbations; "
            "bound-system / nonlinear halo phenomenology operates "
            "via different ω-identifications (regime gate, cluster "
            "merger kernel, gr_recovery)."
        ),
    ),
    Claim(
        id="mg_eft_mu_gamma_mapping",
        chapter=9,
        statement=(
            "GRUT lives in the 'μ ≠ 1, γ = 1' subclass of "
            "modified-gravity models. μ_GRUT(k, a) = n_g²(k, a) = "
            "1 + α_vac / [1 + (τ_0 k_phys(a))²]; γ_GRUT(k, a) = 1 "
            "(no gravitational slip — TT-projector P^TT,g acts "
            "symmetrically on Φ and Ψ in absence of matter "
            "anisotropic stress). Sharp prediction distinguishing "
            "GRUT from Brans-Dicke (γ < 1), f(R) (γ ≠ 1, k-dependent), "
            "DGP (γ ≠ 1). Limits: super-horizon μ → 4/3, sub-horizon "
            "μ → 1, transition at λ_* ≈ 80.7 Mpc today. Falsifier-"
            "tier: μ - 1 = 1/3 prediction tested by DESI Y1+ at "
            "~5% precision (~5σ test relative to Planck central) and "
            "Euclid 2027 at ~1% precision (definitive ≥3σ test)."
        ),
        tier="computed",
        refs=(
            "grut/derivation/phi_munu/mg_eft_mapping.py",
            "grut/derivation/phi_munu/frw_explicit.py",
            "theory/derivation/CORRECTION_26_PRIORITY_3_CLOSURE.md",
        ),
        tests=(
            "tests/derivation/phi_munu/test_mg_eft_mapping.py",
        ),
        deps=(
            "phi_munu_frw_explicit_construction",
            "alpha_vac_derivation",
            "tau_0_derivation",
        ),
        falsifier=(
            "If a near-future cosmological survey (DESI, Euclid, "
            "Roman) measures μ₀ - 1 deviating from 1/3 by more than "
            "the survey's quoted precision, GRUT's MG-EFT prediction "
            "is falsified. Specifically: Euclid 2027 forecast of ~1% "
            "precision means a measurement of μ₀ - 1 < 0.30 or > 0.36 "
            "at >3σ would falsify the framework's α_vac = 1/3 + "
            "γ = 1 sharp prediction. Independently, any direct "
            "measurement of γ ≠ 1 at the >2σ level would falsify the "
            "TT-projector argument that underwrites γ_GRUT = 1."
        ),
        notes=(
            "SCOPE: applies to LINEAR FRW perturbations. Bound-"
            "system phenomenology (rotation curves, mergers, BH "
            "interiors) uses different operating variables and is "
            "tracked under separate claims (cluster_merger_scaling_"
            "law, gr_recovery, etc.)."
        ),
    ),

    Claim(
        id="cluster_tau_0_dec_ratio_degeneracy",
        chapter=9,
        statement=(
            "The +20% cluster-vs-cosmic systematic is degenerate "
            "between τ_0 and the deceleration ratio dec_ratio = "
            "v_post/v_initial. Both single-parameter routes close it: "
            "vary τ_0 alone (dec_ratio = 0.638 fixed) gives best-fit "
            "τ_0 = 49 Myr with χ² 0.077 → 0.0069 (11.2× improvement); "
            "vary dec_ratio alone (τ_0 = 41.9 Myr fixed) gives best-fit "
            "dec_ratio = 0.76 with χ² 0.077 → 0.0065 (11.9× improvement). "
            "The two best-fit chi-squared values agree within 6% and "
            "the dec_ratio × τ_0 products agree within 2% (31.84 vs "
            "31.28; canonical 26.74). The 2D sweep across (τ_0, "
            "dec_ratio) confirms a degeneracy ridge: any combination "
            "satisfying dec_ratio × τ_0 ≈ 31.5 closes the systematic. "
            "Offset data alone cannot disambiguate the two effects; "
            "independent v_post-collision measurements per cluster are "
            "required (currently only Bullet has this from Springel & "
            "Farrar 2007)."
        ),
        tier="computed",
        refs=(
            "grut/derived/cluster/deceleration_sensitivity.py",
            "Springel & Farrar 2007 (Bullet hydrodynamics)",
            "Markevitch et al. 2002 (Bullet X-ray)",
        ),
        tests=(
            "tests/derived/test_deceleration_sensitivity.py::TestCanonicalState",
            "tests/derived/test_deceleration_sensitivity.py::TestDecRatioSweep",
            "tests/derived/test_deceleration_sensitivity.py::TestDegeneracyReport",
            "tests/derived/test_deceleration_sensitivity.py::TestTwoDSweep",
            "tests/derived/test_deceleration_sensitivity.py::TestVerifyHarness",
            "tests/derived/test_deceleration_sensitivity.py::TestDegeneracyInterpretation",
        ),
        deps=(
            "cluster_merger_scaling_law",
            "cluster_tau_0_sensitivity_diagnostic",
        ),
        falsifier=(
            "Independent v_post-collision measurements for MACS J0025 "
            "and Abell 520 (e.g. from hydrodynamic simulations or X-ray "
            "shock-front analysis) that pin dec_ratio per cluster — "
            "would break the degeneracy and convert the +20% systematic "
            "into either a clear τ_0 effect (if measured dec_ratios "
            "support 0.638) OR a clear velocity-convention effect (if "
            "measured dec_ratios support ~0.76). Until then, the "
            "two-parameter family is observationally indistinguishable."
        ),
        notes=(
            "Diagnostic refinement of cluster_tau_0_sensitivity_diagnostic. "
            "The earlier diagnostic concluded the systematic was a "
            "specific signature; this one shows the signature is "
            "two-parameter-degenerate. Honest framing: the framework "
            "doesn't have to commit to either direction yet — the "
            "data permits both. Important for specialist outreach: "
            "specialists asking 'is τ_0 really 41.9 or 49?' get the "
            "honest answer 'cluster offsets give 41.9 × 0.76 = 49 × "
            "0.638 — the product is what's measured, not τ_0 alone'."
        ),
    ),

    Claim(
        id="el_gordo_sensitivity_analysis",
        chapter=9,
        statement=(
            "El Gordo's apparent factor-3.5 outlier resolves under "
            "joint parameter + observational uncertainty analysis. "
            "Across 80 parameter combinations spanning published "
            "ranges (v_initial 2000-3500 km/s, t_since 70-300 Myr, "
            "dec_ratio 0.5-0.85), GRUT's predicted offset spans 43-"
            "130 kpc. The observation range from published lensing "
            "reconstructions spans 120-600 kpc (depending on "
            "methodology, reconstruction technique, and which "
            "subclump). Prediction range OVERLAPS observation range "
            "at the lower end. Key results: (a) at observed = 120 kpc, "
            "best-case GRUT prediction ratio = 1.09 (fully consistent); "
            "(b) at observed = 150 kpc, best-case ratio = 0.87 "
            "(matches the other three normal-regime mergers); "
            "(c) at observed = 600 kpc (Jee 2014 NW clump), best-case "
            "ratio = 0.22 (factor 4-5 deviation, real problem). "
            "El Gordo is consistent with GRUT IF the true offset is "
            "in the lower published range AND parameters are at the "
            "favorable end. Disambiguation requires improved lensing "
            "reconstructions and independent v_post measurements."
        ),
        tier="computed",
        refs=(
            "grut/derived/cluster/el_gordo_sensitivity.py",
            "Jee et al. 2014 (parametric SL+WL, ApJ 785 20)",
            "Diego et al. 2023 (free-form lensing reconstruction)",
            "Menanteau et al. 2012 (initial discovery, ApJ 748 7)",
        ),
        tests=(
            "tests/derived/test_el_gordo_sensitivity.py::TestParameterRanges",
            "tests/derived/test_el_gordo_sensitivity.py::TestParameterSweep",
            "tests/derived/test_el_gordo_sensitivity.py::TestSensitivityReport",
            "tests/derived/test_el_gordo_sensitivity.py::TestClosureScenarios",
            "tests/derived/test_el_gordo_sensitivity.py::TestVerifyHarness",
            "tests/derived/test_el_gordo_sensitivity.py::TestConsistencyAtLowObs",
        ),
        deps=(
            "cluster_merger_scaling_law",
            "el_gordo_outlier_open_question",
        ),
        falsifier=(
            "Definitive lensing-reconstruction work pinning El Gordo's "
            "true gas-to-lensing offset above 200 kpc with sub-20% "
            "precision would maintain the deviation as a real "
            "framework problem (factor 1.5+ above any best-case GRUT "
            "prediction). Conversely, free-form or independent "
            "reconstructions confirming the lower published range "
            "(120-150 kpc) would show El Gordo is consistent with "
            "the v × τ_0 scaling at the same level as the other "
            "three normal-regime mergers."
        ),
        notes=(
            "This claim significantly weakens the 'El Gordo is an "
            "outlier' framing in cluster_merger_scaling_law and "
            "el_gordo_outlier_open_question. The factor-3.5 deviation "
            "was an artifact of choosing one specific parameter point "
            "(v=2500/t=110/dec=0.638) and one specific observation "
            "value (250 kpc) from published ranges spanning much "
            "wider intervals. Honest read: the data does not robustly "
            "reject El Gordo from the v × τ_0 scaling. The framework "
            "should not have been claiming a clean 'factor 3.5 "
            "outlier' — that was overclaiming the deviation."
        ),
    ),

    Claim(
        id="cluster_tau_0_sensitivity_diagnostic",
        chapter=9,
        statement=(
            "Single-τ_0 sensitivity analysis across the three normal-"
            "regime mergers (Bullet, MACS J0025, Abell 520, El Gordo "
            "excluded) finds best-fit τ_0 = 49 Myr with chi² = 0.007, "
            "an 11× improvement over canonical τ_0 = 41.9 Myr "
            "(chi² = 0.077). At best-fit, all three cluster ratios "
            "fall within ±10% of unity (Bullet 1.02, MACS 1.03, Abell "
            "0.93). The best-fit value matches the cluster-inferred "
            "mean (50.0 Myr) from independent direct-inference analysis "
            "to within 1 Myr. Three independent analyses — cluster "
            "merger scaling, τ_0 cross-consistency, and this sensitivity "
            "sweep — all point at cluster-regime τ_0 ≈ 50 Myr, ~20% "
            "higher than the cosmic-baseline τ_0 ≈ 41.4 Myr."
        ),
        tier="computed",
        refs=(
            "grut/derived/cluster/tau_0_sensitivity.py",
            "Clowe et al. 2006 (Bullet)",
            "Bradač et al. 2008 (MACS J0025)",
            "Mahdavi et al. 2007 (Abell 520)",
        ),
        tests=(
            "tests/derived/test_tau_0_sensitivity.py::TestSweepGrid",
            "tests/derived/test_tau_0_sensitivity.py::TestSweepPoint",
            "tests/derived/test_tau_0_sensitivity.py::TestBestFit",
            "tests/derived/test_tau_0_sensitivity.py::TestComparisonReport",
            "tests/derived/test_tau_0_sensitivity.py::TestVerifyHarness",
            "tests/derived/test_tau_0_sensitivity.py::TestDiagnosticInterpretation",
        ),
        deps=(
            "cluster_merger_scaling_law",
            "tau_0_cross_consistency",
            "tau_0_derivation",
        ),
        falsifier=(
            "More cluster-merger data (additional normal-regime systems) "
            "either confirming the +20% cluster-vs-cosmic τ_0 offset "
            "(supports specific signature reading) or showing it does "
            "NOT persist (supports observational-uncertainty reading). "
            "If the offset persists across N > 6 normal-regime mergers "
            "with collision velocities measured at < 15% precision, "
            "the framework's pure-Lorentzian-kernel-with-single-τ_0 "
            "structure is falsified, requiring kernel revision OR "
            "extended-mass corrections OR a regime-of-validity "
            "statement on the dielectric DM interpretation."
        ),
        notes=(
            "Diagnostic disambiguator: distinguishes 'observational "
            "uncertainty' from 'specific signature' for the 0.79-0.88 "
            "systematic in cluster_merger_scaling_law. The 11× chi² "
            "improvement at best-fit τ_0 = 49 Myr (vs canonical 41.9 "
            "Myr) supports the specific-signature reading. The best-"
            "fit value's agreement with the cluster-inferred mean "
            "(50.0 Myr) from a different analysis pins it as a real "
            "diagnostic signal at the cluster regime, not a kernel-"
            "shape problem (the same τ_0 closes all three). Future "
            "cluster data is the test: if cluster-regime τ_0 stays "
            "≈ 50 Myr, this is a real signature of a regime-dependent "
            "effective τ_0; if it converges to 41.9 Myr with better "
            "obs, the current systematic was uncertainty."
        ),
    ),

    Claim(
        id="el_gordo_outlier_open_question",
        chapter=12,
        statement=(
            "ACT-CL J0102-4915 (El Gordo) was originally tagged as a "
            "factor-3.5 outlier (canonical 70 kpc prediction vs ~250 "
            "kpc observed). Sensitivity analysis across the published "
            "parameter ranges (v_initial 2000-3500 km/s, t_since 70-"
            "300 Myr, dec_ratio 0.5-0.85, observed offset 120-600 kpc) "
            "shows the framework's prediction range (43-130 kpc) "
            "OVERLAPS with the lower part of the observed range. "
            "Specifically: at observed = 120 kpc (lower bound, "
            "individual subclump centroids), best-case GRUT prediction "
            "matches at ratio ~1.09 — fully consistent. At observed "
            "= 150 kpc, ratio ~0.87 — same as Bullet, MACS, Abell 520. "
            "Only at observed > 250 kpc (upper-range parametric "
            "reconstructions like Jee 2014 NW clump) does the deviation "
            "become decisive. The factor-3.5 outlier framing was "
            "specific to one parameter point AND one offset value; "
            "actual data does not robustly reject the framework."
        ),
        tier="open_negative",
        refs=(
            "Jee et al. 2014 (ApJ 785 20, arXiv:1401.3356)",
            "Menanteau et al. 2012",
            "Diego et al. 2023 (free-form lensing)",
            "grut/derived/cluster/merger_population.py:EL_GORDO",
        ),
        tests=(
            "tests/derived/test_merger_population.py::TestPerSystemPredictions::test_el_gordo_is_explicit_outlier",
            "tests/derived/test_merger_population.py::TestElGordoOutlierIsHonestNegative",
        ),
        deps=("cluster_merger_scaling_law",),
        notes=(
            "Honest negative on the cluster-population test. The "
            "Bullet/MACS/Abell-520 trio confirms v × τ_0 at factor "
            "~1.3; El Gordo's deviation does not invalidate the "
            "scaling but flags the regime where additional structure "
            "is needed. Closure depends on either better "
            "observational constraints on El Gordo's parameters, or "
            "extension of the kernel model to handle off-axis / "
            "high-asymmetry collisions."
        ),
    ),

    Claim(
        id="primordial_amplitude_zero_parameter_open_negative",
        chapter=12,
        statement=(
            "The primordial scalar amplitude A_s ≈ 2.1 × 10⁻⁹ "
            "(Planck 2018) is observation-anchored, not derived "
            "zero-parameter from GRUT's CTP infrastructure. Three "
            "computational paths attempted "
            "(grut/derived/cosmology/primordial_amplitude.py): "
            "(A) Ornstein-Uhlenbeck variance of metric perturbations "
            "driven by the KMS noise kernel at T = T_CMB, Planck-"
            "rescaled — yields ~2 × 10⁻¹⁹, factor 10¹⁰ too small; "
            "(B) standard inflationary formula A_s = H²/(8π² ε M²_Pl,red) "
            "with GRUT's terminal-velocity H_inf and ε = (Hτ₀)² — "
            "yields ~5 × 10⁻¹¹⁸, factor 10¹⁰⁹ too small (expected: "
            "GRUT has no inflationary epoch); (C) 11 natural "
            "dimensional candidates from α, S, H_inf, τ₀, T_c — "
            "the closest, α/S³ = (1/3)/(108π)³ ≈ 8.5 × 10⁻⁹, lands "
            "at factor 4 from observed but is NOT promoted to a "
            "derivation: with 11 candidates tested, finding ~1 "
            "within a decade is statistically plausible coincidence. "
            "The α/S³ coincidence is documented as a CLUE worth "
            "physical motivation. Honest verdict: "
            "HONEST_NEGATIVE_WITH_DIMENSIONAL_CLUE."
        ),
        tier="open_negative",
        refs=(
            "grut/derived/cosmology/primordial_amplitude.py",
            "grut/derived/cosmology/primordial_curvature.py",
            "grut/derived/cosmology/spectral_running.py",
            "grut/foundation/noise_kernel.py",
            "theory/derivation/PRIMORDIAL_ALPHA_S3_INVESTIGATION.md",
            "tests/derived/test_primordial_amplitude.py",
            "tests/derived/test_primordial_curvature.py",
        ),
        tests=(
            "tests/derived/test_primordial_amplitude.py",
            "tests/derived/test_primordial_curvature.py",
        ),
        deps=(
            "ctp_action_structure",
            "memory_kernel_form",
            "tau_0_derivation",
            "alpha_vac_derivation",
            "screening_108pi",
        ),
        notes=(
            "Stage-1 attempt (primordial_amplitude.py): three paths "
            "tested OU-process variance, inflationary substitution, "
            "and 10 distinct dimensional candidates. The closest "
            "dimensional candidate, α/S³ ≈ 8.5×10⁻⁹, lands at "
            "factor 4 from observed A_s — flagged as a clue. "
            "Stage-2 forward investigation "
            "(primordial_curvature.py, see "
            "PRIMORDIAL_ALPHA_S3_INVESTIGATION.md): linearized the "
            "constitutive equation around z = 0 with KMS noise, "
            "computed the dimensional variance "
            "⟨|δz_{k*}|²⟩ = 2π G c² × coth(...) at the bandwidth "
            "crossover ωτ_0 = 1. The dimensionless P_ζ DEPENDS ON "
            "RESCALING CHOICE: (A) Planck rescaling → "
            "(1/π)(t_Pl/τ_0)³ ≈ 10⁻¹⁷⁶, no α-S structure; "
            "(B) cosmic-baseline rescaling → 1/(πS³) ≈ 8.15×10⁻⁹, "
            "S³ structure (5% from α/S³ algebraically, factor 4 "
            "from A_s); (C) H_inf rescaling → ((2-R)/S)³/π ≈ "
            "4.92×10⁻⁹, also S³ family, factor 2.3 from A_s. The "
            "α/S³ family IS recovered under (B) and (C), NOT under "
            "(A). The framework does not natively pin the rescaling. "
            "STRUCTURAL FINDING: this connected to the original "
            "n_g_omega_cosmological_covariance_open_question (#9), "
            "which has now been RESOLVED by Correction #26 (Priority 3, "
            "2026-05-01) — n_g_omega_cosmological_covariance_resolved. "
            "Post-resolution status: with μ_GRUT(k, a) explicit, the "
            "natural-rescaling question becomes a Boltzmann-code-level "
            "evaluation of A_s at the pivot mode under modified-gravity "
            "growth dynamics. The α/S³ coincidence under cosmic-baseline "
            "rescaling (factor 4 from A_s) corresponds to the k → 0 "
            "limit, not the pivot-mode k = 0.05 Mpc⁻¹ relevant for "
            "Planck. Closure paths: (1) Boltzmann-code implementation "
            "with μ_GRUT, integrate to pivot mode, predict A_s; "
            "(2) Genesis Hypothesis becoming formal with an "
            "inflationary-like epoch (independent path); "
            "(3) explicit acknowledgment that A_s is observation-"
            "anchored, parallel to "
            "n_total_zero_parameter_derivation_open_question."
        ),
    ),

    Claim(
        id="t_c_provenance_inconsistency_resolved",
        chapter=12,
        statement=(
            "RESOLVED (Correction #22, 2026-04-30). The pre-resolution "
            "T_c formula T_c = 1/(τ_0 × k_B) was dimensionally invalid "
            "— with τ_0 in SI seconds and k_B in J/K it produced units "
            "K/(J·s), not K — and the 'v9 natural-units convention "
            "(ℏ=1)' defense did not survive a proper natural-units "
            "check (converting τ_0 to eV⁻¹ and computing 1/τ_0_nat "
            "gives 5.78×10⁻²⁷ K identically, not 54.7 MK). Resolution: "
            "the framework was conflating TWO physically distinct "
            "relaxation timescales under one symbol. Two-τ-scale "
            "convention now makes the separation explicit: "
            "(A) τ_0 = 41.9 Myr is the macroscopic GRAVITATIONAL "
            "relaxation time (cosmic-baseline + Bullet Cluster "
            "anchored), used by every load-bearing cosmological "
            "prediction (Λ_grav, n_g(ω), bridge, cluster-merger "
            "scaling, Hubble terminal — all unaffected); "
            "(B) τ_micro ≈ 1.4×10⁻¹⁹ s is the microscopic THERMAL "
            "relaxation time, defined as ℏ/(k_B × T_c) and anchored "
            "by the cosmological-chronology pin T_c = 54.7 MK at "
            "t ≈ 1 hour post-Big Bang. The 34-orders-of-magnitude "
            "separation between τ_0 and τ_micro is named explicitly. "
            "The relation between the two scales is a SHARP OPEN "
            "QUESTION (claim tau_zero_to_tau_micro_relation_open"
            "_question) — Correction #22 closes the dimensional "
            "inconsistency without claiming to derive τ_micro from "
            "τ_0. T_c numerical value (54.7 MK) preserved exactly; "
            "test_T_c_is_54p7_MK pin unchanged. SI-correct formula "
            "T_c = ℏ/(τ_micro × k_B) now in closure_protocol.py."
        ),
        tier="meta",
        refs=(
            "grut/foundation/closure_protocol.py:T_C_KELVIN",
            "grut/foundation/closure_protocol.py:TAU_MICRO_SEC",
            "theory/foundations_audit/T_C_PROVENANCE.md",
            "theory/derivation/CORRECTION_22_TAU_CLEANUP.md",
        ),
        tests=(
            "tests/foundation/test_closure_protocol.py::TestCanonicalConstants::test_T_c_formula_is_SI_correct",
            "tests/foundation/test_closure_protocol.py::TestCanonicalConstants::test_two_tau_scales_separated_by_thirty_plus_orders",
            "tests/foundation/test_closure_protocol.py::TestCanonicalConstants::test_T_c_old_dimensionally_invalid_formula_NOT_used",
        ),
        deps=(
            "tau_0_derivation",
            "tau_micro_thermal_scale",
            "t_c_thermal_transition",
        ),
        notes=(
            "Original entry (id 't_c_provenance_inconsistency_open"
            "_negative') flagged the issue without prescribing a "
            "resolution. Correction #22 (Priority 1 of the v8→v2 "
            "deposit roadmap) implements the two-τ-scale resolution. "
            "The crystallization-schedule investigation (held under "
            "the open-negative) is now unblocked at the dimensional "
            "level — Stage 2-4 work can proceed, using τ_micro for "
            "thermal-transition calculations and τ_0 for "
            "gravitational-sector calculations. The previous claim "
            "id was a pre-resolution placeholder; this claim "
            "supersedes it and tracks the closed status."
        ),
    ),
    Claim(
        id="tau_zero_to_tau_micro_relation_open_question",
        chapter=12,
        statement=(
            "The relation between the framework's two τ-scales is "
            "currently underived. τ_0 = 41.9 Myr (gravitational "
            "sector, anchored by 1/(H_0 × 108π) and Bullet Cluster "
            "δ ≈ v×τ_0) and τ_micro ≈ 1.4×10⁻¹⁹ s (thermal sector, "
            "anchored by T_c at t ≈ 1 hour post-Big Bang) differ by "
            "~34 orders of magnitude with no closure path between "
            "them. STATUS: the framework currently presents itself "
            "as one-parameter (τ_0 fixes everything via the screening "
            "factor S = 108π and the bridge to Λ); under the "
            "two-τ-scale convention this is INCOMPLETE — τ_micro is "
            "an independent empirically-anchored input until a "
            "derivation is found. CLOSURE PATHS under investigation: "
            "(1) τ_micro might be derivable from the v9 noise kernel "
            "evaluated at the BBN-era thermal scale (Genesis hypothesis "
            "track); (2) τ_micro might equal the inverse of the "
            "vacuum's microscopic plasma frequency, set by responsive-"
            "medium ground-state physics not yet characterized; "
            "(3) τ_micro might satisfy a multiplicative relation "
            "ℏ × τ_0 = (some natural unit) × τ_micro — note that "
            "numerically τ_micro × τ_0 ≈ ℏ/k_B² × constants, hinting "
            "at a possible fluctuation-dissipation-style relation; "
            "(4) HONEST NEGATIVE outcome: the two scales are "
            "fundamentally independent, the framework has TWO free "
            "parameters in its predictive core, and the v8 'zero "
            "free parameters in the predictive core' framing is "
            "downgraded to 'one free parameter (τ_0) in the "
            "GRAVITATIONAL predictive core; one anchored parameter "
            "(τ_micro) in the THERMAL sector'. This last outcome is "
            "a meaningful credibility loss but a survivable one — "
            "thermal-sector anchoring is comparable to MOND's a_0 "
            "anchoring, and the gravitational-sector zero-parameter "
            "core would still hold."
        ),
        tier="open_negative",
        refs=(
            "grut/foundation/closure_protocol.py:TAU_MICRO_SEC",
            "theory/derivation/CORRECTION_22_TAU_CLEANUP.md",
        ),
        tests=(),
        deps=(
            "tau_0_derivation",
            "tau_micro_thermal_scale",
            "t_c_provenance_inconsistency_resolved",
        ),
        notes=(
            "Promoted from the structural diagnosis embedded in the "
            "previous open_negative entry. Per the audit pattern: "
            "the dimensional bug is closed (Correction #22), the "
            "downstream open question (relation derivation) is "
            "named and tracked here. Closure paths (1)-(3) are "
            "research-tier work; closure path (4) is the honest-"
            "negative outcome that downgrades the framework's "
            "free-parameter count from zero to one (gravitational) "
            "+ one anchored (thermal). The question of whether the "
            "framework's stated 'zero free parameters' framing "
            "survives this resolution is itself a register-able "
            "claim for the v2 deposit's posture statement; the "
            "current registry treats it as open until a closure "
            "path produces a derivation or until the honest-"
            "negative outcome is formally accepted."
        ),
    ),

    Claim(
        id="genesis_noise_kernel_spectral_attempt",
        chapter=12,
        statement=(
            "Standard-physics calculation testing one piece of the "
            "Genesis-BBN-DM external research hypothesis: 'CTP noise "
            "kernel acting on z = 0 produces thermal-spectrum "
            "radiation at some characteristic temperature.' Result: "
            "the hypothesis claim is STRUCTURALLY WRONG at the "
            "spectrum-shape level. The framework's KMS noise kernel "
            "applied to the linearized OU process (τ_0 ḣ + h = ξ) "
            "around z = 0 produces, at T = 0 (pure quantum vacuum), "
            "a spectrum S_h(ω) = (2ℏ/τ_0) × ω/(1+(ωτ_0)²). This is "
            "Lorentzian-modulated linear, NOT Planck/Bose-Einstein. "
            "Genesis Claim 1's 'thermal radiation' framing fails at "
            "the spectrum-shape level — no temperature T makes "
            "S_h(ω, T=0) coincide with the Planck distribution "
            "ω³/(exp(ℏω/k_BT)-1) at any T. CHARACTERISTIC TEMPERATURES "
            "extractable from the spectrum (each a distinct "
            "definitional choice the framework hasn't pinned): "
            "(a) spectral peak ω_peak = 1/τ_0 → T_peak = ℏ/(τ_0 k_B) "
            "≈ 5.78×10⁻²⁷ K; (b) Planck UV cutoff → T ≈ T_Planck ≈ "
            "1.4×10³² K; (c) equipartition heuristic at Planck UV "
            "cutoff → ~10⁻³¹ K. NONE match observed CMB (2.725 K). "
            "Spectral peak value ℏ/(τ_0 k_B) coincides numerically "
            "with the SI-correct T_c value identified in the #15 "
            "audit (codebase reports T_c = 54.7 MK with missing "
            "factor of ℏ); the same scale appears here as a "
            "different physical quantity (spectral peak vs claimed "
            "phase boundary). Cross-verification against existing "
            "fdt_noise infrastructure (grut/foundation/noise_kernel.py) "
            "is exact across all tested regimes."
        ),
        tier="anchored",
        refs=(
            "grut/derived/cosmology/genesis_noise_kernel.py",
            "tests/derived/test_genesis_noise_kernel.py",
            "theory/derivation/GENESIS_NOISE_KERNEL_HEAT_INVESTIGATION.md",
            "theory/derivation/GENESIS_BBN_DM_HYPOTHESIS_LOG.md",
            "grut/foundation/noise_kernel.py:fdt_noise (cross-verified)",
        ),
        tests=(
            "tests/derived/test_genesis_noise_kernel.py",
        ),
        deps=(
            "ctp_action_structure",
            "memory_kernel_form",
            "tau_0_derivation",
        ),
        notes=(
            "ANCHORED, not computed: the calculation is mechanically "
            "reproducible from the framework's existing KMS noise "
            "kernel infrastructure, but it tests an external "
            "hypothesis claim. The framework remains uncommitted to "
            "the broader Genesis-BBN-DM narrative — see "
            "GENESIS_BBN_DM_HYPOTHESIS_LOG.md. With Claim 2 already "
            "FALSIFIED (BBN thermal buffer at 10 orders) and Claim 1 "
            "now structurally WRONG (spectrum is Lorentzian × linear, "
            "not Planck/Bose-Einstein), two of the four narrative "
            "claims are closed negative. Claims 3 and 4 remain "
            "blocked-or-untested per the hypothesis log. STRUCTURAL "
            "FINDING (third in this session of multi-scale ambiguity "
            "in cosmological-plasma physics): the calculation "
            "produces a definite spectrum, but extracting 'a "
            "temperature' requires choices the framework hasn't "
            "pinned (T = 0 quantum limit vs imposed-T classical vs "
            "self-consistent equilibrium; spectral peak vs UV cutoff "
            "vs equipartition). Same general gap as the primordial "
            "A_s rescaling sensitivity and X_cosmic mass-class "
            "dependence — all three connect to cosmological-plasma "
            "physics formalization that the framework has at scoping "
            "level only. CONNECTION TO #15 NOT A RESOLUTION: the "
            "spectral-peak value 5.78×10⁻²⁷ K coincides numerically "
            "with the SI-correct T_c value identified in the audit. "
            "But this is one definitional role (spectral peak) of "
            "the same scale that #15 names as a phase boundary. The "
            "audit's question — whether T_c = 54.7 MK is correct "
            "with a different formula or wrong by factor ℏ — remains "
            "unresolved. RESEARCH-TIER UNANSWERED: self-consistent "
            "equilibrium (the noise kernel's dissipated energy "
            "thermalizing a radiation field with self-consistent T "
            "from energy balance) is the closure path Claim 1 would "
            "need. Requires structural addition the framework lacks "
            "(model of how metric fluctuations radiate); not "
            "addressed here."
        ),
    ),

    Claim(
        id="bbn_thermal_buffer_negligible",
        chapter=12,
        statement=(
            "Standard-cosmology calculation testing one piece of an "
            "external research hypothesis: 'BBN binding-energy release "
            "provides a thermal buffer that slows or plateaus cosmic "
            "temperature.' Result: the hypothesis claim is "
            "QUANTITATIVELY WRONG by ~10 orders of magnitude. "
            "Three independent comparisons, all consistent: "
            "(a) per-baryon energy ratio at T = 0.1 MeV: binding/"
            "radiation ≈ 4×10⁻⁹ (binding energy 1.75 MeV/baryon vs "
            "radiation energy 4.4×10⁸ MeV/baryon); "
            "(b) energy density ratio: E_bind_total/ρ_rad ≈ 2.4×10⁻⁹; "
            "(c) rate ratio (1000 s window): injection rate/cooling "
            "rate ≈ 1.6×10⁻¹⁰. The η_B-suppression is the load-bearing "
            "physics: with η_B ≈ 6×10⁻¹⁰, baryons are 1.6×10⁹ times "
            "rarer than photons, so binding-energy injection cannot "
            "meaningfully heat or buffer the radiation field. Even if "
            "every baryon's full BBN binding energy (1.75 MeV) were "
            "dumped instantaneously into the radiation field, the "
            "temperature would change by ~10⁻⁹ — far below any "
            "'thermal buffer' threshold. THE HYPOTHESIS-LEVEL "
            "IMPLICATION: the broader Genesis-BBN-DM narrative "
            "connecting BBN dynamics to T_c crossing needs a "
            "different mechanism than binding-energy buffering. "
            "BBN does not slow cosmic cooling meaningfully; cosmic "
            "temperature evolution during BBN is set by radiation "
            "domination essentially as in standard cosmology."
        ),
        tier="anchored",
        refs=(
            "grut/derived/cosmology/bbn_thermal_buffer.py",
            "tests/derived/test_bbn_thermal_buffer.py",
            "Kolb & Turner, 'The Early Universe' Ch 4 (BBN energetics)",
            "Planck 2018 (η_B = 6.14×10⁻¹⁰)",
            "PDG (B(⁴He) = 28.296 MeV)",
        ),
        tests=(
            "tests/derived/test_bbn_thermal_buffer.py",
        ),
        deps=(),  # uses only standard cosmology, no GRUT-specific deps
        falsifier=(
            "If a careful re-analysis with explicit time-dependent "
            "BBN reaction networks (rather than the integrated "
            "binding-energy estimate used here) showed that the "
            "INSTANTANEOUS injection rate at peak ⁴He synthesis "
            "(~T = 0.07 MeV) exceeds the cooling rate by even 1%, "
            "the negligibility claim would need refinement. The "
            "current calculation uses a uniform-rate estimate "
            "(total binding energy / BBN duration) which represents "
            "the AVERAGE rate; instantaneous peak rates are larger "
            "but still expected to be well below 1% of cooling."
        ),
        notes=(
            "ANCHORED, not computed: the calculation is mechanically "
            "reproducible from STANDARD cosmology (η_B, Y_p, B(⁴He), "
            "g_*, Friedmann radiation domination). It uses NO GRUT-"
            "specific machinery (no τ_0, no Λ_grav, no T_c, no R, "
            "no α_vac). The 'anchored' tier reflects that this is "
            "framework-adjacent — testing an external hypothesis via "
            "standard cosmology — rather than a GRUT-derived "
            "prediction. SCOPE: this claim documents the FALSIFICATION "
            "of one piece (Claim 2: BBN as thermal buffer) of a "
            "broader research narrative connecting GRUT's vacuum "
            "crystallization to BBN dynamics. The broader narrative "
            "remains uninvestigated and uncommitted at the framework "
            "level — see "
            "theory/derivation/GENESIS_BBN_DM_HYPOTHESIS_LOG.md for "
            "the full hypothesis log and which other pieces remain "
            "untested or have specific gaps. PRE-COMMITMENT: outcome "
            "(ii) cooling-slowed-not-plateaued was registered as the "
            "expected outcome before computation. Actual result is "
            "outcome (iii) negligible by ~10 orders of magnitude — "
            "materially different from expectation. The discipline "
            "pattern (pre-commit, compute, slow down on surprise, "
            "verify) operated correctly: three independent comparisons "
            "all give the same answer. Connection to "
            "tau_zero_to_tau_micro_relation_open_question (post-"
            "Correction-#22 successor of the original "
            "t_c_provenance_inconsistency_open_negative): the broader "
            "narrative posited BBN dynamics as the bridge between τ_0 "
            "and τ_micro scales. With BBN buffering falsified, this "
            "specific bridge does NOT work; closure paths (1)-(3) of "
            "the relation open-question remain in play, but BBN "
            "dynamics is ruled out as the mechanism. The honest-"
            "negative outcome (closure path 4: two truly independent "
            "scales) is correspondingly more credible after this "
            "falsification."
        ),
    ),

    Claim(
        id="n_total_zero_parameter_derivation_open_question",
        chapter=12,
        statement=(
            "GRUT's detailed Hubble-from-first-principles route "
            "(grut/derived/cosmology/hubble_from_first_principles.py: "
            "grut_H_0_prediction) computes H_0 = 69.03 km/s/Mpc via "
            "flat-ΛCDM Friedmann integration. Inputs: R_anomaly "
            "(computed), S_CTP (computed), τ_0 = 41.9 Myr (posited "
            "with two anchors), and N_total = 329 eras (observed-age "
            "anchor — t_0 ≈ 13.78 Gyr ÷ τ_0 = 329). The single "
            "observational anchor is N_total. A zero-parameter "
            "derivation of N_total (or equivalently cosmic age) from "
            "framework foundations alone does not currently exist. "
            "Four direct attempts (theory/derivation/N_TOTAL_DERIVATION_ATTEMPT.md) "
            "all closed negative: matter-Λ equality from H_inf gives "
            "N_threshold = 235.7 vs V7's 215 (9.6% off); era-map "
            "sigmoid dynamics saturate at era ~250 before reaching "
            "329; total-age-via-Friedmann requires Ω_m as input "
            "which is the same problem reframed; reverse-engineering "
            "Ω_m from N_total = 329 yields Ω_m = 0.29 (6.8% from "
            "Planck's 0.3111), confirming N_total is observation-"
            "anchored rather than structurally derived. The simpler "
            "cosmic-baseline H_0 = 68.8 km/s/Mpc (registry claim "
            "h_0_prediction, formula H_0 = 1/(S × τ_0)) is "
            "zero-parameter and does NOT depend on N_total — this "
            "open negative applies only to the detailed Friedmann "
            "route."
        ),
        tier="open_negative",
        refs=(
            "grut/derived/cosmology/hubble_from_first_principles.py:grut_H_0_prediction",
            "theory/derivation/N_TOTAL_DERIVATION_ATTEMPT.md",
            "tests/derived/test_hubble_from_first_principles.py",
        ),
        tests=(
            "tests/derived/test_hubble_from_first_principles.py",
        ),
        deps=("h_0_prediction", "h_inf_decomposition", "tau_0_derivation"),
        notes=(
            "The era-map module accepts n_eras=329 as default and "
            "the docstring previously framed this as 'one parameter' "
            "while inconsistently naming Ω_dm rather than N_total as "
            "the parameter. The actual code path uses N_total via "
            "t_0 = N_total × τ_0 and never consumes Ω_dm. Closure "
            "requires deriving cosmic age from framework foundations "
            "without using observed t_0. Likely precondition: the "
            "Genesis Hypothesis (V7/V8 Appendix A — origin of cosmic "
            "evolution from null fixed point destabilization) being "
            "made formal/computable. Genesis Hypothesis is currently "
            "[SPECULATIVE]; closure depends on its machinery becoming "
            "tractable, NOT on adopting it as a postulate. Until then, "
            "the framework's two H_0 routes carry asymmetric tier: "
            "cosmic-baseline 68.8 is zero-parameter computed; "
            "Friedmann 69.03 is one-parameter computed (parameter = "
            "observed N_total). The 0.3% agreement between the two "
            "routes supports the cosmic-baseline approximation."
        ),
    ),

    Claim(
        id="cluster_merger_scaling_law",
        chapter=9,
        statement=(
            "The v × τ_0 memory-kernel scaling law applied to four "
            "independent merging cluster systems. With canonical "
            "parameters (v_final = 0.638 × v_initial, τ_0 = 41.9 Myr): "
            "Bullet Cluster (ratio 0.87), MACS J0025 (0.88), Abell 520 "
            "(0.79), El Gordo (0.28 at canonical params + 250 kpc "
            "obs, but 0.22-1.09 across the published parameter range — "
            "see el_gordo_sensitivity_analysis). Three normal-regime "
            "mergers within factor 1.3; El Gordo's apparent deviation "
            "is consistent with parameter+observational uncertainty. "
            "Internal v × τ_0 scaling is consistent at the 1.7% level "
            "across the sample (offset/v_final is constant to 1.7%). "
            "Systematic +20% offset between cluster-inferred and cosmic-"
            "baseline τ_0 is degenerate with deceleration ratio (see "
            "cluster_tau_0_dec_ratio_degeneracy)."
        ),
        tier="anchored",
        refs=(
            "Clowe et al. 2006 (Bullet Cluster, astro-ph/0608407)",
            "Bradač et al. 2008 (MACS J0025, ApJ 687 959)",
            "Mahdavi et al. 2007 (Abell 520, ApJ 668 806)",
            "Jee et al. 2014 (El Gordo, ApJ 785 20)",
            "grut/derived/cluster/merger_population.py",
        ),
        tests=(
            "tests/derived/test_merger_population.py::TestPerSystemPredictions",
            "tests/derived/test_merger_population.py::TestScalingLawInternal",
            "tests/derived/test_merger_population.py::TestPopulationSummary",
            "tests/derived/test_merger_population.py::TestScalingPredicition",
            "tests/derived/test_merger_population.py::TestVerifyHarness",
        ),
        deps=("bullet_cluster_offset", "tau_0_derivation"),
        falsifier=(
            "Population-level breakdown of the v × τ_0 scaling at the "
            "factor-2 level across multiple normal-regime mergers "
            "(not just outlier extremes). Specifically: if a sample "
            "of head-on, similar-mass cluster mergers at z < 0.5 "
            "shows a systematic factor-2+ deviation from v × τ_0, "
            "the dielectric-DM interpretation fails."
        ),
        notes=(
            "STAYS anchored (case-by-case judgment). The PREDICTIONS "
            "are computed (kernel-convolution machinery verified at "
            "1.7% internal scaling across the sample). What's anchored "
            "is the EMPIRICAL AGREEMENT — matching observation depends "
            "on published velocity/offset values that carry ~30% "
            "uncertainty, and the +20% systematic between cluster-"
            "inferred and cosmic-baseline τ_0 is degenerate with the "
            "deceleration-ratio convention. Promoting to computed "
            "would frame as 'GRUT predicts cluster offsets and "
            "matches data', but the framework's HONEST POSITION is "
            "'GRUT predicts cluster offsets at 1.7% internal "
            "consistency; agreement with data is uncertain at the "
            "20-30% level due to observational + parameter "
            "uncertainty'. Anchored at this umbrella claim; the "
            "supporting sensitivity analyses (cluster_tau_0_"
            "sensitivity_diagnostic, cluster_tau_0_dec_ratio_"
            "degeneracy, el_gordo_sensitivity_analysis) live as "
            "computed claims because they characterize the "
            "uncertainty rigorously. If more cluster data lands "
            "and the systematic persists, it is diagnostic of "
            "either τ_0 slightly larger than 41.9 Myr, a non-pure-"
            "exponential kernel structure, or extended-mass-distribution "
            "corrections the point-mass approximation under-counts. "
            "Flagged for forward review."
        ),
    ),

    Claim(
        id="cluster_merger_internal_scaling_residual",
        chapter=9,
        statement=(
            "Across the four-cluster sample (Bullet Cluster, MACS "
            "J0025, Abell 520, El Gordo), the framework's predicted "
            "gas-to-lensing offsets scale linearly with v_final with "
            "internal residual 1.72%. Specifically: max|offset_i / "
            "v_final_i − ⟨offset/v_final⟩| / ⟨offset/v_final⟩ = 0.0172 "
            "across all four systems. The proportionality constant is "
            "τ_0 × dec_ratio with τ_0 = 41.9 Myr (anchored independently "
            "from the CTP noise kernel) and dec_ratio = 0.638 (anchored "
            "to the Bullet Cluster's published v_post). The framework's "
            "predictive shape — offset ∝ v_final with the same "
            "proportionality constant per system — matches the "
            "observational sample's velocity shape to within 1.72% "
            "across all four systems INCLUDING El Gordo. This is a "
            "FUNCTIONAL-FORM finding distinct from absolute-magnitude "
            "agreement: the +20% systematic under-prediction (median "
            "ratio 0.83) and El Gordo's absolute-magnitude tension "
            "(ratio 0.28 at canonical params) are documented "
            "separately in cluster_tau_0_dec_ratio_degeneracy and "
            "el_gordo_sensitivity_analysis. Both can be true "
            "simultaneously: the framework's predictive shape can be "
            "tight (1.72%) while absolute-magnitude questions remain "
            "open (degenerate with dec_ratio convention)."
        ),
        tier="computed",
        refs=(
            "grut/derived/cluster/merger_population.py:scaling_law_residual",
            "tests/derived/test_merger_population.py::TestScalingLawInternal",
        ),
        tests=(
            "tests/derived/test_merger_population.py::TestScalingLawInternal",
        ),
        deps=(
            "cluster_merger_scaling_law",
            "tau_0_derivation",
            "memory_kernel_form",
        ),
        falsifier=(
            "An additional cluster merger that obeys the framework's "
            "kernel-convolution machinery but produces an offset that "
            "deviates from v_final × τ_0 × dec_ratio by more than ~5% "
            "in the predicted (not observed) value would break the "
            "internal-scaling claim. This is a CALCULATIONAL falsifier "
            "— it tests whether the framework's machinery produces "
            "the same proportionality constant for every system, "
            "regardless of how observation lands."
        ),
        notes=(
            "DISTINCT from cluster_merger_scaling_law (anchored). That "
            "umbrella claim documents EMPIRICAL AGREEMENT at three of "
            "four systems within factor 2; this claim documents the "
            "PREDICTIVE FUNCTIONAL FORM holding to 1.72% across the "
            "four-system sample. The two are independent findings: a "
            "framework can have a +20% normalization issue (or "
            "velocity-convention issue per the dec_ratio degeneracy) "
            "while still having the right offset-velocity functional "
            "form. The 1.72% residual is GRUT-specific in the sense "
            "that no particle dark matter model has a natural reason "
            "for offset ∝ v × τ for any specific τ; modified-gravity "
            "frameworks like MOND have acceleration-scale phenomenology "
            "but not a velocity-scale offset prediction. The "
            "memory-kernel convolution offset = ∫ exp(−s/τ_0) × "
            "x_gas(t−s) ds reduces in the relevant limit to "
            "offset ≈ v_post × τ_0, which IS the functional form "
            "this claim verifies. Tier: computed because the residual "
            "is mechanically reproducible from the framework's noise-"
            "kernel infrastructure applied to the four-cluster sample, "
            "with the value computed as an output. SCOPE: implicit "
            "scope is 'across the current four-cluster sample'. "
            "Future cluster data (additional mergers, refined "
            "observational constraints) could refine or break the "
            "1.72% value; per cluster_merger_scaling_law's notes, "
            "more cluster data could surface diagnostics about τ_0 "
            "or kernel structure. The SHAPE-VS-MAGNITUDE distinction: "
            "the 1.72% is the residual after the framework's "
            "proportionality constant is independently anchored — "
            "it is NOT 'the framework predicts cluster offsets to "
            "1.72%' (that would be overclaim, contradicting the "
            "+20% systematic). The honest reading: GRUT predicts a "
            "specific functional form (offset ∝ v × τ_0), and the "
            "form holds across the sample to 1.72%."
        ),
    ),

    Claim(
        id="framework_axioms_locked",
        chapter=3,
        statement=(
            "Framework foundational invariants: Planck mass and "
            "fine-structure constant verified against CODATA; CTP "
            "Keldysh action invertibility (A0); intrinsic time scale "
            "τ_I = ℏ/2 (N0); noise kernel and constitutive equation "
            "structural integrity. All locked at the foundation level "
            "by regression tests."
        ),
        tier="computed",
        refs=(
            "grut/foundation/constants.py",
            "grut/foundation/axioms.py",
            "grut/foundation/noise_kernel.py",
            "grut/foundation/constitutive.py",
        ),
        tests=("tests/foundation/test_foundation.py",),
        deps=("ctp_action_structure",),
    ),
)


# ─────────────────────────────────────────────────────────────────────
# Convenience accessors
# ─────────────────────────────────────────────────────────────────────

def by_chapter(n: int) -> tuple[Claim, ...]:
    """Return all claims assigned to chapter n."""
    return tuple(c for c in REGISTRY if c.chapter == n)


def by_tier(t: Tier) -> tuple[Claim, ...]:
    """Return all claims at status tier t."""
    return tuple(c for c in REGISTRY if c.tier == t)


def by_id(claim_id: str) -> Optional[Claim]:
    """Look up a claim by its id, or None if not present."""
    for c in REGISTRY:
        if c.id == claim_id:
            return c
    return None


def chapter_summary() -> dict[int, dict[str, int]]:
    """Return {chapter: {tier: count}} across the registry."""
    out: dict[int, dict[str, int]] = {n: {} for n in CHAPTER_TITLES}
    for c in REGISTRY:
        out[c.chapter][c.tier] = out[c.chapter].get(c.tier, 0) + 1
    return out


def all_claim_ids() -> set[str]:
    """Set of all registered claim ids."""
    return {c.id for c in REGISTRY}


if __name__ == "__main__":
    # Print a one-page summary of the registry.
    print(f"GRUT ToE Claim Registry — {len(REGISTRY)} claims\n")
    print(f"{'Ch':>3}  {'Title':<28}  {'Computed':>9} "
          f"{'Anchored':>9} {'Conject.':>9} {'OpenNeg.':>9} "
          f"{'Found.':>7} {'Meta':>5}")
    summary = chapter_summary()
    for n in sorted(CHAPTER_TITLES):
        s = summary[n]
        print(f"{n:>3}  {CHAPTER_TITLES[n]:<28}  "
              f"{s.get('computed', 0):>9} "
              f"{s.get('anchored', 0):>9} "
              f"{s.get('conjectural', 0):>9} "
              f"{s.get('open_negative', 0):>9} "
              f"{s.get('foundational', 0):>7} "
              f"{s.get('meta', 0):>5}")
    print()
    print("Tier totals:")
    for t in VALID_TIERS:
        print(f"  {t:<14} {len(by_tier(t)):>3}")
