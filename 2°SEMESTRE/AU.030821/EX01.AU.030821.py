idad=int(input("Qual a sua idade ?"))
if(idad>0)and(idad<=12):
    print("sua idade é de {}, por isso voce é uma criança.".format(idad))
elif(idad>=13)and(idad<=17):
    print("sua idade é de {}, por isso voce é um(a) adolescente.".format(idad))
elif(idad>=18)and(idad<59):
    print("sua idade é de {}, por isso voce é um adulto.".format(idad))
else:
    print("sua idade é de {}, por isso voce é um(a) idoso(a).".format(idad))