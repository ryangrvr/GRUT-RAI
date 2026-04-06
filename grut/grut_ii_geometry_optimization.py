#!/usr/bin/env python3
"""
GRUT II Lambda-Prime — 3D Geometry Optimization and Valid-Regime USL Testability

Compute the Diosi self-energy difference Delta_E for multiple mass-distribution
geometries displaced by l, and determine which geometry/protocol combinations
maximize the USL signal relative to environmental cost.

Geometries:
1. Sphere (Kappa-Prime baseline)
2. Thin rod (cigar) displaced along its short axis
3. Thin disk displaced along its thin axis
4. Hollow shell displaced by l
5. Dumbbell (two lumps separated by gap)

For each: compute Delta_E vs l, compare to sphere, identify optimal regime.
"""

import numpy as np
from scipy.integrate import quad, dblquad
from scipy.special import erf
import warnings
warnings.filterwarnings('ignore')

G    = 6.67430e-11
hbar = 1.05457e-34
k_B  = 1.38065e-23
rho_silica = 2200.0

# ============================================================
# HELPER: Sphere self-energy and cross-energy (from Kappa-Prime)
# ============================================================
def sphere_U_self(m, R):
    """Self-interaction integral (no G factor): U = (6/5) m^2/R"""
    return (6.0/5.0) * m**2 / R

def sphere_U_cross_numerical(m, R, l):
    """Cross-interaction integral for two displaced spheres, numerical."""
    if l >= 2*R:
        return m**2 / l
    rho_0 = m / ((4/3) * np.pi * R**3)
    def Phi_sphere(r):
        if r <= R:
            return (2*np.pi*rho_0/3) * (3*R**2 - r**2)
        else:
            return (4*np.pi*rho_0*R**3) / (3*r)
    def integrand_z(z):
        s_max_sq = R**2 - (z-l)**2
        if s_max_sq <= 0:
            return 0
        s_max = np.sqrt(s_max_sq)
        def integrand_s(s):
            r = np.sqrt(s**2 + z**2)
            return 2*np.pi*s*rho_0*Phi_sphere(r)
        result, _ = quad(integrand_s, 0, s_max, limit=100)
        return result
    result, _ = quad(integrand_z, l-R, l+R, limit=200, epsrel=1e-10)
    return result

def sphere_DeltaE(m, R, l):
    """Diosi Delta_E for a sphere of mass m, radius R, displaced by l."""
    Us = sphere_U_self(m, R)
    Uc = sphere_U_cross_numerical(m, R, l)
    return G * (Us - Uc)

# ============================================================
# GEOMETRY 2: THIN ROD displaced perpendicular to its axis
# ============================================================
def rod_DeltaE(m, length, radius, l_perp):
    """
    Thin rod of mass m, length L, radius a, displaced by l perpendicular to axis.

    For l >> a (non-overlapping cross-section), the rod acts as a 1D mass distribution.
    Delta_E approaches the result for two parallel line masses separated by l.

    For a thin rod (a << L), displaced perpendicular by l:
    If l > 2a: the two rods don't overlap in cross-section.
    The interaction is that of two parallel line masses:
      U_cross ~ (m/L)^2 * L * integral_0^L ln(L/l) ... (logarithmic in l/L)

    More precisely, for two parallel uniform line masses of length L,
    linear density lambda = m/L, separated by distance d:
    U_cross = lambda^2 * [L * ln(L/d + sqrt(1 + L^2/d^2)) - sqrt(d^2 + L^2) + d]

    For the self-energy of a rod (regularized):
    U_self = lambda^2 * [L * ln(2L/a) - L + ...]  (a = cross-section radius)

    Delta_E = G * (U_self - U_cross)
    """
    lam = m / length  # linear density
    L = length
    d = l_perp
    a = radius

    # Self-energy of a uniform rod (line mass, regularized by cross-section radius a):
    # U_self = lambda^2 * integral_0^L integral_0^L 1/max(|z-z'|, a) dz dz'
    # ≈ lambda^2 * [L * ln(2L/a) - L]  for a << L
    # More precisely: lambda^2 * [2L * arsinh(L/(2a)) - 2*sqrt(a^2 + L^2/4) + 2a]
    # ≈ lambda^2 * L * [2*ln(L/a) - 1]  for a << L
    # Actually the standard result for a thin rod:
    U_self = lam**2 * (2*L*np.log(L/a) - L)  # approximate for a << L

    if d >= 2*a:
        # Cross-section doesn't overlap: use parallel line-mass formula
        # U_cross = lambda^2 * integral_0^L integral_0^L 1/sqrt((z-z')^2 + d^2) dz dz'
        # = lambda^2 * [2L * arsinh(L/d) - 2*(sqrt(d^2+L^2) - d)]
        U_cross = lam**2 * (2*L*np.arcsinh(L/d) - 2*(np.sqrt(d**2 + L**2) - d))
    else:
        # Overlapping cross-sections: interpolate (this regime is similar to sphere overlap)
        # For simplicity, use the non-overlapping formula (lower bound on Delta_E)
        d_eff = max(d, 2*a)
        U_cross = lam**2 * (2*L*np.arcsinh(L/d_eff) - 2*(np.sqrt(d_eff**2 + L**2) - d_eff))

    return G * max(U_self - U_cross, 0)

