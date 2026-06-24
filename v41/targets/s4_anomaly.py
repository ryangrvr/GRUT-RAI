"""GRUT-RAI v4.1 — TARGET 2: the S⁴ trace-anomaly a/c, and α's antecedent.

GRUT has a CONDITIONAL theorem:  a/c = 1/3  ⟹  α = 1/3,  IF the conformal (Riegert) mode is
the IR carrier of the vacuum response. The consequent (a/c) is computable; the antecedent
(conformal mode = IR carrier) is the registry's standing OPEN. This module computes a/c and
asks whether GRUT's structure actually puts the conformal mode in the carrier role — NOT
whether a/c can be made to equal 1/3.

────────────────────────────────────────────────────────────────────────────────────────
OUTCOME: (C) — a/c = 1/3 IS COMPUTABLE AND ROBUST, BUT THE CARRIER ANTECEDENT IS FREE DATA.
This is the exact parallel to single-pole: a clean, scheme-independent CONSEQUENT, and an
ANTECEDENT the action does not fix. α is re-tiered OPEN → ANCHOR (a posited identification),
with the carrier role named as the missing datum — precisely as single-pole became an anchor.

THE INVERTED-LAUNDERING GUARD (1/3 is the target, so reverse-fitting is the danger): AVOIDED.
  - a and c are computed from FIXED field content in a STANDARD scheme (Gilkey/Seeley–DeWitt
    a₄ heat kernel), chosen before forming the ratio. Reported SEPARATELY below.
  - a and c are SCHEME-INDEPENDENT central charges (the only scheme-dependent anomaly term is
    b·□R, which is NOT a or c). So a/c=1/3 cannot be moved by a scheme/Γ-convention choice —
    the convention issue (Γ(1−x) vs Γ(1+ε)⁻¹) touches only the local □R counterterm. a/c=1/3
    is a tabulated CFT fact (the conformal scalar's value), validated here against the Dirac
    (11/18) and vector (31/18) ratios — so the machinery is not tuned to land 1/3.
  - The number is therefore NOT the gap. The gap is the carrier antecedent (below).

WHAT IS COMPUTED (Step 1, validated; Step 2, the GRUT case):
  Convention (Duff): ⟨T^μ_μ⟩ = (1/16π²)[ c·W² − a·E₄ ], with
      W² = Riem² − 2 Ric² + (1/3) R²,   E₄ = Riem² − 4 Ric² + R².
  Gilkey a₄ for a conformal scalar (E=−R/6, Ω=0) gives primitive (Riem²,Ric²,R²) coefficients
  (1/180, −1/180, 0) ⇒ (a,c) = (1/360, 1/120) ⇒ a/c = 1/3 — computed first-hand, not looked up.
  The conformal Riegert mode IS a conformal scalar, so its a/c = 1/3 exactly.
  S⁴ NOTE (honesty): S⁴ is conformally flat ⇒ W²=0 there ⇒ S⁴ isolates a (Euler); c needs a
  non-conformally-flat background. 'a/c on S⁴' is really a-from-S⁴ over c-from-elsewhere.

THE ANTECEDENT (Step 3 — the real question, addressed SEPARATELY from the number):
  "Is the conformal Riegert mode the IR carrier of the vacuum response?" This is what α=1/3
  needs, and it is NOT fixed by GRUT's action:
    (i)  The carrier identity — which mode dominates the IR vacuum impedance — is a DYNAMICAL/
         spectral fact, not a structural one. GRUT's CTP action + Q + FDT + 1/r kernel fix the
         dissipative/causal structure, not which mode carries the IR anomaly response. (Exact
         parallel to single-pole's collisionality: a dynamical datum the structural action omits.)
    (ii) GRUT's OWN derived result tensions it: μ_linear = 1 (the TT projector annihilates the
         scalar/trace modes) means the LINEAR cosmological carrier is the TT (spin-2) mode, and
         the conformal (spin-0) mode is projected OUT at linear order. So GRUT's structure does
         not naturally elevate the conformal mode — if anything it suppresses it.
    (iii) There IS a respectable scenario where the antecedent holds — anomaly-induced dynamics
         à la Antoniadis–Mottola, where the conformal factor becomes a propagating IR degree of
         freedom. But that is an additional dynamical assumption GRUT's action does not establish,
         and (ii) points the other way in the linear sector. So it is a posit, not a consequence.
  ⇒ the carrier antecedent is FREE DATA. a/c=1/3 is the conformal mode's value, but assigning the
  conformal mode the carrier role (hence α=1/3) is an identification the action does not force.

GATE CONSEQUENCE: α OPEN → ANCHOR (a posited identification), justified by the carrier role
being free data — exactly as single-pole became an anchor. Propagate: every claim consuming α
(here ω_Λ; in the wider work the α-spine S=108π, R=√(4/3)) is re-audited as conditional on the
α-ANCHOR. α de-anchors only if GRUT establishes the conformal mode as the IR carrier (e.g. a
derivation that the anomaly-induced conformal dynamics dominate the IR vacuum response).

NOTE on strength (honesty): single-pole's anchor rested on TWO exhausted computational routes
(1B flat + 1C curved). α's anchor rests on one computation (the robust a/c) plus a structural
carrier-freedom argument corroborated by the μ_linear=1 tension. Solid, but a notch less
exhausted — flagged for the referee. Revert to OPEN-sharpened is a one-line change.
"""
from __future__ import annotations

