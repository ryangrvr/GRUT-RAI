# Q1 — energy-basis falsifier, magnitude/ratio: result

**Date:** 2026-06-25 · **Code:** `calc/q1_energy_basis_magnitude.py` (stdlib, <1 s)
**The decisive calc.** Framed around the **ratio** (predicted decoherence rate / detectable
rate), not the commutator — because "lives" and "observable" are different questions.

## The operator structure (the part previously glossed)
Gravity couples to T^{μν}, which splits in the system's energy basis:
- **T^00 = energy density.** For a system at rest this *is* ∼ H_S → **diagonal** → [A,H_S]=0 →
  energy-basis dephasing samples **S(0)**. Super-Ohmic ⇒ S(0)=0 ⇒ **Γ=0, quiet, dies.** This is
  the *dominant* (Newtonian) coupling.
- **T^0i, T^ij = momentum flux / stress.** Off-diagonal in the energy basis, suppressed by (v/c).
  [A,H_S]≠0 → samples S(ΔE), but the rate carries (v/c)² *on top of* the Planck suppression of S.

So the energy-basis **wedge** (the ΔE-scaling that distinguished GRUT from position-basis DP/CSL)
requires the **off-diagonal** piece — and the part gravity couples to most strongly (energy
density) is exactly the one that samples S(0)=0 and is quiet.

## The ratio (the answer)
| branch | Γ/Γ_detect | outcome |
|---|---|---|
| diagonal T^00 (dominant) | **0** (S(0)=0) | **quiet → dies** |
| off-diagonal T^0i,T^ij, ΔE=1 MeV, q=1 (generous) | ~10⁻⁷ | faint |
| off-diagonal, ΔE=1 eV…MeV, q=1…2 | 10⁻¹³ … 10⁻⁴⁷ | faint (B) |

**Most-generous (flat S_φ∼t_P, v/c=1):** would over-decohere heavy energy superpositions
(τ ∼ µs for GeV), which is *not observed* → the natural amplitude is **excluded**; the true
vacuum noise must be suppressed far below it. **Observed matter-wave coherence is the binding
bound** on GRUT's staked noise amplitude (the analogue of GW170817 bounding GW dissipation).

**Inversion:** to reach Γ ∼ 1/s, the noise amplitude must be staked ~10⁷+ above its natural
value — a **tuned number at the current matter-wave edge, not a parameter-free prediction.**

## Two deeper points
1. The Pikovski time-dilation mechanism that *does* give a robust effect decoheres **position**
   (Δx) — the *same axis as DP/CSL*. It is **not** the energy-basis wedge. So even the mechanism
   that works doesn't supply the distinguishing observable.
2. The diagonal/off-diagonal split means the wedge is quiet under the strong coupling and faint
   under the weak one — it is structurally hard to make it both distinct *and* visible.

## Verdict
"Lives" does **not** stand as the headline. The energy-basis falsifier is **quiet (diagonal) or
faint (off-diagonal, 7–47 orders below)** and does **not carry the program** as a parameter-free,
distinct, observable wedge. Rung 8 differentiator → **FAILS-DIFFERENTIATION (quiet-or-faint).**

**This confirms the reframe.** GRUT's genuine contribution is the **structural in-in arrow of
time**, not a tabletop decoherence wedge. The falsifier was the thing we hoped carried it; the
ratio says it doesn't.

## One-line question for the specialist (gray-zone)
> For a system in a pure internal-**energy** superposition (fixed position), is the dominant
> gravitational coupling the diagonal T^00 (∼H_S, sampling S(0)=0, quiet), so the only
> energy-basis decoherence comes from (v/c)-suppressed off-diagonal T^0i/T^ij — or is there a
> leading-order off-diagonal energy coupling that would sample S(ΔE) at O(1)?
