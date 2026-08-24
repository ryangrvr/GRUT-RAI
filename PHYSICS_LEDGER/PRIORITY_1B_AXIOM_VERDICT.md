# Priority 1b — the admissibility verdict, and Priority 1 — the repaired rung7 evidence chain

**Date:** 2026-08-23 · PHYSICS_LEDGER · No claims.json edit. No banking.

## PRIORITY 1B VERDICT: excluded ONLY by the single-pole axiom itself

The question: is the oscillatory family excluded by an INDEPENDENT GRUT axiom, or only by the
single-pole assumption? **Answer: only by single-pole.**

The damped-oscillator kernel K(t)=e^{−γt}cos(Ωt) (χ=1/(Ω²−ω²−iγω)) was tested against every
independent GRUT constraint:

| constraint | satisfied? | verification |
|---|---|---|
| finite memory | **YES** | \|K(t)\|≤e^{−γt}; memory time 1/γ finite |
| causality | YES | poles at −γ/2 ± √(Ω²−γ²/4), both Im<0 (computed) |
| passivity | YES | Im χ>0 ∀ω>0 (computed, 500-point grid) |
| KK analyticity | YES | standard |
| KMS/FDT | YES | passive ⇒ FDT-compatible noise by construction |

**No independent GRUT axiom excludes complex-conjugate pole pairs.** The exclusion comes solely
from §1.2's "single-pole" clause — which is the axiom under test. The ToE's own §2.3 already
concedes this shape for the DOS argument ("the circularity is tight… almost no independent
evidential weight"); the no-crossing export inherits exactly that circularity.

### The sharper separation — three claims now fully distinct

1. **Finite memory ⇏ no-crossing.** The crossing kernel HAS finite memory time 1/γ.
   "Finite memory" alone does not produce the registered prediction.
2. **Single-pole ⇏ observable distinction.** Category 3 empty; nothing observed follows from
   single-pole that broader relaxational physics denies.
3. **Purely-relaxational (no oscillatory mode) ⇒ no-crossing** — the actual theorem, weaker than
   either registered claim.

**Therefore `rung7_w3`'s no-crossing export is DEFINITION-AS-TARGET AT THE AXIOM LEVEL:** GRUT
forbids crossing because GRUT assumed pure relaxation. It is not a result; it is the assumption
restated. This does not falsify the physical argument — it demotes it from "prediction" to
"consistency check of the axiom set with itself."

## PRIORITY 1 — repaired evidence chain (four items, explicitly separate)

1. **Physical passivity argument** Π=−3Hζ, ζ≥0 ⇒ one-signed (w+1): *plausible standard bulk-viscosity reasoning; NOT yet derived from the GRUT response derivation* — its support artifact (`wz_sign.py`) was definition-as-target, so it currently stands UNTESTED within GRUT.
2. **Old artifact** `wz_sign.py`: **DEFINITION-AS-TARGET** (mechanically confirmed; rival unreachable in all 14 swept configurations). Should not be cited as evidence for any claim.
3. **New numerical family result** (`rung7_discriminator.py`): purely-relaxational kernels (Debye, multi-real-pole, Cole–Cole branch cut) do NOT cross; damped oscillatory mode DOES cross (TRUE CROSSING, refinement-stable). Controls passed including corrupted-sign rejection.
4. **Vikman reproduction**: consistent with NO_GO_LEDGER entry 3; GRUT-specific sharpening — multi-mode is insufficient, the mode must be OSCILLATORY.

**Correct citation for rung7_w3 going forward:** item 4 (literature) + item 3 (family scan).
Items 1 and 2 are not evidence. The register's `to-derive` tier on w3 remains appropriate.

## What would make it a genuine prediction

An INDEPENDENT derivation that the gravitational vacuum's response is purely relaxational — i.e.,
the microscopic rung3 calculation (Σ → G_R^TT → K_R → memory spectrum) showing the self-energy
generates real-axis-only relaxation structure with no oscillatory component. Until then,
no-crossing is conditional on an un-derived axiom and cannot outrank its anchor (the register's
own rule).

## Status

Priorities 2 (boundary map) and 3 (rung8 two-band generalization) queued next session.
Priority 1b answered: the gap between architectural and phenomenological novelty is REAL at the
axiom level, and closing it runs through rung3's microscopic calculation or nothing.