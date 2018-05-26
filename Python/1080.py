n = int( input () )
temp = 0
cont = 1
pos = 1
while cont < 100:
    temp = int(input())
    cont = cont + 1
    if temp > n:
        n = temp
        pos = cont
print("%d" %n)
print("%d" %pos)
