primos=0
somamult=0
somapar=0
quantpar=0
for i in range(3):
    num=int(input("Insira o número: "))
    quantdiv=0
    for j in range(1, num+1):
        if num%j==0:
            quantdiv+=1

    if quantdiv==2:
        primos+=1

    if num%3==0:
        somamult+=num

    if num%2==0 and num>20:
        somapar+=num
        quantpar+=1

if quantpar==0:
    medpar=0
else:
    medpar=somapar/quantpar


print("Quantidade de números primos é  ", primos)
print("Soma dos múltiplos de 3 é ", somamult)
print("Média dos números pares maiores que 20 é ", "%.2f" %medpar)