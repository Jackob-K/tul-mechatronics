#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 12:59:28 2025

@author: jakubkoci
"""

from matplotlib import pyplot as plt
import numpy as np

# Create figure
plt.figure(figsize=(8, 2))

# Main pipe line
plt.plot([0.1, 0.9], [0.5, 0.5], linewidth=2)

# Flow arrows
plt.arrow(0.05, 0.5, 0.05, 0, head_width=0.03, head_length=0.02, length_includes_head=True)
plt.arrow(0.9, 0.5, 0.05, 0, head_width=0.03, head_length=0.02, length_includes_head=True)

# Labels
plt.text(0.03, 0.62, r"$Q_A$", fontsize=14)
plt.text(0.92, 0.62, r"$Q_A$", fontsize=14)
plt.text(0.02, 0.32, r"$p_1$", fontsize=14)
plt.text(0.92, 0.32, r"$p_2$", fontsize=14)

# Resistance symbols
theta = np.linspace(0, np.pi, 200)

x1 = 0.35 + 0.05 * np.cos(theta)
y1 = 0.55 + 0.05 * np.sin(theta)
plt.plot(x1, y1, linewidth=1.5)
plt.plot(x1, 0.45 - (y1 - 0.55), linewidth=1.5)

x2 = 0.65 + 0.05 * np.cos(theta)
y2 = 0.55 + 0.05 * np.sin(theta)
plt.plot(x2, y2, linewidth=1.5)
plt.plot(x2, 0.45 - (y2 - 0.55), linewidth=1.5)

# Resistance labels
plt.text(0.33, 0.7, r"$R_1$", fontsize=14)
plt.text(0.63, 0.7, r"$R_2$", fontsize=14)
plt.text(0.32, 0.25, r"$\Delta p_1$", fontsize=14)
plt.text(0.62, 0.25, r"$\Delta p_2$", fontsize=14)

plt.axis("off")

# Save SVG
path = "hydraulicky_odpor_schema.svg"
plt.savefig(path, format="svg", bbox_inches="tight")
plt.close()

path