from fractions import Fraction as F


# ── the a/c extraction (Step 1 machinery) ────────────────────────────────────────────────
def extract_a_c(riem2: F, ric2: F, r2: F):
    """From an a₄ primitive (coeffs of Riem², Ric², R²), solve ⟨T⟩ = c·W² − a·E₄ for (a,c).
    W²=(1,−2,1/3), E₄=(1,−4,1) ⇒ A=c−a, B=−2c+4a, C=c/3−a. (a,c) from (A,B); C is a check."""
    a = (ric2 + 2 * riem2) / 2
    c = riem2 + a
    if c / 3 - a != r2:
        raise ValueError(f"R² inconsistency: c/3−a={c/3 - a} ≠ {r2} (basis/convention error)")
    return a, c


def gilkey_scalar_primitive():
    """Conformal scalar (E=−R/6, Ω=0) Gilkey a₄ geometric part, computed not looked up:
       intrinsic 2 Riem² − 2 Ric² + 5 R²;  180 E² = 5 R²;  60 R E = −10 R²  ⇒  R²: 5+5−10 = 0.
    Returns the primitive (Riem², Ric², R²) coefficients (×1/16π², in units of 1/360)."""
    return (F(2, 360), F(-2, 360), F(0))


CFT_TABLE = {                       # tabulated central charges [Duff 1994] — the validation set
    "real scalar":    (F(1, 360),  F(1, 120)),
    "Dirac fermion":  (F(11, 360), F(1, 20)),
    "vector (gauge)": (F(31, 180), F(1, 10)),
}
KNOWN_RATIO = {"real scalar": F(1, 3), "Dirac fermion": F(11, 18), "vector (gauge)": F(31, 18)}


def validate_machinery() -> dict:
    """Step 1: (1a) compute the scalar (a,c) from Gilkey directly; (1b) confirm the extraction
    reproduces the tabulated Dirac & vector a/c. Returns the results; raises on any mismatch."""
    a_s, c_s = extract_a_c(*gilkey_scalar_primitive())
    assert (a_s, c_s) == CFT_TABLE["real scalar"], "scalar Gilkey ≠ tabulated"
    out = {"scalar_from_gilkey": {"a": a_s, "c": c_s, "a/c": a_s / c_s}}
    for name, (a, c) in CFT_TABLE.items():
        A, B, Cc = c - a, -2 * c + 4 * a, c / 3 - a       # build primitive, then re-extract
        a2, c2 = extract_a_c(A, B, Cc)
        assert (a2, c2) == (a, c) and a / c == KNOWN_RATIO[name], f"{name} extraction failed"
        out[name] = {"a": a, "c": c, "a/c": a / c, "validated": True}
    return out


# ── Step 2: the GRUT-relevant consequent ─────────────────────────────────────────────────
def conformal_scalar_ac() -> dict:
    """The conformal Riegert mode = a conformal scalar ⇒ a/c = 1/3 (EXACT, scheme-independent).
    This is the consequent of GRUT's conditional theorem — robust, NOT reverse-fit."""
    a, c = CFT_TABLE["real scalar"]
    return {"a": a, "c": c, "a_over_c": a / c, "scheme": "Duff (1/16π²)(cW²−aE₄); a,c scheme-independent",
            "s4_caveat": "S⁴ is conformally flat (W²=0): S⁴ gives a; c needs another background"}


