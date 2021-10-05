import random
liA=[]
liB=[]
for k in range (5):
    num1=random.randint(1,50)
    num2=random.randint(1,50)
    liA.append(num1)
    liB.append(num2)
print(liA)
print(liB)
for i in liA:
    for j in liB:
        if(i==j):
            print("O número em comum é",i)
            break
        else:
            print("não há numero em comum.")