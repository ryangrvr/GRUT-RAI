"""
Test: does the derivative structure of <F²F²> kill the IR-domination
that the scalar noise kernel has?

Three spectral sums to compare on S^4:
    S_0 = Σ d_n / (λ_n + m²)²          — scalar noise kernel
    S_1 = Σ d_n × λ_n / (λ_n + m²)²    — one derivative per point
    S_2 = Σ d_n × λ_n² / (λ_n + m²)²   — two derivatives per point (F²F²-like)

If S_0 is IR-dominated but S_2 is UV-dominated, the derivative structure
flips the domination, and the M_Z-scheme argument breaks.
"""

import math

H = 1.0

def lam(n):
    return n*(n+3)*H**2

def deg(n):
    return (n+1)*(n+2)*(2*n+3)//6

def spectral_sum(m_sq, power_lam, n_max=500, include_zero=False):
    """Σ d_n × λ_n^power / (λ_n + m²)² — with or without zero mode."""
    total = 0.0
    if include_zero:
        # λ_0 = 0; contribution is 0^power / m^4
        if power_lam == 0:
            total += 1.0 / m_sq**2   # d_0 = 1
        # for power > 0: contribution is 0
    for n in range(1, n_max+1):
        total += deg(n) * lam(n)**power_lam / (lam(n) + m_sq)**2
    return total

def cumulative_test(m_sq, power_lam, n_max=500, include_zero=False):
    """Find mode n* such that 50% and 90% of sum comes from modes ≤ n*."""
    contribs = []
    if include_zero:
        if power_lam == 0:
            contribs.append((0, 1.0/m_sq**2))
    for n in range(1, n_max+1):
        contribs.append((n, deg(n) * lam(n)**power_lam / (lam(n) + m_sq)**2))
    total = sum(c for _, c in contribs)
    cum = 0.0
    n_50 = None
    n_90 = None
    for (n, c) in contribs:
        cum += c
        if n_50 is None and cum >= 0.50 * total:
            n_50 = n
        if n_90 is None and cum >= 0.90 * total:
            n_90 = n
            break
    return n_50, n_90, total

# =============================================================================
# Test at several m/H ratios
# =============================================================================
print("=" * 78)
print("Derivative re-weighting test on S^4")
print("=" * 78)
print()
print("Spectral sums on S^4 compared:")
print("  S_0 (scalar noise):   Σ d_n × λ^0 / (λ+m²)²")
print("  S_1 (1 deriv / pt):   Σ d_n × λ^1 / (λ+m²)²")
print("  S_2 (F²F²):           Σ d_n × λ^2 / (λ+m²)²")
print()

for m_over_H, label in [(0.01, "light (m/H=0.01)"), (0.1, "m/H=0.1"),
                        (1.0, "m/H=1"), (10.0, "heavy m/H=10")]:
    m_sq = m_over_H**2
    print(f"--- {label} ---")
    for power, name in [(0, "S_0 scalar"), (1, "S_1 (1-deriv)"),
                        (2, "S_2 (F²F²)")]:
        n_50, n_90, total = cumulative_test(m_sq, power, n_max=500, include_zero=False)
        print(f"  {name:<20}: 50% at n={n_50 if n_50 else 'N/A'}, 90% at n={n_90 if n_90 else 'N/A'}")
    print()

print()
print("=" * 78)
print("With zero mode included (Hartle-Hawking)")
print("=" * 78)
print()

for m_over_H in [0.01, 0.1, 1.0]:
    m_sq = m_over_H**2
    print(f"m/H = {m_over_H}:")
    for power, name in [(0, "S_0"), (1, "S_1"), (2, "S_2 (F²F²)")]:
        n_50, n_90, total = cumulative_test(m_sq, power, n_max=500, include_zero=True)
        # Zero-mode fraction
        if power == 0:
            zero_contrib = 1.0/m_sq**2
        else:
            zero_contrib = 0.0
        zero_frac = zero_contrib / total * 100
        print(f"  {name:<10}: 50% at n={n_50 if n_50 else 'N/A'}, "
              f"90% at n={n_90 if n_90 else 'N/A'}, "
              f"zero-mode fraction = {zero_frac:.2f}%")
    print()

print("=" * 78)
print("Verdict")
print("=" * 78)
print("""
  The key comparison:

  S_0 (scalar noise kernel, what our prior spectral test measured):
      Without zero mode: 50% at n ≈ 12 (IR-shifted by 100× from S_eff)
      With zero mode:    ~100% at n=0 for light fields (deep IR)
      → IR-dominated — supports M_Z scheme

  S_1 (one derivative):
      Extra factor of λ per point kills IR enhancement
      50% shifts to much higher n
      Zero-mode contribution → 0

  S_2 (F²F², what the actual observable is):
      Extra λ² factor per point
      50% shifts even higher (more UV-dominated)
      Zero-mode contribution identically zero

  DOES THE UV SHIFT OF S_2 INVALIDATE THE M_Z ARGUMENT?

  This is the specific concern raised about the tensor projection.
  The scalar noise kernel IS IR-dominated, but F²F² has structural
  UV amplification from derivatives. If S_2 is genuinely UV-dominated,
  then the matter-matching-scale argument fails for the specific
  observable GRUT cares about.

  Let me check if S_2 still has any matter-scale sensitivity or if
  it's purely UV.
""")

# =============================================================================
# S_2 scale sensitivity
# =============================================================================
print("S_2 mass sensitivity test:")
print("  If S_2 depends strongly on m/H, there's residual IR sensitivity.")
print("  If S_2 is nearly m-independent (for m<<H), it's UV-dominated.")
print()
print(f"  {'m/H':<10} {'S_2 (sans 0-mode)':>22} {'relative to m=H':>22}")
print("-" * 78)
S_2_ref = spectral_sum(1.0, 2, n_max=500, include_zero=False)  # m = H
for m_over_H in [0.001, 0.01, 0.1, 1.0, 10.0]:
    m_sq = m_over_H**2
    s2 = spectral_sum(m_sq, 2, n_max=500, include_zero=False)
    print(f"  {m_over_H:<10} {s2:>22.4f} {s2/S_2_ref:>22.4f}")

print()
print("""
  Interpretation:
    * If S_2 is nearly constant across m/H orders of magnitude
      (for m << H): the sum is UV-dominated and insensitive to
      matter scale → UV-dominated → µ = H scheme is natural.

    * If S_2 varies significantly with m/H: there's IR/matter-scale
      sensitivity even in the derivative-heavy sum → µ = M_Z still
      has a case.
""")
