# Program W0 — Carrier Barrier Derivation Matrix

## Companion Reference Tables for W0

---

## Table 1 — Barrier Target Specification

| Parameter | Requirement | Source | W0 status |
|-----------|-------------|--------|-----------|
| ΔG_barrier | ≥ 28 kT for robust regime | Book VII Gamma | Lower-stack-supported inequality |
| τ_carrier | ≫ τ_diffusion (~2 ms) | Book VII Gamma | Qualitatively supported (selection rule) |
| η_carrier | > 0.95 in robust regime | Book VII Gamma | Follows from τ_carrier |
| E_carrier (stored energy) | Sufficient to drive target processes | Book VII Beta | Identified: ΔE₁₂ = (3/16)α_g²M_sk |
| Loaded-state identity | Metastable internal configuration | Book VII Beta | Identified: (N=2, ℓ=0, S=0) state |
| Metastability mechanism | Prevents spontaneous discharge during transit | Book VII Beta | Identified: dipole selection rule |

### Regime Classification

| Regime | ΔG (kT) | Condition on α_g²(M_sk/kT) | η_carrier | Level |
|--------|---------|---------------------------|-----------|-------|
| Weak | < 23 | < 123 | < 0.1 | M3 only |
| Marginal | 23–28 | 123–149 | 0.1–0.6 | M3–M4 boundary |
| **Robust** | **≥ 28** | **≥ 149** | **> 0.95** | **M4** |

---

## Table 2 — Lower-Stack Ingredient Inventory

| Ingredient | Source | Scale/Value | Barrier relevance | Assessment |
|-----------|--------|-------------|-------------------|-----------|
| SU(2) gauge coupling α_g | Book IV Beta | Free parameter; α_g = g²/(2π) | Sets binding and excitation energy | **KEY** |
| Singlet-channel potential | Book IV Beta §7 | V = −α_g/d | Creates bound states | **KEY** |
| K=2 ground-state binding | Book IV Beta §5.1 | E_bind = α_g²M_sk/4 | Sets overall energy scale | **KEY** |
| K=2 excitation spectrum | Book IV Beta §5–6 | ΔE₁₂ = 3α_g²M_sk/16 | **Candidate barrier height** | **KEY** |
| Hard core at R_sk | Book IV Beta §4 | V → +∞ at d ≤ R_sk | Prevents collapse; shifts s-wave levels | HELPFUL |
| Degeneracy breaking | Book IV Beta §5.2 | E(N,ℓ=0) > E(N,ℓ=1) within shell | s-wave state less bound (higher energy) | NEUTRAL |
| Selection rules (Δℓ = ±1) | Standard QM (central potential) | Exact | **Creates metastability** | **KEY** |
| Soliton mass M_sk | Book IV Alpha | (F_π/e)C₁; free parameter | Sets thermal stability scale | **KEY** |
| Soliton radius R_sk | Book IV Alpha | ~1/(eF_π) | Core size; a₀ ≫ R_sk required | HELPFUL |
| Relative-coordinate DOF | Book IV Alpha config-space | d, Ω (separation + orientation) | Internal degrees for loaded state | HELPFUL |
| Centrifugal barrier (ℓ > 0) | Standard QM | ℓ(ℓ+1)/(2μd²) | Classical barrier but state is radiatively unstable | UNHELPFUL (Family C fails) |
| Orientational interaction | Soliton profile overlap | Exponentially suppressed at d ≫ R_sk | Only relevant in strong coupling | CONDITIONAL |
| Dissipation (τ dΦ/dt + Φ = X) | GRUT native core | Acts on field Φ, not on quantum numbers | Potential concern for lifetime | OPEN |

---

## Table 3 — Candidate Derivation-Route Summary

| Family | Mechanism | Energy scale | Metastability | Survives? | Debt effect |
|--------|-----------|-------------|---------------|-----------|------------|
| A — Pure binding depth | Excitation energy ΔE₁₂ | **YES**: (3/16)α_g²M_sk | **NO** — energy scale only, no kinetic trapping | Necessary but insufficient | Scale support only |
| **B — Selection-rule metastability** | **ΔE₁₂ + dipole Δℓ=±1 protection** | **YES** | **YES** — (N=2,ℓ=0) forbidden for E1 | **SURVIVES** | **Reduces debt** |
| C — Centrifugal barrier | Centrifugal maximum for ℓ=1 | YES: ~E_bind/4 | **NO** — ℓ=1 decays via allowed E1 | FAILS | None |
| D — Collective-coordinate | Orientational landscape | CONDITIONAL | CONDITIONAL — strong coupling only | CONDITIONAL | Conditional |
| E — Pseudo-support | Renames matched parameter | N/A | N/A | Critique applies partially | Warning |

