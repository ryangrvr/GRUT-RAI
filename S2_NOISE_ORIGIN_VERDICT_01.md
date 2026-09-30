# S2-1 — NOISE-ORIGIN VERDICT 01

**Mechanical status: RUN VOID** (charter §5, item 1).
- An **implementation defect** prevented integrity item I-5 (the E-2 symbolic re-derivations) from
  executing.
- **No physics terminal is assigned.** The artifact is preserved. No silent repair and no re-run.
- **Returned for owner ruling. HARD STOP.**

## Provenance

| Item | Value |
|---|---|
| Frozen charter | `S2_NOISE_ORIGIN_CHARTER_01.md` at `227dd09` |
| Analytic derivation | `S2_NOISE_ORIGIN_DERIVATION_01.md`: draft at `cd0485d`; **independently adversarially verified**, with VG-1 … VG-3 applied, at `32645cc`, **before** the script |
| Script | `calc/s2_noise_origin.py`, committed at `e92cf29` before its single run |
| Result | `S2_NOISE_ORIGIN_RESULT.json` (sha256 `e573f972…`), preserved unmodified; the run log is in the session scratchpad |
| Executions | **One** (3.3 s). No re-run. |

## 1. The defect

**What went wrong.**
- The instantiation loop passed already-exact sympy `Rational` values through `sp.nsimplify`.
- For **8 of the 540** stored instantiated values, `nsimplify` rewrote an exact rational (one with a
  large denominator) as a **non-exact radical expression**, for example
  `-2**(269/350)*3**(153/350)*5**(243/700)*7**(61/140)/60`.
- All 8 are **report-only Δ₄ entries** (and their t⁴ coefficients): 4 in F and 4 in GR(∞).
- The report-only block then called `sp.Rational(...)` on one such string and raised `TypeError`.
- The exception was caught and recorded in `defects`. `all_checks_pass = false`.

**Consequence.**
- **E-2 did not execute.** E-2 holds the symbolic finite-moment M2 coefficient algebra and the HT-B
  identities (ξ-independence of the ± pair's Taylor coefficients, and q − q⁰ = p·e + ρ).
- These are part of **I-5**. Under the frozen rule, I-5 not passing for an implementation reason
  gives **RUN VOID.**

**Remedy (not applied; owner ruling needed).** It is a one-line fix: drop `nsimplify`, since the
values are already exact `Rational`s.

## 2. What the preserved artifact does establish

This is read from the preserved artifact only; nothing was re-run.

| Check | Result |
|---|---|
| **E-3** | K_b is symmetric and positive definite (exact Cholesky); its off-diagonal is ≤ 0 (cooperative); the Gershgorin bound is 3/10; f is odd. **Pass.** |
| **E-1 (symbolic, all β, a, T)** | Δ₀ = Δ₁ = 0. **Δ₂ = −24βT₁a. Δ₃ = 12βT₁a(88βa² + 23) = 24βT₁a(44βa² + 5K₁₁).** Δ₃ has no T₂…T₂₃ dependence. **Pass.** |
| **I-2** | β = 0 gives Δ_n ≡ 0 for n ≤ 4. **Pass.** |
| **I-1** (F), **I-3** (G(∞): Δ₂ = 0), **I-4** (GR(∞): Δ₂ = −24βa) | Instantiated at every (β, a). **Pass.** None of the 8 corrupted entries is a Δ₂ or Δ₃ value. |
| **Symbolic Δ₄** (printed and stored exactly in `symbolic_Delta`) | Δ₄ = −(12aβ/25)·(−13200βT₁² + 110400β²a⁴T₁ + 58880βa²T₁ + 5061T₁ + 200T₂) |
| E-2 | **Not executed** (the defect). |
| The reported block (G(∞) first nonzero order; F vs GR(∞)) | **Not written** (the defect). |

**Information readable from the preserved symbolic Δ₄.** This is not an adjudicated product of the
run.
- **G(∞)** (T₁ = 0, T₂ = 1/22): Δ₄ = −48aβ/11. The first nonzero order is **4**. This is the
  downstream-curvature propagation (T₂ at site 2 → site 1) that the S2-0 verifier anticipated. Per
  the charter, neither its sign nor its value was pre-registered.
- **F − GR(∞)** (T₂ = 1 vs 21/22): the difference is 0 at Δ₂ and Δ₃, and Δ₄ differs by −48aβ/11.
  **The remote orientation first appears at order 4**, while the leading coefficient follows T₁.

## 3. Status of the scientific question (not a terminal)

**The analytic derivation stands as written and independently verified:**
- the coefficient identities (§1);
- the finite-moment M2 no-go (§2);
- **Theorem HT-B**, a moment-free no-go (§3). It closes T-HT for every preparation-independent
  hidden law with a defined O-1 mean, on the profiles F and GR(∞).

**The adversarial verifier independently checked with sympy on symbolic chains:**
- q − q⁰ = p·e + ρ;
- the ξ-independence of the ± pair's t⁰–t² coefficients;
- the M2 coefficient algebra.

These are exactly the content of the unexecuted E-2.

**Nonetheless, under the frozen rule the run is void, and FULL-DISCRIMINATOR-CONFIRMED is not
assigned.**

## 4. Options for the owner (none taken)

1. **Authorize a second execution** with the one-line fix (no `nsimplify`), under the same frozen
   charter.
2. **Rule** that I-5's E-2 content is discharged by the independent verifier's symbolic checks
   together with the verified derivation, and **adjudicate from the preserved artifact**. Every
   frozen coefficient identity and control passed there, and the defect touched only report-only Δ₄
   values and the unexecuted E-2.
3. **Another ruling.**

## 5. HARD STOP

- The artifact, the log reference and this verdict are committed. CURRENT_STATE is updated.
- No re-run, no repair, no terminal.
- No S-3, S-6, or Hamiltonian-bath comparison.
