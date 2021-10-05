
listanome=[]
listapeso=[]
listaaltura=[]
listaimc=[]
for i in range(5):
    nome=str(input("Digite o nome"))
    peso=int(input("Digite o peso"))
    altura=float(input("Digite sua altura em metros"))

    listanome.append(nome)
    listapeso.append(peso)
    listaaltura.append(altura)

    imc=peso/(altura * altura)
    listaimc.append(imc)


print(listanome)
print(listapeso)
print(listaaltura)
print(listaimc)

for i in range(5):
    print("O sr(a) {} tem o peso de {} e altura de {}m, com isso ela possui um IMC de {:0.2f}".format(listanome[i-1],listapeso[i-1],listaaltura[i-1],listaimc[i-1]))