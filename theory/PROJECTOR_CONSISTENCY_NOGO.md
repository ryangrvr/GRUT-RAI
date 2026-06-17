# Projector Consistency and the Conformal ⊥ Separate-Universe No-Go

**Date:** June 2026 (2026-06-15)
**Status:** Theoretical capstone of the low-ℓ CMB investigation. Settles the
constitutive-source question at the level of the action. Provides the
first-principles foundation under the v2.7 demotion (linear cosmology = ΛCDM).
**Companion:** `theory/CMB_ISW_EQUALITY_FILTER.md` (the empirical record),
Correction #38 (Ch 14 ledger).

---

## 0. The result in one statement

> **No-Go (conformal ⊥ separate-universe invariance).** A constitutive response
> that *is* the conformal refractive enhancement `n_g² = 1 + α` cannot also be
> invariant under the long-wavelength (separate-universe) transformation, on
> linear scalar perturbations. The two requirements coincide on the same mode in
> the `k → 0` limit and have opposite demands there. Therefore there is **no
> first-principles linear-scalar constitutive source** that is simultaneously
> (a) the GRUT refractive enhancement and (b) separate-universe invariant.

Consequence: the only consistent linear-scalar response is **`μ_linear = 1`**
(no modification). GRUT's dark sector is therefore **not** a linear-scalar
modified-gravity effect — it must live in the tensor, second-order/nonlinear, and
bound-system (orbital-frequency) sectors. **Linear cosmology = ΛCDM is a derived
requirement, not an empirical demotion.**

This closes the search begun in `CMB_ISW_EQUALITY_FILTER.md`: the low-ℓ excess was
not a bad parameter, not a missing `k_eq`, and not curable by a cleverer linear
source. It was the linear-scalar symptom of an internal inconsistency.

---

## 1. The question this closes

