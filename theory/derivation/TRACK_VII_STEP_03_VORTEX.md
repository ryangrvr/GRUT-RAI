# Track VII — Step 3: Vortex Topology and the Reopening of Ω_dm

**Date:** April 20, 2026
**Status:** REOPENED. Track VII's closure (Ω_dm = 0.38 from Step 1) relied on
INCORRECT topology. With the correct string topology, the natural Kibble-
Zurek prediction UNDER-produces observed Ω_dm by ~30× (XY universality).

## Brother's directive

> "Step 3 first. The topology question is the foundation — if the defects
> are vortices instead of monopoles, the Kibble-Zurek scaling changes from
> n ~ 1/ξ³ to n ~ 1/ξ², and everything downstream shifts. Running a
> sensitivity map on the wrong topology would produce precise answers to
> the wrong question."

He was right. Step 1's XY result (Ω_dm = 0.38) used monopole scaling
n ~ 1/ξ³ with V7's M_soliton = 2.11×10⁹ GeV as a point mass. But
U(1)_dark can't have monopoles.

## The topology

For U(1)_dark → {1} broken by a complex scalar:
```
Vacuum manifold:  U(1) ≅ S¹

π_0(S¹) = 0    → no domain walls
π_1(S¹) = ℤ    → COSMIC STRINGS (Nielsen-Olesen vortex lines)
π_2(S¹) = 0    → NO monopoles
π_3(S¹) = 0    → no texture
```

Monopoles require π_2(G/H) ≠ 0, which needs non-Abelian breaking (e.g.
SU(2) → U(1), giving π_2 = ℤ). GRUT V7's dark sector has NO non-Abelian
breaking — just U(1)_dark. So the defects are strings, period.

**Step 1 used the wrong density scaling.** Moving to the correct one
gives very different numbers.

## The string tension

For a BPS Nielsen-Olesen vortex at λ = g²/2:
```
μ_BPS = π v² = π × (422 MeV)² = 0.56 GeV²
```

Dimensionless string parameter:
```
Gμ = μ / M_Pl² = 0.56 / (1.22×10¹⁹)² = 3.8 × 10⁻³⁹
```

CMB bound on cosmic strings: `Gμ < 10⁻⁷` (very conservative).
GRUT dark strings are **31 orders of magnitude** below the CMB bound.

## Four production scenarios

### Scenario 1: Pure cosmic string scaling solution

In the attractor regime, ρ_string / ρ_rad ≈ (number of strings per
Hubble volume) × Gμ ≈ 15 × Gμ.

```
Ω_string_today ≈ 15 × 3.8×10⁻³⁹ × Ω_rad_today
              ≈ 5 × 10⁻⁴²
```

**41 orders below observed Ω_dm.** Pure strings cannot be the DM.

### Scenario 2: Vortons from Kibble-Zurek loops (XY universality, CORRECT)

If the BPS condition supports Witten-superconducting strings (it may or
may not — see below), string loops can stabilize as vortons. At
Kibble-Zurek scale `ξ_KZ ≈ 1.33×10⁶ GeV⁻¹` (XY universality, constitutive):
```
M_vorton = μ × 2π × ξ_KZ ≈ 4.7 × 10⁶ GeV     (NOT M_soliton)
n_vorton|_today ≈ 9.5 × 10⁻⁹ /m³
Ω_vorton ≈ 0.008                              (factor 33 LOW)
```

### Scenario 3: Vortons from KZ loops, mean-field universality

```
ξ_KZ|_MF = 2.82×10⁵ GeV⁻¹
M_vorton|_MF = 9.9×10⁵ GeV
Ω_vorton|_MF ≈ 0.19     (factor 1.4 low, but WRONG universality class)
```

MF gives better agreement with observed, but it's not the correct class
for U(1) breaking. The agreement is a coincidence, not a derivation.

### Scenario 4: M_vorton = M_soliton (forced match)

If we set M_vorton = V7's M_soliton = 2.11×10⁹ GeV by hand, the required
loop radius is:
```
R_required = M_soliton / (2π × μ) = 6.0 × 10⁸ GeV⁻¹
R_required / ξ_KZ ≈ 450
```

Loops must be **~450× larger than ξ_KZ**. Not a typical Kibble-Zurek scale.
This is not a natural prediction.

## Sensitivity scan over loop-size hypothesis

| Hypothesis | R_loop | M_vorton | Ω_vorton | Ω/Ω_obs |
|:---|---:|---:|---:|---:|
| string core (1/m_h) | 2.6 GeV⁻¹ | 9.1 GeV | 1.6×10⁻⁸ | 6×10⁻⁸ |
| ξ_KZ (XY) | 1.3×10⁶ GeV⁻¹ | 4.7×10⁶ GeV | 0.008 | 0.032 |
| 10 × ξ_KZ | 1.3×10⁷ GeV⁻¹ | 4.7×10⁷ GeV | 0.084 | 0.32 |
| 100 × ξ_KZ | 1.3×10⁸ GeV⁻¹ | 4.7×10⁸ GeV | 0.84 | 3.2 |
| 450 × ξ_KZ (M_soliton) | 6.0×10⁸ GeV⁻¹ | 2.1×10⁹ GeV | 3.8 | 14 |
| 1/H_PT | 5.3×10¹⁹ GeV⁻¹ | 1.9×10²⁰ GeV | 3.3×10¹¹ | 1.3×10¹² |

