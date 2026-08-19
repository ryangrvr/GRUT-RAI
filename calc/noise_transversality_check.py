#!/usr/bin/env python3
"""NOISE-KERNEL TRANSVERSALITY: a theorem on the booked family, conditional on ONE priced input.

THE QUESTION (ruled 2026-08-16). The Ward-scope correction (2026-08-14, accepted) withdrew the
both-branches license for noise-kernel transversality: the diagonal diffeomorphism Ward identity
constrains only the slot contracted with a_r (the retarded slot) and says NOTHING about the
a_a-quadratic noise term. The assumption survived the withdrawal of its license. The ruling:
either BOOK the input (+1) or DERIVE it from what is already booked -- "exhibited, not asserted."

THE ANSWER, as it stands after the 2026-08-16/17 adversarial screen (three refuter lenses plus
adjudicator; the screen's findings are incorporated below and marked where they cut): BOTH horns,
composed. The chain is a genuine derivation, but it consumes ONE premise the register had not
priced -- so that premise is booked (+1 at rung1; renamed at owner verification: the
4d-covariant availability of the Ward-sourced gauge-orbit zero, KC5-reserved), and
transversality is then a THEOREM conditional on that priced input. The chain:

  P1  WARD SOURCES A ZERO (the accepted 2026-08-14 mark): K_R annihilates the gauge orbit
      G = {k (x) xi + xi (x) k} on its retarded slot: K_R g = 0 for all g in G.
      ==> the gauge diagonal of the spectral form vanishes IDENTICALLY:
          g' rho g = (g' K_R g - (K_R g)' g) / 2i = 0,   rho := (K_R - K_R^dag)/2i.
      (D_A = K_R^dag is forced by real fields + stationarity -- D_A(omega) = K_R(-omega)^T =
      K_R(omega)^dag -- not an extra assumption; screen-verified.) Bilinear algebra, no
      positivity, no KMS. PART 1.

  P2  POSITIVITY PROPAGATES THE ZERO -- and the carrier is N ITSELF, not rho. N is a noise
      COVARIANCE: for X = x^munu O_munu (O Hermitian on a positive state space),
      x' N x = <{X^dag, X}>/2 >= 0 in the PLAIN pairing (no metric insertion; Wightman/Bochner,
      per-(omega,k) matrix PSD-ness; state-agnostic among stationary states) -- on the FULL
      index space, no conformal-mode carve-out: this is bath-side unitarity; the system-side
      wrong-sign sector lives in Re K_R and is untouched. THE SCREEN'S PRICING FINDING: this
      premise -- bath genuineness -- is NOT inside rung1's banked form-only statement, and the
      spatial-frame S4 (operator_basis.py, KC5 fence) is frontier-reserved at exactly the
      needed 4d strength, so it CANNOT substitute (it corroborates in the spatial frame only).
      The premise is therefore BOOKED: rung1's fourth declared input (+1, 2026-08-17;
      renamed at owner verification -- the priced half is the 4D-COVARIANT AVAILABILITY
      of the Ward-sourced gauge-orbit zero, the KC5-reserved covariantization;
      N-as-PSD-covariance was ruled CONSTITUTIVE of the banked Gaussian bath).
      [A c-number-commutator route to rho-positivity claimed in this file's first draft was
      WRONG -- T_munu is quadratic in bath fields, its commutator is operator-valued and
      state-dependent; rho-positivity per sign of omega is passive-STATE content. Struck by
      the screen; the N-route below replaces it.]
      For a PSD form, a zero diagonal entry kills its row (Cauchy-Schwarz; M = B'B ==>
      x'Mx = |Bx|^2 = 0 ==> Bx = 0 ==> Mx = 0). This is the propagation mechanism
      passivity_channel_diagonal's own guard licenses ("a zero diagonal kills its
      cross-couplings") -- the zero is WARD-sourced, never positivity-sourced (kill-condition 4
      respected), and no PHYSICAL channel is annihilated, only gauge directions. PART 2.

  P3  THE LOCK CLOSES IT (rung2 + rung7_wz's booked family): equilibrium
      N = coth(beta*omega/2) * rho; the booked non-equilibrium departures multiply rho by a
      SCALAR occupation n(omega) > 0 (the (eps,tau_2) dials -- already paid at rung7_wz; a
      channel-dependent occupation is a NEW dial, priced at entry by rung2's standing fence).
      Then, applying Cauchy-Schwarz DIRECTLY to N:  g'Ng = n(omega) * g'rho g = 0 (P1) and
      N PSD (P2)  ==>  N g = 0: N IS TRANSVERSE. And rho g = N g / n(omega) = 0 wherever
      n != 0 (coth never vanishes at real omega != 0). PART 3.
      omega < 0: coth < 0 and rho is NSD there (apply the lemma to -rho); N stays PSD and the
      transversality conclusion is sign-independent. omega -> 0: coth diverges, N finite
      requires rho -> 0 linearly (standard Im chi ~ omega); transversality at the edge follows
      by continuity.

  COROLLARY (the advanced slot, conditional on the same priced input): K_R^dag g =
      K_R g - 2i rho g = 0 -- K_R transverse on BOTH slots on the booked family. And the
      admissible (K_R, N) pair then CLOSES on {P^(2), P^(0s)} (Schur: sym^2_0 of the
      transverse space is absolutely irreducible under both little groups) -- a
      FAMILY-CONDITIONAL CLOSURE THEOREM. The unconditional both-branch classification stays
      RETIRED; outside the family (independent non-FDT noise, channel-structured occupations
      -- SCDP's Eq. 1.11 class) SCDP's strictly larger space stands, priced at entry by
      rung2's fence.

  THE SIGNATURE FACT (screen finding, verified here, both figures reported): in the plain
      pairing P^(0s) is PSD at every k (rank-1 form), but P^(2) is PSD only at TIMELIKE k^2 --
      at SPACELIKE k^2 the transverse space contains a timelike direction and P^(2) is
      indefinite (this file's first draft ran its spacelike family instance at s2 > 0, which
      the theorem's own premises bar; the screen caught it -- the missing check was this
      file's own composition assert, now PART 3's psd_exact). So ON the covariant eta,k-only
      family, positivity forces s2 = 0 at spacelike k^2: tensor-channel dissipation/noise has
      no spacelike support (Landau-damping-style spacelike support needs a medium frame u^mu,
      which is outside this family). Transversality at spacelike k^2 holds via P^(0s) alone --
      the theorem is not vacuous there, but the tensor channel is closed by positivity itself.

  WHY THE KMS FORM ALONE WAS NEVER ENOUGH (PART 4): K_cx = i (k(x)k) (x) Pi passes the
      diagonal-Ward retarded-slot check and satisfies the MATRIX-ADJOINT lock form
      N = coth*(K - K^dag)/2i -- the form the booked family itself uses (the banked
      per-scalar-channel gate, gate/kms.py, is SILENT on non-normal kernels like K_cx, which
      admit no orthogonal channel decomposition) -- yet its noise is non-transverse. It dies
      at positivity: its spectral form is INDEFINITE (exact witness printed). The bar is
      N-covariance positivity (ruled constitutive of the banked Gaussian bath at owner
      verification; the 2026-08-17 +1 prices the 4d gauge-orbit zero the chain also
      consumes).

  NON-VACUOUS COMPOSITION (PART 3b, the screen's owed instance): for K = K_fam + d*K_cx with
      ANY d != 0 -- retarded-slot Ward intact, general within the post-correction books -- the
      2x2 principal minor on (gauge, probe) directions has determinant -|rho[g,x]|^2 < 0,
      exactly: positivity kills every right-slot-only admixture, which is the closure theorem
      doing real work, not a by-construction pass.

  DEMARCATION AGAINST THE LITERATURE (screen-mandated; verified by the screen's physics lens
  against the fetched texts, NOT first-party-read by this file's author):
    * SCDP App. B.2 and Salcedo-Colas-Pajer arXiv:2412.12299 derive noise constraints in open
      gravity by a Bianchi/conservation route whose no-dissipation corner reproduces this
      conclusion and which DEFORMS under dissipation; the theorem here covers the
      with-dissipation FDT-locked case by a different mechanism.
    * Abe-Nishii arXiv:2605.22822 Sec. 4.3 uses the identical (Ward, FDT, positivity) triad
      with the transverse projection IMPOSED as an input -- the projection this chain derives.
    * The PSD/FDT matrix engine itself is Landau-Lifshitz-standard (matrix FDT + passivity);
      what is new here is only the WARD-SOURCED zero on the gravitational gauge orbit and the
      assembly into the family-conditional closure.
    * Hu-Verdaguer (stochastic gravity, Living Reviews): transversality derived from bath
      stress-tensor CONSERVATION -- a different route in the conserved-current-bath subclass;
      corroboration, not the license (and their PSD-from-self-adjointness independently
      corroborates the carrier in Lorentzian gravity).

Pure sympy, exact rational arithmetic; two momentum instantiations (spacelike and timelike
k^2), with the family instance chosen ON-family per signature as the theorem itself requires.
Conventions: fields upper indices, kernels all-lower, plain-coordinate-sum pairing (this IS
the pairing in which Wightman positivity is a matrix statement); eta = diag(-1,+1,+1,+1).

MUTATION BATTERY (calc-layer floor): six in-process mutants, each must flip a named verdict.
  M1 drop positivity      -> transversality fails (K_cx exhibits it): the premise bites.
  M2 drop Ward            -> the gauge diagonal is nonzero; nothing propagates: flip.
  M3 corrupt the engine   -> the Cauchy-Schwarz bound check must catch a broken bound.
  M4 unlock the noise     -> an INDEPENDENT PSD noise piece (non-FDT) re-opens
                             non-transversality with all Ward content intact: the conclusion's
                             edge is rung2's fence, exhibited.
  M5 shrink the orbit     -> a kernel transverse to k(x)k alone passes the shrunk check and
                             fails the full orbit: the orbit size is load-bearing.
  M6 off-family instance  -> s2 > 0 at spacelike k^2 must FAIL the composition assert (the
                             check whose absence the screen caught).
"""
import random
import sys

