# L0 STRUCTURAL DIAGNOSTIC 01 — EVALUATION 01 (REV-0; read-only)

**Status: EVALUATION COMPLETE. The mechanical result is proposed for owner adjudication. HARD STOP.**
- **Authority:** `S3_OWNER_RULING_01.md` §§11-14 (Issue #2 comment `5909891161`).
- **Criteria:** `L0_STRUCTURAL_DIAGNOSTIC_REVERSAL_01.md` §3, **frozen 2026-09-29 and applied without
  reinterpretation.**
- **No new definitions and no new outcome labels.** There is no physics, no v4 exception and no
  pre-registration, because the criteria were already frozen.
- **Date:** 2026-09-30 · **Branch:** `master-w25bu9`.

## 0. Method

- **Audit A:** the Level-0 floor rulings (L0-1a … L0-1h, O-7, the registry, the deposit), the forest
  synthesis, EA-0, the access bridge, and lift selection with the post-floor deposit.
- **Audit B:** SF-0, SF-1, SFG-0, S5, S2, S2-HB and S3.
- **One independent adversarial verifier.** It was tasked to **find** a qualifying edge, cycle or
  self-duality, and to report as SURVIVES any candidate that plausibly met the literal rule.
  - It read every in-scope ruling in full: L0_1A, 1B, 1C, 1D, 1E ×2, 1F, 1G ×2, 1H ×3, REGISTRY, O7,
    FOREST, EA0 ×2, ACCESS_BRIDGE ×2, LIFT_SELECTION ×2, SF0, SF1 ×2, SFG0, S5 ×3, S2 ×3, S2_HB ×2
    and S3.
  - It also ran a keyword grep over them for constructs / implies / ⇒ / input / feeds / selects /
    required as.
- **Read-only.** Nothing was run.

**Scope.** "Level-0 / post-floor" means the Level-0 direction onward, through S3-0.

**Excluded, and checked anyway (none creates a qualifying edge on a Level-0 node):**
- the pre-Level-0 rulings, dated 2026-09-25 … 28: RELATIONAL_ONTOLOGY, D1_P2, GR1_CP1, P2_S1, P3_P4,
  EQ1_S41, S41_FS1, CLOCK_MISMATCH, KERNEL_TRANSPORT, A6, GR2*, V4*;
- PI0_TRACE_CHANNEL (the gravity branch).

Within those, the relational hierarchy is "candidate, not banked", and D1_P2 §3 is an interpretive
"working map". GR1_CP1:39's open arrow is answered at GR2C:38 as a non-implication.

## R-1. Certified edges

### Ingredient → property

**Carrying the literal frozen certification words:**

| # | Edge | Word | Ruling |
|---|---|---|---|
| E1 | gap → P_memory | LOAD-BEARING | `L0_1A_OWNER_RULING_01.md:11,15-16` |
| E2 | passivity → P_positivity | LOAD-BEARING | `L0_1A_OWNER_RULING_01.md:16-18` |
| E3 | locality → P_geometry | NECESSITY-CERTIFIED | `L0_1B_OWNER_RULING_01.md:17` |
| E4 | linearity → P_exact-reduction | NECESSITY-CERTIFIED **(definitional)** | `L0_1C_OWNER_RULING_01.md:17` |

**Accepted ingredient → property relations under other wording (edge status for the owner; see note
N-1):**

| # | Relation | Wording | Ruling |
|---|---|---|---|
| E2′ | accretivity → P_positivity (b), necessary not sufficient | "HOLDS at tested scope" (H2-n) | `L0_1H_OWNER_RULING_03.md:15-22` |
| E5 | cycle affinity → loss of response CM (P_positivity (c)) | ACCEPTED, L-2; "necessity direction established analytically" | `L0_1D_OWNER_RULING_01.md:15,18` (listed as certified in diagnostic §4) |
| E6 | noise placement → P^corr_CM | CLASS-SPLIT; boundary "identity-determined" | `L0_1E_OWNER_RULING_02.md:8-17` |

**Certified non-edges (⇏ / NOT-LOAD-BEARING):**
- locality ⇏ P_memory or P_positivity;
- linearity ⇏ P_memory or P_positivity;
- cycle affinity ⇏ memory;
- determinism is not load-bearing while FDT holds;
- detailed-balance status does not decide (b);
- stable ⇏ accretive ⇏ monotone.

See `L0_1_FLOOR_DEPOSIT_01.md:95-102`.

### Property → ingredient

**NONE.** 26 candidates were examined across both audits, and the verifier re-attacked the strongest.
Every one fails a frozen condition:

| # | Candidate | Verdict | Condition failed / ground |
|---|---|---|---|
| 1 | O-6: emergent dissipation → ordering | **Tested and FALSIFIED** | `L0_1G_OWNER_RULING_02.md:9-23`: emergent dissipation ≠ ordering |
| 2 | O-5 derived order / clock → P_memory's τ; lift selector D-5n | REJECTED | The order → P_memory direction is ingredient → property. The derived clock is the original parametrization (identity, DORD:161-162). "Ordering" is listed as an ingredient in frozen §3. D-5n excludes nothing and is "preserved identically" (identity). No return edge exists. |
| 3 | P_positivity (b) ⇒ accretivity (the contrapositive of E2′), closing a 2-cycle with E2′ | REJECTED | The same certificate read both ways is one logical fact (condition 3). It sits at the same level, in the n = 23 family ("another level" unmet). "Sz.-Nagy exists because K is accretive" is evaluation text, not a ruling. |
| 4 | S5: "CM chose G-D; G-D ⇒ CM" | REJECTED | The line is audit text calling it "historical circularity" (`S5_GENERATOR_ORIGIN_01.md:277`). G-D ⇒ CM is Bernstein-definitional. The owner bars feeding it backward (`S5_OWNER_RULING_01.md:83-84`). |
| 5 | EA-0: locality reused as an access premise | REJECTED | Ingredient → ingredient. "Has not derived the existence or uniqueness of the local net" (`EA0_OWNER_RULING_02.md:51-53`). Locality-from-spectrum is CRITERION-SMUGGLED. |
| 6 | P_geometry → access sets | REJECTED | Explicitly denied: geometry recovery ≠ derivation of the access sets (`L0_ACCESS_BRIDGE_OWNER_RULING_01.md:18-21`). The end-site dependence is "tautological". |
| 7 | Earned classical substrate → the lift / bridge gates | REJECTED | The substrate is a bundle of held ingredients, and the arrows sequence the gates. The content is a non-implication: earned structure ⇏ a unique physical extension. |
| 8 | Theorem 1: support → access | REJECTED | The source is an ingredient, and the result is TRIVIAL/IDENTITY ("do not count that tautological dependence"). |
| 9 | EA-0: "generator supplies sectors → state selects sector" | REJECTED | "An identity of the reach-based construction". UNFORMULABLE; EA-1 is closed. |
| 10 | Forest synthesis EA-1 / EA-3 and its selection table | REJECTED | "This is not evidence"; EA-3 is not authorized. Table rows run ingredient → property. |
| 11 | O-7 two-property hypothesis | REJECTED | O-7 = FALSIFIED; "do not repair". |
| 12 | L0-1c reading: linearity as an effective regime | REJECTED | Fenced as "*suggests* … not a certified claim". Readings create no edges. |
| 13 | SF-1: sector → law class | REJECTED | The subject is supplied state/boundary data. SFG-0 says the core has no formation variable. |
| 14 | SF-1 / SFG-0 as a generator selector | REJECTED | S-SF is "CRITERION … teleological import". |
| 15 | Dissipative core excludes the conserved charge | REJECTED | An exclusion, not a construction; auditor-graded, not a ruling. |
| 16 | Level-0 properties → the G-D generator | **REJECTED by explicit ruling** | "Cannot be fed backward as selectors" (`S5_OWNER_RULING_01.md:83-84`). |
| 17 | S5-0 | **Evidence against p → i** | "Nothing GRUT has already earned selects the kind of temporal generator" (`S5_OWNER_RULING_01.md:11-13`). |
| 18 | S5-1 derived Markov law → G-D | REJECTED | The subject is a declared parent. The law is another class; G-D stays IRREDUCIBLE/SUPPLIED. |
| 19 | S5-1 set-up → S2-HB bath ingredient | REJECTED | Tested and rejected (A-1b: P-6 fails). |
| 20 | O-6 dissipation → G-D | REJECTED | An oscillatory kernel class, not e^{−Kτ}. |
| 21 | P-2 cone → elimination of the D carrier | REJECTED | Conditional on supplied ℏ. An elimination, not a construction. |
| 22 | L-WB / L-OD as required ingredients | REJECTED | "Indicated, not established as necessary". |
| 23 | S2 discriminator → primitive noise | REJECTED | "Do not declare noise primitive"; S2-HB leaves the question open. |
| 24 | S2 curvature mechanism | Not p → i | An i → p "reading" whose necessity half is the Theorem LD / F-5 contrapositive (an identity). No certification word. |
| 25 | S3 notes R₁ / R₂ | **Barred** | Procedure R-4. Off-invariant and identity-forced. |
| 26 | The keyword sweep (verifier) | Nothing | Every subject is an ingredient, a supplied datum or a declared parent, or the sentence is a non-implication. |

**The record also carries standing disclaimers that no property → ingredient edge was created:**
- `L0_1E_APPENDIX_01.md:111`
- `L0_1H_THEOREM_01.md:132`
- `L0_1H_APPENDIX_01.md:80`
- `L0_1_FLOOR_O7_ADJUDICATION_01.md:181-183`
- `L0_1_FLOOR_DEPOSIT_01.md:132-134`
- `L0_POSTFLOOR_DEPOSIT_01.md:66-67`

## R-2. Cycles

- **Every edge (R-1) runs ingredient → property, so 𝒢 is bipartite with all edges directed one way.
  𝒢 is acyclic.**
- **Rejected cycles:**
  - the E2′ ↔ contrapositive 2-cycle (condition 3, identity; and the "another level" clause is
    unmet);
  - the S5 CM ↔ G-D loop (the backward leg is not certified and is barred; the forward leg is
    definitional).
- **R₂ is barred** by R-4.

## R-3. Self-duality

**No explicit, record-certified map exchanges two subgraphs while preserving their edges.**

| Near-miss | Why it fails |
|---|---|
| D-1 / D-1′ (DORD:66-90) | Parallel theorems, not a map. They do not preserve edges: affinity → response CM is on the ring, and placement → correlation CM is on the chain (S3-0). |
| P^corr_CM ≡ P^resp_CM under R₂ | C = T·k: FDT-type, identity-forced, off-invariant, and barred by R-4. |
| R-3 static ↔ time-domain (registry) | Maps each predicate to itself; explicitly partial. |
| KvN; bosonic vs fermionic lifts | Representational, or a non-selection result. |
| FDT | Excluded by the frozen rule. |

## R-4. S3-0 consumed

- **The crossed cell is not available at fixed invariants** (S3-0 = FORMULABLE-ONLY-WITH-CHANGE).
- **R₂'s off-invariant answer is identity-forced** (P^corr_CM ≡ P^resp_CM), so it is disqualified as
  reversal evidence.
- **R₁ is open only in an undeclared hybrid.**
- **No edge is created from either note.**
- **The response/correlation inversion that prompted the diagnostic** (diagnostic §1) therefore stays
  **confounded**. It supplies no certified edge.

## R-5. Mechanical result (frozen outcomes only)

| Frozen outcome | Holds? |
|---|---|
| Nontrivial reversal: a directed cycle with a property → ingredient edge, fully certified and non-identity | **No.** There is no property → ingredient edge and no cycle. |
| Self-duality: an explicit record-certified edge-preserving subgraph exchange, not FDT | **No.** |
| Death criterion: 𝒢 acyclic (or every cycle fails condition 2 or 3), and no qualifying self-duality | **Yes.** |

> **REV-0: the reversal/self-duality hypothesis is NOT SUPPORTED at recorded scope** (proposed,
> mechanical).
> - Per the frozen death criterion (§3), it is **closed with no re-framing and no search for an
>   alternative diagram.**
> - **This is earned, not inherited.** The later accepted campaigns were scanned (access/lift, EA-0,
>   the forest synthesis, SF/SFG, S5, S2, S2-HB, S3), and **none certified a property as
>   constructing, or being required as, an ingredient at another level.**
> - Several of them certify the opposite, notably:
>   - S5-0: no earned property selects the generator;
>   - "cannot be fed backward";
>   - "geometry recovery ≠ derivation of access";
>   - O-6: dissipation ≠ ordering.

**Scope fence.** "At recorded scope" means the record through S3-0. The result does not say a reversal
is impossible in principle. It says the earned record, which has so far only **deleted** or
**supplied** ingredients, contains none. Diagnostic §4 already noted that a property → ingredient edge
could only come from work that constructs an ingredient out of an earned property; no accepted work
has done so.

## Notes for adjudication (they cannot change R-5)

- **N-1: the list of ingredient → property edges.**
  - Only E1–E4 carry the literal words NECESSITY-CERTIFIED / LOAD-BEARING.
  - E2′, E5 and E6 are accepted under other wording: "HOLDS at tested scope", "ACCEPTED / necessity
    established analytically", and CLASS-SPLIT with an identity-determined boundary.
  - E5 is the edge diagnostic §4 itself lists as certified.
  - Whether E2′, E5 and E6 count as edges is an owner call. **Adding or removing ingredient →
    property edges cannot create a cycle**, so R-5 is unaffected.
- **N-2: the DORD-8 bar** ("Owner acceptance of O-5 may not be cited as certifying any edge",
  `L0_1F_DORD_THEOREM_01.md:274-275`). It is operator text inside an owner-accepted document, not
  restated in the ruling. The verdict on candidate 2 does not rely on it.

**HARD STOP.** This is proposed for owner adjudication. It authorizes no S3 run, no hybrid, no S-4 or
S-6, no S5-WB or S5-OD, and nothing on gravity, Π₀ or cosmology.
