# Response to Specialist Review

### GRUT-RAI v4.1, single-pole status: ANCHOR → ~~DERIVED~~ → **PENDING-REVIEW**

**2026-06-24** · §0–§8 below are Revision 1 (round 1); §R2 at top is Revision 2 (round 2)

---

> ## ⚠ R3 — ROUND-3 CORRECTION (you were right again, and about the *direction*, not just the number)
>
> Two things, and the second is the one that matters.
>
> **(1) The misattribution — the same pattern a third time.** I wrote "collisionless vacuum (T=0):
> stress-tensor phase space ⇒ `s ≈ 2` (your value)." That is not your value. You gave `s = 2` only
> as the `(∂φ)²` *floor*, flagged the gravitational/quadrupole vertex runs higher (Cho–Hu's
> published vacuum graviton kernel is `ω⁵`), and — decisively — said the vacuum `T=0` exponent is
> the *wrong object*, because at finite `T` the memory is set by transport, not vacuum phase space.
> A tidy intermediate I didn't check against the source. Removed from the map and the docs.
>
> **(2) The literature returned something stronger and worse for the claim than "`s≥1` across
> branches."** I leaned on the DOS/phase-space picture for the collisionless case — and that
> picture is exactly what the transport calculation overturns. Weinberg (2004) is a refereed
> derivation that a collisionless massless bath coupled to the TT sector produces a **non-local,
> history-dependent, Bessel-tail memory kernel** — long-ranged memory, the explicit *opposite* of
> single-pole, with a finite non-decaying residual. I reproduced the structure first-hand (this
> time the right object): `K(s)=∫(1−μ²)²cos(μs)dμ` has a `~s⁻³` power-law envelope, 18 sign
> changes, and a long-lag residual ~10²× the exponential branch's. So the honest map is **not**
> "every branch `≥1`, sub-Ohmic forbidden." It is:
> - **collisional → Ohmic → single-pole holds**;
> - **collisionless → Weinberg non-local → single-pole FAILS**;
> - **collisionality is not fixed by the action.**
>
> That is a genuine fork, and the deciding datum is free. **So single-pole-ness is an ANCHOR — and
> it is the *original* 1C ANCHOR, the one with collisionality as the free datum from the start.**
>
> **The thing worth sitting with.** Three rounds in, the destination is where I began. The 1C
> anchor wasn't timidity — it was correct, and each round of AI-assisted "sharpening" moved away
> from it (ANCHOR → DERIVED → PENDING-REVIEW) before the literature moved it back. The loop's
> errors had a *direction*: toward the stronger, more flattering claim. That is the failure mode
> the gate cannot catch — it keeps me honest about what I've *shown*, but it has no opinion about
> which way I'm wrong. Only an outside referee with the transport literature in hand did.
>
> **Reverts (the machinery, not just the claim).** `single_pole` → **ANCHOR**; the `PENDING_REVIEW`
> tier I added in round 2 → **removed** (its "pending a number that settles it" framing was the
> over-optimism — the verdict depends on free data, not a pending computation); the round-1
> `fast_mode_content` scaffolding → **removed**. Clean 6-tier gate, 13 claims, 0 violations; 44
> tests pass. `targets/fast_mode_dos.py` reframed to the collisionality fork.
>
> **The settle target, corrected:** not "does `s≥1` survive," but **"is GRUT's vacuum at `T_c`
> collisional or free-streaming?"** Weinberg 2004 + Hawking 1966 answer what each branch gives; the
> only genuinely open piece is confirming GRUT's exact `z·T_TT` vertex maps onto the
> gravitational-wave-in-a-medium structure. Viscous ⇒ single-pole graduates; free-streaming ⇒
> single-pole is refuted. α is untouched.
>
> Round 2 below (and round 1 under it) are kept as the honest record of the path. Both are
> superseded on the single-pole tier by this section.

---

