maior = menor = 0
numeros = []
for v in range(0,5):
    numeros.append(int(input('Digite um número: ')))
for c in range(0, len(numeros)):
    if c == 0:
        maior = numeros[0]
        menor = numeros[0]
    elif maior < numeros[c]:
        maior = numeros[c]
    elif menor > numeros[c]:
        menor = numeros[c]
print(f'O maior numero da lista e {maior} e esta na posição {numeros.index(maior)}')
print(f'O menor numero da lista e {menor} e esta na posição {numeros.index(menor)}')