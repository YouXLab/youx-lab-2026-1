import random

lista = []
cont = 0
cont2 = 0
cont3 = 0
numSort = int(input('Numero de sorteios: '))
print(f'Sorteando {numSort} Numeros:')
while cont2 != numSort:
    num = random.randint(1,60)
    if num not in lista:
        lista.append(num)
        cont += 1
    if cont >= 6:
        cont += -6
        cont2 += 1
        cont3 += 1
        print(f'Jogo [{cont3}]: {lista}')
        lista.clear()











