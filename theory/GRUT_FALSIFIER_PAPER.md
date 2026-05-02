# Six Near-Term Falsifiers of GRUT: A Concise Adversarial Roster

D. Ryan Grover

May 2026

Correspondence: dryangrover@gmail.com

---

## Abstract

We present six independent, near-term-testable falsifiers of the Grand Responsive Universe Theory (GRUT). Three are laboratory tests in gravity (decoherence plateau at ~689 Hz, ³⁰Si/²⁸Si isotope discriminator vs CSL, and the BMV / sub-micron-separation gravitationally-induced-entanglement protocol); two are cosmological (modified-gravity μ - 1 = 1/3 on horizon scales and Σm_ν ≈ 60 meV with normal hierarchy); and one is observational at cluster scale (gas-to-lensing offset δ ≈ v × τ_0 = 41.9 Myr). Each prediction is sharp, derived, and falsifiable on a 1–10 year timescale by named experiments and surveys (matter-wave interferometry, LIGO/lab gravity, JUNO/DUNE, DESI, Euclid, CMB-S4). Unlike most ToE programs (string theory, loop quantum gravity, asymptotic safety, causal dynamical triangulations), GRUT can be wrong in near-term ways — and it makes specific quantitative predictions, not parameter spaces. We summarize each falsifier's derivation, current observational status, and the precise condition that would refute it.

---

## 1. Why this paper

A theory of everything that cannot be falsified by experiment is, by Popperian standards, not science. Many candidate ToE programs — string theory, loop quantum gravity, asymptotic safety, and causal dynamical triangulations — produce striking mathematical structure but offer few predictions that contemporary experiments can refute. They are not wrong; they are not yet adversarial.

GRUT takes a different posture. The framework deliberately surfaces predictions that contemporary experiments can refute on near-term timescales (1–10 years). This paper enumerates six such predictions across three sectors (laboratory gravity, cosmology, Standard Model) and gives, for each:

1. The framework's prediction (sharp, quantitative).
2. The derivation reference (which module, which equation).
3. The observational test (which experiment, what precision).
4. The current observational status (consistent / borderline / tested).
5. The falsification condition (what result would refute it).

The framework has 16 documented honest negatives in its registry — gaps that have been identified, named, and tested where possible. Those negatives stand alongside these positive predictions. The framework does not hide what it cannot predict; it identifies precisely what it does predict, and at what cost the prediction can be wrong.

This is not a comprehensive review. The framework's 91-claim registry, 1643-test suite, and 28 documented corrections are referenced by claim IDs throughout. For the full theoretical machinery, see the v6 formalism paper, the v7 program document, and `theory/GRUT_TOE.md`. This paper concentrates on six near-term falsifiers that, if any one of them fails decisively, refute the framework's prediction in that sector.

---

## 2. Falsifier F1: Gravitational Decoherence Plateau at ~689 Hz

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

## 3. Falsifier F2: ³⁰Si/²⁸Si Isotope Discriminator versus CSL

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

## 4. Falsifier F3: BMV / Sub-Micron-Separation Gravitational-Entanglement Test

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

## 5. Falsifier F4: Cluster-Merger v × τ_0 Gas-to-Lensing Offset

**Sector:** Cluster astrophysics.
**Registry claim:** `cluster_merger_scaling_law`.
**Module:** `grut/derived/cluster/merger_population.py`, `bullet_cluster.py`.

### Prediction

In a binary cluster merger (post-collisional configuration), the framework predicts the gas-to-lensing offset δ scales as:

    δ ≈ v_post × τ_0 × dec_ratio                                       (3)

where v_post is the post-collision velocity of the gas relative to the dark-matter centroid, τ_0 = 41.9 Myr is the framework's macroscopic gravitational relaxation time, and dec_ratio = v_post / v_initial ≈ 0.638 is a deceleration-ratio adjustment for the gas-DM interaction.

For Bullet Cluster (1E 0657-558): v_post ≈ 3000 km/s gives δ ≈ 150 kpc — matching the observed offset. The framework's prediction is the SCALING LAW: across multiple cluster-merger systems, the gas-to-lensing offset divided by the merger velocity should equal τ_0 × dec_ratio (a universal constant).

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

A larger sample of cluster-merger systems with reconstructed v_post and δ. Sensitive to v×τ_0 scaling at the percent level if the sample reaches ~10–20 systems.

### Status

Predictive at the 1.72% level for three of four currently-measured systems. El Gordo outlier is a documented open question. Future cluster-merger surveys (Euclid + Roman + LSST) will produce a larger sample.

### Falsification condition

