a, b, c, d = map(float, input().split())
media = ((a*2)+(b*3)+(c*4)+d)/10
if media >= 7:
    print("Media: %.1f" % media)
    print("Aluno aprovado.")
elif 5 <= media <= 6.9:
    print("Media: %.1f" % media)
    print("Aluno em exame.")
    exame = float(input())
    print("Nota do exame: %.1f" % exame)
    if exame >= 5:
        print("Aluno aprovado.")
        print("Media final: %.1f" % ((media + exame)/2))
    else:
        print("Aluno reprovado.")
else:
    print("Aluno reprovado.")