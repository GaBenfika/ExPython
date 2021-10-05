mais80=0
peso=altura=idade=0
menor18=0
totalt=time1=time2=time3=time4=time5=[]
med1=med2=med3=med4=med5=0
for i in range(5):
    time=int(input("Digite se o time cadastrado será o Time-1; Time-2, Time-3, Time-4 ou Time-5."))
    if time == 1:
        for j in range(11):
            peso=int(input("Qual o peso do {}° jogador?".format(j+1)))
            altura=int(input("Qual a altura do {}° jogador".format(j+1)))
            idade=int(input("QUal a idade do {}° jogador".format(j+1)))

            time1.append(idade)
            totalt.append(altura)

            if idade<18:
                menor18 += 1

            if peso>80:
                mais80 += 1
    med1=sum(time1)/len(time1)

    if time == 2:
        for k in range(11):
            peso = int(input("Qual o peso do {}° jogador?".format(k+1)))
            altura = int(input("Qual a altura do {}° jogador".format(k+1)))
            idade = int(input("QUal a idade do {}° jogador".format(k+1)))

            time2.append(idade)
            totalt.append(altura)

            if idade<18:
                menor18 += 1

            if peso>80:
                mais80 += 1
    med2=sum(time2)/len(time2)

    if time == 3:
        for l in range(11):
            peso = int(input("Qual o peso do {}° jogador?".format(l+1)))
            altura = int(input("Qual a altura do {}° jogador".format(l+1)))
            idade = int(input("QUal a idade do {}° jogador".format(l+1)))

            time3.append(idade)
            totalt.append(altura)

            if idade<18:
                menor18 += 1

            if peso>80:
                mais80 += 1
    med3=sum(time3)/len(time3)

    if time == 4:
        for m in range(11):
            peso = int(input("Qual o peso do {}° jogador?".format(m+1)))
            altura = int(input("Qual a altura do {}° jogador".format(m+1)))
            idade = int(input("QUal a idade do {}° jogador".format(m+1)))

            time4.append(idade)
            totalt.append(altura)

            if idade<18:
                menor18 += 1

            if peso>80:
                mais80 += 1
    med4=sum(time4)/len(time4)

    if time == 5:
        for n in range(11):
            peso = int(input("Qual o peso do {}° jogador?".format(n+1)))
            altura = int(input("Qual a altura do {}° jogador".format(n+1)))
            idade = int(input("QUal a idade do {}° jogador".format(n+1)))

            time5.append(idade)
            totalt.append(altura)

            if idade<18:
                menor18 += 1

            if peso>80:
                mais80 += 1
    med5=sum(time5)/len(time5)

medalt=sum(totalt)/len(totalt)
porc=mais80*100/55
print("Aquantidade de jogadores com idade inferior a 18 anos é {}".format(menor18))
print("A média das idades dos jogadores de cada time é Time 1:{:0.0}anos, Time 2:{:0.0}anos, Time3:{:0.0}anos, Time4:{:0.0}anos, Time5{:0.0}anos.".format(med1,med2,med3,med4
                                                                                                                 ,med5
                                                                                                                 ))
print("A média das alturas de todos os jogadores do campeonato é {:0.2}cm".format(medalt))
print("A percentagem  de  jogadores  com  mais  de  80  quilos  entre  todos  os  jogadores do campeonato é {:0.0f}%".format(porc))
