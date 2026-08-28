# A3-1 BUILDER PROMPT — FINITE eps^0 MASTER ENGINE ONLY

STATUS: OWNER-AUTHORIZED 2026-08-28. Scope: A3-1 ONLY. A3-2 (finite loop
assembly) begins only after owner/reviewer acceptance of the A3-1 result.
Nothing beyond A3-1 until the master checks are green.

This file freezes, verbatim, the owner's A3-1 builder prompt. It operates
UNDER the ASSEMBLY-3 builder contract
(PHYSICS_LEDGER/WALL_D2_ASSEMBLY3_BRIEF.md, sha256
fff07e5172d1ee0ff9ba7c379cd5716b8c86c43688b89d74a22abbd898314bae) and the
entry object (PHYSICS_LEDGER/WALL_D2_ASSEMBLY3_ENTRY_OBJECT.json, sha256
419c455bccdd90dcbef708698e5339b7a2d32f0c8b07c49af9de6ab099316ccb). Where
this prompt is tighter than the brief (scope fence, controls, performance),
the tighter rule governs; nothing here relaxes the brief.

ORDER OF OPERATIONS (owner's authorization): derive -> independent
scalar-bubble check -> branch/threshold verification -> ONLY THEN assemble
the finite loop (later stage, separate acceptance).

Sections:
  1. THE A3-1 BUILDER PROMPT (verbatim)
  2. LEDGER TERMINOLOGY RULE (owner, binding)
  3. HANDSHAKE

## 1. THE A3-1 BUILDER PROMPT (verbatim)

```text
TASK: ASSEMBLY-3 / A3-1 — FINITE ε^0 MASTER ENGINE ONLY

STANDING STATE:
Commit `c6cf253`.

Read FIRST:
1. `PHYSICS_LEDGER/WALL_D2_ASSEMBLY3_BRIEF.md`
2. `PHYSICS_LEDGER/WALL_D2_ASSEMBLY3_ENTRY_OBJECT.json`
3. the frozen A3/V4 declarations and registry referenced by those files.

Treat them as immutable law.

CURRENT STATUS:
- Phase 10 loop target/cache: FROZEN, SHA-verified.
- Corrected Phase-11 action-functional basis: FROZEN.
- Phase 12 UV pole/MS sector: CLOSED.
- F1 locality amendment V4: FROZEN.
- finite ε^0 response: NOT COMPUTED.
- J(ω): PROHIBITED.
- PV: NOT YET RUN.
- Q1/Q3/Q4/Q5: NOT YET RUN.
- W-0 throughout.

THIS SESSION/STAGE DOES ONE THING:

    DERIVE AND VALIDATE THE FINITE ε^0 LOOP MASTERS.

Do NOT assemble the full finite graviton self-energy yet.

Do NOT touch the tensor loop assembly.
Do NOT modify the Phase-10 cache.
Do NOT modify the Phase-11 basis.
Do NOT run the span test.
Do NOT run Q1-Q5.
Do NOT read J(ω).
Do NOT run PV.

============================================================
A3-1A — FILE CLAIM + INTEGRITY
============================================================

Claim all new/modified paths before writing.

Verify:
- contract hash;
- entry-object hash;
- A3 registry;
- Phase-10 cache;
- Phase-11 AF basis cache;
- Phase-12 result.

No drift.

============================================================
A3-1B — DEFINE THE FINITE MASTER OBJECTS
============================================================

Identify EXACTLY which scalar/tensor master integrals are needed by the
already validated pole machinery.

Do not invent additional masters.

For each master, expose:

    integral definition
    denominator powers
    numerator power
    dimensional regulator d=4-eps
    finite ε^0 coefficient
    dependence on μ
    dependence on Δ = m² - x(1-x)K²

Preserve the same normalization used by the validated pole engine.

============================================================
A3-1C — DERIVE, DON'T IMPORT
============================================================

Derive the ε^0 terms from the dimensional-regularization expression.

Do not insert a remembered Passarino-Veltman result as the answer.

Emit the derivation chain:

    d-dimensional master
       ->
    epsilon expansion
       ->
    1/eps pole
       +
    finite epsilon^0 term
       +
    O(eps).

The already validated pole coefficient is a regression check,
not the source of the finite answer.

============================================================
A3-1D — PRIMARY FINITE SCALAR BUBBLE
============================================================

The first anchor is the ordinary equal-mass scalar bubble.

Derive its finite part in the exact convention used by the project.

Then evaluate it independently by TWO routes:

ROUTE A:
    analytic Feynman-parameter evaluation.

ROUTE B:
    an independently implemented numerical/high-precision evaluation
    of the finite integral.

Require agreement over several spacelike K² values away from threshold.

Do not use the existing finite-master implementation in Route B.

============================================================
A3-1E — BRANCH / THRESHOLD STRUCTURE
============================================================

From the derived expression itself, determine:

- where the denominator Δ(x) can vanish;
- where the branch point/threshold occurs;
- the analytic continuation convention;
- which side carries the imaginary part.

Do not assume the answer is a logarithm merely because that is common
for bubble integrals.

The analytic structure must come from the actual derived expression.

Use a spacelike test region first, then one controlled timelike point
where analytic continuation is unambiguous.

Report:
    real part
    imaginary part
    threshold location
    branch prescription.

============================================================
A3-1F — HIGHER MASTERS
============================================================

Extend the validated scalar finite result to every higher master actually
needed by the Phase-10 numerator algebra.

Where mathematically legitimate, use independently verified relations such as
mass derivatives/Feynman-parameter differentiation, but KEEP the derivation
visible.

For every master:

    pole coefficient = existing validated result
    finite coefficient = NEW RESULT

Run at least one independent numerical check per master family.

============================================================
A3-1G — EXACT/NUMERIC CROSS-CHECK
============================================================

For several rational masses and external momenta:

    analytic finite master
        vs
    independent numerical quadrature

Use sufficiently high precision to distinguish implementation error from
roundoff.

No arbitrary fitting of normalization constants.

============================================================
A3-1H — NONLOCALITY FENCE
============================================================

The finite master may contain logarithms, threshold functions, square roots,
or other non-polynomial dependence.

DO NOT classify these as "nonlocal response" yet at the full tensor level.

At this stage only establish the analytic structure of the master itself.

The later finite-kernel assembly will determine how these pieces combine.

============================================================
A3-1I — NEGATIVE CONTROLS
============================================================

At minimum include:

1. wrong logarithm branch;
2. wrong sign of the imaginary continuation;
3. wrong μ normalization;
4. wrong ε expansion coefficient.

Each must fail a machine check.

============================================================
A3-1J — PERFORMANCE RULE
============================================================

Reduce representation BEFORE symbolic integration.

Prefer:
- rational sample points for numerical checks;
- one symbolic variable Δ where possible;
- no maximal symbolic tensor expressions;
- cached scalar masters.

Print elapsed time per master.

If one symbolic operation exceeds ~10 minutes without producing a new
reusable result, STOP that operation and re-represent it.

Do not brute-force.

============================================================
A3-1K — RESULT FORMAT
============================================================

For every master report:

    master name
    integral definition
    pole coefficient
    finite ε^0 coefficient
    μ dependence
    branch/threshold structure
    independent-check result
    numerical agreement
    pass/fail.

Produce:

    WALL_A3_1_FINITE_MASTERS_RESULT.json
    WALL_A3_1_FINITE_MASTERS_VERDICT.md

The result must contain explicit pass fields for every gate.

============================================================
HARD STOP
============================================================

After A3-1:

STOP.

Do NOT:
- assemble Σ_R^finite;
- construct Π_nonlocal;
- perform TT projection;
- run Q1;
- run Q3;
- run Q4;
- run Q5;
- compare J(ω);
- run PV.

The only question answered by this stage is:

    "Are the finite ε^0 master integrals correctly derived and
     independently validated?"

A3-2 begins only after owner/reviewer acceptance.

W-0.
No register edits.
No frozen-file edits.
```

## 2. LEDGER TERMINOLOGY RULE (owner, binding, 2026-08-28)

Verbatim: "Phase 12's result is a UV renormalization result, not yet a
computed nonlocal response."

What Phase 12 isolated is the ZERO NONLOCAL POLE RESIDUE (with the 208
divergent terms established local and removable by the frozen MS
structure). The finite nonlocal kernel is still ahead. No summary, ledger
entry, or result file may state or imply that "the nonlocal response has
been isolated" in the sense of having been evaluated. This rule binds every
future stage, beginning with A3-1's nonlocality fence (A3-1H).

## 3. HANDSHAKE

  a. Verify this file's sha256 against the value recorded in
     AGENT_COORDINATION.md.
  b. Verify standing state: commit c6cf253 or later; frozen-file integrity
     intact (v1 87e2d24d..., registry faa977d4..., v2 6f2a762f...,
     v3 b0b9983b..., Phase-12 instrument a9850cd5...).
  c. Read the ASSEMBLY-3 brief (fff07e51...) and the entry object
     (419c455b...) in full BEFORE computing. Immutable law.
  d. A3-1A file claim + integrity gate BEFORE any write.
  e. Hard stop after A3-1K. A3-2 only after owner/reviewer acceptance of
     the A3-1 result. J(ω) PROHIBITED; PV NOT RUN; Q1-Q5 NOT RUN.

— end of A3-1 builder prompt —
