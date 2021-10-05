import random
linum=[]
for i in range(10):
    num=random.randint(1,20)
    linum.append(num)
    linum.sort()
totpar=0
porc=0
media15=0
limaior15=[]
poss=0

for j in range(10):
    if linum[j-1]%2 == 0:
        totpar += 1
        porc=(totpar*100)/len(linum)

    else:
        if linum[j-1]>15:
            limaior15.append(linum[j-1])
media15=sum(limaior15)/len(limaior15)
media=sum(linum)/len(linum)
quant=0
for k in range(10):
    if linum[k-1] >media:
        quant += 1
print(media)
print(linum)
print("o menor número da lista é {} em qual posição está (índice) é o 1° da lista".format(linum[0]))
print("a percentagem de números pares é {:0.0f}%".format(porc))
print("a média dos números ímpares e maiores que 15 é {}".format(media15))
print("a quantidade de números maiores que a média é {}".format(quant))