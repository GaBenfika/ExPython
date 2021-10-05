for i in range(3):
    num=int(input("digite um número: "))
    fat=1
    for k in range(2,num+1):
        fat= fat*k
    print("o fatorial de ",num,"é: ",fat)