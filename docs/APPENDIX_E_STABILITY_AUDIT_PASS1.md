# APPENDIX E — STABILITY AND CONSISTENCY AUDIT OF THE GRUT ARCHITECTURE
## PASS 1: Architecture Map, Interface Tensions, Warning Surfaces

**Date:** 2026-03-27
**Status:** PASS 1 ONLY — mapping pass, no code, no proofs
**Classification basis:** Full codebase read (grut/*.py, tests/*.py, docs/*.md)

---

## 1. EXECUTIVE PROVISIONAL DETERMINATION

> **`locally_consistent_globally_underdetermined`**

The GRUT architecture is internally consistent within each sector's claimed regime. Locks are real and defensible. But the cross-sector connections are carried almost entirely by structural assumption and pattern-matching rather than derivation. Three root causes dominate:

1. **No covariant τ_eff** — the frequency argument (ω) is substituted as H (cosmology), mode frequency (interior PDE), or |V/R| (collapse) with no covariant unification.
2. **Φ is two distinct objects** — the collapse barrier order parameter (bounded [0,α_vac]) and the constitutive scalar field (continuous, unbounded) share notation but are not shown to be the same degree of freedom.
3. **Temperature is underdetermined** — six candidates, none proven GRUT-native; this blocks the FDT, blocks thermodynamic self-consistency, and blocks Q4 closure.

No outright contradiction is demonstrated. The named tensions are documented in the existing architecture. The classification does not upgrade to `inconsistency_visible` because no internal inconsistency within a sector is found. It does not downgrade to `coherent_but_tensioned` because the underdetermination is structural, not peripheral.

**Locked inheritance preserved:**
- Appendix C: negative boundary for QM measurement/interference/Born-rule claims — unchanged.
- Q1–Q4: bounded recovery/spectral phase (Q1 shell, Q2 bath-type, Q3 algebraic, Q4 consolidation) — unchanged.
- Appendix D: thermodynamic_sector_partially_consistent; temperature definable but not unique; first law partially consistent; FDT conditional; entropy production underdetermined — unchanged.

---

## 2. AUDIT FRAME DEFINITIONS

**Constitutive well-posedness**
The constitutive relation (τ dΦ/dt + Φ = X) admits a unique, stable solution for generic forcing X given initial data. Well-posedness here means: (a) the ODE has a unique solution, (b) that solution is stable under small perturbations of X, and (c) the solution does not develop singularities in finite time within the claimed regime. The first-order linear relaxation equation is well-posed by inspection. The question is whether the nonlinear extensions (barrier activation, Φ-dependence of τ_eff) preserve this.

**Cross-sector compatibility**
Two sectors are cross-sector compatible if the quantities they share — parameters, fields, operators — carry the same physical meaning in both sectors, and if the result from one sector, when imported into the other, does not violate the receiving sector's constraints. Compatibility is degraded when the same symbol is redefined, when the same formula is used with different physical arguments, or when a quantity's range in one sector is incompatible with its use in another.

**Parameter-authority coherence**
Each parameter must have a single authority tier (locked constant, derived constraint, tunable, or phenomenological) that is stable across all sectors that use it. Authority coherence fails when a parameter is locked in one sector but left free in another, or when its derivation in one sector assumes a value that another sector treats as an output.

**Regime-transition integrity**
A transition between regimes is integral if: (a) the equations used in each regime are clearly valid only in that regime, (b) the transition point is well-defined, (c) the solutions in each regime match continuously (or the discontinuity is controlled and documented), and (d) no regime-change silently changes the physical interpretation of shared quantities. Integrity fails when transition conditions are vague, when the same formula is applied across a boundary where it was not derived, or when the transition point itself depends on the output being computed.

**Visible warning surface**
A visible warning surface is a feature already present in the codebase or documentation that signals potential instability, inconsistency, or scope violation — without yet constituting a proven failure. Examples: a hard numerical cap that, if activated, overrides physics; a sign ambiguity in a key quantity; ghost mode language in comments or test verdicts; a parameter whose sector-local justification does not transfer to other sectors.

---

## 3. INTERFACE MAP

### A. Classical constitutive law ↔ Interior PDE sector

**What is shared:**
- τ_eff formula: τ_eff = τ₀/(1 + (ωτ₀)²)
- Structural identity ω₀·τ = 1 (exact, locked)
- Quality factor Q ~ 6 (PDE-derived from Q = β_Q/α_vac = 2/(1/3))
- Dispersion relation: ω² = ω₀² + 2α·ω_g²/(1 + iωτ_eff)

**What could conflict:**
τ_eff is frequency-dependent. The interior PDE uses τ_eff as a fixed background parameter evaluated at some reference frequency. The mode analysis finds modes at various ω. If those mode frequencies differ significantly from the reference ω used to compute τ_eff, the constitutive background is not self-consistent — τ_eff(ω_mode) ≠ τ_eff(ω_reference). This is a self-consistency gap in the linearized mode analysis.

**Current status:** `compatible_with_assumptions`

**Main assumption carrying compatibility:**
Modes are analyzed in the low-frequency limit where ω·τ₀ ≪ 1, so τ_eff ≈ τ₀ and the frequency-dependence of τ_eff is negligible. The PDE validity is implicitly a slow-mode approximation.

**Evidence that would upgrade or break:**
- *Upgrade:* Self-consistent mode analysis where τ_eff is evaluated at the mode frequency and Q remains ~6.
- *Break:* If ω_mode·τ₀ ~ 1 or larger, τ_eff(ω_mode) drops significantly, Q rises (less damping), and the mixed-viscoelastic classification fails.

---

### B. Classical constitutive law ↔ Quantum recovery/spectral phase (Q1–Q4)

**What is shared:**
- τ_eff functional form (central to Q2 bath identification)
- ω₀·τ = 1 identity (Q3 algebraic grounding)
- Response class: mixed-viscoelastic (Q1 recovery route selection)
- Dissipative structure (Q1: CTP/Galley route as preferred recovery)

**What could conflict:**
Q2 identifies the bath spectral density as Drude/Lorentzian with cutoff Ω = 1/τ₀. This is a structural observation — the functional form of τ_eff matches a Drude bath. It is not a derivation. The claim that GRUT constitutive response IS the physical limit of a CTP system is asserted by structural match, not proven by integrating out bath degrees of freedom. The ghost status of the Galley doubled-field route (Route B) remains underdetermined in the physical sector after projection.

**Current status:** `compatible_with_assumptions`

**Main assumption carrying compatibility:**
(a) Structural match of τ_eff to Drude spectral density is physically meaningful (not coincidental).
(b) The CTP/Galley physical limit (Φ_- = 0 projection) successfully eliminates ghost contamination from the pre-projection sector.

**Evidence that would upgrade or break:**
- *Upgrade:* Derivation showing the constitutive law emerges from integrating out bath DOF with the Drude kernel.
- *Break:* Ghost contamination surviving projection into the physical sector; or demonstration that the τ_eff functional form can match many different bath types, undermining the identification claim.

---

### C. Quantum recovery/spectral phase ↔ Thermodynamic sector

**What is shared:**
- Temperature candidates (Q4 → thermodynamic sector; Q4 declares temperature the missing ingredient)
- FDT condition (requires unique T; thermodynamic sector has 6 candidates)
- Entropy proxies (S = πR²/l_P² in thermodynamic sector; Q4 does not supply entropy)
- Bath-type identification (Q2 Drude bath implies specific fluctuation spectrum → temperature)

**What could conflict:**
Q4 identifies temperature as the missing ingredient for closing the thermodynamic sector. The thermodynamic sector has 6 candidates, none proven. The bath identified in Q2 (Drude/Lorentzian) would, in standard open quantum system theory, carry a temperature via the fluctuation-dissipation relation η(ω) = Im[χ(ω)]/T. But this T is not extracted — Q2 stops at structural match and leaves T undetermined. The 6 thermodynamic candidates include T_kin ~ ω₀/(2Q), which uses PDE quantities but lacks physical derivation.

**Current status:** `underdetermined`

**Main assumption carrying compatibility:**
That temperature exists as a well-defined GRUT-sector quantity, and that one of the 6 candidates will eventually be selected. No selection criterion is currently operative.

**Evidence that would upgrade:**
A GRUT-native temperature derivation (likely via Unruh-type argument constrained by ω₀·τ = 1, or via FDT inversion using Q2 bath spectrum). Consistency of a single T candidate with both the FDT and the first law simultaneously.

---

### D. Interior PDE sector ↔ Thermodynamic sector

**What is shared:**
- Q ~ 6 (appears in T_kin ~ ω₀/(2Q))
- ω₀, τ_eff
- γ_eff (damping rate, relevant to FDT)

**What could conflict:**
Q in the PDE is the quality factor of the viscoelastic response — a mode damping quantity. Using Q to define a temperature imports the assumption that mode damping and thermal fluctuation are related in the standard way (which would require the FDT to already hold). This is circular: the thermodynamic sector uses Q to define T, then checks if FDT holds given that T — but FDT defines the relationship between damping and temperature, so using damping to define T and then checking FDT cannot be a non-trivial test.

**Current status:** `tensioned`

**Main assumption carrying compatibility:**
The kinetic temperature T_kin ~ ω₀/(2Q) is physically the relevant temperature (i.e., mode damping and thermal fluctuation are in equilibrium). This is an equilibrium assumption that may not hold for a driven, dissipative, non-equilibrium system.

**Evidence that would resolve:**
Independent derivation of T that does not use Q from the PDE. Alternatively, proof that the system is in local thermal equilibrium at T_kin.

---

### E. Strong-field/collapse sector ↔ Constitutive response sector

**What is shared:**
- τ_eff (same formula; ω = |V/R| in collapse)
- Φ symbol (barrier order parameter in collapse; constitutive field in action principle)
- α_vac = 1/3 (endpoint law; appears in both barrier activation and constitutive response)
- R_eq/r_s = 1/3 (endpoint; shared)

**What could conflict:**
**Φ is two distinct objects.** In the collapse sector, Φ = a_outward/a_inward is a ratio of accelerations, dimensionless and bounded [0, α_vac] ≈ [0, 0.333]. In the constitutive/action principle, Φ is a scalar field satisfying τ dΦ/dt + Φ = X, where X is a curvature/stress source — continuous and not a priori bounded. Their identification requires showing that the collapse barrier activation corresponds exactly to the constitutive field saturating at α_vac. This is asserted (the barrier sector code uses Φ → α_vac at activation) but not derived from a single governing equation.

Additionally, ω = |V/R| in collapse is a dynamical velocity-over-radius ratio, not a proper mode frequency. Using the same τ_eff formula here imports the PDE derivation into a regime where it was not derived.

**Current status:** `tensioned`

**Main assumption carrying compatibility:**
(a) Φ in collapse and Φ in the constitutive sector are the same DOF at saturation.
(b) |V/R| is an appropriate effective frequency for τ_eff evaluation in the collapse regime.

**Evidence that would upgrade or break:**
- *Upgrade:* A single covariant equation governing Φ that reduces to the barrier activation formula in the collapse limit and to the relaxation equation in the weak-field limit.
- *Break:* Showing that Φ_collapse has different units, boundary conditions, or saturation behavior than Φ_constitutive.

---

### F. Cosmology/phenomenology sector ↔ Constitutive response sector

**What is shared:**
- τ_eff formula (ω = H in cosmology)
- Memory relaxation: τ_eff dM_X/dt + M_X = H²_base
- α_mem (tunable in cosmology; ~0.1 canonical)
- Modified Friedmann: H² = (1−α_mem)H²_base + α_mem·M_X

**What could conflict:**
The cosmological sector uses a scalar isotropic memory (M_X is a scalar). The strong-field constitutive sector uses an anisotropic tensor T^Φ_μν with components (ρ_Φ, p_r, p_⊥). Appendix A explicitly confirms that the two-component support structure (Component A + B) has no FRW analogue. The strong-field closure logic is specific to the compact-object regime.

α_mem in cosmology is a free tunable parameter (~0.1 canonical). α_vac in the collapse sector is locked at 1/3. They are different parameters with similar names — α_vac is derived from endpoint constraint; α_mem is phenomenologically fit. The naming proximity is a silent mismatch risk.

**Current status:** `underdetermined`

**Main assumption carrying compatibility:**
The scalar isotropic memory of the cosmological sector is the spherically-symmetric, zero-angular-momentum sector of the anisotropic constitutive tensor. This covariant reduction has not been demonstrated.

**Evidence that would upgrade:**
A covariant formulation of T^Φ_μν that reduces to the scalar FRW memory in the isotropic limit and to the anisotropic collapse constitutive relation in the strong-field limit.

---

### G. Parameter canon ↔ All active sectors

**What is shared:**
τ₀, α_vac, ε_Q, β_Q, ω₀·τ=1, Q~6, R_eq/r_s=1/3

**Authority and cross-sector risk:**

| Parameter | Canon Tier | Cross-sector Risk |
|-----------|-----------|------------------|
| τ₀ | Phase I anchor (locked) | ω in τ_eff interpreted differently in each sector — no covariant expression |
| α_vac = 1/3 | Endpoint law (locked) | Used in collapse (barrier) and PDE (Q=β_Q/α_vac); consistent |
| β_Q = 2 | **Assumed form, not derived** | All endpoint and Q results depend on this; β_Q ≠ 2 unlocks R_eq/r_s, Q, and ε_Q simultaneously |
| ε_Q = α²_vac | Derived constraint | Dependent on β_Q=2; cascades if β_Q shifts |
| ω₀·τ = 1 | Interior PDE structural identity (locked) | Only established in PDE sector; covariant status not shown |
| Q ~ 6 | PDE-derived | Used thermodynamically without cross-sector derivation |
| α_mem ~ 0.1 | Cosmological tunable | Similar name to α_vac; distinct parameter; naming proximity is a silent risk |
| R_eq/r_s = 1/3 | Locked (Phase V) | Consistent across collapse and interior |
| f(R_eq) = −17.71 | Static interior (locked) | Sector-local; consistent |
| A_crit = 1.062 | Dynamical interior (locked) | Sector-local; consistent |

**Current status:** `compatible_with_assumptions`

**Main assumption carrying compatibility:**
β_Q = 2 is correct, and each sector's substitution of its own ω into the τ_eff formula is physically valid.

---

## 4. WARNING SURFACE MAP

**W1 — τ_eff frequency argument: silent cross-sector reinterpretation**
ω is substituted as H (cosmology), mode frequency (interior PDE), and |V/R| (collapse) into the same τ_eff formula. No covariant expression unifies these. This is the single most pervasive silent reinterpretation in the architecture. Any result depending on τ_eff carries this non-covariance as a background assumption.

**W2 — High-frequency limit of Q: classification breaks**
Q = ω₀·τ_eff/2 (from the PDE structure). As ω → high frequency, τ_eff → 0, so Q → 0. This means in the high-frequency limit, the interior is overdamped (Q → 0), not mixed-viscoelastic (Q ~ 6). The mixed-viscoelastic classification is valid only where ω·τ₀ ≪ 1. This is a regime-dependent classification with a visible warning surface at ω·τ₀ ~ 1.

**W3 — Ghost mode in Galley route: unresolved pre-projection pathology**
Route B (Galley doubled-field) has a ghost by design (Φ_- wrong-sign kinetic). Post-projection (Φ_- = 0), the test verdict is "ghost status UNDETERMINED." Four pathologies identified in the mixed channel: ghost kinetic, IC-dependence, CTP-killing, projection-killing. The physical-limit projection is not shown to be a consistent truncation in the dynamical sense (it is NOT an attractor per galley_truncation.py). Any result importing T^Φ_μν from the Galley route inherits this ghost warning.

**W4 — β_Q = 2: assumed parameter underlies all locked relations**
The relations Q = β_Q/α_vac = 6, R_eq/r_s = ε_Q^(1/β_Q) = 1/3, and ε_Q = α²_vac all depend on β_Q = 2. This is documented as "assumed form (best-fit in PDE; not derived)." If β_Q ≠ 2, three apparently locked quantities are unlocked simultaneously. Single point of assumption failure with large blast radius.

**W5 — Φ dual-use: same symbol, different objects**
Φ = a_outward/a_inward in collapse (dimensionless, bounded [0, α_vac]) and Φ = scalar memory field in constitutive law (continuous scalar). The barrier_action_sector.py uses Φ as the order parameter activating at α_vac. Whether this is the same Φ as in S_macro[Φ,g] is asserted, not derived. This creates a hidden sector-boundary condition: at the endpoint, Φ_collapse = α_vac; what is Φ_constitutive at the same point? If they're the same field, this is an unimposed Dirichlet boundary condition.

**W6 — Hard numerical caps override constitutive physics**
L_stiff activates when |H| > H_cap = 10^6 yr^-1 and clamps H. RHO clamp enforces ρ_min = 0. When these activate (logged as `L_STIFF_ACTIVATED:H_CAPPED`, `RHO_CLAMPED_NONNEGATIVE`), the constitutive response is replaced by an arithmetic guardrail, not a physical result. Any test run triggering these warnings has a contaminated regime that must be excluded from physical claims.

**W7 — Negative ρ_Φ with positive entropy proxy: silent sign mismatch**
The covariant interior analysis locks ρ_Φ < 0 (negative effective energy density) at equilibrium, NEC-saturating (ρ+p=0, w_Φ = −1). The thermodynamic sector uses S = πR²/l_P² (area law), which is positive and grows with R. The statistical interpretation of positive entropy with a negative-ρ_Φ field is not addressed. Standard thermodynamics of negative-ρ fields is not well-understood. The area-law entropy does not distinguish between a positive-ρ and a negative-ρ source. Silent mismatch between covariant closure and thermodynamic sector.

**W8 — γ-coupling sign (D5): source drives away from target configuration**
The γ-coupling in D5 (source-coupled defect) is derived as NEGATIVE — opposing hedgehog growth, not supporting it. Classification is "interpretation_open." But if this coupling is physical, the D-phase architecture may drive the system away from the O(3) hedgehog configuration that Component B requires. A negative driving force for the hedgehog is a dynamical instability risk for the entire D-phase conditional structure.

**W9 — O(3) sector hand-insertion: all D-phase results conditionally inherit**
D13 and D14 establish that no GRUT-native route derives the O(3) sector (5 tetrad routes fail; all tensor completion routes fail; Weyl coupling route CLOSED per D15). The O(3) triplet is introduced as a "principled extension." All D-phase results (D1–D12) that depend on Component B (1/r² support) conditionally inherit an ungrounded sector. "Principled" must not be read as "derived."

**W10 — Cosmological sector has no Component B analogue**
Appendix A confirms the strong-field two-component closure (Component A + B) does not extend to cosmology. The cosmological sector has memory (Component A analogue) but no hedgehog (no Component B). Any phenomenological claim about cosmological observables implicitly requiring Component B is outside the established architecture.

---

## 5. PARAMETER COHERENCE SNAPSHOT

### τ, τ_eff, τ₀

| Parameter | Consistent meaning? | Authority tier stable? | Silent mismatch? |
|-----------|--------------------|-----------------------|-----------------|
| τ₀ = 4.19×10⁷ yr | Yes — Phase I anchor | Stable (locked) | No — but see ω note |
| τ_eff = τ₀/(1+(ωτ₀)²) | Formula consistent | Stable | **YES**: ω = H (cosmo), ω_mode (PDE), \|V/R\| (collapse) — no covariant unification |
| τ (generic) | Sometimes = τ_eff, sometimes = τ₀ | Notation unstable | Minor — context usually resolves |

### Φ and related constitutive variables

| Object | Domain | Status |
|--------|--------|--------|
| Φ_collapse = a_out/a_in | [0, α_vac], dimensionless | Sector-local |
| Φ_constitutive = memory scalar | ℝ, satisfies first-order ODE | Sector-local |
| Φ_action = scalar in S_macro | Standard field | Sector-local |
| Barrier: Φ → α_vac at C→1 | Connects collapse Φ to constitutive saturation | **TENSIONED**: identification asserted, not derived |

Silent mismatch: the endpoint condition Φ = α_vac in collapse is not imposed as a boundary condition on the constitutive ODE.

### ω₀, Q, α, ω_g

| Parameter | Status |
|-----------|--------|
| ω₀·τ = 1 | Structural identity, locked, consistent within PDE sector |
| Q ~ 6 = β_Q/α_vac | PDE-derived; thermodynamic import unvalidated |
| Q in T_kin ~ ω₀/(2Q) | Cross-sector use; physically ungrounded (circular vs FDT) |
| α | **NAME COLLISION**: α_vac = 1/3 (locked), α_mem ~ 0.1 (tunable), α (PDE dispersion coefficient) — three distinct uses |
| ω_g | Interior PDE sector-local; absent from cosmological and collapse sectors |

### Endpoint radius / interior scales

| Quantity | Status |
|----------|--------|
| R_eq/r_s = 1/3 | Locked (Phase V); consistent across collapse and interior |
| f(R_eq) = −17.71 | Static TOV; sector-local lock |
| A_crit = 1.062 | Dynamical interior; sector-local lock |
| η² = 1/(8π) = COMP_B_COEFF | O(3) coefficient; **matched phenomenologically, not derived** — authority tier is "matched constant" |

### Temperature candidates

| Candidate | Origin | Cross-sector consistency |
|-----------|--------|-------------------------|
| T_kin ~ ω₀/(2Q) | PDE damping | Most internally consistent; thermodynamic meaning unvalidated |
| T_Hawk ~ ℏc³/(8πGMk_B) | Standard Hawking | Not a GRUT modification |
| T_Q2 ~ ℏ/(k_B τ₀) | Drude bath cutoff (not yet extracted) | **Gap**: implied by Q2 but never computed or compared |
| Others (×3) | Thermodynamic sector | Not audited individually here |

**Authority tier:** Underdetermined for all candidates. T_Q2 is the most notable gap: the Drude bath identified in Q2 (Ω = 1/τ₀) implies a specific temperature via the FDT that has not been extracted and compared to the 6 candidates.

### Entropy proxies

| Proxy | Status |
|-------|--------|
| S = πR²/l_P² | Area law; positive; classical; not a quantum count |
| GRUT-native entropy derivation | Does not exist |

Silent mismatch with ρ_Φ < 0 at equilibrium (W7).

### Bath-type labels

| Label | Origin | Status |
|-------|--------|--------|
| Drude/Lorentzian spectral density | Q2 structural match | Structural observation, not derivation |
| Cutoff Ω = 1/τ₀ | τ₀ authority | Consistent with τ₀ tier |
| Bath-implied temperature T_Q2 | Not extracted | **Gap** |

---

## 6. REGIME-TRANSITION SNAPSHOT

### Low-frequency → High-frequency

Mixed-viscoelastic classification (Q~6) is derived in the low-frequency limit (ω·τ₀ ≪ 1). At high frequency, Q → 0 (overdamped). High-frequency behavior is neither claimed nor excluded.

**Classification:** `coherent_with_assumptions`

### Weak-field → Strong-field

Cosmological sector: scalar isotropic memory, H-dependent τ_eff. Strong-field collapse: anisotropic T^Φ_μν, barrier activation at C→1. No continuous interpolation demonstrated. Appendix A confirms the strong-field closure does not extend to cosmology.

**Classification:** `underdetermined`

### Interior → Endpoint/Equilibrium

Dynamical interior (A_crit = 1.062) and static TOV (f(R_eq) = −17.71) are separately locked. The endpoint R_eq/r_s = 1/3 is the common equilibrium point. Both locks are consistent there.

**Classification:** `coherent`

### Classical constitutive → Open-system recovery interpretation (Q1–Q4)

Constitutive law matched to CTP/Galley structure (Q1–Q3). Match is structural, not derived. Q4 identifies temperature as the missing ingredient.

**Classification:** `coherent_with_assumptions`

### Dissipative sector → Thermodynamic translation layer

Q (damping) → T_kin (temperature candidate). γ_eff (damping) → FDT input. FDT check conditional on T selection; T is underdetermined. Translation layer exists formally but lacks physics content without T identification.

**Classification:** `underdetermined`

---

## 7. PASS 2 CODE DECISION

**Yes. A narrow deterministic audit module is warranted for PASS 2.**

It should do exactly four things:

**Task 1 — τ_eff self-consistency check.**
For each sector (collapse, interior PDE, cosmology), extract the ω value used in τ_eff, compute τ_eff(ω_sector), and check whether that τ_eff is consistent with the mode/process frequency in the same sector. Report the self-consistency ratio ω·τ_eff per sector. Flag any sector where ω·τ₀ ≳ 1 as outside the validated low-frequency regime.

**Task 2 — Q coherence check.**
Compute Q from three independent routes: (a) Q = β_Q/α_vac from formula, (b) Q = ω₀/(2γ_eff) from damping analysis in interior_pde.py, (c) Q from the mixed-viscoelastic classification in interior_waves.py. Report whether all three agree within the claimed 6–7.5 range. Compute T_kin = ω₀/(2Q) using each Q and report spread.

**Task 3 — Φ boundary condition check.**
At the equilibrium endpoint (R_eq/r_s = 1/3, C → 1/3), extract: (a) Φ_collapse from the barrier formula (expected: α_vac = 1/3), and (b) the steady-state solution Φ_constitutive = X_endpoint from the constitutive ODE. Report whether Φ_collapse = Φ_constitutive at the endpoint. This is a necessary (not sufficient) condition for the two Φ's to be the same field.

**Task 4 — Missing T_Q2 extraction.**
From the Q2 Drude bath identification (Ω = 1/τ₀), extract the implied temperature via the standard fluctuation-dissipation relation: T_Q2 = ℏΩ/k_B = ℏ/(k_B τ₀). Compare to the 6 thermodynamic candidates in thermodynamic_sector.py. Report whether T_Q2 matches any candidate within a factor of 2.

**What PASS 2 code must NOT do:**
- No new simulation runs
- No new physical claims
- No nonlinear analysis
- No claim that passing these checks proves cross-sector coherence

**Why code is justified:**
These four checks are deterministic, narrow, and produce specific numerical verdicts. They address the most structurally significant underdeterminations identified in PASS 1. They do not create false authority because they audit specific claimed relations rather than making new derivations.

---

## 8. DOCUMENT-BUILDING CONSTRAINTS FOR LATER USE

### Claims a future document MAY safely make

1. The GRUT constitutive law (τ dΦ/dt + Φ = X) is a well-posed first-order linear ODE within the low-frequency, weak-curvature regime.
2. The interior PDE structural identity ω₀·τ = 1 is exact and mass-independent within the claimed PDE sector.
3. The quality factor Q ~ 6 is derived from the formula Q = β_Q/α_vac, conditional on β_Q = 2 (assumed, not derived).
4. The endpoint law R_eq/r_s = 1/3 is locked from ε_Q = α²_vac and β_Q = 2, with both assumptions stated.
5. The O(3) defect sector is a principled extension of GRUT; it is not derived from GRUT-native structure.
6. All D-phase results (D1–D12) are conditional on the O(3) extension being physically valid.
7. The Weyl non-minimal curvature coupling route to the O(3) sector is closed (D15 result).
8. The thermodynamic sector is partially consistent: temperature is definable but not unique; first law holds conditionally on temperature choice; FDT is conditional; entropy production is underdetermined.
9. The Galley/CTP route (Route B) provides T^Φ_μν at tree level but contains a ghost mode (Φ_-) whose post-projection status is underdetermined.
10. The cosmological strong-field two-component structure has no demonstrated FRW analogue.
11. No bounce is derived; singularity softening is demonstrated but does not constitute a full bounce.
12. Dark matter and dark energy interpretations remain partial and do not achieve concordance.

### Claims a future document MUST NOT make

1. That τ_eff is covariant across sectors (it is not; ω is sector-locally reinterpreted).
2. That Q ~ 6 is a universal GRUT prediction (it is valid only in the low-frequency interior PDE regime).
3. That temperature is determined (six candidates exist, none proven).
4. That FDT holds in GRUT (it holds conditionally on a temperature choice that has not been made).
5. That the Galley route is ghost-free (the ghost is present by design; post-projection ghost status is underdetermined).
6. That the O(3) sector is derived from GRUT (D13/D14/D15 all close native derivation routes).
7. That Φ in collapse and Φ in the constitutive law are the same degree of freedom (asserted, not derived).
8. That β_Q = 2 is derived (it is assumed from best-fit).
9. That the two-component strong-field closure extends to cosmology (Appendix A contradicts this).
10. That entropy is computed from first principles (S = πR²/l_P² is an area proxy, not a microstate count).
11. That the CTP/Galley structural match to the GRUT constitutive law is a derivation (it is a structural observation).
12. That any observational claim has been confronted against data (all observable predictions remain externally unvalidated).

### Strongest defensible current classification for Appendix E after PASS 1

> **`locally_consistent_globally_underdetermined`**

The GRUT architecture is internally consistent within each named sector, and sector-level locks are defensible. Cross-sector connections are carried by structural assumptions that have not been derived. The three central underdeterminations — τ_eff non-covariance, Φ dual-use, and temperature non-uniqueness — propagate across multiple interfaces and prevent a global coherence claim. No internal contradiction is demonstrated. PASS 2 code is warranted to test four specific deterministic consistency relations identified in this audit.
