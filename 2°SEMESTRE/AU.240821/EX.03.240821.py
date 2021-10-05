import random
listasal=[]
listafilh=[]
totpessoas=0
for i in range(10):
    filh=int(random.randint(0,5))
    sal=int(random.randint(100,5000))
    listafilh.append(filh)
    listasal.append(sal)
    if sal<1000:
        totpessoas += 1

medsal=sum(listasal)/len(listasal)

medfilh=sum(listafilh)/len(listafilh)

maior=max(listasal)

perc=(totpessoas/len(listasal))*100

print(listafilh)
print(listasal)

print("média de salário da população é de R${:0.2f}".format(medsal))
print("média do número de filhos é de aproximadamente {:0.0f} filho por pessoa".format(medfilh))
print("maior salário é de R${},00".format(maior))
print("percentual de pessoas com salário inferior a R$ 1000,00 é de {:0.2f}%".format(perc))