> ## ⚠ R2 — ROUND-2 CORRECTION (you were right again; I over-corrected in round 1)
>
> You caught two things and both land. **(1) The `s = 2` was still wrong** — it conflated the DOS
> with the spectral density. `J(ω)` carries the field-mode normalization `1/(2ω_k)`, and for a
> local linear coupling to a massless field in 3+1D `J(ω) ∝ ∫d³k (1/ω_k) δ(ω−c|k|) ∝ ω` — **Ohmic,
> `s = 1` (marginal), not `s = 2`.** I verified it two ways; the number is fixed in
> `targets/fast_mode_dos.py::linear_coupling_s`. That a wrong intermediate survived a "first-hand
> re-derivation" is the tell you named — the DOS argument wearing the spectral density's clothes,
> the v4 sin in miniature. Owned.
>
> **(2) The exponent is not settled by power-counting — it's collisionality-dependent**, the one
> thing the framework leaves free. The honest map (now in the module):
> - **collisional** (`T_c`, hydrodynamic): Kubo `Im G_R^{TT}(ω) ~ ηω` ⇒ `s = 1` (Ohmic). *This
>   branch is live* — a vacuum at `T_c` has thermal structure; my round-1 "needs self-interaction
>   beyond the action" was wrong.
> - **collisionless vacuum** (`T=0`): stress-tensor phase space ⇒ `s ≈ 2` (your value; my `s = 5`
>   needed GRUT's quadrupole/spin-2 vertex, uncomputed — retracted).
> - **collisionless thermal**: a free-gas `δ(ω)` spike on the continuum — an object to interpret,
>   not an exponent.
>
> **What survives, and what doesn't.** Survives: every clean branch is `s ≥ 1`, and `s < 1` needs
> an IR-enhanced DOS masslessness forbids — so single-pole-ness is **well-motivated across
> branches**. Does not: "relativity fixes the DOS to `ω²` so `s = 2`," and the graduation to
> DERIVED built on it. **`DERIVED … pending review` was a contradiction in my own tier system.**
>
> **Action taken.** Added a `PENDING_REVIEW` tier to the gate (your recommendation) — a
> derivation-grade *argument* that does not pass a settling check, which a DERIVED claim may not
> consume. Re-tiered `single_pole` DERIVED → **PENDING_REVIEW**, with the cross-branch argument as
> its support and the finite-T computation as its settle condition. The round-1 graduation is
> reverted; the honest record (1C wrong, round-1 wrong) is kept, not overwritten. Gate: 14 claims,
> 0 violations; 46 tests pass.
>
> **The externalized question (your phrasing, recorded verbatim as the settle target):** *A slow
> variable bilinearly coupled to the transverse-traceless sector of a thermal massless field
> (graviton bath at `T_c`) — what is the IR exponent of the influence-functional `J(ω)` as `ω→0`?
> Does finite-T interacting `⟨T_TT T_TT⟩(ω,k→0)` give Ohmic (`s=1`, hydrodynamic viscosity peak)
> or super-Ohmic (`s≥2`, free phase space), and how is the free-gas `δ(ω)` handled?*
>
> The rest of round 1 stands: α holds, Q2/Q4 sound, §4 over-tight. Only the single-pole half moved
> — from a premature theorem to an honest strong-conjecture-pending-computation.

---

## 0. What the review did *(round 1)*

You found the load-bearing tension on first pass, traced it across §2/§4/§6, and handed back a
*constructive* correction that makes the foundation stronger, not weaker. Every code and physics
claim you flagged, I re-derived first-hand before accepting it — including a genuine attempt to
break the super-Ohmic conclusion you expected, because the lesson of the review is precisely that
a system talking to itself has a blind spot for standard physics it didn't think to invoke. The
conclusion survived the attempt. Net of the round: **one anchor graduates to a theorem, one holds,
and one aesthetically-pleasing unification was over-tight.** Point-by-point below; the gate and
tests are updated to match.

---

## 1. §6/§2 tension — accepted; resolved by *agreement* (your cleanest catch)

You're right, and it's the cleanest catch. A fully-specified noise kernel is, by the FDT we lock
in §2, a fully-specified dissipation kernel: `J(ω) = N(ω)·tanh(βω/2)`, hence a specified `s`. So
§6's "zero-free-parameter" Anastopoulos–Hu kernel *was* a commitment about `s` all along. And the
standard AH gravitational kernel is **super-Ohmic** (graviton-DOS descended, `J ~ ω³`, `s ≈ 3`),
verified here:

```
AH/graviton J(ω) IR slope          : 3.00   (super-Ohmic)
FDT noise N = coth(βω/2)·J slope    : 2.00
recovered J = N·tanh(βω/2) slope    : 3.00   (identity closes)
```

So the resolution is not the weak one (insulating §6 from §2 by claiming the plateau is
edge-insensitive — which would have *needed showing*). It is the strong one: **§6 and §2 were
never opposed.** §2 was simply wrong to call free what §6 had already committed. With §2 corrected
(below) both sections say super-Ohmic, and the inconsistency a referee sees on first pass is gone.
(`v4/targets/fast_mode_dos.py::ah_kernel_is_super_ohmic`.)

---

## 2. Q1 — accepted, and it inverts in our favour: single-pole is a *theorem*

This is the substantive correction and I'm taking it straight. You're right that the framework is
not input-free on the dispersion relation. "Massless + 1/r kernel + relativistic CTP" reads as
`ω = c|k|`, and once the fast bath modes have a fixed dispersion and the TT vertex, `J(ω)` is the
coupling-weighted DOS and `s` is **computable, not free**. Computed first-hand:

```
massless DOS, 3+1D                  : ρ(ω) ~ ω²       (super-Ohmic)
linear coupling z·φ                 : J(ω) ~ ω²  ⇒ s = 2
stress-tensor coupling z·T, T~(∂φ)² : J(ω) ~ ω⁵  ⇒ s = 5   (two-quantum phase space)
finite-T / interacting (Kubo)       :            s = 1   (the boundary)
```

Every case is `s ≥ 1`. By the §2.2 classification that makes single-pole-ness **DERIVED**. I also
ran the escape you'd expect me to skip: sub-Ohmic (`s<1`) requires an **IR-enhanced** DOS — a
non-relativistic `ω~k²` band (`ρ~ω^{1/2}`) or a glassy/`1/f` soft mode (`ρ~ω^{-1}`) — exactly what
masslessness argues *against*. The relativistic vacuum is not among the slow cases.

**The 1C error, named precisely:** §2.3 treated the DOS IR-edge as a free dial (`s = p`,
`p` free). Relativity fixes `p = 2`. Your inversion is correct — *collisionless free fields are
super-Ohmic in 3+1D*, not sub-Ohmic — and you're right that the document's own sub-results were
already closing every `s<1` channel (the retracted scale-separation lean; the Hubble-broadening
narrowness; the derivative-protected de Sitter finiteness). The loop kept closing slow routes and
never stepped back to read the pattern. That's the in-loop blind spot, demonstrated on us.

**What changed in the gate.** I made the commitment explicit rather than leaving it implicit (you:
"if that's the position, state it"):
- new ANCHOR `fast_mode_content` — *the vacuum's fast modes are standard massless relativistic
  field modes (`ω=c|k|`), as the 1/r kernel + relativistic CTP already imply.*
- `constitutive_law_single_pole`: **ANCHOR → DERIVED**, consuming `fast_mode_content`, with a
  runnable check (`s ≥ 1` from the DOS). It renders as a SPLIT (mechanism derived, premise
  anchored) — the honest structure: the *theorem* is derived, the *premise* (what the fast modes
  are) is the visible anchor.

The old `curved_bath.py` keeps its wrong conclusion under a `CORRECTED BY EXTERNAL REVIEW` banner
— the error stays on the record, not rewritten. (`v4/targets/fast_mode_dos.py` = Target 1D.)

**Honest residual / de-graduate condition:** this rests on the fast modes being standard
relativistic content. An exotic non-relativistic or IR-enhanced substrate could drop `s<1` — but
that contradicts the masslessness the framework commits to. And I have *not* claimed the full
finite-T interacting `J(ω)`; I've shown `s≥1` at the DOS / phase-space level and the Kubo boundary.
That gap is a question for you (below).

---

## 3. Q2 — confirmed sound; banked unchanged

No change. The Δ₄ ~ □² propagator factorizing into a healthy pole and a negative-residue ghost,
routed through Q as `Im χ < 0`, is the cleanest leg, and the conformalon is correctly the single
live escape (contested, not refuted). Your endorsement is banked as-is.

---

## 4. Q3 — accepted; the "one prohibition" unification was over-tight

You're right, and §2.2 contains the reason I missed it. The real slow threat is a sub-Ohmic
**continuum** (a branch cut), not a discrete pole — and Q ("no new propagating pole") does **not**
forbid a branch cut, because the continuum is the same vacuum modes with a softer IR edge, not a
new degree of freedom. So:

- **α leg:** a propagating-mode question. Q genuinely bites. The unification is real here.
- **single-pole leg:** a DOS-edge question. Q is orthogonal to it — it neither blocks nor
  completes the derivation. (And per §2 the derivation is now done by the DOS, not by Q.)

I've downgraded §4 from "emergent unification protecting both anchors" to **"Q-protection is real
for α only; single-pole was a separate DOS-edge question, now derived."** Noted in passing, since
you flagged it: the unification was the most aesthetically pleasing result in the arc, the one that
"just fell out" — and it got the least scrutiny instead of the most. That's on the method, and the
gate now records the correction.

---

## 5. Q4 — confirmed; banked unchanged

No change. `a` and `c` are the physical `E₄`/`Weyl²` coefficients, scheme-independent; the
conformal scalar `(1/360, 1/120) → 1/3`, and reproducing Weyl `11/18` and vector `31/18` from the
same Gilkey extraction is a validation, not a tune. The S⁴ `W²=0` caveat stands, and the risk is
correctly placed in the antecedent, which §3.2/Q2 handles.

---

## 6. Where the foundation stands now

> *(⚠ This is the round-1 table. The single-pole row below — "DERIVED, super-Ohmic theorem" — was
> itself corrected in round 2: see §R2 at the top. Current tier is **PENDING-REVIEW**.)*

| Parameter | Before | After this review |
|---|---|---|
| single-pole | ANCHOR (s "free") | **DERIVED** — super-Ohmic theorem from the committed massless DOS |
| α = 1/3 | ANCHOR, Q-protected | **ANCHOR, Q-protected** (confirmed); de-anchor = the conformalon |
| "one prohibition, two anchors" (§4) | emergent unification | **over-tight** — Q-protection real for α only |
| §6 / §2 | in tension | **consistent** (both super-Ohmic) |

Gate: 14 claims, 0 violations. Tests: 46 passed. The headline result is no longer "two
Q-protected anchors"; it is **one Q-protected anchor (α, with the conformalon as its sole live
de-anchor route) and one super-Ohmic theorem (single-pole)** — exactly your "one graduates, the
symmetry was over-tight."

