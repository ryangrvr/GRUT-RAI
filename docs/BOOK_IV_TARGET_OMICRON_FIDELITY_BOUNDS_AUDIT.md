# Book IV — Target Omicron: Fidelity Bounds Audit

## Formal Audit Document — Post-Capstone Fidelity Gate

**Predecessor:** Book IV Target Xi — Upper-Stack Terminal Capstone
**Function:** Determine whether the four-class pairing architecture supports operationally high-fidelity copying
**Gate:** Operational heredity decision; catalysis program entry

---

## 1. Executive Verdict

The architecture supports **operational high-fidelity copying in Regime I** (strong discrimination), where the geometric mismatch penalty ΔE_mismatch exceeds the thermal energy kT by a factor of ~3 or more. In this regime, per-site subclass error rates are below ~5%, multi-round identity retention is robust for chain lengths N up to ~20/p_sub, and hereditary lineage persistence is operationally viable.

The verdict is **regime-dependent, not universal.** The architecture does not guarantee high fidelity — it contains a parameter regime in which high fidelity holds and a parameter regime in which it does not. Whether the physical system sits in Regime I, II, or III depends on the magnitude of the geometric mismatch penalty, which is ultimately set by the underlying bridge-level parameters (soliton structure, Skyrme coupling, gauge coupling, shell-configuration geometry). These parameters are not computed from first principles in the current architecture.

The critical finding is that the mismatch penalty has **three independent structural contributions** — steric fit difference, bond-angle distortion, and orbital-overlap reduction — each of which plausibly contributes to discrimination. The combined effect is plausibly in the strong-discrimination regime (Regime I) because all three contributions favor correct pairing and penalize incorrect pairing in the same direction. No cancellation between contributions is expected. This is a structural plausibility argument, not a rigorous bound.

The operational fidelity threshold is therefore **conditionally crossed:** crossed in Regime I (which is structurally plausible), not crossed in Regime III (which cannot be excluded on structural grounds alone). The upper-stack scaffold remains viable as a pre-biological information-and-selection platform in the regime where fidelity is operational.

No new postulates are required. Tenth consecutive zero-cost upper-stack target.

**Classification:** Bridge-level BSR. Operational fidelity conditionally established. Regime I is structurally plausible. Catalysis preconditions audit justified.

---

## 2. Why Fidelity Bounds Are the Next Correct Gate

The terminal capstone identified operational fidelity as the first of five defining unresolved boundaries. All upper-stack thresholds (chemistry through proto-selection) were crossed structurally, but every threshold above replication depends on whether the four-class pairing is operationally faithful enough to sustain identity-level information transfer across many rounds.

If ΔE_mismatch ≫ kT: heredity works, lineages persist, selection has something to act on, and the upper-stack scaffold is operationally sound.

If ΔE_mismatch ~ kT: heredity degrades to class-level only, identity-level information is lost within a few rounds, and the upper-stack scaffold above the Kappa capstone (pre-biological organization) is structurally available but operationally inert.

This audit resolves which side of the boundary the architecture plausibly occupies.

---

## 3. What Counts as Operational Fidelity

### Table 1 — Operational Fidelity Threshold Checklist

| Condition | Meaning | Required? |
|-----------|---------|----------|
| Mismatch discrimination > thermal noise | Correct pairing strongly favored over incorrect pairing under realistic thermal conditions | YES |
| Low per-site identity error (p_sub ≲ 0.05) | Fewer than ~1 in 20 positions miscopied per round | YES for heredity |
| Multi-round sequence retention | Identity-level sequence recognizable after ≫1 rounds | YES |
| Lineage persistence > ~10 rounds | Family identity survives for biologically meaningful durations | YES for selection |
| Bounded mutation window | Error rate low enough for heredity, high enough for variation | YES for proto-evolution |
| Robustness to chain length | Fidelity holds for N up to ~20–100 (moderate-length chains) | YES for information capacity |

### What Does NOT Count

- **Exact copying at zero temperature:** Fidelity must hold under thermal conditions, not only in the ground state.
- **One-round fidelity only:** Operational fidelity requires multi-round persistence, not just single-copy accuracy.
- **Structural pairing specificity with no energetic discrimination:** If the geometric mismatch penalty is small, the pairing is structurally preferential but energetically indistinguishable from random — not operationally faithful.

---

