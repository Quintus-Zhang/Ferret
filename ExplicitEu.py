#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 22:30:45 2017

@author: Quintus
"""

import numpy as np

from FiniteDifferences import FiniteDifferences

class ExplicitEu(FiniteDifferences):
    
    def _setup_coefficients_(self):
        self.alpha = 0.5*self.dt * (self.sigma**2 * self.iValues**2 - self.r * self.iValues)
        self.beta  = - self.dt * (self.sigma**2 * self.iValues**2 + self.r)
        self.gamma = 0.5*self.dt * (self.sigma**2 * self.iValues**2 + self.r * self.iValues)
        self.coeffs = np.diag(self.alpha[1:], -1) + \
                      np.diag(1 + self.beta) + \
                      np.diag(self.gamma[:-1], 1)
        
    def _setup_boundary_conditions_(self):
        # terminal condition
        if self.is_call:
            self.grid[:, -1] = np.maximum(self.SValues - self.K, 0)
        else:
            self.grid[:, -1] = np.maximum(self.K - self.SValues, 0)
            
        # side boundary conditions
        self.coeffs[0,   0] += 2*self.alpha[0]
        self.coeffs[0,   1] -= self.alpha[0]
        self.coeffs[-1, -1] += 2*self.gamma[-1]
        self.coeffs[-1, -2] -= self.gamma[-1]
        
    def _traverse_grid_(self):
        for j in reversed(self.jValues):
            self.grid[1:-1, j] = np.dot(self.coeffs, self.grid[1:-1, j+1])

            
if __name__ == "__main__":
    # from FDExplicitEu import FDExplicitEu
    option = ExplicitEu(50, 50, 0.1, 5./12., 0.4, 100, 100, 1000, False)
    print(option.price())

    option = ExplicitEu(50, 50, 0.1, 5./12., 0.4, 100, 100, 100, False)
    print(option.price())
    