---

## Table 4 — Hard-Criteria Pass/Fail Matrix

| Criterion | A (binding) | B (selection rule) | C (centrifugal) | D (collective) | E (pseudo) |
|-----------|------------|-------------------|-----------------|----------------|-----------|
| Lower-stack consistent | **PASS** | **PASS** | **PASS** | PARTIAL | N/A |
| Metastable loaded state | **FAIL** | **PASS** | **FAIL** | CONDITIONAL | N/A |
| Barrier ≥ 28 kT generic | **PASS** | **PASS** | **PASS** | CONDITIONAL | PARTIAL |
| Generic (not fine-tuned) | **PASS** | **PASS** | **PASS** | **FAIL** | N/A |
| No new assumptions | **PASS** | **PASS** | **PASS** | PARTIAL | N/A |
| Reduces debt | PARTIAL | **PASS** | **FAIL** | CONDITIONAL | **FAIL** |
| Low sensitivity to unknowns | MODERATE | MODERATE | HIGH | HIGH | N/A |
| Strengthens Book VII | PARTIAL | **PASS** | **FAIL** | CONDITIONAL | **FAIL** |
| **Overall** | **Ingredient** | **SURVIVES** | **FAILS** | **CONDITIONAL** | **Warning** |

---

## Table 5 — Bound / Inequality Summary

| Inequality | Expression | What it constrains | Derivable? |
|-----------|-----------|-------------------|-----------|
| **Central barrier inequality** | **(3/16)α_g²M_sk ≥ 28 kT** | Robust regime condition on excitation energy | **YES** — from hydrogenic spectrum |
| **Dimensionless form** | **α_g²(M_sk/kT) ≥ 149** | Combined parameter constraint | **YES** |
| Barrier/binding ratio | ΔG/E_bind = 3/4 | Barrier is 75% of binding energy (for N=1→N=2) | **YES** — exact for unperturbed Coulomb |
| Soliton stability | M_sk/kT ≫ 1 | Solitons thermally stable | **Required independently** |
| Weak coupling | α_g M_sk R_sk/2 ≪ 1, i.e. R_sk ≪ a₀ | Hydrogenic approximation valid | **Required for spectrum derivation** |
| Hard-core correction | δE ~ O(R_sk/a₀)² × E | Level shifts from hard core | **Small** in weak coupling |
| Selection-rule exactness | Δℓ = ±1 for E1 | Central-potential theorem | **EXACT** — no exceptions |
| Two-gauge-boson rate | Γ₂γ ~ O(α_g²) × Γ_E1 | Leak rate of metastable state | **NOT COMPUTED** |

### Worked Examples

| α_g | M_sk/kT | α_g²(M_sk/kT) | ΔE₁₂/kT | E_bind/kT | ΔG/E_bind | Robust? |
|-----|---------|---------------|---------|---------|-----------|---------|
| 0.15 | 8000 | 180 | 34 | 45 | 0.75 | **YES** |
| 0.20 | 4000 | 160 | 30 | 40 | 0.75 | **YES** |
| 0.25 | 3000 | 188 | 35 | 47 | 0.75 | **YES** |
| 0.30 | 2000 | 180 | 34 | 45 | 0.75 | **YES** |
| 0.40 | 1000 | 160 | 30 | 40 | 0.75 | **YES** |
| 0.10 | 15000 | 150 | 28 | 38 | 0.75 | **MARGINAL** |
| 0.10 | 10000 | 100 | 19 | 25 | 0.75 | **NO** |
| 0.05 | 50000 | 125 | 23 | 31 | 0.75 | **NO** |

---

## Table 6 — Fragility / Hidden-Assumption Matrix

