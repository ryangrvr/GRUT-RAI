# Book V — Target Delta: Energy-Coupling Candidate Matrix

## Companion Reference Document

---

## 1. Candidate Family Table

| Family | Name | Core concept | Required new objects | Required new rules | Minimum postulates |
|--------|------|-------------|---------------------|-------------------|--------------------|
| **A** | Loaded conformational scaffold | Bistable scaffold deformed by nearby reaction | Bistable scaffold | Conformational switch trigger | 1 (subsumed into D) |
| **B** | Activated bond intermediate | High-energy bond product from favorable reaction | New bond type | Synthesis + hydrolysis reactions | 3+ |
| **C** | Compartment-mediated mechanical loader | Pressure/gradient converted to reusable loaded state | Reusable boundary element | Directed mechanical discharge beyond fission | 2+ |
| **D** | **Hybrid intercepting catalyst (HIC)** | **Scaffold whose pocket mechanically deforms during in-pocket reaction, storing strain** | **Capture-discharge dual-site scaffold** | **Backbone strain transmission** | **1 + 1 param** |

---

## 2. Source / Interceptor / Loaded State / Target Mapping

| Family | Source process | Interceptor | Loaded state | Target process | Transfer mechanism |
|--------|--------------|-------------|-------------|---------------|-------------------|
| A | Nearby favorable reaction | Bistable scaffold | Strained conformation | Unspecified unfavorable reaction | Conformational relaxation |
| B | Specific synthesis reaction | New bond type | High-energy bond in product | Hydrolysis-driven target | Bond-breaking energy release |
| C | Cumulative pressure/gradient | Boundary element | Mechanical strain in boundary | Unspecified internal process | Mechanical discharge |
| **D** | **In-pocket favorable reaction (e.g., K=1+K=1→K=2)** | **HIC scaffold pocket** | **Backbone conformational strain (~6–10 kT)** | **Duplex separation / error correction / directed assembly** | **Backbone relaxation at discharge site** |

---

## 3. Hard-Criteria Pass/Fail Matrix

| Criterion | Family A | Family B | Family C | **Family D** |
|-----------|---------|---------|---------|-------------|
| 1. Capture < thermalization | PARTIAL | NO | NO | **YES** |
| 2. Storage > transfer timescale | YES | YES | YES | **YES** |
| 3. Energy > thermal noise | CONDITIONAL | YES | YES | **CONDITIONAL** (η ≳ 0.1) |
| 4. Transfer selectivity | PARTIAL | YES | NO | **YES** |
| 5. Source ≠ target | YES | YES | NO | **YES** |
| 6. Recurrence | YES | YES | NO | **YES** |
| 7. Scaffold compatibility | YES | NO | YES | **YES** |
| 8. Cost minimization | 1 (→D) | 3+ | 2+ | **1+1** |
| 9. Non-false-positive | PARTIAL | YES | NO | **YES** |
| **Pass count** | **4–5/9** | **5/9** | **3/9** | **8–9/9** |
| **Verdict** | Subsumed | Overbuilt | Fails | **SURVIVES** |

---

## 4. Cost Matrix

| Family | New postulates | New parameters | New fields | New DOF | Total new items | Relative to matter bridge (4+2) |
|--------|---------------|---------------|-----------|---------|----------------|-------------------------------|
| A | 1 (→D) | 0–1 | 0 | 0 | 1–2 | Lighter |
| B | 3+ | 1+ | 0 | 0 | 4+ | Comparable |
| C | 2+ | 1+ | 0 | 0 | 3+ | Comparable |
| **D** | **1** | **1** | **0** | **0** | **2** | **Lightest bridge in the program** |

---

## 5. False-Positive Disqualification Table

| False-positive category | Family A? | Family B? | Family C? | Family D? |
|------------------------|----------|----------|----------|----------|
| Catalysis without storage | PARTIAL (requires explicit storage mechanism) | NO | NO | **NO** — stores as backbone strain |
| Storage without transfer | NO | NO | YES (pressure has no specific target) | **NO** — transfers via backbone relaxation at DS |
| Transfer without distinct target | NO | NO | YES (pressure drives fission only) | **NO** — CS ≠ DS; different reactions |
| One-off pressure release | NO | NO | **YES** — fission is one-off | **NO** — recurrent cycle |
| Ambient thermal opportunism | PARTIAL (unclear capture mechanism without pocket) | NO | **YES** — passive accumulation | **NO** — mechanical capture during in-pocket reaction |
| Concentration bias without capture | NO | NO | PARTIAL | **NO** — captures from specific reaction event |
| Mismatch strain at thermal floor | NO | NO | NO | **NO** — backbone strain ~6–10 kT ≫ kT |
| Dissipation relabeled as work | PARTIAL | NO | PARTIAL | **NO** — genuine interception before thermalization |

---

## 6. Minimum-Postulate Comparison Table

| Postulate count | Best candidate | All criteria met? | Viable? |
|----------------|---------------|-------------------|---------|
| 0 | Existing scaffold | NO (Gamma: 31/31 fail) | **NO** |
| 1 | Family D (HIC class) | 8–9/9 (η_couple conditional) | **YES (CONDITIONAL)** |
| 1 + 1 param | Family D + η_couple | 9/9 | **YES — MINIMUM VIABLE** |
| 2 | Family C (loader + discharge) | 3/9 | NO (fails too many criteria) |
| 2 | Family A + explicit pocket (→D) | 8–9/9 | YES but = D at higher naming cost |
| 3+ | Family B (bond + synth + hydrolysis) | 5/9 | Overbuilt; not minimum |

**Conclusion:** 1 postulate + 1 parameter (Family D / HIC) is the unique minimum viable bridge.

---

## 7. Surviving Candidate Summary Card

### The Hybrid Intercepting Catalyst (HIC)

| Property | Value |
|----------|-------|
| **Bridge family** | D |
| **New postulate** | HIC functional class: scaffold sequence with capture-discharge coupling |
| **New parameter** | η_couple (coupling efficiency; fraction of source energy captured as strain) |
| **New fields** | 0 |
| **New DOF** | 0 |
| **Source process** | Favorable reaction in capture pocket (e.g., K=1+K=1 → K=2) |
| **Capture mechanism** | Product geometry deforms pocket → backbone strained |
| **Loaded state** | Conformational backbone strain (~6–10 kT for 2–3 distorted primary bonds) |
| **Storage barrier** | ΔG_barrier ≳ 5 kT for kinetic stability |
| **Discharge mechanism** | Target substrate at discharge site → backbone relaxes → drives target reaction |
| **Target process** | Unfavorable reaction at discharge site (e.g., duplex separation, error correction) |
| **Reset** | Discharge returns scaffold to unloaded conformation; ready for next cycle |
| **Leak path** | Spontaneous thermal relaxation at rate ~ exp(−ΔG_barrier/kT) |
| **Recurrence** | Unlimited (E_unloaded → E_loaded → E_unloaded is a recurrent cycle) |
| **Cycle notation** | E + source → E* + product_source; E* + target → E + product_target |
| **Authority** | Bridge-level MIP |
| **Conditional on** | η_couple ≳ 0.1; ΔG_barrier ≳ 5 kT; scaffold sequence S_HIC exists in 4-class alphabet |

---

*Energy-Coupling Candidate Matrix complete. Four families tested. One survivor (Family D / HIC). Minimum cost: 1 postulate + 1 parameter. Hard-criteria score: 8–9/9. False-positive firewall: passed. The unique minimum-cost energy-coupling bridge.*
