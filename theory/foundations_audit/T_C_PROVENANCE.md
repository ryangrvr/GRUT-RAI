# T_c Provenance Audit (defensive — no corrections)

**Date:** 2026-04-28.
**Trigger:** While running the crystallization-temperature schedule
investigation (`CRYSTALLIZATION_SCHEDULE_INVESTIGATION.md`), a numerical
discrepancy surfaced: the framework's T_c = 54.7 MK does not equal
ℏ/(τ_0 × k_B) for τ_0 = 41.9 Myr.

**Methodology:** Same pattern as `TAU_0_PROVENANCE.md` and
`ALPHA_VAC_PROVENANCE.md` — audit the value's provenance, document
findings, do NOT correct until the audit is reviewed and a coordinated
correction can be made (or until the audit confirms the value is
correct under a specific convention).

---

## What the codebase has

Two related quantities are defined in `grut/foundation/closure_protocol.py`:

### MU_0_EV (line 290) — the screened local mass-gap

```python
MU_0_EV: float = (HBAR / TAU_0_SEC) / E_CHARGE
```
- Formula uses ℏ explicitly: μ_0 = ℏ/τ_0
- With τ_0 = 41.9 Myr = 1.32×10¹⁵ s:
  - μ_0 = 1.05×10⁻³⁴ / 1.32×10¹⁵ = 7.97×10⁻⁵⁰ J
  - In eV: 4.98×10⁻³¹ eV ≈ 10⁻³¹ eV
- Cited as "Phase I §6: screening maps μ_Λ → μ_0 via same S"
- Self-documented as ≈ 10⁻³¹ eV

### T_C_KELVIN (line 315) — the "boiling point of gravity"

```python
T_C_KELVIN: float = 1.0 / (TAU_0_SEC * K_B)
```
- Formula does NOT include ℏ
- With τ_0 = 41.9 Myr and k_B = 1.38×10⁻²³ J/K:
  - T_c = 1.0 / (1.32×10¹⁵ × 1.38×10⁻²³) = 5.49×10⁷ K = 54.7 MK
- Docstring: "v9 natural-units convention, ℏ = 1"
- Cited as "v9.0 'boiling point of gravity'"
- Test `test_T_c_is_54p7_MK` pins this value at 54.7 MK ± 5%

## The internal inconsistency

μ_0 and T_c are physically the same scale: T_c = μ_0/k_B if T_c is the
"thermal-frequency-equivalent-to-1/τ_0" temperature. The relation is
ℏ/τ_0 = k_B T_c, giving T_c = ℏ/(τ_0 k_B).

**The framework computes μ_0 using ℏ explicitly and computes T_c without
ℏ.** Numerically:

| Quantity | Codebase formula | Value | k_B T equivalent |
|:---|:---|:---|:---|
| μ_0 | ℏ/τ_0 | 4.98×10⁻³¹ eV | **5.78×10⁻²⁷ K** |
| T_c | 1/(τ_0 k_B) | — | **5.47×10⁷ K = 54.7 MK** |

These differ by a factor of ℏ ≈ 1.05×10⁻³⁴ (in J·s).

## What does the framework's narrative require?

The codebase docstring (line 324) states:

> **Cosmological chronology (v9.0):**
>     T > T_c  (plasma era):       gravity is local, no DM effects
>     T ≈ T_c  (~1 hour post-BB):  vacuum begins to "remember" mass
>     T << T_c (today):            deep refractive regime, n_g ≈ 1.1547

**This narrative requires T_c at MK scale.**
- T = 5×10⁷ K corresponds to cosmic age ~tens of seconds to ~hour
  (BBN-adjacent, matching "~1 hour post-BB")
- T = 5.78×10⁻²⁷ K is far below CMB (2.7 K). Universe has NEVER been
  this cold. "T_c crossing happened 1 hour post-BB" is impossible
  under this reading.

