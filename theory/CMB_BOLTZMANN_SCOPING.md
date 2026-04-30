# CMB Boltzmann Scoping — Constitutive Modifications to CLASS / CAMB

*Phase-2 scoping document. Implementation deferred to a separate session.*

**Status:** Anchored — quantitative scoping complete; implementation
of modified Boltzmann code is multi-session work.

**Codebase anchor:** `grut/derived/cmb/scoping.py`,
`tests/derived/test_cmb_scoping.py`.

---

## Executive summary

The framework predicts a constitutive correction to the gravitational
potential evolution at all redshifts via the frequency-dependent
refractive index n_g(ω) = √(1 + α/(1+(ωτ_0)²)). At CMB-relevant
frequencies, this correction's magnitude depends on whether the
recombination-era acoustic dynamics sit in the **crystal** (ωτ_0 ≫ 1)
or **fluid** (ωτ_0 ≪ 1) regime.

**Result.** Both relevant frequencies at recombination — the expansion
rate H(z=1100) and the first-acoustic-peak mode ω_acoustic — give
ωτ_0 ≈ 68 and 140 respectively. The vacuum is in **deep crystal** at
recombination. The predicted shift Δθ_*/θ_* is **3.6 × 10⁻⁵**.

**Comparison to precision.** Planck 2018 measures θ_* to 3 × 10⁻⁴; the
GRUT shift sits a factor 10 below. CMB-S4 / LiteBIRD target 5 × 10⁻⁵;
the GRUT shift sits a factor 1.4 below that target.

**Verdict.** At Planck precision, CMB is a **consistency check**, not a
falsifier — the framework predicts no observable deviation from ΛCDM at
acoustic-peak structure. At CMB-S4 precision, **the leading-order
scoping prediction sits at the detection threshold** but is **not yet
a falsifier-tier claim** — promotion requires closing two upstream
gaps:

1. **n_g(ω) covariance** (`n_g_omega_cosmological_covariance_open_question`)
   — articulate which ω the modification uses in the cosmological
   perturbation sector and how it transforms under gauge changes;
   map to the μ(k,a) / γ(k,a) parameterization of modified-gravity
   EFT.
2. **Full Boltzmann propagation** — implement the constitutive
   modification in CLASS or CAMB and propagate through the full
   hierarchy: CMB anisotropy C_ℓ^TT/TE/EE, lensing C_ℓ^φφ, growth
   rate fσ_8, matter power spectrum P(k). The current scoping
   computes Δθ_* only.

Once both are closed, the prediction graduates to a falsifier-tier
claim. Until then, this is **scoping-tier** — useful as a forward
target, not as a near-term decisive test.

This is structurally clean: the framework's distinctive prediction
lives at frequencies where ωτ_0 is order-unity (galactic and
intermediate cosmological scales), and it correctly predicts no
distinctive CMB signature at Planck precision. The CMB sector is doing
the work of confirming that the high-frequency limit of GRUT reduces
to ΛCDM — exactly as the framework claims.

---

## Q1. What is ωτ₀ at recombination?

The relevant frequencies are:

1. **Expansion rate** — H(z=1100) drives the Friedmann equation and
   sets the rate of change of the gravitational potential during
   matter domination.

2. **First acoustic peak** — ω_acoustic = c_s × k_first-peak sets the
   characteristic frequency of acoustic oscillations of the
   photon-baryon plasma.

### Numerical values

Using Planck 2018 baseline cosmology (H_0 = 67.66 km/s/Mpc,
Ω_m = 0.3158, Ω_Λ = 0.6842, Ω_r = 9.18 × 10⁻⁵):

| Quantity | Value |
|:---|:---|
| H_0 | 2.19 × 10⁻¹⁸ Hz |
| H_rec at z = 1100 | 5.17 × 10⁻¹⁴ Hz |
| H_rec × τ_0 | **68.4** |
| ω_acoustic (k r_s = π) | 1.06 × 10⁻¹³ Hz |
| ω_acoustic × τ_0 | **140.5** |

Both well above 1. The constitutive coupling α_eff(X) = α/(1+X²) is
suppressed by 1/X² at recombination:

