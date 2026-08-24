# Validity-domain gap — Task 1 adjudication input (owner decision required)

**Date:** 2026-08-23 · Evidence-based classification; no register edit.

## Question

Is ω ≪ ω_c — the domain every registered spectral claim implicitly lives in — **(a)** a validity
condition implied by the derivation, **(b)** a newly declared approximation requiring its own entry
and price, or **(c)** an unresolved specification gap?

## Evidence

1. `GRUT_ToE.md:41` ("Scope of validity") declares **assumption classes only**: linear response,
   Gaussian bath, SK/Born reduction. No frequency range appears anywhere in the validity paragraph.
2. `calc/finite_T_exponent.py` works at ω ≤ 0.5 ω_c in practice but states no domain.
3. rung3's registered question is explicitly "the exact **small-ω** scaling exponent" — low-ω by
   construction of the question, not by a stated validity condition.
4. Priority-2A found the Re χ sign change sits exactly at x≈ω/ω_c and is cutoff-shape-dependent —
   i.e., the gate that distinguishes physics from artefact is currently unanswerable from the text.

## Classification: **(c) unresolved specification gap**

It is not (a): nothing in the derivation derives an ω domain; the EFT-with-cutoff structure
*conventionally* carries its own validity window, but that convention is not written in the register,
and an unwritten convention is precisely "implied," which must not silently become "declared."

It is *cheaply closable as* (b): one sentence — e.g. "the effective response description is claimed
for ω < ω_c" — closes it, and EFT convention supports it. But per instruction, that declaration is
an owner adjudication, paired with ω_c pinning since a declared cutoff without a declared window
leaves the §8 gate unanswerable.

## Consequence if left open

Every spectral claim stays implicitly low-ω; the §8 gate (does a dispersive feature fall inside the
theory's domain?) remains structurally unanswerable; and definition-as-target patterns can hide in
the undeclared region (as nearly happened at x≈ω_c).