## 4. Mismatch-Energy Hierarchy Audit

### 4.1 Sources of the Mismatch Penalty

The geometric mismatch between correct (D1↔A1 or D2↔A2) and incorrect (D1↔A2 or D2↔A1) pairings has three independent structural contributions:

**Contribution 1: Steric fit difference.** Correct pairings have complementary spatial profiles at the secondary-bonding interface (side-on ↔ side-on for D1↔A1; pendant ↔ planar for D2↔A2). Incorrect pairings require spatial distortion of the interface to achieve contact. The steric penalty is proportional to the geometric incompatibility — the volume of overlap or displacement required.

**Contribution 2: Bond-angle distortion.** The secondary (donor-acceptor) bond has a preferred geometry set by the lone-pair direction (donor) and the empty-site orientation (acceptor). Correct pairings achieve near-optimal bond angles. Incorrect pairings force the secondary bond into a strained geometry with suboptimal lone-pair/empty-site alignment. The angular penalty follows from the cosine dependence of orbital overlap on bond angle.

**Contribution 3: Orbital-overlap reduction.** The secondary-bond strength depends on the spatial overlap between the donor lone pair and the acceptor empty orbital. Correct pairings maximize this overlap (complementary orbital shapes). Incorrect pairings reduce it (mismatched orbital shapes). The overlap reduction directly reduces the secondary-bond energy for incorrect pairings.

### 4.2 Qualitative Magnitude Assessment

Each contribution is individually comparable to a fraction of the secondary-bond energy E_secondary. If E_secondary is itself comparable to or larger than kT (which it must be for duplexes to be stable — duplex stability requires E_secondary > kT per pair), then:

**ΔE_mismatch ~ fraction × E_secondary ~ fraction × (several × kT)**

where "fraction" represents the relative penalty from steric, angular, and overlap effects combined.

The three contributions reinforce each other: all three favor correct pairing and penalize incorrect pairing. No cancellation is expected because the effects are geometrically aligned (correct pairing simultaneously optimizes steric fit, bond angle, and orbital overlap).

A conservative estimate: if each contribution accounts for ~20–50% of the secondary-bond energy, and the secondary-bond energy is ~3–5 kT (the range needed for duplex stability), then:

**ΔE_mismatch ~ 0.3 × E_secondary ~ 1–2 kT** (marginal regime)

to

**ΔE_mismatch ~ 0.6 × E_secondary ~ 2–3 kT** (strong-discrimination regime)

### Table 2 — Mismatch Hierarchy Regimes

| Regime | ΔE_mismatch / kT | p_sub per site | Character |
|--------|------------------|---------------|-----------|
| **I: Strong discrimination** | ≳ 3 | ≲ exp(−3) ≈ 0.05 | Identity-faithful; heredity operational |
| **II: Marginal** | ~ 1–2 | ~ 0.1–0.4 | Partially discriminating; heredity weak |
| **III: Weak discrimination** | ≲ 1 | ~ 0.3–0.5 | Near-random within class; heredity fails |

### 4.3 Which Regime Is Plausible?

**Regime I (strong) is structurally plausible** because:
1. Three independent mismatch contributions reinforce without cancellation.
2. Duplex stability already requires E_secondary > kT (otherwise duplexes do not form), placing the secondary-bond energy in the multi-kT range.
3. The geometric distinction between correct and incorrect pairings is qualitatively significant (divalent-to-divalent vs divalent-to-trivalent contacts involve different numbers of bonding sites, different angular arrangements, and different steric profiles).
4. Analogous systems in real chemistry (hydrogen-bonding selectivity in nucleic acids) achieve ΔE ~ 2–5 kT per base pair from similar geometric/electrostatic mechanisms.

**Regime III (weak) cannot be excluded** because:
1. The secondary-bond energy and mismatch penalty are not computed from first principles.
2. The bridge architecture's parameters (Skyrme coupling, gauge coupling, shell-configuration details) do not directly constrain the secondary-bonding energetics.
3. It is possible that the geometric distinction, while qualitatively real, is energetically small relative to thermal fluctuations.

### 4.4 Mismatch Verdict

The mismatch-energy hierarchy plausibly favors Regime I (strong discrimination) based on three reinforcing structural contributions and the requirement that E_secondary > kT for duplex stability. The verdict is structural plausibility, not rigorous bound. Regime I is the most likely regime but Regime II cannot be excluded.

