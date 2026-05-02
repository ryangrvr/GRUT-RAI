"""GRUT ToE — Open-Question Ledger.

A state machine for every open_negative claim in the registry. For
each gap, the ledger records:

    closure_condition  — what would close it (specific, falsifiable)
    closure_effort     — rough resource estimate (e.g. "~3 weeks
                         specialist work", "Phase-1+ task")
    affects            — which downstream claims would be hardened
                         if this opens
    blocked_by         — upstream gaps that must close first
    chapter            — the ToE chapter where this open negative
                         is documented (Chapter 12 in the canonical
                         document, but an open negative may also
                         surface in other chapters)
    last_review        — when the gap was last assessed

This module feeds Chapter 12 of the ToE document. Claude Code reads
the ledger; the chat partner uses it to write honest-negative
sections without hand-curating the same information across documents.

Adding a new gap
----------------
Append a `LedgerEntry` to OPEN_NEGATIVES and re-run the enforcement
test (tests/toe/test_ledger.py). The test verifies every open_negative
claim in the registry has a corresponding ledger entry, and every
ledger entry points to a real registry claim.
"""

from __future__ import annotations

from dataclasses import dataclass

from grut.toe.registry import REGISTRY, by_id


@dataclass(frozen=True)
class LedgerEntry:
    """One open-negative entry in the ledger."""
    claim_id: str            # matches a registry claim's id
    closure_condition: str   # specific test that would close it
    closure_effort: str      # rough estimate (weeks, months, "Phase-1+")
    affects: tuple[str, ...] = ()      # downstream claim ids
    blocked_by: tuple[str, ...] = ()   # upstream open-negative claim ids
    last_review: str = ""    # ISO date


# ─────────────────────────────────────────────────────────────────────
# Open-negative ledger — one entry per registry claim with tier='open_negative'
# ─────────────────────────────────────────────────────────────────────

