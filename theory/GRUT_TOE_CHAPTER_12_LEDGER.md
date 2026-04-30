<frozen runpy>:128: RuntimeWarning: 'grut.toe.render' found in sys.modules after import of package 'grut.toe', but prior to execution of 'grut.toe.render'; this may result in unpredictable behaviour
## Open Questions — Auto-rendered Ledger

*This section is auto-generated from `grut/toe/ledger.py` and `grut/toe/registry.py`. To update, edit the ledger entry or registry claim and re-render via `python3 -m grut.toe.render`. Manual edits below this header will be overwritten on regeneration.*

Each open negative below names a specific gap in the framework, with a falsifiable closure condition, a rough effort estimate, and the downstream claims that would be hardened by closure. Open negatives are not deferred promises — they are documented limits on what the framework currently predicts. A specialist reading this section should leave with a complete map of what is open, what would close each item, and what depends on each closure.

### Coverage check

All 15 registry open negatives have ledger entries. ✓

### Summary

| Ch | Claim ID | Fan-out | Effort | Affects |
|:---|:---|---:|:---|:---|
| 6 | `nonlinear_ladder_4_of_8` | 0 | Multi-phase. Rungs 5-6 are tractable in Phase-2... | gr_recovery, bh_information_partial |
| 7 | `tji_7_4_open_negative` | 3 | ~3 weeks specialist work (Phase-1; requires cur... | three_routes_convergence, r_canonical_path_g, h_inf_decom... |
| 12 | `el_gordo_outlier_open_question` | 1 | Phase-2+. Depends on either new observational d... | cluster_merger_scaling_law |
| 12 | `allen_jacobson_phase1_stub_open_negative` | 0 | ~3 weeks specialist work — same envelope as TJI... | tji_7_4_open_negative |
| 12 | `constitutive_projection_gravity_heuristic_open_question` | 0 | Theoretical work, ~3-6 weeks for someone fluent... | gr_recovery |
| 12 | `koide_phase_4_open_negative` | 0 | Open-ended; multiple research-tier attempts hav... | sm_emergence, koide_z3_circulant_structure |
| 12 | `n_g_omega_cosmological_covariance_open_question` | 0 | Theoretical work, ~2-4 weeks for someone fluent... | cmb_boltzmann_scoping |
| 12 | `n_total_zero_parameter_derivation_open_question` | 0 | Multi-phase research. Blocked by Genesis Hypoth... | h_0_prediction |
| 12 | `path_f_translation_gap` | 0 | Research-tier; depends on whether the gap is a ... | r_canonical_path_g |
| 12 | `primordial_amplitude_zero_parameter_open_negative` | 0 | Multi-phase research. Closure path (a) is block... | h_0_prediction |
| 12 | `rho_max_scale_open_question` | 0 | Phase-1+ task. Requires either observational co... | rho_max_universal, bh_information_partial |
| 12 | `t_c_provenance_inconsistency_open_negative` | 0 | Multi-session research. The closure work has th... | t_c_thermal_transition |
| 12 | `track_v_coupling_unification_open_question` | 0 | Specialist QFT-renormalization-group work, ~6-1... | sm_emergence |
| 12 | `two_route_convergence_physical_equivalence_open_question` | 0 | Theoretical work, ~2-4 weeks. Requires fluency ... | three_routes_convergence |
| 12 | `vorton_track_vii_open_negative` | 0 | Research-tier. The dielectric route (dielectric... | dark_sector_u1_extension |

### Closure-priority ranking

Each open negative's _fan-out_ is the number of downstream claims that depend (transitively) on the gap. Closing a high-fan-out gap hardens more of the framework than closing a low-fan-out one. The list is auto-ranked from the dependency graph; this is the recommended attack order, not a wish list.

| Rank | Fan-out | Claim ID | Effort |
|---:|---:|:---|:---|
| 1 | 3 | `tji_7_4_open_negative` | ~3 weeks specialist work (Phase-1; requires cur... |
| 2 | 1 | `el_gordo_outlier_open_question` | Phase-2+. Depends on either new observational d... |
| 3 | 0 | `allen_jacobson_phase1_stub_open_negative` | ~3 weeks specialist work — same envelope as TJI... |
| 4 | 0 | `constitutive_projection_gravity_heuristic_open_question` | Theoretical work, ~3-6 weeks for someone fluent... |
| 5 | 0 | `koide_phase_4_open_negative` | Open-ended; multiple research-tier attempts hav... |
| 6 | 0 | `n_g_omega_cosmological_covariance_open_question` | Theoretical work, ~2-4 weeks for someone fluent... |
| 7 | 0 | `n_total_zero_parameter_derivation_open_question` | Multi-phase research. Blocked by Genesis Hypoth... |
| 8 | 0 | `nonlinear_ladder_4_of_8` | Multi-phase. Rungs 5-6 are tractable in Phase-2... |
| 9 | 0 | `path_f_translation_gap` | Research-tier; depends on whether the gap is a ... |
| 10 | 0 | `primordial_amplitude_zero_parameter_open_negative` | Multi-phase research. Closure path (a) is block... |
| 11 | 0 | `rho_max_scale_open_question` | Phase-1+ task. Requires either observational co... |
| 12 | 0 | `t_c_provenance_inconsistency_open_negative` | Multi-session research. The closure work has th... |
| 13 | 0 | `track_v_coupling_unification_open_question` | Specialist QFT-renormalization-group work, ~6-1... |
| 14 | 0 | `two_route_convergence_physical_equivalence_open_question` | Theoretical work, ~2-4 weeks. Requires fluency ... |
| 15 | 0 | `vorton_track_vii_open_negative` | Research-tier. The dielectric route (dielectric... |

### Inter-gap dependency map

Some open negatives are blocked by others — closing the blocker is a prerequisite. The arrows below read 'closure of X requires closure of Y'.

```
  tji_7_4_open_negative
    └── blocked by → allen_jacobson_phase1_stub_open_negative
  primordial_amplitude_zero_parameter_open_negative
    └── blocked by → n_g_omega_cosmological_covariance_open_question
```

### Detailed entries

### nonlinear_ladder_4_of_8

**Chapter.** 6

**Statement.** The nonlinear-gravity ladder has 4 of 8 rungs explicitly computed (V7 §22-§25): linearized recovery, second-order consistency, third-order matching, and constitutive back-reaction. Rungs 5-8 (full nonlinear closure) remain open.

**Closure condition.** Closure of rungs 5-8 of the nonlinear ladder: tensor-sector stability at 2nd order, diffeomorphism invariance preservation, background independence, and a non-perturbative fixed point. Each rung is a separate research program.

**Closure effort.** Multi-phase. Rungs 5-6 are tractable in Phase-2 timeframes; rungs 7-8 are open research.

**Affects (claims hardened on closure).**
- `gr_recovery` (Ch 6, fan-out 2)
- `bh_information_partial` (Ch 10, fan-out 0)

**References.**
- V7 §22-§25
- V7 §43 outstanding work

**Last reviewed.** 2026-04-26

---

### tji_7_4_open_negative

**Chapter.** 7

**Statement.** The TJI 3-loop path on flat space produces raw Laurent coefficient −541/2304 at ε⁰ in the gamma-function scheme. Reconciliation to V7 §26.2.3's claimed 7/4 (FeynCalc) was attempted across 24 scheme configurations and FAILED. HONEST NEGATIVE.

**Closure condition.** Curved-space TJI on Euclidean S⁴ produces the FeynCalc-claimed +7/4 from a fully verified Laurent expansion in MS-bar (or any consistent scheme). Specifically, the Allen-Jacobson S⁴ propagator must be activated and a scheme-coherent reconciliation produced — not a Phase-0/0.5 flat-space calculation.

**Closure effort.** ~3 weeks specialist work (Phase-1; requires curved-space TJI machinery + scheme-handling). The Allen-Jacobson stub module sits ready as the entry point.

**Affects (claims hardened on closure).**
- `three_routes_convergence` (Ch 7, fan-out 1)
- `r_canonical_path_g` (Ch 7, fan-out 16)
- `h_inf_decomposition` (Ch 8, fan-out 4)

**Blocked by (upstream open negatives).**
- `allen_jacobson_phase1_stub_open_negative` — must close before this can close

**Closure dependency chain.** `tji_7_4_open_negative` blocked through `allen_jacobson_phase1_stub_open_negative`.

**References.**
- theory/derivation/CORRECTION_21_TJI_PHASE_0P5_SCHEME_RECONCILIATION.md
- grut/derivation/tji/flat_space.py
- grut/derivation/tji/ms_bar_reconciliation.py

**Tests pinning the gap.**
- `tests/derivation/tji/test_flat_space.py::test_raw_scheme_value_differs_from_feyncalc_by_scheme`
- `tests/derivation/tji/test_ms_bar_reconciliation.py`

**Last reviewed.** 2026-04-26

---

### allen_jacobson_phase1_stub_open_negative

**Chapter.** 12

**Statement.** The Allen-Jacobson S⁴ propagator module is a STUB — every evaluation function raises Phase1Pending (a NotImplementedError subclass). The interface is pinned by regression tests so silent activation cannot occur. Phase-1 (curved-space TJI) replaces the stub with forward evaluation; until then this is an explicit open negative.

**Closure condition.** Phase-1 implementation of the Allen-Jacobson S⁴ propagator module — i.e. all evaluation functions return numerical values rather than raising Phase1Pending. This unlocks curved-space TJI calculations that in turn unlock tji_7_4_open_negative.

**Closure effort.** ~3 weeks specialist work — same envelope as TJI Phase-1 since they're tightly coupled.

**Affects (claims hardened on closure).**
- `tji_7_4_open_negative` (Ch 7, fan-out 3)

**References.**
- grut/derivation/tji/allen_jacobson.py

**Tests pinning the gap.**
- `tests/derivation/tji/test_allen_jacobson.py`

**Last reviewed.** 2026-04-26

---

### constitutive_projection_gravity_heuristic_open_question

**Chapter.** 12

**Statement.** The constitutive Einstein equation G_μν + Φ_μν[φ] = 8πG T_μν, central to the framework's gravity sector, carries Φ_μν as a constitutive correction — but Φ_μν itself is not derived rigorously from the CTP action's variation. The seven legs of gr_recovery verify limits (high-frequency vanishing, low-frequency enhancement), Bianchi consistency on a single-mode plane wave, and graviton-propagator UV falloff. They verify behavior, not the form of Φ_μν. Chapter 12's 'What GRUT does NOT claim' section already acknowledges 'the constitutive projection is exact in gravity/cosmology (it is heuristic there)'. This entry formalizes that disclaimer at registry/ledger level so the gravity-sector tiering is structurally honest. The cosmological-perturbation sister gap is n_g_omega_cosmological_covariance — both have the same shape: a heuristic projection that needs covariant derivation.

**Closure condition.** Either: (a) derive Φ_μν explicitly from δS_CTP/δh_μν in the gravitational sector, with gauge-fixing prescription and Bianchi preservation shown rigorously across general (ω, k) — not just a single-mode plane wave; OR (b) formally retier gr_recovery from 'computed' to 'anchored — constitutive projection heuristic in gravity' so the document and registry agree on the tiering. Path (a) closes the framework; path (b) preserves honesty about what's been shown.

**Closure effort.** Theoretical work, ~3-6 weeks for someone fluent in curved-space CTP. Tightly coupled to the cosmological-perturbation sister gap (n_g_omega_cosmological_covariance); closing both is one larger task.

**Affects (claims hardened on closure).**
- `gr_recovery` (Ch 6, fan-out 2)

**References.**
- V7 §22-§25 (gravity sector)
- Calzetta-Hu (2008) Nonequilibrium Quantum Field Theory — for CTP variation in gauge theories
- grut/foundation/gr_recovery.py

**Last reviewed.** 2026-04-26

---

### el_gordo_outlier_open_question

**Chapter.** 12

**Statement.** ACT-CL J0102-4915 (El Gordo) was originally tagged as a factor-3.5 outlier (canonical 70 kpc prediction vs ~250 kpc observed). Sensitivity analysis across the published parameter ranges (v_initial 2000-3500 km/s, t_since 70-300 Myr, dec_ratio 0.5-0.85, observed offset 120-600 kpc) shows the framework's prediction range (43-130 kpc) OVERLAPS with the lower part of the observed range. Specifically: at observed = 120 kpc (lower bound, individual subclump centroids), best-case GRUT prediction matches at ratio ~1.09 — fully consistent. At observed = 150 kpc, ratio ~0.87 — same as Bullet, MACS, Abell 520. Only at observed > 250 kpc (upper-range parametric reconstructions like Jee 2014 NW clump) does the deviation become decisive. The factor-3.5 outlier framing was specific to one parameter point AND one offset value; actual data does not robustly reject the framework.

**Closure condition.** Either: (a) tighter observational constraints on El Gordo's velocity/geometry/lensing reconstruction that bring the observed gas-to-lensing offset into the v×τ_0 band (within factor 2), OR (b) extension of the kernel model to off-axis / asymmetric-mass collisions producing a derived correction factor that explains the ~3.5× deviation, OR (c) an additional cluster sample showing the v×τ_0 scaling extends across all merger types and El Gordo is the documented exception.

**Closure effort.** Phase-2+. Depends on either new observational data or an analytic extension of the kernel-convolution model. Observational data may resolve before the model needs extension.

**Affects (claims hardened on closure).**
- `cluster_merger_scaling_law` (Ch 9, fan-out 6)

**References.**
- Jee et al. 2014 (ApJ 785 20, arXiv:1401.3356)
- Menanteau et al. 2012
- Diego et al. 2023 (free-form lensing)
- grut/derived/cluster/merger_population.py:EL_GORDO

**Tests pinning the gap.**
- `tests/derived/test_merger_population.py::TestPerSystemPredictions::test_el_gordo_is_explicit_outlier`
- `tests/derived/test_merger_population.py::TestElGordoOutlierIsHonestNegative`

**Last reviewed.** 2026-04-26

---

### koide_phase_4_open_negative

**Chapter.** 12

**Statement.** Track II Phase 4 (Koide flavor mechanism) was attempted and produced HONEST NEGATIVE: the Yukawa-hierarchy mechanism cannot be derived from V7's current machinery. Phase 4.0 scope document delivered.

**Closure condition.** A computational mechanism that fixes (M_0, θ) from the framework's machinery — i.e. the Z_3 circulant operator is no longer a 2-parameter family but a unique solution to a CTP-derived constraint. Track II Phase 4.0 scope document delivered; Phase 4 itself remains open.

**Closure effort.** Open-ended; multiple research-tier attempts have produced honest negatives. Phase-2+ task at minimum.

**Affects (claims hardened on closure).**
- `sm_emergence` (Ch 5, fan-out 7)
- `koide_z3_circulant_structure` (Ch 9, fan-out 1)

**References.**
- theory/derivation/CORRECTION_20_KOIDE_PHASE_4_FLAVOR_MECHANISM.md
- theory/derivation/CORRECTION_18_KOIDE_PHASE_2_MASS_ANCHOR.md
- theory/derivation/CORRECTION_17_KOIDE_DERIVATION_ATTEMPT.md
- grut/derived/flavor/koide_operator.py

**Tests pinning the gap.**
- `tests/flavor/test_koide_operator.py`

**Last reviewed.** 2026-04-26

---

### n_g_omega_cosmological_covariance_open_question

**Chapter.** 12

**Statement.** The framework writes n_g²(ω) as a Lorentzian susceptibility factor that modifies the gravitational Poisson equation in the cosmological-perturbation sector. In a laboratory frame ω is a well-defined oscillation frequency in the local Lorentz frame. In cosmological perturbations, modes are characterized by comoving wavenumber k with time-evolving amplitudes — 'frequency' could mean (a) mode oscillation rate ~ k·c_s for adiabatic modes near recombination, (b) conformal-time Fourier frequency, (c) ∂_t Φ / Φ in Newtonian gauge, or (d) a covariantly-defined object yet to be specified. The framework has not articulated which ω the n_g(ω) modification uses or how it transforms under gauge changes (synchronous ↔ Newtonian ↔ comoving). This is a real theoretical gap that must close before the CMB scoping prediction can be promoted from scoping-tier to falsifier-tier.

**Closure condition.** Articulate a covariant, gauge-invariant formulation of n_g(ω) in cosmological perturbations. Specifically: (1) specify whether ω corresponds to mode oscillation frequency (k c_s), conformal-time Fourier frequency, ∂_t Φ / Φ, or a covariantly-defined object; (2) verify the formulation transforms correctly under standard gauge choices (synchronous, Newtonian, comoving); (3) map to the μ(k,a) / γ(k,a) parameterization in modified-gravity EFT-of-dark-energy literature so the framework's prediction is comparable to existing observational constraints (Planck MG analyses, DESI, Euclid forecasts).

**Closure effort.** Theoretical work, ~2-4 weeks for someone fluent in EFT of dark energy / modified-gravity perturbation theory. Must close BEFORE the CMB Boltzmann implementation (otherwise the implementation has no well-defined ω to use). Phase-2 prerequisite.

**Affects (claims hardened on closure).**
- `cmb_boltzmann_scoping` (Ch 9, fan-out 0)

**References.**
- theory/CMB_BOLTZMANN_SCOPING.md
- Gubitosi-Piazza-Vernizzi 2013 (EFT of dark energy, arXiv:1210.0201) — for μ(k,a)/γ(k,a) parameterization
- Pogosian-Silvestri 2008 (μ-γ MG parameterization)
- grut/derived/cmb/scoping.py

**Last reviewed.** 2026-04-26

---

### n_total_zero_parameter_derivation_open_question

**Chapter.** 12

**Statement.** GRUT's detailed Hubble-from-first-principles route (grut/derived/cosmology/hubble_from_first_principles.py: grut_H_0_prediction) computes H_0 = 69.03 km/s/Mpc via flat-ΛCDM Friedmann integration. Inputs: R_anomaly (computed), S_CTP (computed), τ_0 = 41.9 Myr (posited with two anchors), and N_total = 329 eras (observed-age anchor — t_0 ≈ 13.78 Gyr ÷ τ_0 = 329). The single observational anchor is N_total. A zero-parameter derivation of N_total (or equivalently cosmic age) from framework foundations alone does not currently exist. Four direct attempts (theory/derivation/N_TOTAL_DERIVATION_ATTEMPT.md) all closed negative: matter-Λ equality from H_inf gives N_threshold = 235.7 vs V7's 215 (9.6% off); era-map sigmoid dynamics saturate at era ~250 before reaching 329; total-age-via-Friedmann requires Ω_m as input which is the same problem reframed; reverse-engineering Ω_m from N_total = 329 yields Ω_m = 0.29 (6.8% from Planck's 0.3111), confirming N_total is observation-anchored rather than structurally derived. The simpler cosmic-baseline H_0 = 68.8 km/s/Mpc (registry claim h_0_prediction, formula H_0 = 1/(S × τ_0)) is zero-parameter and does NOT depend on N_total — this open negative applies only to the detailed Friedmann route.

**Closure condition.** Derive cosmic age t_0 — equivalently the era count N_total = t_0/τ_0 = 329 — from framework foundations alone, without using observed cosmic age as input. The era-map post-threshold dynamics must produce N_total = 329 as a structural endpoint (not a fit to observation). Likely precondition: the Genesis Hypothesis (V7/V8 Appendix A) being formalized to the point where the start time of cosmic evolution emerges from the null fixed point's destabilization timescale. Genesis Hypothesis is currently [SPECULATIVE]; closure does NOT require adopting it as a postulate — it requires the hypothesis's machinery becoming computable. Alternative closure paths: (a) derive Ω_m today from baryogenesis (Ω_b = 0.048 already computed) plus a first-principles Ω_dm derivation that doesn't currently exist (Track VII Step 3 closed negative), or (b) anchor cosmic age to a structurally-predicted event (e.g. CMB decoupling conditions from SM thermodynamics).

**Closure effort.** Multi-phase research. Blocked by Genesis Hypothesis becoming formal/computable rather than purely conjectural. Four direct attempts already documented as honest-negative in N_TOTAL_DERIVATION_ATTEMPT.md (matter-Λ equality structural anchor, era-map saturation, flat-ΛCDM total age, reverse-engineered Ω_m). Closure tied to Track VII Step 3 status (vorton Ω_dm derivation closed negative; dielectric route preferred but not yet zero-parameter).

**Affects (claims hardened on closure).**
- `h_0_prediction` (Ch 8, fan-out 1)

**References.**
- grut/derived/cosmology/hubble_from_first_principles.py:grut_H_0_prediction
- theory/derivation/N_TOTAL_DERIVATION_ATTEMPT.md
- tests/derived/test_hubble_from_first_principles.py

**Tests pinning the gap.**
- `tests/derived/test_hubble_from_first_principles.py`

**Last reviewed.** 2026-04-27

---

### path_f_translation_gap

**Chapter.** 12

**Statement.** Path F (Im Γ on de Sitter) was investigated as an alternate route to V7's R = 1.15428. Published Im(W) on dS computes particle-production rates, NOT V7's ratio. Translation gap documented as HONEST NEGATIVE.

**Closure condition.** A mapping from published Im(W) on de Sitter (which computes particle-production rates via Bogoliubov coefficients) to V7's R = |C_Cosmo / C_Final| ratio, OR an alternate Path F formulation that produces the framework's R directly. Multiple literature scopings have documented the gap.

**Closure effort.** Research-tier; depends on whether the gap is a convention difference or a deeper mismatch.

**Affects (claims hardened on closure).**
- `r_canonical_path_g` (Ch 7, fan-out 16)

**References.**
- theory/path_f_imaginary_action/STAGE_0_LITERATURE.md
- theory/path_f_imaginary_action/STAGE_F_C_CALCULATION.md
- Zhou-Zhang 2025 (arXiv:2510.13712)

**Last reviewed.** 2026-04-26

---

### primordial_amplitude_zero_parameter_open_negative

**Chapter.** 12

**Statement.** The primordial scalar amplitude A_s ≈ 2.1 × 10⁻⁹ (Planck 2018) is observation-anchored, not derived zero-parameter from GRUT's CTP infrastructure. Three computational paths attempted (grut/derived/cosmology/primordial_amplitude.py): (A) Ornstein-Uhlenbeck variance of metric perturbations driven by the KMS noise kernel at T = T_CMB, Planck-rescaled — yields ~2 × 10⁻¹⁹, factor 10¹⁰ too small; (B) standard inflationary formula A_s = H²/(8π² ε M²_Pl,red) with GRUT's terminal-velocity H_inf and ε = (Hτ₀)² — yields ~5 × 10⁻¹¹⁸, factor 10¹⁰⁹ too small (expected: GRUT has no inflationary epoch); (C) 11 natural dimensional candidates from α, S, H_inf, τ₀, T_c — the closest, α/S³ = (1/3)/(108π)³ ≈ 8.5 × 10⁻⁹, lands at factor 4 from observed but is NOT promoted to a derivation: with 11 candidates tested, finding ~1 within a decade is statistically plausible coincidence. The α/S³ coincidence is documented as a CLUE worth physical motivation. Honest verdict: HONEST_NEGATIVE_WITH_DIMENSIONAL_CLUE.

**Closure condition.** Either (a) close n_g_omega_cosmological_covariance_open_question (#9) — gauge-invariant cosmological perturbation theory in the framework, with a defined natural rescaling for P_ζ. Stage-2 forward derivation showed: under cosmic-baseline rescaling P_ζ → 1/(πS³) ≈ 8.15×10⁻⁹ (factor 4 from observed A_s, in α/S³ family); under Planck rescaling P_ζ → (1/π)(t_Pl/τ_0)³ ≈ 10⁻¹⁷⁶ (fails by 167 orders). Closing #9 selects between these. OR (b) the Genesis Hypothesis (Appendix A) is formalized providing an inflationary-like epoch with H ~ 10⁻⁵ M_Pl during horizon crossing of the CMB pivot mode (independent of #9 closure). OR (c) a physically-motivated derivation that yields A_s ~ α/S³ from the noise kernel structure (promoting the Stage-1 coincidence to evidence). OR (d) explicit acknowledgment that A_s is observation-anchored input.

**Closure effort.** Multi-phase research. Closure path (a) is blocked by n_g_omega_cosmological_covariance_open_question — gauge-invariant cosmological perturbation theory is tractable specialist work (~2-4 weeks per the existing ledger entry for #9). Path (b) blocked by Genesis Hypothesis becoming formal/computable. Path (c) requires identifying what physical observable in GRUT plays the role of primordial curvature ζ. The Stage-2 forward investigation has narrowed the gap: the α/S³ family IS conditionally derivable (under rescaling choices B or C), but the rescaling itself is the upstream gap.

**Affects (claims hardened on closure).**
- `h_0_prediction` (Ch 8, fan-out 1)

**Blocked by (upstream open negatives).**
- `n_g_omega_cosmological_covariance_open_question` — must close before this can close

**Closure dependency chain.** `primordial_amplitude_zero_parameter_open_negative` blocked through `n_g_omega_cosmological_covariance_open_question`.

**References.**
- grut/derived/cosmology/primordial_amplitude.py
- grut/derived/cosmology/primordial_curvature.py
- grut/derived/cosmology/spectral_running.py
- grut/foundation/noise_kernel.py
- theory/derivation/PRIMORDIAL_ALPHA_S3_INVESTIGATION.md
- tests/derived/test_primordial_amplitude.py
- tests/derived/test_primordial_curvature.py

**Tests pinning the gap.**
- `tests/derived/test_primordial_amplitude.py`
- `tests/derived/test_primordial_curvature.py`

**Last reviewed.** 2026-04-28

---

### rho_max_scale_open_question

**Chapter.** 12

**Statement.** The universal-τ_0 form ρ_max ~ 10⁻²² kg/m³ is cosmologically weak and below typical naive BH interior densities. Whether additional structure is needed for quantitatively realistic core sizes is open.

**Closure condition.** Either (a) demonstration that ρ_max ~ 10⁻²² kg/m³ is compatible with observed BH interior dynamics under specific Whole-Hole geometry, OR (b) derivation of additional structure (e.g. curvature-dependent τ_eff) that produces quantitatively realistic core sizes without breaking the universal-τ_0 derivation upstream.

**Closure effort.** Phase-1+ task. Requires either observational constraint or derived correction to the universal formula.

**Affects (claims hardened on closure).**
- `rho_max_universal` (Ch 6, fan-out 2)
- `bh_information_partial` (Ch 10, fan-out 0)

**References.**
- grut/foundation/closure_protocol.py:RHO_MAX_KG_M3

**Last reviewed.** 2026-04-26

---

### t_c_provenance_inconsistency_open_negative

**Chapter.** 12

**Statement.** The framework's T_c = 54.7 MK value is propagated through both V7 documentation (V7 §0.5, V7 §22) and the codebase (grut/foundation/closure_protocol.py:T_C_KELVIN, grut/derived/cosmology/thermal_transition.py) via the formula T_c = 1/(τ_0 × k_B). With τ_0 = 41.9 Myr in SI seconds and k_B in J/K, this formula is dimensionally inconsistent — it produces units K/(J·s), not K. The SI-correct expression of the same physics, T_c = ℏ/(τ_0 × k_B), gives 5.78×10⁻²⁷ K, NOT 54.7 MK. The 'v9 natural-units convention (ℏ=1)' defense in the codebase docstring does not recover the 54.7 MK value: converting τ_0 = 41.9 Myr to natural units (eV⁻¹) and computing 1/τ_0_nat gives 5.78×10⁻²⁷ K identically. The 54.7 MK value emerges only by treating the SI numerical operation 1/(1.32×10¹⁵ × 1.38×10⁻²³) as a temperature in K, which is dimensionally invalid. Cross-check: μ_0 = ℏ/τ_0 (computed correctly with ℏ in the same closure_protocol.py) gives 5.78×10⁻²⁷ K when expressed as a temperature, contradicting the 54.7 MK narrative. The framework's cosmological narrative ('T ≈ T_c at ~1 hour post-Big Bang') REQUIRES T_c at MK scale (standard cosmology gives T ~ 10⁸ K at t = 1 h post-BB), anchoring 54.7 MK as the intended physical value despite the formula's dimensional issue. STRUCTURAL DIAGNOSIS: the framework has been using one symbol (τ_0) and one formula for two distinct physical scales — the macroscopic gravitational relaxation time τ_0 = 41.9 Myr (load-bearing for cosmological-scale phenomena: dark-sector refractive enhancement, Hubble terminal velocity, cluster gas-to-lensing offset scaling — these stand intact), and an implicit microscopic plasma relaxation time τ_micro ≈ 1.4×10⁻¹⁹ s (required to make T_c = ℏ/(τ_micro × k_B) = 54.7 MK dimensionally consistent). The 34-orders-of-magnitude separation between τ_0 (1.32×10¹⁵ s) and τ_micro (~10⁻¹⁹ s, atomic-transition timescale) means these are different physical scales, conflated in the current T_c formula.

**Closure condition.** The framework must explicitly define a microscopic relaxation timescale τ_micro for the primordial plasma, decoupled from the macroscopic geometric relaxation τ_0 = 41.9 Myr. Specifically: identify the physical origin of τ_micro (e.g., atomic-transition timescale, weak-interaction rate at the relevant energy, or a specific CTP plasma-dynamics derivation), motivate the value τ_micro ≈ 1.4×10⁻¹⁹ s from framework physics or from a documented external anchor, AND derive (or explicitly postulate) the relationship between τ_micro and τ_0 — they may be independent inputs, related by a specific scale-bridge formula, or otherwise. Once τ_micro is formalized, T_c = ℏ/(τ_micro × k_B) produces 54.7 MK consistently with the cosmological narrative (T_c at ~1 hour post-Big Bang). At that point: update T_C_KELVIN formula in closure_protocol.py to use τ_micro explicitly with ℏ, update the corresponding test to pin the SI-correct value, and revise V7 §0.5, V7 §22, thermal_transition.py docstrings, and the GRUT_TOE.md chapters that reference T_c (Ch 1 predictions table, Ch 2, Ch 4, Ch 9, Ch 13.3-13.4, Appendix C) in a coordinated correction.

**Closure effort.** Multi-session research. The closure work has three tractable paths: (a) derive τ_micro from CTP plasma dynamics (potentially connecting to n_g_omega_cosmological_covariance_open_question #9 — both involve cosmological-plasma physics the framework has at scoping level but not formalized), (b) identify τ_micro with a known atomic/nuclear timescale and motivate the identification from first principles, or (c) acknowledge two independent inputs (one cosmological τ_0, one plasma τ_micro) without a derived relationship between them. Path (a) is most ambitious and most informative; path (c) is most conservative and could close the open negative quickly with a registry-tier framing change.

**Affects (claims hardened on closure).**
- `t_c_thermal_transition` (Ch 8, fan-out 1)

**References.**
- grut/foundation/closure_protocol.py:T_C_KELVIN
- grut/derived/cosmology/thermal_transition.py
- theory/foundations_audit/T_C_PROVENANCE.md
- theory/derivation/CRYSTALLIZATION_SCHEDULE_INVESTIGATION.md
- theory/GRUT_V7_FULL.md (V7 §0.5, V7 §22)

**Last reviewed.** 2026-04-28

---

### track_v_coupling_unification_open_question

**Chapter.** 12

**Statement.** GRUT's Track V proposes that the Standard Model gauge couplings unify at high scale via a constitutive β-function correction from the responsive vacuum. With the canonical framework, the three SM couplings α_s, α_W, α_Y miss exact unification by 8.9% at the GUT scale (~10¹⁶ GeV). The framework asserts a constitutive correction Δβ(α_eff(ω)) to the running closes this gap, but the correction has not been derived rigorously from the CTP action. Track V remains an open negative pending: (1) explicit derivation of the constitutive β-function correction from δS_CTP/δg_i, (2) numerical evaluation showing 8.9% closure at the predicted scale, (3) consistency with other electroweak-scale tests.

**Closure condition.** Derive the constitutive β-function correction Δβ(α_eff(ω)) from the CTP action's gauge-coupling renormalization in the responsive-vacuum framework, and verify numerically that this correction closes the 8.9% unification miss at the predicted GUT scale. Falsifier path: high-precision future-collider measurement showing the SM couplings do NOT unify at any scale would falsify the framework's gauge-structural prediction independent of the β correction.

**Closure effort.** Specialist QFT-renormalization-group work, ~6-12 months. Requires fluency in two-loop SM β-functions plus the constitutive-projection machinery in the gauge sector.

**Affects (claims hardened on closure).**
- `sm_emergence` (Ch 5, fan-out 7)

**References.**
- V7 Track V documentation
- Machacek-Vaughn 1983 (β-function references)
- PDG SM coupling constants at M_Z

**Last reviewed.** 2026-04-27

---

### two_route_convergence_physical_equivalence_open_question

**Chapter.** 12

**Statement.** The two computed routes for R (Path G: pure α=1/3 algebra giving 1.15470; Osborn ε at M_Z: weighted gauge-coupling correction giving 1.15367) agree at 0.089%. The framework asserts this is structural confirmation. But the physical statement that makes them equivalent — e.g. 'the conformal mode's a/c at IR equals the gauge-coupling-corrected trace anomaly at electroweak matching scale' — has not been articulated. Without that statement, the convergence is striking empirical agreement, not structural identity. The framework is responsible for either (a) producing the equivalence statement, or (b) acknowledging the agreement is empirical and tiering accordingly.

**Closure condition.** Articulate the physical statement that makes Path G (α=1/3 from conformal-mode scalar) and Osborn ε at M_Z (QCD-dominant gauge-coupling correction) compute the same physical quantity. Likely path: derivation showing that under the conformal-mode-as-IR-carrier postulate, the Osborn ε-combined at the EW matching scale reduces to a/c = 1/3 at leading order (the Gibbons-Hawking thermal-asymmetry argument in ZENODO_EPSILON_IDENTIFICATION.md gestures at this but does not complete it). Alternative: explicitly state the agreement is empirical, not structural.

**Closure effort.** Theoretical work, ~2-4 weeks. Requires fluency in trace-anomaly literature and the local-coupling formalism. The ZENODO doc has the partial argument; completing it is the task.

**Affects (claims hardened on closure).**
- `three_routes_convergence` (Ch 7, fan-out 1)

**References.**
- Komargodski-Schwimmer 2011 (a-theorem; trace anomaly)
- Osborn (2003) hep-th/0302119 (eq 36, ε coefficient)
- Christensen-Duff 1980 (Nucl Phys B 170 480)
- grut/foundation/conformal_mode_scalar.py
- grut/foundation/osborn_epsilon.py
- theory/ZENODO_EPSILON_IDENTIFICATION.md

**Last reviewed.** 2026-04-26

---

### vorton_track_vii_open_negative

**Chapter.** 12

**Statement.** Track VII Step 3 (vortex-string topology): π_n(U(1)) correctly identifies cosmic strings (not monopoles); BPS tension μ = πv² = 0.56 GeV² with Gμ orders below the CMB bound; pure-string scaling gives negligible Ω ~ 10⁻⁴². Vorton abundance with XY universality UNDER-produces by factor ~30, and M_vorton mismatches V7's M_soliton by factor ~450 — a real discrepancy. Step 3 REOPENS Track VII.

**Closure condition.** Either (a) the vorton mass M_vorton/M_soliton factor-450 discrepancy is closed by additional structure in the topological-defect calculation, OR (b) the dielectric DM interpretation supersedes the particulate route entirely and Track VII Step 3 is retired.

**Closure effort.** Research-tier. The dielectric route (dielectric_dm_reframing) is the framework's preferred path; vorton physics may not need to close — the open negative is preserved as honest documentation of a route that was attempted.

**Affects (claims hardened on closure).**
- `dark_sector_u1_extension` (Ch 9, fan-out 3)

**References.**
- grut/derived/dark_matter/vortex_strings.py

**Tests pinning the gap.**
- `tests/derived/test_vortex_strings.py`

**Last reviewed.** 2026-04-26

---


