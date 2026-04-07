# Program F — Stage F2-B: Φ Identification Hypothesis Ranking and Elimination

**Predecessor:** F2-A (class-level USL protocol complete). F0/F1 (USL robust, non-discriminating).

**The problem:** Φ is a mathematical object in the CTP action with no assigned physical identity. All member-level discrimination requires knowing what Φ IS. This stage ranks candidate identifications.

---

## 1. Hard-Constraint Filter

Every candidate must satisfy ALL of the following non-negotiable constraints inherited from Programs I-III and E. Any candidate failing any constraint is EXCLUDED.

| # | Constraint | Source | Test |
|---|-----------|--------|------|
| **HC1** | Φ must be a SCALAR under coordinate transformations. | CTP backbone (A1-L2, TF3) | Does the candidate transform as a scalar? |
| **HC2** | Φ must have FIRST-ORDER relaxational dynamics in the overdamped regime (no propagating wave modes at low frequency). | A1-L8, E-F2, TF3 | Does the candidate have wave-like propagation? If yes: EXCLUDED (unless demonstrably overdamped at relevant scales). |
| **HC3** | Φ must have a UNIQUE ATTRACTOR Φ* = X(g) in the linear regime (possibly multiple in nonlinear extension). | A1-C4, E-F2 | Does the candidate admit a curvature-determined equilibrium? |
| **HC4** | Φ must couple to the Ricci scalar R (or a scalar functional of the metric) through the source X(g). | AB1 (TF1), B0 | Is the candidate sourced by spacetime curvature? |
| **HC5** | Φ must be in SECTOR 1-2 (constitutive + noise), NOT Sector 3 (gravitational dephasing). The USL is independent of Φ (Sector 3 protection). | Alpha-Prime, F1 | Does the candidate's dynamics decouple from the gravitational self-energy at tree level? |
| **HC6** | Φ must be consistent with weak-field precision tests (PPN parameters, fifth-force bounds, equivalence principle tests). | Book A domain map (X5: no strong-field claim without checking) | Does the candidate violate known experimental constraints? |
| **HC7** | Φ must be sourced by an ENVIRONMENTAL bath (not gravitational vacuum fluctuations in flat space). | A3 (three arguments: D→0, super-Ohmic, 2nd law) | Is the candidate's dissipation compatible with an environmental bath? |

---

## 2. Candidate Scorecard

### H1: Coarse-grained geometric relaxation mode

**Description:** Φ is a coarse-grained average of metric fluctuations — an effective scalar extracted from the metric by averaging over short-wavelength modes. It represents "how relaxed" the local geometry is relative to its equilibrium (Einstein) configuration.

| Criterion | Score | Reasoning |
|-----------|:-----:|-----------|
| **Structural compatibility** | **4/5** | Scalar: YES (trace of metric perturbation is a scalar). First-order relaxation: PLAUSIBLE (coarse-grained modes relax dissipatively via coupling to short-wavelength modes, which act as a bath). Unique attractor: YES (Einstein solution is the equilibrium). Curvature-sourced: YES (X = f(R) naturally). Sector 3 protection: YES (Φ is an effective mode of g, but the USL depends on the FULL g, not the coarse-grained mode). |
| **Empirical viability** | **3/5** | Not directly observed. Consistent with existing tests IF the coupling α is small enough. PPN: the scalar mode would contribute to the PPN parameter γ. If α is below current bounds (~10⁻⁵ in Brans-Dicke ω), consistent. Fifth force: suppressed at short range if Φ has a mass (from the 1/τ term in the EOM acting as an effective mass in the propagator — but Φ is overdamped, not propagating, so "mass" is not the right concept). |
| **Direct-observable pathway** | **2/5** | No direct measurement of a coarse-grained geometric relaxation mode has been proposed. Indirect: gravitational wave ringdown could show relaxation effects (but GRUT-II Upsilon showed QNM shift is 0.002% — negligible). Cosmological: Φ could contribute to dark energy if β/τ ~ Λ_obs^{1/2}. |
| **Major failure modes** | Coarse-graining ambiguity: the split between "short-wavelength bath" and "long-wavelength Φ" is scale-dependent and non-unique. Different coarse-graining scales give different Φ fields. This is a conceptual weakness, not a falsification. |
| **Required imports** | A coarse-graining prescription for the metric. A separation of scales (Φ wavelength >> bath wavelength). Both are ASSUMED, not derived. |

