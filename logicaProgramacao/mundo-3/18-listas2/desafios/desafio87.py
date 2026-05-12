matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = maior = soma_coluna = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digete um numero para [{linha}, {coluna}]: '))

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^3}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
    print()

for linha in range(0, 3):
    soma_coluna += matriz[linha][2]
for coluna in range(0, 3):
    if coluna == 0:
        maior = matriz [1][coluna]
    elif maior < matriz[1][coluna]:
        maior = matriz[1][coluna]
print(f'A soma dos valores pares é {soma_pares}.')
print(f'A soma dos valore na terceira coluna é {soma_coluna}.')
print(f'O maior valor da segunda coluna é {maior}.')