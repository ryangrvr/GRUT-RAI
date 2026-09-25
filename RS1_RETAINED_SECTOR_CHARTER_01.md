# RS-1 — IS THE GAPLESS PHONON SECTOR SELECTED, OR MERELY CHOSEN? CHARTER + PRE-REGISTRATION (frozen before evaluation)

**Date:** 2026-09-25 · **Authority:** GitHub Issue #2, owner comment
**5837437988**. U-1 is accepted at recorded strength. **Binding
record:**
- universality is derived only where exchange is present, and is
  irreducible for genuinely decoupled sectors;
- **universal reach / exchange-carrying coupling is SUPPLIED**;
- g → 0 is continuous, not a physical discontinuity;
- C_cons is irreducible, reduced to the supplied massless gauge probe;
- GeoInv and Sel-4x are unearned.

**Target (owner, verbatim):** *Can the gapless phonon sector used by
GR-1 be selected from the earned influence/access/geometry structure
plus the supplied massless gauge probe, rather than being simply chosen
as the bath?*

**Outcomes:** DERIVED/SELECTED · CONSTRAINED BUT NONUNIQUE ·
CLASS-SPLIT · IRREDUCIBLE INPUT · FAILS/NULL.

**Success bar (owner):** a retention selector must **eliminate at least
one genuinely different gapless candidate using previously earned
structure.** Compatibility is not selection.

**Declared bridging premise (named, not assumed earned):**
**CARRIER** says *the retained sector is the sector whose local static
response carries the G-2-recovered long-range metric* (the additive
resistance geometry of G-2 L-F). G-2 earned that this geometry is
recoverable. CARRIER is the identification that the gravitational bath
*is* its carrier. Every elimination by the geometry selector below is
therefore **conditional on CARRIER**, and the verdict reports it that
way.

**Fences:**
- **ω⁷ is never used to select.** No selector below consults the GR-1
  exponent.
- GeoInv, Sel-4x, D = 4 TT/ξ, operator ordering and geometry selection
  stay separate.
- The FS-1 conserved tower and dynamic-insensitivity results are
  preserved (matched control).
- ℏ located; GR-1 3D red.

## 1. THE CANDIDATES (genuinely different, exactly solvable, frozen)

All on a ring of N = 256 unless stated, with K(k) = 4 sin²(k/2):

| Label | Sector | IR dispersion | Local static kernel χ(k) |
|---|---|---|---|
| **P** | phonon (unpinned harmonic chain), GR-1's | ω = 2 sin(k/2), z = 1 | 1/K |
| **F** | free fermions at half filling (XX via Jordan–Wigner), gapless | δε = 2 sin p from the Fermi point, z = 1 | T = 0 Lindhard density response |
| **M** | ferromagnetic magnon (Schrödinger boson, ψ†Kψ), gapless | ω = K, z = 2 | 1/K (Re ψ) |
| **B** | flexural/bending chain (ω² = K²), gapless | ω = K, z = 2 | 1/K² |
| **G** | gapped control (pinned phonon, m² = 0.25) | ω = √(0.25 + K) | 1/(K + 0.25) |

M and B share a dispersion but differ in static structure; P and F
share an IR class (z = 1) but differ in statistics and in their local
static response. So each selector can be seen acting on one property
at a time.

## 2. THE LEGS (frozen, predictions written before any number)

- **L-GEO (earned geometry: what does additive metric recovery
  select?).**
  - *Setup:* the G-2 resistance form R(0,d) = (2/N) Σ_{k≠0} χ(k)
    (1 − cos kd); the additivity ratio A = R(0,16)/R(0,8).
  - **Predictions:**
    - P: A ∈ [1.8, 2.2];
    - M: A ∈ [1.8, 2.2];
    - B: A > 4 (cubic, not additive);
    - G: A < 1.3 (screened);
    - F (local density): A < 1.3 (compressible, saturating).
  - Also: F's *non-local* bosonized phase field
    φᵢ = Σ_{j≤i}(n_j − ½), with χ_φφ = χ_nn/K, gives A ∈ [1.8, 2.2].
    Frozen consequence: F's elimination is **access-relative**. It
    holds under G-2's local access; a non-local string observable
    would restore it, as bosonization implies.
  - Frozen consequence: given CARRIER, earned geometry eliminates
    **two genuinely different gapless candidates (F and B)** and the
    gapped control. The survivors are {P, M}.
- **L-LOR (the supplied probe structure: Lorentz/boost compatibility of
  the sector's stress).**
  - *Setup:* a massless spin-2 gauge probe needs a symmetric conserved
    source, T^{0x} = T^{x0}. For quasiparticles that means
    v_g·v_p = v² is constant in the IR (a boost-compatible light
    cone). The test ratio is r = v_g v_p(k₂)/v_g v_p(k₁), with
    k₁ = 2π·2/N and k₂ = 2k₁; v_g is taken by central difference.
  - **Predictions:**
    - P, F, G: |r − 1| < 0.05 (compatible);
    - M, B: r ∈ [3.5, 4.5] (v_g v_p ∝ k², so no symmetric stress
      tensor in the IR, and they cannot source the supplied probe
      consistently).
  - The value v = c per sector is a units choice. Cross-sector light
    cones are U-1 territory and not tested here.
- **L-ST (does the gauge structure FORCE full-stress coupling or merely
  PERMIT it?).** Rerun CP-1's D = 2 conservation null space on the
  declared bilinear family. **Prediction:** nullity 2 (canonical plus
  ξ-improvement), so conservation *permits* canonical full-stress
  coupling but does not *force* it. Carried, not re-tested: IR Weyl
  fixes ξ = 0 in D = 2 (CP-1), and TT probes see a rank-1, vacuous
  form (CP-1).
- **Matched control:** the FS-1 phonon conserved tower at R = 2 has
  dim **4** (recomputed).

## 3. OUTCOME RULE (frozen, mechanical)

- **Earned selection (conditional on CARRIER):**
  - it meets the owner's bar iff L-GEO eliminates ≥ 1 gapless
    candidate;
  - the surviving set is reported;
  - if more than one gapless candidate survives:
    **CONSTRAINED-NONUNIQUE** (earned).
- **With the supplied probe structure (L-LOR):** if the intersection of
  survivors is {P} alone, **SELECTED-IN-CLASS, conditional on CARRIER
  plus the supplied Lorentz/gauge structure, relative to the tested
  candidate set.** If it is larger, CONSTRAINED-NONUNIQUE. If empty,
  FAILS.
- **Stress coupling:** "permitted, not forced" if L-ST nullity is 2.
- **Overall:** CLASS-SPLIT across the layers (earned vs earned +
  supplied), with every conditioning premise named.
- Nothing is DERIVED outright unless the earned layer alone leaves {P}.

## 4. CONTROLS

- Halt-grade: the exact finite-ring identity R(0,d) = d(N − d)/N for
  the P kernel, to 1e-9.
- Halt-grade: the Lindhard sum's q → 0 limit equals the Fermi-level
  density of states 1/(π v_F) with v_F = 2, i.e. 1/(2π), per site
  within 2%.
- The zero mode (k = 0) is excluded from all bosonic sums.
- There is no ω⁷ consumption anywhere.

## 5. DELIVERABLES AND STOP

1. `calc/rs1_retained.py` (pure stdlib; emits
   `RS1_RETAINED_RESULT.json`, sha-hashed).
2. `RS1_RETAINED_SECTOR_VERDICT_01.md` and a closing comment on
   Issue #2.
3. **HARD STOP after the retained-sector verdict.**
