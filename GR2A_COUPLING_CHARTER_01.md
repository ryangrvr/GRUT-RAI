# GR2-a — COUPLING SELECTION: CHARTER + PRE-REGISTRATION (frozen before evaluation)

**Fork:** GR2-a, second fork of the GR-2 campaign (Layer 1 of
`GR2_CAMPAIGN_DIRECTIVE_01.md`).
**Authority:** owner ruling of 2026-09-27 (`GR2_L6_OWNER_RULING_01.md`),
which authorizes GR2-a and frames its question.
**Source commits:** `master-w25bu9`; the convention replicated is the L-X
fresh pair instrument of `calc/gr1_gravity.py` (`d827a32`); recorded
gradings cited: CP-1 (`5f5bd77`), CC-1 (`17c4395`), GR-1 (`d827a32`),
P-2 (`80982c1`), TT-1 (`ff3266d`).

## 0. The question (the owner's, verbatim)

> Does anything already earned by the GRUT generative core force the +4
> low-frequency cancellation that turns the 3D ω³ phase-space factor into
> ω⁷?

Frozen disciplines from the ruling: do not assume the stress tensor, spin-2,
universal reach, or the +4 cancellation; do not use ω⁷ as a selection
criterion (exponents are outputs only; loci are defined by coefficients).

## 1. Delta over the record (what this fork asks that is not already banked)

- CP-1 found the +4 locus is a plane inside its four-parameter family and
  that cone admissibility is null as a selector. GR2-a broadens the family
  to **five local channels including the sub-base mass-modulation channel**
  (the coupling CC-1 found passing every earned constant-level selector)
  and higher-derivative channels, and tests the earned constraints
  **family-wide and earned-first**.
- New mechanical content: (i) the family's full **exponent-class law** as a
  coefficient condition, predicted per member in advance; (ii) the
  **soft-flux identification** of the +4 locus; (iii) the locus's
  **instability** to admixture of the earned-admissible channel; (iv) a
  **purely kinetic** non-stress member on the +4 locus.

## 2. The model and convention (replicated exactly from GR-1's L-X)

1D counter-propagating pair channel: dispersion $\omega(q)=q-\alpha q^3$,
$\alpha=0.05$; pair frequency $w=2\omega(q)$ solved by Newton (60 steps
from $q=w/2$); $J(w)=M(q)^2/\lvert dw/dq\rvert$; two-point slope
$\log_2[J(0.2)/J(0.1)]$. Recorded control values (full precision, from
`GR1_GRAVITY_RESULT.json`): kinetic-only 4.001626590846332, potential-only
4.003794021366405, non-minimal 4.010999254328895, full stress
8.005419679013105; exactly linear vertex identically 0; rescale deviation 0.

## 3. The coupling family (frozen)

Local quadratic couplings of the chain, reduced pair vertices in the L-X
convention (which carries one factor of $\omega_q$ relative to the
field-theoretic $\pm q$ pair amplitude — a uniform factor that shifts no
increment):

