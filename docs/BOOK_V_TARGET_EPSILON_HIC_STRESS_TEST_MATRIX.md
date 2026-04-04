# Book V — Target Epsilon: HIC Stress-Test Matrix

## Companion Reference Document

---

## 1. Source-Target Candidate Table

| Pairing | Source process (favorable) | Target process (unfavorable) | Energy match? | Structural plausibility | Overall |
|---------|--------------------------|----------------------------|--------------|----------------------|---------|
| **P1** | **K=1+K=1→K=2 (soliton singlet binding) in CS** | **Duplex separation (secondary-bond peeling) at DS** | **YES: ΔG_source ~50 kT; ΔG_target ~5–10 kT; η_couple ~0.1 suffices** | **STRONGEST: most energetic source + most common unfavorable target** | **PRIMARY** |
| P2 | Monomer assembly (K=1→K=6) in CS | Mismatch removal at DS | YES: cumulative assembly energy large; mismatch cost ~3–5 kT | Demanding: DS must selectively identify and break one incorrect bond | SECONDARY |
| P3 | K=1+K=1→K=2 in CS | Directed monomer incorporation at DS | Marginal: target is kinetically slow but thermodynamically favorable | Closer to enhanced catalysis than true coupling (target is downhill) | MARGINAL |
| P4 | K=6/K=7 assembly in CS | Boundary mesh insertion against pressure at DS | YES: assembly energy large; insertion cost = PΔV | Demanding: HIC anchored at boundary surface | SPECULATIVE |
| P5 | D↔A secondary-bond formation in CS | Template strand release at DS | NO: secondary-bond energy too small (~2–3 kT) to drive anything meaningful even at η=1 | Source too weak | **FAILS** |
| P6 | Cross-catalytic replication as source | Boundary repair at DS | Unclear: replication releases no concentrated single-event energy | Source is distributed across many steps | **FAILS** |

---

## 2. Capture / Loaded / Discharge / Leak Mapping

| Phase | P1 (primary) | P2 (secondary) | P3 (marginal) |
|-------|-------------|----------------|---------------|
| **Capture event** | K=2 product forms in CS; larger geometry deforms pocket walls | K=6 product forms in CS; shell geometry deforms pocket | K=2 forms in CS (same as P1) |
| **Loaded state** | Backbone strained at 2–3 primary bonds; ~5–15 kT stored | Backbone strained; ~5–15 kT stored | Same as P1 |
| **Discharge event** | Strained backbone at DS peels secondary bonds in bound duplex segment | Strained backbone at DS breaks incorrect secondary bond at mismatch site | Strained backbone at DS positions/orients monomer for incorporation |
| **Leak event** | Spontaneous backbone relaxation → heat; rate = k_leak | Same | Same |
| **Reset** | E_unloaded; both sites cleared; ready for next cycle | Same | Same |
| **Concerted?** | YES — both substrates pre-bound | YES — both pre-bound | YES |
| **Estimated discharge benefit** | Duplex separation ~10x faster than thermal | Mismatch removal: proofreading-like; lowers p_sub | Monomer incorporation: modest rate enhancement |

---

## 3. Threshold A/B/C Pass-Fail Table

| Condition | P1 | P2 | P3 | P4 |
|-----------|----|----|----|----|
| **A: Favorable drives unfavorable** | **YES** — assembly drives separation through strain | **YES** — assembly drives mismatch removal | **MARGINAL** — target is kinetically slow, not thermodynamically unfavorable | **CONDITIONAL** — requires boundary-anchored HIC |
| **B: Useful flux persists** | **CONDITIONAL** — recurrent locally; system-level supplementary | **CONDITIONAL** — same | **CONDITIONAL** — same | **SPECULATIVE** |
| **C: More than ambient thermal** | **YES** — mechanical capture, not thermal | **YES** — same | **PARTIAL** — target already thermally accessible | **YES** |
| **Overall** | **CONDITIONAL PASS** | **CONDITIONAL PASS** | **MARGINAL** | **SPECULATIVE** |

---

## 4. Stress-Test Criteria Matrix

| Criterion | P1 verdict | P2 verdict | P3 verdict | Detail |
|-----------|-----------|-----------|-----------|--------|
| 1. Capture before thermalization | **PASS** | **PASS** | **PASS** | Direct mechanical contact during in-pocket reaction |
| 2. Loaded-state lifetime | **PASS (concerted)** | **PASS (concerted)** | **PASS (concerted)** | Concerted mode eliminates storage-lifetime concern |
| 3. Energy quantum > noise | **PASS** (η≥0.1 → 5+ kT) | **PASS** | **PASS** | Source energy ~50 kT; even 10% capture exceeds noise |
| 4. Discharge selectivity | **PASS** | **CONDITIONAL** (high specificity needed for single-bond removal) | **PASS** | P2 requires finest geometric discrimination |
| 5. Source ≠ target | **PASS** | **PASS** | **MARGINAL** (target is kinetically slow, not thermodynamically distinct) | P3 blurs the line between coupling and enhanced catalysis |
| 6. Recurrence | **PASS** | **PASS** | **PASS** | All cycle indefinitely |
| 7. Leak vs useful transfer | **PASS (concerted)** | **PASS (concerted)** | **PASS (concerted)** | Concerted: discharge immediate; leak moot |
| 8. η_couple fragility | **PASS** (works across η=0.1–0.5) | **PASS** | **PASS** | Factor-of-5 parameter range |
| 9. Scaffold compatibility | **PASS** | **PASS** | **PASS** | Uses existing polymer grammar |
| **Score** | **9/9** | **8/9** (C4 conditional) | **7/9** (C4 pass, C5 marginal, overall marginal) | |

