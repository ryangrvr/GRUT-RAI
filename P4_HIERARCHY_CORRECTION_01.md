# CORRECTION 01 to the P-4 record: the descriptiveness attack (record integrity; no rerun)

**Date:** 2026-09-29 · **Authority:** owner ruling on the forest synthesis
(`LEVEL0_FOREST_SYNTHESIS_OWNER_RULING_01.md` §3: "REQUIRED … No rerun and no main-status
change are authorized") · **Found by:** the forest audit (`LEVEL0_FOREST_SYNTHESIS_01.md` §1.1,
row 3) · **House rule:** create a correction artifact rather than silently changing the old
result.

**Preserved, byte-for-byte:**
- the instrument `calc/p4_hierarchy.py`;
- the artifact `P4_HIERARCHY_RESULT.json` (sha `58fc0b65…`);
- the charter `P4_HIERARCHY_CHARTER_01.md` (frozen `d0fc014`);
- the verdict body `P4_HIERARCHY_VERDICT_01.md` (only a pointer to this note is appended).

## What is corrected

The verdict's section **"THE DESCRIPTIVENESS ATTACK (owner point 7)"** states: "No
constraint-satisfying pair with an influence-untracked physics difference was constructible."
That reads as the outcome of an executed adversarial search. **It was not one.**

**The mechanics.** In `calc/p4_hierarchy.py` the conclusion is entered at line 251 as

```
check(True, "DESCRIPTIVENESS ATTACK: no constraint-satisfying pair with an influence-untracked "
            "physics difference was constructible -- …", "note")
```

- The first argument is the literal `True`, and the kind is `"note"`.
- The instrument's own `check` never fails a `"note"`.
- The same holds for the two composite lines beside it (lines 240 and 246) and for the post-hoc
  diagnostic note at line 193. That note appends the same sentence to a real ratio test (the
  ratio test itself is genuine).
- The artifact records these as `"kind": "note"` entries.

**What the frozen charter asked for** (`P4_HIERARCHY_CHARTER_01.md` §3):
- An in-access counterexample "requires two states with identical full hierarchies and
  different reduced dynamics".
- The instrument was to attack this "constructively … pushed to higher-order matching in a
  declared attempt".

**What the instrument actually did:**
- It built the ladder pairs, matched through orders 2, 4 and 6 with their first differences at
  orders 4, 6 and 8.
- It checked that each residual difference scales with the first unmatched order.
- **It did not construct, and did not search for, a non-trivial pair with *matched full
  hierarchies* and an influence-untracked difference in physics.**
- The only full-matching pairs on the record are trivial: the permutation relabel `dperm`
  (line 164), and P-3's Q5 representation control (itself D-1 extended).

## What stands, untouched

- **The complete positive-definite hierarchy characterization** (CHARACTERIZED-AND-REDUCIBLE:
  state positivity on the generated *-algebra; the P-2 cone as its two-point face).
- **The cumulant ladder**:
  - the λ-scaling results at orders 4, 6 and 8;
  - the **order-8 frozen gate FAILED and stays red**;
  - the labeled post-hoc asymptotic diagnostic (325 → 320 → 276, trending toward 256) explains
    the red but does not erase it.
- **The finite-matching results:** finite matching never certifies.
- **The accepted standing** (`P5_ACCESS_CHARTER_01.md:4-12`):
  - 𝔠_full is a CANDIDATE interface characterization, complete only within the declared finite
    bounded-access class;
  - the hierarchy/Gram condition is **NULL-AS-NEW-PRINCIPLE**;
  - "access is the last place a new principle could hide" is not a theorem.

## What must change in citation

- **"DESCRIPTIVENESS ATTACK REPELLED"** (and the verdict sentence above) **must not be cited as
  an executed test.**
- **Interface-completeness at the declared scope rests on:**
  1. the class construction: in the finite class, the reduced probe dynamics is a functional of
     the contour-ordered influence functional *by construction* (Feynman–Vernon at operator
     level; charter §3);
  2. the mathematical characterization above;
  3. inherited matching controls (P-3 Q5).
- **It does not rest on a successful adversarial descriptiveness search.** None was run.
- The accurate wording of the ladder evidence: **every residual difference *found on the
  constructed ladder pairs* tracked the first unmatched cumulant order.** This is a statement
  about the pairs built, not about the space of constraint-satisfying pairs.

## What this note does not do

It does not rerun P-4. It does not change P-4's main status. It does not reopen the P-5
acceptance. It does not assert that an untracked pair exists; that question simply stays
**unsearched.**
