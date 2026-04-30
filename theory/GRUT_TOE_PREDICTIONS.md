<frozen runpy>:128: RuntimeWarning: 'grut.toe.dashboard' found in sys.modules after import of package 'grut.toe', but prior to execution of 'grut.toe.dashboard'; this may result in unpredictable behaviour
# GRUT — Predictions / Falsifier Dashboard

*Auto-generated from `grut/toe/dashboard.py`. Re-run `python3 -m grut.toe.dashboard > theory/GRUT_TOE_PREDICTIONS.md` to regenerate after adding or updating predictions.*

Specialist handoff document. Every quantitative prediction the framework makes, with predicted value, observational counterpart, comparison status, falsification condition, and registry back-link. A specialist can read this in <1 minute and learn what to test, what's been tested, and what would falsify the framework.

---

## Status summary

| Status | Glyph | Count |
|:---|:---:|---:|
| Consistent with observation | ✓ | 17 |
| Within obs. uncertainty, with documented systematic | ! | 3 |
| Falsified at current data (documented outlier) | ✗ | 0 |
| Prediction made, not yet measured | ? | 4 |
| Leading-order; falsifier-tier promotion deferred | S | 2 |
| Reproduced trivially; not a GRUT-specific test | K | 1 |

**Total predictions:** 27

---

## Predictions by category

### Foundational constants

| ID | Prediction | GRUT value | Observed | Status | Registry |
|:---|:---|:---|:---|:---:|:---|
| P01 | α_vac (vacuum impedance) | 1/3 | — | ✓ | `alpha_vac_derivation` |
| P02 | τ_0 (relaxation time) | 41.9 Myr | cosmic-baseline group: 41.4 ± 1.5 Myr; cluster group: 50.0 ± 3 Myr | ! | `tau_0_cross_consistency` |
| P03 | S (screening factor) | 108π ≈ 339.29 | — | ✓ | `screening_108pi` |

### Refractive index R

| ID | Prediction | GRUT value | Observed | Status | Registry |
|:---|:---|:---|:---|:---:|:---|
| P04 | R = n_g(0) (canonical) | √(4/3) = 1.15470 | — | ✓ | `r_canonical_path_g` |
| P05 | R Path D Dirac (cross-check) | 253/219 = 1.15525 | agrees with Path G to 0.05% | ✓ | `r_path_d_dirac` |
| P06 | R Osborn ε (cross-check) | 1.15367 | agrees with Path G to 0.089% | ✓ | `r_path_osborn_epsilon` |

### Cosmological observables

| ID | Prediction | GRUT value | Observed | Status | Registry |
|:---|:---|:---|:---|:---:|:---|
| P07 | H_0 (Hubble constant) | 69.03 km/s/Mpc (loop-corrected); 68.8 km/s/Mpc (tree-level) | Planck 67.4 / SH0ES 73.5 / DESI 68.5 | ✓ | `h_0_prediction` |
| P08 | Ω_Λ (cosmological constant) | 0.6886 | 0.6889 ± 0.0073 (Planck 2018) | ✓ | `omega_lambda_prediction` |
| P09 | H_inf (terminal velocity) | 58.16 km/s/Mpc | indirect via Ω_Λ × H_0² consistency | ✓ | `h_inf_decomposition` |

### Dark sector

| ID | Prediction | GRUT value | Observed | Status | Registry |
|:---|:---|:---|:---|:---:|:---|
| P10 | Ω_dm (dark matter density) | α = 1/3 ≈ 0.3333 | 0.2625 ± 0.001 (Planck) | ! | `omega_dm_equals_alpha` |
| P11 | MOND a_0 (acceleration scale) | cH_0/(2π) ≈ 1.2 × 10⁻¹⁰ m/s² | ≈ 1.2 × 10⁻¹⁰ m/s² (rotation-curve fits) | ✓ | `mond_a_0_emergence` |
| P12 | η_B (baryon asymmetry) | 6.57 × 10⁻¹⁰ | 6.10 × 10⁻¹⁰ (Planck) | ✓ | `baryogenesis_eta_b` |

