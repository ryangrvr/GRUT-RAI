# Book IV — Target Mu: Heredity and Lineage Preconditions Audit

## Formal Audit Document — Upper-Stack Heredity Gate

**Predecessor:** Book IV Target Lambda — Fidelity and Higher-Specificity Pairing Audit
**Function:** Determine whether four-class identity-faithful replication supports hereditary lineage persistence
**Gate:** Proto-Darwinian selection program entry decision

---

## 1. Executive Verdict

The four-class identity-faithful replication substrate supports **heredity and lineage preconditions** at bridge level, conditional on the geometric mismatch hierarchy ΔE_mismatch ≫ kT.

In the high-fidelity regime (subclass error rate p_sub ≪ 1/N for chain length N), identity-level sequences persist across many replication rounds. Variant sequences — produced by occasional subclass mutations during copying — form distinguishable lineage branches that diverge from a common ancestor and remain trackable through their accumulated differences. The system supports stable sequence families: clusters of closely related sequences descended from a common template, separated by a small number of mutations, and distinguishable from unrelated families by their shared sequence motifs.

The heredity/lineage-precondition threshold is crossed in the regime where:

**p_sub × N ≪ 1** (few errors per copied chain per round)

In this regime:
- A sequence persists with high identity through ~1/(p_sub × N) rounds before accumulating order-one errors.
- Variant branches formed by rare mutations persist as stable sub-lineages.
- Family structure (common-ancestor signals) survives noise for timescales set by the inverse mutation rate.
- The information dynamics is lineage-bearing: descent with modification, not random scrambling.

In the low-fidelity regime (p_sub × N ~ 1), errors accumulate per round at a rate comparable to the sequence length. Lineage identity degrades within a few rounds. The system is pre-hereditary in this regime — copying occurs but lineage information does not persist.

The boundary between these regimes is the **Eigen error threshold** applied at four-class level:

**N_max ~ 1/p_sub**

Chains shorter than N_max support hereditary persistence. Chains longer than N_max do not. This threshold is structural (it follows from the mathematics of copying with errors) and conditional (p_sub depends on ΔE_mismatch/kT, which is uncomputed).

The heredity/lineage threshold is therefore **crossed in the high-fidelity regime** and **blocked in the low-fidelity regime.** The architecture contains both regimes; which one is realized depends on the physical parameters. No new postulates are needed — the threshold crossing is a free consequence of the four-class pairing established in Target Lambda.

**Classification:** Bridge-level BSR. Heredity preconditions crossed conditionally. Eighth consecutive zero-cost upper-stack target. Proto-Darwinian selection preconditions audit justified.

---

## 2. Why Heredity/Lineage Are the Next Correct Gate

The fidelity audit raised the copying resolution from two classes to four classes, enabling identity-level sequence preservation through the complement cycle. But single-round fidelity does not guarantee heredity. Heredity requires that information survives through many rounds of copying — that a descendant many generations removed still carries recognizable ancestry from the original template.

The gap between "one accurate copy" and "persistent lineage" is the gap between a photocopy and a family tree. A photocopy degrades with each re-copying. A family tree persists because the copying fidelity is high enough relative to the information length that most of the original survives through many generations. The question is which regime the bridge architecture occupies.

---

## 3. What Counts as Heredity and Lineage Preconditions

### Table 1 — Heredity/Lineage Threshold Checklist

| Condition | Meaning | Required? |
|-----------|---------|----------|
| Multi-round identity retention | Same sequence (at identity level) recognizable after n rounds of copying | YES |
| Persistent inherited variants | Two sequences differing by a mutation remain distinguishable after further copying | YES |
| Lineage branching | One ancestor gives rise to multiple descendant families through copying + mutation | YES |
| Inherited difference survives noise | The signal (ancestry-derived sequence similarity) is stronger than the noise (accumulated errors) for many rounds | YES |
| Sequence-family structure | Groups of related sequences (same ancestor, shared motifs, divergent mutations) persist as identifiable families | YES |
| Structured mutation spectrum | Copy errors are biased (subclass > class) rather than uniformly random | Supporting (not strictly required) |

### What Does NOT Count

