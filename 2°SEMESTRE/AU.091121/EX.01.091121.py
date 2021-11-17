def primo(num):
    div=0
    for i in range(1,num+1):
        if num %i== 0:
            div += 1
    if div==2:
        print("Numero é primo")
    else:
        print("Numero não é primo")

num=int(input("Digite um número"))
primo(num)
