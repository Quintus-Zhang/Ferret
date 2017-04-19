#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 13:45:10 2017

@author: Quintus
"""

import numpy as np

dS = Smax / float(M)
dt = T / float(N)

iValues = np.arange(1, M)

jValues = np.arange(N)

grid = np.zeros(shape=(M+1, N+1))

SValues = np.linspace(0, Smax, M+1)

alpha =  0.5*dt * (r * iValues - sigma**2 * iValues**2)
beta  =  dt * (r + sigma**2 * iValues**2)
gamma = -0.5*dt * (r * iValues + sigma**2 * iValues**2)
coeffs = np.diag(alpha[1:], -1) + \
              np.diag(1 + beta) + \
              np.diag(gamma[:-1], 1)

if is_call:
    grid[:, -1] = np.maximum(SValues - K, 0)
else:
    grid[:, -1] = np.maximum(K - SValues, 0)
    
# side boundary conditions
coeffs[0,   0] += 2*alpha[0]
coeffs[0,   1] -= alpha[0]
coeffs[-1, -1] += 2*gamma[-1]
coeffs[-1, -2] -= gamma[-1]

IV = grid[np.arange(1,M), -1]

multiplier = np.zeros(M-2)
for i in reversed(range(1, M-1)):
    multiplier[i-1] = coeffs[i-1, i] / coeffs[i, i] 
    coeffs[i-1, :] -= coeffs[i, :] * coeffs[i-1, i] / coeffs[i, i] 
                    
for j in reversed(jValues):
    # 
    #grid[1:-2, j+1] -= multiplier * grid[2:-1, j+1] #!!!
    for i in reversed(range(1, M-1)):
        grid[i, j+1] -= grid[i+1, j+1] * multiplier[i-1]
    # solve recursively from the top
    for i in range(1, M):
        if i == 1:
            grid[i, j] = grid[i, j+1] / coeffs[i-1, i-1]
        else:
            grid[i, j] = (grid[i, j+1] - grid[i-1, j]*coeffs[i-1, i-2]) / coeffs[i-1, i-1]
        if grid[i, j] < IV[i-1]:
            grid[i, j] = IV[i-1]