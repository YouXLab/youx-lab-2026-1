from random import randint
from time import sleep
def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        num = randint(1, 10)
        numeros.append(num)
        print(f'{num} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')
def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')
numeros = list()
sorteia()
somaPar(numeros)
