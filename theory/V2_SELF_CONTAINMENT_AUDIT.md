# GRUT-RAI-v2 Self-Containment Audit (vs legacy V7)

**Date:** June 2026 (2026-06-15)
**Question:** Does v2 still rely on V7 for any load-bearing derivation? What must be
imported and re-derived to v2 standards so the v2 program / TOE book stands alone?
**Method:** read-only audit (5 parallel sector agents + 1 adversarial cross-check),
each reading the actual V7 source (`theory/GRUT_V7_FULL.md`, `GRUT_V7.md`) against the
v2 code/registry. Every "derived in V7" claim verified against the V7 text by hand.

---

## Verdict

**v2 is self-contained.** After one genuine mislabel fix (the rotation engine), there is
**no importable hard V7 dependency left**: the remaining open items are open *in V7 too*
(frontier problems, not un-ported derivations). The V7 references that remain are all
either (a) honest historical provenance, (b) correctly-labeled honest-negatives, or
(c) the bedrock constitutive form, which is native to v2.

The key discipline: a "derived in V7" label is only true if the V7 *source text* actually
derives it. Several did not — V7 itself *adopts* or *asserts* them.

---

## Sector scorecard

| Sector | v2 status | What V7 actually does | Verdict | Action |
|---|---|---|---|---|
| **Rotation engine** (`closure_protocol.nu_interpolation`, `rotation_curves.py`) | results present | V7 *adopts* MOND `ν(y)` ("matches MOND phenomenology", V7_FULL:196) — does **not** derive it | RELABEL | **FIXED** — provenance corrected (ν(y) adopted-MOND; `a₀`, `1/(1+X²)` gate native-derived) |
| **Flavor / Koide** (`koide_operator.py`) | K=2/3 native; mechanism partial | V7 §4 **derives** the *general* `z_target = z−F_spatial/F_temporal` (3 routes); V7 §29 marks the *three-flavor* `F_spatial/F_temporal` as "the missing object" | RELABEL | **FIXED** — citation split (§4 general/native vs §29 flavor/open); flavor closure is a genuine open frontier (open in V7 too) |
| **R / 3-loop anomaly coeffs** (`tji/flat_space.py`, `anomaly.py`, `osborn_epsilon.py`) | open_negative; √(4/3) canonical | V7 verifies the *topology* but admits the −100 curved-space normalization is "pending specialist calc (~3 wk)" | HONEST_NEGATIVE | none — already correctly quarantined; Path-G √(4/3) is the committed result |
| **Particulate DM / Track VII** (`relic_abundance.py`, `kibble_zurek.py`) | anchored; retracted/open | V7 §28 *adopts* U(1)_dark params + asserts a production mechanism; V7 itself states the route "has not closed" (Ω_dm ≈ 0.008, ~33× low) | HONEST_NEGATIVE | none — v2 already labels RETRACTED / open_negative; dielectric route is GRUT's position |
| **Foundations: decoherence + τ₀** (`noise_kernel.py`, `closure_protocol.py`, `tau_0_consistency.py`) | native | Six scaling laws from published Diósi–AH kernel; V7 *adopts* τ₀ (does not derive 41.9 Myr from gold benchmark) | NATIVE | none — τ₀ "V7 §18 gold-benchmark" framing already retracted (`closure_protocol.py:208`); τ₀ is v2-anchored (`1/(H₀·108π)` + Bullet Cluster). **Keep tier=computed** (it is computed given H₀) |
| **Citation hygiene** (code + book + registry) | mostly fine | book cites "companion V7" as further-reading (fine); no book *result* asserted as "derived in V7" without a v2 basis | RELABEL (minor) | the one real case (τ₀) already corrected; book V7 citations are legitimate further-reading |

---

## Cross-check findings (adversarial pass)

- The cross-check flagged `koide_theta_2_over_9_uniqueness` (tier=`computed`) as a possible
  over-claim of the rotation-curve type. **Verified by hand and REJECTED:** the tier applies
  to the *uniqueness scan* (a real computation), and both the statement ("status is CANDIDATE
  IDENTITY") and the `notes` ("algebraic mechanism tier is OPEN... above HYPOTHESIS, below
  DERIVED") disclose the candidate status transparently. Adequately labeled — **no change.**
- It also caught a wrong file path in one audit action item (`grut/foundation/rotation_curves.py`
  does not exist; the real file is `grut/derived/cosmology/rotation_curves.py`, already fixed).

---

## Genuine open frontiers (NOT importable from V7 — open in V7 too)

These are research problems, not missing ports. They are already documented as open in v2.

1. **Three-flavor `z_target` (F_spatial/F_temporal).** The flavor mechanism behind K=2/3 / the
   mass anchor. V7 §29 explicitly marks it "the missing object." **HIGH** for v2-completeness.
2. **`ν(y)` derivation.** A *no-go*: GRUT's bounded refractive enhancement (`n_g² ≤ 4/3`) cannot
   bend a flat curve (`theory/PROJECTOR_CONSISTENCY_NOGO.md`). Neither v2 nor V7 derives `ν(y)`;
   GRUT is MOND-compatible with a derived `a₀` and a derived high-ω deviation. **Structural open
   problem — do not relabel as derivable.**
3. **R_anomaly −100 curved-space normalization.** ~3 weeks specialist curved-space work (V7
   §26.2.3a). Already quarantined as open_negative; √(4/3) is the canonical R. **MED.**

---

## What changed in this audit

- `grut/foundation/closure_protocol.py` — `nu_interpolation` docstring: ν(y) labeled ADOPTED-MOND, not "derived from screening".
- `grut/toe/registry.py` — `mond_a_0_emergence` and `rotation_curves_match` statements: ν(y) adopted; `a₀` and the gate GRUT-derived.
- `grut/derived/cosmology/rotation_curves.py` — module docstring: MOND-compatible provenance block.
- `grut/derived/flavor/koide_operator.py` — `z_target` citation split (§4 native general form vs §29 open flavor instantiation).
- Tests: 165/165 pass across rotation, closure-protocol, flavor, and registry suites after all edits.

**Bottom line:** v2 does not rely on V7 for any derivation it can't stand behind. The one false
"derived" label (rotation engine) is fixed; everything else is native, correctly honest-negative,
or a frontier that V7 never closed either.
