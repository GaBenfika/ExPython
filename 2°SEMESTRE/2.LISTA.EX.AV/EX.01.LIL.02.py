liidade=[]
totpessoas=0
maiormedia=0
for i in range(10):
    idade=int(input("Qual a sua idade?"))
    liidade.append(idade)
    if 30>=idade>=20:
        totpessoas += 1
medidade=sum(liidade)/len(liidade)

for i in range(10):
    if liidade[i-1]>medidade:
      maiormedia += 1

print("a menor idade é {}".format(min(liidade)))
print("a média das idades é {:0.0f}".format(medidade))
print("a quantidade de pessoas que tem idade entre 20 e 30 anos (inclusive) é {}".format(totpessoas))
print("a quantidade de pessoas com idade maior que a média é {}".format(maiormedia))
