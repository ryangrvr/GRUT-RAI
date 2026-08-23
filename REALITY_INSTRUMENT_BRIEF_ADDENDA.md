# Instrument-layer brief — addenda

*The owner's builder brief (2026-08-23) is authoritative and carried in full. Five additions,
each for a failure this program has already committed at least once.*

## [A-1] The parallel track needs the interleave contract, or its proviso is unenforceable

The owner's roadmap change: run Rung-3/Class-C physics in parallel once C1 is clean, *"provided
quarantined results never become hidden priors."* Correct concern, no mechanism — and an unstated
prior is by construction invisible to the person holding it.

**Reuse the contract that already exists** (`AGENT_COORDINATION.md`, 2026-08-22, written for
`gw_tensor_friction.py`):

> The physics track MUST record every quarantined or unbanked result it consumes in ONE named block
> at the top of the file, with provenance. Nothing may be used that is not listed there.

Consequence, stated so it is not discovered late: if a quarantined result is later corrected or
withdrawn, the impact is a **one-line recomputation from the declared block**, never a
re-derivation. A quarantined result consumed without being declared couples the tracks invisibly —
which is the whole failure the proviso is trying to prevent.

**The audit layer feeds the physics track only through declared blocks. The physics track feeds
the audit layer only through banked results. Neither reads the other's drafts.**

## [A-2] The prose extractor's dominant failure is FALSE POSITIVES, and the program has already hit it

Not listed in the brief, and it is the risk most likely to inflate the headline.

1. **Substring collision.** `rung3` matches `rung3_single_pole`, `rung3_spectral_structure`,
   `rung3_w2`… The V1 digest already flagged this against itself: *"substring matching inflates the
   56."* **Match full ids on word boundaries; emit the substring-collision count as its own number.**
2. **Retraction blindness.** The corpus contains RETRACTED and QUARANTINED passages. A reference
   inside a retracted section is **not a live dependency.** The extractor must be retraction-aware:
   detect enclosing RETRACTED / QUARANTINED / SUPERSEDED / historical-note markers and tag those
   edges `INACTIVE`, counted separately and **excluded from blast radius by default.**
3. **Negation and contrast already have types** in the brief — good. Add that a NEGATION edge must
   never contribute to blast radius, since "X does not depend on Y" is the opposite of a dependency.

**Report precision honestly:** hand-check a random sample of extracted edges and publish the
false-positive rate. An extractor whose error rate is unmeasured cannot support a load-bearing map.

## [A-3] Plant-and-recover: the plant must be PLAUSIBLE, not obviously wrong

The requirement is right and it is the single most valuable item in the brief. One refinement, or
it can be satisfied trivially.

A runner that detects a planted rival **because the plant is absurd** (a sign flip making a positive
quantity negative, or a value of zero) has demonstrated nothing. **The plant must be close enough to
the incumbent that only the actual physics separates them.**

**The model is the real historical case.** For the axial coefficient the rival was `6l-8` — it
matched the incumbent `l(l+1)-2` at l=2 and l=3 and diverged only at l=4. Someone could have
believed it. The successful runner recovered every planted value including the rival, which is what
made `18` a measurement rather than a confirmation.

**So: plant the actual rival where history supplies one, and otherwise plant the nearest defensible
alternative. Report the plant's distance from the incumbent** — a runner that only rejects distant
plants should be recorded as weak, not as passing.

## [A-4] Record WHY the three measured constants are excluded, so they cannot drift back

`GRUT_MINIMUM_CORE.md` must state, on its face, that `vc_rho_lambda`, `vc_v_ew` and `vc_m_planck`
are **excluded as measured data every candidate theory must reproduce, not GRUT-specific content.**

This is the same category error the charter already fixed once, for Λ: *"an observed value is a
datum every candidate theory must reproduce, not a discretionary posit… Listing it here
over-reported the count of droppable inputs by one."* It was found by pointing the instrument at
foreign physics, and it recurred here inside the minimum-core count. **A correction that is not
written down where the number lives will be made again.**

## [A-5] `rung3_single_pole` is not demoted — it is correctly located, and it stays the flagship

The brief instructs that rung3 must not be counted as surviving UN-ASSUME of the R1 ontology.
Correct. **State the reason alongside it, or a reader of the minimum core will conclude rung3 is
dead.** It is not. It is **conditional on the ontology** — which is precisely the commitment the
Class-C calculation exists to test.

That is why the two tracks converge rather than compete:

| | says |
|---|---|
| the reality audit | rung3 carries GRUT's distinctive novelty and is conditional on an un-derived stance |
| the Class-C program | rung3 is the decisive physics calculation |

**Two independent routes, one target.** That is not evidence rung3 is true. It is evidence the
program has correctly localised its own novelty — and it is the reason the minimum core (three
nodes, two of them negative or open) and the flagship physics test are complementary rather than
contradictory.

**The core scientific question, stated plainly and unchanged:**

> **Does the gravitational vacuum actually generate the finite-memory / single-pole structure that
> GRUT assumes?**

Note what already bears on it: the class-A pair is **adverse at proxy scope** (a horizon-forced
white floor is zero memory; the TT channel is non-stationary), and both results fence themselves as
not a verdict on Class C. That evidence is fenced, unbanked, and must be **declared** by the physics
track under [A-1] rather than absorbed.
