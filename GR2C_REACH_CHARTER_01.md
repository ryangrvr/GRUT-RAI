# GR2-c — UNIVERSAL REACH: CHARTER + PRE-REGISTRATION (frozen before evaluation)

**Fork:** GR2-c, fourth fork of the GR-2 campaign (Layer 3 of
`GR2_CAMPAIGN_DIRECTIVE_01.md`), authorized before GR2-d by dependency
order.
**Authority:** owner ruling of 2026-09-27 (`GR2B_OWNER_RULING_01.md`),
which authorizes GR2-c and freezes its question.
**Source commits:** `master-w25bu9`; machinery replicated: the U-1
universality instrument `calc/u1_universality.py` (targets from
`U1_UNIVERSALITY_RESULT.json` at full precision) and the GR-1 L-X pair
machinery as replicated in `calc/gr2b_probe.py` (`c0dbf98`). Recorded
gradings cited: U-1 (universal reach **supplied**; universality then
derived under exchange), CC-1, P-6, CA-1, G-2/GS-1, GR2-a (`ddcfb76`,
accepted), GR2-b (`c0dbf98`, accepted).

## 0. The question (the owner's, frozen verbatim)

> **Does anything genuinely earned by the GRUT core force every retained
> sector to couple universally to the proposed gravitational response
> (g₁ = g₂ = … = g_N)?**

Two owner warnings bind this charter:

1. *Compatible ≠ selected.* That the universal assignment passes every
   earned gate demonstrates **compatibility only**. Selection would
   require an earned test that **fails** at some non-universal
   assignment. The verdict gate V-1 is a survivor count over
   non-universal assignments, exactly as in GR2-a/GR2-b.
2. *No empirical smuggling.* The empirical observations (universal
   attraction, light bending, Eötvös-type universality) remain
   **outside** the earned/supplied selection machinery; this fork does
   **not** introduce empirical input as a domain datum. They are cited
   only to say where the elimination would have to come from.

## 1. Delta over the record

U-1 established the class split: universality **derived** for
exchanging sectors *conditional on the supplied gauge structure*;
**irreducible input** for genuinely decoupled sectors; universal reach
(that every sector sits in the exchange-coupled component) **supplied**.
GR2-c asks the sharper survivor-count question at the
coupling-magnitude coordinate, with new mechanical content:

- (i) a **joint multi-sector cone leg**: the joint influence kernel
  $C_{ij}(w) = g_i g_j\,J_0(w)$ (rank-1, $J_0$ = the record's
  stress-source pair kernel) is PSD for **every** real coupling vector,
  including sign-non-universal ones — the earned cone admits every
  assignment;
- (ii) an **exchange-grid leg**: the U-1 dynamical-probe exchange system
  run over a grid of coupling pairs $(g_A, g_B)$ — even *exchanging*
  sectors, where U-1's class-II forcing lives, pass every **earned**
  gate at unequal couplings, so the forcing is located entirely in the
  supplied gauge layer;
- (iii) a **geometry-blindness grid**: the recovered hop geometry and
  normalized spectral shape are invariant across coupling assignments
  and under overall rescale;
- (iv) an **observability grid**: non-universal assignments are
  *observable* by joint access, graded in the deviation — and
  observable ≠ forbidden (the GR2-a/GR2-b lesson at the reach
  coordinate);
- (v) the survivor count and the forcing-location statement for the
  reach coordinate of the inventory.

Recorded fact carried (frozen note): U-1's own exchange-channel
demonstration used **unequal** couplings $(0.3, 0.18)$ and passed every
earned gate — the record already contains a functioning non-universal
exchange channel.

## 2. Elimination discipline (frozen)

An assignment is **eliminated** only if an earned *admissibility* test
fails on it: joint-cone PSD, ground-state two-time Gram PSD of the
coupling operator, interaction-graph change, per-sector normalized
shape change. The joint discriminator measures *distinguishability*,
which is labeling, never elimination.

## 3. The gates (frozen, mechanical)

**Controls (halt-grade; exact replication of U-1, seed 20260925, same
loop order; targets from `U1_UNIVERSALITY_RESULT.json` at full
precision) and the L-X control:**

