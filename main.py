#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 15:19:37 2017

@author: Quintus
"""
from ExplicitEu import ExplicitEu
from ImplicitEu import ImplicitEu
from CNEu import CNEu
from ImplicitAm import ImplicitAmBer
from ImplicitAm import ImplicitAmBre

if __name__ == "__main__":
    
    # set up parameters
    S0 = 50
    K = 50
    r = 0.1
    T = 5./12
    sigma = 0.4
    Smax = 100
    M = 100
    N = 1000
    is_call = True
    
    # pricing 
    option = ExplicitEu(S0, K, r, T, sigma, Smax, M, 1000, is_call)
    print(option.price())
    
    option = ExplicitEu(S0, K, r, T, sigma, Smax, M, 100, is_call)
    print(option.price())
    
    
    option = ImplicitEu(S0, K, r, T, sigma, Smax, M, 1000, is_call)
    print(option.price())

    option = ImplicitEu(S0, K, r, T, sigma, Smax, M, 100, is_call)
    print(option.price())
    
    
    option = CNEu(S0, K, r, T, sigma, Smax, M, 1000, is_call)
    print(option.price())

    option = CNEu(S0, K, r, T, sigma, Smax, M, 100, is_call)
    print(option.price())
    
    
    
    option = ImplicitAmBer(S0, K, r, T, sigma, Smax, M, 1000, is_call)
    print(option.price())
    
    option = ImplicitAmBre(S0, K, r, T, sigma, Smax, M, 1000, is_call)
    print(option.price())