"""GRUT-RAI v4.1 — TARGET 1D: the COLLISIONALITY FORK (filename kept; framing corrected).

This file is named for the wrong object. Across three rounds of external review it became clear
that single-pole-ness is NOT decided by a bath density-of-states / vacuum phase-space exponent —
that is the wrong quantity. The deciding object is the finite-temperature TRANSPORT memory of the
TT sector, and it forks on COLLISIONALITY. The honest record of how we got here:

  1C (original): "collisionality is the free datum; single-pole is an ANCHOR." — CORRECT.
  round 1 of review: "relativity fixes the DOS to ω² ⇒ s=2 ⇒ DERIVED." — wrong (DOS≠J).
  round 2 of review: "s=1 with the 1/ω_k factor; argued s≥1 across branches ⇒ PENDING_REVIEW." —
                     still wrong: leaned on the DOS/phase-space picture for the collisionless case.
  round 3 of review: the literature overturns that picture. → back to the 1C ANCHOR, sharpened.

THE FORK (the right object — transport memory, verified first-hand in __main__):
  • COLLISIONAL branch (viscous vacuum at T_c, hydrodynamic): the Kubo formula gives
    Im G_R^{TT}(ω) ~ ηω, i.e. an Ohmic / exponential-decay memory kernel ⇒ SINGLE-POLE HOLDS.
  • COLLISIONLESS branch (free-streaming massless bath): Weinberg (2004, PRD 69 023503) and
    Hawking (1966) give a NON-LOCAL, history-dependent memory kernel — the angular phase-mixing
    integral over streaming directions with the spin-2 weight (1−μ²)² produces a Bessel tail:
    K(s) = ∫_{-1}^{1}(1−μ²)² cos(μs) dμ, whose envelope falls as a POWER LAW (~s⁻³), oscillates,
    and leaves a long-ranged, non-decaying residual ⇒ SINGLE-POLE FAILS. This is the slow branch
    realized concretely (Weinberg's free-streaming reduces the GW amplitude by a finite residual).
  • The action does NOT fix which branch the vacuum is on. ⇒ single-pole-ness is an ANCHOR; the
    free datum is COLLISIONALITY (viscous vs free-streaming), exactly as 1C said.

So the cross-branch claim is NOT "every branch is s≥1, sub-Ohmic forbidden." It is: viscous ⇒
single-pole; free-streaming ⇒ single-pole fails (Weinberg); collisionality undetermined. The
"every branch fine" framing only survived in earlier drafts by leaning on the DOS picture the
free-streaming transport calculation overturns.

MISATTRIBUTION CORRECTED (round 3): earlier drafts wrote "collisionless vacuum s≈2 (the
reviewer's value)." That misattributes. The reviewer's actual position: s=2 is only the (∂φ)²
FLOOR; the gravitational/quadrupole vertex runs higher (Cho–Hu's published vacuum graviton kernel
is ω⁵), and — decisively — the vacuum T=0 exponent is the WRONG object for the single-pole
question, because at finite T the memory is set by transport, not vacuum phase space.

THE DE-ANCHOR CONDITION (settle target, now a clean bounded question): is GRUT's vacuum at T_c
collisional (viscous) or free-streaming? Weinberg 2004 + Hawking 1966 substantially answer what
EACH branch gives; the only genuinely open piece is confirming GRUT's exact z·T_TT vertex maps
onto the gravitational-wave-in-a-medium structure. If GRUT can show its vacuum is viscous,
single-pole graduates; if free-streaming, single-pole is refuted.
"""
from __future__ import annotations

import numpy as np
from numpy.polynomial.legendre import leggauss

_MU, _W = leggauss(400)


def free_streaming_kernel(s: float) -> float:
    """The collisionless (free-streaming) TT memory kernel: angular phase-mixing over streaming
    directions μ=n̂·k̂ with the spin-2 weight (1−μ²)² (Weinberg 2004 structure).
    K(s) = ∫_{-1}^{1} (1−μ²)² cos(μ s) dμ — a Bessel tail (power-law, oscillatory)."""
    return float(np.sum(_W * (1 - _MU ** 2) ** 2 * np.cos(_MU * s)))