- **One or two accurate copies:** A system that makes a few faithful copies before degrading is a copying system, not a hereditary system. Heredity requires persistence across many rounds.
- **Transient identity retention:** If the sequence is recognizable after 3 rounds but randomized after 10, lineage persistence is too short for meaningful heredity.
- **Random drift destroying all distinction:** If all variant lineages converge to the same error-dominated distribution, there are no persistent families and no heredity.
- **Branching without stability:** If descendant branches are created by mutation but immediately scrambled by further errors, the branching is formal but not biologically meaningful.

---

## 4. Multi-Round Fidelity Audit

### 4.1 Error Accumulation Model

At four-class level, each copying round introduces errors at two rates:
- **Class errors:** rate p_class per position (D↔A confusion). Disfavored by primary donor-acceptor energy gap.
- **Subclass errors:** rate p_sub per position (D1↔D2 or A1↔A2 confusion). Disfavored by geometric mismatch penalty ΔE_mismatch.

For a chain of length N, the expected number of errors per round is:

**⟨errors/round⟩ = (p_class + p_sub) × N ≈ p_sub × N** (since p_sub > p_class generically)

### 4.2 Multi-Round Retention

After n rounds of copying (starting from one original template), the expected fraction of positions that retain their original identity is:

**f_retained(n) ≈ (1 − p_sub)^n ≈ exp(−p_sub × n)**

This fraction decreases exponentially with round number. The half-life (rounds until half the positions have changed) is:

**n_half ≈ ln(2) / p_sub ≈ 0.7 / p_sub**

For the sequence to be recognizable as descended from the original (rather than a random sequence), the retained fraction must remain above the baseline similarity of unrelated random sequences. For a four-class alphabet, two random sequences agree at ~25% of positions by chance. The sequence is recognizably ancestral as long as:

**f_retained(n) ≫ 0.25**

This gives a **lineage persistence timescale:**

**n_lineage ~ 1/p_sub** (rounds until ancestry becomes undetectable)

### Table 2 — Multi-Round Fidelity Outcomes

| Regime | Condition | Outcome | Preserved after n rounds |
|--------|-----------|---------|------------------------|
| **High fidelity** | p_sub × N ≪ 1 | Few errors per chain per round; identity persists for ~1/(p_sub × N) rounds | Identity-level sequence; lineage trackable |
| **Intermediate** | p_sub × N ~ 1 | ~1 error per chain per round; gradual divergence | Class-level mostly preserved; identity slowly degrading |
| **Low fidelity** | p_sub × N ≫ 1 | Many errors per round; identity lost rapidly | Only statistical features (composition) preserved |

### 4.3 Multi-Round Verdict

In the high-fidelity regime, identity-level information persists across many rounds. The lineage persistence timescale n_lineage ~ 1/p_sub can be large (many generations) if p_sub is small. The system supports multi-round identity retention in this regime. In the low-fidelity regime, it does not.

---

## 5. Variant Persistence Audit

### 5.1 How Variants Arise

A variant is a sequence that differs from its parent by one or more mutations (subclass substitutions). In the four-class system, the most common variants are **single-subclass substitutions:** one position changes from D1 to D2 (or vice versa within D class), or from A1 to A2 (or vice versa within A class).

### 5.2 Variant Stability

A variant sequence S' differs from the ancestral sequence S at one position. When S' is copied:
- At the mutated position: the new identity (say D2 instead of the ancestral D1) is faithfully copied (with probability 1 − p_sub). The mutation is inherited.
- At all other positions: the identity is faithfully copied (with probability 1 − p_sub each). No new mutations likely if p_sub × N ≪ 1.

Therefore: a single-mutation variant persists through copying with the same fidelity as the original. The mutation is **stably inherited** — it is not corrected (no error correction mechanism) and it is not amplified (each round introduces its own independent errors).

### 5.3 Distinguishability

Two sequences S and S' that differ at k positions remain distinguishable as long as the number of accumulated copying errors (noise) is much less than k. Since each round adds ~p_sub × N new errors, the variants remain distinguishable for:

**n_distinguish ~ k / (p_sub × N)** rounds

