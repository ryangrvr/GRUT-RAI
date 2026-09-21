# T3-01 — ANALYTIC REDUCTION OF THE DANGEROUS COEFFICIENT

**Date:** 2026-09-16 · **Status:** derivation + machine check (`t3_01_ir_coefficient.py`)
**Reads (frozen, unmodified):** `WALL_KR_TIER3_IR_CHECK_RESULT.json`,
`WALL_KR_TIER3_FORK_ADJUDICATION.md`, the Wall-A A3-3/A3-4 chain.

---

## 1. What the frozen record fixes

1. The dangerous IR structure at `k_ext = 0` belongs to the **noise/secular
   class** (retarded α = −1 is protected by the δ-support at q = ω/2; the
   α = −2 power class at `k_ext = 0` is where the divergence lives).
2. The flat-slicing decomposition of the internal-leg object is
   `O_flat = O_constTT + O(q)`, with the `O(q)` remainder IR-finite.
3. The constant-TT mode `ε_ij` is **simultaneously** TT and the image of
   the linear spatial diffeomorphism `ζ^i = ½ ε^i{}_j x^j` **at the
   patch-local level**.

## 2. The reduction

Let `P_⊥` be the quotient projector on the patch-local TT mode space that
removes exactly the declared linear-diffeomorphism sector
(`h^gauge_ij = ε_ij`). Every internal TT mode function has the small-q
expansion

    h_q = ε · f₀ + O(q)          (f₀ = the constant-mode amplitude)

so

    P_⊥ h_q = O(q)               EXACTLY, mode by mode.

The dangerous term in the loop integrand is carried **entirely** by the
`ε·f₀` component (premise 2 above: the remainder is `O(q)` and finite).
Therefore the integrand after quotienting is `O(q)`-bounded and

    C_raw ≠ 0   (the frozen divergent coefficient)
    C_quotient = 0              — IDENTICALLY, by construction.

**This is not a computation; it is an identity.** The entire coefficient
of the dangerous IR term is proportional to `⟨ε, h_q⟩ ⟨ε, h_{q'}⟩`
sandwiched between the vertices, and the quotient projector annihilates
that factor at leading order mode-by-mode. No partial cancellation, no
numerical accident: the object the divergence lives on is the object the
quotient removes.

## 3. What this does NOT decide (the honest scope)

- **Commutation with the loop integral.** The projector acts mode-by-mode
  on field space; the loop integral integrates over q. The identity above
  is a statement about the integrand. Passing from "integrand finite" to
  "integral finite" requires the `O(q)` remainder to be uniformly
  integrable on the patch — true locally, but the **global** statement
  depends on the spatial boundary condition (Case 3 of the fork).
- **Global gauge equivalence.** Nothing here establishes that `ζ` is a
  legitimate transformation on the static patch globally. The
  declaration is patch-local, per spec.
- **Case 3 survives.** If the boundary data re-admits the constant mode
  (e.g. global hyperbolicity forcing quantization on the full patch),
  the divergence re-enters as *boundary data*, not as a local kernel
  failure. The two statements are compatible and this is the live fork.

## 4. Consequences that ARE decided at this scope

1. **The coefficient comparison is trivial.** `C_quotient = 0`
   identically. T3-01's numerical job is therefore not "measure C" but
   (a) machine-verify the two load-bearing premises, and (b) certify the
   `O(q)` remainder: bounded, integrable, and with a well-defined
   `H → 0` limit.
2. **The nonuniform limit question stands.** With the constant mode
   removed, `k_ext = 0` and `k_ext → 0` probe different things: at
   `k_ext = 0` exactly, the external projector has support on the
   removed class, so the *raw* and *quotient* responses differ by the
   full constant-mode contribution; for `k_ext → 0` the external probe
   decouples from the zero mode continuously. The order-of-limits
   noncommutation `lim_k lim_ω ≠ lim_ω lim_k` in the RAW object is a
   **predictor** of the fork, not an artifact.
3. **Flat-limit test.** The frozen H-parity record (assembly2c: ω²(η;H)
   exactly even in H) applies to the `O(q)` remainder: the quotiented
   response has a regular `H → 0` limit equal to the Minkowski
   response, coefficient by coefficient, **provided** the boundary
   prescription does not re-admit the constant mode (Case 3 modifies
   this statement by adding H-dependent global data that need not have
   a smooth flat limit — that would be the "new IR object" branch).

## 5. The verdict fork, restated at T3-01 scope

| Case | Statement | T3-01 signature |
|---|---|---|
| 1 | constant TT is gauge | `C_q = 0`; remainder finite; smooth flat limit |
| 2 | constant TT physical | `C_q = C_raw ≠ 0` — impossible under the declared projector (identity) |
| 3 | boundary-dependent | `C_q = 0` locally AND raw divergence re-enters via global data — the two-level structure |

**T3-01 therefore answers Case 1 vs Case 3, never Case 2.** The physics
question is no longer the coefficient; it is the boundary prescription.

## 6. What the machine check does

`calc/t3_01_ir_coefficient.py`:

- **E1:** symbolic verification that `ζ^i = ½ ε^i{}_j x^j` generates
  `h_ij = ∂_i ζ_j + ∂_j ζ_i = ε_ij`, trace-free and transverse (the
  diffeo-image identity).
- **E2:** symbolic construction of the quotient projector `P_⊥` on the
  TT mode space and verification `P_⊥ h_q = O(q)` at small q.
- **E3:** numerical demonstration on a scalar model of the dangerous
  channel: raw integral diverging as the frozen power class vs the
  quotiented remainder finite, with the `k_ext/H` sequence
  `10^{-1} … 10^{-5}` and the `k_ext = 0` point evaluated separately
  (they are different evaluations, per §4.2).
- **E4:** flat-limit check of the remainder: the quotiented model
  response at finite H vs the H → 0 Minkowski value.

Declarations: patch-local scope only; no global gauge claim; no frozen
artifact modified; W-0 — computed-and-reported, not banked.
