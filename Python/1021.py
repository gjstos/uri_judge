#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 12:44:57 2017

@author: daruin
"""

money = float(input())

cem = money/100
sob = money%100
cinq = sob/50
sub = sob%50
vin = sub/20
res = sub%20
dez = res/10
fin = res%10
cin = fin/5
end = fin%5
dois = end/2
fim = end%2
um = fim/1
moe = fim%1
cinqc = moe/0.50
mo = moe%0.50
vincin = mo/0.25
moed = mo%0.25
dezc = moed/0.10
moeda = moed%0.10
cinc = moeda/0.05
moedas = moeda%0.05
umc = moedas/0.01000

print('NOTAS:\n%d nota(s) de R$ 100.00\n%d nota(s) de R$ 50.00\n%d nota(s) de R$ 20.00\n%d nota(s) de R$ 10.00\n%d nota(s) de R$ 5.00\n%d nota(s) de R$ 2.00' % (cem, cinq, vin, dez, cin, dois))
print('MOEDAS:\n%d moeda(s) de R$ 1.00\n%d moeda(s) de R$ 0.50\n%d moeda(s) de R$ 0.25\n%d moeda(s) de R$ 0.10\n%d moeda(s) de R$ 0.05\n%d moeda(s) de R$ 0.01' % (um, cinqc, vincin, dezc, cinc, umc))
