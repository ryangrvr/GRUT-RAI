# Appendix Q-II.B: Composite and Many-Body State Structure

GRUT Quantum Program -- Phase Q-II.B (First Substantive Second-Wave Stage)

---

## 1. Exact Question Being Audited

Given the extension-level quantum package established in Appendix Q, Part I,
can GRUT support a coherent composite-state and subsystem structure at all,
and if so on what exact doctrinal basis?

---

## 2. Inherited Structure

**Part I (Q-B through Q-F):** Single-system quantum foundations.
- 2-state Hilbert space C^2, density matrix rho (2x2)
- Jump operator L = (1/sqrt(tau)) Phi_hat, gamma = 1/tau
- Constitutive recovery, decoherence, pointer basis, transient interference
- ALL single-system; no composite structure

**Q-II.0:** 29 gap items; composite-state gaps (A1-A4) all classified absent.
**Q-II.A:** 8-stage charter; Q-II.B is the first substantive stage.

---

## 3. Composite-State Eligibility Analysis (Track A)

| ID | Ingredient | Status |
|----|-----------|--------|
| CE1 | Distinguishable subsystem labels | extension_level |
| CE2 | Admissible joint state object | extension_level |
| CE3 | Rule for composition | extension_level |
| CE4 | Admissible reduced-state map | extension_level |
| CE5 | Compatibility with first-wave dynamics | extension_level |

All 5 ingredients are extension-level: none present natively, none blocked.
Composite-state structure is entirely postulational.

---

## 4. Subsystem Identity Analysis (Track B)

| ID | Candidate | Viable | Level |
|----|-----------|--------|-------|
| SS1 | Multiple copies of toy system | Yes | extension_level |
| SS2 | Spatially separated sectors | No | blocked (no spatial DOF) |
| SS3 | Distinct observables within one system | No | blocked (single observable) |
| SS4 | Independent reduced-state factors | No | circular |
| SS5 | No valid subsystem identity | No | rejected |

Only SS1 is viable: postulate two independent copies of QE1 two-state system.
Subsystem verdict: **subsystem_identity_extension_level_only**

---

## 5. Composition-Rule Analysis (Track C)

| ID | Candidate | Coherent | Appendix P |
|----|-----------|----------|-----------|
| CR1 | Tensor product | Yes | motivated_independent_postulation |
| CR2 | Direct sum | Yes | compatible_but_ad_hoc |
| CR3 | Coupled density kernel | No | compatible_but_ad_hoc |
| CR4 | History-space | No | compatible_but_ad_hoc |
| CR5 | No rule | N/A | rejected |

CR1 (tensor product) chosen: coherent, standard, MIP classification.
Composition verdict: **composition_rule_extension_level_only**

---

## 6. Reduced-State Analysis (Track D)

| ID | Candidate | Status |
|----|-----------|--------|
| RS1 | Partial trace | extension_level |
| RS2 | Coarse-graining | extension_level |
| RS3 | Subsystem restriction | extension_level |
| RS4 | No map | rejected |

RS1 (partial trace) chosen: follows from tensor product postulation.
Reduced-state verdict: **reduced_state_map_extension_level_only**

---

## 7. Many-Body Grammar Analysis (Track E)

| Level | Description | Achieved |
|-------|------------|----------|
| MB1 | Two-subsystem grammar | Yes |
| MB2 | Finite-N grammar | No (plausible but not demonstrated) |
| MB3 | Many-body grammar | No (plausible but unbuilt) |
| MB4 | Blocked | No (not the case) |

Many-body verdict: **two_subsystem_grammar_demonstrated**

---

## 8. Decoherence Compatibility Analysis (Track F)

| Check | Result |
|-------|--------|
| DC1: Preserves single-system decoherence | compatible |
| DC2: Cross-system decoherence | underdetermined |
| DC3: Constitutive bridge preserved | compatible |
| DC4: Interaction Hamiltonian needed | requires_new_postulate |

Overall: compatible with independent channels. Interaction requires
additional postulation (expected; beyond Q-II.B scope).

---

## 9. Minimal Composite Benchmark (Track G)

Chosen benchmark: CB1 (two-copy product-state benchmark).
- H_AB = C^2 tensor C^2 = C^4 (4x4 density matrix)
- Product state: rho_AB = rho_A tensor rho_B
- Independent Lindblad channels: L_A, L_B

**Demonstrates:**
- Product-state composition
- Independent subsystem decoherence
- Partial trace recovery of single-system states
- Composite Hilbert space (4x4 density matrix)

**Does NOT demonstrate:**
- Entanglement or nonfactorized states
- Cross-system correlations
- Interaction dynamics
- Many-body scaling

---

## 10. Exact Verdicts

| Verdict | Value |
|---------|-------|
| Subsystem | subsystem_identity_extension_level_only |
| Composition | composition_rule_extension_level_only |
| Reduced state | reduced_state_map_extension_level_only |
| Many-body | two_subsystem_grammar_demonstrated |
| Authorization | authorized_to_proceed_to_QIIC |
| Overall Appendix P | motivated_but_unbuilt |

---

## 11. Allowed and Forbidden Claims

**Allowed:**
1. Subsystem identity coherently established via copy duplication (MIP)
2. Tensor product postulated as composition rule; coherent with Part I
3. Partial trace available within tensor-product extension package
4. Two-subsystem grammar demonstrated in product-state benchmark
5. Independent Lindblad channels compatible with composition
6. Interaction Hamiltonian gap documented
7. Q-II.C authorized to proceed

**Forbidden:**
1. Subsystem identity derived from Part I
2. Tensor product derived from GRUT first principles
3. Two-copy benchmark implies entanglement
4. Partial trace independently derived
5. Composite bookkeeping implies many-body readiness
6. Independent decoherence implies multi-body closure
7. Extension-level results imply native canon

---

## 12. Exact Nonclaims (8)

1. NOT claiming repeated toy labels therefore genuine subsystem structure
2. NOT claiming notation-level tensor product therefore physical composition derived
3. NOT claiming two-copy benchmark therefore entanglement established
4. NOT claiming reduced-state language therefore partial trace derived
5. NOT claiming composite bookkeeping therefore many-body readiness
6. NOT claiming first-wave decoherence therefore multi-body closure
7. NOT claiming extension-level composition therefore native canon
8. NOT claiming composite-state support therefore matter-readiness achieved

---

## 13. Whether Q-II.C May Proceed

Q-II.C (Entanglement and Nonfactorized Structure) is **authorized**.

Authorization basis:
- Subsystem identity established at extension level
- Tensor product composition coherently postulated
- Partial trace available as reduced-state map
- Two-subsystem grammar demonstrated in benchmark

Q-II.C constraints:
- Must use tensor product composition from Q-II.B
- Must not assume interaction Hamiltonian without postulation
- Must test nonfactorized states (not just product states)
- Results inherit MBU/MIP floor
- Must not assume Bell violations without demonstration