For k = 1 (single mutation), distinguishability persists for ~1/(p_sub × N) rounds — the same as the lineage persistence timescale. For k > 1 (multi-mutation variant), distinguishability persists proportionally longer.

### Table 3 — Variant Persistence Modes

| Mode | Present? | Implication |
|------|----------|------------|
| Single-mutation variant inheritable | **YES** | Mutations pass faithfully to descendants |
| Multi-mutation variant distinguishable | **YES** | Variants with more differences persist longer |
| Variant identity degrades over time | **YES** | Noise eventually overwhelms signal after n_lineage rounds |
| Variant reversion possible | **YES** | A subclass error can by chance revert a previous mutation |
| Stable variant families | **YES (high-fidelity regime)** | Families of related sequences persist for many rounds |

### 5.4 Variant Persistence Verdict

Variants are stably inherited. Single mutations persist through copying with the same fidelity as the original sequence. Variant families — groups of sequences related by small numbers of mutations — remain distinguishable from unrelated sequences for timescales set by the lineage persistence timescale. In the high-fidelity regime, variant persistence is robust.

---

## 6. Lineage Branching Audit

### 6.1 How Branching Occurs

Starting from one ancestral template S₀:
- Round 1: S₀ is copied. Most copies are faithful (S₀ again). Occasionally, a copy contains a mutation, producing a variant S₁.
- Round 2: Both S₀ and S₁ are copied. S₀ produces more S₀ copies (and occasionally new variants S₂, S₃, ...). S₁ produces S₁ copies (and occasionally further variants S₁₁, S₁₂, ...).
- Round n: A tree of descent forms, with S₀ at the root and variant branches diverging at each round.

### 6.2 Tree Structure

The branching rate (rate at which new variants appear per round) is:

**r_branch ~ p_sub × N per copied chain per round**

In the high-fidelity regime (p_sub × N ≪ 1), branching is rare per individual chain but inevitable across many copies. After n rounds of exponential amplification (2^n total chains), the expected number of distinct variant lineages is:

**⟨lineages⟩ ~ n × p_sub × N × 2^n / n ≈ p_sub × N × 2^n**

This grows exponentially with round number. The lineage tree is genuinely tree-like: a root (ancestral sequence), branches (mutational events), and leaves (current sequences). Branches that diverge earlier accumulate more differences and are more distantly related.

### 6.3 Ancestry Tracking

Two sequences from the same lineage tree share a common ancestor. Their shared ancestry is detectable through shared sequence motifs (positions that have not mutated since the common ancestor). The number of shared positions decreases with the number of rounds since their divergence. As long as:

**rounds since divergence < n_lineage ~ 1/p_sub**

the common ancestry is detectable above the random-similarity baseline.

### 6.4 Lineage Branching Verdict

Lineage branching is structurally present in the high-fidelity regime. A single ancestral sequence gives rise to a tree of descendants with heritable mutations. The tree structure is trackable through shared sequence motifs. Ancestry is detectable for timescales up to n_lineage ~ 1/p_sub. This is a genuine lineage-bearing system, not merely a copying system.

---

## 7. Inherited Difference vs Noise Audit

### 7.1 Signal and Noise in Sequence Space

**Signal:** The inherited difference between two sequences — the mutations accumulated since their last common ancestor. This signal is deterministic (each specific mutation is stably inherited) and grows linearly with divergence time.

**Noise:** The random errors accumulated during copying since the divergence. These errors are stochastic and also grow linearly with time (at rate p_sub × N per round).

### 7.2 The Signal-to-Noise Boundary

The inherited difference (signal) is distinguishable from noise when:

**inherited mutations ≫ noise-induced random similarity**

For two lineages that diverged t rounds ago:
- Inherited differences: ~2 × p_sub × N × t (each lineage accumulates mutations independently)
- Random noise similarity: ~0.25 × N (baseline for unrelated random four-class sequences)

The lineages are distinguishable as long as:

**2 × p_sub × N × t < (1 − 0.25) × N = 0.75 × N**

i.e., **t < 0.375 / p_sub**

