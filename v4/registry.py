"""GRUT-RAI v4.1 — the registry. Foundation first, then house.

Every claim is a gate.Claim. The build (ci_check.py) runs gate.validate over this
registry; it must return zero violations. The audit (audit.py) renders the
one-pass reader view. The two foundational parameters (single-pole, α) are ANCHORS —
each on a free datum the action does not fix (collisionality; the IR-carrier identity),
established across three rounds of external review. With the kernel carried SWAPPABLE,
the closed-viscoelastic spine (four constitutive inputs) is now pinned, and the first
forward target — the Deborah number running with scale — is a DERIVED consequence that
does NOT depend on resolving the kernel fork.
"""
from __future__ import annotations

from v4.gate import Claim, Tier, Novelty, Step
from v4 import checks
from v4.falsifiers import decoherence_689hz as decoh

_CLAIMS = [
    # ── FOUNDATION: anchors, entered visibly as load-bearing inputs ──────────────
    Claim("ctp_action",
          "The Schwinger–Keldysh closed-time-path (in-in) effective action — the "
          "framework's starting action (the foundational axiom; deriving from it is DERIVED).",
          Tier.ANCHOR, axiom=True),
    Claim("tau0",
          "τ₀ ≈ 41.9 Myr — the macroscopic memory/relaxation time. Measured-type "
          "input; may never be derived.",
          Tier.ANCHOR),
    Claim("tau_micro",
          "τ_micro = ℏ/(k_B T_c) ≈ 1.4×10⁻¹⁹ s — the microscopic correlation scale.",
          Tier.ANCHOR),

    # ── FOUNDATION: α and single-pole are BOTH ANCHORS, each on a free datum the action omits ──
    #    (single-pole: collisionality, Targets 1C/1D; α: the IR-carrier identity, Targets 2/2B)
    Claim("alpha",
          "α = 1/3 — the dimensionless vacuum impedance — POSITED, not derived. GRUT's "
          "conditional theorem is a/c=1/3 ⟹ α=1/3 IF the conformal Riegert mode is the IR "
          "carrier. Target 2 (targets/s4_anomaly.py) computed the CONSEQUENT: a/c=1/3 EXACTLY "
          "for the conformal scalar (Gilkey a₄; scheme-independent central charges; validated vs "
          "Dirac 11/18 and vector 31/18 — so NOT reverse-fit to 1/3). But the ANTECEDENT — "
          "conformal mode = IR carrier — is FREE DATA: the carrier identity is dynamical "
          "(CTP+Q+FDT+1/r fix the dissipative structure, not which mode carries the IR anomaly "
          "— parallel to single-pole's collisionality), and μ_linear=1 (TT projector annihilates "
          "the scalar mode) tensions it (the linear carrier is the TT spin-2 mode). Target 2B "
          "(targets/carrier_identity.py) EXHAUSTED the antecedent on BOTH routes: LINEAR (the TT "
          "projector genuinely annihilates the conformal/trace mode — verified — so the linear "
          "carrier is spin-2) AND ANOMALY (a propagating conformal carrier needs the 4th-order "
          "Riegert/Paneitz kinetic term ⇒ Ostrogradsky ghost ⇒ Im χ<0 ⇒ Q-forbidden, the same "
          "leg as the relic no-go). The anomaly PERMITS at most (the contested Antoniadis–Mottola "
          "conformalon) but does NOT FORCE the carrier. So α is an ANCHOR on TWO exhausted routes, "
          "symmetric with single-pole. De-anchor condition: a legitimate non-ghost conformalon "
          "dominating the IR — itself tensioned by GRUT's Q-unitarity (so not merely unestablished). "
          "Q-unitarity (no new propagating vacuum pole) protects THIS (α) anchor — a propagating-mode "
          "question. CORRECTION (external review, 2026-06-24): it does NOT protect single-pole, which "
          "is a transport / collisionality question Q does not address (a free-streaming continuum is "
          "no new pole). The 'one prohibition, two anchors' unification was over-tight: Q-protection "
          "is real for α only. (single-pole remains an anchor — see its claim — for a DIFFERENT "
          "reason: collisionality is free data.)",
          Tier.ANCHOR, axiom=False),
    Claim("constitutive_law_single_pole",
          "The single-pole constitutive law τ₀ż + z = z_target (χ = α/(1−iωτ₀)). ANCHOR — the "
          "verdict FORKS on collisionality, a free datum the action does not fix (this is the 1C "
          "conclusion, vindicated after three review rounds that wrongly tried to graduate it). "
          "The right object is the finite-T TT transport memory, NOT a vacuum DOS/phase-space "
          "exponent: COLLISIONAL (viscous, T_c) ⇒ Kubo Im G^TT~ηω, exponential/Ohmic kernel ⇒ "
          "single-pole HOLDS; COLLISIONLESS (free-streaming) ⇒ Weinberg 2004 / Hawking 1966 give a "
          "NON-LOCAL Bessel-tail kernel (power-law ~s⁻³, oscillatory, long residual) ⇒ single-pole "
          "FAILS. The action does not say which branch the vacuum is on ⇒ single-pole is a posited "
          "ANCHOR. ERRORS ON RECORD (kept honest): round 1 'DOS fixes s=2' (DOS≠J); round 2 'argued "
          "s≥1 across branches, PENDING_REVIEW' (still leaned on the DOS picture Weinberg overturns; "
          "the s≈2 attributed to the reviewer was a misattribution — their floor was (∂φ)², the "
          "graviton vertex runs to ω⁵ per Cho–Hu, and the vacuum T=0 exponent is the wrong object). "
          "See targets/fast_mode_dos.py.",
          Tier.ANCHOR, axiom=False, notes="de-anchor: prove GRUT's vacuum at T_c is viscous "
          "(⇒ single-pole) or free-streaming (⇒ refuted) — map the z·T_TT vertex onto GW-in-medium "
          "(Weinberg 2004, Hawking 1966 answer each branch)."),

    # ── THE CLOSED-VISCOELASTIC SPINE: four constitutive inputs (the reviewer's forward plan) ──
    #    The medium is a closed viscoelastic solid; these four inputs define it. Pin them as
    #    anchors now; the kernel is SWAPPABLE (the fork is unresolved). Forward targets compute
    #    consequences (Target 3 below: the Deborah mechanism — kernel-independent).
    Claim("relaxation_kernel",
          "INPUT 1 — the relaxation kernel K(t), i.e. the medium's RHEOLOGY, carried as a SWAPPABLE "
          "parameter (NOT a settled value): single-pole (Maxwell) / power-law (critical gel) / "
          "multi-mode. Which one is the collisionality fork (Targets 1C/1D); constitutive_law_single_"
          "pole is its Maxwell instance (holds on the viscous branch, fails — Weinberg non-local — on "
          "the free-streaming branch). Carrying it swappable is the round-3 discipline.",
          Tier.ANCHOR, axiom=False),
    Claim("closure_condition",
          "INPUT 2 — CLOSED system. ENERGY is conserved within the medium (1st law). FINE-GRAINED "
          "information is conserved only under unitary/Liouville evolution — a SEPARATE statement, and "
          "at that level there is no dissipation. At the COARSE-GRAINED level the relaxation kernel and "
          "loss modulus actually describe, memory is redistributed into inaccessible micro-correlations "
          "(operationally lost) and coarse-grained entropy rises. So 'the vacuum remembers ever since' "
          "is literal only fine-grained; at the resolved level it is metaphor — and on the continuum / "
          "free-streaming branch memory radiates to k→∞ and never returns (Poincaré recurrence → ∞). A "
          "posited structural property; the strong 'eternal literal memory' reading is unsupported "
          "(corrected after an adversarial pre-screen, C-D).",
          Tier.ANCHOR, axiom=False),
    Claim("driving_strain",
          "INPUT 3 — the driving strain the medium responds to: the source/forcing whose history the "
          "kernel integrates. Posited as a spine input; its microphysical origin is left open here.",
          Tier.ANCHOR, axiom=False),
    Claim("scale_coupling",
          "INPUT 4 — the scale-coupling: relaxation at one scale feeds structure at the next "
          "('scaling and remembering'). It sets the probe-time-vs-scale law t_probe(L) that makes the "
          "Deborah number run with scale. Posited as a spine input; the explicit cross-scale (RG-like) "
          "map is left open.",
          Tier.ANCHOR, axiom=False),

    # ── FORWARD RUNGS: DERIVED (derivation_ref + passing check + novelty) ─────────
    Claim("Q_causal_arrow",
          "Q — the in-in causal arrow: physics responds only to realized past "
          "differences; the response is causal/retarded (susceptibility pole in the "
          "lower half-ω-plane, kernel zero for t<0).",
          Tier.DERIVED, inputs=("ctp_action",),
          derivation_ref="Schwinger–Keldysh CTP + FDT (analytic structure of χ)",
          check=checks.check_Q_causal_arrow, check_ref="checks.check_Q_causal_arrow",
          step=Step.DERIVE, novelty=Novelty.COMPOSITION,
          novelty_cite="Schwinger–Keldysh in-in formalism + FDT (KNOWN); GRUT's "
                       "composition: Q as the causal-arrow floor and the ORIGIN of the "
                       "dissipative kernel (not an equilibrium assumption)."),
    Claim("mu_linear",
          "μ_linear = 1 — the transverse-traceless projector annihilates the linear "
          "scalar response, so linear cosmology is EXACTLY ΛCDM. α-free and τ₀-free; "
          "the framework's cleanest result.",
          Tier.DERIVED, inputs=("Q_causal_arrow",),
          derivation_ref="P^TT projector theorem (annihilates longitudinal + trace)",
          check=checks.check_mu_linear, check_ref="checks.check_mu_linear",
          step=Step.DERIVE, novelty=Novelty.COMPOSITION,
          novelty_cite="Transverse-traceless projector + μ/γ MG-EFT language (KNOWN); "
                       "NEW: μ_linear=1 as a P^TT no-go for linear scalar modified "
                       "gravity inside an in-in finite-memory vacuum."),
    Claim("arrow_monotone",
          "The arrow of time's MONOTONE FORM: Ṡ = (1/τ₀)⟨(z−z_target)²⟩ ≥ 0 from Q's "
          "retarded kernel, vanishing only at the fixed point. SCOPE: the monotone "
          "form is derived; the low-entropy INITIAL condition (Past Hypothesis) is "
          "INHERITED — not derived here.",
          Tier.DERIVED, inputs=("Q_causal_arrow", "tau0"),
          derivation_ref="constitutive entropy production (sum of squares / τ₀>0)",
          check=checks.check_arrow_monotone_form, check_ref="checks.check_arrow_monotone_form",
          step=Step.DERIVE, novelty=Novelty.COMPOSITION,
          novelty_cite="Second Law / retarded-kernel time-asymmetry (KNOWN); NEW: from "
                       "the in-in constitutive kernel. Initial condition inherited."),
    Claim("qm_recovery",
          "Quantum mechanics recovered as the τ→0 limit: the constitutive update "
          "reduces to the first-order Schrödinger step (norm-preserving; ⟨σ_x⟩=cos ωt). "
          "The Born WEIGHTS are NOT included — a separate inherited boundary.",
          Tier.DERIVED, inputs=("ctp_action",),
          derivation_ref="τ→0 (zero-memory) limit of the constitutive law",
          check=checks.check_qm_recovery, check_ref="checks.check_qm_recovery",
          step=Step.DERIVE, novelty=Novelty.COMPOSITION,
          novelty_cite="Schrödinger equation (KNOWN); NEW: as the zero-memory face of "
                       "the responsive constitutive law."),
    Claim("decoherence_plateau_689",
          "Gravitational-decoherence plateau ≈ 689 Hz (1 μm gold sphere) from the "
          "Diósi/Anastopoulos–Hu kernel + the τ₀-tied scale; the standalone forward "
          "falsifier. Distinguished from Diósi–Penrose by the extended-body F6 kink.",
          Tier.DERIVED, inputs=("Q_causal_arrow", "tau0"),
          derivation_ref="falsifiers/decoherence_689hz.py (G m² S(l/R)/ħl, 0 params)",
          check=decoh.check_plateau, check_ref="falsifiers.decoherence_689hz.check_plateau",
          step=Step.DERIVE, novelty=Novelty.COMPOSITION,
          novelty_cite="Diósi / Anastopoulos–Hu noise kernel, CQG 30 165007 (2013) "
                       "(KNOWN-REUSED); NEW: the extended-body F6 kink + the τ₀-tied plateau."),
    Claim("deborah_runs_with_scale",
          "The closed medium's scale-structure, from the Deborah number De(L)=τ_relax/t_probe(L). On "
          "the single-τ / Maxwell (collisional) branch there is ONE dividing scale L*=c_s·τ_relax — "
          "elastic (holds structure) below, viscous (flows) above — so 'different aspects of reality "
          "at different scales' is literal THERE. On the power-law / free-streaming (Weinberg) branch "
          "there is NO characteristic time, NO L*, and the medium is SCALE-FREE (the same aspect at "
          "every scale). So this does NOT bypass the kernel fork — it presupposes the collisional side; "
          "its value is that the two branches predict DIFFERENT scale-structure (a dividing scale vs "
          "scale invariance), an OBSERVABLE HANDLE on the fork. HOSTED/PLACE: De(L)=c_s·τ/L is "
          "algebraic substitution of two anchors (the kernel's τ + the posited probe law t_probe=L/c_s), "
          "NOT a derivation. The character discriminant is DEGENERATE (many-to-one: closely-spaced "
          "multi-mode mimics Maxwell, a continuum mimics power-law). c_s free; the c_s=c value (~12.9 "
          "Mpc) is suggestive only. (Corrected after an adversarial pre-screen broke the first "
          "'kernel-independent forward motion' framing; targets/deborah_scaling.py.)",
          Tier.HOSTED, inputs=("relaxation_kernel", "scale_coupling", "tau0"), step=Step.PLACE),

    # ── A NO-GO (FORBIDDEN) — forbids a new propagating pole; single-pole is now DERIVED ──
    Claim("propagating_relic_no_go",
          "No new propagating vacuum pole may be built from the vacuum's action "
          "(higher-derivative TT operator ⇒ Ostrogradsky ghost ⇒ Im χ<0 ⇒ N<0 by FDT "
          "⇒ Q-violation). The dark-matter no-go and the hierarchy-magnitude no-go are "
          "this same prohibition. SCOPE (re-stated after external review): this forbids a new "
          "UNDAMPED DISCRETE pole — a propagating-mode statement. It does NOT exclude the free-"
          "streaming CONTINUUM (Weinberg non-local memory) that the collisionless branch produces "
          "— that is no new pole, so this no-go is silent on it. Whether single-pole survives is the "
          "separate collisionality question (an ANCHOR; targets/fast_mode_dos.py), not this no-go.",
          Tier.FORBIDDEN, inputs=("ctp_action", "constitutive_law_single_pole"),
          derivation_ref="Ostrogradsky + Q/FDT pincer; single-mode pole classification",
          novelty=Novelty.REUSED,
          novelty_cite="Ostrogradsky; Stelle/Weyl²; Horndeski/f(R); dRGT/Fierz–Pauli "
                       "(ASSEMBLED from textbook no-gos). GRUT's composition is the "
                       "Q/FDT-unitarity leg (Im χ<0 ⇒ non-unitary in-in)."),

    # ── HOSTED: Ω_Λ — mechanism PLACED, and CONDITIONAL on the α-ANCHOR (Target 2) ───────
    Claim("omega_lambda",
          "Ω_Λ = 0.6886 — dark energy as the relaxing vacuum's terminal velocity. "
          "Mechanism PLACED (not a forward derivation); the value is anchored; and it is "
          "CONDITIONAL on the α-ANCHOR — α=1/3 is itself a posited identification (Target 2), "
          "so ω_Λ inherits that. (Planck 0.6889; never conflate with the tree (2−R)²=0.71453.)",
          Tier.HOSTED, inputs=("alpha", "tau0"), step=Step.PLACE),

    # ── CONJECTURAL: the F(t) dark-matter host ───────────────────────────────────
    Claim("ft_dark_matter",
          "Dark matter as a coherent ~10⁻²² eV misalignment scalar resident in the "
          "substrate F(t): specified, not derived — 2 inserted dials, 0-of-3 "
          "requirements sourced from the bath. A sharpened impossibility, not a result.",
          Tier.CONJECTURAL, inputs=("constitutive_law_single_pole",)),
]

REGISTRY = {c.id: c for c in _CLAIMS}
