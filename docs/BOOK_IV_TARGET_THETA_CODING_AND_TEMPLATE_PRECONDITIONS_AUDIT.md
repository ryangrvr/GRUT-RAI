# Book IV — Target Theta: Coding and Template Preconditions Audit

## Formal Audit Document — Upper-Stack Gate

**Predecessor:** Book IV Target Eta — Biological Information Entry Architecture
**Function:** Determine whether the sequence-bearing substrate supports pairing, complementarity, and template-directed assembly
**Gate:** Replication/coding program entry decision

---

## 1. Executive Verdict

The bridge architecture's sequence-bearing substrate supports **selective pairing**, **complement-like relations**, and **template-directed growth** at the structural level. The coding/template-precondition threshold is crossed.

Selective pairing arises from the bonding grammar itself: different monomer types have different valence characters (s-valence, p-valence, lone pairs, directional bonds), and these characters create **preferential matching** — some monomer pairs bond more favorably than others due to orbital compatibility, orientation matching, and charge complementarity. This selectivity is not arbitrary; it is determined by the shell structure and bonding geometry of each composite type.

Complementarity emerges from the pairing specificity: when monomer type A bonds preferentially with monomer type B (rather than with itself or with C), the relation A↔B defines a primitive complement map. The architecture supports at least partial complementarity through the asymmetry of bonding characters: a monomer with a lone pair (electron-donor-like) bonds preferentially to a monomer with an empty bonding site (electron-acceptor-like). This donor-acceptor complementarity is structurally analogous to hydrogen-bonding specificity in nucleic acids, though far simpler.

Template-directed assembly follows: if a pre-existing chain exposes a sequence of bonding sites along its length, and if incoming monomers attach preferentially according to the pairing rules, then the pre-existing chain biases the sequence of the growing partner. The template chain's monomer ordering constrains the partner's ordering through local pairing specificity. This is not replication — the mechanism is primitive, error-prone, and lacks a separation/re-initiation cycle — but it is the structural precondition for replication: one sequence influencing the construction of another.

No coding system, no replication machinery, no heredity, no metabolism, and no life are obtained. The architecture provides the material preconditions for rule-based information transfer between chains, not the biological machinery that would exploit them.

**Classification:** Bridge-level BSR. Coding/template preconditions crossed. Replication preconditions audit justified.

---

## 2. Why Coding/Template Preconditions Are the Next Correct Gate

The biological information entry architecture established that the substrate can carry sequence information with exponential combinatorial diversity. But carrying information is not the same as transferring, reading, or copying it. A library of unique books is not a printing press.

The gap between information substrate and information processing requires:
1. Rules that determine how one sequence element interacts with another (pairing)
2. Systematic relations between sequence elements (complementarity)
3. A mechanism by which one sequence can guide the construction of another (templating)

These three capabilities — pairing, complementarity, templating — are the minimum preconditions for any information-transfer system. Without them, the sequence-bearing chains are passive storage, not active participants in information dynamics.

---

## 3. What Counts as Coding and Template Preconditions

### Table 1 — Coding/Template-Precondition Checklist

| Condition | Meaning | Required for coding? | Required for templating? |
|-----------|---------|---------------------|------------------------|
| Selective pairing | Some monomer pairs bond more favorably than others | YES | YES |
| Complement-like relation | Systematic A↔B mapping (not arbitrary) | YES | YES |
| Template-directed growth influence | Pre-existing chain biases partner construction | NO (for reading) | YES |
| Persistent matched complexes | Paired chain segments persist over relevant timescales | YES | YES |
| Sequence-to-sequence constraint | Ordering of one chain constrains ordering of another | YES | YES |
| Sequence-to-function mapping | Different sequences produce different functional behaviors | YES (for coding) | NO (for templating alone) |

### What Does NOT Count

- **Nonspecific aggregation:** Two chains sticking together without sequence-dependent selectivity is not pairing.
- **Generic bond preference without sequence dependence:** If all monomers bond equally to all others, there is no pairing specificity and no complementarity.
- **One-off matching without growth consequence:** A single paired monomer that does not influence subsequent additions is not templating.
- **Arbitrary chain association:** Two chains in proximity without sequence-constraining interaction is not template-directed assembly.

