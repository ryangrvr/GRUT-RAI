# C1-a — THE STATIONARITY SEAM: DOMAIN-EXTENSION ATTACK ON ε. VERDICT

**Date:** 2026-09-25 · **Charter:** `C1_STATIONARITY_SEAM_CHARTER_01.md`
(frozen at `fa6ac44` before the run) · **Authority:** owner ruling on
Formalization 02 — the program's **first completion attack**. ·
**Instrument:** `calc/c1_seam.py` · **Artifact:** `C1_SEAM_RESULT.json`
(sha `39e8c864d1b1ddbc…`) · **Gated battery 10/12, two frozen reds
(both in L-B), zero halts, single run.**

Halt-grade identities held: bath-propagator composition to 1.0e-17;
exact stationarity restoration at ε_m = 0 to 7.8e-16; multi-time Gram
positivity to 8.6e-14 (tamper detected at −0.160); Bernstein weights
non-negative in every epoch. The FRW/cosmological kernel was never
used as the model; no C2 content; ω⁷, Class-4, GR-1 and the closed
forks untouched; no absolute exponent computed.

## VERDICT (per component, by the frozen mechanical rule)

> | component | outcome |
> |---|---|
> | **the map ε** | **DERIVED EXTENSION (in-class):** ε extends constructively from stationary to stepped nonstationary microscopic dynamics. The S-level solve — using **only** the per-epoch spectral data {λ_e, u_e}, the mixing matrices C = V_newᵀV_old, and K_SS — reproduces the exact full dynamics to **1.0e-12** (h→h/2 ratio 17.85: the residual is integrator error; the reduction itself is exact). |
> | **continuity** | **ESTABLISHED:** K(t,s) collapses to K(t−s) **exactly** when time-translation invariance is restored (7.8e-16), and the kernel's deviation is linear in the TTI-breaking amplitude (dev(0.02)/dev(0.01) = 1.9968). The owner's outcome-1 clause is met in-class. |
> | **earned structure** | **PRESERVED:** passivity (min eig K(t) = 0.300 > 0; ‖x(t)‖ monotone); **hierarchy positivity extends verbatim** — the multi-time Gram is PSD off the stationary domain, exactly as the identity "hierarchy admissibility = state positivity" predicts, and the ×1.5 tamper is caught; every frozen-epoch snapshot stays in the completely monotone class. **No outcome-3 failure anywhere.** |
> | **stationary packaging** | **NOT MECHANICALLY CERTIFIED — two frozen gates red, kept red** (below). The construction still *exhibits* the priced datum; the certification of the boundary awaits the owner. |
> | **composite** | **PARTIAL, in the frozen rule's own words:** the map, continuity, and structure components — the crossing of S1 at finite level, in-class — are **established**. The packaging-boundary component is observed but not certified. |

## WHAT THE RUN SHOWED

**1. Seam S1 is crossed constructively at finite level, in the tested
class.** The formalization's map ε, previously **[UNDEFINED]** off
stationary backgrounds, is now defined and exact on stepped
nonstationary M(t) ∈ 𝕆_G at finite N: the reduction is closed at S
level, its error is pure integrator error with the correct fourth-order
signature, and it is size-independent (N = 12 diagnostic: 1.0e-12).

**2. The admissibility structure does not care about stationarity.**
This is the run's cleanest structural point: the frequency-domain cone
(J, ν)(ω) needs a stationary state to be defined at all, but the
hierarchy-level object — Gram positivity of multi-time moments — is
the stationarity-independent formulation, and it held at 8.6e-14 with
a detecting tamper. The earned admissibility layer survives the
crossing **because it was always the state-positivity identity, never
a property of stationarity.**

**3. The two-time datum is exhibited, constructively.** The solver
that passes L-E consumes exactly: per-epoch spectral data **plus the
mixing matrices C = V_newᵀV_old**. In the stationary theory the datum
is one spectral measure; here it is provably more — the mixing datum
is the concrete, minimal-looking form of "the bath propagator family."
This converges, from the microscopic side and with no cosmological
input, with what the kernel-transport verdict found from the FRW side
(its three relocation-class items). The convergence is reported, not
promoted.

## THE TWO FROZEN REDS (kept red)