**HC filter:**

| HC | Pass? | Notes |
|:--:|:-----:|-------|
| HC1 | ✓ | Trace of metric perturbation is a scalar |
| HC2 | ✓ | Overdamped (short-wavelength modes provide dissipation) |
| HC3 | ✓ | Einstein solution is the equilibrium target |
| HC4 | ✓ | X = f(R) naturally (Ricci scalar of the background) |
| HC5 | ✓ | Φ is an effective mode; USL uses the full metric |
| HC6 | ? | Depends on α. Must satisfy α < PPN bounds. CONDITIONAL. |
| HC7 | ✓ | Bath = short-wavelength metric fluctuations (environmental relative to the long-wavelength Φ) |

**HC6 is CONDITIONAL.** H1 passes the filter if α is below PPN bounds.

### H2: Stochastic-gravity / noise-kernel scalar

**Description:** Φ is the semiclassical stochastic correction to the metric — the "noise" generated by quantum stress-energy fluctuations (Hu-Verdaguer stochastic gravity program). It represents the scalar sector of the stochastic gravitational noise kernel.

| Criterion | Score | Reasoning |
|-----------|:-----:|-----------|
| **Structural compatibility** | **3/5** | Scalar: PARTIALLY (the noise kernel is a tensor; its trace is a scalar, but the full noise is tensorial). First-order relaxation: PROBLEMATIC (the stochastic gravity noise is not a relaxational field — it is a fluctuation field with no preferred equilibrium). Unique attractor: PROBLEMATIC (noise has no attractor; it fluctuates around zero). Curvature-sourced: YES (the noise kernel depends on curvature through the stress-energy correlator). |
| **Empirical viability** | **2/5** | Stochastic gravity noise has not been directly detected. Its effects are extremely small (suppressed by l_P² / L² where L is the observation scale). Consistent with all current data (too small to see). |
| **Direct-observable pathway** | **1/5** | No proposed measurement. The noise is far below any current detector sensitivity. Even LIGO's quantum noise is photon shot noise, not gravitational stochastic noise. |
| **Major failure modes** | HC2 and HC3 likely fail: noise is NOT relaxational and has NO attractor. The stochastic gravity kernel is a FLUCTUATION, not a dissipation. It has zero mean, not a curvature-determined equilibrium. |
| **Required imports** | The Hu-Verdaguer stochastic gravity formalism. CTP effective action for quantum stress-energy. Both are well-developed but the resulting noise is tensorial and non-relaxational. |

**HC filter:**

| HC | Pass? | Notes |
|:--:|:-----:|-------|
| HC1 | PARTIAL | Trace of the noise kernel is scalar. Full noise is tensor. |
| HC2 | **FAIL** | Noise fluctuates; it does not relax. No first-order dissipative dynamics. |
| HC3 | **FAIL** | No unique attractor. Mean of noise is zero, not X(g). |
| HC4 | ✓ | Noise kernel depends on curvature |
| HC5 | ✓ | Noise is separate from the Newtonian self-energy |
| HC6 | ✓ | Consistent with all current bounds (too small to detect) |
| HC7 | ✓ | Noise IS the quantum stress-energy bath |

**EXCLUDED by HC2 and HC3.** The stochastic gravity noise kernel is a FLUCTUATION field, not a dissipative relaxation field. It does not relax toward a curvature-determined equilibrium. It violates two hard constraints.

### H3: New fundamental scalar field

**Description:** Φ is a NEW fundamental scalar field not yet observed — analogous to the dilaton, quintessence, or a Brans-Dicke scalar, but with explicitly dissipative (first-order) dynamics rather than the usual wave equation (second-order).

