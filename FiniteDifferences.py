#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from OptionsPricing import OptionsPricing

class FiniteDifferences(OptionsPricing):
    """ Shared attributes and functions of FD """

    def __init__(self, S0, K, r, T, sigma, Smax, M, N, is_call=True):
        super(FiniteDifferences, self).__init__(S0, K, r, T, sigma, is_call)
        self.Smax = Smax
        self.M, self.N = int(M), int(N)  # Ensure M&N are integers

        self.dS = Smax / float(self.M)
        self.dt = T / float(self.N)
        self.iValues = np.arange(1, self.M)
        self.jValues = np.arange(self.N)
        self.grid = np.zeros(shape=(self.M+1, self.N+1)) # grid is M+1 by N+1
        self.SValues = np.linspace(0, Smax, self.M+1)

    def _setup_boundary_conditions_(self):
        pass

    def _setup_coefficients_(self):
        pass

    def _traverse_grid_(self):
        """  Iterate the grid backwards in time """
        pass

    def _interpolate_(self):
        """
        Use piecewise linear interpolation on the initial
        grid column to get the closest price at S0.
        """
        return np.interp(self.S0,
                         self.SValues,
                         self.grid[:, 0])

    def price(self):
        self._setup_coefficients_()
        self._setup_boundary_conditions_()
        self._traverse_grid_()
        return self._interpolate_()