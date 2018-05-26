#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 23:16:12 2017

@author: daruin
"""

line1 = input().split(' ')

A, B, C, D = line1

if int(B) > int(C) and int(D) > int(A) and int(C) + int(D) > int(A) + int(B) and int(C) > 0 and int(D) > 0 and int(A)%2==0:
    print("Valores aceitos")

else:
    print("Valores nao aceitos")