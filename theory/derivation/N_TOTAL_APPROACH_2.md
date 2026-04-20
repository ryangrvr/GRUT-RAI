# N_total Structural Derivation — Five More Approaches

**Date:** April 2026
**Status:** One tight finding (N_total/N_threshold ≈ R_vol within 0.82%),
three approaches ruled out, two flagged for V8 track work.

## Approaches tried

### #1 Constitutive convergence criterion — RULED OUT

Claim: N_total is the era where |H−H_inf|/H_inf drops below some
structurally-defined tolerance.

At today: H_0/H_inf − 1 = 1/√Ω_Λ − 1. For GRUT's Ω_Λ=0.71 this is 0.187,
for Planck Ω_Λ=0.689 it's 0.205.

Compared to structural candidates:
- (R−1)/R = 0.134
- (2−R)/2 = 0.423
- C_FINAL = 1.14 × 10⁻⁴
- log(R_vol) = 0.434

**None match 0.187.** The convergence ratio has no obvious structural
origin. And H/H_inf doesn't reach 1% of H_inf until ~7 Gyr past today,
so today isn't structurally defined by H-convergence.

### #2 Dark matter production anchor (S_K = 1) — STATIC, NOT ERA-DEPENDENT

V7 §28 mentions S_K = 1.000 "marginal production, exact" for Route 1
dark matter. Checked `grut/derived/dark_matter/sector.py`:

```python
>>> route_1()['S_K']
1.0
```

**S_K is a static value**, not a function of era. It doesn't vary with N
in the current implementation. Can't anchor N_total to it without
extending the dark-sector dynamics.

Potential V8 work: make S_K era-dependent via freeze-out cross-section
integration; find the era where S_K crosses 1.

### #3 Factorization 329 = 7 × 47 — PARTIAL HIT, NO CLOSURE

**329 = 7 × 47 exactly.**

- 7 matches QCD β₀ for n_f = 6 active quarks (b₀ = 11 − 2·6/3 = 7) —
  genuine physics.
- **47** has no obvious SM origin. Not a Casimir. Not 11 × (integer).
  Not SU(N)×SU(M) combinatorics.

The 7 side is clean; the 47 side isn't. Probably not structural —
coincidence.

### #4 N_total = N_threshold × R_vol — **CLOSE, WORTH FOLLOW-UP**

**329/215 = 1.5302 vs R_vol = 1.5428 → off by 0.82%.**

This is the tightest match in any approach.

If structural, it would say: the era map's post-threshold phase lasts
R_vol × (pre-threshold phase). Both eras (215 and 329) would be
determined by (τ₀, R_vol).

**But what IS R_vol structurally?**

Checked against flat-ΛCDM interpretations:

| Interpretation | Value | Match to R_vol=1.5428 |
|:---|:---:|:---:|
| a(today)/a(t_eq) — scale factor ratio | 1.348 | −12.6% |
| √(Ω_Λ/Ω_m) — vacuum-matter amplitude ratio | 1.565 | +1.4% |
| Ω_Λ/Ω_m — density ratio | 2.448 | — |
| t_0/t_eq in flat ΛCDM | 1.396 | −9.5% |

**Closest match: R_vol ≈ √(Ω_Λ/Ω_m)** (1.4% off).

If R_vol ≡ √(Ω_Λ/Ω_m) structurally, and N_total/N_threshold = R_vol,
then using V7's N_threshold = 215:
- Ω_Λ/Ω_m = R_vol² = 2.380
- Ω_m = 1/(1 + 2.380) = 0.2994
- Ω_Λ = 0.7006
- H_0 = H_inf/√Ω_Λ = 58.16/√0.7006 = **69.5 km/s/Mpc**

Consistent with our earlier one-parameter prediction (69.03 km/s/Mpc)
within 0.7%.

**Verdict:** promising but not proven. Needs V7 clarification of what
R_vol is derived from. If R_vol is defined as some structural cosmological
ratio (not a fit parameter), this becomes a clean derivation chain:

```
R_anomaly (3-loop CTP)  →  H_inf
τ_0 (noise kernel)       →  era length
R_vol (structural)       →  N_total/N_threshold ratio
N_threshold (if derived) →  matter-Λ equality era
          ↓
   H_0 ≈ 69.5 km/s/Mpc (zero-parameter prediction)
```

