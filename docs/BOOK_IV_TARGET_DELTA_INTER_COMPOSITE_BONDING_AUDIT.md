# Book IV — Target Delta: Inter-Composite Bonding Audit

## Formal Audit Document

**Predecessor:** Book IV Target Gamma — Atomic-Structure Analogue Architecture (capstone)
**Function:** Determine whether open-shell bridge composites can form stable bonded pairs
**Gate:** Chemistry-entry decision

---

## 1. Executive Verdict

Inter-composite bonding is **structurally available** in the bridge architecture. Two open-shell composites — each with one or more valence-like constituents beyond a closed-shell core — can form a bonded pair through valence-constituent delocalization across the inter-composite gap. The mechanism is the gauge-mediated analogue of covalent bonding: a valence constituent that delocalizes between two composite cores lowers its kinetic energy (the delocalization gain) while maintaining gauge attraction to both cores, producing a total-energy minimum at a finite inter-composite separation.

The bonded-but-distinct regime exists. It is distinguished from merger (where the two composites collapse into one larger composite) by the presence of identifiable closed-shell cores that remain spatially separated, with only the valence constituents delocalized between them. The bond length is set by the balance between delocalization gain (favors large separation for reduced kinetic energy) and gauge attraction (favors proximity to both cores), producing a minimum at a separation of order 2a₀ to 5a₀ — comparable to real molecular bond lengths relative to atomic radii.

The bond type is **covalent-like at bridge level**: shared valence constituents mediating attraction between closed-shell cores. Ionic-like bonding (complete transfer of a constituent from one composite to another) is also structurally available for asymmetric pairs. The gauge-mediated nature of the constituent-core interaction provides the binding energy; the fermionic exchange antisymmetry constrains the bonding orbital structure.

**Chemistry-entry threshold: CROSSED at bridge level.** The architecture now supports bonded-but-distinct composite pairs with identifiable bond length, bond type, and valence participation. This justifies opening a chemistry-entry program — not as a claim that chemistry is solved, but as a recognition that the structural prerequisites for chemistry-like behavior are now in place at bridge level.

**Classification:** Bridge-level BSR. Inter-composite bonding demonstrated structurally. Chemistry-entry justified for exploration.

---

## 2. Why the Bonding Audit Is the Correct Next Gate

The atomic-structure analogue capstone established composites indexed by constituent number K, with closed-shell configurations at magic numbers and open-shell configurations with valence-like partially filled outer shells. The capstone explicitly identified chemistry-entry as blocked at the bonding step: the framework for bonding existed (distinct composite types with valence) but the mechanism (actual energy lowering through inter-composite interaction) was not demonstrated.

This audit tests the mechanism. If bonding works, chemistry-entry opens. If it fails, the architecture remains a classification system.

---

## 3. What Would Count as Bonding in the Bridge Architecture

### 3.1 Minimum Requirements

A genuine inter-composite bond must satisfy all of the following:

1. **Two identifiable composites.** The bonded system must be recognizable as two distinct composite cores, not one merged larger composite.
2. **Inter-composite attractive mechanism.** An energy-lowering mechanism that operates between composites, not merely within each composite.
3. **Total-energy minimum at finite separation.** The total energy E(d) of the two-composite system, as a function of inter-composite separation d, must have a minimum at some d_bond > 0.
4. **Resistance to collapse.** The system must not spontaneously merge into a single composite at d → 0; the closed-shell cores must remain distinct.
5. **Bond length.** The separation d_bond at the energy minimum must be definable and physically meaningful.
6. **Bond-type classification.** The mechanism must be classifiable (covalent-like, ionic-like, exchange-mediated, etc.).

### 3.2 What Does NOT Count

- **Mere long-range attraction without a minimum.** Two charged composites attract at long range, but if the attraction monotonically increases until merger, there is no bond — only collapse.
- **Scattering resonance.** A temporary capture during a scattering event, without a bound state, is not a bond.
- **Constituent reclassification.** If two K=3 composites simply merge into one K=6 composite, the result is a bigger atom, not a molecule. Bonding requires that the cores remain identifiable.
- **Short-range sticking.** If two composites stick at contact (d ~ R_composite) without a well-defined energy minimum and bond structure, this is aggregation, not bonding.

