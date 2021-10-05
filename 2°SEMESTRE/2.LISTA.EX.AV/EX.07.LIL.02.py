import random
lilA=[]
lilB=[]
lilC=[]
for i in range(5):
    lilA.append(random.randint(1, 50))
    lilB.append(random.randint(1, 50))
    lilC.append(lilA[i-1]*lilB[i-1])


print("Lista A = ",lilA)
print("Lista B = ",lilB)
print("Lista C = ",lilC)
