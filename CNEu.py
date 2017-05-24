#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 03:36:40 2017

@author: Quintus
"""

import numpy as np
import scipy.linalg as linalg

from ExplicitEu import ExplicitEu

class CNEu(ExplicitEu):
    
    def _setup_coefficients_(self):
        self.alpha = 0.25*self.dt * (self.sigma**2 * self.iValues**2 - self.r * self.iValues)
        self.beta  = -0.5*self.dt * (self.sigma**2 * self.iValues**2 + self.r)
        self.gamma = 0.25*self.dt * (self.sigma**2 * self.iValues**2 + self.r * self.iValues)
        self.coeffs = np.diag(self.alpha[1:], -1) + \
                       np.diag(1 + self.beta) + \
                       np.diag(self.gamma[:-1], 1)
        self.coeffs_ = np.diag(-self.alpha[1:], -1) + \
                       np.diag(1 - self.beta) + \
                       np.diag(-self.gamma[:-1], 1)

                       
    def _setup_boundary_conditions_(self):
        super(CNEu, self)._setup_boundary_conditions_()
        self.coeffs_[0,   0] -= 2*self.alpha[0]
        self.coeffs_[0,   1] += self.alpha[0]
        self.coeffs_[-1, -1] -= 2*self.gamma[-1]
        self.coeffs_[-1, -2] += self.gamma[-1]

    def _traverse_grid_(self):           
        P, L, U = linalg.lu(self.coeffs_)
        for j in reversed(self.jValues):
            Ux = linalg.solve(L, np.dot(self.coeffs, self.grid[1:-1, j+1]))
            self.grid[1:-1, j] = linalg.solve(U, Ux)
            self.grid[0, j] = 2 * self.grid[1, j] - self.grid[2, j]
            self.grid[-1, j] = 2 * self.grid[-2, j] - self.grid[-3, j]
    