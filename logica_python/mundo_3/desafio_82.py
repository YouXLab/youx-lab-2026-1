# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares
# e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

numeros = []
pares = []
impares = []

continuar = 's'
while continuar == 's ':
    n = int (input('digite um valoe: '))
    numeros.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
        continuar = input('quer continuar? [S/N ').upper()
    print('-=' * 20)
    print(f'lista completa: {numeros}')
    print(f'lista dos pares: {pares}')
    print(f'lista dos impares: {impares}')

