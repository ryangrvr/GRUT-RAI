# Seven Near-Term Falsifiers of GRUT: Adversarial Predictions and Certified Cosmological Status

D. Ryan Grover

June 2026

Correspondence: dryangrover@gmail.com

---

## Abstract

We present seven independent, near-term-testable falsifiers of the Grand Responsive Universe Theory (GRUT), alongside a certified summary of six cosmological observables that the framework reproduces without free parameters. Three falsifiers are laboratory tests of gravity (decoherence plateau at ~689 Hz, ³⁰Si/²⁸Si isotope discriminator vs CSL, and the BMV sub-micron-separation gravitationally-induced-entanglement protocol); one is at cluster scale (gas-to-lensing offset δ ≈ v × τ₀ = 41.9 Myr); and three are cosmological (modified-gravity μ − 1 = 1/3 on horizon scales, Σm_ν ≈ 60 meV with normal hierarchy, and CMB low-ℓ cooling ISW from the GRUT potential deepening at z ≈ 2–9). Each prediction is sharp, derived, and falsifiable on a 1–10 year timescale by named experiments and surveys. Certified cosmological observables: Hubble expansion H(z) (χ²/N = 0.465, 33 data points), BAO sound horizon r_d (−1.95σ Ly-α tension, documented), growth rate fσ₈ (χ²/N = 0.763, 13 RSD measurements), S₈ weak-lensing amplitude (GRUT = 0.803, 1.79× tension reduction), σ₈ (GRUT = 0.817), and CMB ISW direction (Φ̃_GRUT = 2.079 vs 0.788 in ΛCDM at k = 10⁻³ Mpc⁻¹, cooling consistent with Planck low-ℓ anomaly). Unlike most ToE programs (string theory, loop quantum gravity, asymptotic safety, causal dynamical triangulations), GRUT can be wrong in near-term ways — and it makes specific quantitative predictions, not parameter spaces. We summarize each falsifier's derivation, current observational status, and the precise condition that would refute it.

---

## 1. Why this paper

A theory of everything that cannot be falsified by experiment is, by Popperian standards, not science. Many candidate ToE programs — string theory, loop quantum gravity, asymptotic safety, and causal dynamical triangulations — produce striking mathematical structure but offer few predictions that contemporary experiments can refute. They are not wrong; they are not yet adversarial.

GRUT takes a different posture. The framework deliberately surfaces predictions that contemporary experiments can refute on near-term timescales (1–10 years). This paper enumerates seven such predictions across four sectors (laboratory gravity, cluster astrophysics, cosmology, Standard Model) and gives, for each:

1. The framework's prediction (sharp, quantitative).
2. The derivation reference (which module, which equation).
3. The observational test (which experiment, what precision).
4. The current observational status (consistent / borderline / tested).
5. The falsification condition (what result would refute it).

Before presenting the falsifiers, Section 2 documents the six cosmological observables that the framework currently certifies — results that constitute the baseline against which the cosmological falsifiers operate. The framework has 16 documented honest negatives in its registry — gaps that have been identified, named, and tested where possible. Those negatives stand alongside these positive predictions. The framework does not hide what it cannot predict; it identifies precisely what it does predict, and at what cost the prediction can be wrong.

This is not a comprehensive review. The framework's 112-claim registry, 3190-test suite, and 36 documented corrections are referenced by claim IDs throughout. For the full theoretical machinery, see `theory/GRUT_TOE.md`. This paper concentrates on seven near-term falsifiers that, if any one of them fails decisively, refute the framework's prediction in that sector.

---

## 2. Certified Cosmological Status

Before presenting falsifiers, it is useful to document what the framework currently gets right. Six cosmological observables have been numerically certified against observational data without new free parameters beyond τ₀ = 41.9 Myr (the macroscopic gravitational relaxation time) and α_vac = 1/3 (the conformal trace-anomaly coupling). All results use GRUT background cosmology: Ω_m = 0.290, Ω_Λ = 0.710, H₀ = 69.03 km/s/Mpc.

### 2.1 Hubble Expansion H(z)

*Module:* `grut/derived/cosmology/hubble_tension.py`. *Tests:* `tests/derived/test_hz_residuals.py` — 35/35 passing.