- **L-B(a):** same-lag drift D = **0.0498**, frozen gate > 0.1.
- **L-B(b):** local-anchor family worst errors 0.0562 / 0.0783 /
  **0.0494**, frozen gate > 0.05 for **every** member — the midpoint
  member missed by 0.0006; two of three members passed.

**Labeled post-hoc diagnostic (added after the failures; no gate
repaired):**
- *(i) a normalization artifact:* the frozen D divides by
  max|k| = k(0) = vᵀv, which is **modulation-independent**; measured in
  the kernel's own local scale, the lagwise relative drift reaches
  **0.118** and exceeds 0.1 for all τ ≥ 0.4.
- *(ii) amplitude scaling:* at ε_m = 1.0 (twice the frozen working
  point) D = 0.0887 and the anchor family reads 0.1095 / 0.1484 /
  0.0968 — the misses scale with the TTI-breaking amplitude, exactly
  as L-S(b)'s measured linearity implies. The frozen 0.1 / 0.05
  thresholds were **miscalibrated against the frozen normalization and
  working point, not against the phenomenon.**
- *(iii) what is established regardless of the reds:* the generated
  kernel **is** genuinely two-time — drift 5.0e-2 against a 7.8e-16
  stationary control, a thirteen-orders separation — and that fact
  rides the halt-grade control, not the red magnitude gate.

**Effect on the outcome:** the frozen rule requires both L-B gates for
PRINCIPLED DOMAIN BOUNDARY, so that component is **not mechanically
certified**, whatever the diagnostics suggest. The reds are the
record. Disposition options that belong to the owner, not this
instrument: accept the diagnostic characterization as sufficient, or
charter **C1-a2** (re-frozen packaging gates with the corrected
normalization), or leave the component open.

## STRENGTH AND LIMITS (stated plainly)

- **In-class means in-class:** finite, first-order passive local
  networks, stepped (piecewise-stationary) modulation. Stepped
  protocols genuinely break TTI, but smooth modulation (**C1-c**) and
  the infinite-volume nonstationary limit (**C1-b**) are named
  successors, not covered. A verdict here claims nothing about either.
- **The L-E test's independence is structural, not epistemic:** the
  reduced solver is mathematically equivalent to bath dynamics in
  eigen-coordinates — the point is that the S-level description
  **closes** on the named datum, which is the map-extension claim, not
  a claim of new dynamical content.
- **The separable-rank diagnostic (16/16 on the sampled grid) is
  reported only.** No realization-dimension law is claimed off the
  stationary domain.
- **The mixing datum is exhibited, not proved minimal.** Whether some
  smaller datum suffices is exactly the question a certified packaging
  boundary would close.

## EFFECT ON THE FORMALIZATION (statement, no edit made)

If the owner accepts this verdict, Formalization 02's map table
changes one row at stated scope: ε gains **CONSTRUCTIVE (stepped
nonstationary, finite, in-class)** alongside its stationary domain,
with S1's remainder relocated to {C1-b, C1-c, the packaging
certification}. The hierarchy-positivity row gains the note that
admissibility is stationarity-independent by measurement, not only by
identity. No other object or coordinate moves. The edit itself awaits
the ruling.

## LEDGER (unchanged except as stated)

κ discharged · C_cons irreducible (massless probe) · universality
derived under exchange, reach supplied · retained sector conditional
(CARRIER + probe) · CARRIER = access-seed coincidence · geometry
access-relative · Sel-4x = co-stretch declaration · ξ dead in physical
TT · TT channel existence class-split · ℏ located · GR-1 3D red ·
Class-4 OPEN · ω⁷ occupancy evidence only; v3 closed · operator
ordering fenced. **New, this fork:** ε extends across S1 at finite
level in-class (map + continuity + structure); packaging boundary
observed, uncertified, two reds preserved.

## HARD STOP

Hard stop after the C1-a verdict, as chartered. The decision this stop
waits on: **the owner rules on the verdict — including the disposition
of the two L-B reds (accept the diagnostic characterization, charter
C1-a2, or hold) — and whether the Formalization 02 map-table edit is
authorized.** C1-b and C1-c remain named, not opened. No C2 work was
done or is started.
