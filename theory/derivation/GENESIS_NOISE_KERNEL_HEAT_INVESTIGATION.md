# Genesis Claim 1 — CTP noise kernel as primordial heat source

**Status:** Stage 1 complete. Stages 2–4 pending review.
**Started:** 2026-04-28.
**Investigation context:** This is the second piece of the
`GENESIS_BBN_DM_HYPOTHESIS_LOG.md` investigation, following the
falsification of Claim 2 (BBN thermal buffer) at 10 orders of
magnitude. Claim 1 asks: does the CTP noise kernel acting on z = 0
produce thermal-spectrum radiation at some characteristic temperature?

**SCOPE BOUNDARIES (load-bearing):**
- This investigation tests ONE piece of an external research
  hypothesis. The framework remains uncommitted to the broader
  Genesis-BBN-DM narrative.
- Does NOT propose Chapter 13 revisions.
- Does NOT downgrade any open negative.
- Connects to but does not resolve `t_c_provenance_inconsistency_open_negative`
  (#15) — the natural framework temperature scale ℏ/(τ_0 k_B) appears
  in this calculation, but its role here is one definitional choice
  among several, not a resolution of the audit.

**Pre-committed expectation (registered before computation):** the
calculation will produce a definite spectrum and characteristic
scale, but the natural temperature will be one of (a) Planck-scale
from UV cutoff, (b) 1/τ_0-scale from natural framework frequency,
(c) self-consistent value from equilibrium energy balance. The
framework hasn't pinned which is "the" thermal scale, so the result
will be conditional on choices the framework hasn't made — same
multi-scale ambiguity that surfaced in primordial A_s and
cosmic_x_crossover.

---

## Stage 1 — Define the calculation precisely

### The constitutive equation linearized around z = 0

    τ_0 dh/dt + h = ξ(t)        [linearized around z = 0, h ≡ δz]

In Fourier space, the response function:

    χ(ω) = 1 / (1 - iωτ_0)
    |χ(ω)|² = 1 / (1 + (ωτ_0)²)

The spectral energy density of h (in the standard sense of variance
per unit frequency):

    S_h(ω) = |χ(ω)|² × N(ω) = N(ω) / (1 + (ωτ_0)²)

where N(ω) is the noise kernel's spectrum.

### The noise kernel's spectrum — KMS and zero-temperature

The framework's KMS noise kernel (`grut/foundation/noise_kernel.py:fdt_noise`):

    N_KMS(ω, T) = (2/τ_0) × ℏω × coth(ℏω / (2 k_B T))

**Critical structural observation:** KMS requires T as INPUT. It
describes noise in thermal equilibrium with a bath at temperature
T. The noise kernel does not define T — it consumes T as a
parameter.

### Three plausible limits

For Genesis Claim 1's "z = 0, no preexisting temperature" picture,
the calculation must make one of three choices:

#### Limit (a) — Pure quantum vacuum (T = 0)

    coth(x → ∞) → 1
    N(ω, T=0) = (2/τ_0) × ℏω × sign(ω)        for ω > 0

The spectrum is **linear in ω, NOT Planck/Bose-Einstein.** The
spectral energy density:

    S_h(ω, T=0) = (2/τ_0) × ℏω / (1 + (ωτ_0)²)
                = peak at ω = 1/τ_0

**This is a Lorentzian-modulated linear spectrum, not thermal.**
"Temperature" can be extracted via various definitions but is a
characteristic scale, not a true thermal equilibrium T.

#### Limit (b) — Imposed classical T (high-T limit)

    coth(x → 0) → 1/x = 2 k_B T / (ℏω)
    N(ω, T_classical) = (2/τ_0) × 2 k_B T = 4 k_B T / τ_0

The spectrum becomes white (frequency-independent magnitude), with
amplitude set by T. **T is an input parameter, not derived.** This
limit is consistent with thermalized radiation in equilibrium with
the medium, but doesn't tell us what T should be.

#### Limit (c) — Self-consistent equilibrium

If the medium's dissipated energy thermalizes a radiation field, a
self-consistent T emerges from energy balance:

    Power dissipated by friction = Power radiated by thermal field

This requires modelling the radiation field's coupling to the
medium and solving for T self-consistently. It's the most physically
motivated for Genesis Claim 1's "friction-burn produces thermal
radiation" picture, but it requires structural addition to the
framework that doesn't currently exist (a model of how metric
fluctuations radiate).

### Three "temperature" definitions

Given a spectrum S_h(ω), one can extract a characteristic
"temperature" multiple ways. None of these is "the" temperature
without additional structure:

