# CLASS_C_DISPATCH_SPEC — the rung-3 keystone, frozen before calculation

> **STATUS: SPECIFICATION. NOTHING BANKED, NOTHING COMPUTED.**
> This document freezes the class-C question BEFORE any calculation, per the owner's
> adjudication of 2026-08-21. It supersedes no sealed instrument and touches no register
> field; draft ledger language arising from it lives in the cited RESULTS/DRAFT sections and
> reaches `provenance/claims.json` only through the bank gate / firewall after screening
> (CHARTER §1.3, §5.3). No ledger net figure is typed here.

## 0. The owner's ruling, recorded verbatim

> **Class A — CLOSED/EXHAUSTED FOR PARAMETER-FREE RUNG-3 DISCHARGE.**
>
> Not "falsified universally." Not "failed physics." Not "proven impossible." Precisely:
>
> *The class-A gravitational worldline route cannot discharge the registered Rung-3 memory
> mechanism without the priced epoch-window and IR-regulator inputs; therefore it cannot
> serve as the derivation of a parameter-free GRUT memory scale.*
>
> **Class C — OPEN, DECISIVE.**

Grounds on record: `calc/tt_worldline_spectrum.py` + `calc/RESULTS_tt_worldline.md`
(non-stationarity >130% across epochs; W* < 0.25 e-folds stationarity window;
amplitude regulator-controlled 2.3×; τ_eff epoch-dependent, non-monotonic), and
`calc/worldline_reduction.py` + its RESULTS (proxy floor; [R_wl, R_IR] ≠ 0 in closed form).
No further class-A variations are authorized unless they answer a specific unresolved
mathematical objection.

## 1. The renamed question

Not "does the bath have a single pole?":

> **Does the fully assembled class-C gravitational response contain a physically defined
> low-frequency relaxation structure that survives removal of the class-A regulator/epoch
> artifacts?**

Formally: let R_C denote the full assembled response. Does there exist a well-defined
observable τ_phys = F[R_C] such that ∂τ_phys/∂k_min = 0 and no arbitrary epoch/window
parameter remains in the final definition? That is the real discharge. Anything whose value
tracks k_min or the epoch window is a priced input, not a result.

## 2. The frozen chain

    Sigma(x,x')  ->  G_R^TT(x,x')  ->  allowed stationarity/spectral reduction
                 ->  late-time response

Each arrow is a separate gated step. An arrow may FAIL, and failure is a result.

## 3. The three things class C must prove

### 3.1 A legitimate object
Define exactly what Σ(x,x') is being computed: state, gauge-invariant assembly (source
vertex, observer vertex, external-mode-function corrections), renormalization prescription,
and TIME VARIABLE — named per keystone-map §1 (D1–D6), with the D3a/D3b split respected:
a spectral representation exists globally only in static-Killing time; along worldlines only;
the assembled object may admit neither, in which case step 2 is replaced by two-time response
analysis and no ρ(ω) is manufactured.

### 3.2 A legitimate low-frequency limit
If a stationary reduction EXISTS (proved, not presumed — no imported class-A stationarity),
establish it and take ω → 0 within it. If it does NOT exist, do not manufacture ρ(ω): use the
appropriate two-time response G_R(x,x′) directly and classify its late-time/two-time
structure on its own terms.

### 3.3 A regulator/epoch-independent memory scale
Only after 3.1 and 3.2: does K_R contain a single relaxation pole, multiple poles, a branch
cut, a continuum, secular/nonstationary memory, or no long-memory structure? And is the
resulting scale (∂τ_phys/∂k_min = 0, no window parameter) regulator- and epoch-independent?
Then the result decides what rung 3 becomes.

## 4. Prohibitions (hard, each one a kill condition)

1. **No J(ω) ∼ ω³** — falsified at class A; importing it anywhere is laundering.
2. **No single-pole ansatz** — the ansatz under test may not be assumed inside the test.
3. **No τ₀ target** — no 41.9 Myr, no desired timescale may enter setup, plots, fits, or
   framing; the chain runs ρ → G_R(ω) → G_R(t) → τ_eff IF ONE EXISTS.
4. **No imported class-A stationarity** — D3a licenses worldline scope for invariant fields
   ONLY; the graviton channel was shown non-stationary; nothing carries over unproven.
5. **No chosen epoch/window as an unstated premise** — if a window is unavoidable, it is a
   named, priced input appearing in the final error budget.

Plus the standing guards: do not manufacture a pole; do not manufacture responsiveness; do
not borrow the scalar-probe assembly; do not read a verdict off a gauge-fixed object.

## 5. Execution reality (stated, not evaded)

By standing rule (keystone-map §3 walls, register fences):
- **In-house**: the formal definitions (§3.1), the reduction-order disclosure (§4), the
  outcome classification scheme (§6), and the dispatch packaging. The wall-(A)/(B)
  computations themselves are outside in-house reach.