- RU-1 L-C universal probe: joint $\Delta$ replicates
  1.84297022087776e-14 ($|\Delta_{\text{repl}}|<10^{-12}$).
- RU-2 L-C non-universal probe ($\varepsilon_B=0.6$): joint $\Delta$
  replicates 0.04947765826773509 ($|\Delta_{\text{repl}}|<10^{-9}$).
- RU-3 L-G soft-emission gauge variation: classI_max replicates 0.0
  (exactly); classII_min_neq replicates 0.1297458179916556
  ($|\Delta_{\text{repl}}|<10^{-9}$); classII_max_eq replicates
  8.881784197001252e-16 ($|\Delta_{\text{repl}}|<10^{-15}$).
- RU-4 L-D clock-only probe: $\|[H_A,H_{\text{full}}]\|$ replicates
  8.881784197001252e-16 ($<10^{-15}$); $\langle H_B\rangle(t)$
  variation replicates 7.549516567451064e-15 ($<10^{-13}$).
- RU-5 L-D non-conserved probe at $(g_A,g_B)=(0.3,0.18)$:
  $\|[H_A,H_{\text{full}}]\|$ replicates 2.1708000000000003
  ($|\Delta_{\text{repl}}|<10^{-9}$); variation replicates
  0.30270478920041 ($|\Delta_{\text{repl}}|<10^{-9}$).
- RL-1 the L-X stress-source pair slope replicates 8.005419679013105
  ($|\Delta_{\text{repl}}|<10^{-9}$) — $J_0$ is this channel's kernel.

**J — the joint cone leg (deterministic; N = 3 sectors).**
$C_{ij}(w) = g_i g_j J_0(w)$, $J_0(w)$ the stress-source L-X kernel,
$w$-scan $\{0.10 + 0.02i,\ i = 0..5\}$; frozen coupling grid
$\{(1,1,1),\ (1,0.6,0.36),\ (1,0.1,10),\ (1,-0.7,0.2),\ (2,0,1)\}$:
- J-1 for every grid vector and every $w$: min eig of $C(w)$
  $\ge -10^{-12}\,\lambda_{\max}$ — the joint cone admits **every**
  assignment, sign-non-universal ones included.
- J-2 (halt-grade analytic identity): the spectrum of $C(w)$ is
  $\{|g|^2 J_0(w),\,0,\,0\}$ — $|\lambda_{\max}-|g|^2J_0| <
  10^{-9}\,\lambda_{\max}$ and both remaining $|\lambda| <
  10^{-10}\,\lambda_{\max}$. (GR2-b discipline: an identity gate so an
  eigensolver bug halts the run instead of faking physics.)

**E — the exchange-grid leg (the U-1 L-D system, 80-dim, X-type
coupling; frozen pairs $(g_A,g_B) \in \{(0.3,0.18),\ (0.3,0.3),\
(0.3,0.03),\ (0.3,0.6)\}$):**
- E-1 earned positivity for every pair: ground-state two-time Gram of
  the coupling operator PSD (min eig / scale $\ge -10^{-12}$) — equal
  and unequal couplings pass identically.
- E-2 the exchange channel functions for every pair:
  $\|[H_A,H_{\text{full}}]\| > 10^{-3}$ and $\langle H_B\rangle(t)$
  variation $> 10^{-4}$ on $[0,10]$ — unequal couplings sustain
  exchange; nothing earned degrades or forbids $g_A \ne g_B$.

**G — the geometry-blindness grid (the U-1 L-C ladder, L = 3):**
- G-1 for every $\varepsilon \in \{0.3, 0.6, 0.9, 1.5\}$ with
  $O_\varepsilon = H_A + \varepsilon H_B$: the interaction graph of
  $H + hO_\varepsilon$ ($h = 0.05$) equals that of $H$ — the recovered
  hop geometry is blind to the coupling assignment.
- G-2 the normalized spectral shape of $(1+h)H$ equals that of $H$
  within $10^{-12}$ — the earned geometry is invariant under
  $g \to \lambda g$ and cannot register an absolute coupling.

