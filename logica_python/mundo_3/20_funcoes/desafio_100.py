
from random import randint

def sorteia(lista):
    for contagem in range(0, 5):
        lista.append(randint(1, 10))
numeros = []
sorteia(numeros)
print(numeros)
