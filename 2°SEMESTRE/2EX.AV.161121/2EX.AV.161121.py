import random
mat=[]
mult3=0
menor=101
lin5=[]
quant=0
medlista=[]
tot=0
for i in range(5):
    linha=[]
    med=0
    for k in range(5):
        linha.append(random.randint(1, 100))

        if linha[k] %2==0:
            print()
        else:
            if 10<=linha[k]<=15:
                quant += 1

        if linha[0]<menor:
            menor = linha[0]

        if linha[k] %3==0:
            mult3 += linha[k]
    if i==4:
        lin5.append(linha)
        tot=sum(linha)

    med=sum(linha)/len(linha)
    medlista.append(med)
    mat.append(linha)

print("="*100)
print("RESPOSTAS")
print("="*100)
print("Matriz:", mat)
print("="*100)
print("Soma multiplos de 3 é :", mult3)
print("="*100)
print("Menor número da primeira coluna é :", menor)
print("="*100)
print("Qauntidade de números ímpares entre 10 e 15 inclusive, é :", quant)
print("="*100)
print("A média das linhas são :", medlista)
print("="*100)
print("A média dos números da 5° Linha é :", tot/5)
print("="*100)
