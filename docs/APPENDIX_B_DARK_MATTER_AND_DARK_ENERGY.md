# Appendix B — Dark Matter and Dark Energy in the GRUT Vacuum

## 1. Executive Result

| Track | Classification | Hard Gates | Summary |
|-------|---------------|-----------|---------|
| **Dark Matter** | `dark_matter_interpretation_partial_mimic` | collisionless=False, scaling=False → block upper; no stable phenomenology → block effective_only | Memory stress-energy is nonzero and gravitating but is not collisionless, does not scale as a⁻³, and does not constitute an independent matter sector. No cluster-collision derivation is performed. |
| **Dark Energy** | `dark_energy_interpretation_reframes_but_does_not_solve` | vacuum_tension=False, cc_explained=False → block upper | Transient negative pressure exists during out-of-equilibrium periods. At equilibrium: ρ = 0, w = −1 (trivially vacuum, not a prediction). No persistent vacuum tension is derived. The Λ problem is not addressed. |
| **Overall** | `mixed_and_partial` | Both tracks partial | Neither dark-sector target is derived or strongly suggested within the published architecture. Both tracks yield limited analogy (DM) or limited reframing (DE) only. |

Appendix B does not derive cold dark matter. Appendix B does not derive a cosmological constant. Neither target is closed within published GRUT.

**Placement**: Structured extension — all field content is published canon, all extension assumptions are flagged, and no observational claim is made. See Section 13 for the explicit criterion.

---

## 2. Why Appendix B Is Being Tested

The GRUT memory field produces nonzero stress-energy T^Φ_μν that enters the Einstein equations as a source term. This raises a testable question: does this stress-energy, in appropriate regimes, bear any structural resemblance to dark-sector phenomenology?

Two distinct dark-sector problems exist in modern cosmology:

1. **Dark matter**: ~27% of cosmic energy density; collisionless, gravitating, non-luminous; required by rotation curves, Bullet Cluster mass-gas separation, CMB acoustic peaks, structure formation.

2. **Dark energy**: ~68% of cosmic energy density; accelerating expansion; equation of state w ≈ −1; observed via SNIa, BAO, CMB ISW effect.

Appendix B tests whether the published GRUT architecture (D10–D14 + Omni-ToE v3) produces any defensible analogy or reframing for either problem. It does not test whether GRUT solves either problem — the hard-gated classification logic blocks such conclusions in advance.

---

## 3. Separation of the Dark-Matter and Dark-Energy Problems

These are distinct problems requiring distinct analysis:

| Aspect | Dark Matter | Dark Energy |
|--------|-----------|-------------|
| **Regime** | Galaxy/cluster-scale potential wells | Cosmological (FRW) expansion |
| **Key observable** | Mass-gas separation, rotation curves, lensing | Cosmic acceleration, w ≈ −1 |
| **Relevant GRUT sector** | Memory scalar in weak-field potential wells | Memory scalar in FRW cosmology |
| **Defect sector status** | ABSENT (no compact-object topology) | ABSENT (no FRW analogue) |
| **Trigger sector status** | DORMANT (below threshold) | DORMANT at late times; active in early universe only |
| **Standard-model solution** | CDM particle species (collisionless, a⁻³ scaling) | Cosmological constant Λ (persistent, w = −1, ρ > 0) |
| **GRUT field content available** | Memory scalar only (constitutive, dissipative) | Memory scalar only (constitutive, dissipative) |

Both tracks use the same field content (memory scalar Φ) but in different regimes with different physical requirements. Neither track has access to the O(3) defect sector, which is absent at these scales.

---

## 4. Dark Matter Analysis

### 4.1 Test Results

| Test | Question | Result | Viable? | Level |
|------|----------|--------|---------|-------|
| Memory stress-energy nonzero | Does T^Φ_μν contribute to Einstein equations? | Yes | Partial | effective_only |
| Memory is collisionless | Is the memory field collisionless like CDM? | **No** | No | failed |
| Cluster-collision constitutive response | Can memory produce mass-gas offset? | Qualitative analogy only; no dynamical model | No | partial_mimic |
| Defect sector relevant | Is O(3) relevant at cluster scales? | No | No | failed |
| Scaling matches CDM | Does ρ_mem ~ a⁻³? | **No** | No | failed |
| Halo profiles | Can memory produce stable halos? | Qualitative analogy only; no derivation | No | partial_mimic |