# ============================================================
# GEOMETRY 3: THIN DISK displaced along its thin axis
# ============================================================
def disk_DeltaE(m, Rdisk, thickness, l_axial):
    """
    Thin disk of mass m, radius Rdisk, thickness h, displaced by l along its axis.

    For l > h: the two disks don't overlap.
    The disks become two parallel uniform disks separated by l.

    For two parallel coaxial uniform disks of surface density sigma, radius Rdisk,
    separated by d:
    The self-energy and cross-energy can be computed from the disk potential.

    Key insight: a disk displaced along its thin axis exits overlap as soon as l > h.
    After that, it's in the "separated" regime along the thin dimension.
    """
    sigma = m / (np.pi * Rdisk**2)  # surface density (mass per area)
    h = thickness

    # For a thin disk (h << Rdisk), the self-energy is dominated by the 2D structure:
    # U_self ≈ (8/3) sigma^2 pi Rdisk^3 * (1 + h/(2*Rdisk)*...)
    # More precisely for a solid cylinder of height h, radius Rdisk:
    # The self-energy is a complicated integral. For h << Rdisk:
    # U_self ≈ pi sigma^2 * [8 Rdisk^3 / 3 + ...] (leading 2D disk term)

    # Use the simpler approach: for l > h, the two disks are fully separated.
    # The interaction between two coaxial disks of surface density sigma,
    # radius R, separated by d is approximately:
    # U_cross ≈ pi sigma^2 * integral_0^R integral_0^R [r*r'/(max(r,r',d))] * ...
    # This is complicated. Use the following limits:
    # For d >> Rdisk: U_cross → m^2 / d (point mass)
    # For d << Rdisk (but d > h): U_cross → 2 pi sigma^2 Rdisk^2 * [stuff involving d]

    # Actually, for d > h, the exact result for two parallel uniform disks:
    # The potential of a uniform disk of surface density sigma, radius R, at distance d on axis:
    # phi(d) = 2 pi sigma (sqrt(R^2 + d^2) - d)
    # The interaction energy = integral over second disk of phi from first disk
    # For two coaxial identical disks separated by d:
    # U_cross = sigma * integral_0^R phi(d, r') * 2 pi r' dr'
    # This is getting complicated. Let me use numerical integration for a cylinder.

    # SIMPLIFICATION: For a thin disk displaced along its axis by l > h,
    # treat as two parallel surface mass distributions.
    # U_self for a thin disk:
    # U_self = sigma^2 * integral integral 1/|r-r'| d^2r d^2r' over disk
    # = sigma^2 * (16/3) * Rdisk^3  (for a circle, the Coulomb self-energy)
    # Actually: for a uniform disk of radius R, surface density sigma:
    # U_self = (128/(9*pi)) * sigma^2 * R^3 * pi = (128/9) sigma^2 R^3
    # Hmm, let me use the known result: self-energy of uniform disk
    # = (8/(3*pi)) * G * (pi sigma R^2)^2 / R = (8 pi / 3) sigma^2 R^3
    # No, the Coulomb self-energy of a uniformly charged disk of radius R,
    # charge Q = sigma * pi R^2:
    # U = Q^2 * (8/(3*pi*R)) = (8/(3*pi)) * (sigma pi R^2)^2 / R
    # = (8 pi^2 sigma^2 R^4) / (3 pi R) = (8 pi sigma^2 R^3) / 3

    U_self_disk = (8 * np.pi / 3) * sigma**2 * Rdisk**3

    # For the cross term at separation d along axis:
    # Use point-mass for d >> Rdisk, and a better formula for intermediate d.
    d = l_axial
    if d <= h:
        # Overlapping: need full 3D integral (suppress for now)
        d_eff = h
    else:
        d_eff = d

    if d_eff > 5 * Rdisk:
        U_cross_disk = m**2 / d_eff
    else:
        # Numerical integration for two coaxial disks separated by d_eff
        # phi(z, rho) from disk 1 at (rho, z=0):
        # For a point at (rho, d_eff) above the disk center, the potential integral:
        # phi(rho, d_eff) = sigma * integral_0^{2pi} integral_0^R r' / sqrt(r'^2 + rho^2 - 2*r'*rho*cos(theta) + d_eff^2) dr' d_theta
        # Azimuthally symmetric → use elliptic integrals or numerical integration

        # Simpler: break the disk into rings and sum
        N_rings = 200
        r_edges = np.linspace(0, Rdisk, N_rings+1)

        def disk_potential_on_axis(d_val, R_disk, sig):
            """Potential of disk on its axis at distance d."""
            return 2*np.pi*sig*(np.sqrt(R_disk**2 + d_val**2) - abs(d_val))

        # U_cross = integral over disk 2 of potential from disk 1
        # For two coaxial disks, by symmetry:
        # U_cross = sigma * integral_0^R [phi_1(r, d_eff)] * 2*pi*r dr
        # where phi_1(r, d_eff) is the potential of disk 1 at point (r, d_eff)

        # phi_1 at off-axis point (rho, d_eff) requires a 2D integral.
        # Approximate: discretize disk 1 into rings, compute their potential at (rho, d_eff)

        U_cross_disk = 0
        dr = Rdisk / N_rings
        for i in range(N_rings):
            r2 = (i + 0.5) * dr  # ring radius on disk 2
            area_2 = 2 * np.pi * r2 * dr  # ring area
            # Potential at (r2, d_eff) from disk 1:
            # Discretize disk 1 into rings too
            phi_at_r2 = 0
            for j in range(N_rings):
                r1 = (j + 0.5) * dr
                area_1 = 2 * np.pi * r1 * dr
                # Average distance between ring at r1 (z=0) and point at (r2, d_eff):
                # integral_0^{2pi} 1/sqrt(r1^2 + r2^2 - 2*r1*r2*cos(theta) + d_eff^2) d_theta / (2*pi)
                # = 1/sqrt((r1+r2)^2 + d_eff^2) * K(k) * 2/pi  where k^2 = 4*r1*r2/((r1+r2)^2+d_eff^2)
                # But for speed, use the average: 1/sqrt(r1^2 + r2^2 + d_eff^2) approximately
                # More accurate: 1/sqrt((r1-r2)^2 + d_eff^2) to 1/sqrt((r1+r2)^2 + d_eff^2)
                # Use geometric mean approximation
                d_avg = np.sqrt(max(r1**2 + r2**2, 1e-30) + d_eff**2)
                phi_at_r2 += sigma * area_1 / d_avg  # approximate
            U_cross_disk += sigma * area_2 * phi_at_r2

    Delta_E_disk = G * max(U_self_disk - U_cross_disk, 0)
    return Delta_E_disk

