from random import randint
from time import sleep

numeros = []


def sorteia():
    print("Sorteando 5 valores da lista: ", end="")

    for c in range(0, 5):
        n = randint(1, 10)
        numeros.append(n)
        print(n, end=" ", flush=True)
        sleep(0.5)

    print("PRONTO!")


def somaPar():
    soma = 0

    for valor in numeros:
        if valor % 2 == 0:
            soma += valor

    print(f"Somando os valores pares de {numeros}, temos {soma}")


# Programa principal
sorteia()
somaPar()