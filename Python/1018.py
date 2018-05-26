#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 11:51:43 2017

@author: daruin
"""

vl = int(input())

cem = vl/100
resto = vl%100
cinq = resto/50
sob = resto%50
vin = sob/20
sub = sob%20
dez = sub/10
fim = sub%10
cin = fim/5
subf = fim%5
dois = subf/2
the = subf%2
um = the/1

print(vl)
print("%d nota(s) de R$ 100,00" % cem)
print("%d nota(s) de R$ 50,00" % cinq)
print("%d nota(s) de R$ 20,00" % vin)
print("%d nota(s) de R$ 10,00" % dez)
print("%d nota(s) de R$ 5,00" % cin)
print("%d nota(s) de R$ 2,00" % dois)
print("%d nota(s) de R$ 1,00" % um)