This is comparable to n_lineage. The conclusion: inherited differences dominate over noise for ~1/(p_sub) rounds — the same timescale as lineage persistence.

### 7.3 The Heredity Regime

The architecture supports a clear heredity regime:

**p_sub × N ≪ 1 and t ≪ 1/p_sub**

In this regime:
- Individual sequences are faithfully inherited.
- Variants are stably distinct.
- Lineage trees are trackable.
- Inherited differences dominate noise.
- The system is hereditary in the structural sense.

Outside this regime (p_sub × N ≳ 1 or t ≳ 1/p_sub), the system degrades to noise-dominated copying and lineage information is lost.

### 7.4 Inherited Difference Verdict

Inherited difference dominates noise in the high-fidelity regime for timescales up to ~1/p_sub rounds. The heredity regime is bounded but real. The boundary is the Eigen threshold applied at the four-class identity level.

---

## 8. Proto-Mutation Structure Audit

### Table 5 — Proto-Mutation Structure

| Variation type | Source | Rate | Severity | Meaningful? |
|---------------|--------|------|----------|------------|
| **Subclass substitution (conservative)** | D1↔D2 or A1↔A2 within same class | p_sub per position per round | Low: preserves D/A class; changes only the specific monomer | **YES** — analogous to transition mutation |
| **Class substitution (radical)** | D↔A across class boundary | p_class per position per round (p_class ≪ p_sub) | High: changes the fundamental pairing class | **YES** — analogous to transversion mutation |
| **Insertion/deletion** | Gain or loss of a monomer during template-directed assembly | Not characterized (depends on growth kinetics) | Variable: shifts reading frame downstream | **OPEN** — not audited |
| **No mutation** | Faithful copying at four-class level | (1 − p_sub − p_class) per position per round | None | Faithful inheritance |

### 8.1 Transition/Transversion Analogy

The four-class system naturally produces a two-tier mutation spectrum:
- **Conservative (transition-like):** D1↔D2 or A1↔A2. Preserves the D/A pairing class. Changes only the specific monomer identity. Rate: p_sub.
- **Radical (transversion-like):** D↔A. Changes the fundamental pairing class. Disrupts complementarity at that position. Rate: p_class.

Since p_class ≪ p_sub (the donor-acceptor energy gap is larger than the geometric mismatch penalty), conservative mutations are much more common than radical mutations. This produces a structured, biased mutation spectrum — not flat random noise.

### 8.2 Mutation Structure Verdict

The proto-mutation structure is **genuine and structured.** Two tiers of mutation severity (conservative and radical) with different rates. The bias is a free consequence of the energy hierarchy in the pairing system. This structured variation is the substrate on which selection could in principle act (if functional consequences of sequence variation existed).

---

## 9. Sequence-Family Object Taxonomy

### Table 4 — Lineage Object Taxonomy

| Object type | Defining feature | Status |
|------------|-----------------|--------|
| **Ancestral template** | Original sequence from which a lineage descends | Established |
| **Faithful descendant** | Copy matching ancestor at all positions (within four-class resolution) | High probability per round in high-fidelity regime |
| **Near-variant descendant** | Copy differing from ancestor by 1–few subclass substitutions | Produced at rate ~p_sub × N per round per copy |
| **Branch family** | Group of descendants sharing a common mutation not present in the original ancestor | Formed when a variant is itself copied faithfully |
| **Distant-variant descendant** | Copy differing from ancestor by many substitutions; accumulated over many rounds | Typical after t ~ 1/(2 p_sub) rounds |
| **Convergent sequence** | Sequence from a different lineage that happens to resemble a given family by chance | Probability ~(1/4)^k for k shared specific positions; rare for long motifs |
| **Degraded descendant** | Copy with so many errors that ancestry is no longer detectable | Typical after t > n_lineage |
| **Noise-dominated population** | Collection of sequences where lineage information has been erased by accumulated errors | Outcome in low-fidelity regime or after very many rounds |
| **Extinct lineage** | Variant family that produced no further copies (by chance or by depletion) | Possible in finite-population dynamics |

---

## 10. Threshold Test

### Heredity/Lineage-Precondition Threshold

