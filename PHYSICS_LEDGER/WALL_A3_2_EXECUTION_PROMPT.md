A3-2 AUTHORIZATION — ASSEMBLE THE FINITE RETARDED RESPONSE

Standing state:
    A3-1 ACCEPTED at commit efb6e73.
    Finite epsilon^0 masters independently validated.
    Branch threshold independently verified.
    A3-1 limitations remain disclosed.
    Do not reopen A3-1 unless a contradiction appears in execution.

MISSION:
    Assemble the COMPLETE finite retarded one-loop graviton
    self-energy using the validated finite masters.

DO NOT perform Q1/Q3/Q4/Q5 yet.
DO NOT open J(omega).
DO NOT run PV.
DO NOT TT-project early.

============================================================
A3-2A — INPUT INTEGRITY
============================================================

Validate and load:
- A3-1 finite-master artifact;
- Phase-10 loop cache;
- corrected Phase-11 AF basis;
- Phase-12 frozen MS subtraction;
- A3 entry object;
- V4 F1 amendment.

All hashes must match.

Claim new output paths before writing.

============================================================
A3-2B — FULL FINITE KERNEL
============================================================

Construct:

    Sigma_R^finite(mu nu,rho sigma; omega,k,H,m)

using:
- bubble factor 1/2;
- signed retarded rule;
- l and l-K routing;
- frequency-local insertion machinery;
- corrected action-functional basis conventions;
- A3-1 validated finite masters.

Assemble the COMPLETE tensor object.

Carry all non-TT sectors.

Do not project before assembly is complete.

============================================================
A3-2C — SUBTRACTION
============================================================

Apply the already frozen:

    Pi_local^MS

pole subtraction only.

No finite counterterm freedom.

Verify:

    bare finite-order object
        =
    local subtraction contribution
        +
    remaining finite response

with no accidental modification of finite nonlocal terms.

============================================================
A3-2D — FINITE/NONLOCAL STRUCTURE
============================================================

Identify the finite terms containing:
- logarithms;
- threshold functions;
- square-root/branch structures;
- other non-polynomial dependence.

Do not fit a power law.
Do not classify the low-frequency response.
Do not call anything relaxational/resonant yet.

At this stage only expose the actual analytic structure.

============================================================
A3-2E — INDEPENDENT CHECKS
============================================================

At minimum:

1. Reproduce the scalar-bubble finite limit embedded in a representative
   tensor component.

2. Verify the finite kernel reduces to the validated H0 flat limit.

3. Verify the retarded support/sign convention remains the same as the
   validated pole assembly.

4. Verify the local subtraction removes only the previously identified
   local sector.

5. Verify a deliberately wrong branch choice produces a detectable
   mismatch.

============================================================
A3-2F — REPRESENTATION DISCIPLINE
============================================================

Use the same reduced representation strategy that made Phase 11 tractable.

Do not carry unnecessary symbolic dependence.

Use rational sample points where the contract permits.

Cache expensive finite assembly blocks.

Print elapsed time per block.

If a block exceeds ~20 minutes without a reusable result:
    STOP THAT BLOCK.
    Diagnose/re-represent.
    Do not increase the timeout indefinitely.

============================================================
A3-3 — FREEZE THE COMPLETE RESPONSE
============================================================

When the finite retarded kernel is complete, emit:

    Sigma_R_finite_full.json
    Sigma_R_finite_full.verdict.md

The PRIMARY immutable object is:

    Sigma_R^finite(mu nu,rho sigma; omega,k,H,m)

The TT projection is a DERIVED object only.

Hash the complete object.

Create a manifest containing:
- complete kernel hash;
- TT-view hash;
- master-engine hash;
- subtraction hash;
- input hashes.

After the freeze, nothing may alter the object.

============================================================
HARD STOP
============================================================

Record the finite response and its analytic structure.

Then STOP.

DO NOT:
- run Q1;
- run Q3;
- run Q4;
- run Q5;
- compare J(omega);
- run PV;
- fit Im chi;
- classify relaxation/resonance;
- alter the frozen basis;
- refit coefficients.

The next stage begins only after owner/reviewer inspection.

MOST IMPORTANT:

    Do not tell the calculation what spectral behavior to find.

    Let the finite epsilon^0 kernel produce it.

W-0.
No register edits.
