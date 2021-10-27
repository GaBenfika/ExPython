import random
#Escreva um  programa  que  armazene  em  uma  matriz,  o  nome  e  duas  notas  de  5 alunos. Calcule e armazene em uma listaa média de cada aluno e em outralistao status (media>= 6, “aprovado”, caso contrário, “reprovado”)
#faça  uma  opção  para  que  o  usuário  possa  fazer  uma  pesquisar  por  nome.  Se encontrar seja exibido na tela:
#posição em que foi encontrado(índice)
#nome do aluno
#as duas notas e a média
#status;
mat=[]
med=[]
status=[]
notas=[]
nomes=[]
#Criando a Matriz e Lista
for i in range(3):
    linha=[]
    linha2=[]
    for k in range(5):
        if i == 0:
            linha.append(str(input("Nome do Aluno")))
            nomes.append(linha[k])
        else:
            linha.append(random.randint(0, 10))
            linha2.append(linha[k])
    notas.append(linha2)
    mat.append(linha)

#Preenchendo Lista de Status
for i in range(5):
    med.append(((mat[1][i]+mat[2][i])/2))
    if med[i]>=6:
        status.append("APROVADO")
    else:
        status.append("REPROVADO")

print(mat)
print(med)
print(status)


nome=str(input("Digite o Nome para pesquisar."))
if nome in nomes:
    print("Posição é {}".format(nomes.index(nome)+1))
    print("Nome do aluno é {}".format(nome))
    print("As duas notas {} e {} e a média {}".format(mat[1][nomes.index(nome)],mat[2][nomes.index(nome)],med[nomes.index(nome)]))
    print("status= {}".format(status[nomes.index(nome)]))
else:
    print("Nome não está na lista!")