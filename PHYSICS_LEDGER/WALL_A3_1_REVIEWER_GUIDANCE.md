# Z.AI — REVIEWER GUIDANCE FOR A3-1 EXECUTION

Operates under the frozen A3-1 contract chain at HEAD af61532 (execution
prompt 376fe982...; A3-1 prompt 99a369b3...; brief fff07e51...). This is
supervision guidance, not a new planning layer. Verbatim below.

```text
Z.AI — REVIEWER GUIDANCE FOR A3-1 EXECUTION

You are executing under the already-frozen A3-1 contract at HEAD af61532.
Do not redesign the workflow or create another planning layer.

PRIORITY ORDER:

1. BUILD ONLY THE MINIMAL FINITE MASTER REQUIRED FOR THE SCALAR BUBBLE.
2. GET AN INDEPENDENT NUMERICAL CHECK.
3. ONLY AFTER THAT, derive the remaining masters.
4. HARD STOP if the scalar-bubble anchor fails.

Do NOT start with the full tensor loop.
Do NOT assemble Sigma_R.
Do NOT calculate Pi_nonlocal.
Do NOT inspect J(omega).
Do NOT run Q1-Q5.
Do NOT run PV.

==================================================
FIRST OBJECT: EQUAL-MASS SCALAR BUBBLE
==================================================

Start from the actual d=4-epsilon integral definition already used by
the validated pole engine.

Derive its epsilon expansion explicitly:

    I(epsilon)
      = I_-1/epsilon + I_0 + O(epsilon)

The new target is ONLY I_0.

Preserve exactly the normalization and denominator convention of the
validated pole engine.

Do not import a remembered B0 formula as the result.

==================================================
INDEPENDENT CHECK
==================================================

Route A:
    derive I_0 analytically.

Route B:
    evaluate the ORIGINAL Feynman-parameter integral numerically at
    several spacelike external momenta using high precision.

Route B MUST NOT call, simplify, differentiate, or otherwise reuse
Route A's analytic expression.

The numerical routine should receive the original integrand.

Use at least 3 non-special spacelike points.

Require agreement to a declared high-precision tolerance.

If Route A != Route B:
    STOP.
    Preserve both outputs.
    Diagnose only.
    Do not proceed to higher masters.

==================================================
BRANCH TEST
==================================================

After the spacelike check passes, determine from the actual Delta(x)
where the parameter integrand becomes singular.

Then independently evaluate one controlled timelike point.

Report:
    threshold
    branch prescription
    real part
    imaginary part.

Do not assume the branch structure in advance.

==================================================
EFFICIENCY
==================================================

Keep all calculations scalar.

Use one symbolic parameter Delta where possible.

Do not carry omega,k,m,H simultaneously unless required.

Cache the validated scalar master immediately.

Print elapsed time.

If a symbolic operation becomes expensive, reduce the representation
rather than increasing the timeout.

==================================================
REPORT DISCIPLINE
==================================================

At the first milestone report ONLY:

    scalar bubble finite formula
    independent numerical comparisons
    threshold/branch result
    normalization
    PASS/FAIL

Do not write an essay before producing those outputs.

Do not create speculative diagnostics unless a gate fails.

==================================================
AFTER SCALAR BUBBLE PASSES
==================================================

Then derive only the additional finite masters actually consumed by
the existing numerator algebra.

Use mass derivatives or parameter identities only when independently
verified.

Perform at least one independent numerical check per new master family.

==================================================
FINAL A3-1 STOP
==================================================

A3-1 is complete only when:
    scalar bubble PASS
    branch PASS
    all required higher masters PASS
    normalization/mu checks PASS
    independent checks PASS

Then:
    commit
    update coordination log
    STOP.

Do not advance to A3-2 without owner/reviewer acceptance.

Most important rule:

    COMPUTE FIRST.
    VALIDATE SECOND.
    INTERPRET THIRD.

At this point there is nothing left to plan.
```
