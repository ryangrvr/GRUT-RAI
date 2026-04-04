# Book IV — Target Lambda: Fidelity and Higher-Specificity Pairing Audit

## Formal Audit Document — Upper-Stack Fidelity Gate

**Predecessor:** Book IV Target Kappa — Pre-Biological Organization Capstone
**Function:** Determine whether the two-class fidelity ceiling can be raised to identity-level faithful copying
**Gate:** Heredity/lineage program entry decision

---

## 1. Executive Verdict

The fidelity ceiling can be **partially raised** from two-class (D/A) to **four-class** specificity using physically present within-class distinctions, at **zero additional postulate cost.** The upgrade is a free consequence of existing structural differences between monomers within each class.

The key distinguishing feature is **bonding-site geometry**: within the D class, K=8 (two lone pairs, divalent backbone) and K=9 (two lone pairs, monovalent) differ in the number of available backbone bonds and the spatial arrangement of their lone pairs. Within the A class, K=6 (two empty p-sites, divalent) and K=7 (three empty p-sites, trivalent) differ in the number and geometry of their acceptor sites. These geometric differences produce distinct steric and orientational signatures at the secondary-bonding interface — signatures that a growing partner chain can discriminate if the template-partner contact geometry is sensitive to the acceptor/donor site arrangement.

The resulting four-class pairing map is:

- **D1 (K=8, divalent donor) ↔ A1 (K=6, divalent acceptor)**
- **D2 (K=9, monovalent donor) ↔ A2 (K=7, trivalent acceptor)**

