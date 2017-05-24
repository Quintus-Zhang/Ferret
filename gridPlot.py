#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 14:59:22 2017

@author: Quintus
"""

import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(6,5))
points = np.arange(0, 10, 1)
xs, ys = np.meshgrid(points, points)
plt.scatter(xs, ys, color='lightslategrey')


# set axis limit
plt.axis([-0.5, 9.5, -0.5, 9.5])

# set axes labels
plt.title('$0$---------------------$t$--------------------->$T$', fontsize=20)
plt.ylabel('$S_{max}$<---------------$S$---------------$0$', fontsize=20)

# delete tick parameters & frames of graph
plt.tick_params(top='off', bottom='off', left='off', right='off', 
                labelleft='off', labeltop='off', labelbottom='off')
for spine in plt.gca().spines.values():
    spine.set_visible(False)

# invert the Y axis
ax = plt.gca()
ax.invert_yaxis()

#==============================================================================
# boundary conditions
#==============================================================================
plt.scatter(xs[[0, 1]], ys[[0, -1]], color='darkorange')
plt.scatter(xs[:, -1], ys[:, -1], color='darkorange')

plt.text(4.5, 0, 'Boundary Condition', horizontalalignment='center')
plt.text(4.5, 8.9, 'Boundary Condition', horizontalalignment='center')
plt.text(8.7, 3, 'Terminal Condition', rotation='vertical')


#==============================================================================
# methods illustration
#==============================================================================
# Explicit Method
f = {'i': 2, 'j': 6}
plt.plot([f['j'], f['j']+1], [f['i'], f['i']-1], '-', c='darkorange', linewidth=3)
plt.plot([f['j'], f['j']+1], [f['i'], f['i']], '-', c='darkorange', linewidth=3)
plt.plot([f['j'], f['j']+1], [f['i'], f['i']+1], '-', c='darkorange', linewidth=3)

plt.text(f['j']+0.5, f['i']-1.5, 'Explicit Method', horizontalalignment='center')
plt.text(f['j'], f['i'], '$f_{i, j}$', horizontalalignment='right', fontsize=18)
plt.text(f['j']+1, f['i']-1, '$f_{i-1, j+1}$', horizontalalignment='left', fontsize=18)
plt.text(f['j']+1, f['i'], '$f_{i, j+1}$', horizontalalignment='left', fontsize=18)
plt.text(f['j']+1, f['i']+1, '$f_{i+1, j+1}$', horizontalalignment='left', fontsize=18)

# Implicit Method
f = {'i': 2, 'j': 2}
plt.plot([f['j']+1, f['j']], [f['i'], f['i']-1], '-', c='darkorange', linewidth=3)
plt.plot([f['j']+1, f['j']], [f['i'], f['i']], '-', c='darkorange', linewidth=3)
plt.plot([f['j']+1, f['j']], [f['i'], f['i']+1], '-', c='darkorange', linewidth=3)

plt.text(f['j']+0.5, f['i']-1.5, 'Implicit Method', horizontalalignment='center')
plt.text(f['j']+1, f['i'], '$f_{i, j+1}$', horizontalalignment='left', fontsize=18)
plt.text(f['j'], f['i']-1, '$f_{i-1, j}$', horizontalalignment='right', fontsize=18)
plt.text(f['j'], f['i'], '$f_{i, j}$', horizontalalignment='right', fontsize=18)
plt.text(f['j'], f['i']+1, '$f_{i+1, j}$', horizontalalignment='right', fontsize=18)

# Crank-Nicolson Method
f = {'i': 6, 'j': 4}
plt.plot([f['j'], f['j']+1], [f['i'], f['i']], '-', c='darkorange', linewidth=3)
plt.plot([f['j'], f['j']], [f['i']-1, f['i']+1], '-', c='darkorange', linewidth=3)
plt.plot([f['j']+1, f['j']+1], [f['i']-1, f['i']+1], '-', c='darkorange', linewidth=3)

plt.text(f['j']+0.5, f['i']-1.5, 'Crank-Nicolson Method', horizontalalignment='center')
plt.text(f['j'], f['i']-1, '$f_{i-1, j}$', horizontalalignment='right', fontsize=18)
plt.text(f['j'], f['i'], '$f_{i, j}$', horizontalalignment='right', fontsize=18)
plt.text(f['j'], f['i']+1, '$f_{i+1, j}$', horizontalalignment='right', fontsize=18)
plt.text(f['j']+1, f['i']-1, '$f_{i-1, j+1}$', horizontalalignment='left', fontsize=18)
plt.text(f['j']+1, f['i'], '$f_{i, j+1}$', horizontalalignment='left', fontsize=18)
plt.text(f['j']+1, f['i']+1, '$f_{i+1, j+1}$', horizontalalignment='left', fontsize=18)
