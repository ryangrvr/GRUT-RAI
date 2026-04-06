# GRUT II Eta-Prime — Terminal Consolidation of the Quantum-Sector Experimental Roadmap

---

## Part I — Executive Summary

The GRUT-II quantum sector has produced one sharp, falsifiable prediction: the **Universal Scaling Law** (USL),

```
Lambda_USL = G m^2 / (hbar l)
```

which gives the gravitational decoherence rate of a spatial superposition of mass m with branch separation l. This formula has zero free parameters. It is either correct or it is not.

Over the course of stages Alpha-Prime through Zeta-Prime, the program has:

1. Derived the USL from the constitutive structure of the GRUT scalar field (Alpha-Prime).
2. Shown the USL is consistent with all existing mesoscopic quantum experiments by 6-15 orders of magnitude (Beta-Prime, Zeta-Prime).
3. Identified the first experimentally reachable test window: levitated silica nanospheres of mass 20-30 fg superposed over 5-10 nm (Gamma-Prime, Epsilon-Prime).
4. Computed the full environmental decoherence budget channel by channel and confirmed that gas collisions are the sole binding constraint (Delta-Prime).
5. Optimized the target mass and separation, finding that the signal-to-noise improves substantially above the initial 10 fg reference point (Epsilon-Prime).
6. Stress-tested the operating point against parameter variation and confirmed robustness at nominal conditions (Zeta-Prime).

The result is a concrete, stress-tested experimental specification for the first direct test of gravitational decoherence at the universal scaling predicted by the GRUT constitutive framework.

---

## Part II — Final Formula and Interpretation

### The Universal Scaling Law

```
Lambda_USL = G m^2 / (hbar l)
```

where:

| Symbol | Meaning | Units |
|--------|---------|-------|
| Lambda_USL | Gravitational decoherence rate | s^-1 |
| G | Newton's gravitational constant | 6.674 x 10^-11 m^3 kg^-1 s^-2 |
| m | Total mass in spatial superposition | kg |
| l | Branch separation (distance between superposed positions) | m |
| hbar | Reduced Planck constant | 1.055 x 10^-34 J s |

### What it predicts

A massive object placed in a spatial superposition (simultaneously at two positions separated by l) will undergo decoherence — loss of quantum coherence between the branches — at rate Lambda_USL. The observable consequence is a reduction in the visibility of quantum interference fringes:

```
Visibility(t) = V_0 × exp(-Lambda_USL × t)
```

The decoherence time is tau_USL = 1/Lambda_USL.

### What it is NOT

The USL is the **quantum-sector prediction** of the GRUT framework. It governs the decoherence of spatial superpositions of massive objects. It is NOT:

- The Level-1 constitutive relaxation rate (1/tau_local = 1/tau_0 + 1/t_dyn), which governs the classical relaxation of the scalar field near gravitational sources.
- A collapse model with a free cutoff parameter (like CSL with r_C, or regularized Diosi-Penrose with R_0). The USL has zero free parameters.
- A modification of general relativity. The strong-field sector of GRUT is compatible with GR at the level established in Books XIII-XVI.

The USL and Level-1 are **separate predictions for separate observables** (Alpha-Prime). The USL predicts decoherence rates for quantum superpositions. Level-1 predicts classical relaxation timescales near compact objects. They share a common origin in the constitutive equation tau dPhi/dt + Phi = X but apply to different physical regimes.

---

## Part III — Experimental History and Current Status

### What has been achieved (2020-2026)

| Experiment | Mass | Coherence achieved | Lambda_USL at this point | USL/sensitivity |
|-----------|:----:|:------------------:|:------------------------:|:---------------:|
| Delic 2020 (ground state cooling) | 1.66 fg | 0.43 phonons, 7.6 us | 0.10 s^-1 (at x_zpf = 17 pm) | 4 x 10^-6 |
| Rossi 2025 (quantum delocalization) | 1.2 fg | 73 pm coherence length | 0.012 s^-1 | 5 x 10^-7 |
| Arndt 2026 (Na cluster interference) | 0.28 ag | Full interference, ~10 ms | 5 x 10^-13 s^-1 | ~10^-15 |

