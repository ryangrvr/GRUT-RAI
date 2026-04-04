# GRUT Phase D15 — Non-Minimal Curvature Coupling and Weyl-Induced Vector Deployment Test

## 1. Executive Result

**Classification: `nonminimal_curvature_route_fails`**

D15 tested six non-minimal curvature-coupled tensor-memory action candidates — including Weyl-tensor quadratic coupling, Ricci-tensor contraction, Kretschner-scalar effective coupling, Weyl electric tidal coupling, combined non-FP + Weyl coupling, and Gauss-Bonnet family coupling — to determine whether non-minimal curvature coupling can reopen the vector deployment channel that D14 found blocked in the minimal case.

**Result**: All six candidates fail. The fundamental obstruction identified in D14 — the Fierz-Pauli constraint structure eliminates the spin-1 sector as a dynamical mode — is a **kinetic-level** property determined by the structure of second-derivative terms in the action. Non-minimal curvature coupling is a **mass-level** modification that cannot alter the kinetic structure. No mass-level coupling of any form can convert a constraint equation into a dynamical equation.

D15 provides one conceptual upgrade over D14: it sharpens the understanding that the obstruction is kinetic-level, not mass-level, and therefore **closes the non-minimal curvature coupling loophole** as a derivation route for the O(3) sector. This bounds the remaining derivation space.

**Criteria met: 0/4**
- Vector channel opened: **No**
- Curvature-triggered instability: **No**
- Support-class continuity: **No**
- Eta progress: **No**

**Upgrade over D14: conceptual_only**

---

## 2. Why D15 Remains Open After D14

D14 tested five minimal tensor-memory completions:
1. Fierz-Pauli massive rank-2 → fails (FP eliminates spin-1 as constraint)
2. Non-FP mass term → fails (Boulware-Deser ghost)
3. Proca vector extraction → partially motivated but circular
4. Constrained tensor → fails (transversality kills vector)
5. First-order relaxation → fails (constitutive structure cannot support SSB)

D14's analysis used only **minimal** curvature coupling: R\*Phi (scalar-curvature) and R\_ab\*Phi^ab (Ricci-tensor). The loophole: non-minimal couplings — specifically Weyl-tensor contractions C\_abcd\*Phi^ac\*Phi^bd — act differently on different spin sectors because the Weyl tensor is trace-free. This means Weyl coupling could potentially split the effective mass of vector vs tensor modes, making the vector sector tachyonic in strong curvature while keeping the tensor sector stable.

Why Weyl/tidal is the best remaining candidate:
- Ricci curvature vanishes in vacuum (R\_ab = 0), so Ricci couplings contribute nothing in the exterior strong-field region
- Weyl curvature dominates in vacuum strong-field regions
- The Weyl tensor's irreducible structure naturally distinguishes between spin sectors

What would count as a genuine upgrade beyond D14:
1. A non-minimal coupling that opens a vector channel without ghost
2. Curvature-triggered instability in the vector sector specifically
3. Support-class continuity with 1/r^2 Component B
4. Some progress on eta derivation or constraint

---

## 3. Candidate Non-Minimal Tensor-Memory Actions

### Table A: Candidate Action Table

| Candidate | Coupling Type | Inherited Content | New Completion Content | Ghost Status | Verdict |
|-----------|---------------|-------------------|------------------------|-------------|---------|
| B1: Weyl quadratic C\_abcd\*Phi^ac\*Phi^bd | weyl_tensor | Rank-2 Phi\_ab, trace = scalar, Schwarzschild Weyl | xi\_W coupling coefficient | ghost_risky | **fails** |
| B2: Ricci contraction R\_ab\*Phi^ab | ricci_tensor | Rank-2 Phi\_ab, background metric | xi\_R coupling coefficient | ghost_free | **fails** |
| B3: Kretschner K\*Phi\_ab\*Phi^ab | kretschner_effective | Rank-2 Phi\_ab, K from D10 | xi\_K coupling coefficient | ghost_risky | **fails** |
| B4: Weyl electric tidal E\_ij\*sigma^ij | weyl_tensor | Traceless sigma\_ij, E\_ij | xi\_E tidal coupling | undecidable | **fails** |
| B5: Non-FP + Weyl combined | weyl_tensor | Rank-2 Phi\_ab, Weyl, K | Non-FP mass + xi\_W (3 params) | **ghost_present** | **fails** |
| B6: Gauss-Bonnet f(Phi)\*G\_4 | gauss_bonnet_family | Scalar Phi, G\_4 | alpha\_GB coupling | ghost_free | **fails** |