The geometric basis: D1's lone-pair arrangement matches A1's empty-site arrangement (both divalent, both linear/planar secondary-bonding geometry). D2's lone-pair arrangement matches A2's empty-site arrangement (D2 monovalent, A2 with one of its three sites geometrically complementary to D2's single available secondary bond direction). Cross-class pairings (D1↔A2, D2↔A1) are geometrically disfavored: the steric fit is worse, requiring distortion of the secondary-bonding contact.

This four-class system is not as specific as real nucleotide base pairing (which uses multiple hydrogen bonds with precise geometric complementarity), but it is a genuine structural upgrade from two-class. The complement-of-complement identity C(C(S)) = S now holds at the four-class level, preserving identity across replication rounds for each of the four monomer types, not just their D/A class.

The fidelity ceiling is raised from **class-faithful, identity-lossy** to **four-class-faithful, with reduced but not eliminated within-subclass degeneracy.** The remaining degeneracy (if more than four monomer types exist) would require additional bonding features to resolve. For the four primary monomer types (K=6, K=7, K=8, K=9), identity-level fidelity is structurally available.

**Classification:** Bridge-level BSR. Fidelity ceiling partially raised. Four-class pairing available at zero cost. Heredity preconditions audit justified.

---

## 2. Why Fidelity and Specificity Are the Next Correct Gate

The pre-biological capstone identified the fidelity ceiling as the single most consequential boundary in the architecture. Class-level replication preserves the coarse D/A ordering but loses the specific monomer identity within each class. This loss blocks heredity (no identity-level heritable variation), coding (no identity-level sequence-to-function mapping), and evolution (no identity-level mutation + selection).

Raising the ceiling is the one structural upgrade that would simultaneously open multiple downstream programs. If identity-level fidelity is achievable, the architecture transitions from a pre-biological replication substrate to a proto-biological hereditary substrate — the most consequential single step in the upper-stack program.

---

## 3. What Counts as Higher-Specificity Pairing and Fidelity Gain

### Table 1 — Fidelity/Specificity Threshold Checklist

| Condition | Meaning | Required for identity-faithful replication? |
|-----------|---------|-------------------------------------------|
| Within-class physical distinctions | D-type monomers (K=8, K=9) differ in some exploitable physical property | YES — basis for discrimination |
| Reproducible selective matching | Specific D-monomer pairs preferentially with specific A-monomer | YES — pairing must be nondegenerate |
| Nondegenerate complement map | Each monomer has a unique or near-unique complement | YES — C must resolve identity, not just class |
| Identity-preserving duplex | Duplex encodes which specific monomer occupies each position | YES — information stored at identity level |
| Identity-faithful template reuse | After separation, template re-specifies the same identity-level complement | YES — information survives cycling |
| Bounded identity-level error | Error rate per position per round is below 1/N for chain length N | YES — Eigen threshold at identity level |

### What Does NOT Count

- **Labeling differences without physical discrimination:** Calling K=8 "D1" and K=9 "D2" is not specificity unless the pairing system can tell them apart through physical interaction.
- **Weak preferences that wash out:** If D1↔A1 is only marginally preferred over D1↔A2, the preference provides negligible fidelity gain after many rounds.
- **Geometric variation without template consequence:** If monomers differ in shape but the template-partner contact does not resolve the difference, the variation is invisible to the replication cycle.

---

## 4. Within-Class Distinguishability Audit

### Table 2 — Within-Class Distinguishability Sources

| Source | D class: K=8 vs K=9 | A class: K=6 vs K=7 | Physically meaningful? | Usable for pairing? | Status |
|--------|---------------------|---------------------|----------------------|--------------------|----|
| **Number of backbone bonds** | K=8: divalent (2 bonds); K=9: monovalent (1 bond + 2 lone pairs) | K=6: divalent (2 bonds); K=7: trivalent (3 bonds) | **YES** — determines connectivity and chain role | **YES** — affects steric access to secondary sites | **KEY DISCRIMINATOR** |
| **Lone-pair count** | K=8: 1 lone pair; K=9: 2 lone pairs | N/A for A class (acceptors have empty sites, not lone pairs) | **YES** — affects donor strength and geometry | **PARTIAL** — more lone pairs = different spatial signature | Available |
| **Empty-site count** | N/A for D class | K=6: 0 empty p-sites beyond backbone bonds; K=7: 0 empty sites beyond backbone (all 3 p-sites bonding) | **PARTIAL** — depends on saturation state | **PARTIAL** | Needs careful analysis |
| **Bonding geometry (spatial)** | K=8: lone pair(s) roughly perpendicular to backbone axis; K=9: lone pairs in a specific arrangement relative to single backbone bond | K=6: linear divalent backbone; K=7: trigonal trivalent backbone | **YES** — different angular signatures at secondary-bonding interface | **YES** — template contact geometry differs | **KEY DISCRIMINATOR** |
| **Steric profile** | K=8 divalent: secondary sites flanking a linear backbone; K=9 monovalent: secondary sites surrounding a terminated chain end | K=6 divalent: accepts along linear backbone; K=7 trivalent: accepts in a plane | **YES** — different spatial footprints | **YES** — template-partner steric fit differs | **KEY DISCRIMINATOR** |
| **Shell-occupancy difference** | K=8: 1s² 2s² 2p⁴ (4 p-electrons); K=9: 1s² 2s² 2p⁵ (5 p-electrons) | K=6: 1s² 2s² 2p² (2 p-electrons); K=7: 1s² 2s² 2p³ (3 p-electrons) | **YES** — different charge distributions | **INDIRECT** — affects donor/acceptor strength | Supporting |

### 4.1 The Dominant Discriminator: Bonding-Site Geometry

The most robust within-class distinction is **bonding-site geometry** — the spatial arrangement of secondary bonding sites (lone pairs for donors, empty sites for acceptors) relative to the backbone axis.

**K=8 (D1, divalent donor):** Two backbone bonds (chain linker) + one lone pair available for secondary bonding. The lone pair projects roughly perpendicular to the backbone axis. The secondary-bonding contact is a **side-on** interaction.

**K=9 (D2, monovalent donor):** One backbone bond (chain terminator/pendant) + two lone pairs. The lone pairs project in directions set by the p-orbital geometry around a single backbone bond. The secondary-bonding contact is an **end-on** or **flanking** interaction.

**K=6 (A1, divalent acceptor):** Two backbone bonds (chain linker) + the empty p-site(s) accessible from the sides. The secondary-bonding acceptance geometry is **side-on**, matching D1.

**K=7 (A2, trivalent acceptor):** Three backbone bonds (branch point). The geometry around K=7 is trigonal. The secondary-bonding acceptance geometry is **planar/angular**, matching D2's flanking lone-pair arrangement better than D1's side-on geometry.

### 4.2 Distinguishability Verdict

Within-class distinctions are **physically present and geometrically exploitable.** The dominant discriminator is bonding-site geometry: divalent vs monovalent/trivalent backbone determines the spatial arrangement of secondary-bonding contacts. This distinction is structural (determined by the shell configuration and bonding character) and reproducible (every K=8 has the same geometry; every K=9 has the same geometry).

---

## 5. Higher-Specificity Pairing-Rule Audit

### 5.1 The Four-Class Map

The geometric discrimination defines a four-class pairing system:

### Table 3 — Candidate Higher-Specificity Pairing Rules

| Rule | Alphabet size | Pairing | Physical basis | Specificity | Status |
|------|-------------|---------|---------------|------------|--------|
| **D1↔A1** (K=8↔K=6) | 4-class | Divalent donor ↔ divalent acceptor | Side-on lone pair ↔ side-on empty site; both are backbone linkers | **PREFERRED** — geometric match (linear/linear) | **AVAILABLE** |
| **D2↔A2** (K=9↔K=7) | 4-class | Monovalent donor ↔ trivalent acceptor | End-on/flanking lone pairs ↔ planar/angular empty sites | **PREFERRED** — geometric match (pendant/branch-point) | **AVAILABLE** |
| D1↔A2 (K=8↔K=7) | Cross-class | Divalent donor ↔ trivalent acceptor | Side-on lone pair ↔ planar acceptor; steric mismatch at interface | **DISFAVORED** — geometric mismatch | Energetically penalized |
| D2↔A1 (K=9↔K=6) | Cross-class | Monovalent donor ↔ divalent acceptor | End-on lone pairs ↔ side-on empty site; geometric mismatch | **DISFAVORED** — geometric mismatch | Energetically penalized |

### 5.2 Pairing Specificity

The four-class specificity is based on **geometric complementarity**: side-on matches side-on (D1↔A1), and flanking/pendant matches planar/branch (D2↔A2). Cross-class pairings require geometric distortion — the contact interface does not align naturally — producing an energy penalty ΔE_mismatch that disfavors them.

The specificity is weaker than real nucleotide base pairing (which uses multiple hydrogen bonds with Angstrom-precision geometric complementarity) but stronger than the two-class D/A system (which had no within-class discrimination at all). The four-class system provides a **real structural upgrade** in specificity.

### 5.3 Template Compatibility

The four-class pairing is fully template-compatible. A template chain with sequence (D1, A2, D1, D2, A1) guides assembly of a complement (A1, D2, A1, D1, A2) through sequential local pairing at four-class resolution. Each template position specifies not just "D or A" but "which D or A," constraining the partner to one of four types rather than one of two.

### 5.4 Higher-Specificity Verdict

A four-class pairing system is **structurally available** using existing within-class geometric distinctions. The D1↔A1, D2↔A2 complement map is physically motivated by bonding-site geometry. Cross-class pairings are disfavored by geometric mismatch. The system is template-compatible and integrates with the existing replication cycle.

---

## 6. Fidelity Gain Audit

### 6.1 Complement-of-Complement at Four-Class Level

The four-class complement map C₄ is:

C₄(D1) = A1, C₄(A1) = D1, C₄(D2) = A2, C₄(A2) = D2

Therefore:

**C₄(C₄(S)) = S exactly at the four-class level.**

Each monomer type maps to a unique complement, and the complement of the complement recovers the original exactly. This is the same algebraic involution property that held at the two-class level, now extended to four classes.

### 6.2 What the Four-Class System Preserves

After one replication round at four-class specificity:
- The **identity** of each monomer (D1, D2, A1, or A2) is preserved in the complement, not just the class (D or A).
- After two rounds (complement of complement), the **original four-class sequence is recovered exactly.**
- No identity-level information is lost (within the four primary monomer types).

### 6.3 Error Regime at Four-Class Level

Two error types now:
- **Class errors** (D↔A confusion): disfavored by the primary donor-acceptor energy gap. Same as before.
- **Subclass errors** (D1↔D2 or A1↔A2 confusion): disfavored by the geometric mismatch penalty ΔE_mismatch. New source of discrimination.

The per-position error rate for subclass errors is:

p_subclass ~ exp(−ΔE_mismatch / kT)

If ΔE_mismatch is comparable to the thermal energy kT, subclass errors are frequent. If ΔE_mismatch ≫ kT, subclass errors are rare. The geometric mismatch penalty is a quantitative parameter that has not been computed, but its existence is structural.

The improved Eigen threshold at four-class level:

N_max ~ 1 / max(p_class, p_subclass)

If p_subclass < p_class (geometric mismatch is a weaker discriminator than donor-acceptor energetics), then p_subclass is the bottleneck. If p_subclass ~ p_class, the four-class system has the same effective threshold as the two-class system. The four-class upgrade is valuable only if ΔE_mismatch is large enough to make subclass errors rare.

### 6.4 Fidelity Gain Verdict

The four-class system preserves identity-level sequence information exactly through the complement cycle (C₄(C₄(S)) = S for all four types). The practical fidelity gain depends on the geometric mismatch penalty ΔE_mismatch relative to thermal energy. If ΔE_mismatch is substantial, the four-class system provides a genuine fidelity upgrade. If ΔE_mismatch is small, the upgrade is formal but not operational.

**Structural fidelity gain: YES. Operational fidelity gain: CONDITIONAL on ΔE_mismatch.**

---

## 7. Four-Class-or-Higher Feasibility Audit

### 7.1 Four-Class Feasibility

The four-class system (D1↔A1, D2↔A2) is feasible using existing within-class geometric distinctions (Section 4). It requires no new monomers, no new bonding types, and no new postulates. It is a **free consequence** of the structural differences already present in the composite ladder.

### 7.2 Higher Than Four?

Could a five-class, six-class, or higher system be constructed?

Within the current primary monomer set (K=6, K=7, K=8, K=9), four is the maximum: each monomer type maps to exactly one complement. For higher-class pairing, additional monomer types would be needed — composites with distinct bonding geometries not reducible to the four current types.

The composite ladder does contain additional types: K=5 (monovalent p-acceptor/terminator), K=4 (subclosed, essentially inert), K=3 (monovalent s-donor), K=11 (new shell, sodium-like). These could in principle extend the alphabet beyond four, but:

- K=3 and K=5 are monovalent (chain terminators, not backbone linkers) — they cannot participate in extended chains as interior monomers.
- K=4 is essentially inert — no bonding sites.
- K=11 and higher open new shells but with the same bonding-character categories (s-valence, p-valence, lone pairs) — they may provide additional types but the pairing specificity would rely on the same geometric mechanisms.

**Five or six classes:** Structurally possible if the geometric discrimination can resolve finer distinctions (e.g., K=8 in 2p⁴ vs a hypothetical K=8* in a different orbital configuration). This is speculative and undemonstrated.

### 7.3 Feasibility Verdict

**Four-class: YES, at zero cost.** Uses existing geometric distinctions between four primary monomer types.
**Five or six classes: OPEN.** Possible with additional monomer types from the composite ladder; specificity mechanism is the same but untested.
**Higher: SPECULATIVE.** Would require finer geometric discrimination or additional bonding features.

---

## 8. Fidelity Ceiling Revision Audit

### Table 4 — Fidelity Ceiling Outcomes

| Outcome | What is preserved | What is lost | Implication |
|---------|------------------|-------------|------------|
| **Two-class ceiling (prior)** | D vs A class sequence | Identity within class (K=8 vs K=9, K=6 vs K=7) | Class-faithful, identity-lossy; blocks heredity |
| **Four-class ceiling (this audit)** | Four-type identity sequence (D1, D2, A1, A2) | Nothing within the four primary types (conditional on ΔE_mismatch) | **Identity-faithful for four types; heredity preconditions met** |
| **Identity-level error** | Four-type sequence minus p_subclass per position per round | Accumulates at rate p_subclass × N per round | Bounded by Eigen threshold at four-class level |
| **Higher-class ceiling** | Finer identity if > 4 types | TBD | Open; depends on extended alphabet feasibility |

### 8.1 Ceiling Revision Verdict

The fidelity ceiling is **raised from two-class to four-class.** The four primary monomer types (K=6, K=7, K=8, K=9) are discriminable through bonding-site geometry. The complement-of-complement identity holds at the four-class level. Identity-level information is preserved across replication cycles (conditional on ΔE_mismatch being substantial).

The ceiling is raised **at zero additional postulate cost.** The geometric discrimination is a free consequence of existing shell structure differences. No new fields, parameters, or postulates are required.

---

## 9. Mutation / Variation Preconditions Audit

### Table 5 — Mutation/Variation Preconditions

| Condition | Met? | Why it matters |
|-----------|------|---------------|
| Identity-level sequence variation | **YES** | Four distinct monomer types at each chain position; 4^N possible sequences |
| Persistent variation across rounds | **YES (CONDITIONAL)** | Identity preserved if p_subclass low; variation heritable | Requires ΔE_mismatch ≫ kT |
| Distinguishable copied variants | **YES** | Different four-class sequences produce different chain geometries | Template product encodes variant identity |
| Stable sequence families | **YES (CONDITIONAL)** | Lineages of similar sequences persist if error rate is low | Requires Eigen threshold not exceeded |
| Structured mutation spectrum | **PARTIAL** | Subclass errors (D1→D2, A1→A2) are more likely than class errors (D→A); mutation is biased | Some mutation structure present |
| Selectable variation | **OPEN** | Requires different sequences to have different functional consequences | Function not yet demonstrated |

### 9.1 Mutation Structure

In the four-class system, the most likely replication errors are subclass substitutions (D1→D2 or A1→A2), which maintain the correct D/A class but change the specific monomer. Class substitutions (D→A or A→D) are rarer. This produces a structured mutation spectrum: most mutations are conservative (within-class), and radical mutations (between-class) are suppressed.

This is structurally analogous to the transition/transversion distinction in nucleic acid mutation: transitions (purine↔purine or pyrimidine↔pyrimidine) are more common than transversions (purine↔pyrimidine). The bridge architecture naturally produces this bias through the energy hierarchy (class errors penalized more than subclass errors).

### 9.2 Mutation Verdict

Identity-level variation is structurally present in the four-class system. Variation can persist across replication rounds if ΔE_mismatch is sufficient. The mutation spectrum is structured (conservative mutations more likely than radical). These are the preconditions for later heredity and selection programs. Whether variation is selectable depends on whether different sequences have different functional consequences — a question the current architecture cannot answer (no sequence-to-function mapping).

---

## 10. Cost Audit

### Table 7 — Cost/Accounting Impact

| Category | Pre-Lambda total | Lambda additions | Post-Lambda total |
|----------|-----------------|-----------------|-------------------|
| Extension postulates | 13 | **+0** | **13** |
| Free parameters | 6 | **+0** | **6** |
| Constrained/fixed params | 2 | **+0** | **2** |
| New spacetime fields | 1 | **+0** | **1** |
| New propagating DOF | 6 | **+0** | **6** |

**The four-class pairing upgrade adds zero cost.** The geometric discrimination between monomers within each class is a free consequence of existing shell-structure differences. No new postulates, parameters, fields, or degrees of freedom are required. The zero-cost upper-stack streak continues.

This is now the seventh consecutive upper-stack target (Epsilon through Lambda) that adds zero postulate cost. The entire climb from chemistry-entry through pre-biological organization through four-class identity-faithful replication preconditions is a free mathematical consequence of the matter + gauge bridge installed in Targets Alpha and Beta.

---

## 11. Threshold Test

### Fidelity and Higher-Specificity Threshold

| Requirement | Met? | Evidence |
|------------|------|---------|
| Within-class physical distinctions present | **YES** | Bonding-site geometry, valence count, steric profile differ between K=8/K=9 and K=6/K=7 |
| Reproducible selective matching | **YES (STRUCTURAL)** | D1↔A1 and D2↔A2 geometrically preferred; cross-class disfavored | Conditional on ΔE_mismatch |
| Nondegenerate complement map | **YES** | Four distinct types, each with unique complement |
| Identity-preserving duplex | **YES** | Four-class duplex encodes which specific monomer at each position |
| Identity-faithful template reuse | **YES** | C₄(C₄(S)) = S exactly at four-class level |
| Bounded identity-level error | **CONDITIONAL** | p_subclass bounded by geometric mismatch penalty; value uncomputed |

**Fidelity and higher-specificity threshold: CROSSED at the structural level, conditional on the geometric mismatch penalty being substantial.**

---

## 12. Gains and Non-Gains

### Table 6 — Gains and Non-Gains

| Gain | Description | Status |
|------|------------|--------|
| Four-class pairing alphabet | D1↔A1, D2↔A2 from bonding-site geometry | Bridge-level; zero cost |
| Identity-level complement map | Each of four types maps to unique complement | C₄(C₄(S)) = S exactly |
| Fidelity ceiling raised | From two-class to four-class identity preservation | Conditional on ΔE_mismatch |
| Identity-level sequence diversity | 4^N possible sequences (up from 2^N at class level) | Doubled information capacity per position |
| Structured mutation spectrum | Subclass errors more likely than class errors; transition/transversion-like bias | From energy hierarchy |
| Heritable variation preconditions | Identity-level differences can persist across rounds if fidelity is sufficient | Conditional |
| Zero additional cost | Geometric discrimination is free from existing shell structure | Seventh consecutive zero-cost upper-stack target |

| Non-Gain | Description | What would be needed |
|----------|------------|---------------------|
| Heredity | Cross-generation information transfer with selection | Reproduction + selection + fitness |
| Genetics | Genotype-phenotype mapping | Sequence → function (coding) |
| Evolution | Variation + selection + inheritance | Heredity + functional variation |
| Error correction | Proofreading or repair | Enzymatic/catalytic machinery |
| Coding (functional) | Sequence → structure → function | Folding + catalytic activity |
| Metabolism | Energy-converting cycles | Catalytic reaction networks |
| Cells | Compartmentalized systems | Membranes + transport |
| Life | Integrated self-maintaining system | All of the above |

---

## 13. Hard-Gated Summary Table

| Test | Verdict | Reason |
|------|---------|--------|
| Within-class distinctions physically present | **YES** | Bonding-site geometry, valence count, and steric profile differ between K=8/K=9 and K=6/K=7 |
| Higher-specificity pairing rule present | **YES (BRIDGE)** | D1↔A1, D2↔A2 from geometric complementarity; cross-class disfavored |
| Four-class pairing feasible | **YES** | Uses four primary monomer types with existing structural differences |
| Identity-level complement mapping present | **YES** | C₄ maps each of four types to a unique complement; C₄(C₄(S)) = S |
| Fidelity ceiling raised | **YES (CONDITIONAL)** | Raised from two-class to four-class; conditional on ΔE_mismatch being substantial |
| Identity-faithful copying plausible | **YES (CONDITIONAL)** | Four-class identity preserved across rounds if subclass errors are rare |
| Mutation/variation substrate present | **YES** | Four-type identity variation; structured mutation spectrum; heritable if fidelity sufficient |
| Zero-cost upper-stack continuation preserved | **YES** | Seventh consecutive zero-cost target; geometric discrimination is free |
| Heredity-precondition threshold crossed | **PARTIAL** | Identity-faithful replication preconditions met; heredity also requires reproduction + selection |
| Next-step heredity/lineage audit justified | **YES** | Four-class fidelity established; heredity question now structurally meaningful |

---

## 14. Nonclaims

1. NOT claiming heredity — heredity requires identity-faithful replication + reproduction + selection; only the first is structurally established.

2. NOT claiming genetics — no genotype-phenotype mapping, no genetic code, no gene concept; the four-class alphabet is a material pairing system, not a genetic system.

3. NOT claiming mutation-selection system — structured mutation exists but selection requires functional consequences of sequence variation, which are absent.

4. NOT claiming evolution — evolution requires heritable variation + selection + inheritance; only the variation substrate is established.

5. NOT claiming life — life requires coding + replication + metabolism + selection; only four-class replication preconditions are present.

6. NOT claiming metabolism — no energy-converting reaction cycles.

7. NOT claiming cells — no compartments, membranes, or transport.

8. NOT claiming observer/consciousness structure — entirely separate program.

---

## 15. Next-Step Recommendation

### Table 8 — Next-Route Decision Map

| Outcome | Recommended next document | Rationale |
|---------|--------------------------|-----------|
| **Fidelity ceiling raised to four-class (this outcome)** | **Heredity and Lineage Preconditions Audit** | Identity-faithful replication preconditions met; can sequence families persist across many rounds? Can lineages form? |
| Fidelity gain partial | Error-tolerance and fidelity bounds audit | Quantify ΔE_mismatch and determine operational fidelity |
| Fidelity ceiling unchanged | Catalysis / reaction-network audit | If fidelity cannot be raised, build richer chemistry instead |

### Recommended Next Document

**Heredity and Lineage Preconditions Audit.** With four-class identity-faithful replication structurally established, the next question is whether the system can support **persistent lineages** — families of sequences related by descent through replication, with heritable variation accumulated through mutation. This is the bridge from "information can be copied" to "information can be inherited."

The audit should determine:
1. Whether a sequence can persist through many replication rounds with identity-level fidelity.
2. Whether variant sequences (produced by subclass mutations) form distinguishable lineage branches.
3. Whether lineage persistence requires new structure or is a free consequence of four-class replication.
4. What minimum conditions would be needed for selection to act on lineage variation (the proto-Darwinian threshold).

This would be the audit that determines whether the architecture can support the transition from pre-biological organization to proto-biological heredity.

---

*Fidelity and Higher-Specificity Pairing Audit complete. Four-class pairing system established from bonding-site geometry at zero cost. Identity-level complement map: C₄(C₄(S)) = S for all four types. Fidelity ceiling raised from two-class to four-class. Structured mutation spectrum present. Seventh consecutive zero-cost upper-stack target. Heredity preconditions audit justified.*
