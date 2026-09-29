# L0 ACCESS — RANK-DROP THEOREM 01 (L0-1c, theorem only)

**Status: THEOREM RECORD FOR OWNER RULING. No simulation, no member evaluation, no sweep.**
- **Authority:** `L0_ACCESS_BRIDGE_OWNER_RULING_01.md` §3. It was sequenced after the
  verification, which found the CL-3/CL-4/CL-5 definitions **sound**
  (`L0_ACCESS_BRIDGE_VERIFICATION_01.md` §4).
- **Proof support:** symbolic checks on abstract chains.
  - `calc/feasibility/bridge_verify/s2_nonlinear_rank.py` (verifier; re-run by the operator, it
    reproduced);
  - `calc/feasibility/rankdrop/end_site_general.py` (operator; *arbitrary* on-site
    nonlinearities, N = 3, 4, 5).
- **Independence note.** The operator reached the end-site argument from the K_b construction
  before the verification returned. The verifier derived the same lemma independently. The proof
  below is the operator's, with the verifier's symbolic checks as support.

**The question (owner):**

> Can the nonlinear observability or accessibility structure lose rank at particular states even
> though the interaction graph never changes?

**Outcome scale:** RANK-CONSTANT · RANK-DROP-EXISTS · CLASS-SPLIT · PROBE-DEPENDENT · UNFORMULABLE.
A rank drop counts as a candidate structural access change **only if it changes the exact
distinguishability structure.**

## §0 Result

