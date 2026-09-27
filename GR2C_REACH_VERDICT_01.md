# GR2-c — VERDICT

**Date:** 2026-09-27 · **Charter:** `GR2C_REACH_CHARTER_01.md`, frozen at
`c12edfd` **before** implementation and run · **Authority:**
`GR2B_OWNER_RULING_01.md` (GR2-c authorization, before GR2-d by
dependency order), under `GR2_CAMPAIGN_DIRECTIVE_01.md` Layer 3 ·
**Instrument:** `calc/gr2c_reach.py` (pure stdlib; helpers imported
unchanged from the committed U-1 and s41 modules) · **Artifact:**
`GR2C_REACH_RESULT.json` (sha `452a052b7de81cf1…`) · **Battery: 16/16
gated checks, zero failures, zero halts, in the recorded run.**

## THE VERDICT — C-REACH-NOT-FORCED

> **Nothing genuinely earned by the GRUT core forces every retained
> sector to couple universally to the proposed gravitational response.
> The earned admissibility battery — the joint influence cone, exchange
> positivity, recovered geometry, per-sector unit structure — eliminates
> 0 of the 14 non-universal coupling assignments tested. The joint cone
> is rank-1 PSD for every real coupling vector, so it does not force a
> common coupling sign, let alone a common magnitude; the exchange
> machinery functions identically at unequal couplings; the recovered
> geometry is blind to the assignment; and joint access *observes*
> non-universality (graded in the deviation) without forbidding it. The
> only forcing of g_A = g_B anywhere in the record is the supplied
> massless gauge structure, and it acts only on sectors that exchange
> energy-momentum — while reach into the exchange-coupled component is
> itself supplied (U-1's recorded residual). Universal reach is another
> primitive.**

## The findings

1. **The joint cone admits every assignment.** For $C_{ij}(w) = g_i g_j
   J_0(w)$ ($J_0$ = the record's stress-source pair kernel, RL-1
   replicated at 8.005419679013105), the minimum eigenvalue is
   $\ge -10^{-12}\lambda_{\max}$ across a grid that includes
   $(1, 0.1, 10)$, the sign-non-universal $(1, -0.7, 0.2)$, and the
   zero-coupling $(2, 0, 1)$ — rank-1 positivity is an algebraic
   identity in the coupling vector. The earned cone contributes **zero
   selection pressure** toward $g_1 = g_2 = \dots = g_N$.
2. **Exchanging sectors pass every earned gate at unequal couplings.**
   On the U-1 dynamical-probe system (replicated to full precision:
   2.1708000000000003 and 0.30270478920041 at the record's own —
   already unequal — $(0.3, 0.18)$), the pairs $(0.3, 0.03)$ and
   $(0.3, 0.6)$ sustain the exchange channel and keep the ground-state
   two-time Gram PSD exactly as the equal pair $(0.3, 0.3)$ does. U-1's
   class-II forcing is therefore located **entirely in the supplied
   gauge layer** (replicated: variation ≥ 0.1297 for unequal vs
   8.9e-16 for equal couplings), not in anything earned.
3. **The recovered geometry cannot see the assignment.** The
   interaction graph of $H + hO_\varepsilon$ equals that of $H$ for
   every $\varepsilon \in \{0.3, 0.6, 0.9, 1.5\}$, and the normalized
   spectral shape is invariant under overall rescale (4.7e-15) — the
   earned geometry registers neither coupling ratios nor an absolute
   coupling.
4. **Observable ≠ forbidden — the compatible/selected distinction made
   mechanical.** Joint access resolves non-universality with a graded
   discriminator: $\Delta(0.3) = 0.0798 > \Delta(0.6) = 0.0495 >
   \Delta(0.9) = 0.0119$, vanishing at the universal point (1.8e-14,
   RU-1). Distinguishability is labeling; no admissibility test fails.
   Passing at the universal rows $(1,1,1)$ and $(0.3,0.3)$ demonstrates
   compatibility only — the owner's warning, gated as frozen.
5. **The empirical firewall held.** The eliminators of non-universal
   reach — universal attraction, light bending, Eötvös-type
   universality — are empirical inputs found nowhere in the record's
   earned or supplied layers, and this fork did **not** introduce them
   as domain data (the owner's rule, recorded frozen and ungated).

## Consequence for the inventory and the campaign

**The reach coordinate is sharpened as an irreducible primitive at this
level.** The record's grading — universal reach *supplied*; universality
then *derived under exchange* (U-1) — stands, with its premises now
located constructively: the derivation's entire forcing power comes from
the supplied gauge structure plus the supplied claim that every sector
sits in the exchange-coupled component. This is the demonstration half
of an irreducibility certificate for the reach coordinate (completion
problem C4), feeding the campaign's Layer 7. The arc so far:
continuum/influence core ⇏ specific coupling (GR2-a) ⇏ specific spin
(GR2-b) ⇏ universal reach (GR2-c). What remains is the causal cone
(GR2-d).

## Defect history (disclosed)

Run 1 (same date, not committed) breached the J-2 analytic identity: the
spectrum of the rank-1 $C(w)$ must be $\{|g|^2 J_0, 0, 0\}$, and the
measured relative deviation was 2.0 — exactly the raw-diagonal
signature. Cause: `jacobi_eig`'s convergence tolerance is **absolute**
(1e-12) while $C(w)$'s entries are of order $J_0 \sim
10^{-13}..10^{-11}$, so the solver returned the unrotated diagonal, and
run 1's J-1 pass was therefore vacuous. **Instrument bug, never
physics** — every control and every gate outside the J leg passed
identically in run 1. Repair: the matrix is normalized by its largest
entry before `jacobi_eig` and the eigenvalues rescaled (the
decomposition is scale-invariant). **No gate threshold changed.** The
recorded run is run 2; the history is in the artifact's
`defect_history` field. This is the second time the campaign's
identity-gate discipline (added after GR2-b's run-1 defect) caught a
solver-scaling bug before it could fake a physics result.

## What this does not do

- It does not weaken U-1: the DERIVED-IN-CLASS status for exchanging
  sectors under the supplied gauge structure **stands** — this fork
  locates its premises, it does not remove them.
- It does not evaluate the causal cone (GR2-d), larger sector counts,
  or probe mixtures.
- No red gate is touched; no public-record status moves; the public
  paper is **not** updated (explicit owner instruction). **Scope:** the
  U-1 ladder (L = 3) and two-sector+probe (80-dim) systems; N = 3 in
  the joint cone leg; the L-X pair channel as $J_0$; the D = 4
  soft-emission algebra.

**HARD STOP.** Verdict recorded pending owner ruling. The remaining
authorized fork is GR2-d: does the influence/access/geometry machinery
itself generate a universal causal cone, or is the underdetermination
demonstrable?