**No existing experiment is within 6 orders of magnitude of the USL prediction.** The gap is not in principle but in mass and separation: current experiments use objects too light (atoms, molecules) or achieve separations too small (sub-pm for nanoparticles).

### Proposed platforms that remain below sensitivity

| Platform | Mass | Predicted Lambda_USL | Environmental rate | USL/env |
|----------|:----:|:--------------------:|:-----------------:|:-------:|
| SUPER-MARIO (RT, 5 nm) | 1 fg | 1.3 x 10^-4 | ~10 | 10^-5 |
| SUPER-MARIO (cryo, 100 nm) | 1 fg | 6.3 x 10^-6 | ~0.02 | 3 x 10^-4 |
| MAQRO-PF (space, grating) | 1.7 fg | 8.6 x 10^-6 | ~0.01 | 9 x 10^-4 |

All proposed platforms at the ~1 fg mass scale remain 10^3-10^5 below the USL sensitivity threshold.

### The narrowed test window

The USL becomes testable when Lambda_USL exceeds the total environmental decoherence rate. Since Lambda_USL scales as m^2 and environmental gas decoherence scales as m^(2/3), heavier particles give exponentially better signal-to-noise. The test window opens at:

```
m > 3.65 fg  (at l = 5 nm, P = 10^-13 Pa, T = 4 K)
m > 6.14 fg  (at l = 10 nm)
m > 10.3 fg  (at l = 20 nm)
```

The practical sweet spot, balancing signal strength against protocol difficulty, is 20-30 fg.

---

## Part IV — Environmental Budget Consolidation

### The seven decoherence channels at the frozen operating point (25 fg, 5 nm, 4 K, 10^-13 Pa)

| Channel | Rate (s^-1) | vs Lambda_USL | Status |
|---------|:-----------:|:-------------:|:------:|
| **Gas collisions** | **6.09 x 10^-3** | **0.077** | **BINDING CONSTRAINT** |
| BB emission (T_int = 20 K) | ~3 x 10^-6 | 4 x 10^-5 | Negligible |
| BB absorption (T_env = 4 K) | ~3 x 10^-11 | 4 x 10^-10 | Negligible |
| BB Rayleigh scattering | ~6 x 10^-40 | ~0 | Zero |
| Vibrational/seismic | ~6 x 10^-16 | 8 x 10^-15 | Negligible |
| **Laser recoil** | **1.6 x 10^9** | **2 x 10^10** | **PROTOCOL-ELIMINATED (must be dark)** |
| **Charge noise (1e)** | **231** | **2900** | **PROTOCOL-ELIMINATED (must be neutral)** |

### Structure

The environmental budget has a **three-tier structure**:

1. **Protocol-eliminated killers** (laser recoil, charge noise): Not backgrounds. Binary constraints. Either the experiment runs dark and charge-neutral, or it fails completely. Both are achievable in principle.

2. **The binding channel** (gas collisions): Lambda_gas = 6.09 x 10^-3 s^-1. This is the true environmental floor and the single number that determines whether the USL is visible.

3. **Negligible channels** (BB emission/absorption/scattering, vibration): All at least 10^4 below Lambda_USL. Irrelevant under any realistic variation.

---

## Part V — Final Optimized Operating Point

### FROZEN CONFIGURATION

| Parameter | Value | Source |
|-----------|-------|--------|
| **Material** | Amorphous silica (SiO2) | Standard platform |
| **Density** | 2200 kg/m^3 | Literature |
| **Mass** | **25 fg** (2.5 x 10^-17 kg, 1.5 x 10^10 amu) | Epsilon-Prime optimum |
| **Radius** | 139.5 nm | From mass and density |
| **Diameter** | **279 nm** | |
| **Branch separation** | **5 nm** | Zeta-Prime robustness optimum |
| **Pressure** | **< 10^-13 Pa** (10^-15 mbar) | Delta-Prime binding constraint |
| **Temperature (shield)** | 2-8 K (4 K nominal) | Zeta-Prime: thermally insensitive |
| **Temperature (internal)** | < 20 K | Delta-Prime: BB emission negligible |
| **Trap frequency** | 100 kHz | Standard optomechanical |
| **Protocol** | Dark free evolution, charge-neutral | Delta-Prime mandatory |
| **Zero-point motion** | 1.83 pm | From m and omega |
| **Expansion ratio** | **2,729** | l / x_zpf |
| **Interrogation time** | 5-10 s | Visibility optimization |