**Key findings by candidate:**

- **B1 (Weyl quadratic)**: The Weyl coupling provides curvature-dependent mass splitting between spin sectors. However, in the Fierz-Pauli framework the vector sector is a constraint mode, and a mass-level coupling cannot convert a constraint equation into a dynamical equation.

- **B2 (Ricci contraction)**: R\_ab = 0 in vacuum Schwarzschild. The coupling vanishes identically in the exterior strong-field region where the defect sector is needed. Structurally irrelevant.

- **B3 (Kretschner scalar)**: K is a scalar invariant that shifts all spin-sector masses equally. Cannot produce differential mass splitting between vector and tensor modes.

- **B4 (Weyl electric tidal)**: E\_ij couples only to the tensor (spin-2) sector. The magnetic tidal component B\_ij provides derivative mixing with the vector sector, but derivative coupling cannot overcome the FP constraint structure.

- **B5 (Non-FP + Weyl)**: The strongest combined attempt. Non-FP mass activates the vector; Weyl coupling makes it curvature-sensitive. But the Boulware-Deser ghost is incurable by non-minimal coupling. The ghost is a kinetic-structure property, unaffected by mass/potential modifications.

- **B6 (Gauss-Bonnet)**: Scalar-sector modification only. Cannot address the vector deployment question.

---

## 4. Mode Decomposition and Effective Mass Structure

### Table B: Mode/Instability Table

| Mode Sector | Exists? | Curvature-Sensitive? | Effective Mass Shift | Instability Status | Triplet Relevance | Verdict |
|-------------|---------|---------------------|---------------------|-------------------|-------------------|---------|
| scalar\_trace | Yes | Yes | K-coupling, GB modify scalar mass | curvature\_sensitive\_stable | None (IS existing scalar) | not\_relevant |
| vector\_spin1 | Yes | Yes | Weyl: delta\_m\_v^2 ~ -xi\_W\*M/r^3 (in non-FP only) | **curvature\_sensitive\_stable** | Formally correct DOF count (3), but constrained (FP) or ghostly (non-FP) | **curvature\_sensitive\_but\_blocked** |
| tensor\_spin2 | Yes | Yes | Weyl: anisotropic E\_ij splitting | curvature\_sensitive\_stable | None (wrong spin) | not\_relevant |

**Key result**: Non-minimal Weyl coupling produces real, curvature-dependent mass splitting between spin sectors. The vector effective mass IS modified by tidal curvature. However, this is a mass-level effect operating on a mode whose dynamical status is determined by the kinetic structure. In all ghost-free completions, the vector is a constraint mode, and mass modifications cannot convert it to a dynamical mode.

The obstruction hierarchy:
1. **Kinetic level** (determines propagating DOF) — set by the FP structure → vector is constrained
2. **Mass level** (determines effective masses) — modifiable by curvature coupling → vector mass shifts
3. Conclusion: mass-level modifications cannot alter kinetic-level structure

---

## 5. Curvature-Triggered Vector Deployment Analysis

**Trigger quantity**: Weyl electric tidal tensor E\_ij = C\_{0i0j} = diag(2M/r^3, -M/r^3, -M/r^3). Grows as M/r^3 inward.

**Sign structure**: The trace of E\_ij vanishes (Tr(E) = 0) because R\_ab = 0 in vacuum. The net effective mass shift on the vector sector from Weyl coupling is **zero** when summed over components. Individual polarization components shift differently (radial vs tangential) but there is no net tachyonic trigger.

