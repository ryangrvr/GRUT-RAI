# Reality audit V2 — correction to the split-reach headline

> **Supersedes the V2 headline.** `REALITY_AUDIT_V2_RESULTS.md` is left untouched — it is the record
> of what the audit concluded, and this is a separate citing file per the program's pre-registration
> discipline. **NOTHING BANKED**; `claims.json` untouched; `validate.py` PASS.
>
> **The corrected finding is materially more important than the one it replaces, and it points the
> opposite way.**

## 1. What was reported, and why it was wrong

**Reported:** *"Zero of rung1's 27 dependents reference the ontology. All 27 reference only the
formalism… the stance is nearly free."*

**The methodological error, stated once:**

    Schwinger-Keldysh / Feynman-Vernon formalism  !=  finite-memory / single-pole ontology

The formalism supplies the *language* of K_R and N. It does **not** supply the GRUT claim that the
gravitational vacuum has finite memory, still less that the memory is **single-pole**. The V2 pass
classified `single-pole`, `relaxing`, `memory` and `responsive-medium` as generic SK terminology.
They are not. They are the ontology's content, and `GRUT_ToE.md` §1.2 says so explicitly when it
lists among S_IF's own axioms:

> *"Locality / finite memory -- the influence functional is local with a finite memory kernel
> (**single-pole, the one novel structural commitment**)."*

`CHARTER.md` §2 carries the same. **The one thing the program calls its novel structural commitment
was counted as borrowed vocabulary.**

## 2. The corrected split-reach

Re-run with `single-pole`, `finite-memory`, `short memory`, `memory kernel`, `memory time`,
`responsive-medium`, `responsive-vacuum`, `relaxing`, `relaxor`, `two-scale` treated as **ontology**
terms (hyphen- and space-tolerant), and `dissipat*` held separately because K_R *is* literally the
dissipation kernel and the word is genuinely shared:

| class | count of 27 |
|---|---|
| **ONTOLOGY-DEPENDENT** | **6** |
| AMBIGUOUS (`dissipat` only -- may be formalism) | 4 |
| formalism-only / neither | 17 |
| **upper bound if every ambiguous case is ontology** | **10 of 27 (37%)** |

**The six, with the matching term in their own statement text:**

| node | term | statement fragment |
|---|---|---|
| `rung3_single_pole` | single-pole | *"WITHIN the collisional/analytic-bath class… single-pole"* |
| `rung7_wz` | relaxing, two-scale | *"a **relaxing** chi(omega) yields an effective dark-energy equation of state w(z)"* |
| `rung7_w2_wa_sign` | single-pole | *"for the passive, causal, KMS-consistent **SINGLE-POLE** vacuum"* |
| `rung7_w3_nocrossing_export` | single-pole | consequence of W2's no-crossing |
| `rung7_w1_wz_map` | relaxing | *"a **relaxing** causal susceptibility chi(omega) defines an effective dark-energy stress tensor"* |
| `u1_form_universality` | responsive-medium | *"the **responsive-medium** influence-functional FORM"* |

*Method disclosure, recorded because it is the same defect class this audit exists to catch: the
first re-run of this test used a space-only pattern and **missed the hyphenated `responsive-medium`**,
returning 5 rather than 6. Caught by inspecting the miss rather than by the count looking wrong.*

## 3. The dependency chain the correction exposes

    borrowed formal machinery        Schwinger-Keldysh · Feynman-Vernon · K_R · N
              |
              v
    GRUT-SPECIFIC ONTOLOGICAL COMMITMENT
              |                       responsive vacuum · finite memory
              |                       · single-pole relaxation structure
              v
          rung3_single_pole          (the one novel structural commitment)
              |
              v
          rung7 family               (w1 / w2 / w3 / wz)
              |
              v
       cosmological exports

## 4. Meaningful-versus-collapse — which downstream claims survive without the ontology

Per the owner's added test: if the finite-memory/single-pole ontology is declined, which dependents
remain **mathematically meaningful but lose their physical interpretation**, and which **collapse**?

| node | without the ontology | why |
|---|---|---|
| `rung3_single_pole` | **COLLAPSES as a GRUT claim** | its INPUTS survive as mathematics (DOS ~ ω², J ~ ω³ super-Ohmic are calculations), but `single-pole` is the CONCLUSION and the conclusion *is* the ontology |
| `rung7_w2_wa_sign` | **COLLAPSES** | the single-pole vacuum is its subject; remove it and the claim has nothing to be about |
| `rung7_w3_nocrossing_export` | **COLLAPSES** | consequence of W2 |
| `rung7_wz` | **SURVIVES AS MATHEMATICS, loses GRUT status** | the susceptibility → w(z) map is a valid EFT construction; without the relaxation commitment it is a conditional phenomenological construction, not a GRUT prediction |
| `rung7_w1_wz_map` | **SURVIVES** | its own statement already says *"GENERIC -- not uniquely GRUT"* |
| `u1_form_universality` | **SURVIVES** | already labelled *"GENERIC/BORROWED"*; it claims the FORM is universal, not that the vacuum realises it |

**Three collapse; one survives as mathematics without GRUT status; two were already marked generic.**
And the three that collapse are the single-pole family.

## 5. The corrected finding

**Not** *"the stance is nearly free."* The precise statement, and it is stronger in both directions:

> **GRUT's distinctive physics is concentrated in a small number of ontological claims — and those
> claims carry the downstream novelty while remaining un-derived.**

The borrowed formalism carries the bulk of the register (17 of 27 formalism-only, plus 4 ambiguous).
The un-derived stance carries `rung3` and the `rung7` family — i.e. **everything that is
distinctively GRUT rather than borrowed open-system EFT.**

**This is not a reason to hide the stance. It is the reason to make it the centre of the theory.**
It tells a physicist exactly where to look: the controversial content is not the open-system
formalism — that is standard — but the physical assertion that the gravitational vacuum *realises*
the specific finite-memory, single-pole responsive-medium structure. That assertion is the program's
novelty and its weakest-supported claim, and those are the same claim.

**Do not flatten this to "GRUT is unsupported."** The architecture is now precisely located, which is
what an audit is for.

## 6. Consequences for the rung1 split

`REALITY_AUDIT_V2_BRIEF.md` ADDED-E asked whether the 27 hang off **R1-FORMALISM** or
**R1-ONTOLOGY**. Answer: **17 formalism-only, 6 ontology-dependent, 4 ambiguous** — but the six are
the GRUT-specific ones. So the split is not merely bookkeeping: it **separates the borrowed bulk from
the novel core**, and after the split the two halves should be tiered differently, since R1-FORMALISM
is genuinely `shown` (Schwinger 1961, Keldysh 1964, Feynman-Vernon 1963, Calzetta-Hu) and
R1-ONTOLOGY is a stance the node's own `ledger_note` already calls *"STANCE, not derivation."*

**The Δ4 allocation is NOT proposed here**, per ADDED-E: which half carries the price is a register
decision with ledger consequences, and a split arriving with a price attached is a ledger edit
wearing an analysis's clothes.

## 7. Standing

Twelfth defect in this stretch; **still zero physics errors.** This one is a classification error in
the audit — treating the program's own novel commitment as borrowed vocabulary — and it inverted the
headline. Caught by testing the single node most likely to break the claim rather than by re-reading
the reasoning, consistent with every prior instance.

**The V1/V2 results that stand:** rung1 HOLDS-NARROWER with the SPLIT owed · the chain at 28 of 71 ·
zero DOES-NOT-HOLD · 65 UNRESOLVED-BLOCKED upheld · use-vs-cite 18 USE / 10 CITE-ONLY.
