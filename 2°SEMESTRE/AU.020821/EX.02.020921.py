import random
liA=[]
liB=[]
liC=[]
for i in range(10):
    num=random.randint(2,30)
    liA.append(num)

for j in range (len(liA)):
    mult=min(liA)*liA[j-1]
    liB.append(mult)

liC.extend(liA)
liC.extend(liB)

print("Lista A :",liA)
print("Lista B :",liB)
print("Lista C :",liC)