| channel | local operator | reduced vertex |
|---|---|---|
| $c_1$ U0 | on-site potential $\sum u_i^2$ (mass modulation; CC-1's channel) | $1$ |
| $c_2$ POT | bond strain $\sum(u_{i+1}-u_i)^2$, continuum $(\partial u)^2$ | $q^2$ |
| $c_3$ KIN | on-site kinetic $\sum p_i^2$ | $\omega(q)^2$ |
| $c_4$ HD | higher-derivative potential $(\partial^2 u)^2$ | $q^4$ |
| $c_5$ KG | kinetic gradient $(\partial p)^2$ | $q^2\omega(q)^2$ |

$M_c(q)=c_1+c_2q^2+c_3\omega(q)^2+c_4q^4+c_5q^2\omega(q)^2$. The GR
stress point is $c=(0,-1,1,0,0)$, identically GR-1's `v_ful`.

**The analytic class law (frozen prediction).** With
$\omega^2=q^2-2\alpha q^4+\alpha^2q^6$:
$M_c=c_1+(c_2{+}c_3)q^2+(c_4{+}c_5{-}2\alpha c_3)q^4+\alpha(\alpha c_3-2c_5)q^6+\alpha^2c_5q^8$,
so the two-point slope falls in class $\approx2p$ where $p$ is the first
nonvanishing order:
- $c_1\ne0$ → **class 0** (four below base);
- else $c_2+c_3\ne0$ → **class 4** (base);
- else $c_4+c_5-2\alpha c_3\ne0$ → **class 8** (base+4, the ω⁷ class);
- else (tested member) → **class 12**.

The **soft-flux defect** is $D(c)=c_2+c_3$ at $c_1=0$: the +4 locus is
exactly $\{c_1=0,\ D=0\}$ — the coupling's soft amplitude vanishing on the
cone — with cancellation depth beyond +4 available by plain tuning.

## 4. The member grid (deterministic; class predicted before any run)

| # | $c=(c_1,c_2,c_3,c_4,c_5)$ | description | frozen class |
|---|---|---|---|
| 1 | (0,−1,1,0,0) | the stress point (= `v_ful`) | 8 (and slope = recorded 8.005419679013105) |
| 2 | (1,0,0,0,0) | mass modulation (CC-1's earned-admissible survivor) | 0 |
| 3 | (0,1,0,0,0) | potential-only | 4 |
| 4 | (0,0,1,0,0) | kinetic-only (= `v_kin`) | 4 |
| 5 | (0,−1.3,1,0,0) | non-minimal (= `v_non`) | 4 |
| 6 | (0,0,0,1,0) | pure higher-derivative potential | 8 |
| 7 | (0,0,0,0,1) | pure kinetic gradient | 8 |
| 8 | (0,−1,1,1,0) | stress + HD admixture | 8 |
| 9 | (0,−1,1,0.1,0) | tuned deep cancellation ($c_4=2\alpha$) | 12 |
| 10 | (0.3,−1,1,0,0) | stress + mass-modulation admixture | 0 |
| 11 | (0,0.5,0.5,0,0) | symmetric mix | 4 |
| 12 | (0,−0.5,1,0,0) | partial cancellation | 4 |
| 13 | (2,0,1,0,0) | mass + kinetic | 0 |
| 14 | (0,−1,1,−0.08,0.2) | on-locus mixed ($c_4{+}c_5{-}2\alpha=0.02$) | 8 |
| 15 | (0,1,1,1,1) | all-positive potential/kinetic mix | 4 |

Members 6, 7, 8, 14 are **non-stress members of the +4 locus**; member 7 is
purely kinetic (no tracelessness narrative); member 10 shows the locus's
instability to the earned-admissible channel.

## 5. The gates (frozen, mechanical)

Controls (halt-grade; same algorithm, full-precision targets):
- **R-1..R-4:** replicate the four recorded L-X slopes, $|\Delta|<10^{-9}$.
- **R-5:** exactly linear vertex identically 0 ($<10^{-14}$).
- **R-6:** slope invariance under coupling rescale ×16 ($<10^{-12}$).

Family gates:
- **F-1:** member 1's slope equals the recorded 8.005419679013105
  ($|\Delta|<10^{-9}$): the family contains the stress point identically.
- **G-2..G-15:** each member's measured slope within **±0.2** of its frozen
  class value.

Earned-constraint gates:
- **E-1 (locality blind):** the local family exhibits all four classes
  {0, 4, 8, 12} among its members.
- **E-2 (cone blind):** every member has $J(w)\ge0$ on the scan
  $w\in\{0.10,0.12,\dots,0.20\}$ (golden-rule positivity; P-2 realizability
  of $(J,\nu{=}J/2)$ cited, not re-run).
- **E-3 (the selection rule identified):** for all 15 members, the class
  predicted by the frozen coefficient law matches the measured class —
  i.e. membership of the ω⁷ class is decided exactly by
  $\{c_1=0,\ D(c)=0\}$ and by nothing else.
- **E-4 (nonuniqueness):** members 6, 7, 8, 14 all land in class 8: the +4
  locus strictly exceeds the stress point.
- **E-5 (instability):** member 10 lands in class 0: any admixture of the
  earned-admissible mass-modulation channel destroys the +4 cancellation.

Ungated notes: recovered geometry is member-blind **by construction** (all
members couple to the same substrate, whose recovered geometry is the
substrate's; CP-1 L-G2 at $2.2\times10^{-16}$ and CA-1 leg 1 cited); the
constraint-status table of §6; the convention note of §3.

## 6. Constraint statuses to be recorded in the verdict (frozen frame)

| structure | status (recorded basis) |
|---|---|
| locality | admitted principle of the core; tested here as a selector |
| influence positivity / cone | DERIVED-IN-CLASS (P-2, borrowed-standard); tested as a selector |
| recovered geometry | member-blind by construction (identity; CP-1, CA-1) |
| conservation | **SUPPLIED** (CC-1: not derived; irreducible, reduced to the supplied massless probe) |
| Lorentz/gauge structure | **SUPPLIED** (I3; CP-1's Weyl selection is conditional on it) |
| spin-2 selection | **OPEN here** — GR2-b's question (Layer 2) |
| stress-tensor structure | **SUPPLIED** (one point of the family) |
| tracelessness / +4 cancellation | **CONDITIONAL** on the above; mechanically = the soft-flux condition $\{c_1=0, D=0\}$ |

## 7. Outcome rule (frozen, mechanical)

- **A-COUPLING-NOT-SELECTED** iff every gate holds: within the broadest
  tested local family, no earned constraint (locality, cone admissibility,
  recovered geometry) restricts the exponent class; the ω⁷ class is
  selected exactly by the soft-flux condition, which nothing earned
  imposes; the locus is nonunique (non-stress and purely kinetic members)
  and unstable to the earned-admissible channel. Consequence, in the
  ruling's pre-named form: **the GRUT core does not select ω⁷; the
  gravitational branch requires an additional primitive coupling
  structure.**
- **A-COUPLING-SELECTED-IN-CLASS** iff E-1 fails because every
  earned-admissible member collapses into class 8.
- **A-PARTIAL** for any other gate failure. Halt on any R-gate miss.

Under every outcome: ω⁷ keeps exactly its recorded status (within-class
occupancy evidence, conditional); no public-record status moves; the
GR-1 gates stay as found. **HARD STOP** after the verdict, pending owner
ruling.

## 8. Instrument contract

`calc/gr2a_coupling.py`: pure Python 3 standard library, deterministic (no
randomness), single run, no post-hoc tuning; writes `GR2A_COUPLING_RESULT.json`
(sha-hashed) at the repository root; verdict string assembled from measured
variables; expected runtime under one second. Scope travels with every
number: 1D single-sector pair channel, the L-X convention, this family.
