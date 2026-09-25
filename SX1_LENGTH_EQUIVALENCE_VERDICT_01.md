# SX-1 — CAN Sel-4x (CONSTANT LENGTH RESCALING = PURE UNIT CHANGE) BE SELECTED? VERDICT

**Date:** 2026-09-25 · **Charter:** `SX1_LENGTH_EQUIVALENCE_CHARTER_01.md`
(frozen at `3857e64` before the run) · **Authority:** owner direction
after the GS-1 ruling (Issue #2 comment 5837782502) · **Instrument:**
`calc/sx1_length.py` · **Artifact:** `SX1_LENGTH_RESULT.json` (sha
`09195f70a1a819a1…`) · **Battery 23/23, zero failures, zero halts,
single run, no defects.** Halt-grade identities held: the co-stretch
data identity to 2.4e-15 and the single-site counterexample identity to
1.3e-14. None of the forbidden selectors appears anywhere.

## VERDICT

> **Sel-4x is NOT derived. IRREDUCIBLE INPUT for selection;
> CLASS-SPLIT by access for decidability.**
>
> - **Classification (a data identity):** a uniform *co-stretch*, in
>   which every coupling including the intrinsic-scale-setting pins is
>   rescaled, **is** a pure unit change. All dimensionless accessible
>   data are invariant to 2.4e-15. This is dimensional analysis made
>   operational, not a selection.
> - **The general hypothesis is false:** a constant rescaling of
>   spatial couplings is **not necessarily** a unit change. A *rigid
>   stretch* (springs rescaled, intrinsic scale held fixed) is
>   observable (|Δ𝒟| = 0.013).
> - **Selection:** the rigid stretch, the anisotropic deformation and
>   the inhomogeneous deformation are **all earned-admissible**. Earned
>   structure *detects* which one a probe performed, but *forbids*
>   none. Sel-4x reduces to the **co-stretch declaration**: *a constant
>   probe rescales every scale, intrinsic ones included.*
> - **Decidability:** the owner's counterexample survives under limited
>   access and is separated under full access.

## WHAT THE RUN SHOWED

| Constant spatial action (λ = 1.3) | |Δ𝒟| | Unit change? | 𝔠_full |
|---|---|---|---|
| co-stretch (springs and pins ÷ λ) | 2.4e-15 | **yes** (identity) | admits |
| rigid stretch (springs ÷ λ, pins fixed) | 0.013 | **no**, observable | admits |
| anisotropic (x-springs ÷ λ) | 0.094 (anisotropy ratio 1.094) | no | admits |
| inhomogeneous (half the grid ÷ λ) | 0.181 | no | admits |

**1. "Constant length rescaling" is ambiguous, and the ambiguity is
the whole content of Sel-4x.** A sector with two intrinsic scales, here
the lattice step and the correlation length ξ² = k/p, can be
"uniformly stretched" in two physically different ways:
- if both scales stretch together, it is a unit change;
- if only the geometric couplings stretch, the ratio of the two scales
  changes, and that is observable.

Deciding which one a constant probe performs is exactly the choice
Sel-4x makes. With only one intrinsic scale the ambiguity disappears:
any uniform rescaling is then a unit change. That is why EQ-1's
single-scale continuum found the constant geometric coupling
invisible.

**2. Earned structure detects but does not forbid.** Every action in
the table is PSD, so 𝔠_full admits it. The dimensionless
metric/dynamic data identify which one happened. Graph-integer hop
geometry sees none of them: they change weights, not the graph. It is
the metric and dynamic data from G-2 and GS-1 that carry the
distinction. Detection is not selection.

**3. The owner's counterexample survives under limited access.**
Accessed at one site of the GS-1 path:
- description 1 is a pure unit change (K/λ);
- description 2 is the same unit change plus a non-isometric interior
  deformation (site a now couples to node 2 with weight 0.30).

They produce **identical accessible data** (1.3e-14). Full access
separates them (6.05). So "unit change" versus "unit change plus
physical deformation" is **undecidable under limited access and
decidable under full access**. This is the same access line GS-1 drew.

## STRENGTH AND LIMITS (stated plainly)

- **The classification leg is dimensional analysis.** Its value is
  operationalizing "unit change" as dimensionless-data invariance, so
  the rest of the test has a sharp discriminator.
- **The finding needs at least two intrinsic scales.** For
  single-scale sectors, Sel-4x is vacuous: every uniform rescaling is
  a unit change.
- **Scope:** Gaussian networks (a 6×6 periodic grid and a 3-site path),
  with a single rescaling factor λ = 1.3.
- **Separate from the TT question.** The rigid-scale case is where a
  *time-dependent* geometric probe can act non-trivially (EQ-1's pair
  vertex came from time dependence). SX-1 addresses the constant limit
  only, and does not reopen the ω⁷ class or the TT channel.

## LEDGER

- **κ:** discharged.
- **C_cons:** irreducible, reduced to the supplied massless
  gauge/Lorentz probe.
- **Universality:** derived under exchange; universal reach supplied.
- **Retained sector:** conditional on CARRIER plus the supplied probe;
  the class is selected.
- **CARRIER:** access-seed coincidence, supplied.
- **Geometry:** CLASS-SPLIT / access-relative (GS-1).
- **Sel-4x:** IRREDUCIBLE, reduced to the co-stretch declaration.
  Decidable under full access, undecidable under limited access.
- GeoInv unearned. **Class-4 OPEN.**

ω⁷ not used. GR-1 3D red. ℏ located. D = 4 TT/ξ and operator ordering
fenced.

## HARD STOP

Hard stop after the Sel-4x verdict, as chartered. The spatial coupling
question underneath the graviton channel is now classified: *a constant
length action is a unit change only if it co-stretches every intrinsic
scale, and that is a supplied declaration.* This is the premise the
D = 4 TT/ξ attack would inherit, when the owner rules.
