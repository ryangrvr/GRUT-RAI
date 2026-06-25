"""GRUT-RAI v4.1 — TARGET 5: commit the bath to resolve collisionality — A FAILED ATTEMPT (record).

The goal was to resolve the single-pole collisionality fork by committing to GRUT being a
"viscoelastic" medium (collisional) and thereby excluding the free-streaming (Weinberg) branch. An
adversarial pre-screen broke it four ways; all are verified first-hand here. The honest outcome:
**this does NOT resolve the fork.** The attempt is kept as a record so it is not retried.

WHY IT FAILS (each verified in __main__):

  1. "VISCOELASTIC" DOES NOT ENTAIL MONOTONE MEMORY. GRUT's own viscoelastic χ_mem (the inertial /
     Standard-Linear-Solid kernel, τ₀τ_K g'' + τ₀ g' + g = 0) is UNDERDAMPED and RINGS for
     τ_K > τ₀/4 (6–12 sign changes) — the round-1 "the vacuum rings" regime. So a relaxational
     constitutive law is NOT monotone in general; monotonicity is a narrower thing.

  2. THE SIGN-CHANGE DISCRIMINATOR IS UNSOUND. The first draft classified collisional-vs-free-
     streaming by "monotone vs oscillatory" (sign changes ≤ 1). But it stamps GRUT's OWN underdamped
     viscoelastic χ_mem "free-streaming" — a false positive on a kernel that is manifestly collisional
     (it is χ_mem, an FDT bath, no kinetics). The clean monotone⟺collisional mapping holds ONLY for
     τ_K < τ₀/4 — which is ALREADY the single-pole regime, so the test silently assumes the answer.
     The real distinction is the ENVELOPE class: EXPONENTIAL (collisional, including the ringing
     underdamped case) vs POWER-LAW (free-streaming). But extracting the envelope of GRUT's *actual*
     kernel is the vertex computation (item 4) — the memory-character commitment does not supply it.

  3. EXCLUDING FREE-STREAMING IS DEFINITIONAL, NOT PHYSICS. Round 3 established that the free-streaming
     branch is a legitimate COLLISIONLESS reading of GRUT's OWN minimal action (the action does not fix
     the branch). Promoting the NAME "viscoelastic" to "defining posit" and reclassifying the
     free-streaming branch as "a different kinetic theory outside GRUT" adds nothing to the action — it
     renames the inconvenient branch out of the theory. The honest statement is: we POSIT GRUT sits on
     the viscous branch of its OWN action; the free-streaming branch is an equally-admissible reading we
     have NOT excluded by computation.

  4. THE FREEDOM DID NOT NARROW — IT MULTIPLIED. Single-pole now requires JOINTLY: (i) the strongly-
     collisional endpoint, (ii) single-τ spectrum width, AND (iii) overdamping τ_K < τ₀/4 — a
     measure-zero corner of a 3-dial space, with the neighbouring region (underdamped) re-growing the
     very oscillatory/dark-pole behaviour the posit was meant to exclude (and re-growing it from INSIDE
     the collisional class). So single-pole is NOT less free than round 3's binary fork; the freedom was
     relabelled "resolved" and fanned into three dials.

NET: the collisionality fork STANDS. "Commit to viscoelastic" is, for the purpose of answering round 3,
equivalent to assuming the overdamped/monotone sub-branch where single-pole lives. The ONLY thing that
converts this from posit to physics is the unchanged de-anchor computation: derive GRUT's actual
finite-T ⟨T_TT T_TT⟩(ω, k→0) from the z·T_TT vertex and read whether it is Ohmic (collisional, Im G_R~ηω,
exponential envelope) or Weinberg (free-streaming, power-law envelope). Target 5 did not do that; it
substituted a posit at exactly the point physics was required.

META (worth recording): this is the SECOND consecutive build-forward target (after the power-spectrum
test) on which the loop directionally over-claimed and the pre-screen caught it. The pattern says the
build-forward path is where the loop's optimism bias is worst; the genuine resolution is the hard vertex
computation + external review, not another in-loop attempt.
"""
from __future__ import annotations

import numpy as np
from numpy.polynomial.legendre import leggauss

_T = np.linspace(0.05, 40.0, 4000)
_MU, _W = leggauss(400)


def chi_mem_kernel(tauK: float, tau0: float = 1.0) -> np.ndarray:
    """GRUT's OWN inertial viscoelastic χ_mem impulse response (τ₀τ_K g'' + τ₀ g' + g = 0).
    Overdamped (monotone) for τ_K<τ₀/4; UNDERDAMPED (rings) for τ_K>τ₀/4 — yet collisional throughout."""
    a, b, c = tau0 * tauK, tau0, 1.0
    r = np.roots([a, b, c])
    return np.real((np.exp(r[0] * _T) - np.exp(r[1] * _T)) / (a * (r[0] - r[1])))


