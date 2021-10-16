import random
# Escreva um programa que leia uma matriz de ordem 5 x 4, onde na 1ª coluna da matriz são armazenados os nomes dos
# vendedores, da 2ª coluna a 4ª coluna dão armazenados  as  total  de  vendas  por  mês  de  cada  vendedor,
# portando  na2ª coluna  é  armazenado  a  venda  do  mês  1,  3ª  coluna  do  mês  2  e  na  4ª  coluna  do mês 3.
# Calcule e mostre na tela:
# a)O valor total vendido por vendedor
# b)A maior venda do mês 1
# c)A menor venda do mês 3
# d)O total vendido por mês

mat=[]
for i in range(5):
    linha=[]
    for k in range(4):
        if k == 0:
            vend=str(input("Digite o nome do vendedor."))
            linha.append(vend)
        else:
            linha.append(random.randint(1000, 10000))
    mat.append(linha)
print(mat)
maior1=0
menor3=11000
for j in range(5):
    print("O vendedor {} vendeu um total de R${}".format(mat[j][0], (mat[j][1]+mat[j][2]+mat[j][3])))
    if mat[j][1]>maior1:
        maior1 = mat[j][1]
    if mat[j][3]<menor3:
        menor3 = mat[j][3]

print("A maior venda do mês 1 foi de R${}".format(maior1))
print("A menor venda do mês 3 foi R${}".format(menor3))
print("O total vendido por mês:")
for l in range(3):
    print("Mês {} , total vendido R${}".format(l+1, mat[0][l+1]+mat[1][l+1]+mat[2][l+1]+mat[3][l+1]+mat[4][l+1]))