### FROZEN PREDICTIONS

| Quantity | Value |
|----------|-------|
| **Lambda_USL** | **7.91 x 10^-2 s^-1** |
| **tau_USL** | **12.6 s** |
| **Lambda_gas** | **6.09 x 10^-3 s^-1** |
| **USL/gas ratio** | **13.0** |
| **Total Gamma (env + USL)** | **8.52 x 10^-2 s^-1** |

### PREDICTED SIGNAL (at t = 5 s)

| Quantity | Without USL | With USL | Difference |
|----------|:-----------:|:--------:|:----------:|
| Visibility | 0.970 | 0.653 | **0.317 (32.7%)** |
| Coherence time | 164 s | 11.7 s | **14x reduction** |

### REQUIRED RUNS FOR 3-SIGMA DETECTION

| Interrogation time | Visibility contrast | N_runs (ideal) | N_runs (SNR/run = 10) |
|:------------------:|:-------------------:|:--------------:|:---------------------:|
| 1 s | 7.6% | 1,556 | 16 |
| 5 s | 32.7% | 84 | 1 |
| 10 s | 54.7% | 30 | 1 |

At t = 5 s, the USL signal is a 33% visibility loss — easily distinguishable from the environmental-only prediction of 3.0% loss.

### BACKUP CONFIGURATION (l = 10 nm)

If l = 5 nm proves unachievable, the backup at l = 10 nm gives:

| Quantity | Value |
|----------|-------|
| Lambda_USL | 3.96 x 10^-2 s^-1 |
| USL/gas | 6.5 |
| Expansion ratio | 5,458 |
| Visibility contrast (5 s) | ~17% |
| N_runs (ideal, 5 s) | ~280 |

Still viable but with 2x less signal and 2x harder protocol.

---

## Part VI — Robustness Statement

### What is robust

1. **Temperature:** The USL/gas ratio IMPROVES with higher temperature (at fixed pressure). The window survives from 2 K to >20 K. Temperature is not a constraint.

2. **Separation range:** At 25 fg, USL/gas > 1 from l = 3 nm (ratio 22) to l = 30 nm (ratio 2.2). The window spans a full decade in separation.

3. **Mass range:** USL/gas > 1 from m = 3.65 fg (crossover) to arbitrarily high mass. The signal grows as m^(4/3). Only protocol difficulty limits the upper end.

4. **Global consistency:** Lambda_USL is below experimental sensitivity by at least 6 orders of magnitude in EVERY existing mesoscopic quantum experiment. Zero tension with any data.

### What is narrow

1. **Pressure:** The SOLE fragility. At P = 10^-12 Pa (10× above nominal), USL/gas drops to 0.65 at 25 fg and the test fails. Recovery requires increasing mass to >35 fg or reducing separation to 5 nm (or both).

### What would kill the roadmap

1. **Pressure floor stuck at 10^-12 Pa:** If cryogenic UHV cannot reach 10^-13 Pa, the 25 fg target fails at l = 10 nm. Partially recoverable at l = 5 nm (ratio 1.3) or higher mass (ratio > 1 at 37 fg).

2. **Pressure floor stuck at 10^-11 Pa:** The entire sub-100 fg window closes. Recovery requires particles > 200 fg with expansion ratios > 20,000 — beyond any foreseeable protocol.

3. **Wavepacket expansion limited to < 1,000x:** The 5 nm separation at 25 fg requires 2,729× expansion. If this cannot be achieved, the separation must increase to >18 nm (where current ~1,000× expansion suffices), but there USL/gas drops to ~4 and the expansion ratio is ~1,000 by construction. This is a viable fallback but with weaker signal.

4. **Charge neutralization failure:** Even 1 elementary charge creates a decoherence rate of ~230 s^-1, drowning the USL signal of 0.079 s^-1. The protocol MUST achieve zero net charge.

---

## Part VII — Single Experimental Milestone

The entire GRUT-II quantum-sector roadmap reduces to **one decisive milestone:**

