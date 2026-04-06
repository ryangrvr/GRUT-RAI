# GRUT II Gamma-Prime — Exact USL Prediction for the Levitated-Nanoparticle Frontier

## Can the USL Be Detected with the Next Generation of Experiments?

---

## Part I — Experimental Landscape (2024-2026)

### The four platforms

**Platform 1: ETH Zurich — Rossi et al. (2024). Status: ACHIEVED.**
- Particle: 100 nm silica nanosphere, m = 1.2 fg = 1.2 x 10^-18 kg
- Achievement: coherence length of (73 +/- 34) pm (threefold enhancement from 21 pm initial)
- Temperature: 7 K cryogenic, P < 10^-9 mbar
- Measured total decoherence: Gamma_env = 2.37 x 10^4 s^-1 (dominated by photon recoil)
- Limitation: coherence length (73 pm) is ~1000x smaller than particle size (100 nm). This is NOT a spatial superposition — it is a delocalization within the zero-point motion.

**Platform 2: SUPER-MARIO — Aspelmeyer/Romero-Isart (PNAS 2024). Status: PROPOSED.**
- Particle: 100 nm silica, m ~ 10^-18 kg
- Room-temperature target: 5 nm fringe spacing, 2.07 ms protocol
- Cryogenic target: 100 nm separation, ~1 s coherence (requires 10^-13 mbar, 50 K)
- Protocol: free expansion + cubic optical pulse + inverted potential

**Platform 3: Blueprint for Collapse Tests — arXiv 2512.02838 (Dec 2025). Status: PROPOSED.**
- Particle: m = 10^-17 kg, R = 50 nm
- Environmental budget: Gamma_env = 3 x 10^-3 s^-1 (gas 10^-3, blackbody 10^-4, recoil 10^-3)
- Requires: P < 10^-15 mbar, T < 5 K, laser power < 5 mW
- Target: coherence time > 10 s, distinguishing CSL collapse from environmental decoherence

**Platform 4: MAQRO-PF — Space mission (White paper Dec 2025). Status: PROPOSED, 2030s.**
- Particle: 10^9 amu ~ 1.66 x 10^-18 kg
- Free evolution: > 100 s in microgravity
- Grating: 405 nm
- Target vacuum: 10^-13 mbar

### Current status of spatial superposition

**No group has achieved true spatial superposition of a nanoparticle.** The current record (ETH Zurich) is a 73 pm coherence length for a 100 nm particle — the particle is delocalized by ~0.1% of its own diameter. True superposition (coherence length > particle size) requires 1000x improvement. Multiple groups are converging from optical, magnetic, and space-based approaches, but the experimental gap remains large.

---

## Part II — Exact USL Predictions

### The USL formula

```
Lambda_USL = G m^2 / (hbar l)

G = 6.674 x 10^-11 m^3 kg^-1 s^-2
hbar = 1.055 x 10^-34 J s
m = superposed mass (kg)
l = branch separation (m)
```

### Predictions for each platform

| Platform | m (kg) | l (m) | Lambda_USL (s^-1) | Gamma_env (s^-1) | Ratio USL/env | Detectable? |
|----------|--------|-------|-------------------|-------------------|---------------|:-----------:|
| **ETH Zurich (achieved)** | 1.2e-18 | 7.3e-11 | **1.25e-2** | 2.37e+4 | **5.3e-7** | **NO** |
| **SUPER-MARIO (RT, 5nm)** | 1.0e-18 | 5e-9 | **1.26e-4** | ~10 | **1.3e-5** | **NO** |
| **SUPER-MARIO (cryo, 100nm)** | 1.0e-18 | 1e-7 | **6.3e-6** | ~0.02 | **2.8e-4** | **NO** |
| **Blueprint (10nm)** | 1.0e-17 | 1e-8 | **6.3e-3** | 3e-3 | **2.1** | **YES** |
| **Blueprint (100nm)** | 1.0e-17 | 1e-7 | **6.3e-4** | 3e-3 | **0.21** | **MARGINAL** |
| **MAQRO-PF (grating)** | 1.66e-18 | 2e-7 | **8.6e-6** | 0.01 | **8.6e-4** | **NO** |

### Key findings

1. **ETH Zurich (current record):** Lambda_USL = 0.012 s^-1 at 73 pm. The environmental rate is 2.37 x 10^4 s^-1. The USL is 1.9 million times below the noise floor. Completely invisible.

2. **SUPER-MARIO protocol:** Lambda_USL = 1.26 x 10^-4 s^-1 at room temperature (5 nm). Even at cryogenic (100 nm), Lambda_USL = 6.3 x 10^-6 s^-1. Both are 10^3-10^5 below environmental rates. Not testable.