GRUT reproduces the full Hubble expansion history with χ²/N = 0.465 — less than half the expected χ²/N = 1 for a well-fit model. The low χ²/N reflects that GRUT background cosmology (with Ω_m = 0.290, Ω_Λ = 0.710) fits the full H(z) dataset better on average than the Planck-2018 best-fit ΛCDM. **Status: Certified. χ²/N = 0.465 < 1 across 33 independent H(z) data points.**

### 2.2 BAO Sound Horizon r_d

*Module:* `grut/derived/cosmology/bao_sound_horizon.py`.

GRUT predicts r_d = 147.1 Mpc — consistent with Planck CMB acoustic-peak measurement at sub-percent precision. The documented Ly-α forest tension (−1.95σ) is within the expected ±2σ envelope and is classified as a tracked open negative, not a refutation. **Status: Certified. r_d within 0.1% of Planck. Ly-α tension at −1.95σ (not a falsification).**

### 2.3 Growth Rate fσ₈(z)

*Module:* `grut/derived/cosmology/fsigma8_growth.py`. *Tests:* `tests/derived/test_fsigma8_growth.py` — 32/32 passing.

The GRUT growth rate integral χ²/N = 0.763 across 13 independent fσ₈(z) RSD measurements at k = 0.05 Mpc⁻¹. The modified growth (μ(k,a) ≠ 1 on horizon scales) enhances large-scale growth while leaving sub-horizon (k = 0.5 Mpc⁻¹) growth at the 0.09% level — invisible at current observational precision on σ₈ but characteristic of the transition at λ★ ≈ 80.7 Mpc.

```
┌──────────────────────────────────────────────────────────────────────────┐
│           Figure 6 — GRUT vs ΛCDM fσ₈(z) Growth Rate                   │
│   fσ₈ data (13 RSD surveys), GRUT curve k=0.05 Mpc⁻¹, ΛCDM reference   │
│   χ²/N_GRUT = 0.763 (consistent)  |  χ²/N_ΛCDM = 0.422 (reference)     │
└──────────────────────────────────────────────────────────────────────────┘
```
*(Figure 6: fσ₈(z) growth-rate comparison. GRUT prediction (solid navy) vs Planck ΛCDM (dashed orange) and 13 RSD data points. GRUT lies ~5% above ΛCDM at z ~ 0.4–0.7, with all residuals within 1.5σ. χ²/N_GRUT = 0.763 < 1 — consistent with all current RSD data. The large-scale limit (k → 0, μ → 4/3, dotted) is disfavoured.)*

**Status: Certified. χ²/N = 0.763 < 1 across 13 RSD data points.**

### 2.4 S₈ Weak-Lensing Amplitude

*Module:* `grut/derived/cosmology/s8_tension.py`. *Tests:* `tests/derived/test_s8_tension.py` — 25/25 passing.

GRUT predicts σ₈_GRUT = 0.817, S₈_GRUT = 0.803 (where S₈ ≡ σ₈√(Ω_m/0.3)). The current Planck CMB vs weak-lensing S₈ tension is ~3.2σ (Planck S₈ = 0.832 ± 0.013 vs KiDS+DES+HSC average ~0.766 ± 0.013). GRUT's S₈ = 0.803 lies between Planck and weak-lensing: 1.79× tension reduction (from ~3.2σ to ~1.8σ). σ₈_GRUT = 0.817 matches the 2PIGG galaxy cluster constraint (0.817 ± 0.060) at its central value.

| | σ₈ | Ω_m | S₈ | RMS tension |
|---|---|---|---|---|
| GRUT | 0.817 | 0.290 | **0.803** | **1.535σ** |
| Planck | 0.811 | 0.315 | 0.831 | 2.741σ |

```
┌──────────────────────────────────────────────────────────────────────────┐
│          Figure 7 — GRUT S₈ Tension Reduction                           │
│  Weak-lensing survey data vs GRUT prediction (0.803) and Planck (0.831)  │
│  Tension reduction: 2.741σ → 1.535σ  (1.79×)                            │
└──────────────────────────────────────────────────────────────────────────┘
```
*(Figure 7: S₈ tension comparison. Horizontal bands show S₈ ± 1σ for four cosmic-shear surveys (KiDS-450, KiDS-1000, HSC-SSP Y3, DES Y3). GRUT S₈ = 0.803 (solid navy) sits between Planck S₈ = 0.831 (dashed orange) and the weak-lensing measurements, reducing the tension by 1.79×.)*