---

## 5. η_couple Sensitivity Table

| η_couple | Stored strain (kT) for ΔG_source = 50 kT | Above noise (>1 kT)? | Sufficient for P1 target (~5–10 kT)? | Sufficient for P2 target (~3–5 kT)? | Assessment |
|----------|------------------------------------------|---------------------|--------------------------------------|--------------------------------------|-----------|
| 0.01 | 0.5 | NO | NO | NO | Below noise floor; mechanism non-functional |
| 0.05 | 2.5 | YES (marginal) | NO | MARGINAL | Barely above noise; cannot drive most targets |
| **0.10** | **5.0** | **YES** | **YES (marginal)** | **YES** | **Minimum functional threshold** |
| 0.20 | 10.0 | YES | YES | YES | Comfortably functional |
| 0.30 | 15.0 | YES | YES (robust) | YES (robust) | Robust operation |
| 0.50 | 25.0 | YES | YES (excess) | YES (excess) | Maximum plausible range |

**Conclusion:** The mechanism works for η_couple ≥ 0.10 and fails for η_couple < 0.05. The functional window is η_couple ∈ [0.10, 0.50] — a factor-of-5 range. Not excessively fragile.

---

## 6. False-Positive Disqualification Table

| False-positive category | P1 status | P2 status | P3 status |
|------------------------|----------|----------|----------|
| Catalysis without storage | CLEAR — stores as backbone strain | CLEAR | **MARGINAL** — P3 target is thermodynamically favorable; closer to catalysis |
| Storage without transfer | CLEAR — transfers via backbone relaxation | CLEAR | CLEAR |
| Transfer without distinct target | CLEAR — CS ≠ DS; different reactions | CLEAR | **MARGINAL** — P3 source and target are both favorable processes |
| One-off mechanical discharge | CLEAR — recurrent cycle | CLEAR | CLEAR |
| Ambient thermal dressed as coupling | CLEAR — mechanical capture, not thermal | CLEAR | **MARGINAL** — P3 target is thermally accessible |
| Concentration bias | CLEAR — energy from specific reaction event | CLEAR | CLEAR |
| Mismatch strain at thermal floor | CLEAR — backbone strain ≫ kT | CLEAR | CLEAR |
| Dissipation relabeled | CLEAR — genuine interception before thermalization | CLEAR | CLEAR |
| **Overall** | **CLEAR** | **CLEAR** | **MARGINAL — P3 is close to enhanced catalysis** |

---

## 7. Local vs Cycle-Level Classification Table

| Classification | P1 | P2 | P3 | System-level |
|---------------|----|----|----|----|
| **Local coupling event** | YES — one HIC cycles at one site | YES | YES | Present |
| **Recurrent local coupling** | YES — unlimited cycling | YES | YES | Present |
| **System-level significance** | CONDITIONAL — enhances replication rate; how much depends on HIC density relative to uncatalyzed replication | CONDITIONAL — reduces error rate; significance depends on improvement magnitude | MARGINAL — modest rate enhancement | **SUPPLEMENTARY** — system operates without HIC; HIC enhances specific steps |
| **Cycle-level integration** | OPEN — HIC-driven separation integrated into replication cycle; but cycle proceeds without HIC too | OPEN — HIC-driven proofreading integrated into copying; but copying proceeds without HIC | NO — directed incorporation is not rate-limiting | **NOT DOMINANT** |
| **Proto-metabolic organization** | NO — one coupling route ≠ metabolic network | NO | NO | **NO** |
| **Level classification** | **Level 5 local** | **Level 5 local** | **Level 4.5–5** | **Level 5 local** |

---

## 8. Concerted-Operation Requirement Summary

The adversarial stress test revealed that the HIC's storage-lifetime issue (loaded state leaks before target arrives by diffusion) is resolved by **concerted operation**: both source and target substrates are pre-positioned at their respective sites before the capture event occurs.

| Property | Store-and-wait mode | Concerted mode |
|----------|-------------------|---------------|
| Source substrate | Binds CS; reaction occurs; product loads backbone | Same |
| Target substrate | Must find DS after loading (diffusion-limited) | **Pre-bound at DS before CS fires** |
| Loaded-state lifetime requirement | Must exceed diffusive encounter time (~ms) | Must exceed backbone strain propagation time (~fs) |
| Leak vulnerability | **HIGH** — k_leak ≫ k_encounter at molecular timescales | **LOW** — discharge immediate after capture |
| Useful fraction η_useful | ~10⁻⁷ (negligible) | ~0.5 (functional) |
| Physical analogy | Battery (stores energy for later) | **Mechanical linkage (transduces in real time)** |
| Extra postulate needed? | No | **No** — geometric constraint on S_HIC sequence |

**The HIC is a direct transducer, not an energy-storage device.** This is a narrower capability than Delta originally suggested, but it is genuine Level 5 coupling.

---

*HIC Stress-Test Matrix complete. P1 (soliton assembly → duplex separation) scores 9/9 on stress test. P2 (assembly → mismatch removal) scores 8/9. P3 (assembly → directed incorporation) is marginal. Concerted operation resolves storage-lifetime issue. The HIC is a direct transducer operating at Level 5 local. η_couple functional window: 0.10–0.50.*