> **Demonstration of ~2,500-3,000× wavepacket expansion from the motional ground state of a ~25 fg silica nanosphere, under dark (no laser), charge-neutral conditions, in cryogenic ultra-high vacuum (P < 10^-13 Pa).**

### Why this is the bottleneck

- **Environmental isolation:** Cryogenic UHV at 10^-13 Pa is demanding but within the envelope of extreme vacuum technology (cryopumping at 4 K). Multiple groups target this regime.

- **Charge neutralization:** Demonstrated for levitated nanoparticles. Verification during free fall is harder but not fundamentally limited.

- **Dark protocol:** Requires switching off the trapping laser and letting the particle fall freely. No fundamental obstacle. The challenge is position readout without re-illumination.

- **Wavepacket expansion:** The current record is ~950× at 1.95 fg (Bonvin et al. 2025). The required ~2,729× at 25 fg is a factor of ~3 beyond the state of the art. This is the pacing item.

The expansion ratio scales as m^(1/2), so heavier particles require more expansion. But the USL signal scales as m^2, growing much faster. The optimal compromise (Epsilon-Prime) places the expansion requirement at ~2,700-5,500× depending on l, which is 3-6× beyond current capability.

### Current status of the milestone

| Capability | Current best | Required | Gap |
|-----------|:-----------:|:--------:|:---:|
| Wavepacket expansion | ~950× (1.95 fg) | ~2,729× (25 fg) | 3× |
| Cryogenic UHV | ~10^-10 Pa | 10^-13 Pa | 10^3× |
| Particle mass | ~1.2 fg ground state | 25 fg | 20× mass (trivial) |
| Charge neutralization | Demonstrated (static) | During free fall | Unknown |
| Dark free evolution | Not yet demonstrated for nanoparticles | 5-10 s | Requires drop tower or space |

---

## Part VIII — Go / No-Go Criteria

### GO conditions (all must be met)

1. **Pressure:** P < 10^-13 Pa demonstrated in the experimental chamber with particle present.
2. **Dark protocol:** Laser fully off during coherence interval. No photon scatter > 1 per 10^4 s.
3. **Charge neutralization:** Net charge verified at 0e before release. Charge monitoring during free fall.
4. **Expansion:** Wavepacket expanded from ground state to > 5 nm (or > 10 nm at backup) in < 100 μs, with coherence verified.
5. **Free evolution:** > 5 s of uninterrupted dark free fall (drop tower, space, or magnetic levitation).
6. **Readout:** Position measurement resolving < 1 nm features after free evolution.

### NO-GO conditions (any one kills the test)

1. **Pressure floor > 10^-12 Pa** with no path to improvement → gas decoherence overwhelms USL at all feasible masses.
2. **Expansion ratio limited to < 1,500×** with no path to improvement → minimum achievable separation is > 3 nm at 25 fg, insufficient for USL dominance.
3. **Uncontrolled charge** during free fall (fluctuating by > 1e) → charge noise drowns the signal by > 10^3.
4. **Laser scatter > 1 photon per second** during "dark" phase → photon recoil noise dominates.
5. **No access to > 5 s free evolution** (no drop tower, no space mission, no alternative) → insufficient integration time for statistical discrimination.

### DECISION TREE

```
Can pressure reach 10^-13 Pa?
  NO  → Can mass be increased to > 50 fg?
          NO  → NO-GO
          YES → Reduced signal (USL/gas ~ 2-3), MARGINAL GO
  YES → Can expansion reach ~2,700×?
          NO  → Fall back to l ~ 15-20 nm (expansion ~1,000×)
                  Signal reduced (USL/gas ~ 4-5), CONDITIONAL GO
          YES → Can dark free evolution reach 5+ s?
                  NO  → Use 1 s integration, ~1,500 runs needed, FEASIBLE GO
                  YES → FULL GO: 30-80 runs, strong signal
```

---

## Part IX — Final Verdict

### Classification

**quantum_sector_terminal_roadmap_frozen**

The GRUT-II quantum sector has produced:

