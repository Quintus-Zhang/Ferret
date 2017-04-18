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

