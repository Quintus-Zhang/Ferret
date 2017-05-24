#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 14:46:50 2017

@author: Quintus
"""
from scipy.stats import norm
import numpy as np
from OptionsPricing import OptionsPricing

class BSClosedForm(OptionsPricing):
    # call or put
    def price(self):
        d1 = ((self.r + 0.5 * self.sigma**2) * self.T - np.log(self.K / self.S0)) / (self.sigma * np.sqrt(self.T))
        d2 = ((self.r - 0.5 * self.sigma**2) * self.T - np.log(self.K / self.S0)) / (self.sigma * np.sqrt(self.T))
        if self.is_call:
            p = self.S0 * norm.cdf(d1) - np.exp(-self.r * self.T) * self.K * norm.cdf(d2) 
        else:               
            p = np.exp(-self.r * self.T) * self.K * norm.cdf(-d2) - self.S0 * norm.cdf(-d1)
        return p