---

## 4. Pairing-Rule Audit

### 4.1 Source of Pairing Specificity

The bridge architecture's monomer types differ in their bonding characters:

| Monomer type | Valence character | Available bonding interactions | Pairing preference |
|-------------|------------------|------------------------------|-------------------|
| K=6 (1s² 2s² 2p²) | 2 unpaired p, 0 lone pairs | Two σ-bonds (backbone) | Bonds with other p-valence; no donor character |
| K=7 (1s² 2s² 2p³) | 3 unpaired p, 0 lone pairs | Three σ-bonds (branching) | Bonds with multiple partners; no donor character |
| K=8 (1s² 2s² 2p⁴) | 2 unpaired p, 1 lone pair | Two σ-bonds + 1 lone pair (donor) | **Donor-type:** lone pair available for secondary bonding |
| K=5 (1s² 2s² 2p¹) | 1 unpaired p, 0 lone pairs | One σ-bond (terminator) | Bonds with one partner only |
| K=9 (1s² 2s² 2p⁵) | 1 unpaired p, 2 lone pairs | One σ-bond + 2 lone pairs (strong donor) | **Strong donor-type:** excess lone pairs |
| K=4 (1s² 2s²) | 0 unpaired, 0 lone pairs (subclosed) | Weak or no bonding at leading order | Essentially inert at this level |

### 4.2 Donor-Acceptor Pairing

The key pairing asymmetry is between **donor-type** monomers (K=8, K=9 — carrying lone pairs) and **acceptor-type** monomers (K=6, K=7 — with empty or unsaturated bonding sites). A lone pair on one monomer can form a secondary (coordinate/dative) bond with an empty site on another, producing a directional, selective interaction.

This donor-acceptor pairing is **not the same** as the primary covalent-like backbone bonding. It is a secondary interaction — weaker than a covalent bond, but selective: donors pair preferentially with acceptors, not with other donors.

### 4.3 Pairing Selectivity

The pairing is selective because:
- Donor + acceptor: favorable (lone pair fills empty site; energy lowered)
- Donor + donor: unfavorable (no empty sites; lone-pair repulsion)
- Acceptor + acceptor: unfavorable (no lone pairs to donate; no secondary bond)
- Specific donor-acceptor pairs may have different bond strengths depending on orbital overlap geometry

This produces a primitive **pairing alphabet**: monomers are classified as donors (D) or acceptors (A), and the favorable pairing is D↔A.

### Table 2 — Candidate Pairing Rules

| Pair | Type | Specificity | Status |
|------|------|------------|--------|
| K=8 (donor) ↔ K=6 (acceptor) | D↔A | Selective: lone pair → empty site | **AVAILABLE** |
| K=8 (donor) ↔ K=7 (acceptor) | D↔A | Selective: lone pair → empty site | **AVAILABLE** |
| K=9 (strong donor) ↔ K=6 (acceptor) | D↔A | Selective: stronger donor | **AVAILABLE** |
| K=8 ↔ K=8 (donor-donor) | D↔D | Unfavorable: lone-pair repulsion | **DISFAVORED** |
| K=6 ↔ K=6 (acceptor-acceptor) | A↔A | Neutral: no secondary bond | **WEAK/ABSENT** |

### 4.4 Pairing-Rule Verdict

Selective pairing rules exist. Donor-type monomers (lone-pair carriers: K=8, K=9) pair preferentially with acceptor-type monomers (empty-site carriers: K=6, K=7). The selectivity is determined by the shell structure and bonding character of each composite. This is a genuine pairing alphabet with at least two classes (D and A) and selective D↔A matching.

---

## 5. Complementarity Audit

### 5.1 The Complement-Like Relation

The donor-acceptor pairing defines a **complement-like map**:

