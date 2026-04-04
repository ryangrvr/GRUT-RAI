# Book IV — Target Beta: Bound-State Spectrum and Composite-Structure Audit

## Formal Audit Document

**Predecessor:** Book IV Target Beta — Gauge-Mediated Binding and Atomic-Structure Prerequisites Audit
**Branch:** Native Gauge / Force Program
**Inherited platform:** Fermionic Bridge Architecture + SU(2) Gauge Bridge + Binding Prerequisites (P1–P5, P8 met)
**Question:** What composite spectrum does the singlet binding channel actually produce?

---

## 1. Executive Verdict

The singlet channel of the SU(2) gauge-mediated two-soliton system supports a **discrete bound-state spectrum** that is qualitatively hydrogenic: a tower of levels labeled by principal and angular momentum quantum numbers, with a ground state of finite negative energy and an infinite sequence of excited states accumulating at the continuum threshold. The spectrum is modified at short range by the hard-core boundary at d = R_sk, which cuts off the Coulomb singularity and shifts energy levels upward relative to point-Coulomb predictions, but the qualitative structure — discrete levels, angular momentum degeneracy, a state-classification grammar — survives.

The composite quantum numbers are: a radial quantum number n_r = 0, 1, 2, ...; an orbital angular momentum ℓ = 0, 1, 2, ...; the gauge-singlet constraint (I = 0); and the fermionic exchange antisymmetry constraint, which correlates the spatial wavefunction symmetry with the spin/orientation state. The ground state is a spatially symmetric, orientation-antisymmetric singlet — the bridge-level analogue of para-positronium or a spin-singlet bound pair.

Orbital angular momentum introduces a centrifugal barrier that creates a series of angular momentum channels, each with its own radial spectrum. The ℓ-degeneracy is not exact (the hard core breaks the accidental degeneracy of the pure Coulomb problem), but an approximate principal quantum number N = n_r + ℓ + 1 organizes the levels into shells, with each shell containing states of different ℓ. The FR fermionic antisymmetry constrains which (ℓ, spin-orientation) combinations are allowed, providing the structural analogue of Pauli-constrained shell filling.

The composite is an extended object with size a₀ ≫ R_sk (in the weak-coupling regime), bound by gauge exchange, stabilized against collapse by the hard core, and organized by angular momentum and exchange antisymmetry. It is a bridge-level analogue of a gauge-neutral atom: two charged constituents orbiting in a bound state with discrete energy levels and quantum-number classification.

This is not a real atom. It is not chemistry. But it is the first object in the GRUT architecture that has internal quantum-number structure, discrete energy levels, and a shell-like organizational framework. The atomic-structure analogue investigation is justified.

**Classification:** Bridge-level BSR. The composite spectrum is qualitatively hydrogenic. Orbital and shell analogues exist at the structural level.

---

## 2. Why the Composite-Spectrum Audit Is the Next Correct Move

The binding prerequisites audit established that attractive channels, neutral composites, and hard-core stabilization all exist. But existence of a potential well does not guarantee a useful spectrum. A shallow well might support only a single featureless bound state. A deep well without angular structure would produce bound lumps, not organized composites. The spectrum determines whether the binding platform produces structured matter or structureless aggregates.

---

## 3. Two-Body Problem Setup

### 3.1 The Reduced System

Two identical adjoint-representation solitons in the gauge-singlet (I = 0) channel. The center-of-mass motion separates. The relative coordinate is **r** = X₁ − X₂ with magnitude d = |**r**|. The reduced mass is:

**μ_red = M_sk / 2**

where M_sk = (F_π/e)C₁ is the soliton mass.

### 3.2 The Effective Radial Potential

The radial Schrödinger equation for the relative motion in the singlet channel, with angular momentum quantum number ℓ, is:

**[−(1/2μ_red)(d²/dd² + (2/d)(d/dd)) + V_eff(d, ℓ)] ψ(d) = E ψ(d)**

where the effective potential is:

**V_eff(d, ℓ) = V_gauge(d) + V_hard(d) + V_short(d) + ℓ(ℓ+1)/(2μ_red d²)**