The validated MGCAMB run (Correction #38) showed GRUT's linear `μ → 4/3` (k→0)
over-produces the low-ℓ CMB ISW by ~2.6× (~29σ). Every rescue route was closed:
the QSA `k_eq` filter (not derivable; τ₀ memory reach ≈ L₀ ≈ 13 Mpc cannot encode
equality-era information), the derived FRW retarded kernel (2.79×, marginally
worse), a memory source, a quadratic Keldysh-noise vertex, and gravitational slip.

The residual conceptual clue: the pathology always lives at `k → 0`, where a
perturbation becomes locally indistinguishable from a rescaled background. The
question became whether a covariant, relational constitutive source — one that
responds to *realized structure* rather than absolute density — could be derived
from the action. This document answers that question.

---

## 2. The relational principle, made precise (and corrected)

### 2.1 Stewart–Walker (solid)
Under a gauge generator `ξ`, `δQ → δQ + £_ξ Q̄`. So `δQ` is gauge-invariant at
linear order iff `£_ξ Q̄ = 0`, guaranteed if `Q̄ = 0` on the background. The Weyl
tensor and the projected density gradient `D_aρ` vanish on FRW, so their linear
perturbations are gauge-invariant. This step is standard and survives.

### 2.2 The naive theorem is FALSE
The claim "gauge-invariant + linear + vanishes-on-FRW ⟹ high-pass" is **wrong**.
Counterexamples are the central objects of the field: the **Bardeen potentials
`Φ, Ψ`** and the **comoving curvature perturbation `ℛ`** are gauge-invariant,
linear, vanish on the background — and are **finite (nonzero) as `k → 0`** (`ℛ` is
constant on super-horizon scales). Background gauge invariance does **not** imply
high-pass.

### 2.3 The correct principle: separate-universe invariance
The right statement of the relational intuition is stronger:

> The source must vanish for **any locally-FRW geometry** — i.e. be invariant
> under the large gauge transformation (Weinberg adiabatic mode, `x → (1+λ)x`)
> that realizes a long-wavelength perturbation as a *local rescaling of the
> background*.

`ℛ` and `Φ` are exactly the modes that survive this transformation; they *are* the
background ambiguity. Quantities invariant under it depend on `ℛ` only through its
**gradients** (`∂ℛ ~ kℛ`) or through Weyl/tidal curvature — hence carry ≥ 1 power
of `k` and are **high-pass**. This implication is true:

> separate-universe invariance ⟹ high-pass (`→ 0` as `k → 0`).

### 2.4 High-pass is necessary, not sufficient (corner location)
The comoving density `Δ` is separate-universe invariant and high-pass, but its
corner sits at the **horizon** `k ~ aH`. The low-ℓ ISW modes are *sub-horizon at
their sourcing epoch* (`k = 10⁻³ Mpc⁻¹` enters the horizon at `z ≈ 58`), so for
them the suppression never engages. This is exactly why the earlier
"source-coupling" attempt died. A fix requires the corner at the constitutive
length `L₀`, not the horizon.

### 2.5 Locality selects `L₀`
`Δ` is **nonlocal** (it contains `v/k²`, an inverse-Laplacian of the velocity). A
local medium has no nonlocal reference frame; it can only couple to local
invariants, whose only scale is the medium's own correlation length `L₀`. So
*locality + separate-universe invariance* would point to a local invariant with
corner at `L₀`. Whether such a coupling is **admissible** is decided by the action
(§3) — and it is not.

---

## 3. What the constitutive action actually couples to

Source: `grut/derivation/phi_munu/linearized_ctp_action.py`. Three load-bearing
facts.

### Fact 1 — matter coupling is minimal `h_a T`, forced
The only matter term is `S_matter = ½ h_a^{μν} T_μν` (line 302). Matter couples to
the **metric**, through `T_μν`, by the equivalence principle. There is **no direct
vacuum–matter coupling.**

> **Consequence.** A coupling of the response to `L₀² D²ρ` (the "couple to the
> local separate-universe invariant" route) is **not admissible** — it is a
> non-minimal vacuum–matter coupling that bypasses the metric. **Forbidden.**

### Fact 2 — the vacuum couples to the metric `h_r` through `P^TT`, with no derivative structure
`S_const = −½ h_a K^R h_r`, with `K^R_{μνρσ} = α_vac χ(ω) P^{TT}_{μνρσ}` (line 53).
The kernel is a *temporal* memory `χ(ω) = 1/(1 − iωτ₀)` times an *index* projector
`P^TT`. There is **no spatial-gradient / `k²` / Weyl-curvature operator** in it.
The only `k`-dependence is the low-pass `χ(ω → k_phys) = 1/(1 + (L₀k_phys)²)`.

> **Consequence.** There is no mechanism in the kernel to produce a linear
> high-pass `k²` coupling. The high-pass source `μ = 1 + α(1 − G^R)` cannot be
> generated. **Not derivable.**

### Fact 3 — `P^TT` is tracefree, and the scalar-sector projector is undrived
`η^{μν} P^{TT}_{μνρσ} = 0` (line 443). A transverse-traceless projector
**annihilates scalar (density) perturbations** — scalars have no TT part. Taken
literally, `Φ^{scalar}_{μν} = α χ P^{TT} ⋆ h_r^{scalar} = 0` ⟹ **`μ_linear = 1`**.
The nonzero cosmological `μ → 4/3` (the pathological "C1") was obtained only by
switching to a **trace-only projector** for the scalar sector — and the code
itself flags this as a choice, not a derivation:

> *"Does not derive the projector index structure beyond the transverse-tracefree
> form. Other projectors (e.g., trace-only) are admissible in principle and would
> require additional physical motivation."* — `linearized_ctp_action.py`, lines 108–112

The trace-only projector is moreover **inconsistent with the tracefree
fundamental kernel** (`P^TT` annihilates exactly the trace mode the shortcut then
couples to).

---

## 4. The two options the action permits — and the failed candidate is neither

| Scalar-sector projector | linear `μ(k→0)` | status |
|---|---|---|
| **trace-only** (used in Phase 2C/2D, frw_explicit/frw_gaussian) | `1 + α = 4/3` | inconsistent with tracefree `P^TT`; **not separate-universe invariant**; → low-ℓ falsification |
| **TT / tracefree** (the fundamental kernel) | `1` | consistent; annihilates linear scalars; **linear cosmology = ΛCDM** |

The high-pass candidate `μ = 1 + α(1 − G^R)` requires a `k²` coupling present in
**neither** — not in the kernel (Fact 2), and unreachable through the minimal
matter coupling (Fact 1). It is settled out.

---

## 5. The No-Go theorem

**Claim.** The conformal/refractive response and separate-universe invariance are
mutually exclusive on linear scalar perturbations.

**Proof.**
1. GRUT's foundational object is the conformal refractive enhancement
   `n_g² = 1 + α` — an *isotropic rescaling* of the metric, i.e. a **conformal-mode
   (trace)** response.
2. A conformal-mode response to matter couples to the stress-energy **trace**
   `T = −δρ + 3δp` (the conformal Ward identity: `δS_m/δσ = √g T^μ_μ`). For CDM,
   `δT = −δρ`.
3. A long-wavelength adiabatic `δρ` **is** the separate-universe mode: it is
   locally absorbable into a rescaled FRW background (`Δ → 0`, `ℛ = const ≠ 0` as
   `k → 0`). A conformal rescaling is precisely what reproduces a local background
   rescaling.
4. Therefore, in the `k → 0` limit, a conformal response to `δρ` *is* a response
   to a background ambiguity. **A conformal response cannot be separate-universe
   invariant** — at `k → 0` the conformal mode and the separate-universe mode are
   the same object, and separate-universe invariance demands zero response there
   while the conformal enhancement demands maximal response (`μ → 1 + α`). ∎

**Corollary.** There is no first-principles linear-scalar constitutive source that
is both (a) the GRUT refractive enhancement and (b) separate-universe invariant.
One must be given up:

- keep conformal enhancement on linear scalars ⟹ `μ → 4/3` at `k → 0` ⟹
  **terminal** (the low-ℓ excess is what the mechanism *means*, not a tunable
  error);
- keep separate-universe invariance (non-negotiable — a consistency requirement,
  not a model choice) ⟹ the refractive enhancement **does not act on linear
  scalar perturbations** ⟹ `μ_linear = 1`.

The low-ℓ CMB selected: separate-universe invariance wins, so `μ_linear = 1` is
forced.

---

## 6. Verdict and consequences

1. **The high-pass linear source is dead** — forbidden by minimal coupling
   (Fact 1) and absent from the kernel (Fact 2). It was *not* "conditionally
   derivable"; the action forecloses it.
2. **`μ_linear = 1` is forced**, by the tracefree fundamental kernel (Fact 3) and
   the No-Go (§5). **Linear cosmology = ΛCDM is now a derived requirement.** The
   v2.7 demotion is theoretically necessary, not merely empirical.
3. **The low-ℓ pathology is precisely localized:** the trace-only projector
   shortcut (lines 108–112), which is *both* inconsistent with GRUT's own
   tracefree kernel *and* the unique separate-universe-violating choice. Enforcing
   projector consistency removes the pathology by removing the linear-scalar
   response entirely.
4. **GRUT's dark sector must live where the response is not a linear-scalar
   conformal coupling:**
   - the **temporal susceptibility `χ(ω)` at orbital frequencies** — rotation
     curves, cluster `v × τ₀` offsets (GRUT's actual DM mechanism);
   - the **tensor / TT** sector;
   - **second-order / nonlinear** structure (e.g. the `c`-anomaly `W²` channel,
     which is intrinsically `O(2)` since `δ(W²) = 2 W̄ δW = 0`).
   This is exactly the bound/nonlinear domain v2.7 assigned — now *derived from
   the action's projector structure*, not inferred from data.

---

## 7. The one honest caveat

The verdict assumes the responsive vacuum's susceptibility is genuinely
**conformal/scalar** (which `n_g² = 1 + α` is) and **TT** in its tensor sector
(which the kernel is). The only escape would be to posit a *fundamentally
different, non-conformal* scalar susceptibility — but that would no longer be
GRUT's refractive `n_g`, and it would still have to confront the No-Go (§5) to
avoid the trace coupling. **Within GRUT as written, the result is forced.**

---

## 8. What this defines as the next front (NOT started)

The dark sector is now a non-linear-scalar program with three defined channels:

- **(C5a) Second-order `W²` response.** Set up the `O(2)` constitutive response to
  the Weyl-squared invariant and test whether it yields `Ω_dm ≈ 1/3` and
  rotation-curve phenomenology under nonlinear collapse. (Hard: 2nd-order PT +
  N-body with the `σ·W²` vertex.)
- **(C5b) Orbital-`ω` bound-system sector.** Formalize the temporal-susceptibility
  response `χ(ω)` at orbital frequencies — already GRUT's rotation-curve and
  cluster `v×τ₀` mechanism — as the primary dark-sector physics, decoupled from
  linear cosmology.
- **(C5c) Tensor / TT sector.** Whether the genuine `P^TT` response (gravitational
  waves) carries any observable dark-sector signature.

Linear cosmology is closed: it is ΛCDM, by the No-Go. No further linear-source
search is warranted.

---

## References (internal)

- `grut/derivation/phi_munu/linearized_ctp_action.py` — Phase 2A: the constitutive
  CTP action; `K^R = α χ P^TT` (line 53); minimal matter coupling (line 302);
  `P^TT` tracefree (line 443); scalar-sector projector flagged undrived (108–112).
- `grut/derivation/phi_munu/frw_gaussian_path_integral.py` — Phase 2D: the
  trace-projector scalar reduction (`δT_m = −δρ_m`, C7d) that produces the
  pathological `μ = 1 + α G^R`.
- `theory/CMB_ISW_EQUALITY_FILTER.md` — the empirical record (rescue routes
  closed).
- Ch 14, Correction #38 — the MGCAMB falsification of the linear branch.
- Stewart & Walker (1974); Weinberg (2003), adiabatic modes; Komargodski &
  Schwimmer (2011), conformal-mode trace anomaly (`α_vac = 1/3`).
