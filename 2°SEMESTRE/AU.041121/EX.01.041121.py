#Preencha uma lista com 10 nomes de
#alunos Em seguida utilize o método upper
#para transformar em letra maiúscula todos
#os nomes armazenados na lista Faça uma
#rotina que procure por nomes nessa lista e
#substitua esse nome por outro
li=[]
for i in range(4):
    al=str(input("Nome do aluno"))
    li.append(al.upper())

print(li)
pesquisa=str(input("Digite nome para procurar")).upper()
nome=str(input("Novo nome".upper()))
for k in range(4):
    if pesquisa in li[k]:
        li[k].replace(li[k],nome)