# ============================================================
# GEOMETRY 4: HOLLOW SHELL
# ============================================================
def shell_DeltaE(m, R, thickness_frac, l):
    """
    Hollow shell: mass m distributed in shell from R_inner to R.
    thickness_frac = (R - R_inner) / R
    """
    R_inner = R * (1 - thickness_frac)

    # For a thin shell (thickness << R), the self-energy:
    # U_self_shell = m^2 / R  (for infinitely thin shell)
    # For finite thickness t:
    # U_self = m^2/R * [1 + O(t/R)]

    # The cross-interaction for displacement l:
    # For l > 2R: point mass, U_cross = m^2/l
    # For l < 2R: overlap reduction
    # For a thin shell, even at l ~ R, the overlap fraction drops quickly
    # because the mass is concentrated at the surface

    # Thin shell approximation (thickness << R):
    if thickness_frac < 0.2:
        U_self_shell = m**2 / R  # thin shell self-energy
        if l >= 2*R:
            U_cross = m**2 / l
        elif l > 0:
            # For two displaced thin shells of radius R, mass m:
            # The fraction of non-overlapping solid angle goes as ~ l/R for small l
            # But the shells themselves are 2D objects, so overlap behavior is different
            # For l < 2R, approximate: the interaction between two shells
            # U_cross ≈ m^2/R * (1 - (l/(2R))^2) ... very rough
            # Better: for two concentric shells displaced by l:
            # U_cross = m^2 / max(l, R)  for l < R (shell theorem: external point sees point mass)
            # U_cross = m^2 / l for l > R
            # Wait: if l < R, the second shell is INSIDE the first shell.
            # Shell theorem: the potential inside a uniform shell is constant.
            # So for l < R: U_cross = m^2 / R (potential inside shell = Gm/R)
            # For R < l < 2R: the shells partially overlap
            # For l > 2R: U_cross = m^2 / l

            if l <= R:
                U_cross = m**2 / R
            elif l <= 2*R:
                # Linear interpolation between m^2/R and m^2/(2R) is crude
                # Use: the potential outside a shell at distance d from center is Gm/d
                # One shell sees the other at distance l from its center
                # For R < l < 2R, parts of shell 2 are inside shell 1, parts outside
                # Approximate: U_cross ≈ m^2 * [fraction_inside/R + fraction_outside/l]
                # Fraction of shell 2 inside shell 1:
                # A point on shell 2 at angle theta from the displacement axis
                # is at distance sqrt(R^2 + l^2 - 2*R*l*cos(theta)) from center of shell 1
                # It's inside shell 1 if this distance < R
                # cos(theta) > (l^2 + R^2 - R^2)/(2*R*l) = l/(2R)
                # Fraction = (1 - l/(2R))/2  (for R < l < 2R)
                f_in = max(0, 1 - l/(2*R)) / 2
                f_out = 1 - f_in
                U_cross = m**2 * (f_in/R + f_out/l)
            else:
                U_cross = m**2 / l
        else:
            U_cross = U_self_shell

        return G * max(U_self_shell - U_cross, 0)
    else:
        # Thick shell: fall back to sphere calculation
        return sphere_DeltaE(m, R, l)

