# Closure-premise test on the 3D Lorentz-compatible family — RESULT

**Date:** 2026-08-24 · **Instrument:** `wall_a_closure_premises.py` (REAL_EXIT=0) ·
**Standing state:** `b0bdfb6`, register 73 nodes, net +17 · **W-0:** everything here is
COMPUTED-AND-REPORTED, NOT BANKED. No claims.json edits.

## The question

The measured licensing chain ends 3 → 2. The 3D Ward-allowed family is
K(ω,k) = a·P² + b·P⁰ˢ + c·X_sw; the 2D closure family {P², P⁰ˢ} is reached **only** by
killing c. This test determines, premise by premise, *what* kills c, *by what mechanism*,
*in which regime* — starting from 3D, never from 2D.

## The regime table (every entry computed)

| regime | c = 0 status | mechanism |
|---|---|---|
| equilibrium (T-even couplings, no T-odd background) | **DERIVED** | **P-A**: Onsager reciprocity demands slot-exchange symmetry; the reciprocity partner of X_sw is X_ws, which the diagonal Ward identity **forbids** (r-slot longitudinal). Exact linear solve at (ω,k)=(3,2),(5,2),(7,3): solution space dim 2 — (a₁=a₂), (b₁=b₂) free, **c₁=c₂=0 pinned at every sample**. |
| registered FDT-locked (ε,τ₂) family | **COROLLARY** | **P-B**: KMS ⇒ detailed balance ⇒ equilibrium reciprocity ⇒ P-A's algebra. Load-bearing identity **re-derived on a finite 3-level system, not cited**: χ″_BA(ω) = −χ″_AB(−ω) exact at all resonances for any weights; T-even operators ⇒ slot-symmetric; T-odd operator ⇒ antisymmetric (Hall-type). |
| genuine non-equilibrium | **ABSENT — family stays 3D** | **P-C**: reciprocity inapplicable; passivity is **blind to c** on the physical (conserved-source) domain — computed: conservation k_μv^μν = 0 forces (v:ω) = 0, so the quadratic form never probes the off-diagonal channel. |

**P-D** (bare both-slot transversality) recorded as the *conclusion* the above license,
never an independent premise.

## Findings that deviate from the briefed expectation (diagnosed before reporting)

1. **Passivity does not produce the expected |c| inequality — it produces nothing.** The
   ω-channel diagonal is identically zero (P⁰w is Ward-forbidden), so the
   channel-diagonal passivity lemma's hypothesis (both diagonals probed) fails. On the
   unphysical unconserved-source domain PSD would force c = 0 outright (2×2 minor:
   det = −im(c)²/4 < 0 for c ≠ 0) — but admitting non-conserved sources contradicts the
   diagonal-Ward registration. Reported as found.
2. **The gyrotropic escape is closed for the gravitational vacuum — structurally.** The
   first plant mock used X_sw as a Hall-type antisymmetric part and *correctly failed*
   the proper Onsager test. ~~A compatible antisymmetric part must be ε-tensor-mediated,
   and the registered comoving vacuum contains no T-odd object from which to build one.~~
   **STRUCK-AND-REPLACED at second-author review**: the operative closure is
   **partner-exclusion** — the Onsager partner of c(H)·X_sw is c(−H)·X_ws, a *different*,
   linearly independent, **Ward-forbidden** structure (unlike the 2-channel Hall case,
   whose partner is minus itself), so c(H)=0 for **all** H, odd c(H) included, even in the
   presence of a T-odd scalar background — and FRW's H **is** T-odd, so the
   no-T-odd-object line was flat-scope only. Reachability was re-proven **in the actual
   tensor space**: the family enlarged to include X_ws retains the odd Hall mode
   cs(H)=cw(−H) under the same solve (`second_author_closure_premises.py` E4). The
   2-channel plant stands as the analogue demonstration; the tensor-space plant is the
   reachability proof.

## Defects self-caught during this run (all pre-report)

- **Expectation error (P-A):** first draft expected reciprocity solution-space dim 4;
  correct is dim 2 (6 unknowns − 4 constraints). Corrected before the verdict was used.
- **Variance error (P-C):** first draft mixed index variance (conservation with k^μ,
  contraction with lower ω on a lower-index field) → spurious residual −4k²v₃₃/(k²−ω²).
  The k^μ↔k_μ family, caught by the check's own suspicious output. Fixed with an
  explicit variance registry entry; (v:ω)=0 on conserved sources now exact.
- Two dict-iteration KeyErrors (mechanical).

## Honest boundary — what this table means for the wall