import sympy as sp
from sympy import I, Rational, simplify

random.seed(20260816)

ETA = sp.diag(-1, 1, 1, 1)


def idx(m, n):
    return 4 * m + n


def build(w, q):
    """Momentum environment: k^mu = (w,0,0,q), exact rationals."""
    kup = [Rational(w), 0, 0, Rational(q)]
    klow = [ETA[m, m] * kup[m] for m in range(4)]          # diagonal metric
    k2 = sum(kup[m] * klow[m] for m in range(4))           # -w^2 + q^2
    assert k2 != 0, "instantiate off-shell"
    Pi = sp.zeros(4, 4)                                    # transverse projector, all-lower
    for r in range(4):
        for s in range(4):
            Pi[r, s] = ETA[r, s] - klow[r] * klow[s] / k2
    for s in range(4):                                     # k^rho Pi_{rho sigma} = 0
        assert simplify(sum(kup[r] * Pi[r, s] for r in range(4))) == 0
    # gauge orbit, upper indices: g^{rho sigma} = k^rho xi^sigma + xi^rho k^sigma, xi = e_a
    orbit = []
    for a in range(4):
        g = sp.zeros(16, 1)
        for r in range(4):
            for s in range(4):
                g[idx(r, s)] = kup[r] * (1 if s == a else 0) + (1 if r == a else 0) * kup[s]
        orbit.append(g)
    # transverse-family forms, all-lower (internal contractions carry eta explicitly)
    P0 = sp.zeros(16, 16)
    P2 = sp.zeros(16, 16)
    for m in range(4):
        for n in range(4):
            for r in range(4):
                for s in range(4):
                    P0[idx(m, n), idx(r, s)] = Pi[m, n] * Pi[r, s] / 3
                    P2[idx(m, n), idx(r, s)] = (Pi[m, r] * Pi[n, s] + Pi[m, s] * Pi[n, r]) / 2 \
                        - Pi[m, n] * Pi[r, s] / 3
    u = sp.zeros(16, 1)                                    # (k (x) k), lower
    v = sp.zeros(16, 1)                                    # Pi, lower
    e = sp.zeros(16, 1)                                    # eta, lower
    for m in range(4):
        for n in range(4):
            u[idx(m, n)] = klow[m] * klow[n]
            v[idx(m, n)] = Pi[m, n]
            e[idx(m, n)] = ETA[m, n]
    return dict(kup=kup, klow=klow, k2=k2, Pi=Pi, orbit=orbit, P0=P0, P2=P2, u=u, v=v, e=e)