OPEN_NEGATIVES: tuple[LedgerEntry, ...] = (

    LedgerEntry(
        claim_id="tji_7_4_open_negative",
        closure_condition=(
            "Curved-space TJI on Euclidean S⁴ produces the FeynCalc-"
            "claimed +7/4 from a fully verified Laurent expansion in "
            "MS-bar (or any consistent scheme). Specifically, the "
            "Allen-Jacobson S⁴ propagator must be activated and a "
            "scheme-coherent reconciliation produced — not a Phase-0/0.5 "
            "flat-space calculation."
        ),
        closure_effort=(
            "~3 weeks specialist work (Phase-1; requires curved-space "
            "TJI machinery + scheme-handling). The Allen-Jacobson stub "
            "module sits ready as the entry point."
        ),
        affects=(
            "three_routes_convergence",  # would become 3-way computed
            "r_canonical_path_g",        # downstream-strengthened
            "h_inf_decomposition",       # H_∞ formula gains a 3rd route
        ),
        blocked_by=("allen_jacobson_phase1_stub_open_negative",),
        last_review="2026-04-26",
    ),

    LedgerEntry(
        claim_id="koide_phase_4_open_negative",
        closure_condition=(
            "A computational mechanism that fixes (M_0, θ) from the "
            "framework's machinery — i.e. the Z_3 circulant operator "
            "is no longer a 2-parameter family but a unique solution "
            "to a CTP-derived constraint. Track II Phase 4.0 scope "
            "document delivered; Phase 4 itself remains open."
        ),
        closure_effort=(
            "Open-ended; multiple research-tier attempts have produced "
            "honest negatives. Phase-2+ task at minimum."
        ),
        affects=(
            "sm_emergence",      # uniqueness sub-claim becomes computed
            "koide_z3_circulant_structure",
        ),
        last_review="2026-04-26",
    ),

    LedgerEntry(
        claim_id="neutrino_z3_coupling_derivation_open_question",
        closure_condition=(
            "Derive the neutrino Z₃ coupling a_ν = 1 (giving "
            "K_ν = 1/2) from GRUT primitives, parallel to the "
            "charged-lepton derivation a_e = √2 (giving K_e = 2/3) "
            "from the Komargodski-Schwimmer real-scalar trace anomaly. "
            "Closure paths: (a) Identify a Dirac-ν KS coefficient "
            "yielding a = 1; (b) derive a from SU(2)_L × U(1)_Y × "
            "Dirac-ν Yukawa structure; (c) sterile-neutrino-sector "
            "contribution; (d) show a = 1 is the unique value for "
            "which exactly ONE hierarchy admits an interior "
            "(non-boundary) generic solution. Path (d) is the "
            "tractable closure — a uniqueness theorem about "
            "interior-solution existence as a function of a."
        ),
        closure_effort=(
            "Path (d) is ~1-2 weeks of analytic + numerical work to "
            "establish the uniqueness theorem. Paths (a)/(b)/(c) are "
            "research-tier (months) and connect to the broader Koide "
            "Phase 4 mechanism question."
        ),
        affects=(
            "neutrino_hierarchy_z3_nh_prediction",
            "charged_lepton_z3_does_not_extend_to_neutrinos",
        ),
        blocked_by=(),
        last_review="2026-05-01",
    ),

    LedgerEntry(
        claim_id="path_f_translation_gap",
        closure_condition=(
            "A mapping from published Im(W) on de Sitter (which "
            "computes particle-production rates via Bogoliubov "
            "coefficients) to V7's R = |C_Cosmo / C_Final| ratio, OR "
            "an alternate Path F formulation that produces the "
            "framework's R directly. Multiple literature scopings "
            "have documented the gap."
        ),
        closure_effort=(
            "Research-tier; depends on whether the gap is a "
            "convention difference or a deeper mismatch."
        ),
        affects=("r_canonical_path_g",),  # would add an Im(Γ) route
        last_review="2026-04-26",
    ),

    LedgerEntry(
        claim_id="rho_max_scale_open_question",
        closure_condition=(
            "Either (a) demonstration that ρ_max ~ 10⁻²² kg/m³ is "
            "compatible with observed BH interior dynamics under "
            "specific Whole-Hole geometry, OR (b) derivation of "
            "additional structure (e.g. curvature-dependent τ_eff) "
            "that produces quantitatively realistic core sizes "
            "without breaking the universal-τ_0 derivation upstream."
        ),
        closure_effort=(
            "Phase-1+ task. Requires either observational constraint "
            "or derived correction to the universal formula."
        ),
        affects=("rho_max_universal", "bh_information_partial"),
        last_review="2026-04-26",
    ),

    LedgerEntry(
        claim_id="track_v_coupling_unification_open_question",
        closure_condition=(
            "Derive the constitutive β-function correction Δβ(α_eff(ω)) "
            "from the CTP action's gauge-coupling renormalization in "
            "the responsive-vacuum framework, and verify numerically "
            "that this correction closes the 8.9% unification miss at "
            "the predicted GUT scale. Falsifier path: high-precision "
            "future-collider measurement showing the SM couplings do "
            "NOT unify at any scale would falsify the framework's "
            "gauge-structural prediction independent of the β correction."
        ),
        closure_effort=(
            "Specialist QFT-renormalization-group work, ~6-12 months. "
            "Requires fluency in two-loop SM β-functions plus the "
            "constitutive-projection machinery in the gauge sector."
        ),
        affects=("sm_emergence",),
        last_review="2026-04-27",
    ),

    LedgerEntry(
        claim_id="vorton_track_vii_open_negative",
        closure_condition=(
            "Either (a) the vorton mass M_vorton/M_soliton factor-450 "
            "discrepancy is closed by additional structure in the "
            "topological-defect calculation, OR (b) the dielectric DM "
            "interpretation supersedes the particulate route entirely "
            "and Track VII Step 3 is retired."
        ),
        closure_effort=(
            "Research-tier. The dielectric route (dielectric_dm_reframing) "
            "is the framework's preferred path; vorton physics may not "
            "need to close — the open negative is preserved as honest "
            "documentation of a route that was attempted."
        ),
        affects=("dark_sector_u1_extension",),
        last_review="2026-04-26",
    ),

    LedgerEntry(
        claim_id="allen_jacobson_phase1_stub_open_negative",
        closure_condition=(
            "Phase-1 implementation of the Allen-Jacobson S⁴ propagator "
            "module — i.e. all evaluation functions return numerical "
            "values rather than raising Phase1Pending. This unlocks "
            "curved-space TJI calculations that in turn unlock "
            "tji_7_4_open_negative."
        ),
        closure_effort=(
            "~3 weeks specialist work — same envelope as TJI Phase-1 "
            "since they're tightly coupled."
        ),
        affects=("tji_7_4_open_negative",),
        last_review="2026-04-26",
    ),

    LedgerEntry(
        claim_id="phi_munu_frw_beyond_wkb_open_question",
        closure_condition=(
            "PHASE 2C COMPLETE (Correction #25, 2026-05-01). The "
            "explicit FRW susceptibility χ_FRW^WKB(k, η) = "
            "1 / [1 + (τ_0 k_phys)²] is now derived structurally "
            "in grut.derivation.phi_munu.frw_explicit, with all "
            "three limits verified at code level: sub-horizon "
            "(GR recovery), super-horizon (full constitutive, "
            "n_g² → 4/3), transition (k_phys = 1/τ_0, λ_* ≈ 80.7 "
            "Mpc today). REMAINING WORK: beyond-WKB extension "
            "(Phase 2D) — the next-order correction "
            "χ_FRW = χ^WKB × [1 + O((H_c τ_0)²)]. The correction "
            "is dimensionally suppressed: today (H_0 τ_0)² = "
            "1/(108π)² ≈ 8.7×10⁻⁶; similar across post-equality "
            "cosmology. Closure paths: (a) WKB matching beyond "
            "leading order; (b) numerical Green-function integration "
            "on specific FRW expansion histories (radiation, matter, "
            "ΛCDM); (c) symbolic resummation under specific "
            "expansion ansätze. The correction is NOT operationally "
            "load-bearing for any current cosmological observable — "
            "current data does not constrain (H τ_0)² corrections "
            "at the 10⁻⁶ level."
        ),
        closure_effort=(
            "Research-tier; no operational urgency. Phase 2C "
            "(Correction #25) lands the WKB result that IS "
            "operationally complete for late-universe cosmology. "
            "Beyond-WKB matters only in the radiation era for modes "
            "that crossed k_* during that era. ~2-4 weeks specialist "
            "work if needed; deferred until cosmological precision "
            "demands it."
        ),
        affects=(
            "gr_recovery",
            "phi_munu_linearized_derivation",
            "phi_munu_curved_background_scaffold",
            "phi_munu_frw_explicit_construction",
        ),
        blocked_by=(),
        last_review="2026-05-01",
    ),

    LedgerEntry(
        claim_id="two_route_convergence_physical_equivalence_open_question",
        closure_condition=(
            "Articulate the physical statement that makes Path G "
            "(α=1/3 from conformal-mode scalar) and Osborn ε at M_Z "
            "(QCD-dominant gauge-coupling correction) compute the "
            "same physical quantity. Likely path: derivation showing "
            "that under the conformal-mode-as-IR-carrier postulate, "
            "the Osborn ε-combined at the EW matching scale reduces "
            "to a/c = 1/3 at leading order (the Gibbons-Hawking "
            "thermal-asymmetry argument in ZENODO_EPSILON_"
            "IDENTIFICATION.md gestures at this but does not "
            "complete it). Alternative: explicitly state the "
            "agreement is empirical, not structural."
        ),
        closure_effort=(
            "Theoretical work, ~2-4 weeks. Requires fluency in "
            "trace-anomaly literature and the local-coupling "
            "formalism. The ZENODO doc has the partial argument; "
            "completing it is the task."
        ),
        affects=("three_routes_convergence",),
        blocked_by=(),
        last_review="2026-04-26",
    ),

    # n_g_omega_cosmological_covariance_open_question RESOLVED by
    # Correction #26 (Priority 3, 2026-05-01). All three closure
    # conditions met: ω → k_phys c identification, gauge-invariance
    # at WKB, μ(k,a)/γ(k,a) MG-EFT mapping. Ledger entry retired —
    # the resolved claim is tracked under id
    # n_g_omega_cosmological_covariance_resolved (meta tier, Ch 12)
    # plus the new computed claim mg_eft_mu_gamma_mapping (Ch 9).
    # See theory/derivation/CORRECTION_26_PRIORITY_3_CLOSURE.md.

    LedgerEntry(
        claim_id="el_gordo_outlier_open_question",
        closure_condition=(
            "Either: (a) tighter observational constraints on El "
            "Gordo's velocity/geometry/lensing reconstruction that "
            "bring the observed gas-to-lensing offset into the v×τ_0 "
            "band (within factor 2), OR (b) extension of the kernel "
            "model to off-axis / asymmetric-mass collisions producing "
            "a derived correction factor that explains the ~3.5× "
            "deviation, OR (c) an additional cluster sample showing "
            "the v×τ_0 scaling extends across all merger types and "
            "El Gordo is the documented exception."
        ),
        closure_effort=(
            "Phase-2+. Depends on either new observational data or "
            "an analytic extension of the kernel-convolution model. "
            "Observational data may resolve before the model needs "
            "extension."
        ),
        affects=("cluster_merger_scaling_law",),
        last_review="2026-04-26",
    ),

    LedgerEntry(
        claim_id="nonlinear_ladder_4_of_8",
        closure_condition=(
            "Closure of rungs 5-8 of the nonlinear ladder: tensor-"
            "sector stability at 2nd order, diffeomorphism invariance "
            "preservation, background independence, and a non-"
            "perturbative fixed point. Each rung is a separate "
            "research program."
        ),
        closure_effort=(
            "Multi-phase. Rungs 5-6 are tractable in Phase-2 timeframes; "
            "rungs 7-8 are open research."
        ),
        affects=("gr_recovery", "bh_information_partial"),
        last_review="2026-04-26",
    ),

    LedgerEntry(
        claim_id="tau_zero_to_tau_micro_relation_open_question",
        closure_condition=(
            "DIMENSIONAL CLOSURE COMPLETE (Correction #22, 2026-04-30). "
            "The framework now defines τ_micro ≡ ℏ/(k_B × T_c) ≈ "
            "1.4×10⁻¹⁹ s explicitly in closure_protocol.py:TAU_MICRO_SEC, "
            "uses the SI-correct formula T_c = ℏ/(τ_micro × k_B), and "
            "names the 34-orders-of-magnitude separation from τ_0 in "
            "the registry (claim tau_micro_thermal_scale, anchored "
            "tier). The previous open-negative "
            "(t_c_provenance_inconsistency_open_negative) is "
            "RESOLVED at the dimensional level — see "
            "t_c_provenance_inconsistency_resolved (meta-tier). "
            "REMAINING OPEN QUESTION: derive (or formally accept the "
            "absence of) a closure path between τ_0 and τ_micro. "
            "Path (a) — derivation from CTP plasma dynamics: open. "
            "Path (b) — identification with a known atomic/nuclear "
            "timescale: open. Path (c) — acknowledge two independent "
            "inputs: open as the honest-negative outcome that "
            "downgrades the framework's 'zero free parameters in the "
            "predictive core' framing to 'one free parameter (τ_0) "
            "in the gravitational predictive core; one anchored "
            "parameter (τ_micro) in the thermal sector'. Path (d) — "
            "BBN-mediated bridge: FALSIFIED by bbn_thermal_buffer_"
            "negligible (the 10-orders-of-magnitude shortfall rules "
            "out BBN as the τ_0↔τ_micro bridge). Closure of this "
            "open question proceeds either via paths (a)/(b) — "
            "research-tier work — or via formal acceptance of path "
            "(c) — registry-tier framing change."
        ),
        closure_effort=(
            "Multi-session research for paths (a)/(b). Path (c) is "
            "a registry-tier framing change closeable in one "
            "coordinated session: update Ch 1 predictions table "
            "footer, Ch 2 Medium framing, Appendix C glossary, and "
            "the v8/v2 deposit posture statement to make the two-"
            "scale structure explicit and lower the 'zero free "
            "parameters' claim to 'zero in gravitational sector + "
            "one anchored in thermal sector'. The dimensional bug "
            "(tracked under the original claim id) is closed; this "
            "ledger entry tracks only the relation-derivation "
            "question."
        ),
        affects=(
            "t_c_thermal_transition",   # registry claim for T_c
            "tau_micro_thermal_scale",  # registry claim for τ_micro
        ),
        blocked_by=(),  # research question, not blocked by other open negatives
        last_review="2026-04-30",
    ),

    LedgerEntry(
        claim_id="primordial_amplitude_zero_parameter_open_negative",
        closure_condition=(
            "Closure paths re-stated post-Correction-#26 (which "
            "RESOLVED n_g_omega_cosmological_covariance, the upstream "
            "blocker): (a) DOWNGRADED — with the MG-EFT mapping now "
            "explicit (μ_GRUT = n_g²(k, a), γ_GRUT = 1), the natural "
            "rescaling is the FRW-mode-dependent k_phys/τ_0 argument; "
            "Stage-2's α/S³ family becomes the cosmic-baseline (DC) "
            "limit at k → 0. The 'natural rescaling' question is now "
            "structurally answered by the Phase 2C result. The "
            "remaining gap is whether A_s = α_vac/(π S³) ≈ 8.15×10⁻⁹ "
            "(close to observed but factor 4 off) is the framework's "
            "actual prediction or a coincidence. OR (b) the Genesis "
            "Hypothesis (Appendix A) is formalized providing an "
            "inflationary-like epoch with H ~ 10⁻⁵ M_Pl during "
            "horizon crossing of the CMB pivot mode (independent "
            "path). OR (c) physically-motivated derivation linking "
            "α/S³ family to the noise-kernel structure. OR (d) "
            "explicit acknowledgment that A_s is observation-anchored "
            "input."
        ),
        closure_effort=(
            "Multi-phase research. Closure path (a) is no longer "
            "blocked — Correction #26 closed n_g_omega_cosmological_"
            "covariance. Path (a) is now reframed: with "
            "μ_GRUT(k, a) explicit, the 'rescaling' question is "
            "specialized to whether the framework predicts the "
            "PIVOT-mode A_s ≈ 2.1×10⁻⁹ at k = 0.05 Mpc⁻¹. This is "
            "a Boltzmann-code-level computation (modify CAMB/CLASS "
            "to use μ_GRUT, integrate primordial fluctuation "
            "evolution, compare to observed A_s). Path (b) blocked "
            "by Genesis Hypothesis becoming formal/computable. "
            "Path (c) requires identifying the GRUT analog of "
            "primordial curvature ζ. Path (d) is operational and "
            "always available."
        ),
        affects=("h_0_prediction",),
        blocked_by=(),  # n_g_omega resolved; this entry no longer blocked
        last_review="2026-05-01",
    ),

    LedgerEntry(
        claim_id="n_total_zero_parameter_derivation_open_question",
        closure_condition=(
            "Derive cosmic age t_0 — equivalently the era count "
            "N_total = t_0/τ_0 = 329 — from framework foundations "
            "alone, without using observed cosmic age as input. The "
            "era-map post-threshold dynamics must produce N_total = "
            "329 as a structural endpoint (not a fit to observation). "
            "Likely precondition: the Genesis Hypothesis (V7/V8 "
            "Appendix A) being formalized to the point where the "
            "start time of cosmic evolution emerges from the null "
            "fixed point's destabilization timescale. Genesis "
            "Hypothesis is currently [SPECULATIVE]; closure does NOT "
            "require adopting it as a postulate — it requires the "
            "hypothesis's machinery becoming computable. Alternative "
            "closure paths: (a) derive Ω_m today from baryogenesis "
            "(Ω_b = 0.048 already computed) plus a first-principles "
            "Ω_dm derivation that doesn't currently exist (Track VII "
            "Step 3 closed negative), or (b) anchor cosmic age to a "
            "structurally-predicted event (e.g. CMB decoupling "
            "conditions from SM thermodynamics)."
        ),
        closure_effort=(
            "Multi-phase research. Blocked by Genesis Hypothesis "
            "becoming formal/computable rather than purely "
            "conjectural. Four direct attempts already documented "
            "as honest-negative in N_TOTAL_DERIVATION_ATTEMPT.md "
            "(matter-Λ equality structural anchor, era-map "
            "saturation, flat-ΛCDM total age, reverse-engineered "
            "Ω_m). Closure tied to Track VII Step 3 status (vorton "
            "Ω_dm derivation closed negative; dielectric route "
            "preferred but not yet zero-parameter)."
        ),
        affects=("h_0_prediction",),  # the detailed Friedmann route
        blocked_by=(),  # blocked by speculative content (Genesis Hypothesis), not a registered open negative
        last_review="2026-04-27",
    ),

    LedgerEntry(
        claim_id="born_rule_postulate_open_negative",
        closure_condition=(
            "Born rule probabilities |⟨ψ|pointer_i⟩|² do not derive "
            "from the gravitational noise kernel N_grav alone. The "
            "CTP machinery produces decoherence rates and noise "
            "structure (i.e. THE RATE at which classical states "
            "emerge: Λ_grav at the relevant pointer parameters) "
            "but does not on its own produce probability "
            "assignments (i.e. THE WEIGHTS classical states inherit "
            "on the diagonal of the asymptotic density matrix). "
            "Closure paths: (a) introduce decoherent-histories "
            "weighting explicitly, deriving Born rule from a "
            "history-weighted decoherence functional; (b) add "
            "einselection-with-history-tracking, where pointer-basis "
            "probabilities derive from the dynamics that select the "
            "basis; (c) derive the path-integral weight from a "
            "deeper symmetry principle the framework does not yet "
            "have. The framework registers this as an open question "
            "rather than supplying the postulates informally. This "
            "is not a GRUT-specific weakness; current quantum "
            "foundations programs (Copenhagen, Many-Worlds, "
            "decoherent histories, CSL) all require additional "
            "structure for Born-rule derivation."
        ),
        closure_effort=(
            "Multi-decade research program. Born rule derivation "
            "from underlying dynamics has resisted closure for "
            "nearly a century across all quantum-foundations "
            "programs. Path (a) is the most tractable in the "
            "framework's current machinery — decoherent-histories "
            "formalism would integrate naturally with the existing "
            "CTP infrastructure. Paths (b) and (c) are deeper "
            "research, likely requiring tools beyond GRUT's current "
            "scope. None of the three closure paths is in scope "
            "for the v1 deposit; all are research-tier follow-on "
            "work post-deposit."
        ),
        affects=(
            "lambda_contact_ctp_derivation",
            "wigner_friend_dissolution",
        ),
        blocked_by=(),  # foundational quantum-mechanics issue, not blocked by a registered open negative
        last_review="2026-04-29",
    ),
)


