import random
#Escreva um  programa  que  preencha  uma  listar  com  os  nomes  de 10 alunos,  e outralistacom a média dos alunos. Calcule e mostre:#a)A média de salário da população
#a média da classe;
#a quantidade de alunos que tiveram média igual ou superior a7;
#a quantidade de alunos que tiveram média abaixo de 7;
#a maior média da classe e nome do aluno que obteve a maior média

aluno=[]
med=[]
menor=0
maior=0
for i in range(10):
    aluno.append(input("Nome do aluno"))
    med.append(random.randint(1, 10))
    if med[i] < 7:
        menor += 1
    if med[i] > 7:
        maior += 1

mediaclasse=sum(med)/len(med)

print("Nome alunos", aluno)
print("Media notas",med)

print("a média da classe é = {}".format(mediaclasse))
print("a quantidade de alunos que tiveram média igual ou superior a 7 é {}".format(maior))
print("a quantidade de alunos que tiveram média abaixo de 7 é {}".format(menor))
print("a maior média da classe é {} e nome do aluno que obteve a maior média é {}".format(max(med), aluno[med.index(max(med))]))
