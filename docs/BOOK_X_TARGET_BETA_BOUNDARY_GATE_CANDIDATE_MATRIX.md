# Book X — Target Beta: Boundary-Gate Candidate Matrix

## Companion Reference Tables for Book X Beta

---

## Table 1 — Baseline Boundary-Gap Summary

| Aspect | Current status | What is missing |
|--------|---------------|----------------|
| Boundary type | Passive K=6/K=7 mesh | No functional transport elements |
| Pore control | Structural (fixed pore size) | No dynamic gating |
| Carrier-boundary coupling | ABSENT — carrier terminates at internal targets | No discharge pocket at boundary |
| Transport level | T1 passive selective | T2+ requires boundary-state control |
| Exchange control | None (concentration-driven) | Energy-coupled exchange timing/direction |
| Zero-cost routes tested | 5 families (A–E) | All fail (Book X Alpha) |

---

## Table 2 — Candidate Bridge-Family Comparison

| Family | Mechanism | Postulates | Parameters | Fields | DOF | Transport level | Verdict |
|--------|-----------|-----------|-----------|--------|-----|----------------|---------|
| **F — CCBG (gate)** | **Boundary-embedded scaffold; carrier-driven pore-state switch** | **1** | **1** (+1 optional) | **0** | **0** | **T2–T3** | **MINIMUM VIABLE** |
| G — Shuttle/importer | Boundary-spanning translocator; species-specific | 2 | 2 | 0 | 0 | T3–T4 | Reserved |
| H — Work cycle | Cyclic import/export | Subsumed into G | — | — | — | — | Not independent |
| I — Pseudo-pump | Modern transporter | DISQUALIFIED | — | — | — | — | Prohibited |

---

## Table 3 — CCBG Coupling / Gating / Transport Detail

| Cycle step | Mechanism | Energy source | Timescale | Status |
|-----------|-----------|--------------|-----------|--------|
| Gate resting (closed) | Backbone fills pore | None (stable conformation) | Indefinite | Default |
| Carrier arrival | C_loaded diffuses to gate pocket | Carrier kinetic energy | ~ms (diffusion) | Same as all carrier events |
| Carrier discharge | C_loaded → C_unloaded + ΔE₁₂ to gate backbone | Carrier stored energy | ~μs–ms (discharge) | Same mechanism as all discharges |
| Gate switching | Backbone flips: closed → open | ΔE₁₂ from carrier | ~μs (conformational) | New (CCBG postulate) |
| Species transit | Material diffuses through open pore | Concentration gradient (T2) or binding-release (T3) | ~ms (diffusion through pore) | Passive (T2) or directed (T3) |
| Gate reset | Backbone relaxes: open → closed | Thermal (spontaneous) | τ_reset (parameter-dependent) | New (CCBG postulate) |
| Carrier recycling | C_unloaded returns to pool | Brownian diffusion | ~ms | Same as all carrier events |

---

## Table 4 — Hard-Criteria Pass/Fail Matrix

| Criterion | F (CCBG) | G (shuttle) | I (pseudo-pump) |
|-----------|---------|-----------|----------------|
| 1. Couples carrier to boundary-state change | **PASS** | PASS | DISQUALIFIED |
| 2. Genuine boundary-state control | **PASS** (pore open/closed) | PASS (translocation) | — |
| 3. Selectivity | **PARTIAL** (T2: all species) / **PASS** (T3: binding) | PASS (species-specific) | — |
| 4. Recurrent | **PASS** (gate resets; carrier reusable) | PASS | — |
| 5. Exceeds T1 passive | **PASS** (energy-coupled timing control) | PASS | — |
| 6. Transport level | **T2–T3** | T3–T4 | — |
| 7. Scaffold compatible | **PASS** (uses existing polymer grammar + carrier) | PASS | — |
| 8. Postulate cost | **1** (minimum) | 2 | — |
| 9. Parameter cost | **1** (+1 optional) | 2 | — |
| 10. Fields/DOF | **0/0** | 0/0 | — |
| 11. Elegant or overbuilt | **ELEGANT** | Moderate | Overbuilt |

---

## Table 5 — Transport-Level Consequence Table