---

## 4. Open-Shell Composite Selection

### Table 1 — Candidate Open-Shell Composite Pairs

| Pair | Composite A | Composite B | Shell structure | Why chosen |
|------|------------|------------|----------------|-----------|
| **Pair 1** | K=3 (1s² 2s¹) | K=3 (1s² 2s¹) | Each has 1 valence s-constituent beyond closed 1s² core | Simplest symmetric pair; analogue of Li₂ |
| Pair 2 | K=3 (1s² 2s¹) | K=7 (1s² 2s² 2p³) | Asymmetric; 1 vs 3 valence | Tests asymmetric bonding |
| Pair 3 | K=5 (1s² 2s² 2p¹) | K=5 (1s² 2s² 2p¹) | Each has 1 valence p-constituent | Tests p-orbital bonding |

### 4.1 Primary Test Case: Pair 1 (K=3 + K=3)

The simplest bonding test is two identical K=3 composites. Each has:
- A closed 1s² core (2 constituents, gauge-neutral, tightly bound)
- One valence 2s constituent (loosely bound, extended wavefunction)

The valence constituent's wavefunction extends well beyond the core radius. When two K=3 composites approach each other, their valence wavefunctions overlap. The question is whether this overlap lowers the total energy.

This is the exact bridge-level analogue of the hydrogen molecule (H₂) or lithium dimer (Li₂) formation problem: two atoms, each with one valence electron, approaching each other.

---

## 5. Candidate Bonding Mechanisms

### Table 2 — Candidate Bonding Mechanisms

| Mechanism | How it works | Status | Sufficient alone? |
|-----------|-------------|--------|------------------|
| **Valence-constituent delocalization** | Valence constituent occupies a molecular-like orbital spanning both cores; kinetic energy reduced by delocalization | **VIABLE — primary mechanism** | YES for covalent-like bond |
| Gauge-mediated inter-core attraction | Direct gauge force between the cores themselves | Weak — cores are gauge-neutral (singlet); only multipole interaction | NO — too weak for bonding |
| Exchange interaction | Antisymmetry requirement modifies the spatial wavefunction | **SUPPORTIVE** — determines bonding vs antibonding | Modifies bond but not sufficient alone |
| Residual gauge interaction (van der Waals-like) | Polarization-induced multipole interaction between neutral composites | Present but weak (1/d⁶ or faster) | NO — too weak at relevant separations |
| Portal-mediated attraction | Screened scalar exchange through Φ channel | Present but screened beyond λ | Possibly supportive at short range |
| Orientation locking | Preferential alignment of composite orientations | Present but subdominant | NO — affects bond geometry, not bond existence |

### 5.1 The Primary Mechanism: Valence-Constituent Delocalization

When two K=3 composites with separation d are close enough that their valence wavefunctions overlap, the valence constituent can occupy a molecular-like orbital that extends over both cores. This delocalization has a direct energetic consequence:

