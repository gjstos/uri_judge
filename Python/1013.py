#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 12:58:56 2017

@author: daruin
"""

import math

valor = input().split(' ')

a, b, c = valor

maior = (int(a) + int(b) + abs(int(a) - int(b)))/2
resultado = (int(maior) + int(c) + abs(int(maior) - int(c)))/2

print('%d eh o maior' % resultado)