### 4.2 Hard-Gated Classification Logic

**Hard Gate 1**: `memory_collisionless == False` AND `scaling_matches_cdm == False`
→ BLOCK `derived` and `strongly_suggested`
→ STRONGLY BIAS toward `partial_mimic`
→ Allow `effective_only` ONLY with stable weak-field phenomenology across multiple regimes (not derived here)

**Hard Gate 2**: No cluster-collision derivation or empirical confrontation performed
→ BLOCK any claim of observational reproduction or semi-reproduction

**Hard Gate 3**: Memory field is constitutive (dissipative relaxation), not an independent matter sector
→ BLOCK any language suggesting an autonomous gravitating population

### 4.3 Key Physics

The GRUT memory field is fundamentally NOT dark matter:

- **Not collisionless**: The memory is constitutive (first-order relaxation τ dΦ/dt + Φ = S), not a population of collisionless particles governed by the Boltzmann equation. It has no particle number, no phase space distribution, no velocity dispersion, no self-gravitating virial equilibrium.

- **Wrong scaling**: CDM dilutes as ρ ~ a⁻³ (essential for CMB/BBN concordance). Memory energy density ρ_Φ depends on the lag (Φ − source), not on cosmological dilution. At equilibrium, ρ_Φ → 0. The memory field fails to supply the standard CDM dilution law and is not presently compatible with a standard CDM role in early-universe concordance without further extension.

- **Not an independent sector**: The memory stress-energy is a constitutive response to the local metric — it is sourced by and determined by the baryonic geometry. It does not constitute an independent gravitating population. Calling it "dark matter" would conflate a geometric echo with an autonomous matter species.

- **Cluster-collision analogy only**: In a cluster collision, the constitutive memory response would track the total gravitational potential rather than the shocked gas, because the memory source is curvature, not baryon density. This provides a qualitative analogy to the Bullet Cluster mass-gas offset. However: no dynamical cluster-collision model is constructed, no lensing map is computed, no Bullet Cluster signature is reproduced or semi-reproduced, and the mechanism is constitutive (not collisionless). This is an analogy identification, not a derivation.

- **No independent halo structure**: Memory stress is a constitutive echo of the baryonic gravitational potential, not a self-gravitating virialized population with its own density profile.

### 4.4 Classification

**`dark_matter_interpretation_partial_mimic`** — the memory stress-energy is nonzero and enters the Einstein equations, and the constitutive response to potential rather than gas provides a qualitative analogy to mass-gas offset. But the ontology is wrong (constitutive vs collisionless), the scaling is wrong (lag-dependent vs a⁻³), no independent sector exists, and no observational derivation is performed.

---

## 5. Dark Energy Analysis

### 5.1 Test Results

| Test | Question | Result | Viable? | Level |
|------|----------|--------|---------|-------|
| Produces negative pressure | Can p_Φ < 0? | Yes, during transients only | Partial | effective_only |
| Equation of state w = −1 | Does w_Φ → −1? | Yes, trivially at equilibrium (ρ = 0) | No | reframes_only |
| Vacuum tension derived | Is persistent Λ derived? | **No** | No | failed |
| Cosmological constant explained | Is Λ ~ 10⁻¹²² M_Pl⁴ explained? | **No** | No | failed |
| Requires cosmological extension | Extra assumptions needed? | Yes | No | failed |

### 5.2 Hard-Gated Classification Logic

**Hard Gate 1**: `vacuum_tension_derived == False` AND `cosmological_constant_explained == False`
→ BLOCK `derived` and `strongly_suggested`
→ Default to `reframes_but_does_not_solve` if some reframing value exists
→ Downgrade to `failed` if no reframing value exists

**Hard Gate 2**: w = −1 at equilibrium with ρ = 0 is trivially vacuum
→ BLOCK any claim that this constitutes a dark energy prediction

### 5.3 Key Physics

The GRUT memory architecture provides a limited conceptual reframing, not a solution:

- **At equilibrium** (Φ = source): ρ_Φ = 0, w_Φ = −1. This is trivially vacuum — zero energy density with w = −1 is indistinguishable from empty space. It is not a prediction of dark energy.

- **During transients** (Φ ≠ source): negative pressure is possible when effective potential energy dominates kinetic energy. But constitutive relaxation dissipates the lag on timescale τ. The negative pressure is temporary, not sustained.

