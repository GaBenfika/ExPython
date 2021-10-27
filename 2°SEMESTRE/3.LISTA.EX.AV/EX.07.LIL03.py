import random
#A  prefeitura  de  uma  cidade  fez  uma  pesquisa  entre  seus  habitantes,  coletando dados sobre  o salário, idade eo número  de filhos. Escrevaum programa que  leia esses  dados,  por  exemplo  para  10  pessoas.  Armazene  esses  dados  em  uma matriz, depois calcule e mostre:
#A média de salário da população
#A média do número de filhos
#A quantidade de filhos das pessoas que tem idade entre 15 a 25 anos
#A média de salário de pessoas que tem idade entre 20 a 30 anos
n=int(input("Quantas pessoas foram feitas a pesquisas"))
mat=[]
for i in range(3):
    linha=[]
    if i == 0:
        for j in range(n):
            linha.append(random.randint(500, 5000))
    if i == 1:
        for j in range(n):
            linha.append(random.randint(14, 99))
    if i == 2:
        for j in range(n):
            linha.append(random.randint(0, 4))
    mat.append(linha)
for i in range(3):
    print(mat[i])

sal=[]
for i in range(n):
    sal.append(mat[0][i])

filh=[]
for i in range(n):
    filh.append(mat[2][i])
sal2=[]
filh2=[]
for i in range(n):
    if 20>mat[1][i]<30:
        sal2.append(mat[0][i])
    if 15>mat[1][i]<25:
        filh2.append(mat[2][i])
med=sum(sal2)/len(sal2)
print("A média de salário da população é de R${:0.2f}".format(sum(sal)/len(sal)))
print("A média do número de filhos é {:0.0f}".format(sum(filh)/len(filh)))
print("A quantidade de filhos das pessoas que tem idade entre 15 a 25 anos é {}".format(sum(filh2)))
print("A média de salário de pessoas que tem idade entre 20 a 30 anos é R${:0.2f}".format(med))