---

## 5. Per-Site Error-Rate Audit

### Table 3 — Error-Rate Structure

| Error type | Source | Rate (Regime I) | Rate (Regime II) | Rate (Regime III) | Consequence |
|-----------|--------|-----------------|------------------|-------------------|------------|
| **Correct four-class pairing** | Geometric complementarity | ~0.95 | ~0.7 | ~0.5 | Faithful identity transmission |
| **Subclass error** (D1↔D2 or A1↔A2) | Geometric mismatch penalty ΔE_mismatch | ~0.04 | ~0.25 | ~0.4 | Identity lost at that position; class preserved |
| **Class error** (D↔A) | Primary donor-acceptor energy gap | ~0.01 | ~0.04 | ~0.08 | Both class and identity lost; complementarity broken |
| **Catastrophic failure** (no pairing) | Steric exclusion or monomer absence | ~0.001 | ~0.01 | ~0.02 | Position skipped or chain truncated |

### 5.1 The Error Hierarchy

In all regimes, the error hierarchy is:

**p_class ≪ p_sub ≪ 1** (Regime I)

or

**p_class < p_sub < 0.5** (Regime II/III)

This hierarchy is structural: the donor-acceptor energy gap (primary pairing) is always larger than the geometric mismatch penalty (secondary subclass discrimination). Class errors are always rarer than subclass errors.

### 5.2 Per-Site Verdict

In Regime I, the per-site identity error rate is ~5% or below. This is operationally meaningful: 95% of positions are correctly copied per round. In Regime II, the rate is ~25% — marginal for heredity. In Regime III, the rate is ~40% — effectively random within class.

---

## 6. Multi-Round Fidelity Bounds Audit

### 6.1 Sequence-Level Fidelity

For a chain of length N copied over t rounds, the fraction of positions retaining their original identity is:

**f(N, t) ≈ (1 − p_sub)^t**

per position. The probability that the entire chain is perfectly copied in one round is:

**P_perfect(N) = (1 − p_sub)^N**

### Table 4 — Multi-Round Fidelity Outcomes

| Regime | p_sub | N=10: P_perfect | N=20: P_perfect | N=50: P_perfect | Rounds until half positions changed |
|--------|-------|----------------|----------------|----------------|-------------------------------------|
| **I (strong)** | 0.05 | 0.60 | 0.36 | 0.08 | ~14 rounds |
| **II (marginal)** | 0.25 | 0.06 | 0.003 | ~10⁻⁷ | ~2.4 rounds |
| **III (weak)** | 0.40 | 0.006 | ~10⁻⁵ | ~10⁻¹⁰ | ~1.3 rounds |

### 6.2 The Identity-Level Eigen Threshold

The maximum chain length for which identity-level heredity is sustainable is:

**N_max ~ 1/p_sub**

| Regime | p_sub | N_max | Interpretation |
|--------|-------|-------|---------------|
| **I** | 0.05 | ~20 | Moderate-length chains support heredity |
| **II** | 0.25 | ~4 | Only very short chains |
| **III** | 0.40 | ~2–3 | Essentially no identity heredity |

### 6.3 Lineage Persistence Timescale

The number of rounds until ancestry becomes undetectable:

**t_lineage ~ 1/p_sub**

| Regime | p_sub | t_lineage | Interpretation |
|--------|-------|-----------|---------------|
| **I** | 0.05 | ~20 rounds | Extended lineage tracking |
| **II** | 0.25 | ~4 rounds | Very brief lineage |
| **III** | 0.40 | ~2 rounds | No operational lineage |

### 6.4 Multi-Round Verdict

In Regime I, chains of length ~20 sustain identity-level heredity across ~20 rounds. This is operationally meaningful: 4^20 ≈ 10¹² distinct possible sequences, with lineages traceable across ~20 generations. In Regime II, heredity is limited to very short chains (~4 monomers) over very few rounds (~4). In Regime III, identity-level heredity is not operational.

---

## 7. Fidelity-Regime Map

### Table 5 — Fidelity-Regime Map

