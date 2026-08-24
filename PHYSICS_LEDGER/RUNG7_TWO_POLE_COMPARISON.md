# RUNG7_W3 — two-pole reproduction + the single-pole discriminator

**Date:** 2026-08-23 · PHYSICS_LEDGER · JSON: `RUNG7_TWO_POLE_COMPARISON.json` (authoritative).
No claims.json edit. No banking. Not classified as GRUT success/failure.

## Outcome classification: **C+D**

- **C:** crossing/non-crossing depends on an additional restriction — but the restriction is
  **relaxational one-signedness (absence of a second, oscillatory dynamical mode)**, not single-pole.
- **D (reframed):** the registered derivation's no-crossing is **NOT single-pole-dependent**;
  it is channel/mode-dependent. `rung7_w2`'s own sub_status ("a single passive channel") is
  **correct**, and pole count is decorative for this observable.

## Literature expectation (NO_GO_LEDGER entry 3, Vikman 2005)

A single passive relaxor cannot cross w=−1; crossing needs ≥2 modes / **oscillatory poles** /
active response. **REPRODUCTION / CONSISTENCY WITH CITED RESULT:** obtained below — not a discovery.

## Results (emitted from JSON; criterion frozen pre-scan: TRUE CROSSING iff sign change persists at 4× refinement; band ω=aH(a), a∈[0.02,1] ⇒ ω∈[1.0,3.87]; Ω_M=0.3, Ω_Λ=0.7)

| kernel | passive | KK | elastic framing | dissipative framing |
|---|---|---|---|---|
| single-pole Debye (control) | yes | yes | APPROACH WITHOUT CROSSING | APPROACH |
| two REAL poles | yes | yes | APPROACH WITHOUT CROSSING | APPROACH |
| damped OSCILLATORY pair (γ=0.5,Ω=2) | yes | yes | **TRUE CROSSING** | APPROACH |
| one-channel NON-Debye Cole–Cole (α=0.6) | yes | yes | APPROACH WITHOUT CROSSING | APPROACH |
| three REAL poles (control) | yes | yes | APPROACH WITHOUT CROSSING | APPROACH |
| PLANT corrupted sign | FAILS passivity gate | — | rejected by runner | rejected |

## The discriminator table (§7 PRIOR answered)

| property varied | kernel | crosses? |
|---|---|---|
| pole count up, still pure relaxation | two/three REAL poles | **no** |
| one channel, NOT single-pole | Cole–Cole α<1 | **no** |
| genuine second mode with oscillation | complex-conjugate pair | **YES** |

**The operative variable is the existence of a second dynamical mode with independent phase
(oscillation), not pole count and not single-pole structure.** Single-pole is decorative for
w=−1 crossing: every purely-relaxational kernel — Debye, multi-real-pole, branch-cut — stays on
one side of −1 under both framings.

## Derivation traces

**PASSIVITY-ONLY TRACE:** Π = −ζ(ω)·3H with ζ≥0 (second law) ⇒ (w+1)=Π/ρ has ONE SIGN ∀z ⇒ no
crossing. Uses: passivity + one-signed response. No spectral shape anywhere.

**SINGLE-POLE-DEPENDENT TRACE:** none exists in the registered derivation — `calc/wz_sign.py`
uses w(a)=−1±ε·H/H₀, never invoking χ's spectral form. The proof never needs the pole.

**Where single-pole WOULD enter:** only if one required the correction to have the specific
Debye frequency profile — an extra commitment beyond what no-crossing uses.

## Relation to Vikman / rung8

- Vikman confirmed within GRUT's own map: crossing requires oscillatory poles or active response.
  GRUT-specific refinement: even multi-pole does NOT suffice if all poles are real/relaxational.
- Rung8 relation: the earlier H₀τ bound remains labelled *quantified for the stated
  single-scale/Debye model*. The two-band question now has a sharpened answer path: oscillatory
  modes evade the one-signedness obstruction by construction, so rung8 suppression analysis must be
  redone per mode before any generic claim. NOT assumed generic; OPEN.

## Runner strength

Controls planted: non-crossing single-pole recovered · constructed crossing (oscillatory)
recovered · non-crossing multi-pole recovered · corrupted sign correctly REJECTED by passivity
gate. Runner labels PASS (not WEAK): recovers both signs of the answer and rejects the plant.

## Implementation notes (honesty log)

Two defects caught during this run by the gates themselves: an inconsistent sign convention between
kernel implementations (caught by the passivity gate) and an oscillator whose flip frequency sat
outside the probed band (caught by checking band coverage). Both fixed before interpretation;
neither was tuned toward the expected answer — crossing parameters chosen from band arithmetic,
not from scanning toward a crossing.