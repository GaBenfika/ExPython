import random
sompar = 0
impar = 0
totmaior=quantmaior=0
media=0
mini=999
for i in range(10):
    num=random.randint(1,100)
    print(num)
    if mini > num:
        mini = num

    if num % 2 ==0 :
        if(num>10):
            sompar += num
    else:
        impar += 1

    if num>20 :
        totmaior += 1
        quantmaior += num

media = quantmaior / totmaior

print("o menor número é {}.".format(mini))
print("a soma dos números pares e maiores que 10 é {}.".format(sompar))
print("a quantidade de números ímpares é {}.".format(impar))
print("a média dos números maiores que 20 é {:0.2f}.".format(media))