**Threshold analysis**: No threshold exists for vector instability via Weyl coupling:
1. In FP: vector is constrained (no instability possible for a constraint)
2. In non-FP: BD ghost dominates; vector tachyon is secondary to ghost runaway
3. Tracelessness of E\_ij means net vector mass shift vanishes

**Vector classification**: curvature\_sensitive\_stable. The vector sector is curvature-sensitive but NOT deployed.

---

## 6. Support-Class Continuity Test

### Table C: Support-Class Continuity Table

| Test | Result | Strength | Comment |
|------|--------|----------|---------|
| Hedgehog from Weyl-coupled vector | Not applicable; vector not deployed | **absent** | Prerequisite (dynamical vector) not met |
| Angular gradient ~ 1/r^2 | Hypothetical only; would follow from deployed vector | **absent** | Weyl coupling does not obstruct support class itself — it obstructs vector deployment |
| D12 Q-ontology continuity | No VEV, no topological charge | **absent** | No Q-ontology without deployed vector |
| Component B stress-energy from tensor sector | Tensor (spin-2) stress-energy exists but wrong spin | **fails** | Tensor contribution does not match Component B ~ 1/r^2 support class |

**Overall continuity**: **False**. Support-class continuity fails across all tests because the vector sector is not deployed.

---

## 7. Eta Analysis

### Table D: Eta Analysis Table

| Mechanism | Eta Derived? | Eta Constrained? | Eta Matched Only? | Comment |
|-----------|-------------|-----------------|-------------------|---------|
| Weyl coupling mass splitting | No | No | Yes | xi\_W independent of eta |
| Kretschner coupling threshold | No | No | Yes | xi\_K relates to geometric params, not eta |
| Tidal-driven VEV (hypothetical) | No | No | N/A (fails) | Vector deployment fails; route closed |

**Best outcome**: matched\_only. Non-minimal curvature coupling makes no progress on eta. The coupling parameters (xi\_W, xi\_K) are structurally independent of the defect VEV scale eta.

---

## 8. Comparison to D14

### Table E: D14 vs D15 Upgrade Table

| Criterion | D14 | D15 | Upgrade? | Comment |
|-----------|-----|-----|----------|---------|
| Vector sector status | Constrained (FP) or ghostly (non-FP) | Curvature-sensitive but still constrained/ghostly | **No** | Mass-level coupling cannot resolve kinetic-level obstruction |
| Ghost freedom | FP ghost-free but no vector; non-FP has vector but ghost | Same dichotomy persists | **No** | Weyl coupling cannot cure BD ghost |
| Curvature-triggered instability | Not achieved | Curvature-dependent mass splitting present but on constrained/ghostly mode | **No** | Real effect, but on wrong (non-dynamical) mode |
| Support-class continuity | Fails | Fails | **No** | Both require deployed vector |
| Eta progress | related\_to\_parameters | matched\_only | **No** | Coupling parameters independent of eta |
| Structural understanding | FP constraint vs ghost dichotomy | **Sharpened**: obstruction is kinetic-level, not mass-level | **Yes** | D15 clarifies WHY non-minimal coupling cannot help |

**Overall upgrade: `conceptual_only`**

D15 does not materially upgrade D14 in terms of vector deployment, instability, support-class continuity, or eta progress. D15 provides one conceptual upgrade: it sharpens the understanding that the D14 obstruction is kinetic-level, not mass-level, and therefore cannot be resolved by non-minimal curvature coupling of any form.

---

## 9. Final D15 Classification

### Table F: Final Classification

| | |
|---|---|
| **Classification** | `nonminimal_curvature_route_fails` |
| **Criteria met** | 0 / 4 |
| **Vector channel opened** | No |
| **Instability achieved** | No |
| **Support-class continuity** | No |
| **Eta progress** | No |
| **Upgrade over D14** | conceptual\_only |

**Justification**: Non-minimal Weyl/tidal curvature coupling produces real curvature-dependent mass splitting in the tensor-memory sector, but this is a mass-level effect that cannot overcome the kinetic-level FP constraint structure identified in D14. The Weyl coupling loophole is **closed**: non-minimal curvature coupling of any form cannot resolve the vector deployment obstruction.