| Frequency | α_eff | Δn_g/n_g |
|:---|:---|:---|
| H_rec | 7.13 × 10⁻⁵ | **3.56 × 10⁻⁵** |
| ω_acoustic | 1.82 × 10⁻⁵ | **8.45 × 10⁻⁶** |

### Crystal regime, confirmed

The constitutive correction at recombination frequencies is
parts-in-10⁵, not parts-in-10. The vacuum is fully crystallized at the
acoustic-mode frequencies that source the CMB peaks. This is the
**high-frequency limit** of the framework, where GRUT reduces to GR by
construction.

The prediction Δn_g/n_g ~ 10⁻⁵ is **the framework's specific
quantitative claim** for the CMB. It is small but **not zero**. The
question for Question 4 is whether 10⁻⁵-level precision is reachable
observationally.

---

## Q2. What does n_g(ω) do to the sound horizon?

The Friedmann equation in GRUT is modified at frequency ω:

$$H^2 = \frac{8\pi G}{3} \rho \cdot n_g^2(H \tau_0)$$

self-consistent because the relevant ω is H itself. For ωτ_0 ≫ 1:

$$n_g^2 \approx 1 + \frac{\alpha}{(\omega\tau_0)^2}$$

so the fractional correction to H at recombination is

$$\frac{\Delta H}{H} \approx \frac{\alpha}{2(H_{\rm rec} \tau_0)^2}
\approx \frac{1/3}{2 \times 68.4^2} \approx 3.56 \times 10^{-5}.$$

### Sound horizon shift

The sound horizon r_s integrates the sound speed over the
pre-recombination expansion history:

$$r_s = \int_0^{t_{\rm rec}} \frac{c_s(t')}{a(t')} dt' = \int_0^{a_{\rm rec}}
\frac{c_s(a)}{a^2 H(a)} da$$

A fractional shift in H produces an opposite-sign fractional shift in
r_s (faster expansion ⟹ less sound-horizon accumulation). Leading
order:

$$\frac{\Delta r_s}{r_s} \approx -\frac{\Delta H}{H} \bigg|_{\rm rec}
\approx -3.56 \times 10^{-5}$$

### Acoustic peak position θ_*

The acoustic angular scale θ_* = r_s / d_A inherits both r_s and d_A
shifts. In GRUT:

- **r_s** integrates pre-recombination dynamics where ωτ_0 ≫ 1 →
  shift ≈ 3.6 × 10⁻⁵.
- **d_A** integrates post-recombination dynamics. At low z (today),
  ωτ_0 ≪ 1, so the constitutive correction is large IN PRINCIPLE —
  but GRUT's predicted Ω_Λ = 0.6886 matches Planck's 0.6889 to 0.04%
  by construction. The framework's specific cosmological-parameter
  predictions place d_A within Planck's measurement bands; the
  effective shift to d_A from constitutive corrections is absorbed
  into the matched Ω_Λ value.

**Net effect on θ_*:** Δθ_*/θ_* ≈ **3.56 × 10⁻⁵**, dominated by the
r_s shift.

This is the framework's specific quantitative prediction for the CMB
acoustic peak shift relative to ΛCDM at the same fitted cosmological
parameters.

---

## Q3. What would a CLASS / CAMB modification look like?

A complete implementation requires modifying a Boltzmann code's
gravitational-potential evolution to apply the n_g²(ω) factor. Both
CLASS and CAMB are open-source and well-documented; the modification
points are specific and bounded.

### CLASS entry points

| Module | Function | Modification |
|:---|:---|:---|
| `background_module` | `background.c` (Friedmann) | H²(a) → H² × n_g²(H τ_0). Self-consistent: ω = H. Resolved by direct substitution since correction is small. |
| `perturbations_module` | `perturbations.c::perturb_einstein()` | k² Φ = −4πG a² δρ → k² Φ = −4πG a² δρ × n_g²(ω). The most consequential entry. ω = ∂_t Φ / Φ at the perturbation's natural frequency. |
| `thermodynamics_module` | `thermodynamics.c` | No patch needed — recombination depends on photon thermodynamics (Saha equation), not gravity. |

### CAMB entry points