- **The constitutive obstruction** (inherited from Appendix A): First-order relaxation τ dΦ/dt + Φ = S is kinetic-dominated, not potential-dominated. Cannot sustain w < −1/3 indefinitely. At late times: exponential approach to equilibrium → any dark-energy-like contribution dissipates.

- **Reframing only**: GRUT replaces "what is Λ?" with "why does cosmological memory lag persist?" This is a different question but not a solution. The constitutive structure actively dissipates the lag, so the reframing immediately raises the question of what prevents equilibration — a question the architecture does not answer.

### 5.4 Classification

**`dark_energy_interpretation_reframes_but_does_not_solve`** — transient negative pressure exists during out-of-equilibrium periods, w = −1 at equilibrium is trivially vacuum (not a prediction), no persistent vacuum tension is derived, the Λ problem is not addressed. The reframing replaces one unanswered question with another.

---

## 6. Minimal Mathematical Models

### 6.1 Dark Matter Minimal Model

**Field content**: Scalar memory field Φ(r) in weak-field potential wells

**Regime**: Galaxy/cluster-scale, Φ ≪ 1, curvature well below strong-field threshold

**Effective equations**:
- Constitutive relaxation: τ dΦ/dr + Φ = S(r) = α_vac M(r)/r
- Memory stress-energy contribution: T^Φ_tt ~ (1/2)(dΦ/dr)² ~ (α_vac M/r)² / (2τ²) at lag
- Effective metric correction: δg_tt ~ −2 ΔM(r)/r where ΔM = ∫ T^Φ_tt 4πr² dr

**Interpretation type**: Phenomenological — source function S(r) and galactic timescale τ_galactic are not derived from published canon. The model identifies a stress-energy contribution, not a dark matter sector.

### 6.2 Dark Energy Minimal Model

**Field content**: Homogeneous scalar memory field Φ(t) in FRW cosmology

**Regime**: Late-time cosmology, H ~ H₀, K ≪ K_threshold

**Effective equations**:
- Constitutive relaxation: τ_cosmo dΦ/dt + Φ = S(H, K)
- Effective energy density: ρ_Φ = (1/2)(dΦ/dt)² + V_eff(Φ)
- Effective pressure: p_Φ = (1/2)(dΦ/dt)² − V_eff(Φ)
- Modified Friedmann: H² = (8π/3)(ρ_matter + ρ_Φ)
- Equation of state: w_Φ = p_Φ / ρ_Φ → −1 at equilibrium (where ρ_Φ → 0)

**Interpretation type**: Phenomenological — τ_cosmo, S(H,K), and V_eff are not derived from published canon. The constitutive memory has no variational potential; V_eff is a heuristic effective description only.

---

## 7. Comparison to Classical Baselines

### Table B — Dark Matter Comparison

| Scenario | Outcome | Assumptions Needed | Where Λ-CDM Wins | Comment |
|----------|---------|-------------------|-------------------|---------|
| Classical baseline (Λ-CDM) | Collisionless CDM with a⁻³ scaling; fits rotation curves, Bullet Cluster, CMB, structure formation | CDM particle species (nature unknown) | Collisionless dynamics, a⁻³ scaling, CMB concordance, structure formation, Bullet Cluster lensing | Standard model; CDM as free parameter with extensive observational support |
| GRUT memory only | Nonzero stress-energy in potential wells; constitutive response tracks potential, not gas; NOT collisionless, wrong scaling, no concordance | Weak-field S(r), τ_galactic | All items listed for Λ-CDM above | Partial analogy only: right qualitative direction for mass-gas offset, wrong ontology, wrong scaling |
| GRUT memory + extension | Phenomenological tuning could match specific rotation curves in specific galaxies | S(r) form + τ_galactic + phenomenological enhancement | Collisionless dynamics, a⁻³ scaling, CMB concordance, structure formation | Parameter fitting, not derivation; gains specificity but not explanatory power |

**Assessment**: Λ-CDM clearly outperforms GRUT on every dark-matter observable except the philosophical preference for not introducing a new particle species. The GRUT memory provides a stress-energy contribution but does not replicate any of CDM's core successes (collisionless dynamics, correct scaling, concordance).

### Table C — Dark Energy Comparison

