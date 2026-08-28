# ASSEMBLY-3 BUILDER CONTRACT — THE FINITE eps^0 RETARDED NONLOCAL RESPONSE

STATUS: OWNER-AUTHORIZED 2026-08-28. Phase 12 is CLOSED: the owner accepted
the V4 governance amendment (WALL_A_A3_DECLARATIONS_V4_AMENDMENT.md, sha256
f6127ca65ad6636be432b6d6c6fb6d30bb0b9f0c8912df4a9a1054e54919dd56) and the
51/51 independent replay as complete, and independently verified all four
frozen files byte-identical. F1 is formally superseded, not silently edited.
The finite eps^0 sector remains NOT YET COMPUTED; this contract authorizes
its computation and nothing else.

This document is the immutable ASSEMBLY-3 builder prompt, assembled verbatim
from the owner's authorization of 2026-08-28. A builder session MUST begin
with the handshake in section 5 BEFORE any computation.

STANDING STATE: commit 7a19c2f.
  - Pi_local^MS FROZEN, fingerprint e2f0bbfe6fd4c89d.
  - 208/208 pole terms local under the V4-corrected F1; zero nonlocal pole
    residue (dual independent classifier; bytecode-level independence gate).
  - Entry object: PHYSICS_LEDGER/WALL_D2_ASSEMBLY3_ENTRY_OBJECT.json
    (sha256 419c455bccdd90dcbef708698e5339b7a2d32f0c8b07c49af9de6ab099316ccb)
    — status TO_BE_DERIVED; nothing in it may be read as a prediction. It
    carries the conventions, the 100-slot map, the H grading, and the
    pre-registered Q1-Q5 criteria. It is the input contract.

Sections, in order of authority:
  1. THE OWNER BRIEF (verbatim) — the task.
  2. THE REVIEWER ADDENDUM (verbatim) — two load-bearing firewalls.
  3. THE BRANCH-STRUCTURE GUARD (verbatim) — owner addition to A3-1.
  4. OWNER/CHECKER-SIDE OBLIGATIONS — deliberately kept off the builder.
  5. HANDSHAKE PROTOCOL.

## 1. THE OWNER BRIEF (verbatim)

```text
ASSEMBLY-3 — THE FINITE eps^0 RETARDED NONLOCAL RESPONSE

STANDING STATE: commit 7a19c2f. The UV sector is FROZEN: Pi_local^MS
fingerprint e2f0bbfe6fd4c89d, 208/208 pole terms local under the V4-corrected
F1, zero nonlocal pole residue. The ASSEMBLY-3 entry object
(WALL_D2_ASSEMBLY3_ENTRY_OBJECT.json) carries the conventions, the 100-slot
map, the H grading, and the pre-registered Q1-Q5 criteria. Read it first; it
is the contract.

THIS IS THE FIRST STAGE WHOSE OUTPUT IS A PHYSICS RESULT RATHER THAN
APPARATUS. The verification burden is correspondingly highest.

WHAT IS ACTUALLY NEW: the eps^0 masters. Everything upstream extracted poles;
the finite part requires the O(eps^0) term of the same integrals, which is
where log(Delta/mu^2) enters and the Feynman-parameter integral over x stops
being polynomial. That integral is the source of the branch structure and
therefore of ALL the frequency dependence the physics questions care about.
Build and gate those masters as their own engine before assembling anything.

DESIGN MANDATES (from the reviewer; these are not suggestions):
  M1 REDUCE REPRESENTATION FIRST, then compute, then check independently.
     Do NOT carry maximal symbolic generality. The Phase-11 pattern that
     worked: numeric rational K samples, phases stripped into the derivative
     rule, sector grading so unreachable sectors never form, per-block
     elapsed time printed, any block over ~20 min stopped and re-represented.
     Three representations were tried before one worked; do not relearn that.
  M2 TT PROJECTION IS DOWNSTREAM. Assemble the FULL non-TT object first and
     carry the discard bookkeeping, exactly as A1/A4 established. Projecting
     early would delete structures before the assembly can determine whether
     they matter -- and would partially impose Q1's answer.
  M3 FREEZE THE BARE FINITE RESPONSE BEFORE ANY COMPARISON. Emit and hash
     Sigma_R^TT_finite(omega,k;H,m) as an immutable artifact. Only then may
     any comparator be touched. J(omega) remains a COMPARATOR, NEVER AN
     INGREDIENT -- the barred-inputs guard stays live and must fire on any
     attempt to read it during construction.

STAGED, WITH HONEST STOPS BETWEEN STAGES:
  A3-1 eps^0 MASTERS. Derive the finite part of each master used by the pole
       engine. Gate each against an independently computed case (a known
       scalar bubble finite part is the natural anchor). Report the
       x-integral's analytic structure explicitly -- where the branch cut
       sits and why.
  A3-2 THE FINITE INTEGRAND. Assemble with the frozen conventions: bubble
       1/2, signed retarded rule Sigma_R = Sigma++ + Sigma+- , routing l and
       l-K, frequency-local insertions, corrected F1 locality for any
       subtraction. Subtract Pi_local^MS exactly as frozen -- pole-only, mu
       symbolic, zero finite-part discretion. Verify the subtraction removes
       the pole and touches nothing else (the planted-structure battery from
       Phase 12 is the template).
  A3-3 FREEZE. Emit Pi_nonlocal^invariant with a sha256 manifest. Nothing
       downstream may modify it.
  A3-4 THE VERDICTS, computed against the ALREADY PRE-REGISTERED criteria in
       the entry object -- read them BEFORE computing, do not re-derive them:
         Q1  tensor placement, with the Q1b parity sub-record if X_sw != 0
         Q5  flat-limit reduction, per channel, IR-obstruction branch honest
         Q4  reciprocity, PROPER Onsager-Casimir with H treated as T-ODD
         Q3  IR analytic class, with 1 < s < 2 reported as INTERMEDIATE
       Record all verdicts BEFORE any comparison artifact is opened.

THE +1 DISCHARGE RULE, unchanged and binding: dischargeable ONLY by
Q1 INSIDE AND Q5 INSIDE. Q3 and Q4 answer different questions and DO NOT
vote. Nothing in the UV result votes on it. Discharge itself remains an owner
ruling at the bank gate.

HARD STOPS: no J(omega) comparison, no PV rerun, no response-level dual-gauge
until A3-4 verdicts are recorded and frozen. If a stage needs a convention
the frozen declarations (+v2,+v3,+v4) do not cover, STOP -- the fork is the
finding and a superseding amendment is the only path.

W-0 throughout. Register untouched. Nothing banked.
```

