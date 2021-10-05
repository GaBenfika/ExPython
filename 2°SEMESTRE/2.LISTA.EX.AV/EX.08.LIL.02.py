import random
livend=[]
livenda=[]
comi=[]
for i in range(5):
    vend=str(input("Digite o nome de um vendedor"))
    venda=random.randint(300,30000)
    comissao = venda * 0.1

    livend.append(vend)
    livenda.append(venda)
    comi.append(comissao)
medvenda=sum(livenda)/len(livenda)

mais=0
for k in range(5):
    if livenda[k-1]<medvenda:
        mais += 1

local=livenda.index(max(livenda))

for j in range(5):
    print(" O vendedor {}, ganhou um total de R${}".format(livend[j-1],livenda[j-1]))
print("O total vendido pelos 5 é de R${}".format(sum(livenda)))
print("A média de vendas é de R${}".format(medvenda))
print("{} vendedores venderam mais que a média".format(mais))
print("{} teve maior valor de comissão de R${}".format(livend[local],livenda[local]))