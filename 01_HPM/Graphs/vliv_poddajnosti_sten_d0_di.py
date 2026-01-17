#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 12:59:28 2025

@author: jakubkoci
"""

import numpy as np
import matplotlib.pyplot as plt

# --- Parameters from the formula ---
mu = 0.25          # Poisson's ratio
Ek = 1.6e9         # Bulk modulus of liquid [Pa]
E_ratios = [0.002, 0.004, 0.006, 0.008, 0.01]  # Ek/E

# d0/di range (as in the original figure)
d_ratio = np.linspace(1.0, 1.25, 600)

# --- Plot ---
plt.figure(figsize=(7, 5))

for Ek_E in E_ratios:
    E = Ek / Ek_E  # Elastic modulus of tube material
    num = d_ratio**2 - 1
    den = d_ratio**2 - 1 + (2 * Ek / E) * (
        d_ratio**2 * (1 + mu) + (1 - mu)
    )
    Ee_Ek = num / den
    plt.plot(d_ratio, Ee_Ek, label=f"Eₖ/E = {Ek_E:g}")

plt.xlabel("d₀ / dᵢ [-]")
plt.ylabel("Eₑ / Eₖ [-]")
plt.legend(title="")
plt.grid(True)

# Save as vector SVG in current directory
output_path = "vliv_poddajnosti_sten.svg"
plt.savefig(output_path, format="svg")
plt.close()

output_path
