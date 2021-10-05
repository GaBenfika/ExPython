import random
par=0
tot=0
med=0
mat=[]
mult=0
for i in range(5):
    linha=[]
    for j in range(3):
        linha.append(random.randint(1, 50))
    mat.append(linha)
    tot += sum(linha)
print(mat)
med=tot/15
for k in range(5):
    for l in range(3):
        if mat[k][l] %2 == 0 and mat[k][l] > 10:
            par += mat[k][l]

for k in range(5):
    for l in range(3):
        if mat[k][l] %3 == 0:
            mult += 1

print("A quantidade de números da matriz que são múltiplos de 3 é {}.".format(mult))
print("A soma dos números que são pares e maiores que 10 é {}.".format(par))
print("A média de números que estão armazenados na matriz é {:0.2f}.".format(med))