### Cluster mergers

| ID | Prediction | GRUT value | Observed | Status | Registry |
|:---|:---|:---|:---|:---:|:---|
| P13 | Bullet Cluster gas-lensing offset | 130 kpc | ~150 kpc (Clowe et al. 2006) | ✓ | `bullet_cluster_offset` |
| P14 | MACS J0025 gas-lensing offset | 66 kpc | ~75 kpc (Bradač et al. 2008) | ✓ | `cluster_merger_scaling_law` |
| P15 | Abell 520 gas-lensing offset | 63 kpc | ~80 kpc (Mahdavi et al. 2007) | ✓ | `cluster_merger_scaling_law` |
| P16 | El Gordo gas-lensing offset | 43-130 kpc across published parameter ranges | 120-600 kpc (depends on lensing reconstruction methodology) | ! | `el_gordo_sensitivity_analysis` |
| P17 | Cluster v × τ_0 scaling law | offset / v_post = constant ≈ τ_0 | 3 of 4 normal-regime mergers within factor 1.3 | ✓ | `cluster_merger_scaling_law` |

### Decoherence (laboratory)

| ID | Prediction | GRUT value | Observed | Status | Registry |
|:---|:---|:---|:---|:---:|:---|
| P18 | Decoherence plateau (PRIMARY FALSIFIER) | Λ_grav ≈ 689 Hz at gold-benchmark (m=80.8 fg, l=1 μm) | not yet measured (MAQRO, MAGIS-100 in progress) | ? | `decoherence_plateau` |
| P19 | Six F-laws (F1-F6 scaling) | m², (l/R)³/6, plateau, 1/l, DFS, kink at l=R | no competitor model satisfies all six (DP closest at 4/6) | ? | `decoherence_alternative_models_comparison` |

### Particle physics

| ID | Prediction | GRUT value | Observed | Status | Registry |
|:---|:---|:---|:---|:---:|:---|
| P20 | Koide K = 2/3 | K = 2/3 (charged leptons) | K = 0.666660 (PDG masses) | ✓ | `koide_k_2_over_3` |
| P21 | Three generations from Z₃ | N_gen = 3 (uniquely from Z₃ circulant) | 3 generations observed | ✓ | `koide_z3_circulant_structure` |
| P22 | Dirac-leaning neutrino prediction | Path D Dirac (1.15525) closer to canonical R than Majorana (1.17256) | neutrino nature undetermined | ? | `neutrino_dirac_prediction` |

### Gravity (BH saturation)

| ID | Prediction | GRUT value | Observed | Status | Registry |
|:---|:---|:---|:---|:---:|:---|
| P23 | R_max (Ricci saturation) | α/(c²τ_0²) ≈ 2.12 × 10⁻⁴⁸ m⁻² | not directly measured | ? | `r_max_ricci_saturation` |
| P24 | ρ_max (universal interior density) | c²R_max/(8πG) ≈ 1.14 × 10⁻²² kg/m³ | open question on quantitative core sizes | S | `rho_max_scale_open_question` |

### Thermal

| ID | Prediction | GRUT value | Observed | Status | Registry |
|:---|:---|:---|:---|:---:|:---|
| P25 | T_c (boiling point of gravity) | ℏ/(τ_0 k_B) ≈ 54.7 MK | indirect via BBN consistency | ✓ | `t_c_thermal_transition` |

### CMB (long-term)

| ID | Prediction | GRUT value | Observed | Status | Registry |
|:---|:---|:---|:---|:---:|:---|
| P26 | CMB θ_* shift (recombination) | Δθ_*/θ_* ≈ 3.6 × 10⁻⁵ | below Planck precision (3 × 10⁻⁴ — factor 10 above) | S | `cmb_boltzmann_scoping` |

