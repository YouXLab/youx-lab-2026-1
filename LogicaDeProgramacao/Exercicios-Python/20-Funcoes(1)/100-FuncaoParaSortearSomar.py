import random
def sorteia(lista):
    print('Sorteando numeros aleatorios:',end=' ')
    for i in range(0,5):
        numero = random.randint(1,10)
        lista.append(numero)
        print(numero,end=' ',flush=True)
    print('Pronto!')
def soma(lista):
    cont = 0
    for valor in lista:
        if valor % 2 == 0:
            cont += valor
    print(f'A soma dos valores pares da lista {lista} é {cont}')
numeros = list()
sorteia(numeros)
soma(numeros)