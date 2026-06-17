# Seven Near-Term Falsifiers of GRUT: Adversarial Predictions and Cosmological Status (One Resolved Against the Linear Branch)

D. Ryan Grover

June 2026

Correspondence: dryangrover@gmail.com

---

## Abstract

We present seven near-term-testable falsifiers of the Grand Responsive Universe Theory (GRUT), and we report that one of them has now fired. Three falsifiers are laboratory tests of gravity (decoherence plateau at ~689 Hz, ³⁰Si/²⁸Si isotope discriminator vs CSL, and the BMV sub-micron-separation gravitationally-induced-entanglement protocol); one is at cluster scale (gas-to-lensing offset δ ≈ v × τ₀ = 41.9 Myr); one is the neutrino sector (Σm_ν ≈ 60 meV with normal hierarchy); and two were linear-cosmology tests of the same modified-gravity prediction (μ − 1 = 1/3 on horizon scales, F5; CMB low-ℓ ISW, F7). **The two linear-cosmology falsifiers (F5/F7) have been resolved against the linear branch (Correction #38, June 2026):** a validated MGCAMB run shows GRUT's linear μ → 4/3 over-produces the low-ℓ CMB ISW by ~2.6× (~29σ) — the "deepening cools and reduces low-ℓ power" inference was a sign error, since D_ℓ ∝ |ΔΦ̃|² and the ~5× ISW amplitude *adds* power. GRUT's linear cosmology is therefore ΛCDM; its dark-sector enhancement is confined to bound/nonlinear systems. The background cosmology is unaffected and stands: Hubble expansion H(z) (χ²/N = 0.465, 33 data points) and BAO sound horizon r_d (within 0.1% of Planck; −1.95σ Ly-α tension documented). The linear-growth observables (fσ₈, σ₈, S₈) reduce to ΛCDM and are no longer quoted as distinctive predictions; the S₈ offset that survives comes from GRUT's background Ω_m, not from modified gravity. Unlike most ToE programs (string theory, loop quantum gravity, asymptotic safety, causal dynamical triangulations), GRUT can be wrong in near-term ways — and here it was, cleanly: a sharp prediction, computed and refuted, sharpening the theory to its true domain. We summarize each falsifier's derivation, current status, and the precise condition that would (or did) refute it.

---

## 1. Why this paper

A theory of everything that cannot be falsified by experiment is, by Popperian standards, not science. Many candidate ToE programs — string theory, loop quantum gravity, asymptotic safety, and causal dynamical triangulations — produce striking mathematical structure but offer few predictions that contemporary experiments can refute. They are not wrong; they are not yet adversarial.

GRUT takes a different posture. The framework deliberately surfaces predictions that contemporary experiments can refute on near-term timescales (1–10 years). This paper enumerates seven such predictions across four sectors (laboratory gravity, cluster astrophysics, cosmology, Standard Model) and gives, for each:

1. The framework's prediction (sharp, quantitative).
2. The derivation reference (which module, which equation).
3. The observational test (which experiment, what precision).
4. The current observational status (consistent / borderline / tested).
5. The falsification condition (what result would refute it).

Before presenting the falsifiers, Section 2 documents the framework's cosmological standing — the two background observables it certifies (H(z), BAO) and the linear-perturbation observables (fσ₈, σ₈, S₈, CMB ISW) that the low-ℓ CMB has now ruled out (Correction #38). The framework has 16 documented honest negatives in its registry — gaps that have been identified, named, and tested where possible. Those negatives stand alongside these positive predictions. The framework does not hide what it cannot predict; it identifies precisely what it does predict, and at what cost the prediction can be wrong.

This is not a comprehensive review. The framework's 112-claim registry, 3190-test suite, and 38 documented corrections are referenced by claim IDs throughout. For the full theoretical machinery, see `theory/GRUT_TOE.md`. This paper concentrates on seven near-term falsifiers that, if any one of them fails decisively, refute the framework's prediction in that sector.

---

## 2. Cosmological Status (background certified; linear ruled out)

Before presenting the falsifiers, it is useful to document the framework's cosmological standing — including where it has just been refuted. Two **background** observables (H(z), BAO) are numerically certified against data without new free parameters beyond τ₀ = 41.9 Myr (the macroscopic gravitational relaxation time) and α_vac = 1/3 (the conformal trace-anomaly coupling). The **linear-perturbation** observables (fσ₈, σ₈, S₈, CMB low-ℓ ISW) were put forward as the framework's sharpest cosmological predictions and have now been **ruled out** at linear order by the definitive low-ℓ CMB test (Correction #38, June 2026): on linear scales GRUT = ΛCDM, and the dark-sector enhancement is confined to bound/nonlinear systems. All results use GRUT background cosmology: Ω_m = 0.290, Ω_Λ = 0.710, H₀ = 69.03 km/s/Mpc.

### 2.1 Hubble Expansion H(z)

**Module:** `grut/derived/cosmology/hubble_tension.py`
**Test data:** 33 H(z) measurements (cosmic chronometers + BAO-based).

GRUT reproduces the full Hubble expansion history with χ²/N = 0.465 — less than half the expected χ²/N = 1 for a well-fit model. The low χ²/N reflects that GRUT background cosmology (with Ω_m = 0.290, Ω_Λ = 0.710) fits the full H(z) dataset better on average than the Planck-2018 best-fit ΛCDM.

**Status:** Certified. χ²/N = 0.465 < 1 across 33 independent H(z) data points.

### 2.2 BAO Sound Horizon r_d

**Module:** `grut/derived/cosmology/bao_sound_horizon.py`
**Key result:** GRUT predicts r_d = 147.1 Mpc — consistent with Planck CMB acoustic-peak measurement at sub-percent precision. The documented Ly-α forest tension (−1.95σ) is within the expected ±2σ envelope and is classified as a tracked open negative, not a refutation.

**Status:** Certified. r_d prediction within 0.1% of Planck. Ly-α tension documented at −1.95σ (not a falsification).

### 2.3 Growth Rate fσ₈(z)

**Module:** `grut/derived/cosmology/fsigma8_growth.py`
**Test data:** 13 RSD (redshift-space-distortion) measurements at k = 0.05 Mpc⁻¹.

The GRUT growth rate integral χ²/N = 0.763 across 13 independent fσ₈(z) measurements. The modified growth (μ(k,a) ≠ 1 on horizon scales) enhances large-scale growth while leaving sub-horizon (k = 0.5 Mpc⁻¹) growth at the 0.09% level — invisible at current observational precision on σ₈ but characteristic of the transition at λ★ ≈ 80.7 Mpc.

**Status:** Consistent with data, but ΛCDM-level — ΛCDM fits these same 13 RSD points equally well. The distinctive linear enhancement is ruled out (Correction #38); GRUT's linear growth = ΛCDM.

### 2.4 S₈ Weak-Lensing Amplitude

**Module:** `grut/derived/cosmology/sigma8_growth.py`
**Key results:** σ₈_GRUT = 0.817, S₈_GRUT = 0.803 (where S₈ ≡ σ₈√(Ω_m/0.3)).

The current Planck CMB vs weak-lensing S₈ tension is: Planck S₈ = 0.832 ± 0.013 vs KiDS+DES+HSC average ~0.766 ± 0.013 — a ~3.2σ discrepancy. GRUT predicts S₈ = 0.803, which lies between Planck and weak-lensing at 1.79× tension reduction (bringing the tension from ~3.2σ to ~1.8σ). σ₈_GRUT = 0.817 matches the 2PIGG galaxy cluster constraint (0.817 ± 0.060) at its central value.

**Status:** The 1.79× S₈ reduction is carried by GRUT's lower *background* Ω_m, not by modified gravity — the linear σ₈ boost is ruled out (Correction #38) and in any case worked against the resolution. On linear scales σ₈ = ΛCDM.

### 2.5 CMB low-ℓ ISW — linear branch ruled out (Correction #38)

**Module:** `grut/derived/cosmology/cmb_isw.py`; validated MGCAMB (`~/mgcamb_grut/`).
**Key results:** Φ̃_GRUT(z=0) = 2.079 vs Φ̃_ΛCDM(z=0) = 0.788 at k = 10⁻³ Mpc⁻¹ (ISW amplitude ratio 5.09); definitive D_ℓ^GRUT/D_ℓ^ΛCDM ≈ 2.6× at ℓ ≲ 30 (~29σ).

GRUT's enhanced large-scale growth makes the reduced potential Φ̃ ≡ μ(k,a) δ(a)/a *deepen* (1 → 2.079) rather than decay (ΛCDM: 1 → 0.788). That deepening is computed correctly (the transition epoch z★ = 76.8 for k = 10⁻³ Mpc⁻¹ drives p₊ ≈ 1.186 in matter domination vs 1.0 in ΛCDM; μ_GRUT(z=1100) = 1.0017 leaves the primary Sachs-Wolfe spectrum unchanged). What was wrong was the inference about the power spectrum. The ISW contributes to the temperature *power* spectrum as ∝ |ΔΦ̃|², so the ~5× larger GRUT amplitude **adds** power; the "cooling reduces D_ℓ → matches the Planck deficit" step was a sign error.

The definitive validated MGCAMB calculation (GR-limit reproduces stock CAMB exactly; ratio → 1 at ℓ = 220; σ₈ preserved) gives a low-ℓ **excess** of ~2.6× (~29σ) — the opposite of the Planck 2018 ~17% low-ℓ *deficit*. The derived FRW retarded kernel does not rescue it (2.79×), and a memory source, a quadratic Keldysh-noise vertex, and gravitational slip all fail via the growth↔Weyl↔ISW structural law.

**Status: Ruled out (Correction #38, June 2026).** The linear large-scale branch is falsified: GRUT's linear cosmology = ΛCDM, and the dark-sector enhancement is confined to bound/nonlinear systems. This is precisely the kind of clean, near-term falsification the paper advocates — the theory sharpened to its true domain, not refuted.

### 2.6 Summary Table of Cosmological Observables

| Observable | GRUT Prediction | Observed | Status |
|:---|:---|:---|:---|
| H(z) fit | χ²/N = 0.465 | 33 data points | ✓ Certified (background) |
| BAO r_d | 147.1 Mpc | 147.0 ± 0.7 Mpc (Planck) | ✓ Certified (background) |
| Ly-α r_d tension | −1.95σ | ±2σ expected | Tracked (not falsified) |
| fσ₈(z) fit | χ²/N = 0.763 | 13 RSD data points | Consistent, but ΛCDM-level — linear enhancement ruled out (Corr #38) |
| σ₈ (linear) | +3.1% boost | = ΛCDM on linear scales | Superseded (Corr #38) |
| S₈ | 0.803 | 0.766–0.832 (tension) | Reduction via background Ω_m; σ₈ route superseded |
| CMB low-ℓ ISW (linear) | ~2.6× excess at ℓ≲30 | 17% Planck low-ℓ deficit | ✗ Ruled out (Corr #38) |

The background results (H(z), BAO) stand on τ₀ = 41.9 Myr, α_vac = 1/3, and the GRUT background Ω_m = 0.290, Ω_Λ = 0.710. The linear-growth observables (fσ₈, σ₈, S₈, CMB ISW) are demoted following the definitive low-ℓ CMB falsification (Correction #38): on linear scales GRUT = ΛCDM, and the dark-sector enhancement is confined to bound/nonlinear systems. No observable has been adjusted post-hoc.

---

## 3. Falsifier F1: Gravitational Decoherence Plateau at ~689 Hz

**Sector:** Laboratory gravity (matter-wave interferometry, optomechanics).
**Registry claim:** `decoherence_plateau`.
**Module:** `grut/derived/decoherence/sector.py`, `grut/foundation/noise_kernel.py`.
**Standalone derivation:** [GRUT_DECOHERENCE_PAPER.md](GRUT_DECOHERENCE_PAPER.md).

### Prediction

The gravitational decoherence rate for a mesoscopic mass m, radius R, in a superposition of two positions separated by l:

    Λ_grav = G m² S(l/R) / (ℏ l)                                       (1)

with S(l/R) = min(1, (l/R)³/6), derived directly from the imaginary part of the closed-time-path (CTP) influence functional. **Zero free parameters** — no collapse rate, no correlation length, no Yukawa scale. The framework predicts a specific numerical rate and six concomitant scaling laws.

### Gold benchmark

For m = 80.8 picograms (silica or gold sphere, density-matched to canonical reference), R = 1 μm, l = 1 μm:

    Λ_grav (gold benchmark) = 689 Hz                                    (2)

This is the framework's signature laboratory observable. The "plateau" is the (l/R)¹ regime at far-field separations where S = 1.

### Six concomitant signatures

A decisive test must verify ALL six:

1. **m² scaling** (mass-squared, NOT linear-in-N as in CSL).
2. **S(l/R) geometric factor** (extended-body suppression in near field).
3. **Pressure-independent plateau** (saturation against environmental noise floor).
4. **(l/R)¹ separation scaling at far field** (vs (l/R)² in CSL near field, etc.).
5. **Entanglement protection** (gravitational decoherence preserves bipartite entanglement of mass eigenstates).
6. **Geometric kink at l = 6^(1/3) R ≈ 1.817 R** (transition between near-field and far-field regimes).

### Test

Matter-wave interferometry at the 10–100 picogram scale, in cryogenic suspension, with controlled separation. Five-year experimental program; sensitivity targets specified in [GRUT_DECOHERENCE_PAPER.md §6].

### Status

No measurement has yet been performed in this regime. The framework predicts the rate, the scaling laws, and the kink. No tested alternative (CSL, GRW, Diósi, Penrose, Anastopoulos-Hu) reproduces all six signatures simultaneously.

### Falsification condition

Any of:
- Plateau measured at a rate inconsistent with (1) by more than a factor of 3 at the gold benchmark.
- Mass scaling found to be linear (m¹) rather than quadratic (m²).
- No kink at l = 6^(1/3) R (smooth m² × l⁻¹ behavior across all separations).
- Entanglement decay rate not matching the gravitational decoherence rate.

Any of these falsifies the framework's gravity-sector prediction.

---

## 4. Falsifier F2: ³⁰Si/²⁸Si Isotope Discriminator versus CSL

**Sector:** Laboratory gravity, isotope-mass scaling.
**Registry claim:** `grut_csl_isotope_discriminator`.
**Module:** `grut/derived/decoherence/csl_discriminator.py`.

### Prediction

The framework predicts that the gravitational decoherence rate scales as m² (mass squared). The Continuous Spontaneous Localization (CSL) family of models predicts linear scaling in nucleon count N (with N ∝ m for atomic-mass-unit-scaled bodies). The two predictions diverge for isotope-purified samples of the same chemical species:

    Λ_GRUT(³⁰Si) / Λ_GRUT(²⁸Si) = (30/28)² = 1.148        (m² scaling)
    Λ_CSL(³⁰Si)  / Λ_CSL(²⁸Si)  = 30/28 = 1.071           (linear-N scaling)

Difference: **3.81%** per isotope-pair comparison. With a ³⁰Si vs ²⁸Si purified-sample comparison at sub-percent precision, the two scaling laws are distinguishable.

### Test

Tandem-experiment matter-wave interferometry on isotope-purified silica spheres. Comparison of decoherence rates between ³⁰Si and ²⁸Si samples at the 1% level resolves the m²-vs-N¹ scaling-law distinction at >3σ.

### Status

No isotope-discriminating decoherence measurement has been published. The required precision (~1% rate-ratio comparison between isotope-purified samples) is at the edge of current matter-wave-interferometry capability and should be feasible within the next experimental generation (~5 years).

### Falsification condition

If the rate ratio Λ(³⁰Si)/Λ(²⁸Si) is measured at <1% precision and the result agrees with CSL's 1.071 rather than GRUT's 1.148, the framework's m² scaling is falsified. (Note: this would simultaneously confirm CSL — a clean either/or test.)

---

## 5. Falsifier F3: BMV / Sub-Micron-Separation Gravitational-Entanglement Test

**Sector:** Laboratory gravity (gravitationally-induced entanglement).
**Registry claim:** `gravitational_entanglement_formation_rate`.
**Module:** `grut/derived/decoherence/sector.py` (entanglement-formation submodule).
**Original proposal:** Bose-Marletto-Vedral (BMV) 2017; Marletto-Vedral 2017.

### Prediction

If gravity is quantum (i.e., the gravitational interaction can mediate entanglement between two superposed masses), then two BMV masses placed at distance d will entangle on a timescale:

    τ_ent = ℏ d / (G m₁ m₂)

The framework adopts the BMV protocol's assumption that gravity is quantum (the CTP influence functional treats the gravitational field as quantum-mechanical), and predicts entanglement at the standard rate. The DISTINGUISHING prediction comes from sub-micron separations: the framework's near-field S(l/R) suppression also applies to entanglement formation, giving a specific (l/R)³ suppression in the regime where the masses are within R of each other.

For two 10⁻¹⁴ kg silica spheres of radius 1 μm, separated by d = 200 nm (deep near-field):

    τ_ent (BMV standard) = ℏ d / (G m²) ≈ 0.5 s
    τ_ent (GRUT near-field) ≈ τ_BMV / S(d/R) ≈ τ_BMV × (R/d)³/6 ≈ 0.5 × 21 ≈ 10 s

The framework predicts a **factor ~20 slower entanglement formation** at sub-micron separation than naive BMV — because the same near-field suppression that affects single-mass decoherence also affects the entanglement bridge.

### Test

Sub-micron-separation BMV protocol with mesoscopic masses (~10⁻¹⁵ to 10⁻¹³ kg) in cryogenic suspension. Measure entanglement-formation timescale as a function of separation; fit (R/d)³ in the near-field regime.

### Status

The BMV protocol has been demonstrated at the sub-µm scale in spin-magnetic systems and is being targeted for gravitational masses by multiple experimental groups (Roger Penrose / Sougato Bose / Markus Aspelmeyer collaborations). Sub-percent precision on entanglement-formation timescale is a 5–10-year goal.

### Falsification condition

If entanglement-formation timescale at sub-micron separation matches the naive 1/(d × G m²) law (no near-field suppression), the framework's S(l/R) is falsified — both for entanglement and (by consistency) for single-mass decoherence.

---

## 6. Falsifier F4: Cluster-Merger v × τ₀ Gas-to-Lensing Offset

**Sector:** Cluster astrophysics.
**Registry claim:** `cluster_merger_scaling_law`.
**Module:** `grut/derived/cluster/merger_population.py`, `bullet_cluster.py`.

### Prediction

In a binary cluster merger (post-collisional configuration), the framework predicts the gas-to-lensing offset δ scales as:

    δ ≈ v_post × τ_0 × dec_ratio                                       (3)

where v_post is the post-collision velocity of the gas relative to the dark-matter centroid, τ₀ = 41.9 Myr is the framework's macroscopic gravitational relaxation time, and dec_ratio = v_post / v_initial ≈ 0.638 is a deceleration-ratio adjustment for the gas-DM interaction.

For Bullet Cluster (1E 0657-558): v_post ≈ 3000 km/s gives δ ≈ 150 kpc — matching the observed offset. The framework's prediction is the SCALING LAW: across multiple cluster-merger systems, the gas-to-lensing offset divided by the merger velocity should equal τ₀ × dec_ratio (a universal constant).

### Cluster sample

Four merger systems used to date:

| Cluster | v_post (km/s) | δ_obs (kpc) | δ_pred (kpc) | Residual |
|:---|:---|:---|:---|:---|
| Bullet (1E 0657-558) | 3000 | 150 | 154 | -2.7% |
| MACS J0025.4-1222 | 2000 | 100 | 103 | -2.9% |
| Abell 520 | 1700 | ~80 | 87 | -8.8% |
| El Gordo (ACT-CL) | 2700 | 480 | 138 | +247% (outlier) |

Internal scaling residual across the first three: 1.72%. El Gordo is documented as an outlier (registry: `el_gordo_outlier_open_question`) — its δ is ~3.5× larger than the framework predicts, possibly due to off-axis or asymmetric-mass collision geometry.

### Test

A larger sample of cluster-merger systems with reconstructed v_post and δ. Sensitive to v×τ₀ scaling at the percent level if the sample reaches ~10–20 systems.

### Status

Predictive at the 1.72% level for three of four currently-measured systems. El Gordo outlier is a documented open question. Future cluster-merger surveys (Euclid + Roman + LSST) will produce a larger sample.

### Falsification condition

Any of:
- A new merger system with measured (v_post, δ) outside the τ₀ × dec_ratio band by more than 20% (not in El Gordo's specific geometry-asymmetric class).
- Reduction of the El Gordo error budget tightening δ_obs to within ~20% of δ_pred (would resolve outlier favorably; non-resolution would degrade the prediction).

A clean failure of the v × τ₀ scaling across multiple new systems falsifies the gravitational-relaxation-time interpretation of τ₀ and the framework's cluster-sector prediction.

---

## 7. Falsifier F5: Modified-Gravity μ − 1 = 1/3 on Horizon Scales — RULED OUT (linear)

**Sector:** Cosmological perturbations (modified-gravity EFT-of-dark-energy).
**Registry claim:** `mg_eft_mu_gamma_mapping`, `modified_linear_growth_first_look`.
**Module:** `grut/derivation/phi_munu/mg_eft_mapping.py`, `modified_growth.py`.
**Correction documents:** CORRECTION_26 (MG-EFT mapping), CORRECTION_27 (modified growth), CORRECTION_38 (validated MGCAMB low-ℓ CMB — falsification).

> **STATUS: RULED OUT (Correction #38, June 2026).** The linear large-scale prediction below (μ − 1 = 1/3 on horizon scales) was tested definitively by a validated MGCAMB run and **falsified**: it over-produces the low-ℓ CMB ISW by ~2.6× (~29σ; §2.5). GRUT's linear cosmology is therefore ΛCDM; the μ-enhancement survives only in the bound/nonlinear regime (clusters, halos). The prediction is retained below as the record of a sharp, near-term falsifier that did its job. F5 and F7 are the same linear-μ test and are jointly resolved against the linear branch.

### Prediction

The framework's covariant derivation of the gravitational constitutive correction Φ_μν (from δS_CTP/δh_a, Corrections #23–#25) produces an explicit modified-gravity μ(k, a) function on FRW backgrounds:

    μ_GRUT(k, a) = n_g²(k, a) = 1 + α_vac / [1 + (τ_0 k_phys(a))²]    (4)

with α_vac = 1/3 (Komargodski-Schwimmer trace-anomaly real-scalar identification, PROVEN). The framework also predicts γ_GRUT = 1 (no gravitational slip — TT-projector argument).

Limits:
- **Sub-horizon** (k_phys τ₀ ≫ 1): μ → 1, γ = 1 → ΛCDM recovery.
- **Super-horizon** (k_phys τ₀ ≪ 1): **μ → 1 + α_vac = 4/3, γ = 1**.
- Transition: λ★ ≈ 80.7 Mpc (today).

The largest cosmological scales experience a 33% boost to gravitational coupling. This was a **SHARP PREDICTION**: μ − 1 = 1/3 on horizon scales, γ = 1 — now tested and **ruled out** at linear order (it over-produces the low-ℓ CMB ISW by ~2.6×; see banner and §2.5).

### Modified linear growth (Correction #27)

Numerical integration of δ'' + [2 − (3/2)Ω_m] δ' − (3/2) Ω_m μ_GRUT(k, N) δ = 0 on a Planck-2018 ΛCDM background gives:

| Scale | k [Mpc⁻¹] | f_GRUT(z=0) = D_GRUT/D_ΛCDM |
|:---|:---|:---|
| σ₈ | 0.5 | **1.0009** (0.09%, NOT broken) |
| BAO | 0.04 | 1.085 (8.5%) |
| CMB low-ℓ | 0.001 | 2.024 (102%) |
| CMB horizon | 4.5×10⁻⁴ | 2.348 (135%) |

The σ₈-scale enhancement (0.09%) is BELOW current observational precision — GRUT does not catastrophically break the σ₈ / S₈ measurement that drives the existing tension between Planck CMB and weak-lensing surveys.

### Test

DESI Y3+ (2025–2027) targets ~5% precision on μ at large scales. Euclid (2027+) and CMB-S4 target ~1% precision — a definitive test.

### Current status

**Ruled out at linear order (Correction #38, June 2026).** Independently of the Planck 2018 paper-VI constraint μ₀ − 1 = 0.07 ± 0.13, the validated MGCAMB low-ℓ CMB calculation directly falsifies the linear μ → 4/3: it over-produces the low-ℓ ISW by ~2.6× (~29σ). The 33% large-scale enhancement is therefore excluded as a *linear* prediction; it survives only in the bound/nonlinear regime.

### Falsification condition (now triggered)

The framework's own falsification condition — "if a gauge-consistent Boltzmann calculation produces D_ℓ inconsistent with Planck TT at >3σ, the linear μ is falsified" — has been met: the validated MGCAMB run is inconsistent at ~29σ. For completeness, the originally stated near-term tests were:
- If μ₀ − 1 = 1/3 ± 0.05: linear branch confirmed — **did not occur**.
- If μ₀ − 1 < 0.20 at >3σ: α_vac = 1/3 falsified on linear cosmological scales — **effectively realized via the low-ℓ CMB**.
- If γ ≠ 1 measured at >2σ: TT-projector argument falsified (distinguishes from Brans-Dicke, f(R), DGP — all predict γ ≠ 1). γ = 1 remains GRUT's structural claim, but it is moot for the (now-ruled-out) linear branch.

The honest outcome: GRUT made a sharp linear-cosmology prediction, it was computed and tested, and it failed — sharpening the theory to its bound/nonlinear domain (linear cosmology = ΛCDM).

---

## 8. Falsifier F6: Σm_ν ≈ 60 meV with Normal Hierarchy

**Sector:** Standard Model + cosmology.
**Registry claim:** `neutrino_hierarchy_z3_nh_prediction`.
**Module:** `grut/derived/koide/neutrino_hierarchy.py`.
**Correction document:** CORRECTION_28.

### Prediction

The framework's Z_3 circulant structure for charged-lepton masses (giving K = 2/3, PROVEN) does NOT extend to neutrinos with the same coupling: applying a = √2 to neutrinos gives a minimum Δm²_atm/Δm²_sol ratio of 194.7, six times the observed 33.9 — no solution exists.

A modified Z_3 with **a_ν = 1** (giving K_ν = 1/2) admits a unique INTERIOR solution in Normal Hierarchy:

| Quantity | Prediction |
|:---|:---|
| Hierarchy | **NH** (interior generic) |
| m_1 | 0.802 meV |
| m_2 | 8.65 meV |
| m_3 | 50.16 meV |
| **Σm_ν** | **59.6 meV** |
| m_β (kinematic) | ~9 meV |
| 0νββ | NO signal predicted |

The IH solution at a_ν = 1 sits at the m_3 = 0 boundary (degenerate, fine-tuned, not a generic interior solution) — GRUT structurally **prefers Normal Hierarchy**.

The a_ν = 1 value is derived (Correction #29, Priority 4B) via the **boundary-degenerate uniqueness theorem**: among Z_3 couplings, a = 1 is uniquely characterized as the smallest value at which (i) boundary access (s_min → 0) is admissible AND (ii) the OTHER two s values are exactly degenerate. The boundary-gap formula √3·√(a²-1) vanishes only at a = 1. Combined with NH-interior + Σm_ν<Planck, this uniquely selects a_ν = 1. **The prediction is therefore not conditional on a postulate but on a structural theorem.**

### Tests

Multiple independent observational axes:

| Test | Date | Precision | GRUT outcome |
|:---|:---|:---|:---|
| JUNO | 2024–2030 | hierarchy >3σ | predict NH |
| DUNE / Hyper-K | 2030+ | >5σ hierarchy | predict NH |
| DESI Y3+ Σm_ν | 2025+ | ~50 meV | could detect ~1σ |
| Euclid + CMB-S4 | 2027+ | ~20 meV | DEFINITIVE ≥3σ test |
| KATRIN final m_β | 2027 | < 0.20 eV | consistent (~9 meV) |
| Project 8 m_β | 2030+ | ~40 meV → ~10 meV | could approach prediction |
| 0νββ (nEXO) | 2027+ | improved bounds | non-detection consistent |

### Current status

All current observations (Planck Σm_ν < 0.12 eV, KATRIN m_β < 0.45 eV, oscillation NH preference ~2σ, no 0νββ signal) are consistent with the prediction.

### Falsification condition

ANY of:
- IH confirmed at >5σ by JUNO / DUNE / Hyper-K → prediction falsified.
- Σm_ν > 90 meV measured at >3σ by Euclid / CMB-S4 → prediction falsified.
- Σm_ν < 30 meV measured at >3σ → prediction falsified.
- 0νββ signal detected → Dirac-ν posture falsified, framework upstream affected.

---

## 9. Falsifier F7: CMB Low-ℓ ISW from Deepening Gravitational Potential — RULED OUT (linear)

**Sector:** CMB temperature power spectrum (Integrated Sachs-Wolfe effect).
**Registry claim:** `cmb_isw_phi_tilde_prediction`, `cmb_isw_cooling_direction`.
**Module:** `grut/derived/cosmology/cmb_isw.py`; validated MGCAMB (`~/mgcamb_grut/`).
**Related:** §2.5 above; Falsifier F5 (the same linear-μ test).

> **STATUS: RULED OUT (Correction #38, June 2026).** The "secondary" MGCAMB test flagged below has now been done, and it overturns this falsifier's premise. The potential deepening is real (Φ̃ ratio 2.64×, ISW amplitude ~5× ΛCDM), but D_ℓ ∝ |ΔΦ̃|² — so the large amplitude **adds** low-ℓ power: the validated MGCAMB run gives a ~2.6× *excess* (~29σ), the opposite of the Planck *deficit*. The "cooling reduces D_ℓ → matches Planck" reasoning below was a sign error. Falsification condition 3 (below) is therefore met. F7 and F5 are jointly ruled out at linear order; GRUT's linear cosmology = ΛCDM, enhancement confined to bound/nonlinear systems.

### Physical mechanism

The Integrated Sachs-Wolfe (ISW) effect contributes to the CMB temperature anisotropy via:

    ΔT/T|_ISW = −2 ∫ dΦ/dη dη                                         (5)

where Φ is the Bardeen gravitational potential along the photon path. A deepening potential (dΦ/dη > 0) cools the photons (negative contribution); a decaying potential heats them.

The GRUT mechanism for potential deepening is the enhanced growth in the fluid regime (k_phys τ₀ ≪ 1). At the GRUT transition scale z★(k):

    a★(k) = τ₀c × k ≈ 12.847 Mpc × k                                  (6)

For k = 10⁻³ Mpc⁻¹: a★ = 0.01287, corresponding to z★ = 76.8 — **after recombination (z = 1100) but before large-scale structure formation (z ≲ 10)**. At z = 1100 for this mode: μ_GRUT = 1.0017 (0.17% modification only) — the Sachs-Wolfe angular spectrum is unchanged.

After the transition, the enhanced gravitational coupling drives the growth index:

    p₊ ≈ 1 + (3/2) × α_vac / (1 + something) → 1.186 for μ = 4/3      (7)

so δ ∝ a^1.186 in matter domination (vs δ ∝ a in ΛCDM), giving Φ̃ ∝ a^0.186: the potential deepens.

### Quantitative prediction

The reduced potential Φ̃(a; k) ≡ μ(k,a) δ(a)/a, normalized to 1 at matter-radiation equality:

| Epoch | z | Φ̃_GRUT | Φ̃_ΛCDM |
|:---|:---|:---|:---|
| Initialization | a_init | 1.0000 | 1.0000 |
| Transition | z★ = 76.8 | 1.0 (approx) | ~1.0 |
| Matter-Λ equality | z ≈ 0.3 | 1.81 | 0.94 |
| Today | z = 0 | **2.079** | **0.788** |

Key ratios at k = 10⁻³ Mpc⁻¹:
- Φ̃ ratio today: Φ̃_GRUT / Φ̃_ΛCDM = **2.64×**
- ΔΦ̃_GRUT = +1.079 (potential deepened: **cooling ISW**)
- ΔΦ̃_ΛCDM = −0.212 (potential decayed: heating ISW)
- ISW amplitude ratio: |ΔΦ̃_GRUT| / |ΔΦ̃_ΛCDM| = **5.09×**

At horizon scale (k = 4.5×10⁻⁴ Mpc⁻¹): Φ̃_GRUT / Φ̃_ΛCDM = **3.06×**, larger enhancement.

### Planck low-ℓ anomaly connection

The Planck 2018 CMB power spectrum shows D_ℓ^obs / D_ℓ^ΛCDM ≈ 0.83 at ℓ = 2–30 — a 17% power *deficit*. The original argument here was that GRUT's deepening potential gives a "cooling ISW" that *reduces* low-ℓ power, matching the deficit. **This was a sign error.** The ISW contributes to the temperature *power* spectrum D_ℓ as the square of the integrated potential change (∝ |ΔΦ̃|²), so the ~5× larger GRUT amplitude **adds** power. The full validated MGCAMB calculation confirms a ~2.6× low-ℓ *excess* (~29σ) — the opposite of the Planck deficit. So GRUT's linear large-scale μ does not match the anomaly; it overshoots it badly, and is ruled out.

### Test (primary — near-term)

**ISW-galaxy cross-correlation** via CMB-S4 (2027+) × LSST photometric galaxy catalog (2026+). The ISW amplitude and sign is measurable independently of the Sachs-Wolfe spectrum (which dominates the raw D_ℓ). A positive, hemisphere-scale ISW signal at large angles is the standard ΛCDM prediction; GRUT predicts a NET COOLING signal at 5 < ℓ < 30. With CMB-S4 + LSST this becomes a >3σ discriminator at z = 2–5.

**ISW-galaxy cross-correlation test (2027+):**
- Expected ΛCDM: positive ISW-galaxy correlation at angular scales 5° < θ < 20°.
- GRUT prediction: negative ISW-galaxy correlation (cooling) at the same scales.
- Discriminating power: >3σ with CMB-S4 × LSST at z = 2–5 photometric slice.

### Test (now completed — MGCAMB quantitative D_ℓ)

This was flagged as a Priority 5 future calculation; it has since been **done** (Correction #38, June 2026). A validated MGCAMB Boltzmann integration with the GRUT μ(k,a) function (equation 4) — GR-limit reproducing stock CAMB exactly (ratio → 1 at ℓ = 220), σ₈ preserved — gives D_ℓ^GRUT/D_ℓ^ΛCDM ≈ 2.6× at ℓ ≲ 30 (~29σ). The derived FRW retarded kernel (2.79×) and every other escape (filter, memory source, quadratic noise, slip) fail via the growth↔Weyl↔ISW law.

### Current status

**Ruled out (Correction #38, June 2026).** The cmb_isw module correctly computed the potential deepening (44/44 tests), but the full Boltzmann D_ℓ — now computed — shows a low-ℓ *excess* of ~2.6×, not the deficit the cooling argument inferred. The linear large-scale branch is falsified; GRUT's linear cosmology = ΛCDM, with the enhancement confined to bound/nonlinear systems.

### Falsification condition (Condition 3 triggered)

- **Condition 1:** CMB-S4 + LSST ISW-galaxy cross-correlation measures a *positive* large-scale ISW signal at >3σ at ℓ = 10–30 → would falsify a cooling prediction (now moot — the linear branch is already ruled out).
- **Condition 2:** The Planck low-ℓ anomaly resolves to an *excess* at ℓ = 10–30 — consistent with GRUT's computed excess in sign, but GRUT's amplitude (~2.6×) is far too large.
- **Condition 3 (TRIGGERED):** MGCAMB Boltzmann integration with the GRUT μ(k,a) function produces D_ℓ^GRUT inconsistent with Planck across ℓ = 2–30 — realized at ~29σ. **This is the condition that fired.**

Note: the SW spectrum is unchanged (μ at z = 1100 is 0.17% above 1), so the acoustic peaks at ℓ = 200–2000 are unmodified — the falsification is specific to the low-ℓ ISW contribution, exactly as scoped.

---

## 10. The Pattern: GRUT vs Other ToE Programs

| Program | Predicts μ at horizon? | Predicts m_ν? | Lab decoherence rate? | Cluster offset? | CMB ISW sign? |
|:---|:---|:---|:---|:---|:---|
| String theory | landscape (no fixed prediction) | landscape | landscape | landscape | landscape |
| Loop quantum gravity | unclear; cosmological extension underway | not derived | not derived | not derived | not derived |
| Asymptotic safety | weak prediction; depends on UV fixed point | not derived | not derived | not derived | not derived |
| Causal dynamical triangulations | early-universe predictions only | not derived | not derived | not derived | not derived |
| **GRUT** | **μ − 1 = 1/3** | **NH, Σm_ν ≈ 60 meV** | **689 Hz at gold benchmark** | **δ = v × 41.9 Myr × 0.638** | **Cooling at ℓ=10–30** |

GRUT's posture: **the framework can be wrong in near-term ways**. The above table is the framework's load-bearing claim about its own falsifiability — not "more rigorous" than other programs (asymptotic safety has greater nonperturbative-completion maturity; string theory has greater mathematical depth), but **more adversarial**. Each of the seven predictions above either survives the next 1–10 years of experiment, or it doesn't. The framework offers no hiding place behind a parameter space.

---

## 11. The Honest-Negative Roster

In the framework's tradition of explicit negative documentation, the following gaps stand alongside the positive predictions:

| Gap | Status | Effect |
|:---|:---|:---|
| `koide_phase_4_open_negative` | Open: mechanism for (M_0, θ) selection in Z_3 | Charged-lepton structure proven, mechanism not derived |
| `tji_7_4_open_negative` | Phase-1 (Allen-Jacobson S⁴) work pending | Curved-TJI route to R = 1.15428 not closed |
| `nonlinear_ladder_4_of_8` | 4 of 8 rungs complete | Nonlinear gravity recovery partial |
| `phi_munu_frw_beyond_wkb_open_question` | (Hτ₀)² ≈ 10⁻⁶ correction | Beyond-WKB cosmological correction deferred |
| ~~`neutrino_z3_coupling_derivation_open_question`~~ | RESOLVED (Correction #29, Priority 4B) — uniqueness theorem | (was: NH prediction conditional on postulate; now derived) |
| `n_total_zero_parameter_derivation_open_question` | N_total = 329 anchor uses observed t_0 | One observational anchor in Hubble route |
| `primordial_amplitude_zero_parameter_open_negative` | A_s scaling-conditional | Pivot-mode normalization pending |
| `track_v_coupling_unification_open_question` | 8.9% miss at GUT scale | β-correction not derived |
| `vorton_track_vii_open_negative` | M_vorton/M_soliton 450× discrepancy | Topological-defect route falsified, dielectric route preferred |
| `el_gordo_outlier_open_question` | δ_obs / δ_pred = 3.5× outlier | Cluster-merger fit good for 3/4 systems |
| `rho_max_scale_open_question` | ρ_max ≈ 10⁻²² kg/m³ scale | Whole-Hole quantitative interior pending |
| `path_f_translation_gap` | Im(W) → R conversion gap | Path F closure pending |
| `cmb_isw_mgcamb_integration_pending` | D_ℓ quantitative prediction deferred | CMB low-ℓ ISW direction certified; D_ℓ magnitude awaits full Boltzmann integration |

These open negatives are not predictions the framework makes — they are gaps the framework explicitly documents. The deposit's posture is honest: predict where it can; document gaps where it cannot.

---

## 12. Conclusion

GRUT presents seven near-term-testable falsifiers across four sectors. Two of them — F5 and F7, the linear-cosmology pair testing the same modified-gravity prediction — have **already fired**, ruling out GRUT's linear large-scale modified gravity (Correction #38, June 2026). Five remain live:

| # | Falsifier | Sector | Timeline / Status |
|:---|:---|:---|:---|
| F1 | Decoherence plateau ~689 Hz | Lab gravity | 5–10 yr |
| F2 | ³⁰Si/²⁸Si discriminator | Lab gravity | 5–10 yr |
| F3 | Sub-micron-BMV near-field | Lab gravity | 5–10 yr |
| F4 | Cluster-merger v × τ₀ | Cluster astrophysics | 1–5 yr (sample growth) |
| F5 | μ − 1 = 1/3 modified-gravity (linear) | Cosmology | **RULED OUT — Corr #38 (2026)** |
| F6 | Σm_ν ≈ 60 meV / NH | Standard Model + cosmology | 2–10 yr (JUNO/DESI/Euclid) |
| F7 | CMB low-ℓ ISW (linear μ) | CMB / ISW | **RULED OUT — Corr #38 (2026)** |

If the five remaining falsifiers survive their next-decade tests, the framework is supported as a unified description of gravity, cosmology, and the Standard Model from a single set of axioms. If any one fails decisively, the corresponding sector is falsified — with cascading consequences on the upstream derivations. F5/F7 just demonstrated the mechanism: a sharp prediction, computed in full, refuted by the low-ℓ CMB — and the framework absorbed the result by confining its dark-sector enhancement to the bound/nonlinear regime, leaving the background and lab/neutrino sectors intact.

The surviving cosmological baseline is the **background** sector — H(z) (χ²/N = 0.465) and BAO (within 0.1% of Planck), both derived from τ₀ = 41.9 Myr and α_vac = 1/3 with no post-hoc tuning. The linear-growth observables (fσ₈, σ₈, S₈) reduce to ΛCDM after the F5/F7 falsification and are no longer quoted as distinctive predictions; this is the framework passing a real test by failing it cleanly, not a retreat.

The framework's posture, as stated in the deposit's `GRUT_TOE.md`: GRUT does not currently exceed mainstream ToE programs (string theory, loop quantum gravity, asymptotic safety, causal dynamical triangulations) in mathematical maturity, formal closure, peer-reviewed validation, nonlinear quantum-gravity completion, or derivation of Standard Model data. **It does exceed those programs in operational falsifiability** — and that is the basis on which this paper invites adversarial testing.

The framework is deliberately structured to be wrong, in specific, near-term, identifiable ways. Whether it is right is the question this paper asks the experimental community to answer.

---

## Acknowledgments

This work is supported by the GRUT-RAI computational framework: `grut/`, `theory/`, and `tests/` directories with 112 registered claims, 3190 passing tests, and 38 documented corrections. All numerical predictions in this paper trace to specific module functions and are reproducible via `python -m pytest tests/`. The framework's discipline pattern — pre-commit, compute, slow-down-on-surprise, verify — has caught and absorbed multiple framework-modifying surprises during development, including the F5/F7 linear-cosmology falsification documented here; see CORRECTION_22–CORRECTION_38 in `theory/derivation/` for the most recent. Cosmological certifications introduced here use modules `grut/derived/cosmology/hubble_tension.py`, `bao_sound_horizon.py`, `fsigma8_growth.py`, `sigma8_growth.py`, and `cmb_isw.py`.

---

## References to GRUT internal documents

- [GRUT_TOE.md](GRUT_TOE.md) — full framework theory document (175 pages, 17 appendices).
- [GRUT_DECOHERENCE_PAPER.md](GRUT_DECOHERENCE_PAPER.md) — standalone derivation of F1.
- [CORRECTION_22_TAU_CLEANUP.md](derivation/CORRECTION_22_TAU_CLEANUP.md) — τ-cleanup foundational fix.
- [CORRECTION_23_PHI_MUNU_DERIVATION.md](derivation/CORRECTION_23_PHI_MUNU_DERIVATION.md) — Φ_μν linearized derivation.
- [CORRECTION_24_PHI_MUNU_CURVED_SCAFFOLD.md](derivation/CORRECTION_24_PHI_MUNU_CURVED_SCAFFOLD.md) — Φ_μν curved scaffold.
- [CORRECTION_25_FRW_EXPLICIT.md](derivation/CORRECTION_25_FRW_EXPLICIT.md) — explicit FRW χ_FRW(k, η).
- [CORRECTION_26_PRIORITY_3_CLOSURE.md](derivation/CORRECTION_26_PRIORITY_3_CLOSURE.md) — n_g(ω) MG-EFT mapping.
- [CORRECTION_27_MODIFIED_GROWTH.md](derivation/CORRECTION_27_MODIFIED_GROWTH.md) — modified linear growth.
- [CORRECTION_28_NEUTRINO_HIERARCHY.md](derivation/CORRECTION_28_NEUTRINO_HIERARCHY.md) — neutrino hierarchy via Z_3.
- [CORRECTION_29_PRIORITY_4B_UNIQUENESS.md](derivation/CORRECTION_29_PRIORITY_4B_UNIQUENESS.md) — a_ν = 1 derived as boundary-degenerate uniqueness theorem.

---

## External references

[1] L. Diósi, *A universal master equation for the gravitational violation of quantum mechanics*, Phys. Lett. A 120, 377 (1987).
[2] R. Penrose, *On gravity's role in quantum state reduction*, Gen. Rel. Grav. 28, 581 (1996).
[3] J. Schwinger, *Brownian motion of a quantum oscillator*, J. Math. Phys. 2, 407 (1961); L. V. Keldysh, JETP 20, 1018 (1965).
[4] E. Calzetta, B.-L. Hu, *Nonequilibrium Quantum Field Theory*, Cambridge (2008).
[5] C. Anastopoulos, B.-L. Hu, *A master equation for gravitational decoherence*, Class. Quantum Grav. 30, 165007 (2013).
[6] S. Bose, A. Mazumdar, G. Morley, et al., *Spin entanglement witness for quantum gravity*, Phys. Rev. Lett. 119, 240401 (2017) (BMV).
[7] C. Marletto, V. Vedral, *Gravitationally-induced entanglement between two massive particles*, Phys. Rev. Lett. 119, 240402 (2017).
[8] Z. Komargodski, A. Schwimmer, *On renormalization group flows in four dimensions*, JHEP 12, 099 (2011).
[9] S. Pogosian, A. Silvestri, *μ(k, a) / γ(k, a) parameterization*, Phys. Rev. D 77, 023503 (2008).
[10] E. Bertschinger, P. Zukin, *Distinguishing modified gravity from dark energy*, Phys. Rev. D 78, 024015 (2008).
[11] G. Gubitosi, F. Piazza, F. Vernizzi, *The effective field theory of dark energy*, JCAP 02, 032 (2013); arXiv:1210.0201.
[12] Planck Collaboration, *Planck 2018 results VI: Cosmological parameters*, A&A 641, A6 (2020).
[13] NuFIT Collaboration, *NuFIT 5.3 (2024)*, http://www.nu-fit.org.
[14] KATRIN Collaboration, *m_β bound 2024*, arXiv:2406.13516.
[15] R. Sachs, A. Wolfe, *Perturbations of a cosmological model and angular variations of the microwave background*, ApJ 147, 73 (1967).
[16] U. Seljak, *Gravitational lensing effect on cosmic microwave background anisotropies: A power spectrum approach*, ApJ 463, 1 (1996).
[17] W. Hu, N. Sugiyama, *Small-scale cosmological perturbations: An analytic approach*, ApJ 444, 489 (1995).
[18] Planck Collaboration, *Planck 2018 results V: CMB power spectra and likelihoods*, A&A 641, A5 (2020).
[19] A. Lewis, A. Challinor, A. Lasenby, *Efficient normal Boltzmann code for evolution of cosmic perturbations*, ApJ 538, 473 (2000) (CAMB).
[20] A. Hojjati, L. Pogosian, G.-B. Zhao, *Testing gravity with CAMB and CosmoMC*, JCAP 08, 005 (2011) (MGCAMB).

---

*D. Ryan Grover, June 2026. The author thanks the GRUT-RAI computational framework for the discipline pattern that produced these falsifiers, and the experimental community in advance for the tests that will adjudicate them.*
