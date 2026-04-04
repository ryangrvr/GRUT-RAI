# Book X — Target Gamma: Gate Stress-Test Matrix

## Companion Reference Tables for Book X Gamma

---

## Table 1 — Gate-Cycle Component Verification

| Component | Mechanism | Verified? | Fragility |
|-----------|-----------|-----------|-----------|
| Carrier arrival at gate | C_loaded diffuses to interior-facing gate pocket | **YES** — same as all carrier events | LOW |
| Carrier-gate docking | Geometry-locked docking at discharge pocket | **YES** — same mechanism as all discharges | LOW |
| Carrier discharge → gate switch | ΔE₁₂ drives backbone closed→open | **YES** — ΔG_gate ≤ E_carrier structurally available | MODERATE |
| Species transit during open state | Pore accessible; species diffuses through | **YES** — standard diffusion through open pore | LOW |
| Gate reset (open→closed) | Spontaneous thermal relaxation | **YES** — backbone relaxes to lower-energy conformation | LOW |
| Carrier recycling | C_unloaded returns to pool | **YES** — same as all carrier events | LOW |
| Directional binding (T3) | Exterior pocket captures target during open state | **CONDITIONAL** — K_bind parameter-dependent | MODERATE |
| Displacement (T3) | Conformational reset pushes bound species inward | **CONDITIONAL** — η_displace geometry-dependent | MODERATE |

---

## Table 2 — T2 Verification Summary

| Criterion | Tested | Result | Evidence |
|-----------|--------|--------|----------|
| A. Carrier-coupled boundary-state switching | YES | **PASS** | Carrier discharge flips gate conformation; energy-dependent |
| B. Materially exceeds T1 | YES | **PASS** | Waste export impossible at T1; enabled at T2 |
| C. Selective and repeatable | YES | **PASS** | Specific pores gated; cycle repeats with carrier |
| D. Not relabeled passive bias | YES | **PASS** | Requires carrier energy expenditure; passive pores cannot close/open |
| **T2 overall** | — | **ROBUST** | All four criteria met |

---

## Table 3 — T3 Verification Summary

| Criterion | Tested | Result | Evidence |
|-----------|--------|--------|----------|
| E. Biased import/export of target species | YES | **CONDITIONAL** | Works for large species; fails for small species |
| F. Recurrent and selective directionality | YES | **CONDITIONAL** | Gate cycle is recurrent; selectivity depends on K_bind |
| G. Material environmental-exchange change | YES | **CONDITIONAL** | Large-species import significant; small-species negligible |
| H. Not relabeled passive selectivity | YES | **PASS for large species** | Directed import exceeds passive entry for near-threshold species |
| **T3 overall** | — | **CONDITIONAL (large species only)** | E, F, G conditional; H passes |

### T3 Species-Size Dependence

| Species size | Passive permeability | Gate-directed import | T3 earned? |
|-------------|---------------------|---------------------|-----------|
| Large (near pore threshold) | LOW | **Dominant entry path** | **YES** |
| Medium | MODERATE | Competes with passive | CONDITIONAL |
| Small (≪ pore size) | HIGH | Overwhelmed by passive | **NO** |

---

## Table 4 — Target Species / Process Support

| Species / Process | Size class | T2 benefit | T3 benefit | System consequence |
|------------------|-----------|-----------|-----------|-------------------|
| Large waste products | Large | **SIGNIFICANT** (new exit path) | Export-bias possible | **Waste management enabled** |
| Large precursors / feedstock | Large | Timed entry | **SIGNIFICANT** (directed import) | **Selective import of scarce resources** |
| Boundary-repair precursors | Medium-large | Timed entry | Moderate directed import | Boundary maintenance support |
| K=1 solitons | Small | Negligible | Negligible | Already enters passively |
| Small degradation products | Small | Negligible | Negligible | Already exits passively |
| K=2 carriers | Large (retained) | Gates CLOSED for retention | N/A | Carrier conservation |
| Templates / scaffolds | Very large | N/A (too big for any pore) | N/A | Properly retained |

---

## Table 5 — Parameter Sensitivity Matrix

| Parameter | Effect on T2 | Effect on T3 | Sensitivity | Robust regime |
|-----------|-------------|-------------|------------|--------------|
| ΔG_gate | Gate must switch (≤ E_carrier) | Same | MODERATE | ΔG_gate ≤ (3/16)α_g²M_sk |
| τ_reset | Open duration (pulse width) | Open duration for binding | MODERATE | τ_reset ~ 1–10 ms (pulse gating) |
| N_gates | System-wide transport impact | Same | MODERATE | ≥ 10 gates for system-level effect |
| Carrier budget fraction | Gates per cycle | Same | LOW | ~5–10% of M4 budget sufficient |
| K_bind (T3 only) | N/A | Capture probability | **HIGH for T3** | K_bind ≥ 10³ M⁻¹ for meaningful capture |
| η_displace (T3 only) | N/A | Displacement efficiency | **HIGH for T3** | η_displace ≥ 0.3 for net import |
| Species size | Determines which species benefit | Determines T3 viability | **HIGH** | Large species benefit most |