| Hidden assumption | Family B reliance | Severity | Mitigant |
|------------------|------------------|----------|----------|
| HIC discharge resonant with ΔE₁₂ | Required for loading | MODERATE | HIC operates on K-scale processes; energy matching is self-consistent |
| Collisional quenching at targets | Required for discharge | MODERATE | Standard atomic-physics mechanism; structurally plausible |
| Weak-coupling regime (a₀ ≫ R_sk) | Required for hydrogenic spectrum | LOW | Independently required for composite binding (Book IV Beta) |
| Two-gauge-boson rate ≪ 1/τ_diffusion | Required for τ_carrier ≫ τ_diffusion | **OPEN** | Expected from α_g² suppression; not computed |
| No dissipation dephasing | Required for metastable state survival | **OPEN** | Dissipation acts on Φ, not quantum numbers; but coupling not assessed |
| No non-hydrogenic destruction of metastability | Required for selection-rule protection | LOW | Selection rule is exact for ANY central potential |
| α_g and M_sk/kT in supportive range | Required for robust regime | LOW | Broad parameter range satisfies condition |

---

## Table 7 — False-Positive Disqualification Matrix

| False-positive category | Tested | Result | Reason |
|------------------------|--------|--------|--------|
| Qualitative plausibility only | W0 overall | **DOES NOT APPLY** | Derivable inequality + specific mechanism provided |
| Scale similarity without mechanism | Family A alone | **APPLIES** | Family A has scale but no metastability; disqualified alone |
| Scale similarity without mechanism | Family B | **DOES NOT APPLY** | Family B has both scale AND mechanism |
| Bounds too weak for robust regime | Central inequality | **DOES NOT APPLY** | Robust regime achieved across broad parameter range |
| Metastability without barrier height | Family D | **APPLIES** (partially) | Orientational metastability lacks quantified barrier in weak coupling |
| Debt reduction rhetoric without content | W0 overall | **DOES NOT APPLY** | Physical mechanism identified; inequality derived; loaded state named |
| Carrier support confused with HIC debt | W0 scope | **DOES NOT APPLY** | W0 explicitly addresses only carrier barrier |
| One favorable estimate → native closure | Family B | **HONEST CONCERN** | W0 shows generic support, not unique forcing. Noted in fragility audit. |

---

## Table 8 — Debt-Status Comparison

| Parameter | Pre-W0 class | Post-W0 class | Change | Evidence |
|-----------|-------------|---------------|--------|----------|
| E_carrier | Matched | **Lower-stack supported** | ↑ | Identified with ΔE₁₂ = (3/16)α_g²M_sk |
| τ_carrier | Matched (via Arrhenius) | **Lower-stack supported** (qualitative) | ↑ | Selection-rule protection; Γ₂γ ≪ Γ_E1 |
| ΔG_barrier | Matched ("~half binding energy") | **Approximately derived** (inequality) | ↑ | α_g²(M_sk/kT) ≥ 149 for robust regime |
| Loaded-state identity | Postulated ("conformational switch") | **Lower-stack identified** | ↑ | (N=2, ℓ=0, S=0) excited bound state |
| Metastability mechanism | Postulated (Arrhenius) | **Lower-stack derived** | ↑↑ | Dipole selection rule (exact for central potentials) |
| Carrier postulate (functional class) | Bridge postulate | **Bridge postulate** (unchanged) | — | W0 does not retire the postulate itself |
| Total bridge debt (postulate count) | 1 postulate + 2 parameters | 1 postulate + 2 supported parameters | REDUCED | Parameters better supported; postulate retained |

---

## Table 9 — Pre-W0 vs Post-W0 Epistemic Comparison

| Question | Pre-W0 answer | Post-W0 answer |
|----------|-------------|---------------|
| Why does the barrier exist? | "Physically plausible for K=2 composites" | (N=2, ℓ=0) selection-rule-protected excited state |
| Why is the barrier ≥ 28 kT? | "About half the binding energy" | ΔE₁₂ = (3/4)E_bind; robust when α_g²(M_sk/kT) ≥ 149 |
| Why is the loaded state metastable? | "Conformational barrier with Arrhenius kinetics" | Δℓ = 0 forbidden for E1; two-gauge-boson decay suppressed by α_g² |
| Is the robust regime fine-tuned? | Unknown | **NO** — generic for thermally stable scaffolds with moderate coupling |
| Can the barrier be revoked? | Yes — "if ΔG shown below 28 kT" | Still revocable — but requires α_g²(M_sk/kT) < 149, which conflicts with binding requirements |
| Does this affect the carrier postulate? | N/A | No — postulate retained; parameters supported |

---

*Carrier Barrier Derivation Matrix complete. Nine reference tables covering barrier target, lower-stack ingredients, derivation routes, hard criteria, bounds/inequalities, fragility, false positives, debt status, and epistemic comparison.*
