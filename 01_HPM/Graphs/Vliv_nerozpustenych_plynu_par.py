#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 12:54:36 2025

@author: jakubkoci
"""

import numpy as np
import matplotlib.pyplot as plt

# Parameters
Ek = 1.6e9        # Bulk modulus of liquid [Pa]
pa = 1e5          # Atmospheric pressure [Pa]
n = 1.4           # Polytropic exponent

# More lambdas near 0.001
lambdas = [0.0005, 0.001, 0.002, 0.01, 0.05]

# Pressure range
p = np.linspace(1e5, 3e7, 600)  # 0.1 to 30 MPa

# Plot
plt.figure(figsize=(7,5))
for lam in lambdas:
    Ee_Ek = (1 + lam * (p/pa)**(1/n)) / (1 + (lam * Ek / (n*p)) * (p/pa)**(1/n))
    plt.plot(p/1e6, Ee_Ek, label=f"α = {lam:g}")

plt.xlabel("Tlak p [MPa]")
plt.ylabel("Eₑ / Eₖ [-]")
plt.legend()
plt.grid(True)

# Save as vector SVG
output_path = "vliv_nerozpustenych_plynu_Ee_Ek.svg"
plt.savefig(output_path, format="svg")
plt.close()

output_path
