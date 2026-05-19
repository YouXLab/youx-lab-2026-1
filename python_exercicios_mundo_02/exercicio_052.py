#Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.


numero = int(input("Digite um número: "))
for c in range(1, numero, +1):
    if numero % c == 0:
        print("/033[34m", end = " ")
    else:
        print("/033[m", end = " ")
    print("{}".format(c), end = " "
