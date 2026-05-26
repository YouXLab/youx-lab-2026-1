from random import randint

def sorteia(lista):
    print('Sorteando 5 valores para a lista: ', end='')
    for cont in range(0, 5):
        num = randint(1, 10)
        lista.append(num)
        print(f'{num} ', end='', flush=True)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos a soma de {soma}')
numeros = list()
sorteia(numeros)
somaPar(numeros)
