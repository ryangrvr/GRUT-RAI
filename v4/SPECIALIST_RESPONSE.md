# Response to Specialist Review — Revision 1

### GRUT-RAI v4.1, "Two Q-Protected Anchors" → "One Q-Protected Anchor + One Super-Ohmic Theorem"

**2026-06-24** · in reply to the first external review of [WRITEUP.md](WRITEUP.md)

---

## 0. What the review did

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
