# Appendix S-B: Native Symmetries and Exact Invariants

GRUT Symmetry Program -- Phase S-B

---

## Question
What exact native symmetries and invariants does the raw GRUT scalar
memory architecture possess before any extensions?

---

## Continuous Symmetries (Track A)
| Symmetry | Status |
|----------|--------|
| Time translation | broken (dissipative arrow) |
| Spatial translation | native |
| Spatial rotation SO(3) | native |
| Boost (Lorentz) | broken (preferred frame from tau) |
| Scale | broken (tau^2=3/2 fixed) |

## Discrete Symmetries (Track B)
| Symmetry | Status |
|----------|--------|
| Z2 Phi reflection | native, exact |
| Spatial parity | native, exact |
| Charge conjugation | not applicable (real scalar) |
| Time reversal | broken (dissipative) |
| CPT closure | underdetermined |

## Lorentz (Track C)
**NATIVELY BROKEN.** tau defines preferred frame. First-order ODE not
Lorentz-covariant. Residual: spatial SO(3) + translations.

## Time Reversal (Track D)
**NATIVELY BROKEN.** tau dPhi/dt -> -tau dPhi/dt under t->-t.
Dissipation defines native arrow of time.

## Conservation (Track E)
**No standard Noether conservation.** Open-system dissipation: energy
flows out. Only dissipative balance laws. Momentum/angular momentum
underdetermined.

## Scale (Track F)
**Broken** by tau^2=3/2 and barrier amplitude. Conformal absent.

## Native Invariant Ledger (Track G)
5 exact native invariants:
1. Constitutive form invariance
2. Z2 reflection
3. Spatial isotropy SO(3)
4. Spatial translation
5. tau^2=3/2 canonical identity

## Exact Verdicts
| Verdict | Value |
|---------|-------|
| Lorentz | lorentz_invariance_natively_broken |
| Discrete | z2_reflection_native_and_exact |
| Time reversal | time_reversal_natively_broken_by_tau_dissipation |
| Conservation | dissipative_balance_laws_only |
| Authorization | authorized_to_proceed_to_SC |
| Overall Appendix P | native_canon |

**S-C (Extension-Level and Emergent Symmetries) is authorized.**
