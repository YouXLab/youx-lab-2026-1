import random
import time

numeros = []
def sorteia(a, b):
    print('Sorteando 5 valores da lista', end=' ')
    for n in range(0, 5):
        numero = random.randint(a, b)
        numeros.append(numero)
        print(numero, end=' ')
        time.sleep(0.25)
    print('PRONTO!', end='')
    print('')

def somaPar(lista):
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {numeros}, temos {soma}')

sorteia(1, 20)
somaPar(numeros)