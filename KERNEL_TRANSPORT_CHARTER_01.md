# KERNEL-TRANSPORT INSTRUMENT — CHARTER + PRE-REGISTRATION (frozen before evaluation)

**Date:** 2026-09-25 · **Chartered by:** owner
(`CLOCK_MISMATCH_OWNER_RULING_01.md` §4), question verbatim:

> **Can GRUT derive a dS→FRW kernel transport rule from already admitted
> principles and inputs? If yes, derive it. If no, establish precisely what
> additional structure is required. If multiple inequivalent transport rules
> survive, that nonuniqueness itself becomes a structural result.**

**Binding discipline clause (owner):** *"don't let 'this would be useful'
become a reason to assume the transport law exists."* The instrument's three
outcome classes have equal standing; the directional-optimism rule applies
hardest to O-DERIVED (the outcome the program would like).

This file is committed and pushed **before** the instrument runs. Register
untouched; ledger 0; banks nothing. Λ_R, Matsubara, Π₀, U5 remain fenced.

---

## 1. THE OBJECT, NAMED PRECISELY (the E7 rider discharged for this instrument)

The record's own defect note (keystone E7) says "the kernel" denotes no unique
object. This instrument therefore fixes its object **before** running:

**Primary object: the free TT graviton retarded/commutator kernel per comoving
mode k**, G_R(t, t′; k) ∝ θ(t−t′)·[v₁(η)v₂(η′) − v₂(η)v₁(η′)] / (a(η)a(η′)),
built from any two independent solutions of the C1-validated tensor mode
equation v″ + (k² − a″/a)v = 0, h = v/a (unit Wronskian). This object is
**state-independent** (any solution basis gives the same commutator — verified
in-run), so the transport question can be posed for it without a state choice.

**Secondary object (derivational leg only, no computation): the noise/KMS
structure** (the Matsubara ladder). Its transport requires a state and a
temperature structure and is treated in §5 (T-III).

Out of scope, walled: the interacting/assembled Σ (wall A), anything ω ≲ H at
contract scope (Decision C), and every fenced route.

## 2. ADMITTED-INPUTS INVENTORY (declared before the attempt)

- **A1** — the SK/in-in formalism (rung1_inin_formalism; borrowed-standard).
- **A2** — T_dS = H/2π on the declared flows (rung2) — **dS-specific; no FRW
  analog is banked** (recorded fact, feeds T-III).
- **A3** — the frozen Tier-2 dS bath machinery: TT modes on flat-slicing dS,
  state-independent G_R (T2-verified), flat anchor G_R(H=0) ∝ sin(kΔ)/k.
- **A4** — the C1-validated FRW tensor primitive: v EOM, h = v/a, Wronskian
  constancy (`C1_GROUND_TRUTH_STATUS.json` 5/5, `C1_PRIMITIVE_VALIDATION` 6/6)
  — **the free FRW kernel is computable from admitted inputs.**
- **A5** — the D1–D6 clock maps (screened 2026-08-21; re-verified 2026-09-25).
- **A6** — the X2 refusal: constant-H dS and Ω_m ≠ 0 FRW are different
  solutions; no diffeomorphism relates them.
- **A7** — the declared central background: flat ΛCDM, Ω_m = 0.315.
- **A8** — `background_time_translation_flow` booked as a +1 omission — the
  acknowledgment that the background flow question is unpaid.

## 3. THE CANDIDATE ROUTES (declared; all computed or derived, none favored)

- **T-I — the local substitution family** (the naive transports): K_dS applied
  over the lag with a locally chosen rate,
  H_\* ∈ {H(t) observation-time, H(t′) emission-time, H(t̄) midpoint-time,
  H₀ frozen}, comoving-k identification, scale factor matched at the emission
  point (a_dS(t) = a(t′)e^{H_\*(t−t′)}). Each member is an explicit,
  well-defined rule; the family's **internal spread** measures the
  nonuniqueness of "apply the dS kernel with the local rate."
- **T-II — the exact in-admitted-inputs kernel** (ground truth at free level):
  G_R(t, t′; k) computed from A4/A7 directly on the ΛCDM background. If it
  exists (it should — that is what A4 validates), then a transport rule
  **exists as recomputation**; the question becomes whether it **reduces to
  any T-I local rule**, i.e. whether the kernel is a function of a local rate
  or a functional of the whole a(η) history.
