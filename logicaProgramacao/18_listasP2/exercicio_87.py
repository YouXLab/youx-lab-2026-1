#Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.


matriz= [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
valorColuna = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        numero = int(input(f'digita o valor de {linha} e {coluna} :'))
        matriz[linha][coluna] = numero
        if numero % 2 == 0:
            pares += numero
        if coluna == 2:
            valorColuna += numero
for linha in range(0, 3):
    print(f'[{matriz[linha] [coluna]}', end=' ')
    print()
print(pares)
print(valorColuna)
print(max(matriz[1]))
print(f'o soma de todos os valores de pares é {pares}')
print(f'a soma dos valores da terceira coluna é {valorColuna}')
print(f'o maior valor da segunda linha é {numero}')