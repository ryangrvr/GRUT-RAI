# RRT0_TEST_MATRIX.md
| TEST ID | PURPOSE | INPUTS | EXPECTED BEHAVIOR | PASS | FAIL | NEGATIVE CONTROL | VALIDATION ROUTE |
|---|---|---|---|---|---|---|---|
| T01 | H0 nontriviality | primary seed, E_int | 1 < #classes < #states | #classes in (1,S) | trivial partition | null model | recomputed with independent route B implementation |
| T02 | internal-operation reproducibility | E_alpha at two amplitudes | monotone response in lam | monotone or saturated consistently | non-monotone anomaly | lam=0 must give exactly zero response | route B recomputation |
| T03 | relabeling invariance | permutation of basis labels | diagnostics identical up to relabel | identical Phi multiset | differs | permuted control | exact assert |
| T04 | representation invariance | different operator basis | same edge set | identical edges | differs | — | route B |
| T05 | influence detection | primary model | Phi computed for all ordered pairs | finite, reproducible | NaN/irreproducible | lam=0 | route B |
| T06 | threshold stability | epsilon ladder | edge count monotone in epsilon | monotone | non-monotone jump > 20% | — | ladder report |
| T07 | state robustness | 6 initial states | edge set stable >=4/6 | >=4/6 agreement | <4/6 | varied-state control | held-out states |
| T08 | dynamics robustness | H + small perturbation | edge set largely stable | >=70% Jaccard | <70% | perturbed control | held-out perturbations |
| T09 | coupling rearrangement | permuted-coupling control | classified Outcome A-E | classification reported | crash/NaN | — | — |
| T10 | null calibration | structureless null | <5% false edges | <5% at all eps | >=5% | — | STOP AND REPAIR if fail |
| T11 | planted positive | planted model | planted edges recovered | >=95% recovery, Phi-delta > 5 eps | <95% | — | STOP AND REPAIR if fail |
| T12 | coarse-graining stability | two CG variants | influence stable | Jaccard >=0.7 | <0.7 | — | — |
| T13 | reconstruction independence | d1,d2,d3 | held-out Spearman reported | reported honestly | — | — | held-out pairs only |
| T14 | recurrence/finite-size | T_obs window | recurrence time recorded | recorded | — | — | — |
| T15 | precision/convergence | dt, lam ladders | residual error estimated | delta < epsilon/2 between ladder rungs | larger | — | ladder report |
| T16 | held-out prediction | edge set from half A predicts half B | predictive utility quantified | AUC > 0.6 OR honestly FAILED | — | null AUC | held-out only |
