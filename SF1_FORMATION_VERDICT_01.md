# SF-1 — FORMATION VERDICT 01

> **ACCEPTED (owner ruling 02, Issue #2 comment `5903593151`; `SF1_OWNER_RULING_02.md`):**
> - **SF-1 = FORMATION-OF-LAW-CLASS** (terminal at frozen scope).
> - **C-6 = MULTISCALE / PATH-DEPENDENT IR** (report-only).
> - No re-run.
> - **Terminology fence:** read "law class" as **effective-law / IR universality class**. The
>   microscopic law did not change.
> - **Architectural consequence:** *a supplied sector does not imply a supplied effective law.*
>
> The verdict below is preserved as filed.

**Mechanical terminal: FORMATION-OF-LAW-CLASS.**
**C-6 (report-only): MULTISCALE / PATH-DEPENDENT IR.**

**Status: proposed for owner adjudication. HARD STOP.**

## Provenance

| Item | Value |
|---|---|
| Frozen charter | `SF1_FORMATION_CHARTER_01.md` at `8a4f71c` (sha256 `31142088c8fd…`) |
| Authority | `SF1_OWNER_RULING_01.md` (comment `5903400225`); one run; v4 exception for SF-1 only |
| Script | `calc/sf1_formation.py`, committed at `840b3c3` **before** execution (sha256 `63eadfddd46f…`) |
| Result | `SF1_FORMATION_RESULT.json` (sha256 `65a026fc0901…`) |
| Executions | **One** (6 s wall clock). No defects were recorded, and nothing was re-run. |

**Pre-run disclosures:**
- **Pre-run code review fix, made before the run and included in `840b3c3`.** The first draft of
  the script computed particle–hole energies as −2cos k₂ + 2cos k₁. At large L that form loses
  about 9 digits to cancellation, which would have falsely failed the frozen 10⁻¹² ω₁ check. The
  draft now uses the exact identity 4 sin(π(2j+m)/L) sin(πm/L).
- **Tooling test.** sympy's limit machinery was exercised on **non-member** toy expressions
  (ν = 1/3, N = L−5, N = 5√L) to rule out a tooling crash. No SF-1 member was computed before the
  run.
- **Implementation thresholds not in the charter.** They were used only to *verify* the exact
  soft-point candidates of I-q:
  - the value at q* ± 10⁻¹² must be below 10⁻⁹;
  - in a 2×10⁵-point scan, no other point with ω⁻ < 10⁻⁴ may lie more than 2×10⁻² from a candidate.

## 1. Integrity (all pass)

| Control | Result |
|---|---|
| **C-5** | Pass. One parent (`bonds`, `eps`, `fock_H`) and one readout (`occupied`, `ff_support`, `fock_sector_support`) serve every sector. None takes a family or sector tag, and none references the family table. Source hashes are recorded. |
| **V-FOCK** | Pass. H_F was built once per L on the full 2^L Fock space (L = 6, 10, 12), with Jordan–Wigner signs and the periodic bond. For all 12 sectors: <ul><li>the sector ground state is unique (gap ≥ 0.268);</li><li>E₀ matches the analytic Σ ε;</li><li>for every q, the grouped ρ_q support equals the I-FF particle–hole set;</li><li>the weights are unit per particle–hole state.</li></ul> |
| **A-ODD** | Pass on 41 sectors. <ul><li>Symmetric fill: k = 0 plus complete ±k pairs.</li><li>Strictly positive Fermi-edge gap.</li><li>Odd-hole statement: k = π plus pairs.</li><li>Agreement with the Fock E₀ and with uniqueness.</li></ul> |
| **C-1** | Pass. <ul><li>(Fock) Spectra and supports coincide for N ↔ L−N at every V-FOCK L.</li><li>(Family) class(D-¼) = class(D-¾) and class(E) = class(Ē).</li><li>**Quotient verified:** the raw 2k_F representatives are π/2 (D-¼) and 3π/2 (D-¾). They differ before the quotient and coincide after it.</li></ul> |
| **Closed form vs numeric** | Pass for every non-C-6 family. <ul><li>The worst P-check deviation is 0.143 of the frozen tolerance.</li><li>The ω₁ closed form matches enumeration to relative 0.0 at every L.</li></ul> |

## 2. Invariants (closed form; common prescription)

| Family | k_F^∞ | Small-q lower edge ω⁻(q) (P) | **I-z = z_P** | ω₁(L) (P′) | z_{P′} | Soft set (mod q~−q~q+2π) | **I-q** | Class |
|---|---|---|---|---|---|---|---|---|
| **D** (ν=½) | π/2 | 4 sin(q/2) cos(q/2) | **1** | 4 sin(π/L) | 1 | {0, π} | **2** | (1, 2) |
| **E** (N₀=1) | 0 | 4 sin²(q/2) | **2** | 4 sin²(π/L) | 2 | {0} | **1** | (2, 1) |
| D-¼ | π/4 | 4 sin(q/2) cos(q/2 + π/4) | 1 | 2√2 sin(π/L) | 1 | {0, π/2} | 2 | (1, 2) |
| D-¾ | 3π/4 | 4 sin(q/2) cos(q/2 + π/4) | 1 | 2√2 sin(π/L) | 1 | {0, π/2} | 2 | (1, 2) |
| E-3 | 0 | 4 sin²(q/2) | 2 | 4 sin(π/L) sin(3π/L) | 2 | {0} | 1 | (2, 1) |
| Ē (N = L−1) | π | 4 sin²(q/2) | 2 | 4 sin(π/L) sin(π(L−1)/L) | 2 | {0} | 1 | (2, 1) |

The numeric log-slopes of ω₁ are reported, not gated:
- D, D-¼ and D-¾: 1.0000;
- E and Ē: 2.0000;
- E-3: 1.9998 → 2.0000.

## 3. Mechanical terminal (charter §7)

1. **Integrity:** all pass, so the run is not void.
2. **SECTOR-SMUGGLED:** no. It is decided by the C-5 audit, which passed. It therefore cannot fire
   independently at this step, and that is stated rather than hidden.
3. **UNFORMULABLE:** no. Every class is defined.
4. **class(D) = (1, 2) ≠ class(E) = (2, 1).** Both I-z and I-q differ.
5. Controls:
   - **C-4** holds in all six families: z_P = z_{P′}.
   - **C-2** holds: D-¼ ≡ D.
   - **C-3** holds: E-3 ≡ E.

   The terminal is therefore **FORMATION-OF-LAW-CLASS.**

## 4. C-6 report (REPORT-ONLY; no terminal effect)

- **Family:** N_L = nearest odd(√L) = 17, 33, 65, 129, 257, on L = s² + 1.
- **Scale:** k_F(L) = π(N_L − 1)/L. Its symbolic exponent is **−1/2**; the numeric log-slopes run
  −0.476 → −0.497.
- **P** (k_F → 0 at fixed q first) gives **z_P = 2**.
- **P′** (q = 2π/L) gives ω₁ = 4 sin(π/L) sin(πN_L/L) ~ L^{−3/2}, so **z_{P′} = 3/2**. The numeric
  slopes run 1.496 → 1.4999.
- There is **no unique one-parameter z**, so the label is **MULTISCALE / PATH-DEPENDENT IR.**
- **Reading:** the two vanishing scales are k_F(L) ~ L^{−1/2} and q ~ L^{−1}.
  - P lets k_F vanish first and sees the band bottom.
  - P′ probes q ≪ k_F and sees v_F(L) q with v_F ~ L^{−1/2}.

This is the two-scale regime the owner anticipated. Per ruling §2 it is not a defect and not a
negative terminal.

## 5. Allowed statement (ruling §7 wording fence, verbatim)

> **Within one fixed free-fermion microscopic parent, different exact conserved particle-number
> scaling sectors support inequivalent IR effective-law classes under the preregistered
> density-response coarse-graining.**
>
> **The result concerns distinct asymptotic sector scalings; intermediate sub-extensive
> particle-number scalings form a crossover/multiscale regime rather than a third preregistered
> terminal class.**

## 6. Scope qualifications (carried; not reasons to demote)

1. **The sector is supplied.** It is selected by conserved boundary/state data. The reference state
   is the declared sector ground state; nothing relaxes to it. This is **not** dynamical selection
   and not attractor formation.
2. **The contrast is textbook physics.**
   - The linear Fermi-point excitations at finite density and the quadratic band-bottom dispersion
     in the dilute limit are standard one-band facts.
   - SF-1's contribution is procedural: the contrast survives the program's frozen formation gate.
     That means one full-Fock parent, one readout and one coarse-graining, with PH, filling, N₀ and
     limit-order controls and the SF-0 quotient.
   - It is not a new condensed-matter result.
3. **Both classes come from the same ε(k) = −2 cos k.** The conserved sector selects **which region
   of the one band is the IR**: the Fermi points or the band bottom. This is the R-F = (b) reading
   (excitation law of the sector restriction), adopted by owner ruling. It is not the single-particle
   law read alone.
4. **The dilute class is an asymptotic density-zero scaling sector.** C-6 shows that the dense and
   dilute classes are separated by a path-dependent crossover. The binary classification is
   **not exhaustive** over all particle-number scalings.
5. **The parent is quadratic (free).** Nothing here addresses interacting parents, and the parent
   was not replaced or modified.

## 7. What this does not establish (ruling §5 / §7)

This does not establish:
- universes;
- domain formation;
- varying constants;
- cross-universe mixing;
- the origin of constants;
- that GRUT's substrate has this property;
- that S-5 is solved;
- any cosmological or empirical claim.

## 8. HARD STOP

- Result and verdict committed; CURRENT_STATE updated.
- **Awaiting owner adjudication.**
- There is no second run, no SF-2, and no migration of the result to cosmology or to GRUT's
  fundamental substrate.
- S-5 stays HELD pending the owner's ruling.