| File | Modification |
|:---|:---|
| `equations.f90::derivs()` | Boltzmann + Einstein system; add n_g²(ω) factor to gravitational potential equation. |
| `GaugeInterface.f90` | Ensure n_g²(ω) factor is gauge-invariant; cleanest in synchronous or Newtonian gauge. |

### Implementation effort

**4–8 weeks specialist work** (Phase-2+). Tasks:

1. Add τ_0 and α_vac as new cosmological parameters
2. Modify the gravitational Poisson equation in the perturbations
   module to apply n_g²(ω)
3. Calibrate against unmodified CLASS/CAMB output for ωτ_0 ≫ 1 —
   must reproduce ΛCDM at the relevant precision when the correction
   is suppressed
4. Re-derive the C_l power spectra
5. MCMC fit against the Planck 2018 likelihood

**Prerequisites:** CLASS or CAMB experience, access to Planck
likelihood code, MCMC infrastructure (Cobaya, MontePython, or
equivalent).

### Implementation choice: CLASS vs CAMB

**Recommended: CLASS.** The C codebase is simpler to modify than CAMB's
Fortran, the documentation is more accessible, and CLASS has cleaner
separation between background, thermodynamics, and perturbations
modules. The trade-off is that CAMB has a larger user base in the
cosmology community, so a CAMB patch would have wider adoption.

**Recommended: CLASS first, then port to CAMB if results warrant.**

---

## Q4. What does success and failure look like?

### Predicted CMB modification

| Quantity | GRUT prediction | Note |
|:---|:---|:---|
| Δθ_*/θ_* | 3.6 × 10⁻⁵ | Acoustic peak position shift |
| Δn_g/n_g at recombination | 3.6 × 10⁻⁵ | Refractive enhancement |
| C_ℓ residuals (peak heights) | ~10⁻⁴ to 10⁻⁵ | Order-of-magnitude estimate; full Boltzmann run needed for precision |

### Observational precision benchmarks

| Experiment | θ_* precision | GRUT detectable? |
|:---|:---|:---|
| Planck 2018 | 3 × 10⁻⁴ | **No** — factor 10 below precision |
| CMB-S4 (~2030) | 5 × 10⁻⁵ | **At threshold** — factor 1.4 below target |
| Simons Observatory | ~10⁻⁴ | No |
| LiteBIRD (polarization) | 10⁻⁵ in r | Different observable; complementary |

### Success scenarios

1. **Planck consistency check (now).** GRUT's predicted shift is below
   Planck's measurement precision. The framework's CMB prediction
   is **consistent with Planck data** for the same fitted cosmological
   parameters. This validates the high-frequency limit (GRUT → GR)
   of the framework.

2. **CMB-S4 detection (~2030).** If CMB-S4 measures θ_* with
   sufficient precision and detects a shift consistent with
   Δθ_*/θ_* ~ 3.6 × 10⁻⁵, the framework's CMB-scale prediction is
   **confirmed**. Combined with the decoherence plateau (laboratory
   primary falsifier) and the cluster-merger scaling (Track VII
   primary falsifier), three independent precision tests would all
   confirm the framework.

### Failure scenarios

1. **CMB-S4 detects deviation incompatible with GRUT.** If the
   detected shift is materially different from 3.6 × 10⁻⁵ (wrong
   sign, wrong magnitude > factor 3), the framework's CMB-scale
   prediction is **falsified**. Either τ_0 is different, or the kernel
   has higher-order structure not captured by the simple Lorentzian.

2. **CMB-S4 sets a stronger limit than 5 × 10⁻⁵.** If future precision
   is high enough to constrain the prediction below the GRUT value
   without detection, the framework's CMB-scale prediction is
   **falsified** in the simple-kernel form. This would force
   τ_0 > current value or a non-pure-exponential kernel.

3. **Planck reanalysis tightens precision below 3.6 × 10⁻⁵.** Unlikely
   without new instruments, but possible via combined-likelihood
   analyses with low-redshift data. Would move the falsification
   window forward in time.

### Honest framing

