# The Generic-Kernel Substitution Test — first results

**Date:** 2026-08-23 · PHYSICS_LEDGER (epoch-tagged at creation; fenced from prose corpus).
**Labels:** DERIVED FROM ESTABLISHED PHYSICS / DERIVED GIVEN GRUT ASSUMPTION / BORROWED /
OPEN / FALSIFIED / NUMERICALLY UNVERIFIED. No banking. No claims.json edit.

**H_GRUT:** the gravitational vacuum admits a causal, KMS-compatible responsive-medium
description with finite memory, in the strongest form single-pole.

## Admissible family (all causal, passive, KMS-compatible)

| kernel | χ(ω) | causality | verified |
|---|---|---|---|
| single-pole (Debye) | χ₀/(1−iωτ) | pole at −i/τ, lower half-plane | **sympy-verified** |
| two-pole | Σ wᵢχ₀/(1−iωτᵢ) | all poles lower half-plane | sympy-verified |
| multi-pole/continuum | ∫ ρ(τ)/(1−iωτ)dτ | lower half-plane if ρ≥0 | established |
| branch-cut/collisionless | Landau-damped χ | cut off imaginary axis | established (BORROWED) |
| Markovian limit | τ→0 ⇒ χ→χ₀ | trivially causal | **sympy-verified** |

Passivity: Im χ(ω>0) = χ₀ωτ/(ω²τ²+1) > 0 — positive-definite for χ₀,τ>0. KK analyticity holds for every member.

## The three-category sort

**Category 1 — needs only causality+passivity+KMS (GENERIC):**
- KK relations between Re χ and Im χ [DERIVED FROM ESTABLISHED PHYSICS]
- fluctuation–dissipation relation at finite T [BORROWED]
- retarded response vanishing for t<t′ [DERIVED FROM ESTABLISHED PHYSICS]
- passivity/no-exergy extraction bounds [DERIVED FROM ESTABLISHED PHYSICS]

**Category 2 — needs SOME finite memory (SEMI-GENERIC):**
- a characteristic crossover frequency ω_c ~ 1/τ in the susceptibility [DERIVED GIVEN GRUT ASSUMPTION for the value; the *existence* of some scale is generic to any non-Markovian kernel]
- frequency-dependent effective w(z) across cosmological epochs: requires χ varying between epochs — any kernel with τ spanning dark-energy band supplies it; two-pole and continuum do equally well [DERIVED GIVEN GRUT ASSUMPTION on τ placement]
- dephasing suppression of long-baseline interference at 22–62 orders: follows from τ_c ≪ baseline timescales; ANY short-memory kernel gives it [DERIVED FROM ESTABLISHED PHYSICS + measured scales]

**Category 3 — needs SINGLE POLE specifically (the actual wager): currently ONE candidate, unverified**
- rung7_w3 no-crossing export: the w(z) no-crossing property was derived using the monotonic single-pole structure. A two-pole kernel with competing relaxations can produce crossing effective-w curves. **Status: NUMERICALLY UNVERIFIED — this is the sharpest testable consequence of the wager and has not been computed against a two-pole rival.**
- rung3's "THE memory time": the free theory supplies a family; THE single-pole is an insertion, not a derivation [DERIVED GIVEN GRUT ASSUMPTION]

## rung8 sharpening — O(1) vs 10⁻⁷

Suppression derives from the ratio of memory time to the propagation timescale raised to a
positive power. An O(1) effect requires τ_mem comparable to the cosmological/horizon time.
But a horizon-scale memory time puts the crossover ω_c at H₀ — where observations of w ≈ −1
constrain frequency-dependent deviations. **Candidate no-go: O(1) rung8 effects and observed
dark-energy smoothness are in tension for ANY admissible kernel, not just single-pole.**
Status: superseded by the quantitative bound below.

## rung8 O(1) bound — QUANTITATIVE (the next calculation, done)

Single-scale kernel χ(ω)=χ₀/(1−iωτ); fractional Re-χ variation between ω=0 and ω=H₀:
δ(x)=(H₀τ)²/(1+(H₀τ)²), x≡H₀τ. Vacuum response feeding the dark-energy stress tensor gives
Δw ≥ c·δ (c = coupling > 0). Observed: |w+1| ≲ σ ≈ 0.06.
Solving c·x²/(1+x²)=σ ⇒ **H₀τ ≤ √(σ/(c−σ))**:

| coupling c | bound H₀τ ≤ | τ_max |
|---|---|---|
| 0.1 | 1.23 | ~18 Gyr (c≈σ degenerate; no constraint) |
| 0.5 | **0.37** | **~5.4 Gyr** |
| 1.0 | 0.25 | ~3.6 Gyr |

Consequences, labelled:

1. **Cosmological O(1) escape blocked unless c≲σ:** for order-unity coupling, horizon-scale
   memory forces Δw≳O(0.5), excluded at >8σ. [DERIVED GIVEN GRUT ASSUMPTION + EMPIRICALLY
   CONSTRAINED]
2. **The two-band no-go (new, sharper):** an O(1) effect requires τ_mem matched to the observation
   timescale of that channel; a single-τ kernel can match at most ONE band (lab O(1) needs
   τ≈T_lab; cosmological visibility needs τ~H₀⁻¹ — separated by ~17 orders).
   > For any single-scale admissible kernel, O(1) GRUT effects in two disjoint observational bands
   > are impossible. Observing O(1) anomalies in even two bands would refute single-scale memory
   > and REQUIRE multi-pole/continuum structure — refuting the single-pole wager from above.
   > Conversely, single-pole predicts O(1) in at most one band.
   [DERIVED GIVEN GRUT ASSUMPTION; NUMERICALLY UNVERIFIED at the two-band level]
3. **Residual escape routes, stated honestly:** (a) small coupling c<σ — proportionally suppresses
   every other GRUT signature including rung7; (b) τ in no observation band — no O(1) anywhere,
   architecture empirically idle. Neither yields an observable O(1) without abandoning either
   single-scale memory or detectability.

**Status: the generic no-go candidate survives quantitatively for single-scale kernels.**
Multi-band version OPEN pending numeric two-pole comparison. Not banked; NO_GO_LEDGER entry
requires owner adjudication.

## Where the ontological commitment first becomes necessary (rung3 trace)

1. SK influence functional exists — BORROWED (Schwinger/Keldysh/Feynman-Vernon)
2. Retarded kernel K_R well-defined per mode — BORROWED
3. Finite memory time τ_c appears — **INSERTION (the stance)** — everything upstream is generic
4. Single-pole relaxation shape — INSERTION (strongest form)
5. Everything downstream (rung4 bounds, rung7 map, rung8 falsifier) inherits from step 3–4.

**The exact line is between steps 2 and 3.** That is where derivation stops and ontology begins.

## Mirror-fence compliance

Category 2 survivals are reported as survivals, not softened toward failure; Category 3's near-
emptiness is reported without manufacturing a member. The one Category-3 candidate (no-crossing)
is flagged NUMERICALLY UNVERIFIED rather than claimed.