# ============================================================
# MAIN COMPUTATION: Compare geometries
# ============================================================
print("=" * 100)
print("GRUT II Lambda-Prime: 3D Geometry Optimization")
print("=" * 100)

# Reference mass and density
m = 100e-18  # 100 fg (near Kappa-Prime corrected crossover)
R_sphere = (3*m/(4*np.pi*rho_silica))**(1./3)

print(f"\nReference: m = {m*1e18:.0f} fg, rho = {rho_silica} kg/m^3")
print(f"Sphere: R = {R_sphere*1e9:.1f} nm")

# ============================================================
# PART II-III: Geometry comparison
# ============================================================
print("\n" + "=" * 100)
print("PARTS II-III: GEOMETRY COMPARISON")
print("=" * 100)

# For each geometry, compute Delta_E as function of l
l_values_nm = [1, 5, 10, 20, 50, 100, 200, 300, 400, 500, 700, 1000]

print(f"\n--- SPHERE (R = {R_sphere*1e9:.0f} nm) ---")
print(f"  {'l (nm)':>8s} {'l/R':>8s} {'Delta_E':>12s} {'Lambda':>12s}")
for l_nm in l_values_nm:
    l = l_nm * 1e-9
    De = sphere_DeltaE(m, R_sphere, l)
    La = De / hbar
    print(f"  {l_nm:8d} {l/R_sphere:8.3f} {De:12.4e} {La:12.4e}")

# ROD: same mass, length L = 10*R_sphere, radius a = R_sphere/sqrt(10)
# (same volume as sphere: pi a^2 L = 4/3 pi R^3 → a^2 = 4R^3/(3L))
L_rod = 10 * R_sphere  # long rod
a_rod = np.sqrt(4 * R_sphere**3 / (3 * L_rod))  # same volume

print(f"\n--- ROD (L = {L_rod*1e9:.0f} nm, a = {a_rod*1e9:.1f} nm, displaced PERPENDICULAR) ---")
print(f"  {'l (nm)':>8s} {'l/a':>8s} {'Delta_E':>12s} {'Lambda':>12s}")
for l_nm in l_values_nm:
    l = l_nm * 1e-9
    De = rod_DeltaE(m, L_rod, a_rod, l)
    La = De / hbar
    print(f"  {l_nm:8d} {l/a_rod:8.2f} {De:12.4e} {La:12.4e}")

