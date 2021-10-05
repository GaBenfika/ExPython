import math
import random
listanum=[]
listafatorial=[]
for i in range(2):
    num=random.randint(1,20)
    fat=math.factorial(num)

    listanum.append(num)
    listafatorial.append(fat)

print(listanum)
print(listafatorial)
for i in range (2):
    print("O número {} possui com fatoria o valor de {}".format(listanum[i-1],listafatorial[i-1]))
