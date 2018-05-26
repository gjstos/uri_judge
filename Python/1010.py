		#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 11:53:47 2017

@author: daruin
"""

A = input().split(' ')
B = input().split(' ')
cod1, qnt1, vlr1 = A
cod2, qnt2, vlr2 = B
valortt = int(qnt1) * float(vlr1) + int(qnt2) * float(vlr2)
print('VALOR A PAGAR: R$ %.2f' %valortt)