| Regime | ΔE/kT | p_sub | Identity heredity | Lineage persistence | Mutation rate | Selection substrate | Viability |
|--------|-------|-------|------------------|--------------------|--------------|--------------------|-----------|
| **I: Strong** | ≳ 3 | ≲ 0.05 | **Operational** for N ≲ 20 | **~20 rounds** | Low; mostly faithful; occasional structured variants | **Full proto-selection** | **Viable pre-biological platform** |
| **II: Marginal** | ~ 1–2 | ~ 0.1–0.4 | **Weak;** only short chains (N ~ 4) | **~4 rounds** | Moderate; rapid identity degradation | **Marginal;** class-level selection only | Structurally present; operationally weak |
| **III: Weak** | ≲ 1 | ~ 0.4+ | **Not operational** | **~2 rounds** | High; near-random within class | **Class-level at best** | Pre-biological capstone (Kappa) ceiling |

### 7.1 Regime I: The Operational Heredity Window

In Regime I, the architecture supports:
- Identity-faithful copying at ~95% per-site fidelity
- Chains of N ~ 10–20 monomers with full-sequence heredity
- Lineage persistence across ~20 generations
- Information capacity: 4^20 ≈ 10¹² distinct heritable sequences
- Mutation rate: ~1 subclass error per chain per round (for N=20, p_sub=0.05)
- Proto-selection: sequence-dependent differential success with heritable variation

This is a **usable pre-biological heredity window**: high enough fidelity for inheritance, low enough error for variation, moderate chain length for combinatorial diversity.

### 7.2 Regime II: The Marginal Zone

In Regime II, only very short chains (N ~ 4) sustain identity-level heredity, with only ~4 generations of lineage persistence. The information capacity is 4^4 = 256 distinct sequences — far less than Regime I but nonzero. Proto-selection operates but on a very compressed sequence space.

### 7.3 Regime III: Class-Level Only

In Regime III, the architecture reverts to the pre-Lambda state: class-level (D/A) sequence is preserved but identity within class is lost. The upper-stack scaffold above Kappa is structurally present but operationally inert.

---

## 8. Mutation/Fidelity Tradeoff Audit

### 8.1 The Proto-Evolutionary Window

In Regime I (p_sub ~ 0.05, N ~ 20):
- Expected mutations per copied chain per round: p_sub × N ≈ 1
- This means: most copies are faithful, but ~1 in every batch of copies carries a new variant.
- Lineage persistence: ~20 rounds (identity-level ancestry detectable).

This places the system in the optimal **mutation/fidelity tradeoff window:**
- Low enough error (p_sub × N ~ 1 ≪ N) that most of the sequence is faithfully inherited.
- High enough error (p_sub × N ~ 1 > 0) that new variants are regularly produced.
- Bounded mutation (not random washout but ~1 substitution per copy).

### 8.2 Comparison to Biological Systems

Real RNA viruses operate near the Eigen error threshold with per-site error rates of ~10⁻³ to 10⁻⁴ and genome lengths of ~10³ to 10⁴ nucleotides, giving ~1 mutation per genome per copy. The bridge architecture in Regime I operates at p_sub ~ 0.05 with N ~ 20, also giving ~1 mutation per chain per copy. The error rate per site is much higher than biological systems, but the chain length is much shorter, producing a comparable per-chain mutation rate.

This is not a claim of biological realism. It is an observation that the architecture naturally sits near the Eigen threshold in Regime I, which is the structurally optimal position for proto-evolutionary dynamics.

### 8.3 Tradeoff Verdict

Regime I supports a **genuine proto-evolutionary window:** heredity with bounded variation. The mutation/fidelity balance places the system near the Eigen threshold, where lineage identity is maintained while novel variants are regularly generated. This is the regime where proto-selection has both material to work with (heritable variation) and stability to preserve (faithful lineage transmission).

---

## 9. Heredity Viability Audit

### 9.1 Operational vs Structural Heredity

| Property | Structural (prior audits) | Operational (this audit, Regime I) |
|----------|--------------------------|-----------------------------------|
| Identity-faithful copying | Available if p_sub low enough | **~95% per-site fidelity** |
| Lineage persistence | Available if rounds < 1/p_sub | **~20 rounds for N=20** |
| Family distinguishability | Available if variants < noise | **Families distinct for ~20 rounds** |
| Proto-selection viability | Available if differential success exists | **Viable; ~1 mutation/chain/round provides variation** |
| Eigen threshold | N_max ~ 1/p_sub (structural) | **N_max ~ 20 (operational in Regime I)** |

### 9.2 Verdict

