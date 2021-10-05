import random
mat=[]
maiord=[]
col1=[]
tot=[]
quant=0
for i in range(5):
    linha=[]
    for j in range(5):
        linha.append(random.randint(1, 50))
        tot.append(linha[j])
    mat.append(linha)

print(mat)

for k in range(5):
    maiord.append(mat[k-1][k-1])
    col1.append(mat[k-1][1])
    for l in range(5):
        if mat[k-1][l-1] > (sum(tot)/len(tot)):
            quant += 1


print(maiord)
print("o maior número da diagonal principal da matriz é: {}".format(max(maiord)))
print("o maior número da coluna 2, ou seja, índice 1, é {}".format(max(col1)))
print("a quantidade de números da matriz que são maiores que média dos números da matriz é: {}".format(quant))