### Table 1 — Two-Body Effective Potential Ingredients

| Term | Origin | Range | Sign | Status |
|------|--------|-------|------|--------|
| V_gauge(d) = −α_g/d | SU(2) gauge exchange, singlet channel | All d > R_sk | Attractive (negative) | Bridge-level; α_g = g²/(2π) |
| V_hard(d) | Soliton profile overlap hard core | d ≤ R_sk | Repulsive (→ +∞) | Bridge-level; from Skyrme soliton structure |
| V_short(d) | Yukawa/portal/orientation corrections | R_sk < d < few/m_π | Mixed (parameter-dependent) | Bridge-level; exponentially suppressed beyond 1/m_π |
| ℓ(ℓ+1)/(2μ_red d²) | Centrifugal barrier | All d | Repulsive for ℓ > 0 | Standard quantum mechanics |

### 3.3 Approximation Level

The dominant features of the spectrum are determined by the competition between V_gauge (long-range, ~1/d) and V_hard (short-range, hard wall at R_sk). The short-range corrections V_short modify the details but not the qualitative structure in the regime a₀ ≫ R_sk ≫ 1/m_π.

The analysis proceeds at the level of the hydrogen atom with a hard-core cutoff — the standard "Coulomb with hard core" problem, which is well-studied in nuclear and atomic physics.

---

## 4. Effective Potential Audit

### 4.1 Shape of the Potential

For ℓ = 0 (s-wave):

V_eff(d, 0) = −α_g/d for d > R_sk, rising to +∞ at d = R_sk.

This is an attractive Coulomb well truncated by a hard wall. The well depth at d = R_sk is V(R_sk) = −α_g/R_sk. The well supports bound states if the depth exceeds the quantum-mechanical zero-point energy.

For ℓ > 0:

V_eff(d, ℓ) = −α_g/d + ℓ(ℓ+1)/(2μ_red d²) for d > R_sk.

The centrifugal barrier creates a local maximum at d_max = ℓ(ℓ+1)/(μ_red α_g) and a minimum at larger d. For large ℓ, the minimum moves outward and the binding weakens. There is a maximum ℓ above which no bound state exists.

### 4.2 Bound-State Existence Condition

The Coulomb-with-hard-core system supports bound states when the dimensionless parameter:

**ξ = α_g μ_red R_sk = (g²/(2π)) × (M_sk/2) × R_sk**

is not too large (the hard core does not push out all bound states) and the coupling α_g is strong enough to support at least one level. Since M_sk R_sk ~ C₁/(e²F_π²) × eF_π = C₁/(eF_π), we have:

**ξ ~ g² C₁ / (4π e F_π)**

For the pure Coulomb problem (R_sk → 0), the number of bound states is infinite for any α_g > 0. With a hard core at R_sk > 0, states with characteristic radius smaller than R_sk are eliminated, but states with radius ≫ R_sk survive essentially unchanged.

### Table 2 — Bound-State Existence Conditions

| Condition | What it depends on | Satisfied? |
|-----------|-------------------|-----------|
| α_g > 0 (attractive coupling) | Gauge coupling g; singlet channel | **YES** — singlet channel is attractive |
| Bohr radius a₀ = 1/(α_g μ_red) > R_sk | Coupling vs soliton size | **CONDITIONAL** — requires g not too large, or M_sk R_sk not too large |
| Well depth > zero-point energy | α_g²μ_red/2 > ℏ²/(μ_red R_sk²) | **PARAMETER-DEPENDENT** — standard Coulomb condition modified by hard core |
| At least one ℓ = 0 state exists | a₀ > R_sk | **YES** in weak-coupling regime (a₀ ≫ R_sk) |

### 4.3 Effective Potential Verdict

The singlet potential is a Coulomb well truncated by a hard core. It supports bound states when the Bohr radius exceeds the soliton radius. The well structure is qualitatively identical to the hydrogen atom with a finite nuclear radius. Short-range corrections modify the near-core wavefunction but do not destroy the Coulomb tower at large radii.

---

