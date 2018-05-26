#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 10:48:27 2017

@author: daruin
"""

n = int(input())
x = 0
contador = 0
while x in range(n):
    lista = raw_input().split()
    lista.sort()
    print(lista)
    contador += 1
    if contador == n:
        break
