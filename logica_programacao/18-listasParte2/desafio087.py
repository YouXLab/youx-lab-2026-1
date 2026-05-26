linha1 = []
linha2 = []
linha3 = []
matriz = [linha1, linha2, linha3]
terceira_coluna = 0
soma = 0
for lado in range(3):
    for c in range(3):
        valor =int(input(f'Valor para: {lado, c}: '))
        if lado == 0:
            linha1.append(valor)
        elif lado == 1:
            linha2.append(valor)
        elif lado == 2:
            linha3.append(valor)
for lado in linha1:
    print([lado], end=" ")
print()
for lado in linha2:
    print([lado], end=" ")
print()
for lado in linha3:
    print([lado], end=" ")
print()
for linha in range (0, 3):
    for coluna in range (0, 3):
        if matriz[linha][coluna] % 2 == 0:
            soma += matriz[linha][coluna]
print(f"A soma dos valores pares é {soma}")
for linha0 in range (0, 3):
    if matriz[linha0][2]:
        terceira_coluna += matriz[linha0][2]
print(f"A soma dos valores da terceira coluna são: {terceira_coluna}")
listaSegundaLinha = []
for coluna0 in range (0, 3):
    if matriz[1][coluna0]:
        listaSegundaLinha.append(matriz[1][coluna0])
maiorSegundaLinha = max(listaSegundaLinha)
print(f"O maior valor da segunda linha é: {maiorSegundaLinha}")