## 5. Bound-State Existence Audit

### 5.1 The Weak-Coupling Regime (a₀ ≫ R_sk)

In the regime where the gauge coupling α_g is small enough that the Bohr radius a₀ = 1/(α_g μ_red) greatly exceeds the soliton radius R_sk, the hard core is a small perturbation. The spectrum is approximately hydrogenic:

**E_N ≈ −α_g² μ_red / (2N²)**

where N = n_r + ℓ + 1 is the principal quantum number (n_r = 0, 1, 2, ... is the radial quantum number, ℓ = 0, 1, ..., N−1 is the orbital angular momentum).

- **Ground state (N = 1, ℓ = 0):** E₁ ≈ −α_g² μ_red / 2. Spatial size ~ a₀.
- **First excited shell (N = 2):** E₂ ≈ −α_g² μ_red / 8. Contains ℓ = 0 and ℓ = 1 states. Size ~ 4a₀.
- **Higher shells (N = 3, 4, ...):** E_N ≈ −α_g² μ_red / (2N²). Each shell N contains ℓ = 0, 1, ..., N−1.

The number of bound states is in principle infinite (Coulomb tower), though in practice the series is cut off when the bound-state radius exceeds the screening length λ or when other physical effects (dissipation, finite-temperature, external fields) intervene.

### 5.2 Hard-Core Modifications

The hard core at d = R_sk modifies the spectrum in two ways:

1. **Level shift:** All levels shift upward (less bound) relative to pure Coulomb, because the wavefunction cannot penetrate below R_sk. The shift is largest for s-wave (ℓ = 0) states, which have maximum probability near the origin, and negligible for high-ℓ states, which are centrifugally excluded from the core region.

2. **Degeneracy breaking:** In the pure Coulomb problem, states with the same N but different ℓ are exactly degenerate (the "accidental" hydrogen degeneracy). The hard core breaks this degeneracy: s-wave states are shifted up more than p-wave states, which are shifted more than d-wave states, etc. The result is a spectrum where, within each shell N, the energy increases with decreasing ℓ:

E(N, ℓ=0) > E(N, ℓ=1) > ... > E(N, ℓ=N−1)

(s-wave least bound, high-ℓ most bound within each shell). This is the opposite of the ordering in multi-electron atoms (where screening produces the opposite pattern), but the structural point — that ℓ-degeneracy is broken and states within a shell are split — is the same.

### 5.3 Strong-Coupling Regime (a₀ ~ R_sk)

If the gauge coupling is strong enough that a₀ ~ R_sk, the Coulomb picture breaks down. The bound state is strongly modified by the hard core. The spectrum may support only a small number of deeply bound states, with the system behaving more like a nuclear bound state than an atomic one. In the extreme strong-coupling limit (a₀ < R_sk), no bound states exist because the hard core excludes the entire attractive region.

### 5.4 Bound-State Existence Verdict

In the weak-coupling regime (a₀ ≫ R_sk): a discrete, approximately hydrogenic tower of bound states exists. Multiple levels, multiple angular momentum channels, shell structure with broken degeneracy. This is the regime of interest for atomic-structure analogues.

In the intermediate regime (a₀ ~ R_sk): a small number of bound states exist, strongly modified by the hard core. Reduced shell structure.

In the strong-coupling regime (a₀ < R_sk): no bound states. The hard core wins.

The spectrum is parameter-dependent but structurally available across a wide parameter range.

---

## 6. Quantum-Number Audit

### Table 3 — Quantum Numbers and State Labels

