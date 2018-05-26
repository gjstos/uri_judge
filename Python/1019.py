#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 12:00:34 2017

@author: daruin
"""

seg = int(input())

horas = seg/3600
sob = seg%3600
minu = sob/60
res = sob%60
seg = res

print(('%d:%d:%d') % (horas,minu,seg))
