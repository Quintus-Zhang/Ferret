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
from BSClosedForm import BSClosedForm

if __name__ == "__main__":
    
    # set up parameters
    S0 = 50
    K = 50
    r = 0.1
    T = 5/12
    sigma = 0.4
    Smax = 100
    M = 100  # S
    N = 1000 # t
    is_call = False
    
    # pricing test
    option = ExplicitEu(S0, K, r, T, sigma, Smax, M, N, is_call)
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
    
    # convergence error 
    def convergeError(method, S0, K, r, T, sigma, Smax, m, n, is_call):
        p = np.array([])
        for M, N in zip(m, n):
            option = method(S0, K, r, T, sigma, Smax, M, N, is_call)
            p = np.append(p, option.price())
        option = BSClosedForm(S0, K, r, T, sigma, is_call)
        error = np.abs(p-option.price())
        return error, p, option.price()
    
    m = np.array([50, 100, 200, 400, 800])
    n = np.array([100, 200, 400, 800, 1600])
    errorImp, impPrice, anaPrice = convergeError(ImplicitEu, S0, K, r, T, sigma, Smax, m, n, is_call)
    errorCN, CNPrice, anaPrice = convergeError(CNEu, S0, K, r, T, sigma, Smax, m, n, is_call)

    #==============================================================================
    # plotting
    #==============================================================================
    # price surface
    def priceSurface(method, S0, K, r, T, sigma, Smax, M, N, is_call):
        fig = plt.figure(figsize=(6,5))
        ax = Axes3D(fig)
        t, S = np.meshgrid(np.linspace(0, 1, N+1), np.linspace(0, Smax, M+1))
        option = method(S0, K, r, T, sigma, Smax, M, N, is_call)
        option.price()
        ax.plot_surface(t, S, option.grid, cmap='coolwarm', linewidth=0, antialiased=False)
        ax.set_xlabel('time')
        ax.set_ylabel('stock price')
        ax.set_zlabel('option price')
        plt.show()
    N = 1000
    priceSurface(ExplicitEu, S0, K, r, T, sigma, Smax, M, N, is_call)
    N = 100
    priceSurface(ExplicitEu, S0, K, r, T, sigma, Smax, M, N, is_call)
    
    
    # convergence
    fig = plt.figure(figsize=(6,5)) 
    ax = fig.gca()
    ax.plot(np.log(n), np.log(errorImp), '*-', c='royalblue')
    ax.plot(np.log(n), np.log(errorCN), '*-', c='darkorange')
    ticks = ax.set_xticks(np.log(n))
    labels = ax.set_xticklabels(['log(100)', 'log(200)', 
                                 'log(400)', 'log(800)', 
                                 'log(1600)'], rotation=10, fontsize='small')
    ax.set_xlabel('log(N)')
    ax.set_ylabel('log(Error)')
    ax.set_title('Difference between numerical solution \n and analytical solution')
    plt.legend(['Implicit Method', 'CN method'])
    plt.show()

    
    
    
    
    