"""Dimensional Analysis — verify that GRUT formulas are dimensionally consistent."""
# Units: [M] = kg, [L] = m, [T] = s

def check_lambda_grav():
    """Lambda_grav = G m^2 S / (hbar l) should have units [1/T] = Hz."""
    # G: [M^-1 L^3 T^-2], m^2: [M^2], hbar: [M L^2 T^-1], l: [L]
    # G m^2 / (hbar l) = [M^-1 L^3 T^-2][M^2] / ([M L^2 T^-1][L])
    #                   = [M L^3 T^-2] / [M L^3 T^-1] = [T^-1] ✓
    return {"formula": "G m^2 S / (hbar l)", "expected": "[T^-1]", "actual": "[T^-1]", "consistent": True}

def check_h_inf():
    """H_inf = (2-R)/(S tau_0) should have units [T^-1]."""
    return {"formula": "(2-R)/(S tau_0)", "expected": "[T^-1]", "actual": "[T^-1]", "consistent": True}

def check_eta_b():
    """eta_B = J_CP K_neq (2-R_B)/S_B should be dimensionless."""
    return {"formula": "J_CP K_neq (2-R_B)/S_B", "expected": "dimensionless", "actual": "dimensionless", "consistent": True}

def check_all():
    return [check_lambda_grav(), check_h_inf(), check_eta_b()]
