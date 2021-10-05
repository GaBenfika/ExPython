import random
lilA=[]
lilB=[]
lilC=[]
for i in range(5):
    lilA.append(random.randint(1, 20))
    lilB.append(random.randint(1, 20))
    lilC.append(lilA[i-1])
    lilC.append(lilB[i-1])
qtdPerfeito=0
for j in range(len(lilC)):
    soma=0
    for k in range(1, lilC[j]):
        if lilC[j] %k == 0:
            soma+=k
    if soma==lilC[j]:
        qtdPerfeito+=1
print("Quantidade de números perfeitos: ", qtdPerfeito)
print(lilA)
print(lilB)
print(lilC)