# H² IR-FORK — OWNER AUDIT AND RULING

**Date:** 2026-09-01 · **Instrument:** `wall_kr_h2_ir_owner_ruling.py` ·
**Artifact:** `WALL_KR_H2_IR_OWNER_RULING_RESULT.json` ·
**Battery: 23/23, zero failures.** · **Frozen inputs and register:
byte-identical.** · **No IR regulator, scale, or coefficient chosen.**
**W-0: unbanked. HARD STOP.**

## PART 0 — CORRECTION TO THE BUILDER'S OWN COMMITTED EVIDENCE

**Commit `390a22d` contained a material error, self-caught here.** Its
numeric route integrated the **c_m cone branch alone**; the retarded
response carries **both** branches.

| | single branch (what 390a22d measured) | **both branches (correct)** |
|---|---|---|
| q⁻² piece | 2ω³/15 | **cancels exactly** |
| q⁻¹ piece | −4ω²/15 | **−8ω²/15** |

- The **power** (1/δ) divergence reported in 390a22d is **not** a
  property of the retarded response — it cancels between branches.
- What **survives** is a **logarithmic** IR divergence, coefficient
  exactly **−8ω²/15** (per H², d = 3).
- Numerically confirmed independently: the cutoff ladder shows a
  **constant additive step per decade** matching −(8ω²/15)·ln 10 to
  rel 1e-6 — a textbook log, not the ≈10× multiplicative growth the
  single-branch run showed.
- In master-exponent terms: the **a = −1** (cone q⁻⁴) IR pole
  **cancels**; the **a = 0** (cone q⁻³) IR pole **survives**.

**Verdict impact: H2-B STANDS.** An IR-origin *logarithmic* pole still
contaminates the 1/(d−3) structure. Only the characterization and
strength are corrected — and the corrected form is *precisely* the
"scaleless log class" the Tier-2 fork registered in advance.

## THE QUESTION

*Does the current GRUT record independently license an IR prescription
for the H² retarded local extraction?*

## RULING: **IR-B**

**No pre-existing license — but the frozen record pre-registers the
route** by which a new owner-declared IR convention may be introduced:
fork (ii), *"named and priced (a new register input)."*

**Practical state today is identical to IR-C:** no prescription is
licensed, no declaration exists, so **c0′ and c2′ remain unresolved** and
the H² local sector stays fork-gated.

**Why not IR-A:** zero authorities license an IR prescription.
**Why not IR-C strictly:** IR-C asserts no new prescription is
*authorized* at this stage. The record does not merely leave the question
open — it **pre-registered the fork and its price**, a standing,
independently justified route for the owner to declare one. That
distinction is the only thing separating B from C here.
**Flagged for the owner, not decided:** if you intend "no new
prescription may be introduced at this stage," that is a one-line
amendment to this record and changes nothing computational.

## AUTHORITY SWEEP — 5 entries, ZERO licensing

| file | section | quote | licenses extraction? |
|---|---|---|---|
| `K_R_CONTRACT_OWNER_RULING.md` | D3 / Option-3a | *"IR: dimensional continuation ONLY; NO explicit IR scale"* | **No** |
| `K_R_CONTRACT_OWNER_RULING.md` | D3 fork trigger | *"If the calculation demonstrates an IR scale is necessary: STOP — the preregistered fork (ii) fires verbatim ('named and priced — a new register input')"* | **No** |
| `K_R_CONTRACT_DECLARATION_SHEET.md` | IR sub-choice | *"dimensional continuation only, NO explicit IR scale … any divergence appears as a pole/log to be CLASSIFIED — the honest default"* | **No** |
| `MICROSCOPIC_TARGET_BENCHMARK.md` | fork (ii) | *"an IR cutoff exists — then it must be named and priced (a new register input)"* | **No** |
| `WALL_A_A3_DECLARATIONS.md` | Decl. 1 F2 | *"MINIMAL SUBTRACTION — pole terms only"* (against the 1b basis) | **No — UV only** |

## UV vs IR, AND THE "DROP THE POLE" TEST — REJECTED

UV poles map onto the registered 1b basis; MS pole-only subtraction **is**
licensed for those. The surviving IR pole originates at q → 0 and is
**not** a UV counterterm and is **not** absorbed into c0′ or c2′.

> The claim *"the 1/(d−3) pole is discarded by MS, therefore the finite
> H² local term is defined"* **does not hold here.** Calling an IR
> subtraction "MS" merely because it is a 1/(d−3) pole is exactly the
> move this audit was instructed to test for — and it is rejected.

## SCALE-FREE RESOLUTION — ONE REAL CANCELLATION FOUND, NOT ENOUGH

A genuine cancellation was **found, not manufactured**: the power piece
cancels between cone branches. But after summing **all** branches and all
Δ-powers of the frozen cone, the log coefficient is exactly −8ω²/15 ≠ 0.
**No further cancellation is available inside the existing formalism**,
and no zero-mode subtraction, Ward identity, or observable-level
subtraction in the record removes it. A false-cancellation control
confirms the test is not vacuous.

## STATE / BOUNDARY SUFFICIENCY

The frozen declaration (D3 = 3a, BD-analogue via Option-B adiabatic)
fixes the **state** and the H-grading. It specifies **no** initial-time,
switching, box, horizon, or observation-time condition, and the frozen IR
sub-choice explicitly refuses a scale. **Insufficient** to single out an
IR prescription — recorded as part of the fork, **not** patched with a
new state assumption.

## SCALE FIREWALL

Nine regulators (q_min, H as an ad hoc cutoff, 1/T, box size, horizon
radius, observational frequency, WC, Λ_R, μ) are each mathematically
capable of regulating the log. **None is licensed by any authority in the
sweep. None is adopted.** Each is recorded solely as a candidate
requiring a **new owner decision**.

## THE CONDITIONAL c0′ STATEMENT — REVIEWED, NOT PROMOTED

Still conditionally valid *in form* (the scale-free structure is
unchanged by the correction), but its premise is now sharper: the
extraction would have to be licensed for an **IR-log-divergent**
integral, and any prescription regulating that log generically
introduces its own scale, which can feed the ω⁰ slot. **Not promoted.**

## PARAMETER COUNT

H⁰ unchanged at **one** (Λ_R), read back from the certified ledger. H²
stays **outside** the count. If an IR prescription is later declared it
must be classified then: one that merely regulates may leave the count
unchanged; one introducing a physical IR scale is a **new input** and
must be counted. **No IR scale is hidden inside Λ_R.**

## HARD STOP

c0′ and c2′ unresolved. Axis-2 C, unchanged. Noise fork untouched.
Gate-E untouched. Next: **owner decision** on whether to invoke fork (ii)
and price a new IR input, or to leave the H² local sector fork-gated.
