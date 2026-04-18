# STEP 02 — Log: Wick rotation, Euler density, and Im(Γ_CTP)

**Date:** April 2026
**Status:** Completed with one sign correction caught on cross-check.

## What Step 02 sets out to do

Establish rigorously where the Euler-density contribution to the 1-loop
effective action on S⁴ lands in the Lorentzian CTP framework — Re(Γ_CTP)
(dissipation) or Im(Γ_CTP) (decoherence/noise).

This is the formal version of the "imaginary element" physical intuition
from earlier sessions.

## What was done

1. **Gauss-Bonnet evaluation:** ∫E₄√g_E d⁴x_E = 32π² · χ(S⁴) = 64π²
   (real positive topological invariant).

2. **Wick rotation:** t_E = −i·t_L ⇒ d⁴x_L = +i·d⁴x_E.
   The Euler density E₄ itself is a real scalar in both signatures
   (no i factor from the Riemann tensor contractions).

3. **Integrated Euler in Lorentzian:** ∫E₄√(−g_L)d⁴x_L = i·64π² — purely
   imaginary.

4. **Effective action:** using W_L = +i · W_E, the Euler piece becomes
   W_L_Euler = +i · b · 64π². This is purely imaginary in the Lorentzian
   effective action.

5. **CTP decomposition:** Γ_CTP = Re(Γ_CTP) + i·Im(Γ_CTP). The Euler
   piece +i·b·64π² contributes to Im(Γ_CTP) with coefficient +b·64π².
   Re(Γ_CTP) gets zero from the Euler term.

6. **Weyl² note:** The "a" coefficient (Weyl²) does not contribute on S⁴
   at all, because C_μνρσ = 0 identically on a conformally flat space.
   So on S⁴: Im(Γ_CTP) gets +b·64π² from the bulk anomaly; Re(Γ_CTP)
   gets nothing from the bulk anomaly.

## The sign correction (honesty-log entry)

First draft of the script used W_L = −i · W_E, giving Euler contribution
−b·64π² in Im(Γ_CTP). On cross-check against Srednicki §6 and
Peskin-Schroeder §9.5, the correct convention is:

```
Z_E = exp(−W_E),   Z_L = exp(+i · W_L)
Analytic continuation Z_L → Z_E ⇒ i · W_L = −W_E ⇒ W_L = +i · W_E
```

Sign flipped, script corrected. The qualitative conclusion (Euler in
Im(Γ_CTP) not Re(Γ_CTP)) is convention-independent — it follows purely
from the fact that d⁴x_L carries an i factor from Wick rotation. The
specific sign of the contribution depends on the W_L ↔ W_E convention.

Updated conclusion: Im(Γ_CTP) ⊃ **+b·64π²** (not −b·64π² as in the
first draft).

## Cross-check against GRUT's own CTP action

GRUT's V7 eq (1):
```
S_CTP[z_r, z_a] = z_a · F[z_r] + (i/2) · z_a · N · z_a
```

Here `F[z_r]` is the dissipation kernel (couples to real part of Γ)
and `N` is the noise kernel (couples to imaginary part of Γ). Step 02
shows the Euler contribution lands in the imaginary part, which
means it couples to the noise kernel N — the decoherence sector.

This is **structurally consistent** with GRUT's framework-level claim
that the cosmological formula derives from decoherence physics. The
imaginary part of Γ_CTP is exactly where the Euler-density coefficient
naturally sits on S⁴.

Important caveat: this is a consistency check, not yet a derivation of
R = ε. Step 02 establishes that the physical object on S⁴ is the
coefficient of E₄ in Im(Γ_CTP), not the flat-space ratio |b/a|. It
does NOT yet show that this coefficient equals b_free × ε with
ε from Osborn 2003 eq (36) — that requires Step 03.

## Transcendentals tracking

Step 02 introduced: π² (from 4-dim S⁴ volume). No ζ values yet, as
expected at 1-loop. ζ(3) is a 3-loop quantity and should appear in
Step 06 if the derivation proceeds correctly.

## Status labels

- **DERIVED:**
  - ∫E₄√g_E d⁴x_E = 64π² (Gauss-Bonnet + χ(S⁴) = 2)
  - d⁴x_L = +i · d⁴x_E (Wick rotation)
  - Euler piece lands in Im(Γ_CTP) with sign +b·64π²
    (W_L = +i·W_E convention, cross-checked vs Srednicki/PS)

- **STRUCTURAL:**
  - The decoherence-relevant part of Γ_CTP on S⁴ couples to the Euler
    coefficient b, not to |b/a|. The Weyl² coefficient a does not
    enter the bulk anomaly because C² = 0 on S⁴.

- **OPEN:**
  - Whether the coefficient entering Im(Γ_CTP) equals b_free × ε
    (coupling-corrected) or just b_free (free-field). ← Step 03.
  - How forward/backward CTP branches split this coefficient ← Step 05.
  - Whether C_Cosmo/C_Final = ε ← Step 06 (load-bearing).

## Takeaway

Step 02 is clean: the imaginary CTP structure is forced by Wick
rotation, and the Euler density lives in Im(Γ_CTP) exactly where
GRUT's decoherence sector expects it.

The sign-fix caught on cross-check is another successful application
of the honesty protocol — generated a result with the wrong sign on
first draft, caught it within one cycle by comparing against standard
references, documented transparently.

Next: Step 03 — does the coefficient entering Im(Γ_CTP) acquire the
Osborn ε correction when couplings are local? That's where the
cosmological constant problem either closes or stays open.
