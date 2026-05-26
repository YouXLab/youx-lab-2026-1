matriz = [[0,0,0],[0,0,0],[0,0,0]]
for baixo in range(0,3):
    for lado in range(0,3):
        matriz[baixo][lado] = int(input(f'Digite um número para a posição [{baixo}][{lado}]: '))
print('≃'*25)
for baixo in range(0,3):
    for lado in range(0,3):
        print(f'[{matriz[baixo][lado]:^5}]',end='')
    print(' ]≃[')
print('≃'*25)