| Scenario | Outcome | Assumptions Needed | Where Λ-CDM Wins | Comment |
|----------|---------|-------------------|-------------------|---------|
| Classical baseline (Λ-CDM) | Persistent Λ with w = −1, ρ_Λ > 0; fits SNIa, BAO, CMB ISW | Λ (value unexplained) | Persistent vacuum tension, quantitative fit to expansion history | Standard model; Λ as free parameter with strong observational fit |
| GRUT memory only | Trivial w = −1 at equilibrium (ρ = 0); transient negative pressure; no persistent tension | S(H,K), τ_cosmo, V_eff | Persistent vacuum tension, quantitative acceleration, nonzero ρ_Λ | Reframing only: replaces one unanswered question with another |
| GRUT memory + extension | Persistent lag possible if source fine-tuned to prevent equilibration | Slowly-evolving S + persistence mechanism (fine-tuned) | Persistence without fine-tuning | Substantial extension; fine-tuning mirrors the Λ problem it was meant to address |

**Assessment**: Λ-CDM clearly outperforms GRUT on dark energy observables. Λ-CDM fits the expansion history quantitatively (albeit with an unexplained parameter). GRUT provides no persistent vacuum tension and no quantitative fit. The reframing is conceptual only.

---

## 8. Classification

### Table E — Final Classification

| Track | Classification | Hard Gates Applied | Justification |
|-------|---------------|--------------------|---------------|
| **Dark Matter** | `dark_matter_interpretation_partial_mimic` | collisionless=False + scaling=False → block derived/strongly_suggested; no stable phenomenology → block effective_only; no cluster-collision derivation → block observational claims | Nonzero stress-energy and qualitative analogy to mass-gas offset, but wrong ontology (constitutive vs collisionless), wrong scaling (lag vs a⁻³), no independent sector, no concordance |
| **Dark Energy** | `dark_energy_interpretation_reframes_but_does_not_solve` | vacuum_tension=False + cc_explained=False → block derived/strongly_suggested; trivial w = −1 at ρ = 0 → not a prediction | Transient negative pressure during out-of-equilibrium periods; trivial w = −1 at equilibrium; no Λ derivation; reframing replaces one unanswered question with another |
| **Overall** | `mixed_and_partial` | Both tracks partial | Neither dark-sector target is derived or strongly suggested within the published architecture |

---

## 9. Assumptions

### Table A — Assumption Table

| Assumption | Status | Source | Comment |
|-----------|--------|--------|---------|
| Memory scalar Φ produces nonzero T^Φ_ab | Inherited from canon | Phase IV memory tensor | Established |
| Constitutive relaxation: τ dΦ/dt + Φ = S | Inherited from canon | Phase IV first-order structure | Locked |
| O(3) defect sector absent at cosmological/cluster scales | Inherited from canon | Appendix A structural finding | Hedgehog requires spatial center + S² topology |
| Weak-field source function S(r) for DM interpretation | Extension assumption | Extended from strong-field | Form not derived; required for DM minimal model |
| Galactic relaxation timescale τ_galactic | Phenomenological | Not derived from canon | May differ from compact-object τ; value unknown |
| Cosmological source function S(H,K) for DE interpretation | Extension assumption | Extended from strong-field | Form not derived; required for DE minimal model |
| Cosmological relaxation timescale τ_cosmo | Phenomenological | Not derived from canon | May differ from compact-object τ; value unknown |
| Effective potential V_eff(Φ) for DE stress-energy | Extension assumption | Heuristic relaxation model | Constitutive memory has no variational potential; V_eff is a heuristic only |
| No new fields or particle species introduced | Inherited from canon | Minimal extension principle | Only published GRUT field content used |

### Table D — Parameter Authority

| Parameter | Value/Form | Authority | Source |
|-----------|-----------|-----------|--------|
| α_vac | 1/3 | Inherited | GRUT canonical vacuum ratio |
| τ | √(3/2) | Inherited | GRUT canonical relaxation timescale |
| S(r) | α_vac M(r)/r (assumed) | Phenomenological | Extended from strong-field; not derived |
| τ_galactic | Unidentified | Open | Not derived; value unknown |
| S(H,K) | Monotonic in curvature (assumed) | Phenomenological | Extended from strong-field; not derived |
| τ_cosmo | Unidentified | Open | Not derived; value unknown |
| V_eff | ~Φ²/(2τ²) (effective) | Phenomenological | Heuristic; constitutive memory has no potential |
| H₀ | ~70 km/s/Mpc | Phenomenological | Observation; not GRUT-derived |

---

## 10. Nonclaims

