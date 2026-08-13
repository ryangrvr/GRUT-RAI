# The rigorous μ/η/Σ pass across the interior (the graduation-path calc)


> **ANCHOR CORRECTION (2026-08-03, `calc/isw_exclusion.py`):** the ~32σ anchor was computed and **not confirmed** (cross-channel N(1) ~ 2.0σ, Σ-corrected; binding inversion — lensing binds at x < ~0.59 loose-upper per F-MAP). The family identities (μ/η/Σ, exact) are untouched; the edge-value table below stands as the historical record only.

*Closes the first pass's named fences at the inherited-bookkeeping level. Code: `calc/mu_slip_interior.py` (pure stdlib; imports and verifies against `calc/mu_linear.py` — the banked source of truth for the endpoints). Register: appended to `zeta_interior_family.boundary_condition`. Default-BROKEN: the win is closed fences and a confirmed edge — the family allows, it does not predict.*

---

## What closed

- **F1 (linearity):** μ(x) = 1 + xα is **exact** in the inherited bookkeeping — the scalar coupling enters the Poisson sector linearly. The first pass's "leading-order interpolation" fence closes at this level.
- **F2 (slip/Σ):** η(x) = 1/(1+xα), **inherited from the same one-sided structure** (the coupling enters the Ψ-equation only; Φ stays GR — η = 1/μ is *conditional* on that one-sidedness, which `mu_linear.py` postulates; a genuine P0s admixture could split the law via scalar anisotropic stress — R2's case). Given it, **Σ(x) − 1 = (μ(x) − 1)/2 is an identity for all x** (machine-checked; endpoints reproduce `musigma("TT")`/`musigma("trace-only")` exactly). The "slip owed" fence closes **at the inherited-bookkeeping level** — exact-in-bookkeeping, family-wide.
- **F3 (ISW scaling), partly:** x is a **pure amplitude rescale** of one fixed modification shape, so the template is x-independent and N_σ(x) = 32x is **leading-order-exact given the fixed template** — the bookkeeping itself contains no ISW dynamics; signal linearity is an additional leading-order dynamical statement with **O((xα)²) growth-feedback corrections (~2% at the edge), a small named family-side softness**. The **anchor's own O(1) softness also remains** (the ~32σ number is an in-house-derived exclusion significance, `calc/isw_exclusion.py` owed, not in-repo).

## The confirmed edge (2σ, all three observables)

| observable | value at the edge x = 1/16 |
|---|---|
| μ − 1 | **α/16 ≈ 0.0208** |
| Σ − 1 | **α/32 ≈ 0.0104** |
| 1 − η (slip deviation) | **≈ 0.0204** |

## What stays open (named, the node's continuing to-derive content)

**R1** the x↔c₀ action-level map (one-dial bookkeeping → the P0s modulus normalization; partly frontier-reserved, conformal/Riegert–Paneitz). **R2** the inherited model question (one scalar dial; a richer model could split Poisson-vs-slip couplings) — owned by the open `mu_linear` demotion screen. **R3** the u5-facing dynamics classification. The family **allows** deviations up to the edge; it predicts none (x has no floor).

## Independent firewall (2026-08-02) — amber → green after tightening

Physics + fidelity lenses + adjudicator; **no blocker**. Verified: the α → xα rescale is the correct one-dial generalization (Ψ-only coupling *forces* μ=1+c, η=1/(1+c), Σ=1+c/2 for any coupling c); all algebra machine-exact; edge numbers 1/48, 1/96, 1/49 confirmed; closures honestly scoped; R1/R2/R3 named everywhere; no stealth graduation (to-derive/0, 45 nodes, +13 unchanged). Tightenings applied: η=1/μ marked *inherited-conditional on one-sidedness* (postulated in `mu_linear.py`, not computed; the P0s-split case is R2's); "exact-in-bookkeeping" ISW scaling corrected to *leading-order-exact given the fixed template* with the ~2% growth-feedback nonlinearity named as **family-side** softness; ToE §2.8's "every GRUT observable… 20+ orders" over-generalization weakened to the banked record; the changelog gains the allows-not-predicts shading; the endpoint-variance direction mechanism spelled out.
