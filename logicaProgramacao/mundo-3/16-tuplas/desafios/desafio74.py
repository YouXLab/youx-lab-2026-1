import random
numeros = (random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9))
maior = menor = 0
contador = 0
for c in range(0, len(numeros)):
    if maior == 0:
        maior = numeros[0]
    elif maior < numeros[1]:
        maior = numeros[1]
    elif maior < numeros[2]:
        maior = numeros[2]
    elif maior < numeros[3]:
        maior = numeros[3]
    elif maior < numeros[4]:
        maior = numeros[4]
    elif menor == 0:
        menor = numeros[0]
    elif menor > numeros[0]:
        menor = numeros[0]
    elif menor > numeros[1]:
        menor = numeros[1]
    elif menor > numeros[2]:
        menor = numeros[2]
    elif menor > numeros[3]:
        menor = numeros[3]
    elif menor > numeros[4]:
        menor = numeros[4]
print(f'Os números sorteaos foram: {numeros}')
print(f'O maior numero e {maior}')
print(f'O menor numero e {menor}')