# Genesis-BBN-DM Hypothesis — Research Log (NOT framework content)

**Status:** External research hypothesis under investigation. The
framework remains UNCOMMITTED to this narrative. This log documents
what's been tested, what remains untested, and what specific gaps
each piece has. Per the framework's discipline pattern, no piece of
this narrative is registered as framework content unless and until
it survives forward derivation.

**Started:** 2026-04-28.

---

## The hypothesis

A research narrative connecting GRUT's foundational components
(noise kernel, constitutive equation, T_c crossing, dielectric DM)
into a unified cosmological history:

1. **Spark — Genesis Instability.** The CTP noise kernel ξ(t) makes
   the null state z = 0 unstable. Quantum fluctuations away from
   zero are dissipated by constitutive friction, converting
   metric-fluctuation kinetic energy into thermal radiation. The
   heat of the Big Bang is the friction-burn of the universe
   tearing itself out of nothingness.

2. **Buffer — BBN Thermal Plateau.** Once filled with hot plasma,
   the universe begins to expand and cool. But nuclear fusion
   (BBN) releases binding energy at a rate matching the expansion
   cooling rate, creating a thermal plateau at T ≫ T_c.

3. **Catalyst — Density Drop and Freeze-out.** As expansion
   continues, particle density drops below the threshold needed
   for fusion. The reactor shuts down. Without binding-energy
   injection, temperature crashes through T_c. The vacuum
   crystallizes, gravity lags, and dark matter is born.

4. **Dielectric DM Activation.** At T_c crossing, the constitutive
   medium acquires its bandwidth. The refractive enhancement
   n_g² − 1 = α/3 turns on. What we observe as dark matter is the
   crystallized viscoelastic wake of the vacuum responding to
   stress-energy.

The narrative is qualitatively beautiful. The framework's discipline
asks: which pieces survive forward derivation, and which don't?

---

## Piece-by-piece status

### Claim 1 — CTP noise kernel produces primordial heat

**Status: STRUCTURALLY WRONG at spectrum-shape level (2026-04-28).**

**What was tested:**
`grut/derived/cosmology/genesis_noise_kernel.py` — forward
derivation of the spectral density produced by the framework's
KMS noise kernel applied to the linearized OU process around
z = 0. Cross-verified against existing `fdt_noise` infrastructure
(rel_diff = 0 across tested regimes).

**Result at T = 0 (pure quantum vacuum):**

S_h(ω) = (2ℏ/τ_0) × ω/(1+(ωτ_0)²)
       = Lorentzian-modulated linear, NOT Planck/Bose-Einstein

**The shape is structurally non-thermal.** No temperature T makes
S_h(ω, T=0) coincide with the Planck distribution
ω³/(exp(ℏω/k_BT)-1) at any T.

