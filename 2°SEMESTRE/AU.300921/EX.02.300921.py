import random
mat=[]
med=0
tot1=0
soma=0
quant=0
for i in range(4):
    linha=[]
    for j in range(3):
        linha.append(random.randint(1, 50))
    mat.append(linha)
print(mat)

for i in range(3):
    tot1 += mat[2][i]
med = tot1 / 3
for i in range(4):
    soma += mat[i][1]

for i in range(4):
    for j in range(3):
        if 5 < mat[i][j] < 15:
            quant += 1



print("A média dos numero da linha 3 é {:0.2f}".format(med))
print("A soma dos números da 2ª coluna é {}".format(soma))
print("A quantidade de números maiores que 5 e menores que 15 armazenados na matriz é {}".format(quant))
print(mat[0])
print(mat[1])
print(mat[2])
print(mat[3])
