"""GRUT-RAI v4.1 — the registry. Foundation first, then house.

Every claim is a gate.Claim. The build (ci_check.py) runs gate.validate over this
registry; it must return zero violations. The audit (audit.py) renders the
one-pass reader view. This file is small ON PURPOSE: the brief forbids expanding
sectors before the two OPEN targets (K̃, S⁴ a/c) land. Breadth on an unproven
footing is the v4 baggage in cleaner code.
"""
from __future__ import annotations

from v41.gate import Claim, Tier, Novelty, Step
from v41 import checks
from v41.falsifiers import decoherence_689hz as decoh

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

    # ── FOUNDATION: α is the one OPEN gap left (single-pole was re-tiered ANCHOR by 1C) ──
    Claim("alpha",
          "α = 1/3 — the dimensionless vacuum impedance. ADOPTED: the conditional "
          "a/c = 1/3 is proven, but its antecedent is open.",
          Tier.OPEN, target="S⁴ Riegert/Paneitz a/c — targets/riegert_paneitz.py"),
    Claim("constitutive_law_single_pole",
          "The single-pole constitutive law τ₀ż + z = z_target (χ = α/(1−iωτ₀)) — POSITED, not "
          "derived. Single-pole-ness reduces to ONE number: the IR exponent s of the TT-shear "
          "bath J(ω) (s≥1 ⇒ single-pole theorem; s<1 ⇒ a dark sub-Ohmic continuum). BOTH "
          "derivation routes failed to fix s: flat-space (1B, targets/bath_spectrum.py) and "
          "curved-space de Sitter/FRW (1C, targets/curved_bath.py). s is the bath TRANSPORT "
          "exponent — 1 if collisional (Kubo/finite shear viscosity), the free DOS-edge if "
          "collisionless — and GRUT's Q + FDT + 1/r kernel + KMS(T_c) fix NEITHER the "
          "collisionality NOR the DOS edge. (1C also broke 1B's 'Hubble-friction ⇒ fast' lean and "
          "closed only the de Sitter-IR slow channel.) With both routes exhausted, single-pole-ness "
          "is an ANCHOR (a posited input), not a theorem — it de-anchors only if GRUT later "
          "specifies the bath microphysics. v4's τ_K=τ_micro (assume s=1) was the fast conclusion "
          "smuggled in as an input; now entered HONESTLY as a visible anchor instead.",
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

    # ── A NO-GO (FORBIDDEN) — CONDITIONAL on the single-pole ANCHOR (audit shows SPLIT) ──
    Claim("propagating_relic_no_go",
          "No new propagating vacuum pole may be built from the vacuum's action "
          "(higher-derivative TT operator ⇒ Ostrogradsky ghost ⇒ Im χ<0 ⇒ N<0 by FDT "
          "⇒ Q-violation). The dark-matter no-go and the hierarchy-magnitude no-go are "
          "this same prohibition. SCOPE (re-stated after 1C): this forbids a new UNDAMPED "
          "DISCRETE pole; it is CONDITIONAL on the single-pole ANCHOR. It does NOT exclude the "
          "sub-Ohmic dark CONTINUUM that an s<1 bath would produce — that slow channel is closed "
          "only as a discrete relic (FDT positivity, 1B/1C), not as a continuum.",
          Tier.FORBIDDEN, inputs=("ctp_action", "constitutive_law_single_pole"),
          derivation_ref="Ostrogradsky + Q/FDT pincer; single-mode pole classification",
          novelty=Novelty.REUSED,
          novelty_cite="Ostrogradsky; Stelle/Weyl²; Horndeski/f(R); dRGT/Fierz–Pauli "
                       "(ASSEMBLED from textbook no-gos). GRUT's composition is the "
                       "Q/FDT-unitarity leg (Im χ<0 ⇒ non-unitary in-in)."),

    # ── HOSTED: Ω_Λ rests on α (OPEN), so the gate FORBIDS it being DERIVED ───────
    Claim("omega_lambda",
          "Ω_Λ = 0.6886 — dark energy as the relaxing vacuum's terminal velocity. "
          "Mechanism PLACED; the value is anchored; it consumes α (OPEN), so it is "
          "NOT a derivation. (Planck 0.6889; never conflate with the tree (2−R)²=0.71453.)",
          Tier.HOSTED, inputs=("alpha", "tau0"), step=Step.PLACE),

    # ── CONJECTURAL: the F(t) dark-matter host ───────────────────────────────────
    Claim("ft_dark_matter",
          "Dark matter as a coherent ~10⁻²² eV misalignment scalar resident in the "
          "substrate F(t): specified, not derived — 2 inserted dials, 0-of-3 "
          "requirements sourced from the bath. A sharpened impossibility, not a result.",
          Tier.CONJECTURAL, inputs=("constitutive_law_single_pole",)),
]

REGISTRY = {c.id: c for c in _CLAIMS}
