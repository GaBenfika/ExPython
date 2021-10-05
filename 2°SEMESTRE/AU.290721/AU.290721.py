from random import randint
qnt=par=0
for i in range (10):
    nm= randint(1,50)
    if nm < 10 :
        qnt += 1
    if (nm % 2)==0:
        par += nm
print("A soma dos numeros pares é {}, e a quantidade de números menores a 10 é {}".format(par,qnt))