- D-type monomers (K=8, K=9) are the complement of A-type monomers (K=6, K=7)
- The relation is: D↔A (donors pair with acceptors)

This is a two-class complementarity. In real nucleic acids, the complementarity is four-class (A↔T, G↔C). The bridge architecture's two-class system is simpler but structurally genuine: it provides a rule that constrains which monomer can pair with which.

### Table 3 — Complementarity Structure

| Relation type | Present? | Mechanism | Caveat |
|--------------|----------|-----------|--------|
| D↔A two-class complementarity | **YES** | Donor lone pair pairs with acceptor empty site | Only two classes; less specific than A-T/G-C |
| Unique pairing (each type has exactly one complement) | **PARTIAL** | D pairs with any A; A pairs with any D | Within-class degeneracy: K=8 pairs with both K=6 and K=7 |
| Sequence-constraining complementarity | **YES** | A D-sequence constrains the partner to be an A-sequence | Ordering preserved: D₁D₂D₃ → A₁A₂A₃ (partner follows donor order) |
| Higher-specificity subclasses | **OPEN** | Different D-A pairs have different bond strengths/geometries | Could refine two-class into four-class with geometric discrimination |

### 5.2 Sequence-Level Complementarity

Consider a chain with sequence (D-A-D-D-A) along its backbone. If a partner chain grows alongside it, guided by D↔A pairing, the partner sequence is constrained to be (A-D-A-A-D) — the complement. The original chain's sequence determines the partner's sequence through local pairing rules.

This is **sequence-level complementarity**: the ordering information in one chain is transferred to another through the complement map. The transfer is imperfect (within-class degeneracy means K=8 and K=9 are both "D" and may not be distinguished by the pairing rule), but the ordering constraint is real.

### 5.3 Complementarity Verdict

Complement-like relations exist at the two-class level (D↔A). Sequence-level complementarity is present: a chain's monomer ordering constrains the partner chain's ordering through local pairing rules. The complementarity is less specific than real nucleic-acid base pairing (two classes vs four) but structurally genuine.

---

## 6. Template-Directed Assembly Audit

### 6.1 The Templating Mechanism

Template-directed assembly requires:
1. A pre-existing chain (the template) with an exposed sequence of monomer types
2. A pool of free monomers in solution
3. Local pairing rules that cause free monomers to attach to the template preferentially according to the complement map
4. Sequential addition: each monomer attaches next to the previous one, extending the partner chain along the template

### 6.2 Does the Architecture Support This?

**Step 1: Template exposure.** A sequence-bearing chain has monomers with secondary bonding sites (lone pairs or empty sites) exposed along its length. These sites are available for pairing with free monomers. The template is the chain itself; the exposed secondary sites are the reading surface.

**Step 2: Selective attachment.** Free monomers in the vicinity of the template preferentially attach to sites that match their pairing class. A free D-type monomer attaches to an exposed A-type site on the template; a free A-type monomer attaches to an exposed D-type site. The pairing selectivity from Section 4 governs this attachment.

**Step 3: Sequential growth.** Once a monomer attaches to the template at position n, the next position (n+1) on the template becomes the most favorable site for the next free monomer, because:
- The newly attached monomer partially blocks access to position n (steric effect)
- Position n+1 is the nearest unoccupied template site
- The growing partner chain's backbone bonding (covalent-like) connects monomer n to monomer n+1, directing growth along the template

**Step 4: Sequence transfer.** The partner chain, growing along the template, has a sequence determined by the template's complement: where the template has D, the partner has A, and vice versa. The template's ordering information is transferred to the partner through local pairing rules applied sequentially.

### 6.3 Quality of Templating

The templating is:
- **Sequence-directed:** The partner's ordering is constrained by the template's ordering
- **Local:** Each addition depends on the current template site, not on distant sites
- **Sequential:** Growth proceeds along the template direction
- **Error-prone:** Within-class degeneracy (K=8 and K=9 both serve as D) means the template cannot fully specify the partner's monomer identity — only its pairing class
- **Without separation/re-initiation:** The template and partner remain associated; no mechanism separates them for another round

