from random import randint
nome = []
idade_lista = []
altura = []
idade_sub = 0
porc = 0
porce_altura = 0

for i in range(5):
    nome.append(str(input("Qual o nome? ")))
    idade_lista.append(randint(1, 50))
    altura.append(float(input("Qual a altura ?")))
media_idade = sum(idade_lista)/5
media_altura = sum(altura)/5
for altura in altura:
    if altura < 1.5:
        porc += 1
        porce_altura=(porc *100)/5

for idade in idade_lista:
    if idade > media_idade:
        idade_sub += 1

for idade in range(5):
    if min(idade_lista) == idade_lista[idade]:
        menor = idade
print("A menor idade  é de  {} anos  e se chama {}".format(min(idade_lista),nome[menor]))
print("A media das idades é {:.0f} na media das alturas é {:.2f}".format(media_idade,media_altura))
print("A quantidade de pessoas com idade maior que a media é  de {}".format(idade_sub))
print("A porcentagem de pessoas com altura inferior a 1.5 é de {}%".format(porce_altura))