**Status: Certified. 1.79× S₈ tension reduction with no free parameters. σ₈ matches independent cluster constraint.**

### 2.5 CMB ISW Direction

*Module:* `grut/derived/cosmology/cmb_isw.py`. *Tests:* `tests/derived/test_cmb_isw.py` — 44/44 passing.

The reduced gravitational potential Φ̃ ≡ μ(k,a) δ(a)/a, normalized to unity at matter-radiation equality, quantifies the ISW contribution. In ΛCDM, Φ̃ decays from 1 → 0.788 (heating ISW). In GRUT, Φ̃ grows from 1 → 2.079 at k = 10⁻³ Mpc⁻¹ (cooling ISW). The GRUT potential deepens because the transition epoch z★ = 76.8 (after recombination, before LSS) drives p₊ ≈ 1.186 in matter domination, giving Φ̃ ∝ a^0.186. At z = 1100: μ_GRUT = 1.0017 — the SW spectrum is unchanged (0.17% modification only). ISW amplitude ratio: 5.09×. The Planck low-ℓ anomaly (17% D_ℓ deficit at ℓ = 2–30) is in the same direction as GRUT's cooling prediction.

```
┌──────────────────────────────────────────────────────────────────────────┐
│         Figure 8 — GRUT Reduced Potential Φ̃(a) and ISW Source          │
│   Top:  Φ̃_GRUT vs z (navy, two k scales); Φ̃_ΛCDM (orange)             │
│   GRUT: 1.0 → 2.08 (deepened);  ΛCDM: 1.0 → 0.79 (decayed)            │
│   Bottom: ISW source dΦ̃/dz at z=0–10 (cooling vs heating bands)        │
└──────────────────────────────────────────────────────────────────────────┘
```
*(Figure 8: Top panel: reduced potential Φ̃(a) vs redshift for GRUT (navy, two CMB scales) and ΛCDM (orange). GRUT potential deepens from 1.0 at matter-radiation equality to 2.08 today; ΛCDM decays to 0.79. The GRUT transition at z★ = 77 is marked. Bottom panel: ISW source dΦ̃/dz at z = 0–10, showing the GRUT cooling region (shaded blue) where the growing potential cools CMB photons, vs the ΛCDM heating region (shaded orange) from the decaying potential. The Planck low-ℓ anomaly ratio ~0.83 is annotated.)*

**Status: Certified direction. GRUT cooling ISW consistent with Planck low-ℓ anomaly. Not yet decisive (cosmic variance ±20–60% at ℓ = 2–30).**

### 2.6 Summary Table of Certified Observables

| Observable | GRUT Prediction | Observed | Status |
|:---|:---|:---|:---|
| H(z) fit | χ²/N = 0.465 | 33 data points | Certified |
| BAO r_d | 147.1 Mpc | 147.0 ± 0.7 Mpc (Planck) | Certified |
| Ly-α r_d tension | −1.95σ | ±2σ expected | Tracked (not falsified) |
| fσ₈(z) fit | χ²/N = 0.763 | 13 RSD data points | Certified |
| σ₈ | 0.817 | 0.817 ± 0.060 (2PIGG) | Certified |
| S₈ | 0.803 | 0.766–0.832 (tension) | 1.79× tension reduction |
| CMB ISW direction | Cooling at ℓ=10–30 | 17% Planck low-ℓ deficit | Consistent direction |

No observable in this table has been adjusted post-hoc. All six results derive from τ₀ = 41.9 Myr, α_vac = 1/3, and the GRUT background with Ω_m = 0.290, Ω_Λ = 0.710.

---

## 3. Falsifier F1: Gravitational Decoherence Plateau at ~689 Hz

**Sector:** Laboratory gravity (matter-wave interferometry, optomechanics).
**Registry claim:** `decoherence_plateau`.
**Module:** `grut/derived/decoherence/sector.py`, `grut/foundation/noise_kernel.py`.

### Prediction

The gravitational decoherence rate for a mesoscopic mass m, radius R, in a superposition of two positions separated by l:

    Λ_grav = G m² S(l/R) / (ℏ l)                                       (1)