The Ch 13.4 ToE narrative ("At T_c = ℏ/(τ_0 k_B) = 54.7 MK, the vacuum
undergoes a phase transition") and the Ch 9 narrative ("T > 10⁹ K is
above T_c... explains why GRUT and ΛCDM agree during BBN") both
qualitatively work either way, but quantitatively the "~1 hour
post-BB" anchoring requires the MK reading.

## What τ_0 would give T_c = 54.7 MK self-consistently?

If T_c = ℏ/(τ_0 × k_B) is required (SI-correct formula) AND T_c = 54.7 MK,
then:

    τ_0 = ℏ/(k_B × T_c) = 1.05×10⁻³⁴ / (1.38×10⁻²³ × 5.47×10⁷)
        = 1.39×10⁻¹⁹ s

This is **femtosecond-scale** τ_0 — atomic/molecular dynamics. **No such
τ_0 exists in the framework codebase as a separate constant.** The only
τ_0 the framework defines is the cosmic-baseline τ_0 = 41.9 Myr, which
doesn't yield 54.7 MK via the SI-correct formula.

## Three possible resolutions

### (i) The codebase formula is missing ℏ — actual T_c is 5.78×10⁻²⁷ K

Under this reading:
- T_c = 54.7 MK is wrong (off by factor of ℏ).
- Correct T_c = 5.78×10⁻²⁷ K, far below any cosmic temperature.
- Cosmological chronology "T_c ≈ ~1 hour post-BB" is wrong — T_c
  has never been crossed; the universe has been below T_c always.
- Multiple chapters' prose claiming T_c = 54.7 MK needs correction.
- The qualitative picture ("BBN above T_c → memoryless regime")
  still holds under this reading, just at a vastly different scale.

### (ii) The framework intends T_c = 54.7 MK via a different mechanism

Under this reading:
- T_c = 54.7 MK is correct, but the formula T_c = 1/(τ_0 × k_B)
  in the codebase is shorthand for something else.
- Possible alternate derivation: T_c is set by some thermal-decoupling
  process not equal to ℏ/(τ_0 k_B). The "natural-units convention"
  comment in the docstring may indicate this — perhaps τ_0 in the
  natural-units formula is a different object than τ_0 in seconds.
- This would require finding the actual derivation of 54.7 MK in V7
  / V8 / Phase I documents (not in the codebase that I've audited).

### (iii) Two different τ_0 values exist for different physical contexts

Under this reading:
- Cosmic-baseline τ_0 = 41.9 Myr (the codebase's TAU_0_SEC)
- Thermal-transition τ_0 ~ 10⁻¹⁹ s (atomic-scale, not in codebase)
- T_c is computed from the thermal-transition τ_0, not the
  cosmic-baseline one.
- This would be parallel to how τ_0 = 41.9 Myr (cosmic) and the
  gold-benchmark Λ_grav at lab nanoparticles are different physical
  scales of the same medium. The framework might have a thermal-
  scale τ_0 separate from the cosmic-baseline one.

## What's NOT in the audit's scope to resolve

This audit identifies the inconsistency but does NOT determine which
resolution is correct. That requires:

1. Tracing the T_c = 54.7 MK derivation to its primary source (V7,
   V8, Phase I) and seeing whether the original derivation used a
   different τ_0 or a different formula.
2. Reviewing the v9.0 Thermodynamics chapter (referenced in the
   docstring) to see what convention was being used.
3. Specialist review on whether the framework's claimed
   cosmological-chronology narrative ("T_c ≈ 1 hour post-BB", "BBN
   above T_c") is essential or replaceable.

## Recommendation

**Do not correct T_c without coordinated review.** The bug-ish
appearance of the missing ℏ COULD be:
- A genuine units error (resolution (i))
- A v9 natural-units convention with τ_0 reinterpreted (resolution (ii))
- A second τ_0 scale not in the codebase (resolution (iii))

Each resolution has different downstream consequences:
- (i) requires updating multiple chapters' prose AND test pinning
- (ii) requires documenting the convention explicitly without changing values
- (iii) requires adding a second τ_0 to the codebase

Until the primary-source v9 derivation is reviewed, the value 54.7 MK
should NOT be changed in the codebase. The audit recommendation is to
flag this for specialist review and add a registry open_negative
documenting the inconsistency.

## Where T_c is consumed (for impact assessment)

Direct consumers of `T_C_KELVIN` and `T_C_MK`:
- `grut/foundation/closure_protocol.py` — definition + verify() test
- `grut/toe/coherence.py` — imports T_C_MK
- `grut/toe/dashboard.py` — reports "ℏ/(τ_0 k_B) ≈ 54.7 MK"
- `tests/foundation/test_closure_protocol.py` — pins value
- `theory/GRUT_TOE.md` Ch 2, 9, 13 — narrative references

Indirect consumers (use T_c qualitatively):
- BBN consistency arguments (Ch 9, 13)
- Cosmic-history chronology (Ch 13.4)
- Phase-transition narrative (Ch 13.3, 13.4)

A coordinated correction (resolution (i) or (iii)) would touch all
of the above. A documentation-only resolution ((ii)) would update
only the docstrings and audit log.

---

## Primary-source review findings (extended audit)

Following user direction to do a primary-source audit before
declaring a bug, traced T_c through V7 documentation and the
`thermal_transition.py` module:

### V7 Section 0.5 (line 141)

> "Critical temperature T_c = 54.7 MK (v9.0): The 'boiling point of
> gravity' is T_c = 1/(τ_0 k_B) ≈ 5.47 × 10⁷ K. ... Cosmological
> chronology: plasma era (T > T_c) → transition at t ≈ 1 hour →
> recombination (T ≪ T_c, full refractive regime) → today
> (n_g ≈ 1.1547)."

V7 uses the same formula `T_c = 1/(τ_0 k_B)` and gets the same value
54.7 MK. The anchor is "transition at t ≈ 1 hour post-BB."

### V7 Section (line 741)

> "The metric-memory phase transition (v9.0). The vacuum develops
> memory only below the critical temperature T_c = 1/(τ_0 k_B) ≈
> 54.7 × 10⁶ K, approximately one hour post-Big Bang. ... See
> `grut/derived/cosmology/thermal_transition.py`."

Same formula, same value. References `thermal_transition.py` module.

### `grut/derived/cosmology/thermal_transition.py`

```
T_c = 1 / (τ_0 k_B) ≈ 54.7 × 10⁶ K
... using v9 convention (natural units)
```

The module's chronology (lines 13-16) explicitly anchors:
- t ≈ 1 s post-Big Bang: T ~ 10⁹–10¹⁰ K, above T_c
- t ≈ 1 h post-Big Bang: T ~ T_c ≈ 5.5 × 10⁷ K, transition
- t ≈ 380 kyr (recombination): T ~ 3000 K ≪ T_c

**This anchoring requires T_c ≈ 5.5 × 10⁷ K** to be self-consistent.
The cosmic temperature at t = 1 hour post-BB is approximately 10⁸ K
in standard cosmology. So 54.7 MK is the INTENDED physical scale.

### Natural-units check

I checked whether the "v9 natural-units convention" salvages the
value. In natural units (ℏ = c = k_B = 1), τ_0 has units of
[1/energy]. The conversion of τ_0 = 41.9 Myr to natural units
(in eV⁻¹):

    τ_0_nat = τ_0_seconds / ℏ_in_eV·s = 1.32×10¹⁵ / 6.58×10⁻¹⁶
            = 2.0×10³⁰ eV⁻¹

Then 1/τ_0_nat = 5.0×10⁻³¹ eV ≈ 5.78×10⁻²⁷ K.

The natural-units convention does NOT rescue 54.7 MK. The same
physical scale ℏ/τ_0 emerges either way: 5.78×10⁻²⁷ K, not 54.7 MK.

**The 54.7 MK value emerges ONLY if you treat the SI numerical
operation `1.0 / (1.32×10¹⁵ × 1.38×10⁻²³)` as a temperature in
K, dropping the resulting units of K/(J·s).** This is not a valid
physical formula in either SI or natural units.

### Summary of audit findings

1. **The formula `T_c = 1/(τ_0 k_B)` (no ℏ) is dimensionally
   inconsistent.** With τ_0 in SI seconds, it produces a number
   with units K/(J·s), not K.

2. **Both V7 documentation and the codebase propagate the same
   inconsistency.** This is not a codebase typo — V7 Section 0.5,
   V7 Section 22 (line 741), `thermal_transition.py`, and
   `closure_protocol.py` all use the same formula and arrive at
   54.7 MK.

3. **The natural-units convention claim (in the docstring) does
   not salvage the value.** τ_0 converted to natural units gives
   2.0×10³⁰ eV⁻¹, and 1/τ_0_nat = 5.0×10⁻³¹ eV → 5.78×10⁻²⁷ K.
   Same answer as the SI calculation with explicit ℏ.

4. **The framework's cosmological narrative (T_c at "1 hour
   post-BB") requires T_c ~ 10⁸ K** to be self-consistent with
   standard cosmic-temperature-vs-time relations. This anchors
   the INTENDED physical scale at MK level.

5. **No τ_0 in the framework codebase yields T_c = 54.7 MK
   via the SI-correct formula T_c = ℏ/(τ_0 k_B).** That formula
   would require τ_0 ≈ 1.4×10⁻¹⁹ s — atomic-timescale, not
   gravitational-relaxation timescale, and not present in the
   codebase as a separate constant.

6. **μ_0 (computed correctly with ℏ) gives 5.78×10⁻²⁷ K when
   converted to a temperature.** This matches the SI-correct
   formula but contradicts the 54.7 MK narrative.

### What this means

The framework has **internally inconsistent treatment of T_c**:

- The narrative requires T_c at MK scale (cosmic chronology anchor)
- The formula in V7 and codebase produces 54.7 MK only through a
  dimensionally invalid numerical operation
- The SI-correct version of the same physics gives 10⁻²⁷ K
- The "v9 natural-units convention" defense doesn't hold up under
  proper dimensional analysis

There is no single resolution that makes the framework's prose,
formula, and cosmological narrative all self-consistent. Either:

- (i) **The narrative is wrong.** T_c = 5.78×10⁻²⁷ K is the physically
  correct value. The "T_c crossing at 1 hour post-BB" picture is
  wrong — the universe has been below T_c for essentially its entire
  history. The "boiling point of gravity" never gets crossed in cosmic
  evolution. This requires major revision of Ch 2, Ch 13.4, Ch 9, and
  cross-consistency tables.

- (ii) **The formula is wrong.** T_c is genuinely 54.7 MK, but this
  is set by physics other than ℏ/(τ_0 k_B) — perhaps a different
  τ_0, or a different relation entirely. This requires identifying
  what T_c actually IS in the framework, then correcting the formula
  in V7, `thermal_transition.py`, and `closure_protocol.py`.

- (iii) **Both are partially right.** The framework has TWO distinct
  T_c-like scales: a cosmological-narrative scale (~MK) and a
  formal-derivation scale (~10⁻²⁷ K). The codebase has been
  conflating them. Resolution requires distinguishing the two
  explicitly, with separate names.

### Audit verdict

**The framework's T_c value 54.7 MK is propagated through both V7
documentation and the codebase via a dimensionally inconsistent
formula. Neither the SI calculation nor the natural-units convention
yields this value from τ_0 = 41.9 Myr. The 54.7 MK value is the
"intended" physical scale per the cosmological narrative, but no
framework-derivable formula produces it.**

This is potentially a significant foundational issue, larger in
scope than the τ_0 unit error (which was a conversion typo, factor
of 1000) because the affected narrative spans multiple chapters
and downstream predictions.

### Strong recommendation: do NOT correct yet

1. **Specialist review of v9.0 Thermodynamics primary source.**
   The codebase docstring cites "v9.0 Thermodynamics" for T_c.
   Find the original v9.0 derivation. Was T_c derived from τ_0
   via a different formula? Is the 54.7 MK value independently
   established (e.g., from BBN consistency arguments) or
   derived from τ_0?

2. **Check downstream consumers for T_c-dependent predictions.**
   Specifically: η_B (baryogenesis), Ch 13.4 cosmic chronology,
   Ch 9 BBN consistency, the predictions table in Ch 1, the
   glossary entry in Appendix C. Each needs review.

3. **Decide framework posture before correcting.** The three
   resolutions (i), (ii), (iii) have different implications:
   - (i) is honest but disrupts a substantial narrative section
   - (ii) preserves the narrative but requires re-deriving T_c
   - (iii) requires renaming and disambiguation across the
     framework

4. **Add a registry open_negative.** Suggested:
   `t_c_provenance_inconsistency_open_negative` — formal
   acknowledgment that the framework's T_c value is propagated
   through a dimensionally inconsistent formula. Closure
   conditions: identify whether T_c = 54.7 MK is independently
   established or formally wrong.

### Out of scope for this audit

- Correcting any code or test
- Updating any document prose
- Re-running any T_c-dependent calculation
- Closing the crystallization-schedule investigation (held until
  T_c resolves)

---

## End of audit

**Status:** unresolved foundational issue surfaced. Inconsistency is
real and propagated through both source documents and codebase. The
"v9 natural-units convention" defense doesn't hold under dimensional
analysis. The 54.7 MK value matches the framework's cosmological
narrative anchor (T at 1 hour post-BB) but no framework-derivable
formula produces it from τ_0 = 41.9 Myr.

**Recommended next step:** specialist review of v9.0 Thermodynamics
primary source to determine whether T_c = 54.7 MK has independent
derivation (preserving the value, correcting the formula) or whether
the value should be 5.78×10⁻²⁷ K (correcting the value, requiring
multi-chapter narrative revision).

This finding should be flagged to the document-composition session.
The current GRUT_TOE.md mentions T_c = 54.7 MK in multiple places
(Ch 1 predictions table, Ch 2 Medium, Ch 4 Crystal/Fluid, Ch 9 Dark
Sector, Ch 13.3-13.4 cosmic chronology, Appendix C glossary). All
references depend on the same audit resolution.

---

## CLOSING ADDENDUM — Correction #22 (2026-04-30)

The audit's recommended resolution path (iii — two distinct τ-scales)
has been implemented as Correction #22 in the v8→v2 deposit roadmap
(Priority 1, the τ-cleanup). See
`theory/derivation/CORRECTION_22_TAU_CLEANUP.md` for the full
correction document.

**What changed.**

- `grut/foundation/closure_protocol.py` now defines `TAU_MICRO_SEC ≈
  1.396×10⁻¹⁹ s` as a separate constant alongside `TAU_0_SEC = 41.9
  Myr`. The thermal-transition temperature is recomputed via the
  SI-correct formula `T_C_KELVIN = ℏ/(τ_micro × k_B)`, with τ_micro
  defined from the empirical anchor `T_C_KELVIN_CANONICAL = 5.47×10⁷
  K` (cosmological-chronology pin: T at t ≈ 1 h post-BB).

- The numerical value 54.7 MK is preserved EXACTLY. The
  `test_T_c_is_54p7_MK` pin (5% tolerance) is unchanged. Seven new
  tests in `TestCanonicalConstants` pin the SI-correctness, the
  τ_micro value, the 34-orders-of-magnitude separation between
  scales, and the structural distinction (τ_micro ≠ τ_0).

- Registry: claim `t_c_thermal_transition` updated to reference
  τ_micro and the SI-correct formula. New claim
  `tau_micro_thermal_scale` (Ch 8, anchored tier) tracks τ_micro
  with its empirical anchor and tests. The original
  `t_c_provenance_inconsistency_open_negative` open-negative is
  retired and replaced by `t_c_provenance_inconsistency_resolved`
  (meta tier, documenting closure) and
  `tau_zero_to_tau_micro_relation_open_question` (open_negative,
  the sharper successor).

**What remains open.**

The 34-orders-of-magnitude separation between τ_0 and τ_micro is
unexplained. Four closure paths for the relation question, tracked
in `tau_zero_to_tau_micro_relation_open_question`:

1. Derive τ_micro from CTP plasma dynamics (research-tier).
2. Identify τ_micro with a known atomic/nuclear timescale (research-tier).
3. Accept that the two scales are independent — the honest-negative
   outcome that downgrades the framework's "zero free parameters in
   the predictive core" framing to "zero in gravitational core; one
   anchored in thermal sector" (registry-tier framing change).
4. BBN-mediated bridge: FALSIFIED by `bbn_thermal_buffer_negligible`
   (the 10-orders-of-magnitude shortfall rules out BBN dynamics).

**Audit verdict re-stated post-resolution.**

The original verdict — "no framework-derivable formula produces 54.7
MK from τ_0 = 41.9 Myr" — is preserved. The resolution does not
derive τ_micro from τ_0; it explicitly names τ_micro as a separate
empirically anchored constant and routes the dimensional consistency
through a SI-correct formula. The framework's load-bearing
predictions (Λ_grav, n_g(ω), bridge, cluster scaling, Hubble) all
use τ_0 unambiguously and are unaffected; the thermal sector now
carries one additional anchored input (τ_micro) until the relation
derivation closes.

This audit's status: **CLOSED at the dimensional level (Correction #22)
with the relation-derivation question explicitly tracked as a sharp
open question.**

*Closing addendum by Claude Code, 2026-04-30.*