1. **Appendix B does not derive cold dark matter.** The memory field is a constitutive geometric response, not a collisionless particle species. It has no particle number, no phase space distribution, no velocity dispersion, and no self-gravitating virial equilibrium.

2. **Appendix B does not derive a cosmological constant.** No persistent vacuum tension is produced. At equilibrium the memory contributes zero energy density. The fundamental question of why Λ ~ 10⁻¹²² M_Pl⁴ is not addressed.

3. **Appendix B does not reproduce the Bullet Cluster.** No dynamical cluster-collision model is constructed. No lensing map is computed. No mass-gas separation is derived. The appendix identifies only a qualitative analogy by which a constitutive geometric response could track potential rather than gas.

4. **Appendix B does not establish early-universe concordance.** The memory field does not scale as a⁻³ and is not presently compatible with a standard CDM role in CMB acoustic peaks, BBN, or structure formation without fundamental extension beyond published canon.

5. **Appendix B does not close the dark sector within published GRUT.** Neither the dark matter nor the dark energy interpretation is derived or strongly suggested. Both remain at the level of limited analogy or limited reframing.

6. **The O(3) defect sector is not invoked.** It has no cosmological or cluster-scale analogue. The hedgehog requires a spatial center and S² winding topology absent in FRW and cluster geometries.

7. **The dark-energy w = −1 at equilibrium is trivially vacuum, not a prediction.** Zero energy density with w = −1 is indistinguishable from empty space. No observational consequence follows.

8. **Memory lag is not persistent vacuum energy.** The constitutive structure actively dissipates the lag via exponential relaxation toward equilibrium. The reframing ("why does lag persist?") immediately raises a question the architecture does not answer.

9. **No empirical confrontation is performed.** Neither interpretation has been tested against rotation curves, lensing data, SNIa, BAO, CMB power spectrum, or any other observational dataset.

10. **Parameters τ_cosmo, τ_galactic, S(H,K), S(r), and V_eff are not derived from published canon.** They are extension assumptions or phenomenological placeholders required for the minimal models.

11. **The memory stress-energy does not constitute an independent matter sector.** It is a constitutive response to the local metric, sourced by and determined by the baryonic gravitational potential. It is not autonomous.

12. **Appendix B does not claim the memory field is equivalent to modified gravity (MOND, f(R), etc.).** The constitutive memory mechanism has different physical content from modified-gravity theories.

---

## 11. What Would Be Required to Upgrade Appendix B Further

### Dark Matter: partial_mimic → effective_only

All of the following would be required simultaneously:
- Derive the weak-field source function S(r) from published GRUT canon (not assumed)
- Demonstrate that the resulting memory stress-energy produces stable, repeatable effective gravitating mass across both halo AND cluster observables (not just one regime)
- Establish explicit regime bounds within which the phenomenology is controlled
- Construct a dynamical cluster-collision model showing quantitative mass-gas offset

Even if all of the above were achieved: the collisionless and scaling failures would remain, permanently blocking `derived` and `strongly_suggested`.

### Dark Matter: effective_only → strongly_suggested

Would require resolving at least one of two structural obstructions:
- Demonstrate that the constitutive response mimics collisionless behavior across the relevant observational regime (this appears structurally impossible: constitutive relaxation is dissipative, collisionless dynamics is Hamiltonian)
- Show that cosmological concordance (CMB/BBN) does not actually require a⁻³ scaling for this component (would require fundamental revision of concordance cosmology)

Neither appears achievable within the constitutive framework.

### Dark Energy: reframes_but_does_not_solve → effective_only

All of the following would be required simultaneously:
- Derive a mechanism by which constitutive memory lag persists against dissipation at cosmological timescales (the constitutive structure actively opposes this)
- Show that the resulting effective vacuum tension is quantitatively consistent with observed cosmic acceleration (H₀, q₀)
- Derive the cosmological source function S(H,K) and timescale τ_cosmo from published canon

### Dark Energy: effective_only → strongly_suggested

Would require:
- Derive or predict the observed dark energy density ρ_Λ ~ 10⁻¹²² M_Pl⁴ from GRUT parameters
- This appears structurally impossible within the constitutive framework: at equilibrium ρ_Φ = 0, and the constitutive structure drives toward equilibrium

### Both Tracks

Any upgrade requires empirical confrontation: testing the interpretations against rotation curves, Bullet Cluster lensing data, SNIa, BAO, CMB power spectrum. The observable roadmap from the Bridge document provides the framework but no test has been performed.

