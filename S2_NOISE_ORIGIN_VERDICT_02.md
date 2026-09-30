# S2-1 — NOISE-ORIGIN VERDICT 02 (corrective execution)

**Mechanical terminal: FULL-DISCRIMINATOR-CONFIRMED.**
- This is proposed for owner adjudication. **HARD STOP.**
- The first execution stays **RUN VOID**, per `S2_NOISE_ORIGIN_VERDICT_01.md` and ruling S2-02 §1. It is
  preserved unchanged. **Nothing from it is used here.**

## Provenance

| Item | Value |
|---|---|
| Authority | `S2_OWNER_RULING_02.md` (comment `5908791267`): one corrective execution |
| Frozen charter (unchanged) | `227dd09` |
| Verified derivation (unchanged) | `32645cc` |
| Pre-run correction note and patch | `S2_RUN_VOID_CORRECTION_01.md` + `calc/s2_noise_origin.py`, committed together at **`64d9cc9`** before the run |
| The patch | Three `nsimplify` removals on exact rationals, plus the output path redirected so the void artifact is preserved. **No change to physics, predicates or ordering.** |
| Result | `S2_NOISE_ORIGIN_RESULT_CORRECTIVE_01.json` (sha256 `7746602389e3…`) |
| Execution | **One** (2.4 s). The **entire instrument ran from the beginning.** No RNG, no simulation. |

## 1. Integrity and coefficient checks: all 18 pass in one artifact

The result records `all_checks_pass = true` and `defects = []`.

| Group | Checks |
|---|---|
| **E-3** | K_b symmetric; off-diagonal ≤ 0 (cooperative); positive definite (exact Cholesky); Gershgorin bound 3/10; f odd |
| **E-1 (symbolic, all β, a, T)** | Δ₀ = Δ₁ = 0; **Δ₂ = −24βT₁a**; **Δ₃ = 12βT₁a(88βa² + 23) = 24βT₁a(44βa² + 5K₁₁)**; Δ₃ has no T₂…T₂₃ dependence |
| **I-2** | β = 0 ⇒ Δ_n ≡ 0 for n ≤ 4 |
| **I-1 (F)** | the Δ₂ and Δ₃ identities hold at every (β, a) |
| **I-3 (G(∞))** | Δ₂ = 0 at every (β, a) |
| **I-4 (GR(∞))** | Δ₂ = −24βT₁a, with T₁ = 1, at every (β, a) |
| **E-2 / I-5** | the O(t) M2 difference polynomial; the O(t²) M2 difference with ξ₁ = 0, equal to K₁₂(4βξ₂³ + K₂₃ξ₃) + const·ξ₂; the ξ-independence of the ± pair's Taylor coefficients through t²; q − q⁰ = p·e + ρ; q⁰ = p² |

**All 1,080 stored instantiated values are exact rationals.** None has a radical form.

In ordinary Taylor normalization (m₁ = Σ c_n tⁿ/n!), the coefficients of t² and t³ are −12βT₁a and
4βT₁a(44βa² + 5K₁₁).

## 2. Report-only fields (no pre-registered sign or value; ruling S2-01 §6 OR-4)

**Exact symbolic Δ₄** (Dynkin normalization):

Δ₄ = −(12aβ/25)·(−13200βT₁² + 110400β²a⁴T₁ + 58880βa²T₁ + 5061T₁ + 200T₂)

**G(∞)** (T₁ = 0):
- Δ₂ = Δ₃ = 0 at all 30 (β > 0, a) members.
- The **first nonzero order is 4 at all 30**, with **Δ₄ = −48aβ/11** exactly.
- This is the downstream-curvature propagation: noise at site 2 reaches the retained mean at O(t⁴).
  It is the effect the S2-0 verifier's counterexample anticipated, carried by the 200T₂ term.

**F vs GR(∞)** (both have T₁ = 1; T₂ = 1 vs 21/22):
- Δ₂ and Δ₃ are identical, so **the leading local coefficients follow T₁**, independent of remote
  orientation.
- They **first differ at order 4**, with Δ₄(F) − Δ₄(GR(∞)) = −48aβ/11 at all 30 members.

There is no downstream-threshold claim.

## 3. Mechanical terminal (charter §5; ruling S2-02 §7)

1. **RUN VOID:** no. There is no implementation defect, and I-1 … I-5 all pass.
2. **COEFFICIENT/CONTROL-REFUTED:** no. The coefficient identities and the finite-moment M2 algebra
   all pass.
3. **FULL-DISCRIMINATOR-CONFIRMED: yes.**
   - I-1 … I-5 pass.
   - The finite-moment M2 no-go is reproduced (derivation §2, with its algebra in E-2).
   - **T-HT closes by HT-B.** This is the moment-free no-go of derivation §3: independently
     verified, accepted by the owner as the theorem basis (ruling S2-02 §3), with its identities
     re-derived in E-2.
   - No arbitrary preparation-independent hidden law ν reproduces O-1 across the frozen preparations,
     for β > 0 and the T₁ > 0 profiles F and GR(∞).
   - No HT-C counterexample exists: HT-B excludes it.

> **S2-1 = FULL-DISCRIMINATOR-CONFIRMED** (proposed, mechanical).
>
> **Within the declared nonlinear C-B class, ongoing stochastic forcing is observationally
> distinguishable in the retained mean-response map from uncertainty confined to the initial
> condition on the same deterministic state space.**

**Mechanism:** noise-generated spread + drift curvature → mean-response structure. The leading term
is −12βT₁a·t², carried by the retained-site noise T₁. Remote noise enters from O(t⁴).

## 4. Scope and fences (ruling S2-02 §8; charter §6)

**This establishes** the failure of the S-1 *initial-uncertainty* equivalence in C-B, against
**arbitrary** preparation-independent hidden initial laws on the same state space.

**It does not establish:**
- ontologically fundamental randomness;
- that an **enlarged deterministic Hamiltonian bath** cannot reproduce the reduced stochastic process
  (deferred, not opened);
- quantum measurement outcomes or Born probabilities;
- that the L0-1c drift is derived (S-5: it is a supplied premise).

**Further limits:**
- **G(∞) (T₁ = 0):** HT-B is not claimed. The separation there first appears at O(t⁴) and is reported
  only.
- The result is local (Taylor grade) near t = 0. There is no finite-time magnitude claim (OR-3).

## 5. HARD STOP

- The corrective result and this verdict are committed.
- The RUN VOID record (`S2_NOISE_ORIGIN_VERDICT_01.md`, `S2_NOISE_ORIGIN_RESULT.json`) is preserved.
- CURRENT_STATE is updated. **Awaiting owner adjudication.**
- **Not opened automatically:**
  - the Hamiltonian-bath follow-up;
  - S-3, the reversal diagnostic, S-6;
  - S5-WB or S5-OD;
  - gravity, Π₀ or cosmology.
