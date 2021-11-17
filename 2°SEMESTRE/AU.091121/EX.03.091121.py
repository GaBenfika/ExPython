def soma(A, B):
    total=0
    for i in range(A, B+1):
        total += i
    print("A soma dos número {} a {} são {}".format(A, B, total))

soma(3, 10)