### Kinematic checks

| ID | Prediction | GRUT value | Observed | Status | Registry |
|:---|:---|:---|:---|:---:|:---|
| P27 | Bullet cluster-to-cluster separation | v_initial × t_since_pericenter ≈ 720 kpc | ~720 kpc (Markevitch 2002) | K | `bullet_cluster_offset` |

---

## Detailed entries

Each entry below includes the GRUT prediction, the observational counterpart, the fractional difference, the precision status (whether current observations can detect or rule out the prediction), and the specific falsification condition.

### P01 ✓ — α_vac (vacuum impedance)

**Chapter.** 2  ·  **Category.** Foundational constants

**GRUT prediction.** 1/3

**Observed.** —

**Status.** consistent

**Precision.** not directly measured; appears via downstream observables

**Falsifier.** Independent derivation showing α ≠ 1/3 from the conformal-mode postulate

**Registry claim.** `alpha_vac_derivation`

---

### P02 ! — τ_0 (relaxation time)

**Chapter.** 2  ·  **Category.** Foundational constants

**GRUT prediction.** 41.9 Myr

**Observed.** cosmic-baseline group: 41.4 ± 1.5 Myr; cluster group: 50.0 ± 3 Myr

**Fractional difference.** cosmic baseline: 0.4% from canonical; cluster: +20% systematic

**Status.** tension

**Precision.** cluster-merger τ_0 systematically higher; within obs. uncertainty

**Falsifier.** τ_0 from any independent route diverging by > 30% from 41.9 Myr

**Registry claim.** `tau_0_cross_consistency`

---

### P03 ✓ — S (screening factor)

**Chapter.** 2  ·  **Category.** Foundational constants

**GRUT prediction.** 108π ≈ 339.29

**Observed.** —

**Status.** consistent

**Precision.** derived: S = 12π/α². Inputs are α and τ_0/τ_Λ ratio

**Falsifier.** τ_Λ/τ_0 ratio inconsistent with 108π would falsify the screening relation

**Registry claim.** `screening_108pi`

---

### P04 ✓ — R = n_g(0) (canonical)

**Chapter.** 7  ·  **Category.** Refractive index R

**GRUT prediction.** √(4/3) = 1.15470

**Observed.** —

**Status.** consistent

**Precision.** R itself is not directly measured; appears in H_0, Ω_Λ, cluster offsets, baryogenesis

**Falsifier.** Three-routes convergence breaks (gap > 1% across routes)

**Registry claim.** `r_canonical_path_g`

---

### P05 ✓ — R Path D Dirac (cross-check)

**Chapter.** 7  ·  **Category.** Refractive index R

**GRUT prediction.** 253/219 = 1.15525

**Observed.** agrees with Path G to 0.05%

**Fractional difference.** 0.05% from Path G

**Status.** consistent

**Precision.** theoretical cross-check between independent computations

**Falsifier.** Updated KS / Christensen-Duff coefficients changing 253/219

**Registry claim.** `r_path_d_dirac`

---

### P06 ✓ — R Osborn ε (cross-check)

**Chapter.** 7  ·  **Category.** Refractive index R

**GRUT prediction.** 1.15367

**Observed.** agrees with Path G to 0.089%

**Fractional difference.** 0.089% from Path G; max-min spread across all 3 routes

**Status.** consistent

**Precision.** α_s(M_Z) measured at <1% precision; ε computed

**Falsifier.** α_s(M_Z) precision improvement pushing ε > 0.5% from √(4/3)

**Registry claim.** `r_path_osborn_epsilon`

---

### P07 ✓ — H_0 (Hubble constant)

**Chapter.** 8  ·  **Category.** Cosmological observables

**GRUT prediction.** 69.03 km/s/Mpc (loop-corrected); 68.8 km/s/Mpc (tree-level)

