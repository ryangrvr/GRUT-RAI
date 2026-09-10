# CUTOFF_REFERENT_AUDIT_01 (lab artifact)

Commit: `0cf4a9a76faab2e4ed1fb819938ef1dbd4aa9121`

## Referent families found within cutoff/separation-scale occurrences

- **memory_temporal**: 38 statement(s)
- **Lambda_UV**: 34 statement(s)
- **Pi_mode**: 22 statement(s)
- **H_SxB**: 19 statement(s)
- **mu_RG**: 4 statement(s)

## Status histogram

- SAME_REFERENT: 98
- UNRESOLVED_REFERENT: 7

## Transport/self-energy object typing (occurrence counts, co-occurrence is NOT identity)

- response_kernel: 97
- mori_zwanzig_kernel: 82
- full_retarded_self_energy: 81
- noise_kernel: 46
- symmetrized_correlation: 26
- kubo_mori_correlation: 21
- friction_kernel: 13
- free_bath_correlator: 7

## September 3 contradiction — verbatim, preserved NOT reconciled

### Statement A — WALL_KR_U3_SCALE_SPLIT_CORRECTION.md:70-78 (fd6d6fd, 2026-09-03 00:04:10, unretracted)
> 70: 
> 71: ## THE CATEGORY-IMPORT HAZARD — NOW VERIFIED, NOT ALLEGED
> 72: 
> 73: Importing the foundations-of-QM preferred-factorization problem into an EFT program whose split
> 74: is a **cutoff choice** inflates the difficulty of GRUT's actual problem and **mislabels a
> 75: solved-enough question as "the deepest frontier."**
> 76: 
> 77: I contributed to that inflation in `6675d1c` and `f5a9e69`. The correction is recorded rather
> 78: than quietly absorbed.

### Statement B — WALL_KR_U3_EFT_BASELINE.md:20-30 (9b9036b, 2026-09-03 00:09:30)
> 20: - **No momentum shell, no band, no fast-mode cutoff** anywhere in the ledger.
> 21: - Regularization is *"dimensional continuation ONLY; NO explicit IR scale."*
> 22: - The operation performed is a **one-loop self-energy**, not a Wilsonian RG step.
> 23: 
> 24: **Category: NOT B (Wilsonian momentum-shell).** The implemented split is the **external-leg vs
> 25: internal-line partition** of a one-loop influence-functional calculation — closest to **E/H**: a
> 26: *diagrammatic* partition described in scale/mode language.
> 27: 
> 28: **The consequence that matters: there is no cutoff parameter whose placement could be varied.**
> 29: The loop integrates **all** internal momenta, soft ones included.
> 30: 

### Adjudication-relevant observations (mechanical, not conclusive)

- A calls the split a 'cutoff choice' WITHOUT specifying which mathematical object 'cutoff' denotes (NOT SPECIFIED).
- B explicitly rejects the WILSONIAN momentum-shell referent ('NOT B (Wilsonian momentum-shell)') and asserts 'no cutoff parameter whose placement could be varied'.
- Therefore B's denial is, on its face, scoped to the Wilsonian/momentum-shell referent; A's assertion is unscoped. Whether A's 'cutoff' means the same thing B denies is NOT determined by the corpus.
- Corpus itself (DEPENDENCY_EQUIVALENCE_AUDIT_01.md §6) records the same three-way fork and forbids choosing.

### Status

- same_object: UNRESOLVED_REFERENT · supersession: UNRESOLVED · genuine_contradiction: UNRESOLVED

## Transport objects (item 7)

The corpus distinguishes (in the single-pole ANCHOR node) 'committing the system/bath partition yields only the FREE bath correlator' vs 'Sigma additionally needs the bath's INTERNAL dynamics' — i.e. it explicitly treats free-bath-correlator and full-transport-self-energy as DIFFERENT inputs in that passage. This is corpus-level DISTINCT evidence for that specific pair of objects (not a general theorem).