| Requirement | Met? | Condition |
|------------|------|-----------|
| Multi-round identity retention | **YES (CONDITIONAL)** | Requires p_sub × N ≪ 1; identity persists for ~1/(p_sub × N) rounds |
| Persistent inherited variants | **YES (CONDITIONAL)** | Single mutations stably inherited; families persist for ~1/p_sub rounds |
| Lineage branching | **YES** | Exponentially growing tree of descendants with heritable mutations |
| Inherited difference survives noise | **YES (CONDITIONAL)** | Signal dominates noise for t ≪ 1/p_sub rounds |
| Sequence-family structure | **YES (CONDITIONAL)** | Branch families distinguishable by shared motifs; trackable through ancestry |
| Structured mutation spectrum | **YES** | Two-tier (conservative/radical); biased by energy hierarchy |

**Heredity/lineage-precondition threshold: CROSSED in the high-fidelity regime (p_sub × N ≪ 1).**

The threshold is conditional on the same parameter hierarchy that has governed the entire upper stack: the geometric mismatch penalty ΔE_mismatch must be large enough relative to thermal energy that subclass errors are rare. If this condition holds, the architecture is hereditary. If it does not, the architecture is pre-hereditary (class-level copying only, no identity-level lineage).

---

## 11. Gains and Non-Gains

### Table 6 — Gains and Non-Gains

| Gain | Description | Status |
|------|------------|--------|
| Multi-round identity retention | Sequence identity persists across ~1/(p_sub × N) rounds | Conditional on high fidelity |
| Heritable variant production | Subclass mutations stably inherited by descendants | Structural consequence of copying + error |
| Lineage branching | Tree of descendants with trackable ancestry | Structural consequence of amplification + mutation |
| Branch-family persistence | Variant families remain distinguishable for ~1/p_sub rounds | Conditional on high fidelity |
| Structured mutation spectrum | Conservative (subclass) ≫ radical (class); biased, not random | Free from energy hierarchy |
| Hereditary regime identified | Bounded but real: p_sub × N ≪ 1 and t ≪ 1/p_sub | Structural + conditional |
| Lineage object taxonomy | 9 classified object types from ancestral template through extinct lineage | First pre-Darwinian taxonomy |
| Zero additional cost | Eighth consecutive zero-cost upper-stack target | Heredity is free from existing structure |

| Non-Gain | Description | What would be needed |
|----------|------------|---------------------|
| Darwinian selection | Differential reproduction based on functional advantage | Functional consequences of sequence variation |
| Adaptation | Directional change in sequence composition driven by fitness | Selection + variation + inheritance |
| Genetics | Genotype-phenotype mapping; genes; alleles | Coding (sequence → function) |
| Evolution | Open-ended increase in complexity and adaptation | Selection + heredity + ecological dynamics |
| Error correction | Proofreading or repair reducing p_sub | Enzymatic/catalytic machinery |
| Metabolism | Energy-converting reaction cycles | Catalytic networks |
| Cells | Compartmentalized self-maintaining systems | Membranes + transport |
| Life | Integrated self-replicating, metabolizing, evolving system | All of the above |
| Consciousness | Observer-state organization | Requires biology as prerequisite |

---

## 12. Cost Audit

### Table 7 — Cost/Accounting Impact

| Category | Pre-Mu total | Mu additions | Post-Mu total |
|----------|-------------|-------------|---------------|
| Extension postulates | 13 | **+0** | **13** |
| Free parameters | 6 | **+0** | **6** |
| Constrained/fixed params | 2 | **+0** | **2** |
| New spacetime fields | 1 | **+0** | **1** |
| New propagating DOF | 6 | **+0** | **6** |

**Heredity/lineage preconditions add zero cost.** Lineage branching, variant persistence, and family structure are free consequences of four-class identity-faithful replication (which was itself free from the matter + gauge bridge). This is the **eighth consecutive zero-cost upper-stack target.**

The complete accounting: the entire pipeline from chemistry-entry (Epsilon) through reaction grammar (Zeta) through biological information (Eta) through templating (Theta) through replication (Iota) through pre-biological capstone (Kappa) through fidelity upgrade (Lambda) through heredity preconditions (Mu) = **eight targets, zero new postulates.** The organizational richness of the upper stack is entirely mathematical consequence.

