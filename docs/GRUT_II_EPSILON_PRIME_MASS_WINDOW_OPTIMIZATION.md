# GRUT II Epsilon-Prime — Mass-Window Optimization and Protocol Feasibility Audit

## Purpose

Determine whether the USL test window identified in Delta-Prime widens above the 10 fg Blueprint reference, and find the true optimal mass range where the USL signal is strongest relative to both environmental noise and protocol difficulty.

---

## Part I — Scan Definition

### Fixed parameters

| Parameter | Value | Held fixed because |
|-----------|-------|-------------------|
| Material | Silica (2200 kg/m^3) | Standard platform |
| Branch separation l | 10 nm | Gamma-Prime target |
| Environment T_env | 4 K | Liquid He cryostat |
| Internal T_int | 20 K | Post-release radiative cooling |
| Gas pressure P | 10^-13 Pa | Delta-Prime baseline |
| Gas species | N2 | Conservative |
| Trap frequency | 100 kHz | Standard optomechanical |
| Protocol | Dark, charge-neutral | Delta-Prime mandatory constraints |

### Scanned parameter

Mass: **3 fg to 100 fg** (14 points: 3, 4, 5, 7, 10, 12, 15, 20, 25, 30, 40, 50, 70, 100 fg)

Corresponding diameter: 138 nm to 443 nm silica.

---

## Part II — Environmental Scaling Across Mass

### Scaling laws

```
Lambda_USL = G m^2 / (hbar l)              ∝ m^2
Lambda_gas = n_gas × pi × R^2 × v_th       ∝ R^2 ∝ m^{2/3}
Lambda_emi = C × V^2 × T_int^7 / c^5       ∝ V^2 ∝ m^2

Ratio USL/gas ∝ m^2 / m^{2/3} = m^{4/3}   [monotonically increasing]
```

### Results table

| m (fg) | d (nm) | Lambda_USL (s^-1) | Lambda_gas (s^-1) | Lambda_emi (s^-1) | USL/gas | Classification |
|:------:|:------:|:-----------------:|:-----------------:|:-----------------:|:-------:|:--------------:|
| 3 | 138 | 5.70×10^-4 | 1.48×10^-3 | 1.6×10^-6 | 0.39 | COMPARABLE |
| 5 | 163 | 1.58×10^-3 | 2.08×10^-3 | 4.5×10^-6 | 0.76 | COMPARABLE |
| **7** | **182** | **3.10×10^-3** | **2.60×10^-3** | **8.7×10^-6** | **1.19** | **USL > gas** |
| 10 | 206 | 6.33×10^-3 | 3.30×10^-3 | 1.8×10^-5 | 1.92 | USL > gas |
| 15 | 235 | 1.42×10^-2 | 4.33×10^-3 | 4.0×10^-5 | 3.29 | USL > gas |
| 20 | 259 | 2.53×10^-2 | 5.24×10^-3 | 7.1×10^-5 | 4.83 | USL > gas |
| 30 | 296 | 5.70×10^-2 | 6.87×10^-3 | 1.6×10^-4 | 8.29 | USL > gas |
| 50 | 351 | 1.58×10^-1 | 9.66×10^-3 | 4.5×10^-4 | 16.4 | USL-DOMINATED |
| 100 | 443 | 6.33×10^-1 | 1.53×10^-2 | 1.8×10^-3 | 41.3 | USL-DOMINATED |

### Key observations

1. **The crossover (USL = gas) is at ~7 fg (182 nm diameter).** Confirmed from Delta-Prime.

2. **USL/gas ratio grows as m^{4/3}.** At 10 fg: ratio ≈ 2. At 50 fg: ratio ≈ 16. At 100 fg: ratio ≈ 41.

3. **BB emission remains negligible** across the entire range (always <2% of gas). BB emission scales as m^2, same as USL, so it never catches up unless T_int rises dramatically.

4. **Gas collisions are the sole environmental constraint** at every mass point. The ranking of channels never changes.

---

## Part III — Protocol Feasibility Scaling

### The critical metric: expansion ratio

The zero-point motion of a trapped particle is:
```
x_zpf = sqrt(hbar / (2 m omega_trap))
```

To create a spatial superposition of size l = 10 nm, the wavepacket must be expanded from x_zpf to l. The expansion ratio l/x_zpf is the key protocol-difficulty metric.

