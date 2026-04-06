# GRUT II Delta-Prime — Blueprint-Platform Environmental Budget and USL Testability Audit

## Purpose

Determine whether the Blueprint-class nanoparticle platform identified in Gamma-Prime remains a real test window for the Universal Scaling Law once a full environmental decoherence budget — computed channel by channel from published formulas — is included.

---

## Part I — Reference Platform Specification

One concrete, coherent target configuration:

| Parameter | Value | Source/Justification |
|-----------|-------|---------------------|
| Material | Amorphous silica (SiO2) | Standard in levitated optomechanics |
| Density | 2200 kg/m^3 | Literature value for fused silica |
| Diameter | 150 nm (R = 75 nm) | Gamma-Prime crossover size |
| Mass | 3.89 fg = 3.89 × 10^-18 kg | Computed from density and radius |
| Refractive index (optical) | 1.45 (eps = 2.10) | Standard |
| Clausius-Mossotti K | 0.269 | (eps-1)/(eps+2) |
| Branch separation l | 10 nm | Gamma-Prime target |
| Interrogation time | 10 s | Blueprint paper target |
| Shield temperature T_env | 4 K | Liquid helium cryostat |
| Internal temperature T_int | 20 K | Post-release radiative cooling |
| Residual gas pressure | 10^-13 Pa (10^-15 mbar) | Extreme UHV (cryopumped) |
| Gas species | N2 (residual) | Conservative assumption |
| Trapping | Optical, 1550 nm, 5 mW | Low-power telecom laser |
| Trap frequency | 100 kHz | Blueprint paper |
| Release protocol | Laser off → free fall | Dark free evolution |
| Readout | Position measurement (dark) | No laser during coherence |
| Residual charge | 0 elementary charges (target) | Charge neutralization required |
| Vibrational PSD | 10^-18 m^2/Hz | State-of-art cryogenic isolation |

**Classification:** This is an ASPIRATIONAL platform. No existing experiment meets all these specifications simultaneously. The individual parameters range from demonstrated (cryogenic temperature, particle fabrication) to undemonstrated (10 nm spatial superposition, 10 s free evolution, 10^-15 mbar).

---

## Part II — Full Environmental Decoherence Inventory

### USL prediction at reference parameters

```
Lambda_USL = G m^2 / (hbar l) = 6.674e-11 × (3.89e-18)^2 / (1.055e-34 × 10e-9)
           = 9.57 × 10^-4 s^-1
```

### Channel 1: Residual Gas Collisions

**Formula:** Hornberger-Sipe (2003), Joos-Zeh localization.

In the short-wavelength limit (l >> lambda_dB of gas, which applies here since l = 10 nm >> lambda_dB = 165 pm):

```
Lambda_gas = n_gas × sigma_geo × v_th
```

where:
- n_gas = P/(k_B T) = 10^-13 / (1.38e-23 × 4) = 1.81 × 10^9 m^-3
- sigma_geo = pi R^2 = pi × (75e-9)^2 = 1.77 × 10^-14 m^2
- v_th = sqrt(8 k_B T / (pi m_gas)) = 55.0 m/s (N2 at 4 K)

**Result:** Lambda_gas = **1.76 × 10^-3 s^-1**

**Confidence:** HIGH. Standard, experimentally validated formula. The short-wavelength regime (l/lambda_dB = 61) means every gas collision causes full decoherence — the rate equals the scattering rate.

**Status:** This is the DOMINANT channel. Lambda_gas alone is **1.84× larger than Lambda_USL**.

### Channel 2: Blackbody Emission (from particle)

**Formula:** Romero-Isart (2011). Thermal photon emission from a dielectric nanosphere at T_int.

```
N_emi = V × (2/pi^2) × Im{K_CM(omega)} × omega_th^4 × (pi^4/15) / c^3
D_pp^emi = N_emi × (2/3) × (hbar × omega_mean / c)^2
Lambda_emi = D_pp^emi × l^2 / hbar^2
```

At T_int = 20 K:
- Peak emission wavelength: 145 um (deep far-IR)
- Im{epsilon} at 145 um for silica: ~0.05 (far from 10 um Si-O band)
- Photon emission rate: ~36 s^-1
- But each photon carries very low momentum (lambda ~ 188 um >> l = 10 nm)
- Momentum kick per photon: hbar × omega / c ~ 3.5 × 10^-30 kg m/s

**Result:** Lambda_emi = **2.70 × 10^-6 s^-1**

