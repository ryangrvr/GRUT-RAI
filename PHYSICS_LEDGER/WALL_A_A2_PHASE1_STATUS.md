# A2 phase 1 — status: STARTED, STOPPED AT SOURCE VERIFICATION

**Date:** 2026-08-23 · Honest stop, per the same discipline that stopped G1.

## What happened

Implementation began from recalled Barnes–Rivers operator forms. On review **before running**:
the Ω¹ and Ω⁰ᵗ normalizations were being written from memory, not from a verified source.
This session's own precedent (the cos-kernel reported passive with Im χ = −4.99 at resonance;
the object substitution caught only because someone recomputed) makes shipping recalled algebra
the exact failure mode A2 exists to prevent. Stopped; nothing incorrect was emitted.

## What the frozen brief requires before coding resumes

Per the borrowed-vs-derived discipline: **source-verify the Barnes–Rivers definitions against a
primary source** (or a registered secondary carrying them), record the convention (which of the
several BR normalizations is in use), THEN implement, then plant-and-recover:

- plant a pure-TT structure → must land entirely in the P² sector;
- plant a pure-scalar-solenoidal structure → P⁰s sector;
- verify completeness Σ = 1 on symmetric tensors, idempotence, orthogonality, dof counts
  2/2/1/1 — reproducing banked Part A of `calc/RESULTS_operator_basis.md`;
- verify the EH counterexample: linearized EH = ½k²(P² − 2P⁰s) in this normalization
  (banked Part C connection).

Only then does the diagonal-Ward covariant enumeration begin, per B-1..B-4.

## Why this is a clean stopping point rather than an omission

The alternative — implementing half-recalled operators and testing them against each other —
would produce internally consistent checks on possibly-wrong objects: the exact failure class
of this session's twentieth defect. The spatial-frame result is banked; its reproduction is a
bounded next-session task once the definitions are source-grounded.

## Queue state

A5 FULL PASS (closed) · A2 phase 1 blocked-on-source-verification (this document) · A2 phases
2+ queued behind it · +1 discharge untouched pending graduation screen · W-0 fence binding.