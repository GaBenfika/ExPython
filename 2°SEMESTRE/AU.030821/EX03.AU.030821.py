tnota=nota=0
rep=0
for i in range (10):
    nota=float(input("Nota"))
    tnota+=nota
    if nota<6:
        rep+=1
media=tnota/10
print("A média de notas da sala foi de {}".format(media))
print("O total de alunos com nota menor de 6 foi de{}".format(rep))