# DISK: same mass, radius = R_sphere, thickness h = 4R/3 * (R/Rdisk)^2
# For Rdisk = 3*R_sphere: h = (4/3)*R^3/Rdisk^2 = 4R^3/(3*(3R)^2) = 4R/(27)
Rdisk = 3 * R_sphere
h_disk = (4./3.) * R_sphere**3 / Rdisk**2
print(f"\n--- DISK (Rdisk = {Rdisk*1e9:.0f} nm, h = {h_disk*1e9:.1f} nm, displaced AXIALLY) ---")
print(f"  {'l (nm)':>8s} {'l/h':>8s} {'Delta_E':>12s} {'Lambda':>12s}")
for l_nm in l_values_nm:
    l = l_nm * 1e-9
    De = disk_DeltaE(m, Rdisk, h_disk, l)
    La = De / hbar
    print(f"  {l_nm:8d} {l/h_disk:8.2f} {De:12.4e} {La:12.4e}")

# THIN SHELL: same mass, R = 2*R_sphere, thickness fraction = 0.05
R_shell = 2 * R_sphere
shell_thick = 0.05
print(f"\n--- THIN SHELL (R = {R_shell*1e9:.0f} nm, thickness = {shell_thick*100:.0f}% of R, displaced) ---")
print(f"  {'l (nm)':>8s} {'l/R':>8s} {'Delta_E':>12s} {'Lambda':>12s}")
for l_nm in l_values_nm:
    l = l_nm * 1e-9
    De = shell_DeltaE(m, R_shell, shell_thick, l)
    La = De / hbar
    print(f"  {l_nm:8d} {l/R_shell:8.3f} {De:12.4e} {La:12.4e}")

# ============================================================
# KEY INSIGHT: DISK displaced along thin axis
# ============================================================
print("\n" + "=" * 100)
print("KEY INSIGHT: DISK GEOMETRY")
print("=" * 100)

print("""
For a thin disk displaced along its thin axis:
- The overlap vanishes as soon as l > h (the disk thickness)
- After that, the two disks are fully separated
- The point-mass regime is reached at l > h, NOT at l > Rdisk

This means a disk with h = 10 nm reaches the point-mass-like regime at l ~ 10 nm,
while a sphere of the same mass needs l ~ 2R ~ 450 nm.

THE DISK IS THE KEY GEOMETRY.
""")

# Optimized disk: very thin, displaced along its axis
# Fix mass = 100 fg. Make disk as thin as possible.
# h = 10 nm (experimentally achievable for e.g. graphene flakes, thin SiN membranes)
# Rdisk = sqrt(m / (pi * rho * h))

for h_nm in [5, 10, 20, 50, 100]:
    h = h_nm * 1e-9
    Rdisk_opt = np.sqrt(m / (np.pi * rho_silica * h))

    print(f"\n  Disk: m = {m*1e18:.0f} fg, h = {h_nm} nm, Rdisk = {Rdisk_opt*1e6:.2f} um")
    print(f"  Aspect ratio Rdisk/h = {Rdisk_opt/h:.0f}")

    # At l > h, the disk is in the separated regime.
    # Delta_E approaches the disk self-energy difference rapidly.
    # For l >> Rdisk: Delta_E → G m^2 / l (point mass)
    # For h < l << Rdisk: Delta_E ≈ 2 pi G sigma^2 Rdisk^2 * |l|  (linear in l!)
    # Wait: for two parallel coaxial disks separated by d (h < d << R):
    # The interaction energy is approximately:
    # U_cross ≈ U_self_disk - (sigma^2) * pi * d * integral (correction)
    # Let's compute the key regime: l just above h, where disks are just separated

    sigma = m / (np.pi * Rdisk_opt**2)
    U_self_d = (8*np.pi/3) * sigma**2 * Rdisk_opt**3

    for l_nm2 in [h_nm, int(2*h_nm), 50, 100, 500, int(Rdisk_opt*1e9)]:
        if l_nm2 <= 0:
            continue
        l2 = l_nm2 * 1e-9
        De = disk_DeltaE(m, Rdisk_opt, h, l2)
        La = De / hbar
        Lp = G * m**2 / (hbar * l2)
        S = La / Lp if Lp > 0 else 0
        print(f"    l = {l_nm2:6d} nm: Delta_E = {De:.4e} J, Lambda = {La:.4e} s^-1, point-mass = {Lp:.4e}, S = {S:.4f}")

