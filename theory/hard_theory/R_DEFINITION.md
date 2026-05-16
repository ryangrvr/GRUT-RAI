# R Definition (OR4)

## Domain
- round Euclidean S4
- conformally flat
- Weyl^2 = 0
- Euler density survives

## Definition
- R is defined only as a protected Euler-channel anomaly quotient.
- R is not currently defined as C_Cosmo/C_Final unless C_Cosmo is mapped to a protected Euler-channel source.
- R is not an Im-log/curvature-log quotient unless a CTP->Euler projection is derived.

## Allowed route
- R_log_box_R is the current Euler-channel protected kernel candidate.
- Weyl_log_box_Weyl is blocked on round S4 without off-shell continuation.
- Im_log_minus_box_i_epsilon is blocked without a CTP->Euler bridge.

## Current status
- unique numeric R cannot yet be computed.
- coefficient symbols may be bound only to Euler-channel roles.
- physical R claim is forbidden.

## Freeze note — 2026-05-07
OR1–OR6 + P1–P11 + Stage12 passed (861 tests, 0 failures).
Symbolic Euler-channel R quotient exists and is legally constructed.
Numeric R remains forbidden: coefficient values are null.
The protected symbolic ratio C_Euler_cosmo / C_Euler_final is the only
current legal form of R in this domain.

## Two-loop separation note
The 2-loop result (≈1.1498 from nearby anomaly ratio / Path-D / Osborn)
is a separate extraction route. It must NOT be merged into the 3-loop
Euler-channel route until both coefficient values are independently
computed and compared. Treat as: independent 2-loop result / nearby
anomaly-ratio finding — not proof of the 3-loop value.

## Next required action
Provide explicit Euler-channel coefficient values via the landing interface:
  grut/hard_theory/s4_ctp_solver/euler_coefficient_landing.py
Source: Mathematica + HypExp evaluation of the target integral
  ∫₋₁¹ [₂F₁(h₊,h₋;D/2;(1+Z)/2)]³ (1-Z²)^{(D-3)/2} dZ
  with D = 4-2ε, massless limit, Laurent extraction to ε⁰.
See: theory/hard_theory/HYPEXP_TARGET_NOTEBOOK.ipynb

## Sources
- theory/ZENODO_EPSILON_IDENTIFICATION.md
- grut/foundation/anomaly.py
- OR1/OR1-R1/OR2/OR3 reports (pipeline)
- grut/hard_theory/s4_ctp_solver/euler_coefficient_landing.py (landing interface)
