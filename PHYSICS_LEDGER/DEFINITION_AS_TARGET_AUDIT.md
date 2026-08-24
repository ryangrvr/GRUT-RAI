# Definition-as-Target Audit — calc/ sweep

**Date:** 2026-08-23 · PHYSICS_LEDGER · JSON: `DEFINITION_AS_TARGET_AUDIT.json` (authoritative).
No claims.json edit. No banking. Old calculations NOT rewritten.

**The failure class:** a calculation whose defining ansatz mathematically excludes the advertised
rival outcome, so it cannot test the proposition it is cited for (CHARTER §4 "definition-as-target").

**Discriminator applied [D-1]:** exclusion must come from a *free parameterization choice* (caller-set,
never derived, never swept) — not from a computed step.

## CONFIRMED DEFINITION-AS-TARGET: 2 files

### 1. `calc/wz_sign.py` — rung7_w2 / rung7_w3 no-crossing export

| field | content |
|---|---|
| claim tested | w(z) cannot cross the phantom divide for the passive vacuum |
| defining ansatz | `w(a)+1 = sign·EPS·H/H₀`, both `sign` and `EPS` caller-set constants |
| mathematical constraint | H/H₀>0 ⇒ (w+1) inherits the fixed sign of EPS·sign ∀a |
| excluded outcome | sign change of (w+1) across z |
| plant-and-recover [D-2] | swept sign∈{−1,+1}, EPS∈{−0.05,0.05,1,50}: **zero configs produce crossing** — rival unreachable, mechanically confirmed |
| downstream uses | register `rung7_w3_nocrossing_export` (`to-derive`), rung7_w2 sub_status; NO_GO_LEDGER entry 3 in-house line |
| replacement required | kernel-family scan over χ(ω) with passivity as an emergent constraint — **already built**: `PHYSICS_LEDGER/rung7_discriminator.py`; its result should become the cited artifact |

### 2. `calc/wz_dark_energy.py` — rung7_wz relaxor toy

| field | content |
|---|---|
| claim tested | single-relaxor w(z): CPL parameters + no-crossing |
| defining ansatz | `w_relaxor = −1 + eps·x²/(1+x²)`; x²/(1+x²)≥0; eps never swept through 0 |
| mathematical constraint | (w+1) inherits sign of eps ∀z |
| excluded outcome | crossing −1 within this ansatz |
| status modifier | **self-flagged**: header SUPERSEDED 2026-06-29, read "as the toy output they are" — the defect was declared before this audit, but the structural classification was missing until now |
| downstream uses | rung7_wz narrative only; superseded content |

## NOT-DEFINITION-AS-TARGET (inspected, survives)

| file | why it survives |
|---|---|
| mu_linear.py | bookkeeping-only by design; no-go export framed adversarially pre-computation |
| x_no_pin.py | pre-registered (sealed hash BEFORE file existed); default-BROKEN framing |
| kk_static_transfer.py | pre-registered sealed; tests transfer to static modulus — rival reachable |
| zeta_interior.py | default-BROKEN, both horns first-class |
| isw_exclusion.py | computes against the externally cited observable (low-ℓ cross-correlation) |
| u5u6_deformability.py | factors deformability; graduates neither claim; horns undecided |
| finite_T_pole_structure.py | re-analysis of booked overturning computation; question open either way |

## Coverage statement

35 calc files exist. Deep-read: priority subset above (10). Mechanical [D-3] grep (sign/crossing/
monotone patterns + free-parameter check) over all: remaining 25 show either computed-step
exclusions (derivations per D-1) or external-observable comparison. **Files NOT hand-read are
listed in the JSON and remain candidates at lower priority** — flagged, not cleared.
