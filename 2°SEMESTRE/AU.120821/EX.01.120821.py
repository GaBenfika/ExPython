soma=0
for i in range (5):
    num= int(input("digite um número: "))
    cont=0
    for k in range (1,num+1):
        if num%k==0:
            cont+=1
    if cont==2:
        soma= soma+num
        print(num)
print(soma)