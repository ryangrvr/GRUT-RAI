# Koide Amplitude Unification — Frontier #1 Partial Result

**Date:** June 2026 (2026-06-15)
**Status:** Genuine progress on the three-flavor `z_target` frontier (V7 §29 "the
missing object"). **Not a closure** — it corrects a V7 conjecture, unifies two
candidate identities into one, and sharpens the open target to a single number.
**Code:** `grut/derived/flavor/koide_circulant_unification.py` (6/6 verify legs,
11/11 tests). **Companion:** `theory/V2_SELF_CONTAINMENT_AUDIT.md` (frontier #1).

---

## Setup

Circulant (Z₃) Koide parameterization for N generations:

    √m_k = M_0 (1 + A cos(θ + 2πk/N)),   k = 0 … N−1

`M_0` = scale, `θ` = phase (mass ratios), `A` = oscillation amplitude.
Koide invariant `K = (Σ m_k)/(Σ √m_k)²`.

---

## Result 1 — the V7 "Spectral Koide" conjecture is overstated

V7 §29 (Conjecture, Spectral Koide) asserts `K = 2/3` is **"FORCED by the Z₃
cyclic structure of three generations."** This is **not correct.** Summing the
circulant series (`Σcos = 0`, `Σcos² = N/2` for N ≥ 3) gives, for **any** θ:

> **K_N(A) = (1 + A²/2) / N**   — θ-independent (symbolically verified, N=3,4,5)

So Z₃ fixes the *form* (θ-independence) but **not the value**: at N=3, K ranges
over all of (1/3, ∞) as A varies (K=0.5 at A=1, K=2/3 at A=√2, K=1 at A=2). The
Koide value requires the **specific amplitude**

> **A = √2**  ⟺  √m makes a **45° angle** with the democratic axis (1,1,1).

The amplitude — not the Z₃ symmetry — carries the physics. Empirically nature
sits at A = 1.414201 (vs √2 = 1.414214), from the measured charged-lepton masses
(K_obs = 0.666661).

**Consequence:** the open question is not "why Z₃" (that's the generation count)
but **"why A = √2."**

---

## Result 2 — both candidate identities collapse to one input: A² = N − 1

v2 carried two separate candidate identities: `K = 2/3` (Koide) and
`θ = K·α_vac = 2/9` (the phase, `koide_theta_2_over_9_uniqueness`). **They are not
independent.** Posit the single structural relation

> **A² = N − 1**   (with α_vac = 1/N)

— the oscillation variance equals the number of non-zero circulant modes
(equipartition of the N−1 oscillating Fourier modes about a unit mean; equivalently
`A² = 1/α_vac − 1`). Then **both** observables follow at once:

| quantity | general (A²=N−1) | N = 3 |
|---|---|---|
| K  = (1+A²/2)/N | **(N+1)/(2N)** | **2/3** |
| θ  = K·α_vac = K/N | **(N+1)/(2N²)** | **2/9** |

So `K = 2/3` and `θ = 2/9` are two faces of `A² = N − 1`. The flavor sector's two
"coincidences" reduce to one. (All verified symbolically + numerically.)

---

## Status ledger

| Item | Status |
|---|---|
| `K_N(A) = (1+A²/2)/N` | **PROVEN** (symbolic, tested) |
| `K = 2/3 ⟺ A = √2` | **PROVEN** |
| V7 "Z₃ forces K=2/3" | **CORRECTED** (overstated; needs A=√2) |
| `A²=N−1 ⟹ (K,θ)=(2/3, 2/9)` at N=3 | **PROVEN** (the unification) |
| `A² = N − 1` itself | **CANDIDATE** (numerically `= 1/α_vac − 1`; but NOT forced by the fixed point — see no-go) |
| Does the fixed point force `A²=N−1`? | **NO-GO** (June 2026; see below) |
| `M_0` absolute mass scale | **OPEN** (dimensional-anchor gap, untouched) |

---

## The fixed-point derivation — attempted, NO-GO (June 2026)

The sharpened question was: *does the three-flavor CTP fixed point `F_spatial[z*]=0`
force `A²=N−1` (the 45° cone), turning K=2/3 and θ=2/9 into theorems?* We attempted
it. **The answer is NO.** Three findings (verified; `fixed_point_amplitude_nogo`):

1. **Symmetry does not fix the amplitude.** The Z₃-invariant Landau potential has
   critical point `ρ* = −a₂/(2b)` — the amplitude is a function of the potential
   *coefficients*. Z₃ + gradient flow give the form, not the value.
2. **GRUT's own impedance gives the *wrong* value.** The natural self-referential
   balance (response = α_vac × drive, i.e. structured/democratic power
   `2ρ = α_vac = 1/N`) gives `K = (1+1/N)/N = 4/9` at N=3, **not** 2/3. The Koide
   amplitude `A=√2` is `~4.24×` the impedance α_vac=1/3 — GRUT's impedance is far
   too small to be its source.
3. **Koide requires equipartition** (`2ρ=1`, structured = democratic power,
   "impedance 1"), which is **not** GRUT's α_vac=1/3. A linear self-consistency
   gives only pure modes (K=1/3 or 1), never the mixture; the ζ₀:ζ₁ ratio that
   yields K=2/3 needs nonlinear potential coefficients = the SM Yukawa input.

**Conclusion:** `K = 2/3` and `θ = 2/9` are **NOT derivable** from the GRUT
constitutive fixed point. They remain **CANDIDATE IDENTITIES**, not theorems. The
amplitude is irreducibly Yukawa-input — consistent with V7 §29 ("GRUT hosts, does
not generate, the Yukawas"). The earlier hope that the fixed point would close it
is **retracted**.

**Surviving coincidence** (recorded as such, *not* a derivation): at N=3,
`K = 2/3 = (1+α_vac)/2 = n_g²(0)/2 = 2·α_vac` — the Koide ratio equals half the GRUT
DC refractive index `n_g²(0)=4/3`. Numerically clean, but it is a re-expression of
the `A²=N−1` posit; the dynamics (finding 2) does not produce it.

`M_0` (the absolute mass scale) remains a separate, untouched honest-negative.

---

## What changed in the codebase

- `grut/derived/flavor/koide_circulant_unification.py` — module (derivation +
  `fixed_point_amplitude_nogo()` + `verify()`, 8 legs).
- `tests/derived/flavor/test_koide_circulant_unification.py` — 12 tests, all passing.
- Corrects V7 Conjecture F1 (Spectral Koide); records the fixed-point no-go.

**Bottom line:** the flavor frontier is **sharpened and bounded, not closed.** A V7
over-claim was corrected (Z₃ does not force 2/3); the two coincidences were unified
(`A²=N−1`); and the fixed-point route was tried and shown to be a **no-go** (GRUT's
impedance gives 4/9, not 2/3). K=2/3 and θ=2/9 are candidate identities requiring
Yukawa input — that is now a *result*, not an open hope.
