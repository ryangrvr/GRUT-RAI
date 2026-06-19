# GRUT v3 — Test 06: the dark-sector profile failure is a THEOREM, not an artifact

**Date:** June 2026 · branch `main_v3` · constructive phase · workflow `wo7mvnscu` (read-only)
**Question (the single load-bearing assumption of the K⁽²⁾ verdict):** the resolution of the
flagship (`GRUT_V3_K2_DERIVATION.md`) found C5a "right magnitude, wrong shape" — but the *shape*
rested on the heuristic identification `ρ_eff ∝ W²` (the scalar). **Is the `1/r⁴` profile failure an
unavoidable theorem of the full second-order kernel, or a consequence of that identification?**

---

## Method

Derive the effective gravitating source — the `00`-component of the second-order response tensor
`Φ⁽²⁾_μν = δ²S_IF/δh_a δh_r²|_{O(2)}` — from its actual tensor structure rather than the scalar `W²`,
via three independent physics handles (sympy, weak-field static halo):

- **Route A — scalar `W²`:** `Φ⁽²⁾_00 ∝ W² = C_μνρσC^μνρσ` (the current heuristic).
- **Route B — Bach tensor:** the metric variation of a `∫√g W²` action term is
  `B_μν = (2∇^ρ∇^σ + R^ρσ)C_μρνσ` — *linear* in curvature, 4 derivatives. Its `00` component sources
  like `∇⁴Φ = ∇²ρ_baryon`.
- **Route C — the `P^TT` loophole:** the transverse projector hides `k_ik_j/k²`, formally an inverse
  Laplacian. Does it survive into the effective `00` density and shallow the profile toward `1/r²`
  (reviving C5a), or is it bounded/angular?

---

## Result — all three routes converge: `ρ_eff ∝ 1/r⁴` (or steeper)

For an isothermal baryon halo (`ρ ∝ 1/r²`, the most favorable case for an extended signal):

| Route | Effective `00` source | Radial scaling | Helps? |
|---|---|---|---|
| **A** scalar `W²` | `(16/3)Λ²`, `Λ=4π(ρ−⟨ρ⟩)∝1/r²` | `ρ_eff ∝ 1/r⁴` (slope −4) | no |
| **B** Bach `∇²ρ` | `∇²ρ_baryon = 2/r⁴` | `ρ_eff ∝ 1/r⁴` (same; ≥ for point mass) | no |
| **C** `P^TT` projector | `k̂k̂` is degree-0 in `\|k\|` | `ρ_eff ∝ 1/r⁴` (unchanged) | no |

Flat rotation curves require `ρ_DM ∝ 1/r²` (slope −2). Every route is **at least two powers too
steep**; the implied `v_eff(r)` *declines*. `differs_from_W2_scalar = False` for all three.

**Profile-independence (checked, with a correction).** `ρ_eff ∝ W² ∝ (ρ−⟨ρ⟩)²`. In the *interior*
of a power-law halo this is `∝1/r⁴`; in the *outskirts* (where baryons fall off) it follows the
**exterior tidal Weyl** `(M_enc/r³)² ∝ 1/r⁶`. So `ρ_eff` is `1/r⁴`-to-`1/r⁶` *everywhere* — always
steeper than the `1/r²`–`1/r³` a halo needs, for *any* baryon profile (verified on isothermal,
Hernquist, exponential). Note this corrects a tempting shorthand: `ρ_eff` does **not** simply "track
`ρ_baryon²`" and vanish where baryons do — in a truncated disk's outskirts the `1/r⁶` tidal term
*outpaces* the (exponentially vanishing) baryons, so `ρ_eff/ρ_baryon` can even *rise* outward. That
makes the shape *more* wrong, not less: it is centrally peaked **and** has a too-steep tidal tail,
never an extended flat-curve halo.

### The `P^TT` loophole is closed (the decisive point)

The `k_ik_j/k²` in `P^TT` is a **dimensionless angular/index projector** (`δ_ij − k̂_ik̂_j`, degree 0
in `|k|`) — it selects transverse components, it does **not** functionally invert `∇²`. Because
Stage B proved `K⁽²⁾(ω,k) = σ·α·χ(ω)` is **k-independent** (`χ` purely temporal), there is no
`k`-factor to "activate" the projector's `1/k²` into a genuine pole at `k=0`. A spatially-local
causal kernel is an *entire* (polynomial) function of `k²`; the `W²` source contributes `k⁴`
(polynomial); their product is polynomial — never `1/k²`. **No inverse Laplacian survives.**

### Why this is a *theorem*

Shallowing a local source (baryons, or `1/r⁴`) into an extended `1/r²` halo *requires integrating*
it — applying `1/∇²`. The same locality result that forces `L=L₀` (no genuine `1/k²` pole) **forbids
that integration**. So no choice of tensor structure within the permitted, local, causal kernel can
flatten the profile. 3/3 skeptics — including one tasked solely with *reviving* C5a — classified the
failure as `theorem_from_locality`; none found a surviving shallowing mechanism.

---

## Verdict

> **The `ρ_eff ∝ 1/r⁴` profile failure is a THEOREM of the full second-order kernel, tied to the same
> locality result that fixes `L=L₀` — not an artifact of the `ρ_eff ∝ W²` identification.** C5a is the
> wrong shape for a dark-matter halo across *all* permitted tensor structures (scalar `W²`, Bach,
> TT-projected). GRUT has no derived dark-matter mechanism reproducing halo phenomenology; dark matter
> remains a hosted input (derived `a₀`, `μ_linear=1`).

This **narrows, and then closes, the frontier** the resolution had left open. The dark-sector question
is no longer "can the `W²` response be dressed to change its radial scaling?" — within the locality +
No-Go structure, it provably cannot. The two genuinely open frontiers (α-selection / 4th-order
Riegert; the `L₀→0` redundancy proof) are unaffected and were never dark-sector.

**Honest residual (cannot change the verdict):** the exact `O(1)` prefactor `σ` and the full
*covariant* tensor form of `K⁽²⁾` need a dedicated CAS (xAct); `σ` scales magnitude only, never the
shape. The routes here are weak-field/flat-space (tractable by hand); a curved-FRW covariant
computation would harden — not overturn — the scaling, since the locality block is background-independent.