def is_zero_vec(x):
    return all(sp.expand(x[i, 0]) == 0 for i in range(x.rows))


def quad(K, x, y):
    return (x.H * K * y)[0, 0]


def rho_of(K):
    return (K - K.H) / (2 * I)


def psd_exact(M):
    """Exact PSD test for a Hermitian rational(-complex) matrix: symmetric-pivot elimination.
    PSD iff every pivot is > 0 and any zero-diagonal step has an entirely zero row. Exact
    rational arithmetic -- no floats, no eigensolvers."""
    A = M.copy().applyfunc(sp.expand)
    n = A.rows
    live = list(range(n))
    while live:
        pivot_i = None
        for i in live:
            d = sp.re(sp.expand(A[i, i]))
            if d < 0:
                return False
            if d > 0:
                pivot_i = i
                break
        if pivot_i is None:                                # all remaining diagonals are zero
            return all(sp.expand(A[i, j]) == 0 for i in live for j in live)
        p = A[pivot_i, pivot_i]
        rest = [i for i in live if i != pivot_i]
        for i in rest:
            f = sp.expand(A[i, pivot_i] / p)
            for j in rest:
                # Schur complement: A[i,j] - A[i,p]*A[p,j]/p. (The first draft wrote
                # conj(A[p,j]) here -- equal to A[j,p] for Hermitian input, so correct only
                # in the real-symmetric case; the 2026-08-17 re-screen caught it with a
                # complex-Hermitian counterexample. All shipped call sites were real
                # symmetric, so no verdict moved -- fixed and selftested below regardless.)
                A[i, j] = sp.expand(A[i, j] - f * A[pivot_i, j])
        live = rest
    return True


