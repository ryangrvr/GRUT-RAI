# The primitive-inversion question — scoping document

> **STATUS: NOTHING BANKED. NOT A CLAIM. NOT A RESULT.**
> The register is untouched by this file. No node added, no tier moved, no `ledger_delta` changed.
> This is a scoping document for a question, written **default-BROKEN** per CHARTER §1.4, and it
> may not be cited as content by any other artifact. Before any part of it enters
> `provenance/claims.json` it requires an adversarial pre-screen (CHARTER §1.3) and an overseer
> relay (CHARTER §5.3). Opened 2026-08-19 at the owner's direction.
>
> **Scope release recorded at the outset:** the owner has stated that a ToE is *not* required and
> that the EFT lane is an acceptable terminus. This document is therefore written so that a
> negative outcome is a *result*, not a loss — see §7 and §10. That release is deliberate: it
> removes the directional-optimism pressure CHARTER §1.4 names as the program's worst failure mode,
> on the one question most exposed to it.

---

## 1. The question

> **Can `(observable algebra, state)` sit BELOW `rung1_inin_action` as the primitive — such that
> the time-translation flow, the system/bath split, and the KMS condition are CONSEQUENCES rather
> than inputs?**

Stated as a question, held default-BROKEN, in both directions. "Yes" is not to be pre-answered; per
`u3_split_origin`'s standing fence, neither is "no."

## 2. Why this, why now

Two independent facts, neither of which was arranged:

1. **`background_time_translation_flow` was booked as an input on 2026-08-18 (+1).** Its own
   `tier_note` performs the atomisation and concludes: part (b), the state's invariance under the
   flow, *"is ALREADY BOOKED: it is inside rung2's KMS content (a KMS state is invariant under the
   modular flow it is defined against)."* The register wrote "modular flow" into the justification
   for booking the input that a modular flow would supply. The framing held it as an assumption
   because the primitive sits downstream of it — which is the whole of the observation this
   document exists to test.

2. **`calc/static_patch_tt_response.py` migrated the computation to the de Sitter static patch on
   2026-08-19.** The static patch is the one arena in this program's reach where the identification
   of the modular flow with a *geometric* time flow is a candidate theorem rather than a
   hypothesis (§4.3). The migration was made for unrelated rung3 reasons.

## 3. What it would discharge, if it worked — stated at honest strength

| Currently paid | What the inversion would have to EXHIBIT to discharge it |
|---|---|
| `background_time_translation_flow`, `assumed` **+1** | that the modular automorphism group of the state supplies the one-parameter flow, AND that it is the flow the kernel actually uses (§5 — this is where it most likely breaks) |
| `rung2_kms_gate`, `shown` **−1** | that KMS is not an admission gate you impose but a property the modular flow has by construction — see the tautology hazard, §4.1 |
| `u3_split_origin`, `to-derive`, un-worked since 2026-06-29 | a criterion for WHEN a split exists, exhibited, not asserted (§4.2) |
| part of `rung1_inin_action`'s **+4** | only the split component. The Gaussian/linear-response truncation is **NOT** touched by this and stays paid in full. |

**Nothing above is claimed as discharged. The table is a specification of work, not a ledger.**
Note honestly that the arithmetic is not obviously favourable even on success: the algebraic frame
takes a state and an expectation functional as primitive — already booked in this register as
`vc_state_expectation_functional`, and already flagged there as *the first confirmed cross-cluster
shared input*. The inversion trades a list for a shorter list; whether it is actually shorter is
itself one of the things to be computed, not assumed.

## 4. The three theorems that would have to do the work