def collisional_kernel(s: float, s_c: float = 1.0) -> float:
    """The collisional (viscous) memory kernel: exponential relaxation (Ohmic ⇒ single-pole)."""
    return float(np.exp(-s / s_c))


def kernel_is_single_pole(kernel, smax: float = 60.0, n: int = 4000) -> dict:
    """Classify a memory kernel: single-pole requires EXPONENTIAL (Markovian) decay. A power-law/
    oscillatory tail (free-streaming) is NON-single-pole. Returns the envelope log-log slope, the
    sign-change count, and the long-lag residual."""
    s = np.linspace(0.5, smax, n)
    K = np.array([kernel(x) for x in s])
    env = np.abs(K)
    m = s > smax / 7
    slope = float(np.polyfit(np.log(s[m]), np.log(np.maximum(env[m], 1e-12)), 1)[0])
    signs = int(np.sum(np.diff(np.sign(K)) != 0))
    resid = float(np.abs(np.cumsum(K[::-1])[::-1])[int(n / 6)] / np.abs(np.cumsum(K[::-1])[::-1])[0])
    return {"envelope_loglog_slope": slope, "sign_changes": signs, "long_lag_residual": resid,
            "single_pole": (signs <= 1 and resid < 1e-3)}


def the_fork() -> list:
    """The two branches and which one single-pole survives. Collisionality (which branch) is the
    free datum the action does not fix ⇒ ANCHOR."""
    col = kernel_is_single_pole(lambda s: collisional_kernel(s, 1.0))
    fs = kernel_is_single_pole(free_streaming_kernel)
    return [
        {"branch": "collisional (viscous, T_c)", "kernel": "exponential (Kubo Im G^TT~ηω)",
         "single_pole": col["single_pole"], "verdict": "HOLDS", "diag": col},
        {"branch": "collisionless (free-streaming)", "kernel": "Bessel tail (Weinberg 2004)",
         "single_pole": fs["single_pole"], "verdict": "FAILS", "diag": fs},
    ]


def settle_condition() -> str:
    return ("is GRUT's vacuum at T_c collisional (viscous ⇒ single-pole) or free-streaming "
            "(⇒ Weinberg non-local, single-pole fails)? Weinberg 2004 + Hawking 1966 answer each "
            "branch; the open piece is mapping GRUT's exact z·T_TT vertex onto the GW-in-medium "
            "structure. Collisionality is the free datum the action does not fix ⇒ ANCHOR.")


def status() -> dict:
    return {
        "target": "1D — the collisionality fork (post round-3 review; back to the 1C ANCHOR)",
        "outcome": "single-pole HOLDS on the viscous branch, FAILS on the free-streaming branch "
                   "(Weinberg); collisionality is the free datum ⇒ single_pole is an ANCHOR",
        "not": "NOT 'every branch s≥1, sub-Ohmic forbidden' — that leaned on the DOS picture the "
               "free-streaming transport calculation (Weinberg) overturns",
        "corrections_on_record": "DOS≠J (round 2); the vacuum T=0 exponent is the wrong object; "
                                 "the s≈2 misattribution removed (reviewer's floor was (∂φ)²; "
                                 "Cho–Hu vacuum graviton kernel is ω⁵)",
        "de_anchor": settle_condition(),
        "meta": "three rounds of AI-assisted 'sharpening' moved away from the correct original "
                "1C ANCHOR before the literature moved it back; the original anchor was correct.",
    }


if __name__ == "__main__":
    print("TARGET 1D — the collisionality fork (post round-3 review).\n")
    print("Is each branch's TT memory kernel single-pole (exponential) or not?")
    for b in the_fork():
        d = b["diag"]
        print(f"  {b['branch']:32s} {b['kernel']:32s}")
        print(f"      envelope ~ s^{d['envelope_loglog_slope']:+.2f}, sign-changes={d['sign_changes']:>2d}, "
              f"residual={d['long_lag_residual']:.3e}  → single-pole {b['verdict']}")
    print("\n  collisional → exponential → single-pole HOLDS")
    print("  free-streaming → power-law Bessel tail (Weinberg) → single-pole FAILS")
    print("  collisionality (which branch) is the free datum ⇒ single_pole is an ANCHOR.")
    print(f"\n  de-anchor: {settle_condition()}")