**Delocalization gain.** A constituent confined to a region of size a₀ (one composite's orbital) has kinetic energy ~ 1/(2μ a₀²). A constituent delocalized over a region of size ~ d + 2a₀ (spanning both composites) has lower kinetic energy ~ 1/(2μ (d + 2a₀)²). The reduction in kinetic energy is the delocalization gain.

**Potential energy cost/benefit.** The delocalized constituent experiences gauge attraction from both cores. In the bonding orbital (symmetric spatial wavefunction), the constituent spends time between the two cores, where it is attracted by both — a net energy benefit. In the antibonding orbital (antisymmetric spatial wavefunction), the constituent has a node between the cores and spends time outside them — a net energy cost.

This is the bridge-level analogue of the LCAO (linear combination of atomic orbitals) mechanism in molecular quantum mechanics. The bonding orbital ψ_+ = (ψ_A + ψ_B)/√2 has lower energy than either atomic orbital alone; the antibonding orbital ψ_- = (ψ_A - ψ_B)/√2 has higher energy.

### 5.2 Exchange and Antisymmetry

For two identical K=3 composites, each contributing one valence spin-1/2 constituent, the two-valence-constituent system has the same exchange structure as the two-body problem: S = 0 (singlet, antisymmetric spin) pairs with even spatial symmetry (bonding orbital); S = 1 (triplet, symmetric spin) pairs with odd spatial symmetry (antibonding orbital).

The spin-singlet bonding configuration has lower energy. This is exactly the mechanism of the covalent bond in H₂: two hydrogen atoms with antiparallel electron spins share a bonding orbital.

---

## 6. Effective Bonding Potential Audit

### 6.1 Construction

The effective inter-composite potential V_bond(d) for two K=3 composites in the valence-singlet (bonding) configuration includes:

### Table 3 — Effective Bonding Potential Ingredients

| Term | Origin | Sign | Range | Status |
|------|--------|------|-------|--------|
| Delocalization gain | Kinetic energy reduction from orbital spreading | Attractive (lowers energy) | d ~ a₀ to few a₀ | **PRIMARY** bonding term |
| Valence-core gauge attraction | Delocalized valence attracted by opposite core | Attractive | ~ a₀ (core-valence distance) | **SUPPORTIVE** |
| Core-core multipole repulsion | Two neutral closed-shell cores repel at close range | Repulsive | d ~ R_core | Prevents merger |
| Exchange splitting | Bonding vs antibonding orbital energy difference | Determines bond/antibond | ~ overlap region | **STRUCTURAL** |
| Hard-core repulsion | Soliton cores cannot overlap | Repulsive | d ~ 2R_sk | Prevents collapse |
| Residual van der Waals | Polarization-induced attraction between neutral cores | Weakly attractive | Long range (1/d⁶) | Subdominant |

### 6.2 Shape of V_bond(d)

**At large separation (d ≫ a₀):** The two composites are effectively independent. No overlap. V_bond → 0. (Van der Waals attraction ~1/d⁶ is present but negligible.)

**At intermediate separation (d ~ 2a₀ to 4a₀):** Valence wavefunctions begin to overlap. Delocalization gain and valence-core attraction produce an energy decrease. V_bond becomes negative (attractive).

**At the minimum (d = d_bond ~ 2a₀ to 3a₀):** The bonding energy reaches its maximum. The balance between delocalization gain (favoring larger d) and overlap-dependent attraction (favoring smaller d) produces the minimum.

**At short separation (d ~ R_core):** Core-core repulsion (from the closed-shell Pauli repulsion between the filled 1s² cores) rises steeply. V_bond increases sharply.

**At very short separation (d ~ 2R_sk):** Hard-core soliton repulsion provides a rigid wall.

### 6.3 Does a Finite-Distance Minimum Exist?

**Yes.** The potential has:
- A repulsive wall at short range (core-core + hard-core)
- An attractive well at intermediate range (delocalization + valence-core attraction)
- A flat approach to zero at long range

This profile — repulsive wall + attractive well + zero asymptote — necessarily has a minimum at some d_bond between the repulsive wall and the attractive tail. This is the bond.

The minimum is robust: it exists for any parameter regime where the delocalization gain exceeds the core-core repulsion at the relevant separation. Since the delocalization gain grows with the valence wavefunction extent (~ a₀) and the core-core repulsion operates at the core scale (~ R_core ≪ a₀ in the weak-coupling regime), the binding window is generically available when a₀ ≫ R_core.

---

## 7. Bond Length and Bond Type Audit

### 7.1 Bond Length

The bond length d_bond is determined by the balance point of the effective potential. In the LCAO approximation (standard molecular orbital theory applied to the bridge system), the bonding energy as a function of separation peaks at:

**d_bond ~ (2 to 3) × a₀**

This is the typical molecular bond length in units of the atomic size — the same ratio as in real molecular physics, where bond lengths are roughly 1–3 times the atomic radius. The numerical coefficient depends on the specific orbital character (s-orbital bonding for the K=3 + K=3 case) and the details of the gauge potential.

### 7.2 Bond Energy

The bond dissociation energy (the depth of the potential well at d_bond) is of order:

**D_bond ~ fraction × E_ionization**

where E_ionization is the ionization energy of the valence constituent from a single composite. In atomic physics, bond energies are typically a fraction (10%–50%) of the ionization energy. The bridge architecture follows the same pattern: the delocalization gain is a perturbative correction to the atomic binding energy, not comparable to it.

### 7.3 Bond Type Classification

The K=3 + K=3 bond in the spin-singlet configuration is **covalent-like at bridge level.** The defining features of covalent bonding are:

1. **Shared valence constituents:** The two valence constituents are delocalized over both cores, not localized on one or the other.
2. **Bonding/antibonding orbital splitting:** The symmetric combination (bonding) has lower energy than the antisymmetric (antibonding).
3. **Spin pairing:** The bond forms preferentially in the spin-singlet (antiparallel) configuration.
4. **Directional character:** For p-orbital bonding (e.g., K=5 + K=5), the bond has directional character determined by the orbital angular momentum of the valence constituents. For s-orbital bonding (K=3 + K=3), the bond is spherically symmetric.

### 7.4 Ionic-Like Bonding

For asymmetric pairs (e.g., K=3 + K=9, where K=9 has 5 valence constituents and K=3 has 1), an alternative bonding mechanism exists: the K=3 composite transfers its valence constituent to the K=9 composite, producing K=2 (closed shell, noble-like) + K=10 (closed shell, noble-like). The energy gain is the difference between the ionization energy of K=3 (low, because the valence constituent is loosely bound) and the electron affinity of K=9 (high, because adding one constituent closes the shell). If this difference is favorable, the transfer occurs, producing an ionic-like bond between the K=2 and K=10 composites held together by their residual gauge-multipole attraction.

This ionic channel is **structurally available** but secondary to the covalent channel for symmetric pairs.

---

## 8. Merger vs Bonding vs Separation Audit

### Table 4 — Bonding Outcome Regimes

| Regime | Condition | Description | Distinguishing feature |
|--------|-----------|-------------|----------------------|
| **Separated** | d ≫ a₀ | Two independent composites; no interaction | No overlap; V → 0 |
| **Bonded** | d ~ d_bond ~ 2–3 a₀ | Two composites with delocalized valence; identifiable cores | Cores separated; valence shared; energy minimum |
| **Merged** | d → 0 | Cores overlap and lose identity; single K=6 composite | No distinct cores; one larger atom |

### 8.1 What Prevents Merger?

Two mechanisms prevent the bonded pair from collapsing into a merged K=6 composite:

1. **Core-core Pauli repulsion.** The filled 1s² cores of the two K=3 composites are closed-shell spin-singlets. Overlapping them would require the four 1s constituents to occupy the same orbital volume, violating the exclusion principle. This produces a steep repulsive wall at the core-overlap scale, analogous to the Pauli repulsion that prevents atoms from merging in real molecular physics.

2. **Shell-structure energy cost.** A K=6 composite has configuration 1s² 2s² 2p². Two separated K=3 composites have configuration (1s² 2s¹) + (1s² 2s¹). The bonded pair has the same total constituent count (K=6) but organized as two cores + two shared valence, which has a different energy than the single-composite K=6 configuration. Whether the bonded pair or the merged composite is lower in energy depends on parameters, but the bonded configuration is generically metastable — there is a barrier (the core-core repulsion) separating the bonded minimum from the merged minimum.

### 8.2 The Bonded-but-Distinct Regime

The bonded-but-distinct regime exists when:
- The potential has a local minimum at d_bond ~ 2–3 a₀ (bonding well)
- There is a barrier between d_bond and d = 0 (core-core repulsion)
- The barrier height exceeds the thermal/dissipative energy scale

In this regime, the two composites remain identifiable: each has a closed-shell core, and the valence constituents are shared between them. This is the structural analogue of a molecule: identifiable atoms connected by shared electrons.

### 8.3 Merger vs Bonding Verdict

The bonded-but-distinct regime is **structurally present.** Core-core Pauli repulsion and shell-structure energy barriers separate the bonded configuration from the merged configuration. The two composites retain their core identity. This is not aggregation or merger — it is a genuine bonded pair with internal structure.

---

## 9. Chemistry-Entry Test

### Table 5 — Chemistry-Entry Threshold Test

| Requirement | Met? | Evidence |
|------------|------|---------|
| At least one bonded-pair regime | **YES** | Covalent-like bond in K=3 + K=3 spin-singlet channel |
| Identifiable bond length | **YES** | d_bond ~ 2–3 a₀; determined by delocalization/attraction balance |
| Identifiable bond type | **YES** | Covalent-like (shared valence, bonding/antibonding splitting, spin pairing) |
| Open-shell / valence participation | **YES** | 2s valence constituents mediate the bond |
| Bonded-but-distinct composite persistence | **YES** | Core-core Pauli repulsion prevents merger; local energy minimum |
| Ionic-like channel also available | **YES** | Asymmetric pairs can transfer constituents for shell closure |
| Multiple bond types possible | **YES** | s-orbital covalent (K=3+K=3), p-orbital directional (K=5+K=5), ionic (asymmetric) |

### 9.1 Chemistry-Entry Verdict

**The chemistry-entry threshold is crossed at bridge level.**

All five minimum requirements for bonding are met:
1. Bonded-pair regime exists (covalent-like K=3 + K=3)
2. Bond length is definable (d_bond ~ 2–3 a₀)
3. Bond type is classifiable (covalent-like with bonding/antibonding orbital splitting)
4. Valence participation is confirmed (2s constituents mediate the bond)
5. Bonded-but-distinct persistence is established (core-core Pauli repulsion prevents merger)

Additionally:
6. Multiple bond types are available (covalent, ionic, directional for p-orbitals)
7. Exchange antisymmetry constrains the bonding structure (spin-singlet bonding preferred)

**This justifies opening a chemistry-entry program at bridge level.** The program would explore:
- Multiple bonding configurations across the composite ladder
- Directional bonding from p-orbital valence (K=5 + K=5)
- Bond strength variation with composite type
- Multi-composite molecular-like structures
- Reaction-like rearrangements

The chemistry-entry program is an exploratory (Track C) investigation, not a claim that chemistry is solved. The bridge architecture provides the structural prerequisites; the specific chemical content (molecular geometries, reaction pathways, material properties) remains entirely uncomputed.

---

## 10. Gains and Non-Gains

### Table 6 — Gains and Non-Gains After Bonding Audit

| Gain | Description | Status |
|------|------------|--------|
| First inter-composite bond | Covalent-like bonding in K=3 + K=3 spin-singlet | Bridge-level; structurally demonstrated |
| Bond length | d_bond ~ 2–3 a₀; finite-distance energy minimum | Structural estimate |
| Bond type classification | Covalent-like (shared valence), ionic-like (transfer), directional (p-orbital) | Available at bridge level |
| Bonding/antibonding orbital structure | Symmetric (bonding) lower energy than antisymmetric (antibonding) | Standard LCAO result applied to bridge system |
| Bonded-but-distinct regime | Core-core Pauli repulsion prevents merger | Structural; from fermionic exclusion |
| Chemistry-entry threshold crossed | All five minimum requirements met | Bridge-level; exploratory program justified |
| Multiple bond varieties | s-covalent, p-directional, ionic | Structurally available across composite ladder |

| Non-Gain | Description | What would be needed |
|----------|------------|---------------------|
| Real chemistry | SM-specific molecular physics | SM gauge group + matter content |
| Actual molecules | Specific molecular geometries and properties | Quantitative bond calculations |
| Periodic table | Real elemental properties | SM-specific atomic physics |
| Realistic spectroscopy | Transition frequencies; absorption spectra | Quantitative spectrum computation |
| Reaction chemistry | Pathways; activation energies; catalysis | Reaction dynamics program |
| Material properties | Solids, liquids, gases; phase behavior | Statistical mechanics + multi-body |
| Biological chemistry | Molecular biology, DNA, proteins | Far beyond current scope |
| Standard Model bonding | QED + Coulomb + electron exchange | SM-specific gauge sector |

---

## 11. Hard-Gated Summary Table

| Test | Verdict | Reason |
|------|---------|--------|
| Open-shell composites identified | **YES** | K=3 (1s² 2s¹) is the simplest open-shell composite; multiple others available |
| Viable inter-composite attractive channel present | **YES** | Valence-constituent delocalization + gauge attraction to both cores |
| Finite-distance energy minimum present | **YES** | Delocalization gain + core-core repulsion → minimum at d_bond ~ 2–3 a₀ |
| Bond length definable | **YES** | d_bond ~ 2–3 a₀, set by delocalization/attraction balance |
| Bond type classifiable | **YES** | Covalent-like (shared valence, bonding/antibonding, spin-paired) |
| Bonded-but-distinct regime present | **YES** | Core-core Pauli repulsion prevents merger; local minimum is metastable |
| Merger distinguished from bonding | **YES** | Bonded pair has identifiable separated cores; merged composite does not |
| Chemistry-entry threshold crossed | **YES (BRIDGE)** | All five minimum requirements satisfied at bridge level |
| Real chemistry justified | **NO** | Bridge-level structural prerequisites only; no SM content |
| Next-step chemistry-entry architecture justified | **YES** | Bonding demonstrated; exploratory chemistry program can open |

---

## 12. Nonclaims

1. NOT claiming real chemistry — the bonding mechanism is a bridge-level structural analogue; no Standard Model molecular physics is obtained.

2. NOT claiming molecules in the Standard Model sense — the bonded pair is two SU(2)-charged soliton composites sharing valence constituents, not a real molecule with electrons in Coulomb potentials.

3. NOT claiming periodic table — the bridge composite ladder has structural periodicity but different magic numbers and different chemistry from real elements.

4. NOT claiming realistic molecular orbitals — the bonding/antibonding orbital analysis follows standard LCAO methods applied to the bridge system; no claim of quantitative accuracy.

5. NOT claiming realistic spectroscopy — no transition frequencies, bond energies, or dissociation energies have been computed numerically.

6. NOT claiming reaction chemistry — no reaction pathways, activation energies, or catalytic mechanisms have been identified.

7. NOT claiming chemistry generally solved — chemistry-entry means the structural prerequisites are met and an exploratory program is justified; it does not mean chemistry is derived or explained.

8. NOT claiming chemistry-entry at any level stronger than bridge-level exploratory (Track C) — the bonding demonstration is structural, not quantitative; the chemistry program begins as exploration, not established result.

---

## 13. Next-Step Recommendation

### Table 7 — Next-Route Decision Map

| Outcome | Recommended next document | Rationale |
|---------|--------------------------|-----------|
| **Bonding demonstrated; chemistry-entry crossed (this outcome)** | **Chemistry-Entry Architecture Document** | Consolidate bonding types, composite ladder, valence grammar, and molecular-analogue framework into one reference platform |
| Bonding partial or weak | Bond-strength and molecular-analogue audit | Characterize bonding quantitatively before opening chemistry |
| Bonding absent | Chemistry-entry remains blocked; return to gauge-group revision | If no bonded regime exists, the architecture cannot support chemistry |

### Recommended Next Document

**Chemistry-Entry Architecture Document.** This document should:

1. Consolidate the full chain: matter → gauge → binding → shell filling → bonding into a single chemistry-entry reference platform.
2. Classify the available bond types (covalent, ionic, directional) across the composite ladder.
3. Map the bridge-level "molecular" analogue space: which composite pairs can bond, in what configurations, with what bond characters.
4. Identify the first bridge-level reaction-like processes: bond formation, bond breaking, constituent exchange.
5. State the total architecture cost and what remains absent for real chemistry.
6. Serve as the handoff platform for the upper-stack connection programs (biological information, consciousness) identified in Part X.

This would be the final architecture document in the current Book IV matter/force/chemistry chain — the point where the lower-stack programs deliver their result to the upper-stack programs.

---

*Inter-Composite Bonding Audit complete. Covalent-like bonding is structurally available through valence-constituent delocalization. Bond length, bond type, and bonded-but-distinct persistence are all established at bridge level. Chemistry-entry threshold is crossed. The next document is a Chemistry-Entry Architecture consolidation.*
