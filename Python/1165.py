#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 19:44:48 2017

@author: daruin
"""

num = int(input())
y = 1
x = 0
divisores = 0
n = 1

while n in range(1, num + 1):
    x = int(input())
    for y in range(1,x + 1):
        if x%y ==0:
            divisores += 1
        y = y+1
    if divisores == 2:
        print('%d eh primo' % x)
    else:
        print('%d nao eh primo' % x)
    divisores = 0
    n += 1