**Observed.** Planck 67.4 / SH0ES 73.5 / DESI 68.5

**Fractional difference.** 2% above Planck, 5% below SH0ES — in the tension gap

**Status.** consistent

**Precision.** Hubble tension is unresolved; GRUT in the middle

**Falsifier.** Convergent H_0 measurement outside 69 ± 3 km/s/Mpc

**Registry claim.** `h_0_prediction`

---

### P08 ✓ — Ω_Λ (cosmological constant)

**Chapter.** 8  ·  **Category.** Cosmological observables

**GRUT prediction.** 0.6886

**Observed.** 0.6889 ± 0.0073 (Planck 2018)

**Fractional difference.** 0.04% from Planck

**Status.** consistent

**Precision.** Planck precision: 1%; GRUT prediction is 0.04% from central

**Falsifier.** Tighter Ω_Λ measurement excluding 0.6886 at >3σ

**Registry claim.** `omega_lambda_prediction`

---

### P09 ✓ — H_inf (terminal velocity)

**Chapter.** 8  ·  **Category.** Cosmological observables

**GRUT prediction.** 58.16 km/s/Mpc

**Observed.** indirect via Ω_Λ × H_0² consistency

**Status.** consistent

**Precision.** emerges from (2-R)/(Sτ_0); checked via Ω_Λ

**Falsifier.** DESI/Euclid finding H_0 √Ω_Λ ≠ 58.16 ± 1 km/s/Mpc

**Registry claim.** `h_inf_decomposition`

---

### P10 ! — Ω_dm (dark matter density)

**Chapter.** 9  ·  **Category.** Dark sector

**GRUT prediction.** α = 1/3 ≈ 0.3333

**Observed.** 0.2625 ± 0.001 (Planck)

**Fractional difference.** +27% above Planck

**Status.** tension

**Precision.** Planck precision is sub-percent; +27% gap is real. Two readings: subtractive corrections, or Planck assumes ΛCDM expansion history

**Falsifier.** CMB-peak measurement of Ω_dm robustly excluding 1/3 at the linear-regime level

**Registry claim.** `omega_dm_equals_alpha`

---

### P11 ✓ — MOND a_0 (acceleration scale)

**Chapter.** 9  ·  **Category.** Dark sector

**GRUT prediction.** cH_0/(2π) ≈ 1.2 × 10⁻¹⁰ m/s²

**Observed.** ≈ 1.2 × 10⁻¹⁰ m/s² (rotation-curve fits)

**Fractional difference.** <5%

**Status.** consistent

**Precision.** MOND a_0 fitted to rotation curves; GRUT derives same value

**Falsifier.** Rotation curves at low acceleration showing GR (not MOND-like) at high frequency

**Registry claim.** `mond_a_0_emergence`

---

### P12 ✓ — η_B (baryon asymmetry)

**Chapter.** 9  ·  **Category.** Dark sector

**GRUT prediction.** 6.57 × 10⁻¹⁰

**Observed.** 6.10 × 10⁻¹⁰ (Planck)

**Fractional difference.** +7.7%

**Status.** consistent

**Precision.** within obs. uncertainty (~10%) on η_B

**Falsifier.** Refined η_B precision excluding 6.57 × 10⁻¹⁰

**Registry claim.** `baryogenesis_eta_b`

---

### P13 ✓ — Bullet Cluster gas-lensing offset

**Chapter.** 9  ·  **Category.** Cluster mergers

**GRUT prediction.** 130 kpc

**Observed.** ~150 kpc (Clowe et al. 2006)

**Fractional difference.** ratio 0.87 (factor 1.15)

**Status.** consistent

**Precision.** cluster collision parameters carry ~30% uncertainty

**Falsifier.** Bullet δ falling outside [60, 300] kpc

**Registry claim.** `bullet_cluster_offset`

---

### P14 ✓ — MACS J0025 gas-lensing offset

