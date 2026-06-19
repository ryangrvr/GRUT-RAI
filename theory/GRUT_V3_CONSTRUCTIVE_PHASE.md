# GRUT v3 — The Constructive Phase: the K⁽²⁾ Flagship Problem

**Date:** June 2026 (2026-06-17) · branch `main_v3` · audit frozen at tag `v3-audit-complete`
**Purpose:** mark the end of the v3 audit phase and define the constructive phase by a single
flagship problem — with a moratorium that protects the compression the audit achieved.

---

## The audit phase is COMPLETE (Tests 01–05) — frozen

The v3 dark-sector audit ran five tests and ends at **Test 05** (its endpoint). It compressed the
dark sector from a sprawl of claimed mechanisms to a single open computation:

```
4 candidate mechanisms  →  1 surviving channel (C5a, W²)
                            1 surviving scale   (a₀)
                            1 decisive computation (K⁽²⁾)
```

| Test | Channel | Verdict |
|---|---|---|
| 01 | dielectric Ω_dm / linear enhancement | refuted |
| 02 | C5b orbital-gate frequency | assumed |
| 03 | C5b orbital-gate magnitude | refuted (~1/√N) |
| 04 | C5a (W²) existence | undetermined — sign ✓, scaling ✓, magnitude open |
| 05 | C5a K⁽²⁾ entry | undetermined_needs_symbolic — reduced to ONE calculation |

This state is frozen. (Records: `GRUT_V3_TEST_0[1-5]_*.md`, `GRUT_V3_AUDIT_CHECKPOINT.md`.)

---

## The flagship problem of the constructive phase

> **Compute the explicit second-order CTP kernel**
> `K⁽²⁾_μνρσ(ω,k) = δ²S_IF / δh_a δh_r² |_{O(2)}`
> **on an FRW background with a superposed bound-system (halo/cluster) perturbation, and evaluate the
> resulting effective source `ρ_eff = σ·α·L²·W²`.**

This single symbolic calculation determines whether GRUT possesses a *derived* dark-matter mechanism.
It yields the two quantities the audit could not fix:

1. **The coupling length scale `L`** — the ~10²⁷× swing. `L = L₀ = cτ₀` (memory) ⇒ negligible ⇒ C5a
   dies; `L = local r` ⇒ galaxy-marginal (with a cluster-overshoot tension).
2. **The dimensionless prefactor `σ`** — estimated `~O(1)` (`c·α` / `α`), unverified.

**Steps (sequential):** (i) symbolic 2nd-order variation → `K⁽²⁾` in closed form (new module
`grut/derivation/phi_munu/second_order_kernel.py`); (ii) locality smoking-gun — does `K⁽²⁾` carry
`∇²`/`(τ₀k)²` (→ `L₀`, dead) or stay ω-local (→ local `r`)?, resolving the `W²~(∂²h)²` derivative
subtlety the structural lean ignored; (iii) extract `σ` via the `C²`/anomaly contraction;
(iv) phenomenology on galaxy + cluster `W²` profiles, confirming `W²≈0` on FRW keeps `μ_linear=1`.

**Soft prior (not a result):** `K^R`'s spatial locality leans toward `L = local r` (⇒ galaxy-marginal,
the best signal GRUT has produced) — but this is structural inference, weakened by `W²`'s own
derivative structure, and carries a ~100× cluster overshoot. Only the explicit computation decides.

**Decisive outcomes:** `L₀`/small-σ ⇒ **C5a dead, GRUT has no derived DM mechanism (DM hosted)**;
local-`r`/`O(1)`-σ ⇒ **galaxy-marginal** (warrants 04D phenomenology, with the cluster tension);
unphysical algebra ⇒ ruled out internally. All three are decisive.

---

## RESOLVED (June 2026) — the flagship is closed

The K⁽²⁾ derivation ran as four stages (full record: `GRUT_V3_K2_DERIVATION.md`; module
`grut/derivation/phi_munu/second_order_kernel.py`):

- **Stage A** — operator basis closed: **W² is the unique dynamically-active O(2) operator**
  (E₄ topologically dormant; Ricci-built terms forbidden).
- **Stage B** — **scale `L=L₀` is forced**: `K⁽²⁾(ω,k)=σ·α·χ(ω)` has no `1/k²` pole (a spatially-local
  causal memory kernel is polynomial in `k²`; the local-`r` branch would need a `1/∇²` it cannot make).
- **Stage C** — **magnitude is viable, not negligible**: `ρ_eff/ρ_baryon ~ O(1–100)` at galaxy scales.
  (The intermediate "`1e-27` ⇒ dies" was a unit-mixing + wrong-Weyl-formula error, corrected — `L₀`
  is comparable to the *curvature radius* `r/√Φ` of a weak-field galaxy, not its size.)
- **Stage D** — **shape is wrong (decisive)**: `ρ_eff ∝ W² ∝ ρ_baryon² ∝ 1/r⁴` (slope ≈ −3.9), far
  steeper than the `1/r²` flat rotation curves require; `σ` scales magnitude only, never the shape.

> **VERDICT:** C5a has roughly the right magnitude but the **wrong radial profile** to be the
> dark-matter halo. **GRUT has no derived dark-matter mechanism reproducing halo phenomenology;
> dark matter remains a hosted input** (with the derived `a₀` scale and `μ_linear=1`). Registry:
> `c5a_weyl_squared_dark_sector` → `open_negative` (+ ledger entry). Math survives, ontology changes.

The moratorium **succeeded**: the dark sector was held to one computation, that computation is done,
and its honest negative is *not* a cue to invent a fifth mechanism.

## The moratorium (standing discipline of the constructive phase)

> **No new dark-sector mechanisms are to be proposed until `K⁽²⁾` is computed.**

Rationale: the audit's entire achievement was **compression** — taking the dark sector from a sprawl
of co-existing mechanisms (V2's mechanism-accumulation failure mode) down to one channel and one
calculation. Inventing a new mechanism now — before `K⁽²⁾` is done — would *re-spread* the question,
squander the compression, and reproduce exactly the V2 pathology v3 was built to cure. The
constructive phase is defined by **solving one problem, not proposing more.** If C5a dies on the
`K⁽²⁾` computation, the honest conclusion is that GRUT's dark sector is a *hosted input* (with a
derived `a₀` scale) — not a cue to invent a fifth mechanism.

**GRUT's honest position until `K⁽²⁾` is computed:** a proven Q pillar, a postulated F pillar,
`μ_linear=1` (linear cosmology = ΛCDM, derived), a derived `a₀` scale, and one well-posed open
computation that decides the dark sector. Dark matter is otherwise a hosted input.
