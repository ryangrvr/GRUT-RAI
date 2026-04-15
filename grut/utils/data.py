"""Experimental Data Tables — PDG, Planck, material properties."""

# Planck 2018 cosmological parameters
PLANCK_2018 = {
    "H_0": {"value": 67.4, "error": 0.5, "unit": "km/s/Mpc"},
    "Omega_Lambda": {"value": 0.6889, "error": 0.0056},
    "Omega_m": {"value": 0.3111, "error": 0.0056},
    "Omega_b_h2": {"value": 0.02242, "error": 0.00014},
    "n_s": {"value": 0.9649, "error": 0.0042},
    "sigma_8": {"value": 0.8111, "error": 0.0060},
    "tau_reion": {"value": 0.0544, "error": 0.0073},
    "eta_B": {"value": 6.12e-10, "error": 0.04e-10},
    "N_eff": {"value": 2.99, "error": 0.17},
    "z_eq": {"value": 3402, "error": 26},
}

# SH0ES (late-universe)
SHOES = {"H_0": {"value": 73.04, "error": 1.04, "unit": "km/s/Mpc"}}

# PDG 2024 particle masses
PDG_MASSES = {
    "electron": {"mass_GeV": 0.000511, "error_GeV": 0},
    "muon": {"mass_GeV": 0.10566, "error_GeV": 0.00001},
    "tau": {"mass_GeV": 1.77686, "error_GeV": 0.00012},
    "up": {"mass_GeV": 0.00216, "error_GeV": 0.00049},
    "down": {"mass_GeV": 0.00467, "error_GeV": 0.00048},
    "strange": {"mass_GeV": 0.0934, "error_GeV": 0.0084},
    "charm": {"mass_GeV": 1.27, "error_GeV": 0.02},
    "bottom": {"mass_GeV": 4.18, "error_GeV": 0.03},
    "top": {"mass_GeV": 173.0, "error_GeV": 0.4},
    "W": {"mass_GeV": 80.377, "error_GeV": 0.012},
    "Z": {"mass_GeV": 91.1876, "error_GeV": 0.0021},
    "Higgs": {"mass_GeV": 125.25, "error_GeV": 0.17},
}

PDG_CONSTANTS = {
    "G_F": {"value": 1.1663788e-5, "unit": "GeV^-2", "description": "Fermi constant"},
    "alpha_s_MZ": {"value": 0.1185, "error": 0.0006, "description": "Strong coupling at M_Z"},
    "alpha_em": {"value": 1/137.036, "description": "Fine structure constant"},
    "sin2_theta_W": {"value": 0.23122, "error": 0.00003, "description": "Weak mixing angle"},
    "J_CP": {"value": 3.18e-5, "error": 0.15e-5, "description": "Jarlskog invariant"},
    "V_us": {"value": 0.2243, "error": 0.0005, "description": "CKM element"},
    "V_cb": {"value": 0.0422, "error": 0.0008, "description": "CKM element"},
}

MATERIALS = {
    "gold": {"density": 19300, "symbol": "Au"},
    "silica": {"density": 2200, "symbol": "SiO2"},
    "diamond": {"density": 3510, "symbol": "C"},
    "silicon": {"density": 2330, "symbol": "Si"},
    "water": {"density": 1000, "symbol": "H2O"},
    "protein": {"density": 1350, "symbol": "~"},
    "tungsten": {"density": 19250, "symbol": "W"},
    "osmium": {"density": 22590, "symbol": "Os"},
}
