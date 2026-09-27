# GR2-b — PROBE REPRESENTATION: CHARTER + PRE-REGISTRATION (frozen before evaluation)

**Fork:** GR2-b, third fork of the GR-2 campaign (Layer 2 of
`GR2_CAMPAIGN_DIRECTIVE_01.md`).
**Authority:** owner ruling of 2026-09-27 (`GR2A_OWNER_RULING_01.md`),
which authorizes GR2-b and frames its question.
**Source commits:** `master-w25bu9`; machinery replicated: the CC-1
exchange-positivity leg of `calc/cc1_ccons.py` (`17c4395`) and the GR-1
L-X pair machinery (`d827a32`). Recorded gradings cited: CC-1, U-1
(`8e3232b`), TT-1, RS-1, P-2, P-5/P-6, G-2/GS-1, CA-1, and GR2-a
(`ddcfb76`, accepted).

## 0. The question (the owner's)

> **Does the earned core select spin-2, or is spin itself another
> primitive?** Test whether *any* already-earned structural property
> distinguishes representation class, across scalar ↔ vector ↔ massless
> vector ↔ spin-2, in a common admissible response/influence framework.
> The desired output is whether the map (influence structure → probe
> representation) is injective enough to select spin — not "spin-2 wins."

## 1. Delta over the record

- CC-1 tested vector and spin-2 exchange (massless vs massive, conserved
  vs not). GR2-b adds the **scalar rows** — the representation CC-1 never
  tested — and runs the battery as a **survivor count over a six-candidate
  representation family** in one framework.
- New mechanical content: (i) the scalar exchange rows; (ii) the static
  exchange **sign table** (attraction/repulsion), locating the classic
  spin discriminators explicitly outside the record; (iii) an access-leg
  demonstration that density-, current-, and stress-type coupling seeds
  each generate canonical closures (sp(6) Lie closure), so access admits
  every representation's source; (iv) the injectivity statement for I3.

## 2. The candidate family (common framework, frozen)

Each probe couples linearly to a local source of the retained sector:

| candidate | source type | mass |
|---|---|---|
| scalar | density $\rho$ (mass-modulation type) | massless / massive (2 rows) |
| vector | current $j^\mu$ | massless / massive (Proca) |
| spin-2 | stress $T^{\mu\nu}$ | massless / massive (Fierz–Pauli) |

## 3. The gates (frozen, mechanical)

**Controls (halt-grade; exact RNG replication of CC-1's L-P leg, seed
20260925, loops in recorded order; targets from `CC1_CCONS_RESULT.json`
at full precision, $|\Delta|<10^{-9}$):**
- RC-1 vector conserved min residue 0.00945472594605436 (and dev $<10^{-12}$);
- RC-2 vector non-conserved min −10.617825792867652;
- RC-3 spin-2 conserved min 0.016561276082769805 (dev $<10^{-10}$);
- RC-4 spin-2 non-conserved min −17.818443050769414;
- RC-5 Proca min 0.29456006917729094; RC-6 Fierz–Pauli min 1.5305026792418885.
- RL-1 the L-X stress-source pair slope equals the recorded
  8.005419679013105 ($|\Delta|<10^{-9}$).

**New scalar rows (fresh RNG stream, same seed, disclosed; predictions
analytic — the scalar numerator is $\rho^2$):**
- S-1 massless scalar, arbitrary (unconstrained) sources: min residue ≥ 0.
- S-2 massive scalar, arbitrary sources: min residue ≥ 0.
  (Positivity never constrains the scalar's source: the
  conservation-for-masslessness tie is a spin ≥ 1 phenomenon.)

**Influence leg (L-X machinery; distinguishability without prohibition):**
- I-1 induced pair-channel $J(w)\ge0$ on the scan for both the
  density-source and stress-source candidates.
- I-2 the two candidates occupy different classes: density slope within
  ±0.2 of 0; stress slope = the recorded class-8 value. The influence
  data *distinguish* representations; the cone *forbids* none.

**Access leg (sp(6) Lie closures on the 3-site chain, pins 0.3):**
- A-1/A-2/A-3 the density, current, and stress seeds each generate, with
  $H$, a bracket-closed subalgebra of sp(6): dimension stable within 8
  sweeps, closure defect $<10^{-8}$ (dimensions reported, not gated —
  P-6's recorded finding, "the seed is a supplied input, not dynamically
  selected", is cited, not re-adjudicated).

**Static sign table (deterministic; frozen predictions):**
- N-1 static exchange between like sources: scalar **attractive** (+),
  massless vector **repulsive** (−), massless spin-2 **attractive** (+)
  (D = 4 numerators 1, $\eta_{00}$, $\tfrac12$ for static sources).

**The verdict gates:**
- V-1 (earned layer): the number of candidates eliminated by the earned
  tests (locality, cone/exchange positivity, access, recovered geometry)
  is **0** — all six survive everything earned.
- V-2 (conditional supplied layer, statuses tagged as the record grades
  them): imposing the record's supplied set {masslessness, Lorentz/gauge
  structure} with positivity ties spin ≥ 1 to conserved sources
  (RC-2/RC-4) but leaves **at least two representation classes standing,
  scalar and spin-2 among them**: the map is not injective.

**Ungated notes:** recovered geometry is probe-blind by construction
(CA-1 leg 1; CP-1 L-G2); universal reach and clock universality are
conditional/supplied per U-1 (cited, not re-run); and the classic
eliminators of the survivors — universal **attraction** (removes the
vector) and **light bending** (removes the scalar; Nordström-type scalar
gravity fails empirically, not structurally) — are **empirical inputs
found nowhere in the record's earned or supplied layers**.

## 4. Outcome rule (frozen, mechanical)

- **B-SPIN-NOT-SELECTED** iff every gate holds: no earned structure
  distinguishes representation class except to *label* it through the
  influence data; the supplied layer ties masslessness of spin ≥ 1 to
  conservation but does not select spin; at least scalar and spin-2
  survive everything the record earns or supplies; the further
  elimination down to spin-2 requires empirical inputs external to the
  record. Consequence: **I3 (the probe) is sharpened as an irreducible
  primitive at this level — the representation-degeneracy demonstration
  half of its certificate, feeding C4 and Layer 7.**
- **B-SPIN-SELECTED-IN-CLASS** iff V-1 fails with exactly the spin-2
  candidates surviving an earned test.
- **B-PARTIAL** for any other gate failure; halt on any RC miss.

Under every outcome: no red gate is touched; RS-1's and TT-1's recorded
conditional results stand; no public-record status moves. **HARD STOP**
after the verdict, pending owner ruling.

## 5. Instrument contract

`calc/gr2b_probe.py`: pure Python 3 standard library (helpers imported
from the committed `cc1_ccons` and `partition_selection_p1` modules,
unchanged), deterministic, single run, no post-hoc tuning; writes
`GR2B_PROBE_RESULT.json` (sha-hashed) at the repository root; verdict
assembled from measured variables; runtime seconds. Scope: D = 4
exchange kinematics as in CC-1; the 1D L-X pair channel; the 3-site
classical chain for closures. Spin content beyond spin-2, multi-probe
mixtures, and sector universality are out of scope (GR2-c, GR2-d).
