# A3-1 EXECUTION PROMPT — Z.AI BUILDER, ASSEMBLY-3 / A3-1 ONLY

STATUS: OWNER-ISSUED 2026-08-28, for execution by the builder session. This
is the operational build order; it hard-scopes the build to A3-1 and adds
gates beyond the parent contract.

DOCUMENT HIERARCHY (tighter rule governs at every level; a genuine conflict
between levels is a STOP-and-report fork, not a builder liberty):
  1. ASSEMBLY-3 brief  — PHYSICS_LEDGER/WALL_D2_ASSEMBLY3_BRIEF.md,
     sha256 fff07e5172d1ee0ff9ba7c379cd5716b8c86c43688b89d74a22abbd898314bae
  2. A3-1 builder prompt — PHYSICS_LEDGER/WALL_A3_1_BUILDER_PROMPT.md,
     sha256 99a369b3b9d83d79fde9b36a36e1c991348d37730ba79dd93af882e25817c218
  3. THIS execution prompt — the build-session order of operations.

REVIEWER EMPHASES CARRIED INTO EXECUTION (owner, 2026-08-28):
  E1. The independent numerical route (Route B) must GENUINELY bypass the
      new analytic master implementation. If both routes share the same
      formula generator, a perfect agreement tells us much less than it
      appears. This is THE load-bearing check (see A3-1G).
  E2. After A3-1 is green there is an EXPLICIT HARD STOP before A3-2, so
      the owner/reviewer can inspect the finite-master formulas and branch
      structure BEFORE they propagate into the full tensor response.

RIGID PRINCIPLE (owner, verbatim): "the independent numerical integral is
the referee of the analytic finite master."

## THE EXECUTION PROMPT (verbatim)

