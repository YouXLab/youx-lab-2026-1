#Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porçao inteira.
#Ex: Digite um numero: 6.127, O numero 6.127 tem a parte inteira 6.

#DESAFIO 016.
from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porçao inteira é {}'.format(num, trunc(num)))