**Confidence:** MODERATE. The Im{epsilon} of silica at 145 um is approximate (literature values range 0.01-0.1 depending on material quality and frequency). The T^7 scaling makes this very sensitive to T_int.

**Status:** Negligible. 350× below Lambda_USL.

### Channel 3: Blackbody Absorption (from environment)

**Formula:** Same as emission but with T_env = 4 K.

At T_env = 4 K: peak at 725 um. Im{epsilon} ~ 0.01. Much lower photon density.

**Result:** Lambda_abs = **3.46 × 10^-11 s^-1**

**Confidence:** MODERATE.

**Status:** Utterly negligible.

### Channel 4: Blackbody Rayleigh Scattering

**Formula:** Elastic scattering of environmental thermal photons.

```
sigma_sca(omega) = (8 pi/3) × (omega/c)^4 × R^6 × |K_CM|^2
```

At T_env = 4 K: thermal photon wavelengths ~ 700 um. Rayleigh cross section scales as omega^4, so it is extremely suppressed at long wavelengths.

**Result:** Lambda_sca = **5.88 × 10^-40 s^-1**

**Confidence:** HIGH (Rayleigh regime exact for R << lambda).

**Status:** Zero for all practical purposes.

### Channel 5: Trap-Laser Photon Recoil

**Formula:** Rayleigh scattering of 1550 nm trap photons.

During illumination:
```
sigma_Rayleigh = (128 pi^5/3) × R^6 / lambda^4 × K_CM^2 = 2.91 × 10^-17 m^2
Gamma_sc = 1.48 × 10^12 s^-1 (at 5 mW, diffraction-limited focus)
Lambda = D_pp × l^2 / hbar^2 = 1.63 × 10^9 s^-1
```

**This is catastrophic during illumination.** Every millisecond of laser exposure destroys coherence completely.

**Critical constraint:** The protocol MUST be fully dark during free evolution. No laser can illuminate the particle between release and readout.

**Result:**
- During illumination: 1.63 × 10^9 s^-1 (FATAL)
- Dark protocol: **0 s^-1**

**Confidence:** HIGH (Rayleigh scattering exact).

**Status:** Protocol design constraint, not a noise floor. Dark free-fall protocols eliminate this channel entirely. If ANY illumination occurs during the coherence interval — even 1 microsecond — the experiment fails.

### Channel 6: Electric/Charge Noise

**Formula:**
```
Lambda_charge = q^2 × S_E × l^2 / hbar^2
```

For 1 elementary charge and S_E = 10^-12 (V/m)^2/Hz (cryogenic environment):

**Result:**
- At 1e charge: Lambda_charge = **231 s^-1** (FATAL)
- At 0 charge: **0 s^-1**

**Confidence:** LOW-MODERATE. S_E depends strongly on electrode geometry, shield quality, distance to conductors. The 10^-12 value is a reasonable cryogenic estimate but could be better or worse by an order of magnitude.

**Status:** This is a **hard constraint**: the particle MUST be charge-neutralized to zero residual charge. Even a single elementary charge at this noise level kills the experiment by 2.4 × 10^5 above the USL. Charge neutralization is demonstrated in the laboratory but achieving and verifying zero charge during 10 s of free fall remains technically challenging.

### Channel 7: Vibrational/Seismic Coupling

**Formula:** During free fall, coupling only through gravity gradients of nearby masses:

```
omega_grav = sqrt(G M_app / d^3) = 2.58 × 10^-4 rad/s (for M = 1 kg at d = 10 cm)
D_pp^vib = m^2 × omega_grav^4 × S_x
Lambda_vib = D_pp^vib × l^2 / hbar^2
```

**Result:** Lambda_vib = **6.05 × 10^-16 s^-1**

**Confidence:** HIGH (gravitational coupling is fundamental).

**Status:** Utterly negligible. Gravity-gradient coupling is far too weak to matter at this scale.

---

## Part III — Total Budget vs USL

### Budget table (ranked)

| Channel | Rate (s^-1) | vs USL (ratio) | Confidence | Protocol note |
|---------|-------------|-----------------|------------|--------------|
| Laser recoil | 1.63 × 10^9 | 1.7 × 10^12 | HIGH | MUST be dark |
| Charge noise (1e) | 231 | 2.4 × 10^5 | LOW-MOD | MUST be neutral |
| **Gas collisions** | **1.76 × 10^-3** | **1.84** | **HIGH** | — |
| BB emission | 2.70 × 10^-6 | 2.8 × 10^-3 | MOD | — |
| BB absorption | 3.46 × 10^-11 | 3.6 × 10^-8 | MOD | — |
| Vibrational | 6.05 × 10^-16 | 6.3 × 10^-13 | HIGH | — |
| BB Rayleigh | 5.88 × 10^-40 | 6.1 × 10^-37 | HIGH | — |

