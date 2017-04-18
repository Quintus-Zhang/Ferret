#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 22:33:27 2017

@author: Quintus
"""
import numpy as np
import scipy.linalg as linalg

from ExplicitEu import ExplicitEu

class ImplicitEu(ExplicitEu):
    
    def _setup_coefficients_(self):
        self.alpha =  0.5*self.dt * (self.r * self.iValues - self.sigma**2 * self.iValues**2)
        self.beta  =  self.dt * (self.r + self.sigma**2 * self.iValues**2)
        self.gamma = -0.5*self.dt * (self.r * self.iValues + self.sigma**2 * self.iValues**2)
        self.coeffs = np.diag(self.alpha[1:], -1) + \
                      np.diag(1 + self.beta) + \
                      np.diag(self.gamma[:-1], 1)
    
    def _traverse_grid_(self):           
        P, L, U = linalg.lu(self.coeffs)
        for j in reversed(self.jValues):
            Ux = linalg.solve(L, self.grid[1:-1, j+1])
            self.grid[1:-1, j] = linalg.solve(U, Ux)

if __name__ == "__main__":
    option = ImplicitEu(50, 50, 0.1, 5./12., 0.4, 100, 100, 1000, False)
    print(option.price())

    option = ImplicitEu(50, 50, 0.1, 5./12., 0.4, 100, 100, 100, False)
    print(option.price())