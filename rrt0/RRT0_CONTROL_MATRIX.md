# RRT0_CONTROL_MATRIX.md
| CONTROL | CONSTRUCTION | INVARIANT PRESERVED | BROKEN STRUCTURE | MANDATORY CHECK |
|---|---|---|---|---|
| C1 permuted-coupling | apply fixed unitary P: H' = P H P^dagger, evaluate in ORIGINAL basis | spectrum, norms, symmetry class | representation-level connectivity in original basis | spec(H')==spec(H) to 1e-10 |
| C2 isospectral rewiring | H' = O diag(eig(H)) O^dagger with O random orthogonal mix, matched norms | spectrum, operator norm, param count | graph pattern in declared representation | same as C1; used for Outcome A/B/C test |
| C3 state control | 6 varied initial states incl. coherent-in-basis | dynamics identical | state-dependence of edges | all states reported, none dropped |
| C4 dynamics control | H -> H + 0.05*GUE | framework identical | specific dynamics | perturbation norm recorded |
| C5 coarse-graining | two pre-registered CG maps Gamma1, Gamma2 | — | reduction-dependence | both reported |
| C6 reconstruction | d1, d2, d3 frozen maps | — | map-dependence | agreement on held-out only |
| C7 conjugation | H' = H^T (antiunitary/conjugate dynamics) | spectrum | complex-orientation-dependent structure | mathematically defined for Hermitian H |
| C8 null | H = diagonal random (non-entangling), sector ops still applied | dimension, param count | ALL correlation/entanglement structure | must show <5% false edges |
| C9 planted positive | product-state coupling block-diagonal H with KNOWN interaction blocks A<->B | — | — | diagnostic MUST recover planted edges, Phi-delta > 5 eps, else STOP |
