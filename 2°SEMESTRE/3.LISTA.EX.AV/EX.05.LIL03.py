import random
#Escrevaum programa que preencha uma matriz 4x 3com números inteiros, calcule e mostrena tela:
#a)A soma dos elementos que estão na 2ª e 4ª linha da matriz
# b)A soma dos números primos
mat=[]
soma=0
somaprimo=0
div=0
for i in range(4):
    linha=[]
    for j in range(3):
        linha.append(random.randint(1, 80))
        div = 0
        for k in range(1, linha[j] + 1):
            if linha[j] % k == 0:
                div += 1
        if div == 2:
            somaprimo += linha[j]
    mat.append(linha)
    if i==1 or i==3:
        soma += sum(linha)
print("Matriz=", mat)

print("A soma dos elementos que estão na 2ª e 4ª linha da matriz é {}".format(soma))
print("A soma dos números primos é:",somaprimo)