**O — the observability grid (joint discriminator, best common
rescale, exactly U-1's machinery):**
- O-1 $\Delta(\varepsilon) > 10^{-3}$ for $\varepsilon \in
  \{0.3, 0.9\}$ — every tested non-universal assignment is observable
  by joint access.
- O-2 strict ordering $\Delta(0.3) > \Delta(0.6) > \Delta(0.9)$ — the
  deviation is graded in $|1-\varepsilon|$ and vanishes at the
  universal point (RU-1's 1.8e-14). Observable, never forbidden.

**The verdict gates:**
- V-1 (earned survivor count): the earned admissibility battery (§2)
  eliminates **0 of the 14 non-universal assignments** tested — J-leg
  4 (the grid minus $(1,1,1)$), E-leg 3 (the pairs minus $(0.3,0.3)$),
  G-leg 4 ($\varepsilon \ne 1$), O-leg 3 ($\varepsilon \in \{0.3, 0.6,
  0.9\}$, the 0.6 row being RU-2's replicated recorded probe).
- V-2 (forcing located): the **only** mechanism anywhere in the record
  that forces $g_A = g_B$ is the supplied massless gauge structure, and
  it acts only on exchanging sectors — mechanically: classI_max = 0.0
  (unequal couplings unconstrained even under the supplied layer when
  sectors are decoupled) AND classII_min_neq $> 10^{-3}$ AND
  classII_max_eq $< 10^{-12}$ (forced exactly when exchanging, under
  the supplied structure) AND every unequal E-leg pair passes E-1/E-2
  AND V-1 holds. Whether every sector sits in the exchange-coupled
  component at all is itself **supplied** (U-1's recorded residual —
  cited, not re-adjudicated).

**Ungated frozen notes:** (i) compatible ≠ selected, per §0; (ii) the
empirical firewall, per §0 — the eliminators of non-universal reach are
empirical and stay outside the record; (iii) the joint cone is PSD even
for sign-non-universal assignments, so the earned cone does not force a
common coupling *sign*, let alone a common magnitude; (iv) access does
not select the assignment (P-6, GR2-b A-leg — cited, not re-run).

## 4. Outcome rule (frozen, mechanical)

- **C-REACH-NOT-FORCED** iff every gate holds: nothing earned
  eliminates any non-universal coupling assignment; the earned
  structures are compatible with all of them and select none; the only
  forcing in the record lives in the supplied gauge layer, conditional
  on exchange, and reach into the exchange component is itself
  supplied. Consequence: **the reach coordinate is sharpened as an
  irreducible primitive at this level — the demonstration half of its
  certificate, feeding C4 and Layer 7. U-1's DERIVED-IN-CLASS status
  for exchanging sectors STANDS; this fork locates its premises, it
  does not weaken it.**
- **C-REACH-FORCED-IN-CORE** iff V-1 fails: some earned admissibility
  test eliminates a non-universal assignment.
- **C-PARTIAL** for any other gate failure; **HALT** (instrument bug,
  never physics; no verdict) on any RU/RL control miss or a J-2
  identity breach.

Under every outcome: no red gate is touched; U-1's, CC-1's, TT-1's and
RS-1's recorded statuses stand; no public-record status moves; the
public paper is **not** updated (explicit owner instruction). **HARD
STOP** after the verdict, pending owner ruling (which also decides
GR2-d chartering).

## 5. Instrument contract

`calc/gr2c_reach.py`: pure Python 3 standard library; helpers imported
**unchanged** from the committed `u1_universality`, `s41_sel4`, and
`partition_selection_p1` modules; the replicated U-1 leg bodies
reproduced verbatim with this instrument's check plumbing (the GR2-b
pattern); deterministic (seeded scans only, seed 20260925); single run;
no post-hoc tuning; writes `GR2C_REACH_RESULT.json` (sha-hashed) at the
repository root with a `defect_history` field; verdict assembled from
measured variables; runtime minutes (the 80-dim exchange grid and four
joint discriminators are dense pure-Python linear algebra). Scope: the
U-1 ladder (L = 3) and two-sector+probe systems; N = 3 in the joint
cone leg; the L-X pair channel as $J_0$; the D = 4 soft-emission
algebra. Larger sector counts, probe mixtures, and the causal cone are
out of scope (GR2-d).