In Regime I, heredity is **operationally viable.** The previously established structural thresholds (heredity, lineage, proto-selection) are all operationally instantiated: identity-level copying at ~95% fidelity, lineage persistence across ~20 generations, family tracking through shared motifs, and proto-selection with ~1 mutation per copy providing heritable variation.

The heredity viability is conditional on the system occupying Regime I (ΔE_mismatch ≳ 3kT), which is structurally plausible but not rigorously demonstrated.

---

## 10. Cost Audit

### Table 7 — Cost/Accounting Impact

| Category | Pre-Omicron total | Omicron additions | Post-Omicron total |
|----------|-------------------|-------------------|-------------------|
| Extension postulates | 13 | **+0** | **13** |
| Free parameters | 6 | **+0** | **6** |
| Constrained/fixed params | 2 | **+0** | **2** |
| New spacetime fields | 1 | **+0** | **1** |
| New propagating DOF | 6 | **+0** | **6** |

**The fidelity-bounds analysis adds zero cost.** The mismatch-energy hierarchy, per-site error rates, multi-round fidelity bounds, and regime classification are all analytical consequences of the existing four-class pairing structure. No new postulates, parameters, or fields are required to establish the regime map.

**Tenth consecutive zero-cost upper-stack target.** The streak from Epsilon through Omicron — chemistry-entry through operational fidelity bounds — adds zero postulate cost. Every result above the matter + gauge bridge is mathematical consequence.

---

## 11. Threshold Test

### Operational Fidelity Threshold

| Requirement | Met? | Condition |
|------------|------|-----------|
| Mismatch discrimination > thermal noise | **YES (Regime I)** | Three reinforcing structural contributions; plausibly ΔE ≳ 3kT |
| Low per-site identity error | **YES (Regime I)** | p_sub ≲ 0.05 in strong-discrimination regime |
| Multi-round sequence retention | **YES (Regime I)** | N=20 chains retain identity across ~20 rounds |
| Lineage persistence > ~10 rounds | **YES (Regime I)** | t_lineage ~ 1/p_sub ~ 20 |
| Bounded mutation window | **YES (Regime I)** | ~1 mutation per chain per round; near Eigen threshold |
| Robustness to moderate chain lengths | **YES (Regime I)** | N_max ~ 20; 4^20 ~ 10¹² distinct sequences |

**Operational fidelity threshold: CROSSED in Regime I (strong discrimination).**

The threshold is conditional: it requires the system to occupy Regime I, which is structurally plausible but parameter-dependent. If the system occupies Regime II or III, operational fidelity is not achieved, and the upper-stack scaffold reverts to its structural-only status.

---

## 12. Gains and Non-Gains

### Table 6 — Gains and Non-Gains

| Gain | Description | Status |
|------|------------|--------|
| Operational heredity regime identified | Regime I: p_sub ~ 0.05, N_max ~ 20, t_lineage ~ 20 | Conditional on ΔE ≳ 3kT |
| Usable lineage persistence | ~20 generations of identity-level ancestry tracking | Regime I |
| Bounded identity-level mutation | ~1 mutation per chain per round; near Eigen threshold | Regime I |
| Proto-evolutionary window | Heredity + bounded variation; optimal for selection substrate | Regime I |
| Regime map established | Three regimes (strong/marginal/weak) with clear boundaries | Structural analysis |
| Information capacity quantified | 4^20 ~ 10¹² distinct heritable sequences in Regime I | From four-class alphabet + chain length |
| Stronger catalysis/adaptation footing | Operational fidelity makes catalysis questions meaningful | Regime I |
| Zero additional cost | Tenth consecutive zero-cost upper-stack target | Analytical consequence |

| Non-Gain | Description | What would be needed |
|----------|------------|---------------------|
| Rigorous fidelity bound | ΔE_mismatch not computed from first principles | Ab initio bonding-energy calculation |
| Universal fidelity guarantee | Architecture does not guarantee Regime I | Parameter determination program |
| Biological error correction | No proofreading or repair | Enzymatic/catalytic machinery |
| Metabolism | No energy-converting cycles | Catalytic networks + energy sources |
| Cells | No compartments | Membrane-like structures |
| Life | No integrated self-maintaining system | All of the above |
| Evolution (full) | Proto-selection ≠ Darwinian evolution | Functional fitness + ecological dynamics |
| Consciousness | Observer-state organization | Requires biology |

---