- **Dispatch territory**: the actual computation. This spec IS the re-pose of
  `DISPATCH_ONE_PAGE.md`, superseding its cosmic-time pinning (keystone map C7) with the
  clock-naming requirement and adding the regulator/epoch-independence criterion of §1.
  The HELD status transfers: the re-posed ask inherits the hold until its own pre-screen
  passes and the owner authorizes transmission.

## 6. Outcome classes (all first-class, none predetermined)

1. **Pole** — with location/residue; check regulator/epoch independence (§1 criterion);
2. **Multiple poles / ladder** — characterize; compare against the free ladder (state, not
   dynamics — E6 fence);
3. **Branch cut / continuum** — determine whether the low-frequency behavior yields the
   registered memory kernel shape;
4. **Secular / nonstationary memory** — the two-time object grows; classify the growth;
5. **No long-memory structure** — rung-3 mechanism fails as registered; retire and say so;
6. **Ill-posed even after assembly** — the reduction does not exist in any clock; a
   structural no-go result about the question itself.

Every outcome is publishable stand-alone de Sitter physics regardless of consequence for
this program; attribution downstream and stated.

## 7. Ledger consequences (draft language — NOT APPLIED)

Candidate additions for the bank gate (owner adjudication required):

> (i) `rung3_single_pole`: scope marker — the class-A gravitational route is CLOSED/
> EXHAUSTED for parameter-free discharge (owner ruling 2026-08-21); the open anchor question
> is re-posed at class C under CLASS_C_DISPATCH_SPEC.md. Tier unchanged (derived-pending);
> no delta.
>
> (ii) New draft node (class TBD at banking): "class-A gravitational worldline sector cannot
> supply a parameter-free rung-3 quantity" — tier derived-pending on the exhibited
> calculations, sub_status carrying the priced-inputs list (epoch window W* < 0.25 e-folds;
> IR amplitude 2.3× across k_min ∈ [0.25, 1.0]).

Both drafts require adversarial pre-screen before entering the register; neither may be
cited as content until banked.

## 8. Status ledger (as of this spec)

- **Green**: D3a worldline stationarity (invariant fields); C→A machinery at proxy scope;
  flat T=0 origin of ω³; [R_wl, R_IR] ≠ 0; robust finite low-frequency proxy behavior;
  TT-channel non-stationarity exhibit; the adversarial verification machinery itself.
- **Amber**: exact functional form of the dS proxy spectrum (closed forms falsified;
  converged numerics stand); everything class C.
- **Closed/Exhausted (owner ruling)**: class A as a parameter-free discharge route.
- **Red if asserted prematurely**: any of the owner's red-list phrasings; "class C will show
  X" for any X; any τ₀-derived framing.

## 9. Build-queue status (owner brief phases)

| phase | item | status |
|---|---|---|
| 0 | contamination audit | **EXECUTED & CLEAN (owner-accepted)** — `provenance/class_c_contamination_audit.py` → `provenance/CLASS_C_CONTAMINATION_AUDIT.md`; checker/reference-data classification added 2026-08-22 |
| 1 | machine-readable manifest | **EXECUTED & PASS (owner-accepted)** — `CLASS_C_MANIFEST.json` + `provenance/class_c_manifest_gate.py` (recursive fail-closed `require()`, demonstrated) |
| 2–4 | object / clock / regulator gates | **ENFORCED against the executable surface** — dependency-closure audit `provenance/class_c_dependency_closure.py`: 8 bypass mutants caught, clean source passes, live surface CLOSED; first executable skeleton `calc/class_c_solver.py` refuses all six undecided prerequisites |
| 5–6 | independent routes + benchmark suite | **EXECUTED** — golden-limit matrix `provenance/CLASS_C_BENCHMARK_MATRIX.md` (quantitative tolerances; SAME-CODE RERUN vs INDEPENDENT-CODE provenance labelled); independent-route disagreement caught and investigated (domain error in the checker itself) |
| 7 | no imposed spectral form | encoded in manifest prohibited list + permitted outcome classes |
| 8–9 | dynamics reconstruction + parameter-independence tests | specified in §1 criterion (∂τ_phys/∂k_min = 0, no window parameter); measured dependencies on record (TT results file, Findings 4–5) |
| 10 | four-lens screen | infrastructure + skeleton screened (`provenance/SCREEN_RECORD_2026-08-22_classc_infrastructure.md`); result-screen queued for the first physics result |
| 11 | provenance classification | **EXECUTED** — `provenance/CLASS_C_PROVENANCE_LEDGER.md` (SAME-CODE RERUN ≠ INDEPENDENT IMPLEMENTATION ≠ EXTERNAL REPRODUCTION) |
| 12 | dispatch freeze | **FROZEN 2026-08-22** — `CLASS_C_DISPATCH_FROZEN.md` (immutable certificate; re-freeze refuses). Wall contracts D4/D5 frozen same day: `CLASS_C_WALL_CONTRACTS.md`. Remaining owner/dispatch items: execute or transmit per contract |

No ledger edits are applied because this brief exists. Every resulting claim remains draft
until screened and bank-gated.




