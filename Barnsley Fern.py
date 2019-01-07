# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 19:08:34 2018

@author: JDeCarvalho
"""

import matplotlib.pyplot as plt
import numpy as np

def f1 (x, y):
    return (0, (0.16)*y)

def f2 (x, y):
    return (((0.85*x)+(0.04*y)), ((-0.04*x)+(0.85*y)+1.6))

def f3 (x, y):
    return (((0.2*x)-(0.26*y)),((0.23*x)+(0.22*y)+1.6))

def f4 (x, y):
    return (((-0.15*x)+(0.28*y)),((0.26*x)+(0.24*y)+0.44))

plt.figure(num=None, figsize=(15,15), dpi=80, facecolor='w', edgecolor='k' )
x = 0
y = 0
plt.plot(x, y, 'go', markersize=1)
for i in range(0, 1000):
     dice = np.random.randint(100, size=1)
     if(dice == 0):
         (x,y) = f1(x,y)
     elif(dice < 6):
         (x,y) = f3(x,y)
     elif(dice < 13):
         (x,y) = f4(x,y)
     else:
         (x,y) = f2(x,y)
     plt.plot(x, y, 'go', markersize=1)
plt.title('Barnsley Fern')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.savefig('fern.pdf', bbox_inches='tight')
plt.show()

     