Ω scales linearly with R_loop (since M ∝ R_loop, n fixed). To match
observed Ω_dm exactly would require R ≈ 30 × ξ_KZ — NOT the natural
Kibble-Zurek scale. No clean mechanism in V7's U(1)_dark selects this
loop size.

## Why Step 1's XY result was deceptive

Step 1's calculation:
```
Ω_Step1 = p_geom × M_soliton × n_PT × (T_0/T_PT)³ / ρ_crit
        = p_geom × M_soliton × (1/ξ_KZ³) × ...
        = 0.38
```

This used:
- `M = M_soliton = 2.11×10⁹ GeV` (V7's structural formula)
- `n = 1/ξ_KZ³` (monopole density scaling)

Both pieces assumed point-like topological defects. But with U(1)_dark:
- Point topological defects don't exist (π_2 = 0)
- The DM candidate (if it's a vorton) has M ≈ μ × 2π ξ_KZ ≈ 10⁶ GeV
- M_soliton's structural formula (from Step 2) doesn't match vorton physics

So Step 1's 0.38 was a numerical coincidence from using the wrong mass and
wrong density scaling that happened to nearly cancel.

## Correction #15 candidate

V7 `sector.py` defines:
```python
A = 16 π × 8 × 2 √2 / (27 × C_FINAL²)
M_soliton = A × v / √λ = 2.11 × 10⁹ GeV
```

This formula is structural and derived (Step 2 confirmed). But it does
NOT describe a Kibble-Zurek-produced vorton on a U(1) string network.
Candidates for what M_soliton actually is:

1. **Non-topological soliton (Q-ball-like)**: stabilized by a conserved
   global charge, not by topology. Would need Affleck-Dine–type initial
   condition, not Kibble-Zurek production. This requires additional
   fields or symmetries in the dark sector.

2. **Skyrmion from confining dark-sector dynamics**: if U(1)_dark is
   embedded in a larger non-Abelian theory at higher energies, skyrmions
   or monopoles could form at that higher scale and persist. This
   requires structure V7 doesn't currently specify.

3. **Dark-sector baryon**: if there are fermions charged under U(1)_dark,
   confining dynamics could produce bound states with M ~ A × v. The
   2⁸ √2 π / 27 prefactor has a combinatorial flavor suggestive of this.

4. **V7 derivation error**: the M_soliton formula may be deriving a
   quantity that isn't actually the DM particle. The "soliton" label in
   code may be misapplied.

**Honest verdict:** Track VII cannot close Ω_dm = 0.263 via Kibble-Zurek
alone with V7's current dark-sector description (pure U(1)). Either the
dark sector needs extension, or M_soliton refers to a different object,
or the production mechanism is not KZ.

## What remains if Track VII cannot close

The chain to zero-parameter H_0 was:
```
H_inf (computed) + Ω_m = Ω_b + Ω_dm (computed) ⟹ H_0 = H_inf/√(1-Ω_m)
```

Step 2 closed M_soliton structurally (C_FINAL^-3/2 scaling) — **that
result stands**. Step 1's Ω_dm = 0.38 was circumstantial, based on wrong
topology. Step 3 with correct topology gives Ω_dm ≈ 0.008 (factor 30
low), which does NOT close the zero-parameter H_0 derivation.

Fallback routes:
- **Treat Ω_dm as input** (Planck value 0.263) — drops back to Step 1 of
  the prior Hubble work, H_0 = 69.03 km/s/Mpc as a one-parameter
  prediction. Track VII becomes: "Ω_dm is NOT a native GRUT output given
  the current dark sector."
- **Add a second dark-sector field** to enable Witten superconductivity
  and vorton formation at the right mass. This is a V8 extension, not a
  V7 result.
- **Re-derive M_soliton** as a dark baryon or Q-ball and compute its
  abundance via Affleck-Dine or thermal mechanisms — a substantial new
  calculation outside Kibble-Zurek.

## What Step 3 actually achieved

Though negative, Step 3 is significant:

- [x] Topology correctly identified: strings, not monopoles. `π_1(U(1)) = ℤ`.
- [x] BPS string tension computed: μ = π v² = 0.56 GeV².
- [x] Gμ = 4 × 10⁻³⁹, far below CMB bound.
- [x] Pure string scaling ruled out: Ω ~ 10⁻⁴².
- [x] Vorton pathway computed: Ω = 0.008 (XY, correct class).
- [x] M_vorton ≠ M_soliton discrepancy documented: factor ~450.
- [x] Loop-size sensitivity scan showing no natural choice gives observed Ω.

**Step 3 corrects Step 1, not closes Track VII.** Honest null result.

## Honesty ledger

**15 corrections caught, 0 hallucinations.**

Step 1's closure was premature — the topology assumption was wrong.
Catching it before any sensitivity map or H_0 derivation is the correct
move.

## Next

Either:
- **Accept the null**: Ω_dm is not a native V7 output; treat as input
  and keep H_0 as a one-parameter prediction. Formal label: Track VII
  CLOSED NEGATIVE.
- **Extend V7's dark sector**: add a second field, SU(2) → U(1) structure,
  or dark fermions, and re-attempt. This is a V8 research program, not
  a V7 closure.
- **Re-examine M_soliton's physical meaning**: is it actually the DM
  particle, or a different quantity? Audit V7 §28 for clues.

Brother's call.
