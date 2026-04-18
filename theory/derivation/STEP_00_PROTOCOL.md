# CTP-on-S⁴ Derivation — Step 0: Protocol

**Date:** April 2026
**Authors:** D. Ryan Grover, with Claude as derivation partner
**Goal:** Derive R = |C_Cosmo / C_Final| = ε_combined(SM, M_Z) = 1.1537
from the 3-loop CTP effective action on Euclidean S⁴ with SM matter at the
electroweak matching scale, step by step.

## Purpose of this document

This records the protocol for the full derivation attempt. Each subsequent
step document (STEP_01 through STEP_N) executes one piece of the chain with
complete transparency about what is derived, what is assumed, and what
remains conditional.

The derivation proceeds in nine planned steps. Each step:

1. States its goal precisely.
2. Lists inputs (published results, prior steps, assumptions).
3. Executes the derivation symbolically where possible, numerically where
   needed.
4. States the result with explicit uncertainty or caveat.
5. Is tested against GRUT-RAI's honesty protocol before proceeding.

## The nine planned steps

| Step | Topic | Purpose |
|:---|:---|:---|
| 01 | Heat kernel on S⁴, free-field |b/a| | Establish baseline; reproduce Birrell-Davies |
| 02 | Wick rotation of Euler density | Show E₄ picks up i factor in integrated action |
| 03 | Osborn 2003 eq (36) symbolic derivation | Derive ε structure from local Callan-Symanzik |
| 04 | A × g⁴ weighting across SM gauge groups | Derive weighting from perturbative counting |
| 05 | Gibbons-Hawking thermal asymmetry | Work out forward/backward CTP branches |
| 06 | CTP assembly: C_Cosmo / C_Final | The load-bearing step — does it equal ε? |
| 07 | Scale selection: why M_Z | Matter decoupling on S⁴ with radius 1/H_inf |
| 08 | 2-loop residual estimate | Account for the 0.48% gap |
| 09 | Full synthesis and comparison | Match to ε_combined = 1.1537? |

## Honesty protocol

This derivation operates under the GRUT-RAI labeling system:

- **DERIVED**: exact, follows rigorously from the inputs
- **STRUCTURAL**: constrained by symmetry, power counting, or consistency conditions
- **ASSUMED**: taken as input from published literature with citation
- **CONDITIONAL**: depends on an assumption that could in principle fail
- **OPEN**: stated but not resolved at this step

At the end of each step, the result is labeled with one of these tags.
No step is upgraded without explicit justification.

If a step produces output that does not survive scrutiny — either
internal (fails a cross-check) or external (GRUT-RAI flags it as
unjustified) — we stop and re-anchor rather than paper over the gap.

## Tools used

- **Python 3.x** with numpy, sympy, scipy (symbolic algebra, numerical
  verification)
- **Wolfram Engine** (wolframscript) for heat kernel coefficients and
  tensor algebra where sympy is insufficient
- **Published literature** (Birrell-Davies 1982, Jack-Osborn 1990,
  Osborn 1991, Osborn 2003, Jack-Osborn 2014, Chetyrkin-Zoller 2012)

All computational steps produce scripts in `grut/derivation/` that any
reader can execute and audit. No number appears in a result document
without being reproducible from a committed script.

## What we expect to conclude

Honest prediction before we start: steps 01-04 and 08 are likely
tractable and will produce clean DERIVED or STRUCTURAL results. Steps
05-07 are the load-bearing steps where the identification R = ε is
either structurally forced or fails. Step 09 then stitches the
conclusions together.

If the derivation goes through cleanly, we have converted the R = ε
identification from a numerical coincidence (0.05% match between R_hand
and ε_combined) to a structural theorem, and the cosmological sector of
GRUT becomes SM-derived at ~0.4% residual from Planck.

If the derivation fails at some step, we learn exactly where the gap is
and whether a specialist calculation could close it.

Either outcome is honest progress. The process is the point.

## Transcendentals tracking (added after Step 1)

GRUT's hand-constructed C_FINAL contains the combination `ln(2) · ζ(3)`:

```
C_FINAL = 3(99 + 2π² + 576 ln(2) · ζ(3)) / (16384 π⁶)
```

This is not a coincidence — `ln(2) · ζ(3)` is a known 3-loop transcendental that
appears in 3-loop QCD β-functions, electron g-2 at 3-loop, and heat kernel
coefficients on curved space. The expected pattern by loop order is:

- 1-loop: rationals, π² (from 4-dim integrals)
- 2-loop: ζ(2) = π²/6, ζ(3), Li₂ values
- 3-loop: ζ(3), ζ(5), ln(2) · ζ(3), π⁴
- 4-loop: ζ(5), ζ(7), more exotic

Each subsequent step will track which transcendentals appear in intermediate
results. If the CTP-on-S⁴ derivation is physically correct, ln(2) · ζ(3) should
appear naturally at the 3-loop stage with the same structural coefficient as
in C_FINAL. This is an independent structural check, separate from the
numerical match to ε_combined.

The connection: heat kernel zeta-function regularization on S⁴ generates
ζ(3) through the Minakshisundaram-Pleijel spectral zeta function. Gibbons-
Hawking thermal sums on de Sitter produce ln(2) factors from Boltzmann
factors at the de Sitter horizon temperature. Their combination `ln(2) · ζ(3)`
at 3-loop is therefore expected, not ad hoc.

## The imaginary element — the central physical insight

The physical picture guiding this derivation (articulated in earlier
sessions) is:

1. De Sitter is conformally flat → Weyl² = 0 on S⁴ → only Euler density
   matters
2. Wick rotation E → L introduces i in the integrated Euclidean action
3. GRUT's CTP formalism makes Im(Γ_CTP) the decoherence-relevant part
4. Therefore R in GRUT is NOT Birrell-Davies |b/a| — it's the
   coupling-corrected Euler coefficient, which is Osborn's ε
5. Gibbons-Hawking thermal asymmetry makes the forward/backward CTP
   ratio equal to ε by construction
6. Matter decoupling on S⁴ forces the evaluation at M_Z
7. QCD dominance forces the A × g⁴ weighting

Each of these claims will be checked in the corresponding step. The
imaginary structure is the thread that ties them together.

---

**Next: STEP_01 — Heat kernel on S⁴, free-field |b/a|**
