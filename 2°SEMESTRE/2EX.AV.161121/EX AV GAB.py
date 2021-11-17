import random
mat=[]
mult3=[]
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

        if k == 2:
            if linha[2]<menor:
                menor = linha[2]

        if linha[k] %3==0:
            mult3.append(linha[k])
    if i==4:
        lin5.append(linha)
        tot=sum(linha)

    med=sum(linha)/len(linha)
    medlista.append(med)
    mat.append(linha)
media3=sum(mult3)/len(mult3)
print("="*100)
print("RESPOSTAS")
print("="*100)
print("Matriz:", mat)
print("="*100)
print("Média dos multiplos de 3 Ã© :", media3)
print("="*100)
print("Menor nÃºmero da terceira coluna Ã© :", menor)
print("="*100)
print("Qauntidade de nÃºmeros Ã­mpares entre 10 e 15 inclusive, Ã© :", quant)
print("="*100)
print("A mÃ©dia das linhas sÃ£o :", medlista)
print("="*100)
print("A mÃ©dia dos nÃºmeros da 5Â° Linha Ã© :", tot/5)
print("="*100)