### 6.4 Template-Directed Assembly Verdict

Template-directed assembly is **structurally available** at bridge level. A pre-existing chain can bias the construction of a partner chain through sequential application of local D↔A pairing rules. The partner's sequence is the complement of the template's sequence (at the two-class level). The mechanism is primitive and error-prone but genuine: it transfers ordering information from one material object to another through rule-based molecular-level interactions.

---

## 7. Stability vs Error Audit

### Table 5 — Stability and Error Conditions

| Condition | Met? | Why it matters |
|-----------|------|---------------|
| Persistent matched complexes | **YES (CONDITIONAL)** | Template-partner duplex persists if secondary bonds persist; requires bond energy > thermal/dissipative scale | Template reading requires contact time |
| Tolerable mismatch handling | **YES** | A D-monomer at an A-site is unfavorable but not catastrophic; chain growth can continue past errors | Error tolerance allows imperfect but functional templating |
| Reversible attachment regime | **STRUCTURAL** | Secondary (donor-acceptor) bonds are weaker than primary (covalent-like) bonds; can break and reform | Allows error correction through re-annealing |
| Error rate | **UNKNOWN** | Depends on pairing specificity, monomer concentrations, and kinetic vs thermodynamic control | Not computed; structural estimate only |
| Error correction mechanism | **NO** | No proofreading, no enzymatic repair; errors persist once incorporated into covalent backbone | Limits fidelity of information transfer |

### 7.1 The Error Regime

The two-class complementarity (D↔A) provides selectivity but not specificity within each class. Errors of two types are expected:

- **Class errors:** An A-type monomer attaches where a D-type should (wrong class). These are disfavored by the pairing energy but not forbidden. Rate depends on the D↔A energy gap relative to thermal energy.
- **Identity errors:** The correct class (D) attaches but the wrong specific monomer (K=8 instead of K=9). These are not discriminated by the two-class pairing rule at all.

The error rate for class errors is parameter-dependent. The error rate for identity errors is structurally high (no discrimination mechanism within each class). A higher-specificity pairing system (four-class or more) would reduce identity errors but requires additional structural features not yet present.

### 7.2 Stability-Error Balance

The architecture sits in a regime where:
- Primary (covalent-like) bonds are strong → chain backbone is stable
- Secondary (donor-acceptor) bonds are weaker → template-partner association is reversible
- The hierarchy (strong backbone, weak pairing) is the correct structure for template-directed assembly: the chain persists while the pairing can anneal

This is structurally analogous to the hierarchy in nucleic acids: strong phosphodiester backbone + weak hydrogen-bonded base pairing.

---

## 8. Coding-Precondition Audit

### 8.1 What Coding Would Require

A coding system maps sequences to functions: a specific monomer ordering produces a specific structural or behavioral output. In biology, the genetic code maps triplet codons to amino acids; the amino acid sequence determines protein fold and function.

### 8.2 Does the Architecture Support Coding Preconditions?

| Coding requirement | Status |
|-------------------|--------|
| Distinguishable symbols | **YES** — multiple monomer types with distinct bonding characters |
| Reproducible pairing/mapping | **YES** — D↔A pairing is reproducible and rule-based |
| Ordered substrate | **YES** — sequence-bearing chains with position-specific ordering |
| Constrained output from input sequence | **YES** — template-directed assembly constrains partner sequence |
| Nontrivial relation between sequences | **YES** — complementarity (D↔A map) relates template to product |
| Sequence-to-structure mapping | **PARTIAL** — different sequences produce different chain geometries (branch patterns, directionality); but no analogue of protein folding |
| Sequence-to-function mapping | **NO** — no demonstrated functional output from sequence; no catalysis, no regulation |

### 8.3 Coding-Precondition Verdict

The architecture supports coding preconditions at the structural level: distinguishable symbols, reproducible pairing, ordered substrate, and sequence-constrained output. What it lacks is the functional layer: a mapping from sequence to behavior (catalysis, regulation, structural function). The bridge architecture has the substrate for coding but not the semantics.