with S(l/R) = min(1, (l/R)³/6), derived directly from the imaginary part of the closed-time-path (CTP) influence functional. **Zero free parameters.** The framework predicts a specific numerical rate and six concomitant scaling laws.

### Gold benchmark

For m = 80.8 picograms, R = 1 μm, l = 1 μm:

    Λ_grav (gold benchmark) = 689 Hz                                    (2)

### Six concomitant signatures

A decisive test must verify ALL six:

1. **m² scaling** (mass-squared, NOT linear-in-N as in CSL).
2. **S(l/R) geometric factor** (extended-body suppression in near field).
3. **Pressure-independent plateau** (saturation against environmental noise floor).
4. **(l/R)¹ separation scaling at far field** (vs (l/R)² in CSL near field).
5. **Entanglement protection** (gravitational decoherence preserves bipartite entanglement).
6. **Geometric kink at l = 6^(1/3) R ≈ 1.817 R** (transition between near and far field).

### Test

Matter-wave interferometry at the 10–100 picogram scale, in cryogenic suspension, with controlled separation. Five-year experimental program.

### Status

No measurement has yet been performed in this regime. No tested alternative (CSL, GRW, Diósi, Penrose, Anastopoulos-Hu) reproduces all six signatures simultaneously.

### Falsification condition

Any of:
- Plateau measured at a rate inconsistent with (1) by more than a factor of 3 at the gold benchmark.
- Mass scaling found to be linear (m¹) rather than quadratic (m²).
- No kink at l = 6^(1/3) R.
- Entanglement decay rate not matching the gravitational decoherence rate.

---

## 4. Falsifier F2: ³⁰Si/²⁸Si Isotope Discriminator versus CSL

**Sector:** Laboratory gravity, isotope-mass scaling.
**Registry claim:** `grut_csl_isotope_discriminator`.
**Module:** `grut/derived/decoherence/csl_discriminator.py`.

### Prediction

The framework predicts m² scaling; CSL predicts linear-N scaling. For isotope-purified samples:

    Λ_GRUT(³⁰Si) / Λ_GRUT(²⁸Si) = (30/28)² = 1.148        (m² scaling)
    Λ_CSL(³⁰Si)  / Λ_CSL(²⁸Si)  = 30/28 = 1.071           (linear-N scaling)

Difference: **3.81%**. A ³⁰Si vs ²⁸Si comparison at sub-percent precision distinguishes the two scaling laws.

### Test

Tandem matter-wave interferometry on isotope-purified silica spheres at ~1% rate-ratio precision. Resolves m²-vs-N¹ at >3σ.

### Status

No isotope-discriminating decoherence measurement published. Required precision at the edge of current capability (~5-year horizon).

### Falsification condition

If Λ(³⁰Si)/Λ(²⁸Si) agrees with CSL's 1.071 rather than GRUT's 1.148 at <1% precision, the framework's m² scaling is falsified. (Clean either/or test with CSL.)

---

## 5. Falsifier F3: BMV / Sub-Micron-Separation Gravitational-Entanglement Test

**Sector:** Laboratory gravity (gravitationally-induced entanglement).
**Registry claim:** `gravitational_entanglement_formation_rate`.
**Module:** `grut/derived/decoherence/sector.py`.

### Prediction

For two 10⁻¹⁴ kg silica spheres of radius 1 μm, separated by d = 200 nm (deep near-field):

    τ_ent (BMV standard) ≈ 0.5 s
    τ_ent (GRUT near-field) ≈ 0.5 × (R/d)³/6 ≈ 10 s

The framework predicts **~20× slower entanglement formation** at sub-micron separation than naive BMV via the same near-field S(l/R) suppression that governs single-mass decoherence.

### Test

Sub-micron-separation BMV protocol with mesoscopic masses (~10⁻¹⁵ to 10⁻¹³ kg) in cryogenic suspension. Measure entanglement-formation timescale vs separation; fit (R/d)³.

### Status

BMV protocol demonstrated at sub-µm scale in spin-magnetic systems; gravitational-mass implementation is a 5–10-year goal.

### Falsification condition

If entanglement-formation timescale at sub-micron separation matches the naive 1/(d × G m²) law (no near-field suppression), S(l/R) is falsified — both for entanglement and single-mass decoherence.

---

## 6. Falsifier F4: Cluster-Merger v × τ₀ Gas-to-Lensing Offset