| m (fg) | x_zpf (pm) | Expansion ratio (l/x_zpf) | Difficulty |
|:------:|:----------:|:-------------------------:|:----------:|
| 3 | 5.3 | 1,891 | HARD |
| 5 | 4.1 | 2,441 | HARD |
| 7 | 3.5 | 2,888 | HARD |
| **10** | **2.9** | **3,452** | **VERY HARD** |
| 15 | 2.4 | 4,228 | VERY HARD |
| 20 | 2.0 | 4,882 | VERY HARD |
| 30 | 1.7 | 5,979 | VERY HARD |
| **50** | **1.3** | **7,719** | **VERY HARD** |
| 100 | 0.9 | 10,916 | EXTREMELY HARD |

The expansion ratio grows as m^{1/2}. Going from 10 fg to 50 fg increases it by √5 ≈ 2.2×.

### Inverted potential protocol

The inverted-potential (anti-trap) technique (Bonvin et al. 2025, arXiv:2503.20707) provides exponential wavepacket expansion:
```
sigma(t) ~ x_zpf × exp(omega_inv × t)
t_inv = (1/omega_inv) × ln(l / x_zpf)
```

At omega_inv = omega_trap = 2π × 100 kHz:

| m (fg) | t_creation (μs) | Gas decoherence during creation | Free-fall during creation |
|:------:|:----------------:|:-------------------------------:|:-------------------------:|
| 3 | 12.0 | 1.8×10^-8 (negligible) | 0.7 nm |
| 10 | 13.0 | 4.3×10^-8 (negligible) | 0.8 nm |
| 50 | 14.2 | 1.4×10^-7 (negligible) | 1.0 nm |
| 100 | 14.8 | 2.3×10^-7 (negligible) | 1.0 nm |

**Critical finding:** The inverted-potential protocol makes the creation time nearly mass-independent (~12-15 μs). Gas decoherence during creation is utterly negligible (< 10^-7). Free fall during creation is < 1 nm. **The creation phase is NOT the bottleneck at any mass in the scan range.**

### What IS the protocol bottleneck?

The difficulty is not in the creation time, but in:

1. **The expansion ratio itself.** Expanding a wavepacket by 3,000-10,000× requires exquisite control of the inverted potential. Any anharmonicity, timing jitter, or noise during the 13 μs expansion pulse corrupts the quantum state. The tolerance scales inversely with the expansion ratio.

2. **Recombination and readout.** After the superposition is created, the branches must be recombined (or their interference pattern read out). This requires either:
   - A second inverted pulse to recombine (Mach-Zehnder), demanding matched fidelity
   - Talbot-Lau grating readout, which requires specific grating periods
   - Direct position-resolved detection, which must resolve ~nm features

3. **Free evolution time.** The 10 s interrogation time during which the USL acts requires free fall of ~490 m (ground) or microgravity (space/drop tower). This is mass-independent.

### SUPER-MARIO achievable separation

The SUPER-MARIO protocol (PNAS 2024) targets particles of ~10^8 amu (~170 fg) and claims several-nm delocalization with ms-timescale protocols. The achievable separation scales roughly as m^{-1/6} for fixed optics, giving:

| m (fg) | SM separation (nm) | Reaches 10 nm? |
|:------:|:------------------:|:--------------:|
| 3 | 4.2 | No |
| 10 | 3.4 | No |
| 50 | 2.6 | No |
| 100 | 2.3 | No |

**SUPER-MARIO as published does NOT achieve 10 nm for any mass in our range** at the published optical parameters. The inverted-potential or modified-MARIO protocols would be needed. This is a protocol R&D question, not a fundamental obstacle.

### Stern-Gerlach scaling (for nanodiamonds)

SG separation scales as 1/m. At m = 10 fg: Δx_SG ~ 100 nm (plenty). At m = 100 fg: Δx_SG ~ 10 nm (marginal). SG has favorable scaling for this range but requires magnetic nanodiamonds, not silica.

---

## Part IV — True Optimum Window

### Theory-only optimum

USL/gas ∝ m^{4/3}: **monotonically increasing with mass.** There is no decoherence-driven upper limit in the 3-100 fg range. Even at 100 fg, gas is only 1.5×10^-2 s^-1 while USL is 0.63 s^-1 (ratio 41).

Theory-only optimum: **largest mass achievable.**

### Protocol-limited optimum

The combined figure of merit (USL/gas ratio × protocol feasibility penalty from expansion ratio):

```
FoM = (USL/gas) × exp(-(expansion_ratio - 1000) / 3000)
```

