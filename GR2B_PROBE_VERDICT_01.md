# GR2-b — VERDICT

**Date:** 2026-09-27 · **Charter:** `GR2B_PROBE_CHARTER_01.md`, frozen at
`940ef46` **before** implementation and run · **Authority:**
`GR2A_OWNER_RULING_01.md` (GR2-b authorization), under
`GR2_CAMPAIGN_DIRECTIVE_01.md` Layer 2 · **Instrument:**
`calc/gr2b_probe.py` (pure stdlib; helpers imported unchanged from the
committed CC-1 module) · **Artifact:** `GR2B_PROBE_RESULT.json`
(sha `effbb5ab58a37c45…`) · **Battery: 20/20 gated checks, zero
failures, zero halts, in the recorded run.**

## THE VERDICT — B-SPIN-NOT-SELECTED

> **The earned core does not select spin-2. No earned structure —
> locality, exchange/cone positivity, access, recovered geometry —
> eliminates a single one of the six representation candidates; the
> influence data *label* representations (different exponent classes)
> but forbid none. The record's own supplied layer (masslessness,
> Lorentz/gauge structure) ties spin ≥ 1 to source conservation, yet
> still leaves scalar, vector, and spin-2 standing. The map from the
> influence structure to the probe representation is not injective, and
> the elimination down to spin-2 lives in empirical inputs — universal
> attraction, light bending — that appear nowhere in the record's earned
> or supplied layers. Spin is another primitive.**

## The findings

1. **The scalar rows are new, and positivity never touches them.** The
   CC-1 exchange machinery, replicated to full RNG-exact precision (six
   controls at $|\Delta|<10^{-9}$; e.g. the recorded −10.6178… and
   −17.8184… non-conserved violations), extends to the scalar with
   minimum residue $\ge0$ for **arbitrary** sources, massless and
   massive. The conservation-for-masslessness tie is a spin ≥ 1
   phenomenon; the cone leaves the scalar's source completely free.
2. **Influence data distinguish without forbidding.** The density-source
   candidate occupies class 0 (slope 0.0016) and the stress-source
   candidate class 8 (slope 8.0054, replicating the recorded value), and
   both induced $J(w)$ are cone-admissible. Distinguishable ≠ selected —
   the GR2-a lesson, now at representation level.
3. **Access admits every source type.** On the 3-site chain, the
   density, current, and stress seeds each generate with $H$ the full
   canonical algebra sp(6) (dim 21 of 21, closure defect
   $\lesssim10^{-14}$): every representation's coupling operator is a
   legitimate access assignment, and per P-6 (cited) the seed is a
   supplied input. Access does not select the representation.
4. **The survivor count.** Earned layer: 0 of 6 candidates eliminated.
   Supplied layer: three representation classes stand — massless scalar
   (any source), massless vector (conserved current), massless spin-2
   (conserved symmetric tensor).
5. **The classic discriminators are outside the record.** The static
   sign table (scalar +, vector −, spin-2 +) shows that removing the
   vector requires *universal attraction*, and removing the
   Nordström-type scalar requires *light bending* — both empirical data,
   neither earned nor supplied anywhere in the record.

## Consequence for the inventory and the campaign

**I3 (the probe) is sharpened as an irreducible primitive at this
level.** The representation degeneracy is now exhibited constructively
under everything the record earns and everything it supplies short of
empirical input — the demonstration half of an irreducibility
certificate for the probe coordinate (completion problem C4), feeding
the campaign's Layer 7 alongside GR2-a's coupling result. Under the
campaign's arc so far: the coupling is a primitive (GR2-a), and the
representation is a primitive (GR2-b); what remains for GR2-c/GR2-d is
reach and the cone.

## Defect history (disclosed)

Run 1 (same date, not committed) breached the analytic identity
$\dim\le\dim\mathrm{sp}(6)=21$ in the access leg (it reported dim 30 for
the density seed, and a stress-seed closure defect of 0.94): brackets
were stored unnormalized, so exponential norm growth defeated an
absolute independence tolerance. **Instrument bug, never physics** —
every gate outside the access leg passed identically in run 1. Repair:
brackets normalized, relative independence test, and the $\dim\le21$
identity added as a halt-grade gate. **No gate threshold changed.** The
recorded run is run 2; the history is in the artifact's
`defect_history` field, per the campaign's disclosed-defect convention.

## What this does not do

- It does not weaken spin-2: the spin-2 probe remains fully admissible,
  and TT-1's and RS-1's conditional results stand at recorded strength.
- It does not evaluate higher spins, probe mixtures, or cross-sector
  universality (GR2-c, GR2-d).
- No red gate is touched; no public-record status moves. **Scope:**
  D = 4 exchange kinematics as in CC-1; the 1D L-X pair channel; sp(6)
  closures on the 3-site chain.

**HARD STOP.** Verdict recorded pending owner ruling. The natural next
forks are GR2-c (does anything earned force universal reach?) and
GR2-d (can the machinery produce a common causal cone, or is the
underdetermination demonstrable?).