def psd_selftest():
    """Known-verdict cases for psd_exact, run before anything relies on it. Includes the
    complex-Hermitian class where the first draft's elimination was wrong: [[1,2i],[-2i,2]]
    (det -2, indefinite) came back POSITIVE under the conj-slip formula."""
    cases = [
        (sp.Matrix([[1, 2 * I], [-2 * I, 2]]), False),     # the re-screen's counterexample class
        (sp.Matrix([[1, I], [-I, 2]]), True),              # complex Hermitian PD (det 1)
        (sp.Matrix([[0, 1], [1, 0]]), False),              # zero diagonal, nonzero row
        (sp.Matrix([[1, 1], [1, 1]]), True),               # PSD with nontrivial kernel
        (sp.Matrix([[2, 1 + I], [1 - I, 3]]), True),       # complex Hermitian PD (det 4)
        (sp.diag(0, 0, 0), True),                          # the zero form
        (sp.Matrix([[1, 2], [2, 1]]), False),              # real symmetric indefinite
    ]
    B = sp.Matrix([[1, I, 0], [0, 1, 1], [1, 0, -I]])
    cases.append((B.H * B, True))                          # Gram matrix, PSD by construction
    return all(psd_exact(M) is want for M, want in cases)


def rand_rational():
    return Rational(random.randint(-5, 5), random.randint(1, 4))


def rand_matrix(rows, cols, cplx=False):
    M = sp.zeros(rows, cols)
    for i in range(rows):
        for j in range(cols):
            M[i, j] = rand_rational() + (I * rand_rational() if cplx else 0)
    return M


def perp_projector(vectors):
    """I - G (G^H G)^-1 G^H  onto the orthogonal complement of span(vectors). Exact."""
    G = vectors[0]
    for g in vectors[1:]:
        G = G.row_join(g)
    return sp.eye(G.rows) - G * (G.H * G).inv() * G.H


def family_kernel(env, s2_override=None):
    """The booked-family instance, chosen ON-family per signature: at spacelike k^2 the
    theorem's own positivity premise forces s2 = 0 (P^(2) indefinite in the plain pairing
    there); at timelike k^2 both channels are open. s2_override exists for the battery."""
    spacelike = env["k2"] > 0
    s2 = s2_override if s2_override is not None else (Rational(0) if spacelike else Rational(2))
    h2, h0, s0 = Rational(3), Rational(-1), Rational(1, 2)
    K = (h2 + I * s2) * env["P2"] + (h0 + I * s0) * env["P0"]
    return K, s2, s0


