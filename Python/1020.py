#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 12:35:41 2017

@author: daruin
"""

valor = int(input())

ano = valor/365
year = valor%365
mes = year/30
mounth = year%30
dia = mounth

print('%d ano(s)' % ano)
print('%d mes(es)' % mes)
print('%d dia(s)' % dia)
