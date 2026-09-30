# S3-0 — THE CROSSED CELL 01 (formulation/audit gate only)

> **CLOSED / ACCEPTED (owner ruling S3-01, Issue #2 comment `5909891161`; `S3_OWNER_RULING_01.md`):**
> **S3-0 = FORMULABLE-ONLY-WITH-CHANGE**, under both declared readings.
> - **The changed invariants are accepted:** I-1, I-4, and I-5/X-c.
> - **D-1 … D-6 are resolved.** In particular, absence is not identity, and identity-forced counts only
>   at the invariants.
> - **READING-DEPENDENT is not assigned.**
> - **Status of the two readings:** R₂ (P^corr_CM ≡ P^resp_CM) is trivial and carries no reversal
>   evidence. R₁ is open only in an undeclared hybrid.
> - **The response/correlation inversion remains confounded.** No hybrid and no run.
> - **Next:** REV-0 (`L0_STRUCTURAL_DIAGNOSTIC_REVERSAL_EVALUATION_01.md`).
>
> The text below is preserved as filed.

**STATUS: PRE-REGISTERED.** §§0–3 are frozen at the commit that introduces this file, **before any
candidate record is inspected**.
- **Read before freezing, to define the question only:**
  - `L0_1_FLOOR_SUCCESSOR_LIST.md` (the S-3 row);
  - `L0_STRUCTURAL_DIAGNOSTIC_REVERSAL_01.md` (the defining source, §2.3).
- **Appended later:** the audit (§4) and the assignment (§5), in separate commits.
- **Authority:** `S2_HB_OWNER_RULING_02.md` §12 (Issue #2 comment `5909652190`).
- **What this gate is:** audit only. No physics run, no v4 exception, no RNG, no numerical evaluation
  of members, and no reversal-diagnostic terminal. **No hybrid may be invented.**
- **Date:** 2026-09-30 · **Branch:** `master-w25bu9`.

## §0 Question

> **Does generator-side cycle affinity break correlation complete monotonicity when the noise is held
> FDT-like?** (S-3; reversal diagnostic §2.3)

**Why it is needed** (reversal diagnostic §2 caution 3). The recorded contrast is confounded on three
axes at once:

| Axis | One side | Other side |
|---|---|---|
| Object | response (P^resp) | correlation (P^corr) |
| Route | generator K (cycle affinity → loss of response CM) | noise Q (broken detailed balance in the noise does not break correlation CM near the FDT point) |
| Substrate | ring | chain |

- **The crossed cell:** generator affinity's effect on *correlation* CM, with the noise held
  FDT-like.
- **The other crossed cell** (noise → response) is empty by F-5.

**Owner constraint (ruling §12).** The crossed cell must be formulable from **declared records only**,
without changing any of five invariants:

| # | Invariant |
|---|---|
| **I-1** | substrate class |
| **I-2** | retained observable |
| **I-3** | stochastic convention |
| **I-4** | temperature/noise rule |
| **I-5** | response/correlation normalization |

If it is not formulable, **stop; do not invent a hybrid.**

## §1 Definitions (frozen)

### 1.1 Parent records

- **Generator side (G):** the record(s) whose accepted ruling certifies "cycle affinity → loss of
  response complete monotonicity" (reversal diagnostic §4). The audit locates them.
- **Noise side (N):** the record(s) whose accepted ruling certifies "noise-side broken detailed
  balance does not break correlation CM near the FDT point" (L0-1e / D-DET). The audit locates them.

### 1.2 The crossed cell 𝒳

𝒳 is the comparison in which:
- **(X-a)** generator cycle affinity is **varied**, as a declared generator parameter, across at least
  one zero-affinity member and one nonzero-affinity member;
- **(X-b)** the noise is held **FDT-like**, meaning by a **declared** noise/temperature rule that is
  defined for every member of (X-a);
- **(X-c)** the tested predicate is **P^corr_CM**, the correlation complete-monotonicity predicate as
  declared on the N side, on the declared retained observable.

### 1.3 Formulable at the invariants

𝒳 is **formulable at the invariants** iff the declared record supplies all of (X-a)–(X-c), **and**
each of I-1 … I-5 is either:
- **(i)** supplied by a single declared **home record** that already carries both the affinity
  parameter and the FDT-like noise rule; or
- **(ii)** **identical** on the G and N sides, so that carrying one side's generator variation into
  the other side's setting changes nothing.

**Anything else is a change of invariant.** Examples:
- the G and N substrate classes differ (ring vs chain);
- the N-side noise rule is undefined for affinity-carrying generators;
- the normalizations differ.

The audit names each changed invariant.

### 1.4 "FDT-like"

A noise rule counts as FDT-like only if it is **declared in the record as an FDT/Einstein/KMS-matched
rule**, with a citation.

- If several declared rules qualify, **each is audited separately** as a reading R₁, R₂, ….
- **Choosing a rule because it makes 𝒳 formulable, or because of the answer it gives, is
  forbidden.**
- A rule declared only for symmetric/detailed-balanced generators is **not** thereby defined for
  affinity-carrying ones. Extending it counts as a change of I-4 unless the record itself extends it.

### 1.5 Identity-forced

An answer to 𝒳 is **identity-forced** iff, at the invariants, P^corr_CM's truth value on the
affinity members follows from one of:
- **(i)** an identity **already on the record**: F-5, FDT, a declared relation between correlation
  and response, or another recorded identity; or
- **(ii)** a one-line algebraic consequence of **declared definitions** alone, such as a declared
  stationary covariance that makes the correlation a fixed multiple of the response.

The independent verifier must confirm it. By reversal diagnostic §2 caution 2, an identity-forced cell
carries **no independent evidence** for or against a reversal.

### 1.6 Answer tags (reported only when the record, or an identity per 1.5, fixes them)

| Tag | Meaning |
|---|---|
| **CM-PRESERVED** | P^corr_CM holds on every affinity member |
| **CM-LOST** | P^corr_CM fails on some nonzero-affinity member |
| **MEMBER-DEPENDENT** | CM holds on some affinity members and fails on others |
| **OPEN** | not fixed without execution |

## §2 Per-record audit template (frozen)

For each record inspected, report with file:line citations (an uncited answer counts as undefined):
- **role:** G, N, candidate home record, FDT-rule source, or not relevant;
- **affinity:** is cycle affinity a declared, variable generator parameter (X-a)? On which substrate
  class?
- **FDT-like rule:** is one declared (X-b)? What is its exact form, and for which generators is it
  defined?
- **P^corr_CM:** its declared definition (X-c): which observable, which normalization, which lag
  domain;
- **stochastic convention:** Itô, Stratonovich or additive;
- **invariants I-1 … I-5:** for each, the value in this record;
- **recorded identities:** any identity relating correlation and response on this record's class.

## §3 Frozen outcomes and mechanical rule

### 3.1 Outcomes

| # | Outcome | Predicate |
|---|---|---|
| O-1 | **CELL-ALREADY-CERTIFIED** | An accepted owner ruling already decides P^corr_CM on 𝒳 at the invariants. The answer tag is reported. |
| O-2 | **CELL-IDENTITY-FORCED** | 𝒳 is formulable at the invariants (1.3) under some declared FDT-like reading, and its answer is identity-forced (1.5). Tag reported; the cell carries no independent reversal evidence. |
| O-3 | **FORMULABLE-CROSSED-CELL** | 𝒳 is formulable at the invariants under some declared FDT-like reading, and its answer is not identity-forced. The declared structure fixes a clean executable test. **Nothing is run; a charter needs a separate ruling.** |
| O-4 | **FORMULABLE-ONLY-WITH-CHANGE** | Every construction of 𝒳 from declared records changes at least one of I-1 … I-5. The audit names the invariants. **Stop; no hybrid.** |
| O-5 | **UNFORMULABLE** | A load-bearing object has no declared meaning, so 𝒳 cannot even be posed. Examples: no declared affinity parameter; no declared FDT-like rule; no declared P^corr_CM. |

### 3.2 Mechanical rule

1. The first true predicate in the order O-1 … O-5 is the primary terminal.
2. Every other true predicate is reported as a sub-label.
3. With several FDT-like readings (1.4), each is evaluated separately. **The primary terminal is the
   first predicate true under any reading.** The per-reading results are all reported, and so is the
   sub-label **READING-DEPENDENT** if the readings disagree.
4. **HARD STOP** for owner adjudication.

### 3.3 Audit method (frozen)

- **Read-only.** Abstract symbolic reasoning only; no code on members, no RNG.
- **Two parallel auditors:**
  - **A: generator side** (the G records; affinity; substrate; P^resp_CM);
  - **B: noise side** (the N records; the FDT-like rules; the P^corr_CM definition; the convention;
    the normalization), plus a discovery sweep for any record carrying both affinity and a declared
    noise rule.
- **One independent adversarial verifier** for the load-bearing items:
  - every formulability claim;
  - every claimed change of invariant;
  - every identity-forced claim;
  - the primary terminal.

### 3.4 Fences

**Not established by this gate, whatever its result:**
- a reversal or self-duality in the diagnostic graph 𝒢 (the diagnostic is evaluated only at program
  synthesis);
- any new edge in 𝒢;
- primitive noise;
- gravity, Π₀ or cosmology.

**Not authorized by O-2 or O-3:** a run.

### 3.5 Prior expectations (disclosed before inspection; not evidence)

**Expectation 1:** the G side lives on a **ring** (a cycle is needed for affinity) and the N side on a
**chain**.
- If so, 𝒳 needs I-1 to change, unless a declared record carries both.
- That gives **FORMULABLE-ONLY-WITH-CHANGE**.

**Expectation 2:** suppose some record declares both an affinity-carrying generator K and a local
Einstein-type noise Q = T(K + Kᵀ).
- The stationary covariance is then Σ = T·I.
- The retained correlation is then T times the retained response.
- CM would be lost exactly where response CM is lost.
- That gives **CELL-IDENTITY-FORCED (CM-LOST)**.

These are guesses from memory. The audit must test them and report any record that contradicts them.

## §4 Audit

**How the audit was run.** §§0–3 were frozen at `febc3f6` before any candidate was inspected. Two
read-only auditors ran (A: the generator side; B: the noise side plus the discovery sweep), followed by
one independent adversarial verifier on V1–V6. **No claim was refuted.** Two reasoning corrections were
applied (§4.4). No code was run on members, and no RNG was used.

### 4.1 G side: L0-1d (D-HERM-a) is the only certified generator record

**Substrate.** A 23-site ring, K_s = K_b + (e₁ − e₂₃)(e₁ − e₂₃)ᵀ, with diagonal 3.3 at site 1 and 2.3
elsewhere (`L0_1D_CHARTER_01.md:80-82`).

**Affinity (X-a) is a declared, variable parameter.**
- An antisymmetric deformation γa_i gives 𝒜 = Σ ln[(1 + γa_i)/(1 − γa_i)] (`:69-73`).
- **Zero-affinity members:** C(0), B(·), T(·).
- **Nonzero-affinity members:** C(0.1 … 0.9), with 𝒜 = 4.6 … 67.7 (`:83-99`;
  `L0_1D_VERDICT_01.md:43-44`).
- K_s is held fixed, so every member is accretive with μ > 0.3 (`L0_1D_CHARTER_01.md:174-176`).

**The certified edge.** "Nonzero cycle affinity breaks complete monotonicity at all four circulating
members" (L-2, `L0_1D_OWNER_RULING_01.md:15,18,58`; diagnostic §4).

**What the record contains.**
- Response: k(τ) = e₁ᵀe^{−Kτ}e₁, with k(0) = 1.
- **No noise, no FDT rule, no covariance, and no correlation object.** A grep of `L0_1D_*.md` finds
  none.

**Excluded.** L0-1h, the one-way ring, is not a certified G edge. Its affinity "stays completely
outside O-2" (`L0_1H_OWNER_RULING_02.md:47-51`), and it remains the open successor item S-8.

### 4.2 N side: L0-1e (D-DET) on the symmetric chain K_b

**Setting.**
- K = K_b, symmetric (`L0_1E_THEOREM_01.md:17-27`).
- Noise: Q = 2·diag(T_i), "never set from rung2's KMS lock".
- Σ is defined by **KΣ + ΣK = Q**.

**The FDT point.** T-4 gives Q = 2I, Σ = K⁻¹ and **−C′ = k_resp** (`:68-79`). The temperature form F-6
holds only "if … K is symmetric" (`L0_1_FLOOR_DESIGN_01.md:117-118`).

**The P^corr_CM object.**
- C(τ) = e₁ᵀe^{−Kτ}Σe₁, with c = C/C(0) and τ ≥ 0 (`L0_1E_CHARTER_01.md:59-75`).
- Noise is additive, so the result is convention-free.

**Affinity is impossible on the chain.** By F-1, every sign-consistent tree coupling is diagonally
similar to a symmetric one (`L0_1_FLOOR_DESIGN_01.md:47-59`).

**The crossed cell is left open on the record.** L0-1e says separating the axes "needs successor item
S-3" (`L0_1E_THEOREM_01.md:198-199`).

### 4.3 Home record and FDT-like readings

**No home record exists (1.3(i)).** No declared record pairs a variable affinity generator with a
declared FDT-like rule. The verifier ran its own co-occurrence sweep over every `*.md`.

| Near-miss | Why it fails |
|---|---|
| D-ORD | Lists the ring members only in the deterministic class 𝒞₁; its stochastic class 𝒞₃ is L0-1e only (`L0_1F_DORD_THEOREM_01.md:46,56-59`) |
| Lift selection | Declares an FDT-like rule, but has no affinity parameter |
| CA-1 | A symmetric Laplacian ring with no affinity |
| S2 candidates C-A … C-D | All on K_b |
| rung2 KMS lock | Not defined for L0 matrices; L0-1e excludes it |

**Two declared FDT-like readings (1.4):**

- **R₁ (L0-1e).** Q = 2T·I at the FDT point.
  - Declared FDT, but **only for symmetric K**. The record does not extend it.
  - Satisfies the record's FDT relation −C′ = T·k_resp.
- **R₂ (lift selection, real Λ-B).** Q = K + Kᵀ.
  - "FDT-held, L0-1e-type declared extension, which exists iff K is accretive"
    (`L0_LIFT_SELECTION_VERIFICATION_01.md:97-98`); "FDT pairing" (`S5_GENERATOR_ORIGIN_01.md:306`).
  - **The record itself extends it to non-symmetric K.** The "iff accretive" condition, the
    non-symmetric 2-mode check (`:86`), and the general-K covariance with Σ = I (LS-2,
    `L0_LIFT_SELECTION_CORRECTIONS_01.md:12`) all say so. It is instantiated only on K_b.
  - **Caveats:**
    - The governing correction LS-5 and `L0_LIFT_SELECTION_OWNER_RULING_02.md:37` repeat
      Q = K + Kᵀ **without** the "FDT-held" label.
    - R₂ gives **C = T·k**, not the record's FDT relation −C′ = T·k_resp. On the ring,
      −C′(0) = T·K₁₁ = 3.3T ≠ T.
    - It is FDT-like by label (an Einstein relation with K as the mobility), not by the N-side
      identity.

### 4.4 Per-reading construction of 𝒳 (with the verifier's corrections)

Both readings need the **ring** (I-1 changes) and a **different noise rule from N's**:
- R₁ would have to be extended to non-symmetric K, which the record does not do.
- R₂ replaces 2I by 2K_s, and it is not diagonal even on the chain.

So I-4 changes under both readings.

**Correction 1 (Lyapunov form).**
- N's literal definition, KΣ + ΣK = Q, is valid only for symmetric K.
- For non-symmetric K it must be replaced by the general form KΣ + ΣKᵀ = Q
  (`L0_1_FLOOR_DESIGN_01.md:114-115`; `L0_1F_DORD_THEOREM_01.md:85-86`).
- This is a definitional change to X-c/I-5 under both readings.

**Correction 2 (identity-forced).** 1.5 defines "identity-forced" only at the invariants. The R₂
result below is therefore a **note carrying no evidence**, not an O-2 tag.

**Answers of the off-invariant constructions (reported only; no predicate relies on them):**
- **R₁ on the ring: OPEN.** With non-symmetric K, K(TK⁻¹) + (TK⁻¹)Kᵀ = T(I + K⁻¹Kᵀ) ≠ 2TI. So
  Σ ≠ TK⁻¹, and no recorded identity fixes CM.
- **R₂ on the ring: CM-LOST, by identity.**
  - −K is Hurwitz, since Re λ ≥ λ_min(K_s) > 0.3.
  - Q = 2T·K_s ≻ 0 is the same for every member.
  - So Σ = T·I is unique, C = T·k, and c = k.
  - Hence CM-LOST at C(0.1) … C(0.9) and CM at the zero-affinity members. **This is a copy of L-2.**
  - By §2 caution 2 it carries **no independent reversal evidence.**

### 4.5 The five invariants

| Invariant | G (L0-1d) | N (L0-1e) | 𝒳 under R₁ / R₂ |
|---|---|---|---|
| I-1 substrate | 23-site ring, K_s held | symmetric chain K_b | **changed** under both (affinity impossible on the chain) |
| I-2 observable | x₁ / e₁ | x₁ / e₁ | unchanged (the 3.3 vs 2.3 diagonal is an I-1 effect) |
| I-3 convention | absent (deterministic) | additive | literal change only; no substantive effect (additive noise is convention-free) |
| I-4 noise rule | absent | Q = 2·diag(T_i), FDT Q = 2I, symmetric K only | **changed** under both (R₁ extended; R₂ replaced) |
| I-5 normalization / X-c | k unnormalized, k(0) = 1 | c = C/C(0); KΣ + ΣK = Q | the normalization is unchanged; **the Lyapunov form changes** under both |

### 4.6 Prior expectations (§3.5)

- **Expectation 1 is confirmed:** the generator side is on a ring and the noise side on a chain.
- **Expectation 2's premise is not met.** The declared form is Q = K + Kᵀ, not T(K + Kᵀ), and it is
  never paired with an affinity generator. Its conditional algebra is correct, but only under the
  general Lyapunov form.

### 4.7 Wording defects reported for adjudication (not repaired)

| # | Defect | Effect here |
|---|---|---|
| D-1 | 1.3(ii) does not say how to treat an invariant that is absent on one side. | Affects I-3 and I-4; the terminal does not change. |
| D-2 | 1.3 does not cover an FDT rule sourced from a third record. | Applies to R₂, from lift selection. |
| D-3 | 1.4 does not say whether a formula stated for "any accretive K", but instantiated only on symmetric K, counts as the record extending the rule. | Read here as extended. |
| D-4 | 1.5 leaves "identity-forced" undefined for off-invariant constructions. | Handled as a note carrying no evidence. |
| D-5 | 3.2(3) does not say whether READING-DEPENDENT refers to the predicates or to the off-invariant tags. | The predicates agree (O-4 under both); only the off-invariant tags differ (OPEN vs CM-LOST). |
| D-6 | X-c's phrase "as declared on the N side" imports the symmetric-only KΣ + ΣK = Q. | Recorded as a change of the Lyapunov form. |

## §5 Mechanical assignment

| Predicate | Value | Ground |
|---|---|---|
| O-1 CELL-ALREADY-CERTIFIED | **false** | No ruling decides P^corr_CM under generator affinity; L0-1e defers it to S-3. |
| O-2 CELL-IDENTITY-FORCED | **false** | 𝒳 is not formulable at the invariants under either reading. |
| O-3 FORMULABLE-CROSSED-CELL | **false** | Same reason. |
| **O-4 FORMULABLE-ONLY-WITH-CHANGE** | **true, under both readings** | Changed invariants: **I-1** (ring vs chain; affinity impossible on the chain), **I-4** (R₁ must be extended to non-symmetric K; R₂ replaces N's rule), and **the I-5/X-c Lyapunov form**. I-3 is a literal change only. |
| O-5 UNFORMULABLE | **false** | Every load-bearing object is declared: affinity, two FDT-like rules, and P^corr_CM. |

> **S3-0 = FORMULABLE-ONLY-WITH-CHANGE** (proposed, mechanical).
> - It is **not READING-DEPENDENT** at the predicate level.
> - **Changed invariants:** I-1, I-4, and the I-5/X-c Lyapunov form. I-3 is a literal change only.
> - **Stop. No hybrid is built.**

**Report-only (outside the invariants; no evidence):**
- **R₂ on the ring would be identity-forced to CM-LOST.** Σ = T·I gives C = T·k, which reproduces
  L-2. It carries no independent reversal evidence.
- **R₁ on the ring would be OPEN.**

**Reading (fenced).**
- As the record stands, the crossed cell cannot be posed without changing the substrate and the
  noise rule.
- Of the two declared FDT-like rules that could be carried to the ring:
  - **R₂ would make the cell trivial:** correlation ∝ response, a copy of the generator result.
  - **R₁ would leave a genuine open question**, but only after both changes.
- Either way, the separation of "response ↔ correlation" from "generator ↔ noise" that reversal
  diagnostic §2 caution 3 asks for **is not available from declared structure alone.**
- The diagnostic graph 𝒢 is unchanged: no edge is added and no reversal is assessed.

**HARD STOP.** This is proposed for owner adjudication. There is no run and no hybrid, and nothing is
opened: no S-6, no S5-WB or S5-OD, and no gravity, Π₀ or cosmology.
