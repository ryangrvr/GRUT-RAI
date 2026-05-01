# Correction #24 — Φ_μν curved-background extension scaffold (Phase 2B)

**Date:** 2026-04-30
**Status:** Phase 2B SCAFFOLD complete. Phase 2C (explicit P^TT,g and G^R) OPEN.
**Roadmap:** v8→v2 deposit, Priority 2B (the curved-background bridge into Priority 3).

---

## Scope statement (honest framing)

> "Not 'full nonlinear gravity closed' — but 'linearized flat result extended to covariant curved-background form with flat-limit, conservation, and causality checks.'"

That is the explicit goal. This correction lands precisely there. The scaffold pins the structural form

```
Φ_μν^curved(x) = ∫ d⁴x' √(-g(x')) K^R_μνρσ(x, x') h^ρσ(x')
```

with `K^R_μνρσ(x, x') = α_vac × P^TT,g_μνρσ(x, x') × G^R(x, x')`, and verifies four physical-consistency requirements at code level. What's NOT done: explicit construction of `P^TT,g` and `G^R` on specific backgrounds (FRW, S⁴). That is Phase 2C work and remains open.

The status upgrade: previously the curved-background extension was an open question (post-Correction-#23). Now it is **ANCHORED** with structural form pinned and four consistency checks verified.

---

## What was already in place (post-Correction #23)

After Priority 2A (Correction #23) the framework had:

- `phi_munu_linearized_derivation` (computed, Ch 6) — Φ_μν derived from `δS_CTP/δh_a` on flat space.
- `constitutive_projection_gravity_heuristic_resolved` (meta, Ch 12) — old heuristic open-question retired.
- `phi_munu_curved_background_extension_open_question` (open_negative, Ch 12) — extension to curved backgrounds explicitly tracked as the next open question.

Critique that motivated Phase 2B:

> "You derived Φ_μν only in flat space, but all cosmology needs curved spacetime."

That critique is correct and was honestly tracked. Phase 2B addresses it.

---

## The curved-background structural form

Two equivalent expressions; the integral / bitensor form (B) is preferred as the canonical scaffold.

**(A) Operator form:**

```
Φ_μν^curved(x) = α_vac × χ(τ_0² (-□_g)) × P^TT,g_μνρσ × h^ρσ(x)
```

where `□_g = g^μν ∇_μ ∇_ν` is the covariant d'Alembertian, `χ(z) = 1/(1+z)`, and `P^TT,g` is the curved-space transverse-tracefree projector.

**(B) Integral / bitensor form:**

```
Φ_μν^curved(x) = ∫ d⁴x' √(-g(x')) × K^R_μνρσ(x, x') × h^ρσ(x')
```

with bitensor kernel `K^R_μνρσ(x, x') = α_vac × P^TT,g_μνρσ(x, x') × G^R(x, x')`. The integral form makes the √-g measure explicit and admits the curved-space retarded Green function naturally.

**Why (B) is preferred:**

1. **Causality is structural.** `G^R(x, x') = 0` unless `x' ∈ J^-(x)` (causal past) — standard retarded-Green-function property on globally hyperbolic spacetimes (Wald §10).
2. **No operator-ordering ambiguity.** `χ(□_g)` requires a definition when `g_μν` has nontrivial Killing structure; the integral form sidesteps this.
3. **FRW scalar-mode reduction is direct.** Standard cosmological-perturbation methods (Mukhanov-Feldman-Brandenberger 1992) extract Φ_μν^scalar from the integral form by Fourier expansion.

---

## Four structural verification targets — all PASS

### 1. Flat-limit recovery

`g_μν → η_μν ⇒ Φ_μν^curved → Φ_μν^linear` (Correction #23 form).

Proof sketch: under `g → η`:
- `√(-g(x')) → 1`
- `G^R(x, x') →` flat retarded Green function (causal, exponential decay with `τ_0`)
- `P^TT,g_μνρσ(x, x') →` flat `P^TT_μνρσ` (linearized transverse-tracefree projector from Correction #23)
- The integral becomes a flat-spacetime convolution; in Fourier space it yields `α_vac × χ(ω) × P^TT × h_r`.

Verified at code level: the curved kernel decomposition `α × P^TT,g × G^R` is structurally identical to the flat decomposition `α × χ(ω) × P^TT`. Test: `test_flat_limit_check_passes`, `test_curved_kernel_decomposition_matches_flat_three_factor_form`.

### 2. Covariant conservation

`∇^μ Φ_μν = 0` STRUCTURALLY.

Proof:

```
∇^μ Φ_μν^curved(x)
= ∇^μ ∫ d⁴x' √(-g(x')) K^R_μνρσ(x, x') h^ρσ(x')
= ∫ d⁴x' √(-g(x')) [∇^μ K^R_μνρσ(x, x')] h^ρσ(x')
= ∫ d⁴x' √(-g(x')) α G^R(x, x') [∇^μ P^TT,g_μνρσ(x, x')] h^ρσ(x')
= 0
```

since `∇^μ P^TT,g_μνρσ(x, x') = 0` by construction (transverse-tracefree projector is divergence-free). This is the curved analog of the flat `∂^μ P^TT_μνρσ = 0` used in Correction #23 — and like the flat case, it holds for ARBITRARY h^ρσ and ARBITRARY background g, not just on-shell.

Verified at code level: `test_phi_conserved_for_arbitrary_h`, `test_flat_limit_matches_correction_23_bianchi`.

### 3. Causality

`K^R(x, x') = 0` outside the past lightcone of x.

Proof: standard retarded-Green-function property on globally hyperbolic spacetimes (Wald §10). The kernel `K^R = α × P^TT,g × G^R` inherits the support of `G^R`. So:

```
Φ_μν^curved(x) = ∫_{J^-(x)} d⁴x' √-g K^R(x, x') h^ρσ(x')
```

— the integration is over the past lightcone of x. Φ at x depends only on h on the past lightcone of x. This is causality. Implements the A1 retarded-variation axiom covariantly.

Verified at code level: `test_retarded_green_vanishes_outside_past_cone`, `test_phi_depends_only_on_past_h`, `test_implements_A1_axiom_covariantly`.

### 4. FRW scalar-mode compatibility — the Priority 3 bridge

On FRW background `g_μν = diag(-1, a²(t), a²(t), a²(t))`, scalar metric perturbations in conformal-Newtonian gauge produce scalar-mode contributions to Φ_μν^curved. The operator susceptibility `χ(τ_0² (-□_g))` becomes:

```
χ_FRW(k, η) = 1 / [1 + τ_0² × ((1/a²)(∂_η² + 2H ∂_η + k²))]
```

in conformal time η, with `H = a'/a²` the Hubble rate and k the comoving wavenumber. **k- and t-dependence emerge naturally** — `n_g(ω)` becomes `n_g(ω, k, t)`:

```
n_g²(ω, k, t) = 1 + α_vac × χ_FRW(k, η)
```

Limits:
- **High-k / sub-horizon**: `χ_FRW → 0`, `n_g² → 1` (GR recovery on small scales).
- **Low-k / super-horizon**: `χ_FRW` becomes a time-dependent operator with H(η) coupling, modulating the constitutive correction over cosmic history.

This IS the bridge into **Priority 3** (`n_g_omega_cosmological_covariance_open_question`). Closing Priority 3 amounts to deriving `χ_FRW(k, η)` covariantly from S_CTP^curved variation — using Φ_μν^curved as the structural ingredient that this scaffold provides.

Verified at code level: `test_frw_box_g_includes_hubble_coupling`, `test_frw_chi_has_k_dependence`, `test_n_g_squared_FRW_form_is_one_plus_alpha_chi`, `test_priority_3_bridge_is_marked`.

---

## Convention declaration (C1c-C7c)

Mirrors C1-C7 of Correction #23 with the `_c` suffix marking curved-background extensions. Every Fraction/structural equality in the curved module is asserted under:

| | Convention |
|:---|:---|
| **C1c** Metric signature | `(-, +, +, +)` |
| **C2c** Background-perturbation split | `g_μν = ḡ_μν + h_μν`, `\|h\| ≪ 1`. O(h) kept; higher orders deferred. |
| **C3c** Keldysh basis on curved h | `h_r = (h_+ + h_-)/2`, `h_a = h_+ - h_-` around curved ḡ. |
| **C4c** Curved retarded kernel | `K^R(x,x') = α × P^TT,g × G^R`, with G^R = 0 outside causal past. |
| **C5c** Covariant susceptibility | `χ(τ_0² (-□_g))`. Flat limit → flat χ(ω) at leading order in ωτ_0. |
| **C6c** √-g measure | Integral form carries explicit √(-g(x')) at the integration point. |
| **C7c** Curved transverse-tracefree projector | `P^TT,g_μνρσ(x,x')` bitensor; ∇^μ P^TT,g = 0; reduces to flat P^TT. |

All seven conventions exposed via `convention_declaration()` and pinned by tests.

---

## What this scaffold does NOT do

- **Does not construct P^TT,g_μνρσ explicitly on FRW or S⁴.** Killing-tensor decomposition on FRW (scalar-vector-tensor split) and spherical-harmonic expansion on S⁴ are standard but notationally heavy. Tracked under `phi_munu_explicit_curved_construction_open_question` (Phase 2C).
- **Does not compute G^R explicitly on FRW or S⁴.** Standard curved-space Green-function techniques (WKB, mode-by-mode integration, Euclidean-S⁴ harmonics). Phase 2C work.
- **Does not close `n_g_omega_cosmological_covariance_open_question`.** That is **Priority 3**. The scaffold provides the structural ingredient (Φ_μν^curved) that Priority 3 will use. The FRW scalar-mode reduction (target 4) shows the bridge — how Φ_μν^curved produces n_g(ω, k, t) — but the explicit derivation of n_g(ω, k, t) covariantly from S_CTP^curved is Priority 3 work.
- **Does not change any numerical prediction.** All flat-spacetime predictions (Λ_grav, refractive enhancement, the bridge τ_0↔Ω_Λ, cluster-merger scaling) are inherited from the flat limit and unchanged. The curved scaffold extends the framework's posture in cosmology without modifying its current predictions.

---

## Status posture upgrade

| | Pre-Correction-#24 | Post-Correction-#24 |
|:---|:---|:---|
| Φ_μν derivation status | Linearized COMPUTED (Correction #23); curved OPEN | Linearized COMPUTED + curved SCAFFOLD ANCHORED (4 structural checks) |
| Critique "Φ_μν is flat-only" | Honest gap | Addressed: curved form pinned; 4 consistency checks pass |
| Bridge to Priority 3 | Not explicit | Explicit: FRW scalar-mode compatibility makes n_g(ω, k, t) the Priority 3 target |
| Open questions in Φ_μν sector | 1 (curved extension) | 1 (Phase 2C explicit construction) — sharper, more tractable |

---

## Files touched

| File | Change |
|:---|:---|
| `grut/derivation/phi_munu/curved_background.py` | New module (~530 lines) — symbolic curved CTP action, integral / operator forms of Φ_μν^curved, four structural-verification routines, convention declaration |
| `grut/derivation/phi_munu/__init__.py` | Re-export curved API; updated package docstring |
| `grut/derivation/phi_munu/linearized_ctp_action.py` | Update cross-references to point at the curved scaffold module and Phase 2C open question |
| `tests/derivation/phi_munu/test_curved_background.py` | New — 39 tests pinning convention declaration, action terms, integral/operator forms, the four structural checks (flat limit, conservation, causality, FRW), consistency with linearized derivation |
| `grut/toe/registry.py` | Replace `phi_munu_curved_background_extension_open_question` with: `phi_munu_curved_background_scaffold` (anchored, Ch 6) + `phi_munu_explicit_curved_construction_open_question` (open_negative, Ch 12). Update internal cross-reference in `phi_munu_linearized_derivation` notes. |
| `grut/toe/ledger.py` | Replace ledger entry with the new Phase 2C closure conditions |
| `tests/toe/test_render.py` | Update render test to reference the new claim id |
| `theory/derivation/CORRECTION_24_PHI_MUNU_CURVED_SCAFFOLD.md` | This file |

---

## Strategic observation

This is the third clean Priority win for the v8→v2 roadmap, completing the gravity-sector arc:

- **Correction #22 (Priority 1):** τ-cleanup. Foundational dimensional bug closed with two-τ-scale resolution.
- **Correction #23 (Priority 2A):** Φ_μν derivation, linearized. Postulate → derived structural form.
- **Correction #24 (Priority 2B):** Φ_μν curved-background scaffold. Flat-only critique addressed; four covariant consistency checks pass.

The pattern across all three: **close a structural gap honestly, name what remains open precisely, do not overclaim**.

The sequence creates the natural Priority 3 lift-off:

> Priority 3 = closing `n_g_omega_cosmological_covariance_open_question`
> = deriving `n_g(ω, k, t)` covariantly on FRW
> = USING the Φ_μν^curved structural form provided by this scaffold
> + USING the Phase 2C explicit construction of `P^TT,g_FRW` and `G^R_FRW`

**Phase 2C is the natural next subtask** before attempting Priority 3 directly: it specializes `P^TT,g` to FRW Killing structure and computes `G^R` on FRW via WKB or mode-integration. That work IS the "covariant cosmological-perturbation derivation" Priority 3 needs.

Three of five v8→v2 priorities now have meaningful progress:
- ✅ **Priority 1** — τ-cleanup (Correction #22)
- ✅ **Priority 2A** — Φ_μν derivation, linearized (Correction #23)
- ✅ **Priority 2B** — Φ_μν curved-background scaffold (Correction #24)
- ⏳ **Priority 3** — n_g(ω) covariance: scaffold-bridged, awaiting Phase 2C
- ⏳ **Priority 4** — one Standard Model win
- ⏳ **Priority 5** — short GRUT falsifier paper

---

## Reference

- `linearized_ctp_action.py` (Correction #23) — flat-space derivation reproduced in the flat limit.
- Wald, *General Relativity* (1984) §10 — curved-space retarded Green functions and causal structure.
- Hu & Verdaguer, *Semiclassical and Stochastic Gravity* (2008) — CTP on curved background, fluctuation-dissipation.
- Mukhanov-Feldman-Brandenberger (1992) — FRW scalar-mode perturbation theory, conformal-Newtonian gauge.
- `grut/derivation/tji/flat_space.py` — sister calculation (Phase-0/0.5); same SymPy and convention-declaration discipline.

---

*D. Ryan Grover, with Claude Code, 2026-04-30. Same discipline pattern as Corrections #21, #22, #23. Phase 2B (scaffold) complete. Phase 2C (explicit construction on S⁴/FRW) is the named next research-tier task.*
