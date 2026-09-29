# L0-1d — VERDICT (three lines, never composed)

**Date:** 2026-09-29 · **Charter:** `L0_1D_CHARTER_01.md`, FROZEN at
`3a8ae1b` after an analytic-only pre-freeze review
(`L0_1D_PREFREEZE_REVIEW_01.md`; nothing previewed, nothing
quarantined) · **Authority:** registry rulings R-1 … R-4, under the
adopted floor termination condition; floor obligation **O-1** ·
**Instrument:** `calc/l01d_cycle_affinity.py` (`07f6103`; pure
stdlib; exact integer arithmetic for Instrument E) · **Artifact:**
`L0_1D_RESULT.json` (sha `dd9e9028885f247f…`) · **Battery: 12/12 gated
checks, zero failures, zero halts, in the recorded single run (18
trajectories + exact computations for 9 members, 37 s).**

**Scope of every line below:** *within the declared background
mathematics (exact rational arithmetic for Instrument E, the frozen RK4
schedule for Instrument B, exact symmetric eigendecomposition for the
identity references), the declared members T ∈ {0, 0.9},
C ∈ {0, 0.1, 0.3, 0.6, 0.9}, B ∈ {0.3, 0.9} on the sealed C1 bath and
its one-spring ring closure, with K_s held, and the declared window,
grids, and comparator.*

## RUN LABEL: OUTCOME-B — the affinity split

## LINE L-1 — NON-RECIPROCITY WITHOUT CYCLE AFFINITY: REDUCIBLE TO A RECIPROCAL TWIN

> **Identity-grade (F-1 and Kolmogorov instantiated).** Every
> zero-affinity member is exactly completely monotone, by exact
> rational Hankel test: T(0), T(0.9), C(0), B(0.3), and B(0.9) all
> have H₀ ≻ 0 with d = r and inertia (d, 0). The time-domain
> kernels match their symmetric twins to 5×10⁻¹³, envelope-normalized
> (RC-3). **These kernels change a great deal with γ,** and that is
> F-1's content, not a violation of it. T(0.9) and B(0.9) reach
> k(40) = 5.9×10⁻²⁸ and 1.8×10⁻²⁵, against the anchor's 6.8×10⁻⁹,
> because their reciprocal twins carry weakened couplings
> √(1 − γ²) = 0.436. What is identity-held is that the kernels **never
> leave the reciprocal class.**

## LINE L-2 — CYCLE AFFINITY: BREAKS P_positivity (c), complete monotonicity, exactly, at every declared circulating member

> **(i) The necessity of affinity for any breach is a theorem** (L-1's
> identity). **(ii) The breach at each declared member is certified by
> exact computation:** C(0.1), C(0.3), C(0.6), and C(0.9) all have
> d = r = 23 and H₀ not ≻ 0, with exact inertia **(12, 11)** at every
> one of them. The cycle affinities are 𝒜 = 4.6, 14.2, 31.9, and 67.7.
> **(iii) Components:** (c) was adjudicated exactly; (a) is held by
> identity at every member (RC-5; minimum recorded k = 5.9×10⁻²⁸ > 0);
> (b) was not adjudicated and is mapped below.

## LINE L-3 — CYCLE AFFINITY: NOT-LOAD-BEARING for P_memory (R-1 envelope reading; accretivity held)

> The envelope comparator reads EXPONENTIAL-GRADE at every member, and
> X-1′ confirms that affinity acts in the window: C(0.9) differs from
> its reciprocal twin by 0.040, envelope-normalized, above the 0.01
> threshold. **Disclosure of a thin margin:** at C(0.6) the comparator
> read R_exp = 2.430 against R_alg = 2.516, a margin of 0.086. This was
> the not-banded, genuinely attackable gate the charter named, and it
> came close to routing to COMPARATOR-LIMITATION. It passed, and the
> margin is on the record. The exponential *bound* |k| ≤ e^{−μτ} held
> everywhere by identity (RC-6, zero breaches).

## OUTCOME B, at recorded scope

> *On one substrate with one symmetric part, zero-affinity asymmetry
> keeps the retained-site kernel exactly in the reciprocal, completely
> monotone class; cycle affinity takes it out of that class at every
> declared member; the exponential memory envelope survives
> throughout.*

Per the frozen table, this **supports CLASS-SPLIT for O-1**: the
zero-affinity class is exactly CM and the affinity class is exactly
not CM, on the same substrate, with L-3 certified inside it. The owner
assigns the terminal label.

## The pre-registered expectations: three of four refuted (reported, moving no label)

The charter recorded four labeled analytic expectations for the maps
(§3.6), to be confirmed or refuted on the record. **Three were
refuted, one only in part.** This is the most informative part of the
run, because it is where the analysis was wrong.

