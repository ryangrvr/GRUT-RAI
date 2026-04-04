# Appendix U-B: Native Field Content and Degrees of Freedom

GRUT Unified-Field Program -- Phase U-B

---

## Core Result

**SINGLE SCALAR DoF**: Phi(x,t) is the only native dynamical field variable.
First-order ODE: one state per spatial point. Sparser than standard second-order field theory.

**X is external/constitutive input**: no native evolution equation. Drives Phi but not determined by Phi.

**Memory modifies operator, not field count**: CTP doubling is effective representation; Phi_- is ghost. Nonlocal kernels modify evolution law class without adding local fields.

**Extensions add only nonnative structure**: O(3) target coords, C^2 qubit, permutation labels, winding numbers — none are native vacuum field DOF.

---

## Evidence

| Regime | Native vars | DOF added? | X role | Memory |
|--------|------------|-----------|--------|--------|
| Free | Phi only | No | X=0 | None |
| Constant | Phi only | No | Parameter | None |
| Driven | Phi only | No | External | None |
| Memory | Phi (history) | No local | Input | Kernel on operator |
| O(3) | +(theta,phi) ext | Extension MIP | N/A | N/A |
| SU(2) | +rho ext | Extension MBU | N/A | N/A |

---

## Verdicts

| Verdict | Value |
|---------|-------|
| Native DOF | single_scalar_dof_natively_supported |
| Source | X_is_external_or_constitutive_input |
| Memory | memory_modifies_evolution_without_new_native_field |
| Extensions | extensions_add_only_nonnative_target_or_observable_structure |
| Authorization | authorized_to_proceed_to_UC |

**Overall: native_scalar_field_content_confirmed_with_external_source_boundary**

**U-C authorized** for action principle and variational structure audit.
