#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 01:03:09 2017

@author: daruin
"""

n = float(input())

if n >= 0 and n <= 25:
    print('Intervalo [0,25]')
if n > 25 and n <= 50:
    print('Intervalo (25,50]')
if n > 50 and n <= 75:
    print('Intervalo (50,75]')
if n > 75 and n <= 100:
    print('Intervalo (75,100]')
if n < 0:
    print('Fora do intervalo')