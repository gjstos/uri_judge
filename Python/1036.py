#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 23:55:18 2017

@author: daruin
"""
import math

a, b, c = input().split(' ')

a = float(a)
b = float(b)
c = float(c)

delta = b*b-4*a*c


if (delta > 0 and a!=0):
    r1 = (-b + math.sqrt(delta)) / (2 * a)
    r2 = (-b - math.sqrt(delta)) / (2 * a)
    print('R1 = %.5f\nR2 = %.5f' % (r1, r2))
    
else:
    print('Impossivel calcular')