def free_streaming_memory() -> np.ndarray:
    """Collisionless free-streaming (Weinberg): oscillatory, POWER-LAW envelope (~t^-3)."""
    return np.array([np.sum(_W * (1 - _MU ** 2) ** 2 * np.cos(_MU * ti)) for ti in _T])


def memory_sign_changes(K: np.ndarray) -> int:
    return int(np.sum(np.diff(np.sign(K)) != 0))


def sign_change_discriminator_is_unsound() -> bool:
    """The fatal finding (verified): the 'monotone ⇒ collisional' sign-change test MISCLASSIFIES GRUT's
    own underdamped (collisional) χ_mem as free-streaming. Returns True iff the test is unsound, i.e.
    χ_mem rings for τ_K>τ₀/4 while being collisional."""
    return memory_sign_changes(chi_mem_kernel(tauK=1.0)) > 1   # collisional, yet >1 sign change


def envelope_logslopes(K: np.ndarray):
    """Exponential envelope ⇒ |d ln|K|/dt| ~ const (collisional); power-law ⇒ |d ln|K|/d ln t| ~ const
    (free-streaming). The REAL distinction — but it needs GRUT's actual kernel (the vertex computation)."""
    env = np.abs(K); m = (_T > 5) & (_T < 35) & (env > 1e-6)
    return (abs(float(np.polyfit(_T[m], np.log(env[m]), 1)[0])),
            abs(float(np.polyfit(np.log(_T[m]), np.log(env[m]), 1)[0])))


def residual_dials() -> list:
    """Single-pole occupies a measure-zero corner of THREE dials — NOT less free than round 3."""
    return [
        "(i) collision STRENGTH (mean free path) — strongly-collisional endpoint",
        "(ii) relaxation-SPECTRUM WIDTH — single-τ (Maxwell) vs broad (gel)",
        "(iii) OVERDAMPING τ_K < τ₀/4 — outside it GRUT's own χ_mem rings and re-grows the dark pole",
    ]


def status() -> dict:
    return {
        "target": "5 — commit the bath to resolve collisionality: FAILED (record)",
        "outcome": "does NOT resolve the fork. The sign-change discriminator is UNSOUND (misclassifies "
                   "GRUT's own underdamped viscoelastic χ_mem as free-streaming); excluding free-streaming "
                   "is DEFINITIONAL (the branch is internal to GRUT's action); single-pole is a measure-zero "
                   "corner of a 3-dial space, NOT less free than round 3",
        "real_distinction": "envelope class (exponential=collisional vs power-law=free-streaming) — but it "
                            "needs GRUT's ACTUAL kernel, i.e. the vertex computation, not a memory-character posit",
        "the_only_resolution": "derive finite-T ⟨T_TT T_TT⟩(ω,k→0) from the z·T_TT vertex; Ohmic ⇒ collisional/"
                               "single-pole, Weinberg ⇒ free-streaming/refuted (the unchanged 1D de-anchor)",
        "meta": "second consecutive build-forward target over-claimed and caught by pre-screen — the genuine "
                "resolution is the hard vertex computation + external review, not another in-loop attempt",
    }


if __name__ == "__main__":
    print("TARGET 5 — commit the bath to resolve collisionality: FAILED (honest record).\n")
    print("1+2. GRUT's OWN viscoelastic χ_mem rings for τ_K>τ₀/4, and the sign-change test misclassifies it:")
    for tauK in (0.1, 0.24, 0.5, 1.0, 4.0):
        sc = memory_sign_changes(chi_mem_kernel(tauK))
        regime = "overdamped" if tauK < 0.25 else "UNDERDAMPED (rings)"
        verdict = "collisional ✓" if sc <= 1 else "stamped FREE-STREAMING ✗ (it IS GRUT collisional χ)"
        print(f"   τ_K={tauK:4.2f} ({regime:18s}): sign changes={sc:2d} → {verdict}")
    print(f"\n   sign-change discriminator is UNSOUND? {sign_change_discriminator_is_unsound()}")
    es_chi = envelope_logslopes(chi_mem_kernel(1.0)); es_fs = envelope_logslopes(free_streaming_memory())
    print(f"\n   REAL distinction (envelope): χ_mem |dln|K|/dt|={es_chi[0]:.2f} (exponential=collisional); "
          f"Weinberg |dln|K|/dln t|={es_fs[1]:.2f} (power-law=free-streaming)")
    print("   — but reading the envelope of GRUT's ACTUAL kernel is the vertex computation, not done here.")
    print("\n   single-pole is a measure-zero corner of 3 dials (NOT less free than round 3):")
    for d in residual_dials():
        print(f"      {d}")
    print("\n   ⇒ the fork STANDS. The only resolution is the z·T_TT vertex computation (unchanged de-anchor).")
