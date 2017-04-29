#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 15:19:37 2017

@author: Quintus
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from ExplicitEu import ExplicitEu
from ImplicitEu import ImplicitEu
from CNEu import CNEu
from ImplicitAm import ImplicitAmBer
from ImplicitAm import ImplicitAmBre

if __name__ == "__main__":
    
    # set up parameters
    S0 = 0
    K = 10
    r = 0.1
    T = 0.25
    sigma = 0.4
    Smax = 50
    M = 200
    N = 2000
    is_call = True
    
    # pricing
    option = ExplicitEu(S0, K, r, T, sigma, Smax, M, N, is_call)
    option.price()
    V = option.grid
    
    T = np.linspace(0, 1, N+1)
    T = np.tile(T, (M+1, 1))
    S = np.linspace(0, Smax, M+1)
    S = np.tile(S, (N+1, 1)).T
    
#    option = ExplicitEu(S0, K, r, T, sigma, Smax, M, 100, is_call)
#    print(option.price())
#    
#    
#    option = ImplicitEu(S0, K, r, T, sigma, Smax, M, 1000, is_call)
#    print(option.price())
#
#    option = ImplicitEu(S0, K, r, T, sigma, Smax, M, 100, is_call)
#    print(option.price())
#    
#    
#    option = CNEu(S0, K, r, T, sigma, Smax, M, 1000, is_call)
#    print(option.price())
#
#    option = CNEu(S0, K, r, T, sigma, Smax, M, 100, is_call)
#    print(option.price())
#    
#    
#    
#    option = ImplicitAmBer(S0, K, r, T, sigma, Smax, M, 1000, is_call)
#    print(option.price())
#    
#    option = ImplicitAmBre(S0, K, r, T, sigma, Smax, M, 1000, is_call)
#    print(option.price())

#==============================================================================
# plotting
#==============================================================================

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_wireframe(T, S, V, label='parametric curve')
ax.legend()

plt.show()