### Three-tier structure

1. **Protocol-eliminated channels** (laser recoil, charge noise): These are not noise floors — they are binary protocol constraints. Either the experiment runs dark and charge-neutral, or it fails completely. Both are achievable in principle but technically demanding. We ASSUME they are satisfied.

2. **The binding channel** (gas collisions): Lambda_gas = 1.76 × 10^-3 s^-1. This is the true environmental floor. It is **1.84× the USL prediction** at the reference parameters. Gas collisions DOMINATE.

3. **Subdominant channels** (BB emission, absorption, scattering, vibration): All at least 350× below the USL. Negligible.

### Verdict at reference parameters

```
Lambda_USL = 9.57 × 10^-4 s^-1
Lambda_env (optimistic, dark + neutral) = 1.76 × 10^-3 s^-1

Ratio USL/env = 0.54

Classification: ENVIRONMENT-DOMINATED BUT CLOSE
```

**The USL does NOT dominate at the Gamma-Prime crossover mass (4 fg).** The gas collision rate alone exceeds the USL by a factor of 1.84. The Gamma-Prime "ratio 2.1" used a different mass point (10 fg, not 4 fg). At 4 fg, the test window is narrower than claimed.

### Corrected mass scan

| Mass (fg) | Lambda_USL (s^-1) | Lambda_gas (s^-1) | USL/gas | Classification |
|-----------|-------------------|-------------------|---------|:-------------:|
| 3.9 (150 nm) | 9.6 × 10^-4 | 1.76 × 10^-3 | 0.54 | env-dominated |
| 5 (164 nm) | 1.6 × 10^-3 | 2.04 × 10^-3 | 0.78 | env-dominated |
| **7 (183 nm)** | **3.1 × 10^-3** | **2.54 × 10^-3** | **1.22** | **USL wins** |
| 10 (206 nm) | 6.3 × 10^-3 | 3.23 × 10^-3 | 1.96 | USL dominates |
| 20 (260 nm) | 2.5 × 10^-2 | 5.12 × 10^-3 | 4.93 | USL dominates |
| 50 (352 nm) | 1.6 × 10^-1 | 9.38 × 10^-3 | 16.9 | USL dominates |

**Note:** Lambda_gas scales as R^2 ~ m^(2/3). Lambda_USL scales as m^2. The USL grows MUCH faster with mass. The true crossover (accounting for gas scaling) is at **m ~ 7 fg (diameter ~366 nm)**, not the naive 4 fg from Gamma-Prime.