# ─────────────────────────────────────────────────────────────────────
# Convenience accessors
# ─────────────────────────────────────────────────────────────────────

def by_claim(claim_id: str) -> LedgerEntry | None:
    for e in OPEN_NEGATIVES:
        if e.claim_id == claim_id:
            return e
    return None


def all_claim_ids_in_ledger() -> set[str]:
    return {e.claim_id for e in OPEN_NEGATIVES}


def open_negatives_in_registry() -> set[str]:
    """Set of registry claim ids with tier='open_negative'."""
    return {c.id for c in REGISTRY if c.tier == "open_negative"}


def coverage_report() -> dict:
    """Report which open negatives in the registry are covered by the ledger."""
    in_ledger = all_claim_ids_in_ledger()
    in_registry = open_negatives_in_registry()
    return {
        "ledger_entries":           sorted(in_ledger),
        "registry_open_negatives":  sorted(in_registry),
        "in_registry_not_ledger":   sorted(in_registry - in_ledger),
        "in_ledger_not_registry":   sorted(in_ledger - in_registry),
        "coverage_complete":        in_registry == in_ledger,
    }


def closure_dependency_chain(claim_id: str) -> tuple[str, ...]:
    """Walk the blocked_by chain — what other open negatives must close first?"""
    chain: list[str] = []
    visited: set[str] = set()

    def walk(cid: str) -> None:
        if cid in visited:
            return
        visited.add(cid)
        entry = by_claim(cid)
        if entry is None:
            return
        for blocker in entry.blocked_by:
            chain.append(blocker)
            walk(blocker)

    walk(claim_id)
    return tuple(chain)


def affects_summary() -> dict[str, tuple[str, ...]]:
    """For each claim_id in the ledger: which downstream claims it affects."""
    return {e.claim_id: e.affects for e in OPEN_NEGATIVES}


if __name__ == "__main__":
    rep = coverage_report()
    print("=" * 72)
    print("Open-Question Ledger — coverage")
    print("=" * 72)
    print(f"  ledger entries:              {len(rep['ledger_entries'])}")
    print(f"  registry open_negatives:     {len(rep['registry_open_negatives'])}")
    print(f"  coverage complete:           {rep['coverage_complete']}")
    if rep["in_registry_not_ledger"]:
        print()
        print("⚠  Registry open_negatives WITHOUT ledger entries:")
        for c in rep["in_registry_not_ledger"]:
            print(f"      {c}")
    if rep["in_ledger_not_registry"]:
        print()
        print("⚠  Ledger entries WITHOUT a registry claim:")
        for c in rep["in_ledger_not_registry"]:
            print(f"      {c}")

    print()
    print("=" * 72)
    print("Per-entry affects map")
    print("=" * 72)
    for cid, affects in affects_summary().items():
        print(f"  {cid}")
        for a in affects:
            print(f"     → {a}")