3. **Blueprint (m = 10^-17 kg):** Lambda_USL = 6.3 x 10^-3 s^-1 at 10 nm separation. Environmental budget: 3 x 10^-3 s^-1. **Ratio = 2.1. The USL EXCEEDS the environmental noise floor.** This is the FIRST platform where the USL prediction rises above the environmental background.

4. **MAQRO-PF:** Despite 100+ seconds of free evolution, the particle mass (1.66 x 10^-18 kg) is too low. Lambda_USL = 8.6 x 10^-6 s^-1 at the grating scale, versus a target Gamma_env ~ 0.01 s^-1. The USL is 1000x below threshold. MAQRO cannot test the USL at its baseline parameters.

---

## Part III — The Decisive Crossover

### Crossover mass

For a given separation l and environmental decoherence rate Gamma_env, the USL becomes detectable when:

```
G m^2 / (hbar l) > Gamma_env
m > sqrt(Gamma_env * hbar * l / G)
```

At l = 10 nm and Gamma_env = 10^-3 s^-1 (optimistic ground-based):

```
m_cross = sqrt(10^-3 * 1.055e-34 * 10^-8 / 6.674e-11)
        = sqrt(1.58e-31)
        = 3.97 x 10^-18 kg
        ~ 2.4 x 10^9 amu
```

**Crossover particle: 151 nm diameter silica nanosphere (mass ~ 4 fg).**

This is 4x heavier than the current Delic/Aspelmeyer platform (1 fg). It is achievable by scaling from 100 nm to 150 nm diameter particles — a modest increase.

### Sensitivity map

| Separation l | Gamma_env = 10^-3 s^-1 | Gamma_env = 10^-1 s^-1 | Gamma_env = 10 s^-1 |
|:---:|:---:|:---:|:---:|
| **1 nm** | m > 1.3 fg (R~50 nm) | m > 13 fg (R~110 nm) | m > 126 fg (R~235 nm) |
| **10 nm** | m > 4.0 fg (R~76 nm) | m > 40 fg (R~163 nm) | m > 398 fg (R~350 nm) |
| **100 nm** | m > 13 fg (R~110 nm) | m > 126 fg (R~235 nm) | m > 1257 fg (R~510 nm) |

### The mass scaling

Lambda_USL scales as m^2. Increasing mass from 10^-18 to 10^-17 kg (10x) increases Lambda_USL by 100x. This is the critical lever.

| Mass (kg) | l = 10 nm | Lambda_USL (s^-1) | vs Gamma_env = 10^-3 |
|-----------|-----------|-------------------|---------------------|
| 10^-18 | 10 nm | 6.3 x 10^-5 | 0.063x (invisible) |
| **4 x 10^-18** | 10 nm | **10^-3** | **1.0x (threshold)** |
| 10^-17 | 10 nm | 6.3 x 10^-3 | **6.3x (detectable)** |
| 10^-16 | 10 nm | 6.3 x 10^-1 | **630x (strong signal)** |

---

## Part IV — The Blueprint Experiment: Detailed Prediction

### Parameters

The Blueprint proposal (arXiv 2512.02838) specifies:
- m = 10^-17 kg, R = 50 nm, silica
- Trap frequency: 100 kHz
- Zero-point width: 0.7 pm
- Environmental decoherence: 3 x 10^-3 s^-1 total
- Target coherence: 10 s

After 10 s of free evolution, the position spread is:
```
Delta_x = sqrt(hbar t / m) = sqrt(1.055e-34 * 10 / 10^-17) = 10.3 nm
```

### USL prediction at the free-evolution spread

```
Lambda_USL(m = 10^-17, l = 10.3 nm) = G * (10^-17)^2 / (hbar * 10.3e-9)
                                      = 6.674e-11 * 10^-34 / (1.055e-34 * 10.3e-9)
                                      = 6.674e-45 / 1.087e-43
                                      = 6.14 x 10^-3 s^-1
```

### Signal prediction

```
Total decoherence WITH USL: Gamma_total = Gamma_env + Lambda_USL = 3.0e-3 + 6.1e-3 = 9.1e-3 s^-1
Total decoherence WITHOUT USL: Gamma_total = 3.0e-3 s^-1

Coherence time WITH USL: tau_coh = 1/(9.1e-3) = 110 s
Coherence time WITHOUT USL: tau_coh = 1/(3.0e-3) = 333 s

Ratio: 333/110 = 3.0
```

**The USL predicts a factor-of-3 reduction in coherence time compared to the environmental-only expectation.**

