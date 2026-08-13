# RESULTS — x_no_pin: the channel-diagonal passivity lemma

*Calc: `calc/x_no_pin.py` (pure stdlib, selftest green, four-mutant battery in
`provenance/mutation_registry.py`). Pre-registered: `provenance/prereg/PREREG_X_NO_PIN_2026-08-09.txt`
(sha256 `47e3a29e7c162739ee56699d7d6403af9459225e9b63d86963334e7b3ec4ee2b`, sealed before the calc
existed); scored in `provenance/prereg/RESULT_X_NO_PIN_2026-08-09.txt`. This is X_FLOOR_MAP attack
item 2 — the register's own named next step, built under the 2026-08-09 overseer brief. Scoped up
front: nothing here is a first-of-its-kind application; the ζ≥0 pattern is precedented in-house on
rung7 (`RESULTS_wz_sign.md`), and the candidate re-homing of the retracted orientation lemma to the
passivity argument is X_FLOOR_MAP's own written invitation.*

> **REGISTER HOMES, POST-RULING 2026-08-09 (read this before the sections below):** the overseer
> SPLIT the single staged node. The **general lemma** (PSD factorizes over orthogonal idempotents —
> frame-free mathematics) banks at `passivity_channel_diagonal` (shown, Δ0). Everything in this
> document that is GRUT-family-specific — the two-channel floor, the no-ceiling/no-pin cone, route
> R3's closure as classifier, the x_diss(ω) ≥ 0 restatement — banks at **`x_no_pin_theorem`**
> (derived-pending on the enumeration's 4d-covariant frontier, Δ0), which carries the enumeration
> edge and the KC5 fence. The dissipative-to-static transfer gap (fence 1 and the "what it does not
> give" items below) is its own owed register node, **`kk_static_transfer`**. Where the prose below
> says "the lemma" of a family-specific result, read it against `x_no_pin_theorem`.*

## The lemma (pre-registered outcome (a): FLOOR ONLY — the non-flattering branch)

For the Ward-surviving two-channel family `K_R = c₂(ω,k²)·P⁽²⁾ + c₀(ω,k²)·P⁽⁰ˢ⁾`
(`eft_operator_basis`), the banked matrix-sense passivity condition (rung2's S4) is **exactly
equivalent to the two independent scalar conditions**

> ω·Im c₂(ω) ≥ 0  AND  ω·Im c₀(ω) ≥ 0, channel by channel, pointwise in ω.

**No cross-channel rescue exists**: with the bulk channel violating at −10⁻³, the minimum
eigenvalue of the assembled kernel stays pinned at −10⁻³ while the compliant shear channel is
amplified through 10⁶. The spin sectors are orthogonal; the matrix condition cannot trade between
them. (An aggregate reading — trace positivity — *would* allow the trade; that is mutant M1, and
the battery kills it.)

Method note (why this is not tautological): the PSD test is a generic cyclic-Jacobi eigenvalue
computation on the explicitly assembled 6×6 matrix, never using the theorem's own structure; the
Jacobi engine is itself selftested against a hidden known spectrum; the projector algebra is
re-verified per k-hat at four k-hats.

## Classifier, not pinner — the no-pin fragment EARNED

The admissible set is a **convex cone**, closed under independent nonnegative rescaling of each
channel (verified through amplitude 10⁶) and realizing **every** nonnegative ratio c₀/c₂ tested
(0 through 10⁶). So passivity:

- **orients** each channel (the sign floor — the only thing it gives),
- **never bounds** an amplitude (no ceiling — the pre-registered flattering direction, and it did
  not bank),
- **never selects** a ratio (no pin — u5 route R3 closes as X_FLOOR_MAP priced it: a classifier).

The KMS lock adds nothing cross-channel at this level: `N(ω) = coth(βω/2)·Im K_R(ω)` has a common
scalar thermal factor, so the noise decomposes on the same projectors and its positivity is the
same two per-channel conditions — verified both ways (the passive pair's noise is PSD; a
dissipation-sign violation survives the lock rather than being masked).

## The firewall event of this wave, recorded

The first run's selftest FAILED — correctly. An absolute eigenvalue tolerance let the Jacobi
engine's 10⁻¹⁴-relative float error read as a violation at amplitude 10⁶, which *computed a fake
ceiling* — the exact outcome the pre-registration names as the seductive one. The frozen-verdict
comparison caught it before any prose was written. Fix: scale-relative tolerance (the standard
reading of PSD at machine precision), documented in `psd()`'s docstring.

## Fences (each pre-committed in the sealed prereg)

1. **Variable caution — this is about c₀, not x.** The x↔c₀ action-level map was
   `mu_slip_interior.py`'s named open item R1 at build time; the same 2026-08-09 ruling marked it
   **DISCHARGED-BY-CONSTRUCTION** via `S_IF.md`'s declared construction x ≡ normalized c₀ modulus —
   a declaration, not an output of this calc. The residual transfer question (dissipative → static)
   is registered at `kk_static_transfer`.
2. **The KC4 guard, verbatim in the node** (`BRIEF_p_tt_interrogation.md` kill-condition 4):
   passivity "constrains signs and cross-channel magnitudes; it can *propagate* a channel's
   vanishing (a zero diagonal kills its cross-couplings) but can never *source* one. Any argument
   deriving channel annihilation from passivity *alone* is a category error and dies." This lemma
   is a sign condition on c₀ — **not a licence for the pure-TT ansatz, and not evidence against
   it.**
3. **No Israel–Stewart ceiling.** An honest causality ceiling needs named background inputs
   (relaxation time, sound speed, entropy density) that exist nowhere in this corpus, and the
   register's Israel–Stewart node is a borrowed-scaffold pointer (`attaches_to`, deliberately not
   `depends_on`) that cannot carry structure into GRUT's ledger. Reclassified as a rung3-dispatch
   sub-question (see `SPECIALIST_BRIEF_rung3_spine.md`, Rider C). No number was computed.
4. **The orientation lemma's re-homing is exactly this and no more**: the x ≥ 0 statement now has
   a correct fence (passivity standing alone, screened on its own merits, never inherited from
   R1's scheme-degenerate sign) — but it remains a statement about the *dissipative modulus's
   orientation*, pointwise in ω, and becomes "x(ω) ≥ 0" only under S_IF's definition of x.

## Ledger

Zero, as pre-registered. A structural lemma about the already-admissible family adds no underived
input; GRUT stays at net +13. Register disposition, post-ruling: the general lemma at
`passivity_channel_diagonal` (shown, Δ0), the family application at `x_no_pin_theorem`
(derived-pending, Δ0), the transfer gap at `kk_static_transfer` (to-derive, Δ0) — all three staged
through the bank gate's firewall flags and accepted on the overseer's 2026-08-09 ruling.
