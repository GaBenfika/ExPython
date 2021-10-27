import random
mat=[]
impar=[]
primo=[]
maior=[]
coluna=[]
li=0
for i in range(3):
    linha=[]
    for j in range(5):
        linha.append(random.randint(1, 50))
        div = 0
        for k in range(1, linha[j]+1):
            if linha[j] %k==0:
                div += 1
        if div == 2:
            primo.append(linha[j])

        if linha[j] %2 == 0:
            print("")
        else:
            impar.append(linha[j])

    maior.append(max(linha))
    coluna.append(linha.index(max(linha))+1)
    mat.append(linha)
li += maior.index(max(maior))
medimpar=sum(impar)/len(impar)

print("A matriz:", mat)
print("O maior elemento da matriz é {} em qual linha:{} e coluna:{} ".format(max(maior), li+1, coluna[li]))
print("A média dos números ímpares da matriz é {:0.2f}".format(medimpar))
print("Mostre na tela todos os números primos, se houver: {}".format(primo))
