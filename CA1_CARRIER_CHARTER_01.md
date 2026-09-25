# CA-1 — CAN "THE GRAVITATIONAL BATH IS THE GEOMETRY CARRIER" BE DERIVED? CHARTER + PRE-REGISTRATION (frozen before evaluation)

**Date:** 2026-09-25 · **Authority:** GitHub Issue #2, owner comment
**5837554943**. RS-1 was accepted at recorded strength, but not promoted.
**CARRIER** is an **unresolved supplied bridging premise** and is not
absorbed into 𝒯. RS-1's selection is of a class, relative to five
candidates, and is access-relative for fermions. Full-stress coupling
is permitted, not forced. The flexural gate stays red.

**Target (owner, verbatim):** *Can the identification "the gravitational
bath is the sector that carries the recovered geometry" be derived from
the already-earned structure, rather than imposed?*

**Outcomes:** DERIVED/SELECTED · CONSTRAINED BUT NONUNIQUE · CLASS-SPLIT ·
IRREDUCIBLE INPUT · FAILS/NULL.

**Success condition (owner):** a genuinely different carrier candidate
must be **eliminated by previously earned structure**, not by defining
CARRIER into the observables.

**Required structure, and how it is met:**
1. *At least one genuinely different sector carrying the same recovered
   geometric observable under the same access, or a construction
   showing only one can:* leg L-MC.
2. *Test influence hierarchy, access boundary, spectral geometry,
   static response and locality:* leg L-SEL.
3. *No ω⁷:* never consulted.
4. *No prior assumption of phononic, bosonic, Goldstone or linear:*
   the candidates include a z = 2 Schrödinger boson, a classical
   relaxational field and free fermions.
5. *The supplied massless gauge/Lorentz structure is kept separate:*
   RS-1's L-LOR is NOT used.
6. *RS-1's candidate set is evidence, not a premise.*
7. *Dependencies preserved:* C_cons and universal reach.
8. *Fences:* GeoInv, Sel-4x, D = 4 TT/ξ, ordering, ℏ, GR-1 3D red and
   ω⁷ untouched.

**Working hypothesis, to be attacked and not assumed:** G-2's recovered
geometric observables (heat-kernel hop metric, resistance metric) are
properties of the substrate operator K = graph Laplacian. Any sector
whose local dynamics is built on K carries them.

## 1. CANDIDATES (all on the same ring substrate, K(k) = 4 sin²(k/2))

| Label | Sector | Dynamics | Local static kernel |
|---|---|---|---|
| **P** | phonon | ü = −Ku (z = 1, quantum) | 1/K |
| **M** | Schrödinger boson | iψ̇ = Kψ (z = 2, quantum) | 1/K |
| **T** | "twin" phonon | mass 2.3, stiffness 0.7 (quantum) | 1/(0.7K) |
| **D** | classical relaxational field | ṅ = −ΓKn + noise, Γ = 1 | 1/K |
| **F** | free fermions (hopping h = −(S + S⁻¹), half filling) | non-carrier contrast | Lindhard |

## 2. THE LEGS (frozen, predictions written before any number)

- **L-MC (are there many carriers of the same recovered geometry?).**
  - (a) *Normalized resistance profile* R(0,d)/R(0,1), d = 1..32,
    N = 256. **Prediction:** identical for P, M, T and D to 1e-12,
    since the geometry is a property of K.
  - (b) *G-2 hop recovery from each sector's own short-time response*
    (ring N = 64; log-slope s(d) at t = 0.02, 0.04, 0.08 with
    Richardson extrapolation). Responses: the P and T retarded
    response [sin(√K t)/√K]; the M amplitude |[e^{−iKt}]|; the D heat
    kernel [e^{−Kt}]. The recovered distance
    d̂ = 1 + (s(d) − s(1))/(s(2) − s(1)) uses d = 1, 2 only as
    calibration. **Prediction:** |d̂ − d| < 0.3 for d = 3, 4, for all
    four carriers.
  - Frozen consequence: genuinely different sectors (different
    statistics of motion, z = 1 vs z = 2, quantum vs classical,
    different scales) carry **identical** recovered geometric data.
    "The carrier" is not unique.
- **L-SEL (does earned structure pick one carrier, or forbid a
  non-carrier bath?).**
  - **(i) Influence hierarchy (𝔠_full, the P-2 cone ν ≥ ℏJ/2, ℏ = 1).**
    For the classical carrier D, with local response
    J(ω) = (1/N)Σ_k Γω/((ΓK_k)² + ω²) and classical noise
    ν = (2T/ω)J:
    - T = 0: min(ν − J/2) < −1e-3 at ω = 1 (**violates the floor**);
    - T = 0.5: admissible at ω = 1 (ω ≤ 4T) but **violates** at ω = 3.
    - Frozen consequence: the cone **eliminates the classical carrier
      at every temperature** (at high enough ω). This is an earned
      elimination of a genuinely different carrier candidate. The
      quantum carriers P, M and T sit on the floor in vacuum (P-2,
      GR-1 L-H; noted, not re-gated).
  - **(ii) A non-carrier bath: is it excluded?** For F, with geometry
    recovered through a carrier:
    - F's own hop recovery from its amplitude [e^{−iht}]: |d̂ − d|
      < 0.3 for d = 3, 4 (it shares the graph);
    - F's local additive metric **fails** (RS-1's A ≈ 1.02,
      recomputed);
    - F is 𝔠_full-admissible (its fermionic vacuum sits on the floor,
      noted by construction).
    - Frozen consequence: a bath that does **not** carry the additive
      recovered metric passes influence positivity, locality and
      hop-geometry recovery. **Earned structure does not force the
      gravitational bath to be the geometry carrier.**
  - **(iii) Access: which carrier is the bath?** Among the surviving
    carriers {P, M, T}, all admissible with identical geometry, which
    one the gravitational probe couples to is an **access declaration**
    (P-6: the access seed is irreducible). CARRIER therefore reduces to
    the coincidence *"the gravitational probe's access seed equals the
    geometry-recovery access seed"*, which is supplied.

## 3. OUTCOME RULE (frozen, mechanical)

- **Carrier set:**
  - the carriers are the candidates passing L-MC (a) and (b);
  - earned structure cuts those failing L-SEL(i);
  - if more than one remains: **CONSTRAINED-NONUNIQUE**;
  - the owner's bar is met for the carrier set iff at least one
    genuinely different carrier is cut by earned structure.
- **CARRIER as an identification:** **DERIVED** only if exactly one
  carrier survives AND the non-carrier bath F is excluded by earned
  structure. If F survives: **IRREDUCIBLE INPUT**, reduced to the
  access-seed coincidence (P-6).
- **Overall:** the components are reported separately.

## 4. CONTROLS

- Halt-grade: the P-kernel exact ring identity (RS-1) is reproduced.
- Halt-grade: the D noise-floor identity: at T = 0 the classical noise
  is exactly 0 while J > 0.
- Matrix powers are computed exactly by vector iteration; series
  truncation is m ≤ 20 at t ≤ 0.08.
- No ω⁷ and no L-LOR anywhere.

## 5. DELIVERABLES AND STOP

1. `calc/ca1_carrier.py` (pure stdlib; emits `CA1_CARRIER_RESULT.json`,
   sha-hashed).
2. `CA1_CARRIER_VERDICT_01.md` and a closing comment on Issue #2.
3. **HARD STOP after the CARRIER verdict.** No geometry selection or
   TT/ξ.
