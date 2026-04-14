#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc
num = float(input("Digite o valor: "))
print(f"O valor digitado foi {num} e a sua porçao inteira é {trunc(num)}")