---

## 7. Four questions back to you (using you twice, as intended)

1. **The exponent, rigorously.** I have `s ≥ 1` at the DOS / two-quantum-phase-space level and the
   Kubo `s=1` boundary. Does `s ≥ 1` survive the *full finite-T interacting* `⟨T_TT T_TT⟩(ω, k→0)`
   for GRUT's actual content, or is there a low-`ω` transport subtlety (a `δ(ω)` for the free gas,
   a hydrodynamic peak) that I'm gliding over? Is `s=1` (Ohmic) or `s≥2` (super-Ohmic) the right
   reading, and does it matter past the single-pole verdict?
2. **The commitment.** Is `fast_mode_content` ("standard massless relativistic field modes") the
   correct reading of "massless + 1/r + relativistic CTP," or is there a substrate subtlety where
   the Mori–Zwanzig fast modes are *not* the free relativistic modes?
3. **The plateau.** Is the 689 Hz observable's (in)sensitivity to the `ω→0` edge still worth
   showing for its own sake, or is it moot now that `s ≥ 1` is consistent across §2 and §6?
4. **The new shape.** With single-pole a theorem and only α anchored, is "one Q-protected anchor +
   the conformalon de-anchor route" the right characterization of GRUT's remaining freedom — or
   does graduating single-pole expose a downstream claim that was leaning on its anchored status?

---

## 8. Reproducibility (new since v1)

```
python -m v4.targets.fast_mode_dos     # Target 1D — s from the committed massless DOS (s≥1)
python -m v4.ci_check                   # gate: 14 claims, single_pole now DERIVED
python -m pytest v4/tests               # 46 tests (incl. the graduation + escape-closed checks)
python -m v4.audit                      # one-pass view: α anchored+Q-protected; single-pole derived
```

The error was real, the correction makes the foundation stronger, and it took someone outside the
loop to ask the one-line question — what does a massless field's DOS actually do — that the loop
never thought to. That's the review working. Thank you; round two above.