| Level | Description | Achievable by | Cost | Immediate use |
|-------|------------|-------------|------|--------------|
| T1 | Passive selective | Current scaffold | 0 | Current (no change) |
| **T2** | **Gated permeability** | **CCBG (closed)** | **+1P +1p** | **Controlled exchange timing** |
| **T3** | **Biased transport** | **CCBG + directional** | **+1P +2p** | **Import/export bias** |
| T4 | Active transport | Family G shuttle | +2P +2p | Species-specific pumping |
| T5 | Transport regulation | Further architecture | +nP +np | Metabolic integration |

---

## Table 6 — Fragility / Sensitivity Matrix

| Parameter | CCBG impact | Sensitivity | Mitigant |
|-----------|-----------|------------|---------|
| ΔG_gate ≤ E_carrier | Gate must be drivable by single carrier | MODERATE | ΔG_gate is a free parameter chosen ≤ ΔE₁₂ |
| τ_reset | Determines gate open time | MODERATE | Pulse-like (short τ_reset) or sustained (long τ_reset); both functional |
| Gate density (N_gates) | Determines system-wide transport impact | MODERATE | More gates = more exchange; few gates = localized effect |
| Carrier budget for gates | Gates consume carriers; must not deplete internal budget | LOW | Under M4, ~5–10% of carrier events to gates leaves ~90%+ for internal use |
| Passive pore dilution | Ungated pores provide passive exchange regardless | MODERATE | Transport effect is additive to passive baseline; not competing |
| Gate failure mode | Gate stuck open = slightly larger passive pore | LOW | Graceful degradation to T1 |
| Gate failure mode | Gate stuck closed = permanently blocked pore | LOW | One pore blocked; others (gated and passive) still function |
| Binding-release efficiency (T3 only) | Directional transport requires efficient bind → displace cycle | MODERATE | Binding affinity K_bind is a tunable parameter |

---

## Table 7 — False-Positive Disqualification Table

| False-positive category | Tested against CCBG | Result | Reason |
|------------------------|-------------------|--------|--------|
| Passive selectivity relabeled | T2 gating | **DOES NOT APPLY** | Gate requires carrier energy; without carrier, pore stays closed |
| Repair-coupled maintenance | CCBG | **DOES NOT APPLY** | Gate controls pore STATE, not pore INTEGRITY |
| Carrier proximity without state change | CCBG discharge | **DOES NOT APPLY** | Carrier DOCKS and DISCHARGES at gate pocket; genuine state change |
| State change without material consequence | T2 gating | **HONEST CONCERN** | T2 controls WHEN pores open, not DIRECTION. Material consequence = exchange timing. Resolved at T3. |
| One-off event | CCBG cycle | **DOES NOT APPLY** | Cycle is recurrent: carrier → open → transit → reset → repeat |
| Modern pump rhetoric | CCBG | **DOES NOT APPLY** | Minimal conformational gate; no ion channels, proton gradients, or rotary motors |

---

## Table 8 — Cost/Debt Comparison Table

| Stage | Postulates | Parameters | Fields | DOF | Transport | Bridges | New cost |
|-------|-----------|-----------|--------|-----|-----------|---------|----------|
| Book IX Terminal | 15 | 9 | 1 | 6 | T1 | 4 | — |
| Book X Alpha | 15 | 9 | 1 | 6 | T1 | 4 | +0 (gap audit) |
| **Book X Beta (if T2 committed)** | **16** | **10** | **1** | **6** | **T2** | **5** | **+1P +1p** |
| Book X Beta (if T3 committed) | 16 | 11 | 1 | 6 | T3 | 5 | +1P +2p |
| (Future: if T4 needed) | 17–18 | 12–13 | 1 | 6 | T4 | 5–6 | +1–2P +1–2p more |

### All Bridges (with CCBG)

| Bridge | Postulates | Parameters | Character |
|--------|-----------|-----------|-----------|
| Matter | 4 | 2 | Topological soliton matter |
| Gauge | 2 | 1 (+1F +6DOF) | Yang–Mills force |
| HIC | 1 | 1 | Fixed-site energy transduction |
| Carrier | 1 | 2 | Mobile energy distribution |
| **CCBG** | **1** | **1** | **Boundary-crossing work** |
| **Total bridge** | **9** | **7** | **5 bridges** |

---

*Boundary-Gate Candidate Matrix complete. Eight reference tables covering boundary gap, bridge families, CCBG cycle detail, hard criteria, transport levels, fragility, false-positive disqualification, and cost/debt comparison.*
