#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 15:19:37 2017

@author: Quintus
"""
from ExplicitEu import ExplicitEu
from ImplicitEu import ImplicitEu
from CNEu import CNEu


if __name__ == "__main__":
    option = ExplicitEu(50, 50, 0.1, 5./12., 0.4, 100, 100, 1000, False)
    print(option.price())

    option = ExplicitEu(50, 50, 0.1, 5./12., 0.4, 100, 100, 100, False)
    print(option.price())
    
    
    option = ImplicitEu(50, 50, 0.1, 5./12., 0.4, 100, 100, 1000, False)
    print(option.price())

    option = ImplicitEu(50, 50, 0.1, 5./12., 0.4, 100, 100, 100, False)
    print(option.price())
    
    
    option = CNEu(50, 50, 0.1, 5./12., 0.4, 100, 100, 1000, False)
    print(option.price())

    option = CNEu(50, 50, 0.1, 5./12., 0.4, 100, 100, 100, False)
    print(option.price())