---

## 13. Hard-Gated Summary Table

| Test | Verdict | Reason |
|------|---------|--------|
| Multi-round identity retention plausible | **YES (CONDITIONAL)** | Persists for ~1/(p_sub × N) rounds in high-fidelity regime |
| Persistent inherited variants present | **YES (CONDITIONAL)** | Single mutations stably inherited; families persist for ~1/p_sub rounds |
| Lineage branching present | **YES** | Exponentially growing descent tree with heritable mutations |
| Inherited difference survives noise | **YES (CONDITIONAL)** | Signal dominates noise for t ≪ 1/p_sub in high-fidelity regime |
| Proto-mutation substrate present | **YES** | Two-tier structured spectrum (conservative ≫ radical) |
| Heredity/lineage-precondition threshold crossed | **YES (CONDITIONAL)** | Crossed in high-fidelity regime p_sub × N ≪ 1 |
| Zero-cost upper-stack continuation preserved | **YES** | Eighth consecutive zero-cost target |
| Selection preconditions justified | **PARTIAL** | Hereditary variation exists; functional consequences absent |
| Evolution justified | **NO** | Requires selection + adaptation + functional variation |
| Next-step selection/fidelity audit justified | **YES** | Heredity established; selection question is now structurally meaningful |

---

## 14. Nonclaims

1. NOT claiming genetics — no genotype-phenotype mapping, no genes, no alleles, no genetic code; the architecture provides heritable sequence families, not a genetic system.

2. NOT claiming Darwinian evolution — evolution requires selection + adaptation; only heritable variation is established; no functional consequences of sequence variation exist.

3. NOT claiming natural selection — selection requires differential reproduction based on functional advantage; no functional advantage has been demonstrated.

4. NOT claiming life — life requires coding + replication + metabolism + selection; only hereditary replication preconditions are present.

5. NOT claiming metabolism — no energy-converting reaction cycles.

6. NOT claiming cells — no compartments, membranes, or transport.

7. NOT claiming biology solved — the architecture provides the substrate for biology-like organization; biology itself is not derived.

8. NOT claiming observer/consciousness structure — entirely separate program; requires biology as prerequisite.

---

## 15. Next-Step Recommendation

### Table 8 — Next-Route Decision Map

| Outcome | Recommended next document | Rationale |
|---------|--------------------------|-----------|
| **Heredity threshold crossed conditionally (this outcome)** | **Proto-Darwinian Selection Preconditions Audit** | Hereditary variation exists; can differential success of variant lineages produce directional change? |
| Heredity conditional but weak | Error-tolerance and fidelity bounds audit | Quantify ΔE_mismatch and determine operational heredity |
| Heredity blocked | Catalysis / reaction-network audit | Build functional chemistry before attempting heredity |

### Recommended Next Document

**Proto-Darwinian Selection Preconditions Audit.** With hereditary variation structurally established, the next question is whether the system can support **differential lineage success** — the mechanism by which some variants proliferate more than others based on structural or functional properties.

The audit should determine:

1. Whether different sequences have different replication rates (sequence-dependent copying efficiency).
2. Whether different sequences have different stability (sequence-dependent degradation resistance).
3. Whether different sequences have different interaction properties (sequence-dependent binding, pairing, or catalytic behavior).
4. Whether any of these differences can produce differential lineage growth — the minimal condition for selection.
5. What minimum additional structure (if any) would be needed for selection to operate.

This is the audit that determines whether the architecture can support the transition from "heredity without purpose" to "heredity with differential success" — the most fundamental step in the origin of Darwinian dynamics.

---

*Heredity and Lineage Preconditions Audit complete. Four-class identity-faithful replication supports hereditary lineage persistence in the high-fidelity regime. Lineage branching, variant persistence, and family structure are structurally present. Structured two-tier mutation spectrum confirmed. Heredity threshold crossed conditionally on p_sub × N ≪ 1. Eighth consecutive zero-cost upper-stack target. The next step is a proto-Darwinian selection preconditions audit.*
