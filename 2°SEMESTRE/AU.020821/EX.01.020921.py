linome=[]
lipeso=[]
liidade=[]
a=1
for i in range(10):
    nome=str(input("Digite o nome")).upper()
    peso=int(input("Digite o peso"))
    idade=int(input("Digite a idade"))
    linome.append(nome)
    lipeso.append(peso)
    liidade.append(idade)

while a>0:
    perg=str(input("Digite nome a ser pesquisado"
                   "Para, parar digite Fim")).upper()

    if perg == "FIM":
        break
    for j in range(10):
        if perg == linome[j-1]:
            print("Nome: ",linome[j-1])
            print("Peso:",lipeso[j -1],"Kg.")
            print("Idade:",liidade[j-1]," anos.")

        else:
            print("Este nome não está na lista!")