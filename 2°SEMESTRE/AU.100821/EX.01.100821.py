idma=idme=media=maialt=soma=0
for i in range(5):
    idade=int(input("digite sua idade: "))
    altura=float(input("digite sua altura: "))

    if i==0:
        idma=idade
        idme=idade
        meialt=altura

    if idade>idma:
        idma=idade
    if idade<idme:
        idme=idade
    if altura> maialt:
        maialt=altura

    soma=soma+altura
media=soma/5
print("A maior idade é: ",idma)
print("A menor idade é: ",idme)
print("A média das alturas é: ",media)
print("A maior altura é: ",maialt)