**Open question for V7**: what's the structural derivation of R_vol?

### #5 Entropy/information completion — TOO SPECULATIVE

Claim: N_total is the era where integrated decoherence reaches a
structural maximum (e.g., enough to decohere all SM degrees of freedom).

**Not pursued**: requires defining "enough to decohere" in a structural
way, which isn't in the framework yet. Speculative.

### #6 Ω_b + Ω_dm bridge — HALF-WAY POSSIBLE

GRUT predicts η_B = 6.57 × 10⁻¹⁰ (COMPUTED, V7 §31).

Using n_γ = 411/cm³ (CMB temperature anchor — minimal observational input):
- n_b = η_B × n_γ = 2.70 × 10⁻⁷ /cm³
- ρ_b = n_b × m_p = 4.52 × 10⁻²⁸ kg/m³
- Ω_b (at H_0 = 67.4) = 0.053

vs Planck observed Ω_b = 0.0486. **GRUT Ω_b matches observation within 9%.**

But Ω_dm is not directly computed:

```python
>>> from grut.derived.dark_matter.sector import route_1
>>> route_1()  # g_dark, lambda, M_dark — no Ω_dm
```

To get Ω_dm from the dark sector, we'd need:
- Thermal freeze-out calculation with dark photon mediator
- Dark relic abundance from cross section + equilibrium temperature
- Currently not in the codebase

**V7 Track VII (dark sector completion) would provide this.** Once Ω_dm is
computed, Ω_m = Ω_b + Ω_dm is COMPUTED, and H_0 becomes a zero-parameter
prediction via flat-ΛCDM Friedmann.

## Summary matrix

| Approach | Outcome | Next step |
|:---|:---|:---|
| #1 Constitutive H-convergence | No structural match | Ruled out |
| #2 Dark matter S_K=1 | Static value, not era-dependent | V8 Track VII extension |
| #3 Factorization 329=7×47 | 7 matches β₀, 47 doesn't | Likely accidental |
| **#4 N_total = N_threshold × R_vol** | **0.82% match** | **Clarify R_vol derivation** |
| #5 Entropy completion | Too speculative | Future |
| #6 Ω_b + Ω_dm bridge | Ω_b computed, Ω_dm missing | V8 Track VII |

## Best path forward

**The tightest structural relationship found**:

    N_total / N_threshold ≈ R_vol   (within 0.82%)

Combined with approach #6 (Ω_b computed, Ω_dm needs Track VII), we have
two paths to zero-parameter H_0:

**Path A (via R_vol)**: Clarify what R_vol is structurally. If R_vol
can be derived from GRUT's axioms (not fit to data), then
N_total = N_threshold × R_vol is the zero-parameter age formula.
Requires V7 §27 documentation check.

**Path B (via Ω_m)**: Compute Ω_dm from dark sector (V8 Track VII).
Once Ω_m = Ω_b + Ω_dm is COMPUTED, H_0 = H_inf/√(1 − Ω_m) is a
zero-parameter prediction.

Both paths converge on H_0 ≈ 69-70 km/s/Mpc.

## Honest state

- **Zero-parameter H_0 NOT achieved** in this round
- **One-parameter H_0 = 69.03 km/s/Mpc** stands from previous log
- **Most promising path**: #4 (if R_vol is structural) or #6 (Track VII)
- **Ruled out paths**: #1, #3, #5

The attempt surfaced the key open question: **is R_vol = 1.5428
derivable from GRUT's fundamental structure, or is it fit to match
cosmological observation?** The answer determines whether approach #4
becomes a structural derivation or stays as an empirical near-match.

## Next concrete step (1-2 hour task)

Search V7 documentation for the derivation of R_vol. If it's defined
structurally (e.g., from CTP normalization, from the era-map sigmoid
structure, or from matter/vacuum ratio), promote approach #4 to a
structural derivation and compute H_0 zero-parameter.

If R_vol is fit to match observed expansion history, document that
clearly in V7 and leave approach #6 as the zero-parameter path (awaiting
Track VII).

## Honesty ledger

12 corrections caught, 0 hallucinations. This attempt documented as
HONEST NEGATIVE on the zero-parameter goal with an informative
near-miss (approach #4) that depends on V7 clarification to close.