| Label | Meaning | Present? | Notes |
|-------|---------|----------|-------|
| N (principal) | N = n_r + ℓ + 1; labels the shell | **YES** | Approximate (exact degeneracy broken by hard core) |
| n_r (radial) | Number of radial nodes | **YES** | Standard for central-force problems |
| ℓ (orbital angular momentum) | Angular momentum of relative motion | **YES** | ℓ = 0, 1, ..., N−1 within shell N |
| m_ℓ (magnetic) | z-projection of orbital angular momentum | **YES** | m_ℓ = −ℓ, ..., +ℓ; (2ℓ+1)-fold degeneracy |
| I (gauge isospin) | Total SU(2) gauge representation | **FIXED** | I = 0 (singlet) for the neutral composite; constraint, not variable |
| S (total spin/orientation) | Combined spin of two spin-1/2 solitons | **YES** | S = 0 (singlet) or S = 1 (triplet); constrained by exchange antisymmetry |
| Exchange parity | Symmetry of total wavefunction under particle exchange | **FIXED** | Antisymmetric (fermionic FR sector); constrains (ℓ, S) combinations |

### 6.1 Exchange-Antisymmetry Constraint

The total two-soliton wavefunction must be antisymmetric under exchange (from the FR/Hopf fermionic sector). The total wavefunction factorizes as:

ψ_total = ψ_spatial(d) × χ_gauge × χ_spin-orientation

- **Gauge factor χ_gauge:** The singlet (I = 0) is symmetric under particle exchange (the singlet contraction δ_ab is symmetric for the adjoint representation).
- **Spin-orientation factor χ_spin:** Two spin-1/2 solitons combine into S = 0 (antisymmetric singlet) or S = 1 (symmetric triplet).
- **Spatial factor ψ_spatial:** Has parity (−1)^ℓ under exchange (r → −r).

Antisymmetry of the total wavefunction requires:

(−1)^ℓ × (+1)_gauge × (exchange parity of χ_spin) = −1

- If S = 0 (spin singlet, antisymmetric): (−1)^ℓ × (+1) × (−1) = −1, so (−1)^ℓ = +1, meaning **ℓ even** (0, 2, 4, ...).
- If S = 1 (spin triplet, symmetric): (−1)^ℓ × (+1) × (+1) = −1, so (−1)^ℓ = −1, meaning **ℓ odd** (1, 3, 5, ...).

This is the bridge-level analogue of the spin-statistics correlation in positronium: para-states (S = 0) have even ℓ; ortho-states (S = 1) have odd ℓ.

### 6.2 State-Classification Grammar

The composite states are labeled by (N, ℓ, m_ℓ, S, m_S) subject to:
- N = 1, 2, 3, ...
- ℓ = 0, 1, ..., N−1
- m_ℓ = −ℓ, ..., +ℓ
- S = 0 with ℓ even; or S = 1 with ℓ odd
- I = 0 (gauge singlet, fixed)

The number of states in shell N:
- Even-ℓ states (S = 0): ℓ = 0, 2, 4, ..., contributing Σ(2ℓ+1) × 1 each
- Odd-ℓ states (S = 1): ℓ = 1, 3, 5, ..., contributing Σ(2ℓ+1) × 3 each

For N = 1: ℓ = 0 only → S = 0 → 1 state.
For N = 2: ℓ = 0 (S=0, 1 state) + ℓ = 1 (S=1, 3×3 = 9 states) → 10 states.
For N = 3: ℓ = 0 (S=0, 1) + ℓ = 1 (S=1, 9) + ℓ = 2 (S=0, 5) → 15 states.

The state count grows with N, producing a rich internal spectrum.

### 6.3 Quantum-Number Verdict

A complete quantum-number grammar exists: (N, ℓ, m_ℓ, S, m_S) with exchange-antisymmetry constraints correlating ℓ and S. This is a genuine state-classification system, not a trivial labeling. The exchange constraint produces a nontrivial pattern of allowed states that is structurally analogous to the spin-orbit correlation in two-fermion atoms.

---

## 7. Orbital / Shell Analogue Audit

### Table 4 — Orbital / Shell Analogue Status

| Feature | Present? | Caveat |
|---------|----------|--------|
| Discrete energy levels | **YES** | Hydrogenic tower in weak-coupling regime |
| Orbital angular momentum ℓ | **YES** | Standard central-force quantum number |
| Shell structure (N labeling) | **YES** | Approximate; broken degeneracy from hard core |
| Degeneracy within shells | **YES (broken)** | Not exact (hard core breaks accidental Coulomb degeneracy) |
| Exchange-constrained occupation | **YES** | S = 0 ↔ even ℓ; S = 1 ↔ odd ℓ |
| Multi-electron shell filling | **NOT APPLICABLE** | This is a two-body system; shell filling requires many-body |
| Spectral transitions | **STRUCTURAL** | Transition rules exist (dipole selection Δℓ = ±1); no specific frequencies computed |
| Periodic-table analogue | **NO** | Requires many-body composites with sequential filling |

