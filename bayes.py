# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 14:37:27 2019

@author: JDeCarvalho
"""

def bayes_odds (prior, evidence):
    a = prior[0]
    b = prior[1]
    for e in evidence:    
        a = a * e[0]
        b = b * e[1]
    posterior = [a, b]
    return posterior

print (bayes_odds([1, 1], [[2, 1], [1, 4], [1, 2]]))

