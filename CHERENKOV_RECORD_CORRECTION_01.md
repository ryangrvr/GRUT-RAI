# CHERENKOV RECORD CORRECTION 01 — a charter premise refuted post-charter

**Date:** 2026-09-25 · **Executed under:** `DIRECTIVE_TO_CLAUDE_CLOUD_01.md`
(owner-relayed, adjudicator session; committed at `1dac54e`), Step 2.
**This note corrects the record in THIS session's files only; the owner
charter is not edited.**

## 1. WHAT THE CHARTER SAYS (quoted from the file itself)

`ONTOLOGY_RECONSTRUCTION_CHARTER_01.md:78-79` instructs:

> "gravity-as-bath result is currently only spectrally viable, and the
> acoustic Cherenkov channel was disderived. Preserve those"
> [line 80:] "constraints. Find physically admissible channels rather than
> forcing the acoustic one."

and its method section (lines 120–121) lists "the gravity-as-bath
spectral-viability and Cherenkov disderivation records" among the evidence
to mine.

## 2. THE DISDERIVATION WAS REFUTED THE SAME EVENING IT WAS PRODUCED

Per `rrp/rrp_adjudications/U3_COUPLING_ADJUDICATION_03.md`
(`origin/adjudicator-track`, head `90218f5`; repair-set `5f5395e`): **"Verdict
on the verdict: REFUTED. The acoustic two-phonon graviton channel is OPEN,
not kinematically empty."** Three instrument defects, all repaired:

1. **False kinematics:** ω_q + ω_q′ < |q+q′| holds only for same-sign
   (co-propagating) pairs; counter-propagating pairs reach any ω at small
   k∥ — verified by tolerance-free root-finding (16/16 exact interior
   on-shell roots at machine precision).
2. **Inverted control (V1b):** the windowed sum lacked the golden-rule
   1/(2dω) normalization; an OPEN channel's windowed weight scales ∝ dω,
   which was misread as emptiness (the recorded numbers give a convergent
   density W/dω ≈ 2.5e-5).
3. **Mutilated vertex:** the kinetic stress term had been removed; T_xx
   carries both kinetic and potential terms, and their near-cancellation
   for counter-propagating pairs (matter tracelessness) is the central
   mechanism.

**The repaired instrument** (`calc/u3_resistive_graviton_coupling.py` v3 +
RESULT, `origin/adjudicator-track`, **20/20**): acoustic channel **OPEN**;
J ~ ω⁷ in its declared convention — measured ω^7.008 against its own
pre-registered 7 ± 0.15 (the ±0.15 is the instrument's tolerance; the
sealed ledger's G5 figure is 7.00 ± 0.05 under the propagator convention);
coefficient ratio 1.0005 vs the analytic asymptote; kernel class t⁻⁸;
mechanism identified by counterfactual controls (kinetic-only → ω^3.003,
potential-only → ω^3.006, full bracket → ω⁷; linear-dispersion and
lattice-sine vertices → exact zeros).

## 3. THE RE-STATUS, IN THIS SESSION'S OWNER-FIXED CLASS SET

The acoustic-coupling entry moves from **DISDERIVED** to **CONDITIONALLY
DERIVED** — conditions = the ledgered imports: κ = 1/M_Pl, retained-sector
structure, minimal-stress postulate — annotated **"derived within the
minimal-stress class; class-4 gate unpassed"** and always paired with the
v3 20/20 RESULT citation. (Conflation guard: the bare phrase
"derived-within-class" was also the refuted first attempt's verdict string;
an uncited use invites conflation with that discredited run — hence the
mandatory pairing.)

**Fence acknowledgment (recorded with the change, per the directive):** the
owner-set fence "do not soften DISDERIVED entries" is not breached: this
re-status is not a softening — it is a **refutation-with-certificate**
(ADJUDICATION_03 + the committed 20/20 primary), executed under the owner
authorization named at the top of the directive.

## 4. WHAT SURVIVES FROM THE OLD RECORD (still citable)

Same-sign channel closure at all ω · aligned-channel TT death (e_xx = 0) ·
gapped-sector threshold emptiness (J ≡ 0 below 2Ω — the true-emptiness
fingerprint).

## 5. SEAL-CHAIN AND CITATION RULES (standing)

`adjudicator-track` commits are never rebased, squashed, or cherry-picked —
merge or cite by hash only. The sealed ledger
`T2_THEOREM_GATE_AND_PREREGISTRATION_01.md` (seal commit `d2da3a5`,
2026-09-24 18:37:06 −05:00) is immutable; riders live in this session's
files. Timeline asymmetry, stated whenever the dual pre-registration is
cited: the adjudicator side is commit-sealed; the builder side's first
rebuilt run is mtime/timestamp-attested (18:49 local, per
U3_COUPLING_ADJUDICATION_02), not commit-sealed.

## 6. DOWNSTREAM EFFECTS IN THIS SESSION'S FILES

`GRUT_ONTOLOGY_RECONSTRUCTION_01.md` carries a dated addendum discharging
provenance rows 1 and 3 and re-statusing its E-list entry per §3 above;
`RELATIONAL_ONTOLOGY_MAP_01.md` carries the cross-track convergence
addendum; the T3-confrontation rider lives in
`handover/RIDERS_2026-09-25_adjudicator.md`. The class-4 gate remains
unpassed program-wide; nothing here changes that.