The 3 → 2 step is a **regime-gated equilibrium fact**: derived from reciprocity at
equilibrium, corollary inside the registered KMS-locked family, and simply **absent**
out of equilibrium — where the response family is honestly 3-dimensional. The chain is
three mechanisms, never one argument:

```
21 ──gauge/orbit──► 11 ──Lorentz-covariant response (+1, booked)──► 3 ──equilibrium reciprocity/KMS──► 2
```

Left unanswered, as designed: **does the microscopic de Sitter gravitational response
place itself in the 3D Lorentz-covariant subspace, and then in the 2D closure family,
without those properties being imposed?** That is Σ_R^TT — Wall A — the next task.

## Second-author verification targets (load-bearing first)

1. **P-A reciprocity signs**: the T-parity assignment (h_mn T-even ⇒ ε_Aε_B = +1), the
   ω-argument placement (Onsager–Casimir at same ω, k→−k absorbed by k-evenness of the
   structures), and the claim that the exact solve's dim-2 nullspace pins both c's.
   A from-memory derivation could flip any of these.
2. **P-C domain distinction**: that conservation k_μv^μν = 0 genuinely forces (v:ω)=0
   (variance-consistent), and that the passivity lemma's hypothesis fails because the
   ω-channel diagonal vanishes *by Ward*, not by assumption.
3. **P-B finite-system identity**: χ″_BA(ω) = −χ″_AB(−ω) and the T-parity sign branch.
4. **Gyrotropic plant redesign**: that the ε-mediated structure is the only Onsager-
   compatible Hall form, and that no T-odd tensor exists in the registered vacuum.

## SECOND-AUTHOR REVIEW — COUNTERSIGNED WITH CORRECTIONS (2026-08-24)

Instrument: `second_author_closure_premises.py` (E1–E7 all PASS, exit 0) plus four
independent adversarial verifiers (exact arithmetic, own conventions/orderings/samples,
prompted to refute). **Verdict: NOT REFUTED on all four load-bearing steps — the regime
table stands.** Every check reproduced: reciprocity nullspace dim 2 with the exact
a₁=a₂, b₁=b₂, c₁=c₂=0 pattern at (3,2),(5,2),(7,3) **and** fresh sample (9,4); the full
256-term Q(v) reduction exact; conservation ⇒ (v:ω)=0 identically; the spectral identity
exact on an independent 4-level *degenerate* system for fully symbolic complex operators.

**Corrections applied (mechanism-level; the c=0 conclusion unaffected by all of them):**

1. **Target 1 was right to worry**: "h_mn T-even" is false — h_0i is **T-odd** — and
   "k→−k absorbed by k-evenness" is false componentwise (72 sign-flipping components
   across the four structures). The true mechanism is the **ε-signature cancellation**:
   ε_mn ε_rs against the structures' k-parity, verified at 0/256 violations per
   structure (E1/E2). Same endpoint, corrected reason; registry amended in place.
2. **Target 4's mechanism replaced by partner-exclusion** (see the struck finding
   above) — a *stronger* closure: robust to T-odd scalar backgrounds, reachability
   proven in the actual tensor space (E4).
3. **Three dead/tautological gates fixed** (a recurring defect *class*, not one bug):
   the T-odd plant predicate was inverted **and** ungated (the two defects cancelled —
   shipped verdict unaffected); `pc_kills` was a hardcoded literal making its gate
   tautological (now derived from the conserved-domain computation); the T-even ⇒
   slot-symmetry bridge — the actual step reaching P-A's algebra — was printed but
   never gated (now gated). Plus a new scope gate: assembled plant kernels verified
   r-slot Ward-allowed.
4. **Regime-table precision (FDT-locked row)**: T-even slot symmetry holds for
   *arbitrary* populations — KMS is not needed for that step. KMS's genuine additions,
   now NAMED in the row: it does **not** supply T-evenness of couplings (Gibbs + a
   T-odd operator keeps the Hall branch exactly), and for degenerate spectra
   state = f(H) kills the static ω=0 Hall line (verifier-exhibited:
   28iπ(p₁−p₂)/3 → 0 under Gibbs) — a line a non-degenerate 3-level system can
   never expose. Reality of matrix elements is load-bearing in the T-even bridge
   (a complex-Hermitian non-real operator breaks oddness in ω while the general
   identity survives).
5. **P-C's strongest escape route closed by the verifier**: two-field forms *do* probe
   the antisymmetric part of X_sw that the single-field quadratic form cannot see —
   but every c-channel bilinear vanishes exactly when **both** fields are conserved,
   while the P² channel stays nonzero on the same pair. The conserved-domain blindness
   is not a trivial-domain artifact.

Zero confirmed physics errors; all defects were instrument/wording currency. The
recurring session pattern holds.