Any of:
- A new merger system with measured (v_post, δ) outside the τ_0 × dec_ratio band by more than 20% (not in El Gordo's specific geometry-asymmetric class).
- Reduction of the El Gordo error budget tightening δ_obs to within ~20% of δ_pred (would resolve outlier favorably; non-resolution would degrade the prediction).

A clean failure of the v × τ_0 scaling across multiple new systems falsifies the gravitational-relaxation-time interpretation of τ_0 and the framework's cluster-sector prediction.

---

## 6. Falsifier F5: Modified-Gravity μ − 1 = 1/3 on Horizon Scales

**Sector:** Cosmological perturbations (modified-gravity EFT-of-dark-energy).
**Registry claim:** `mg_eft_mu_gamma_mapping`, `modified_linear_growth_first_look`.
**Module:** `grut/derivation/phi_munu/mg_eft_mapping.py`, `modified_growth.py`.
**Correction documents:** CORRECTION_26 (MG-EFT mapping), CORRECTION_27 (modified growth).

### Prediction

The framework's covariant derivation of the gravitational constitutive correction Φ_μν (from δS_CTP/δh_a, Corrections #23–#25) produces an explicit modified-gravity μ(k, a) function on FRW backgrounds:

    μ_GRUT(k, a) = n_g²(k, a) = 1 + α_vac / [1 + (τ_0 k_phys(a))²]    (4)

with α_vac = 1/3 (Komargodski-Schwimmer trace-anomaly real-scalar identification, PROVEN). The framework also predicts γ_GRUT = 1 (no gravitational slip — TT-projector argument).

Limits:
- **Sub-horizon** (k_phys τ_0 ≫ 1): μ → 1, γ = 1 → ΛCDM recovery.
- **Super-horizon** (k_phys τ_0 ≪ 1): **μ → 1 + α_vac = 4/3, γ = 1**.
- Transition: λ_* ≈ 80.7 Mpc (today).

The largest cosmological scales experience a 33% boost to gravitational coupling. This is a **SHARP PREDICTION**: μ − 1 = 1/3 on horizon scales, γ = 1.

### Modified linear growth (Correction #27)

Numerical integration of δ'' + [2 − (3/2)Ω_m] δ' − (3/2) Ω_m μ_GRUT(k, N) δ = 0 on a Planck-2018 ΛCDM background gives:

| Scale | k [Mpc⁻¹] | f_GRUT(z=0) = D_GRUT/D_ΛCDM |
|:---|:---|:---|
| σ_8 | 0.5 | **1.0009** (0.09%, NOT broken) |
| BAO | 0.04 | 1.085 (8.5%) |
| CMB low-ℓ | 0.001 | 2.024 (102%) |
| CMB horizon | 4.5×10⁻⁴ | 2.348 (135%) |

The σ_8-scale enhancement (0.09%) is BELOW current observational precision — GRUT does not catastrophically break the σ_8 / S_8 measurement that drives the existing tension between Planck CMB and weak-lensing surveys.

### Test

DESI Y3+ (2025–2027) targets ~5% precision on μ at large scales. Euclid (2027+) and CMB-S4 target ~1% precision — a definitive test.

### Current status

Planck 2018 paper VI gives μ₀ − 1 = 0.07 ± 0.13 (1σ). GRUT's prediction (1/3 ≈ 0.33) is ~2σ above the central value but within current bounds.

### Falsification condition

DESI / Euclid / CMB-S4 measurement of μ₀ − 1 with precision better than 0.10:
- If μ₀ − 1 = 1/3 ± 0.05: GRUT confirmed at high confidence.
- If μ₀ − 1 < 0.20 at >3σ: GRUT's α_vac = 1/3 falsified on cosmological scales (would also tension the conformal-mode-scalar derivation upstream).
- If γ ≠ 1 measured at >2σ: GRUT's TT-projector argument falsified (distinguishes from Brans-Dicke, f(R), DGP — all predict γ ≠ 1).

---

## 7. Falsifier F6: Σm_ν ≈ 60 meV with Normal Hierarchy

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

## 8. The Pattern: GRUT vs Other ToE Programs

| Program | Predicts μ at horizon? | Predicts m_ν? | Lab decoherence rate? | Cluster offset? |
|:---|:---|:---|:---|:---|
| String theory | landscape (no fixed prediction) | landscape | landscape | landscape |
| Loop quantum gravity | unclear; cosmological extension underway | not derived | not derived | not derived |
| Asymptotic safety | weak prediction; depends on UV fixed point | not derived | not derived | not derived |
| Causal dynamical triangulations | early-universe predictions only | not derived | not derived | not derived |
| **GRUT** | **μ − 1 = 1/3** | **NH, Σm_ν ≈ 60 meV** | **689 Hz at gold benchmark** | **δ = v × 41.9 Myr × 0.638** |

GRUT's posture: **the framework can be wrong in near-term ways**. The above table is the framework's load-bearing claim about its own falsifiability — not "more rigorous" than other programs (asymptotic safety has greater nonperturbative-completion maturity; string theory has greater mathematical depth), but **more adversarial**. Each of the six predictions above either survives the next 1–10 years of experiment, or it doesn't. The framework offers no hiding place behind a parameter space.

---

## 9. The Honest-Negative Roster

In the framework's tradition of explicit negative documentation, the following gaps stand alongside the positive predictions:

| Gap | Status | Effect |
|:---|:---|:---|
| `koide_phase_4_open_negative` | Open: mechanism for (M_0, θ) selection in Z_3 | Charged-lepton structure proven, mechanism not derived |
| `tji_7_4_open_negative` | Phase-1 (Allen-Jacobson S⁴) work pending | Curved-TJI route to R = 1.15428 not closed |
| `nonlinear_ladder_4_of_8` | 4 of 8 rungs complete | Nonlinear gravity recovery partial |
| `phi_munu_frw_beyond_wkb_open_question` | (Hτ_0)² ≈ 10⁻⁶ correction | Beyond-WKB cosmological correction deferred |
| ~~`neutrino_z3_coupling_derivation_open_question`~~ | RESOLVED (Correction #29, Priority 4B) — uniqueness theorem | (was: NH prediction conditional on postulate; now derived) |
| `n_total_zero_parameter_derivation_open_question` | N_total = 329 anchor uses observed t_0 | One observational anchor in Hubble route |
| `primordial_amplitude_zero_parameter_open_negative` | A_s scaling-conditional | Pivot-mode normalization pending |
| `track_v_coupling_unification_open_question` | 8.9% miss at GUT scale | β-correction not derived |
| `vorton_track_vii_open_negative` | M_vorton/M_soliton 450× discrepancy | Topological-defect route falsified, dielectric route preferred |
| `el_gordo_outlier_open_question` | δ_obs / δ_pred = 3.5× outlier | Cluster-merger fit good for 3/4 systems |
| `rho_max_scale_open_question` | ρ_max ≈ 10⁻²² kg/m³ scale | Whole-Hole quantitative interior pending |
| `path_f_translation_gap` | Im(W) → R conversion gap | Path F closure pending |

These open negatives are not predictions the framework makes — they are gaps the framework explicitly documents. The deposit's posture is honest: predict where it can; document gaps where it cannot.

---

## 10. Conclusion

GRUT presents six near-term-testable falsifiers across three sectors:

| # | Falsifier | Sector | Timeline |
|:---|:---|:---|:---|
| F1 | Decoherence plateau ~689 Hz | Lab gravity | 5–10 yr |
| F2 | ³⁰Si/²⁸Si discriminator | Lab gravity | 5–10 yr |
| F3 | Sub-micron-BMV near-field | Lab gravity | 5–10 yr |
| F4 | Cluster-merger v × τ_0 | Cluster astrophysics | 1–5 yr (sample growth) |
| F5 | μ − 1 = 1/3 modified-gravity | Cosmology | 2–5 yr (DESI/Euclid) |
| F6 | Σm_ν ≈ 60 meV / NH | Standard Model + cosmology | 2–10 yr (JUNO/DESI/Euclid) |

If all six survive their next-decade tests, the framework is supported as a unified description of gravity, cosmology, and the Standard Model from a single set of axioms. If any one fails decisively, the corresponding sector of the framework is falsified — with cascading consequences on the upstream derivations.

The framework's posture, as stated in the deposit's `GRUT_TOE.md`: GRUT does not currently exceed mainstream ToE programs (string theory, loop quantum gravity, asymptotic safety, causal dynamical triangulations) in mathematical maturity, formal closure, peer-reviewed validation, nonlinear quantum-gravity completion, or derivation of Standard Model data. **It does exceed those programs in operational falsifiability** — and that is the basis on which this paper invites adversarial testing.

The framework is deliberately structured to be wrong, in specific, near-term, identifiable ways. Whether it is right is the question this paper asks the experimental community to answer.

---

## Acknowledgments

This work is supported by the GRUT-RAI computational framework: `grut/`, `theory/`, and `tests/` directories with 91 registered claims, 1643 passing tests, and 28 documented corrections. All numerical predictions in this paper trace to specific module functions and are reproducible via `python -m pytest tests/`. The framework's discipline pattern — pre-commit, compute, slow-down-on-surprise, verify — has caught and absorbed multiple framework-modifying surprises during development; see CORRECTION_22–CORRECTION_28 in `theory/derivation/` for the most recent.

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

---

*D. Ryan Grover, May 2026. The author thanks the GRUT-RAI computational framework for the discipline pattern that produced these falsifiers, and the experimental community in advance for the tests that will adjudicate them.*
