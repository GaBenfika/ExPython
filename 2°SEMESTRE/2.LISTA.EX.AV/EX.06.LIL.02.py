import random
liA=[]
liB=[]
liC=[]
for k in range (5):
    num1=random.randint(1,50)
    num2=random.randint(1,50)
    liA.append(num1)
    liB.append(num2)
    liC.append(num1)
    liC.append(num2)

for i in liA:
    for j in liB:
        if(i==j):
            liC.remove(i)
            liC.remove(j)

print(liA)
print(liB)
print(liC)