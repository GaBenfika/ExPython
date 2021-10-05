import random
par=0
somaimpar=0
lista=[]
quant=0
medlista=0
for i in range(10):
    num=random.randint(1,50)
    print(num)
    lista.append(num)
    if num %2 ==0:
        par += 1
    else:
        somaimpar= somaimpar + num

    if 10<=num<=20:
        quant += 1

print(lista)
medlista=sum(lista)/len(lista)
print("A quantidade de números pares é {}".format(par))
print("A soma dos números ímpares é {}".format(somaimpar))
print("A quantidade de números entre 10 e 20 (inclusive) é {}".format(quant))
print("A média dos números da lista é {:0.2f}".format(medlista))