"""GRUT-RAI v4.1 — STEP 4, TARGET 2: the S⁴ Riegert/Paneitz a/c coefficient.

This decides α's antecedent. The structure:
  - PROVEN (conditional): IF the gravitational conformal mode is the IR carrier of
    the vacuum susceptibility, THEN the trace-anomaly ratio a/c = 1/3 (Duff;
    Komargodski–Schwimmer). Fraction-exact, normalization-independent.
  - OPEN (decisive, kinematic): the 4th-order Riegert/Paneitz a/c on S⁴ — a STATIC
    curved-space coefficient (NOT a propagating EOM; the dynamical completion is
    structurally blocked by the 1/k⁴ pole + Paneitz ghost, so we stay kinematic).
  - Criterion: a/c = 1/3 closes the keystone (with monopole dominance); a/c ≠ 1/3
    FALSIFIES the conformal-scalar identification and FREES α's value. Decisive
    either way — which is what the framework prizes.
"""
from __future__ import annotations

from fractions import Fraction


def a_over_c_under_identification() -> Fraction:
    """The PROVEN conditional result: a/c = 1/3 under the IR-carrier identification.
    Normalization-independent (so it cannot be reverse-fit)."""
    return Fraction(1, 3)


def compute_S4_anomaly_ac(*_args, **_kwargs) -> Fraction:
    """THE DECISIVE OPEN CALCULATION. Compute the 4th-order S⁴ Riegert/Paneitz a/c
    as a KINEMATIC anomaly ratio on the sphere (static coefficient), then compare to
    1/3. This is the one named computation that closes (or falsifies) α = 1/3."""
    raise NotImplementedError(
        "OPEN target: compute the 4th-order S⁴ Riegert/Paneitz a/c (kinematic). "
        "a/c=1/3 ⇒ α antecedent closes; a/c≠1/3 ⇒ conformal-scalar identification "
        "falsified, α's value freed. Stay kinematic (dynamical completion is blocked)."
    )


def status() -> dict:
    return {
        "target": "S⁴ Riegert/Paneitz a/c (kinematic anomaly ratio)",
        "state": "OPEN",
        "proven_conditional": "a/c = 1/3 under the IR-carrier identification (Duff; KS)",
        "decisive_unknown": "the 4th-order S⁴ a/c coefficient itself",
        "criterion": "=1/3 closes α (with monopole dominance); ≠1/3 falsifies + frees α",
        "blocks": ["alpha"],
    }


if __name__ == "__main__":
    print("TARGET 2 — S⁴ a/c:", status()["criterion"])
    print("  proven conditional a/c =", a_over_c_under_identification())
    try:
        compute_S4_anomaly_ac()
    except NotImplementedError as e:
        print("  decisive calc:", e)