| Leg | Declaration | Proposed outcome | Grade |
|---|---|---|---|
| **Observability** | **The earned output:** the identity readout h = x₁ at the retained end site of K_b | **RANK-CONSTANT.** Rank N at *every* state, and global observability: every indistinguishability class is a singleton. | **theorem** (Theorem 1) |
| Accessibility | **No earned input.** With the **priced** probe g = e₁ (L0-1c's impulse direction) | **PROBE-DEPENDENT.** With that probe the accessibility rank is N at every state. | theorem (Theorem 2), conditional on the priced input |
| Observability, unearned declarations | interior sites; multi-site sets; non-injective readouts | Drops **can** exist (an explicit N = 3 interior quadric; x₁² on the linear flow). **For K_b's interior sites: NOT ESTABLISHED.** | example + open |

**Consequence (factual, not a ruling).** At the earned declaration, the L0-1c nonlinear flow
produces **no** state-dependent observability or indistinguishability structure. The one
remaining direct classical opportunity named by the owner is therefore **closed at earned
scope.** It survives only under access declarations the record does not earn, and those would be
priced.

## §1 Setting (from the record)

- **Chain.** K_b is the (1:,1:) block of `build_K(24, 0)` (`L0_1C_CHARTER_01.md:61-67`;
  `calc/c1_seam.py:58-69`). It is a **path** on 23 sites with diagonal entries dₖ (2.3 in the
  interior and at the retained site; 1.3 at the far end) and off-diagonal entries −wₖ, where
  **wₖ = 1 ≠ 0** (the springs; 1 + ε on the modulated set, with ε = 0 in L0-1c).
- **Dynamics:** ẋ = f(x) = −K_bx − 4βx^{∘3}. Componentwise,
  fₖ = −dₖxₖ + w_{k−1}x_{k−1} + wₖx_{k+1} − 4βxₖ³ (with w₀ = w_N := 0).
- **Retained observable:** x[0] (`calc/l01c_linearity.py`, the recorded readout), i.e. **site 1,
  an end of the path.**
- **Forward completeness:** V is coercive for β ≥ 0, so solutions are global
  (`L0_1C_CHARTER_01.md` §3).
- **Definitions** (verification §4):
  - 𝒪 = span{L_fʲ h}, and Φ = (L_f⁰h, …, L_f^{N−1}h) : ℝᴺ → ℝᴺ;
  - x I x′ iff h(φ_t x) = h(φ_t x′) for all t ≥ 0.

## §2 Theorem 1 (end-site observability is rank-constant and global)

**Statement.** Let f be any vector field on ℝᴺ of the form

> fₖ(x) = −dₖxₖ − gₖ(xₖ) + w_{k−1}x_{k−1} + wₖx_{k+1},

with every wₖ ≠ 0 (k = 1…N−1) and each gₖ smooth (**any on-site nonlinearity**). Let h(x) = x₁.
Then:
- **(i)** φⱼ := L_fʲh depends only on x₁…x_{j+1} and is **affine in x_{j+1} with constant
  coefficient** cⱼ = ∏_{k=1}^{j} wₖ;
- **(ii)** DΦ is lower-triangular with constant determinant ∏_{k=1}^{N−1} wₖ^{N−k} ≠ 0, so
  **rank d𝒪(x) = N for every x ∈ ℝᴺ**;
- **(iii)** Φ is a bijection of ℝᴺ, with inverse obtained by successive solution;
- **(iv)** for forward-complete f (β ≥ 0 here), **x I x′ ⟹ x = x′**. Every indistinguishability
  class is a singleton, at every state.

**Proof.**
- **(i), by induction.** φ₀ = x₁ holds with c₀ = 1. Suppose φⱼ = cⱼx_{j+1} + ψⱼ(x₁…xⱼ). Then
  φ_{j+1} = Σ_{k≤j+1} (∂ₖφⱼ)fₖ.
  - For k ≤ j, fₖ involves only x_{k−1}, xₖ, x_{k+1}, all of which lie in x₁…x_{j+1}.
  - For k = j+1, ∂_{j+1}φⱼ = cⱼ is constant, and f_{j+1} contains x_{j+2} only through the linear
    term w_{j+1}x_{j+2}. The on-site term g_{j+1} involves x_{j+1} alone.
  - So φ_{j+1} = cⱼw_{j+1}x_{j+2} + (a function of x₁…x_{j+1}), which gives
    c_{j+1} = cⱼw_{j+1}.
- **(ii)** follows directly from (i). The row of dφⱼ has zeros beyond column j+1 and entry cⱼ in
  column j+1. The determinant is ∏ⱼcⱼ.
- **(iii)** Given (φ₀, …, φ_{N−1}), set x₁ = φ₀, and for each j solve
  x_{j+1} = (φⱼ − ψⱼ(x₁…xⱼ))/cⱼ.
- **(iv)** If x ≠ x′, then Φ(x) ≠ Φ(x′) by (iii). So some φⱼ differs, i.e. the j-th time
  derivative at t = 0 of the output differs, and the outputs differ on every interval [0, ε).
  ∎

**Symbolic support:**
- N = 2…6 with the quartic (verifier; diagonal [1, w₁, w₁w₂, …], determinant
  w₁^{N−1}w₂^{N−2}⋯);
- N = 3, 4, 5 with **arbitrary** sympy functions gₖ (operator; the same triangular pattern).

**Applied to the earned L0-1c:** wₖ = 1, so det DΦ = 1 at every state. It holds for every β (and
for every pin, spring modulation ε ≠ −1, and on-site nonlinearity). **RANK-CONSTANT.**

## §3 Theorem 2 (accessibility with the priced end-site probe)

**Pricing, on the face.** The earned model is autonomous, so any control input is an **added probe
datum**. The minimal choice consistent with the record is g = e₁, the direction of L0-1c's
impulse probe x(0) = a·e₁. **This leg is therefore PROBE-DEPENDENT by construction, and does not
carry Theorem 1's evidentiary weight.**

**Statement.** For ẋ = f(x) + u·e₁ with f as in Theorem 1, let v₀ = e₁ and v_{j+1} = [f, vⱼ].
Then vⱼ is supported on sites 1…j+1 with constant (j+1)-th component (−1)ʲ∏_{k≤j}wₖ. So the
matrix [v₀ … v_{N−1}] is upper-triangular with non-zero constant diagonal, and **the accessibility
rank is N at every state.**

**Proof.** [f, v] = (Dv)f − (Df)v.
- If v is supported on 1…j+1 with constant component c at j+1, then (Dv)f is supported on
  1…j, because ∇c = 0.
- Here −Df = K + diag(gₖ′(xₖ)), where K is the path matrix with diagonal dₖ and off-diagonal
  −wₖ. So ((−Df)v)_{j+2} = K_{j+2,j+1}·v_{j+1} = −w_{j+1}c, which is constant. Components beyond
  j+2 vanish. The next front coefficient is therefore −w_{j+1}c, giving
  (−1)^{j+1}∏_{k≤j+1}wₖ.
- Induction gives the claim. ∎

Symbolic support (verifier): N = 3, 4, 5, diagonal [1, −w₁, w₁w₂, −w₁w₂w₃, …].

## §4 Unearned declarations (context; not the theorem's scope)

- **Interior output, N = 3, output x₂:**
  det DΦ = −w₁w₂(12β(x₁² − x₃²) + d₁ − d₃).
  - This is a real quadric of rank-deficient states for β > 0, even where the linear system is
    observable (d₁ ≠ d₃).
  - **Rank drops exist at interior outputs in general.**
  - Whether such a drop also changes the indistinguishability class needs separate analysis: a
    rank drop is not sufficient on its own (verification §4).
- **K_b's interior sites.**
  - At x = 0 the codistribution equals the linear one.
  - The eigenvector components sin(mθ_k), θ_k = (2k−1)π/47, never vanish for m ≤ 23 (47 is
    prime), so the rank is N at 0, and hence generically.
  - **Whether real rank-drop states exist for any interior site of K_b is NOT ESTABLISHED.**
    Deciding it means analysing a large polynomial determinant. That was **not** attempted: it
    would border on a member computation outside this task's authorization.
- **Non-injective readout at the retained site** (x₁² on the linear flow): rank 0 at x = 0 and
  generic rank N. This is a within-site seed (verification §3), and unearned.

## §5 Reading against Routes A/B/C (factual; the route choice is the owner's)

- **Route B (direct classical state-dependent access).** At the earned declaration it is **closed
  by theorem**: there are no rank changes and no state-dependent indistinguishability. It
  survives only under unearned, priced declarations (interior or multi-site access, non-injective
  readouts, added inputs).
- **Route A (generator structure).**
  - Theorem 1's conclusion depends **only on the coupling pattern of K_b** (a path, with non-zero
    wₖ, observed from an end). It does not depend on β, the pin, or the form of the on-site
    nonlinearity.
  - So the observability structure at the earned site is fixed by the generator's support.
  - As with EA-0, this is close to an identity (on-site nonlinearity cannot move a triangular
    front), so it should **not** be over-counted as independent evidence for S-5.
- **Route C (category boundary).** This theorem does not bear on it. The lift side is priced in
  the verification and corrections (KvN, statistics non-selection, and ħ only for physical
  identification).

**HARD STOP** for the owner's ruling on the bridge terminal and Route A/B/C.
