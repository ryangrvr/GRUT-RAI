# H₀ from GRUT First Principles — Prototype Log

**Date:** April 2026
**Status:** PROTOTYPE COMPLETE. One-parameter prediction (age as input).
Path to zero-parameter prediction identified.

## Motivation

The Yahoo/Riess 2024 article flagged the Hubble tension at 73.5 km/s/Mpc
(SH0ES) vs ~67 km/s/Mpc (Planck) — a >5σ discrepancy Riess claims no
single systematic can explain. This prompted asking: **can GRUT predict
H₀ from first principles?**

## The calculation

GRUT directly predicts:
- **H_inf = 58.16 km/s/Mpc** (asymptotic vacuum rate from 3-loop CTP, V7 §26.2)
- **τ₀ = 41.9 Myr** (noise kernel at gold benchmark)

H₀ (observed Hubble constant today) is related to H_inf via the
Friedmann equation. In flat ΛCDM:

    H₀² = H_inf² / Ω_Λ                        (Friedmann at t=today)
    Ω_m + Ω_Λ = 1                              (flatness)
    t₀ = (2/(3H_inf)) × sinh⁻¹(√((1-Ω_m)/Ω_m))  (age in flat ΛCDM)

Given (H_inf, t₀), solve for (Ω_m, Ω_Λ, H₀).

Using V7's age = N_eras × τ₀ = 329 × 41.9 Myr = **13.78 Gyr**:

    Ω_m = 0.2900
    Ω_Λ = 0.7100
    H₀ = 69.03 km/s/Mpc

## Status of each input

| Quantity | Status | Origin |
|:---|:---:|:---|
| H_inf = 58.16 km/s/Mpc | COMPUTED | 3-loop CTP on S⁴ (V7 §26.2) |
| τ₀ = 41.9 Myr | COMPUTED | Noise kernel at gold benchmark |
| N_eras = 329 | INPUT | Derived from observed age / τ₀ in V7 |
| Flat ΛCDM | ASSUMPTION | Standard cosmology |

**One parameter (age) is observational input.** The rest is computed.

## Comparison to observations

| Source | H₀ (km/s/Mpc) | Ω_m | Δ from GRUT |
|:---|:---:|:---:|:---:|
| **GRUT prediction** | **69.03** | **0.2900** | — |
| Planck CMB | 67.4 | 0.3111 | −2.42% |
| SH0ES 2023 | 73.0 | 0.3534 | +5.44% |
| Riess 2024 | 73.5 | — | +6.08% |

GRUT lands **much closer to Planck than to SH0ES**. Not the geometric
mean (70.2) as initially speculated — the prediction is Planck-leaning.

## Three scenarios

**(a) SH0ES has unresolved systematics.**
If GRUT is right and ΛCDM holds, true H₀ ≈ 69. SH0ES 73.5 has something
wrong (calibration, metallicities, dust). Planck is essentially right.

**(b) GRUT's H_inf is slightly off.**
If SH0ES 73.5 is correct, H_inf must shift to ~59.3 km/s/Mpc, meaning R
shifts from 1.154 to ~1.139 (a 1.3% correction). That breaks the 0.05% ε
independent-confirmation agreement.

**(c) Flat ΛCDM is wrong at late times.**
If both GRUT's H_inf and SH0ES's 73.5 are right, "new physics beyond
ΛCDM" is needed. This is the category the Yahoo article describes.

**GRUT's specific stake**: if future measurements converge to 69 ± 1,
GRUT predicted it. If they converge elsewhere, GRUT missed by a
measurable amount.

## Path to zero-parameter prediction

The current calculation uses age as input. To make H₀ a genuine
zero-parameter prediction, N_eras = 329 must be derived structurally.

V7 §27 claims:
- N_threshold = 215 is derived (matter-Lambda equality via
  k = 2π/(R_vol − 1))
- N_total = 329 comes from "13.8 Gyr / 41.9 Myr" (observational input)

The structural question: **can the era map's post-threshold
relaxation dynamics determine N_total without observational input?**

