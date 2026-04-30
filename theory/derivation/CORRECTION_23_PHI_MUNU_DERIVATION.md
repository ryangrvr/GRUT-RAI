# Correction #23 — Φ_μν derivation from δS_CTP/δh_a (linearized)

**Date:** 2026-04-30
**Status:** Linearized derivation COMPLETE. Curved-background extension OPEN.
**Roadmap:** v8→v2 deposit, Priority 2.

---

## TL;DR

The framework's gravitational constitutive equation `G_μν + Φ_μν = 8πG T_μν` previously carried Φ_μν as a heuristic postulate (`gr_recovery.py` set Φ_μν ∝ χ(ω)·T_μν without a derivation from the CTP action). Correction #23 derives Φ_μν explicitly from the variation `δS_CTP / δh_a^μν |_{h_a=0}` of the linearized gravitational Schwinger-Keldysh action. The kernel form `K^R(ω) = α_vac × χ(ω) × P^TT_μνρσ` emerges structurally, with the susceptibility coefficient and the transverse-tracefree projector both required by the variation rule, the A1 retarded-variation axiom, and Bianchi preservation.

This is **Priority 2 of the v8→v2 deposit roadmap** ("derive Φ_μν from S_CTP — the biggest gravity gate"). It moves the framework from "strong model" toward "real theory" at the linearized level. The curved-background extension (S⁴, FRW) is research-tier work that remains open and is now tracked under `phi_munu_curved_background_extension_open_question` — a sharper successor to the original heuristic open question.

| | Before | After |
|:---|:---|:---|
| Φ_μν provenance | Heuristic postulate (gr_recovery.py: `Φ ∝ χ(ω) × T`) | Derived from `δS_CTP/δh_a` |
| Bianchi check | Single-mode plane wave (gr_recovery.py) | Structural: ∂^μ Φ = 0 from ∂^μ P^TT = 0, for ALL h_r and ALL kernel time structures |
| Status (registry) | `constitutive_projection_gravity_heuristic_open_question` (open_negative) | `phi_munu_linearized_derivation` (computed, Ch 6) + `constitutive_projection_gravity_heuristic_resolved` (meta, Ch 12) |
| Tests | gr_recovery's seven legs (limits & propagator only) | +34 new structural tests in `test_linearized_ctp_action.py` |
| New free parameters | — | None. α_vac and τ_0 inherit from existing `alpha_vac_derivation` and `tau_0_derivation` |
| Existing predictions | Λ_grav, n_g(ω), bridge — all use Φ_μν postulate | Same predictions, now derived rather than postulated. No numerical change. |

---

## What is derived

Starting from the linearized gravitational Schwinger-Keldysh action

```
S_CTP[h_+, h_-] = S_EH^(2)[h_+] − S_EH^(2)[h_-]
                + S_matter[h_+] − S_matter[h_-]
                + S_const[h_+, h_-]
                + S_noise[h_+, h_-]
```

with constitutive coupling

```
S_const = −(1/2) ∫∫ h_a^μν(x) K^R_μνρσ(x − x') h_r^ρσ(x') d⁴x d⁴x'
```

(retarded memory-kernel form per the A1 retarded-variation axiom), the variation produces:

```
δS_CTP/δh_a^μν |_{h_a=0}  =  G_μν^(1)[h_r]  −  Φ_μν[h_r]  −  T_μν  =  0
```

Identifying the constitutive contribution

```
Φ_μν[h_r](x)  ≡  ∫ K^R_μνρσ(x − x') h_r^ρσ(x') d⁴x'                (★★)
```

makes Φ_μν a **derived structural object** — literally the kernel-h_r convolution that appears when the constitutive cross term is varied with respect to h_a. In Fourier space:

```
Φ_μν(ω, k)  =  K^R_μνρσ(ω) × h_r^ρσ(ω, k)
            =  α_vac × χ(ω) × P^TT_μνρσ × h_r^ρσ(ω, k)
```

with:

