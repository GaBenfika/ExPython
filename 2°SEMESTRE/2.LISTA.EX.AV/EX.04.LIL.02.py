import random
liA = []
liB = []
liC = []
for i in range(10) :
    n1 = random.randint(1, 50)
    n2 = random.randint(1, 50)

    liA.append(n1)
    liB.append(n2)

for j in liA:
    for k in liB:
        if(j==k):
            liC.append(j)

print("Lista A",liA)
print("Lista B",liB)
print("Lista C",liC)