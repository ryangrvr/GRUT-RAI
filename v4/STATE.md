# GRUT-RAI v4.1 — current state (read me first)

**2026-06-24.** A one-page, honest snapshot for an outside reader. Detail lives in
[WRITEUP.md](WRITEUP.md) (the foundation), [SPECIALIST_RESPONSE.md](SPECIALIST_RESPONSE.md)
(three rounds of external review, §R1–R3), and the runnable modules in `v4/`. The organizing
rule is a **tier gate** (`gate.py`/`ci_check.py`) that refuses to call a claim *derived* unless
it is checked and rests on no open input. Everything below is gate-enforced.

## What's solid (the foundation)

- **Five DERIVED rungs**, each checked: **Q** (the in-in causal arrow), **μ_linear = 1** (the
  TT projector annihilates the linear scalar response → linear cosmology is *exactly* ΛCDM),
  the monotone arrow of time, QM as the τ→0 limit, and the **689 Hz gravitational-decoherence
  falsifier** (zero parameters, framework-independent).
- **One no-go** (no new propagating vacuum pole — Ostrogradsky + Q/FDT).
- **Two foundational parameters, both ANCHORS** on free data the action does not fix:
  - **single-pole-ness** ← the vacuum bath's *collisionality* (the crux, below);
  - **α = 1/3** ← which mode is the IR carrier; `a/c = 1/3` is robust and scheme-independent,
    and α's would-be derivation is Q-protected (a propagating conformal mode is ghost-forbidden).

## The forward work (the closed-viscoelastic spine) — honest, including two failures

The reviewer's plan: pin the medium as four constitutive inputs (kernel *swappable*, closure,
drive, scale-coupling) and build outward. Done as anchors. Then two build-forward targets, **both
of which over-claimed and were demoted by an adversarial pre-screen aimed at exactly that** — kept
as honest record, not banked as results:

- **Power-spectrum branch test (OPEN, not a falsifier).** "Collisional ⇒ a characteristic scale;
  free-streaming ⇒ scale-invariance" is *degenerate* (a broad collisional spectrum reads
  scale-free), *one-sided* (a free location lets the collisional break hide), and *entangled* with
  known ΛCDM features (k_eq, BAO). Its OPEN target names what would rescue it.
- **Collisionality commitment (FAILED, `bath_collisionality.py`).** The attempt to resolve the
  fork by declaring GRUT "viscoelastic" fails: the exclusion of free-streaming is *definitional*,
  and **GRUT's own viscoelastic χ_mem rings** for τ_K > τ₀/4, so a memory-character test
  misclassifies GRUT's own collisional kernel as free-streaming. The fork **stands**.

## The one crux, and the one thing that resolves it

Everything funnels to: **is GRUT's vacuum bath collisional (→ Ohmic/single-pole) or free-streaming
(→ Weinberg non-local memory → single-pole fails)?** The minimal action (Q + FDT + 1/r + KMS) does
not fix it, and it cannot be resolved by renaming or by building harder (we tried, twice). The
**only** resolution is a real computation: derive the finite-T `⟨T_TT T_TT⟩(ω, k→0)` from GRUT's
`z·T_TT` vertex and read whether it is **Ohmic** (collisional, `Im G_R ~ ηω`, exponential-envelope
memory) or **Weinberg** (free-streaming, power-law-envelope memory). This is hard physics and is
exactly the calculation the in-loop process is *most* prone to bias on — so it should be done with,
or by, someone outside the loop.

## What can contact reality now

The **689 Hz decoherence plateau** (1 μm gold sphere; `Λ = G m² S(l/R)/(ħl)`, zero free
parameters, distinguished from Diósi–Penrose by an extended-body kink). It does **not** wait on
the fork — it is the one claim ready for an experimentalist today.

## Honest meta

Three review rounds returned single-pole to its original ANCHOR (the loop walked away from the
correct answer and the literature walked it back), and the last two build-forward targets
over-claimed in the same *direction* (toward "single-pole survives"). The gate keeps the work
honest about what is *shown*; it has no opinion about *which way* it is wrong. That is why this
needs you: the directional error and the missing physics are the kinds an outside referee catches
and the loop does not.

## Verify / state

```
python -m v4.ci_check     # gate: 20 claims, 0 violations
python -m v4.audit        # one-pass tier view
python -m pytest v4/tests # 60 tests
```
Tiers: ANCHOR 9 · DERIVED 5 · HOSTED 2 · FORBIDDEN 1 · OPEN 1 · CONJECTURAL 2. All v4.1 work is
local (12 commits, unpushed).

**What's asked:** (1) the `z·T_TT` vertex computation — is GRUT's vacuum viscous or free-streaming?
(that single number decides single-pole); (2) whether 689 Hz is worth an experimental contact; and
(3) a referee's read on the foundation in [WRITEUP.md](WRITEUP.md).