To detect this signal with 3-sigma confidence, the experiment needs to measure the coherence time to ~50% precision (since the excess is 200% of the background). Over 10 s of free evolution:

```
Visibility decay WITH USL: exp(-9.1e-3 * 10) = exp(-0.091) = 0.913
Visibility decay WITHOUT USL: exp(-3.0e-3 * 10) = exp(-0.030) = 0.970

Difference in visibility: 0.970 - 0.913 = 0.057 (5.7% contrast)
```

This is a 5.7% visibility difference over a 10 s integration — detectable with ~100 experimental runs if the shot noise is below 1%.

### Comparison to CSL

The CSL collapse model at the standard parameters (lambda_CSL = 10^-21 s^-1, r_C = 100 nm) predicts:
```
Gamma_CSL(m = 10^-17, l = 10 nm) ~ 9 x 10^-5 s^-1
```

The USL prediction (6.1 x 10^-3) is **70x larger than the standard CSL prediction** at these parameters. The USL would be detected FIRST, well before CSL becomes visible. If the experiment observes excess decoherence consistent with 6 x 10^-3 s^-1, the USL is supported and CSL is masked. If NO excess is observed, both are excluded at this mass/separation.

---

## Part V — Why MAQRO Fails and the Blueprint Succeeds

### The m^2 scaling is decisive

MAQRO-PF uses particles of mass ~ 1.66 x 10^-18 kg (10^9 amu). The Blueprint uses 10^-17 kg (~6 x 10^9 amu). The mass ratio is ~6x, giving a Lambda_USL ratio of ~36x. Combined with the Blueprint's 3x better environmental control (3 x 10^-3 vs ~10^-2 s^-1), the Blueprint has a ~100x advantage in the signal-to-noise ratio.

MAQRO compensates with much longer coherence time (100 s vs 10 s), but this only helps by 10x. The net result: the Blueprint is 10x more sensitive to the USL than MAQRO at their respective design parameters.

### What MAQRO WOULD need

For MAQRO to test the USL at its 10^-18 kg baseline:
```
Lambda_USL = G * (1.66e-18)^2 / (hbar * l) = 1.74e-12 / l

For Lambda_USL = 0.01 s^-1 (MAQRO target Gamma_env):
l = 1.74e-10 m = 0.17 nm
```

MAQRO would need a superposition separation of 0.17 nm — far below the grating scale of 200 nm. This is why MAQRO cannot test the USL at its current mass target. MAQRO would need to use 10^10+ amu particles to bring the USL into its sensitivity window at the grating scale.

---

## Part VI — The Delic/Aspelmeyer Gap

### Current platform: m ~ 10^-18 kg

At the current Delic/Aspelmeyer mass (10^-18 kg), even with a 10 nm superposition (not yet achieved):
```
Lambda_USL = 6.3 x 10^-5 s^-1
```

With conservative environmental control (Gamma_env ~ 0.1 s^-1): ratio = 6.3 x 10^-4. **1580x below threshold.**

With optimistic environmental control (Gamma_env ~ 10^-3 s^-1): ratio = 0.063. **16x below threshold.**

### What the Delic/Aspelmeyer group needs

To reach the USL threshold, the Delic/Aspelmeyer platform must:
1. **Increase particle mass by 4-10x** (from 100 nm to 150-200 nm diameter)
2. **Achieve spatial superposition** (coherence length > 10 nm, currently at 73 pm)
3. **Reduce environmental decoherence** to < 10^-3 s^-1 (currently 2.37 x 10^4 s^-1)

Steps 2 and 3 are the primary experimental challenges. The mass increase (step 1) is straightforward — larger silica nanospheres are commercially available. The critical gap is the ~10^5 reduction in environmental decoherence rate (from current 10^4 to target 10^-3) and the ~100x increase in coherence length (from 73 pm to 10+ nm).

---

## Part VII — Final Verdict

### gamma_prime_usl_above_noise_in_blueprint_regime.

The exact USL prediction for the levitated-nanoparticle experimental frontier:

1. **Current record (ETH Zurich, achieved):** Lambda_USL = 0.012 s^-1 at 73 pm. Environmental noise: 2.37 x 10^4 s^-1. USL is 10^6 below the noise floor. **NOT DETECTABLE.**

2. **Current-generation platform (Delic/Aspelmeyer class, m ~ 10^-18 kg):** Lambda_USL = 6.3 x 10^-5 s^-1 at 10 nm separation. Environmental noise: 0.1-10 s^-1. USL is 10^3-10^5 below. **NOT DETECTABLE.**