---

## Table 6 — Robust vs Plausible Regime

| Regime | T2 status | T3 status | Parameter conditions |
|--------|-----------|-----------|---------------------|
| **Robust** | **T2 verified** | T3 for large species only | ΔG_gate ≤ E_carrier; N_gates ≥ 10; carrier budget ≥ 5% |
| Plausible | T2 verified | T3 marginal (medium species compete with passive) | K_bind ≥ 10³; η_displace ≥ 0.3 |
| Marginal | T2 weak (few gates, slow cycling) | T3 absent | N_gates < 5 or carrier budget < 2% |
| Failed | T2 negligible | T3 absent | ΔG_gate > E_carrier or gate mechanically non-functional |

---

## Table 7 — Multi-Domain Impact

| Domain | Impact | Magnitude | New capability? |
|--------|--------|-----------|----------------|
| **Waste handling** | Large-waste export through gated pores | **SIGNIFICANT** | **YES — impossible at T1** |
| **Large-precursor import** | Timed/directed entry of scarce large species | **MODERATE** | **YES — negligible at T1** |
| **Pre-division integrity** | Gates closed during fission → reduced leak | **MODERATE** | YES |
| **Environmental responsiveness** | Gate state reflects internal energetic state | **QUALITATIVELY NEW** | **YES — absent at T1** |
| **Lineage persistence (L4)** | Waste removal reduces toxic accumulation | MODEST | Incremental |
| **Adaptive dynamics (A4)** | Gate-quality traits selectable | MODEST | Incremental |
| **Division quality (D4)** | Marginal — transport doesn't directly affect division | NEGLIGIBLE | No |

---

## Table 8 — False-Positive Disqualification

| False-positive category | Tested against | Result |
|------------------------|---------------|--------|
| Passive selectivity + gate label | T2 waste export | **DOES NOT APPLY** — waste cannot exit at T1 |
| Repeated motion without consequence | T2 gating | **DOES NOT APPLY** — waste export is real consequence |
| T2 mislabeled as T3 | T3 small-species claim | **APPLIES** — T3 fails for small species |
| T2 mislabeled as T3 | T3 large-species claim | **DOES NOT APPLY** — genuine directed import |
| One species class / negligible | Overall claim | **PARTIALLY** — main benefit is large species. But waste export alone is system-significant |
| Parameter-fine-tuned | T2 | **NO** — works across broad range |
| Parameter-fine-tuned | T3 | **MODERATE** — K_bind and η_displace matter |

---

## Table 9 — Transport-Level Comparison

| Level | Description | Mechanism | Cost | Status post-Gamma |
|-------|------------|-----------|------|------------------|
| T0 | Passive porous | Open pores | 0 | Superseded |
| T1 | Passive selective | Size-selective pores | 0 | Superseded by T2 |
| **T2** | **Gated permeability** | **CCBG carrier-coupled pore switching** | **+1P +1p** | **ROBUST — committed** |
| **T3-cond** | **Biased transport (large species)** | **CCBG + directional binding pocket** | **+1p** | **CONDITIONAL — committed** |
| T3-stabilized | Broad-species directional | Would need stronger binding / more gates | — | NOT achieved |
| T4 | Shuttle/importer | Family G | +1–2P +1–2p | NOT present; reserved |

---

## Table 10 — Commit / No-Commit Criteria

| Criterion | Met? | Evidence |
|-----------|------|---------|
| T2 robustly verified | **YES** | Waste export new; timed exchange exceeds T1; carrier-coupled |
| Cost minimal | **YES** | 1P + 2p total (gate + binding pocket); lightest bridge |
| Multiple domains benefit | **YES** | 4+ domains improved |
| Without CCBG, T1 permanent | **YES** | Alpha confirmed; no zero-cost bypass |
| T3 conditional adds value | **YES** | Large-species directed import genuinely useful |
| Family G NOT required | **YES** | T2 + T3-conditional sufficient for current needs |
| **Decision** | **PROVISIONALLY COMMIT** | T2 robust; T3 conditional; cost 16/11/1/6 |

---

*Gate Stress-Test Matrix complete. Ten reference tables covering cycle components, T2/T3 verification, species support, parameter sensitivity, regime analysis, multi-domain impact, false-positive disqualification, transport-level comparison, and commit criteria.*
