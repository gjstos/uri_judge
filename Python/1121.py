n = float(input())
notas = [100,50,20,10,5,2,1,0.5,0.25,0.10,0.05,0.01]
k = 0
acm = 0
print('Notas:')
while k < 5:
    valor = n//(notas[k])
    print('%d nota(s)de R$ .2f' % (valor, notas[k]))
    k += 1
