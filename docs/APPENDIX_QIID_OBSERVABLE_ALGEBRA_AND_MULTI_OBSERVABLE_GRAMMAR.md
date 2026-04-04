# Appendix Q-II.D: Observable Algebra and Multi-Observable Grammar

GRUT Quantum Program -- Phase Q-II.D

---

## 1. Exact Question Being Audited

Can GRUT support a coherent multi-observable grammar beyond the single
constitutive observable Phi_hat, and what exact observable-algebra claims
are justified at this stage?

---

## 2. Inherited Structure

**Part I:** One constitutive observable Phi_hat = sigma_z; QE3 second
observable underdetermined.

**Q-II.B:** Composite C^4 = C^2 tensor C^2; product observables formal.

**Q-II.C:** Nonfactorized states demonstrated; purity/PPT witness justified;
Bell not yet justified (missing multi-observable + Born rule).

---

## 3. Observable Eligibility (Track A)

| ID | Ingredient | Status |
|----|-----------|--------|
| OE1 | Constitutive observable (Phi_hat) | present |
| OE2 | Complementary observable (sigma_x) | extension_level |
| OE3 | Expectation-value rule | present |
| OE4 | Correlator grammar | extension_level |
| OE5 | State-structure compatibility | present |

3 present, 2 extension-level, 0 absent.

---

## 4. Candidate Observables (Track B)

| ID | Observable | Motivation |
|----|-----------|-----------|
| OBS1 | Phi_hat = sigma_z | motivated |
| OBS2 | sigma_x (complementary) | compatible |
| OBS3 | sigma_y (algebraic closure) | compatible |
| OBS4 | X_hat (source) | underdetermined |
| OBS5 | Composite locals (sigma_z tensor I) | motivated |
| OBS6 | Composite joints (sigma_z tensor sigma_z) | extension_level |

sigma_x is the key extension: unlocks noncommutativity and correlators.

---

## 5. Noncommutativity (Track D)

Toy noncommuting pair justified: {sigma_z, sigma_x} with exact commutator

    [sigma_z, sigma_x] = 2i sigma_y

This is a mathematical fact of C^2, not a physical derivation. The
noncommuting structure exists once sigma_x is acknowledged as an observable.

Resolves QE3 gap (conditional on sigma_x postulation).

Noncommutativity verdict: **toy_noncommuting_pair_justified**

---

## 6. Correlator Grammar (Track E)

| Level | Description | Available |
|-------|------------|-----------|
| CG1 | Single-observable expectation | Yes |
| CG2 | Two-point (same system) | Yes |
| CG3 | Subsystem correlators | Yes |
| CG4 | CHSH algebraic correlator | Yes |
| CG5 | Time-ordered correlators | No |

4 of 5 levels available. CHSH correlator S = <AB> - <AB'> + <A'B> + <A'B'>
can be WRITTEN and Tr(rho S) COMPUTED.

CAVEAT: Tr(rho S) = 2 sqrt(2) for Bell state is an algebraic result; its
interpretation as a statistical correlation requires Born rule (absent).

Correlator verdict: **correlator_grammar_extension_level_only**

---

## 7. Minimal Algebra (Track F)

Achieved levels: AL1 (observable list), AL2 (expectation grammar),
AL3 (toy noncommutative algebra), AL4 (extension-level multi-observable).
Not achieved: AL5 (full observable ontology with physical interpretation).

---

## 8. Composite Observables (Track G)

All 4 composite observable types available on C^4: product observables,
local observables, joint expectation values, entanglement witness
observables.

---

## 9. Bell-Boundary Readiness (Track H)

| Level | Description | Achieved |
|-------|------------|----------|
| BR1 | Algebraic CHSH structure | Yes |
| BR2 | Entangled state benchmark (Tr = 2 sqrt 2) | Yes |
| BR3 | Probability interpretation (Born rule) | No |
| BR4 | Operational Bell violation | No |

Bell boundary **structurally advanced** from Q-II.C: algebraic structure
now present. Remaining gap: Born-rule probability interpretation (Q-II.F).

Bell readiness verdict: **bell_boundary_structurally_advanced**

---

## 10. Exact Verdicts

| Verdict | Value |
|---------|-------|
| Observable | multiple_observable_classes_extension_level_only |
| Noncommutativity | toy_noncommuting_pair_justified |
| Correlator | correlator_grammar_extension_level_only |
| Bell readiness | bell_boundary_structurally_advanced |
| Authorization | authorized_to_proceed_to_QIIE |
| Overall Appendix P | motivated_but_unbuilt |

---

## 11. Allowed and Forbidden Claims

**Allowed:**
1. Multiple observable classes at extension level
2. Toy noncommuting pair with exact commutator
3. Correlator grammar through CHSH algebraic level
4. Bell boundary structurally advanced (algebraic only)
5. QE3 gap conditionally resolved
6. Composite observables on C^4
7. Q-II.E authorized

**Forbidden:**
1. sigma_x implies grammar derived from GRUT
2. Toy pair implies full operator algebra
3. Correlator notation implies Bell readiness
4. Composite notation implies physical coupling
5. Expectation success implies canonical commutator derived
6. Two-observable grammar implies matter readiness
7. Extension-level implies native canon

---

## 12. Exact Nonclaims (8)

1. NOT claiming sigma_x notation therefore observable grammar solved
2. NOT claiming toy noncommuting pair therefore full operator algebra
3. NOT claiming correlator notation therefore Bell readiness achieved
4. NOT claiming composite observable notation therefore physical coupling
5. NOT claiming expectation-value success therefore canonical commutator derived
6. NOT claiming two-observable grammar therefore matter readiness
7. NOT claiming extension-level multi-observable therefore native canon
8. NOT claiming Bell-style toy correlators therefore nonlocality established

---

## 13. Whether Q-II.E May Proceed

Q-II.E (Excitation and Many-Mode Structure) is **authorized**.

Q-II.E constraints:
- Must use observable grammar from Q-II.D
- Must not assume Bell violation without Born rule
- Must address mode decomposition and excitation language
- May build on noncommutative structure for ladder operators
- Results inherit MBU/MIP floor
