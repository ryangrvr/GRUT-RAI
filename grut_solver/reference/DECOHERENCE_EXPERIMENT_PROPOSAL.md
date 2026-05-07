# Experimental Proposal: Gravitational Decoherence Plateau in Levitated Optomechanics

## A Zero-Parameter Prediction from the CTP Influence Functional

D. Ryan Grover, April 2026

---

## Summary

We predict a pressure-independent decoherence floor for mesoscopic objects in spatial superposition. As environmental noise is suppressed (lower pressure, lower temperature), the decoherence rate does not go to zero. It saturates at a gravitational plateau set entirely by the object's mass, size, and superposition geometry:

    Lambda_grav = G m^2 S(l/R) / (hbar l)

with S(l/R) = min(1, (l/R)^3/6). Zero free parameters. Standard quantum mechanics predicts this plateau does not exist. One pressure-scan measurement decides.

---

## 1. The Prediction

### 1.1 The rate formula

The gravitational decoherence rate for a uniform sphere of mass m, radius R, in a spatial superposition of separation l:

    Lambda_grav = G m^2 S(l/R) / (hbar l)

where the extended-body suppression factor:

    S(l/R) = { 1             for l >= 2R  (far field)
             { (l/R)^3 / 6   for l < 2R   (near field)

This is derived from the tree-level gravitational Diosi self-energy integral in the CTP (Schwinger-Keldysh) influence functional. It is not a free-parameter model — the rate is fully determined by (m, R, l, G, hbar).

### 1.2 Corrected benchmark objects

Previous publications used inconsistent parameters (m = 10 pg with R = 50 nm, which requires unphysical density). Corrected benchmarks using single realizable objects:

| Object | Material | R [nm] | m [pg] | l [nm] | S(l/R) | Lambda [Hz] | t_coh [ms] |
|:---|:---|:---|:---|:---|:---|:---|:---|
| **Primary** | Gold | 1000 | 80.8 | 1000 | 0.167 | **689** | **1.5** |
| Secondary | Gold | 500 | 10.1 | 1000 | 1.000 | 64.6 | 15.5 |
| Far-field | Gold | 500 | 10.1 | 500 | 0.167 | 21.5 | 46 |
| Large | Gold | 750 | 34.1 | 1500 | 1.000 | 491 | 2.0 |

All use gold (density 19,300 kg/m^3). Mass and radius are mutually consistent.

### 1.3 What standard QM predicts

In standard quantum mechanics, all decoherence arises from the environment. As environmental coupling is reduced (lower P, lower T, better isolation), Lambda → 0. There is no gravitational floor.

### 1.4 What the CTP prediction says

Lambda_grav is irreducible. It comes from the object's own gravitational self-energy — the Newtonian self-interaction of the mass distribution in superposition. Suppressing the environment reveals this floor. It does not go to zero.

---

## 2. The Measurement

### 2.1 What to measure

The visibility of a matter-wave interference pattern (or equivalently, the off-diagonal decay rate of the center-of-mass density matrix) as a function of residual gas pressure, at fixed temperature and trap parameters.

### 2.2 The pressure scan

At high pressure (P > 10^-8 Pa): Lambda_gas dominates. The decoherence rate decreases with decreasing pressure.

At intermediate pressure (P ~ 10^-9 Pa): Lambda_gas ~ Lambda_grav. The rate curve begins to flatten.

At low pressure (P < 10^-10 Pa): Lambda_grav dominates. The rate should SATURATE at the gravitational plateau, independent of further pressure reduction.

The crossover pressure for the primary gold benchmark:

    P* = Lambda_grav × k_B T / (sigma × v_th × (l/lambda_dB)^2)
       ~ 4 × 10^-9 Pa  (at T = 10 mK)

Below P*, the plateau should be visible.

### 2.3 Required experimental parameters

| Parameter | Required | Current state-of-art | Gap |
|:---|:---|:---|:---|
| Mass | > 10 pg (10^10 amu) | ~ 10^5 amu (nanoparticle interferometry) | 10^5 |
| Superposition separation | > 100 nm | ~ 10 nm (demonstrated) | 10 |
| Pressure | < 10^-10 Pa | ~ 10^-8 Pa (UHV) | 100 |
| Temperature | < 100 mK | Achieved (dilution fridges) | Met |
| Coherence time | > 1 ms | ~ 10 us (current) | 100 |

The primary gap is mass. Current interferometry reaches ~10^5 amu. The prediction requires ~10^10 amu. Levitated optomechanics with gold or osmium nanospheres at R ~ 500-1000 nm is the most promising path.

### 2.4 Experimental platforms

The following groups have platforms approaching the required regime:

- **Arndt group (Vienna):** OTIMA interferometer. Current: ~10^5 amu molecules. Path to nanoparticles.
- **Aspelmeyer group (Vienna):** Levitated optomechanics. Demonstrated ground-state cooling of nanoparticles.
- **Geraci group (Northwestern):** Levitated nanospheres in optical traps. Active development toward larger masses.
- **Bateman group (UCL):** Proposals for MAQRO-type space-based interferometry at mesoscopic masses.

---

## 3. Six Discriminating Signatures

The gravitational plateau has six properties that distinguish it from all tested alternative models. A complete experimental program would test all six:

### 3.1 Signature F3: Pressure plateau

The rate saturates below P*. No alternative decoherence source (gas, blackbody, trap noise, charge noise) produces a pressure-independent floor at the predicted value.

**Test:** Measure Lambda vs P from 10^-6 to 10^-11 Pa. Look for flattening.

### 3.2 Signature F2: Geometry dependence

At fixed mass m, the rate depends on the material density through R = (3m/4 pi rho)^(1/3). A denser sphere (smaller R) gives a HIGHER rate (less suppression from S(l/R)).

**Test:** Compare Lambda for gold (rho = 19,300) vs silica (rho = 2,200) nanospheres at the same mass. Gold should decohere faster by a factor (rho_gold/rho_silica)^(2/3) ~ 5 in the near-field regime.

### 3.3 Signature F5: Entanglement protection

Bell-entangled pairs of particles decohere SLOWER than independent pairs. The cross-term in the Diosi functional is state-dependent: entangled states have a partial cancellation.

**Test:** Prepare entangled vs separable two-particle states. The entangled state should have Lambda_Bell < Lambda_product.

### 3.4 Signature F4: l-scaling

In the far field (l > 2R): Lambda ~ 1/l (slope = -1 on log-log).
In the near field (l < 2R): Lambda ~ l^2 (slope = +2 on log-log).

**Test:** Vary the superposition separation l and measure the slope.

### 3.5 Signature F6: Geometric kink

At l = 6^(1/3)R ≈ 1.817R, the rate has a kink where the near-field scaling transitions to the far-field scaling. No smooth power law can reproduce this feature.

**Test:** Fine-scan Lambda vs l near l ~ 2R. Look for a slope change.

### 3.6 Signature F1: Mass-squared scaling

In the far field: Lambda ~ m^2 (slope = 2 on log-log of Lambda vs m).

**Test:** Measure Lambda for several masses at fixed l > 2R. The slope should be exactly 2.

---

## 4. Alternative Models and How to Distinguish Them

| Model | Parameters | Reproduces F1? | F2? | F3? | F5? | All 6? |
|:---|:---|:---|:---|:---|:---|:---|
| Standard QM (no floor) | 0 | N/A | N/A | NO (no plateau) | N/A | NO |
| Constant floor | 1 | No (wrong scaling) | No | Yes | No | NO |
| Power-law floor | 2 | Partial | No | Yes | No | NO |
| CSL | 2 (lambda, r_C) | Yes | No (state-independent) | Yes | No | NO |
| Diosi-Penrose (point-mass) | 0 | Yes | No (no S(l/R)) | Yes | No | NO |
| **CTP gravitational (this work)** | **0** | **Yes** | **Yes** | **Yes** | **Yes** | **YES** |

No tested alternative reproduces all six signatures. The adversarial kill framework (183 tests) verifies this computationally.

---

## 5. What a Null Result Means

If no plateau is observed at P < 10^-10 Pa and the decoherence rate continues to decrease with pressure:

- The CTP gravitational decoherence prediction (Lambda_grav) is falsified
- The gravitational Diosi self-energy integral does not produce an observable decoherence floor at the predicted mass scale
- The constitutive framework loses its predictive core
- The cosmological constant formula H_inf = (2-R)/(S tau_0), which uses constants derived from the decoherence sector, loses its quantitative grounding

A null result is clean and decisive. The framework does not survive it.

---

## 6. What a Positive Result Means

If a plateau IS observed at ~689 Hz for the gold primary benchmark (or at the appropriate value for any benchmark object):

- The CTP gravitational decoherence prediction is confirmed
- The zero-parameter nature of the prediction (no fitting) makes this a strong test
- The six discriminating signatures distinguish it from all tested alternatives
- The framework gains credibility for its downstream predictions (cosmological constant, QCD mapping, etc.)
- The extended-body suppression factor S(l/R) is confirmed as a novel feature beyond standard Diosi-Penrose

---

## 7. Summary of the Experimental Target

**The question:** Does the decoherence rate of a mesoscopic spatial superposition saturate at a pressure-independent gravitational plateau?

**The prediction:** Yes. Lambda_grav = G m^2 S(l/R) / (hbar l). Zero parameters.

**The benchmark:** Gold microsphere, R = 1 um, m = 80.8 pg, l = 1 um → Lambda = 689 Hz.

**The test:** Pressure scan below 10^-10 Pa. Look for rate saturation.

**The alternative:** Standard QM says Lambda → 0. One measurement decides.

---

*D. Ryan Grover, April 2026.*

*Software: github.com/ryangrvr/GRUT-RAI-v1.0*
*183 passing tests. Zero free parameters.*