The threshold for **template preconditions** is fully crossed. The threshold for **coding preconditions** is partially crossed (substrate and pairing present; function absent).

---

## 9. Template-Complex Object Taxonomy

### Table 4 — Template-Complex Object Taxonomy

| Object type | Defining feature | Status |
|------------|-----------------|--------|
| **Free single chain** | Sequence-bearing heteropolymer; no partner | Established (Target Zeta) |
| **Paired segment** | Two chains locally matched via D↔A secondary bonds | **AVAILABLE** — local pairing produces short matched regions |
| **Extended duplex** | Two complementary chains fully matched along their length | **AVAILABLE** — sequential pairing along full template produces duplex |
| **Partially templated intermediate** | Growing partner chain partially assembled on template | **AVAILABLE** — intermediate state of template-directed assembly |
| **Mismatched complex** | Two chains paired with errors (wrong-class or wrong-identity monomers) | **EXPECTED** — error-prone templating produces imperfect duplexes |
| **Separated product** | Partner chain released from template after assembly | **OPEN** — no separation mechanism demonstrated; duplex may persist |
| **Inert closed-shell composite** | Does not participate in pairing or templating | Established (K=2, K=10 etc.) |

### 9.1 The Duplex as Information Object

The extended duplex — two complementary chains matched along their length via D↔A pairing — is the first **two-chain information object** in the architecture. It carries the same sequence information as each individual chain (one is the complement of the other), but in a paired, stabilized form. The duplex is structurally analogous to double-stranded DNA, though far simpler (two-class pairing vs four-class, no helical twist, no specific backbone chemistry).

The duplex is also the first object that demonstrates **information redundancy**: the same sequence information is stored in two physically distinct chains. If one chain is damaged, the other retains the information. This is the structural precondition for error-tolerant information storage.

---

## 10. Threshold Test

### Coding/Template-Precondition Threshold

| Requirement | Met? | Evidence |
|------------|------|---------|
| Selective pairing | **YES** | D↔A donor-acceptor matching from shell/bonding character |
| Complement-like relation | **YES** | Two-class complementarity; D↔A map |
| Template-directed influence on growth | **YES** | Pre-existing chain biases partner assembly through sequential local pairing |
| Persistent matched complex formation | **YES (CONDITIONAL)** | Secondary bonds persist if energy > thermal/dissipative scale |
| Sequence-to-sequence constraint | **YES** | Template ordering constrains partner ordering through complement map |
| Sequence-to-function mapping | **NO** | No demonstrated functional output from sequence |

**Template-precondition threshold: CROSSED.**
**Coding-precondition threshold: PARTIALLY CROSSED** (substrate and pairing present; functional layer absent).

---

## 11. Gains and Non-Gains

### Table 6 — Gains and Non-Gains

| Gain | Description | Status |
|------|------------|--------|
| First pairing alphabet | D/A two-class system from donor-acceptor bonding character | Bridge-level |
| First complement-like relation | D↔A map constraining partner sequence | Bridge-level |
| First template-directed assembly | Pre-existing chain guides partner construction through sequential pairing | Bridge-level; error-prone |
| First duplex information object | Two complementary chains matched along their length | Bridge-level |
| First information redundancy | Same sequence stored in two physical chains | Structural consequence of duplexing |
| Template-precondition threshold crossed | All five template requirements met | Bridge-level |
| Coding preconditions partially crossed | Substrate and pairing present; function absent | Partial |
| Replication-preconditions audit justified | Template-directed assembly exists; separation and re-initiation next | YES |

| Non-Gain | Description | What would be needed |
|----------|------------|---------------------|
| DNA / RNA | Specific nucleotide chemistry | SM-specific molecular realization |
| Real base pairing | A-T / G-C four-class specificity | Higher-specificity pairing system |
| Coding (sequence → function) | No functional output from sequence | Catalytic or structural function of chains |
| Replication | No separation/re-initiation cycle | Strand separation + template re-use |
| Heredity | No cross-generation information transfer | Replication + selection |
| Translation | No sequence → structure → function pipeline | Folding + catalysis |
| Metabolism | No energy-converting reaction cycles | Catalytic reaction networks |
| Cells | No compartments | Membrane-like structures |
| Life | None of the above | All of the above |
| Error correction | No proofreading or repair | Enzymatic machinery |