# ----------------------------------------------------------------------------------------------
# PART 1 -- Ward sources the zero: K g = 0  ==>  g' rho g = 0, identically. No positivity used.
def part1_identity(env, draws=3):
    Pp = perp_projector(env["orbit"])
    for _ in range(draws):
        K = rand_matrix(16, 16, cplx=True) * Pp            # generic kernel annihilating the orbit
        for g in env["orbit"]:
            assert is_zero_vec(K * g)
            if simplify(quad(rho_of(K), g, g)) != 0:
                return False
    return True


# ----------------------------------------------------------------------------------------------
# PART 2 -- the PSD engine: zero diagonal kills the row (M = B'B), plus the quantitative bound
# x' M^2 x <= tr(M) * x' M x  that forces Mx = 0 whenever x'Mx = 0.
def part2_engine(draws=3, bound_stat=None):
    for _ in range(draws):
        x0 = rand_matrix(4, 1, cplx=True)
        if is_zero_vec(x0):
            continue
        B = (rand_matrix(4, 4, cplx=True) * perp_projector([x0])).applyfunc(sp.expand)
        M = (B.H * B).applyfunc(sp.expand)                 # PSD with engineered null direction
        if not is_zero_vec(M * x0):                        # zero diagonal -> zero row: exact
            return False
        x = rand_matrix(4, 1, cplx=True)
        Mx = (M * x).applyfunc(sp.expand)
        lhs = sp.re(sp.expand((Mx.H * Mx)[0, 0]))          # x'M^2x = |Mx|^2 (M Hermitian)
        rhs = sp.re(sp.expand(sp.trace(M) * (x.H * Mx)[0, 0]))
        stat = bound_stat if bound_stat is not None else rhs
        if not (lhs <= stat):                              # the engine's bound, exact rationals
            return False
    return True


# ----------------------------------------------------------------------------------------------
# PART 3 -- the theorem end-to-end on the booked family (equilibrium lock + scalar dials),
# WITH the composition assert the screen found missing, plus the advanced-slot corollary.
def part3_theorem(env, orbit=None, extra_noise=None, s2_override=None):
    orbit = orbit if orbit is not None else env["orbit"]
    K, s2, s0 = family_kernel(env, s2_override=s2_override)
    for g in orbit:                                        # Ward on the retarded slot
        if not is_zero_vec(K * g):
            return False
    rho = rho_of(K)                                        # = s2 P2 + s0 P0, exactly
    assert is_zero_vec((rho - (s2 * env["P2"] + s0 * env["P0"])).reshape(256, 1))
    # THE COMPOSITION CHECK (the screen's finding -- the check whose absence let the first
    # draft pass an off-family instance): the family spectral form must itself satisfy the
    # positivity the theorem consumes. Exact, full 16-dim, plain pairing.
    assert psd_exact(rho), "family rho must be PSD -- off-family instance"
    c, n = sp.symbols("c n", positive=True)                # coth factor / scalar occupation dial
    for N in (c * rho, n * rho):
        if extra_noise is not None:
            N = N + extra_noise
        for g in env["orbit"]:                             # the CONCLUSION checks the FULL orbit
            if not is_zero_vec(N * g):
                return False
    for g in env["orbit"]:                                 # corollary: advanced slot returns
        if not is_zero_vec(K.H * g):
            return False
    return True


# ----------------------------------------------------------------------------------------------
# PART 3b -- the NON-VACUOUS composition (screen-owed): a general kernel with ONLY
# retarded-slot Ward -- K_fam + d*K_cx -- has, for EVERY d != 0, a negative 2x2 principal
# minor pairing a gauge direction with a probe: positivity kills every right-slot-only
# admixture. Exhibited exactly, three values of d.
def part3b_composition(env):
    K_fam, _, _ = family_kernel(env)
    K_cx = I * env["u"] * env["v"].T
    g = env["orbit"][0]                                    # xi = e_0: klow.xi != 0
    for d in (Rational(1), Rational(1, 7), Rational(-3)):
        rho = rho_of(K_fam + d * K_cx)
        if simplify(quad(rho, g, g)) != 0:                 # gauge diagonal still zero (P1)
            return False
        x = env["v"]                                       # probe hit by the gauge row
        a = sp.expand(quad(rho, g, x))
        if a == 0:                                         # the admixture must move the row
            return False
        b = sp.re(sp.expand(quad(rho, x, x)))
        det = sp.re(sp.expand(-a * sp.conjugate(a)))       # det [[0, a],[a*, b]] = -|a|^2
        if not (det < 0):
            return False
    return True