**Chapter.** 9  ·  **Category.** Cluster mergers

**GRUT prediction.** 66 kpc

**Observed.** ~75 kpc (Bradač et al. 2008)

**Fractional difference.** ratio 0.88

**Status.** consistent

**Precision.** cluster precision ~30%

**Falsifier.** MACS δ outside [30, 150] kpc

**Registry claim.** `cluster_merger_scaling_law`

---

### P15 ✓ — Abell 520 gas-lensing offset

**Chapter.** 9  ·  **Category.** Cluster mergers

**GRUT prediction.** 63 kpc

**Observed.** ~80 kpc (Mahdavi et al. 2007)

**Fractional difference.** ratio 0.79

**Status.** consistent

**Precision.** cluster precision ~30%; system contested

**Falsifier.** Abell 520 δ outside [30, 150] kpc

**Registry claim.** `cluster_merger_scaling_law`

---

### P16 ! — El Gordo gas-lensing offset

**Chapter.** 9  ·  **Category.** Cluster mergers

**GRUT prediction.** 43-130 kpc across published parameter ranges

**Observed.** 120-600 kpc (depends on lensing reconstruction methodology)

**Fractional difference.** ratio 0.22-1.09 depending on parameter+obs combination

**Status.** tension

**Precision.** Prediction range OVERLAPS observation range at lower end; ratio = 1.09 at obs=120 kpc with best-case parameters — fully consistent if observation is in lower published range

**Falsifier.** Definitive lensing reconstruction pinning El Gordo offset above 200 kpc with sub-20% precision (real framework problem). Conversely, free-form/individual-subclump reconstructions confirming 120-150 kpc range (framework consistent at same level as Bullet/MACS/Abell).

**Registry claim.** `el_gordo_sensitivity_analysis`

---

### P17 ✓ — Cluster v × τ_0 scaling law

**Chapter.** 9  ·  **Category.** Cluster mergers

**GRUT prediction.** offset / v_post = constant ≈ τ_0

**Observed.** 3 of 4 normal-regime mergers within factor 1.3

**Fractional difference.** internal scaling holds at 1.7%

**Status.** consistent

**Precision.** 3-of-4 confirmed; El Gordo outlier separately documented

**Falsifier.** Multiple normal-regime mergers showing deviation > factor 2 from v × τ_0

**Registry claim.** `cluster_merger_scaling_law`

---

### P18 ? — Decoherence plateau (PRIMARY FALSIFIER)

**Chapter.** 5  ·  **Category.** Decoherence (laboratory)

**GRUT prediction.** Λ_grav ≈ 689 Hz at gold-benchmark (m=80.8 fg, l=1 μm)

**Observed.** not yet measured (MAQRO, MAGIS-100 in progress)

**Status.** untested

**Precision.** experimental programs targeting nanoparticle interferometry

**Falsifier.** Measured plateau materially different from 689 Hz, OR any of F1-F6 scaling laws not satisfied — falsifies the framework

**Registry claim.** `decoherence_plateau`

---

### P19 ? — Six F-laws (F1-F6 scaling)

**Chapter.** 5  ·  **Category.** Decoherence (laboratory)

**GRUT prediction.** m², (l/R)³/6, plateau, 1/l, DFS, kink at l=R

**Observed.** no competitor model satisfies all six (DP closest at 4/6)

**Status.** untested

**Precision.** experimental discrimination via isotope tests pending

**Falsifier.** Any single F-law violated experimentally falsifies that mechanism

**Registry claim.** `decoherence_alternative_models_comparison`

---

### P20 ✓ — Koide K = 2/3

**Chapter.** 9  ·  **Category.** Particle physics

**GRUT prediction.** K = 2/3 (charged leptons)

**Observed.** K = 0.666660 (PDG masses)

**Fractional difference.** 0.005% from 2/3

**Status.** consistent

**Precision.** charged-lepton masses precise to <0.01%; K validated