---

## 12. Hard-Gated Summary Table

| Test | Verdict | Reason |
|------|---------|--------|
| Selective pairing present | **YES (BRIDGE)** | D↔A donor-acceptor matching from shell/bonding characters |
| Complement-like relation present | **YES** | Two-class complementarity; D↔A map constrains partner sequence |
| Template-directed growth present | **YES (BRIDGE)** | Sequential local pairing guides partner assembly along template |
| Persistent matched complexes present | **YES (CONDITIONAL)** | Secondary bonds persist above thermal/dissipative threshold |
| Sequence-to-sequence constraint present | **YES** | Template ordering → partner ordering through complement map |
| Coding/template-precondition threshold crossed | **YES (template) / PARTIAL (coding)** | Template fully crossed; coding lacks functional layer |
| Replication justified | **NO** | No separation/re-initiation; no copying cycle |
| Heredity justified | **NO** | No cross-generation transfer |
| Biology justified | **NO** | No replication + metabolism + selection |
| Next-step replication-preconditions audit justified | **YES** | Template exists; the question of strand separation and re-use is now meaningful |

---

## 13. Nonclaims

1. NOT claiming DNA — no nucleotide bases, no double helix geometry, no phosphodiester backbone, no A-T/G-C specificity; the architecture provides two-class complementary chains, not nucleic acids.

2. NOT claiming RNA — no ribose, no nucleotides, no catalytic RNA, no ribosomal translation.

3. NOT claiming real base pairing — the D↔A two-class system is structurally analogous to base pairing but far less specific; within-class identity errors are not discriminated.

4. NOT claiming coding — no sequence-to-function mapping exists; the architecture provides a substrate for coding but not the semantic content.

5. NOT claiming replication — template-directed assembly exists but no strand-separation or re-initiation cycle; one template produces one partner, then they remain associated.

6. NOT claiming heredity — no information transfer across generations; no offspring, no lineage, no selection.

7. NOT claiming metabolism — no energy-converting reaction networks, no catalytic cycles.

8. NOT claiming life — life requires coding + replication + metabolism + selection; none present.

9. NOT claiming evolution — no variation + selection + inheritance mechanism.

10. NOT claiming observer/consciousness — entirely separate program chain.

---

## 14. Next-Step Recommendation

### Table 7 — Next-Route Decision Map

| Outcome | Recommended next document | Rationale |
|---------|--------------------------|-----------|
| **Template threshold crossed (this outcome)** | **Replication Preconditions Audit** | Template-directed assembly exists; can strand separation and re-use be achieved? |
| Template partial | Pairing specificity deepening audit | Strengthen the pairing system before attempting replication |
| Template blocked | Reaction network / catalysis audit | Build richer chemistry before attempting information transfer |

### Recommended Next Document

**Replication Preconditions Audit.** This document should determine:

1. Whether the template-partner duplex can be separated (strand separation).
2. Whether a separated template can serve as a template again (template re-use / cycling).
3. Whether the complement of a complement recovers the original sequence (C(C(S)) = S, the fundamental property of faithful replication).
4. What minimum additional mechanism (if any) would be needed for a complete copy cycle.
5. Whether the architecture can support exponential copying (one template → two duplexes → four → ...).

This is the audit that determines whether the information-transfer substrate can become an information-copying system — the single most consequential step between chemistry and biology.

---

*Coding and Template Preconditions Audit complete. Selective pairing (D↔A) established. Two-class complementarity confirmed. Template-directed assembly demonstrated structurally. Duplex information objects available. Template-precondition threshold crossed. Coding preconditions partially crossed (substrate present, function absent). The next step is a replication preconditions audit: can the template system cycle?*
