# RESULTS — noise-kernel transversality: booked-and-derived (2026-08-17)

**Question** (ruled 2026-08-16): after the Ward-scope correction withdrew the both-branches
license, noise-kernel transversality survived as an assumption the ledger was not pricing.
The ruling: book it (+1) or derive it from what is already booked — exhibited, not asserted.

**Answer: both horns, composed.** The derivation exists and is exhibited
(`noise_transversality_check.py`, exact rationals, both signatures), but the adversarial
screen found it consumes ONE premise the register had never priced — so that premise is
booked, and transversality is a theorem conditional on it.

## The theorem

On the register's booked family (FDT-locked kernels, scalar occupation dials):

1. **Ward sources a zero.** K_R annihilates the gauge orbit on its retarded slot (the
   accepted 2026-08-14 content) ⇒ g′ρg = 0 identically, ρ = (K_R − K_R†)/2i. Bilinear
   algebra; no positivity. (D_A = K_R† is forced by real fields + stationarity —
   screen-verified, not an extra assumption.)
2. **Positivity propagates it.** N is a PSD covariance on the full index space, plain
   pairing (Wightman/Bochner; bath-side unitarity — the system-side wrong-sign sector
   lives in Re K_R). PSD + zero diagonal ⇒ zero row (Cauchy–Schwarz applied directly
   to N). **The priced input** (renamed at owner verification 2026-08-17): rung1's fourth declared
   input (+1, net +14) is the **4d-covariant availability of the Ward-sourced gauge-orbit
   zero** — the KC5-reserved covariantization ("P2 full-4d-invariant; P0s
   spatial-subgroup-only, Bardeen completion frontier-reserved"), with an explicit
   discharge condition: the +1 retires when that frontier work lands.
   N-as-PSD-covariance was ruled CONSTITUTIVE of the banked Gaussian bath; the
   spatial-frame S4 stays frontier-reserved at the needed 4d strength (KC5 fence,
   x_no_pin precedent).
3. **The lock closes it.** N = coth·ρ in equilibrium; the booked departures are scalar
   occupations n(ω) (the (eps, τ₂) dials, already paid at rung7_wz). So N g = 0 —
   **the noise kernel is transverse** — and ρg = Ng/n(ω) ⇒ **K_R is transverse on both
   slots**: the admissible pair **closes on {P⁽²⁾, P⁽⁰ˢ⁾}** — a family-conditional
   closure theorem. The unconditional both-branch classification stays retired; outside
   the family (SCDP's Eq. 1.11 class) the larger space stands, priced by rung2's fence.

**Signature fact** (screen-found): plain-pairing positivity itself forces the tensor
channel closed at spacelike k² (P⁽²⁾ indefinite there; spacelike support needs a medium
frame u^μ, outside the η,k-only family). Transversality there rides on P⁽⁰ˢ⁾ alone.

**Why KMS alone was never enough**: K_cx = i(k⊗k)⊗Π passes retarded-slot Ward and the
matrix-adjoint lock form, has non-transverse noise, and is barred only by positivity
(exact indefiniteness witnesses in the calc's output).

## Demarcation (screen-mandated; lens-verified against fetched texts, not first-party-read)

- SCDP App. B.2 + `salcedo_colas_pajer2025`: Bianchi-route noise constraints; their
  no-dissipation corner reproduces this conclusion and deforms under dissipation — this
  theorem covers the with-dissipation FDT-locked case by a different mechanism.
- `abe_nishii2026` §4.3: same triad, projection **imposed** — the projection derived here.
- `landau_lifshitz_sp1`: the PSD/FDT matrix engine is textbook. New content is only the
  Ward-sourced zero on the gravitational gauge orbit, and the assembly.
- `hu_verdaguer_lrr`: corroboration by a different route (bath stress-tensor conservation),
  conserved-current subclass. Shipped unamended by the screen.

## The screen's own catches, recorded because this is the program's recurring shape

Three refuter lenses + adjudicator (2026-08-16/17), then a targeted re-screen: the first
draft's exhibit ran an **off-family spacelike instance its own theorem bars** (the missing
check was the composition assert, now PART 3; nine mutants had missed exactly it), and its
exact-PSD tool carried a **conj-slip wrong on complex-Hermitian input** (correct on every
shipped call site — real symmetric — so no verdict moved; fixed, selftested in PART 0, and
a registry mutant proves the selftest catches its re-installation). The first draft also
claimed a c-number-commutator route to ρ-positivity that is **wrong** for a tensor bath
operator (struck; the N-route replaces it) and claimed "either carrier suffices" for a
premise only one carrier delivers (struck). Adjudication: four AMENDs, one SHIP, booking
required — every amendment is applied in the calc's docstring and the register addenda.
Re-screen verdict: SHIP.

## Register footprint

- `rung1_inin_action`: ledger_delta 3 → 4 (fourth input, renamed at owner verification:
  the 4d-covariant gauge-orbit Ward zero, KC5-reserved, explicit discharge condition),
  stance updated; the 0-delta horn was DECLINED by the owner 2026-08-17, three grounds
  recorded in the note.
- `p_tt_ansatz`, `eft_operator_basis`: discharge addenda appended to the 2026-08-14 marks
  (appended, not superseding). p_tt_ansatz's +1 stays: transversality-derived does not
  force tracelessness; TT remains CHOSEN.
- `S_IF.md`: the declared-restriction mark now points at the theorem and its condition.
- Net: GRUT +13 → **+14**. Sync stamps updated across the eight standing docs.
- Battery: six in-process + six registry mutants, all verified killers; `slow: True`.
