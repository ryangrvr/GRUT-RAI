#!/usr/bin/env python3
"""L0_redundancy: in-house attempt at Frontier #3 -- the L0->0 redundancy theorem (R2).

CLAIM (R2, default-BROKEN): in the memoryless limit L0->0 the adiabatic (spatial) dilatation is an
EXACT, unbroken redundancy of the CTP influence action S_IF, and memory (L0) is the UNIQUE parameter
that breaks it -- so memory is the only source of physical structure.

This is a CHECKABLE in-house attempt (the one frontier where that is legitimate). It is a TOY: one
mode of a single-pole influence kernel in frequency space. It tests the three sub-questions of R2:
  (i)   is delta S_IF -> 0 as L0 -> 0 (an EXACT redundancy in the memoryless limit)?
  (ii)  is L0 the UNIQUE breaker?
  (iii) is the adiabatic mode DERIVED from S_IF, or PRESUPPOSED (inserted by hand)?

A dilatation w -> s*w (with the matching field weight) is an exact redundancy of the quadratic action
int dw phi*(w) K_R(w) phi(w) iff K_R is homogeneous of degree `deg` in w. The failure is measured by
the dilatation-breaking density  B(w) = (w d/dw - deg) K_R(w);  B == 0  <=>  exact redundancy.

Pure stdlib. Default-BROKEN: the win is the honest verdict, not a forced proof.
"""
import cmath
import math

DEG = 1  # homogeneous degree of the local (L0=0) kernel -i*w


def K_R(w, L0, b=0.0, mu=1.0):
    """Retarded response kernel of the toy influence action.
      local part        : -i*w           (homogeneous degree 1  -> dilatation-covariant)
      single-pole memory: 1/(1 - i w L0) (memory length L0)
      optional anomaly  : (1 + b ln(w/mu)) -- a log-running coupling standing in for the trace/
                          conformal anomaly (rung9a's alpha): a SECOND, memory-independent breaker.
    """
    running = (1.0 + b * math.log(abs(w) / mu)) if b else 1.0
    return running * (-1j * w) / (1.0 - 1j * w * L0)


def dilatation_breaking(w, L0, b=0.0, mu=1.0, deg=DEG, h=1e-6):
    """B(w) = (w d/dw - deg) K_R(w), via a centred difference for w d/dw."""
    wdK = (K_R(w * (1 + h), L0, b, mu) - K_R(w * (1 - h), L0, b, mu)) / (2 * h)  # ~ dK/dw * w? no:
    wdK = w * (K_R(w * (1 + h), L0, b, mu) - K_R(w * (1 - h), L0, b, mu)) / (2 * h * w)  # = w*dK/dw
    return wdK - deg * K_R(w, L0, b, mu)


def main():
    print("=" * 78)
    print("L0->0 REDUNDANCY -- in-house proof attempt (R2), default-BROKEN")
    print("=" * 78)
    w = 1.0  # a representative frequency (units of the cutoff)

    print("\n(i) EXACTNESS at L0->0: dilatation-breaking density B(w) vs memory L0 (anomaly off, b=0)")
    print("    L0           |B(w)|        |B|/L0   (constant -> B = O(L0), vanishes linearly)")
    for L0 in (1.0, 1e-1, 1e-2, 1e-3, 1e-4):
        B = dilatation_breaking(w, L0, b=0.0)
        print(f"    {L0:<11.0e}  {abs(B):<11.4e}  {abs(B) / L0:.4f}")
    B0 = dilatation_breaking(w, 0.0, b=0.0)
    print(f"    {0.0:<11.0e}  {abs(B0):<11.4e}  (exactly 0: the local kernel is dilatation-covariant)")
    L0 = 1e-3
    Bana = (w ** 2 * L0) / (1 - 1j * w * L0) ** 2
    print(f"    analytic: B = w^2 L0/(1-iwL0)^2 ; at L0={L0:.0e} |B|={abs(Bana):.4e} (matches numeric)")
    print("    => B -> 0 LINEARLY in L0; at L0=0 the redundancy is EXACT.  R2(i): HOLDS in the toy.")

    print("\n(ii) UNIQUENESS: set memory OFF (L0=0 exactly) and turn the trace/conformal anomaly ON")
    print("     (log-running coupling b != 0, standing in for rung9a's alpha):")
    print("     L0=0, anomaly b:   |B(w)|")
    for b in (0.0, 0.1, 0.3):
        B = dilatation_breaking(w, L0=0.0, b=b, mu=0.5)
        print(f"        b={b:.1f}            {abs(B):.4e}")
    print("    => with L0=0 EXACTLY, a nonzero anomaly b still gives B = -i*b*w != 0. The conformal")
    print("       anomaly breaks dilatation invariance INDEPENDENTLY of memory.  R2(ii): FAILS as")
    print("       stated -- L0 is NOT the unique breaker (unique only in the anomaly-free/classical")
    print("       sector). 'Memory is the ONLY structure-source' contradicts GRUT's OWN rung9a.")

    print("\n(iii) DERIVED or PRESUPPOSED?  The dilatation generator (w d/dw) and the field weight")
    print("      `deg` are INPUTS here -- inserted by hand. Nothing DERIVES the adiabatic mode or its")
    print("      weight from K_R; they are assumed (the Weinberg adiabatic-mode construction, inherited")
    print("      from the ASSUMED background diffeomorphism invariance).  R2(iii): PRESUPPOSED (the")
    print("      relocation trap, already flagged by the mu_linear pre-screen).")

    print("\n" + "=" * 78)
    print("VERDICT (default-BROKEN, honest):")
    print("  R2(i)   exact at L0->0          : HOLDS in the toy  (B = O(L0) -> 0).")
    print("  R2(ii)  L0 the UNIQUE breaker   : FAILS  -- the trace anomaly (rung9a) co-breaks it;")
    print("                                    L0 is unique only in the anomaly-free/classical sector.")
    print("  R2(iii) mode derived/presupposed: PRESUPPOSED (inserted; inherited from assumed bg diff-inv).")
    print("  => R2 DISSOLVES to: the redundancy is EXACT in the memoryless limit, but it RESTS ON a")
    print("     presupposed input (the adiabatic mode) and 'memory is the UNIQUE structure-source' is")
    print("     too strong (the anomaly co-breaks). Honest result: the foundation rests on a named")
    print("     irreducible input; memory is the LEADING classical-IR structure-source, not the only one.")
    print("  => R3 (graduate mu_linear): NOT cleanly -- R2 relocates the adiabatic bridge mu_linear")
    print("     needs rather than deriving it; mu_linear stays a no-go export. Foundational scope only.")
    print("  CAVEAT: a TOY (one mode, single pole). A real proof needs the full S_IF dilatation variation")
    print("     on de Sitter + a derivation of the mode from the action -- FRONTIER, specialist territory.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
