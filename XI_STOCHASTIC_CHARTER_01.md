# ξ_ij — THE DISSIPATION-SOURCED STOCHASTIC BACKGROUND: CHARTER + PRE-REGISTRATION (frozen before evaluation)

**Fork:** XI-1, the closure computation of the **second Part-7 front**
(v4 channel C5): the ξ_ij calc — "the dissipation-sourced stochastic GW
background — still unclaimed ground" (`STAGE_CLOSE_2026-08-09.md`).
**Authority:** the owner's ruling of 2026-09-27
(`A6_OWNER_RULING_01.md`): "Proceed to C5, the ξ_ij/Γ_T calculation,
without letting C3's unresolved status contaminate its charter."
**Standing state of the channel's other half:** the Γ_T rider is
already a **computed closure** (2026-09-06, owner-authorized:
`calc/gw_tensor_friction.py`, `calc/RESULTS_gw_tensor_friction.md` —
SPEC §5 REFUSE registered with the obstruction named; the
parameter-free Γ_T(ω) pinned 62.7 orders below the shared-slot bound;
adversarially verified). This fork computes the **remaining unclaimed
half**: the stochastic background that the KMS lock *mandates* as that
friction's companion.
**Sources:** `GRUT_PREDICTION_GATE_GAMMA_T.md` (the wave equation with
the mandatory companion ⟨ξξ⟩(ω) = coth(ω/2T_dS)·|Im K_R(ω)|,
T_dS = H/2π per rung2's KMS/FDT lock), `calc/SPEC_gw_tensor_friction.md`
(traps and must-not-touch list, inherited), `PHYSICS_LEDGER/`
ROOT-1 §3 (the licensed domain ω ≫ 3.4H; ω ≲ 3.4H UNASKABLE, O1–O4).
**Register read-only; nothing banks; no register field moves here**
(v4 R2: consumption at the channel's node is the owner's adjudication —
the C3 precedent of this date governs the distinction between finishing
a computation and satisfying a channel).

## 0. The question (frozen)

> **Does the dissipation-sourced stochastic tensor background — the
> FDT-mandated companion of any friction in the TT slot, at the locked
> temperature T_dS = H/2π — reach any observable level at any licensed
> frequency?**

This is a **closure, not a prediction hunt** (the Γ_T gate's pricing
carries over): the object is parameter-free on horn (a), and the
central suppression is horn-independent (§1), so a computation can only
pin the number, never move the routing.

## 1. The frozen derivation route

Per TT polarization, licensed domain ω ≫ 3.4H (flat contract; the
ω ≲ 3.4H region including horn (b)'s τ₂ pole is UNASKABLE and out of
scope, stated not evaluated):

1. The KMS companion of any friction Γ in the slot carries the
   stationary occupation of the locked bath:
   n̄(ω) = 1/(e^{2πω/H₀} − 1) (T_dS = H₀/2π; coth(ω/2T) = 1 + 2n̄, the
   +1 being vacuum, never counted as background — frozen).
2. **The upper member (pure-FDT stationary limit):** the mode
   thermalizes fully to the bath —
   Ω^upper(ω) = ω⁴ n̄(ω) / (3π² H₀² M̄_P²)
   (2 polarizations; dρ/dlnω = ω⁴n̄/π²; ρ_c = 3H₀²M̄_P²).
3. **The expansion-damped member (the physical one):** the noiseless
   Hubble friction 3H₀ competes with the noisy Γ_T for the stationary
   balance — Ω^damped = Ω^upper · Γ_T(ω)/(Γ_T(ω) + 3H₀), with Γ_T the
   pinned parameter-free horn-(a) kernel
   Γ_T(ω) = (3/1280π)(ω³/M̄_P²)[1 + (104/9)(H₀/ω)²].
4. **Horn-independence (the structural statement, frozen):** n̄(ω) is a
   property of the KMS lock at T_dS, not of the kernel — *any* friction
   in the constitutive family carries the same Boltzmann factor
   e^{−2πω/H₀} at licensed frequencies. Only the damped member's ratio
   feels the kernel, and only downward.
5. All evaluation in **log space** (ln n̄ → −2πω/H₀ for
   2πω/H₀ > 50; switch error < e^{−50}, frozen) — no overflow, exact
   asymptotics.

**Constants (frozen; the Γ_T closure's own):** H₀ = 67.4 km/s/Mpc =
2.1841e-18 s⁻¹ (MPC = 3.0856775814913673e22 m); M̄_P = 2.435e18 GeV
expressed in s⁻¹ via ħ = 1.054571817e-34, e = 1.602176634e-19.

**Frozen frequency set:** ω/H₀ ∈ {10, 100} (the licensed-floor region)
and f ∈ {1e-8 Hz (PTA band), 1e-3 Hz (LISA band), 100 Hz (ground
band)}.

**Frozen comparison levels (design-level, memory-grade, declared as
insertions):** Ω_BBN = 1e-6; Ω_PTA = 1e-9; Ω_LISA = 1e-12;
Ω_ground = 1e-9. The expected margins are so large (> 100 orders,
exponential in frequency) that any literature-accurate replacement
within ±6 orders leaves every verdict unchanged — which is why
memory-grade levels are chartered here and would never be acceptable
for a close call.

## 2. The gates (frozen, mechanical)

**Controls (halt-grade):**
- RC-1 the Γ_T closure replicates: Γ_T(ω) at f ∈ {10, 100, 1024} Hz
  reproduces the recorded (1.352e-83, 1.352e-80, 1.452e-77) s⁻¹ within
  0.5% each, and the recorded 62.7-order margin at 100 Hz within ±0.1
  (recomputed from the frozen constants — the two records must agree or
  this instrument's constants are wrong).
- RC-2 identities: coth(ω/2T_dS) − 1 = 2n̄(ω) to 1e-12 relative on the
  evaluable part of the scan; the log-space asymptotic switch matches
  the exact expression to 1e-10 relative at the switch point.

**The closure table:**
- M-1 log₁₀ Ω^upper and log₁₀ Ω^damped at every frozen frequency, with
  the margin (in orders of magnitude) against every frozen comparison
  level; the Γ_T/(Γ_T+3H₀) damping ratio reported per frequency.
- M-2 (gate) **no-effect at every member and every frequency:** both
  members sit **more than 30 orders below every comparison level** at
  every frozen frequency. (Design foresight: the binding case is
  ω = 10H₀ against BBN, expected ≈ 139 orders; the gate at 30 is
  deliberately far inside certainty — magnitudes are otherwise
  reported, never gated, per the Γ_T closure's own discipline.)
- M-3 (frozen note, horn-independence): the e^{−2πω/H₀} factor is
  kernel-free — the verdict covers the whole constitutive family in the
  licensed domain, horn (b) included wherever it is askable.

**Inherited obligations honored (SPEC §6–§7):** no functional form is
transplanted across backgrounds (the kernel enters only through the
already-pinned flat-contract Γ_T); no staked amplitude enters any
number (B appears nowhere); no headline carries an unpinned constant
(ω_c appears nowhere); the register, the TT quarantine, and the
dephasing statements are untouched.

## 3. Outcome rule (frozen, mechanical)

- **XI-CLOSED-NO-EFFECT** iff every gate holds: the dissipation-sourced
  stochastic background is exponentially dead (Boltzmann e^{−2πω/H₀})
  at every licensed frequency, parameter-free, member- and
  horn-independent. The unclaimed ground is claimed as a **computed
  closure**. Consequence for the program's standing statement: the
  last dissipation-channel observable candidate named by the stage
  close is closed by computation; "no discriminator identified on the
  current record" (the Γ_T closure's statement) extends to the
  stochastic channel.
- **XI-PARTIAL** for any other gate failure; **HALT** (instrument bug,
  never physics; no verdict) on any RC breach.

Under every outcome: nothing banks; no register field moves; no red
gate is touched; the public paper is untouched. The verdict carries a
**proposed C5 channel line** for the owner's adjudication under v4 R2 —
presented as candidate readings, neither forced (R1), exactly as the
C3 precedent of this date requires. **HARD STOP** after the verdict.

## 4. Instrument contract

`calc/xi_stochastic_closure.py`: pure Python 3 standard library;
deterministic; no RNG; single run; no post-hoc tuning; log-space
arithmetic throughout the exponentially suppressed regime; writes
`XI_STOCHASTIC_RESULT.json` (sha-hashed) at the repository root with a
`defect_history` field; runtime seconds. Scope: the licensed domain
ω ≫ 3.4H only; the UNASKABLE region is named, never evaluated;
cosmological production mechanisms other than the FDT-stationary
companion (e.g. inflationary-era amplification) are **out of scope** —
this closure adjudicates exactly the object the stage close named: the
dissipation-sourced background of the present-epoch response kernel.