- **T-III — the state/temperature leg (derivational, recorded not computed):**
  what the Matsubara/KMS side of the transport would require beyond A1–A8.
  Known recorded facts feeding it: no timelike Killing field on matter+Λ FRW;
  A2 is flow-specific; D6 ("the transport itself is the assumption"); the
  ~367× variation already computed. The deliverable is the **named list of
  additional structure** (each item with its register price class), not a rule.
- **Adiabaticity control (computed):** ε(z) = −Ḣ/H² = (3/2)·Ω_m(z) on A7 —
  the small parameter every local substitution rule implicitly assumes. Its
  minimum over the real history is part of the record this instrument files.

## 4. THE COMPARISON GRID AND CLASSIFICATION RULE (pre-registered, mechanical)

**Grid (declared):** comoving k/(a₀H₀) ∈ {0.5, 1, 2}; emission times
z′ ∈ {0.296 (z_Λ), 1, 3}; observation t = t₀. These bracket the
horizon-scale, late-time regime the rung7 comparison lives in.

**Metric:** for each grid point and each T-I member r,
Δ(r) = |K_r − K_exact| / max_grid|K_exact| (normalized to the exact kernel's
grid maximum, so near-zeros do not manufacture fake divergence). All numbers
reported in full; the thresholds below feed only the classification.

**Classification (exhaustive, one primary outcome):**

- **O-DERIVED (local rule):** some single T-I member has Δ ≤ 0.10 over the
  ENTIRE grid. Then that rule is derived-with-domain and the instrument
  reports its validity boundary.
- **O-NONUNIQUE:** no member passes O-DERIVED, AND at least two T-I members
  differ from each other by > 0.25 at some grid point. The structural result:
  the "apply dS locally" prescription is not a rule but a family, with the
  computed spread as its size.
- **O-MISSING (functional):** no member passes O-DERIVED and the family is
  internally tight (< 0.25 everywhere) yet wrong against T-II — the kernel
  depends on the history through more than any local rate.
- O-NONUNIQUE and O-MISSING may co-occur; both are then reported with
  O-NONUNIQUE primary (the owner's framing names it a structural result).
- **In every outcome**, T-II's own status is reported: if the exact FRW kernel
  is computable from A4/A7 (expected), the sentence "a transport rule exists
  as recomputation at free level; what does NOT exist is <outcome>" is the
  headline, and T-III's named-structure list covers the ladder/KMS side.

**Verdict sentence for the ruling's §2.4 slot:** whichever outcome lands, the
instrument states what it does to the conditional calculation of
`CLOCK_MISMATCH_OWNER_RULING_01.md` §3 (which T-I member, if any, the naive
application corresponds to, and what its computed error against T-II is).

## 5. CONTROLS AND FENCES

- **Integrator controls (halt on miss):** (i) flat limit H → 0 reproduces
  sin(kΔη)/k (the T2 flat anchor's form); (ii) the dS run reproduces the
  closed-form dS commutator [(1 + 1/(k²ηη′))sin kΔη − (Δη/(kηη′))cos kΔη]/k;
  (iii) Wronskian constancy along every integration; (iv) state-independence:
  two different solution bases give the same commutator to tolerance;
  (v) superhorizon freezing: h → const for k ≪ aH.
- **EXISTENCE-ASSUMPTION fence (owner):** no step may presume a transport law
  exists; T-I members are hypotheses under test, T-II is a computation, and a
  null (nothing derivable beyond recomputation) is a first-class result.
- **DERIVE-OR-PRICE (keystone §7):** every T-III item is stated with whether
  it derives or relocates, and its price class.
- **NO-DOWNSTREAM-SELECTION:** the fate of the demoted conditional
  calculation (rung3/rung7) must not influence route evaluation; the grid,
  metric and thresholds above are frozen here, before any number exists.
- **NO-BANKING:** result JSON + verdict document only; `claims.json`
  untouched; proposed annotations go to the handover draft.

## 6. DELIVERABLES AND STOP

1. `calc/kernel_transport_rule.py` — pure stdlib, self-checking, emits
   `KERNEL_TRANSPORT_RESULT.json` (sha-hashed), verdict computed mechanically
   by §4.
2. `KERNEL_TRANSPORT_VERDICT_01.md` — outcome, the T-III named-structure
   list, and the effect on the demoted conditional calculation.
3. **HARD STOP at the verdict** (bounded instrument; the waiting decision:
   the owner reads it and either selects the next instrument or reopens the
   prediction/uniqueness tree). Λ_R, Matsubara, Π₀, U5 stay fenced throughout.