> **ALL THREE ARE UNVERIFIED IN THIS REGISTER.** `provenance/sources.json` contains essentially
> none of the algebraic-QFT literature (`tomita|takesaki|bisognano|sewell|connes` returns one hit
> across the whole register, inside `info_i2`'s prose). The citations below are from recall and are
> exactly the class of detail CHARTER §2 requires checking against the actual papers before use.
> **Verify first; nothing here is a source until it has been.**

### 4.1 Tomita–Takesaki → the flow, and the tautology hazard
*Takesaki, Springer LNM 128 (1970) — VERIFY.* From a von Neumann algebra and a faithful normal
state, a canonical one-parameter modular automorphism group follows, and the state is KMS with
respect to it.

**The hazard, named up front because it is the obvious refutation and it is a good one:** this is
*automatic*. Every faithful normal state is KMS at β=1 against its own modular flow. So "KMS
emerges" is true and, by itself, **physically empty**. It buys nothing unless the modular flow can
be identified with the *physical, geometric* time translation. That identification is the entire
question, and it is what §4.3 is about. Any version of this argument that stops at 4.1 and declares
rung2 discharged has laundered a tautology into a result, and should be killed on sight.

### 4.2 Takesaki's conditional-expectation theorem → the split criterion (this is `u3`)
*Takesaki, J. Funct. Anal. 9 (1972) 306 — VERIFY.* A normal conditional expectation onto a
subalgebra exists **iff** the subalgebra is globally invariant under the modular group.

This is the most interesting item in the document, because it speaks directly to `u3`'s statement —
*why is there a system/bath split at all?* — with a criterion and an explicit failure condition:
subalgebras not invariant under the modular flow admit no conditional expectation, hence no clean
coarse-graining, hence **no influence functional at all**. That is a candidate answer of exactly the
shape `u3`'s fence demands: falsifiable, with a named failure state, graduating only on exhibition.

Compounding fact, also unverified: local QFT algebras are type III₁, which admit **no tensor
factorisation and no density matrix**. Taken at face value this says the split `rung1` presupposes
does not literally exist in the algebra, and "trace out the bath" is a type-II/type-I idiom used
outside its domain. A live literature thread (*Chandrasekaran–Longo–Penington–Witten, "An Algebra
of Observables for de Sitter Space", arXiv:2206.10780 — VERIFY*) reports that including an observer
converts the de Sitter algebra to type II₁, which does have a trace. If that holds up, the split
becomes available exactly when an observer is included — on this program's own arena.

**Fence compliance:** none of the above banks "emergent." It specifies what an exhibited derivation
would have to look like. `u3_split_origin`'s `sub_status` fence is respected and remains in force.

### 4.3 Bisognano–Wichmann / Sewell → geometric = modular, and this is the crux
*Bisognano–Wichmann, J. Math. Phys. 16 (1975) 985 and 17 (1976) 303; Sewell, Ann. Phys. 141 (1982)
201 — VERIFY BOTH.* For the vacuum restricted to a Rindler wedge the modular flow **is** the boost;
Sewell extends the argument to horizon-bounded regions, giving the Gibbons–Hawking temperature
algebraically.

Where a theorem of this class applies, the flow is genuinely derived and §4.1's tautology hazard is
defused. Where it does not, the identification is the Connes–Rovelli thermal-time **hypothesis**
(*Class. Quantum Grav. 11 (1994) 2899 — VERIFY*), which replaces `background_time_translation_flow`
one-for-one with a differently-named assumption. **No ledger gain. Relabeling.** CHARTER §4's
"fiat exclusion" entry is the closest existing name for that failure.

## 5. The predicted failure point — written before the work, so it cannot be discovered late

**Flow mismatch.** The geometric modular flow of the de Sitter static patch is the static patch's
Killing flow: horizon-bounded and observer-dependent. GRUT's kernel is written in cosmological
slicing at (ω, k) on an FRW background. In flat slicing de Sitter has **no global timelike Killing
vector** — a(t) = e^{Ht}. That absence is plausibly the very reason
`background_time_translation_flow` had to be booked as an assumption in the first place.

So the flow that is geometric by theorem and the flow the kernel actually uses are, on the face of
it, **different flows**. If they cannot be connected, the inversion fails exactly here, and it fails
for a reason that is already this program's known hard problem: de Sitter observer-dependence, the
same one driving the rung3 IR controversy.

**Standing prediction: this is where it breaks.** Recorded now so that a later "we found a
subtlety" is a confirmation of the pre-registered failure mode and not a fresh discovery.

## 6. Pre-registered kill conditions

The question is **REFUTED** if any one of these lands:

- **K1 — the tautology.** The KMS discharge rests only on §4.1 with no geometric identification.
  Empty; kill.
- **K2 — flow mismatch unbridgeable (§5).** Static-patch Killing flow cannot be connected to the
  cosmological-slicing flow the kernel uses. Kill.
- **K3 — one-for-one relabel.** Every import discharged is replaced by an algebraic assumption of
  equal or greater cost. Net ledger does not move. Kill — and this outcome is the *most likely* one
  after K2.
- **K4 — no conditional expectation, no repair.** §4.2's criterion fails for the relevant
  subalgebra with no observer/crossed-product repair. Then the split is not derived AND `rung1` is
  additionally in trouble. Kill — and note this kills more than the inversion.
- **K5 — recovers nothing downstream.** Even on success, if `S_IF` is not recovered as a limit,
  the frame is not an inversion of GRUT; it is a different theory wearing the name. CHARTER §4,
  "fiat exclusion," applies.

**Success requires an exhibited derivation, in either direction.** A screen returning "looks
promising" banks nothing. Per `u3`'s fence, so does a screen returning "looks emergent."

## 7. What this does NOT do — stated up front, not discovered later

It does not derive **α = 1/3** (heat-kernel / field content — `info_i2`'s structural reason stands
and is not disturbed by this document). It does not derive **Λ**, the **SM spectrum**, or the
**Born rule** — the algebraic frame takes states as primitive, which is its own price, honestly a
*relocation* of the Born question rather than an answer to it. It does not produce a novel
observable, and **it must not be sold as making GRUT a ToE.** The most it can do is shorten and
relocate the input list. That is the program's own stated win condition, and it is a smaller thing
than the word "inversion" suggests.

## 8. Why the two prior declines do not dispose of this

- **`info_i2` (2026-06-28)** — "Modular theory = Tomita-Takesaki = KMS = rung2." Screened as a
  candidate **differentiator**: does it yield beyond-standard falsifiable content, does it derive α?
  Answer: no, correctly, and the monotonicity-vs-value argument is sound. That screen did not ask
  whether the structure sits *below* rung1 and discharges inputs. Note the equation is direction-free:
  read downstream it says "no new content"; read upstream it says "rung2 is not an independent
  input." The screen recorded only the first reading.
- **`SPECIALIST_BRIEF_rung3_spine.md:114` (2026-08-09)** — an algebraic-QFT reader found the
  observable unspecified for want of static-patch/Killing-time vocabulary; ruled a convention
  mismatch, and for a dispatch brief that ruling is defensible. It is a ruling about **legibility to
  a recipient**, not about the frame's standing as a primitive.

Both declines were locally correct. Neither adjudicates §1. Recording this pattern is not a
criticism of either ruling — it is the observation that a node-by-node audit cannot see a question
that was never any one node's.

## 9. RETRACTED 2026-08-20 — the Matsubara coincidence was numerology

*This section originally offered a "same-day checkable": that `static_patch_tt_response.py`'s
c = 0 pole set at omega = -i m H coincides with the Matsubara ladder of the Gibbons-Hawking
temperature T = H/2pi, and that if real it would mean result (D) reads a **thermal** structure of
the state as a **bath-structural** one — with the flattering gloss that this would be "a direct
fingerprint of the modular flow in an object this program computed for unrelated reasons."*

**It was tested and it is refuted.** It fails on four elementary counts before reaching the
Euclidean-vs-retarded objection that was flagged here in advance:

1. **Support.** Rungs m = 0, 1, 2 have no candidate at any physical multipole l >= 2. The candidate
   set is a proper subset of the ladder; the sets are not equal. (The register reached the same
   arithmetic from the opposite direction — "rungs 1 and 2 die for every physical multipole",
   commit `deacfb9`.)
2. **Sign.** coth is odd, so the ladder is symmetric under m -> -m. The candidate set is
   lower-half-plane only.
3. **Multiplicity.** The ladder has uniform simple poles at constant residue 2T = H/pi. The
   candidate set carries degeneracy growing as m - 2.
4. **Cause.** The integer bracket holds iff sqrt(1-4c) is an odd integer — c-SELECTIVE — while
   beta = 2pi/H is c-independent. A thermal cause cannot be c-selective, so the temperature is not
   what puts the set on the integers.

**Then the flagged objection, which is fatal on its own.** Matsubara frequencies are the discrete
sampling points at which the Euclidean correlator is defined; G_E has no poles there. What
genuinely has poles at omega = i m H is the KMS weight coth(beta*omega/2) — a property of THE
STATE, present for every J and every regulator. A retarded pole is a property of THE DYNAMICS and
must lie in the lower half plane by causality. Different objects. Had the coincidence held it would
have produced an order-2 pole in the symmetrised noise kernel at every shared rung — a pathology,
not a fingerprint.

**What is real underneath, and it is the opposite of the conjecture.** At c = 0 the free response's
special points on the imaginary axis partition exactly at m = l: the response has **zeros** where
the ladder has rungs (cancelling them for |m| <= l), and where the conjecture placed poles the
response is pole-free and what sits there is coth's pole — the state, not the graviton.

**Process note, which is the part worth keeping.** This section named both blockers correctly,
cited CHARTER §4's "match temptation" against itself, and held the claim at conjecture-grade. That
worked: the caveat was the thing that got it tested rather than banked. But the section ALSO wrote
the flattering reading beside the caveat, and the flattering reading was wrong on five independent
counts. The lesson is not "the caveat saved it" — it is that a caveat is not a licence to state the
attractive version at all. **Nothing here graduates; §1 is untouched by this retraction, which was
always separable from it.**

## 10. Cost, and what survives a negative result

**Not a demolition.** On success, Vol 2 survives as a *limit*: `S_IF` becomes what modular structure
looks like once a split is chosen and the expansion is truncated to quadratic order. The no-go
ledger survives untouched. The arrow existence/direction decomposition survives and sharpens —
"direction is state-dependent" is what modular theory says, because the flow *is* the state.

**On a negative result** — the more likely outcome, per §5 and K3 — the program has an exhibited
statement of *why* the influence-functional primitive cannot be pushed below its own presuppositions,
which is a real answer to `u3` in the "fundamental" direction and a genuine addition to the no-go
ledger. Under the owner's scope release (§0) that terminus is acceptable, the EFT lane is unaffected,
and `calc/gw_tensor_friction.py` remains the near-term deliverable either way.

## 11. Before anything here banks

1. Verify every citation in §4 against the actual papers; add to `sources.json` only what verifies.
2. Adversarial pre-screen, panel charged to break it, defaulting to broken (CHARTER §1.3), with K1–K5
   as the explicit targets and **K3 as the presumed outcome**.
3. Relay to the overseer before any register edit (CHARTER §5.3).
4. `u3_split_origin`'s fence stays in force throughout. This document pre-answers nothing.

**Anti-scope-creep clause.** This question gets one bounded attempt with a written verdict. It does
not get a wave apparatus, a screening tier, a vocabulary ruling, or a sub-register. If it needs
those to survive, it has already failed §1.
