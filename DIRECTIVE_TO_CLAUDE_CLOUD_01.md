# DIRECTIVE TO CLAUDE CLOUD — from the adjudicator session, owner-relayed (2026-09-24)

**Authority note:** this directive is relayed by the owner, and the record
corrections it orders were owner-authorized in the adjudicator session ("apply
all necessary fixes... so they can take the reins"). Where a step touches one of
your own owner-set fences, the step names the fence and the authority explicitly.

You are working on `origin/master-w25bu9`. A parallel adjudication track you
could not see has been pushed: **`origin/adjudicator-track`** (fetch its head;
this directive is itself committed on it). It contains committed primaries you
flagged as missing, a sealed pre-registration ledger, and — critically — a
same-day refutation and repair of a verdict your charter currently instructs you
to build on. This directive was itself adversarially verified against both
branches before being sent (two independent checkers; four reference errors and
four instruction hazards found and repaired — you are reading the corrected
version).

## Step 0 — Fetch and read (in this order)

```
git fetch origin adjudicator-track
```
1. `CHANGELOG_FROM_ADJUDICATOR.md` — the complete repair log (what changed, why,
   validated check counts).
2. `rrp/rrp_adjudications/U3_COUPLING_ADJUDICATION_03.md` — the refutation of
   the "Cherenkov no-go" verdict.
3. `T2_THEOREM_GATE_AND_PREREGISTRATION_01.md` — the sealed blinded ledger
   (seal commit d2da3a5, 2026-09-24 18:37:06 −05:00). Immutable; cite, never
   edit.
4. `GRUT_SKELETON_01.md` (Version 02.1) — the physicist-facing skeleton,
   including §10 (five narrative-vs-run instances, all repaired and committed).

## Step 1 — Discharge your own provenance remedy

Your `GRUT_ONTOLOGY_RECONSTRUCTION_01.md` (line 22) states: "Three cited results
have no committed primary source," naming the commit-the-external-files remedy.
Partially executed on `adjudicator-track`:

- **Row 1 (u3_continuum_origin.py):** committed primary now exists —
  `calc/u3_continuum_origin.py` + `calc/U3_CONTINUUM_ORIGIN_RESULT.json` (6/6).
  The t^(−d) vs t^(−d/2) inconsistency you carried is fixed at source (stale
  docstring corrected; the body always derived −d/2).
- **Row 3 (gravity-as-bath "spectrally viable" / acoustic-Cherenkov
  disderivation record):** committed primaries now exist —
  `calc/u3_gravity_bath_spectral_match.py` + RESULT (8/9; the one FAIL is
  `B3_discrete_box_kernel_matches_continuum_in_accessible_window`, banked in the
  RESULT itself as a box-floor instrumentation limit — carry that identity with
  any citation of the 8/9) and `calc/u3_resistive_graviton_coupling.py` + RESULT
  (v3, 20/20). **The Cherenkov-disderivation half of this row is superseded —
  see Step 2.**
- **Row 2 (the ℏ-emergence attempt):** no primary on adjudicator-track either;
  it remains EXTERNAL-RECORD.

Action: amend the EXTERNAL-RECORD markings for rows 1 and 3 to cite
`origin/adjudicator-track` (head) with the file paths above; historical anchors
you may also cite: repair-set commit 5f5395e, seal commit d2da3a5.

## Step 2 — Correct the stale premise (critical; your charter carries it)

Your `ONTOLOGY_RECONSTRUCTION_CHARTER_01.md` (line 79) instructs: "the acoustic
Cherenkov channel was disderived. Preserve those constraints. Find physically
admissible channels rather than forcing the acoustic one." — and its method
section (line ~121) lists "the Cherenkov disderivation records" among the
evidence to mine. **The disderivation verdict was refuted the same evening it
was produced** (`U3_COUPLING_ADJUDICATION_03` on adjudicator-track):

- The no-go inequality ω_q + ω_q′ < |q+q′| = k_par holds ONLY for same-sign
  (co-propagating) pairs; counter-propagating pairs reach any ω at small k_par —
  verified by tolerance-free root-finding, 16/16 exact interior on-shell roots
  at machine precision.
- The "decisive" V1b control lacked the golden-rule 1/(2dω) normalization: an
  OPEN channel's windowed weight scales ∝ dω, which was misread as emptiness.
  V1b's own recorded numbers give a convergent finite density W/dω ≈ 2.5e-5.
- The instrument's vertex had also been mutilated (kinetic stress term removed);
  T_xx carries both kinetic and potential terms, and their near-cancellation for
  counter-propagating pairs (matter tracelessness) is the central mechanism.

The repaired instrument (v3, committed, 20/20) gives: **acoustic channel OPEN;
J ~ ω⁷ in its declared convention — measured ω^7.008 against its own
pre-registered 7 ± 0.15, sitting equally inside the sealed ledger's G5 figure
(7.00 ± 0.05 under the propagator convention; the ±0.15 is the instrument's
tolerance, not the sealed ledger's) — coefficient ratio 1.0005 vs the analytic
asymptote; kernel class t⁻⁸; mechanism identified by counterfactual controls
(kinetic-only → ω^3.003, potential-only → ω^3.006, full bracket → ω⁷;
linear-dispersion and lattice-sine vertices → exact zeros).**

Actions (all in YOUR OWN files — do not edit the owner charter):
1. Write a standalone `CHERENKOV_RECORD_CORRECTION_01.md` on your branch: quote
   charter line 79 **from the file itself** (not from this directive), state
   that the disderivation was refuted post-charter, and cite
   `U3_COUPLING_ADJUDICATION_03` + the v3 RESULT by branch and path. Reference
   this correction note from `GRUT_ONTOLOGY_RECONSTRUCTION_01.md`.
2. Locate every entry on your branch that relies on the Cherenkov disderivation
   or on "spectral-viability-only" (grep for Cherenkov / disderiv /
   spectrally-viable — your E-list DISDERIVED entries and C-map arrows; there is
   no single "coupling row," so find the actual occurrences). Re-status each
   using YOUR owner-fixed class set: the acoustic-coupling entry moves from
   DISDERIVED to **CONDITIONALLY DERIVED** (conditions = the ledgered imports:
   κ = 1/M_Pl, retained-sector structure, minimal-stress postulate), annotated
   "derived within the minimal-stress class; class-4 gate unpassed" and ALWAYS
   paired with the v3 20/20 RESULT citation — the bare phrase
   "derived-within-class" was also the refuted first attempt's verdict string,
   and an uncited use invites conflation with that discredited run.
3. Fence acknowledgment: your owner-set fence says "do not soften DISDERIVED
   entries." This re-status is not a softening — it is a refutation-with-
   -certificate (ADJUDICATION_03 + committed 20/20 primary), executed under the
   owner authorization named at the top of this directive. Record that sentence
   with the change.
4. What survives from the old record and stays citable: same-sign channel
   closure at all ω; aligned-channel TT death (e_xx = 0); gapped-sector
   threshold emptiness (J ≡ 0 below 2Ω — the true-emptiness fingerprint).

## Step 3 — Seal-chain protection (standing rule)

Never rebase, squash, or cherry-pick the `adjudicator-track` commits; merge or
cite by hash only. Evidentiary honesty when citing the dual pre-registration:
the adjudicator side is commit-sealed (d2da3a5, 18:37:06 −05:00); the builder
side's first rebuilt run is mtime/timestamp-attested (18:49 local, recorded in
`U3_COUPLING_ADJUDICATION_02`), not commit-sealed — state the asymmetry when you
cite the timeline. The sealed file `T2_THEOREM_GATE_AND_PREREGISTRATION_01.md`
is immutable — riders and mappings go in YOUR files, citing it.

## Step 4 — Register the cross-track convergences (register, do not merge claims)

(a) **Partition/first-rung convergence.** Your P-1 regime trichotomy
(A-where-structured / B-where-symmetric / C-where-generic) and the repaired base
rung on adjudicator-track (P3 reduced-vs-full trajectory equivalence at 1.4e-16;
P4 law: realization dimension = number of DISTINCT eliminated modes, with a
degenerate-pair control returning M−1; E4a CDF-level representability) attack
the same first rung from two sides. Add one cross-reference row in your
dependency graph citing the adjudicator primaries; the shared open remainder is:
which sector, why few modes, criterion unification.

(b) **Non-stationarity rider for the T3 confrontation.** Your measured
order-unity non-stationarity (pooled best-stationary residual R = 0.516 on FRW)
becomes a RIDER on the T3 confrontation mapping specified in the sealed ledger:
the comparison of J(ω) exponent classes inside the certificate window ω ≳ 3.4H
must state the stationarity regime it assumes, and whether that window sits in
the adiabatic regime relative to your measured lags. This is a
required-statement rider, not an invalidation claim — R = 0.516 does not by
itself impugn the window comparison. Write the rider into your own
handover/register notes; do not modify the sealed ledger.

(c) **Realization-dimension citation (informational; touch nothing frozen).**
Your D-1 charter is FROZEN — change nothing in it. In your rider notes only:
record that the committed primary for realization-dimension/mode-count claims
is the repaired P4 (`calc/u3_origin_persistence.py`, adjudicator-track), and
note the symbol collision for future readers — D-1's N is the noise kernel of
the (K, N) influence-functional pair; P4's N is the realization dimension.

## Step 5 — Resume D-1 exactly as frozen

Your D-1 charter, frozen worlds, thresholds, and hard stop are sound; nothing on
the adjudicator track conflicts with them. Proceed to DISCRIMINATOR_VERDICT_01
and stop there, per your own hard stop.

## Prohibitions

- Do not modify the `calc/` primaries on `adjudicator-track` (the builder owns
  the live U3 lattice line locally; the adjudicator owns that branch).
- Do not edit owner charters or the sealed ledger; corrections and riders live
  in your own files, citing by branch/path/hash.
- Do not soften or promote any status beyond Step 2's certificated re-status:
  CONDITIONALLY DERIVED never becomes DERIVED without a new certificate; other
  DISDERIVED entries stay unsoftened.
- Do not touch fenced routes (Λ_R/Matsubara/Π_0/U5 per your own fences).
- The class-4 gate remains unpassed program-wide; nothing in this directive
  changes that.
