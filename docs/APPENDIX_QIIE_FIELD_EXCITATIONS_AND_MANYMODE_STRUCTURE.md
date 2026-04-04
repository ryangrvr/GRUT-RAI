# Appendix Q-II.E: Field Excitations and Many-Mode Structure

GRUT Quantum Program -- Phase Q-II.E

---

## 1. Exact Question Being Audited

Can GRUT support a coherent field-excitation and many-mode structure beyond
two-state toys, and what exact excitation claims are justified?

---

## 2. Inherited Q-II.D Observable-Grammar Structure

- Multiple observable classes at extension level (sigma_z, sigma_x, sigma_y)
- Toy noncommuting pair: [sigma_z, sigma_x] = 2i sigma_y
- Correlator grammar through CHSH algebraic level
- Bell boundary structurally advanced (algebraic only; Born rule absent)
- Composite C^4 from Q-II.B; entanglement witnesses from Q-II.C

---

## 3. Excitation Eligibility (Track A)

| ID | Ingredient | Status |
|----|-----------|--------|
| EE1 | Multi-mode DOF | extension_level |
| EE2 | Mode labels | extension_level |
| EE3 | Propagation/coupling | extension_level |
| EE4 | Excitation counting | extension_level |
| EE5 | Lindbladian compatibility | present |

1 present, 4 extension-level. Eligible once H_hop postulated.

---

## 4. Mode-Label Analysis (Track B)

| ID | Candidate | Viable |
|----|-----------|--------|
| ML1 | Repeated local sites | Yes (extension) |
| ML2 | Spatially indexed sectors | No (blocked) |
| ML3 | Normal-mode decomposition | No (blocked) |
| ML4 | Topological mode classes | No (underdetermined) |
| ML5 | No mode grammar | No (rejected) |

Mode verdict: **mode_grammar_extension_level_only**

---

## 5. Excitation-Operator Analysis (Track C)

sigma_+ = (sigma_x + i sigma_y)/2 and sigma_- = (sigma_x - i sigma_y)/2:
- Raising: sigma_+ |0> = |1>
- Lowering: sigma_- |1> = |0>
- Number: n = sigma_+ sigma_- = (I + sigma_z)/2, eigenvalues {0, 1}

These are QUBIT operators, NOT canonical bosonic ladder operators.
{sigma_+, sigma_-} = I (anticommutation), not [a, a^dag] = 1.

Excitation verdict: **dissipative_mode_excitation_structure_demonstrated**

---

## 6. Propagation and Coupling (Track D)

| ID | Candidate | Viable |
|----|-----------|--------|
| PR1 | Nearest-neighbor hopping | Yes |
| PR2 | Linear response propagation | No (blocked) |
| PR3 | Lindbladian transport | Yes |
| PR4 | Influence-functional coupling | No |
| PR5 | No propagation | No (rejected) |

H_hop = J sum (sigma_+^i sigma_-^j + h.c.): coherent hopping.
Combined with Lindblad: dissipative propagation (excitations move and decay).

Propagation verdict: **dissipative_propagation_only**

---

## 7. Many-Mode Benchmark (Track E)

Chosen: MB1 (two-site hopping chain).
- H = C^2 tensor C^2 = C^4
- H_hop = J (sigma_+^1 sigma_-^2 + h.c.)
- L_1, L_2: independent Lindblad channels

**Demonstrates:** mode labeling, excitation transfer, dissipative decay,
occupation counting, coherent oscillation before decoherence.

**Does NOT demonstrate:** continuum modes, particle dispersion, QFT, matter.

---

## 8. Excitation-Class Analysis (Track F)

| Level | Achieved |
|-------|----------|
| EC1: Many-mode bookkeeping | Yes |
| EC2: Propagating toy excitations | Yes |
| EC3: Dissipative mode excitations | Yes |
| EC4: Quasi-particle structure | No |
| EC5: Particle language | No |

Highest achieved: EC3 (dissipative mode excitations).

---

## 9. Constitutive-Field Compatibility (Track G)

Excitation operators (sigma_+/sigma_-) live in the complementary sector
to the constitutive observable (sigma_z). This is consistent with Q-F
finding that interference requires the complementary sector.

H_hop modifies per-site dynamics but preserves overall structure.

---

## 10. Matter-Readiness Boundary (Track H)

| Level | Status |
|-------|--------|
| MR1: Excitation grammar | achieved |
| MR2: Pre-matter readiness | achieved |
| MR3: Particle ontology | not_achieved |
| MR4: Bosonic route | partial |
| MR5: Fermionic route | blocked |

Matter verdict: **pre_matter_readiness_advanced_but_particle_ontology_premature**

Fermionic route STILL blocked (Q0 3-layer obstruction unchanged).

---

## 11. Exact Verdicts

| Verdict | Value |
|---------|-------|
| Mode | mode_grammar_extension_level_only |
| Excitation | dissipative_mode_excitation_structure_demonstrated |
| Propagation | dissipative_propagation_only |
| Matter boundary | pre_matter_readiness_advanced_but_particle_ontology_premature |
| Authorization | authorized_to_proceed_to_QIIF |
| Overall Appendix P | motivated_but_unbuilt |

---

## 12. Allowed and Forbidden Claims

**Allowed:**
1. N-site qubit chain mode grammar at extension level
2. sigma_+/sigma_- toy excitation operators (qubit, not bosonic)
3. Dissipative propagation via H_hop + Lindblad
4. Two-site hopping benchmark demonstrated
5. Pre-matter readiness advanced; particle ontology premature
6. Fermionic route still blocked; bosonic route constrained
7. Q-II.F authorized for probability/determination

**Forbidden:**
1. Mode labels imply field theory
2. Excitation bookkeeping implies particles
3. Propagating toy implies matter ontology
4. sigma_+/sigma_- implies canonical creation/annihilation
5. Coupled sites imply continuum quantization
6. Many-mode decoherence implies measurement solved
7. Extension-level excitation implies native canon

---

## 13. Exact Nonclaims (8)

1. NOT claiming many-mode labels therefore field theory solved
2. NOT claiming excitation bookkeeping therefore particles derived
3. NOT claiming propagating toy therefore matter ontology
4. NOT claiming ladder-like notation therefore canonical algebra
5. NOT claiming coupled sites therefore continuum quantization
6. NOT claiming many-mode decoherence therefore measurement solved
7. NOT claiming extension-level excitation therefore native canon
8. NOT claiming excitation grammar therefore fermionic route reopened

---

## 14. Whether Q-II.F May Proceed

Q-II.F (Probability, Determination, and Outcome Extensions) is **authorized**.

Q-II.F constraints:
- Must address Born rule and probability interpretation
- Must not assume particle ontology from excitation grammar
- Must assess outcome selection and determination
- May enable Bell investigation if Born rule is addressed
- Results inherit MBU/MIP floor