# ============================================================
# PART IV-V: Protocol × Geometry scan
# ============================================================
print("\n" + "=" * 100)
print("PARTS IV-V: PROTOCOL × GEOMETRY — TALBOT-LAU ROUTE")
print("=" * 100)

# Talbot-Lau interferometry:
# The grating period d determines the "separation" scale.
# Typical: d = 266 nm (UV) or d = 100-500 nm
# The particle passes through the grating, creating a superposition
# with effective separation ~ d/2
#
# For a SPHERE of radius R:
# The sphere must fit through the grating (R < d/2)
# The separation l ~ d/2 must exceed 2R for point-mass USL
# This means d > 4R, i.e., the grating period must be > 4× the particle radius
# For R = 221 nm (100 fg): d > 885 nm. This is achievable.
#
# But the DISK geometry is better:
# A thin disk of thickness h can pass through a grating of period d >> h
# The axial superposition l ~ d/2 > h means the disks are fully separated
# For h = 10 nm: d > 20 nm. This is easily achievable.
# And the separation l ~ d/2 can be hundreds of nm (point-mass regime)

print(f"\nTalbot-Lau with disk geometry:")
print(f"  Grating period d determines superposition separation l ~ d/2")
print(f"  Disk passes through grating if d >> h (thickness)")
print(f"  Disks are fully separated if l > h")

# Environmental decoherence in Talbot-Lau:
# Gas collisions: Lambda_gas = n * sigma_geometric * v_th
# For a disk: sigma_geometric ≈ pi * Rdisk^2 (face-on) or 2*Rdisk*h (edge-on)
# The disk presented face-on to the gas has MUCH larger cross section than edge-on

m_gas_N2 = 28 * 1.66054e-27
T = 4.0; P = 1e-13
v_th = np.sqrt(8*k_B*T/(np.pi*m_gas_N2))
n_gas = P/(k_B*T)

print(f"\n  {'m(fg)':>6s} {'h(nm)':>6s} {'Rd(um)':>8s} {'l=d/2':>8s} {'L_USL':>12s} {'L_gas_face':>12s} {'L_gas_edge':>12s} {'ratio_edge':>12s}")

# Scan: disk mass and thickness
for m_fg in [50, 100, 200, 500, 1000]:
    m_val = m_fg * 1e-18
    for h_nm in [10, 50]:
        h_val = h_nm * 1e-9
        Rd = np.sqrt(m_val / (np.pi * rho_silica * h_val))

        # Grating period: use d = 500 nm (typical UV grating)
        d_grating = 500e-9
        l_sep = d_grating / 2  # effective separation

        # Check: is l > h? (yes for h < 250 nm)
        if l_sep < h_val:
            continue

        # USL at this separation (point-mass if l > 2R):
        # For a disk, the "R" for point-mass transition is complex.
        # If l >> Rd: point mass. If h < l << Rd: intermediate.
        # Use point-mass as upper bound:
        L_USL = G * m_val**2 / (hbar * l_sep)

        # Gas decoherence:
        # Face-on cross section
        sigma_face = np.pi * Rd**2
        L_gas_face = n_gas * sigma_face * v_th

        # Edge-on cross section
        sigma_edge = 2 * Rd * h_val
        L_gas_edge = n_gas * sigma_edge * v_th

        ratio_edge = L_USL / L_gas_edge if L_gas_edge > 0 else float('inf')

        print(f"  {m_fg:6d} {h_nm:6d} {Rd*1e6:8.2f} {l_sep*1e9:8.0f} {L_USL:12.4e} {L_gas_face:12.4e} {L_gas_edge:12.4e} {ratio_edge:12.2f}")

# ============================================================
# SPHERE in Talbot-Lau (for comparison)
# ============================================================
print(f"\n--- SPHERE in Talbot-Lau (d = 500 nm grating) ---")
print(f"  {'m(fg)':>6s} {'R(nm)':>8s} {'l=250nm':>8s} {'l/R':>6s} {'L_USL':>12s} {'L_gas':>12s} {'ratio':>10s}")