**Characteristic temperatures extractable** (each a distinct
definitional choice the framework hasn't pinned):

| Definition | Value | vs CMB |
|:---|:---:|:---:|
| Spectral peak ℏω_peak/k_B | 5.78×10⁻²⁷ K | 27 orders too cold |
| Planck UV cutoff | 1.4×10³² K | 32 orders too hot |
| Equipartition heuristic | ~10⁻³¹ K | 31 orders too cold |
| Observed CMB | 2.725 K | reference |

**None match CMB.** The framework's noise kernel alone cannot
derive observed CMB temperature.

**Connection to T_c provenance audit (#15) — NOT a resolution:**
the spectral-peak value 5.78×10⁻²⁷ K coincides numerically with
the SI-correct T_c value identified in the audit (codebase
reports T_c = 54.7 MK with missing factor of ℏ). The same
scale appears here as a different physical quantity (spectral
peak vs claimed phase boundary). The audit's question remains
unresolved.

**Pre-commitment:** "the natural temperature scale will likely
be either Planck-scale (absurdly hot) or 1/τ_0-scale (absurdly
cold) — same kind of multi-scale ambiguity that's been surfacing
throughout. The honest outcome is probably 'definite calculation
that requires choices the framework hasn't pinned' rather than
'produces observed CMB temperature cleanly.'" The actual result
matches: definite spectrum (Lorentzian × linear, not thermal),
multiple T extractions possible, none match CMB.

**Implication for the broader narrative:** Genesis Claim 1's
"thermal radiation" framing is structurally wrong. The framework
needs either:
- Self-consistent equilibrium structure (model of metric
  fluctuations radiating into a thermalized field with T set by
  energy balance) — research-tier addition the framework currently
  lacks
- Different mechanism entirely for primordial heat
- Acknowledgment that primordial T is observation-anchored input

**Registered:** `genesis_noise_kernel_spectral_attempt` (Ch 12,
anchored).

### Claim 2 — BBN thermal buffer

**Status: FALSIFIED (2026-04-28).**

**What was tested:**
`grut/derived/cosmology/bbn_thermal_buffer.py` —
standard-cosmology calculation testing whether BBN
binding-energy release significantly buffers cosmic
expansion cooling. Three independent comparisons
(per-baryon, energy density, rate). All gave consistent
result.

**Result:** Outcome (iii) — NEGLIGIBLE BUFFER EFFECT.

| Comparison | Ratio | Interpretation |
|:---|:---:|:---|
| Per-baryon (binding/radiation) | 4.0×10⁻⁹ | Negligible |
| Energy density (E_bind/ρ_rad) | 2.4×10⁻⁹ | Negligible |
| Rate (injection/cooling, 1000 s window) | 1.6×10⁻¹⁰ | Negligible |

**Why it failed:** η_B-suppression. Baryons are 1.6×10⁹ times
rarer than photons. Even if every baryon's full BBN binding
energy (1.75 MeV) were dumped instantaneously into the
radiation field, T would change by only ~10⁻⁹. The radiation
field is too vast for binding energy to meaningfully heat
or buffer it.

**Pre-commitment:** Outcome (ii) cooling-slowed-not-plateaued
was registered as the expected outcome before computation.
The actual result is materially different by ~10 orders of
magnitude. The discipline pattern operated correctly: three
independent comparisons all give the same answer; the
hypothesis claim is quantitatively wrong, not just imprecise.

**Implication for the broader narrative:** The "wait until BBN
ends for crystallization" framing in Claim 3 cannot rely on
binding-energy buffering. BBN does not slow cosmic cooling
meaningfully. The narrative needs a different mechanism, or
the BBN-trigger framing needs to be dropped.

**Registered:** `bbn_thermal_buffer_negligible` (Ch 12,
anchored).

### Claim 3 — BBN cessation triggers T_c crossing

**Status:** BLOCKED + FALSIFIED PRECONDITION.

**Two independent issues:**

(a) **Pre-condition falsified.** The narrative posited BBN
binding energy as the mechanism keeping T ≫ T_c. Claim 2's
falsification removes this mechanism. Without binding-energy
buffering, there's no reason for cosmic temperature to be
"held above T_c" during BBN — temperature evolves as
T ∝ a⁻¹ throughout, with binding-energy injection a
~10⁻⁹ perturbation.

(b) **T_c provenance unresolved.** The narrative requires
T_c at MK scale (~4.7 keV, "1 hour post-BB"). The
framework's T_c via the canonical formula
T_c = ℏ/(τ_0 k_B) using τ_0 = 41.9 Myr gives 5.78×10⁻²⁷ K
— far below CMB. Until
`t_c_provenance_inconsistency_open_negative` (#15) resolves
through τ_micro formalization, the precise T_c value is
under audit.

**Closure path:** Even if (b) resolves with T_c at MK scale,
(a) requires a different mechanism than binding-energy
buffering for the "T held above T_c during BBN" picture
to work. Possible alternatives: cosmic expansion delay,
non-trivial g_*(T) dynamics during e⁺e⁻ annihilation,
some other thermal physics. Untested.

### Claim 4 — Dielectric DM activation at T_c crossing

**Status:** STRUCTURAL ADDITION REQUIRED.

**What's needed:** A calculation showing that the dielectric
refractive enhancement (n_g² − 1 = α/3) is suppressed above
T_c and active below. The framework currently treats Λ_grav
and τ_0 as constants; the bandwidth integral gives
Ω_dm,eff = α regardless of cosmic temperature.

**Risk:** The framework's existing infrastructure does not
naturally produce temperature-dependent dielectric activation.
Ch 4's regime classification X = max(ω, Λ_grav) × τ is a
FREQUENCY classification, not a TEMPERATURE classification.
For "dielectric DM turns on at T_c" to work, the framework
needs additional structure connecting cosmic temperature to
the medium's bandwidth response.

**Closure path:** Theoretical work to formalize the
temperature-dependence of the constitutive coupling.
Connects to the τ_micro question and to #9 covariance —
all three are aspects of cosmological-plasma physics the
framework has at scoping level but not formalized.

---

## Honest read on the narrative as a whole

Of the four claims:

- 1 untested, with specific scale-ambiguity risks
- 2 FALSIFIED by 10 orders of magnitude
- 3 doubly-blocked (pre-condition falsified + T_c unresolved)
- 4 requires structural addition not currently in framework

**The narrative as written does not survive forward derivation.**
Its load-bearing piece (Claim 2) is quantitatively wrong; its
trigger mechanism (Claim 3) is doubly-broken; its terminal
prediction (Claim 4) requires structure the framework lacks.

This is informative. The narrative's qualitative beauty
("universe crystallizes when nuclear furnace shuts down") does
not translate to quantitative physics in the framework's current
form. The framework is honest about this: each claim's status
is documented; the falsification of Claim 2 is registered as a
formal anchored claim; the broader narrative is logged as a
research direction, not adopted as framework content.

What CAN survive: pieces of the narrative might be reconstructible
under different mechanisms. For example, the "phase transition at
some specific cosmic temperature" picture could potentially work
if the relevant mechanism is e⁺e⁻ annihilation (which IS a real
g_*(T) discontinuity around T = 0.5 MeV, much closer to the
current T_c value of 54.7 MK = 4.7 keV). Or some other thermal
physics. But "BBN binding energy as buffer" is dead.

## What this log is NOT

- NOT framework content. None of these claims are registered as
  framework predictions.
- NOT a roadmap. The closure paths named are speculative; whether
  they close depends on future work and on resolving upstream
  open negatives.
- NOT a critique of the narrative's qualitative shape. The
  "nothing → fluctuation → friction → heat → crystallization"
  picture is coherent at the qualitative level. The quantitative
  pieces are what's been tested.

## What this log IS

- A documented research direction with specific testable claims.
- A record of which pieces have been forward-derived (Claim 2,
  falsified) and which remain untested.
- A connection point between the broader narrative and the
  framework's already-registered open negatives (#9 covariance,
  #15 T_c provenance).
- An example of the framework's discipline pattern operating on
  externally-suggested narratives: pre-commit, compute, follow
  the math, register honestly.

---

## End of log

**Last updated:** 2026-04-28 (Claim 1 spectrum-shape falsification
recorded, Claim 2 falsification recorded earlier same date).

**Status snapshot (2026-04-28):**
- Claim 1: STRUCTURALLY WRONG (spectrum is Lorentzian × ω, not
  Planck/Bose-Einstein); registered as
  `genesis_noise_kernel_spectral_attempt`
- Claim 2: FALSIFIED (BBN binding energy at 10⁻⁹ of radiation
  budget); registered as `bbn_thermal_buffer_negligible`
- Claim 3: DOUBLY-BLOCKED (precondition Claim 2 falsified;
  T_c provenance unresolved at #15)
- Claim 4: STRUCTURAL ADDITION REQUIRED (no T-dependent dielectric
  activation in framework; structurally untested)

Two of four narrative claims are closed negative. The narrative as
written does not survive forward derivation.

**Next reviewable update:** When Claims 3 or 4 receive forward-
derivation work, OR when the upstream open negatives (#9 or #15)
close in ways that affect this narrative.
