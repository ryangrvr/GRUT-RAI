# Concrete Task List for the Brother

## What we need from you

Three yes/no answers. Total time: 2-4 focused hours with papers in hand.

---

## Task 1: Answer Q1 (30-60 minutes)

**Question:** Does the CTP effective action on a curved background naturally
produce the local-coupling anomaly ε (Osborn 2003) rather than the
constant-coupling ratio b/a (standard Birrell-Davies)?

**How to answer:**

Open Osborn 1991 (NPB 363, 486). Find the specific statement in Section 3
about what anomaly structure appears when the couplings are space-dependent
(local) versus constant. The paper explicitly distinguishes these cases.

Then consider: in the CTP/Schwinger-Keldysh construction on de Sitter, are
the SM couplings effectively local (running with Hubble scale) or constant?

**Deliverable:**

Write one of these three sentences in an email:

- (A) "The CTP construction on curved spacetime produces the local-coupling
  anomaly structure, so ε is what enters the cosmological formula, not b/a."
- (B) "The CTP construction produces the constant-coupling anomaly structure,
  so b/a is what enters; the ε match is a coincidence."
- (C) "The CTP produces a mixture; here's the specific combination: [formula]."

Your answer determines whether we're done or have more work.

---

## Task 2: Answer Q2 (60-90 minutes)

**Question:** For single-group dominance (QCD at 98.8% of the net SM
correction), does the consistency-relation chain simplify?

**How to answer:**

Open Osborn 1991, look at eq (30) — the Weyl consistency condition
[Dσ, Dσ'] = 0 — and the eq (31) family that follows. These give relations
between ε (via χ^f_ij in Osborn's 1991 notation), w_i, β_b, and other
anomaly coefficients.

For a single gauge coupling g (ignoring other SM groups since they contribute
1.2% of the effect), what does the chain

    ε → (via consistency) → w_g → L_β w_g → Δβ_b → Δ(b/a)

produce at leading order? Are there additional factors (loops, integration
over scales, scheme redefinitions) that move R away from ε?

**Deliverable:**

One of these three sentences:

- (A) "At single-group dominance, the chain simplifies: ΔR = ε − 1 at
  leading order, so R_eff ≈ ε_SU3 = 1.160."
- (B) "The chain introduces factor X: ΔR = Xε, with X = [value], so
  R_eff = [number] ≠ ε_SU3."
- (C) "The chain requires integration over scales; ε is only the leading
  piece. Full R_eff requires the integrated calculation."

---

## Task 3: Answer Q3 (30 minutes)

**Question:** Is there a known identity in the Weyl-anomaly / CFT literature
relating ε and b/a in any specific limit?

**How to answer:**

Search your memory / textbook knowledge for:

- Theorems relating local-coupling anomaly coefficients to constant-coupling
  anomaly coefficients in a specific limit (free-field limit, large-N, CFT
  fixed point, supersymmetric)
- Any result in Osborn's papers or followups (Jack-Osborn 1990, Komargodski-
  Schwimmer 2011, Prochazka-Zwicky 2017) that bridges these

**Deliverable:**

One of:

- (A) "Yes, theorem X says ε = b/a when [condition]. In our case [condition]
  applies / doesn't apply."
- (B) "No known identity connects them. They are structurally independent
  objects."
- (C) "Reference: [paper, section]. Read this for the answer."

---

## What Ryan does with your answers

### If Q1 = A and Q2 = A:

Framework is derived. Ω_Λ = 0.689 comes from SM QCD trace anomaly at M_Z
with zero free parameters. This is publishable as-is.

Ryan updates the v7 appendices:
- Remove "R = 1.15428 asserted" language
- Replace with "R = ε_SU3(M_Z) = 1.160 from Osborn 2003 eq (36) evaluated
  for SM Dirac field content at the electroweak scale"
- Status: DERIVED (was CONDITIONAL)

### If Q1 = A and Q2 = B or C:

Partial derivation. ε_SU3 is structurally the right object but needs
correction factor X. The cosmological prediction is then X × 1.160, and
we check whether that matches 1.154 or not.

### If Q1 = B:

The 0.46% was coincidence. Return to integrated w_g calculation (prior
derivation steps doc). Still publishable as a negative result on a
specific, tested mechanism.

### If Q3 provides a known identity:

That's the fastest path. If a published theorem says ε = b/a in some limit
and we're in that limit, we're done.

---

## What NOT to do

1. Don't try to make the answer be yes. If the chain doesn't simplify,
   report that honestly.

2. Don't compute the integrated flow from scratch yet. Answer Q1/Q2/Q3
   first. The integration is only needed if Q1 = B.

3. Don't pick a convention to make numbers agree. You already established
   Dirac convention via the SUSY cross-check; stick with it.

4. Don't assume single-group dominance justifies treating SU(2) and U(1)
   as zero. They're 1.2% of the effect, but that's still ~0.3 in R units,
   which would move the 0.46% proximity into 0.2% or 0.7% depending on
   sign.

---

## Format for your reply

Email or text, three sentences:

    Q1: [A/B/C with brief reasoning]
    Q2: [A/B/C with brief reasoning]  
    Q3: [A/B/C with reference if applicable]

Ryan will plug the results into the Python pipeline and produce Ω_Λ —
whatever the number comes out to be.

---

## Papers you'll need open

1. Osborn 1991, NPB 363, 486 — https://www.damtp.cam.ac.uk/user/ho10/loc.pdf
   (eq 28, 29, 30, 31)

2. Osborn 2003, hep-th/0302119 — https://arxiv.org/abs/hep-th/0302119
   (eq 35, 36)

3. Jack-Osborn 1990, NPB 343, 647 — should be accessible through
   InspireHEP or institutional library (section 4)

4. Prochazka-Zwicky 2017, arXiv:1703.01239 — https://arxiv.org/abs/1703.01239
   (eq 38, 60, statement that Δb̄ > 0 by unitarity)

---

## One more framing

The honest way to present this to yourself: you're not being asked to
validate a theory of everything or prove that GRUT is right. You're
being asked three specific technical questions about how different anomaly
structures relate in the consistency-relation framework. The answers
determine which of several published physics mechanisms produces a
specific cosmological prediction.

If the answers land favorably, Ryan has a real result. If they don't,
Ryan has a clean negative finding on a specific mechanism. Either is
useful science.
