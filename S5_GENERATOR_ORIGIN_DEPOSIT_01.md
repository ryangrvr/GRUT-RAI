# S-5 GENERATOR ORIGIN — DEPOSIT 01 (current-parent scope; no new analysis)

- **Authority:** `S5_OWNER_RULING_03.md` §§9–11 (Issue #2 comment `5904495463`).
- **What this file is:** a record of accepted terminals only. **It contains no new analysis.**
- **Date:** 2026-09-30 · **Branch:** `master-w25bu9`.

## 1. S5-0: generator-kind selection

| | |
|---|---|
| **Terminal** | **GENERATOR-IRREDUCIBLE/SUPPLIED**, at the audited/current GRUT scope (`S5_OWNER_RULING_01.md`) |
| **Record** | `S5_GENERATOR_ORIGIN_01.md` (pre-registered at `afab923`; audit at `334662a`) |
| **Correction** | `S5_CORRECTIONS_01.md` (SC5-1: clock-rescaling quotient) |
| **Binding** | Nothing GRUT has already earned selects the kind of temporal generator. The first-order dissipative generator is a declared substrate premise. **Earned static structure ⇏ unique temporal generator.** |
| **Architecture** | Two primitive-looking layers: the static substrate (K, net) and the temporal generator class. Neither is derived from the other. |
| **Flags** | F-1: UNFORMULABLE does not fire. F-2: P-2 is earned within a supplied quantum-class premise, and CONDITIONAL as a generator-origin selector. F-3: clock quotient. F-4: NG-1 is ring-scoped. F-5: the comparison set is {G-D, G-OU, G-W, G-S}. |

## 2. S5-1: conservative origin / Markovian limit

| | |
|---|---|
| **Terminal** | **MARKOV-LIMIT-OTHER-CLASS**, conditional on the admitted L-vH weak-coupling deformation (`S5_OWNER_RULING_03.md`) |
| **Records** | charter `S5_CONSERVATIVE_ORIGIN_01.md` (frozen `d603db5`); derivation `S5_CONSERVATIVE_ORIGIN_DERIVATION_01.md` (`6170129`); script `calc/s5_conservative_origin.py` (`ed2bbe3`); result and verdict (`6a17b57`); correction `S5_CONSERVATIVE_ORIGIN_CORRECTIONS_01.md` |
| **Binding** | The declared local conservative parent does not derive the Level-0 first-order G-D generator. In the admitted weak-coupling limit it derives a controlled Markov effective law of a different class: an underdamped oscillator on the retained phase-space variables. |

## 3. Native parent (L-N, g = 1)

> **NON-MARKOVIAN DISSIPATION ONLY.**

- The retained spectral measure is purely a.c. on [0.3, 4.3], with no bound state and √ branch
  points.
- There is retained decay with t^{−3/2} oscillatory tails, consistent with the O-6 t^{−3} bilinear
  tail.
- At every fixed g > 0 the branch cut persists.

## 4. Weak-coupling limit (L-vH)

> **The weak-coupling kinetic limit derives a controlled underdamped Markov effective dynamics, with
> a parent-derived damping rate of order g².**

- **Convergence:** sup_{t≥0}‖Φ_g(t) − e^{(A₀ − κg²I)t}‖ → 0, with κ = 1/(2√2.3). This is via the
  Scheffé L¹ convergence of the exact density to Cauchy.
- **Effective law:** A_eff = A₀ − κg²I, i.e. q̈ + 2κg²q̇ + (ω_s² + κ²g⁴)q = 0.
- **Grades:** **M-1 YES; M-2 NO.**
  - Inertia survives and the spectrum is complex.
  - The response is not CM.
  - q₁ is not autonomous, and there is no slaving.
- **Wording fence:** in physical time the rate κg² → 0. The finite decay is on the kinetic scale
  τ = g²t.

## 5. K-L0

> **K-L0 FAILS** for every finite N, for N = ∞, and for every fixed g > 0.

- **Local:** φ″(0) = −K₁₁ < 0.
- **At N = ∞:** also the branch cut.
- **Memory diagnostic:** Γ_fric″(0) = −g², and the friction is never white at fixed g. It is kept
  separate from the K-L0 object φ.

## 6. Level-0 G-D generator: status

> **The Level-0 first-order G-D generator remains IRREDUCIBLE/SUPPLIED relative to the current GRUT
> parent and admitted reductions.**

**S-5 current-scope synthesis:**

> **Static GRUT structure does not select the temporal generator. The existing conservative parent
> can derive an underdamped Markov effective law in a controlled weak-coupling limit, but neither the
> native parent nor that admitted limit derives the Level-0 first-order completely-monotone
> generator.**

> *GRUT's conservative parent can generate Markovianity, but not the Markovianity GRUT originally
> assumed.*

**Not claimed:**
- that conservative dynamics cannot yield Markovianity;
- that all dissipation is non-Markovian;
- that an overdamped limit is impossible;
- that a wide-band limit is necessary;
- that G-D can never be derived.

## 7. Preserved future options (NOT selected)

- **S5-WB:** can a principled wide-band parent limit derive local friction?
- **S5-OD:** can an independently earned overdamped/slaving hierarchy derive the inertia-free G-D
  law?

**Opening either automatically would violate the no-rescue discipline.**

## 8. Status

- **S-5 is CLOSED at current-parent scope.**
- **HARD STOP**, for the owner's selection of a genuinely new campaign.
- No S5-2, no re-run, no new parent, no SF-2, no gravity, Π₀ or cosmology.