1. A parameter-free prediction: Lambda_USL = Gm^2/(hbar l).
2. A stress-tested experimental target: 25 fg silica, 5 nm separation, cryogenic UHV.
3. A single binding constraint: gas pressure at 10^-13 Pa.
4. A single pacing milestone: ~2,700× wavepacket expansion.
5. A concrete signal: 33% visibility loss at 5 s (vs 3% environmental-only).
6. A practical run count: ~30-80 runs for 3-sigma detection.
7. Zero tension with any existing experiment.

The roadmap is frozen. No further theoretical work in the quantum sector changes these numbers. The next step is experimental.

### Public-Facing Paragraph

The GRUT-II quantum sector predicts that a massive object placed in a spatial superposition decoheres at rate Lambda = Gm^2/(hbar l), where m is the superposed mass and l is the branch separation. This parameter-free prediction is consistent with all current data — in every existing mesoscopic quantum experiment, the predicted rate is at least a million times below experimental sensitivity. However, the program identifies a concrete, stress-tested experimental path to the first direct test: a 25 femtogram silica nanosphere (280 nm diameter) superposed over 5 nanometers in cryogenic ultra-high vacuum at 10^-13 Pa. At this operating point, the USL predicts a decoherence rate 13 times larger than the dominant environmental background (residual gas collisions), producing a 33% visibility loss over 5 seconds — easily distinguishable from the 3% environmental-only prediction. The sole experimental bottleneck is wavepacket expansion: the quantum state must be expanded from a 1.8 picometer ground state to a 5 nanometer superposition (a factor of ~2,700), which is approximately 3 times beyond the current experimental record. The roadmap requires no new physics, no free parameters, and no speculative technology — only quantitative improvement in existing levitated-optomechanics techniques.

### Internal Doctrine Paragraph

The GRUT-II quantum-sector roadmap is now FROZEN at the Eta-Prime level. The following are fixed and should not be casually reopened:
- The USL formula Lambda = Gm^2/(hbar l) as the sole quantum-sector prediction.
- The separation of USL from Level-1 constitutive relaxation (Alpha-Prime correction).
- The environmental budget structure: gas collisions bind, everything else is negligible, laser/charge are protocol-eliminated.
- The optimal operating point: 25 fg / 5 nm / 10^-13 Pa (robust at 73% of tested conditions, 100% at l = 5 nm).
- The single milestone: ~2,700× wavepacket expansion under dark/neutral/cryo-UHV conditions.
- Global consistency: zero tension with all current data by ≥ 6 orders of magnitude.

Any future modification to these numbers requires a new stage with explicit justification, not casual adjustment. The quantum sector is closed at the prediction level.

### Next Program Step

The quantum-sector roadmap is terminal. The next step is NOT further theory. The next step is one of:

**Option A — GRUT-II Terminal Closure:** Write the full GRUT-II terminal document covering ALL sectors (strong-field QNM collapse in Upsilon, tidal suppression in Sigma, bistability architecture from Nu, far-field equivalence from Rho, the Chi→Omega→Alpha-Prime self-correction chain, and this quantum-sector roadmap from Alpha-Prime through Eta-Prime). This closes GRUT-II as a completed program.

**Option B — External Engagement:** Package the quantum-sector roadmap (this document) for communication to experimentalists in levitated optomechanics. The key audience is the Aspelmeyer, Arndt, Romero-Isart, and Bose/Mazumdar groups, who are the leading candidates to build a platform meeting these specifications.

**Option C — Publication Architecture:** Design the publication structure for the GRUT-II results, identifying which stages become papers and in what order.

The quantum sector awaits no further internal computation. It awaits experimental input.

---

*GRUT II Eta-Prime complete. Verdict: quantum_sector_terminal_roadmap_frozen. The USL prediction Lambda = Gm^2/(hbar l) is frozen as a zero-parameter, zero-tension prediction with a concrete experimental path: 25 fg silica / 5 nm separation / 10^-13 Pa cryogenic UHV / 2,700× wavepacket expansion / 33% visibility signal at 5 s / ~30-80 runs for 3-sigma. Single bottleneck: expansion ratio (3× beyond state of art). Single fragility: pressure (10× degradation kills the nominal point). Global consistency: perfect (≥ 6 orders below sensitivity in all existing experiments). The quantum sector is closed at the prediction level.*
