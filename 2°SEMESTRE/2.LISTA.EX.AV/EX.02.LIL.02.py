lilcor=[]
for i in range(4):
    cor=str(input("Digite uma cor."))
    lilcor.append(cor)

pesq=str(input("Digite a cor a ser pesquisada."))
for j in range (4):
    if pesq == lilcor[j-1]:
        print(lilcor)
        print("A cor {} está localizada no {}° elemento da lista.".format(pesq,j))
    else:
        print("Essa cor não está na lista.")