| m (fg) | USL/gas | Expansion ratio | FoM |
|:------:|:-------:|:---------------:|:---:|
| 3 | 0.39 | 1,891 | 0.29 |
| 7 | 1.19 | 2,888 | 0.63 |
| 10 | 1.92 | 3,452 | 0.85 |
| 15 | 3.29 | 4,228 | 1.12 |
| 20 | 4.83 | 4,882 | 1.32 |
| 30 | 8.29 | 5,979 | 1.58 |
| 40 | 12.2 | 6,904 | 1.70 |
| **50** | **16.4** | **7,719** | **1.74** | ← PEAK |
| 70 | 25.7 | 9,133 | 1.71 |
| 100 | 41.3 | 10,916 | 1.51 |

**Protocol-limited optimum: ~50 fg (351 nm diameter).** The FoM peaks because the USL advantage (m^{4/3}) finally saturates against the exponential expansion-ratio penalty (m^{1/2}). Above 50 fg, the penalty degrades the FoM faster than the USL signal improves it.

### The two optima disagree

| | Theory-only | Protocol-limited |
|---|---|---|
| Optimal mass | ∞ (no ceiling) | ~50 fg |
| USL/gas at optimum | unbounded | 16.4 |
| Expansion ratio | irrelevant | 7,719 |
| Signal strength | large | strong |

The difference reflects the fact that protocol difficulty grows as m^{1/2} while signal grows as m^{4/3} — the exponents are different, so they balance at a finite mass.

---

## Part V — Practical Go/No-Go Thresholds

### Milestone ladder

| Threshold | Mass | Diameter | USL/gas | Notes |
|-----------|:----:|:--------:|:-------:|-------|
| USL first exceeds gas | 7 fg | 182 nm | 1.19 | Minimum mass for any signal |
| Visibility contrast > 1% (ground) | 12 fg | 218 nm | 2.44 | 1.3% contrast, ~54k runs |
| USL dominates gas by 3× | 15 fg | 235 nm | 3.29 | Clear signal, ~22k runs |
| Contrast > 5% (ground) | 25 fg | 279 nm | 6.50 | 5.5% contrast, ~3k runs |
| N_runs < 1000 (ground) | 40 fg | 326 nm | 12.2 | ~500 runs needed |
| **Optimal FoM** | **50 fg** | **351 nm** | **16.4** | **~220 runs (ground)** |
| N_runs < 30 (ground) | 100 fg | 443 nm | 41.3 | 25 runs, but extremely hard expansion |

### Does the window widen above 10 fg?

**YES.** The window widens substantially. At 10 fg, the signal is marginal (USL/gas = 2, ~111k runs for ground-based). At 50 fg, it is strong (USL/gas = 16, ~220 runs). The improvement is a factor of ~500 in required runs.

### Where does protocol difficulty become limiting?

The expansion ratio passes 5,000× at m ≈ 25 fg and 10,000× at m ≈ 100 fg. No existing experiment has demonstrated expansion ratios above ~1,000× (Bonvin et al. achieved 43.4 nm / 45.6 pm ≈ 950× at 1.95 fg). The required expansion ratio for 10 nm superposition at ANY mass in our range exceeds demonstrated capability.

**However:** the expansion ratio is a TECHNICAL challenge, not a physical impossibility. The inverted-potential technique is well-understood physically (Bonvin et al. 2025) and the ~12 μs creation time means decoherence during creation is negligible. The question is control fidelity of the inverted potential, not any fundamental barrier.

### Preferred target mass

**15-50 fg (235-351 nm diameter).** This range offers:
- USL/gas = 3-16 (clear signal above gas noise)
- Expansion ratio = 4,200-7,700 (hard but not extreme)
- Required runs = 200-22,000 (feasible for dedicated experiment)
- Particle fabrication: straightforward (commercial nanospheres)
- Optical trapping: demonstrated for particles up to micron scale

Within this range, **20-30 fg** represents the best compromise between signal strength and protocol difficulty for a first-generation experiment.

---

## Part VI — Final Verdict

### Classification

**higher_mass_region_widens_the_test_window**

The 10 fg Blueprint reference is not near-optimal — it sits at the lower edge of the viable window where the USL signal barely exceeds gas noise. The test window extends upward to ~50 fg before protocol difficulty (expansion ratio) turns the figure-of-merit back over. The practical sweet spot is 20-30 fg (260-300 nm diameter silica), where the USL exceeds gas by 5-8× and the expansion ratio (~5,000-6,000) is at the edge of near-term technical capability.

