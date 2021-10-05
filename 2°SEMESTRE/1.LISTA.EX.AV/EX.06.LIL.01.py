liidade=[]
idade=1
quantpessoas=0
medidade=0
while idade>0:
    idade=int(input("Qual sua idade ?"))
    if idade >= 1:
        liidade.append(idade)

        if idade>20 and idade<40 :
            quantpessoas += 1


medidade=sum(liidade)/len(liidade)
print(liidade)
print("A quantidade de pessoas que tem idade entre 20 e 40 anos é {}".format(quantpessoas))
print("A maior idade {}".format(max(liidade)))
print("A menor idade {}".format(min(liidade)))
print("A média das idades {:0.0f}".format(medidade))
