# S6-1 — COARSE-GRAINED ARROW VERDICT 01

**Mechanical terminals (charter §4), proposed for owner adjudication:**
- **Primary:** **NET-ARROW-CONFIRMED**
- **Secondary:** **NO-ERASURE-ON-OPEN-MEMBERS**

**HARD STOP.**

## Provenance

| Item | Value |
|---|---|
| Authority | `S6_OWNER_RULING_01.md` (comment `5914432316`); one S6-1 analytic/certified execution under the S6-1 v4 exception |
| Frozen charter | `S6_1_COARSEGRAINED_ARROW_CHARTER_01.md` at `fbd15c8` |
| Theorem block | `S6_1_THEOREM_01.md`. Draft `303d3f3`/`303a216`; **independently verified** and committed at `122928a`, with VC-1 (edge phases) and VC-2 (analytic non-degeneracy) |
| Script | `calc/s6_1_certify.py`, committed at `84e244d` **before** its run. Pre-run primitive tests used non-member controls only, and are disclosed in its header |
| Result | `S6_1_RESULT.json` (sha256 `f0f88f40…`) |
| Execution | **One** run, 65.5 s. All adjudicating arithmetic was `mpmath.iv` at 128 bits. No RNG, no simulation, no float gate |

## 1. Integrity (P-7): all pass, with `defects = []`

- **(i)** The quadrature reproduces the exact values: m₀ = 1, m₁ = 2.3, m₂ = 6.29, and ∫λ⁻¹dμ = r.
- **(ii)** At t = 0, every member reproduces:
  - the declared initial covariances (Q₁₁ = T_s/2.3, P₁₁ = T_s, Q₁₂ = C₁₁ = J = 0);
  - ΔQ₁₂(0) = −T_b r²;
  - X_f(0) = X_f′(0) = 0;
  - the LS-2 value of X_f''(0).
- **(iii)** The derivative of the X_J jet contains J from its independent formula at t = 1/3, 2 and 5.
- **(iv)** The tail constants V_{k,w} are finite and positive.
- **(v)** At T\*, the LS-2 closed forms lie inside the enclosures widened by the LS-4 bound. For σ, D(T\*) ≤ ½ε².

## 2. Primary: T-1 and T-2 (theorem-grade: LS-1/LS-2 verified, and integrity passes)

**T-1: net bath self-energy transfer, forward-oriented.** X_f(∞) = ±[(T_s − T_b) + ½T_b r²], with r = (2.3 − √1.29)/2 and
½T_b r² = 0.16943 (the equal-temperature offset, A-3).

| Member (T_s, T_b) | X_f(∞) | Sign |
|---|---|---|
| (2, 1) | 1.16943 | **+** |
| (10, 1) | 9.16943 | **+** |
| (1/2, 1) | 0.33057 | **+** |
| (1/10, 1) | 0.73057 | **+** |

**T-2: net entropy-reference approach.** X_σ(∞) = D(0).

| Member (T_s, T_b) | X_σ(∞) = D(0) | Sign |
|---|---|---|
| (2, 1) | 0.19967 | **+** |
| (10, 1) | 5.57787 | **+** |
| (1/2, 1) | 0.27578 | **+** |
| (1/10, 1) | 1.53584 | **+** |

**Both observables carry the forward sign at every declared member, so the primary terminal is NET-ARROW-CONFIRMED.**

## 3. Secondary: T-3 and T-4, no erasure on the open members (certified protocol)

| Member | T₀ (small-T certified) | T\* (LS-4 formula) | Main boxes | Unresolved | Verdict |
|---|---|---|---|---|---|
| J, (2, 1) | 1/16 | 7.366 | 141 | 0 | **TRUE** |
| J, (10, 1) | 1/16 | 5.902 | 118 | 0 | **TRUE** |
| σ, (1/2, 1) | 1/32 | 5.264 | 147 | 0 | **TRUE** |
| σ, (1/10, 1) | 1/64 | 5.115 | 178 | 0 | **TRUE** |

- On every open member, X_f(T) > 0 is **proved** for all T > 0. The proof has three parts: the Taylor bound on
  (0, T₀], certified mean-value boxes on [T₀, T\*], and the LS-4/LS-5 tail bound for T ≥ T\*.
- The resource use was far below the cap.
- **The secondary terminal is NO-ERASURE-ON-OPEN-MEMBERS.**

**Controls (the already-decided switch-on failures, reported separately).** Negativity of X_f on (0, T₀] was
re-certified at all four control members:

| Control | X_f''(0) |
|---|---|
| J, (1/2, 1) | −0.2174 |
| J, (1/10, 1) | −0.0435 |
| σ, (2, 1) | −0.2911 |
| σ, (10, 1) | −0.5239 |

K-2 therefore stays **FALSE from switch-on** on J-L2 and σ-L1. These are the controls, not targets.

## 4. LS-3 and the cross-checks (report-only)

**LS-3.** The leading amplitude P(t) takes certified different values at t = 0 and t = 1 at every member, which is
consistent with the analytic proof p₄,₀ > 0 (VC-2). **Ḋ has leading class t⁻⁶ and changes sign at arbitrarily late
times.**

**The finite-N cross-check.** N = 95, float64, at T ∈ {0.5, 1, 2, 4, 8}, below T_rec.
- It agrees with the midpoints of the N = ∞ enclosures to 6 decimal places.
- It shows the switch-on behaviour directly. For example, at (1/2, 1) the record-convention X_J is +0.020 at
  T = 0.5 and then goes negative, i.e. the forward quantity becomes positive.

## 5. Statement (charter §6 fence)

> **In the declared infinite conservative pinned chain, the integrated bath-self-energy transfer and the
> reduced-state entropy measure retain a net direction despite arbitrarily late band-edge-memory backflow.**
>
> At the members where "never completely erased from switch-on" was open (J on L1, σ on L2), **cumulative
> forward progress is never erased at any time.** Where the switch-on identity fixes the direction (J on L2, σ on
> L1), the running total is negative at first. Its limit is still positive.

**Pointwise arrow: NO** (O-6 stays FALSIFIED; Ḋ and J reverse sign at arbitrarily late times).
**Integrated / net arrow: YES** (theorem-grade, at every declared member).

**Not claimed:**
- that monotonicity is restored;
- that O-6 is repaired;
- that microscopic reversibility is gone;
- a fundamental thermodynamic arrow;
- that J is a unique heat current (it is the bath self-energy flux, with offset ½T_b r²).

**The Ḋ-tail correction to O-6** (its t⁻³ wording is a valid upper bound; the leading class is t⁻⁶) is ready for an
additive note once the owner accepts it. No O-6 terminal changes.

## 6. HARD STOP

The result and verdict are committed, and CURRENT_STATE is updated.

**Nothing is opened:**
- no second run;
- no S-4, S-7 or S-8;
- no S5-WB or S5-OD;
- no new reversal diagnostic;
- nothing on gravity, Π₀ or cosmology.
