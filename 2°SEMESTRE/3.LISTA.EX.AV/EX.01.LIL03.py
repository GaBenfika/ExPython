import random

mat = []
mult=[]
tot=[]
menor=51
for i in range(3):
    linha = []
    for k in range(5):
        linha.append(random.randint(1, 50))
        tot.append(linha[k])
        if linha[k] %3 == 0:
            mult.append(linha[k])

    mat.append(linha)

print("MATRIZ:", mat)

#Escreva um programa que leia uma matriz de ordem 3 x 5 de elementos inteiros, calcule e mostre na tela:

print("menor número da matriz é {}".format(min(tot)))
print("soma dos números múltiplos de 3 da matriz é {}".format(sum(mult)))
print("média dos números da matriz é {:0.2f}".format(sum(tot)/len(tot)))
