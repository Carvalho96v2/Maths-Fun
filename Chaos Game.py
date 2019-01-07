# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 09:38:06 2018

@author: JDeCarvalho
"""

import matplotlib.pyplot as plt
import numpy as np


def findMidpoint (a, b):
    return ((a[0] + b[0])/2, (a[1] + b[1])/2)

def nextTarget(case, a, b, c, d, e):
    if(case == 0):
        return a
    elif (case == 1):
        return b
    elif(case == 2):
        return c
    elif(case == 3):
        return d


a = (0,0)
b = (0, 10000)
c = (10000, 10000)
d = (10000,0)
e = (8000, 0)
f = (15000, 15000)
seed = np.random.randint(10, size=2)

plt.plot([a[0], b[0], c[0], d[0]], [a[1], b[1], c[1], d[1]], 'ro')
plt.plot([seed[0]], [seed[1]], 'g.')
prev = 0
for i in range(0, 10000): 
    target = nextTarget(np.random.randint(4, size=1), a, b, c, d, e)
    while(prev == target):
        target = nextTarget(np.random.randint(4, size=1), a, b, c, d, e)
    prev = target
    seed = findMidpoint(seed, target)
    plt.plot([seed[0]], [seed[1]], 'b.', markersize=1)
    
    