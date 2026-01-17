#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 12:59:28 2025

@author: jakubkoci
"""

import numpy as np
import matplotlib.pyplot as plt

# Mřížka
x = np.linspace(-4, 4, 800)
y = np.linspace(-2, 2, 400)
X, Y = np.meshgrid(x, y)

def electric_field(charges):
    Ex = np.zeros_like(X)
    Ey = np.zeros_like(Y)
    for q, x0, y0 in charges:
        rx = X - x0
        ry = Y - y0
        r2 = rx**2 + ry**2
        r2[r2 < 0.03] = 0.03
        Ex += q * rx / r2**(3/2)
        Ey += q * ry / r2**(3/2)
    return Ex, Ey

# Náboje
charges_left = [
    (-1, -2.5, 0),
    (-1, -1.5, 0)
]

charges_right = [
    (+1, 1.5, 0),
    (-1, 2.5, 0)
]

ExL, EyL = electric_field(charges_left)
ExR, EyR = electric_field(charges_right)

gap = 0.25
mask_left = X < -gap
mask_right = X > gap

Ex = np.zeros_like(X)
Ey = np.zeros_like(Y)
Ex[mask_left] = ExL[mask_left]
Ey[mask_left] = EyL[mask_left]
Ex[mask_right] = ExR[mask_right]
Ey[mask_right] = EyR[mask_right]

# -----------------------------
# START POINTS OKOLO NÁBOJŮ
# -----------------------------
def charge_seed_points(x0, y0, r=0.15, n=20):
    angles = np.linspace(0, 2*np.pi, n, endpoint=False)
    return np.column_stack([
        x0 + r*np.cos(angles),
        y0 + r*np.sin(angles)
    ])

start_points = []
for q, x0, y0 in charges_left + charges_right:
    start_points.append(charge_seed_points(x0, y0))

start_points = np.vstack(start_points)

# -----------------------------
# Vykreslení
# -----------------------------
plt.figure(figsize=(10, 4))

plt.streamplot(
    X, Y, Ex, Ey,
    start_points=start_points,
    linewidth=1.2,
    arrowsize=1.2,
    color="tab:blue"
)

# -----------------------------
# NÁBOJE A POPIS (AŽ NAKONEC)
# -----------------------------
def draw_charge(x, y, q):
    plt.scatter(
        x, y,
        s=700,
        c="#f1c40f",
        edgecolors="black",
        linewidths=1.5,
        zorder=10
    )
    label = "q⁺" if q > 0 else "q⁻"
    plt.text(
        x, y, label,
        ha="center", va="center",
        fontsize=18,
        weight="bold",
        zorder=11
    )

for q, x0, y0 in charges_left + charges_right:
    draw_charge(x0, y0, q)

plt.axis("off")
plt.xlim(-4, 4)
plt.ylim(-2, 2)

plt.show()
plt.savefig("elektricke_pole.svg", format="svg", bbox_inches="tight")
plt.close()
