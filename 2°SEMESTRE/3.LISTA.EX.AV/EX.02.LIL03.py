import random
mat=[]
a1=0
a2=0
a3=[]
for i in range(4):
    linha=[]
    for k in range(6):
        linha.append(random.randint(1, 50))
        if 10 < linha[k] < 30:
            a1 += 1
        if linha[k]>10:
            a2 += linha[k]
    mat.append(linha)
for j in range(4):
    a3.append(mat[j][3])

print("MATRIZ:",mat)
print(a3)
print("A quantidade de números que estão no intervalo entre 10 e 30 é {}".format(a1))
print("A soma dos números maiores que 10 é {}".format(a2))
print("A soma dos números que estão na quarta coluna da matriz é{}".format(sum(a3)))
print("A média dos números da matriz que estão na terceira linha é {:0.2f}".format(sum(mat[2])/len(mat[2])))