```text
Z.AI BUILDER — EXECUTE ASSEMBLY-3 / A3-1 ONLY

CURRENT HEAD:
    1096c39

THIS IS A HARD-SCOPED BUILD.
DO NOT ADVANCE TO A3-2.

============================================================
AUTHORITATIVE INPUTS
============================================================

Before writing anything:

1. Read:
   PHYSICS_LEDGER/WALL_A3_1_BUILDER_PROMPT.md
2. Read:
   PHYSICS_LEDGER/WALL_D2_ASSEMBLY3_ENTRY_OBJECT.json
3. Read the frozen A3 declarations + V4 amendment referenced by those files.
4. Verify all load-bearing hashes.
5. Verify W-0 / register untouched.
6. Claim your new file paths in AGENT_COORDINATION.md BEFORE writing.

Do not modify:
- frozen A3 declarations;
- A3 registry;
- Phase-10 cache;
- Phase-11 AF basis cache;
- wall_d2_span_test.py;
- existing Phase-10/11 machinery except where the contract explicitly
  permits a read-only reuse.

============================================================
MISSION
============================================================

The ONLY question for this stage is:

    Are the finite epsilon^0 master integrals correctly derived
    and independently validated?

Nothing beyond that is authorized.

The finite nonlocal response has NOT yet been computed.

============================================================
A3-1A — FILE CLAIM + INPUT INTEGRITY
============================================================

Create a fresh A3-1 instrument.

At entry, print:

- contract hash;
- entry-object hash;
- A3/V4 hashes;
- Phase-10 cache hash;
- Phase-11 AF cache hash.

Refuse to run if any load-bearing artifact drifts.

W-0.

============================================================
A3-1B — IDENTIFY THE MINIMAL MASTER SET
============================================================

Inspect the validated pole machinery and determine EXACTLY which scalar
masters are required to obtain its finite epsilon^0 continuation.

Do not automatically reproduce the entire Phase-10 tensor engine.

Build the smallest sufficient master set.

For each master record:

    definition
    denominator powers
    numerator degree
    d = 4-epsilon form
    pole coefficient
    finite coefficient
    O(epsilon) remainder status
    mu dependence
    Delta dependence

Do NOT import a remembered finite B0/B1/etc. expression as the answer.

============================================================
A3-1C — DERIVE THE epsilon^0 TERMS
============================================================

Derive the finite term from the same dimensional-regulation integral
definition used by the validated pole engine.

Expose the actual chain:

    d-dimensional integral
        -> Feynman parameters
        -> Gamma-function structure
        -> epsilon expansion
        -> 1/epsilon coefficient
        -> epsilon^0 coefficient.

The existing pole result is a regression target only.

Do not back-solve the finite answer from the pole.

============================================================
A3-1D — PRIMARY SCALAR BUBBLE ANCHOR
============================================================

Start with the equal-mass scalar bubble.

Derive its finite part in the project's exact convention.

Then independently evaluate the SAME integral by a route that does not
use the new analytic formula.

Required:

ROUTE A:
    analytic Feynman-parameter derivation.

ROUTE B:
    independent high-precision numerical evaluation of the original
    parameter integral.

Route B MUST NOT call the Route-A analytic result internally.

Use multiple spacelike K^2 samples away from threshold.

Require agreement to an explicitly stated numerical tolerance.

============================================================
A3-1E — BRANCH / THRESHOLD ANALYSIS
============================================================

Derive, from the actual integral:

    Delta(x) = ?

and determine:

- when Delta(x) can vanish;
- threshold location;
- analytic continuation;
- branch prescription;
- real/imaginary parts on the physical side.

Do not assume a logarithm merely because standard bubbles often give one.

The expression must determine the structure.

Use:
    several spacelike points
    +
    at least one controlled timelike point.

For the timelike point, verify the imaginary part independently.

============================================================
A3-1F — HIGHER MASTERS
============================================================

Extend the derivation only to the finite masters actually needed later.

Where a relation such as mass differentiation is used:

    show the differential identity;
    verify it independently on one numerical case.

Do not use the new formula to prove itself.

At least one independent numerical check per master family.

============================================================
A3-1G — INDEPENDENT ROUTE REQUIREMENTS
============================================================

The two routes must genuinely differ.

BAD:
    formula A -> numerical evaluation of formula A.

GOOD:
    integral definition -> analytic derivation

versus

    original parameter integral -> independent numerical quadrature.

If independence cannot be demonstrated, mark the gate UNVERIFIED and STOP.

============================================================
A3-1H — NORMALIZATION / MU CHECKS
============================================================

Explicitly verify:

- the project's factor of 1/(16 pi^2)-type normalization;
- the pole normalization against the validated pole engine;
- mu dependence;
- dimensional-log argument;
- sign convention.

Do not fit an overall normalization constant.

Include negative controls for:
- wrong factor of 2;
- wrong mu scale;
- wrong epsilon sign.

Each control must fail.

============================================================
A3-1I — PERFORMANCE DISCIPLINE
============================================================

REDUCE FIRST.

Do not carry:
- full tensor expressions;
- symbolic 4x4 matrices;
- symbolic external omega,k,m,H everywhere;
- unnecessary epsilon-sector expansions.

Use a small scalar symbolic core.

Cache every validated master.

Print elapsed time per master.

If any single symbolic operation exceeds ~10 minutes without producing a
reusable object:

    STOP that operation,
    diagnose,
    re-represent,
    continue only after the representation is reduced.

Do NOT launch a giant all-masters calculation blindly.

============================================================
A3-1J — RESULT INTEGRITY
============================================================

Every check entry MUST contain an explicit Boolean `pass` field.

Keep explanatory notes outside the check array.

Result JSON must distinguish:

    PASS
    FAIL
    UNVERIFIED

Do not convert a diagnostic note into PASS.

============================================================
A3-1K — DELIVERABLE
============================================================

Produce:

    PHYSICS_LEDGER/wall_a3_1_finite_masters.py

    PHYSICS_LEDGER/WALL_A3_1_FINITE_MASTERS_RESULT.json

    PHYSICS_LEDGER/WALL_A3_1_FINITE_MASTERS_VERDICT.md

Report for each master:

    exact definition
    pole term
    finite epsilon^0 term
    mu dependence
    branch structure
    threshold
    independent numerical comparison
    tolerance
    verdict.

Also report all self-caught defects.

============================================================
HARD STOP
============================================================

When A3-1 is green:

    COMMIT
    UPDATE COORDINATION LOG
    STOP.

Do NOT begin A3-2.

Do NOT:
- assemble Sigma_R^finite;
- calculate Pi_nonlocal;
- TT-project;
- run Q1;
- run Q3;
- run Q4;
- run Q5;
- run J(omega);
- run PV;
- compare against the registered benchmark;
- interpret the low-frequency spectrum.

The ONLY authorized output is:

    validated finite epsilon^0 master engine.

============================================================
REVIEW PRIORITY
============================================================

The load-bearing checks, in order:

1. independent scalar bubble;
2. branch/threshold continuation;
3. higher-master consistency;
4. normalization/mu;
5. reproducibility.

If #1 fails, STOP immediately.
If #1 passes but #2 fails, STOP.
Never proceed downstream with an unvalidated finite master.

W-0.
No register edits.
No frozen-file edits.
```

## BUILD-SESSION HANDSHAKE

  a. Verify this file's sha256 against the value recorded in
     AGENT_COORDINATION.md.
  b. Verify standing state: HEAD 1096c39 or later; tree state as recorded;
     frozen-file integrity intact (v1 87e2d24d..., registry faa977d4...,
     v2 6f2a762f..., v3 b0b9983b..., Phase-12 instrument a9850cd5...).
  c. Read the A3-1 builder prompt (99a369b3...), the ASSEMBLY-3 brief
     (fff07e51...), and the entry object (419c455b...) in full.
  d. Claim file paths in AGENT_COORDINATION.md BEFORE writing (A3-1A).
  e. Execute A3-1B..A3-1K in order; observe the review-priority stop ladder
     and every hard stop above.
  f. On green: COMMIT, update the coordination log, STOP. A3-2 requires
     explicit owner/reviewer acceptance of the A3-1 result — including
     inspection of the finite-master formulas and branch structure —
     before anything downstream reads them.

— end of A3-1 execution prompt —