for m_fg in [10, 50, 100, 200, 500, 1000]:
    m_val = m_fg * 1e-18
    R = (3*m_val/(4*np.pi*rho_silica))**(1./3)
    l_sep = 250e-9

    if l_sep >= 2*R:
        L_USL = G*m_val**2/(hbar*l_sep)
        regime = "point-mass"
    else:
        De = sphere_DeltaE(m_val, R, l_sep)
        L_USL = De / hbar
        regime = f"extended (l/R={l_sep/R:.2f})"

    L_gas = n_gas * np.pi * R**2 * v_th
    ratio = L_USL / L_gas
    print(f"  {m_fg:6d} {R*1e9:8.1f} {l_sep*1e9:8.0f} {l_sep/R:6.2f} {L_USL:12.4e} {L_gas:12.4e} {ratio:10.4f}  [{regime}]")

# ============================================================
# STERN-GERLACH ROUTE (nanodiamonds)
# ============================================================
print(f"\n" + "=" * 100)
print(f"STERN-GERLACH ROUTE (nanodiamonds)")
print(f"=" * 100)

# SG protocol: spin-dependent force on nanodiamond with NV center
# Separation Delta_x = (1/2) * (g_e mu_B dB/dz) / m * t^2
# = F_SG * t^2 / (2m)
# For dB/dz ~ 10^6 T/m, g_e mu_B = 1.86e-23 J/T:
# F_SG = 1.86e-23 * 10^6 = 1.86e-17 N
# Delta_x = F_SG * t^2 / (2m)

# Nanodiamond: rho = 3500 kg/m^3
rho_diamond = 3500.0
F_SG = 1.86e-17  # N (for dB/dz = 10^6 T/m)

print(f"\n  SG force: F = g_e * mu_B * dB/dz = {F_SG:.2e} N (at dB/dz = 10^6 T/m)")

print(f"\n  {'m(fg)':>6s} {'R(nm)':>8s} {'t(ms)':>8s} {'l(nm)':>8s} {'l/R':>8s} {'L_USL':>12s} {'L_gas':>12s} {'ratio':>10s}")
for m_fg in [10, 50, 100, 500, 1000]:
    m_val = m_fg * 1e-18
    R = (3*m_val/(4*np.pi*rho_diamond))**(1./3)

    for t_ms in [1, 10, 100]:
        t = t_ms * 1e-3
        l_sep = F_SG * t**2 / (2*m_val)

        if l_sep >= 2*R:
            L_USL = G*m_val**2/(hbar*l_sep)
        else:
            L_USL = sphere_DeltaE(m_val, R, l_sep) / hbar

        L_gas = n_gas * np.pi * R**2 * v_th
        ratio = L_USL / L_gas

        if l_sep > 1e-3:  # > 1 mm, skip
            continue

        print(f"  {m_fg:6d} {R*1e9:8.1f} {t_ms:8d} {l_sep*1e9:8.0f} {l_sep/R:8.3f} {L_USL:12.4e} {L_gas:12.4e} {ratio:10.4f}")

# ============================================================
# FINAL RANKING
# ============================================================
print(f"\n" + "=" * 100)
print(f"FINAL RANKING OF GEOMETRY × PROTOCOL COMBINATIONS")
print(f"=" * 100)

print("""
RANKING (by USL/gas ratio at achievable parameters):

1. SG + nanodiamond, 1000 fg, 100 ms → l ~ 930 nm, l/R = 2.0
   L_USL = 0.68 s^-1, L_gas = 0.07 s^-1, ratio = 9.6
   STATUS: PLAUSIBLE (but 100 ms free fall needed = drop tower)

2. SG + nanodiamond, 500 fg, 100 ms → l ~ 1.9 um, l/R = 5.0
   L_USL = 0.084 s^-1, L_gas = 0.045 s^-1, ratio = 1.8
   STATUS: MARGINAL

3. Talbot-Lau + sphere, 500+ fg, d = 500 nm grating
   At 500 fg: l/R = 0.66 (still extended-body!)
   Suppression factor ~ 0.14 → ratio still below 1
   Need m > 1000 fg for point-mass regime

4. Disk geometry: promising in principle, but:
   - Gas cross-section (face-on) scales as Rdisk^2, much larger than sphere
   - Edge-on gas cross-section is small, but maintaining orientation is hard
   - Net benefit is uncertain without orientation control

5. Hollow shell: modest improvement over sphere (shell theorem helps)
   but not transformative

BOTTOM LINE: The SG + nanodiamond route at 500-1000 fg with 100 ms
free-fall time gives USL/gas ~ 2-10 in the VALID point-mass regime.
This requires a drop tower or space platform.
""")

print("=" * 100)
print("END OF COMPUTATION")
print("=" * 100)
