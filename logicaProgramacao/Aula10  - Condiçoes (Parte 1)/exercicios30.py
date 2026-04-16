#crie e um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n1 = int(input("Digite um numero: "))
resultado = n1 % 2
if resultado==0:
    print("É par")
else:
    print("É impar")