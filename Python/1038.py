#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 01:33:02 2017

@author: daruin
"""

n = int(input()).split(' ')

a, b = n


if (a == 1):
    total = b * 4
elif (a == 2):
    total = b * 4.5
elif (a == 3):
    total = b * 5
elif (a == 4):
    total = b * 5
elif (a == 5):
    total = (b * 1.5)
print('Total: R$ %.2' % total)