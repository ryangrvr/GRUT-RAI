# Schrödinger-in-the-Box — BMV/KTM comparison (Stage 2)

**Status:** Stage 2 complete. Stage 3 (registry-language drafting) pending review.
**Started:** 2026-04-28.

**Investigation context:** The Schrödinger-in-the-Box brief proposes a
Λ_grav-rate prediction for gravitational entanglement formation,
flagged as the testable claim distinguishing GRUT-with-entanglement
from standard environmental decoherence. Stage 1 found that the
framework's existing `lambda_grav_bell` infrastructure already
computes this rate. Stage 2 asks: is GRUT's prediction
operationally distinguishable from Bose-Marletto-Vedral (2017) and
Kafri-Taylor-Milburn (2014) in measurable regimes?

**Pre-committed expectation (registered before computation):**
matches BMV in the regime where both apply; the screening function
S(l/R) might discriminate at small separations where l < ~1.82 R,
but that regime is experimentally inaccessible. Therefore
"anchored interpretation, worked-example value, not a novel
discriminating prediction."

---

## Stage 2 — numerical comparison at BMV-canonical parameters

Used existing framework infrastructure: `lambda_grav_single` from
`grut/derived/decoherence/entanglement.py`, `lambda_blackbody` and
`lambda_gas` from `grut/derived/decoherence/competition.py`. No new
infrastructure built.

### BMV canonical setup

- m = 10⁻¹⁴ kg (diamond microsphere, ρ ≈ 3500 kg/m³)
- R ≈ 0.88 μm (radius from m, ρ)
- l = 200 μm (separation between the two masses)
- l/R ≈ 227 → far-field regime, S(l/R) = 1

### Predicted entanglement formation timescale

| Framework | Λ_grav (Hz) | t_entangle (s) |
|:---|:---:|:---:|
| GRUT | 3.164 × 10⁻¹ | 3.16 |
| BMV literature ℏl/(Gm²) | 3.164 × 10⁻¹ | 3.16 |
| Ratio (GRUT/BMV) | **1.0000** | **identical** |

GRUT's prediction is **mathematically identical** to BMV's literature
formula at BMV-canonical parameters because S(l/R) = 1 reduces the
framework's Λ_grav = Gm²S(l/R)/(ℏl) to the point-mass form Gm²/(ℏl).

### Environmental decoherence at typical BMV operating conditions

At UHV pressure P = 10⁻¹³ Pa and cryogenic T = 10 mK:

| Channel | Λ_env (Hz) |
|:---|:---:|
| Λ_gas (residual gas scattering) | 4.85 |
| Λ_blackbody (300 K BB radiation) | ~10⁻²⁴ |
| Λ_grav (the signal) | 3.16 × 10⁻¹ |
| **Ratio Λ_grav / (Λ_gas + Λ_bb)** | **0.065** |

Even at UHV/cryogenic conditions, residual gas dominates by ~15×.
This is the well-known experimental challenge of BMV-class proposals:
the gravitational signal is suppressed by gas scattering unless
extreme isolation is achieved. Standard literature finding,
reproduced by the framework's existing competition infrastructure.

### Discriminator regime: where S(l/R) < 1 becomes measurable

GRUT's framework-specific signature is the screening factor
S(l/R) = min(1, (l/R)³/6). This drops below 1 when l < (6)^(1/3) × R
≈ 1.82 R. For BMV-canonical R = 0.88 μm, this means l < 1.6 μm.

Suppression scan at small l:

| l (μm) | l/R | S(l/R) | GRUT/BMV ratio |
|:---|:---:|:---:|:---:|
| 5.0 | 5.68 | 1.000 | 1.000 |
| 2.0 | 2.27 | 1.000 | 1.000 |
| **1.0** | **1.14** | **0.244** | **0.244** |
| **0.5** | **0.57** | **0.031** | **0.031** |

Below l ~ 1 μm, GRUT predicts the framework's entanglement-formation
rate is suppressed by factors 0.24 to 0.03 relative to BMV's
point-mass prediction. **This is the framework's specific
discriminating signature.**

### Why this regime is experimentally inaccessible

At l ~ 1 μm with masses ~ 10⁻¹⁴ kg:
- Casimir force scales as 1/l⁴ — at l = 1 μm, becomes large
- van der Waals contributes additionally
- Path-superposition techniques (Stern-Gerlach with NV-centers as
  in BMV) require much larger separations to maintain coherence
