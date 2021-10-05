medalt = 0
quant1 = 0
totpeso2 = 0
medpeso2 = 0
totpessoas2 = 0
totpessoas3 = 0
totalt3 = 0
medalt3 = 0
totalt = 0
for i in range (2):
    idade=int(input("idade"))
    peso=int(input("peso"))
    alt=int(input("altura em CM"))


    if (idade>50) and (peso>90) :
        quant1 += 1
        totalt += alt


    elif 51>idade>29:
        totpeso2 += peso
        totpessoas2 += 1
        medpeso2 = totpeso2/totpessoas2
        totalt += alt


    elif 26<idade<14:
        totalt3 += alt
        totpessoas3 += 1
        medalt3 = totalt3/totpessoas3
        totalt += alt
    else :
        totalt += alt


medalt = totalt/2
print("A quantidade de pessoas com idade superior a 50 anos e que pesam mais que 90 quilos {}".format(quant1))
print("A média do peso das pessoas com idade entre 30 e 50 anos {}".format(medpeso2))
print("A média da altura de todas pessoas {}".format(medalt))
print("A media de altura da pessoas com idade entre 15 e 25 anos {}".format(medalt3))