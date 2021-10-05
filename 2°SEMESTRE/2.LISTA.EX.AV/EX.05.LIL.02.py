import random
lilprod=[]
lilpreco=[]
menor10=0
maismed=0
for i in range(5):
    prod=str(input("Digite o nome do produto"))
    lilprod.append(prod)
    lilpreco.append(random.randint(0, 100))
    if lilpreco[i-1] < 10:
        menor10 += 1
media=sum(lilpreco)/len(lilpreco)

for j in range(5):
    if lilpreco[j-1] > media:
        maismed += 1

pos=lilpreco.index(max(lilpreco))

print("a quantidade de produtos que o valor é abaixo de 10 reais é {}".format(menor10))
print("a média dos valores dos produtos é R${:0.2f}".format(media))
print("a quantidade de produtos que valor acima da média é {}".format(maismed))
print("a maior valor é R${} e o nome do produto é {}".format(lilpreco[pos], lilprod[pos]))
for k in range(5):
    print("Produto = {} Preço = {}".format(lilprod[k-1], lilpreco[k-1]))
