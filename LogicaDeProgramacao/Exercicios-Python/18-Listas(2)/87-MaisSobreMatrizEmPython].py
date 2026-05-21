N1 = [[0,0,0],[0,0,0],[0,0,0]]
somaPar = 0
somaTerceiraColuna = 0
maiorSegundaColuna = 0
cont = 0
for l in range(3):
    for c in range(3):
        N1[l][c] = int(input(f'Digite um valor para {l} {c}:'))
print('-='*30)
for l in range(3):
    for c in range(3):
        print(f'[{N1[l][c]:3}]',end='')
        cont += 1
        if cont == 4:
            maiorSegundaColuna = N1[l][c]
        if cont >= 4 and cont <= 6:
            if N1[l][c] >= maiorSegundaColuna:
                maiorSegundaColuna = N1[l][c]
        if cont >=7 and cont <= 9:
            somaTerceiraColuna += N1[l][c]
        if N1[l][c] % 2 == 0:
            somaPar += N1[l][c]
    print()
print('-='*30)
print(f'A soma dos valores pares é: {somaPar}')
print(f'O maior valor da segunda coluna é: {maiorSegundaColuna}')
print(f'A soma da terceira coluna é: {somaTerceiraColuna}')



