| Expectation (frozen before the run) | Result | Status |
|---|---|---|
| C(0.1) is in the real phase: Sturm count = r, p squarefree | Squarefree, but **only 3 of 23 roots are real**. Ten complex pairs are already present at γ = 0.1. | **REFUTED.** The real phase ends *below* γ = 0.1. |
| H₀ inertia at C(0.1) shows negative pivots, consistent with negative real weights | Inertia (12, 11). With 3 real roots and 10 complex pairs, that decomposes as (10, 10) from the pairs plus (2, 1) from the real atoms: **one negative real weight, with the breach carried mostly by complex pairs.** | **PARTLY CONFIRMED.** Both mechanisms are present, and complex pairs dominate. |
| The operational Gram minimum eigenvalue at small γ is at or near the integration floor, so trajectories can't see the breach | C(0.1): **−4.0×10⁻⁸**, which is 11 orders of magnitude above the floor (about 10⁻¹⁹ for CM members) and 400 times beyond −10⁻¹⁰. Full and halved schedules agree to every printed digit. | **REFUTED.** The trajectory battery sees the breach at every declared γ. |
| Exceptional points appear somewhere in (0.1, 0.9], dropping the Sturm count below r | The count is already below r at γ = 0.1 (3), and it falls to 1 between γ = 0.3 and 0.6. | **REFUTED on location.** Exceptional points begin below γ = 0.1. |

**What the refutations say (post-run analytic note, labeled; it changes
no gate or line).** The small-γ negative-weight theorem (charter §3.5)
still stands, but its "sufficiently small" range lies entirely below
γ = 0.1. The likely reason is visible in the γ = 0 structure. Each
R-even mode sits next to an R-odd mode that is its degenerate circulant
partner, shifted only slightly by the one-site defect. Those near-pairs
collide into complex pairs under very small circulation. The charter
did not derive the exceptional-point locations and said so. The run
located them: **almost all of the ring's retained-site spectrum goes
complex before γ = 0.1.**

## The other maps (ungated)

- **Operational Gram minimum eigenvalue:**

  | Members | Gram minimum eigenvalue |
  |---|---|
  | Every zero-affinity member | −10⁻¹⁹ to −10⁻²⁴ (the integration floor) |
  | C(0.1) | −4.0×10⁻⁸ |
  | C(0.3) | −2.2×10⁻⁵ |
  | C(0.6) | −1.2×10⁻³ |
  | C(0.9) | −6.4×10⁻³ |

  Detection grows monotonically with affinity.
- **Monotone decrease, component (b):** C(0.1) and C(0.3) are still
  monotone on the grid. **C(0.6) and C(0.9) are not** (maximum step
  increases of +2.2×10⁻⁵ and +1.8×10⁻⁴). So (a) held and (c) broke at
  every C member, while (b) broke only at the two strongest. That
  matches the registry's rule that positivity components are
  independent and must never be composed.
- **Memory under affinity (post-run note, labeled):** at the same K_s
  and the same edge products, C(0.9) keeps k(40) = 4.7×10⁻⁸, *above*
  C(0)'s 1.5×10⁻⁸. The zero-affinity members with weakened edge
  products instead collapse (B(0.9): 1.8×10⁻²⁵). Suggestively, with
  the symmetric part held, zero-affinity asymmetry acts like a
  reciprocal system with weaker couplings and forgets fast, while
  affinity rotates the spectrum into the complex plane and keeps the
  slow decay. This is suggestive only, and it adjudicates nothing.
- The difference from the twin grows with γ: 0.0021, 0.012, 0.026, and
  0.040.

## What this does and does not establish

- It does **not** say "reality breaks detailed balance" or "positivity
  requires reversibility in nature." The class is one pinned ring with
  uniform or balanced deformations, N = 23, with K_s held.
- It **does** give the floor its first certified result, and the
  cleanest version so far of the distinction the owner asked about.
  **Within the tested class, what breaks the reciprocal (completely
  monotone) response structure is not asymmetry, it is cycle affinity:
  broken detailed balance.** Asymmetry without affinity is reducible
  to a reciprocal twin exactly. That is the design's two-property
  hypothesis tested on its detailed-balance half, **at this scope only;
  it remains a hypothesis at the floor level until O-7.**
- It **refuted three pre-registered analytic expectations.** The
  exceptional-point structure sits far lower in γ than the analysis
  anticipated, and trajectory batteries are far more sensitive than
  expected. Both are recorded against the analysis, not rationalized.
- Nothing changes on O-2 (still open, per the corrected F-7), the v4
  deposit, the red gates, GR2, L0-1a/b/c, or the public paper.

**HARD STOP.** The verdict is recorded pending owner ruling on the
three lines and on **O-1's terminal label.** The frozen table proposes
CLASS-SPLIT. After that, the adopted sequence continues with D-DET
(O-3/O-4), and O-2 remains a live obligation with a named candidate
substrate.
