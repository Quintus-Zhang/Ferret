#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 14:49:45 2017

@author: Quintus
"""

class OptionsPricing(object):
    def __init__(self, S0, K, r, T, sigma, is_call=True):
        self.S0 = S0
        self.K = K
        self.r = r
        self.T = T
        self.sigma = sigma
        self.is_call = is_call