### The mass window

```
Lower edge:   7 fg  (182 nm)  — USL first exceeds gas
Viable:      10 fg  (206 nm)  — USL/gas = 2 (marginal signal)
Sweet spot:  20-30 fg (260-300 nm)  — USL/gas = 5-8, expansion ratio ~5000-6000
Peak FoM:    50 fg  (351 nm)  — USL/gas = 16, expansion ratio ~7700
Upper edge: ~100 fg (443 nm)  — USL/gas = 41 but expansion ratio > 10000
```

### Pressure sensitivity

At the optimal 50 fg, even modest pressure improvements dramatically boost the ratio:

| Pressure (Pa) | USL/gas | Needed runs (ground) |
|:-:|:-:|:-:|
| 10^-12 | 1.6 | ~170,000 |
| 10^-13 | 16 | ~220 |
| 10^-14 | 164 | ~25 |

Going from 10^-13 to 10^-14 Pa would make even 10 fg particles give a clear, unambiguous signal.

### Public-Facing Paragraph

GRUT II Epsilon-Prime scans the mass range 3-100 fg to find the true optimal operating point for a USL test. The USL signal grows as m^2 while gas decoherence grows as m^(2/3), so heavier particles give stronger signals — but the wavepacket expansion ratio required to create a 10 nm superposition also grows as m^(1/2), imposing a protocol-difficulty penalty. The combined figure of merit peaks at ~50 fg (351 nm silica diameter), where the USL exceeds the gas noise floor by 16× and would produce a clear signal in ~220 experimental runs on a ground-based 10 m drop tower. The practical sweet spot for a first-generation experiment is 20-30 fg (260-300 nm diameter), where the USL/gas ratio of 5-8 is robust while the expansion ratio of ~5,000-6,000 is at the edge of near-term capability. The 10 fg Blueprint reference sits at the lower margin of the viable window; the window widens substantially above it. The sole environmental bottleneck remains gas pressure at 10^-13 Pa.

### Internal Doctrine Paragraph

The optimal experimental target for the USL is not the minimum-mass crossover (7 fg) but the peak of the signal-to-difficulty figure of merit at ~50 fg. However, this mass requires an expansion ratio of ~8,000, which has not been demonstrated. The current experimental record is ~1,000× (Bonvin et al. 2025 at 1.95 fg). The first realistic target is therefore the lowest mass where the USL signal is unambiguous: **20-30 fg, where USL/gas = 5-8 and the expansion ratio = 5,000-6,000.** If the expansion ratio can be pushed to ~5,000 through improved inverted-potential control (a factor of 5 beyond current), the USL test becomes viable. This is the single technical milestone that determines whether the program has a real experimental path: demonstration of wavepacket expansion by ~5,000× from the ground state of a ~20 fg particle, in a dark cryogenic UHV environment, with the quantum state surviving the expansion.

### Next Forced Move

The mass optimization is complete. The program has now identified:
- A specific theory (USL: Lambda = Gm^2/(hbar l))
- A specific experimental platform (20-50 fg silica nanosphere)
- A specific bottleneck (wavepacket expansion ratio ~5000×)
- A specific environmental floor (gas collisions at 10^-13 Pa)
- A specific signal (USL/gas = 5-16, visibility contrast 3-20%)

The next forced move is **GRUT II Zeta-Prime — Terminal Consolidation of the Quantum-Sector Experimental Roadmap**: collect all stages (Alpha-Prime through Epsilon-Prime) into a single coherent experimental specification document, with one target platform, one predicted signal, one timeline, and one decision tree for go/no-go. This is the terminal document for the GRUT-II quantum prediction sector.

---

*GRUT II Epsilon-Prime complete. Verdict: higher_mass_region_widens_the_test_window. The viable mass window extends from 7 fg (marginal) to ~100 fg (protocol-limited). Peak FoM at 50 fg (USL/gas = 16.4, expansion ratio 7719). Practical sweet spot: 20-30 fg (USL/gas = 5-8, expansion ratio 5000-6000). The window widens substantially above the 10 fg reference. The sole bottleneck is wavepacket expansion fidelity: demonstration of ~5000× expansion from ground state in dark cryogenic UHV. If achieved, the USL produces a clear, statistically significant signal in ~200-3000 experimental runs on a ground-based platform.*
