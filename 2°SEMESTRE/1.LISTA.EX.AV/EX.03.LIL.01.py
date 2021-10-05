qtdRegular=0
qtdBom=0
qtdOtimo=0
soma=0
qtdIdade=0
idade=int(input("Qual a sua idade ? "))

while idade>0:
    opiniao=int(input("Digite sua avaliação sobre o filme: 1-REGULAR; 2-BOM; 3-ÓTIMO"))
    if opiniao==1:
        qtdRegular+=1
    elif opiniao==2:
        qtdBom+=1
    elif opiniao==3:
        qtdOtimo+=1
    else:
        print("Avaliação Inválida!, Digite apenas números!")

    qtdIdade+=1
    soma+=idade
    idade=int(input("Insira sua idade: "))

media=soma/qtdIdade



print("Quantidade de avaliações ótimo é  ", qtdOtimo)
print("Quantidade de avaliações regular é ", qtdRegular)
print("Quantidade de avaliações bom é ", qtdBom)
print("Média das idades é ", "%.0f" %media)