| Criterion | Score | Reasoning |
|-----------|:-----:|-----------|
| **Structural compatibility** | **5/5** | Scalar: YES (by definition). First-order relaxation: BY CONSTRUCTION (the GRUT equation IS the definition of Φ). Unique attractor: BY CONSTRUCTION. Curvature-sourced: BY CONSTRUCTION (X = β + αR). Sector 3 protection: YES. |
| **Empirical viability** | **2/5** | No scalar field with first-order dissipative dynamics has been observed. All known fundamental scalars (Higgs) have second-order (wave) dynamics. A fundamental first-order scalar field has no precedent in the Standard Model or known BSM physics. Fifth-force bounds: must satisfy α < ~10⁻⁵ (Brans-Dicke type). Equivalence principle: must couple universally or not at all to matter. |
| **Direct-observable pathway** | **2/5** | If Φ couples to matter: fifth-force experiments, PPN measurements, or cosmological scalar-field searches (dark energy surveys). If Φ does NOT couple to matter directly (only through curvature): extremely difficult to detect. |
| **Major failure modes** | (a) No precedent for fundamental first-order scalars — this would be a new class of field. (b) The first-order dynamics requires a bath (A3: environmental, not gravitational). What is the bath for a FUNDAMENTAL field? This is a circularity: a fundamental field dissipates into ... what? If the bath is matter/radiation: Φ is not fundamental (it's an effective mode of the matter/radiation system). If the bath is something else: what? |
| **Required imports** | A new field content in the Standard Model (or beyond). A bath for the fundamental field. Both are major assumptions. |

**HC filter:**

| HC | Pass? | Notes |
|:--:|:-----:|-------|
| HC1 | ✓ | Scalar by definition |
| HC2 | ✓ | First-order by definition |
| HC3 | ✓ | By construction |
| HC4 | ✓ | By construction |
| HC5 | ✓ | By construction |
| HC6 | ? | Depends on coupling to matter. CONDITIONAL on α < bounds. |
| HC7 | **PROBLEMATIC** | What is the bath for a fundamental field? The environmental-bath requirement (A3) is hard to satisfy for a field that is itself supposed to be fundamental. |

**HC7 is PROBLEMATIC.** A fundamental field that dissipates requires an even-more-fundamental bath. This creates a regress problem. H3 passes the filter CONDITIONALLY — if the bath can be identified without regress.

### H4: Thermodynamic entropy-density scalar

**Description:** Φ is a local entropy density (or a monotonic function thereof). It represents the local thermodynamic state of matter, coarse-grained to a scalar. Its relaxation toward X(g) represents the second law: entropy approaches its equilibrium value determined by the local geometry.

| Criterion | Score | Reasoning |
|-----------|:-----:|-----------|
| **Structural compatibility** | **4/5** | Scalar: YES (entropy density is a scalar). First-order relaxation: YES (entropy approaches equilibrium via dissipation — this IS the second law). Unique attractor: YES (maximum-entropy state for given constraints). Curvature-sourced: PARTIAL (the maximum entropy depends on the available phase space, which depends on the gravitational potential → X(g)). Sector 3 protection: YES (entropy density is a thermodynamic quantity, not a gravitational self-energy). |
| **Empirical viability** | **3/5** | Entropy density is well-defined in thermodynamics. Its coupling to curvature is less clear — how does local geometry determine the maximum entropy? In the Tolman-Ehrenfest effect (thermal equilibrium in a gravitational field), the local temperature IS geometry-dependent: T(x) = T₀ / √(g₀₀(x)). This DOES couple thermodynamic state to curvature. |
| **Direct-observable pathway** | **3/5** | Temperature and entropy are measurable in many contexts. The Tolman-Ehrenfest effect is a measurable curvature-entropy coupling. In cosmology, the entropy per baryon is a measurable quantity that evolves. The constitutive relaxation time τ could be identified with the thermalization timescale of local matter — which IS measurable in astrophysical systems (e.g., cooling of neutron stars, equilibration of stellar interiors). |
| **Major failure modes** | (a) Entropy density is already well-understood in standard thermodynamics. Calling it Φ does not add new physics — it repackages known physics in GRUT notation. (b) The specific first-order equation τ dΦ/dt + Φ = X(g) must match the actual entropy evolution, which is more complex (entropy transport, production, non-equilibrium effects). The GRUT equation is a SIMPLIFICATION of the full entropy dynamics, not an exact representation. |
| **Required imports** | Identification of Φ with entropy density (or a function thereof). Identification of X(g) with the equilibrium entropy determined by local geometry. Identification of τ with the local thermalization timescale. All are PHYSICALLY MOTIVATED but not derived. |

**HC filter:**

| HC | Pass? | Notes |
|:--:|:-----:|-------|
| HC1 | ✓ | Entropy density is a scalar |
| HC2 | ✓ | Entropy relaxes (second law) — first-order approach to equilibrium |
| HC3 | ✓ | Maximum-entropy state is the unique attractor |
| HC4 | ✓ | Tolman-Ehrenfest: equilibrium temperature/entropy depends on curvature |
| HC5 | ✓ | Entropy is not the gravitational self-energy |
| HC6 | ✓ | Entropy evolution is fully consistent with existing physics |
| HC7 | ✓ | The bath IS the local matter/radiation environment |

**ALL HARD CONSTRAINTS PASS.** H4 is the only candidate that passes all seven constraints without conditionality.

---

## 3. Elimination Table

| Candidate | Classification | Confidence | Reason |
|:---------:|:--------------:|:----------:|--------|
| **H1** (geometric relaxation mode) | **viable_conditional** | 0.55 | Passes HC1-HC5, HC7. HC6 conditional on α < PPN bounds. Coarse-graining ambiguity is a conceptual weakness. |
| **H2** (stochastic gravity noise) | **excluded** | 0.85 | FAILS HC2 (not relaxational) and HC3 (no attractor). Noise fluctuates, it does not relax. |
| **H3** (new fundamental scalar) | **viable_conditional** | 0.40 | Passes HC1-HC6 by construction. HC7 problematic: bath regress for a fundamental field. |
| **H4** (entropy-density scalar) | **viable_now** | 0.65 | Passes ALL seven hard constraints. Physically motivated. Observable pathway exists (Tolman-Ehrenfest, thermalization timescale). Main risk: repackaging known physics, not new prediction. |

---

## 4. Discriminator Observable Map

### H1 (geometric relaxation mode) — if viable

| Observable type | Signature | Direction | Feasibility |
|----------------|-----------|:---------:|:-----------:|
| Lab: fifth force | Short-range force from Φ exchange | Deviation from 1/r² at submillimeter scales | MEDIUM (current bounds: α < 10⁻⁵ at ~mm) |
| Cosmological: dark energy | Φ energy density ρ_Φ = β²/(2τ²) contributes to Λ_eff | If β/τ ~ Λ_obs^{1/2}: Φ drives cosmic acceleration | LOW (requires β/τ tuning) |
| Strong gravity: GW ringdown | Φ relaxation during BH ringdown adds a damped scalar mode | Additional damped mode at frequency ~1/τ | LOW (GRUT-II Upsilon: 0.002% QNM shift) |
| Null test: PPN γ | Scalar-tensor PPN: γ = (1+ω)/(2+ω) where ω ~ 1/α² | γ deviates from 1 if α ≠ 0 | HIGH (Cassini: |γ−1| < 2.3×10⁻⁵) |

### H3 (new fundamental scalar) — if viable

| Observable type | Signature | Direction | Feasibility |
|----------------|-----------|:---------:|:-----------:|
| Lab: fifth force | Same as H1 | Same | MEDIUM |
| Collider: production | Φ production via curvature coupling at LHC energies | Production rate ~ α² × (E/M_P)² — negligibly small | IMPOSSIBLE at current energies |
| Cosmological: early universe | Φ as inflaton or dark energy | Model-dependent | LOW (requires full cosmological model) |
| Null test: equivalence principle | If Φ couples differently to different matter species | Composition-dependent acceleration | HIGH (MICROSCOPE: Eötvös parameter < 10⁻¹⁵) |

### H4 (entropy-density scalar) — if viable

| Observable type | Signature | Direction | Feasibility |
|----------------|-----------|:---------:|:-----------:|
| Lab: thermalization dynamics | τ identified as local thermalization timescale → measure τ by observing approach to thermal equilibrium | τ measurable for specific systems (gas, plasma, condensed matter) | HIGH (standard calorimetry / relaxation measurement) |
| Astrophysical: neutron star cooling | τ_NS identified as NS cooling timescale → X(g) as equilibrium temperature profile → constitutive law governs cooling curve | Cooling curve shape reveals τ(g_NS) | MEDIUM (requires NS temperature data + GRUT model fitting) |
| Cosmological: entropy per baryon | Φ → entropy per baryon s. X(g) → equilibrium s in the expanding universe. | s evolves according to constitutive law on Hubble timescale | LOW (requires cosmological GRUT model) |
| Null test: Tolman-Ehrenfest | Local temperature in gravitational field: T(x) = T₀/√(g₀₀). If Φ = s(T), then Φ(x) depends on g₀₀. | Temperature gradient in gravitational field matches curvature coupling | MEDIUM (precision thermometry in varying g-field) |

---

## 5. Experimental Priority Recommendation

| Rank | Test | Candidate targeted | Rationale |
|:----:|------|:------------------:|-----------|
| **P1** | **Precision fifth-force / PPN measurement at submillimeter scales** | H1, H3 | HIGHEST feasibility. Current experiments (MICROSCOPE, Cassini, torsion balance) already bound scalar-tensor couplings. A dedicated search for Φ-mediated force at the α ~ 10⁻⁵-10⁻⁸ level would either detect H1/H3 or push them to unobservably small coupling. This ELIMINATES or CONSTRAINS two candidates. |
| **P2** | **Thermalization timescale measurement in controlled gravitational gradient** | H4 | MEDIUM feasibility. Measure the relaxation timescale of a thermodynamic system (gas, liquid, or solid) in varying gravitational potential (e.g., tower experiment, centrifuge). If the relaxation timescale τ varies with the gravitational potential in a way consistent with τ(g) = f(curvature), H4 is supported. If τ is geometry-independent, H4 is DISFAVORED. |
| **P3** | **Neutron star cooling curve analysis** | H4 | MEDIUM-LOW feasibility (requires NS thermal data). If the NS cooling timescale matches a constitutive law τ dΦ/dt + Φ = X(g_NS) where X depends on the NS interior metric, H4 is supported. Existing cooling data could be re-analyzed in this framework. |

---

## 6. Decision Token

### **phi_identification_narrowed**

**Rationale:**

1. **One candidate excluded (H2).** Stochastic gravity noise fails HC2 (not relaxational) and HC3 (no attractor). Eliminated with confidence 0.85.

2. **One candidate scored highest (H4).** Entropy-density scalar passes all seven hard constraints without conditionality. It has the clearest observable pathway (thermalization timescale, Tolman-Ehrenfest). Its main weakness is the risk of repackaging known thermodynamics rather than adding new physics.

3. **Two candidates conditional (H1, H3).** Geometric relaxation mode and fundamental scalar both pass most constraints but require conditional assumptions (PPN bounds for H1; bath identification for H3).

4. **The hypothesis space is NARROWED from four to three, with a clear ranking:**

```
H4 (entropy-density)  >  H1 (geometric relaxation)  >  H3 (new fundamental)  >>  H2 (excluded)
```

5. **The blocking obstacle is partially resolved.** H4 provides a PHYSICAL IDENTIFICATION (Φ = entropy density, τ = thermalization timescale) that makes the constitutive-sector observables measurable. If H4 is correct, τ is measurable by standard calorimetry, and the member-selection problem becomes an empirical question.

---

## Gate Table

| Gate | Criterion | Status | Evidence |
|:----:|-----------|:------:|---------|
| **F2B-G1** | Hard-constraint filter applied | **PASS** | Seven constraints (HC1-HC7) applied to all four candidates. H2 excluded. H1, H3 conditional. H4 passes all. |
| **F2B-G2** | All candidates scored on same rubric | **PASS** | Three scores per candidate (structural, empirical, observable) on 0-5 scale. Plus failure modes and required imports. |
| **F2B-G3** | At least one elimination or narrowing | **PASS** | H2 excluded (HC2+HC3 fail). Field narrowed from 4 to 3 with clear ranking. |
| **F2B-G4** | Observable discriminator map produced | **PASS** | Three surviving candidates × four observable types (lab, cosmo, strong-grav, null test). Directionality and feasibility tagged. |
| **F2B-G5** | Next-test priorities actionable | **PASS** | P1 (fifth-force: constrains H1/H3), P2 (thermalization: tests H4), P3 (NS cooling: tests H4). Ranked by feasibility and discriminating power. |

---

*Program F Stage F2-B complete. Decision: phi_identification_narrowed. H2 (stochastic noise): EXCLUDED (fails HC2, HC3). H4 (entropy-density): VIABLE NOW (passes all 7 constraints, best observable pathway). H1 (geometric relaxation): CONDITIONAL (HC6 depends on α). H3 (fundamental scalar): CONDITIONAL (HC7 bath regress). Ranking: H4 > H1 > H3 >> H2. Top test: P1 (fifth-force bounds to constrain H1/H3), P2 (thermalization timescale to test H4). Gates: 5/5 pass.*