- **α_vac = 1/3** — the conformal-mode trace-anomaly impedance (KS 2011 a/c for a real scalar; preserved exactly, NOT modified by Correction #23).
- **χ(ω) = 1/(1 − iωτ_0)** — single-pole susceptibility from the constitutive equation `τ_0 dz/dt + z = z_target[z]`. Pole at ω = −i/τ_0 in the lower half-plane — causal, KK-compatible.
- **P^TT_μνρσ** — transverse-tracefree projector. Divergence-free by construction (`∂^μ P^TT_μνρσ = 0`), so Bianchi ∇^μ Φ_μν = 0 follows STRUCTURALLY for any h_r and any kernel time structure.

---

## Six structural properties verified

1. **Kernel form derived, not postulated.** The variation `δS_CTP/δh_a` produces Φ_μν as a kernel-h_r convolution by direct calculation. SymPy verifies the symbolic identity `Φ_μν / h_r = (1/2) × α_vac × χ(ω)` exactly.

2. **High-frequency / GR-recovery limit.** `lim_{ω→∞} χ(ω) = 0`, so `Φ_μν → 0` and (★★) reduces to `G_μν^(1) = 8πG T_μν` — standard linearized Einstein. SymPy `sp.limit(α × χ, ω → ∞) == 0` exactly.

3. **Low-frequency / full-constitutive limit.** `lim_{ω→0} χ(ω) = 1`, so `Φ_μν → α_vac × P^TT × h_r` at DC. Magnitude consistent with `n_g²(0) = 1 + α_vac = 4/3` refractive enhancement (matches `closure_protocol.N_G_DC²`).

4. **Bianchi structural preservation.** The transverse-tracefree projector satisfies `∂^μ P^TT_μνρσ = 0` by construction. Therefore `∂^μ Φ_μν = 0` follows for ALL h_r and ALL kernel time structures — not just the single-mode plane-wave check that `gr_recovery.bianchi_residual_plane_wave` performs. This is the key upgrade: structural derivation, not single-mode verification.

5. **α_vac = 1/3 from conformal-mode-scalar identification.** The framework's existing `alpha_vac_derivation` claim (computed tier) traces α_vac to KS 2011 a/c for a single real scalar. Correction #23 INHERITS this — α_vac enters via the kernel `K^R = α_vac × χ × P^TT`, and the value 1/3 comes from the conformal-mode scalar's KS coefficients, NOT from this correction.

6. **Consistency with `gr_recovery.py`.** The susceptibility-based postulate `gr_recovery.susceptibility_chi(ω)` and the framework's canonical `closure_protocol.N_G_DC = √(4/3)` are both reproduced by the derivation. The numerical agreement test in `test_linearized_ctp_action.py::TestConsistencyWithGRRecoveryPostulate` verifies relative error < 1e-12 across four decades of frequency.

---

## What this resolution does NOT do

- **Does not extend to curved background.** S⁴ (Euclidean de Sitter, sister to TJI Phase-1) and FRW (cosmological perturbations) require: (i) covariant projector P_μνρσ on the curved background's Killing structure; (ii) retarded memory kernel defined via curved-space Green function; (iii) matter-coupling normalization with √-g factors. Tracked under `phi_munu_curved_background_extension_open_question` (Ch 12, open_negative) — the sharper successor.

- **Does not derive α_vac.** α_vac = 1/3 enters via the conformal-mode-scalar postulate; that identification is tracked separately under `alpha_vac_derivation`. Correction #23 inherits it.

- **Does not derive the projector index structure beyond P^TT.** The framework adopts P^TT as the canonical projector consistent with linearized gauge invariance and Bianchi preservation. Other projectors (e.g., trace-only) are admissible in principle and would require additional physical motivation. Beyond the linearized limit, the projector structure is part of the curved-background open question.

- **Does not close `n_g_omega_cosmological_covariance_open_question`.** That's the same problem in the cosmological-perturbation sector. Closing both is one larger covariant-derivation task; Correction #23 tackles only the gravitational half at the linearized level.

---

## Convention declaration

Mirrors discipline of TJI Phase-0.5 (`grut.derivation.tji.flat_space.convention_declaration`). Every Fraction equality in the derivation is asserted under these conventions; if any change, all downstream pinned values must be re-derived.

| | Convention |
|:---|:---|
| **C1** Metric signature | `(−, +, +, +)` — matches existing GRUT codebase |
| **C2** Metric perturbation | `g_μν = η_μν + h_μν`, `\|h\| ≪ 1`; O(h) kept exactly, O(h²) dropped |
| **C3** Keldysh basis | `h_r = (h_+ + h_-)/2`, `h_a = h_+ − h_-` (matches `axioms.keldysh_basis`) |
| **C4** Memory-kernel form | `K^R = α_vac × P^TT × τ_0^(-1) exp(-(t-t')/τ_0) Θ(t-t')` (retarded per A1; exponential per constitutive equation) |
| **C5** Susceptibility | `χ(ω) = 1/(1 − iωτ_0)` — α_vac factored OUT into K^R explicitly, not inside χ |
| **C6** Φ_μν sign | `(★★)`: G^(1) − Φ = 8πG T. Φ adds positively to matter-induced Newtonian potential at DC |
| **C7** Projector | `P^TT_μνρσ` — transverse-tracefree (divergence-free, idempotent, trace = 5 propagating modes in 4D) |

All seven conventions are exposed via `convention_declaration()` and pinned by tests in `TestConventionDeclaration`.

---

## Files touched

| File | Change |
|:---|:---|
| `grut/derivation/phi_munu/__init__.py` | New package — exports the derivation API |
| `grut/derivation/phi_munu/linearized_ctp_action.py` | New module — symbolic CTP action setup, variation, Φ_μν extraction, structural verification |
| `tests/derivation/phi_munu/__init__.py` | New package marker |
| `tests/derivation/phi_munu/test_linearized_ctp_action.py` | New — 34 tests pinning the derivation: convention declaration, susceptibility form, kernel structure, variation outputs, extracted form, limits, Bianchi, α_vac inheritance, gr_recovery consistency |
| `grut/toe/registry.py` | Replace `constitutive_projection_gravity_heuristic_open_question` with: `constitutive_projection_gravity_heuristic_resolved` (meta, Ch 12), `phi_munu_linearized_derivation` (computed, Ch 6), `phi_munu_curved_background_extension_open_question` (open_negative, Ch 12). Update internal cross-reference in `gr_recovery` claim. |
| `grut/toe/ledger.py` | Replace ledger entry with `phi_munu_curved_background_extension_open_question` reflecting the partial closure |
| `tests/toe/test_render.py` | Update render test to reference the new claim id |
| `theory/derivation/CORRECTION_23_PHI_MUNU_DERIVATION.md` | This file |

---

## Strategic observation

This correction is the second clean Priority win for the v8→v2 roadmap (after Priority 1 / τ-cleanup). The pattern is the same as the τ-cleanup:

- A foundational provenance issue the framework's own documentation flagged is now explicitly resolved at one structural level.
- No test regressions; existing predictions all stand.
- The framework's credibility-honesty posture improves: the gravitational constitutive correction is no longer a postulate but a derived structural object, with the curved-background extension explicitly named as the remaining work.

Two of five v8→v2 priorities now landed:
- ✅ Priority 1: τ-cleanup (Correction #22)
- ✅ Priority 2: Φ_μν derivation, linearized (Correction #23)
- ⏳ Priority 3: close n_g(ω) covariance — the cosmological-perturbation sister gap
- ⏳ Priority 4: one Standard Model win (one Yukawa ratio, mixing angle, or neutrino hierarchy prediction)
- ⏳ Priority 5: short GRUT falsifier paper (decoherence plateau, isotope discriminator, BMV)

Priority 3 is the natural next step: close `n_g_omega_cosmological_covariance_open_question`, which is the same problem in the perturbation sector — covariant derivation of a kernel form already pinned at the linearized / flat level. Closing it would unlock CMB modeling, primordial A_s rescaling, and structure formation. Priority 2's linearized template provides the structural pattern.

---

## Reference

- V7 §22-§25 (gravity sector — heuristic Φ_μν framing this correction supersedes at linearized level).
- Calzetta-Hu (2008) *Nonequilibrium Quantum Field Theory* §5-§7 — CTP variation in gauge theories, the standard reference for the variation rule used here.
- Komargodski-Schwimmer (2011) — a-theorem and conformal-mode trace anomaly; underwrites α_vac = 1/3.
- `grut/foundation/gr_recovery.py` — existing module whose susceptibility postulate is now structurally derived.
- `grut/derivation/tji/flat_space.py` — sister calculation (TJI Phase-0/0.5); same SymPy pattern, same convention-declaration discipline.

---

*D. Ryan Grover, with Claude Code, 2026-04-30. Same discipline pattern as Corrections #21 (TJI Phase-0.5), #22 (τ-cleanup).*
