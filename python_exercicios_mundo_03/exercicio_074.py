#Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.


import random
from random import randint
numeros = randint(1,10) , randint (1 , 10) , randint (1 , 10) , randint (1 , 10) , randint(1 , 10)
print(f"Os numeros sorteados foram {numeros}")
for n in numeros:
    print(f"[{n}]", end= ' ' )
print(f"\n O maior numero foi {max(numeros)}")
print(f"O menor numero foi {(min(numeros))}")
