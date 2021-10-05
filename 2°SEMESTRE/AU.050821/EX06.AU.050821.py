np = 1
pnove: int=0
tidade: int=0
qpes=0
maior=0
while np == 1 :
np = int(input("Deseja utilizar denovo? Sim(1) ; Não(0)"))
    idade = int(input("Qual a idade da pessoa ?"))
    peso = float(input("Qual o peso da pessoa?"))
    if (idade>maior) :
        maior - maior
        maior += idade
    if (peso>90) :
        pnove += 1
    elif (peso<50):
        qpes += 1
        tidade += idade
media = (tidade/qpes)
print("A média da idade das pessoas com peso menor de 50kg é  {}".format(media))
print("O total de pessoas com peso maior de 90kg é {}".format(pnove))
print("A maior idade registrada é {}".format(maior))