import random
listaA=[]
listaB=[]
listaC=[]

for i in range(5):
    listaA.append(random.randint(1, 50))
    listaB.append(random.randint(1, 50))
    listaC.append(listaA[i-1]*listaB[i-1])

print("Lista A = ", listaA)
print("Lista B = ", listaB)
print("Lista C = ", listaC)