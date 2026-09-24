# RRP_00_STAGE4_PROTOCOL — requirements extraction (pre-registered before execution)

**Date:** 2026-09-23. **Status:** frozen at commit; execution may not alter it. Inputs:
the nine TRANCHE-1 corpus records (adversarially verified), the constraints register
(`RRP_00_CHARTER.md` §5), and the Reverse Physics equivalences (arXiv:2111.09107).

## The claim form (every extracted requirement uses exactly this shape)

```
REQUIREMENT R<n>: <one sentence>
PHENOMENON BASIS: <corpus entries cited by domain/field/index — VERIFIED entries only;
                   TO-VERIFY entries may not be load-bearing>
FORMALIZATION RELATIVE TO: <the declared framework(s) in which the requirement is forced;
                   alternative formulations from the corpus inventoried — a requirement
                   with no surviving alternative is marked FORCED*, always starred,
                   never absolute>
STAMP: M | D | P | O   (highest gate at which the requirement is established; no
                   inference upward)
ARROW EVIDENCE: <why the phenomenon forces the structure, at the stamped gate>
WHAT WOULD REFUTE: <two-sided: a formulation that evades it, or evidence dissolving it>
STATUS: EXTRACTED -> (after refutation pass) SURVIVES-AS-STATED | SURVIVES-NARROWED |
        REFUTED | FORMULATION-RELATIVE | DUPLICATE-OF R<m>
```

## Pre-registered extraction clusters (ten; no additions mid-run)

R1 interference/superposition → composition and state-space structure
R2 no-signaling / finite causal influence → locality/propagation structure
R3 stable localized excitations → dynamical stability structure
R4 classical limit → coarse-graining/scaling structure
R5 Lorentz-like behavior → symmetry/limit structure
R6 conservation laws → invariant structure
R7 measurement statistics → operational probability structure
R8 gravity as observed → geometric/effective response structure
R9 thermodynamic irreversibility → coarse-graining + boundary-condition input structure
R10 subsystem selection → the C2/X1 meta-requirement: a candidate theory must either
    derive its decomposition/selection or price it as a declared input

## Rules

1. **Requirement relativity is mandatory.** "Reality forces X" is never written; the form
   is "given phenomena P (cited), any theory formulated in class F must have X; known
   formulation classes evading it: <list or NONE-FOUND-with-search-note>."
2. **Two-sided.** Every requirement ships with its refutation condition. An extraction
   agent that cannot state one has not extracted a requirement.
3. **Adversarial pass.** Every extracted requirement is attacked by an independent refuter
   whose instruction is to find an evading formulation (corpus alternative_formulations,
   Reverse Physics equivalences, the QG-approaches record) or to break the arrow evidence.
   Default to refuted when uncertain.
4. **Minimality pass.** Survivors are checked pairwise for derivability/duplication;
   equivalences are recorded as edges (LIMIT_RELATION / STRUCTURAL_ISOMORPHISM / etc.),
   never silently merged.
5. **Firewalls bind** (charter §5): relation ≠ space; directed update ≠ time; connectivity
   ≠ geometry; complex amplitude ≠ QM; interference ≠ Born; stable pattern ≠ particle.
6. **Nothing banks from Stage 4 alone.** The output is input to Stage 5 adjudication.

## Pre-registered legitimate outcomes

The extracted set may be: empty in a cluster; entirely COMMUNITY-known (nothing new);
non-unique (formulation-relative through and through); or dominated by R10's meta-form.
Each of these is an answer, deliverable as such. **Kill condition:** if more than half the
clusters return FORMULATION-RELATIVE with no invariant residue, Stage 5's headline is that
the "smallest structural requirement set" is not a well-posed object at current evidence —
and that conclusion ships instead of a manufactured set.