- Sticking, surface forces, and electromagnetic crosstalk dominate

The BMV experimental window (l ~ 100-300 μm) was specifically chosen
to avoid these complications. Pushing into the discriminator regime
would require fundamentally different experimental designs not
currently in the literature.

### Cross-reference to BMV 2017 / Kafri-Taylor-Milburn 2014

- **Bose et al. 2017 (PRL 119, 240401):** "Spin Entanglement Witness
  for Quantum Gravity." Proposed parameters m = 10⁻¹⁴ kg, l = 200 μm,
  t_entangle ~ ℏl/(GMm) ~ 3 s. Same formula as GRUT in far-field.
- **Marletto & Vedral 2017 (PRL 119, 240402):** Companion paper
  arguing entanglement formation requires quantum gravity. Same
  formula.
- **Kafri, Taylor, Milburn 2014 (NJP 16, 065020):** "A classical
  channel model for gravitational decoherence." Proposes GRUT-like
  classical-channel mechanism that would NOT entangle the masses.
  Distinguished from BMV by entanglement vs no-entanglement, NOT by
  rate. GRUT's framework predicts entanglement (state-dependent
  decoherence per F5), placing it on BMV's side of the KTM
  discrimination.

**Where GRUT sits in the literature triangle:**
- BMV: quantum gravity → entanglement at rate Λ_grav = Gm²/(ℏl)
- KTM: classical-channel gravity → no entanglement
- GRUT: state-dependent decoherence → entanglement at rate
  Λ_grav = Gm²S(l/R)/(ℏl) ≡ BMV in far-field

GRUT's prediction is operationally indistinguishable from BMV at
planned experimental scales. The framework lands on the same
prediction by independent reasoning (CTP noise kernel structure
rather than direct quantum-gravity assumption).

---

## Stage 2 — honest verdict

**At measurable BMV-class experimental scales, GRUT's gravitational
entanglement formation rate is identical to BMV's prediction.** The
framework's specific signature (screening factor S(l/R) < 1) emerges
only at l ≲ 1.82 R, which is below practical experimental
separations.

This confirms the pre-committed expectation: the Schrödinger-in-the-
Box formulation adds **anchored interpretation and worked-example
value**, not novel discriminating physics. The framework lands on
BMV's prediction by independent reasoning (CTP noise kernel
structure), giving it conceptual independence from BMV's
quantum-gravity-assumption framing without producing experimentally
distinct claims.

**Discriminator window — flagged for future experimental design:**
At l = 1 μm with m = 10⁻¹⁴ kg, GRUT predicts factor 0.24 suppression
relative to BMV. At l = 0.5 μm, factor 0.031. If a BMV-class
experiment can be designed at sub-micron separations (overcoming
Casimir, vdW, surface-force constraints), the screening factor
becomes the framework's GRUT-vs-BMV discriminator. This is not
practical with current literature proposals but worth noting as a
long-term experimental target.

---

## Direction for Stage 3 — registry-language drafting

Per the user's pre-committed structure (and now confirmed by Stage 2):

- **`schrodinger_in_box_inversion`** (Ch 11, anchored) — the
  philosophical inversion (observer is boxed, cat continues outside
  observer's information horizon, Bayesian filtering equation
  dp/dt = −μp − γp(1−p) with reset at contact). The Bayesian Layer
  is genuinely new content; the entanglement-locking inversion is
  re-narrativization of `measurement_resolution` applied to the
  Schrödinger-cat scenario.
- **`gravitational_entanglement_formation_rate`** (Ch 5, anchored) —
  explicit framing of what `lambda_grav_bell` already computes as
  "formation rate" alongside the existing F5 "protection rate"
  framing. Connects framework to BMV-class experimental program.
  Anchored because the formation rate is identical to BMV in
  measurable regimes; the only discriminator (S(l/R) < 1) is
  experimentally inaccessible with current designs. **Closure
  condition for tier promotion: sub-micron BMV-class experiment
  reaching the S(l/R) discriminator regime.**
- **`wigner_friend_dissolution`** (Ch 11, anchored) — worked example
  of `measurement_resolution` applied to multi-observer paradox.
  No new physics; explicit application of existing principles.

All three anchored. No computed-tier or scoping-tier additions
warranted by Stage 2. The brief's Bayesian filtering equation is the
single piece of genuinely new content, framed as anchored
interpretation.

Pausing for review.
