matriz = [[0,0,0],[0,0,0],[0,0,0]]
pares = []
num_par = []
soma_pares = 0
soma_linha = 0
linha = []
for baixo in range(0,3):
    for lado in range(0,3):
        matriz[baixo][lado] = int(input(f'Digite um número para a posição [{baixo}][{lado}]: '))
print('≃'*24)
for baixo in range(0,3):
    for lado in range(0,3):
         print(f'[{matriz[baixo][lado]:^5}]',end= '')
         if matriz[baixo][lado] % 2 == 0:
            num_par = matriz[baixo][lado]
            pares.append(num_par)
         if matriz[1] < matriz[1]:
            soma_linha = matriz[1]
            linha.append(soma_linha)
    print()
for pares in pares:
    soma_pares += pares
print(f'A soma dos números pares é : {soma_pares}')
print(soma_linha)
