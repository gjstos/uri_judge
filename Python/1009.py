#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 11:35:21 2017

@author: daruin
"""

nome = input()
slfixo = float(input())
montante = float(input())
bonus = float(montante * 0.15)
total = (slfixo + bonus)
print('TOTAL = R$ %0.2f' % total)