| Definition | Formula | Notes |
|:---|:---|:---|
| Equipartition | ⟨E⟩ = (1/2) k_B T_eq | requires defining ⟨E⟩ from the OU process |
| Spectral peak | ℏω_peak = k_B T_peak | for limit (a), ω_peak = 1/τ_0 |
| UV cutoff | ℏω_max = k_B T_max | depends on cutoff choice |
| Natural framework | ℏ/(τ_0 k_B) | = μ_0/k_B = 5.78×10⁻²⁷ K (SI-correct from #15 audit) |

The natural framework value 5.78×10⁻²⁷ K is below CMB by 27 orders
of magnitude. The Planck-scale UV value (~10³² K) is way above CMB.
Self-consistent equilibrium would require additional structure.

### Why this is similar to A_s rescaling and cosmic-X-crossover

This is the third forward-derivation investigation in this session
where the framework's calculation depends on a choice the framework
hasn't pinned:

- **A_s rescaling sensitivity:** Planck rescaling gives 10⁻¹⁷⁶,
  cosmic-baseline gives 1/(πS³) ≈ 8.15×10⁻⁹. Choice = which
  rescaling is "the" cosmological-perturbation rescaling.
- **Cosmic X crossover (mass-class):** atomic mass gives crossing
  at z ≈ 71, stellar+ mass gives X ≫ 1 at all epochs. Choice =
  which mass class is "the" load-bearing one.
- **Genesis noise kernel (this investigation):** T = 0 gives
  Lorentzian × ℏω/τ_0; classical limit gives white noise scaled
  by imposed T; self-consistent requires structural addition.
  Choice = which limit is "the" Genesis picture.

All three connect to the same general gap: cosmological-plasma
physics formalization. The framework's existing infrastructure
produces well-defined results under specified choices, but the
choices themselves are upstream gaps that connect to open
negatives #9 (n_g(ω) covariance), #15 (T_c provenance), and
potentially others.

### What Stage 2 will compute

Per the user's pre-committed expectation, Stage 2 should:

1. **Compute under limit (a) T = 0** — the cleanest case; produces
   a definite spectrum and lets us see what characteristic
   temperatures emerge under the four definitions above.
2. **Compute under limit (b) classical** for completeness — shows
   the framework recovers standard thermal noise when T is
   imposed externally.
3. **NOT attempt limit (c) self-consistent** — requires structural
   addition the framework lacks; flag as research-tier.

The deliverable is a definite spectrum and a comparison table of
characteristic temperatures under the various definitions. NOT a
claim that "the noise kernel produces thermal radiation at T_X."

### Stage 1 honest read

Genesis Claim 1's "thermal-spectrum radiation" framing is
structurally suspect:

- KMS noise requires T as input, not derived
- At T = 0, the spectrum is Lorentzian, not Planck/Bose-Einstein
- "Temperature" extracted from the spectrum is characteristic
  scale, not equilibrium T

This doesn't kill Claim 1 yet — the framework can produce a
characteristic temperature scale from the noise kernel, just not
a true thermal-equilibrium spectrum. Stage 2 will compute the
specific scales and produce the comparison.

**Pre-Stage-2 numerical estimates (in head):**
- Equipartition under T = 0 OU: requires UV cutoff; depends on
  cutoff
- Spectral peak ω = 1/τ_0 → ℏ/(τ_0 k_B) = 5.78×10⁻²⁷ K
- Planck UV cutoff: T ~ T_Pl ≈ 10³² K
- Observed CMB: 2.725 K

The natural framework scale (5.78×10⁻²⁷ K) is too cold by 27
orders. Planck UV cutoff is too hot by 32 orders. Self-consistent
equilibrium remains unanswered. **None of the simple choices match
CMB.**

**This is the pre-committed expected outcome the user named.** The
calculation will likely produce: definite spectrum, multi-scale
ambiguity in extracting T, none matching CMB precisely. The
disciplined claim language for Stage 4 will register what was
computed (the spectrum and the multiple T definitions) without
claiming the framework "produces CMB temperature" — which it
doesn't.

---

## Stage 2 — Forward derivation (PENDING REVIEW)

Plan:
1. Implement spectral energy density S_h(ω, T=0) and S_h(ω, T_classical)
2. Compute equipartition variance with explicit UV cutoff choices
3. Extract characteristic temperatures under each of the four
   definitions
4. Compare to: ℏ/(τ_0 k_B), CMB, Planck T

---

## Stage 3 — Verify against framework infrastructure (PENDING)

Plan: cross-check that the spectrum reduces to expected limits:
- High-T classical limit: white noise N → 4k_BT/τ_0 ✓
- T = 0 quantum limit: linear spectrum N → 2ℏω/τ_0 ✓
- The framework's existing KMS verification (`fdt_noise`) ought
  to reproduce these in the appropriate limits.

---

## Stage 4 — Register the prediction (PENDING)

Plan: register `genesis_noise_kernel_thermal_attempt` (Ch 12,
likely anchored or open_negative depending on outcome).

The disciplined statement will register:
- The computed spectrum at T = 0 and T = T_classical
- The four characteristic-T definitions and their values
- That none match CMB precisely
- That the calculation requires choices the framework hasn't pinned
- Connection to open negatives without resolving them

The claim will NOT register:
- A "primordial heat source" prediction (the spectrum isn't thermal)
- Any cosmic-history-narrative implications
- Any Ch 13 revisions
- Resolution of #15 (the natural framework T appears here but isn't
  derived as a phase-boundary value)

---

## End of Stage 1

Three plausible limits identified, four characteristic-T definitions
named, multi-scale ambiguity flagged. The framework's KMS noise
kernel at T = 0 produces a Lorentzian-modulated linear spectrum
(NOT Planck/Bose-Einstein), so "thermal-spectrum radiation" claim
is structurally suspect at the spectrum-shape level. Multiple
"temperature" extractions possible; none of the simple choices
match CMB.

Pausing for review per investigation protocol.