**Correction:** The Gamma-Prime crossover estimate assumed a FIXED environmental rate of 10^-3 s^-1. The actual gas rate INCREASES with particle size (larger cross section). This pushes the crossover mass upward. At m = 10 fg (the Blueprint paper's target), USL/gas ~ 2.0 — consistent with Gamma-Prime's claim, but only because m = 10 fg is 2.5× the naive crossover.

---

## Part IV — Visibility and Run-Count Forecast

### At the corrected crossover mass (m = 10 fg, R = 103 nm)

```
Lambda_USL = 6.33 × 10^-3 s^-1
Lambda_gas = 3.23 × 10^-3 s^-1
Lambda_total = 9.56 × 10^-3 s^-1 (with USL)
Lambda_total = 3.23 × 10^-3 s^-1 (without USL)
```

Over t_int = 10 s:

```
Visibility without USL: exp(-0.0323) = 0.9682
Visibility with USL:    exp(-0.0956) = 0.9089
Difference: 0.0593 (6.1% of baseline visibility)
```

Coherence time:
```
Without USL: 1/0.00323 = 310 s
With USL:    1/0.00956 = 105 s
Reduction: 66%
```

### Run-count estimate

Signal: Delta_V / V = 6.1%

For 3-sigma detection:
- **Ideal (shot-noise limited):** N_runs = (3 / 0.061)^2 = 2,420
- **Realistic (SNR/run = 10):** N_runs = (3 / (0.061 × 10))^2 = 24
- **Practical (SNR/run = 3):** N_runs = (3 / (0.061 × 3))^2 = 268

At ~300 experiments/day (MAQRO-rate), this requires ~1 day of data-taking in the optimistic scenario.

### At the reference crossover mass (m = 4 fg, the minimal mass)

```
Lambda_USL = 9.57 × 10^-4 s^-1
Lambda_gas = 1.76 × 10^-3 s^-1
Delta_V = 0.009 (0.95% of baseline visibility)
```

Required runs for 3-sigma:
- Ideal: ~100,000 (impractical for this class of experiment)
- Realistic (SNR=10): ~1,000

**The 4 fg crossover is marginal. The 10 fg target is viable with ~100-1000 runs.**

---

## Part V — Sensitivity Bottleneck Analysis

### Hierarchy (after protocol constraints are met)

1. **Gas collisions: THE BINDING CONSTRAINT.** Lambda_gas = 1.76 × 10^-3 s^-1 at P = 10^-13 Pa, T = 4 K, R = 75 nm. This is the single number that determines whether the USL is visible. Everything else is negligible.

2. **Blackbody emission: DISTANT SECOND.** Lambda_emi = 2.7 × 10^-6 s^-1. Three orders of magnitude below gas. Becomes relevant only if gas is suppressed below 10^-5 s^-1, which requires P < 10^-16 Pa (beyond current technology).

3. **All other channels: IRRELEVANT** at this operating point. Scattering, absorption, vibration are 8-37 orders below the USL.

### What improvements matter most?

**Reducing gas pressure is the ONLY lever that matters.** All other environmental channels are already negligible.

Specifically:
- At P = 10^-13 Pa: Lambda_gas = 1.76 × 10^-3 s^-1 (gas > USL at m = 4 fg)
- At P = 10^-14 Pa: Lambda_gas = 1.76 × 10^-4 s^-1 (gas < USL at m = 4 fg by 5×)
- At P = 10^-15 Pa: Lambda_gas = 1.76 × 10^-5 s^-1 (gas < USL by 54×)

**An additional order of magnitude in vacuum** (from 10^-13 to 10^-14 Pa, i.e., 10^-16 mbar) would make the USL clearly dominant even at the minimal crossover mass.

### What improvements give diminishing returns?

- **Lower T_env below 4 K:** BB channels are already negligible. Going to mK temperatures gains nothing.
- **Better vibration isolation:** Already 10^-13 below USL. Irrelevant.
- **Lower laser power:** Only matters during illumination, which must be zero during coherence anyway.

### What DOESN'T the environmental budget cover?

Three effects are NOT captured above:
1. **Wavepacket expansion and free-fall constraints:** Over 10 s, the particle falls ~490 m under gravity. This requires either microgravity (space, drop tower) or magnetic levitation. This is a platform constraint, not a decoherence source.
2. **Internal heating from surface effects:** The particle's internal temperature may rise during free fall due to internal strain energy release. Poorly characterized.
3. **Stray electromagnetic fields from cryostat:** Beyond the charge noise estimate. Could add to D_pp.

---

## Part VI — Viability Ladder

### Already achievable (demonstrated in existing labs)
- Particle fabrication (150+ nm silica nanospheres: commercial)
- Optical trapping of nanoparticles (multiple groups since 2010)
- Ground-state cooling (Delic 2020, phonon number < 1)
- Cryogenic environment T_env = 4 K (standard He cryostat)
- UHV at 10^-10 Pa (standard room-temp UHV)

### Plausible with near-term improvement (2-3 years)
- Charge neutralization to ~0e (demonstrated but reliability and verification during free fall uncertain)
- Internal temperature T_int < 20 K (requires radiative equilibration after laser release)
- Dark free-evolution protocol (no fundamental obstacle, but readout without illumination is hard)
- Vacuum at 10^-12 Pa (cryogenic UHV with bakeout)

### Requires major but realistic technical advance (3-7 years)
- Vacuum at 10^-13 to 10^-14 Pa (extreme cryopumped UHV — approaches gas-kinetic limit of cryosorption)
- Spatial superposition l ~ 10 nm (current record: 73 pm for nanoparticle, 100x gap)
- 10 s free evolution (requires drop tower ~490 m, or space, or magnetic levitation)
- Position readout at nm resolution after seconds of free fall (no demonstrated scheme at this precision)

### Speculative with current architecture (>7 years or new paradigm)
- All of the above simultaneously in a single experiment
- Statistical discrimination of USL from environment at the required precision
- Vacuum at 10^-15 Pa (below outgassing floor of most materials)

---

## Part VII — Final Verdict

### Classification

**usl_test_window_narrows_but_survives**

The full environmental budget reveals that Gamma-Prime's crossover estimate was too optimistic at the 4 fg crossover mass: gas collisions alone exceed the USL by 1.84× at P = 10^-13 Pa. However, the test window SURVIVES at higher mass. At the Blueprint paper's target of m = 10 fg (206 nm diameter), the USL exceeds the gas collision floor by ~2× — consistent with Gamma-Prime's original claim for that mass point. The gas collision rate is the sole binding constraint; all other channels are negligible.

The practical test window is:

```
m > 7 fg  (diameter > 183 nm silica)
l ~ 10 nm
P < 10^-13 Pa  (10^-15 mbar)
T_env < 5 K
Dark protocol (zero laser during coherence)
Charge-neutral particle (0 elementary charges)
Free evolution > 10 s
```

The signal at m = 10 fg: 6.1% visibility contrast over 10 s, requiring ~100-1000 runs for 3-sigma detection.

### Public-Facing Paragraph

GRUT II Delta-Prime computes the full environmental decoherence budget for a Blueprint-class levitated nanoparticle platform, evaluating seven decoherence channels from published formulas. Two channels (laser photon recoil and charge noise) are protocol-eliminated: the experiment must use a fully dark, charge-neutral protocol or it fails catastrophically. Of the remaining five channels, gas collisions dominate by three or more orders of magnitude over all others. At the Gamma-Prime crossover mass of 4 fg, gas collisions alone exceed the USL prediction by 1.84×, narrowing the test window. However, at m = 10 fg (206 nm silica diameter), the USL exceeds the gas floor by ~2× and produces a 6.1% visibility contrast over 10 s — detectable with ~100-1000 experimental runs. The sole experimental bottleneck is residual gas pressure: achieving 10^-13 Pa (10^-15 mbar) at 4 K by cryopumping is technically demanding but within the envelope of extreme UHV technology. The USL test window survives the full environmental budget, but is narrower and harder to reach than the coarse Gamma-Prime estimate suggested.

### Internal Doctrine Paragraph

The experimental go/no-go for the USL reduces to a SINGLE number: the residual gas collision rate at the operating point. If an experiment prepares a spatial superposition of a >200 nm silica nanosphere at >10 nm separation in a dark, charge-neutral, cryogenic UHV environment, and observes a coherence time consistent with environmental-only decoherence (tau ~ 300 s), the USL is excluded at the parameters Lambda = Gm^2/(hbar l). If the coherence time is ~100 s (3× shorter than environment-only), the USL is supported. The discriminant is the ratio of measured to predicted-environmental coherence time. Any intermediate value requires a careful subtraction of the gas collision rate (which must be independently calibrated via pressure measurement). The irreducible experimental question is: can the gas collision contribution be measured and subtracted with sufficient precision to reveal or exclude a ~6 × 10^-3 s^-1 excess?

### Next Forced Move

The full budget has identified the single binding constraint: gas collision rate at extreme UHV. The next forced move is **GRUT II Epsilon-Prime — Gas Collision Subtraction and Calibration Protocol**: determine whether the gas collision rate can be independently measured (via pressure gauges, ion gauges, or residual gas analysis) to sufficient precision that a ~10^-3 s^-1 excess can be resolved above it. This is the metrological question that determines whether the USL test is a real measurement or a background-limited null result. Alternatively, if the gas rate can be suppressed below 10^-4 s^-1 (by reaching 10^-14 Pa), the USL dominates by 10× and subtraction becomes unnecessary — the cleaner path.

---

*GRUT II Delta-Prime complete. Verdict: usl_test_window_narrows_but_survives. Gas collisions are the sole binding constraint (1.76e-3 s^-1 at P=10^-13 Pa, T=4K). All other channels negligible by 3+ orders. USL/gas ratio: 0.54 at 4 fg (marginal), 1.96 at 10 fg (detectable), 4.93 at 20 fg (clear signal). Protocol-eliminated constraints: dark free evolution (mandatory), charge neutralization (mandatory). The coarse Gamma-Prime crossover at 4 fg was optimistic by ~2×; the corrected crossover is ~7 fg. At the Blueprint target of 10 fg, the USL produces a 6.1% visibility contrast detectable in 100-1000 runs. Single bottleneck: residual gas pressure.*