### 7.1 What "Shell Analogue" Means Here

The two-body composite has a discrete spectrum organized by the principal quantum number N into shells. Within each shell, states of different ℓ have slightly different energies (degeneracy broken by hard core). The exchange constraint correlates spatial (ℓ) and spin (S) quantum numbers.

This is a genuine shell-like organizational structure — but it is a property of a single two-body composite, not of a many-body system with sequential filling. The periodic table requires many fermions filling shells one by one, with Pauli exclusion forcing occupation of higher levels. That multi-body problem has not been addressed.

### 7.2 Ground State

The ground state is (N = 1, ℓ = 0, S = 0): a spatially symmetric, spin-singlet, gauge-singlet bound pair. It is the most deeply bound state. Its size is ~ a₀. Its binding energy is ~ α_g² μ_red / 2. It is the bridge-level analogue of the hydrogen ground state (or more precisely, para-positronium, since both constituents have the same mass).

### 7.3 Excited States and Transitions

The first excited shell (N = 2) contains 10 states: 1 state with (ℓ=0, S=0) and 9 states with (ℓ=1, S=1). Transitions between shells are governed by selection rules: the dominant (dipole) transitions have Δℓ = ±1. The N=2 → N=1 transition connects the (ℓ=1, S=1) states to the (ℓ=0, S=0) ground state. The transition energy is E₂ − E₁ ≈ (3/8)α_g² μ_red.

These transitions would, in a complete theory, produce radiation (gauge boson emission). The detailed transition rates depend on matrix elements that have not been computed, but the selection rules and energy ordering are determined by the quantum numbers alone.

### 7.4 Orbital / Shell Verdict

Orbital and shell analogues exist at the structural level. The two-body composite has a discrete spectrum with angular momentum quantum numbers, shell organization, broken degeneracy, and exchange-constrained state classification. This is a genuine (if minimal) internal organizational structure.

---

## 8. Composite-Structure Audit

### 8.1 Physical Picture

The gauge-singlet composite is an extended object of size ~ a₀, containing two solitons of size ~ R_sk each, orbiting at typical separation ~ a₀ in the gauge-mediated Coulomb-like potential. In the weak-coupling regime (a₀ ≫ R_sk), the composite is much larger than its constituents — the structural analogue of an atom being much larger than its nucleus.

### 8.2 Ontological Classification

The composite is best classified as a **gauge-neutral meson-like bound pair** — two gauge-charged constituents bound by gauge exchange into a neutral object. It is:

- Not an "atom" in the Standard Model sense (no electron/nucleus distinction; both constituents are identical solitons).
- Not a "molecule" (no directional bonding, no valence structure).
- Closer to **positronium** (particle-particle bound state of equal-mass constituents with opposite gauge charge in the singlet channel).

The positronium analogy is structurally precise: two identical-mass spin-1/2 fermions bound by gauge exchange in the singlet channel, with the same exchange-antisymmetry constraints and the same para/ortho state classification.

### 8.3 Multi-Composite Outlook

The two-body composite is gauge-neutral (I = 0). Two such composites interact only through higher-multipole (van der Waals-type) forces, which fall off as 1/d⁷ or faster. This means composites are weakly interacting at long range — they form a dilute gas rather than a condensed phase, absent additional structure.

For a richer composite sector, one would need:
- Composites with residual charge (not singlets) that can participate in further binding.
- Or many-body composites where sequential soliton addition with exchange constraints produces shell-filling and progressively larger neutral objects.
- Or a mechanism for inter-composite interactions beyond van der Waals.

The current two-body analysis does not address these possibilities. They are the subject of future multi-body audits.

---