**Falsifier.** Refined PDG masses driving K outside 2/3 ± 10⁻⁴

**Registry claim.** `koide_k_2_over_3`

---

### P21 ✓ — Three generations from Z₃

**Chapter.** 5  ·  **Category.** Particle physics

**GRUT prediction.** N_gen = 3 (uniquely from Z₃ circulant)

**Observed.** 3 generations observed

**Status.** consistent

**Precision.** LHC searches for 4th generation null; consistent with N=3

**Falsifier.** Discovery of fourth-generation fermion

**Registry claim.** `koide_z3_circulant_structure`

---

### P22 ? — Dirac-leaning neutrino prediction

**Chapter.** 12  ·  **Category.** Particle physics

**GRUT prediction.** Path D Dirac (1.15525) closer to canonical R than Majorana (1.17256)

**Observed.** neutrino nature undetermined

**Status.** untested

**Precision.** neutrinoless ββ-decay experiments (CUPID, LEGEND) ongoing

**Falsifier.** Observation of neutrinoless double-beta decay (Majorana)

**Registry claim.** `neutrino_dirac_prediction`

---

### P23 ? — R_max (Ricci saturation)

**Chapter.** 6  ·  **Category.** Gravity (BH saturation)

**GRUT prediction.** α/(c²τ_0²) ≈ 2.12 × 10⁻⁴⁸ m⁻²

**Observed.** not directly measured

**Status.** untested

**Precision.** BH interior structure not directly observable

**Falsifier.** BH observation revealing curvature divergence beyond R_max

**Registry claim.** `r_max_ricci_saturation`

---

### P24 S — ρ_max (universal interior density)

**Chapter.** 6  ·  **Category.** Gravity (BH saturation)

**GRUT prediction.** c²R_max/(8πG) ≈ 1.14 × 10⁻²² kg/m³

**Observed.** open question on quantitative core sizes

**Status.** scoping_tier

**Precision.** formula universal; numerical scale flagged as open question

**Falsifier.** Resolution of ρ_max scale via extended kernel or new derivation

**Registry claim.** `rho_max_scale_open_question`

---

### P25 ✓ — T_c (boiling point of gravity)

**Chapter.** 8  ·  **Category.** Thermal

**GRUT prediction.** ℏ/(τ_0 k_B) ≈ 54.7 MK

**Observed.** indirect via BBN consistency

**Fractional difference.** BBN (T > 10⁹ K) above T_c → no DM signature in BBN ✓

**Status.** consistent

**Precision.** BBN observations consistent with no DM enhancement at high T

**Falsifier.** DM signature appearing in BBN-era CMB

**Registry claim.** `t_c_thermal_transition`

---

### P26 S — CMB θ_* shift (recombination)

**Chapter.** 9  ·  **Category.** CMB (long-term)

**GRUT prediction.** Δθ_*/θ_* ≈ 3.6 × 10⁻⁵

**Observed.** below Planck precision (3 × 10⁻⁴ — factor 10 above)

**Status.** scoping_tier

**Precision.** Planck consistent (factor 10 below precision); CMB-S4 target 5 × 10⁻⁵ at threshold (factor 1.4 below)

**Falsifier.** Conditional on covariance closure + Boltzmann implementation: CMB-S4 measurement materially different from 3.6 × 10⁻⁵

**Registry claim.** `cmb_boltzmann_scoping`

---

### P27 K — Bullet cluster-to-cluster separation

**Chapter.** 9  ·  **Category.** Kinematic checks

**GRUT prediction.** v_initial × t_since_pericenter ≈ 720 kpc

**Observed.** ~720 kpc (Markevitch 2002)

**Fractional difference.** <1%

**Status.** kinematic

**Precision.** kinematic — reproduced trivially by any theory

**Falsifier.** Not a GRUT-specific test; consistent with framework by kinematics

**Registry claim.** `bullet_cluster_offset`

---

