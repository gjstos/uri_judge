#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 12:12:47 2017

@author: daruin
"""

valor = input().split(' ')

a, b, c = valor
pi = 3.14159

triangulo = (float(a) * float(c))/2
circulo = pi * (float(c) * float(c))
trapezio = (float(a) + float(b)) * float(c) / 2
quadrado = float(b) * float (b)
retangulo = float(a) * float(b)

print ('TRIANGULO: %0.3f\nCIRCULO: %0.3f\nTRAPEZIO: %0.3f\nQUADRADO: %0.3f\nRETANGULO: %0.3f' % (triangulo, circulo, trapezio, quadrado,retangulo))