# GRUT v3 — Test 04: C5a, the W² Nonlinear Channel (existence test)

**Date:** June 2026 (2026-06-17) · branch `main_v3`
**Status:** COMPLETE — **verdict UNDETERMINED (NOT refuted)**; adversarially verified, **read-only**
workflow (`w3zgsvvwi`). The first channel of the v3 audit to clear its structural gates.
**Question:** does the second-order Weyl-squared (W²) constitutive response — the only dark-sector
channel not already refuted — produce an effective source of the right sign, scaling, and magnitude?
Structured as the gated sequence 04A→04B→04C (04D deferred).

---

## Why C5a was eligible at all

The No-Go forbids *first-order* responses to locally-absorbable/separate-universe modes (which killed
Tests 01–03). `W² = C_μνρσ C^μνρσ` is genuinely *second-order* (`δ(W²)=2W̄·δW=0` on FRW, since the
background Weyl tensor vanishes), so it is **not** subject to that first-order cancellation. C5a is
the residue that survived the constraint gauntlet — the first *constructive* candidate.

## The gated sequence

- **04A — Sign: PASSES (positive, dark-matter-like).** `W²` is a sum of squares (`>0` wherever tidal
  structure is realized); the trace-anomaly c-channel (`⟨T^μ_μ⟩ = a·E₄ − c·W²`, `c=3>0`) gives an
  effective source `ρ_eff ∝ c·W² > 0` — attractive. No sign obstruction.
- **04B — Scaling: SOUND.** Dimensions force `ρ_eff ~ α·L²·W²` (n=2: `[W²]=L⁻⁴`, `[ρ_eff]=L⁻²`).
  `W²=0` on the FRW background → **no cosmological signal** (consistent with `μ_linear=1`); it appears
  only in bound systems where the realized tidal field is O(1) (`W² ~ (GM/r³)² ~ (v²/r²)²`). The
  temporal gate `χ(ω_dyn)` does **not** suppress it (galaxies/clusters are DC-like, `ωτ₀≪1`).
- **04C — Magnitude: UNDETERMINED — the ~10²⁷× length-scale swing.** The CTP kernel is spatially
  *local* (no `∇²`), so the length prefactor `L` is not fixed by dimensions:

  | scale | galaxy `ρ_eff/ρ_b` | cluster | status |
  |---|---|---|---|
  | `L = L₀ ≈ 12.85 Mpc` | ~10⁻²⁷ | ~10⁻²⁹ | **negligible → C5a dies** |
  | `L = r` (local) | ~few (within 2–3× of DM) | ~100× | **galaxy marginal, cluster overshoot** |

  Under local coupling the galaxy case is the **best signal any GRUT mechanism has produced** — but
  it carries a **galaxy–cluster tension** (the same local scale overshoots clusters ~100×). The
  scale and the dimensionless kernel prefactor are *not* derivable from dimensional analysis.

## Verdict: UNDETERMINED — and that is the result

C5a is **not refuted** (sign and scaling pass) and **not confirmed** (magnitude undetermined,
contingent, and tension-bearing). This is categorically different from Tests 01–03, which died.
**GRUT's entire dark-matter fate is now reduced to one specific, well-posed, uncomputed quantity:**
the explicit second-order constitutive kernel
`K⁽²⁾_μνρσ(ω) = δ²S_CTP/δh_a δh_r |_{O(2)}` — specifically (i) its dimensionless prefactor `σ` in the
`σ·∫W²` coupling, and (ii) the coupling length scale (`L₀` vs local `r`). 

- If the computation gives `L₀`-scale or a small prefactor → **negligible**: C5a dies, GRUT has **no
  derived dark-matter mechanism**, dark matter is a hosted input.
- If it gives local-`r` scale with an O(1) prefactor → galaxy-marginal: C5a becomes GRUT's **first**
  dark-sector candidate to pass the gauntlet, and 04D (phenomenology, incl. the galaxy–cluster
  tension) is warranted.

**Do not over-read the marginal galaxy signal:** it is contingent on an undetermined scale and
already in tension with clusters. The honest statement is *undetermined*, not *viable*.

## The four-test dark-sector map

| Channel | Verdict |
|---|---|
| Linear cosmological enhancement | refuted (Test 01) |
| Dielectric `Ω_dm = α` | refuted (Test 01) |
| C5b orbital-frequency gate | refuted on magnitude (Test 03) |
| Derived `a₀` scale | survives |
| **C5a (W² second-order)** | **undetermined — sign+scaling pass; magnitude rests on the 2nd-order CTP kernel** |

## Next — the decisive computation (04D gated on it)

Compute `Φ⁽²⁾_μν = δ²S_CTP/δh_a δh_r |_{O(2)}` explicitly → the second-order kernel `K⁽²⁾`, its
prefactor `σ`, and its coupling length scale. Evaluate `ρ_eff` on realistic `W²` profiles
(galaxy + cluster). This single computation closes GRUT's dark sector — viable or dead — on the
framework's own terms. Only if it yields sufficient magnitude does 04D (rotation curves, cluster
offsets, the galaxy–cluster tension) become warranted.