# ----------------------------------------------------------------------------------------------
# PART 4 -- the counterexample: retarded-slot Ward-legal, satisfies the matrix-adjoint lock
# form, noise non-transverse -- and provably indefinite (positivity bars it). Report both
# slots (report-both-figures).
def part4_counterexample(env, verbose=False):
    u, v = env["u"], env["v"]
    K = I * u * v.T                                        # K_{mn,rs} = i (k k)_{mn} Pi_{rs}
    ward_ret = all(is_zero_vec(K * g) for g in env["orbit"])           # retarded slot: PASSES
    ward_adv = all(is_zero_vec(K.H * g) for g in env["orbit"])         # advanced slot: FAILS
    rho = rho_of(K)                                        # = (u v' + v u')/2, real symmetric
    c = sp.symbols("c", positive=True)
    N = c * rho                                            # the matrix-adjoint lock, saturated
    nonT = [sp.expand((rho * g).T * (rho * g))[0, 0] for g in env["orbit"]]  # |rho g|^2, exact
    noise_nontransverse = any(x != 0 for x in nonT)
    # indefiniteness witness: x = u + t v gives Q(t) = (u.(u+tv))(v.(u+tv)), a real quadratic
    # with roots t = -uu/uv and t = -uv/vv; Q is negative between them if it opens upward,
    # outside them if it opens downward -- try both and keep whichever witness is negative.
    uu, uv, vv = (u.T * u)[0], (u.T * v)[0], (v.T * v)[0]
    assert uv != 0
    roots = sorted([sp.Rational(-uu, uv), sp.Rational(-uv, vv)])
    t = None
    Qx = None
    for cand in ((roots[0] + roots[1]) / 2, roots[1] + 1, roots[0] - 1):
        val = sp.expand(quad(rho, u + cand * v, u + cand * v))
        if val < 0:
            t, Qx = cand, val
            break
    indefinite = Qx is not None and Qx < 0
    if verbose:
        print(f"    K_cx Ward: retarded slot {'PASS' if ward_ret else 'FAIL'}, "
              f"advanced slot {'PASS' if ward_adv else 'FAIL'}  (both figures reported)")
        print(f"    N_cx non-transverse: |rho g|^2 over orbit = {nonT}")
        print(f"    positivity witness: x = u + ({t}) v  gives  x' rho x = {Qx} < 0 -- "
              f"indefinite; barred by N-covariance positivity (ruled constitutive of the "
              f"banked Gaussian bath, owner verification 2026-08-17)")
    return ward_ret and (not ward_adv) and noise_nontransverse and indefinite


# ----------------------------------------------------------------------------------------------
# PART 5 -- the battery.
def part5_battery(env):
    results = {}
    # M1 drop positivity: the counterexample's noise is non-transverse -- part3's conclusion
    # fails on a kernel differing ONLY in violating positivity.
    K = I * env["u"] * env["v"].T
    m1_flip = any(not is_zero_vec(rho_of(K) * g) for g in env["orbit"])
    results["M1 drop-positivity flips transversality"] = m1_flip
    # M2 drop Ward: an anti-Hermitian eta(x)eta piece leaves a nonzero gauge diagonal.
    e = env["e"]
    K2 = (Rational(3) + I * Rational(2)) * env["P2"] + I * e * e.T
    m2_diag = [simplify(quad(rho_of(K2), g, g)) for g in env["orbit"]]
    results["M2 drop-Ward flips the sourced zero"] = any(x != 0 for x in m2_diag)
    # M3 corrupt the engine: replace tr(M) by 0 in the bound -- the check must FAIL.
    results["M3 corrupt-engine is caught"] = (part2_engine(draws=3, bound_stat=0) is False)
    # M4 unlock the noise: an independent PSD non-FDT piece W = u u' re-opens non-transversality
    # with the SAME Ward-clean family kernel. The edge is rung2's fence, exhibited.
    W = env["u"] * env["u"].T
    results["M4 independent noise flips the conclusion"] = \
        (part3_theorem(env, extra_noise=W) is False)
    # M5 shrink the orbit: K = i (k k) (x) sym(k m), m.k = 0 -- transverse to g = k(x)k alone.
    klow, kup = env["klow"], env["kup"]
    m = [klow[3], 0, 0, klow[0]]                           # plain-orthogonal to k^mu: m.k = 0
    assert sum(m[r] * kup[r] for r in range(4)) == 0
    vp = sp.zeros(16, 1)
    for r in range(4):
        for s in range(4):
            vp[idx(r, s)] = (klow[r] * m[s] + m[r] * klow[s]) / 2
    K5 = I * env["u"] * vp.T
    g0 = env["orbit"][0] * 0
    for r in range(4):
        for s in range(4):
            g0[idx(r, s)] = 2 * kup[r] * kup[s]            # the 1-parameter slice xi ~ k
    shrunk_pass = is_zero_vec(K5 * g0)
    full_fail = any(not is_zero_vec(K5 * g) for g in env["orbit"])
    results["M5 shrunk orbit passes what the full orbit fails"] = shrunk_pass and full_fail
    # M6 off-family instance: s2 > 0 at spacelike k^2 must FAIL the composition assert.
    if env["k2"] > 0:
        try:
            part3_theorem(env, s2_override=Rational(2))
            m6 = False                                     # assert did not fire: check is dead
        except AssertionError:
            m6 = True
        results["M6 off-family spacelike instance is refused"] = m6
    else:
        # at timelike k^2 the on-family instance already runs s2 > 0; the composition assert's
        # bite is exhibited by the spacelike branch. Report the timelike PSD fact instead.
        K_t, s2_t, s0_t = family_kernel(env)
        results["M6 (timelike) family rho with s2>0 is PSD as claimed"] = \
            psd_exact(rho_of(K_t))
    return results


