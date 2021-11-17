def soma_quadrados(n):
    soma=0
    for i in range(1, n+1):
        soma += i*i
    print("A soma do quadrado do números é:", soma)

n=int(input("Digite um número"))
soma_quadrados(n)
