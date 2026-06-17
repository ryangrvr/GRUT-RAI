# GRUT v3 — Test 05: The K⁽²⁾ Computation (constructive-phase entry)

**Date:** June 2026 (2026-06-17) · branch `main_v3`
**Status:** COMPLETE — **verdict `undetermined_needs_symbolic`**; adversarially verified, **read-only**
workflow (`w03abuxtf`). The first *constructive* test — it requires producing new mathematics, not
stress-testing an existing claim.
**Question:** what is the second-order CTP kernel `K⁽²⁾ = δ²S_IF/δh_a δh_r²|_{O(2)}` — its coupling
length scale and prefactor — which together decide whether the W² channel (C5a) yields a viable
dark sector?

---

## Result: the dark sector reduces to ONE symbolic computation

C5a's magnitude rests on exactly two uncomputed quantities, **both extracted from a single
calculation** (the explicit symbolic second-order variation):

1. **The coupling length scale `L`** in `ρ_eff ~ σ·α·L²·W²` — a ~10²⁷× swing:
   - `L = L₀ = cτ₀ ≈ 12.85 Mpc` → `ρ_eff ~ 10⁻²⁷` → **C5a dies** (no derived DM mechanism).
   - `L = local r` → galaxy **marginal** (`~few × ρ_DM`) but cluster **overshoot ~100×** (a tension).
2. **The dimensionless prefactor `σ`** — estimated `~O(1)` (naively `c·α = 3·⅓ = 1` or `α = ⅓`), but
   **not derived**.

## The structural lean (soft, not a derivation)

The first-order kernel `K^R = α·χ(ω)·P^TT` is spatially **local** (no `∇²`; memory in *time* only).
The agents argued K⁽²⁾ *inherits* that locality → `L = local r` → galaxy-marginal viability (the best
signal any GRUT dark-sector channel has produced). **But this is structural inference, not proven
algebra, and it has a real hole:** `W² = C_μνρσ C^μνρσ` is itself built from curvature (`~(∂²h)²`),
so the W²-coupling carries higher spatial-derivative structure that the naive "inherits K^R locality"
argument does not account for. Whether that promotes the scale toward `L₀` (or a mixed scale) can
only be settled by the explicit variation. So the lean toward viability is **encouraging but soft**.

## What stands at Test 05

| Gate | Status |
|---|---|
| 04A Sign | ✓ positive / DM-like (`c=3>0`) |
| 04B Scaling | ✓ `ρ_eff ~ α·L²·W²`; `W²=0` on FRW (no cosmological signal) |
| 04C/05 Magnitude | ⊗ **undetermined** — the scale (`L₀` vs `r`) and prefactor `σ` are uncomputed |

**Not refuted, not confirmed.** GRUT does **not** have a derived dark-matter mechanism today; it has a
**well-posed computational gate.**

## The exact remaining computation (the single calculation that closes the dark sector)

Compute `Φ⁽²⁾_μν = δ²S_IF/δh_a δh_r²|_{O(2)}` explicitly (symbolic, sympy/xAct on FRW + a bound-system
metric perturbation):
1. **2nd-order variation** → `K⁽²⁾_μνρσ(ω,k)` in closed form (new module `second_order_kernel.py`).
2. **Locality smoking-gun** → does `K⁽²⁾` carry `∇²`/`k²`/`(τ₀ k)²` (→ `L₀`, dead) or remain
   ω-local (→ local `r`)? — *resolving the W²-derivative subtlety above.*
3. **Prefactor `σ`** → contract `K⁽²⁾` with `C²` via the anomaly structure.
4. **Phenomenology** → evaluate `ρ_eff(r)` on galaxy + cluster `W²` profiles; verify `W²≈0` on FRW
   leaves `μ_linear=1` intact; quantify the galaxy–cluster tension.

## What it means

Three decisive outcomes, all settled by the computation:
- `L₀`-scale or tiny `σ` → **C5a dead → GRUT has NO derived dark-matter mechanism (DM hosted).**
- local `r` + `O(1) σ` → **galaxy-marginal** (GRUT's first gauntlet-passing DM candidate) with a
  documented **cluster overshoot** to resolve.
- unphysical structure emerging from the algebra → ruled out on internal grounds.

Test 05 **entered** the constructive phase and sharpened the dark sector to this one calculation; it
did **not** close it. The explicit symbolic second-order variation is the genuine next deep
computation — substantial, tooling-dependent (xAct/sympy), and decisive.