The CMB sector is *not* GRUT's primary falsifier — the decoherence
plateau is. The CMB is a **consistency check at Planck precision** and
becomes a **leading-order scoping prediction at CMB-S4 threshold**,
**conditional on two upstream closures** (covariance question + full
Boltzmann implementation) before it can be promoted to falsifier-tier.

What's forced and what isn't:

- **Forced**: the ωτ_0 ≫ 1 classification at recombination
  (parameters are inputs, not fits).
- **Forced**: the order-of-magnitude estimate Δθ_*/θ_* ~ 10⁻⁵ at
  leading order — this follows from α_eff = α/(1+(ωτ_0)²) regardless
  of how the gauge / covariance details are pinned down.
- **Not yet pinned**: which ω enters the cosmological-perturbation
  Poisson equation, and how the modification propagates through
  P(k), lensing, fσ_8 self-consistently. The scoping is one
  observable; the implementation phase computes the rest and
  checks for blow-ups.

If, after both upstream closures, CMB-S4 shows no deviation at the
predicted level, the framework's CMB sector is honestly constrained.
If it detects the predicted deviation, three independent precision
tests have independently confirmed τ_0 = 41.9 Myr. Until those
upstream closures land, this is a scoping target, not a decisive
test.

---

## Implementation roadmap

### Phase 0 — Preparation (this document)

**Status: Complete.**

- Quantitative scoping numbers computed via
  `grut/derived/cmb/scoping.py`
- Four scoping questions answered
- CLASS/CAMB entry points identified
- Effort estimate: 4–8 weeks specialist work

### Phase 1 — CLASS modification

- Fork CLASS, add τ_0 and α_vac as cosmological parameters
- Implement n_g²(ω) factor in `perturb_einstein`
- Calibrate against unmodified CLASS for ωτ_0 ≫ 1 (must reproduce
  ΛCDM C_ℓ to numerical precision)
- Add unit tests

**Estimated effort:** 2–3 weeks (CLASS-experienced developer).

### Phase 2 — Power spectrum and MCMC

- Compute modified C_ℓ TT, TE, EE for fiducial GRUT cosmology
- Fit against Planck 2018 likelihood
- Compare χ² of GRUT vs ΛCDM at fixed cosmological parameters
- Extract residuals and predict CMB-S4 detectability

**Estimated effort:** 2–3 weeks (cosmology-likelihood experience).

### Phase 3 — CAMB port (if results warrant)

- Port the CLASS modification to CAMB
- Cross-validate the two implementations agree at numerical precision
- Distribute as patches to the cosmology community

**Estimated effort:** 1–2 weeks (Fortran experience).

---

## What this document does NOT claim

- That a modified CLASS/CAMB has been implemented and run
- That the predicted Δθ_*/θ_* = 3.6 × 10⁻⁵ has been validated against
  Planck data via full likelihood analysis
- That CMB-S4 will detect the prediction (the CMB-S4 collaboration
  determines this)
- That the constitutive correction's structure is exactly the simple
  Lorentzian n_g²(ω) at all frequencies (higher-order kernel
  corrections may modify the prediction)

These are **deferred to the implementation phases**. The current
document establishes the scoping numbers and identifies the entry
points; nothing more is claimed.

---

## References

- **Planck 2018 baseline:** Aghanim et al. (Planck Collaboration),
  *Planck 2018 results. VI. Cosmological parameters*, A&A 641 (2020) A6
- **CLASS:** Lesgourgues, *The Cosmic Linear Anisotropy Solving System*,
  arXiv:1104.2932 (2011)
- **CAMB:** Lewis, Challinor, Lasenby, *Efficient Computation of CMB
  Anisotropies in Closed FRW Models*, ApJ 538 (2000) 473
- **CMB-S4 forecasts:** Abazajian et al., *CMB-S4 Science Case, Reference
  Design, and Project Plan*, arXiv:1907.04473 (2019)
- **GRUT cosmological prediction (H_0, Ω_Λ):** GRUT V7 §27,
  `tests/derived/test_cosmology.py`
- **GRUT scoping calculation:** `grut/derived/cmb/scoping.py`,
  `tests/derived/test_cmb_scoping.py`

---

*Scoping completed by Claude Code on 2026-04-26. Implementation
deferred to a future session per the user's directive.*
