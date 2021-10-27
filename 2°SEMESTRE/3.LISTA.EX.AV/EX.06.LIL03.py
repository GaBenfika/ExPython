import random
#Escreva um   programa   que leia uma   matriz   6   x   10,   some   as   colunas individualmente  e  acumule  as  somas  na  7ª  linha  da  matriz.  O  programa  deverá mostrar o resultado de cada coluna.
mat=[]
for i in range(6):
    linha=[]
    for k in range(10):
        linha.append(random.randint(0, 50))
    mat.append(linha)
tot=[]
for i in range(10):
    soma=0
    for k in range(6):
        soma += mat[k][i]
    print("soma",soma)
    tot.append(soma)
mat.append(tot)
for i in range(7):
    if i == 6:
        print("A soma das colunas:", mat[6])
    else:
        print("Linha N:",i+1,"==>",mat[i])

