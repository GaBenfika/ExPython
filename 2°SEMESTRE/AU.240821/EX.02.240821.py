
listanome=[]
listaidade=[]
listaabaixo=[]

maior2=0
idadeabaixo=0
for i in range(10):
    nome=str(input("Nome do aluno."))
    idade=int(input("Idade do aluno."))
    listanome.append(nome)
    listaidade.append(idade)
    if(idade>15):
        maior2 += 1

medidade=sum(listaidade)/len(listaidade)

for i in range(len(listaidade)):
    if(listaidade[i-1]<medidade):
        idadeabaixo += 1


print("a quantidade de alunos que tem idade superior a 15 {}".format(maior2))
print("a média das idades dos alunos {:0.0f} ".format(medidade))
print("a quantidade de alunos que tem idade abaixo da média {} ".format(idadeabaixo))