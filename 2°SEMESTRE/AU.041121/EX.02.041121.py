#Faça um programa que peça como
# entrada 2 palavras, em seguida
# junte essas duas palavras em uma
# string e depois faça uma busca
# de uma palavra ou sílaba nessa
# string usando find().

n1=str(input("Primeiro nome"))
n2=str(input("Segundo nome"))
n3=n1+n2

print(n3)
fn=str(input("Palavra para pesquisar."))
n3.find(fn)