## 9. Atomic-Prerequisite Re-Evaluation

### Updated Prerequisite Status

| Prerequisite | Previous status | Updated status | Change |
|-------------|----------------|---------------|--------|
| P1: Force carrier | YES | YES | Unchanged |
| P2: Long-range interaction | YES | YES | Unchanged |
| P3: Attractive channel | YES | **YES (realized)** | Binding confirmed in singlet channel |
| P4: Hard-core repulsion | YES | YES | Unchanged |
| P5: Gauge-neutral composite | YES (possible) | **YES (spectrum computed)** | Upgraded: discrete bound-state spectrum with quantum numbers |
| P6: Multi-body persistence | PARTIAL | PARTIAL | Unchanged: two-body spectrum established; multi-body still unaddressed |
| P7: Scale hierarchy | CONDITIONAL | **YES (in weak-coupling)** | Upgraded: a₀ ≫ R_sk confirmed as a consistent regime |
| P8: Exclusion / Pauli-like | YES | **YES (exchange-constrained spectrum)** | Strengthened: ℓ-S correlation from antisymmetry realized in spectrum |
| P9: Orbital / shell analogue | OPEN | **YES (two-body level)** | Upgraded: discrete levels, angular momentum, shell labeling N |
| P10: Chemistry-entry readiness | NO | **NO** | Unchanged: requires multi-body + specific charges + periodic structure |

Seven of ten prerequisites are now met. P6 (multi-body) remains partial. P10 (chemistry-entry) remains unmet. The atomic-prerequisite landscape is significantly strengthened by the realization of P5 (neutral composite with spectrum), P7 (scale hierarchy), and P9 (orbital/shell analogue).

---

## 10. Gains and Non-Gains

### Table 5 — Composite Gains and Non-Gains

| Gain | Description | Status |
|------|------------|--------|
| First actual composite spectrum | Discrete, approximately hydrogenic, with quantum numbers | Bridge-level; realized |
| Gauge-neutral bound state | Two adjoint solitons in singlet channel with E < 0 | Bridge-level; realized |
| Quantum-number grammar | (N, ℓ, m_ℓ, S, m_S) with exchange constraints | Complete for two-body |
| Orbital angular momentum | Central-force ℓ quantum number with centrifugal barrier | Standard QM result applied to bridge system |
| Shell labeling | Principal quantum number N = n_r + ℓ + 1 | Approximate (broken degeneracy) |
| Exchange-constrained states | S = 0 ↔ even ℓ; S = 1 ↔ odd ℓ | From FR antisymmetry |
| Positronium-like structure | Equal-mass bound pair with para/ortho classification | Structural analogue |
| Scale hierarchy | a₀ ≫ R_sk in weak coupling | Constituent/composite separation confirmed |
| Transition structure | Selection rules Δℓ = ±1; excited-state hierarchy | Structural; no frequencies computed |

| Non-Gain | Description | What would be needed |
|----------|------------|---------------------|
| Real atoms | No electron/nucleus; no mass hierarchy; no Standard Model | SM particle content |
| Electromagnetism | SU(2) ≠ U(1)_em; no photon | U(1) gauge sector |
| Multi-electron shell filling | Two-body only; no many-body filling | Many-body composite audit |
| Periodic table | No sequential filling; no atomic number | Multi-body + specific gauge group |
| Chemistry | No bonding, valence, reactions | Full atomic + molecular physics |
| Realistic spectroscopy | No computed frequencies; no comparison to data | Phenomenological program |
| Confinement effects | Non-Abelian dynamics may confine; not analyzed | Dedicated confinement audit |
| Dissipation compatibility | Gauge + bound-state dynamics in dissipative background | Dedicated compatibility audit |
| Specific mass/energy predictions | All in terms of bridge parameters (g, M_sk, R_sk) | Parameter determination program |

---

## 11. Hard-Gated Summary Table