**What D15 closes**: The entire non-minimal curvature coupling route for O(3) sector derivation from tensor memory. This includes:
- Weyl-tensor contractions (quadratic, tidal electric, tidal magnetic)
- Ricci-tensor contractions (vanish in vacuum)
- Kretschner-scalar couplings (no spin selectivity)
- Gauss-Bonnet family (scalar-sector only)
- Combined non-FP + non-minimal (ghost incurable)

---

## 10. Remaining Foundational Gaps

1. **O(3) defect sector remains a principled extension, not derived** (critical). D13 established partially\_motivated\_not\_derived. D14 closed minimal tensor-memory routes. D15 closes non-minimal curvature coupling routes. The O(3) sector must still be introduced as an extension.

2. **All rank-2 tensor-memory routes to O(3) induction are now exhausted** (critical). Minimal completions (D14): blocked by FP constraint or ghost. Non-minimal curvature coupling (D15): blocked because mass-level coupling cannot overcome kinetic-level constraint. Remaining loopholes: (a) non-perturbative/lattice effects, (b) higher-spin/extended multiplet, (c) UV completion beyond EFT, (d) fundamentally new sector unrelated to tensor-memory decomposition.

3. **eta = 1/sqrt(8*pi) remains a matched parameter** (significant). Neither D14 nor D15 makes progress on deriving or constraining eta.

4. **Empirical confrontation not achieved** (critical). Independent of derivation questions, the strong-field interior predictions remain unconfronted by observation.

---

## 11. Explicit Nonclaims

1. D15 does not claim that non-minimal curvature coupling is irrelevant to GRUT; it is irrelevant specifically for the vector sector deployment question.

2. D15 does not claim that the tensor memory sector gains nothing from Weyl coupling; the tensor (spin-2) sector gains curvature-dependent mass splitting that may be relevant for gravitational-wave memory effects.

3. D15 does not claim to have exhausted ALL possible O(3) derivation routes; it closes the non-minimal curvature coupling route specifically. Remaining loopholes include non-perturbative effects, higher-spin content, UV completion, and fundamentally new sectors.

4. D15 does not claim that the O(3) sector is wrong or unnecessary; it remains a principled extension that must be introduced rather than derived from the tensor memory.

5. D15 does not prove that the kinetic-mass level separation is absolute in all possible extensions; non-perturbative or strongly-coupled regimes might blur this distinction.

6. D15 does not address whether dRGT nonlinear massive gravity could change the picture. dRGT is ghost-free and nonlinear, but its vector sector has the same constraint property as FP.

7. D15 does not claim that Weyl-tensor physics is unimportant for GRUT; tidal effects enter the D10 trigger mechanism and D11 two-field structure. The negative result is specifically about using Weyl coupling to deploy a vector sector from the tensor memory.

---

## Assumptions

| Assumption | Status | Source |
|------------|--------|--------|
| Rank-2 Phi\_ab decomposes as trace + vector + tensor | Inherited | Phase IV |
| Fierz-Pauli is the unique ghost-free linear massive spin-2 theory | Standard result | Boulware-Deser (1972) |
| Non-minimal curvature coupling modifies mass-level, not kinetic-level | D15 analysis | Perturbative EFT framework |
| Weyl tensor vanishes nowhere in Schwarzschild exterior | Inherited | Vacuum Einstein equations |
| Ricci tensor vanishes in vacuum | Inherited | R\_ab = 0 by field equations |
| Ghost-free massive spin-2 constraint structure is kinetic-determined | Standard result | Constraint analysis literature |
| Strong-field region r ~ R\_S is vacuum | Inherited | D8 background |
| dRGT preserves FP constraint structure for vector | Assumed | Literature; not independently verified |

---

*Module: `grut/weyl_coupling_vector_deployment.py`*
*Tests: `tests/test_weyl_coupling_vector_deployment.py` (86 tests)*