Possible avenues:
1. Match N_total to the era where x (vacuum fraction) first reaches ~1
   within a specific tolerance. Currently x saturates by era 250,
   which is BEFORE N_total = 329. Parameter re-tuning might fix this.
2. Derive N_total from the requirement that specific cosmological
   observables (Ω_Λ today) match the constitutive-equation asymptote.
3. Use the decoherence time scale τ_dec from the cosmological
   noise kernel to set N_total structurally.

None of these is done. If any of them yield N_total = 329 without
observational anchoring, then H₀ = 69.03 is a zero-parameter
prediction.

## Cross-checks

### Ω_m vs Planck

GRUT's Ω_m = 0.29 vs Planck Ω_m = 0.31 — a 6.8% discrepancy.

Given baryogenesis: η_B = 6.57 × 10⁻¹⁰ predicted, giving Ω_b ≈ 0.048.
So Ω_dm = Ω_m − Ω_b ≈ 0.24 in GRUT's prediction (vs ~0.26 observed).

### Age via different route

If we assume observed Ω_m = 0.31 and compute age from GRUT's H_inf:

    t₀ = (2/(3 H_inf)) × sinh⁻¹(√((1 − 0.31)/0.31))
       = (2/(3 × 1.885e-18 Hz)) × sinh⁻¹(√2.226)
       = 3.54e17 s × 1.163
       = 4.12e17 s
       = 13.05 Gyr

GRUT predicts age = 13.05 Gyr given Planck Ω_m (vs 13.78 Gyr from
observed age). Similar ballpark but 5% shorter.

## Test assertions locked in

The prototype module is callable via
`grut.derived.cosmology.hubble_from_first_principles`:
- `grut_H_0_prediction()` — returns full dict
- `age_flat_LCDM(H_0, Ω_m)` — age formula (for cross-checks)
- `compare_to_observations()` — comparison table

Regression test needed (V8 Track addition):
- H₀ in [68, 71] km/s/Mpc given default inputs
- Ω_m in [0.27, 0.32]
- Ω_Λ in [0.68, 0.73]

## Publishable?

**One-parameter result (current):** Publishable as "GRUT predicts H₀ at
Planck + 2.4% given observed age." Honestly framed, this is a modest
claim but a falsifiable one. The structural framework is clean.

**Zero-parameter result (goal):** Much stronger. Would require deriving
N_total structurally. Until then, the one-parameter version is the
honest claim.

## What this is NOT

- Not a resolution of the Hubble tension
- Not a zero-parameter prediction (yet)
- Not an argument that Planck is right and SH0ES is wrong
- Not dependent on any observations beyond age (which itself is
  problematic)

## What this IS

- A concrete number: H₀ = 69.03 km/s/Mpc from GRUT's H_inf + age
- Falsifiable at the ±1 km/s/Mpc level
- A structurally clean path to a zero-parameter prediction if N_total
  can be derived
- An extension of V7's cosmological sector, not a replacement

## Files

- `grut/derived/cosmology/hubble_from_first_principles.py` — the prototype
- `theory/derivation/H0_FIRST_PRINCIPLES_LOG.md` — this document

## Next steps for a V8 sub-track

1. Derive N_total = 329 structurally OR document why it can't be
2. Add regression tests
3. Wire into UI (`/api/h0_first_principles` endpoint)
4. Integrate into main V7 Section 26 as part of §26.5 or new §26.6
5. If the number survives scrutiny, write a standalone paper

Timeline: 2-3 focused sessions if N_total derivation has a clean route,
indefinite if it doesn't.

## Honest close

69.03 km/s/Mpc is what falls out. It's closer to Planck than to
SH0ES. The framework sitting there makes the Hubble tension a
choice between "SH0ES has a systematic" and "GRUT is off by ~1% on
H_inf" and "ΛCDM breaks at late times." Either answer is real
physics and is being tested by near-term observations.

The honest framing in the article's terms: GRUT is a specific
candidate for the "new physics beyond ΛCDM" that Riess hints at,
but currently GRUT is closer to the ΛCDM prediction than to SH0ES.
If SH0ES is right, GRUT needs adjustment. If Planck is right, GRUT
is already close.

Let future measurements decide.