| Test | Verdict | Reason |
|------|---------|--------|
| Singlet bound state exists | **YES (BRIDGE)** | Coulomb-like well + hard core → discrete ground state in weak-coupling regime |
| Multiple bound levels exist | **YES** | Hydrogenic tower: N = 1, 2, 3, ... with multiple ℓ per shell |
| Gauge-neutral composite realized | **YES** | I = 0 singlet with zero total gauge charge; discrete spectrum computed |
| Quantum-number grammar exists | **YES** | (N, ℓ, m_ℓ, S, m_S) with exchange constraints |
| Orbital analogue exists | **YES** | Angular momentum ℓ with centrifugal barrier and selection rules |
| Shell-like organization begins | **YES (two-body)** | Approximate N-labeling; broken degeneracy; exchange-constrained occupation |
| Multi-composite sector suggested | **PARTIAL** | Neutral composites interact weakly (van der Waals); richer sector needs multi-body |
| Atomic-prerequisite threshold strengthened | **YES** | P5, P7, P9 upgraded; 7 of 10 prerequisites now met |
| Chemistry-entry readiness achieved | **NO** | Multi-body filling, specific charges, periodic structure all absent |
| Next-step atomic-structure analogue audit justified | **YES** | Two-body spectrum established; many-body and multi-composite investigation warranted |

---

## 12. Nonclaims

1. NOT claiming real atoms — the composite is a positronium-like gauge-neutral bound pair of identical-mass solitons, not a hydrogen atom with distinct electron and nucleus.

2. NOT claiming electromagnetism — the binding force is SU(2) Yang–Mills, not U(1) electromagnetism; there is no photon and no electric charge.

3. NOT claiming chemistry — chemistry requires multi-electron atoms with specific charge assignments, shell-filling rules, and bonding; none of this is present.

4. NOT claiming periodic table — the periodic table requires sequential filling of many-body shells with Pauli exclusion driving occupancy; this is a two-body analysis only.

5. NOT claiming realistic spectroscopy — transition energies, oscillator strengths, and spectral series are structurally available but not computed; no comparison to observational data.

6. NOT claiming multi-electron structure — the exchange-constrained spectrum applies to a single two-body composite, not to a many-fermion system.

7. NOT claiming Standard Model matter — the bridge solitons are topological objects with SU(2) gauge charge, not electrons or quarks.

8. NOT claiming chemistry-entry readiness — the audit has strengthened 7 of 10 atomic prerequisites but P6 (multi-body) and P10 (chemistry-entry) remain unmet.

---

## 13. Next-Step Recommendation

### Table 6 — Next-Route Decision Map

| Outcome | Recommended next document | Rationale |
|---------|--------------------------|-----------|
| **Strong spectrum with shell structure (this outcome)** | **Many-body composite and shell-filling audit** | Test whether sequential soliton addition with exchange constraints produces atomic-number-like progression |
| Weak spectrum | Gauge-group revision or coupling-strength audit | If spectrum is too thin for organized structure |
| No orbital analogue | Alternative binding mechanism audit | If angular momentum structure fails to emerge |

### Recommended Next Document

**Many-Body Composite and Shell-Filling Audit.** This document should:

1. Extend the two-body analysis to three-body and N-body gauge-singlet composites.
2. Determine whether sequential addition of solitons with FR antisymmetry produces shell-filling behavior.
3. Assess whether the exchange constraint forces occupation of higher shells, producing size/energy progression with constituent number.
4. Determine whether any analogue of atomic number (Z) and shell closure emerges.
5. Evaluate whether the multi-body sector is rich enough to justify a chemistry-entry audit.

This is the bridge from "one composite has internal structure" to "a family of composites exhibits progressive organization." If it succeeds, the chemistry-entry threshold comes into view. If it fails, the program knows that the SU(2) bridge produces interesting individual composites but not a matter hierarchy.

---

*Bound-State Spectrum and Composite-Structure Audit complete. The singlet channel supports a discrete, approximately hydrogenic spectrum with orbital angular momentum, shell labeling, and exchange-constrained quantum numbers. The composite is a positronium-like gauge-neutral bound pair. Seven of ten atomic-structure prerequisites are now met. The next step is a many-body composite and shell-filling audit to determine whether progressive matter organization emerges.*