---

## 12. Strongest Hostile Reading and Conservative Reply

**Hostile reading**: "Appendix B identifies that the GRUT memory field produces nonzero stress-energy and then spends several pages calling this 'partial mimicry' and 'reframing.' But a constitutive response that vanishes at equilibrium, cannot replicate collisionless dynamics, does not scale as a⁻³, and produces zero vacuum energy density at late times has no dark-sector interpretive force whatsoever. The 'qualitative analogy' to Bullet Cluster mass-gas offset is not a result — it is a speculation dressed in conservative language. Any scalar field coupled to curvature will produce stress-energy in potential wells; this is not specific to GRUT. The dark energy 'reframing' replaces an unanswered question (what is Λ?) with a harder one (why does dissipative lag persist against its own relaxation dynamics?). The correct classification for both tracks is 'failed,' and the correct overall classification is 'appendix_b_failed.'"

**Conservative reply**: The hostile reading correctly identifies every structural limitation. The memory field is not collisionless, does not scale correctly, vanishes at equilibrium, and provides no quantitative dark-sector prediction. We do not dispute any of these points — they are the basis of our own hard-gated logic. The difference between `partial_mimic` and `failed` is narrow and turns on a specific criterion: does the memory stress-energy provide any structural resemblance to the dark-sector target beyond generic "any scalar field produces stress-energy"? We judge that the constitutive response tracking potential rather than gas (for DM) and the transient negative pressure during out-of-equilibrium periods (for DE) are GRUT-specific structural features, not generic scalar-field properties — the first-order relaxation structure and the curvature-sourced constitutive relation are particular to the GRUT architecture. This justifies `partial_mimic` over `failed` for DM and `reframes_but_does_not_solve` over `failed` for DE. If a reviewer judges these features insufficiently specific, downgrading to `failed` on both tracks would be a defensible alternative reading. We would not contest that judgment on technical grounds.

---

## 13. Structured Extension vs. Speculative Horizon

**Criterion**: An appendix qualifies as *structured extension* if (1) all field content used is established in published canon, (2) every extension assumption beyond canon is explicitly flagged, (3) no observational claim is made without a supporting derivation, and (4) the classification is determined by explicit hard-gated logic, not by narrative judgment.

**Why Appendix B meets this criterion**:
- The only field content used is the published memory scalar Φ and its constitutive relaxation (Phase IV canon).
- Every extension assumption (S(r), τ_galactic, S(H,K), τ_cosmo, V_eff) is explicitly flagged in the assumption table with status `extension_assumption` or `phenomenological`.
- No observational reproduction is claimed — not for Bullet Cluster, not for rotation curves, not for SNIa, not for CMB.
- The classifications are produced by hard-gated logic with explicit boolean criteria and blocking conditions, not by prose interpretation.

**What would immediately push Appendix B into speculative horizon**:
- Claiming the memory field IS dark matter (ontological overclaim without collisionless dynamics)
- Claiming the memory field derives the cosmological constant (no persistent vacuum tension exists)
- Claiming Bullet Cluster reproduction without a dynamical cluster-collision model
- Claiming CMB/BBN concordance without a⁻³ scaling
- Introducing unpublished field content (D15+, O(3) at cosmological scales, new couplings)
- Allowing narrative to override hard-gated classification outcomes

None of these occur in Appendix B.

---

## 14. Internal Consistency Check

| Section | Must Not Exceed | Status |
|---------|----------------|--------|
| Executive overview | Hard-gated classification levels | Checked: states "limited analogy" and "limited reframing only"; states neither target derived |
| DM analysis prose | `partial_mimic` | Checked: every positive statement is immediately qualified by structural failure |
| DE analysis prose | `reframes_but_does_not_solve` | Checked: every positive statement is immediately qualified; reframing called "conceptual only" |
| Comparison tables | Λ-CDM clearly wins where it should | Checked: added "Where Λ-CDM Wins" column; assessment paragraphs state Λ-CDM outperforms |
| Nonclaims | Cover all tempting overclaims | Checked: 12 nonclaims including independence, concordance, Bullet Cluster, Λ |
| Upgrade path | Requirements are hard, not soft | Checked: "all of the following simultaneously" language; structural impossibility noted |
| Classification table | Matches hard-gated code output | Checked: DM=partial_mimic, DE=reframes, Overall=mixed_and_partial |