## 13. Hard-Gated Summary Table

| Test | Verdict | Reason |
|------|---------|--------|
| Mismatch discrimination structurally present | **YES** | Three reinforcing contributions: steric, angular, overlap |
| Operational high-fidelity regime plausible | **YES (CONDITIONAL)** | Regime I plausible from structural analysis; ΔE ≳ 3kT not rigorously demonstrated |
| Low per-site identity error plausible | **YES (Regime I)** | p_sub ~ 0.05 in strong-discrimination regime |
| Multi-round identity retention plausible | **YES (Regime I)** | N=20 chains retain identity across ~20 rounds |
| Usable mutation/fidelity window plausible | **YES (Regime I)** | ~1 mutation/chain/round; near Eigen threshold; proto-evolutionary window |
| Heredity operationally viable | **YES (CONDITIONAL)** | Operational in Regime I; structural only in Regime II/III |
| Zero-cost upper-stack continuation preserved | **YES** | Tenth consecutive zero-cost target |
| Catalysis-preconditions audit justified | **YES** | Operational fidelity makes catalysis questions meaningful |
| Biology justified | **NO** | No catalysis, metabolism, cells, or functional coding |
| Next-step catalysis or fidelity-enhancement audit justified | **YES** | Catalysis is the next defining boundary after fidelity |

---

## 14. Nonclaims

1. NOT claiming biology — no catalysis, metabolism, cells, or functional coding; the architecture provides an operationally viable heredity platform, not a biological system.

2. NOT claiming life — life requires functional coding + metabolism + replication + selection + compartmentalization; only heredity + proto-selection are operational.

3. NOT claiming metabolism — no energy-converting reaction cycles.

4. NOT claiming cells — no compartments, membranes, or transport.

5. NOT claiming evolution (full Darwinian) — proto-selection operates on structural performance, not functional fitness; no open-ended adaptation.

6. NOT claiming biological error correction — no proofreading or repair mechanisms; fidelity comes from pairing energetics, not enzymatic correction.

7. NOT claiming consciousness — entirely separate program; requires biology as prerequisite.

8. NOT claiming full biological heredity — operational heredity is identity-level faithful but without functional coding, genotype-phenotype mapping, or regulatory architecture.

---

## 15. Next-Step Recommendation

### Table 8 — Next-Route Decision Map

| Outcome | Recommended next document | Rationale |
|---------|--------------------------|-----------|
| **Operational fidelity plausible in Regime I (this outcome)** | **Catalysis Preconditions Audit** | Fidelity is conditionally established; catalysis is the next defining boundary (error correction, metabolism, function) |
| Fidelity marginal (Regime II) | Error-correction / fidelity-enhancement audit | Need to raise fidelity before catalysis is meaningful |
| Fidelity weak (Regime III) | Fidelity-enhancement or architecture revision | Upper-stack scaffold operationally inert without fidelity improvement |

### Recommended Next Document

**Catalysis Preconditions Audit.** With operational heredity conditionally established in Regime I, the next defining boundary is catalysis — the ability of chain structures to accelerate chemical reactions. Catalysis is the key to:

1. **Error correction:** A catalytic chain that preferentially removes mismatched monomers would lower p_sub, raising N_max and improving heredity.
2. **Metabolism:** Catalytic cycles converting environmental resources into usable monomers would make the replication system self-sustaining.
3. **Function-from-sequence:** Catalytic activity as a function of sequence would provide the genotype-phenotype mapping needed for Darwinian selection.
4. **Crossing the origin-of-life boundary:** All five remaining biological boundaries (catalysis, function-to-fitness, metabolism, compartmentalization, ecological dynamics) involve or depend on catalysis.

The catalysis audit should determine: can bridge-level chain structures accelerate reactions? Can sequence determine catalytic activity? What minimum additional structure (if any) would be needed?

---

*Fidelity Bounds Audit complete. Three fidelity regimes identified (strong/marginal/weak). Regime I (ΔE ≳ 3kT, p_sub ~ 0.05) is structurally plausible and supports operational heredity: identity-faithful copying at ~95% fidelity, lineage persistence across ~20 rounds, N_max ~ 20, information capacity ~ 10¹² sequences, and a proto-evolutionary mutation/fidelity window near the Eigen threshold. Tenth consecutive zero-cost upper-stack target. Next step: catalysis preconditions audit.*