## 2. THE REVIEWER ADDENDUM (verbatim — two load-bearing firewalls)

```text
REVIEWER ADDENDUM — TWO LOAD-BEARING FIREWALLS

A3-1 INDEPENDENCE:
The finite eps^0 master engine is a NEW engine layer.

Do not validate it solely by algebraic identities derived from the same
implementation that produced it.

At least one finite master must be independently obtained from a separate
route (e.g. direct analytic evaluation / independently implemented
Feynman-parameter integral / high-precision numerical quadrature against
the analytic form).

The comparison must include:
    - real part;
    - logarithmic dependence;
    - branch/threshold location;
    - normalization.

A3-3 FREEZE SEMANTICS:
The immutable object is the COMPLETE finite retarded kernel BEFORE TT
projection:

    Sigma_R^finite(mu nu,rho sigma; omega,k,H,m).

Its TT projection is a derived view:

    Sigma_R^TT,finit[e].

Do not hash only the TT projection as the primary frozen object.

A3-4 must read the frozen complete object and perform the TT projection
from that object.

No comparison artifact may alter either representation.
```

NOTE (cross-reference only, not new policy): the addendum's "A3-3 FREEZE
SEMANTICS" refines brief mandate M3's hash target. Both texts are
authoritative; the addendum governs the freeze: the PRIMARY immutable object
is the COMPLETE finite retarded kernel BEFORE TT projection,
Sigma_R^finite(mu nu, rho sigma; omega, k, H, m); Sigma_R^TT_finite is a
derived view, emitted and hashed secondarily, never the primary artifact.

## 3. THE BRANCH-STRUCTURE GUARD (verbatim owner addition to A3-1)

```text
A3-1 must derive and report the analytic structure of the x-integral
from the computed finite master.

Do not assume a particular logarithm, threshold exponent, branch location,
or low-frequency power law beyond what follows from the derived analytic
expression.

The known scalar bubble serves as the normalization/control case, not as
a template for the de Sitter result.
```

## 4. OWNER/CHECKER-SIDE OBLIGATIONS (kept on our side, not the builder's)

  1. eps^0 MASTER INDEPENDENT VERIFICATION. The masters are the new engine
     layer; every prior stage's worst failures came from an unvalidated
     engine layer. The checker independently verifies the masters BEFORE
     anything is built on them — on top of the builder's own A3-1 anchor
     and the addendum's separate-route requirement.
  2. Q3 BLINDNESS. Q3 is the question the program has an interest in. Its
     verdict must be computed and recorded before anyone looks at a
     comparator; supervision stays owner/checker-side, not delegated.
  3. THE +1. Dischargeable ONLY by Q1 INSIDE and Q5 INSIDE; Q3 and Q4 do
     not vote; nothing in the UV result votes. Discharge itself remains an
     owner ruling at the bank gate.

## 5. HANDSHAKE PROTOCOL (builder session entry)

  a. Verify this file's sha256 against the value recorded in
     AGENT_COORDINATION.md.
  b. Verify standing state: git HEAD at 7a19c2f or later AND frozen-file
     integrity intact (v1 87e2d24d..., registry faa977d4..., v2 6f2a762f...,
     v3 b0b9983b..., Phase-12 instrument a9850cd5... byte-identical).
  c. Read WALL_D2_ASSEMBLY3_ENTRY_OBJECT.json in full BEFORE computing.
     Its Q1-Q5 criteria are pre-registered; do NOT re-derive them.
  d. Observe every HARD STOP in the brief: no J(omega) comparison, no PV
     rerun, no response-level dual-gauge until the A3-4 verdicts are
     recorded and frozen; a needed-but-uncovered convention is a STOP —
     the fork is the finding; a superseding amendment is the only path.
  e. W-0 throughout. Register untouched. Nothing banked. The barred-inputs
     guard (J(omega) is a comparator, NEVER an ingredient) stays live and
     must fire on any construction-time read attempt.

— end of contract —
