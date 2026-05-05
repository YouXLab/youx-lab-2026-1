N1 = int(input('Digite um valor: '))
N2 = 0
for c in range(0, N1, 1):
    if N1 % c == 0:
        print('\033[33m',end = ' ')
        N2 += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}'end=' ')
print(f'\n\033[m0 numero {N1} foi divisivel {N2} vezes')
if N2 == 2:
    print('Primo')
else:
    print('Não Primo')