#Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.


matriz = [[0,0,0],[0,0,0],[0,0,0]]
somaPares = maior = somaColuna = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"digite um valor para [{l},{c}]: "))
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]",end = " ")
        if matriz[l][c] % 2 == 0:
            somaPares += matriz[l][c]
    print()
print(f"a soma dos numeros pares é {somaPares}")
for l in range(0,3):
    somaColuna += matriz[l][2]
print(f"a soma dos numeros da terceira coluna é {somaColuna}")
for c in range(0,3):
    if c == 0:
        maior = matriz[l][c]
    elif matriz[l][c] > maior:
        maior = matriz[l][c]
print(f"o maior valor da segunda linha é {maior}")
