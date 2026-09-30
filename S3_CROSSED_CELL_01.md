# S3-0 — THE CROSSED CELL 01 (formulation/audit gate only)

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

*(appended after this pre-registration is committed)*

## §5 Mechanical assignment

*(appended after §4)*