def main():
    ok = psd_selftest()
    print(f"  {'PASS' if ok else 'FAIL'}  PART 0  psd_exact selftest (known verdicts, incl. "
          "the complex-Hermitian class the re-screen caught)")
    for w, q, label in ((2, 3, "spacelike k^2"), (3, 1, "timelike k^2")):
        env = build(w, q)
        _, s2, s0 = family_kernel(env)
        print("=" * 94)
        print(f"instantiation k = ({w},0,0,{q}), k^2 = {env['k2']}  [{label}] -- exact "
              f"rationals; ON-family instance (s2, s0) = ({s2}, {s0})")
        checks = [
            ("PART 1  Ward sources the zero (g'rho g = 0, no positivity used)",
             part1_identity(env)),
            ("PART 2  PSD engine (zero diagonal kills the row; bound holds exactly)",
             part2_engine()),
            ("PART 3  theorem on the booked family (family-rho-PSD asserted) + corollary",
             part3_theorem(env)),
            ("PART 3b non-vacuous composition: every d*K_cx admixture breaks positivity",
             part3b_composition(env)),
            ("PART 4  counterexample: adjoint-locked, Ward-legal, non-transverse, INDEFINITE",
             part4_counterexample(env, verbose=True)),
        ]
        for name, res in checks:
            print(f"  {'PASS' if res else 'FAIL'}  {name}")
            ok = ok and res
        print("  battery:")
        for name, res in part5_battery(env).items():
            print(f"  {'PASS' if res else 'FAIL'}  {name}")
            ok = ok and res
    print("=" * 94)
    print("VERDICT: noise-kernel transversality is a THEOREM on the booked family, CONDITIONAL "
          "on the 2026-08-17 priced input (renamed at owner verification: the 4d-covariant "
          "availability of the Ward-sourced gauge-orbit zero, KC5-reserved; rung1 +1; "
          "N-as-PSD-covariance ruled constitutive of the banked Gaussian bath); the family "
          "closes on the transverse pair; outside the family SCDP's larger space stands." if ok else "SOME CHECK FAILED -- verdict not established.")
    # The verdict line above is prose. provenance/test_mutation_battery._run() classifies a mutant
    # as caught BY A CHECK only on the exact string "SELFTEST: FAIL"; this file emitted neither
    # that nor an AssertionError, so its OWN battery's gauge_orbit_lowered mutant -- which IS
    # caught, by three separate PART failures -- was recorded as an incidental CRASH from the day
    # it was written. The battery is slow-flagged, so it never ran in the default suite and the
    # defect sat undetected. Third instance of this marker slip; the guard in
    # test_mutation_battery.TestSelftestMarker now requires every batteried calc to emit it.
    print(f"  SELFTEST: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
