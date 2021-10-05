
poltrona=[1,40]
ocupado=[]
num=1
while num != 0:
    num=int(input("Digite o número da poltrona de 1-40. Para finalizar digite 0."))
    var = num in poltrona
    if var == True:

        ocupado.append(num)
        del poltrona[num]

    if var == False:
        print("Esta poltrona já está ocupada.")


    print(poltrona)
    print(ocupado)