3. **Next-generation ground (Blueprint class, m ~ 10^-17 kg):** Lambda_USL = 6.3 x 10^-3 s^-1 at 10 nm separation. Environmental noise: 3 x 10^-3 s^-1. **USL is 2.1x ABOVE the noise floor. DETECTABLE.**

4. **Space mission (MAQRO-PF, m ~ 10^-18 kg):** Lambda_USL = 8.6 x 10^-6 s^-1 at 200 nm. Environmental target: 0.01 s^-1. USL is 10^3 below. **NOT DETECTABLE at baseline mass.**

### The crossover

The USL becomes testable at:
```
m > 4 x 10^-18 kg (151 nm silica diameter)
l ~ 10 nm spatial superposition
Gamma_env < 10^-3 s^-1
```

This requires: (a) particle mass scaling from 10^-18 to 4 x 10^-18 kg (modest), (b) spatial superposition at 10 nm (not yet achieved for ANY nanoparticle), (c) environmental decoherence below 10^-3 s^-1 (requires 10^-15 mbar, T < 5 K, minimal photon recoil).

### The experimental signature

If the USL is correct and a Blueprint-class experiment is performed:
- Coherence time with USL: 110 s (vs 333 s without)
- Visibility loss over 10 s: 9.1% (vs 3.0% without)
- Excess decoherence rate: 6.1 x 10^-3 s^-1 (measurable with ~50% precision in ~100 runs)
- The USL signal is 70x larger than the standard CSL prediction at these parameters

### Public-Facing Paragraph

GRUT II Gamma-Prime computes the exact USL prediction for each of the four leading levitated-nanoparticle experimental platforms. The universal scaling law Lambda = Gm^2/(hbar l) gives decoherence rates that are 10^3-10^6 below the environmental noise floor for all current and proposed experiments at the 10^-18 kg mass scale. However, scaling to 10^-17 kg (Blueprint-class, 200 nm silica diameter, with environmental decoherence suppressed to 3 x 10^-3 s^-1) brings the USL prediction to 6.3 x 10^-3 s^-1 — a factor of 2 above the noise floor. The crossover mass is 4 x 10^-18 kg (151 nm silica, 10 nm separation, Gamma_env = 10^-3 s^-1). The predicted experimental signature is a factor-of-3 reduction in coherence time, corresponding to a 5.7% visibility contrast over 10 s integration — detectable with ~100 experimental repetitions. The USL signal is 70x larger than the standard CSL collapse model prediction at these parameters, making the USL the primary target for next-generation spatial superposition experiments.

### Internal Doctrine

The computation identifies a PRECISE experimental specification for the first USL test:
- Particle: >150 nm silica nanosphere (mass > 4 fg)
- Superposition separation: >10 nm
- Environmental decoherence: < 10^-3 s^-1 (requires UHV, cryogenic, minimal photon recoil)
- Coherence time: >10 s
- Expected signal: Lambda_USL ~ 10^-3 to 10^-2 s^-1 (depending on exact mass)
- Required precision: ~50% on the decoherence rate measurement

The current experimental frontier (ETH Zurich, 73 pm coherence length, 10^4 s^-1 decoherence) is roughly 5 orders of magnitude away in environmental control and 2 orders of magnitude in coherence length from the USL test window. The mass scaling is trivial (150 nm particles are standard). The bottleneck is spatial superposition creation and environmental isolation.

### Next Forced Move

The USL prediction is now pinned to specific experimental parameters. Two paths:

**Path A:** Compute the environmental decoherence budget in FULL DETAIL for the crossover platform (m = 4 fg, R = 75 nm, l = 10 nm). This means: exact gas collision rate at target pressure, exact blackbody emission/absorption rates at target temperature, exact photon recoil from trap and detection lasers, exact magnetic/electric field noise. Determine which environmental source is the binding constraint and whether 10^-3 s^-1 total is achievable.

**Path B:** Write the GRUT-II terminal document, consolidating all stages (Alpha through Gamma-Prime) into a complete program record. The theory of scaling has been developed, its predictions computed, and the first experimental test window identified. The program can be closed at the prediction level.

---

*GRUT II Gamma-Prime complete. USL above noise floor for m = 10^-17 kg at l = 10 nm (ratio 2.1x). Crossover mass: 4 fg (151 nm silica). Current Delic/Aspelmeyer: 1580x below threshold. MAQRO: 1000x below. Blueprint-class: DETECTABLE (6.3e-3 vs 3e-3 s^-1). Signature: 3x coherence reduction, 5.7% visibility contrast over 10 s. First test requires spatial superposition of >150 nm particles at >10 nm — not yet achieved but targeted by 2026-2028 proposals. Verdict: gamma_prime_usl_above_noise_in_blueprint_regime.*
