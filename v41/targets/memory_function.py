"""GRUT-RAI v4.1 — STEP 4, TARGET 1: K̃(ω), the Mori–Zwanzig memory function.

This is the load-bearing OPEN calculation that single-pole-ness (and therefore the
relic / dark-matter no-go) rests on. The decision procedure is binary and decisive:

    fast tail  (τ_K < τ₀/4)  →  single-pole becomes a THEOREM of {Q + bath spectrum}
    slow tail  (τ_K > τ₀/4)  →  a dark-capable (off-axis) pole reappears inside F(t)

What is computable now (and is): given the memory correlation time τ_K, the pole
structure and the off-axis threshold τ₀/4. What is NOT yet computed (the decisive
piece): τ_K itself, from the TT-shear orthogonal-force autocorrelation against the
KMS bath, K(t) = ⟨F(0)F(t)⟩/⟨|z|²⟩. v4 ASSERTED τ_K = τ_micro "by construction" of
the slow/fast projection; this module refuses to assert it — it is the open target.
"""
from __future__ import annotations

import numpy as np

OFF_AXIS_THRESHOLD_FACTOR = 0.25   # poles go off-axis iff τ_K > τ₀/4


def poles_second_level(tau0: float, tauK: float):
    """First non-Markovian rung: χ ∝ (1−iωτ_K)/(1 − iωτ₀ − ω²·τ₀τ_K). Returns the
    denominator roots (poles). On-axis (relaxational) iff overdamped (τ_K ≤ τ₀/4)."""
    # denominator −(τ₀τ_K) ω² − i τ₀ ω + 1, in descending powers of ω
    return np.roots([-(tau0 * tauK), -1j * tau0, 1.0])


def is_single_pole(tau0: float, tauK: float) -> bool:
    """True iff the memory time is fast enough that no off-axis (dark-capable) pole
    appears: τ_K < τ₀/4. This is COMPUTABLE — given τ_K."""
    return tauK < OFF_AXIS_THRESHOLD_FACTOR * tau0


def compute_tauK_from_bath(*_args, **_kwargs) -> float:
    """THE DECISIVE OPEN CALCULATION. Compute τ_K = the correlation time of the
    TT-shear orthogonal force F against the KMS bath, from
        K(t) = ⟨F(0) F(t)⟩ / ⟨|z|²⟩,
    with the Zwanzig projector onto the slow TT variable and the FDT bath spectrum
    N(ω) = (2/τ) ħω coth(ħω/2k_BT). Until this is done, single-pole-ness is a
    theorem MODULO this integral. Refusing to assert τ_K = τ_micro is the point."""
    raise NotImplementedError(
        "OPEN target: compute τ_K from the TT-shear/KMS bath autocorrelation. "
        "fast tail (τ_K<τ₀/4) ⇒ single-pole is a theorem of {Q+bath}; "
        "slow tail (τ_K>τ₀/4) ⇒ a dark-capable pole lives in F(t)."
    )


def status() -> dict:
    return {
        "target": "K̃(ω) memory function from the bath",
        "state": "OPEN",
        "computable_now": "pole structure + off-axis threshold τ₀/4 (given τ_K)",
        "decisive_unknown": "τ_K from ⟨F(0)F(t)⟩/⟨|z|²⟩ (TT-shear vs KMS bath)",
        "criterion": "τ_K<τ₀/4 → single-pole theorem; τ_K>τ₀/4 → dark pole in F(t)",
        "blocks": ["constitutive_law_single_pole", "propagating_relic_no_go (provisionally)"],
    }


if __name__ == "__main__":
    print("TARGET 1 — K̃(ω):", status()["criterion"])
    print("  sanity (given τ_K): single-pole at τ_K=τ₀/100?", is_single_pole(1.0, 0.01),
          "| dark pole at τ_K=τ₀?", not is_single_pole(1.0, 1.0))
    try:
        compute_tauK_from_bath()
    except NotImplementedError as e:
        print("  decisive calc:", e)