**Sector:** Cluster astrophysics.
**Registry claim:** `cluster_merger_scaling_law`.
**Module:** `grut/derived/cluster/merger_population.py`, `bullet_cluster.py`.

### Prediction

Post-collisional gas-to-lensing offset:

    δ ≈ v_post × τ₀ × dec_ratio                                        (3)

with τ₀ = 41.9 Myr, dec_ratio ≈ 0.638. **The prediction is the SCALING LAW** across multiple systems.

### Cluster sample

| Cluster | v_post (km/s) | δ_obs (kpc) | δ_pred (kpc) | Residual |
|:---|:---|:---|:---|:---|
| Bullet (1E 0657-558) | 3000 | 150 | 154 | -2.7% |
| MACS J0025.4-1222 | 2000 | 100 | 103 | -2.9% |
| Abell 520 | 1700 | ~80 | 87 | -8.8% |
| El Gordo (ACT-CL) | 2700 | 480 | 138 | +247% (outlier) |

Internal scaling residual (3/4 systems): 1.72%. El Gordo documented as outlier (`el_gordo_outlier_open_question`).

### Status

Predictive at 1.72% for three of four currently-measured systems. El Gordo outlier is a documented open question.

### Falsification condition

Any of:
- A new merger system with (v_post, δ) outside the τ₀ × dec_ratio band by >20% (not in El Gordo's geometry class).
- El Gordo error budget tightened without resolving toward δ_pred.

---

## 7. Falsifier F5: Modified-Gravity μ − 1 = 1/3 on Horizon Scales

**Sector:** Cosmological perturbations (modified-gravity EFT-of-dark-energy).
**Registry claim:** `mg_eft_mu_gamma_mapping`, `modified_linear_growth_first_look`.
**Module:** `grut/derivation/phi_munu/mg_eft_mapping.py`, `modified_growth.py`.

### Prediction

    μ_GRUT(k, a) = 1 + α_vac / [1 + (τ₀ k_phys(a))²]                 (4)

with α_vac = 1/3 (PROVEN). Super-horizon limit: **μ → 4/3, γ = 1**. Sub-horizon: μ → 1 (ΛCDM recovery). Transition scale: λ★ ≈ 80.7 Mpc.

Growth ratio D_GRUT/D_ΛCDM at z = 0:

| Scale | k [Mpc⁻¹] | D_GRUT/D_ΛCDM |
|:---|:---|:---|
| σ₈ | 0.5 | 1.0009 (0.09%, NOT broken) |
| BAO | 0.04 | 1.085 (8.5%) |
| CMB low-ℓ | 0.001 | 2.024 (102%) |
| CMB horizon | 4.5×10⁻⁴ | 2.348 (135%) |

### Test

DESI Y3+ (2025–2027) ~5% on μ at large scales. Euclid + CMB-S4 (2027+) ~1% — definitive.

### Current status

Planck 2018: μ₀ − 1 = 0.07 ± 0.13. GRUT's 1/3 ≈ 0.33 is ~2σ above central value, within current bounds.

### Falsification condition

- μ₀ − 1 < 0.20 at >3σ: α_vac = 1/3 falsified.
- γ ≠ 1 at >2σ: TT-projector argument falsified.

---

## 8. Falsifier F6: Σm_ν ≈ 60 meV with Normal Hierarchy

**Sector:** Standard Model + cosmology.
**Registry claim:** `neutrino_hierarchy_z3_nh_prediction`.
**Module:** `grut/derived/koide/neutrino_hierarchy.py`.

### Prediction

Z_3 circulant structure with a_ν = 1 (derived via boundary-degenerate uniqueness theorem, Correction #29):

| Quantity | Prediction |
|:---|:---|
| Hierarchy | NH (interior generic) |
| m_1 | 0.802 meV |
| m_2 | 8.65 meV |
| m_3 | 50.16 meV |
| **Σm_ν** | **59.6 meV** |
| m_β | ~9 meV |
| 0νββ | NO signal |

### Tests

| Test | Date | Precision | GRUT outcome |
|:---|:---|:---|:---|
| JUNO | 2024–2030 | hierarchy >3σ | predict NH |
| DUNE / Hyper-K | 2030+ | >5σ hierarchy | predict NH |
| DESI Y3+ Σm_ν | 2025+ | ~50 meV | could detect ~1σ |
| Euclid + CMB-S4 | 2027+ | ~20 meV | DEFINITIVE ≥3σ test |
| KATRIN final m_β | 2027 | < 0.20 eV | consistent (~9 meV) |
| 0νββ (nEXO) | 2027+ | improved bounds | non-detection consistent |

### Current status

All current observations (Planck Σm_ν < 0.12 eV, KATRIN m_β < 0.45 eV, NH preference ~2σ, no 0νββ) consistent with prediction.

### Falsification condition

- IH confirmed at >5σ by JUNO / DUNE / Hyper-K.
- Σm_ν > 90 meV at >3σ by Euclid / CMB-S4.
- Σm_ν < 30 meV at >3σ.
- 0νββ signal detected.

---

## 9. Falsifier F7: CMB Low-ℓ Cooling ISW from Deepening Gravitational Potential

**Sector:** CMB temperature power spectrum (Integrated Sachs-Wolfe effect).
**Registry claim:** `cmb_isw_phi_tilde_prediction`, `cmb_isw_cooling_direction`.
**Module:** `grut/derived/cosmology/cmb_isw.py`.

### Physical mechanism

The ISW contribution to CMB temperature anisotropy:

    ΔT/T|_ISW = −2 ∫ dΦ/dη dη                                         (5)

A deepening potential (dΦ/dη > 0) cools the photons; a decaying potential heats them.

The GRUT transition scale for k = 10⁻³ Mpc⁻¹:

    a★(k) = τ₀c × k ≈ 12.847 Mpc × k     →    z★ = 76.8              (6)

This falls **after recombination (z = 1100) but before large-scale structure formation (z ≲ 10)**. At z = 1100: μ_GRUT = 1.0017 — the Sachs-Wolfe spectrum is unchanged at 0.17% precision.

After the transition, enhanced gravitational coupling drives:

    p₊ ≈ 1.186  (μ → 4/3 matter domination)  →  Φ̃ ∝ a^0.186          (7)

### Quantitative prediction (k = 10⁻³ Mpc⁻¹)

| Epoch | z | Φ̃_GRUT | Φ̃_ΛCDM |
|:---|:---|:---|:---|
| Initialization | a_init | 1.0000 | 1.0000 |
| GRUT transition | z★ = 76.8 | 1.217 | 1.000 |
| z = 4 | 4 | 2.080 | 0.997 |
| z = 1 (peak) | 1 | 2.334 | 0.956 |
| Today | z = 0 | **2.079** | **0.788** |

| Quantity | Value |
|:---|:---|
| Φ̃_GRUT / Φ̃_ΛCDM today | **2.64×** |
| ΔΦ̃_GRUT = Φ̃(z=0) − 1 | +1.079 (potential deepened — **cooling ISW**) |
| ΔΦ̃_ΛCDM = Φ̃(z=0) − 1 | −0.212 (potential decayed — heating ISW) |
| ISW amplitude ratio | **5.09×** |

At horizon scale (k = 4.5×10⁻⁴ Mpc⁻¹): Φ̃_GRUT / Φ̃_ΛCDM = **3.06×**.

### Planck low-ℓ anomaly

Planck 2018 shows D_ℓ^obs/D_ℓ^ΛCDM ≈ 0.83 at ℓ = 2–30 (17% deficit). GRUT's cooling ISW at ℓ = 10–30 (probing z ≈ 2–9, the deepening epoch) predicts reduced D_ℓ — same direction as the anomaly.

### Test

**Primary (near-term):** CMB-S4 (2027+) × LSST ISW-galaxy cross-correlation. ΛCDM predicts positive ISW-galaxy correlation at 5° < θ < 20°. GRUT predicts negative (cooling) correlation at the same scales. Discriminating power >3σ at z = 2–5 with CMB-S4 × LSST.

**Secondary:** MGCAMB Boltzmann integration with GRUT μ(k,a) for quantitative D_ℓ prediction (flagged as Priority 5 future calculation).

### Current status

Cooling direction certified from 44/44 cmb_isw.py tests (June 2026). Planck anomaly direction consistent. Quantitative D_ℓ magnitude awaits MGCAMB integration.

### Falsification condition

- **Condition 1:** CMB-S4 + LSST ISW-galaxy cross-correlation measures *positive* large-scale ISW at >3σ at ℓ = 10–30.
- **Condition 2:** Planck anomaly resolves to a *power excess* at ℓ = 10–30 at >2σ (PICO, LiteBIRD).
- **Condition 3:** MGCAMB integration with μ_GRUT produces D_ℓ^GRUT inconsistent with Planck TT at >3σ across ℓ = 2–30.

Note: SW spectrum unchanged (μ = 1.0017 at z = 1100); acoustic peaks at ℓ = 200–2000 are not modified at measurable precision.

---

## 10. The Pattern: GRUT vs Other ToE Programs

| Program | Predicts μ at horizon? | Predicts m_ν? | Lab decoherence rate? | Cluster offset? | CMB ISW sign? |
|:---|:---|:---|:---|:---|:---|
| String theory | landscape | landscape | landscape | landscape | landscape |
| Loop quantum gravity | unclear | not derived | not derived | not derived | not derived |
| Asymptotic safety | weak prediction | not derived | not derived | not derived | not derived |
| Causal dynamical triangulations | early-universe only | not derived | not derived | not derived | not derived |
| **GRUT** | **μ − 1 = 1/3** | **NH, Σm_ν ≈ 60 meV** | **689 Hz at gold benchmark** | **δ = v × 41.9 Myr × 0.638** | **Cooling at ℓ=10–30** |

GRUT's posture: **the framework can be wrong in near-term ways**. Each of the seven predictions above either survives the next 1–10 years of experiment, or it doesn't. The framework offers no hiding place behind a parameter space.

---

## 11. The Honest-Negative Roster

| Gap | Status | Effect |
|:---|:---|:---|
| `koide_phase_4_open_negative` | Open: (M_0, θ) selection mechanism | Charged-lepton structure proven, mechanism not derived |
| `tji_7_4_open_negative` | Phase-1 (Allen-Jacobson S⁴) pending | Curved-TJI route to R not closed |
| `nonlinear_ladder_4_of_8` | 4 of 8 rungs complete | Nonlinear gravity recovery partial |
| `phi_munu_frw_beyond_wkb_open_question` | (Hτ₀)² ≈ 10⁻⁶ correction | Beyond-WKB correction deferred |
| ~~`neutrino_z3_coupling_derivation`~~ | RESOLVED (Correction #29) | (was: NH conditional on postulate) |
| `n_total_zero_parameter` | N_total = 329 uses observed t_0 | One observational anchor in Hubble route |
| `primordial_amplitude_zero_parameter` | A_s scaling-conditional | Pivot-mode normalization pending |
| `track_v_coupling_unification` | 8.9% miss at GUT scale | β-correction not derived |
| `vorton_track_vii_open_negative` | M_vorton/M_soliton 450× discrepancy | Topological-defect route falsified |
| `el_gordo_outlier_open_question` | δ_obs / δ_pred = 3.5× | Cluster fit good for 3/4 systems |
| `rho_max_scale_open_question` | ρ_max ≈ 10⁻²² kg/m³ scale | Whole-Hole interior pending |
| `path_f_translation_gap` | Im(W) → R conversion gap | Path F closure pending |
| `cmb_isw_mgcamb_integration_pending` | D_ℓ quantitative prediction deferred | ISW direction certified; D_ℓ magnitude awaits Boltzmann integration |

These open negatives are not predictions the framework makes — they are gaps the framework explicitly documents. Predict where it can; document gaps where it cannot.

---

## 12. Conclusion

GRUT presents seven near-term-testable falsifiers across four sectors, grounded in six certified cosmological observables:

| # | Falsifier | Sector | Timeline |
|:---|:---|:---|:---|
| F1 | Decoherence plateau ~689 Hz | Lab gravity | 5–10 yr |
| F2 | ³⁰Si/²⁸Si discriminator | Lab gravity | 5–10 yr |
| F3 | Sub-micron-BMV near-field | Lab gravity | 5–10 yr |
| F4 | Cluster-merger v × τ₀ | Cluster astrophysics | 1–5 yr |
| F5 | μ − 1 = 1/3 modified-gravity | Cosmology | 2–5 yr (DESI/Euclid) |
| F6 | Σm_ν ≈ 60 meV / NH | SM + cosmology | 2–10 yr (JUNO/DESI/Euclid) |
| F7 | CMB low-ℓ cooling ISW | CMB / ISW | 3–7 yr (CMB-S4 + LSST) |

If all seven survive their next-decade tests, the framework is supported as a unified description of gravity, cosmology, and the Standard Model from a single set of axioms. If any one fails decisively, the corresponding sector is falsified — with cascading consequences on upstream derivations.

The certified cosmological baseline (six observables, all consistent within current data, no post-hoc tuning) represents the framework's current evidential position: passing tests at a level that alternative dark-sector models typically fail without additional free parameters. All six results derive from two constants: τ₀ = 41.9 Myr and α_vac = 1/3.

The framework's posture: GRUT does not currently exceed mainstream ToE programs in mathematical maturity, formal closure, peer-reviewed validation, or Standard Model derivation. **It does exceed those programs in operational falsifiability** — and that is the basis on which this paper invites adversarial testing.

The framework is deliberately structured to be wrong, in specific, near-term, identifiable ways. Whether it is right is the question this paper asks the experimental community to answer.

---

## Acknowledgments

This work is supported by the GRUT-RAI computational framework: `grut/`, `theory/`, and `tests/` directories with 112 registered claims, 3190 passing tests, and 36 documented corrections. All numerical predictions trace to specific module functions and are reproducible via `python -m pytest tests/`. Cosmological certifications use modules `grut/derived/cosmology/hubble_tension.py`, `bao_sound_horizon.py`, `fsigma8_growth.py`, `sigma8_growth.py`, and `cmb_isw.py`.

---

## References to GRUT internal documents

- `theory/GRUT_TOE.md` — full framework theory document.
- `theory/GRUT_DECOHERENCE_PAPER.md` — standalone derivation of F1.
- `theory/derivation/CORRECTION_26_PRIORITY_3_CLOSURE.md` — n_g(ω) MG-EFT mapping.
- `theory/derivation/CORRECTION_27_MODIFIED_GROWTH.md` — modified linear growth.
- `theory/derivation/CORRECTION_28_NEUTRINO_HIERARCHY.md` — neutrino hierarchy via Z_3.
- `theory/derivation/CORRECTION_29_PRIORITY_4B_UNIQUENESS.md` — a_ν = 1 uniqueness theorem.

---

## External references

[1] L. Diósi, Phys. Lett. A 120, 377 (1987).
[2] R. Penrose, Gen. Rel. Grav. 28, 581 (1996).
[3] J. Schwinger, J. Math. Phys. 2, 407 (1961); L. V. Keldysh, JETP 20, 1018 (1965).
[4] E. Calzetta, B.-L. Hu, *Nonequilibrium Quantum Field Theory*, Cambridge (2008).
[5] C. Anastopoulos, B.-L. Hu, Class. Quantum Grav. 30, 165007 (2013).
[6] S. Bose et al., Phys. Rev. Lett. 119, 240401 (2017) (BMV).
[7] C. Marletto, V. Vedral, Phys. Rev. Lett. 119, 240402 (2017).
[8] Z. Komargodski, A. Schwimmer, JHEP 12, 099 (2011).
[9] S. Pogosian, A. Silvestri, Phys. Rev. D 77, 023503 (2008).
[10] E. Bertschinger, P. Zukin, Phys. Rev. D 78, 024015 (2008).
[11] G. Gubitosi, F. Piazza, F. Vernizzi, JCAP 02, 032 (2013).
[12] Planck Collaboration, A&A 641, A6 (2020).
[13] NuFIT Collaboration, NuFIT 5.3 (2024), http://www.nu-fit.org.
[14] KATRIN Collaboration, arXiv:2406.13516.
[15] R. Sachs, A. Wolfe, ApJ 147, 73 (1967).
[16] Planck Collaboration, A&A 641, A5 (2020) (CMB power spectra).
[17] A. Lewis, A. Challinor, A. Lasenby, ApJ 538, 473 (2000) (CAMB).
[18] A. Hojjati, L. Pogosian, G.-B. Zhao, JCAP 08, 005 (2011) (MGCAMB).

---

*D. Ryan Grover, June 2026. The author thanks the GRUT-RAI computational framework for the discipline pattern that produced these falsifiers, and the experimental community in advance for the tests that will adjudicate them.*
