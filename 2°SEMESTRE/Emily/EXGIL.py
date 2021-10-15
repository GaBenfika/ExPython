import random
#Matriz A e B 2x2 que gera uma 3 Mat C que é a soma das duas
matA=[]
matB=[]
matC=[]
for i in range(2):
    lia=[]
    lib=[]
    lic=[]
    for j in range(2):
        lia.append(random.randint(1, 50))
        lib.append(random.randint(1, 50))
        lic.append(lia[j]+lib[j])
    matA.append(lia)
    matB.append(lib)
    matC.append(lic)
print("Matriz C:", matA)
print("Matriz B:", matB)
print("Matriz C:", matC)