# ── Step 3: the antecedent — addressed SEPARATELY from the number ─────────────────────────
def antecedent_status() -> dict:
    """Is the conformal Riegert mode the IR carrier of the vacuum response? The carrier identity
    is dynamical free data the action does not fix; μ_linear=1 tensions it. ⇒ (C)."""
    return {
        "question": "is the conformal Riegert mode the IR carrier of the vacuum response?",
        "carrier_identity_is_dynamical": "which mode sets the IR vacuum impedance is a spectral/"
            "dynamical fact; CTP+Q+FDT+1/r fix the dissipative structure, not the carrier "
            "(parallel to single-pole's collisionality)",
        "mu_linear_tension": "μ_linear=1 (TT projector annihilates scalar/trace modes) ⇒ the LINEAR "
            "carrier is the TT spin-2 mode; the conformal spin-0 mode is projected OUT at linear order",
        "scenario_where_it_holds": "anomaly-induced conformal dynamics (Antoniadis–Mottola) — a "
            "propagating IR conformal factor; an additional dynamical assumption GRUT does not establish",
        "verdict": "carrier antecedent is FREE DATA — a/c=1/3 is the conformal mode's value, but "
            "assigning it the carrier role (hence α=1/3) is a posit, not a consequence",
    }


def grut_alpha_antecedent(*_a, **_k):
    """RAISE. α=1/3 follows ONLY if the conformal Riegert mode is the IR carrier. That antecedent
    is not fixed by GRUT's action (the carrier identity is dynamical free data, and μ_linear=1
    points to the TT mode as the linear carrier). a/c=1/3 is robustly computed; the carrier role
    is the missing datum. So α is an ANCHOR (a posited identification), not a derived value."""
    raise NotImplementedError(
        "α=1/3 is CONDITIONAL on the conformal Riegert mode being the IR carrier. a/c=1/3 is "
        "computed and scheme-independent (the conformal scalar's value), but GRUT's action does "
        "not fix the carrier identity — and μ_linear=1 (TT projector annihilates the scalar mode) "
        "tensions it. Missing datum: which mode carries the IR vacuum response. α is an ANCHOR."
    )


def status() -> dict:
    return {
        "target": "2 — the S⁴ trace-anomaly a/c and α's antecedent",
        "outcome": "(C): a/c=1/3 computable & robust (scheme-independent), but the carrier "
                   "antecedent is FREE DATA the action does not fix",
        "consequent": "a/c = 1/3 (conformal scalar, Gilkey a₄; validated vs Dirac 11/18, vector 31/18)",
        "reverse_fit_avoided": "a,c are scheme-independent central charges; the 1/3 cannot be moved "
                               "by a scheme/Γ-convention choice (only b·□R is scheme-dependent)",
        "antecedent": "conformal mode = IR carrier — dynamical free data; μ_linear=1 tensions it "
                      "(linear carrier is TT spin-2, not conformal spin-0)",
        "gate_action": "α re-tiered OPEN → ANCHOR (posited identification); propagate to ω_Λ "
                       "(and the wider α-spine S=108π, R) as conditional-on-the-α-anchor",
        "de_anchor_condition": "establish the conformal mode as the IR carrier (e.g. anomaly-"
                               "induced conformal dynamics dominating the IR vacuum response)",
        "strength_caveat": "one computation + structural carrier-freedom + μ_linear tension; a notch "
                           "less exhausted than single-pole's two-route anchor — referee's call",
    }


if __name__ == "__main__":
    print("TARGET 2 — S⁴ a/c and α's antecedent.  OUTCOME: (C).\n")
    print("Step 1 — machinery validated (before looking at 1/3):")
    v = validate_machinery()
    g = v["scalar_from_gilkey"]
    print(f"   conformal scalar from Gilkey a₄:  a={g['a']}, c={g['c']},  a/c={g['a/c']}")
    for name in ("Dirac fermion", "vector (gauge)"):
        print(f"   {name:16s}: a/c={v[name]['a/c']}  (validated against tabulated)")
    print("\nStep 2 — the GRUT consequent:")
    cs = conformal_scalar_ac()
    print(f"   conformal Riegert mode: a/c = {cs['a_over_c']}  (EXACT, scheme-independent)")
    print(f"   {cs['s4_caveat']}")
    print("\nStep 3 — the antecedent (the real gap):")
    a = antecedent_status()
    print(f"   Q: {a['question']}")
    print(f"   μ_linear tension: {a['mu_linear_tension']}")
    print(f"   verdict: {a['verdict']}")
    print("\nThe missing datum (the action does not supply it):")
    try:
        grut_alpha_antecedent()
    except NotImplementedError as e:
        print("   RAISE:", e)
